from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation279.json'; M=G/'upload-manifest-continuation279.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='130f69720aef3ceec75c8682a80b058fedbf30f52da5881c1d23d47de54c3746'
assert r['commit_sha']=='d638f663706a2d640cdf9e2ce8f32ce20a2ab127' and r['tree_sha']=='98c8a03b5ea45cff5e1d8acb35a8866d7942a655'
assert r['parent_sha']=='e9593cf1a49f8d9aca8cdd2e7add95a4ba192041'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==279
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=279,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Launch frozen native275 entire390388389 generalE1 operator; whole native274 proof/source/scope review then nextP12.3 campaign, at mostTWO. Original26OPEN/counts unchanged; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=279,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
