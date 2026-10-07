from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research'); G=R/'github-checkpoint'; M=G/'upload-manifest-continuation205.json'
d=json.loads((G/'push-receipt-continuation205.json').read_text()); m=json.loads(M.read_text())
assert d['parent_sha']=='1654908be98f945cdfbeda44cc44f8768b8595c6'
assert d['files']==len(m['files'])+1==62 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()
assert all(d[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==76 and j['remaining_open_original_atoms']==33
    assert j['github_pending_checkpoint']['continuation']==205
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=205,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=76),indent=2))
