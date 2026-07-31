# Repository rules

- Keep exactly one discoverable Skill entry: `full-stack-development-workflow`.
- Put reusable engineering guidance in the three references linked directly from the entry Skill.
- Integrate principles from `codex-dev-good-taste` and `multi-agent-github-workflow`; invoke installed platform Skills for actual connector operations.
- Keep Zeabur tools external and update the routing table when installed capabilities change.
- Maintain compatibility and add one runnable check for non-trivial logic.
- Preserve source attribution and do not copy unlicensed third-party content.
- Update `project.json`, architecture, routing cases, and tests when the reference structure changes.
- Run `python3 tools/validate_project.py .` and `python3 -m unittest discover -s tests -v` before publishing.
