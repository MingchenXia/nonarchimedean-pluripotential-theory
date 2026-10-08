from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research'); G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation233.json'
d = json.loads((G / 'push-receipt-continuation233.json').read_text()); m = json.loads(M.read_text())
assert d['parent_sha'] == 'fcbb49c1572c5ad26f511cd0ecde235dd2eda038'
assert d['commit_sha'] == 'aa989fc0954c04ea83818d033a6523abb907e5ed'
assert d['tree_sha'] == 'c91b42062fbe92acbf23898fd22cad5ac3d95332'
assert d['files'] == len(m['files']) + 1 == 229 and not d['force_update']
assert d['manifest_sha256'] == hashlib.sha256(M.read_bytes()).hexdigest() == '84222c27a242153ff5ac6b16525de435ff8531abc09a6d1749d817feeecd065b'
assert all(d[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 86 and j['github_pending_checkpoint']['continuation'] == 233
    j.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(verified_checkpoint=233, commit_sha=d['commit_sha'], originals_solved=9, cumulative_accepted_papers=86), indent=2))
