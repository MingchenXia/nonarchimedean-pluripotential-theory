from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'
P=K/'P16.7-continuation407-Gauss-skeleton-bounds-and-bounded-test-uniform-integrability-working-paper-20261009.tex'
S=K/'ROOT407-fresh-Gauss-and-tail-proof-source-and-compilation-scope-20261009.json'
B=K/'P16.7-continuation407-ROOT-whole-paper-source-scope-and-binding-20261009.json'
A=K/'ROOT407-actual-native-editor-compiler-success-20261009.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(P)=='8c376c0f2d0470329fd61c9c7cc3a2a2fd4eecee4ba9d60b12bed588cbb05692'
actual=load(A); assert actual['path']==str(P) and actual['kind']=='success' and actual['actual_result_observed']
now=datetime.now(timezone.utc).isoformat(); compiler=dict(actual,recorded_utc=now,source_sha256=sha(P),result_record=str(A),result_record_sha256=sha(A))
s=load(S); b=load(B); assert s['compiler']['kind']==b['compiler']['kind']=='pending' and not s['accepted'] and not b['accepted']
s.update(compiler=compiler); write(S,s); b.update(compiler=compiler,source_scope=dict(path=str(S),sha256=sha(S))); write(B,b)
assert b['whole_paper']['sha256']==sha(P)
for name in ['active-work.json','checklist-current.json']:
    path=R/name; x=load(path)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==290 and x['current_active_batch']==[282,283]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,ROOT407_Gauss_and_uniform_tail_working_proof=dict(paper=str(P),sha256=sha(P),binding=str(B),binding_sha256=sha(B),compiler='success',UNREVIEWED=True,original_closed=False),next_work='Whole407 compiled: universal normalized Gauss bound, actual reference curvature support/density, fixed bounded-test gradient domination and uniform negative-part tails including actual decreasing nets/poles. Original arbitrary-limit representability/compactness/envelopes remain OPEN. Native282283 independently continue at mostTWO, no hot feedback. Publish407 with verified NONFORCE checkpoint291; no count change, protected editor OPEN UNCHANGED.')
    write(path,x)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(paper=407,source_sha256=sha(P),compiler='success',source_scope_sha256=sha(S),UNREVIEWED=True,original_closed=False,solved=16,open=26),indent=2))
