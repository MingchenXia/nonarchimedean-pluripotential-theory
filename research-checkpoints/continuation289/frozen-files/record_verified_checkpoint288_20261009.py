from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation288.json';M=G/'upload-manifest-continuation288.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='9a24a83fb9ea36663fdd0be01d09d3a6575fb242ad072227bb13e89474138695'
assert r['commit_sha']=='b1a3de693bbfae52f95de50e2bfc5285b6bcf63a' and r['tree_sha']=='57873bb631d64db81bf2d70107feb7b531b1eee0'
assert r['parent_sha']=='7aa3b5de5b0881dc83f633e5819235c3b2840c8f' and r['files']==16 and len(r['file_bindings'])==16
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==288 and x['current_active_batch']==[]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=288,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Whole402403 compiled/source-qualified/remote verified288 UNREVIEWED. Read all actual/expanded terminal280281 mathematical bodies and programs-as-DATA before independent reconstruction; freeze fresh native audit of point atoms/two-fibre generated uniqueness and continue actual compactness/existence/P12.3 residual at mostTWO. No count change, protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=288,commit=r['commit_sha'],files=16,verified=True,solved=16,open=26,papers=97),indent=2))
