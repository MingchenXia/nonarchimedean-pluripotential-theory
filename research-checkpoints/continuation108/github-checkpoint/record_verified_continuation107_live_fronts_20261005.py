"""Update mutable live fronts only after the exact107 receipt is verified."""
from pathlib import Path
import hashlib
import json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
r = json.loads((G / 'push-receipt-continuation107.json').read_text())
assert r['commit_sha'] == '8d44aebef757ea326e923e16c7af7141d091deef'
assert hashlib.sha256((G / 'upload-manifest-continuation107.json').read_bytes()).hexdigest() == r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote',
                         'independent_native_git_tree_verified'])
for name, key in [('active-work.json', 'github_checkpoint'),
                  ('checklist-current.json', 'latest_verified_github_checkpoint')]:
    p = R / name
    d = json.loads(p.read_text())
    assert d['fully_solved_original_atoms'] == r['fully_solved_original_atoms']
    d[key] = r
    d['github_pending_checkpoint'] = None
    d['updated_utc'] = r['verified_utc']
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(r['commit_url'])
