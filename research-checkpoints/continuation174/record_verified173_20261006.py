from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R = Path('/workspace/research')
G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation173.json').read_text())
assert d['commit_sha'] == '728a240fe3d219cead75408c760d3168b698b2e3'
assert d['parent_sha'] == 'a61bb373885ed4a270f528a5eae0d51799931df8'
assert d['tree_sha'] == 'c7cf029f5dc7c8d5efca5a2d78fa9815eaeca337'
assert d['files'] == 17 and not d['force_update']
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation173.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': 173, 'commit_sha': d['commit_sha'], 'originals_solved': 8, 'accepted_supporting_papers': 63}, indent=2))
