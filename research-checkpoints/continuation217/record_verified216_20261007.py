from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation216.json'
d=json.loads((G/'push-receipt-continuation216.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='14362e47b892730cbb4e1791e11e96e9fc4512a4' and d['commit_sha']=='305afec7f2e25705f173704f3727387e0f519083'
assert d['tree_sha']=='4c0fa1615d680f15a624ad481c0e6cf2ad2bc9b4' and d['files']==len(m['files'])+1==57 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='cdaab1428d249667cfc258f01d9a4383a72526d343c02b12e0c1a92571a7ebc8'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==80
    assert j['github_pending_checkpoint']['continuation']==216
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=216,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=80),indent=2))
