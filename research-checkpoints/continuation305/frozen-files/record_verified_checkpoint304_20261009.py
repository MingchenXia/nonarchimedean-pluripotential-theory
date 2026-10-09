from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
Q = G / 'push-receipt-continuation304.json'
q = load(Q)
assert q['continuation'] == 304 and q['commit_sha'] == 'd267b02b6807ca63a69848509c14ad551775e770'
assert q['tree_sha'] == 'fd13398a5f899835f1a4f9e2fea4f15b5f020ea3' and q['parent_sha'] == '5e1f5b0c4df72d9f4f4cd045cb8bf913859f8908'
assert not q['force_update'] and q['file_count'] == 54 and q['remote_blobs_verified'] == 52
assert all(q[k] for k in ['remote_ref_verified', 'remote_commit_parent_and_tree_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
M = G / 'upload-manifest-continuation304.json'
assert sha(M) == q['manifest_sha256'] == 'd28fbb6641bcd2f044e6a8a7133f81c2987d88daef22af018023f19ca0c07262'
m = load(M)
assert len(m['files']) == m['file_count'] == 53
for e in m['files']:
    assert sha(e['local']) == e['sha256'] and Path(e['local']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    assert y['github_pending_checkpoint']['continuation'] == 304 and y['latest_verified_github_checkpoint']['continuation'] == 303 and y['current_active_batch'] == [293,294]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
    y.update(updated_utc=now, github_pending_checkpoint=None, latest_verified_github_checkpoint=dict(continuation=304, commit_sha=q['commit_sha'], tree_sha=q['tree_sha'], parent_sha=q['parent_sha'], receipt=str(Q), receipt_sha256=sha(Q), manifest=str(M), manifest_sha256=sha(M), verified_utc=q['verified_utc'], force_update=False, remote_ref_verified=True, all_file_blob_bindings_verified_remote=True, independent_native_git_tree_verified=True), next_work='NONFORCE304 verified whole UNREVIEWED422 and qualified frozen294 unproved marked-centre/irreducible proposals. Independently draft ROOT423 same-centre pinch-threefold signed-model failure and every-degree uniform gap. Native293294 advance original equation/conductor residuals, no active math/hot feedback, compiler unverified, counts/editor unchanged.')
    p.write_text(json.dumps(y, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(continuation=304, commit=q['commit_sha'], verified=True, pending=None, current_active_batch=[293,294], solved=16, open=26, accepted_scoped_papers=97), indent=2))
