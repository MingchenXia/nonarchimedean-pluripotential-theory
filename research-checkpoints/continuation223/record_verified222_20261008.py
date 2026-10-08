from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation222.json'
d=json.loads((G/'push-receipt-continuation222.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='49a125d7d90ae302a4e57295bc514550511a7a41'
assert d['commit_sha']=='bcfd5a32ceb0f0321f2389f8ed7ffa668a2a4d46'
assert d['tree_sha']=='83d7392e543abdb1cf42f0fb9385477a818976a5'
assert d['files']==len(m['files'])+1==86 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='c3b706f6f0788c3d119b6b43f73c38852191dd765ba4f1e8f144fd099ae555fd'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==82 and j['github_pending_checkpoint']['continuation']==222
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=222,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=82),indent=2))
