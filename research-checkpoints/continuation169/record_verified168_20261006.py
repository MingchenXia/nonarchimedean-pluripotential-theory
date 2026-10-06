from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation168.json').read_text())
assert d['commit_sha']=='f777c2225e651f92ed02cc0c2bc327418397a4a0' and d['parent_sha']=='edac8a297152e7b45086bd09b9c4b0f206719713'
assert d['tree_sha']=='46c75d9082aa46c33244a17744d4c75964b4bec2' and d['files']==29 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation168.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name;a=json.loads(p.read_text())
    assert a['historical_reviewed_scoped_papers']==59 and len(a['fully_solved_original_atoms'])==8 and a['remaining_open_original_atoms']==34
    a.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':168,'commit_sha':d['commit_sha'],'originals_solved':8,'accepted_papers':59},indent=2))
