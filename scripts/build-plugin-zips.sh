#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/plugins"
rm -rf "$OUT"
mkdir -p "$OUT"
if ! command -v zip >/dev/null 2>&1; then
  echo "Error: zip not found. Install zip and retry." >&2
  exit 1
fi
count=0
for plugin_dir in "$ROOT"/plugins/*; do
  [ -d "$plugin_dir" ] || continue
  plugin_name="$(basename "$plugin_dir")"
  (cd "$ROOT/plugins" && zip -qr "$OUT/$plugin_name.zip" "$plugin_name")
  count=$((count+1))
done
echo "Created $count plugin ZIPs in dist/plugins"
