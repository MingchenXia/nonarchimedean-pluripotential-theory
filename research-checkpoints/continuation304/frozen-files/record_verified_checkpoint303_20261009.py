from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
Q = G / 'push-receipt-continuation303.json'
q = load(Q)
assert q['continuation'] == 303 and q['commit_sha'] == '5e1f5b0c4df72d9f4f4cd045cb8bf913859f8908'
assert q['tree_sha'] == '143f3d8aeaa6df62eca8e223e7f0a64c681dc0de' and q['parent_sha'] == '1aeb16838fc957d36947eb70664cab1ea15335e6'
assert not q['force_update'] and q['file_count'] == 52 and q['remote_blobs_verified'] == 50
assert all(q[k] for k in ['remote_ref_verified', 'remote_commit_parent_and_tree_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
M = G / 'upload-manifest-continuation303.json'
assert sha(M) == q['manifest_sha256'] == 'e6b149dc8a37dd6a7aecc3dec0aa2778e84911a1147a41d1429c45123f678b51'
m = load(M)
assert len(m['files']) == m['file_count'] == 51
for e in m['files']:
    assert sha(e['local']) == e['sha256'] and Path(e['local']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    assert y['github_pending_checkpoint']['continuation'] == 303 and y['latest_verified_github_checkpoint']['continuation'] == 302 and y['current_active_batch'] == [292,293]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
    y.update(updated_utc=now, github_pending_checkpoint=None, latest_verified_github_checkpoint=dict(continuation=303, commit_sha=q['commit_sha'], tree_sha=q['tree_sha'], parent_sha=q['parent_sha'], receipt=str(Q), receipt_sha256=sha(Q), manifest=str(M), manifest_sha256=sha(M), verified_utc=q['verified_utc'], force_update=False, remote_ref_verified=True, all_file_blob_bindings_verified_remote=True, independent_native_git_tree_verified=True), next_work='NONFORCE303 verified whole UNREVIEWED420421 and qualified frozen293 unproved existence route. Native292 just terminal, capture actual FINAL and physically read ALL current actual/expanded/source scopes before ROOT422 and next small P12.3 batch. Native293 advances actual Radon existence and general recognition, no active math/hot feedback, compiler unverified, counts/editor unchanged.')
    p.write_text(json.dumps(y, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(continuation=303, commit=q['commit_sha'], verified=True, pending=None, current_active_batch=[292,293], solved=16, open=26, accepted_scoped_papers=97), indent=2))
