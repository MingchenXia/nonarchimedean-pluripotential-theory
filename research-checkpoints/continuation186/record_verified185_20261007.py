from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation185.json').read_text())
assert d['commit_sha']=='02e8f998ba555e2dd03c972d2bf136c781db2cc0'
assert d['parent_sha']=='5f47319803bed86628375cc6a98b0fdae6160946'
assert d['tree_sha']=='8af6042374ee0ff6eb1e3f043284d7f9ad60ba3f' and d['files']==31 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation185.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==65 and j['remaining_open_original_atoms']==33
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':185,'commit_sha':d['commit_sha'],'originals_solved':9,'cumulative_accepted_papers':65},indent=2))
