from pathlib import Path
import subprocess,sys,json,hashlib
ROOT=Path(__file__).resolve().parent;logs=ROOT/'execution-logs';logs.mkdir(exist_ok=True)
report=[]
for script in ['audit_sources.py','checks.py','build.py','make_notes.py','validate.py']:
 cmd=[sys.executable,script]
 p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
 (logs/f'{script}.stdout').write_text(p.stdout);(logs/f'{script}.stderr').write_text(p.stderr)
 report.append({'command':cmd,'cwd':str(ROOT),'returncode':p.returncode,'stdout':str((logs/f'{script}.stdout').relative_to(ROOT)),'stderr':str((logs/f'{script}.stderr').relative_to(ROOT))})
 print(script,p.returncode,p.stdout[:250].strip())
 if p.returncode:
  print(p.stderr);break
final={'commands':report,'success':len(report)==5 and all(x['returncode']==0 for x in report),'compute':'Light exact finite grids, source hashing and document compilation only. No supervised compute facility exposed or needed.','limits':'All mathematical claims remain unverified drafts; successful execution is not mathematical validation.'}
(ROOT/'execution-report.json').write_text(json.dumps(final,indent=2)+'\n')
raise SystemExit(0 if final['success'] else 1)
