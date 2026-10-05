from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re

R=Path('/workspace/research');G=R/'github-checkpoint'
D=R/'root-checks/P16.2-continuation115-valuative-primary'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
units=[]
for response_name,tag,start,end in [
    ('UFD-and-valuative-open.json','0AG0',24,29),
    ('UFD-and-valuative-open.json','0BX5',24,35),
    ('UFD-and-valuative-open.json','01KA',31,63),
    ('UFD-and-valuative-open.json','01KF',23,25),
    ('uniqueness-and-Pic-open.json','01KZ',22,23),
    ('uniqueness-and-Pic-open.json','0AFZ',22,24)]:
    p=D/response_name
    response=json.loads(p.read_text())
    text='\n'.join(c['text'] for c in response['content'] if c['type']=='text')
    blocks=text.split('\n\n--------------------------------------------------------------------------------\n')
    matching=[b for b in blocks if 'https://stacks.math.columbia.edu/tag/'+tag in b.split('\nL0:',1)[0]]
    assert len(matching)==1,(tag,len(matching))
    selected=[];coords=[]
    for line in matching[0].split('\n'):
        m=re.match(r'L(\d+):',line)
        if m and start<=int(m.group(1))<=end:
            selected.append(line);coords.append(int(m.group(1)))
    assert coords==list(range(start,end+1)),(tag,coords)
    unit=D/(tag+'-selected-renderer-unit.txt');assert not unit.exists()
    unit.write_text('\n'.join(selected)+'\n')
    units.append({'tag':tag,'url':'https://stacks.math.columbia.edu/tag/'+tag,
        'path':str(unit),'sha256':sha(unit),'original_response':str(p),'response_sha256':sha(p),
        'inclusive_zero_based_renderer_lines':[start,end],
        'extraction_rule':'Select exact Ln-prefixed renderer lines from the matching response block; keep labels and literal bytes; append one LF.',
        'entire_selected_mathematical_statement_and_printed_proof_root_read':True,
        'whole_primary_work_root_read':False,'recursive_cross_references_all_read':False})
note=R/'root-checks/P16.2-compatible-valuative-centers-and-local-factoriality-20261005-continuation115.md'
binding=D/'binding.json';assert not binding.exists()
binding.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_saved_note_root_read':True,'units':units,
    'independent_review_performed':False,'original_closed':False,
    'native112_113_private_outputs_read_or_used':False,'hot_feedback_sent':False},ensure_ascii=False,indent=2)+'\n')
receipt=json.loads((G/'push-receipt-continuation111.json').read_text())
assert receipt['commit_sha']=='fe9bf711957bc25366b945248332fd79369241dc'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation111.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']=None
    data['continuation115_unreviewed_P16_2_centers']={'binding':str(binding),'sha256':sha(binding),'original_closed':False,'published_in_checkpoint111':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_units':len(units),'binding':str(binding),'binding_sha256':sha(binding),
                  'latest_verified_commit':receipt['commit_sha'],'immutable_snapshot111_modified':False},indent=2))
