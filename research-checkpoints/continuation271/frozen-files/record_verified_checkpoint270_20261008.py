from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation270.json';M=G/'upload-manifest-continuation270.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='d9cfce5a470c688c2abb39ed98d6bfd2ed549861b6a71b8d9205c0706bfaf793'
assert r['commit_sha']=='2730e26317220798fd1695df88a0c7afe0b5abc0' and r['tree_sha']=='e13566419bb91541bbbbeb5e5d8e2974e20b542d'
assert r['parent_sha']=='420a9e9014de25faf2f401497c3d718985cbf6d4'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==270
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=270,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Launch frozen native270 ENTIRE378/P16.7 Picard and intrinsic E1 as second campaign with native269 ENTIRE377/P12.3. Whole377378 published270 UNREVIEWED; read completed268 whole paper/source and independently pursue gaps.16solved26OPEN97papers, protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=270,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
