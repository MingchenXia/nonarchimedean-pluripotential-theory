from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation283.json';M=G/'upload-manifest-continuation283.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='68e6ce6ddb37b9e6df49c98aa769b8ed101bd6677e50ae93ef4f5a3c6e0336c6'
assert r['commit_sha']=='1771c0c5bdd98de2bb4ffc03f381b3f3de94f3fa' and r['tree_sha']=='ebfb493f26a3ae174a50db44b5cc583ec8844226'
assert r['parent_sha']=='8fdefde6823413db47641042e3f7ce87c7f24dc8'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==283
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=283,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Independent native276 formalBIG and277 intrinsicE1 continue, at mostTWO. ROOT verify actual classical-psh/max-principle sources and surface compactness/uniqueness gates. No acceptance/closure/countchange; protected editor OPEN UNCHANGED.');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=283,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
