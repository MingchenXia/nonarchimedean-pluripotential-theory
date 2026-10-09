"""Record verified NONFORCE308 without mathematical acceptance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research')
K=R/'root-checks'
G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
Q=G/'push-receipt-continuation308.json'
q=load(Q)
assert q['continuation']==308 and q['commit_sha']=='91609cb14e933072e9a6199014a5a443284d3717'
assert q['tree_sha']=='d5511897a06f3354108cbef00a72ef31980a8cc4' and q['parent_sha']=='6a6bdf513eff650f8971b9cf59ef281de7b6c160'
assert not q['force_update'] and q['file_count']==23 and q['remote_blobs_verified']==23 and q['remote_actual_tree_nodes_verified']==14
assert all(q[k] for k in ['remote_ref_verified','remote_commit_parent_and_tree_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
M=G/'upload-manifest-continuation308.json'
assert sha(M)==q['manifest_sha256']=='035ae1493820a0b7af35a9a8d17cab1901f8d9c945376a267b47bc284c79e35d'
m=load(M)
assert len(m['files'])==m['file_count']==22
for e in m['files']:
    assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    assert y['github_pending_checkpoint']['continuation']==308 and y['latest_verified_github_checkpoint']['continuation']==307 and y['current_active_batch']==[296,297]
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
    y.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=308,commit_sha=q['commit_sha'],tree_sha=q['tree_sha'],parent_sha=q['parent_sha'],receipt=str(Q),receipt_sha256=sha(Q),manifest=str(M),manifest_sha256=sha(M),verified_utc=q['verified_utc'],force_update=False,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True),next_work='NONFORCE308 verified WHOLE428 finite-group quotient/envelope/everydegree proof. Continue independent conductor-envelope compatibility criterion or other necessary source work while native296297 isolated and active. No active mathematics inspection/hot feedback. Compiler993 pending/unverified; counts/editor unchanged.')
    p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=308,commit=q['commit_sha'],verified=True,pending=None,current_active_batch=[296,297],solved=16,open=26,accepted_scoped_papers=97),indent=2))
