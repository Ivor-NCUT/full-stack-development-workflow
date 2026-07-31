#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
errors: list[str] = []
for name in ("README.md", "AGENTS.md", "LICENSE", "VERSION", "project.json"):
    if not (root / name).is_file():
        errors.append(f"missing {name}")
project = json.loads((root / "project.json").read_text(encoding="utf-8"))
names = [project["entry_skill"], *[item["skill"] for item in project["experts"]]]
for name in names:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"invalid skill name: {name}")
    path = root / "skills" / name / "SKILL.md"
    if not path.is_file():
        errors.append(f"missing skill: {name}")
    elif "[TODO" in path.read_text(encoding="utf-8"):
        errors.append(f"unresolved template: {path}")
if errors:
    print("INVALID")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)
print(f"VALID: {root}")
