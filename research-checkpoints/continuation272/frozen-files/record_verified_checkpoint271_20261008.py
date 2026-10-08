from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation271.json';M=G/'upload-manifest-continuation271.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='4098c1cd716e23a4b4aafa562716dd85e79abae55eda64f6ff14fa28a6fb69a0'
assert r['commit_sha']=='cdabc6a12258ca4bb6d3779feaddac1614943014' and r['tree_sha']=='e82b7d39f646cf945aac0ae518d63c3b1bbad9c9'
assert r['parent_sha']=='2730e26317220798fd1695df88a0c7afe0b5abc0'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==271
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=271,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Continue TWO native269 P12.3 entire377 and270 P16.7 entire378; inspect only completed outputs. Whole379380 published271 UNREVIEWED. ROOT independent mathematical/source gate work, no active feedback.16solved26OPEN97papers, protected editor unchanged.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=271,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
