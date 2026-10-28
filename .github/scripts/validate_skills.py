#!/usr/bin/env python3
"""Check that every skills/*/SKILL.md starts with YAML frontmatter containing
a `name` that matches its folder and a non-empty `description`."""
import pathlib
import sys

import yaml

root = pathlib.Path(__file__).resolve().parents[2]
skills = sorted(root.glob("skills/*/SKILL.md"))
errors = []

if not skills:
    errors.append("no skills/*/SKILL.md files found")

for path in skills:
    rel = path.relative_to(root)
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{rel}: missing YAML frontmatter (file must start with '---')")
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{rel}: frontmatter is not closed with '---'")
        continue
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{rel}: invalid YAML frontmatter: {exc}")
        continue
    if not isinstance(meta, dict):
        errors.append(f"{rel}: frontmatter must be a mapping")
        continue
    name = meta.get("name")
    desc = meta.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{rel}: missing 'name'")
    elif name != path.parent.name:
        errors.append(f"{rel}: name '{name}' does not match folder '{path.parent.name}'")
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{rel}: missing 'description'")

for e in errors:
    print(f"ERROR: {e}")
print(f"Checked {len(skills)} skill(s), {len(errors)} error(s).")
sys.exit(1 if errors else 0)
