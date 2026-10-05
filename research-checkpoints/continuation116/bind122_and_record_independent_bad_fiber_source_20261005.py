from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
note=K/'P16-analytic-frame-invariance-and-integrable-local-weights-20261005-continuation122.md'
sources=[K/'P16.2-continuation117-common-collar-primary/complete-original-PL-contact-bridge-and-collar-reconstruction.LF25-149.txt',
         K/'P16.2-common-ample-collar-and-intrinsic-generated-local-operator-20261005-continuation117.md',
         K/'P16.2-all-point-continuous-canonical-reference-and-local-frame-compatibility-20261005-continuation119.md',
         K/'public-P16.5-round112-final-reader/P16.5-paper.md',
         K/'public-P16.2-round113-final-reader/P16.2-paper.md']
binding=K/'P16-continuation122-analytic-frame-and-weighted-local-binding.json'
save(binding,{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_saved_note_root_read':True,
    'sources':[{'path':str(p),'sha256':sha(p)} for p in sources],
    'independent_review_performed':False,'original_closed':False,
    'only_exact_actual_ample_G0_granted':True,
    'native114_115_private_outputs_read_or_used':False,'hot_feedback_sent':False,
    'whole_primary_works_root_read':False,'original_counts_incremented':False})
unit=K/'P16.2-continuation109-stacks-primary/0BFP-mathematical-body.txt'
response=K/'P16.2-root-independent-0BFP-response-20261005.json'
save(K/'P16.2-root-independent-bad-fiber-source-observation-20261005.json',{
    'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'url':'https://stacks.math.columbia.edu/tag/0BFP',
    'selected_primary_body':str(unit),'selected_primary_body_sha256':sha(unit),
    'entire_selected_statement_and_printed_proof_root_read':True,
    'fresh_native_web_response':str(response),'fresh_native_web_response_sha256':sha(response),
    'native_renderer_reference':'turn890829view0',
    'fresh_printed_statement_and_proof_renderer_lines':[22,38],
    'exact_application':'Normal-base proper birational modification is an isomorphism near the image of every quasifinite source point; every bad geometric fiber component is positive dimensional.',
    'source_hypotheses_checked':'Noetherian smooth normal integral base, proper birational modification, smooth reduced source; smoothness and geometric integrality retained under the geometric field extension.',
    'all_recursively_referenced_background_proofs_read':False,
    'independent_full_original_review_performed':False,'original_closed':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    data['updated_utc']=datetime.now(timezone.utc).isoformat()
    data['continuation122_unreviewed_analytic_frames_and_local_weights']={
        'binding':str(binding),'sha256':sha(binding),'original_closed':False,
        'frozen_reviews114_115_modified':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'binding':str(binding),'binding_sha256':sha(binding),
    'fresh_source_observation':str(K/'P16.2-root-independent-bad-fiber-source-observation-20261005.json'),
    'original_count_incremented':False},indent=2))
