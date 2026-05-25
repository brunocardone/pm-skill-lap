#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/skill-zips"
rm -rf "$OUT"
mkdir -p "$OUT"
if ! command -v zip >/dev/null 2>&1; then
  echo "Error: zip not found. Install zip and retry." >&2
  exit 1
fi
count=0
for skill_file in "$ROOT"/plugins/*/skills/*/SKILL.md; do
  [ -f "$skill_file" ] || continue
  skill_dir="$(dirname "$skill_file")"
  skill_name="$(basename "$skill_dir")"
  tmp="$(mktemp -d)"
  cp -R "$skill_dir" "$tmp/$skill_name"
  (cd "$tmp" && zip -qr "$OUT/$skill_name.zip" "$skill_name")
  rm -rf "$tmp"
  count=$((count+1))
done
echo "Created $count skill ZIPs in dist/skill-zips"
