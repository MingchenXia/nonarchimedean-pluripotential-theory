from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation249.json';m=G/'upload-manifest-continuation249.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
z=json.loads(p.read_text())
assert z['commit_sha']=='d0b4f0bbe91f850140f21644398f70114b0149e9' and z['tree_sha']=='18d9cc102bc57c35bab92f9c2dc2fcc19d9d2f30'
assert z['parent_sha']=='08c187e338c0fdaef7a4e373e66d05c50e86676f'
assert z['manifest_sha256']==sha(m)=='ba66aee5eb1b9fe50fe0ec9176b157d647109947176a0ce3f7397a8c187f2e9b'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==140 and z['files']==141
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==249
    assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=249,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=249,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=13,originals_open=29),indent=2))
