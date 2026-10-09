from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat();results=[]
for paper,label,tex in [(404,'public-P16.7-continuation404-finite-extension-and-unbounded-probe-currents-unreviewed','standalone.tex'),(405,'public-P12.3-continuation405-excellent-germ-contact-and-nonmonomial-envelopes-unreviewed','P12.3-contact-envelopes.tex')]:
    d=K/label;p=d/tex;b=d/'ROOT-whole-proof-source-scope-and-binding.json';v=load(b)
    assert v['compiler']['kind']=='pending' and not v['accepted'] and not v['original_closed']
    for e in v['public_files']:assert sha(Path(e['path']))==e['sha256']
    rec=dict(recorded_utc=now,paper=paper,path=str(p),sha256=sha(p),kind='success',message="The current source compiled successfully with the desktop editor's compiler.",tool='codex_app.compile_latex_document',actual_result_observed=True,native_identical_source_success=True,mathematical_certification=False,protected_editor_OPEN_UNCHANGED=True,UNREVIEWED=True,accepted=False,original_closed=False)
    q=K/f'ROOT{paper}-native-editor-compiler-success-20261009.json';write(q,rec);write(d/q.name,rec)
    scope=d/'ROOT-review-scope.md';s=scope.read_text();assert s.count('Compiler pending.')==1;scope.write_text(s.replace('Compiler pending.','Whole standalone compiled successfully with the built-in editor compiler; native mathematical body is unchanged.'))
    v.update(recorded_utc=now,compiler=rec,public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(d.iterdir()) if p.is_file() and p!=b]);write(b,v)
    results.append(dict(paper=paper,source=str(p),sha256=sha(p),kind='success',files=len(v['public_files'])+1))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,ROOT404405_actual_compiler_success=results,next_work='Freeze282 whole revised402403 plus404 actual generated uniqueness audit and compactness/existence residual; freeze283 whole405 excellent-germ contact and arbitrary P12.3 residual. Regular NONFORCE checkpoint289 with whole404405/revised402403. Counts unchanged.')
    write(p,x)
print(json.dumps(dict(whole_standalones=results,solved=16,open=26,accepted_papers=97),indent=2))
