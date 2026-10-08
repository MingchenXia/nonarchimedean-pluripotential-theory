from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation242.json'
d = json.loads((G / 'push-receipt-continuation242.json').read_text())
m = json.loads(M.read_text())
assert d['parent_sha'] == 'b56ceedac244039d17fd2100654ad41a233b2a10'
assert d['commit_sha'] == '79f007ee717f62ced9ae236a278a0157bc34f1f0'
assert d['tree_sha'] == '9e6eb508d24a5e890f1996d5da8e9be312e8a52c'
assert d['files'] == len(m['files']) + 1 == 120
assert d['manifest_sha256'] == hashlib.sha256(M.read_bytes()).hexdigest() == '02057ace7ca687328f4e3a995042b9c650b042f5a9d418bae35b7935ce410b0d'
assert not d['force_update']
assert all(d[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    x = json.loads(p.read_text())
    assert len(x['fully_solved_original_atoms']) == 11
    assert x['remaining_open_original_atoms'] == 31
    assert x['historical_reviewed_scoped_papers'] == 89
    assert x['github_pending_checkpoint']['continuation'] == 242
    assert x['fully_solved_original_atoms'] == d['fully_solved_original_atoms']
    x.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(verified_checkpoint=242, commit_sha=d['commit_sha'], originals_solved=11, originals_open=31, accepted_papers=89), indent=2))
