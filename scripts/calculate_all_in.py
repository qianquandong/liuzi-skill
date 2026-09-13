#!/usr/bin/env python3
"""Calculate comparable all-in costs from a small JSON schema."""

from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


def money(value: Decimal) -> str:
    return str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def as_decimal(value: Any, field: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be a number")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field} must be a number") from None
    if result < 0:
        raise ValueError(f"{field} must be non-negative")
    return result


def sum_group(raw: Any, field: str) -> Decimal:
    if raw is None:
        return Decimal("0")
    if not isinstance(raw, dict):
        raise ValueError(f"{field} must be an object")
    return sum((as_decimal(value, f"{field}.{key}") for key, value in raw.items()), Decimal("0"))


def calculate(option: dict[str, Any]) -> dict[str, Any]:
    periods = as_decimal(option.get("periods", 1), "periods")
    if periods <= 0:
        raise ValueError("periods must be greater than zero")
    recurring = sum_group(option.get("recurring", {}), "recurring")
    one_time = sum_group(option.get("one_time", {}), "one_time")
    credits = sum_group(option.get("credits", {}), "credits")
    gross = recurring * periods + one_time
    total = gross - credits
    return {
        "name": str(option.get("name", "option")),
        "currency": str(option.get("currency", "USD")),
        "periods": money(periods),
        "recurring_per_period": money(recurring),
        "one_time": money(one_time),
        "credits": money(credits),
        "gross_cost": money(gross),
        "all_in": money(total),
        "effective_per_period": money(total / periods),
    }


def read_json(path: str) -> Any:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="JSON file, or - for stdin")
    args = parser.parse_args()
    try:
        payload = read_json(args.input)
        raw_options = payload.get("options") if isinstance(payload, dict) else None
        options = raw_options if raw_options is not None else [payload]
        if not isinstance(options, list) or not options or not all(isinstance(item, dict) for item in options):
            raise ValueError("input must be an option object or an object with a non-empty options array")
        output = {"results": [calculate(item) for item in options]}
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

