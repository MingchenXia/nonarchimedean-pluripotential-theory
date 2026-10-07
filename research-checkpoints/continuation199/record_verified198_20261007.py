from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation198.json').read_text())
assert d['commit_sha']=='828595b1d038e32523cf6bf7257bd05577aa4637'
assert d['parent_sha']=='f3842d75e9846de2c0332daa35aa0ca14772d921'
assert d['tree_sha']=='4f315999489e5c8dcdefba5353ba5604cf66c34e' and d['files']==64 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation198.json').read_bytes()).hexdigest()
assert all(d[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==74 and j['remaining_open_original_atoms']==33
    assert j['github_pending_checkpoint']['continuation']==198
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=198,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=74),indent=2))
