from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation244.json'
d=json.loads((G/'push-receipt-continuation244.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='fe311b244a6dd0a6fc16b669ec93048148acb6aa' and d['commit_sha']=='1ebf677734a444e776c6024bf2cf09684d930381'
assert d['tree_sha']=='daaa234a1df97af2398153373707481e3f4e8a95' and d['files']==len(m['files'])+1==17
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='72e093870a9d73fddd005e5be0f507afa60e373e4363daf67fe7712878f0ecd8'
assert not d['force_update'] and all(d[k] for k in('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in('active-work.json','checklist-current.json'):
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==11 and x['remaining_open_original_atoms']==31 and x['historical_reviewed_scoped_papers']==89 and x['github_pending_checkpoint']['continuation']==244
    assert x['fully_solved_original_atoms']==d['fully_solved_original_atoms']
    x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=244,commit_sha=d['commit_sha'],originals_solved=11,originals_open=31,accepted_papers=89),indent=2))
