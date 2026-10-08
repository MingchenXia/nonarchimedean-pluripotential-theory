from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation230.json'
d=json.loads((G/'push-receipt-continuation230.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='f4ae742fa7d95450b5d2f49c41618fb854a5240f'
assert d['commit_sha']=='7fc7e81f1d2ac0bceacdeed02ce509dbdcd6ab63'
assert d['tree_sha']=='b0f82d6f31797c740aff5aff12ce4435dd24b91b'
assert d['files']==len(m['files'])+1==123 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='283976eff37f50b6180748a2bbb0aedea6bb8b2fc4c943d23965d4059de775b8'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==85 and j['github_pending_checkpoint']['continuation']==230
    assert j['P05_1_accepted_dependent_pages298_after223']['both_annotations_required_on_import']
    assert all(not e['new_accepted_paper'] for e in j['new301302303_unreviewed_working_proofs'].values())
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=230,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=85),indent=2))
