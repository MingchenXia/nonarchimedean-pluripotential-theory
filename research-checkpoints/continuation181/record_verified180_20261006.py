from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation180.json').read_text())
assert d['commit_sha']=='31c17e9d0e7206511df07710f31b98fef8bc8a77'
assert d['parent_sha']=='8d73fbbcb128b0a575975f23782c1d2356c4ce00'
assert d['tree_sha']=='1ef13a942727efd238bdddb35dd1eaf8bbedd789'
assert d['files']==62 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation180.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==64 and j['remaining_open_original_atoms']==33
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':180,'commit_sha':d['commit_sha'],'originals_solved':9,'cumulative_accepted_papers':64},indent=2))
