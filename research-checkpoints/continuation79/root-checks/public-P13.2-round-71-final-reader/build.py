"""Produce a standalone TeX paper, then retain two distinct compilation logs."""
from pathlib import Path
import json
import platform
import re
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
commands=[]
def run(label,argv):
    r=subprocess.run(argv,cwd=ROOT,capture_output=True)
    (ROOT/f'{label}.stdout').write_bytes(r.stdout)
    (ROOT/f'{label}.stderr').write_bytes(r.stderr)
    commands.append({'label':label,'argv':argv,'returncode':r.returncode})
    if r.returncode:
        print(r.stdout.decode(errors='replace')[-5000:])
        print(r.stderr.decode(errors='replace')[-2000:])
        raise RuntimeError(f'{label} failed')
    return r

environment={'python':sys.version,'platform':platform.platform(),
             'executables':{q:shutil.which(q) for q in ['python','pandoc','pdflatex','pdftotext']},
             'resource_policy':'Light source hashing, exact arithmetic and existing TeX only. No heavy computation.'}
for q in ['pandoc','pdflatex']:
    r=subprocess.run([q,'--version'],capture_output=True,cwd=ROOT)
    environment[q+'_version']=r.stdout.decode(errors='replace').split('\n')[0]
(ROOT/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
run('pandoc',['pandoc','P13.2-argument.md','--standalone','--from=markdown+tex_math_dollars',
              '--to=latex','--output=P13.2-paper.tex'])
tex_path=ROOT/'P13.2-paper.tex'
tex=tex_path.read_text()
def wrap_long_code(m):
    value=m.group(1)
    if len(value)>50 and re.fullmatch(r'[A-Za-z0-9/_.-]+',value):
        return r'\nolinkurl{'+value+'}'
    return m.group(0)
tex=re.sub(r'\\texttt\{([^{}]+)\}',wrap_long_code,tex)
tex_path.write_text(tex)
for i in [1,2]:
    run(f'tex-pass-{i}',['pdflatex','-interaction=nonstopmode','-halt-on-error',
                        '-file-line-error','P13.2-paper.tex'])
    shutil.copyfile(ROOT/'P13.2-paper.log',ROOT/f'tex-pass-{i}.log')
report={'commands':commands,'deterministic_TeX_postprocess':'Long literal paths and SHA256 strings use nolinkurl to permit line breaks without changing characters.',
        'two_TeX_passes_succeeded':True,
        'mathematical_certification':False}
(ROOT/'build-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
