from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');G=R/'github-checkpoint';P=G/'push-receipt-continuation293.json';M=G/'upload-manifest-continuation293.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='d1ac1ffd816dc5fc9243f540704bc356f34f131de80f2f60e36402686eedb546'
assert r['commit_sha']=='ea296f0c4988436141045660ae4ac0d23c6047d1' and r['tree_sha']=='81bf23aec4971d63ebba4f2df90722bbc66c934b'
assert r['parent_sha']=='348850f690b3a427e9b3788946b6261ba27d514f' and r['files']==35 and len(r['file_bindings'])==35
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==293 and x['current_active_batch']==[285]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=293,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Whole compiled409 verified293, UNREVIEWED. Native285 advances original P16.7 NONORDERED compactness/envelopes/existence using whole406407409. ROOT reads terminal284 distinct full expanded formal quotient-envelope proof/ledger/programs-as-DATA and applies whole BFJ immediate source before reconstruction410 and frozen P12.3 follow-up. At mostTWO, no hot feedback/count change; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(checkpoint=293,commit=r['commit_sha'],files=35,verified=True,solved=16,open=26,papers=97),indent=2))
