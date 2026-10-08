from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'; M=G/'upload-manifest-continuation238.json'
d=json.loads((G/'push-receipt-continuation238.json').read_text()); m=json.loads(M.read_text())
assert d['parent_sha']=='595e0cd1c3faf5edf10ada2c4885abb9399f688e' and d['commit_sha']=='bf52ec01e609718b38b5c84bda2304642066644a'
assert d['tree_sha']=='6c5cb6963b414b601825333085dc2c9a7bfdfd2e' and d['files']==len(m['files'])+1==84
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='88b49bf3678a1f23e0488109256dbe56fbc13a1f2ea558b29ea5b7ddaeb67492'
assert not d['force_update'] and all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text())
    assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']['continuation']==238
    x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat()); p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=238,commit_sha=d['commit_sha'],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
