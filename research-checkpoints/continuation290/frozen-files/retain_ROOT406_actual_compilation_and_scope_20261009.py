from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'
P=K/'P16.7-continuation406-energy-bounded-decreasing-nets-and-sequential-flattening-working-paper-20261009.tex'
S=K/'ROOT406-fresh-decreasing-net-proof-primary-application-and-compilation-scope-20261009.json'
B=K/'P16.7-continuation406-ROOT-whole-paper-source-scope-and-binding-20261009.json'
A=K/'ROOT406-actual-native-editor-compiler-success-20261009.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(P)=='7e4881ee3d0b7a81198e793b071ad31f32f6a66430b9876b481a688043c682f4'
actual=load(A); assert actual['path']==str(P) and actual['kind']=='success' and actual['actual_result_observed']
now=datetime.now(timezone.utc).isoformat(); compiler=dict(actual,recorded_utc=now,source_sha256=sha(P),result_record=str(A),result_record_sha256=sha(A))
s=load(S); b=load(B)
assert s['compiler']['kind']==b['compiler']['kind']=='pending' and not s['accepted'] and not b['accepted']
s.update(compiler=compiler); write(S,s)
b.update(compiler=compiler,source_scope=dict(path=str(S),sha256=sha(S))); write(B,b)
assert b['whole_paper']['sha256']==sha(P)
for name in ['active-work.json','checklist-current.json']:
    path=R/name; x=load(path)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==289 and x['current_active_batch']==[282,283]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,ROOT406_actual_decreasing_completion_working_proof=dict(paper=str(P),sha256=sha(P),binding=str(B),binding_sha256=sha(B),compiler='success',UNREVIEWED=True,original_closed=False),next_work='Whole406 compiled: actual energy-bounded decreasing-net closure/canonical energy, sequence flattening, finite-dual Radon integrability and full-point bounds. Original arbitrary-limit representability/compactness/envelopes remain OPEN. Native282283 continue independently at mostTWO, no hot feedback. Publish406 with next verified NONFORCE checkpoint290. No count change; protected editor OPEN UNCHANGED.')
    write(path,x)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(paper=406,source_sha256=sha(P),compiler='success',source_scope_sha256=sha(S),UNREVIEWED=True,original_closed=False,solved=16,open=26),indent=2))
