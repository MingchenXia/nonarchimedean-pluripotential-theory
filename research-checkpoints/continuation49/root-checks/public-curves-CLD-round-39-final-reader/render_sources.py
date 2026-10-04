#!/usr/bin/env python3
"""Rerun the three PDF inspections; retain exact commands and renderer output."""
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PUBLIC=Path('/workspace/research/shared-sources')
ITEMS=[('Thu','Thuillier-tel-00010990v1.pdf',76),
       ('CD','CD-1204.6277v2-20261004.pdf',196),
       ('GJR','GJR-2111.05741.pdf',80)]

def main():
    records=[]
    for ident,file,page in ITEMS:
        prefix=f'source-extracts/{ident}-pdf{page}'
        cmd=['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1600','-png','-singlefile',str(PUBLIC/file),prefix]
        r=subprocess.run(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=60)
        out=prefix+'-render.stdout.txt'; (ROOT/out).write_text(r.stdout)
        records.append({'command':cmd,'exit_code':r.returncode,'stdout_file':out,'image':prefix+'.png',
                        'warning_count':len([x for x in r.stdout.splitlines() if 'Warning' in x])})
    (ROOT/'source-extracts/render-diagnostics.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps({'rendered':len(records),'exit_codes':[r['exit_code'] for r in records],
                      'warning_counts':[r['warning_count'] for r in records]}))

if __name__=='__main__':main()
