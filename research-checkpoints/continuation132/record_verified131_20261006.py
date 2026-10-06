from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
receipt = json.loads((G / 'push-receipt-continuation131.json').read_text())
assert receipt['commit_sha'] == '29ad1cbe2b42b6bfa9d200bea21fd8917f47f493'
assert receipt['parent_sha'] == 'ee15585af9645fd48b0d1d17407eac57951e06a2'
assert receipt['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation131.json').read_bytes()).hexdigest()
assert receipt['files'] == 18
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
assert receipt['force_update'] is False
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    data = json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms']) == 7
    assert data['historical_reviewed_scoped_papers'] == 47
    data['updated_utc'] = datetime.now(timezone.utc).isoformat()
    data['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    data['github_pending_checkpoint'] = None
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': receipt['commit_sha'], 'files': 18, 'original_count': 7, 'open_originals': 35}, indent=2))
