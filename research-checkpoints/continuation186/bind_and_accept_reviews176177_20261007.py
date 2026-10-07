from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv

R = Path('/workspace/research'); K = R / 'root-checks'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
specs = [
    dict(round=176, continuation=214, atom='P16.4', count=66, premises=10, passages=12, grants=[],
         directory='public-P16.4-continuation214-completed-closure-descent', pages=8,
         tex='21e33250faf0c61601bc0b7383827004b2b4b40dc91fce5105e224767acbd282',
         pdf='d039e5acc2003d48569bfed38b8a25ffc2780eab4f194f6fac3db15a064863da',
         scope='All complete characteristic-zero non-Archimedean fields, arbitrary-dimensional smooth geometrically integral projective varieties and actual ample rational bundles: completed-algebraic-closure quotient, actual all-point singular PSH and extended-energy/E1 descent, unique invariant Radon lift, continuous-test dual equality, and genuine continuous mixed-operator covariance with unchanged raw mass. General E1 operator/equation transfer is conditional on its explicit antecedents.',
         gaps='General unbounded mixed operators, weighted limits, strict locality/comparison, normalized actual-potential compactness, envelope continuity/orthogonality/both-sign outer differentiation and original all-E1 target characterization/attainment/every-solution uniqueness over nontrivial and nondiscrete fields remain unestablished.',
         clarifications=['Analytification is boundaryless; properness supplies compact support for Stokes. Compactness alone is not the reason for absence of boundary terms.', 'The cited BE work has title Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry.', 'The exact reviewed source remains immutable; its conditional operator/equation implications do not establish their antecedents.']),
    dict(round=177, continuation=215, atom='P14.4', count=67, premises=5, passages=58, grants=['B'],
         directory='public-P14.4-continuation215-corrected-polar-reader', pages=10,
         tex='70d0b4fea90607091af97c8ad5328d3d0fb5006fc21c8f428deced4798f3f6ed',
         pdf='caaa7df0cae37671b783e8ff06d36b836ccf11510859bbfac2ec22572117a0be',
         scope='The explicit geometric polar-measure sector on the blown-up projective surface, its declared primitive-coordinate topology, all real-scale multiplier ideals, every specified smooth birational tower, genuine first/top nonpluripolar products and raw masses, and mandatory disjoint-support envelope-separation example. The corrected L1 estimate controls divisor coefficient, measure total variation and additive constant. The actual rational big-bundle stationary calculation uses only the entire accepted B within its exact domain.',
         gaps='Intrinsic general NA cone, full big non-nef transcendental and nonprojective domains, all P-types, closure under maxima, PL approximation, DXZ/MP projection/common-scope operator comparisons and energy theory remain unestablished. Original P14.4 and other atoms stay open.',
         clarifications=['In the maximum paragraph the winner Hessian is -omega for U_mu and -s omega for the actual scaled weights U_(s mu). Both imply nonconstancy.', 'The review report refers to an unnumbered task-grant passage, but the actual model final contains only the 58 indexed HTTP passages. No task quotation was manufactured. B is present in full in the frozen task/input and is not an external-premise registry entry.'])
]
fronts = {name: json.loads((R / name).read_text()) for name in ('active-work.json', 'checklist-current.json')}
for j in fronts.values():
    assert len(j['fully_solved_original_atoms']) == 9 and j['historical_reviewed_scoped_papers'] == 65 and j['remaining_open_original_atoms'] == 33
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
records = []
for s in specs:
    n = s['round']; C = next((R/f'campaigns/round-{n}').iterdir()); D = K/s['directory']
    x = json.loads((K/f'round{n}-completed-inspection-LOCALONLY.json').read_text()); ca = x['campaign']
    assert ca['status'] == 'completed' and ca['error'] is None
    kernel = ca['result']; assert kernel['verdict'] == 'PASS'
    request = next(t['data']['payload'] for t in x['records'] if t['kind'] == 'xean.call.request')
    message = next(t['data']['message'] for t in x['records'] if t['kind'] == 'xean.call.settled')
    assert message['exitCode'] == 0 and not message['failed'] and not message['isCanceled']
    finals = []
    for line in message['stdout'].splitlines():
        item = json.loads(line)
        if item.get('type') == 'item.completed' and item.get('item', {}).get('type') == 'agent_message':
            try: final = json.loads(item['item']['text'])
            except (ValueError, TypeError): continue
            if isinstance(final, dict) and set(final) == {'verdict', 'report', 'premises', 'passages'}: finals.append(final)
    assert len(finals) == 1; native = finals[0]
    for key in ('verdict', 'report', 'premises'): assert native[key] == kernel[key]
    assert len(kernel['premises']) == s['premises'] and len(native['passages']) == len(kernel['passages']) == s['passages']
    normalizations = []
    for i, (a, b) in enumerate(zip(native['passages'], kernel['passages'])):
        assert {key: b[key] for key in ('premise', 'url', 'quote')} == a
        assert b['id'] == kernel['operationId']+'/'+str(i)
        assert 0 <= b['premise'] < s['premises'] and b['statement'] == kernel['premises'][b['premise']]
        normalizations.append(dict(index=i, id=b['id'], unchanged_model_fields=['premise', 'url', 'quote'], kernel_added_fields=['id', 'statement']))
    coverage = []
    for i, statement in enumerate(kernel['premises']):
        passages = [p for p in kernel['passages'] if p['premise'] == i and p['url'].startswith(('https://', 'http://'))]
        assert passages
        coverage.append(dict(premise_index=i, exact_statement=statement, external_passage_ids=[p['id'] for p in passages], primary_urls=sorted(set(p['url'] for p in passages))))
    prompt = json.loads(request['prompt']); assert set(prompt) == {'task', 'argument'}
    assert prompt['task'] == json.loads((C/'task.json').read_text()) and prompt['argument'] == (C/'argument.md').read_text()
    assert request['model'] == 'gpt-6.1-sol' and request['reasoning'] == 'xhigh' and request['sandbox'] == 'read-only' and request['shell'] is False
    freeze = json.loads((C/'freeze.json').read_text())
    for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]: assert sha(C/name) == freeze[key]
    assert sha(D/(s['atom']+'-paper.tex')) == s['tex'] and sha(D/(s['atom']+'-paper.pdf')) == s['pdf']
    compiler = json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text())
    assert compiler['native_compiler_success'] and compiler['source_sha256'] == s['tex']
    canonical = K/f"{s['atom']}-round{n}-actual-canonical-independent-review-20261007.json"
    native_file = K/f"{s['atom']}-round{n}-native-model-final-review-20261007.json"
    binding = K/f"{s['atom']}-round{n}-whole-partial-review-binding-20261007.json"
    acceptance = D/f'whole-partial-paper-acceptance{n}-20261007.json'
    clarification = D/f'harmless-reader-clarifications{n}-20261007.json'
    assert not any(p.exists() for p in (canonical, native_file, binding, acceptance, clarification))
    canonical.write_text(json.dumps(kernel, ensure_ascii=False, indent=2)+'\n')
    native_file.write_text(json.dumps(native, ensure_ascii=False, indent=2)+'\n')
    record = dict(recorded_utc=now, round=n, atom=s['atom'], verdict='PASS', operation_id=kernel['operationId'], reported_at=kernel['reportedAt'],
        canonical_review=str(canonical), canonical_review_sha256=sha(canonical), native_model_final=str(native_file), native_model_final_sha256=sha(native_file),
        entire_report_all_premises_and_passages_root_read=True, premises=s['premises'], passages=s['passages'], all_zero_based_exact_statement_bindings_verified=True,
        external_coverage=coverage, passage_normalization=normalizations, task_only_passages_excluded_from_external_coverage=[p['id'] for p in kernel['passages'] if not p['url'].startswith(('https://', 'http://'))],
        kernel_report_premises_and_quotes_equal_native_final=True, exact_decoded_native_task_and_argument_equal_entire_frozen_inputs=True,
        native_prompt_sha256=hashlib.sha256(request['prompt'].encode()).hexdigest(), frozen_task_sha256=freeze['task_sha256'], frozen_argument_sha256=freeze['argument_sha256'], frozen_settings_sha256=freeze['settings_sha256'],
        model=request['model'], reasoning=request['reasoning'], child_sandbox=request['sandbox'], caller_grants=s['grants'],
        accepted_partial_scope=s['scope'], residual_original_gaps=s['gaps'], whole_partial_manuscript_accepted=True, original_closed=False, new_accepted_scoped_paper=True,
        root_recursive_primary_proof_reading_claimed=False, private_active_output_read=False, hot_feedback_sent=False, protected_editor_unchanged=True)
    binding.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    accept = dict(recorded_utc=now, atom=s['atom'], continuation=s['continuation'], independent_review_round=n, verdict='PASS', cumulative_accepted_paper_number=s['count'],
        source=str(D/(s['atom']+'-paper.tex')), source_sha256=s['tex'], pdf=str(D/(s['atom']+'-paper.pdf')), pdf_sha256=s['pdf'], pdf_pages=s['pages'],
        review_binding=str(binding), review_binding_sha256=sha(binding), accepted_scope=s['scope'], only_caller_grants=s['grants'],
        whole_saved_source_root_read=True, whole_independent_report_all_premises_and_passages_root_read=True, fresh_clean_local_builds=2, native_compiler_success=True,
        root_visual_pages_read=[1, s['pages']], all_pdf_pages_visually_root_read=False, exact_reviewed_source_preserved=True,
        fully_solved_original_atoms_count=9, original_closed=False, residual_original_scope=s['gaps'], protected_editor_unchanged_open=True, no_active_private_streams_read=True, no_hot_feedback_sent=True)
    acceptance.write_text(json.dumps(accept, ensure_ascii=False, indent=2)+'\n')
    clarification.write_text(json.dumps(dict(recorded_utc=now, independent_review_round=n, source_sha256=s['tex'], exact_reviewed_source_preserved=True, clarifications=s['clarifications'], substantial_mathematical_repair=False), ensure_ascii=False, indent=2)+'\n')
    records.append(accept)
for name, j in fronts.items():
    j['historical_reviewed_scoped_papers'] = 67; j['updated_utc'] = now
    j['accepted_partial_reviews176177'] = records
    if name == 'checklist-current.json':
        for t in j['targets']:
            if t['id'] in ('P16.4', 'P14.4'):
                assert not t['fully_solved'] and t['closure'] == 'open'
                a = next(a for a in records if a['atom'] == t['id'])
                t['research_status'] = 'whole_partial_theorem_independently_accepted_original_open'
                t['current_focus'] = a['accepted_scope']+' Remaining: '+a['residual_original_scope']
    (R/name).write_text(json.dumps(j, ensure_ascii=False, indent=2)+'\n')
table = R/'checklist-current.tsv'
with table.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t'); columns = reader.fieldnames; rows = list(reader)
for row in rows:
    if row['ID'] in ('P16.4', 'P14.4'): row['Research'] = 'whole_partial_theorem_independently_accepted_original_open'
with table.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=columns, delimiter='\t', lineterminator='\n'); writer.writeheader(); writer.writerows(rows)
print(json.dumps(dict(accepted_reviews=[176, 177], accepted_scoped_papers=67, originals_solved=9, originals_open=33, acceptance_records=[dict(path=a['review_binding'], sha256=a['review_binding_sha256']) for a in records]), indent=2))
