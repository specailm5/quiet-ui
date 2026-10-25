# Quiet UI

A skill for AI coding agents. It keeps interface text quiet: no implementation
notes, no obvious qualifiers, no narrated basics. Secondary detail goes to an
info icon or the help page.

## Why

Agents fill interfaces with text nobody asked for:

- implementation notes: "Images are cached in IndexedDB"
- obvious qualifiers: "Search all files on your computer"
- narrated basics: "Type a note, then press Save"
- defensive disclaimers: "Results may vary"

The user does not need any of it to act. It adds reading, pushes the controls
down, and makes the product feel unsure of itself.

## The rule

If the user ignores the text, do they fail to do what they came to do? If no,
it does not belong on screen. Move it to an info icon or the help page, or cut
it.

## What is inside

| File | Purpose |
| --- | --- |
| `SKILL.md` | The rule, workflow, cut list, keep list, checklist |
| `references/patterns.md` | 11 anti-patterns with tell, reason, fix |
| `references/placement.md` | Where a fact goes: inline, info icon, help page, nowhere |
| `references/examples.md` | 9 before/after cases |

## Use

This repository is the source. It is not installed anywhere by default. To use
the skill, point your agent at `SKILL.md` or copy the folder into its skill
directory.

## Validate

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

Both run in CI on every push and pull request.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The change log follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## License

MIT. See [LICENSE](LICENSE).
