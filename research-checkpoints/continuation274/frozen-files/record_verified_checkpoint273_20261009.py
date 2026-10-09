from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation273.json'; M=G/'upload-manifest-continuation273.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='4d5fcf5e051b034c68106d4c852f7bb570dbfd3e10e335f79fd5aff09be6cf91'
assert r['commit_sha']=='8e30699ac521247446811756102a57dcd8b1ee9c' and r['tree_sha']=='47ef04af9a8d19496e1f8634fba55e18e2a8a45a'
assert r['parent_sha']=='06e845d734fa4d48a49a8bfea49c0faeef62c836'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==273
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=273,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Native271 independently verifies whole382380381/HH02 and originalP12.3. Native272 independently verifies whole383 and intrinsicE1/finite-depth analyticDirac. Maximum TWO; no active math feedback. ROOT primary proof and intrinsic mathematical work; capture completed only. Whole383 published273 UNREVIEWED,16solved26OPEN97accepted unchanged; protected editor unchanged.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=273,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
