"""Record only the verified NONFORCE publication, without mathematical acceptance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
Q = G / 'push-receipt-continuation307.json'
q = load(Q)
assert q['continuation'] == 307 and q['commit_sha'] == '6a6bdf513eff650f8971b9cf59ef281de7b6c160'
assert q['tree_sha'] == '370d7eb90cc58621859e84165d1f936ec8b5c84f' and q['parent_sha'] == '47246110a56af214776920dc8d4822bed2b38c83'
assert not q['force_update'] and q['file_count'] == 57 and q['remote_blobs_verified'] == 51
assert all(q[k] for k in ['remote_ref_verified','remote_commit_parent_and_tree_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
M = G / 'upload-manifest-continuation307.json'
assert sha(M) == q['manifest_sha256'] == '4e14d3d2a98e7bc8c999de39eda324d16080bf3f8f9c659cc2d25e06eebc4143'
m = load(M)
assert len(m['files']) == m['file_count'] == 56
for e in m['files']:
    assert sha(e['local']) == e['sha256'] and Path(e['local']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    assert y['github_pending_checkpoint']['continuation'] == 307 and y['latest_verified_github_checkpoint']['continuation'] == 306 and y['current_active_batch'] == [296,297]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
    y.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=307,commit_sha=q['commit_sha'],tree_sha=q['tree_sha'],parent_sha=q['parent_sha'],receipt=str(Q),receipt_sha256=sha(Q),manifest=str(M),manifest_sha256=sha(M),verified_utc=q['verified_utc'],force_update=False,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True),next_work='NONFORCE307 verified WHOLE427 prescribed nonskeletal equation and dominatedL1 plus frozen297. Independently develop finite-group norm/orbit/envelope descent and normal quotient scope as ROOT428. Native296297 isolated active, no mathematics inspection/hot feedback; compiler unverified, counts/editor unchanged.')
    p.write_text(json.dumps(y,ensure_ascii=False,indent=2) + '\n')
print(json.dumps(dict(continuation=307,commit=q['commit_sha'],verified=True,pending=None,current_active_batch=[296,297],solved=16,open=26,accepted_scoped_papers=97),indent=2))
