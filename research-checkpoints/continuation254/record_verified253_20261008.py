from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation253.json';m=G/'upload-manifest-continuation253.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest();z=json.loads(p.read_text())
assert z['commit_sha']=='82ad5f09155a291b494a5b546c889c9b9f9d3fe9' and z['tree_sha']=='4eafb7443ee89b3d5dff7f5e531ea3435bc90caa'
assert z['parent_sha']=='ef17dfa600a59f3eff9e87a5eb45a4a061da2f64'
assert z['manifest_sha256']==sha(m)=='d0acafa75002ab6e9aaae8cb555e5a6fbeeef96f9db6f88ff6ef295df5209e49'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==61 and z['files']==62
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==253
    assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==94
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=253,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=253,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=13,originals_open=29,papers=94),indent=2))
