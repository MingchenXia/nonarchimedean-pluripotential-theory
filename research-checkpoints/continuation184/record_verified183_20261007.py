from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation183.json').read_text())
assert d['commit_sha']=='2172fcf78d2a07d688989902e89d0e5f9617d890'
assert d['parent_sha']=='ed2e88eb55104f193343cac718d3c8ee339c2fec'
assert d['tree_sha']=='74f6f7c5132b9b2665bd1d82bdd741bee902601d'
assert d['files']==27 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation183.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text())
 assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==64 and j['remaining_open_original_atoms']==33
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':183,'commit_sha':d['commit_sha'],'originals_solved':9,'cumulative_accepted_papers':64},indent=2))
