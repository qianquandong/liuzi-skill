from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class StructureTests(unittest.TestCase):
    def test_skill_frontmatter_has_only_supported_keys(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match)
        keys = {
            line.split(":", 1)[0].strip()
            for line in match.group(1).splitlines()
            if line and not line.startswith((" ", "\t"))
        }
        self.assertEqual(keys, {"name", "description"})

    def test_openai_default_prompt_names_skill(self) -> None:
        text = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$liuzi-skill", text)
        self.assertIn("allow_implicit_invocation: true", text)

    def test_eval_suite_has_at_least_25_unique_cases(self) -> None:
        payload = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
        cases = payload["evals"]
        self.assertGreaterEqual(len(cases), 25)
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            self.assertTrue(case["prompt"].strip())
            self.assertGreaterEqual(len(case["assertions"]), 2)

    def test_core_references_have_operational_sections(self) -> None:
        required = ("最少", "硬", "搜索顺序", "输出结构", "失败回退", "Eval 映射")
        for name in ("money-credit.md", "housing.md", "immigration-school.md", "car.md", "healthcare.md"):
            text = (ROOT / "references" / name).read_text(encoding="utf-8")
            for heading in required:
                self.assertIn(heading, text, f"{name} missing {heading}")


if __name__ == "__main__":
    unittest.main()

