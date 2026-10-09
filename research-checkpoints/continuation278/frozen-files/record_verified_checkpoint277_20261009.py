from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation277.json'; M=G/'upload-manifest-continuation277.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='41d36c279d4fc23c2a76661e34ea5e55f4278afa22f4e0e3e1a652dfc114b58f'
assert r['commit_sha']=='a9d7d960ddc0dafaebd5b85e12cc8b9794a2b16b' and r['tree_sha']=='a3404646a7a71e4dd9fcbaa03a1b44e6b4b2338e'
assert r['parent_sha']=='cad97c40d2fe51c35bd86d937312460ba95e068e'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==277
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=277,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Native273 fullboundedCtheta Green/tangent/radialdual/originalE1 and native274 whole386/Jensen/completion/originalP12.3 continue, at mostTWO. ROOT fresh localdimension theorem immediate dependencies and errata recorded with printed typos/version qualifications. Continue fullbounded Green proof independently without hotfeedback; capture completed nativeFINAL only when completed/errornull/unsettled0.16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=277,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
