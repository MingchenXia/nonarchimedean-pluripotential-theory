from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation225.json'
d=json.loads((G/'push-receipt-continuation225.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='4ee217d7a5a1902b7915b1008f359b8b1539a3e6'
assert d['commit_sha']=='6d5e6e9d461447b3425ba5804990203a3d09ac3e'
assert d['tree_sha']=='f466bbc770a570f45e9892ee1308decef8326c1b'
assert d['files']==len(m['files'])+1==125 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='cafcb4803cf2f2881d5ba986606f69ae9ea2240e1270dd55d644884ed567e658'
assert all(d[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==83 and j['github_pending_checkpoint']['continuation']==225
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    j['new291_unreviewed_paper'].update(new_accepted_paper=True,mathematical_sector_only_with_bound_source_corrections=True,native_unchanged_source_combined_FAIL=True,publication_origin_was_unreviewed=True)
    j['settled218_unreviewed_audit'].update(mathematical_acceptance_with_source_corrections=True,unqualified_native_source_acceptance=False)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=225,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=83),indent=2))
