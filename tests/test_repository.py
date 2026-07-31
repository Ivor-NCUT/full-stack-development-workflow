from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PROJECT = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))


class RepositoryTest(unittest.TestCase):
    def test_skills_exist_and_are_unique(self) -> None:
        names = [PROJECT["entry_skill"], *[item["skill"] for item in PROJECT["experts"]]]
        self.assertEqual(len(names), len(set(names)))
        for name in names:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(f"name: {name}", text)
            self.assertNotIn("[TODO", text)

    def test_every_expert_has_a_routing_case(self) -> None:
        cases = json.loads((ROOT / "tests" / "routing_cases.json").read_text(encoding="utf-8"))
        self.assertEqual(
            {item["expected"] for item in cases},
            {item["skill"] for item in PROJECT["experts"]},
        )


if __name__ == "__main__":
    unittest.main()
