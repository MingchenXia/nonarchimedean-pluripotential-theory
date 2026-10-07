from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research'); G=R/'github-checkpoint'; M=G/'upload-manifest-continuation207.json'
d=json.loads((G/'push-receipt-continuation207.json').read_text()); m=json.loads(M.read_text())
assert d['parent_sha']=='8eaf0c421727f607b20cab6676f05ff3da4caa00'
assert d['commit_sha']=='4241f594a7d705b841ab03ff2f28ad2f63e48802'
assert d['tree_sha']=='2a5995d689987581a44db446ec137931902ddbea'
assert d['files']==len(m['files'])+1==31 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='c547964c64693ad71579c6ed22f6b649fd2c47944884a56f74f3655c72f8ef54'
assert all(d[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==76 and j['remaining_open_original_atoms']==33
    assert j['github_pending_checkpoint']['continuation']==207
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=207,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=76),indent=2))
