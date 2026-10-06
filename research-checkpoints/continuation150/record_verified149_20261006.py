from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('/workspace/research'); G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation149.json').read_text())
assert d['commit_sha']=='f3a957fb293464aa8e05d72cf5fda2433f8323e2'
assert d['parent_sha']=='b842b5c822534ba689804316589e5197d669e253'
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation149.json').read_bytes()).hexdigest()
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name; a=json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms'])==8 and a['remaining_open_original_atoms']==34 and a['historical_reviewed_scoped_papers']==52
    a.update({'github_checkpoint':d,'github_pending_checkpoint':None,'updated_utc':datetime.now(timezone.utc).isoformat()})
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':149,'commit_sha':d['commit_sha'],'originals_solved':8,'accepted_papers':52},indent=2))
