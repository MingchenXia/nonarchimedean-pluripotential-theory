from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation214.json'
d=json.loads((G/'push-receipt-continuation214.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='4f5e1cc15498be9e72e0f006fabee990bb1c1b90'
assert d['commit_sha']=='835717b537956ae065c671fb700e39ce51eba43a'
assert d['tree_sha']=='617892c3ddd17ac8b5ab100dec466e8003e937e8'
assert d['files']==len(m['files'])+1==39 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='6de1b73c7d4eda513b1a1a5eb91cc03573db51970236cb3cc3f73a68a08d3845'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78
    assert j['github_pending_checkpoint']['continuation']==214
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=214,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=78),indent=2))

