from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';P=G/'push-receipt-continuation265.json';M=G/'upload-manifest-continuation265.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads(P.read_text());assert sha(M)==receipt['manifest_sha256']=='403622ce084f36d307532606efc0e6c8090a6705a9d3d29daefcbbca78251154'
assert receipt['commit_sha']=='b9950c6e2b21fb9c3018f8557c1e97190d24333b' and receipt['tree_sha']=='dc6872bbf2df6bdb7cd04f0bd084288adb12ad82'
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not receipt['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==265 and len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=265,commit=receipt['commit_sha'],tree=receipt['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=receipt['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Continue TWO native263/P21.3 and264/P16.7, original candidates pending. ENTIRE261/370 candidateFALSE preserved and published265 with mandatory actual/source/scope qualifiers, future independent reconstruction pending. ROOT investigate authenticated positive-characteristic test-ideal replacements on actual smooth primary models, no active feedback.16solved26OPEN97papers; protected editor OPEN UNCHANGED.');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=265,commit=receipt['commit_sha'],files=receipt['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
