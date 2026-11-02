"""Offline invariant tests; synthetic examples contain no customer data."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("trade_tools", Path(__file__).parents[1] / "scripts/trade_tools.py")
trade = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = trade
SPEC.loader.exec_module(trade)


class ScoringTests(unittest.TestCase):
    def test_no_evidence_is_ungraded_not_low_priority(self):
        result = trade.score_customer({})
        self.assertEqual(result["tier_status"], "ungraded")
        self.assertEqual(result["possible_score_range"], [0, 120])
        self.assertIsNone(result["tier"])

    def test_missing_social_and_trade_remain_unknown(self):
        dimensions = {name: {"score": maximum, "evidence": "Synthetic source"}
                      for name, maximum in trade.DIMENSIONS.items()
                      if name not in ("social", "purchasing")}
        result = trade.score_customer({"dimensions": dimensions, "risk_flags": ["Identity mismatch"]})
        self.assertEqual(result["known_score"], 100)
        self.assertEqual(result["possible_score_range"], [100, 120])
        self.assertEqual(result["unknown_dimensions"], ["social", "purchasing"])
        self.assertEqual(result["tier"], "T1")
        self.assertEqual(result["risk_flags"], ["Identity mismatch"])

    def test_cross_tier_interval_is_not_definite(self):
        dimensions = {name: {"score": maximum, "evidence": "Synthetic source"}
                      for name, maximum in trade.DIMENSIONS.items()
                      if name not in ("company", "social", "purchasing")}
        result = trade.score_customer({"dimensions": dimensions})
        self.assertEqual(result["possible_score_range"], [80, 120])
        self.assertEqual(result["tier_status"], "provisional")

    def test_full_known_boundaries(self):
        for value, tier in ((0, "T4"), (30, "T3"), (60, "T2"), (90, "T1"), (120, "T1")):
            remaining, dimensions = value, {}
            for name, maximum in trade.DIMENSIONS.items():
                score = min(remaining, maximum)
                remaining -= score
                dimensions[name] = {"score": score, "evidence": "Synthetic source"}
            self.assertEqual(trade.score_customer({"dimensions": dimensions})["tier"], tier)

    def test_invalid_score_or_missing_evidence_rejected(self):
        for item in ({"score": 26, "evidence": "x"}, {"score": True, "evidence": "x"},
                     {"score": 2}, {"score": 2.5, "evidence": "x"}):
            with self.assertRaises(ValueError):
                trade.score_customer({"dimensions": {"intent": item}})

    def test_misspelled_dimension_is_not_silently_ignored(self):
        with self.assertRaises(ValueError):
            trade.score_customer({"dimensions": {"intnet": {"score": 20}}})


class FAQTests(unittest.TestCase):
    def test_parser_keeps_topic_heading_out_of_answer(self):
        text = "### MR-001 | Question one?\n- 核查：test\n- 行动：act\n## Topic\n### MR-002 | Question two?\n- 核查：check\n- 行动：next"
        entries = trade.parse_entries(text, "fixture.md")
        self.assertEqual(len(entries), 2)
        self.assertNotIn("Topic", entries[0].body)
        self.assertEqual(entries[1].id, "MR-002")

    def test_normalization_detects_cosmetic_duplicate(self):
        self.assertEqual(trade.normalize("客户：怎么报价？"), trade.normalize("客户怎么报价!"))

    def test_search_selects_relevant_question(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / trade.MODULES["MR"]
            target.parent.mkdir(parents=True)
            target.write_text("### MR-001 | 海关单位怎么换算？\n- 核查：区分重量和面积。\n- 行动：取得密度厚度数据后核算。\n### MR-002 | 如何选择展会？\n- 核查：访客与渠道。\n- 行动：比较买家覆盖。", encoding="utf-8")
            result = trade.search(root, "海关 单位", ["MR"], 1)
            self.assertEqual(result[0]["id"], "MR-001")

    def test_empty_query_rejected(self):
        with self.assertRaises(ValueError):
            trade.search(trade.ROOT, "?!", ["MR"], 5)

    def test_english_product_query_finds_chinese_question(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / trade.MODULES["PE"]
            target.parent.mkdir(parents=True)
            target.write_text("### PE-001 | 如何核实橡木核心床？\n- 核查：确认木材结构。\n- 行动：索取当前材料单。\n### PE-002 | 包装尺寸如何确定？\n- 核查：测量外包装。\n- 行动：准备装柜资料。", encoding="utf-8")
            self.assertEqual(trade.search(root, "oak reformers", ["PE"], 1)[0]["id"], "PE-001")

    def test_missing_modules_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            result = trade.validate(Path(directory))
            self.assertEqual(len(result["errors"]), len(trade.MODULES))

    def test_broken_local_link_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SKILL.md").write_text("[missing](missing.md)", encoding="utf-8")
            result = trade.validate(root)
            self.assertTrue(any("Broken local link" in item for item in result["errors"]))

    def test_duplicate_questions_and_missing_fields_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / trade.MODULES["MR"]
            target.parent.mkdir(parents=True)
            target.write_text("### MR-001 | 同一个问题？\n- 核查：检查字段。\n### MR-001 | 同一个问题？\n- 核查：第二个字段。", encoding="utf-8")
            result = trade.validate(root, minimum=1)
            self.assertTrue(any("Duplicate question" in item for item in result["errors"]))
            self.assertTrue(any("IDs must be consecutive" in item for item in result["errors"]))
            self.assertTrue(any("missing non-empty 行动" in item for item in result["errors"]))


class QuoteGateTests(unittest.TestCase):
    def ready_input(self):
        def evidence(value, party="buyer"):
            return {"status": "confirmed", "value": value, "source": "Synthetic approval/date",
                    "confirmed_by": party}
        return {"reply_stage": "subsequent",
                "needs": {key: evidence("Synthetic confirmed " + key) for key in trade.NEED_FIELDS},
                "pain_or_goal": {**evidence("New studio fit-out; no existing defect"), "kind": "goal"},
                "product_selection": evidence("Suitable current model/structure", "seller"),
                "seller_offer": {"authorized": True, "scope_matches": True, "source": "Synthetic Eric approval"}}

    def test_first_reply_blocked_even_when_everything_else_ready(self):
        payload = self.ready_input()
        payload["reply_stage"] = "first"
        result = trade.quote_gate(payload)
        self.assertFalse(result["quote_allowed"])
        self.assertEqual(result["status"], "hold_first_reply")
        self.assertEqual(result["missing_or_blocked"], ["first_reply_must_be_non_price"])

    def test_unknown_stage_does_not_default_to_subsequent(self):
        payload = self.ready_input()
        del payload["reply_stage"]
        self.assertIn("reply_stage_not_confirmed", trade.quote_gate(payload)["missing_or_blocked"])

    def test_empty_input_is_held(self):
        result = trade.quote_gate({})
        self.assertEqual(result["status"], "hold_discovery")
        self.assertFalse(result["quote_allowed"])

    def test_inferred_pain_cannot_unlock_price(self):
        payload = self.ready_input()
        payload["pain_or_goal"].update(status="inferred", kind="pain")
        self.assertIn("buyer_confirmed_pain_or_goal", trade.quote_gate(payload)["missing_or_blocked"])

    def test_confirmed_goal_without_old_problem_is_allowed(self):
        result = trade.quote_gate(self.ready_input())
        self.assertTrue(result["quote_allowed"])
        self.assertEqual(result["status"], "ready_to_quote")

    def test_confirmed_pain_with_evidence_is_allowed(self):
        payload = self.ready_input()
        payload["pain_or_goal"].update(kind="pain", value="Documented current tile movement and downtime")
        self.assertTrue(trade.quote_gate(payload)["quote_allowed"])

    def test_research_cannot_pretend_to_be_buyer_confirmation(self):
        payload = self.ready_input()
        payload["needs"]["decision_basis"]["confirmed_by"] = "research"
        self.assertIn("needs.decision_basis", trade.quote_gate(payload)["missing_or_blocked"])

    def test_blank_evidence_is_not_confirmation(self):
        payload = self.ready_input()
        payload["needs"]["application_and_use"]["source"] = " "
        payload["product_selection"]["value"] = ""
        result = trade.quote_gate(payload)
        self.assertIn("needs.application_and_use", result["missing_or_blocked"])
        self.assertIn("seller_confirmed_product_selection", result["missing_or_blocked"])

    def test_unapproved_or_mismatched_offer_is_blocked(self):
        for key in ("authorized", "scope_matches", "source"):
            payload = self.ready_input()
            payload["seller_offer"][key] = "" if key == "source" else False
            self.assertIn("authorized_matching_seller_offer", trade.quote_gate(payload)["missing_or_blocked"])

    def test_invalid_types_and_typos_rejected(self):
        for payload in ([], {"reply_stage": False}, {"needs": []}, {"needs": {"aplication": {}}},
                        {"seller_offer": {"authorized": "true"}}, {"product_selection": True},
                        {"pain_or_goal": {"kind": "suspected"}}, {"first_response": False},
                        {"needs": {"project_scope": {"status": "confirmed", "value": 123}}}):
            with self.assertRaises(ValueError):
                trade.quote_gate(payload)


class SellerFactsTests(unittest.TestCase):
    def test_flooring_sizes_and_literal_hs_preserved(self):
        facts = json.loads((trade.ROOT / "products/gym-rubber-flooring/seller_facts.json").read_text(encoding="utf-8"))
        self.assertEqual(facts["tile_sizes_cm"], [[50, 50], [100, 100]])
        self.assertEqual(facts["tile_sizes_mm"], [[500, 500], [1000, 1000]])
        self.assertEqual(facts["hs_code_as_provided"], "400821000")
        self.assertEqual(facts["evidence_status"], "user_provided_not_independently_verified")


class QuoteGateCLITests(unittest.TestCase):
    def run_cli(self, payload):
        return subprocess.run([sys.executable, str(trade.ROOT / "scripts/trade_tools.py"), "quote-gate", "-"],
                              input=payload, text=True, capture_output=True, check=False)

    def test_stdin_first_reply_returns_non_price_hold(self):
        result = self.run_cli('{"reply_stage": "first"}')
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        self.assertEqual(data["status"], "hold_first_reply")
        self.assertFalse(data["quote_allowed"])

    def test_stdin_ready_reply_passes_without_echoing_evidence(self):
        payload = QuoteGateTests().ready_input()
        result = self.run_cli(json.dumps(payload))
        self.assertEqual(result.returncode, 0)
        self.assertTrue(json.loads(result.stdout)["quote_allowed"])
        self.assertNotIn("New studio fit-out", result.stdout)

    def test_invalid_json_reports_failure(self):
        result = self.run_cli("{invalid")
        self.assertEqual(result.returncode, 2)
        self.assertIn("error", json.loads(result.stderr))


if __name__ == "__main__":
    unittest.main()
