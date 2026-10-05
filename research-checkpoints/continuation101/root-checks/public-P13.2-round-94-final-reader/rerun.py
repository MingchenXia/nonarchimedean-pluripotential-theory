#!/usr/bin/env python3
"""Rerun preservation, finite diagnostics, and existing-tool paper builds."""
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
def run(args,name):
    completed=subprocess.run(args,cwd=ROOT,capture_output=True)
    (ROOT/f'{name}.stdout.log').write_bytes(completed.stdout)
    (ROOT/f'{name}.stderr.log').write_bytes(completed.stderr)
    record={'command':args,'cwd':str(ROOT),'exit_code':completed.returncode,
      'stdout':f'{name}.stdout.log','stderr':f'{name}.stderr.log'}
    if args[0].endswith('pdflatex') and (ROOT/'P13.2-paper.log').exists():
        shutil.copyfile(ROOT/'P13.2-paper.log',ROOT/f'{name}.full.log')
        record['full_tex_log']=f'{name}.full.log'
    print(json.dumps(record))
    return record

def main():
    os.chdir(ROOT)
    logs=[]
    for script in ('audit_sources.py','diagnostics.py'):
        rec=run([sys.executable,script],script.removesuffix('.py'))
        logs.append(rec)
        if rec['exit_code']:
            raise SystemExit(rec['exit_code'])
    versions={}
    for tool in ('pandoc','pdflatex','pdfinfo'):
        path=shutil.which(tool)
        versions[tool]={'path':path}
        if path:
            proc=subprocess.run([path,'--version'] if tool!='pdfinfo' else [path,'-v'],capture_output=True)
            versions[tool]['version_output']=(proc.stdout+proc.stderr).decode('utf8',errors='replace')
    environment={'python_executable':sys.executable,'python_version':sys.version,
        'platform':platform.platform(),'tools':versions,
        'supervised_compute_facility':'not exposed; no resource-heavy computation needed or launched',
        'installation_performed':False,'additional_worker_used':False}
    (ROOT/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
    if not versions['pandoc']['path'] or not versions['pdflatex']['path']:
        (ROOT/'build-output.json').write_text(json.dumps({'logs':logs,'missing_existing_tool':True},indent=2)+'\n')
        raise SystemExit('Required existing Pandoc/pdfTeX tool is absent; no installation attempted.')
    rec=run([versions['pandoc']['path'],'argument.md','--standalone','--from=markdown+tex_math_single_backslash',
             '--to=latex','--output=P13.2-paper.tex'],'pandoc-build')
    logs.append(rec)
    if rec['exit_code']:
        raise SystemExit(rec['exit_code'])
    for passnum in (1,2):
        rec=run([versions['pdflatex']['path'],'-interaction=nonstopmode','-halt-on-error',
                 '-file-line-error','P13.2-paper.tex'],f'pdftex-pass{passnum}')
        logs.append(rec)
        if rec['exit_code']:
            (ROOT/'build-output.json').write_text(json.dumps({'logs':logs,'success':False},indent=2)+'\n')
            raise SystemExit(rec['exit_code'])
    if versions['pdfinfo']['path']:
        logs.append(run([versions['pdfinfo']['path'],'P13.2-paper.pdf'],'pdfinfo'))
    registered=run([sys.executable,'register_notes.py'],'register-notes')
    logs.append(registered)
    if registered['exit_code']:
        raise SystemExit(registered['exit_code'])
    artifacts={}
    for filename in ('argument.md','P13.2-paper.tex','P13.2-paper.pdf'):
        data=(ROOT/filename).read_bytes()
        artifacts[filename]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    result={'success':True,'logs':logs,'artifacts':artifacts,
       'documentary_only':True,'mathematical_acceptance':False}
    (ROOT/'build-output.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':
    main()
