# Repository rules

- Keep the main router thin and each expert responsible for one development outcome.
- Reuse `codex-dev-good-taste`, Ponytail, and installed platform Skills instead of copying them.
- Maintain compatibility and add one runnable check for non-trivial logic.
- Update `project.json`, architecture, routing cases, and tests when experts change.
- Run `python3 tools/validate_project.py .` and `python3 -m unittest discover -s tests -v` before publishing.
