from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation241.json'
d=json.loads((G/'push-receipt-continuation241.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='62154b4bdeef51c9ca38ba7eb1a84b5e79c56039' and d['commit_sha']=='b56ceedac244039d17fd2100654ad41a233b2a10'
assert d['tree_sha']=='7eac87e2442748c1385da9ed727f06b8a97e6d46' and d['files']==len(m['files'])+1==15
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='009b0164c09f509f5b477524327efe4babf190e1eec81fbb0b83b1a4fe8721ec'
assert not d['force_update'] and all(d[k]for k in['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']['continuation']==241
    x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=241,commit_sha=d['commit_sha'],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
