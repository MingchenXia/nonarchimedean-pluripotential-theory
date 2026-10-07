from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R = Path('/workspace/research'); G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation181.json').read_text())
assert d['commit_sha'] == '58b4babd53dd05f9899b81b4ba4537024a8be0b4'
assert d['parent_sha'] == '31c17e9d0e7206511df07710f31b98fef8bc8a77'
assert d['tree_sha'] == '950b96cfe7b4141ddcd7fd6edf9e8eea74a3b315'
assert d['files'] == 25 and not d['force_update']
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation181.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name; j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['historical_reviewed_scoped_papers'] == 64 and j['remaining_open_original_atoms'] == 33
    j.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': 181, 'commit_sha': d['commit_sha'], 'originals_solved': 9, 'cumulative_accepted_papers': 64}, indent=2))
