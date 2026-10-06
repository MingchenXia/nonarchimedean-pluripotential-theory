from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation160.json').read_text())
assert d['commit_sha'] == 'e2c2c9e598391b2421a271eb512489472a507f61'
assert d['parent_sha'] == '9a3d143842ff9c1709492752873ae859d4e0983d'
assert d['tree_sha'] == 'b3dc9abd45ee4a3952211bd6967e32e3be9c3d4b'
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation160.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
assert d['files'] == 54 and d['force_update'] is False
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    a = json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms']) == 8 and a['remaining_open_original_atoms'] == 34
    assert a['historical_reviewed_scoped_papers'] == 58
    a.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': 160, 'commit_sha': d['commit_sha'], 'originals_solved': 8, 'accepted_papers': 58}, indent=2))
