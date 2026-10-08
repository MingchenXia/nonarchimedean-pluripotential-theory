from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation239.json'
d=json.loads((G/'push-receipt-continuation239.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='bf52ec01e609718b38b5c84bda2304642066644a' and d['commit_sha']=='9793f3ace6e73911fc32c2bdb9b2ba0d178f8c7f'
assert d['tree_sha']=='9f5d7ab26de3fd0e8f0277e9307bc139b291b128' and d['files']==len(m['files'])+1==78
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='9503be6fbefd87e5b1364072a38218b204cf39f64017cc09438d3e0ab38acfa5'
assert not d['force_update'] and all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']['continuation']==239
    x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=239,commit_sha=d['commit_sha'],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
