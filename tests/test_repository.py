from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PROJECT = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))


class RepositoryTest(unittest.TestCase):
    def test_repository_has_one_deep_skill(self) -> None:
        self.assertEqual(PROJECT["experts"], [])
        skill_dirs = sorted(path.name for path in (ROOT / "skills").iterdir() if path.is_dir())
        self.assertEqual(skill_dirs, [PROJECT["entry_skill"]])
        text = (ROOT / "skills" / PROJECT["entry_skill"] / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f"name: {PROJECT['entry_skill']}", text)
        self.assertNotIn("[TODO", text)

    def test_references_and_routing_cases(self) -> None:
        skill_root = ROOT / "skills" / PROJECT["entry_skill"]
        main = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        expected_references = set(PROJECT["references"])
        for name in expected_references:
            self.assertTrue((skill_root / "references" / name).is_file())
            self.assertIn(name, main)
        cases = json.loads((ROOT / "tests" / "routing_cases.json").read_text(encoding="utf-8"))
        self.assertEqual({item["expected"] for item in cases}, {PROJECT["entry_skill"]})
        self.assertEqual({name for item in cases for name in item["references"]}, expected_references)

    def test_sources_record_mattpocock_license(self) -> None:
        sources = [
            json.loads(line)
            for line in (ROOT / "knowledge" / "sources.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        matt = next(item for item in sources if item["id"] == "mattpocock-skills")
        self.assertEqual(matt["license"], "MIT")


if __name__ == "__main__":
    unittest.main()
