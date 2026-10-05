from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research'); G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt = json.loads((G / 'push-receipt-continuation121.json').read_text())
assert receipt['commit_sha'] == '1434ad650e5438b64dfc6a1c541ac2a9466385e6'
assert receipt['parent_sha'] == '3dec2b22580439036cf5c566223292a1b9c5b953'
assert sha(G / 'upload-manifest-continuation121.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; a = json.loads(p.read_text()); assert len(a['fully_solved_original_atoms']) == 7
    assert [i['round'] for i in a['current_small_batch']['items']] == [119, 120]
    if name == 'checklist-current.json': assert a['historical_reviewed_scoped_papers'] == 44
    a['updated_utc'] = now
    a['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    a['github_pending_checkpoint'] = None
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': receipt['commit_sha'], 'files': receipt['files'],
    'original_count_unchanged': 7, 'remaining_open_originals': 35}, indent=2))
