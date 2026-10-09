from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation296.json';M=G/'upload-manifest-continuation296.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='c5a29fbd51a894cff3c64332fd9d889ea7abe6fa3c634428ba991947986de76f'
assert r['commit_sha']=='950fb067dc6af402bf0c34225a728971cf093b2f' and r['tree_sha']=='754d99e453dc004c2b02142f5e6f88c5c5f318c3'
assert r['parent_sha']=='974cae4738cff711f09e9e3b32e5748fa8d16094' and r['actual_file_count']==34 and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==296 and x['current_active_batch']==[287]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,
        latest_verified_github_checkpoint=dict(continuation=296,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['recorded_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),
        next_work='Whole compiled412 verified296, UNREVIEWED. Native287 advances whole411412 P16.7 universal variational limits. ROOT reconstructs whole terminal286 P12.3 field/root descent after all five actual notes and five distinct expanded proofs were physically read; audit remaining native programs solely as DATA, exact current primary application units and formal preamble/scope; compile413 then freeze288. At mostTWO, no hot feedback/count change; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=296,commit=r['commit_sha'],files=34,verified=True,solved=16,open=26,papers=97),indent=2))
