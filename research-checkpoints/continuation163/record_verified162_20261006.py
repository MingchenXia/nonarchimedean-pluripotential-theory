from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';d=json.loads((G/'push-receipt-continuation162.json').read_text())
assert d['commit_sha']=='06aa810202cda527d935227981b789f7838fa50a' and d['parent_sha']=='9e3a5396216d4b06b61258d023ec355b884fc2c0'
assert d['tree_sha']=='451c56e692140dfa43a8e3024f8ddf408a120a27' and d['files']==34 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation162.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name;a=json.loads(p.read_text());assert a['historical_reviewed_scoped_papers']==59 and len(a['fully_solved_original_atoms'])==8 and a['remaining_open_original_atoms']==34
    a.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':162,'commit_sha':d['commit_sha'],'originals_solved':8,'accepted_papers':59},indent=2))
