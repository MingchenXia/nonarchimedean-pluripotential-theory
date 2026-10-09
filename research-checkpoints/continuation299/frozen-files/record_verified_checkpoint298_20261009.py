from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation298.json';M=G/'upload-manifest-continuation298.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='b8b20f517c44ca33a0443bedca0fd9ef544eefac3013092fd699ce9b0520a09a'
assert r['commit_sha']=='400982936d6d43813d426c8e86541a624efdbf8b' and r['tree_sha']=='2eeaf083da64cbd05b5b38efcfa56d0cce91ebdf'
assert r['parent_sha']=='8cbfe025d86dcd48354703546c8f1288ed65feed' and r['actual_file_count']==12 and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==298 and x['current_active_batch']==[287,288]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=298,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['recorded_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Whole compiled414 verified298, UNREVIEWED. Native287/288 continue original P16.7/P12.3. Only compact statuses until terminal; then capture and ROOT physically read ALL actual five-field and distinct expanded proofs before new papers/follow-up. Next P16.7 immutable campaign must include separate whole414 universal variational MA limits/calibrated retraction; no hot feedback to287. At mostTWO; counts/editor unchanged.');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=298,commit=r['commit_sha'],files=12,verified=True,solved=16,open=26,papers=97),indent=2))
