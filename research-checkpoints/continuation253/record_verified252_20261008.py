from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';p=G/'push-receipt-continuation252.json';m=G/'upload-manifest-continuation252.json'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest();z=json.loads(p.read_text())
assert z['commit_sha']=='ef17dfa600a59f3eff9e87a5eb45a4a061da2f64' and z['tree_sha']=='2937649f6a7fd970c439db83c4450a75c9b5cf09'
assert z['parent_sha']=='2521579f18fc499c8eb182202bbbac8660f2e2c8'
assert z['manifest_sha256']==sha(m)=='44783346702d136f6b9a78bbe8e71baf0a50957fd667c958ca77400a7bd7106c'
assert not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
entries=json.loads(m.read_text())['files'];assert len(entries)==293 and z['files']==294
for e in entries:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    q=R/name;x=json.loads(q.read_text());assert x['github_pending_checkpoint']['continuation']==252
    assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==94
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=252,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(p),receipt_sha256=sha(p),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False))
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=252,commit=z['commit_sha'],remote_verified=True,pending=None,originals_solved=13,originals_open=29,papers=94),indent=2))
