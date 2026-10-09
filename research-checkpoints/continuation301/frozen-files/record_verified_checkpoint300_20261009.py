from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
Q = G / 'push-receipt-continuation300.json'
q = load(Q)
assert q['continuation'] == 300 and q['commit_sha'] == 'a1a39b2333d07b8d69619d528c671754323fb467'
assert q['tree_sha'] == 'c3bec6604e666c7021d08432c5f5c5ff7cee3ee6' and q['parent_sha'] == '3e62fd915dcf705bd8ba0c5773dd01561d85fbea'
assert not q['force_update'] and q['file_count'] == q['remote_blobs_verified'] == 43 and q['unique_blobs'] == 42
assert all(q[k] for k in ['remote_ref_verified', 'remote_commit_parent_and_tree_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
M = G / 'upload-manifest-continuation300.json'
assert sha(M) == q['manifest_sha256'] == '2714fea7dd87839da4b2ad53932e8338805f959542a34084de513f3295eaf316'
m = load(M)
assert len(m['files']) == m['file_count'] == 42
for e in m['files']:
    assert sha(e['local']) == e['sha256'] and Path(e['local']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    assert y['github_pending_checkpoint']['continuation'] == 300 and y['latest_verified_github_checkpoint']['continuation'] == 299
    assert y['current_active_batch'] == [289, 290]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
    y.update(updated_utc=now, github_pending_checkpoint=None, latest_verified_github_checkpoint=dict(continuation=300, commit_sha=q['commit_sha'], tree_sha=q['tree_sha'], parent_sha=q['parent_sha'], receipt=str(Q), receipt_sha256=sha(Q), manifest=str(M), manifest_sha256=sha(M), verified_utc=q['verified_utc'], force_update=False, remote_ref_verified=True, all_file_blob_bindings_verified_remote=True, independent_native_git_tree_verified=True), next_work='NONFORCE300 verified whole UNREVIEWED416 excellent normal surface envelope proof and qualified native290 metadata. Native290 advances unchanged higher-dimensional normal/conductor envelope residual; native289 actual P16.7 analytic representation and every eligible prescribed-measure equation. At mostTWO, no active mathematics inspection/hot feedback. Actual416 and second415 desktop compile requests remain pending UNVERIFIED; first415 returned connection closed before answer. Sources preserved; counts/protected editor unchanged.')
    p.write_text(json.dumps(y, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(continuation=300, commit=q['commit_sha'], verified=True, pending=None, current_active_batch=[289, 290], solved=16, open=26, accepted_scoped_papers=97), indent=2))
