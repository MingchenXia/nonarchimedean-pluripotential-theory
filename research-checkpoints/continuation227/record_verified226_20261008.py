from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation226.json'
d=json.loads((G/'push-receipt-continuation226.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='6d5e6e9d461447b3425ba5804990203a3d09ac3e'
assert d['commit_sha']=='6c86922ceb6995da713943040cf0fbc556510eed'
assert d['tree_sha']=='b79a187af632ce950e0854b5061468f784c7b986'
assert d['files']==len(m['files'])+1==74 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='d1126abe2363d42b94763975a5a074b7325ce679fa2d1c0ab330e859ab37a72e'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==84 and j['github_pending_checkpoint']['continuation']==226
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    j['new292_unreviewed_paper'].update(publication_origin_was_unreviewed=True,whole_scoped_math_accepted_after220=True,native_universal_history_INCONCLUSIVE_retained=True)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=226,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=84),indent=2))
