from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation275.json'; M=G/'upload-manifest-continuation275.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='1ee7abe5ef654410cd1f250d1a1f13cf09b2c872fa3b605f9fded04f4c3cc3c7'
assert r['commit_sha']=='1fcb952cc79d605ab2bde0ecb714354b9d9980dd' and r['tree_sha']=='061217e4146a136c409bb888f87cd09de66c5a30'
assert r['parent_sha']=='1d9276b93a30c6ad00d030b3a8d4521e0975b284'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==275
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=275,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Launch frozen native273 entire384385387383 and FULLboundedCtheta tangent/dual-admissibility gate. Prepare nextP12.3 whole386/Jensen/completion residual, maximumTWO. Whole385386387 published275 UNREVIEWED, no countincrease/originalclosure. All fullprimary/bookbodiesLOCALONLY; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=275,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
