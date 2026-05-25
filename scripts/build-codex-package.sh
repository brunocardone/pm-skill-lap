#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/codex"
SKILLS_OUT="$OUT/.agents/skills"
rm -rf "$OUT"
mkdir -p "$SKILLS_OUT"
count=0
for skill_file in "$ROOT"/plugins/*/skills/*/SKILL.md; do
  [ -f "$skill_file" ] || continue
  skill_dir="$(dirname "$skill_file")"
  skill_name="$(basename "$skill_dir")"
  rm -rf "$SKILLS_OUT/$skill_name"
  cp -R "$skill_dir" "$SKILLS_OUT/$skill_name"
  count=$((count+1))
done
cat > "$OUT/AGENTS.md" <<'EOFAGENTS'
# PM Skill LAP for Codex

Use the skills in `.agents/skills` as reusable PM workflows. Start with `pm-skills-select` when the user is unsure which PM framework or artifact is needed.
EOFAGENTS
(cd "$OUT" && zip -qr "$ROOT/dist/codex/pm-skill-lap-codex.zip" .agents AGENTS.md)
echo "Created Codex package with $count skills in dist/codex"
