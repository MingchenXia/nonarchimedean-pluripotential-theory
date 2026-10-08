from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation221.json'
d = json.loads((G / 'push-receipt-continuation221.json').read_text())
m = json.loads(M.read_text())
assert d['parent_sha'] == '7718cb6532e7663ec8534a49312e867c78ebd766'
assert d['commit_sha'] == '49a125d7d90ae302a4e57295bc514550511a7a41'
assert d['tree_sha'] == 'ccd1dce76e276a11c77607be669f15f5f2c69d79'
assert d['files'] == len(m['files']) + 1 == 17 and not d['force_update']
assert d['manifest_sha256'] == hashlib.sha256(M.read_bytes()).hexdigest() == '8ff25d6918e01b6a20526e50c9e82713ef97a192dfaf50a26409f208976aa41b'
assert all(d[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9
    assert j['remaining_open_original_atoms'] == 33
    assert j['historical_reviewed_scoped_papers'] == 82
    assert j['github_pending_checkpoint']['continuation'] == 221
    j.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(verified_checkpoint=221, commit_sha=d['commit_sha'], originals_solved=9, cumulative_accepted_papers=82), indent=2))
