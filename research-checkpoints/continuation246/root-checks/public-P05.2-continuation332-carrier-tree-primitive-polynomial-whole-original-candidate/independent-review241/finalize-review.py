"""Validate and bind this owned review. No supplied programs are run/imported."""
import hashlib
import json
import pathlib
import platform
import sys

ROOT = pathlib.Path.cwd()
BASE = ROOT.parents[1]

def read_json(path):
    return json.loads(pathlib.Path(path).read_text())

def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def bind(path):
    path = pathlib.Path(path)
    data = path.read_bytes()
    return {'path': str(path.resolve()), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

identities = read_json('input-bindings.json')
for group in ('mathematical_packet', 'private_primaries', 'historical_evidence_files',
              'historical_author_owned_33', 'historical_frozen_43', 'historical_input_controls_4',
              'qualified_note_text_bindings'):
    assert all(row['matches'] for row in identities[group]), group
assert identities['actual_saved_identity']['objects_equal']
assert len(identities['actual_saved_identity']['all_five_fields']) == 5
assert identities['actual_saved_identity']['saved_is_actual_plus_one_newline']
assert identities['input_identity']['task_equal'] and identities['input_identity']['notes_equal']
assert identities['input_identity']['assignment_equal']
assert identities['input_identity']['original_task_equal_author_original']
assert identities['input_identity']['current_original_problem_chars'] == 55562

events = [json.loads(line) for line in pathlib.Path('read-events.jsonl').read_text().splitlines()]
coverage = {}
for event in events:
    key = event['path']
    coverage.setdefault(key, {'mode': event['mode'], 'ranges': [], 'sha256': event['sha256']})['ranges'].append([event['start'], event['end']])
for path, item in coverage.items():
    ranges = sorted(item['ranges'])
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + (1 if item['mode'] in ('BMPS', 'BBGS') else 0):
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    item['merged_ranges'] = merged
    item['interpretation'] = 'one-based inclusive literal LF' if item['mode'] in ('BMPS', 'BBGS') else 'zero-based decoded character slice'
write_json('read-coverage.json', {
    'actual_owned_file_display_events': coverage,
    'whole_original_dossier': {'problem_chars': 55562, 'decoded_artifacts': ['controlling-problem.txt', 'controlling-completion.txt'],
                               'ad_hoc_display_ranges': ['0:14000', '14000:28000', '28000:42000', '42000:end'],
                               'range_description_not_fabricated_tool_receipt': True},
    'qualified_notes_read_as_whole_supplied_mathematical_data': [n['id'] for n in read_json('input.json')['notes']],
    'all_qualified_component_files_separately_redisplayed': False,
    'support_components_verbatim_in_supplied_notes': 29,
    'other_9_supplemental_ledgers_scopes_read_separately': True,
    'whole_paper_actual_final_parallel_argument_candidate_ledger_scope_coverage_decision_read': True,
    'whole_private_primary_pdfs_visually_read': False,
    'universal_historical_read_acts_attested': False
})

history = read_json(BASE / 'historical-own-evidence-bindings.json')
logs = []
for index in (12, 13, 14):
    text = pathlib.Path(history[index]['path']).read_text()
    logs.append({'path': history[index]['path'], 'sha256': history[index]['sha256'],
                 'undefined_reference_warning': 'There were undefined references' in text,
                 'label_rerun_warning': 'Rerun to get cross-references right' in text,
                 'epstopdf_shell_escape_disabled_warning': 'Shell escape feature is not enabled' in text,
                 'output_line': next(line for line in text.splitlines() if line.startswith('Output written on'))})
build_results = read_json(history[3]['path'])
write_json('bounded-evidence-report.json', {
    'verdict': 'PASS for current packet identity and bounded recorded observations',
    'specific_metadata_counterexample_verdict': 'FAIL: asserted assignment inequality is disproved',
    'universal_retrospective_provider_history_verdict': 'INCONCLUSIVE',
    'mathematical_acceptance_inferred_from_evidence': False,
    'verified_counts': {group: len(identities[group]) for group in ('mathematical_packet','private_primaries','historical_evidence_files','historical_author_owned_33','historical_frozen_43','historical_input_controls_4','qualified_note_text_bindings')},
    'all_manifest_byte_bindings_match': True,
    'input_identity': identities['input_identity'],
    'actual_saved_identity': identities['actual_saved_identity'],
    'assignment_discrepancy': {
        'supplied_historical_assertion': 'controller/native assignments differ',
        'own_observation': 'All three decoded top-level fields task, notes and assignment are equal; full decoded objects equal. Raw serializations differ.',
        'consequence': 'Narrow evidence metadata correction; mathematical forwarding is intact. Historical files are unchanged.'
    },
    'candidate_authoritative_source': identities['mathematical_packet'][38],
    'parallel_argument': {'binding': identities['mathematical_packet'][39], 'whole_separate_read': True, 'byte_identical_to_TeX_claimed': False},
    'actual_final': identities['mathematical_packet'][44],
    'ROOT328': {'binding': identities['mathematical_packet'][45], 'independently_reviewed': True,
                'frozen_author239_input': False, 'supplied_helper_executed_or_imported': False,
                'mathematical_verdict': 'PASS optional finite-vertex pair criterion; translating back to non-strict all-root tree syntax uses a smaller tolerance for margin',
                'essential_to_frozen_candidate_acceptance': False},
    'build_observations': {'source': 'bound author logs, not reviewer execution', 'return_codes': [r['returncode'] for r in build_results],
                           'passes': logs, 'final_pdf_bytes': 304914, 'final_pdf_pages_by_own_pdfinfo': 14,
                           'final_pdf_sha256': 'b7ce4fe7d6c3860c0a6b211e25cd3bdf137baa6ea0c942f1431e302d13a62a08',
                           'builtin_receipt': read_json(history[16]['path']), 'builtin_success_is_acceptance': False},
    'author_finite_observations': {'input': read_json(history[7]['path']), 'output': read_json(history[8]['path']),
                                 'reviewer_reran_author_code': False, 'independent_exhaustive_finite_result_claimed': False,
                                 'continuum_proof_inferred': False},
    'preserved_history': ['source FAIL', 'combined FAIL', 'retrospective evidence INCONCLUSIVE', 'provider/model historical uncertainty', 'native231 unknown-S306 result-registration failure'],
    'supplied_notes_checks': 'All eight checks lists are empty caller trust; no new model PASS fabricated.',
    'execution_configuration': {'network_web_provider_agents': False, 'heavy_compute': False, 'supplied_code_execution_import': False,
                                'protected_editor_or_new_tab': False, 'ACTIVE240_private_output': False,
                                'auth_runtime_HOME_CODEX_HOME_proxy_CA_changes': False,
                                'owned_small_identity_and_report_programs_only': True,
                                'supervised_compute_needed': False, 'provider_model_effort_independently_attested': False},
    'reading_evidence': 'read-events.jsonl and read-coverage.json; descriptions are not substituted for nonexistent historical receipts',
    'rerun_commands': ['python verify-review-inputs.py', 'python finalize-review.py'],
    'environment': identities['environment']
})

review = pathlib.Path('independent-review.md').read_text()
def section(start, end):
    return review.split(start, 1)[1].split(end, 1)[0].strip()

notes = []
def note(number, summary, detailed, text, support):
    notes.append({'id': 'n' + str(number), 'summary': summary, 'detailedSummary': detailed, 'text': text, 'support': support})

note(1, 'PASS actual author n1: raw finite legal-tree identity includes discontinuous upper-only competitors; R230 applied only afterward.',
     'Finite grafting makes the tree infimum an original competitor without density or MA. Actual node incidence and reference costs are retained. Proper-height same-tree estimates give bounded local envelope convergence; terminal probabilities are not MA.',
     'Independent mathematical verdict on actual author n1: PASS.\n\n' + section('## Raw legal trees — actual author n1: PASS', '## Finite PA rows') + '\n\nFull reconstruction: independent-review.md. Own read evidence: read-events.jsonl; rerun identities with python verify-review-inputs.py. No supplied program was run.', ['R230'])
note(2, 'PASS actual author n2 and essential raw sources: genuine scalar PA, exact whole-cell PC rows and full signed primitive polynomials.',
     'O323 applies to continuous bounded-relative real matching tuples on finite positive all-face balanced geometry. Every original incident cell enters a common ambient support. BBGS whole3.12/3.15/3.18/3.19 is calibrated by saturated covolumes and -p at every dimension; 8ABw plane atom, no appended factorial.',
     'Independent mathematical verdict on actual author n2: PASS. Essential NEW source-application verdict: PASS at the exact qualifications.\n\n' + section('## Finite PA rows and primitive polynomials — actual author n2: PASS', '## Exact finite-PA') + '\n\nComplete source ledger: whole-source-application-ledger.md. Immediate BMPS LF254–301,418–604,689–852,1000–1034,1350–1503,1741–1752,2253–2358 and BBGS LF196–264,379–532,533–603,604–674,675–718 were independently read, including3.15 ending670. Raw-PC automatic continuity, defective irrational-center insertion,6.4 density,6.6 shortcuts, AR10 delegation and absent bibliographies are excluded. Unchanged caller grants and all mandatory qualifications are premises, not fresh historical verification. Rerun owned bindings: python verify-review-inputs.py.', ['O323','S272'])
note(3, 'PASS actual author n3: T iff PA-obstacle domain/contact, with strict global PA regularization before any completed measure.',
     'Necessity starts at an already completed endpoint and uses a strict near-optimal-tree margin plus fixed-test/variable-error convergence. Sufficiency produces p_n<=e<=p_n+epsilon_n and g_n=p_n+4epsilon_n with strict descent and one relative bound before S272. Zero mass does not create a domain.',
     'Independent mathematical verdict on actual author n3: PASS.\n\n' + section('## Exact finite-PA equivalence — actual author n3: PASS','## All bounded continuous') + '\n\nArtifacts: independent-review.md and whole-proof-coverage.md. Rerun owned identity verification with python verify-review-inputs.py.', ['n1','n2','S272'])
note(4, 'PASS actual author n4: ALL-C_b extension has independently global genuine domains and fixed-C localized measure/gap limits.',
     'O323 compatible non-PC obstacle roofs and R230 supply all endpoints before local limits. Rational ambient norm bumps approximate arbitrary obstacles only locally with one bound. Dense ambient compact PA tests meet S272 auxiliary scope; bounded IBP, signed-TV localization and pre-existing fixed-C moments pass contact to non-PA endpoints.',
     'Independent mathematical verdict on actual author n4: PASS.\n\n' + section('## All bounded continuous obstacles — actual author n4: PASS','## All coefficient/category') + '\n\nThe compact-test shorthand is used only for the explicitly constructed dense ambient rational PA restriction family; no broader intrinsic-test grant or new extension lemma is needed. Artifacts: independent-review.md, whole-source-application-ledger.md and whole-proof-coverage.md. Rerun metadata with python verify-review-inputs.py.', ['n1','n3','O323','R230','S272'])
scope = pathlib.Path('original-scope-and-noncircularity.md').read_text()
root_text = scope.split('## ROOT328: independent optional finite-vertex strengthening',1)[1].strip()
note(5, 'PASS optional NEW ROOT328 finite-vertex criterion; separate from frozen author239 and unnecessary to rescue its acceptance.',
     'Actual positive recession makes gamma-affine carrier cells pointed. Continuous cell-convex envelope secants and exact p recession propagate finitely many vertex bounds globally. Pair-criterion equivalence uses a smaller tolerance when reconstructing actual all-root trees, avoiding an infimum-attainment assumption.',
     'Independent proof, not an imported ROOT328 grant:\n\n' + root_text + '\n\nThis note uses the preceding independently reviewed raw identity/rows/PA/all-C_b chain. It executes no ROOT328 helper.', ['n1','n2','n3','n4','R230'])
scope_core = scope.split('## ROOT328: independent optional finite-vertex strengthening',1)[0]
note(6, 'PASS actual author n5 and WHOLEORIGINALSCOPE: coefficient-separated infinite structural characterization in the defined embedded category.',
     'Three explicit eliminations and a constructive global domain proof make T substantive, without requiring a finite taxonomy or decision algorithm. The full dossier supplies no alternative atlas category. Literal actual-obstacle arithmetic failure, direct d=0 zero-fold contact, empty support and compact divergence cover the remaining cases. ROOT328 is optional, not a rescue premise.',
     'Independent mathematical verdict on actual author n5: PASS. WHOLEORIGINALSCOPE/noncircularity verdict: PASS.\n\n' + section('## All coefficient/category cases — actual author n5: PASS','## Meaningfulness and ROOT328') + '\n\n' + scope_core + '\n\nArtifacts: original-scope-and-noncircularity.md, original-scope-decision.md and whole-proof-coverage.md. Exactly all five actual author notes were reviewed; the candidate notes are not imported support Notes. Rerun bindings: python verify-review-inputs.py.', ['n1','n2','n3','n4','O323','S272','S282'])
note(7, 'Bounded evidence PASS for current packet; assignment-difference assertion specifically FAIL; universal historical/provider claims INCONCLUSIVE.',
     'All46math/4primary/17evidence/33own/43frozen+4controls/8qualified-text bindings match. Saved and actual five-note objects/candidate equal; saved bytes add one newline. Both hash-bound full author input objects, INCLUDING assignments, are equal despite different serialization. Builds and finite counts remain author observations; no supplied code rerun or historical verdict upgrade.',
     'Independent bounded-evidence verdict: PASS for current identity and bounded recorded observations. The specific historical assignment-inequality flag is FAIL; universal retrospective read/action/provider certification is INCONCLUSIVE.\n\n' + section('## Evidence boundaries','Artifacts are independent-review.md') + '\n\nPrograms: verify-review-inputs.py (owned, inspected before execution) and finalize-review.py (owned report validation/binding). Inputs, exact per-file outputs and environment: input-bindings.json, identity-output.json, read-events.jsonl, read-coverage.json and bounded-evidence-report.json. Author counts390/32/24/2/1 and compile successes do not prove mathematics. No supplied builder/checker/binder or ROOT328 helper was executed/imported. Rerun python verify-review-inputs.py and python finalize-review.py.', [])
note(8, 'Independent whole-original closure recommendation: PASS mathematics, essential sources and scope; candidate=true pending later ROOT acceptance.',
     'All five actual author notes PASS and the real T equivalence covers every admitted PA and C_b obstacle with genuine domains, actual reference/weights and all faces. Literal/d=0/empty/compact cases are resolved in the exact original category. Current bounded evidence passes with one corrected metadata assertion; historical uncertainty remains. No essential revision or ROOT328 rescue is required; original stays OPEN until ROOT acceptance.',
     pathlib.Path('original-scope-decision.md').read_text() + '\n\nThis last note claims completion of the EXACT independent whole-original review assignment and recommends the complete original mathematical solution for acceptance. candidate=true is this independent original-closure recommendation, not adoption of authorcandidateTRUE and not an acceptance mutation. Reports and notes are unverified drafts; execution success does not establish mathematical correctness. All unproved supplied/earlier results used are declared in support.', ['n1','n2','n3','n4','n5','n6','n7'])
write_json('review-notes.json', {'notes': notes, 'candidate': True})
allowed = {n['id'] for n in read_json('input.json')['notes']}
for n in notes:
    assert set(n) == {'id','summary','detailedSummary','text','support'}
    assert set(n['support']) <= allowed, (n['id'], n['support'])
    allowed.add(n['id'])

write_json('commands.json', {
    'owned_reruns': ['python verify-review-inputs.py','python finalize-review.py'],
    'reader_syntax': ['python review-reader.py math INDEX CHAR_START CHAR_END','python review-reader.py BMPS LF_START LF_END','python review-reader.py BBGS LF_START LF_END'],
    'candidate_pdf_metadata_command': 'pdfinfo /workspace/research/campaigns/round-239/P05.2-original-finite-carrier-PCC-tree-and-raw-contact-classification/artifacts/codex-hcfWTS/P05.2-paper.pdf',
    'supplied_commands_are_recorded_data_not_executed': True,
    'mathematical_checks': 'No numerical search or supplied checker rerun. Continuum proofs are reasoned in review notes/reports.'
})
write_json('environment.json', {'python': sys.version,'platform': platform.platform(),'cwd': str(ROOT),
                               'provider_identity_model_effort': 'not independently attested',
                               'no_installation_or_runtime_change': True})
validation = {'status':'PASS owned metadata/report validation', 'notes': len(notes), 'supports_valid': True,
              'candidate': True, 'original_status_mutated': False, 'all_required_reports_present': True,
              'continuum_math_certified_by_program': False,
              'report_files': ['independent-review.md','whole-source-application-ledger.md','whole-proof-coverage.md',
                               'original-scope-and-noncircularity.md','original-scope-decision.md','bounded-evidence-report.json']}
for filename in validation['report_files']:
    assert pathlib.Path(filename).is_file()
write_json('validation-output.json', validation)
files = [p for p in ROOT.iterdir() if p.is_file() and p.name != 'own-bindings.json']
write_json('own-bindings.json', {'files': [bind(p) for p in sorted(files)],
                               'self_excluded_to_avoid_circular_hash': True,
                               'meaning': 'Owned artifact identities, not mathematical acceptance or provider/history attestation.'})
print(json.dumps(validation, indent=2))
