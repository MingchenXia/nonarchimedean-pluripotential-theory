from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation209.json'
d=json.loads((G/'push-receipt-continuation209.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='50f7633af3f5f9d5012430b272aaea167b6c136a'
assert d['commit_sha']=='adf55f9f5908e565e6dc4b3f9fae46a33f80511f'
assert d['tree_sha']=='51b1acd74e3d71d317043c4c9e4875ac85ecaca9'
assert d['files']==len(m['files'])+1==61 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='a668f20625d674115cf552ab1f2e5de0797012e0c6ad8539bf661fb844c8c04f'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==77 and j['remaining_open_original_atoms']==33
 assert j['github_pending_checkpoint']['continuation']==209
 j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=209,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=77),indent=2))
