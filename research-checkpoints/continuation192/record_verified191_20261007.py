from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation191.json').read_text())
assert d['commit_sha']=='b4d5f1bf0def87cc283a6a3546e025796be3f1e4'
assert d['parent_sha']=='24da23bdfa4f351fad46e8e2756dce1ad587111d'
assert d['tree_sha']=='d1c279aad835eea8f8b0972330ba7e51b5f79c54' and d['files']==43 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation191.json').read_bytes()).hexdigest()
assert all(d[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text())
 assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==71 and j['remaining_open_original_atoms']==33
 assert j['github_pending_checkpoint']['continuation']==191
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=191,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=71),indent=2))
