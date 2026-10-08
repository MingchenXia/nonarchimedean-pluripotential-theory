from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation228.json'
d=json.loads((G/'push-receipt-continuation228.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='a121194f596ed66d77d6619e1d00031f84f8a80f'
assert d['commit_sha']=='58b2be60734bc86564d2b572ba325407dd1a7858'
assert d['tree_sha']=='f0d29c7acee2278d218331ab5e0835aa494fb51e'
assert d['files']==len(m['files'])+1==76 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='e0972df4c3576fe9b01e2ee57f08b87c90ab7dc15fa3836c800c875a7e0a3188'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==84 and j['github_pending_checkpoint']['continuation']==228
    assert not j['new299_unreviewed_working_proof']['new_accepted_paper'] and j['incomplete_whole_audit222']['native222_entire_math_source_verdict']=='INCONCLUSIVE'
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=228,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=84),indent=2))
