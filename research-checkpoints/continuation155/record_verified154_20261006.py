from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation154.json').read_text())
assert d['commit_sha'] == '1ac80d9f543434cdddd34b857637344cfd831f0e'
assert d['parent_sha'] == '6b3084cdb1eb974e6b5f80271c2ce3a0551b2a84'
assert d['tree_sha'] == '864d854fc80da0baec9fe8eca89e489e204edfba'
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation154.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
assert d['files'] == 43 and d['force_update'] is False
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    a = json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms']) == 8 and a['remaining_open_original_atoms'] == 34
    assert a['historical_reviewed_scoped_papers'] == 53
    a.update({'github_checkpoint': d, 'github_pending_checkpoint': None,
              'updated_utc': datetime.now(timezone.utc).isoformat()})
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': 154, 'commit_sha': d['commit_sha'],
                  'originals_solved': 8, 'accepted_papers': 53}, indent=2))
