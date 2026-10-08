from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation220.json'
d=json.loads((G/'push-receipt-continuation220.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='360d458267ecf4f7d6241a011576634e95f72523' and d['commit_sha']=='7718cb6532e7663ec8534a49312e867c78ebd766'
assert d['tree_sha']=='423d29bee4c9aef830224f12e3e052fcb5ee3284' and d['files']==len(m['files'])+1==64 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='81d481a2309561afc5e75361e33d2804a039825a6d540183c4a086f8ad9fff70'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==82 and j['github_pending_checkpoint']['continuation']==220
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=220,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=82),indent=2))
