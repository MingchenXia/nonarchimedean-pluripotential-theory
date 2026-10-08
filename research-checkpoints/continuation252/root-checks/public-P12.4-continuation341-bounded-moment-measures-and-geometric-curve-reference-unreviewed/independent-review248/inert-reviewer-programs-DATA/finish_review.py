"""Fresh delivery packager and consistency audit, no supplied executable calls."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def read_json(name):
    return json.loads((ROOT / name).read_text())
def save(name, obj):
    (ROOT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

metadata = [
 ('n1', 'Qualified G331/domain and whole input identity audited; actual and expanded notes remain distinct.',
  'Uses only the entire qualified independent cone grant. Retains all supports, actual bounded-D membership, n-1 arity, nonpure top-degree convention and all exceptional zero/unit/bottom/empty cases. Current and historical whole grant identities agree; no product theorem is imported.', ['G331']),
 ('n2', 'All-field mixed kernel independently supported; algebraic presentation independence supplies no Cartier/locality theorem.',
  'Reconstructs simultaneous superficial choices for both tuples, product/power linearity, integral-closure invariance and all-support test positivity. Infinite-field passage is algebraic only; units are separate and lower-dimensional coefficients vanish by convention.', ['G331','n1']),
 ('n3', 'Real C and actual bounded-D moment extension supported, including weak decreasing-net continuity at a specified bounded-D limit.',
  'Full positive-functional extension, common bounds, shift estimate, representation independence, scalar order, additivity and majorant formula are reconstructed. No measure-order assertion, increasing function closure, arbitrary infimum closure, flattened nested nets or locality follows.', ['G331','n1','n2']),
 ('n4', 'Exact single-factor gauge, actual residue-degree normalization and bounded smooth BFJ comparison supported with source qualification.',
  'BFJ applies only to smooth affine closed germs over algebraically closed characteristic-zero fields, dimension>=2. The 4.4 topological proof gives decreasing nets; 4.8 alone is sequential. SH17.4.7 has a literal missing-quotient printing issue, avoided by repeated17.4.6 in the final quotient.', ['G331','n1','n2','n3']),
 ('n5', 'Complete excellent reduced-curve geometric reference theorem supported at zero arity, with real Cartier/model comparison.',
  'Normalization dominates every actual primary curve blowup by a finite graph and closed generic-image argument. A normalization snake sequence proves proper Cartier degree with inseparable residue weights; all real presentations and common models are handled before moments. Includes k+t l[[t]], DVR/empty and exactly zero-arity locality/continuity.', ['G331','n1','n2','n3','n4']),
 ('n6', 'Nilpotent and nonpure diagnostics supported at exact scope; two-point toy is not the primary kernel.',
  'Proves reduced boundary data cannot recover unreduced lengths, and a nonzero lower-component input has zero top-degree moments. Fresh arithmetic PASS covers48 curve,8 nilpotent and27 gauge cases only, not universal geometry or arbitrary inputs.', ['G331','n1','n2','n3','n4','n5']),
 ('n7', 'Whole partial paper supported as an unverified review draft; entire original P12.4 remains OPEN, candidate=false.',
  'Higher-dimensional independent Cartier comparison and actual positive-arity open-set locality are unproved. Reviews whole-paper/source/evidence scope separately, leaves energy/general finite-map targets distinct, and does not infer acceptance from historical builds, provider labels or finite checks.', ['G331','n1','n2','n3','n4','n5','n6'])
]
proof = (ROOT / 'whole-proof.md').read_text()
sections = re.split(r'(?m)^## R[1-7]\. ', proof)[1:]
assert len(sections) == 7
notes = []
for (ident, summary, detail, support), section in zip(metadata, sections):
    body = '## ' + section
    body += '\n\nArtifacts: whole-proof.md, independent-review.md, whole-source-application-ledger.md, '
    body += 'whole-proof-coverage.md, original-scope-and-noncircularity.md, acceptance-decision.json, '
    body += 'native-notes.json and reports/. Rerun: python audit_packets.py; python own_evidence.py; '
    body += 'python finish_review.py. These commands audit bytes/finite observations, not mathematics. '
    body += 'ROOT owns compilation; no supplied program or TeX source is executed.\n'
    (ROOT / (ident + '.md')).write_text(body)
    notes.append({'id': ident, 'summary': summary, 'detailedSummary': detail,
                  'text': body, 'support': support})
save('native-notes.json', {'notes': notes, 'candidate': False})

judgments = [{'author_id': n['id'], 'actual': 'supported_independent_draft',
              'expanded': 'supported_independent_draft',
              'qualifications': n['detailedSummary']} for n in notes]
save('acceptance-decision.json', {
 'review_status': 'unverified_independent_review_draft',
 'review_implementation_delivered': True,
 'ROOT_acceptance_or_publication': False,
 'whole_paper_mathematics': 'partial_results_supported_at_exact_stated_domains',
 'per_note': judgments,
 'essential_source_applications': 'supported_with_explicit_SH17.4.7_printing_qualification',
 'author_mathematical_claim_replacement_required': False,
 'immutable_author_or_source_edited': False,
 'bounded_evidence': {'bound_bodies': 57, 'all_hashes_sizes_match': True,
   'actual_FINAL_notes': 7, 'expanded_notes': 7, 'actual_expanded_whole_equal': False,
   'controller_worker_decoded_whole_equal': True, 'whole_qualified_grant_equal': True,
   'historical_own_records': 62, 'directly_matched': 47, 'recovered_note_bodies': 7,
   'unavailable_historical_bodies': 8, 'fresh_pdf_pages': 15,
   'fresh_curve_arithmetic_cases': 48, 'fresh_nilpotent_cases': 8, 'fresh_gauge_cases': 27,
   'fresh_compilation': False, 'fresh_provider_attestation': False,
   'supplied_programs_executed_or_imported': False},
 'entire_original_P12_4': 'OPEN_NOT_SOLVED',
 'missing': ['independent_higher_dimensional_singular_Cartier_intersection_comparison',
             'actual_positive_arity_open_set_locality'],
 'curve_result': 'supported_independent_geometric_zero_arity_reference_only',
 'smooth_result': 'bounded_BFJ_recovery_only_smooth_affine_CLOSED_algebraically_closed_char0_dim_ge2',
 'P12_3_P12_5_general_P12_6': 'separate_unclaimed_targets',
 'candidate': False,
 'limitations': 'Historical labels/builds, matching bytes and finite checks do not establish mathematical correctness or original completion.'
})

required = ['independent-review.md','whole-proof.md','whole-source-application-ledger.md',
 'whole-proof-coverage.md','original-scope-and-noncircularity.md','acceptance-decision.json',
 'native-notes.json','bounded-evidence-input.json','source-qualification-addendum.md']
seen = {'G331'}
for n in notes:
    assert set(n['support']) <= seen
    assert n['text'] == (ROOT / (n['id'] + '.md')).read_text()
    seen.add(n['id'])
for name in required:
    assert (ROOT / name).is_file()
bindings = read_json('reports/input-bindings.json')
for entry in bindings:
    body = (ROOT / entry['local']).read_bytes()
    assert len(body) == entry['bytes']
    assert hashlib.sha256(body).hexdigest() == entry['sha256']
assert read_json('reports/own-exact-diagnostics.json')['status'] == 'PASS'
save('reports/final-integrity.json', {'status': 'PASS', 'notes': 7, 'candidate': False,
 'required': required, 'bound_bodies': len(bindings),
 'checks': ['required deliverables', 'earlier-only supports', 'full note-body consistency',
            'retained byte bindings', 'fresh declared finite observations'],
 'limits': 'Artifact consistency only; no mathematical checker, build, provider or ROOT acceptance attestation.'})
reading = {
 'mathematical': 'Complete TeX, whole argument, all7 actual FINAL objects and all7 expanded objects; expanded text exactly matches argument bodies. Whole G331 prompt/embedded components used with qualifications; separate components bound and identical.',
 'source_units': 'See whole-source-application-ledger.md; full immediate SH and BFJ application units freshly inspected, truncations repaired.',
 'pixels': [{'source': 'SH author PDF', 'pdf_page':154,'printed_page':140,'purpose':'integral-closure bars'},
            {'source': 'SH author PDF', 'pdf_page':370,'printed_page':356,'purpose':'literal colon-term missing quotient'},
            {'source': 'BFJ published PDF', 'pdf_page':33,'printed_page':481,'purpose':'multiplier dependence and topological decreasing-family proof'}],
 'not_claimed': ['whole fresh reading of all23 primary files','all manuscript PDF pages visually inspected',
                 'fresh TeX compilation','fresh provider attestation','unavailable original-task hash verification']}
save('reports/reading-boundary.json', reading)
files = []
for path in sorted(ROOT.rglob('*')):
    if not path.is_file():
        continue
    relative = path.relative_to(ROOT)
    if any(part.startswith('.') for part in relative.parts) or str(relative) == 'reports/own-bindings.json':
        continue
    body = path.read_bytes()
    files.append({'path': str(relative), 'bytes': len(body),
                  'sha256': hashlib.sha256(body).hexdigest()})
save('reports/own-bindings.json', {'files': files, 'self_exclusion': 'This manifest excludes itself.',
       'mathematical_status': 'Unverified independent-review drafts; original OPEN; candidate=false.'})
print(json.dumps({'status':'PASS','notes':7,'candidate':False,'required_deliverables':len(required),
                  'bound_bodies':len(bindings),'own_files':len(files)}))
