#!/usr/bin/env python3
import json,pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parent
def main():
    reports=[]
    for script in ['audit_sources.py','checks.py','build.py','make_notes.py','validate.py']:
        p=subprocess.run([sys.executable,script],cwd=ROOT,capture_output=True)
        (ROOT/(script+'.stdout')).write_bytes(p.stdout)
        (ROOT/(script+'.stderr')).write_bytes(p.stderr)
        reports.append({'command':[sys.executable,script],'returncode':p.returncode,
                        'stdout':script+'.stdout','stderr':script+'.stderr'})
        print(script,p.returncode,p.stdout.decode(errors='replace').strip())
        if p.returncode:
            print(p.stderr.decode(errors='replace')); break
    (ROOT/'execution-report.json').write_text(json.dumps(reports,indent=2)+'\n')
    assert len(reports)==5 and all(r['returncode']==0 for r in reports)
if __name__=='__main__':main()
