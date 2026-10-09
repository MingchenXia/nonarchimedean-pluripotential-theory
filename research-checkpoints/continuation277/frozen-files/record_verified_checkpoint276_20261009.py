from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation276.json'; M=G/'upload-manifest-continuation276.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='c240d35a6c9319873c1c8d266f7ad365f466b800f482ba55958fdc6f1362f245'
assert r['commit_sha']=='cad97c40d2fe51c35bd86d937312460ba95e068e' and r['tree_sha']=='e790e5f047f1e779ae5a7bd5a5a84d99abf4b2dd'
assert r['parent_sha']=='1fcb952cc79d605ab2bde0ecb714354b9d9980dd'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==276
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=276,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Launch frozen native274 whole386/Jensen/completion/originalP12.3. Native273 fullboundedCtheta tangent/radialdual/originalP16.7 runs, at mostTWO. ROOT independently check freshDucros2012localdimension+erratum without hotfeedback.16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=276,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
