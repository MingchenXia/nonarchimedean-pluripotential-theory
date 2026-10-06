from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research');G=R/'github-checkpoint';d=json.loads((G/'push-receipt-continuation177.json').read_text())
assert d['commit_sha']=='e7676dc3d24345ff355245d835485b44efe8333d'
assert d['parent_sha']=='492c7a02fc4b5713463225fdc855d7ace6f1a3d2' and d['tree_sha']=='13c7ce76769d4f8c9815b814c303deba26fc657b'
assert d['files']==22 and not d['force_update'] and d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation177.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==63 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':177,'commit_sha':d['commit_sha'],'originals_solved':8,'accepted_supporting_papers':63},indent=2))
