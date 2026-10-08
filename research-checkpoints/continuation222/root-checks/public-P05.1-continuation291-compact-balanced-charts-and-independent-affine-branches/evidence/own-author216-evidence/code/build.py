"""Fresh local no-shell-escape build; source bytes are checked before and after."""
from pathlib import Path
import hashlib,json,subprocess,shutil,platform
source=Path('P05.1-paper.tex')
before=hashlib.sha256(source.read_bytes()).hexdigest()
commands=[]
for i in [1,2]:
    cmd=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex']
    p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    Path(f'logs/build-pass-{i}.log').write_text(p.stdout)
    commands.append({'argv':cmd,'exit_code':p.returncode,'log':f'logs/build-pass-{i}.log'})
    if p.returncode:break
if all(x['exit_code']==0 for x in commands):
    cmd=['pandoc','-f','latex','-t','gfm','--wrap=none','P05.1-paper.tex','-o','argument.md']
    p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    Path('logs/pandoc.log').write_text(p.stdout)
    commands.append({'argv':cmd,'exit_code':p.returncode,'log':'logs/pandoc.log'})
after=hashlib.sha256(source.read_bytes()).hexdigest()
assert before==after
warnings=[]
for c in commands:
    for line in Path(c['log']).read_text().splitlines():
        if any(k in line for k in ['Warning','Overfull','Underfull','undefined','Error']):warnings.append(line)
report={'commands':commands,'source_sha256_before':before,'source_sha256_after':after,
        'source_unchanged':before==after,'warnings':warnings,
        'python':platform.python_version(),
        'visible_tool_paths':{t:shutil.which(t) for t in ['pdflatex','pandoc']},
        'mathematical_certification':False,'operator_native_invocation_certified_by_child':False}
Path('evidence/build-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'exit_codes':[c['exit_code'] for c in commands], 'source_unchanged':True,'warnings':len(warnings)}))
