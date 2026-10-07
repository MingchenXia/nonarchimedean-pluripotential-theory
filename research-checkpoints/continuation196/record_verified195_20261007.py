from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation195.json').read_text())
assert d['commit_sha']=='113664f5ec69c5d3296f6aba72ec2c410114e61a'
assert d['parent_sha']=='14230bd5f978442a529081a705d61c443e3a7a1b'
assert d['tree_sha']=='b64c12e64b935a66174ef813a05024f3995f323e' and d['files']==27 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation195.json').read_bytes()).hexdigest()
assert all(d[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==74 and j['remaining_open_original_atoms']==33
    assert j['github_pending_checkpoint']['continuation']==195
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=195,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=74),indent=2))
