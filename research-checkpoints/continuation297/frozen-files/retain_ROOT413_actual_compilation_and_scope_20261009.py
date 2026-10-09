from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
D=K/'public-P12.3-continuation413-algebraic-field-and-Frobenius-root-envelope-descent-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
B=D/'ROOT-whole-proof-source-scope-and-binding.json';b=load(B)
assert b['compiler']['kind']=='pending' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
P=D/'P12.3-algebraic-descent-envelopes.tex'
assert sha(P)=='e90056cbc192c33006332554b3e82a8b3390f566dcc9687b2aa6ce9b75a20263'
now=datetime.now(timezone.utc).isoformat()
rec=dict(recorded_utc=now,path=str(P),paper=413,sha256=sha(P),kind='success',message="The current source compiled successfully with the desktop editor's compiler.",actual_result_observed=True,tool='codex_app.compile_latex_document',mathematical_certification=False,protected_editor_OPEN_UNCHANGED=True,UNREVIEWED=True,accepted=False,original_closed=False)
Q=D/'ROOT413-actual-native-editor-compiler-success-20261009.json';write(Q,rec)
scope=D/'ROOT-review-scope.txt';s=scope.read_text();assert s.count('Compiler pending.')==1
scope.write_text(s.replace('Compiler pending.','Whole source compiled successfully with the built-in editor compiler.'))
b.update(recorded_utc=now,compiler=dict(kind='success',actual_result_observed=True,result_record=str(Q),result_record_sha256=sha(Q)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.iterdir()) if p.is_file() and p!=B]);write(B,b)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[287] and x['latest_verified_github_checkpoint']['continuation']==296
    x.update(updated_utc=now,ROOT413_actual_compiler_success=rec,next_work='Whole413 compiled. Freeze288 original general P12.3 envelope residual with whole413 and sole fullG331; native287 continues universal P16.7 variational representation/existence. Verify regular NONFORCE297. At mostTWO native campaigns, no hot feedback; counts/editor unchanged.');write(p,x)
print(json.dumps(dict(paper=413,compiler='success',sha256=sha(P),files=len(b['public_files'])+1),indent=2))
