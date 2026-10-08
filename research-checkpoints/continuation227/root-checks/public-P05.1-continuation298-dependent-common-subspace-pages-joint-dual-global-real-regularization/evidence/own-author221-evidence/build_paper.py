#!/usr/bin/env python3
"""Build only this author's fixed TeX; preserve initial logs; no shell execution."""
import hashlib, json, platform, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
assert Path.cwd().resolve()==ROOT
source=ROOT/'P05.1-paper.tex'
initial=hashlib.sha256(source.read_bytes()).hexdigest()
DEST=ROOT
if (ROOT/'build-report.json').exists():
    index=1
    while (ROOT/f'build-rerun-{index}').exists():index+=1
    DEST=ROOT/f'build-rerun-{index}';DEST.mkdir()
env={'python':sys.version,'platform':platform.platform(),'tools':{},'source_sha256':initial,'shell_escape':False,'model_attestation':'Unavailable; caller-requested configuration is not independently attested.'}
for name,args in [('pdflatex',['--version']),('pandoc',['--version'])]:
    exe=shutil.which(name); assert exe, name
    cp=subprocess.run([exe]+args,cwd=ROOT,text=True,capture_output=True,check=False)
    env['tools'][name]={'path':exe,'version_lines':(cp.stdout+cp.stderr).splitlines()[:3]}
(DEST/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
steps=[]
commands=[('pandoc',[shutil.which('pandoc'),'-f','latex','-t','markdown','P05.1-paper.tex','-o','argument.md'])]
commands += [(f'tex-pass-{p}',[shutil.which('pdflatex'),'-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex']) for p in [1,2,3]]
for label,argv in commands:
    cp=subprocess.run(argv,cwd=ROOT,text=True,capture_output=True,check=False)
    (DEST/(label+'.stdout.log')).write_text(cp.stdout)
    (DEST/(label+'.stderr.log')).write_text(cp.stderr)
    if label.startswith('tex') and (ROOT/'P05.1-paper.log').exists():
        shutil.copyfile(ROOT/'P05.1-paper.log',DEST/(label+'.engine.log'))
    warnings=[line for line in (cp.stdout+cp.stderr).splitlines() if any(x in line for x in ['Warning','Overfull','Underfull','Undefined','Error'])]
    steps.append({'label':label,'argv':argv,'returncode':cp.returncode,'warnings':warnings})
    if cp.returncode: break
assert hashlib.sha256(source.read_bytes()).hexdigest()==initial
(DEST/'build-report.json').write_text(json.dumps({'source_unchanged':True,'source_sha256':initial,'steps':steps},indent=2)+'\n')
print(json.dumps({'log_directory':str(DEST.relative_to(ROOT)),'source_unchanged':True,'steps':steps},indent=2))
if any(s['returncode'] for s in steps):sys.exit(1)
