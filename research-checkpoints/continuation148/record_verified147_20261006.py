from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('/workspace/research');G=R/'github-checkpoint'
receipt=json.loads((G/'push-receipt-continuation147.json').read_text())
assert receipt['commit_sha']=='50e1703956ad10903d683b4531f0297b686b85d5'
assert receipt['parent_sha']=='188b4e05af21282bd151433e76d7f6d913f46b21'
assert receipt['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation147.json').read_bytes()).hexdigest()
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
 p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==8 and d['historical_reviewed_scoped_papers']==52 and d['remaining_open_original_atoms']==34
 d['github_checkpoint']=receipt;d['github_pending_checkpoint']=None;d['updated_utc']=datetime.now(timezone.utc).isoformat()
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':147,'commit_sha':receipt['commit_sha'],'originals_solved':8,'accepted_papers':52},indent=2))
