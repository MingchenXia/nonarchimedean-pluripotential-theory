from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation274.json'; M=G/'upload-manifest-continuation274.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='28f8e4e06321bd4c088541efab84ef1bf90ba2f26d75ca4a6a3d379921551ac5'
assert r['commit_sha']=='1d9276b93a30c6ad00d030b3a8d4521e0975b284' and r['tree_sha']=='5521e31255b1a7d39832bf176d794d389c6ab8e2'
assert r['parent_sha']=='8e30699ac521247446811756102a57dcd8b1ee9c'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==274
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=274,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Independent native271/P12.3 and272/P16.7 continue, maximum TWO; inspect completed only. Whole conditional ROOT384 multiscale branch dual published274 UNREVIEWED, compiler213 pending. ROOT construct carefully scoped branch finite-energy extension; no active feedback.16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=274,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
