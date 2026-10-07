"""Build this author's argument only; use installed tools, with no shell escape."""
from pathlib import Path
import hashlib, json, platform, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parent
HISTORY=ROOT/'build-runs'
HISTORY.mkdir(exist_ok=True)
RUN=HISTORY/('run-'+str(len(list(HISTORY.iterdir()))+1).zfill(2))
RUN.mkdir()
commands=[]
def run(argv, stem):
    p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    (ROOT/(stem+'.stdout')).write_text(p.stdout)
    (ROOT/(stem+'.stderr')).write_text(p.stderr)
    (RUN/(stem+'.stdout')).write_text(p.stdout)
    (RUN/(stem+'.stderr')).write_text(p.stderr)
    commands.append({'argv':argv,'cwd':str(ROOT),'exit_code':p.returncode,
                     'stdout':stem+'.stdout','stderr':stem+'.stderr'})
    (ROOT/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    (RUN/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    if p.returncode:
        print(p.stdout[-5000:]);print(p.stderr[-2000:]);sys.exit(p.returncode)

for name in ('pandoc','pdflatex'):
    if not shutil.which(name):
        raise SystemExit('Required existing compiler capability absent: '+name)
run(['pandoc','--from=markdown+tex_math_single_backslash','P16.4-argument.md','--standalone','--number-sections','-o','P16.4-paper.tex'],'pandoc')
for i in (1,2):
    run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P16.4-paper.tex'],f'pdflatex-pass{i}')
log=(ROOT/'P16.4-paper.log').read_text(errors='replace')
diagnostics=[l for l in log.splitlines() if any(w in l for w in
             ('Warning:','Overfull','Underfull','! '))]
result={'status':'local build completed','exit_codes':[x['exit_code'] for x in commands],
        'shell_escape':False,'diagnostics':diagnostics,
        'builtin_compiler':'Separate operator action; not invoked or certified here',
        'mathematical_acceptance':False}
(ROOT/'build-result.json').write_text(json.dumps(result,indent=2)+'\n')
(RUN/'build-result.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ('P16.4-paper.log','P16.4-paper.tex'):
    shutil.copy2(ROOT/name,RUN/name)
print(json.dumps(result,indent=2))
