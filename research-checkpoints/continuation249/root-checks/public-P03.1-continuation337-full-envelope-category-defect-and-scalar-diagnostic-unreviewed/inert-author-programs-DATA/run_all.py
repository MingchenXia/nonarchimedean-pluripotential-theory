"""Owned, bounded sequential rerun and exact command/output recording."""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parent

def main():
    (ROOT/'evidence').mkdir(exist_ok=True)
    steps=[('prepare_evidence.py','prepare-output.txt'),
           ('diagnostics.py','diagnostics-output.txt'),
           ('build_artifacts.py','build-output.txt'),
           ('make_notes.py','notes-output.txt'),
           ('check_artifacts.py','check-output.txt')]
    records=[]
    for program, filename in steps:
        cmd=[sys.executable,program]
        start=datetime.now(timezone.utc).isoformat()
        run=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,timeout=60)
        output=ROOT/'evidence'/filename
        output.write_text(run.stdout+run.stderr)
        records.append({'command':cmd,'cwd':str(ROOT),'started_utc':start,
                        'exit_code':run.returncode,'output':str(output.relative_to(ROOT))})
        print(program+': '+run.stdout.strip())
        if run.returncode:
            print(run.stderr)
            break
    (ROOT/'evidence'/'execution.json').write_text(json.dumps({'runs':records,
                   'max_seconds_per_step':60,'supplied_executables_used':False,
                   'mathematical_correctness_certified':False},indent=2)+'\n')
    if len(records)!=len(steps) or any(row['exit_code'] for row in records):
        sys.exit(1)

if __name__=='__main__':
    main()
