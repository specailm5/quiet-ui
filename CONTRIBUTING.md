# Contributing

## Before you open a pull request

1. Keep `SKILL.md` short. Put detail in `references/`.
2. Run the checks:

   ```bash
   python3 scripts/validate_skill.py
   python3 -m unittest discover -s tests -v
   ```

3. Add an entry under `Unreleased` in `CHANGELOG.md`.
4. Use a Conventional Commits message, such as `docs: add a tooltip pattern`.

## What belongs here

- A pattern that appears in real interfaces.
- A placement rule that says where a fact goes.
- A before/after example that shows the fix.

## What does not

- A phrase blocklist. The skill is judgment, not a linter.
- A rule that repeats a label or a standard control.
- Em dashes.

## Review

One maintainer reviews pull requests. Keep each change focused on one pattern
or one example.
