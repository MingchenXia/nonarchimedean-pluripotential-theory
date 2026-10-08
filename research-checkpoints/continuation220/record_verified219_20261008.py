from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation219.json'
d=json.loads((G/'push-receipt-continuation219.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='b125e92eae324285e5d582b88ca17c194fa3fcc2' and d['commit_sha']=='360d458267ecf4f7d6241a011576634e95f72523'
assert d['tree_sha']=='1642254b41e8830bb7533942a0243c9958b2b298' and d['files']==len(m['files'])+1==65 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='cdd7905c7eb84c768a4d2a77d23230716889d4e0cafe648d0a0183f412c29f5e'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==81 and j['github_pending_checkpoint']['continuation']==219
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=219,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=81),indent=2))
