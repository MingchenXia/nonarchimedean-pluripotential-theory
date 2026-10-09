from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
Q = G / 'push-receipt-continuation299.json'
q = load(Q)
assert q['continuation'] == 299 and q['commit_sha'] == '3e62fd915dcf705bd8ba0c5773dd01561d85fbea'
assert q['tree_sha'] == 'fa6ccbf6279f0fc12e515630867939c132676652' and q['parent_sha'] == '400982936d6d43813d426c8e86541a624efdbf8b'
assert not q['force_update'] and q['file_count'] == q['remote_blobs_verified'] == 41
assert all(q[k] for k in ['remote_ref_verified', 'remote_commit_parent_and_tree_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
M = G / 'upload-manifest-continuation299.json'
assert sha(M) == q['manifest_sha256'] == '847a6c6846ec80576433205ccadbd5eca279b9b03d882d8b04ec71649f8ef028'
m = load(M)
assert len(m['files']) == m['file_count'] == 40
for e in m['files']:
    assert sha(e['local']) == e['sha256'] and Path(e['local']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    assert y['github_pending_checkpoint']['continuation'] == 299 and y['latest_verified_github_checkpoint']['continuation'] == 298
    assert y['current_active_batch'] == [289]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
    y.update(updated_utc=now, github_pending_checkpoint=None, latest_verified_github_checkpoint=dict(continuation=299, commit_sha=q['commit_sha'], tree_sha=q['tree_sha'], parent_sha=q['parent_sha'], receipt=str(Q), receipt_sha256=sha(Q), manifest=str(M), manifest_sha256=sha(M), verified_utc=q['verified_utc'], force_update=False, remote_ref_verified=True, all_file_blob_bindings_verified_remote=True, independent_native_git_tree_verified=True), next_work='NONFORCE299 verified whole UNREVIEWED415 and finite-tail-maxima proof plus qualified native289 frozen/launch metadata. Native289 continues actual analytic representation and EVERY eligible prescribed-measure MA equation. Actual415 desktop compilation still pending/unverified; no success claim. Read all four terminal288 actual five-field notes and every unique expanded proof/source before whole ROOT416 and next P12.3 follow-up. At mostTWO; no active mathematics inspection/hot feedback; counts/editor unchanged.')
    p.write_text(json.dumps(y, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(continuation=299, commit=q['commit_sha'], verified=True, pending=None, current_active_batch=[289], solved=16, open=26, accepted_scoped_papers=97), indent=2))
