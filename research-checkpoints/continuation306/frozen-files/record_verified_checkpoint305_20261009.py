"""Record only the independently verified NONFORCE GitHub checkpoint."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
Q = G / 'push-receipt-continuation305.json'
q = load(Q)
assert q['continuation'] == 305 and q['commit_sha'] == 'd91fed0faba2f946f7488c2e2534424dccd8bc48'
assert q['tree_sha'] == '68017fa634fe8f9cd9d9bc13e8bc10ce081c5c5e' and q['parent_sha'] == 'd267b02b6807ca63a69848509c14ad551775e770'
assert not q['force_update'] and q['file_count'] == 69 and q['remote_blobs_verified'] == 58
assert all(q[k] for k in ['remote_ref_verified','remote_commit_parent_and_tree_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
M = G / 'upload-manifest-continuation305.json'
assert sha(M) == q['manifest_sha256'] == '5a9aa5749410e98942e1198c7e2b5cf83dd3f294ff50d881c9d3e3ff69ab1579'
m = load(M)
assert len(m['files']) == m['file_count'] == 68
for e in m['files']:
    assert sha(e['local']) == e['sha256'] and Path(e['local']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    assert y['github_pending_checkpoint']['continuation'] == 305 and y['latest_verified_github_checkpoint']['continuation'] == 304 and y['current_active_batch'] == [294,295]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
    y.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=305,commit_sha=q['commit_sha'],tree_sha=q['tree_sha'],parent_sha=q['parent_sha'],receipt=str(Q),receipt_sha256=sha(Q),manifest=str(M),manifest_sha256=sha(M),verified_utc=q['verified_utc'],force_update=False,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True),next_work='NONFORCE305 verified whole UNREVIEWED423424 plus qualified frozen295 nonskeletal proposals. Independently develop ROOT425 general conductor-cover exponent/characteristic dichotomy. Native294295 pursue original geometric and equation residuals, no active math/hot feedback; compilation unverified, counts/editor unchanged.')
    p.write_text(json.dumps(y,ensure_ascii=False,indent=2) + '\n')
print(json.dumps(dict(continuation=305,commit=q['commit_sha'],verified=True,pending=None,current_active_batch=[294,295],solved=16,open=26,accepted_scoped_papers=97),indent=2))
