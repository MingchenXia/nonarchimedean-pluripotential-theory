from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation229.json'
d=json.loads((G/'push-receipt-continuation229.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='58b2be60734bc86564d2b572ba325407dd1a7858'
assert d['commit_sha']=='f4ae742fa7d95450b5d2f49c41618fb854a5240f'
assert d['tree_sha']=='327bd0468c8499e4203de4f05eedc34b97bb3e95'
assert d['files']==len(m['files'])+1==15 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='ee79713d15a7b666a002bcc5d2748eb269a3475fbd591d200c4e01987c53d712'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==84 and j['github_pending_checkpoint']['continuation']==229
    assert not j['new300_unreviewed_working_proof']['new_accepted_paper'] and j['new300_unreviewed_working_proof']['exact_legal_outside_tau_PCC_cost']=='-1/4'
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=229,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=84),indent=2))
