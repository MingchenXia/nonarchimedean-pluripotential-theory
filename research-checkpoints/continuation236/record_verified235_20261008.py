from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation235.json'
d=json.loads((G/'push-receipt-continuation235.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='9c8be7be0e6e7f7ab7feeb29b4b2ed1599384a3f' and d['commit_sha']=='7c70de340d5f3b818d325e667a52f802e6adc64f'
assert d['tree_sha']=='1f44cd64382e43f7e20dbf9768d4cd5ac7ecbde2' and d['files']==len(m['files'])+1==156
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='75bcdf479c9138cc6e7da468930a9d9466aae57ab71981bbce6bfedb20d7eadd'
assert not d['force_update'] and all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']['continuation']==235
 x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=235,commit_sha=d['commit_sha'],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
