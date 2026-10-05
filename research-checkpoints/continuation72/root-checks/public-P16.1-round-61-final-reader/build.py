from pathlib import Path
import json
import subprocess
import shutil

root = Path(__file__).resolve().parent
existing = [root/p for p in ['build-results.json','pandoc.stdout.txt','pandoc.stderr.txt','tex-run-1.stdout.txt','tex-run-1.stderr.txt','tex-run-1.log','tex-run-2.stdout.txt','tex-run-2.stderr.txt','tex-run-2.log'] if (root/p).exists()]
if existing:
    history = root/'build-history'
    history.mkdir(exist_ok=True)
    index = 1
    while (history/f'build-{index}').exists(): index += 1
    dest = history/f'build-{index}'
    dest.mkdir()
    for path in existing: shutil.copyfile(path,dest/path.name)
commands = [
 ['pandoc','P16.1-argument.md','--standalone','--from=markdown+tex_math_dollars','--to=latex','--number-sections','--variable=geometry:margin=1in','--variable=fontsize:11pt','--include-in-header=tex-header.tex','-o','P16.1-paper.tex'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex'],
]
records = []
for i,cmd in enumerate(commands):
    name = 'pandoc' if i == 0 else f'tex-run-{i}'
    p = subprocess.run(cmd,cwd=root,capture_output=True)
    (root/f'{name}.stdout.txt').write_bytes(p.stdout)
    (root/f'{name}.stderr.txt').write_bytes(p.stderr)
    if i:
        logfile = root/'P16.1-paper.log'
        if logfile.exists():
            (root/f'{name}.log').write_bytes(logfile.read_bytes())
    records.append({'command':cmd,'returncode':p.returncode,'stdout':f'{name}.stdout.txt','stderr':f'{name}.stderr.txt','tex_log':f'{name}.log' if i else None})
    print(name,p.returncode)
    if p.returncode:
        (root/'build-results.json').write_text(json.dumps(records,indent=2)+'\n')
        raise SystemExit(p.returncode)
(root/'build-results.json').write_text(json.dumps(records,indent=2)+'\n')
