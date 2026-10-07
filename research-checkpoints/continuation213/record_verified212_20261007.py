from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation212.json'
d=json.loads((G/'push-receipt-continuation212.json').read_text());m=json.loads(M.read_text())
assert d['parent_sha']=='b479d3a6e43969c678a289a4383334b141718a14'
assert d['commit_sha']=='4a78924d0ed58a0e92a7752b3577973ec0c3c6ed'
assert d['tree_sha']=='43714bdb03f3016f9acc3d58ffe4f3c98e149df2'
assert d['files']==len(m['files'])+1==56 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256(M.read_bytes()).hexdigest()=='77e2349e70ec9b1e9c2321f409d4f250fd05404dc507551f2bf638b6948556f0'
assert all(d[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78
    assert j['github_pending_checkpoint']['continuation']==212
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=212,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=78),indent=2))
