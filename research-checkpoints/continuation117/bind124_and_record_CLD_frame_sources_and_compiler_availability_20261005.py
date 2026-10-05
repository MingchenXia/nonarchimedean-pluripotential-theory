from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
note=K/'P16.5-explicit-big-nonnef-reference-mass-and-nested-types-20261005-continuation124.md'
response=K/'P16.5-root-independent-0AGQ-blowup-response-20261005.json'
cld=K/'P16-root-independent-CLD-analytic-frame-application-observation-20261005.json'
c=json.loads(cld.read_text())
assert sha(c['native_response']['path'])==c['native_response']['sha256']
assert not c['reading_limits']['original_closed']
binding=K/'P16.5-continuation124-explicit-big-nonnef-reference-binding.json'
save(binding,{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'note':str(note),'note_sha256':sha(note),'entire_final_saved_note_root_read':True,
    'actual_native_source_response':{'path':str(response),'sha256':sha(response)},
    'primary':{'url':'https://stacks.math.columbia.edu/tag/0AGQ',
        'tag':'0AGQ','native_renderer_reference':'turn677588view0',
        'whole_printed_statement_and_proof_read_lines':[22,42],
        'entire_printed_statement_and_proof_root_read':True,
        'all_recursive_background_proofs_read':False,
        'application':'Blowup of the two-dimensional regular local ring at a plane point: exceptional P1 and normal bundle O(-1).'},
    'retained_scope':'Explicit blowup P2 at a k-point over every algebraically closed trivially valued characteristic-zero k; a>0 and epsilon in (0,1) rational; actual L=H+aE and A=H-epsilon E.',
    'algebraic_conclusions':'Actual very ample decompositions, h0 and volume1, L nonnef, nested genuinely distinct original-carrier singularity cones.',
    'operator_mass_application':'If the proposed intrinsic local operator is reconstructed, its retained-type raw mass is A^2=1-epsilon^2, not automatically vol(L) or L^2. This note does not prove that local operator.',
    'sources':[{'path':str(K/'public-P16.5-round112-final-reader/P16.5-paper.md'),
                'sha256':sha(K/'public-P16.5-round112-final-reader/P16.5-paper.md')}],
    'independent_review_performed':False,'original_closed':False,
    'frozen_reviews114_115_modified':False,'hot_feedback_sent':False,
    'original_counts_incremented':False})
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    data['updated_utc']=now
    data['continuation124_unreviewed_explicit_big_nonnef_reference_masses']={
        'binding':str(binding),'sha256':sha(binding),'original_closed':False,
        'frozen_reviews114_115_modified':False}
    data['independent_CLD_analytic_frame_application_check']={
        'observation':str(cld),'sha256':sha(cld),'full_primary_work_read':False,
        'new_original_acceptance':False}
    data['native_compiler_availability_observation_20261005_1955']={
        'previous_cells':[815,831,885],
        'returned_result':'Dynamic app tool no longer available; no compile diagnostics or success returned.',
        'new_compile_cell':1231,
        'new_source':'/workspace/research/deliverables/original-P13.2/P13.2-paper.tex',
        'new_source_sha256':sha(R/'deliverables/original-P13.2/P13.2-paper.tex'),
        'new_status':'Pending; no success asserted',
        'editor_modified_replaced_or_new_tab_opened':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'binding':str(binding),'binding_sha256':sha(binding),
    'original_count_incremented':False,'native_compile_success_asserted':False},indent=2))

