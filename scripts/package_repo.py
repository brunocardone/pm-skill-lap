#!/usr/bin/env python3
from pathlib import Path
import zipfile, subprocess, sys
root = Path(__file__).resolve().parents[1]
subprocess.check_call([sys.executable, str(root/'scripts'/'validate_repo.py')])
dist = root/'dist'
dist.mkdir(exist_ok=True)
out = dist/'pm-skill-lap-repo.zip'
if out.exists(): out.unlink()
with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for path in root.rglob('*'):
        if '.git' in path.parts or path == out: continue
        if path.is_file(): z.write(path, path.relative_to(root.parent))
print(out)
