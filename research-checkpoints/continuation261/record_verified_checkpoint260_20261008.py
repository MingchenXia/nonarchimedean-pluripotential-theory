from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';P=G/'push-receipt-continuation260.json';M=G/'upload-manifest-continuation260.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
z=json.loads(P.read_text());m=json.loads(M.read_text())
assert z['commit_sha']=='7cc2af8e39f1a2f0e3d131c7664119d82d0f6c27' and z['tree_sha']=='1eaa1850b6536106b287ee3abd2b7e44d87e9df3' and z['parent_sha']=='525c3eb34ee595983d5d67693f3d8de5ed7299c7'
assert z['manifest_sha256']==sha(M)=='5e3decacab77cbf65f78bb01d6030f623d196f43456470b4ca00f3d7e467f8c8' and z['files']==m['file_count']+1==293
assert z['repository']=='MingchenXia/nonarchimedean-pluripotential-theory' and z['branch']=='codex/xean-research-20261003' and not z['force_update'] and all(z[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for e in m['files']:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==260 and len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=260,commit=z['commit_sha'],tree=z['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=z['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False));p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=260,verified_commit=z['commit_sha'],verified_tree=z['tree_sha'],files=z['files'],formal_solved=15,formal_OPEN=27,accepted_papers=96,pending_checkpoint=None),indent=2))
