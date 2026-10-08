from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research'); G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation231.json'
d = json.loads((G / 'push-receipt-continuation231.json').read_text()); m = json.loads(M.read_text())
assert d['parent_sha'] == '7fc7e81f1d2ac0bceacdeed02ce509dbdcd6ab63'
assert d['commit_sha'] == '4ad457a0994bd3914fc2aa498274b85832ef5949'
assert d['tree_sha'] == '818a5c6e057c8e6e9a309aa54b3483255c5b7f9c'
assert d['files'] == len(m['files']) + 1 == 219 and not d['force_update']
assert d['manifest_sha256'] == hashlib.sha256(M.read_bytes()).hexdigest() == '247a475b28e39d5c23e8f863aea0cb80e6da8fcc85a04b88a89e636fd70d52ea'
assert all(d[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 85 and j['github_pending_checkpoint']['continuation'] == 231
    assert not j['new306_unreviewed_paper']['new_accepted_paper']
    assert j['current_small_batch']['reserved_batch'] == [226, 227]
    j.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(verified_checkpoint=231, commit_sha=d['commit_sha'], originals_solved=9, cumulative_accepted_papers=85), indent=2))
