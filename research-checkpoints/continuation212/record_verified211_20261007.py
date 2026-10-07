from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation211.json'
d=json.loads((G/'push-receipt-continuation211.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='bad032b33e33ec83ad47239f2fcdc00557457275'
assert d['commit_sha']=='b479d3a6e43969c678a289a4383334b141718a14'
assert d['tree_sha']=='cd04c99ea24fe7cbb4ed57e41f4110f64365d1c4'
assert d['files']==len(m['files'])+1==27 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='d1d7d100dd2bfe5f113d025f77d5a2a1cbebc7c2212c338365e3f1b0016d48cd'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78
    assert j['github_pending_checkpoint']['continuation']==211
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=211,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=78),indent=2))
