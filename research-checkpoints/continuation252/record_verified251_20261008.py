from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation251.json';m=G/'upload-manifest-continuation251.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest();z=json.loads(p.read_text())
assert z['commit_sha']=='2521579f18fc499c8eb182202bbbac8660f2e2c8' and z['tree_sha']=='1b6a9a3408996cc4a76262a665ef3eaa35fdf03c'
assert z['parent_sha']=='de26bd19865404402af10b011384af3ac95ad7c8'
assert z['manifest_sha256']==sha(m)=='e8da66c56d1499d303b1e8170865e7036a3b2f75338542fd19ba35ba1b7b9b44'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==81 and z['files']==82
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==251
    assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==93
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=251,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=251,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=13,originals_open=29),indent=2))
