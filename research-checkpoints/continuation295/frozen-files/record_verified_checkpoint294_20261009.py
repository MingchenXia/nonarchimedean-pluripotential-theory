from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation294.json';M=G/'upload-manifest-continuation294.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='b11bc87e41918c97e0606c025357756383a033b6db73f9d1697db9eeb3efbda8'
assert r['commit_sha']=='9e2205b4b46953624b4a73018cb9bea6e0c4894a' and r['tree_sha']=='e93a258f6fc50d6fb96e342f8e24d2103c809b10'
assert r['parent_sha']=='ea296f0c4988436141045660ae4ac0d23c6047d1' and r['files']==36 and len(r['file_bindings'])==36
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==294 and x['current_active_batch']==[285,286]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,
        latest_verified_github_checkpoint=dict(continuation=294,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),
            receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,
            all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),
        next_work='Whole compiled410 verified294, UNREVIEWED. Native285 advances P16.7 nonordered compactness/envelopes/arbitrary-support existence; native286 reconstructs whole410 and advances general excellent/mixed/imperfect P12.3 CE. ROOT continues independent mathematics and essential source work; only compact status before settlement. At mostTWO, no hot feedback/count change; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=294,commit=r['commit_sha'],files=36,verified=True,solved=16,open=26,papers=97),indent=2))
