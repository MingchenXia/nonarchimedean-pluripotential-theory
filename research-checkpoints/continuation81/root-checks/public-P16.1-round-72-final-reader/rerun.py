from pathlib import Path
import subprocess,sys,json
root=Path(__file__).resolve().parent
report=[]
for script in ['audit_sources.py','checks.py','build.py','make_notes.py','validate.py']:
    p=subprocess.run([sys.executable,script],cwd=root,capture_output=True)
    report.append({'command':[sys.executable,script],'returncode':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')})
    Path('execution-report.json').write_text(json.dumps({'commands':report},indent=2)+'\n')
    print(p.stdout.decode(errors='replace'),end='')
    if p.returncode:
        print(p.stderr.decode(errors='replace'));raise SystemExit(p.returncode)
