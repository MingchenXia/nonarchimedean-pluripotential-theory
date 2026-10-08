from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation227.json'
d=json.loads((G/'push-receipt-continuation227.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='6c86922ceb6995da713943040cf0fbc556510eed'
assert d['commit_sha']=='a121194f596ed66d77d6619e1d00031f84f8a80f'
assert d['tree_sha']=='b408362151765bbed0249a8ccc6e6ff158312327'
assert d['files']==len(m['files'])+1==130 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='f37e1b2e22b97625cb5f7fb0351c7dc681aced725b3a672f5f69505616f477bc'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==84 and j['github_pending_checkpoint']['continuation']==227
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    j['new298_unreviewed_paper'].update(publication_origin_was_unreviewed=True,new_accepted_paper=False,whole_independent_audit223_pending=True)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=227,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=84),indent=2))
