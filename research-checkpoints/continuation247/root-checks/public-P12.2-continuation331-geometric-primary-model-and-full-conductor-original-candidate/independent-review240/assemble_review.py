"""Assemble fresh review prose and observational reports; no candidate code imports."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]

rows = [
 ('Compact boundary, full-support lifts and exact conductor/completion rules pass for excellent positive-dimensional local reduction; nilpotents and empty field factors are handled.',
  'Reconstructs bounded positive primary-gauge denominators, quotient-first finite field lifts, normalization local centres, finite OPEN singleton fibres and CLOSED quotient fibres at infinity. Completion covers all supports and primary contraction is exact.', []),
 ('All-component integral dependence and one common contraction exponent pass; normal-domain Izumi and excellent-domain residue hypotheses are checked.',
  'Zero-dimensional nonunit components require Q-image zero, supplied by a positive boundary-ideal power. Finite graded-algebra generation gives the common exponent. Exact normal completion, dimension formula and Rees residue degree justify the characteristic-free nonunit order bound; units are separate.', ['n1']),
 ('The rational difference lattice and canonical normal-domain trace pass with full fibres, inseparable lengths and primary-gauged continuity.',
  'Uniform closure gives a REAL lattice without an irrational integer formula. Norm coefficients lie in the normal target; quotient Gauss valuations cover nonminimal supports. Finite fibre measures have full support and normalized positive weights at least 1/n; arbitrary vertical sources receive no invented generic degree.', ['n1']),
 ('Continuous positive descent passes by exact conductor contraction and compact approximation, including arbitrary reduced finite injections.',
  'Uses dimension induction, ALL components, a common integral-dependence exponent and internal dyadic monotonicity. Finite-conductor errors and quotient estimates at infinity are separated. Reduced base change is injective by spectra. Only Q subset N subset C and equal uniform closures are claimed.', ['n1','n2','n3']),
 ('Strictly negative D-descent passes for unbounded and partial-bottom profiles using an actual decreasing net of majorants.',
  'Finite positive gaps and compact strict insertion replace unsupported nested-net flattening. Rational quotient approximation, primary-factor contraction and positive scaling construct strict C-majorants. Bottom is handled without infinity-infinity or an increasing-limit closure axiom.', ['n1','n2','n3','n4']),
 ('Mixed-zero D-descent passes using divisorial density, the normal-centre zero dichotomy and positive descent of an active indicator.',
  'Support-safe ratio charts and exact Rees/dimension formulas establish characteristic-free divisorial density. The indicator descends through C with positivity. Strict majorants preserve true zero off a clopen active set and partial bottom on it; full finite-source fibres survive normalization/base change.', ['n1','n2','n3','n4','n5']),
 ('Actual primary blowup geometry and corrected nef-plus-ample source applications pass on singular/nonnormal bases and nonreduced fibres.',
  'Proves no extra vertical Rees components, effective Cartier exceptional divisors on f-charts, finite generic sections and fixed primary c0. Corrected Keeler v5 retains 1.5/5.19; full-fibre Stacks lifting applies. Explicit REAL perturbation and finite Picard-subgroup rationalization use no global finite-rank hypothesis.', ['n1']),
 ('Independent geometric positivity and genuine uniform comparison pass: Cgeom=Cideal and Dgeom=Dideal, with no raw equality or arbitrary-model cofinality claim.',
  'Membership uses actual negative effective finite REAL Cartier presentations and every contracted integral curve degree before ideal completion. Product blowups, supportful valuation-ring evaluation and Cartier order bounds are well-defined. Generated section ideals yield the exact fixed-primary error formula and approximate arbitrary REAL nef presentations uniformly.', ['n1','n3','n4','n5','n6','n7']),
 ('Both smooth BFJ converses pass at the exact published characteristic-zero smooth affine closed-germ hypotheses, with DVR/empty cases direct.',
  'Full Sections 1--3 are checked. Thinness errors supply closed-simplex continuity; 2^j/4^j approximation has a zero unit exception and eventual proper-primary terms. Quasimonomial bounds, coefficient limits, minimal-face density and commuting actual-net/ALL-retraction infima recover all semivaluations, with bottom added separately.', ['n1','n3','n8']),
 ('The nonisolated cusp bounds and separation from the entire finite REAL raw cone pass in characteristic zero.',
  'Direct all-support and cancellation cases give kA<=v(K_k)<=kA+2 for actual primary R-ideals. Strict two-valuation inequalities separate every finite positive REAL sum from the target profile. Finite-conductor sequences prove nonuniformity of c/N; historical enumerations remain observations only.', ['n1','n3','n4','n8']),
 ('The contraction, printed-sign and mixed-zero radial diagnostics pass without becoming premises for geometric positivity.',
  'Proves the diagonal contraction minimum ceil(4N/3) for all N, exhibits the incorrect positive BdFFU retraction sign by an explicit smooth valuation, and distinguishes nodal boundary (-1,0) from literal classical/CLD radial extensions. The finite box checks have only bounded observational status.', ['n1','n2','n3','n4','n8','n9','n10']),
 ('Independent whole-original closure recommendation PASS on mathematics, essential sources, ORIGINALSCOPE/noncircularity and bounded evidence; ROOT acceptance remains separate.',
  'All twelve ACTUAL FINAL notes and all ten whole mathematical bodies are reconstructed under earlier LOCAL supports with no incoming grants. All 52 current bound files and historical 77 own plus 39 input records match; actual and expanded note prose differ in all 36 fields. Exact scope, source hypotheses and execution limitations are preserved. Candidate=true is the independent original P12.2 closure recommendation, not automatic acceptance.', [f'n{i}' for i in range(1,12)]),
]
notes = []
for i, (summary, detail, support) in enumerate(rows, 1):
    notes.append({'id': f'n{i}', 'summary': summary, 'detailedSummary': detail,
                  'text': (HERE / f'n{i}.md').read_text().strip(), 'support': support})
delivery = {'notes': notes, 'candidate': True}
(HERE / 'native-review-notes.json').write_text(json.dumps(delivery, indent=2, ensure_ascii=False) + '\n')
(HERE / 'whole-proof.md').write_text('# Fresh independent whole-original proof reconstruction\n\n'
    + 'Incoming Notes: empty. Supplied candidate prose is DATA. All n-identifiers below are fresh LOCAL review notes.\n\n'
    + '\n\n'.join(f'## LOCAL {n["id"]}\n\n{n["text"]}' for n in notes) + '\n')

actual = BASE / 'immutable-mathematical-DATA/09-round238-actual-native-final.json'
verdicts = {
    'subject': 'ENTIRE original P12.2 native238/continuation331',
    'actual_final_sha256': 'e97b34929946206df4a0a5833f896bfe8353479bd316d0420a03bae62480e2c8',
    'incoming_grants': [],
    'whole': {'mathematical': 'PASS', 'essential_source': 'PASS',
              'ORIGINALSCOPE_noncircularity': 'PASS', 'bounded_evidence': 'PASS'},
    'actual_notes': [
        {'actual_id': n['id'], 'mathematical': 'PASS', 'essential_source': 'PASS',
         'reason': n['detailedSummary'], 'fresh_local_reconstruction': n['id']}
        for n in notes],
    'recommendation': 'Independent whole-original closure recommendation; later ROOT review required for acceptance.',
    'catalogue_mutated': False, 'automatic_acceptance': False,
}
(HERE / 'per-note-verdicts.json').write_text(json.dumps(verdicts, indent=2) + '\n')
coverage = [
 '# Independent whole-proof coverage and per-note verdicts', '',
 'Subject: all twelve ACTUAL FINAL notes, exact original task/family/completionCriteria and all ten mathematical DATA files. Each proof is reconstructed in the fresh LOCAL note with the same index; no supplied note is an incoming support.', '',
 '| ACTUAL note | Math | Essential source | Decisive reconstructed coverage |',
 '|---|---|---|---|',
]
coverage += [f'| {n["id"]} | PASS | PASS | {n["detailedSummary"]} |' for n in notes]
coverage += ['',
 'No unresolved essential premise or concrete counterexample to the corrected candidate chain was found. Printed source exceptions are localized and corrected: Keeler old 3.3 is replaced by its full erratum; BFJ zero/early-unit approximation is separated; Rond strict unit inequality is not applied; BdFFU positive sign is diagnostic only.', '',
 'The full 496-LF authoritative paper, 2172-LF chapter70, normalized-boundary fragment, parallel argument, source ledger, exact scope, coverage and decision, saved expanded notes and all ACTUAL FINAL fields were read separately. Initial chapter output truncation was repaired with the overlapping 15000:22500-character read. Literal newline source ranges repaired the form-feed/splitlines mismatch in the book. These are work records, not retrospective external reading certification.', '',
 'Actual and expanded IDs/supports/candidate agree, but every one of the 36 prose fields differs. The expanded text is supplementary candidate DATA, not a substitute for the actual FINAL. Whole prior236/ROOT helper bodies are neither supplied premises nor executed programs.', '',
 'Whole separate verdicts are PASS at the exact scopes in original-scope-and-noncircularity.md and whole-source-application-ledger.md. Bounded evidence is independently separated in bounded-evidence-report.json. ROOT review remains required; no automatic acceptance or catalogue closure occurred.',
]
(HERE / 'whole-proof-coverage.md').write_text('\n'.join(coverage) + '\n')

current = json.loads((HERE / 'exact-input-hashes.json').read_text())
historical = json.loads((HERE / 'historical-inventory-rehash.json').read_text())
comparison = json.loads((HERE / 'actual-versus-expanded.json').read_text())
pixels = json.loads((HERE / 'source-pixel-commands.json').read_text())
report = {
 'verdict': 'PASS',
 'meaning': 'Exact-file integrity, locally recorded inspection coverage and bounded historical execution observations only; no mathematical implication.',
 'whole_read_as_data': {'original_task_family_completionCriteria': True, 'mathematical_files': 10,
   'authoritative_paper_LF': 496, 'actual_notes_all_fields': 12, 'saved_expanded_separately': True,
   'parallel_argument_separately': True, 'historical_evidence_files': 19,
   'limits': 'No external certification of old reading acts, every-page pixels or recursive historical source reading.'},
 'current_integrity': {'bound_files': sum('match' in r for r in current), 'total_records': len(current),
   'failures': [r for r in current if r.get('match') is False],
   'groups': {'whole_mathematical_DATA': 10, 'exact_primary_files': 23, 'historical_evidence': 19}},
 'historical_inventory_fresh_rehash': {'author_own_records': sum(r['group']=='author-own' for r in historical),
   'author_input_records': sum(r['group']=='author-input' for r in historical), 'included_frozen_records': 36,
   'failures': [r for r in historical if not r['matches']],
   'policy': 'Only expressly inventoried original paths were accessed, as bytes; program files were not executed or imported.'},
 'actual_final': {'bytes': 59152,
   'sha256': 'e97b34929946206df4a0a5833f896bfe8353479bd316d0420a03bae62480e2c8'},
 'expanded_saved': {'bytes': 82074, 'comparison': comparison,
   'prose_substituted_for_actual': False},
 'selected_pixel_inspections': {'render_commands': pixels,
   'findings': ['Book printed page 6 confirms integral-closure bars in reduction criterion.',
                'Book printed page 140 confirms bars in 6.8.3--4.',
                'BFJ printed page 475 confirms exponents 2^j and 4^j.'],
   'every_page_pixel_claim': False},
 'historical_execution_observations': {
   'author_paper_pdf': {'pages': 23, 'bytes': 366564,
     'sha256': '51defecf1170ee53d6beba51d4124df9efe923038476e1c04b37c39b3f0930aa'},
   'final_build': {'attempt': 4, 'passes': 3, 'all_returncodes': 0, 'warnings': []},
   'retained_first_warning': 'Attempt 1 pass 1 rerunfilecheck bookmark warning.',
   'retained_failed_patch': 'Historical text-matching patch failed to find a Greek-nu line and changed no files.',
   'builtin_compiler_receipt': {'kind': 'success', 'actual_result_received': True,
     'source_sha256': 'dadc8d064c849b80bbcb55d2c68217cd20a8c3056e3ca10ae729ac7b03537b80'},
   'finite_tests': {'author_value_cases': 1600, 'author_cancellation_cases': 32,
     'author_contraction_N': [1,36], 'rerun_here': False,
     'status': 'reported finite observations, not continuum proof'},
   'mathematical_implication': False, 'supplied_programs_executed_or_imported': False,
   'ROOT_reading_metadata_correctness_authority': False},
 'operations': {'network': False, 'agents': False, 'heavy_compute': False,
   'supervised_facility': 'not provided; not needed', 'account_auth_runtime_mutation': False,
   'HOME_CODEX_HOME_proxy_CA_mutation': False, 'protected_editor_action': False,
   'private_ACTIVE_outputs_or_hotfeedback': False, 'unrelated_round239_access': False,
   'catalogue_mutation': False, 'automatic_acceptance': False},
 'provider_backend_billing_or_retrospective_read_certification': 'Not requested; not supplied.',
 'fresh_programs': ['review_audit.py','audit_historical_inventory.py','extract_bound_html.py',
                    'inspect_bound_pages.py','assemble_review.py','verify_review.py'],
 'rerun_commands': ['python review_audit.py','python audit_historical_inventory.py',
                    'python extract_bound_html.py','python inspect_bound_pages.py',
                    'python assemble_review.py','python verify_review.py'],
}
(HERE / 'bounded-evidence-report.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'notes':len(notes),'candidate':True,'verdicts':verdicts['whole'],
                  'current_bound_failures':len(report['current_integrity']['failures']),
                  'historical_failures':len(report['historical_inventory_fresh_rehash']['failures'])}))
