#!/usr/bin/env python3
from pathlib import Path
import subprocess,json
ROOT=Path(__file__).resolve().parent
records=[]
for stage in ['prepare_provenance.py','build.py','verify.py','write_notes.py']:
 command=['python3',stage];r=subprocess.run(command,cwd=ROOT,capture_output=True)
 (ROOT/f'{stage}.stdout.txt').write_bytes(r.stdout);(ROOT/f'{stage}.stderr.txt').write_bytes(r.stderr)
 records.append({'command':command,'returncode':r.returncode,'stdout':f'{stage}.stdout.txt','stderr':f'{stage}.stderr.txt'})
 print(r.stdout.decode('utf-8',errors='replace').strip())
 if r.returncode:
  print(r.stderr.decode('utf-8',errors='replace'))
  (ROOT/'rerun-results.json').write_text(json.dumps(records,indent=2)+'\n');raise SystemExit(r.returncode)
(ROOT/'rerun-results.json').write_text(json.dumps(records,indent=2)+'\n')
