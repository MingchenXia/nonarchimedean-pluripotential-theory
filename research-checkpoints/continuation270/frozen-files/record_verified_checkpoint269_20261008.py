from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation269.json';M=G/'upload-manifest-continuation269.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='aff50af0d214e9eabdf0c50104da32c318930cf2b2873926d110aaebcdf9e8f2'
assert r['commit_sha']=='420a9e9014de25faf2f401497c3d718985cbf6d4' and r['tree_sha']=='26e9a3f225823c07c0c81af706d45e81437cca63'
assert r['parent_sha']=='180e0a53dd1e5937036fe1218a385bab3baa8632'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==269
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=269,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Continue TWO native267/P16.7 entire373374/originalall-supportE1 and268/P21.3 entire372/arbitrarypositive doubleclosedcurrent. Inspect ONLYsettledcompleteoutputs. Whole376 published269UNREVIEWED; ROOT independent residualprimary/modelresearch whilewaiting, nohotfeedback.16solved26OPEN97papers; protectededitorOPENUNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=269,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
