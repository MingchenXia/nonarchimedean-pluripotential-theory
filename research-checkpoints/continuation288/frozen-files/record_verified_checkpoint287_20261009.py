from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation287.json';M=G/'upload-manifest-continuation287.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='512d7c1b0ed761c24d72a3eb668b2954884ffdc5394aab8d6b8c82a971916f89'
assert r['commit_sha']=='7aa3b5de5b0881dc83f633e5819235c3b2840c8f' and r['tree_sha']=='da266c1729c8e762126ffb38256bf7fb775a27e3'
assert r['parent_sha']=='f6179edfdefcf078c5df4e52c51aebb89c241b98' and r['files']==68 and len(r['file_bindings'])==68
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==287
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=287,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Native280281 independently continue whole400398399 actual unbounded P16.7 and whole401 actual general P12.3 residual. ROOT pursue concrete actual MA atom/pointcontrol and remaining proofs. Whole400401 compiled/qualified/remotely verified287 UNREVIEWED; at mostTWO, no hot feedback/countchange; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=287,commit=r['commit_sha'],files=68,verified=True,solved=16,open=26,papers=97),indent=2))

