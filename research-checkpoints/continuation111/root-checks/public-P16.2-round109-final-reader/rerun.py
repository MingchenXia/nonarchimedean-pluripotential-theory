"""Rebuild local research artifacts without network, installations, or external reads."""
import datetime
import hashlib
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LOG=ROOT/'logs'; LOG.mkdir(exist_ok=True)
commands=[]

def run(argv,name):
    p=subprocess.run(argv,cwd=ROOT,text=True,capture_output=True)
    (LOG/(name+'.stdout')).write_text(p.stdout)
    (LOG/(name+'.stderr')).write_text(p.stderr)
    record=dict(argv=argv,exit_code=p.returncode,stdout=str((LOG/(name+'.stdout')).relative_to(ROOT)),stderr=str((LOG/(name+'.stderr')).relative_to(ROOT)))
    commands.append(record)
    (LOG/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    if p.returncode:
        print(p.stderr[-3000:]); print(p.stdout[-3000:])
        raise SystemExit(f'{name}: exit {p.returncode}')

environment=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),python=sys.version,
                 platform=platform.platform(),machine=platform.machine(),cwd=str(ROOT),
                 tools={t:shutil.which(t) for t in ['python3','pandoc','pdflatex','curl','pdftotext']},
                 supervised_compute='No facility exposed; no heavy computation required or run.',
                 restrictions='Only supplied workspace read/written; no private environment/config/auth inspected; no workers or Active105 inspected.')
(LOG/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
for t in ['pandoc','pdflatex']:
    run([t,'--version'],t+'-version')
run([sys.executable,'extract_input.py'],'extract')
run([sys.executable,'build_ledger.py'],'ledger')
run([sys.executable,'diagnostics.py'],'diagnostics')

status=json.loads((ROOT/'status.json').read_text())
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
notes=json.loads((ROOT/'notes.json').read_text())
assert notes['candidate'] is False and 0 < len(notes['notes']) <= 4
seen=set()
for n in notes['notes']:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    assert n['id'] not in seen
    assert all(s in seen for s in n['support'])
    seen.add(n['id'])
run(['pandoc','paper.md','--standalone','--table-of-contents','--from','markdown+tex_math_single_backslash','--to','latex','--output','P16.2-paper.tex'],'pandoc')
for i in [1,2]:
    run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.2-paper.tex'],f'pdflatex-{i}')
if 'Label(s) may have changed' in (LOG/'pdflatex-2.stdout').read_text():
    run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.2-paper.tex'],'pdflatex-3')
run(['pdftotext','P16.2-paper.pdf','P16.2-paper-rendered.txt'],'pdftotext')
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='manifest.json' and '.git' not in p.parts]
manifest=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),candidate=False,
              warning='Execution, literal hashes, compilation, and finite diagnostics are not mathematical proof certificates.',
              files=[dict(file=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(files)])
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(candidate=False,paper='P16.2-paper.pdf',status=status,artifact_files=len(files)),indent=2))
