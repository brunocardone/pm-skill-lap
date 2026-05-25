#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
errors = []
market = json.loads((root/'.claude-plugin'/'marketplace.json').read_text())
for p in market['plugins']:
    pdir = root / p['source']
    if not pdir.exists(): errors.append(f"missing plugin dir: {p['source']}")
    manifest = pdir / '.claude-plugin' / 'plugin.json'
    if not manifest.exists(): errors.append(f"missing plugin manifest: {manifest}"); continue
    m = json.loads(manifest.read_text())
    for s in m.get('skills', []):
        if not (pdir / s).exists(): errors.append(f"missing skill: {pdir/s}")
    for c in m.get('commands', []):
        if not (pdir / c).exists(): errors.append(f"missing command: {pdir/c}")
if not (root/'.claude'/'commands'/'pm-skills-select.md').exists(): errors.append('missing root selector command')
if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-', e)
    raise SystemExit(1)
print('VALIDATION PASSED')
print(f"plugins: {len(market['plugins'])}")
