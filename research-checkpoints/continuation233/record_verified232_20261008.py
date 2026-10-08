from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research'); G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation232.json'
d = json.loads((G / 'push-receipt-continuation232.json').read_text()); m = json.loads(M.read_text())
assert d['parent_sha'] == '4ad457a0994bd3914fc2aa498274b85832ef5949'
assert d['commit_sha'] == 'fcbb49c1572c5ad26f511cd0ecde235dd2eda038'
assert d['tree_sha'] == 'c4deddc7a1dd43173e7d0cc49c9f340de2a58d2d'
assert d['files'] == len(m['files']) + 1 == 144 and not d['force_update']
assert d['manifest_sha256'] == hashlib.sha256(M.read_bytes()).hexdigest() == 'b561cd825e83f97f38adde20d7981637872300dcc9ea8946652da686bf1577c4'
assert all(d[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 85 and j['github_pending_checkpoint']['continuation'] == 232
    assert not j['new308_unreviewed_projective_line_formal_realization']['new_accepted_paper']
    assert not j['prepared_whole307_audit228']['launched']
    j.update(github_checkpoint=d, github_pending_checkpoint=None, updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(verified_checkpoint=232, commit_sha=d['commit_sha'], originals_solved=9, cumulative_accepted_papers=85), indent=2))
