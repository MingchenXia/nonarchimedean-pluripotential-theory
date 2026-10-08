from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation267.json';M=G/'upload-manifest-continuation267.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads(P.read_text())
assert sha(M)==receipt['manifest_sha256']=='690eec8b5aff05d494e1d34cfe0da6fbe202d3c405714a5147cf0e6b22786006'
assert receipt['commit_sha']=='d3fe5ddd455ddf4cffdef62207d321c87b202b40' and receipt['tree_sha']=='eb23a9f5c1cd3e7cd43e9b3d6c387976e09c95fa'
assert receipt['parent_sha']=='9997cf100c282b298c3adeb5026ea7370a5decb4'
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not receipt['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text())
 assert x['github_pending_checkpoint']['continuation']==267 and len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=267,commit=receipt['commit_sha'],tree=receipt['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=receipt['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Continue TWO native265/P12.3 whole370371 independent completion and266/ONE originalP02.1 arbitrary classical psh realPL regularization. Inspect ONLY settled COMPLETE outputs. ENTIRE372/373 and ROOT/source/scopebindings published267 unreviewed; actual originalP21.3/P16.7 remainOPEN. Authenticate full period classification/ampleness/algebraization source, then future ENTIRE372/373 independent reconstruction.16solved26OPEN97papers; protected editor OPEN UNCHANGED; no active output reading/hot feedback.')
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=267,commit=receipt['commit_sha'],files=receipt['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
