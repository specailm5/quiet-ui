import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import validate_skill

GOOD = """---
name: quiet-ui
description: "A description long enough to pass validation."
---

# Quiet UI

See `references/patterns.md`.
"""


class ValidateSkillTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        (self.root / "SKILL.md").write_text(GOOD, encoding="utf-8")
        (self.root / "README.md").write_text("# Quiet UI\n", encoding="utf-8")
        (self.root / "references").mkdir()
        (self.root / "references" / "patterns.md").write_text("# Patterns\n", encoding="utf-8")

    def test_valid(self):
        self.assertEqual(validate_skill.validate_skill(self.root), [])

    def test_missing_frontmatter(self):
        (self.root / "SKILL.md").write_text("# No frontmatter\n", encoding="utf-8")
        errors = validate_skill.validate_skill(self.root)
        self.assertTrue(any("frontmatter" in error for error in errors))

    def test_name_mismatch(self):
        text = GOOD.replace("name: quiet-ui", "name: other")
        (self.root / "SKILL.md").write_text(text, encoding="utf-8")
        errors = validate_skill.validate_skill(self.root)
        self.assertTrue(any("name" in error for error in errors))

    def test_missing_reference(self):
        (self.root / "references" / "patterns.md").unlink()
        errors = validate_skill.validate_skill(self.root)
        self.assertTrue(any("patterns.md" in error for error in errors))

    def test_em_dash(self):
        (self.root / "README.md").write_text("# Quiet UI \u2014 text\n", encoding="utf-8")
        errors = validate_skill.validate_skill(self.root)
        self.assertTrue(any("em dash" in error for error in errors))

    def test_symlink(self):
        (self.root / "link.md").symlink_to(self.root / "README.md")
        errors = validate_skill.validate_skill(self.root)
        self.assertTrue(any("symlink" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
