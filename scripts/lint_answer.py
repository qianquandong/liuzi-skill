#!/usr/bin/env python3
"""Lint a Liuzi-style Markdown answer for required decision safeguards."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EVIDENCE_LABELS = ("官方直接确认", "第一方自述", "第三方支持", "合理推测", "无法验证")
ABSOLUTE_PATTERNS = (
    r"百分之百(?:获批|通过|安全)",
    r"保证(?:获批|通过|合法|安全)",
    r"肯定(?:获批|通过|合法|没问题)",
)


def lint(text: str, risk: str, require_recommendation: bool) -> list[str]:
    errors: list[str] = []
    if risk in {"medium", "high"} and not re.search(r"核验日期[:：]\s*\d{4}-\d{2}-\d{2}", text):
        errors.append("missing 核验日期: YYYY-MM-DD")
    if risk == "high":
        if not any(label in text for label in EVIDENCE_LABELS):
            errors.append("high-risk answer needs an evidence status label")
        if not re.search(r"https?://", text):
            errors.append("high-risk answer needs a direct source URL")
        if not re.search(r"(Human gate|提交前|签字前|付款前|开始工作前|就医)", text, re.IGNORECASE):
            errors.append("high-risk answer needs an action gate or medical escalation")
    if require_recommendation and "我最推荐" not in text:
        errors.append("missing explicit 我最推荐")
    if not re.search(r"(你现在直接做|下一步)", text):
        errors.append("missing executable next step")
    for pattern in ABSOLUTE_PATTERNS:
        if re.search(pattern, text):
            errors.append(f"unsupported absolute claim: {pattern}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="Markdown file, or - for stdin")
    parser.add_argument("--risk", choices=("low", "medium", "high"), default="medium")
    parser.add_argument("--require-recommendation", action="store_true")
    args = parser.parse_args()
    try:
        text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    errors = lint(text, args.risk, args.require_recommendation)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("answer: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

