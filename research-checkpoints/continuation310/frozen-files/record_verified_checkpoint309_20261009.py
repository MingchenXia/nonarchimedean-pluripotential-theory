"""Record independently verified NONFORCE309 without mathematical acceptance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research')
K=R/'root-checks'
G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
Q=G/'push-receipt-continuation309.json'
q=load(Q)
assert q['continuation']==309 and q['commit_sha']=='9556f41667eb56aea7e4ec0ddf1b8665a320698e'
assert q['tree_sha']=='fcdba33ef15df4736ced1664baccd73a184f7b09' and q['parent_sha']=='91609cb14e933072e9a6199014a5a443284d3717'
assert not q['force_update'] and q['file_count']==64 and q['remote_blobs_verified']==63 and q['remote_actual_tree_nodes_verified']==13
assert all(q[k] for k in ['remote_ref_verified','remote_commit_parent_and_tree_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
M=G/'upload-manifest-continuation309.json'
assert sha(M)==q['manifest_sha256']=='226d679b021daa8d98f390ee14f9f49e918d056581376f44b5b44974ae344bd3'
m=load(M)
assert len(m['files'])==m['file_count']==63
for e in m['files']:
    assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    assert y['github_pending_checkpoint']['continuation']==309 and y['latest_verified_github_checkpoint']['continuation']==308 and y['current_active_batch']==[298]
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
    y.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=309,commit_sha=q['commit_sha'],tree_sha=q['tree_sha'],parent_sha=q['parent_sha'],receipt=str(Q),receipt_sha256=sha(Q),manifest=str(M),manifest_sha256=sha(M),verified_utc=q['verified_utc'],force_update=False,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True),next_work='NONFORCE309 verified WHOLE429430 and frozen native298 inputs. Retain independent WHOLE431 normal finite-cover maxima and envelope transfer before any native297 terminal mathematical inspection; then inspect only settled297 actual FINAL. Active298 remains isolated with no mathematical inspection or hot feedback. Counts/editor unchanged; compilation unverified.')
    p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=309,commit=q['commit_sha'],verified=True,pending=None,current_active_batch=[298],solved=16,open=26,accepted_scoped_papers=97),indent=2))
