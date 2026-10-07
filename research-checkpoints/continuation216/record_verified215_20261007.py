from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation215.json'
d=json.loads((G/'push-receipt-continuation215.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='835717b537956ae065c671fb700e39ce51eba43a'
assert d['commit_sha']=='14362e47b892730cbb4e1791e11e96e9fc4512a4'
assert d['tree_sha']=='38b8b427f1df97852a26480425618743044f7ab8'
assert d['files']==len(m['files'])+1==47 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='81ea796b24c400b7897f489613b552b5f7e15aa653698cc11018bef0a0fa52a2'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==79
    assert j['github_pending_checkpoint']['continuation']==215
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=215,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=79),indent=2))
