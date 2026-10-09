from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';P=G/'push-receipt-continuation292.json';M=G/'upload-manifest-continuation292.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='2055227edd71efdf65db17cc6d5f565d5e238cd9dcfe21d7d0880299d6039474'
assert r['commit_sha']=='348850f690b3a427e9b3788946b6261ba27d514f' and r['tree_sha']=='4839becc6a0fbf496e8491f6b8181fe8c364651e'
assert r['parent_sha']=='9e02dab574529993f85c368ef73c79ecab8d8517' and r['files']==32 and len(r['file_bindings'])==32
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==292 and x['current_active_batch']==[284]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=292,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Whole408 canonical obstacle filtration verified292, UNREVIEWED and compiler UNKNOWN/source preserved. Native284 continues general original P12.3 CE. ROOT reconstructs terminal282 full formal proof and new ordered energy-gap/arbitrary-net closure in sequence-generated G as409; then frozen P16.7 follow-up including whole406407409. At mostTWO, no hot feedback/count change; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=292,commit=r['commit_sha'],files=32,verified=True,solved=16,open=26,papers=97),indent=2))
