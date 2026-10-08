from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation223.json'
d=json.loads((G/'push-receipt-continuation223.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='bcfd5a32ceb0f0321f2389f8ed7ffa668a2a4d46'
assert d['commit_sha']=='d7ff360d16ec8f01542a3718dc5341052eda974e'
assert d['tree_sha']=='1b8a9b4b38a95b1a56a16709bbeacc39babf19e4'
assert d['files']==len(m['files'])+1==67 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='6d0c720099600986b40a80bca07ca8e2035862006da0a2eb3c15ea4865303f9c'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==82 and j['github_pending_checkpoint']['continuation']==223
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=223,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=82),indent=2))
