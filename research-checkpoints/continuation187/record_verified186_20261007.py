from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation186.json').read_text())
assert d['commit_sha']=='b1d2a49004fda1d3092f6b26072874f4ddacd0ed'
assert d['parent_sha']=='02e8f998ba555e2dd03c972d2bf136c781db2cc0'
assert d['tree_sha']=='55ff3da4962b49582a5918c1f78e639706f517ac' and d['files']==56 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation186.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==67 and j['remaining_open_original_atoms']==33
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':186,'commit_sha':d['commit_sha'],'originals_solved':9,'cumulative_accepted_papers':67},indent=2))
