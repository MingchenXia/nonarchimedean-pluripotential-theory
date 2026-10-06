from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint'
r=json.loads((G/'push-receipt-continuation140.json').read_text())
assert r['commit_sha']=='a2470baf155c17d754b55974e6e799276c82eb41'
assert r['parent_sha']=='552bfc9e1eaed5bed7b85b332684dd9263783bef'
assert r['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation140.json').read_bytes()).hexdigest()
assert r['files']==20 and r['force_update'] is False
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==49
    assert [i['round'] for i in data['current_small_batch']['items']]==[125,129]
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=r
    data['github_pending_checkpoint']=None
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':r['commit_sha'],'files':20,'originals_solved':7,'originals_open':35,'reviewed_scoped_papers':49},indent=2))
