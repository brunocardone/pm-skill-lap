
#!/usr/bin/env bash

set -euo pipefail



echo "[1/4] JSON syntax"

python3 - <<'PY'

from pathlib import Path

import json



paths = [Path(".claude-plugin/marketplace.json")] + list(Path("plugins").glob("*/.claude-plugin/plugin.json"))

for p in paths:

    with p.open(encoding="utf-8") as f:

        json.load(f)

    print(f"ok {p}")

PY



echo "[2/4] Required marketplace/plugin paths"

python3 - <<'PY'

from pathlib import Path

import json

import sys



marketplace = Path(".claude-plugin/marketplace.json")

data = json.loads(marketplace.read_text(encoding="utf-8"))



errors = []

for plugin in data.get("plugins", []):

    name = plugin.get("name")

    source = plugin.get("source")

    if not name or not source:

        errors.append(f"marketplace plugin missing name/source: {plugin}")

        continue



    plugin_dir = Path(source)

    if not plugin_dir.exists():

        errors.append(f"missing plugin source for {name}: {source}")

        continue



    manifest = plugin_dir / ".claude-plugin" / "plugin.json"

    if not manifest.exists():

        errors.append(f"missing plugin manifest for {name}: {manifest}")



    if not (plugin_dir / "skills").exists():

        errors.append(f"missing skills dir for {name}: {plugin_dir / 'skills'}")



    if not (plugin_dir / "commands").exists():

        errors.append(f"missing commands dir for {name}: {plugin_dir / 'commands'}")



if errors:

    print("\n".join(errors))

    sys.exit(1)



print("ok marketplace plugin paths")

PY



echo "[3/4] Skill frontmatter sanity"

python3 - <<'PY'

from pathlib import Path

import sys



errors = []



for p in sorted(Path("plugins").glob("*/skills/*/SKILL.md")):

    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")

    lines = text.splitlines()



    if not lines or lines[0].strip() != "---":

        errors.append(f"{p}: first line must be ---")

        continue



    try:

        end = lines[1:].index("---") + 1

    except ValueError:

        errors.append(f"{p}: missing closing ---")

        continue



    fm = "\n".join(lines[1:end])

    if "name:" not in fm:

        errors.append(f"{p}: missing name in frontmatter")

    if "description:" not in fm:

        errors.append(f"{p}: missing description in frontmatter")



if errors:

    print("\n".join(errors))

    sys.exit(1)



print("ok skill frontmatter")

PY



echo "[4/4] Command markdown sanity"

python3 - <<'PY'

from pathlib import Path

import sys



errors = []



paths = sorted(Path("plugins").glob("*/commands/*.md")) + sorted(Path(".claude/commands").glob("*.md"))



for p in paths:

    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")

    if not text.strip():

        errors.append(f"{p}: empty command file")

        continue



    lines = text.splitlines()

    if lines and lines[0].strip() == "---":

        try:

            lines[1:].index("---")

        except ValueError:

            errors.append(f"{p}: command starts frontmatter but missing closing ---")



if errors:

    print("\n".join(errors))

    sys.exit(1)



print("ok command markdown")

PY



echo "Validation passed."

