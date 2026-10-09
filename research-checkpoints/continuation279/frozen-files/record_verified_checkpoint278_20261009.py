from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation278.json'; M=G/'upload-manifest-continuation278.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='825d6b6661bfeb984a2301c1c54d37611e0b085dff00609cda71b77fbdb0d8d5'
assert r['commit_sha']=='e9593cf1a49f8d9aca8cdd2e7add95a4ba192041' and r['tree_sha']=='88428bb5a2d1d686afd7ec12180d3c3336960bfa'
assert r['parent_sha']=='a9d7d960ddc0dafaebd5b85e12cc8b9794a2b16b'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==278
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=278,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Native273 fullboundedCtheta tangent/fullradialdual/intrinsicE1 and native274 whole386/Jensen/completion/originalP12.3 continue, at mostTWO. EntireROOT388 published UNREVIEWED, not fed back; independently review complete nativeFINAL before any acceptance/countchange. General E1/arbitrarysupport and P12.3 residualOPEN;16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=278,commit=r['commit_sha'],files=r['files'],remote_verified=True,solved=16,open=26,papers=97),indent=2))
