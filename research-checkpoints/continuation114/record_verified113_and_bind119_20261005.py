from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
note=K/'P16.2-all-point-continuous-canonical-reference-and-local-frame-compatibility-20261005-continuation119.md'
binding=K/'P16.2-continuation119-continuous-canonical-reference-binding.json'
assert not binding.exists()
dependencies=[]
for p in [K/'P16.2-continuation110-primary-units/binding.json',
          K/'P16.2-continuation115-valuative-primary/binding.json',
          K/'P16.2-continuation117-local-operator-binding.json',
          K/'public-P16.5-round112-final-reader/external-premise-ledger.json']:
    dependencies.append({'path':str(p),'sha256':sha(p)})
binding.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_saved_note_root_read':True,
    'unreviewed_dependencies':dependencies,'independent_review_performed':False,'original_closed':False,
    'exact_actual_ample_G0_only':True,'native113_114_private_outputs_read_or_used':False,
    'hot_feedback_sent':False,'whole_primary_works_root_read':False},indent=2)+'\n')
receipt=json.loads((G/'push-receipt-continuation113.json').read_text())
assert receipt['commit_sha']=='bc70815f2502f7232c0648f6ee6c42226c6200d0'
assert sha(G/'upload-manifest-continuation113.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']=None
    data['continuation119_unreviewed_original_canonical_reference']={'binding':str(binding),'sha256':sha(binding),'original_closed':False,'published_in_checkpoint113':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'binding':str(binding),'binding_sha256':sha(binding),
    'verified_commit':receipt['commit_sha'],'immutable_snapshot113_modified':False},indent=2))
