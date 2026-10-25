#!/usr/bin/env python3
"""Validate the quiet-ui skill and repository layout."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME = "quiet-ui"
MIN_DESCRIPTION = 20
MAX_DESCRIPTION = 1024
MAX_SKILL_LINES = 500
SKIP = {".git", "__pycache__", ".venv", "venv", "node_modules", ".pytest_cache", ".mypy_cache"}


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def walk(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP for part in path.relative_to(root).parts):
            continue
        yield path


def validate_skill(root: Path) -> list[str]:
    errors = []
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return ["SKILL.md is missing"]
    if not (root / "README.md").is_file():
        errors.append("README.md is missing")

    text = skill_path.read_text(encoding="utf-8")
    lines = text.count("\n") + (0 if text.endswith("\n") else 1)
    if lines > MAX_SKILL_LINES:
        errors.append(f"SKILL.md is {lines} lines; keep it under {MAX_SKILL_LINES}")

    fields = parse_frontmatter(text)
    if fields is None:
        return errors + ["SKILL.md has no valid frontmatter"]
    if fields.get("name") != NAME:
        errors.append(f"frontmatter name must be {NAME!r}")
    description = fields.get("description", "")
    if not MIN_DESCRIPTION <= len(description) <= MAX_DESCRIPTION:
        errors.append(f"description must be {MIN_DESCRIPTION}-{MAX_DESCRIPTION} characters")

    for rel in sorted(set(re.findall(r"references/[a-z0-9-]+\.md", text))):
        if not (root / rel).is_file():
            errors.append(f"missing referenced file: {rel}")

    for path in walk(root):
        if path.is_symlink():
            errors.append(f"symlink not allowed: {path.relative_to(root)}")
        if path.is_file() and path.suffix == ".md":
            if "\u2014" in path.read_text(encoding="utf-8"):
                errors.append(f"em dash in {path.relative_to(root)}")
    return errors


def validate_repo(root: Path) -> list[str]:
    required = (
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
        ".github/workflows/validate.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
    )
    return [f"{name} is missing" for name in required if not (root / name).is_file()]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors = validate_skill(root) + validate_repo(root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"OK: {NAME} is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
