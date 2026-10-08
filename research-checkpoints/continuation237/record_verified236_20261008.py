from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation236.json'
d=json.loads((G/'push-receipt-continuation236.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='7c70de340d5f3b818d325e667a52f802e6adc64f' and d['commit_sha']=='8b7750a07a9f54d7a20ff7f552671994bcb8ae1c'
assert d['tree_sha']=='1aa660433bc853550bb37cba5310c809360e1a20' and d['files']==len(m['files'])+1==36
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='99714dcefb62841a245fe812c4f36a9f0baab535d2392d17d14a9daad844cad9'
assert not d['force_update'] and all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']['continuation']==236
 x.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=236,commit_sha=d['commit_sha'],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
