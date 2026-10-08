from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation237.json'
d=json.loads((G/'push-receipt-continuation237.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='8b7750a07a9f54d7a20ff7f552671994bcb8ae1c' and d['commit_sha']=='595e0cd1c3faf5edf10ada2c4885abb9399f688e'
assert d['tree_sha']=='4adbd83dc36435f5e3361804a9bcf447a64445c8' and d['files']==len(m['files'])+1==122
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='dfc33d44016f51c69f07bd1b6a4f0c6698522fc9463b86b7a21e8685cf0ff403'
assert not d['force_update'] and all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']['continuation']==237
 x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=237,commit_sha=d['commit_sha'],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
