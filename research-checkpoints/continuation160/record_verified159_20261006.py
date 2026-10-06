from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation159.json').read_text())
assert d['commit_sha'] == '9a3d143842ff9c1709492752873ae859d4e0983d'
assert d['parent_sha'] == 'cfefa17e769d0677d99121ee3a77bad90d8f90db'
assert d['tree_sha'] == 'ee508e13e3811effcc4ff4a541c704e42a7472a8'
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation159.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
assert d['files'] == 56 and d['force_update'] is False
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    a = json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms']) == 8 and a['remaining_open_original_atoms'] == 34
    assert a['historical_reviewed_scoped_papers'] == 58
    a.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': 159, 'commit_sha': d['commit_sha'], 'originals_solved': 8, 'accepted_papers': 58}, indent=2))
