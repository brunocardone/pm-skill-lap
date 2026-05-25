#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
VERSION="$(python3 - <<'PYVERSION'
import json
print(json.load(open('.claude-plugin/marketplace.json')).get('version','dev'))
PYVERSION
)"
DIST="$ROOT/dist"
RELEASE="$DIST/release"

echo "[1/5] Validate"
bash scripts/validate-pm-lap.sh

echo "[2/5] Build skill ZIPs"
bash scripts/build-skill-zips.sh

echo "[3/5] Build Claude Desktop/Web packs"
bash scripts/build-claude-desktop-packs.sh

echo "[4/5] Build plugin ZIPs and Codex package"
bash scripts/build-plugin-zips.sh
bash scripts/build-codex-package.sh

echo "[5/5] Build master release artifact"
rm -rf "$RELEASE"
mkdir -p "$RELEASE/docs"
cp -R .claude-plugin "$RELEASE/.claude-plugin"
cp -R plugins "$RELEASE/plugins"
cp -R dist/skill-zips "$RELEASE/skill-zips"
cp -R dist/claude-desktop "$RELEASE/claude-desktop"
cp -R dist/plugins "$RELEASE/plugin-zips"
cp -R dist/codex "$RELEASE/codex"
cp README.md "$RELEASE/README.md"
cp docs/INSTALL-CLAUDE-CODE.md docs/INSTALL-CLAUDE-DESKTOP.md docs/INSTALL-CODEX.md docs/RELEASE-PACKAGING.md docs/GOLD-STANDARD-OPERATING-MODE.md "$RELEASE/docs/"
artifact="$DIST/pm-skill-lap-$VERSION-release.zip"
rm -f "$artifact"
(cd "$RELEASE" && zip -qr "$artifact" .)
echo "Release artifact: $artifact"
