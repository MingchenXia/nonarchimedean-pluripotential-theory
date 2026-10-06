from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint'
r=json.loads((G/'push-receipt-continuation134.json').read_text())
assert r['commit_sha']=='73b2ce3b5a0181daa47e60c92278c20ac0f87fd8'
assert r['parent_sha']=='7ebd61e715488b22cac1961105ef4be8c58a6420'
assert r['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation134.json').read_bytes()).hexdigest()
assert r['files']==18 and r['force_update'] is False
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==47
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=r
    data['github_pending_checkpoint']=None
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':r['commit_sha'],'files':18,'originals_solved':7,'originals_open':35},indent=2))
