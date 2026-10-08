from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation247.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
z=json.loads(p.read_text());m=G/'upload-manifest-continuation247.json'
assert z['commit_sha']=='7d01ac5ddcb21c2d3dcbaa2c21a9b7e41fcc9a00'
assert z['tree_sha']=='2a13d66afdf618f42a66219ae3352e77081416c3'
assert z['parent_sha']=='c23b53a3abe644a3414f4206201d4e6c3ecaa4eb'
assert z['manifest_sha256']==sha(m)=='15074dbdf10ef2ae83089afc8ea09c8ba4d76ee727e6d18616c49f470f88048a'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==134 and z['files']==135
for e in entries:
    assert sha(e['local'])==e['sha256']
    assert Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==247
    assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=247,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=247,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=13,originals_open=29),indent=2))
