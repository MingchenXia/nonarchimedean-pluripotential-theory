from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

R = Path('/workspace/research')
now = datetime.now(timezone.utc).isoformat()

def bind(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

units = [
    ('Thuillier-tel-00010990v1.txt', 1424, 1468, 'All-domain G-site distinguished from the strict rigid site; complete selected definitions.'),
    ('Thuillier-tel-00010990v1.txt', 3350, 3445, 'Full proof of 2.3.8: finite separable embedding and semistable reduction for strict rig-smooth affinoid curves; following 2.3.9 and 2.3.10 complete, 2.3.11 prefix only.'),
    ('Thuillier-tel-00010990v1.txt', 4104, 4235, 'Complete definitions and proofs of 3.2.4 and 3.2.5; the latter uses the all-domain G-site, not the strict GJR site.'),
    ('Thuillier-tel-00010990v1.txt', 4235, 4300, 'Complete remaining density proof of 3.2.7, proof of 3.2.8 and complete 3.2.9 density argument.'),
    ('Thuillier-tel-00010990v1.txt', 2650, 2825, 'Complete 2.2.21 scalar skeleton statement and proof, preceding 2.2.20 complete; 2.2.22 statement and initial proof only.'),
    ('GJR-2111.05741.txt', 1818, 1939, 'Complete 5.11 finite-flat norm descent statement/proof and 5.12/5.13 scalar and Galois descent statements/proofs.'),
    ('Berkovich-PMIHES-1993-78-5.txt', 5475, 5545, '7.1.1 exact torsion comparison statement and proof prefix, not full proof. Published theorem used only with proper connected scheme, constant Z/2, degree zero.'),
    ('CD-1204.6277v2-20261004.txt', 10624, 10694, '8.9.4 complete statement including explicit smooth psh log-sum-exponential approximants; proof prefix, not full proof of its additional Monge-Ampere formula.'),
    ('CD-1204.6277v2-20261004.txt', 9726, 9795, 'Rechecked full 8.1.1 definitions, 8.1.2 proof, 8.1.4 ordinal definition/proof and 8.1.5 pullback proof. Definition permits -infinity; sequence closure explicit.'),
]
source_records = []
for name, first, last, scope in units:
    path = R / 'shared-sources' / name
    lines = path.read_text().split('\n')
    text = '\n'.join(lines[first-1:last])
    source_records.append({**bind(path), 'LF_first': first, 'LF_last': last,
                           'selected_unit_sha256': hashlib.sha256(text.encode()).hexdigest(),
                           'read_scope': scope})
source_record = {
    'recorded_utc': now, 'literal_units_read_untruncated': source_records,
    'reads_before_and_after_compaction_are_one_continuous_root_turn': True,
    'earlier_indispensable_foundation_reads': [
        str(R/'P03-public-primary-root-read-20261004.json'),
        str(R/'P03-additional-public-primary-root-read-20261004.json'),
        str(R/'P03-general-curve-realization-and-stage-root-read-20261004.json'),
        str(R/'P03-CLD-v2-primary-cache-and-root-read-20261004.json')],
    'R39_general_Thu_lisse_equals_strict_real_PL_premise': 'False as a blanket identification; final Theorem C retains the gap.',
    'R40_density_application': 'Uses ambient boundaryless projective curve and separately legalizes finite graph breakpoints; it does not import that false identification.',
    'new_theorem_independently_accepted': False, 'original_target_closed': False,
    'running_author_feedback_or_frozen_input_mutation': False,
}
(R/'P03-curve-final-source-applications-root-read-20261004.json').write_text(json.dumps(source_record, ensure_ascii=False, indent=2)+'\n')

pre_gap = R/'root-checks/P03.2-round39-preliminary-strict-PL-gap-20261004.md'
final_gap = R/'root-checks/P03.2-round39-final-strict-PL-gap-20261004.md'
assert not final_gap.exists()
final_gap.write_text(
    '# Final R39 proof gap: Theorem C is not verified\n\n'
    'The completed final core has SHA-256 4a4e66e6544c4ce2c9b2224e6f46d6cc2eb326ee769cb8be0d799e2491d67c38. '
    'Its proof of Theorem C still identifies every Thuillier-lisse subharmonic approximant with a strict GJR real-PL function. '
    'Actual canonical notes n1 and n2 retain that premise, and n3 imports its stage-3 conclusion. '
    'The complete final diff changes scope purity, formatting, the disc Shilov justification and reproduction instructions; it does not repair this premise.\n\n'
    'The following independently constructed preliminary gap proof applies unchanged to the final mathematical step. '
    'Its historical observations about a running author refer to the preliminary snapshot. Both authors have now completed; no feedback was sent.\n\n'
    + pre_gap.read_text() + '\n\n'
    'Final disposition: no acceptance of Theorem C or its stage-3 bundle consequence. '
    'The separate Theorems A/B and the split-node calculation do not use this premise, and were reconstructed separately; independent review is still pending. '
    'The conclusion of Theorem C is not disproved by this example. No original target is closed.\n')

for n, atom, tex_units, cell in [
    (39, 'P03.2', [[1,210],[211,420],[421,610],[611,820]], '1619'),
    (40, 'P03.3', [[1,110],[111,210],[211,350]], '1624'),
]:
    d = R/'root-checks'/f'public-curves-CLD-round-{n}-final-reader'
    snap = json.loads((d/'snapshot.json').read_text())
    preliminary = R/'root-checks'/f'public-curves-CLD-round-{n}-preliminary-reader'/f'{atom}-argument.md'
    repro = json.loads((d/'reproduction-result.json').read_text())
    assert repro['all_script_steps_succeeded'] and repro['core_tex_provenance_and_literal_units_identical']
    canonical = json.loads((d/'actual-canonical-notes.json').read_text())
    seen = set()
    for note in canonical:
        assert set(note['support']) <= seen
        seen.add(note['id'])
    native = {
        'recorded_utc': now, 'cell_id': cell,
        'source': str(d/f'{atom}-paper.tex'),
        'requested_sequence': ['open_in_codex', 'compile_latex_document after successful open'],
        'open_call_returned_a_result': False, 'compile_call_reached': False,
        'observed_output': 'No output or diagnostics before the still-running cell was terminated.',
        'editor_opening_confirmed': False, 'native_compilation_confirmed': False,
        'editor_close_requested': False, 'source_preserved': True,
        'fallback': 'Fresh local reproduction after complete source/script reads; no installation.',
    }
    (d/'native-request-unresponsive.json').write_text(json.dumps(native, ensure_ascii=False, indent=2)+'\n')
    record = {
        'recorded_utc': now, 'round': n, 'problem': atom,
        'full_argument_read': True,
        'argument_read_method': 'All preliminary core units read untruncated, followed by the full untruncated preliminary/final diff and all changed mathematical text; full final TeX also read.',
        'preliminary_binding': bind(preliminary), 'final_argument_binding': bind(d/f'{atom}-argument.md'),
        'all_actual_canonical_notes_read': True, 'canonical_binding': bind(d/'actual-canonical-notes.json'),
        'canonical_note_count': len(canonical), 'all_summary_detailedSummary_text_and_support_fields_read': True,
        'support_dag_checked': True, 'local_notes_not_assumed_canonical': True,
        'full_standalone_tex_read': True, 'tex_binding': bind(d/f'{atom}-paper.tex'), 'tex_read_LF_units': tex_units,
        'all_root_executed_generated_scripts_fully_read_before_execution': True,
        'scripts_executed': [step['command'] for step in repro['steps']],
        'package_notes_script_executed_by_root': False,
        'full_provenance_administrative_fields_and_checked_applications_read': True,
        'every_retained_published_page_claimed_fully_read': False,
        'foundation_scope': 'Exact applicable published statements and indispensable newly applied proof segments read; the embedded primary material includes additional pages not all claimed read.',
        'source_application_read_record': bind(R/'P03-curve-final-source-applications-root-read-20261004.json'),
        'provenance_binding': bind(d/'source-extracts/source-provenance.json'),
        'fresh_reproduction': bind(d/'reproduction-result.json'),
        'paper_first_page_inspected': True, 'first_page_finding': 'Legible; no visible clipping in the inspected page. Mathematical correctness is separate.',
        'mathematical_reconstruction': (
            'Stage-1 curve theorem, countable net extraction, ordinary smooth normalization descent, exact projective-space bundle reduction and the full node calculation reconstructed. Theorem C has an indispensable strict/non-strict G-site gap; no whole-paper acceptance.' if n==39 else
            'Legal local formal Cartier star realization; genus/cycle and boundary degree rules; graph obstacle; maximum-locus comparison for every analytic competitor and all scalar extensions; ambient arbitrary-obstacle density; legal-cut interpolation; finite Galois averaging/descent; common extension argument; proper fiber connectedness and exact entire-class/fiber-minimum descent; normalization sector and full node counterexample reconstructed. This is a sufficient sector, not the sharp classification.'),
        'unresolved_subsidiary_proof_gap': bind(final_gap) if n==39 else None,
        'independent_review_submitted': False, 'independent_review_pass': False,
        'mathematical_acceptance': False, 'original_target_closed': False,
        'all_42_original_targets_remain_open': True,
    }
    (d/'complete-root-read.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'round':n,'root_read':bind(d/'complete-root-read.json'),'original_target_closed':False},ensure_ascii=False))

active_path = R/'active-work.json'
active = json.loads(active_path.read_text())
active['updated_utc'] = now
for c in active['current_public_curves_and_CLD_batch']['campaigns']:
    n = c['round']; d=R/'root-checks'/f'public-curves-CLD-round-{n}-final-reader'
    c.update(state='Completed native author; entire core, actual canonical notes and standalone TeX read; fresh local reproduction passed; original sharp target still open.',
             root_read_record=str(d/'complete-root-read.json'), root_read_record_sha256=bind(d/'complete-root-read.json')['sha256'],
             reproduction_result=str(d/'reproduction-result.json'), reproduction_result_sha256=bind(d/'reproduction-result.json')['sha256'],
             independent_acceptance=False)
    if n==39: c['subsidiary_stage3_proof_gap'] = bind(final_gap)
active['goal_state'] = 'ACTIVE. All 42 original targets remain open. R39/R40 completed and locally reproduced; R39 Theorem C has a documented strict/non-strict G-site gap. Native editor requests were unresponsive. Independent reviews and GitHub checkpoint 43 exports remain awaiting specific approvals. No blocked action retried.'
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
checklist_path=R/'checklist-current.json'
checklist=json.loads(checklist_path.read_text()); assert checklist['fully_solved_original_atoms']==[]
checklist['updated_utc']=now
for target in checklist['targets']:
    if target['id']=='P03.2': target['current_focus']='R39 completed a scoped stage-1 curve/projective-space bundle draft and a full node obstruction. Full core, actual canonical notes and TeX read; 11-page fresh local reproduction passed. Subsidiary Theorem C and its stage-3 bundle extension have a documented strict/non-strict G-site gap and are not accepted. Stage-1 proof does not use that premise. No independent review or sharp-classification closure.'
    if target['id']=='P03.3': target['current_focus']='R40 completed an unverified full-family continuity draft on arbitrary compact strict rig-smooth affinoid curves, genus and cycles allowed, all scalar extensions, actual projective bundles and smooth proper projective factors, plus ground-field bijective normalization and a node counterexample. Full core, actual canonical notes and TeX read; 10-page fresh local reproduction passed. Exact independent review not yet submitted; original sharp classification remains open. Earlier R36/R38 review exports remain separately blocked pending approvals.'
checklist_path.write_text(json.dumps(checklist,ensure_ascii=False,indent=2)+'\n')
