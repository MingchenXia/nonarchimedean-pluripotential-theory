from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def file(p):
    p = Path(p)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}
def save(p, v):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
common = {'recorded_utc': now, 'whole_final_own_note_root_read': True,
          'independently_reviewed': False, 'new_original_closure': False,
          'active_frozen114_116_modified_or_hot_feedback_sent': False,
          'whole_third_party_PDF_images_extended_responses_uploaded': False,
          'whole_primary_work_or_recursive_background_read': False}
v125 = dict(common)
v125.update({
    'own_note': file(K / 'P16-continuous-local-products-and-signed-CLN-estimate-20261005-continuation125.md'),
    'source': 'Boucksom--Eriksson, arXiv1805.01016v3,99 pages',
    'primary_PDF_local_only': file(R / 'shared-sources/BE-1805.01016v3-official-20261005-continuation69.pdf'),
    'native_response_local_only': file(K / 'P16-root-independent-BE-continuous-product-native-response-20261005.json'),
    'full_selected_statement_and_printed_proof_readings': [
        {'reference': 'turn273342view0', 'units': 'Example7.12--Theorem7.14 and proof', 'renderer_lines': [3894, 3908]},
        {'reference': 'turn273342view1', 'units': 'Proposition8.3 complete proof and Theorem8.4/Proposition8.5 statements', 'renderer_lines': [4305, 4370]},
        {'reference': 'turn273342view2', 'units': 'Lemma8.6 full statement/proof and Theorem8.4 full global proof', 'renderer_lines': [4376, 4516]}],
    'visually_read_exact_local_printed_page57': file(K / 'P16-root-BE8.6-sign-reading-20261005/printed-page57.png'),
    'native_screenshot_returned_image': False,
    'own_clarification': 'Stokes equality has minus; the absolute-value uniform-continuity estimate survives by triangle inequality. Finite continuous local metric products require the actual reference frame weight. G0, rather than uniform convergence alone, supplies the distinct bounded discontinuous passage.',
    'historical_note_header': 'Written before canonical115; it is preserved. This later observation supplies no new premise to the accepted P16.2 proof.'
})
save(K / 'P16-root-continuation125-continuous-products-reading-binding.json', v125)
v126 = dict(common)
v126.update({
    'own_note': file(K / 'P16.3-fixed-vertical-test-ideal-defect-and-envelope-estimate-20261005-continuation126.md'),
    'source': 'Fang--Gubler--Kunnemann, arXiv2203.12282v2; Nagoya259(2025),548--561,DOI10.1017/nmj.2025.8',
    'primary_PDF_local_only': file(R / 'shared-sources/FGK-2203.12282v2-20261005.pdf'),
    'literal_extract_local_only': file(R / 'shared-sources/FGK-2203.12282v2-20261005.txt'),
    'native_responses_local_only': [file(K / name) for name in [
        'P16.3-root-FGK-v2-first-native-response-20261005.json',
        'P16.3-root-FGK-v2-exact-find-native-response-20261005.json']],
    'local_reading_coordinates': 'Literal LF split, not Python splitlines; form feeds are not line breaks.',
    'whole_selected_local_statement_and_proof_ranges': [[287, 420], [420, 555], [556, 710]],
    'full_selected_local_units': ['Definitions/Remark4.2', 'Lemma4.4', 'Lemma4.6', 'Theorem4.7', 'Theorem5.1', 'Definitions6.1/6.3', 'Lemma6.4', 'Theorem7.1', 'Theorem8.1', 'Remark8.2'],
    'native_find_response_not_claimed_as_contiguous_full_Theorem5_1_proof': True,
    'fresh_Stacks_native_response': file(K / 'P16.3-normal-localization-native-primary-response-20261005.json'),
    'Stacks_attribution': 'The Stacks Project; tags031T/01P7; GNU Free Documentation License. Original open web response preserved without mathematical editing.',
    'full_Stacks_statement_and_proof_readings': [
        {'url': 'https://stacks.math.columbia.edu/tag/031T', 'reference': 'turn637150view0', 'renderer_lines': [23, 33], 'application': 'Normal Noetherian height-one intersection in local bundle frames'},
        {'url': 'https://stacks.math.columbia.edu/tag/01P7', 'reference': 'turn637150view1', 'renderer_lines': [23, 40], 'application': 'Generic sections extend after multiplying by a uniformizer power on a qcqs model'}],
    'own_result': 'Fixed vertical ideal contributes bounded O(1/m) error; subadditivity and uniform global generation give an all-point uniform model-envelope estimate while retaining the actual generic bundle.',
    'unproved_inputs': ['Pointwise model envelope input', 'Arbitrary-dimensional resolution/cofinal regular and SNC models', 'Unbounded genuine finite-energy operator and arbitrary-support equation beyond the exact source scope']
})
save(K / 'P16.3-root-continuation126-vertical-defect-reading-binding.json', v126)
canonical = K / 'P16.5-round114-actual-full-original-review-20261005.json'
v = json.loads(canonical.read_text())
assert v['verdict'] == 'INCONCLUSIVE'
assert sha(canonical) == 'ad2a0471f1fa3259741dbb430b6bc46c8642b005d8456c9f88b7e8f78634162d'
assert len(v['premises']) == 9 and len(v['passages']) == 16
for p in v['passages']:
    assert 0 <= p['premise'] < 9
    assert p['statement'] == v['premises'][p['premise']]
    assert p['url'].startswith('https://')
assert {p['premise'] for p in v['passages']} == set(range(9))
review_binding = {
    'recorded_utc': now, 'canonical': file(canonical), 'verdict': v['verdict'],
    'operation_id': v['operationId'], 'reported_utc': v['reportedAt'],
    'entire_report_all9_premises_all16_passage_objects_root_read': True,
    'all_zero_based_exact_statement_bindings_verified': True,
    'canonical_verdict_overridden': False, 'original_P16_5_closed': False,
    'accepted_scoped_paper_count_incremented': False,
    'precise_supported_scope': 'Prescribed actual L=A+D on the original smooth projective trivially valued characteristic-zero variety, whole actual big rational L domain; raw A^n, plus effective full-divisor zero-volume mass0 extension.',
    'remaining_original_obligations': [
        'Minimal-singularity or general model references with genuine big-class volume mass',
        'Arbitrary nonbig pseudoeffective data without an effective full-divisor reference; intrinsic operator and correct uniqueness formulation',
        'Reference compatibility for any claimed class-intrinsic equation or entire PSH(L) theorem'],
    'two_harmless_clarifications': ['Smaller auxiliary scaling-ray parameter in section3.4', 'Empty obstacle feasible cone has envelope minus infinity in section5.2'],
    'report_passage_mismatch': 'Final report mentions passages marked minus1 for task grant; actual canonical passages contain exactly16 HTTPS objects at indices0--8 and no minus1/URN object. No nonexistent passage is asserted as read.',
    'whole_original_packet_root_read_previously': True,
    'current_extended_native_inspection_wholly_root_read': False,
    'fresh_independent_primary_reading_by_root_for_this_verdict': False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened': False
}
save(K / 'P16.5-round114-canonical-reading-and-open-scope-binding-20261005.json', review_binding)
print(json.dumps({'bound_own_notes': [125, 126], 'review114': 'INCONCLUSIVE',
                  'original_count_unchanged': 7, 'scoped_paper_count_unchanged': 44}, indent=2))
