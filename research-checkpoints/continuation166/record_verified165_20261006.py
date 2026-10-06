from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';d=json.loads((G/'push-receipt-continuation165.json').read_text())
assert d['commit_sha']=='15097e35c1ccc41e82e2e2304f0b4ea5abc1ccdd' and d['parent_sha']=='7abed9d2c9aedefb052af681e999e91011c745ce'
assert d['tree_sha']=='ae245ec2d08fe3defb4f0c9472fd95e9ba090c44' and d['files']==17 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation165.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name;a=json.loads(p.read_text());assert a['historical_reviewed_scoped_papers']==59 and len(a['fully_solved_original_atoms'])==8 and a['remaining_open_original_atoms']==34
    a.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':165,'commit_sha':d['commit_sha'],'originals_solved':8,'accepted_papers':59},indent=2))
