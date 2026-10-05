"""Update mutable fronts after the exact108 receipt; frozen records stay fixed."""
from pathlib import Path
import hashlib
import json
R = Path('/workspace/research')
G = R / 'github-checkpoint'
r = json.loads((G / 'push-receipt-continuation108.json').read_text())
assert r['commit_sha'] == 'c7efec2cb60159cdd3ac8e698fd4648c853944e7'
assert hashlib.sha256((G / 'upload-manifest-continuation108.json').read_bytes()).hexdigest() == r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote',
                         'independent_native_git_tree_verified'])
for name, key in [('active-work.json', 'github_checkpoint'), ('checklist-current.json', 'latest_verified_github_checkpoint')]:
    p = R / name
    d = json.loads(p.read_text())
    assert d['fully_solved_original_atoms'] == r['fully_solved_original_atoms']
    d[key] = r
    d['github_pending_checkpoint'] = None
    d['updated_utc'] = r['verified_utc']
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(r['commit_url'])
