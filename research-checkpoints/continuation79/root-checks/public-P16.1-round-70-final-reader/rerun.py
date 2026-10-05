#!/usr/bin/env python3
"""Recreate provenance, disposition, finite illustrations and the paper."""
import json
import subprocess
import sys
from pathlib import Path

root=Path(__file__).resolve().parent
logdir=root/'rerun-logs';logdir.mkdir(exist_ok=True)
records=[]
for stage in ['prepare_provenance.py','write_metadata.py','algebra_checks.py','build.py','verify.py']:
    command=[sys.executable,stage]
    p=subprocess.run(command,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    (logdir/(stage+'.stdout')).write_bytes(p.stdout)
    (logdir/(stage+'.stderr')).write_bytes(p.stderr)
    records.append({'command':command,'cwd':str(root),'returncode':p.returncode})
    (root/'execution-record.json').write_text(json.dumps({'stages':records,'success':all(r['returncode']==0 for r in records)},indent=2)+'\n')
    print(stage+': '+p.stdout.decode(errors='replace').strip())
    if p.returncode:
        print(p.stderr.decode(errors='replace'));raise SystemExit(p.returncode)
# Include the completed rerun record and output logs in the final manifest.
p=subprocess.run([sys.executable,'verify.py'],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
(logdir/'final-verification.stdout').write_bytes(p.stdout)
(logdir/'final-verification.stderr').write_bytes(p.stderr)
print('final-verification: '+p.stdout.decode(errors='replace').strip())
raise SystemExit(p.returncode)
