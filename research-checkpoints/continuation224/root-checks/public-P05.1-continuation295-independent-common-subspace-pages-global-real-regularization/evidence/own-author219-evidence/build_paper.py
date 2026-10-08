#!/usr/bin/env python3
"""Own small TeX/Markdown build, fixed argument arrays, shell escape disabled."""
import subprocess,pathlib,json,shutil,sys
P=pathlib.Path(__file__).resolve().parent
runs=[]
for i in [1,2,3]:
 cmd=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','P05.1-paper.tex']
 r=subprocess.run(cmd,cwd=P,capture_output=True,text=True)
 (P/f'build-pass-{i}.stdout.txt').write_text(r.stdout)
 (P/f'build-pass-{i}.stderr.txt').write_text(r.stderr)
 if (P/'P05.1-paper.log').exists():shutil.copyfile(P/'P05.1-paper.log',P/f'build-pass-{i}.tex.log')
 runs.append({'pass':i,'command':cmd,'returncode':r.returncode})
 (P/'build-runs.json').write_text(json.dumps(runs,indent=2)+'\n')
 if r.returncode:print(f'TeX pass {i} failed; logs retained.');sys.exit(r.returncode)
cmd=['pandoc','P05.1-paper.tex','--from=latex','--to=gfm','--standalone','--output=argument.md']
r=subprocess.run(cmd,cwd=P,capture_output=True,text=True)
(P/'markdown-build.stdout.txt').write_text(r.stdout);(P/'markdown-build.stderr.txt').write_text(r.stderr)
runs.append({'kind':'markdown','command':cmd,'returncode':r.returncode})
(P/'build-runs.json').write_text(json.dumps(runs,indent=2)+'\n')
print('TeX passes 1, 2 and 3 completed; all stdout, stderr and TeX logs preserved.')
print('Markdown conversion return code:',r.returncode)
sys.exit(r.returncode)
