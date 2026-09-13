from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_script(script: str, fixture: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [PYTHON, str(ROOT / "scripts" / script), str(ROOT / "tests" / "fixtures" / fixture), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class ToolTests(unittest.TestCase):
    def test_all_in_calculation(self) -> None:
        result = run_script("calculate_all_in.py", "all_in.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["results"][0]["all_in"], "15850.00")
        self.assertEqual(payload["results"][1]["effective_per_period"], "1406.25")

    def test_score_hard_filters_and_evidence_gate(self) -> None:
        result = run_script("score_options.py", "score_options.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual([item["name"] for item in payload["ranked"]], ["Balanced"])
        excluded = {item["name"]: item["reasons"] for item in payload["excluded"]}
        self.assertIn("evidence:unverified", excluded["Cheap but unverified"])
        self.assertIn("budget", excluded["Over budget"])

    def test_valid_evidence_passes(self) -> None:
        result = run_script("validate_evidence.py", "evidence_valid.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_high_risk_nonofficial_evidence_fails(self) -> None:
        result = run_script("validate_evidence.py", "evidence_invalid.json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("high risk", result.stdout)

    def test_valid_answer_passes(self) -> None:
        result = run_script("lint_answer.py", "answer_valid.md", "--risk", "high", "--require-recommendation")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unsafe_answer_fails(self) -> None:
        result = run_script("lint_answer.py", "answer_invalid.md", "--risk", "high", "--require-recommendation")
        self.assertEqual(result.returncode, 1)
        self.assertIn("unsupported absolute claim", result.stdout)

    def test_repository_links_resolve_locally(self) -> None:
        result = subprocess.run(
            [PYTHON, str(ROOT / "scripts" / "check_source_links.py"), "."],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()

