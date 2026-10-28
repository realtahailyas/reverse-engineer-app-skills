# Security Policy

## Supported versions

Only the latest release on `main` is supported.

## Reporting a vulnerability

Please **do not open a public issue** for security problems. Report them privately through GitHub: go to the **Security** tab of this repository and choose **Report a vulnerability**.

Include what you found, how to reproduce it and the impact. You will get a reply within 7 days, and a fix or a decision within 30 days for confirmed issues.

## Scope

This repository ships instructions (`SKILL.md`), templates and small standard-library Python tools. Relevant reports include:

- a tool that executes, writes or deletes files outside the paths it is given,
- `install.sh` / `install.ps1` doing anything beyond copying the skills into `~/.claude/skills/`,
- a skill instruction that would lead an agent to leak secrets, disable security controls or break the clean-room rules.

## A note on the one-line installers

`curl ... | sh` and `irm ... | iex` run remote code. If you prefer, download the script, read it, then run it, or use the plugin marketplace or manual install from the README.
