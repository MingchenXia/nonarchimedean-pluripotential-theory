from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); G=R/'github-checkpoint'
P=G/'push-receipt-continuation285.json'; M=G/'upload-manifest-continuation285.json'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(P.read_text())
assert sha(M)==r['manifest_sha256']=='b4b8a62c3c70acb8d7e873b71198fbc00aed6bfedbc93b1d15c26658abd45c3b'
assert r['commit_sha']=='80475a6b047ac041dd4173dcf0b75267b0113430' and r['tree_sha']=='a6b33e759734e3c43e7863d0b906da721d668be7'
assert r['parent_sha']=='d2a8d1809109dbe2cfc92e69b30fb625d0c80ec7' and r['files']==47 and len(r['file_bindings'])==47
assert all(e['verified'] for e in r['file_bindings']) and not r['force_update']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text()); assert x['github_pending_checkpoint']['continuation']==285
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=285,commit=r['commit_sha'],tree=r['tree_sha'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=r['verified_utc'],ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Native278 corrected formalCE and279 full uniqueness/compactness remain independent, at mostTWO. ROOT398 local analytic divisor extension and exact pluriharmonic recognition gate, source-qualified own mathematics. No active math read/hot feedback or closure/countchange; protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checkpoint=285,commit=r['commit_sha'],files=47,verified=True,solved=16,open=26,papers=97),indent=2))
