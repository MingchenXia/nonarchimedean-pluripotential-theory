from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation268.json';M=G/'upload-manifest-continuation268.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads(P.read_text())
assert sha(M)==receipt['manifest_sha256']=='e1cb8bcf06aa49d8693e68549ca2ee95fa9dbce803dc33f14922dfb3ec311da6'
assert receipt['commit_sha']=='180e0a53dd1e5937036fe1218a385bab3baa8632' and receipt['tree_sha']=='c629125290113e99edb641f603fd3b663bb63db8'
assert receipt['parent_sha']=='d3fe5ddd455ddf4cffdef62207d321c87b202b40'
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not receipt['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==268 and len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=268,commit=receipt['commit_sha'],tree=receipt['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=receipt['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Continue native267 independentWHOLE373374 sourcegate and originalP16.7 fullintrinsicE1. Read ENTIRE settlednative265 actualFINAL/wholepaper/newproof/source/scope, then stage376. Nextfreedslot P21.3 WHOLE372 independentcompletion.268publishedwhole374375unreviewed.16solved26OPEN97papers; protectededitorOPENUNCHANGED; no activeoutputmath/hotfeedback.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=268,commit=receipt['commit_sha'],files=receipt['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
