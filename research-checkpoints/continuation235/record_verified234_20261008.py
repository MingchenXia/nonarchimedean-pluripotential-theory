from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research'); G=R/'github-checkpoint'; M=G/'upload-manifest-continuation234.json'
d=json.loads((G/'push-receipt-continuation234.json').read_text()); m=json.loads(M.read_text())
assert d['parent_sha']=='aa989fc0954c04ea83818d033a6523abb907e5ed'
assert d['commit_sha']=='9c8be7be0e6e7f7ab7feeb29b4b2ed1599384a3f'
assert d['tree_sha']=='b2cca27ef6fc232371e7100634d9e4ea7f4e614b'
assert d['files']==len(m['files'])+1==114 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='708472724186cbc0f788b4b30ba6fcc6ac669e3fa8a0bd28573da96d93b87b63'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
 p=R/name; j=json.loads(p.read_text())
 assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==87 and j['github_pending_checkpoint']['continuation']==234
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=234,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=87),indent=2))
