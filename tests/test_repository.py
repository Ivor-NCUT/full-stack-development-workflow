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
        self.assertEqual(matt["commit"], "84fdeffd12f2ee307994d1eb6feb48173b6e0502")

    def test_ponytail_is_optional_external_capability(self) -> None:
        sources = [
            json.loads(line)
            for line in (ROOT / "knowledge" / "sources.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        ponytail = next(item for item in sources if item["id"] == "ponytail")
        self.assertEqual(ponytail["license"], "MIT")
        self.assertEqual(ponytail["type"], "third-party-plugin")
        self.assertIn("do not vendor", ponytail["allowed_use"])
        dependency = next(item for item in PROJECT["dependencies"] if item.get("skill") == "ponytail")
        self.assertEqual(dependency["role"], "optional-on-demand-coding-capability")

    def test_security_redaction_and_wizard_are_routed_without_vendoring(self) -> None:
        skill_root = ROOT / "skills" / PROJECT["entry_skill"]
        security = (skill_root / "references" / "security-review.md").read_text(encoding="utf-8")
        engineering = (skill_root / "references" / "engineering-principles.md").read_text(encoding="utf-8")
        main = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("codex-security:security-diff-scan", security)
        self.assertIn("<REDACTED>", engineering)
        self.assertIn("已安装的 `wizard`", main)
        security_dependency = next(item for item in PROJECT["dependencies"] if item.get("plugin") == "codex-security")
        wizard_dependency = next(item for item in PROJECT["dependencies"] if item.get("skill") == "wizard")
        self.assertEqual(security_dependency["role"], "external-security-review-tools")
        self.assertEqual(wizard_dependency["role"], "optional-human-setup-capability")


if __name__ == "__main__":
    unittest.main()
