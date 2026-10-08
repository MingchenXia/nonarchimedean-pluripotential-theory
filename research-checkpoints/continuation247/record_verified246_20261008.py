from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation246.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
z=json.loads(p.read_text());m=G/'upload-manifest-continuation246.json'
assert z['commit_sha']=='c23b53a3abe644a3414f4206201d4e6c3ecaa4eb'
assert z['manifest_sha256']==sha(m)=='4d48109918934d3a8d533c0cbf0ee2b5ff1d088b090b6d8b01118a648de0e71d'
assert not z['force_update'] and all(z[k]for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for e in json.loads(m.read_text())['files']:assert sha(e['local'])==e['sha256']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==246
    assert len(x['fully_solved_original_atoms'])==12 and x['remaining_open_original_atoms']==30 and x['historical_reviewed_scoped_papers']==90
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=246,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=246,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=12,originals_open=30),indent=2))
