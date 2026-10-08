from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';P=G/'push-receipt-continuation266.json';M=G/'upload-manifest-continuation266.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads(P.read_text());assert sha(M)==receipt['manifest_sha256']=='8d0e35a3c134f62d049724f08ca4a7b3ef4938b9f9c69b31d809b2cb9d2a9412'
assert receipt['commit_sha']=='9997cf100c282b298c3adeb5026ea7370a5decb4' and receipt['tree_sha']=='f7b90487c2204a72f793d85a050d510afb1f2fb4'
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not receipt['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==266 and len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=266,commit=receipt['commit_sha'],tree=receipt['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=receipt['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Native263 and264 completed with candidateFALSE; actual FINAL captured for full ROOT reading and independent continuation. ENTIRE ROOT371 published266 as unreviewed fixed-smooth-primary-model test-ideal theorem, NOT an unconditional resolution claim; ENTIRE native261/370 reconstruction next.16solved26OPEN97papers; protected editor OPEN UNCHANGED.');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=266,commit=receipt['commit_sha'],files=receipt['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
