"""Rerun preservation, source-map, exact finite checks and native compilation."""
from pathlib import Path
import hashlib,json,platform,subprocess,sys,shutil
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def command(argv,name):
    r=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    (ROOT/f'logs/{name}.stdout').write_text(r.stdout)
    (ROOT/f'logs/{name}.stderr').write_text(r.stderr)
    (ROOT/f'logs/{name}.json').write_text(json.dumps(dict(argv=argv,returncode=r.returncode),indent=2)+'\n')
    if r.returncode:raise RuntimeError((name,r.returncode,r.stdout[-1500:],r.stderr[-500:]))
    return r.stdout
raw=(ROOT/'input.json').read_bytes();j=json.loads(raw)
assert raw==(ROOT/'frozen/input-original.json').read_bytes()
assert j['task']==json.loads((ROOT/'frozen/task-original.json').read_text())
assert j['assignment']==(ROOT/'frozen/assignment-original.txt').read_text()
lines=j['assignment'].split('\n')
for u in json.loads((ROOT/'supplied/index.json').read_text()):
    p=ROOT/u['file'];text='\n'.join(lines[u['assignment_lf_start']-1:u['assignment_lf_end']])
    assert p.read_text()==text and sha(p)==u['sha256']
command([sys.executable,'extract_sources.py'],'source-extraction')
for u in json.loads((ROOT/'sources/unit-index.json').read_text()):
    assert not u['missing'];p=ROOT/u['file'];assert sha(p)==u['sha256']
    text=p.read_text().split('\n');maps=json.loads((ROOT/u['map']).read_text())
    assert len(maps)==len(text)
    for m in maps:assert text[m['local_lf']-1]==m['text']
out=command([sys.executable,'checks.py'],'finite-checks')
(ROOT/'checks-output.json').write_text(out)
result=json.loads((ROOT/'result.json').read_text());ids=[]
for note in result['notes']:
    assert note['id'] not in ids and all(s in ids for s in note['support'])
    assert set(note)=={'id','summary','detailedSummary','text','support'}
    ids.append(note['id'])
assert isinstance(result['candidate'],bool)
versions={}
for exe,arg in [('pdflatex','--version'),('pdftotext','-v')]:
    r=subprocess.run([exe,arg],capture_output=True,text=True)
    versions[exe]=(r.stdout+r.stderr).splitlines()[0]
environment=dict(python=sys.version,platform=platform.platform(),versions=versions,
                 commands={x:shutil.which(x) for x in ['python3','pdflatex','pdftotext']},
                 supervised_compute='No operator-provided service exposed; no heavy computation launched',
                 environment_variables_recorded=False,credentials_accessed=False)
(ROOT/'logs/environment.json').write_text(json.dumps(environment,indent=2)+'\n')
for passnum in [1,2]:command(['pdflatex','-interaction=nonstopmode','-halt-on-error','paper.tex'],f'latex-pass-{passnum}')
command(['pdftotext','-layout','paper.pdf','paper-rendered.txt'],'pdf-text')
summary=dict(preserved_units=16,source_units=6,finite_checks='passed',
             compilation_passes=2,paper_pdf_sha256=sha(ROOT/'paper.pdf'),candidate=result['candidate'])
(ROOT/'logs/rerun-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(ROOT/'logs/rerun-invocation.json').write_text(json.dumps(dict(argv=[sys.executable]+sys.argv,cwd=str(ROOT)),indent=2)+'\n')
manifest={str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha(p))
          for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name not in ['artifact-manifest.json']}
(ROOT/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(summary,indent=2))
