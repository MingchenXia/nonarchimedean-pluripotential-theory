#!/usr/bin/env python3
"""Convert the draft and compile twice, keeping every process output/log."""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

out=Path('build-logs'); out.mkdir(exist_ok=True)
header=Path('paper-header.tex')
header.write_text('\\usepackage{amsmath,amssymb}\n\\setlength{\\emergencystretch}{3em}\n')
commands=[
 [shutil.which('pandoc'), 'P16.1-argument.md', '--standalone', '--from=markdown+tex_math_dollars', '--to=latex', '--include-in-header=paper-header.tex', '-V','documentclass=article','-V','geometry:margin=1in','-V','fontsize=10pt','-o','P16.1-paper.tex'],
 [shutil.which('pdflatex'),'-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.1-paper.tex'],
 [shutil.which('pdflatex'),'-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.1-paper.tex'],
]
results=[]
for i,command in enumerate(commands):
    label='pandoc' if i==0 else f'tex-run-{i}'
    p=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    (out/f'{label}.stdout').write_bytes(p.stdout)
    (out/f'{label}.stderr').write_bytes(p.stderr)
    (out/f'{label}.command.json').write_text(json.dumps(command,indent=2)+'\n')
    if i>0 and Path('P16.1-paper.log').exists():
        shutil.copyfile('P16.1-paper.log',out/f'{label}.log')
    results.append({'stage':label,'command':command,'returncode':p.returncode})
    if p.returncode:
        Path('build-results.json').write_text(json.dumps({'runs':results,'success':False},indent=2)+'\n')
        print(json.dumps(results[-1])); raise SystemExit(p.returncode)
pdf=Path('P16.1-paper.pdf')
info=subprocess.run([shutil.which('pdfinfo'),str(pdf)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(out/'pdfinfo.stdout').write_bytes(info.stdout); (out/'pdfinfo.stderr').write_bytes(info.stderr)
pages=[line for line in info.stdout.decode().splitlines() if line.startswith('Pages:')]
versions={}
for tool in ['pandoc','pdflatex','pdfinfo']:
    flag='--version' if tool!='pdfinfo' else '-v'
    p=subprocess.run([shutil.which(tool),flag],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    versions[tool]=(p.stdout+p.stderr).decode(errors='replace').splitlines()[0]
result={'runs':results,'success':True,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_pages':int(pages[0].split()[1]) if pages else None,'tool_versions':versions,
 'standalone_tex_sha256':hashlib.sha256(Path('P16.1-paper.tex').read_bytes()).hexdigest(),
 'epistemic_status':'Compilation certifies document execution only.'}
Path('build-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'success':True,'runs':len(results),'pdf_pages':result['pdf_pages']}))
