from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation254.json';m=G/'upload-manifest-continuation254.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest();z=json.loads(p.read_text())
assert z['commit_sha']=='6785490a7aec28d210d4a8c9f721f7fc379942db' and z['tree_sha']=='eea93981b7b6ef10296db924725208d9aff482e6'
assert z['parent_sha']=='82ad5f09155a291b494a5b546c889c9b9f9d3fe9'
assert z['manifest_sha256']==sha(m)=='d0921bac066f0ef994e1165b45c41eb505dc2076a7ef2eb3a9fe02ebe7c37a81'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==210 and z['files']==211
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==254
    assert len(x['fully_solved_original_atoms'])==14 and x['remaining_open_original_atoms']==28 and x['historical_reviewed_scoped_papers']==95
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=254,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=254,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=14,originals_open=28,papers=95),indent=2))
