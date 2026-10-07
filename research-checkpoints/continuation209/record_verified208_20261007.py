from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation208.json'
d=json.loads((G/'push-receipt-continuation208.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='4241f594a7d705b841ab03ff2f28ad2f63e48802'
assert d['commit_sha']=='50f7633af3f5f9d5012430b272aaea167b6c136a'
assert d['tree_sha']=='c0a785f029aeb513f51b7da1ea31287e80405e2c'
assert d['files']==len(m['files'])+1==30 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='9c731ff5096d04c1ff3de9a2d73305fee2d4c771330d87a5706eb28f7f275c2f'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==77 and j['remaining_open_original_atoms']==33
    assert j['github_pending_checkpoint']['continuation']==208
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=208,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=77),indent=2))
