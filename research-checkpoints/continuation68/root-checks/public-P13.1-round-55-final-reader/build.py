"""Use existing tools; preserve actual output and separate TeX logs for two passes."""
from pathlib import Path
import hashlib
import json
import platform
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parent
report={'platform':platform.platform(),'python':platform.python_version(),
        'commands':[],'tools':{},'artifacts':{}}

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def run(command, stem):
    start=time.time()
    proc=subprocess.run(command,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (ROOT/f'{stem}.stdout.txt').write_bytes(proc.stdout)
    (ROOT/f'{stem}.stderr.txt').write_bytes(proc.stderr)
    report['commands'].append({'argv':command,'returncode':proc.returncode,
                              'stdout':f'{stem}.stdout.txt','stderr':f'{stem}.stderr.txt',
                              'elapsed_seconds':time.time()-start})
    return proc.returncode

for name in ['pandoc','pdflatex']:
    exe=shutil.which(name)
    assert exe, f'Missing existing tool: {name}'
    proc=subprocess.run([exe,'--version'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (ROOT/f'{name}-version.stdout.txt').write_bytes(proc.stdout)
    (ROOT/f'{name}-version.stderr.txt').write_bytes(proc.stderr)
    report['tools'][name]={'path':exe,'version_returncode':proc.returncode,
                           'version_stdout':f'{name}-version.stdout.txt',
                           'version_stderr':f'{name}-version.stderr.txt'}

assert (ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes()
command=[report['tools']['pandoc']['path'],'P13.1-argument.md','--from=markdown',
         '--to=latex','--standalone','--number-sections','--pdf-engine=pdflatex',
         '-V','colorlinks=true','-o','P13.1-paper.tex']
rc=run(command,'pandoc-conversion')
if rc==0:
    for num in [1,2]:
        rc=run([report['tools']['pdflatex']['path'],'-interaction=nonstopmode',
                '-halt-on-error','-file-line-error','P13.1-paper.tex'],f'tex-pass-{num}')
        log=ROOT/'P13.1-paper.log'
        if log.exists():
            shutil.copyfile(log,ROOT/f'tex-pass-{num}.log')
            report['commands'][-1]['tex_log']=f'tex-pass-{num}.log'
        if rc:
            break

for name in ['input.json','input-original.json','assignment-original.txt','task-original.json',
             'P13.1-argument.md','P13.1-paper.tex','P13.1-paper.pdf',
             'checks.py','checks-output.json','audit_sources.py',
             'source-extracts/source-provenance.json']:
    p=ROOT/name
    if p.exists(): report['artifacts'][name]={'sha256':digest(p),'bytes':p.stat().st_size}
report['input_original_byte_identical']=True
report['two_successful_tex_passes']=sum(c['returncode']==0 and c['argv'][0]==report['tools']['pdflatex']['path']
                                      for c in report['commands'])==2
report['mathematical_correctness_established_by_build']=False
(ROOT/'build-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'returncode':rc,'two_successful_tex_passes':report['two_successful_tex_passes'],
                  'report':'build-report.json'},indent=2))
raise SystemExit(rc)
