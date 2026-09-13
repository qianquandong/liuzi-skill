#!/usr/bin/env python3
"""Hard-filter and rank options using normalized weighted scores."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

RANKABLE = {"official_confirmed", "first_party_claim", "third_party_supported"}


def read_json(path: str) -> Any:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def score(payload: dict[str, Any]) -> dict[str, Any]:
    weights = payload.get("weights")
    options = payload.get("options")
    if not isinstance(weights, dict) or not weights:
        raise ValueError("weights must be a non-empty object")
    if not isinstance(options, list) or not options:
        raise ValueError("options must be a non-empty array")
    numeric_weights: dict[str, float] = {}
    for key, value in weights.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"weight {key} must be a non-negative number")
        numeric_weights[key] = float(value)
    weight_total = sum(numeric_weights.values())
    if weight_total <= 0:
        raise ValueError("weights must total more than zero")

    ranked: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    for option in options:
        if not isinstance(option, dict) or not option.get("name"):
            raise ValueError("every option needs a name")
        failures = [str(key) for key, passed in option.get("hard_constraints", {}).items() if passed is not True]
        status = option.get("evidence_status", "unverified")
        risk = option.get("risk", "low")
        if status not in RANKABLE:
            failures.append(f"evidence:{status}")
        if risk == "high" and status != "official_confirmed":
            failures.append("high-risk-requires-official")
        if failures:
            excluded.append({"name": option["name"], "reasons": failures})
            continue
        scores = option.get("scores", {})
        total = 0.0
        for dimension, weight in numeric_weights.items():
            value = scores.get(dimension)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 10:
                raise ValueError(f"{option['name']}.{dimension} must be between 0 and 10")
            total += float(value) * weight
        ranked.append({
            "name": option["name"],
            "score": round(total / weight_total * 10, 2),
            "evidence_status": status,
        })
    ranked.sort(key=lambda item: (-item["score"], item["name"].lower()))
    for index, item in enumerate(ranked, 1):
        item["rank"] = index
    return {"ranked": ranked, "excluded": excluded}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="JSON file, or - for stdin")
    args = parser.parse_args()
    try:
        payload = read_json(args.input)
        if not isinstance(payload, dict):
            raise ValueError("input must be an object")
        result = score(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

