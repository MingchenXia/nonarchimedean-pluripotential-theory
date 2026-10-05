from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint'
receipt=json.loads((G/'push-receipt-continuation117.json').read_text())
assert receipt['commit_sha']=='356b309610962137233ff2f0e76ff0c4518555ca'
assert receipt['parent_sha']=='ebe44098c616f64c4caa5ac4686c81cb3e18138a'
assert hashlib.sha256((G/'upload-manifest-continuation117.json').read_bytes()).hexdigest()==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']=None
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':receipt['commit_sha'],'remaining_open_originals':36,
    'original_counts_incremented':False},indent=2))

