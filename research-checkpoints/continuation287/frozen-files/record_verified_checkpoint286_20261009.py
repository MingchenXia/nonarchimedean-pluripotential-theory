from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation286.json';M=G/'upload-manifest-continuation286.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='0de69a03a0c9da030d6f5569d4f21e3b579fc50e591e0edd98e75a0298e4fd71'
assert r['commit_sha']=='f6179edfdefcf078c5df4e52c51aebb89c241b98' and r['tree_sha']=='4b22b9ed48fa6cbc4448128005eeb29106db7d76'
assert r['parent_sha']=='80475a6b047ac041dd4173dcf0b75267b0113430' and r['files']==14 and len(r['file_bindings'])==14
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==286
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=286,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Continue native278 corrected formal CE/residual and native279 full uniqueness/compactness at mostTWO; whole398399 independently drafted, compiled, source-qualified and remotely verified286, UNREVIEWED. Pursue actual unbounded uniqueness/compactness/existence; preserve frozen active inputs and protected editor.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=286,commit=r['commit_sha'],files=14,verified=True,solved=16,open=26,papers=97),indent=2))
