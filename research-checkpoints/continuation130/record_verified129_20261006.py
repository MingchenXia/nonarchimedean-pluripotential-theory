from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads((G/'push-receipt-continuation129.json').read_text())
assert r['commit_sha']=='6c6b3bd7bfca1aa6fdce393ce3fd73b62efd174f'
assert r['parent_sha']=='a4938bb324497fe931854a332799f625d7de7698'
assert sha(G/'upload-manifest-continuation129.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;a=json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
    a['updated_utc']=datetime.now(timezone.utc).isoformat()
    a['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=r
    a['github_pending_checkpoint']=None
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':r['commit_sha'],'files':r['files'],'original_count':7,'open_originals':35},indent=2))
