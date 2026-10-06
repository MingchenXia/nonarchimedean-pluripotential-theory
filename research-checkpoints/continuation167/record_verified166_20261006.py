from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation166.json').read_text())
assert d['commit_sha']=='29e939088159937de76a0605f8b2b4a662146b0d' and d['parent_sha']=='15097e35c1ccc41e82e2e2304f0b4ea5abc1ccdd'
assert d['tree_sha']=='949b4c2c2255842073e0b3df13c1b1b189fb56e7' and d['files']==33 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation166.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name;a=json.loads(p.read_text())
    assert a['historical_reviewed_scoped_papers']==59 and len(a['fully_solved_original_atoms'])==8 and a['remaining_open_original_atoms']==34
    a.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':166,'commit_sha':d['commit_sha'],'originals_solved':8,'accepted_papers':59},indent=2))
