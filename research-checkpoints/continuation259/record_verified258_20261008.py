from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation258.json';m=G/'upload-manifest-continuation258.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest();z=json.loads(p.read_text())
assert z['commit_sha']=='568aed3f9ac956a05ce665857881cc44766606e6' and z['tree_sha']=='78291a058c69792bfcd33a50696f5aea49be462e'
assert z['parent_sha']=='61b44c17f10a3d9fd2af00cd9775d6b0b0f661c0'
assert z['manifest_sha256']==sha(m)=='351936afa0edc617470e91f605b291393a79dc2faaf291bfdda9b3ff2af5a259'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==291 and z['files']==292
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
 q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==258
 assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=258,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
 q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=258,commit=z['commit_sha'],remote_verified=True,pending=None,solved=15,open=27,papers=96),indent=2))
