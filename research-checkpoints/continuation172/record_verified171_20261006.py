from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R = Path('/workspace/research')
G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation171.json').read_text())
assert d['commit_sha'] == 'e9d743fdbe9d7e73b453965a954cf50f7b284e88'
assert d['parent_sha'] == '4e9caa569adf91337807ebd47c53cdcbc2313b68'
assert d['tree_sha'] == '8f6d5c776254578769ed2900e529dd6147d8a1f1'
assert d['files'] == 18 and not d['force_update']
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation171.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    a = json.loads(p.read_text())
    assert a['historical_reviewed_scoped_papers'] == 63 and len(a['fully_solved_original_atoms']) == 8 and a['remaining_open_original_atoms'] == 34
    a.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': 171, 'commit_sha': d['commit_sha'], 'originals_solved': 8, 'accepted_supporting_papers': 63}, indent=2))
