from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation256.json';m=G/'upload-manifest-continuation256.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest();z=json.loads(p.read_text())
assert z['commit_sha']=='19a9fc49970392c5f2daa35fc57cd1b1c138d6e6' and z['tree_sha']=='d174ef7ee3cc781cbe8f94d4108b90b51c624629'
assert z['parent_sha']=='2dac27a9fd42063f36975c5477b5b870cef6627b'
assert z['manifest_sha256']==sha(m)=='d1a8bd2688f8df60041c984bdbaa8877dfee456cb139830ea57c96a8cc6370ed'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==70 and z['files']==71
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==256
    assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=256,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=256,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=15,originals_open=27,papers=96),indent=2))
