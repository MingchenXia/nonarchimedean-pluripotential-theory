from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
Q = G / 'push-receipt-continuation302.json'
q = load(Q)
assert q['continuation'] == 302 and q['commit_sha'] == '1aeb16838fc957d36947eb70664cab1ea15335e6'
assert q['tree_sha'] == '385fa2a14f07af6eba6eac2096fc1cba09e68ced' and q['parent_sha'] == '359819768bb095ba106e3510cce15eaf3c663118'
assert not q['force_update'] and q['file_count'] == 53 and q['remote_blobs_verified'] == 52
assert all(q[k] for k in ['remote_ref_verified', 'remote_commit_parent_and_tree_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
M = G / 'upload-manifest-continuation302.json'
assert sha(M) == q['manifest_sha256'] == '38db3692425bc30847f4f395c91928fa409c62ce9c7246123c933022e375ad5c'
m = load(M)
assert len(m['files']) == m['file_count'] == 52
for e in m['files']:
    assert sha(e['local']) == e['sha256'] and Path(e['local']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    assert y['github_pending_checkpoint']['continuation'] == 302 and y['latest_verified_github_checkpoint']['continuation'] == 301 and y['current_active_batch'] == [291, 292]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
    y.update(updated_utc=now, github_pending_checkpoint=None, latest_verified_github_checkpoint=dict(continuation=302, commit_sha=q['commit_sha'], tree_sha=q['tree_sha'], parent_sha=q['parent_sha'], receipt=str(Q), receipt_sha256=sha(Q), manifest=str(M), manifest_sha256=sha(M), verified_utc=q['verified_utc'], force_update=False, remote_ref_verified=True, all_file_blob_bindings_verified_remote=True, independent_native_git_tree_verified=True), next_work='NONFORCE302 verified WHOLE UNREVIEWED419 conductor/cusp envelopes and actual threefold obstruction, plus qualified frozen292 including ONLY unproved ROOT conductor proposal. Native291 advances P16.7 representation/J/equation; native292 independently checks actual geometric nonsingleton-conductor envelope failure. Develop independent ROOT explicit canonical-filtration proof; no active mathematics/hot feedback, at mostTWO, compiler unverified, counts/editor unchanged.')
    p.write_text(json.dumps(y, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(continuation=302, commit=q['commit_sha'], verified=True, pending=None, current_active_batch=[291,292], solved=16, open=26, accepted_scoped_papers=97), indent=2))
