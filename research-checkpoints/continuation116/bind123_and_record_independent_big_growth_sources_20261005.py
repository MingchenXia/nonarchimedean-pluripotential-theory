from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
note=K/'P16-every-actual-big-bundle-numerical-and-section-growth-equivalence-without-Bertini-20261005-continuation123.md'
sources=[K/'public-P16.5-round112-final-reader/P16.5-paper.md',
         K/'public-P16.2-round113-final-reader/P16.2-paper.md',
         K/'public-P16.5-round112-final-reader/evidence/Fujino-Miyamoto-1.4-statement-and-proof-rendered.txt']
responses=[K/'P16-root-independent-big-growth-01Q3-0B5T-0BEM-response-20261005.json',
           K/'P16-root-independent-positive-ample-degree-0BEV-0BJ8-response-20261005.json']
primary=[
    {'tag':'01Q3','native_renderer_reference':'turn612231view2','whole_printed_statement_and_proof_read_lines':[23,67]},
    {'tag':'0B5T','native_renderer_reference':'turn612231view0','whole_printed_statement_and_proof_read_lines':[22,52]},
    {'tag':'0BEM','native_renderer_reference':'turn612231view1','whole_printed_statement_and_proof_read_lines':[22,43]},
    {'tag':'0BEV','native_renderer_reference':'turn407445view1','whole_printed_statement_and_proof_read_lines':[23,29]},
    {'tag':'0BJ8','native_renderer_reference':'turn407445view0','whole_printed_statement_and_proof_read_lines':[22,28]}]
for p in primary:
    p['url']='https://stacks.math.columbia.edu/tag/'+p['tag']
    p['entire_printed_statement_and_proof_root_read']=True
    p['all_recursively_referenced_background_proofs_read']=False
binding=K/'P16-continuation123-full-big-domain-and-growth-binding.json'
save(binding,{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_final_saved_note_root_read':True,
    'sources':[{'path':str(p),'sha256':sha(p)} for p in sources],
    'actual_native_source_responses':[{'path':str(p),'sha256':sha(p)} for p in responses],
    'fresh_primary_units':primary,
    'retained_scope':'Smooth integral projective positive-dimensional Y over every algebraically closed characteristic-zero k; actual rational bundles, all numerically trivial twists retained.',
    'application':'Equivalent numerical big interior, positive section-growth limsup and actual rational ample-plus-effective presentation; proper original X uses separately proved actual H0 pullback identity.',
    'independent_review_performed':False,'original_closed':False,
    'native114_115_private_outputs_read_or_used':False,'hot_feedback_sent':False,
    'all_recursively_referenced_background_proofs_read':False,
    'original_counts_incremented':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['continuation123_unreviewed_full_big_domain']={
        'binding':str(binding),'sha256':sha(binding),'original_closed':False,
        'frozen_reviews114_115_modified':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'binding':str(binding),'binding_sha256':sha(binding),
    'fresh_primary_tags':[p['tag'] for p in primary],
    'original_count_incremented':False},indent=2))
