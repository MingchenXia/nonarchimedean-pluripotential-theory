from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation282.json';M=G/'upload-manifest-continuation282.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='3a02bd8ebd104c99be5cfa77cd3dcaec9d8fa3acb1d367c54079265fff85a084'
assert r['commit_sha']=='8fdefde6823413db47641042e3f7ce87c7f24dc8' and r['tree_sha']=='f3e964b5798ee64ad7fe612beb821f10b1ec93a2'
assert r['parent_sha']=='cabfc4424dc1902e79ac61b3993409e5fd818a58'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==282
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=282,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Launch frozen277 independent whole393 and actual intrinsic equation gates. Native276 formalBIG independent continues, at mostTWO. ROOT direct remaining mathematics, no originalclosure/acceptance/countchange; protected editor OPEN UNCHANGED.');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=282,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
