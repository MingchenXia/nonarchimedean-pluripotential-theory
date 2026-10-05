#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,hashlib,datetime
ROOT=Path(__file__).resolve().parent
commands=[['pandoc','P16.1-argument.md','--from=markdown+tex_math_dollars','--standalone','--to=latex','--pdf-engine=pdflatex','-V','documentclass=article','-V','geometry:margin=1in','-V','fontsize=10pt','-V','colorlinks=true','-o','P16.1-paper.tex'],['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.1-paper.tex'],['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.1-paper.tex']]
records=[]
for i,command in enumerate(commands):
 name='pandoc' if i==0 else f'tex-run-{i}'
 r=subprocess.run(command,cwd=ROOT,capture_output=True)
 (ROOT/f'{name}.stdout.txt').write_bytes(r.stdout);(ROOT/f'{name}.stderr.txt').write_bytes(r.stderr)
 if i and (ROOT/'P16.1-paper.log').exists():
  (ROOT/f'{name}.log').write_bytes((ROOT/'P16.1-paper.log').read_bytes())
 records.append({'command':command,'returncode':r.returncode,'stdout':f'{name}.stdout.txt','stderr':f'{name}.stderr.txt','tex_log':f'{name}.log' if i else None})
 if r.returncode:
  (ROOT/'build-results.json').write_text(json.dumps(records,indent=2)+'\n')
  print(r.stdout.decode('utf-8',errors='replace')[-4500:]);raise SystemExit(r.returncode)
(ROOT/'build-results.json').write_text(json.dumps(records,indent=2)+'\n')
info=subprocess.run(['pdfinfo','P16.1-paper.pdf'],cwd=ROOT,capture_output=True)
(ROOT/'pdfinfo.stdout.txt').write_bytes(info.stdout);(ROOT/'pdfinfo.stderr.txt').write_bytes(info.stderr)
versions={}
for tool in ['pandoc','pdflatex']:
 r=subprocess.run([tool,'--version'],cwd=ROOT,capture_output=True)
 versions[tool]=r.stdout.decode('utf-8',errors='replace').splitlines()[:3]
(ROOT/'tool-versions.json').write_text(json.dumps(versions,indent=2)+'\n')
print(json.dumps({'runs':len(records),'all_returncodes_zero':True,'pdf_sha256':hashlib.sha256((ROOT/'P16.1-paper.pdf').read_bytes()).hexdigest()}))
