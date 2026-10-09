from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation280.json'; M=G/'upload-manifest-continuation280.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='9362d99afb6a1c2394a590b5db8a10660baa50d94587768b5d27cb4842b837db'
assert r['commit_sha']=='09ff974b780030295a4642131d6095cfcc39d73e' and r['tree_sha']=='770d3fbc2693edca0527922ea0577f2ec65230f5'
assert r['parent_sha']=='d638f663706a2d640cdf9e2ce8f32ce20a2ab127'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==280
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=280,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Bind whole ROOT392 Noetherdifferent/completedCartier product proof with exact primary source qualifications. Native275 generalE1 continues; freeze nextP12.3 native276 entire391392 to finish BIGdiagonal/subadditivity/formalCE. At mostTWO, original26OPEN/counts unchanged; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=280,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
