from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation213.json'
d=json.loads((G/'push-receipt-continuation213.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='4a78924d0ed58a0e92a7752b3577973ec0c3c6ed'
assert d['commit_sha']=='4f5e1cc15498be9e72e0f006fabee990bb1c1b90'
assert d['tree_sha']=='489a55b24c7ea8af588a4e219433d4eaf9161f9e'
assert d['files']==len(m['files'])+1==59 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='a3d7e502b6d78c566101c63ce832b061a951e96adb127f2d21cd3571d20654c9'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78
    assert j['github_pending_checkpoint']['continuation']==213
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=213,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=78),indent=2))
