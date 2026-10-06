from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('/workspace/research');G=R/'github-checkpoint'
receipt=json.loads((G/'push-receipt-continuation146.json').read_text())
assert receipt['commit_sha']=='188b4e05af21282bd151433e76d7f6d913f46b21'
assert receipt['parent_sha']=='05ff411a8c6490c06671270bb93d5372b6b673d2'
assert receipt['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation146.json').read_bytes()).hexdigest()
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
 p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==7 and d['historical_reviewed_scoped_papers']==51
 d['github_checkpoint']=receipt;d['github_pending_checkpoint']=None;d['updated_utc']=datetime.now(timezone.utc).isoformat()
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':146,'commit_sha':receipt['commit_sha'],'originals_solved':7,'accepted_scoped_papers':51},indent=2))
