from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation255.json';m=G/'upload-manifest-continuation255.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest();z=json.loads(p.read_text())
assert z['commit_sha']=='2dac27a9fd42063f36975c5477b5b870cef6627b' and z['tree_sha']=='f8e9bd1b02403779815f974354cdda3bddf8b45f'
assert z['parent_sha']=='6785490a7aec28d210d4a8c9f721f7fc379942db'
assert z['manifest_sha256']==sha(m)=='ae91dfa02e633b18cc6041eb286b821e36a7973fcb3c4a6da95d7b4adad2615c'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==43 and z['files']==44
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==255
    assert len(x['fully_solved_original_atoms'])==14 and x['remaining_open_original_atoms']==28 and x['historical_reviewed_scoped_papers']==95
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=255,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=255,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=14,originals_open=28,papers=95),indent=2))
