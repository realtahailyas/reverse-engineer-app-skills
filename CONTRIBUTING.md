# Contributing

Thanks for helping improve Replica. Bug reports, fixes to existing skills, new tools and new skills are all welcome.

## Ground rules

- **Clean room only.** Skills must work from public pages, help docs, store listings, public videos, the user's own account and official APIs. No scraping behind logins, no paywall or login bypass, no decompiling, no private API endpoints, no copying code, assets, fonts or copy. PRs that add any of these will be closed. See [The rules](README.md#the-rules).
- **Standard-library Python.** Tools in `skills/*/` must run with `python3` and no `pip install`.
- **Keep skills focused.** One skill, one job. If a change makes a skill do two things, it probably wants to be a second skill.

## Skill format

Every skill lives in `skills/<name>/SKILL.md` and starts with YAML frontmatter:

```yaml
---
name: replica-example          # must match the folder name
description: >-
  What the skill does and the phrases that should trigger it.
---
```

Supporting templates and tools sit next to `SKILL.md` in the same folder. Outputs a skill writes into the user's project go under `replica/`.

## Before you open a pull request

```bash
pip install pyyaml
python .github/scripts/validate_skills.py   # frontmatter check
python -m py_compile skills/*/*.py          # tools compile
```

Then try the skill for real in Claude Code (copy it to `~/.claude/skills/` and restart) on at least one app. CI runs the same checks on every pull request.

## Pull requests

1. Fork the repo and create a branch from `main`.
2. Make your change, and update `README.md` (skills table, tools table, repo layout) and `CHANGELOG.md` if it is user-facing.
3. Fill in the pull request template.

## Reporting bugs and ideas

Use the issue templates: **Bug report**, **Feature request** or **New skill proposal**. For security problems, see [SECURITY.md](SECURITY.md) instead of opening a public issue.

By contributing you agree that your contributions are licensed under the [MIT License](LICENSE) and that you will follow the [Code of Conduct](CODE_OF_CONDUCT.md).
