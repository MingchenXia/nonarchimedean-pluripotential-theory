from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research'); G=R/'github-checkpoint'; M=G/'upload-manifest-continuation224.json'
d=json.loads((G/'push-receipt-continuation224.json').read_text()); m=json.loads(M.read_text())
assert d['parent_sha']=='d7ff360d16ec8f01542a3718dc5341052eda974e'
assert d['commit_sha']=='4ee217d7a5a1902b7915b1008f359b8b1539a3e6'
assert d['tree_sha']=='d9e559a470e10e68fbd4de20670b442dea12ed1d'
assert d['files']==len(m['files'])+1==168 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='62e3e482cc4e28861818fc32e579d8f10735fc10baf243e3fed486c0d2c5056a'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==82 and j['github_pending_checkpoint']['continuation']==224
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=224,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=82),indent=2))
