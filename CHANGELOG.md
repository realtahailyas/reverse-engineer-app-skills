# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- MIT license, and `license` field in the plugin and marketplace manifests.
- Contributing guide, Code of Conduct (Contributor Covenant 2.1), security policy.
- Issue templates (bug report, feature request, new skill) and a pull request template.
- CI workflow that validates `SKILL.md` frontmatter, compiles the Python tools and checks the manifests.

## [1.0.0] - 2026-10-22

### Added
- 11 Claude Code skills: `replica-recon`, `replica-architect`, `replica-design`, `replica-build`, `replica-backend`, `replica-test`, `replica-diff`, `replica-entrepreneur`, `replica-brand`, `replica-launch`, `replica-deploy`.
- Standard-library Python tools: `parity.py`, `imgdiff.py`, `contrast.py`, `reviews.py`, `sweep.py`, `listing.py`.
- Claude Code plugin and marketplace manifests.
- One-line installers for macOS/Linux (`install.sh`) and Windows (`install.ps1`).
- Example prompts in `examples/prompts.md`.

[Unreleased]: https://github.com/realtahailyas/reverse-engineer-app-skills/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/realtahailyas/reverse-engineer-app-skills/releases/tag/v1.0.0
