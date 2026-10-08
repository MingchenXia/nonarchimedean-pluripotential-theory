from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation240.json'
d=json.loads((G/'push-receipt-continuation240.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='9793f3ace6e73911fc32c2bdb9b2ba0d178f8c7f' and d['commit_sha']=='62154b4bdeef51c9ca38ba7eb1a84b5e79c56039'
assert d['tree_sha']=='d56e3e8cc6e74563700723ef43858792d6de19cf' and d['files']==len(m['files'])+1==107
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='142121a5e3e3775174b8e885accf39c058a5d4ff3d9bfef83401fd36fa9c26c6'
assert not d['force_update'] and all(d[k]for k in['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']['continuation']==240
    x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=240,commit_sha=d['commit_sha'],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
