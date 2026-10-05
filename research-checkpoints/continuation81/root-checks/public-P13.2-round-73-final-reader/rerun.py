import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def main():
    records=[]
    for script in ['audit_sources.py','checks.py','build.py','make_notes.py','validate.py']:
        args=[sys.executable,script]
        result=subprocess.run(args,cwd=ROOT,capture_output=True)
        (ROOT/(script+'.stdout')).write_bytes(result.stdout)
        (ROOT/(script+'.stderr')).write_bytes(result.stderr)
        records.append({'command':args,'returncode':result.returncode,
                        'stdout_file':script+'.stdout','stderr_file':script+'.stderr'})
        if result.returncode:
            (ROOT/'execution-report.json').write_text(json.dumps(records,indent=2)+'\n')
            raise SystemExit(result.returncode)
    (ROOT/'execution-report.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps({'status':'passed','steps':len(records),'candidate':False},indent=2))

if __name__=='__main__':main()
