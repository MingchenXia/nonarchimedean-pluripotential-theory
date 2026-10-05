#!/usr/bin/env python3
"""Offline reproduction using retained inputs and already-installed programs."""
import datetime, hashlib, json, os, platform, shutil, subprocess, sys, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
LOGS=ROOT/'logs';LOGS.mkdir(exist_ok=True)
commands=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(path,x): (ROOT/path).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def run(argv,label):
    p=subprocess.run(argv,cwd=ROOT,capture_output=True)
    (LOGS/f'{label}.stdout').write_bytes(p.stdout)
    (LOGS/f'{label}.stderr').write_bytes(p.stderr)
    commands.append({'argv':argv,'cwd':str(ROOT),'exit_code':p.returncode,'stdout':f'logs/{label}.stdout','stderr':f'logs/{label}.stderr'})
    dump('commands.json',commands)
    if p.returncode:raise RuntimeError(f'{label} returned {p.returncode}; complete outputs retained')
    return p

raw=(ROOT/'input.json').read_bytes();preserved=(ROOT/'input-original.json').read_bytes()
assert raw==preserved
inp=json.loads(raw)
assert json.loads((ROOT/'task-original.json').read_bytes())==inp['task']
assert (ROOT/'assignment-original.txt').read_text()==inp['assignment']
records=json.loads((ROOT/'source-files.json').read_bytes())
for record in records:
    b=(ROOT/record['path']).read_bytes()
    assert sha(b)==record['sha256'] and len(b)==record['bytes'],record['path']
dump('preservation-check.json',{'input_bytes':len(raw),'input_sha256':sha(raw),'byte_identical':True,'task_equal':True,'assignment_equal':True,'primary_files_verified':len(records)})
env={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'working_directory':str(ROOT),'installed_programs':{},'supervised_compute':'No operator-provided supervised facility exposed; no resource-heavy computation run.'}
for name in ['pandoc','pdflatex','pdfinfo','pdftotext']:
    exe=shutil.which(name);assert exe,name
    arg=[exe,'--version'] if name in ['pandoc','pdflatex'] else [exe,'-v']
    p=subprocess.run(arg,capture_output=True)
    env['installed_programs'][name]={'path':exe,'version':(p.stdout+p.stderr).decode(errors='replace').split('\n')[0]}
dump('environment-rerun.json',env)
run([sys.executable,'make_evidence.py'],'evidence')
run([sys.executable,'finite_checks.py'],'finite-checks')
argument=(ROOT/'argument.md').read_text(encoding='utf8')
# Only the paper typography is normalized; the exact original task remains byte-preserved.
mapping={'µ':'mu','Σ':'Sigma','θ':'theta','α':'alpha','ω':'omega','ϕ':'phi','ψ':'psi','ν':'nu','π':'pi','∈':' in ','≥':'>=','≤':'<=','−':'-','×':' x ','∞':'infinity','∅':'empty','ℝ':'R','ℂ':'C'}
def ascii_typography(s):
    for a,b in mapping.items():s=s.replace(a,b)
    return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().replace('\\','\\\\')
task_appendix='\n## Unchanged original mathematical task and full family\n\nThis appendix reproduces the original task with typographic ASCII normalization for pdfTeX. The authoritative exact text and JSON value are preserved in `input-original.json` and `task-original.json`. No mathematical condition has been replaced.\n\n'+ascii_typography(inp['task']['problem'])+'\n\n**Exact completion criterion (typography normalized).** '+ascii_typography(inp['task']['completionCriteria'])+'\n'
manuscript=argument+'\n'+(ROOT/'primary-index.md').read_text()+task_appendix
(ROOT/'manuscript-full.md').write_text(manuscript,encoding='utf8')
run([env['installed_programs']['pandoc']['path'],'--standalone','manuscript-full.md','-o','P16.1-paper.tex'],'pandoc')
for number in [1,2]:
    run([env['installed_programs']['pdflatex']['path'],'-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex'],f'pdflatex-pass{number}')
    shutil.copyfile(ROOT/'P16.1-paper.log',LOGS/f'pdflatex-pass{number}.log')
run([env['installed_programs']['pdfinfo']['path'],'P16.1-paper.pdf'],'pdfinfo')
run([env['installed_programs']['pdftotext']['path'],'-layout','P16.1-paper.pdf','proof-rendered.txt'],'pdftotext')
run([sys.executable,'make_notes.py'],'notes')
run([sys.executable,'validate.py'],'validation')
excluded={'artifact-manifest.json'}
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name not in excluded and '.git' not in p.parts:
        b=p.read_bytes();manifest.append({'file':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha(b)})
dump('artifact-manifest.json',manifest)
print(json.dumps({'status':'documentary checks passed','input_sha256':sha(raw),'primary_files':len(records),'artifact_files':len(manifest),'pdf_sha256':sha((ROOT/'P16.1-paper.pdf').read_bytes()),'candidate':False}))
