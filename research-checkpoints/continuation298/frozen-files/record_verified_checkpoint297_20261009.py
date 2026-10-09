from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation297.json';M=G/'upload-manifest-continuation297.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='3d5d0be3eab54e4c919b8d8caa6ded25107d0140b969f29fc0dc446cb2b7f1df'
assert r['commit_sha']=='8cbfe025d86dcd48354703546c8f1288ed65feed' and r['tree_sha']=='639a45409a00013d09a6ad3bbc029e7ec3ac147b'
assert r['parent_sha']=='950fb067dc6af402bf0c34225a728971cf093b2f' and r['actual_file_count']==37 and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==297 and x['current_active_batch']==[287,288]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=297,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['recorded_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Whole compiled413 verified297, UNREVIEWED. Native287/288 continue original P16.7/P12.3. ROOT writes complete universal variational energy/diagonal/measure-limit and calibrated dual retraction paper414 from settled411412, without active proof inspection/hot feedback. At mostTWO; counts/editor unchanged.');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=297,commit=r['commit_sha'],files=37,verified=True,solved=16,open=26,papers=97),indent=2))
