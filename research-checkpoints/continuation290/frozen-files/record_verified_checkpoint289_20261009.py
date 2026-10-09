from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'; P=G/'push-receipt-continuation289.json'; M=G/'upload-manifest-continuation289.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='27f94ee0b23dd8d7b121f59e9d8d254048b59920ac9e276910bc98e59f1c06fd'
assert r['commit_sha']=='ce652496f2f82b2c883813592db7e414f11b25e7' and r['tree_sha']=='273c7d6c5cf481fb3699147afe64c573b3641562'
assert r['parent_sha']=='b1a3de693bbfae52f95de50e2bfc5285b6bcf63a' and r['files']==64 and len(r['file_bindings'])==64
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==289 and x['current_active_batch']==[282,283]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=289,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Whole compiled404405 and citation-only revised402403 verified289, all UNREVIEWED. Native282283 audit frozen full proofs and continue exact original P16.7/P12.3 residuals. ROOT advances actual decreasing-generated energy-class closure and compactness, retaining source qualifications. At mostTWO, no hot feedback/count change, protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=289,commit=r['commit_sha'],files=64,verified=True,solved=16,open=26,papers=97),indent=2))
