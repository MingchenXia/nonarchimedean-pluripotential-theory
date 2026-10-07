from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation210.json'
d=json.loads((G/'push-receipt-continuation210.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='adf55f9f5908e565e6dc4b3f9fae46a33f80511f'
assert d['commit_sha']=='bad032b33e33ec83ad47239f2fcdc00557457275'
assert d['tree_sha']=='02ef3b6748ba3e1280f0539fe5fdab6fd594f976'
assert d['files']==len(m['files'])+1==57 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='a45922c69b8f0288f61c2e44bf65b8edd3ab649d58e51858a17a27789de97d61'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==77
    assert j['github_pending_checkpoint']['continuation']==210
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=210,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=77),indent=2))
