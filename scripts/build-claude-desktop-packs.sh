#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_ZIPS="$ROOT/dist/skill-zips"
OUT="$ROOT/dist/claude-desktop"
mkdir -p "$OUT"
bash "$ROOT/scripts/build-skill-zips.sh" >/dev/null
pack() {
  local zip_name="$1"; shift
  local tmp="$(mktemp -d)"
  local count=0
  for skill in "$@"; do
    if [ -f "$SKILL_ZIPS/$skill.zip" ]; then
      cp "$SKILL_ZIPS/$skill.zip" "$tmp/"
      count=$((count+1))
    else
      echo "warning: missing skill zip $skill.zip" >&2
    fi
  done
  if [ "$count" -eq 0 ]; then
    echo "error: pack $zip_name would be empty" >&2
    exit 1
  fi
  (cd "$tmp" && zip -qr "$OUT/$zip_name" .)
  rm -rf "$tmp"
  echo "Created $zip_name ($count skills)"
}
pack 01-core-pm-starter-pack.zip pm-skills-select problem-statement jobs-to-be-done prioritization-frameworks create-prd outcome-roadmap product-strategy
cp "$OUT/01-core-pm-starter-pack.zip" "$OUT/pm-skills-starter-pack.zip"
pack 02-discovery-pack.zip discovery-process problem-statement jobs-to-be-done opportunity-solution-tree interview-script summarize-interview experiment-design prioritize-assumptions
pack 03-strategy-pack.zip product-strategy product-vision value-proposition positioning-statement pricing-strategy lean-canvas business-model
pack 04-delivery-pack.zip create-prd user-stories test-scenarios outcome-roadmap brainstorm-okrs sprint-plan release-notes
pack 05-ai-pm-pack.zip ai-readiness context-engineering recommendation-canvas experiment-design metrics-dashboard
(cd "$SKILL_ZIPS" && zip -qr "$OUT/99-all-skills-pack.zip" .)
echo "Claude Desktop/Web packs ready in dist/claude-desktop"
