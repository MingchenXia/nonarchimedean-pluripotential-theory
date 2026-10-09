from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint'
P=G/'push-receipt-continuation295.json';M=G/'upload-manifest-continuation295.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='c43d4402404edc87013ecec30b6991a81a85d4e147dec9baf979e66ede404863'
assert r['commit_sha']=='974cae4738cff711f09e9e3b32e5748fa8d16094' and r['tree_sha']=='3b2b0735acd2c311964aa6c0bfcbe7c95b83022c'
assert r['parent_sha']=='9e2205b4b46953624b4a73018cb9bea6e0c4894a' and r['files']==14 and len(r['file_bindings'])==14
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert x['github_pending_checkpoint']['continuation']==295 and x['current_active_batch']==[286]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,
        latest_verified_github_checkpoint=dict(continuation=295,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),
            receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,
            all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),
        next_work='Whole compiled ROOT411 verified295, UNREVIEWED. Native286 continues general P12.3. ROOT reads terminal285 distinct expanded formal nonordered midpoint/absolute-moment/maximum-energy proof and all programs-as-DATA before full reconstruction412, then freezes next P16.7 with whole411 universal coercivity. At mostTWO, no hot feedback/count change; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=295,commit=r['commit_sha'],files=14,verified=True,solved=16,open=26,papers=97),indent=2))
