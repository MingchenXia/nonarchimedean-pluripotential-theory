from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
note=K/'P16.2-entire-divisor-cone-by-normalized-ample-finite-suprema-20261005-continuation120.md'
binding=K/'P16.2-continuation120-finite-supremum-cone-binding.json';assert not binding.exists()
sources=[]
for p in [K/'public-P16.2-round113-final-reader/P16.2-paper.md',
          K/'public-P16.5-round112-final-reader/P16.5-paper.md',
          K/'public-P16.5-round-105-terminal-draft-reader/preserved/block-00.md']:
    sources.append({'path':str(p),'sha256':sha(p)})
binding.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_saved_note_root_read':True,
    'sources':sources,'independent_review_performed':False,'original_closed':False,
    'only_exact_actual_ample_G0_granted':True,'native114_115_private_outputs_read_or_used':False,
    'hot_feedback_sent':False,'whole_primary_works_root_read':False},indent=2)+'\n')
receipt=json.loads((G/'push-receipt-continuation114.json').read_text())
assert receipt['commit_sha']=='1f36b4819cef7942581cbba13f2030d27f3a6b22'
assert sha(G/'upload-manifest-continuation114.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']=None
    data['continuation120_unreviewed_entire_cone']={'binding':str(binding),'sha256':sha(binding),'original_closed':False,'published_in_checkpoint114':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'binding':str(binding),'binding_sha256':sha(binding),
    'verified_commit':receipt['commit_sha'],'immutable_snapshot114_modified':False},indent=2))
