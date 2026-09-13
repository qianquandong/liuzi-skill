#!/usr/bin/env python3
"""Validate a decision's claims, sources, and recommendation evidence."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

STATUSES = {"official_confirmed", "first_party_claim", "third_party_supported", "inference", "unverified"}
RISKS = {"low", "medium", "high"}
SOURCE_TYPES = {"official", "first_party", "mature_platform", "community"}
UNRANKABLE = {"inference", "unverified"}


def is_http_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    checked_at = payload.get("checked_at")
    if not isinstance(checked_at, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked_at):
        errors.append("checked_at must use YYYY-MM-DD")
    else:
        try:
            date.fromisoformat(checked_at)
        except ValueError:
            errors.append("checked_at is not a valid date")

    claims = payload.get("claims")
    if not isinstance(claims, list) or not claims:
        return errors + ["claims must be a non-empty array"]
    by_id: dict[str, dict[str, Any]] = {}
    for index, claim in enumerate(claims):
        prefix = f"claims[{index}]"
        if not isinstance(claim, dict):
            errors.append(f"{prefix} must be an object")
            continue
        claim_id = claim.get("id")
        if not isinstance(claim_id, str) or not claim_id:
            errors.append(f"{prefix}.id is required")
        elif claim_id in by_id:
            errors.append(f"duplicate claim id: {claim_id}")
        else:
            by_id[claim_id] = claim
        if not isinstance(claim.get("claim"), str) or not claim["claim"].strip():
            errors.append(f"{prefix}.claim is required")
        status = claim.get("status")
        risk = claim.get("risk")
        if status not in STATUSES:
            errors.append(f"{prefix}.status is invalid")
        if risk not in RISKS:
            errors.append(f"{prefix}.risk is invalid")
        sources = claim.get("sources", [])
        if not isinstance(sources, list):
            errors.append(f"{prefix}.sources must be an array")
            sources = []
        official = False
        for source_index, source in enumerate(sources):
            source_prefix = f"{prefix}.sources[{source_index}]"
            if not isinstance(source, dict):
                errors.append(f"{source_prefix} must be an object")
                continue
            if source.get("type") not in SOURCE_TYPES:
                errors.append(f"{source_prefix}.type is invalid")
            if not is_http_url(source.get("url")):
                errors.append(f"{source_prefix}.url must be http(s)")
            official = official or source.get("type") == "official"
        if status == "official_confirmed" and not official:
            errors.append(f"{prefix} claims official confirmation without an official source")
        if risk == "high" and status != "official_confirmed":
            errors.append(f"{prefix} is high risk and must be official_confirmed")

    recommendations = payload.get("recommendations", [])
    if not isinstance(recommendations, list):
        errors.append("recommendations must be an array")
        recommendations = []
    for index, recommendation in enumerate(recommendations):
        prefix = f"recommendations[{index}]"
        if not isinstance(recommendation, dict) or not recommendation.get("name"):
            errors.append(f"{prefix}.name is required")
            continue
        refs = recommendation.get("claim_refs")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{prefix}.claim_refs must be non-empty")
            continue
        for ref in refs:
            if ref not in by_id:
                errors.append(f"{prefix} references unknown claim {ref}")
            elif by_id[ref].get("status") in UNRANKABLE:
                errors.append(f"{prefix} relies on unrankable claim {ref}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="JSON file, or - for stdin")
    args = parser.parse_args()
    try:
        text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
        payload = json.loads(text)
        if not isinstance(payload, dict):
            raise ValueError("input must be an object")
        errors = validate(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("evidence: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

