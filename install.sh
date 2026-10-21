#!/usr/bin/env sh
# Installs the Replica skills into ~/.claude/skills so every Claude Code project can use them.
set -e
REPO="https://github.com/realtahailyas/reverse-engineer-app-skills"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
TMP="$(mktemp -d)"
git clone --depth 1 "$REPO" "$TMP/repo" >/dev/null 2>&1
mkdir -p "$DEST"
cp -R "$TMP"/repo/skills/replica-* "$DEST"/
rm -rf "$TMP"
echo "Installed 11 Replica skills into $DEST"
echo "Open Claude Code and type: /replica-recon <app url>"
