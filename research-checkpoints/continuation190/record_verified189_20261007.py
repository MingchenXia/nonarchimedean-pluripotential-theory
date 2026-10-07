from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
d=json.loads((G/'push-receipt-continuation189.json').read_text())
assert d['commit_sha']=='d3bbf41a0a279a5fd38934b35a8bd553fa4031f6'
assert d['parent_sha']=='39c534adc1d24561176384e7b727785b710e0c99'
assert d['tree_sha']=='6e9dd946ce8cd8b827a2292a6f2d5f840021ed48' and d['files']==38 and not d['force_update']
assert d['manifest_sha256']==hashlib.sha256((G/'upload-manifest-continuation189.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==69 and j['remaining_open_original_atoms']==33
    assert j['github_pending_checkpoint']['continuation']==189
    j.update(github_checkpoint=d,github_pending_checkpoint=None,updated_utc=datetime.now(timezone.utc).isoformat())
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified_checkpoint=189,commit_sha=d['commit_sha'],originals_solved=9,cumulative_accepted_papers=69),indent=2))
