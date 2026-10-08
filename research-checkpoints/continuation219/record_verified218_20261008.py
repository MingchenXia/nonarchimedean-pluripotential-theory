from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation218.json'
d=json.loads((G/'push-receipt-continuation218.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='f400ddc7034cf68bf6d737b83e849e908a412727' and d['commit_sha']=='b125e92eae324285e5d582b88ca17c194fa3fcc2'
assert d['tree_sha']=='d219a636f8468c4bb5ff5d315f12f0fbbd07386c' and d['files']==len(m['files'])+1==72 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='82683cccf9597de69c9ebfe9874af389c38bf76a4776f8a922aedc422b564e55'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==80 and j['github_pending_checkpoint']['continuation']==218
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=218,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=80),indent=2))
