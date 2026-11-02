"""Offline invariant tests; synthetic examples contain no customer data."""

import importlib.util
from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
