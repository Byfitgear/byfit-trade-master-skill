#!/usr/bin/env python3
"""Offline FAQ validation/search, evidence-aware scoring and quote gate. Standard library only."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
MODULES = {
    "MR": "faq/faq_market_research.md",
    "BG": "faq/faq_background_investigation.md",
    "SM": "faq/faq_social_media_investigation.md",
    "PB": "faq/faq_purchasing_behavior.md",
    "CN": "faq/faq_core_needs.md",
    "PP": "faq/faq_pain_points.md",
    "CG": "faq/faq_client_grading.md",
    "RD": "faq/faq_reply_drafting.md",
    "RF": "products/gym-rubber-flooring/faq_product_specific.md",
    "GE": "products/gym-equipment/faq_product_specific.md",
    "PE": "products/pilates-equipment/faq_product_specific.md",
}
DIMENSIONS = {
    "intent": 25, "company": 20, "potential": 20, "fit": 20,
    "communication": 15, "social": 10, "purchasing": 10,
}
TIERS = (("T4", 0, 29), ("T3", 30, 59), ("T2", 60, 89), ("T1", 90, 120))
NEED_FIELDS = ("application_and_use", "performance_priorities", "project_scope", "decision_basis")
HEADER = re.compile(r"^### ([A-Z]{2})-(\d{3}) \| (.+)$", re.M)
QUERY_ALIASES = {
    r"\breformers?\b": "普拉提 核心床 滑车",
    r"\boak\b": "橡木", r"\bmaple\b": "枫木", r"\brubberwood\b": "橡胶木",
    r"\bsprings?\b": "弹簧 阻力", r"\bdensity\b": "密度 重量",
    r"\bthickness\b": "厚度 公差", r"\brolls?\b": "卷材",
    r"\btiles?\b": "地砖 拼接", r"\bvinyl\b": "乙烯基 PVC",
    r"\bwarrant(?:y|ies)\b": "保修 质保", r"\bcertificat\w*\b|\bce\b": "认证 合规",
    r"\bdiscounts?\b": "折扣 优惠", r"\bpric(?:e|ing)\b": "价格 报价",
    r"\blead time\b": "交期 排产", r"\bcourier\b": "快递 样品",
    r"\bpayment\b|\bbank\b": "付款 银行 受益人",
    r"\bcustoms\b|\bimports?\b": "海关 进口 提单",
    r"\bsocial\b": "社媒 账号", r"\bprocurement\b": "采购 决策",
    r"\bnoise\b|\bacoustic\w*\b": "噪音 声学",
    r"\btreadmills?\b": "跑步机 电机", r"\bcables?\b": "钢索 滑轮",
    r"\bpacking\b|\bpackaging\b": "包装 装柜", r"\bsamples?\b": "样品 验收",
}


@dataclass(frozen=True)
class Entry:
    module: str
    number: int
    question: str
    body: str
    path: str

    @property
    def id(self) -> str:
        return f"{self.module}-{self.number:03d}"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return "".join(char for char in value if char.isalnum())


def grams(value: str, n: int = 3) -> set[str]:
    value = normalize(value)
    if len(value) < n:
        return {value} if value else set()
    return {value[i:i + n] for i in range(len(value) - n + 1)}


def similarity(left: str, right: str) -> float:
    a, b = grams(left), grams(right)
    return len(a & b) / len(a | b) if a | b else 1.0


def parse_entries(text: str, path: str) -> list[Entry]:
    matches = list(HEADER.finditer(text))
    entries = []
    for i, match in enumerate(matches):
        stop = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        # A thematic heading belongs to navigation, not to the preceding answer.
        body = re.split(r"^## ", text[match.end():stop], maxsplit=1, flags=re.M)[0].strip()
        entries.append(Entry(match[1], int(match[2]), match[3].strip(), body, path))
    return entries


def read_modules(root: Path, modules: list[str] | None = None) -> dict[str, list[Entry]]:
    return {
        module: parse_entries((root / MODULES[module]).read_text(encoding="utf-8"), MODULES[module])
        for module in (modules or list(MODULES))
    }


def validate(root: Path, minimum: int = 100, near_threshold: float = 0.78) -> dict:
    errors, warnings, counts = [], [], {}
    questions: dict[str, str] = {}
    bodies: dict[str, str] = {}
    for module, path in MODULES.items():
        target = root / path
        if not target.is_file():
            errors.append(f"Missing module: {path}")
            continue
        text = target.read_text(encoding="utf-8")
        entries = parse_entries(text, path)
        counts[module] = len(entries)
        if len(entries) < minimum:
            errors.append(f"{module}: {len(entries)} entries, minimum {minimum}")
        if any(entry.module != module for entry in entries):
            errors.append(f"{module}: unexpected ID prefix")
        if [entry.number for entry in entries] != list(range(1, len(entries) + 1)):
            errors.append(f"{module}: IDs must be consecutive, unique and start at 001")
        topics = [title for title in re.findall(r"^## (.+)$", text, re.M)
                  if not re.match(r"^(目录|contents|使用说明|阅读说明)(?:\s|[：:]|$)", title, re.I)]
        if len(topics) < 10:
            errors.append(f"{module}: fewer than 10 topic sections")
        for entry in entries:
            for field in ("核查", "行动"):
                if not re.search(rf"^- {field}：\S.+", entry.body, re.M):
                    errors.append(f"{entry.id}: missing non-empty {field}")
            if len(normalize(entry.body)) < 40:
                errors.append(f"{entry.id}: answer too short to contain useful checks/actions")
            for key, seen, label in ((normalize(entry.question), questions, "question"),
                                     (normalize(entry.body), bodies, "answer")):
                if key in seen:
                    errors.append(f"Duplicate {label}: {seen[key]} / {entry.id}")
                else:
                    seen[key] = entry.id
        for i, left in enumerate(entries):
            for right in entries[i + 1:]:
                overlap = similarity(left.question, right.question)
                if near_threshold <= overlap < 1:
                    warnings.append({"left": left.id, "right": right.id,
                                     "similarity": round(overlap, 3),
                                     "questions": [left.question, right.question]})
    for document in root.rglob("*.md"):
        if ".git" in document.parts:
            continue
        content = document.read_text(encoding="utf-8")
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            destination = link.split("#", 1)[0]
            if not destination or re.match(r"^[a-z][a-z0-9+.-]*:", destination, re.I):
                continue
            if not (document.parent / destination).is_file():
                errors.append(f"Broken local link: {document.relative_to(root)} -> {destination}")
    return {"counts": counts, "total": sum(counts.values()), "errors": errors,
            "near_duplicate_candidates": warnings,
            "semantic_review_required": True,
            "note": "Counts/exact uniqueness are machine checks; semantic distinctness needs editorial review."}


def search(root: Path, query: str, modules: list[str] | None, limit: int) -> list[dict]:
    query_normalized = normalize(query)
    if not query_normalized:
        raise ValueError("Query must contain letters, numbers, or Chinese characters")
    # Offline lexical bridge for common English buyer terms; not semantic proof.
    expanded = query + " " + " ".join(value for pattern, value in QUERY_ALIASES.items()
                                      if re.search(pattern, query, re.I))
    tokens = re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]{2,}", expanded.casefold())
    pairs = grams(expanded, 2)
    ranked = []
    for entries in read_modules(root, modules).values():
        for entry in entries:
            title, body = normalize(entry.question), normalize(entry.body)
            title_grams, body_grams = grams(title, 2), grams(body, 2)
            score = (20 * (query_normalized in title) + 6 * (query_normalized in body)
                     + sum(5 for token in tokens if normalize(token) in title)
                     + 3 * len(pairs & title_grams) + len(pairs & body_grams))
            if score:
                ranked.append((score, entry))
    ranked.sort(key=lambda item: (-item[0], item[1].id))
    return [{"id": entry.id, "question": entry.question, "answer": entry.body,
             "path": entry.path, "relevance": score}
            for score, entry in ranked[:limit]]


def score_customer(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("Input must be a JSON object")
    raw = payload.get("dimensions", {})
    if not isinstance(raw, dict):
        raise ValueError("dimensions must be an object")
    unexpected = set(raw) - set(DIMENSIONS)
    if unexpected:
        raise ValueError(f"Unknown dimensions: {', '.join(sorted(unexpected))}")
    known_score, known_max, evidence = 0, 0, []
    unknown = []
    for name, maximum in DIMENSIONS.items():
        item = raw.get(name, {"score": None})
        if not isinstance(item, dict):
            raise ValueError(f"{name}: expected an object containing score/evidence")
        value = item.get("score")
        if value is None:
            unknown.append(name)
            continue
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= maximum:
            raise ValueError(f"{name}: score must be an integer from 0 to {maximum}, or null")
        explanation = item.get("evidence", "")
        if not isinstance(explanation, str) or not explanation.strip():
            raise ValueError(f"{name}: a known score requires non-empty evidence")
        known_score += value
        known_max += maximum
        evidence.append({"dimension": name, "score": value, "max": maximum,
                         "evidence": explanation.strip()})
    flags = payload.get("risk_flags", [])
    if not isinstance(flags, list) or any(not isinstance(flag, str) for flag in flags):
        raise ValueError("risk_flags must be a list of strings")
    lower, upper = known_score, known_score + 120 - known_max
    candidates = [tier for tier, lo, hi in TIERS if lower <= hi and upper >= lo]
    eligible = bool(known_max >= 90 and len(candidates) == 1)
    return {"known_score": known_score, "known_max": known_max, "total_max": 120,
            "possible_score_range": [lower, upper],
            "evidence_coverage_pct": round(known_max / 120 * 100, 2),
            "tier_status": "ungraded" if known_max == 0 else "determinate" if eligible else "provisional",
            "tier": candidates[0] if eligible else None,
            "tier_candidates": candidates, "unknown_dimensions": unknown,
            "evidence": evidence, "risk_flags": flags,
            "risk_note": "Sales priority is not credit approval or a payment-safety guarantee."}


def quote_gate(payload: dict) -> dict:
    """Conservative rule check only; it cannot authenticate supplied evidence."""
    if not isinstance(payload, dict):
        raise ValueError("Input must be a JSON object")
    unexpected = set(payload) - {"reply_stage", "needs", "pain_or_goal", "product_selection", "seller_offer"}
    if unexpected:
        raise ValueError(f"Unknown gate fields: {', '.join(sorted(unexpected))}")
    stage = payload.get("reply_stage", "unknown")
    if stage not in ("first", "subsequent", "unknown"):
        raise ValueError("reply_stage must be first, subsequent or unknown")
    needs = payload.get("needs", {})
    if not isinstance(needs, dict) or set(needs) - set(NEED_FIELDS):
        raise ValueError("needs must be an object with only the four documented need fields")
    missing = []
    if stage == "first":
        missing.append("first_reply_must_be_non_price")
    elif stage == "unknown":
        missing.append("reply_stage_not_confirmed")

    def confirmed(item: dict, name: str, party: str, *, objective: bool = False) -> bool:
        if not isinstance(item, dict):
            raise ValueError(f"{name}: expected an evidence object")
        allowed = {"status", "value", "source", "confirmed_by"} | ({"kind"} if objective else set())
        if set(item) - allowed:
            raise ValueError(f"{name}: unknown evidence fields")
        state = item.get("status", "unknown")
        if state not in ("confirmed", "inferred", "unknown"):
            raise ValueError(f"{name}: status must be confirmed, inferred or unknown")
        for field in ("value", "source", "confirmed_by"):
            if field in item and not isinstance(item[field], str):
                raise ValueError(f"{name}: {field} must be a string")
        if objective and "kind" in item and item["kind"] not in ("pain", "goal"):
            raise ValueError("pain_or_goal.kind must be pain or goal")
        return (state == "confirmed" and item.get("confirmed_by") == party
                and all(item.get(key, "").strip() for key in ("value", "source"))
                and (not objective or item.get("kind") in ("pain", "goal")))

    for field in NEED_FIELDS:
        if not confirmed(needs.get(field, {}), f"needs.{field}", "buyer"):
            missing.append(f"needs.{field}")
    if not confirmed(payload.get("pain_or_goal", {}), "pain_or_goal", "buyer", objective=True):
        missing.append("buyer_confirmed_pain_or_goal")
    if not confirmed(payload.get("product_selection", {}), "product_selection", "seller"):
        missing.append("seller_confirmed_product_selection")
    offer = payload.get("seller_offer", {})
    if not isinstance(offer, dict) or set(offer) - {"authorized", "scope_matches", "source"}:
        raise ValueError("seller_offer must contain only authorized, scope_matches and source")
    for key in ("authorized", "scope_matches"):
        if key in offer and not isinstance(offer[key], bool):
            raise ValueError(f"seller_offer.{key} must be a boolean")
    if "source" in offer and not isinstance(offer["source"], str):
        raise ValueError("seller_offer.source must be a string")
    if not (offer.get("authorized") is True and offer.get("scope_matches") is True
            and offer.get("source", "").strip()):
        missing.append("authorized_matching_seller_offer")
    allowed = not missing
    return {"quote_allowed": allowed,
            "status": "hold_first_reply" if stage == "first" else "ready_to_quote" if allowed else "hold_discovery",
            "reply_stage": stage, "missing_or_blocked": missing,
            "next_action": "Draft a needs-matched authorized offer; do not send automatically." if allowed
            else "Provide non-price value and clarify only material unanswered needs; do not invent pain.",
            "evidence_note": "Field/rule check only. Confirm source authenticity and substantive adequacy separately."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate")
    check.add_argument("--minimum", type=int, default=100)
    check.add_argument("--near-threshold", type=float, default=0.78)
    finder = sub.add_parser("search")
    finder.add_argument("query")
    finder.add_argument("--module", type=str.upper, choices=list(MODULES), action="append")
    finder.add_argument("--limit", type=int, default=5)
    scorer = sub.add_parser("score")
    scorer.add_argument("input", help="JSON file, or - for stdin; input is never stored")
    gate = sub.add_parser("quote-gate")
    gate.add_argument("input", help="Private JSON file, or - for stdin; input is never stored")
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            if args.minimum < 1 or not 0 < args.near_threshold <= 1:
                raise ValueError("minimum must be positive and near-threshold in (0, 1]")
            result = validate(args.root, args.minimum, args.near_threshold)
            status = 1 if result["errors"] else 0
        elif args.command == "search":
            if not 1 <= args.limit <= 20:
                raise ValueError("limit must be 1-20")
            result, status = search(args.root, args.query, args.module, args.limit), 0
        else:
            data = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
            evaluator = quote_gate if args.command == "quote-gate" else score_customer
            result, status = evaluator(json.loads(data)), 0
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return status
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
