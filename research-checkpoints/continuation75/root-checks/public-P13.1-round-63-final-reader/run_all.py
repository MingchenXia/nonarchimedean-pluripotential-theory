"""Rerun light audit/diagnostics and twice compile using already installed tools."""
from pathlib import Path
import subprocess,json,sys
records=[]
for script in ['audit_sources.py','checks.py','build.py','make_notes.py','validate.py']:
    command=[sys.executable,script]
    result=subprocess.run(command,text=True,capture_output=True)
    stem=script.removesuffix('.py')
    Path(stem+'.stdout').write_text(result.stdout);Path(stem+'.stderr').write_text(result.stderr)
    records.append({'command':command,'returncode':result.returncode,'stdout':stem+'.stdout','stderr':stem+'.stderr'})
    Path('run-report.json').write_text(json.dumps({'commands':records,'scope':'Reproducibility only, not mathematical verification.'},indent=2)+'\n')
    if result.returncode:
        print(result.stdout,result.stderr);sys.exit(result.returncode)
print(json.dumps({'successful_commands':len(records),'math_verification':False}))
