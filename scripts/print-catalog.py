#!/usr/bin/env python3
import json
from pathlib import Path
market=json.load(open('.claude-plugin/marketplace.json', encoding='utf-8'))
print(f"# {market['name']} v{market.get('version','')}")
for p in market['plugins']:
    root=Path(p['source'].replace('./',''))
    skills=sorted(x.parent.name for x in root.glob('skills/*/SKILL.md'))
    commands=sorted(x.stem for x in root.glob('commands/*.md'))
    print(f"\n## {p['name']}")
    print(p.get('description',''))
    print(f"Skills ({len(skills)}): " + ', '.join(skills))
    print(f"Commands ({len(commands)}): " + ', '.join('/'+c for c in commands))
