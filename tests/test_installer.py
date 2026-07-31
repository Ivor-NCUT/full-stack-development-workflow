from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PROJECT = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))
INSTALLER = ROOT / "tools" / "install.mjs"


class InstallerTest(unittest.TestCase):
    def run_installer(self, skills_home: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["node", str(INSTALLER)],
            env={**os.environ, "SKILLS_HOME": str(skills_home)},
            check=True,
            capture_output=True,
            text=True,
        )

    def test_retires_only_links_managed_by_this_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skills_home = Path(temp) / "skills with spaces"
            skills_home.mkdir()
            for name in PROJECT["retired_entries"]:
                (skills_home / name).symlink_to(ROOT / "skills" / name, target_is_directory=True)
            protected_directory = skills_home / PROJECT["retired_entries"][0]
            protected_directory.unlink()
            protected_directory.mkdir()
            foreign_link = skills_home / PROJECT["retired_entries"][1]
            foreign_link.unlink()
            foreign_link.symlink_to(Path(temp) / "foreign", target_is_directory=True)

            first = self.run_installer(skills_home)
            second = self.run_installer(skills_home)

            self.assertTrue((skills_home / PROJECT["entry_skill"] / "SKILL.md").is_file())
            self.assertTrue(protected_directory.is_dir())
            self.assertTrue(foreign_link.is_symlink())
            for name in PROJECT["retired_entries"][2:]:
                self.assertFalse((skills_home / name).is_symlink())
            self.assertIn("installed full-stack-development-workflow", first.stdout)
            self.assertIn("ok full-stack-development-workflow", second.stdout)


if __name__ == "__main__":
    unittest.main()
