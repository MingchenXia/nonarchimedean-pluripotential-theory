from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv

R = Path('/workspace/research'); K = R/'root-checks'
C = next((R/'campaigns/round-192').iterdir())
D = K/'public-P05.2-continuation230-continuous-completion-and-envelope'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
x = json.loads((K/'round192-completed-inspection-LOCALONLY.json').read_text())
ca = x['campaign']; k = ca['result']
assert ca['status'] == 'completed' and ca['error'] is None and k['verdict'] == 'PASS'
req = next(t['data']['payload'] for t in x['records'] if t['kind'] == 'xean.call.request')
msg = next(t['data']['message'] for t in x['records'] if t['kind'] == 'xean.call.settled')
assert msg['exitCode'] == 0 and not msg['failed'] and not msg['isCanceled']
finals = []
for line in msg['stdout'].splitlines():
    t = json.loads(line)
    if t.get('type') == 'item.completed' and t.get('item', {}).get('type') == 'agent_message':
        try: n = json.loads(t['item']['text'])
        except (ValueError, TypeError): continue
        if isinstance(n, dict) and set(n) == {'verdict', 'report', 'premises', 'passages'}: finals.append(n)
assert len(finals) == 1
n = finals[0]
assert all(k[q] == n[q] for q in ('verdict', 'report', 'premises'))
assert len(k['premises']) == 7 and len(k['passages']) == len(n['passages']) == 33
normalizations = []
for i, (a, b) in enumerate(zip(n['passages'], k['passages'])):
    assert {q: b[q] for q in ('premise', 'url', 'quote')} == a
    assert b['id'] == k['operationId'] + '/' + str(i)
    assert 0 <= b['premise'] < 7 and b['statement'] == k['premises'][b['premise']]
    normalizations.append(dict(index=i, id=b['id'], unchanged_model_fields=['premise','url','quote'], kernel_added_fields=['id','statement']))
coverage = []
for i, premise in enumerate(k['premises']):
    ps = [p for p in k['passages'] if p['premise'] == i and p['url'].startswith(('https://','http://'))]
    assert ps
    coverage.append(dict(premise_index=i, exact_statement=premise, external_passage_ids=[p['id'] for p in ps], primary_urls=sorted({p['url'] for p in ps})))
prompt = json.loads(req['prompt'])
assert set(prompt) == {'task','argument'}
argument = (C/'argument.md').read_text()
assert prompt['task'] == json.loads((C/'task.json').read_text()) and prompt['argument'] == argument
assert req['model'] == 'gpt-6.1-sol' and req['reasoning'] == 'xhigh' and req['sandbox'] == 'read-only' and req['shell'] is False
f = json.loads((C/'freeze.json').read_text())
for name, key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]: assert sha(C/name) == f[key]
data = json.loads((C/'mathematical-data-bindings.json').read_text())
lines = argument.splitlines()
for entry in data:
    p = Path(entry['source']); lo, hi = entry['argument_inclusive_lf']
    assert sha(p) == entry['sha256'] and p.stat().st_size == entry['bytes']
    assert '\n'.join(lines[lo-1:hi]) == p.read_text().rstrip('\n')
assert sha(D/'P05.2-paper.tex') == 'ffadbcedcb0eb49c893ae81f3d7696ef4cba25a9df6179644eedb7b51286cc3a'
assert sha(D/'P05.2-paper.pdf') == '3497de8d90a759545c7a94df8d7a624527072863dc6ae5210c2db85abf14ab0c'
repro = json.loads((D/'root-reproduction-binding-20261007.json').read_text())
compile_record = json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text())
visual = json.loads((D/'root-limited-pdf-visual-addendum-20261007.json').read_text())
assert repro['whole_saved_tex_source_root_read'] and repro['whole_native_argument_separately_root_read']
assert repro['root_local_build_exit_codes'] == [0,0] and repro['root_local_final_warnings'] == []
assert compile_record['source_sha256'] == sha(D/'P05.2-paper.tex') and compile_record['native_result']['kind'] == 'success'
assert visual['pdf_sha256'] == sha(D/'P05.2-paper.pdf') and visual['root_visual_pages_read'] == [1,13]
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ('active-work.json','checklist-current.json'):
    j = json.loads((R/name).read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['historical_reviewed_scoped_papers'] == 74 and j['remaining_open_original_atoms'] == 33
canonical = K/'P05.2-round192-actual-canonical-independent-review-20261007.json'
native = K/'P05.2-round192-native-model-final-review-20261007.json'
binding = K/'P05.2-round192-whole-partial-review-binding-20261007.json'
P = D/'whole-partial-paper-acceptance192-20261007.json'
Q = D/'harmless-reader-clarifications192-20261007.json'
assert not any(p.exists() for p in (canonical,native,binding,P,Q))
now = datetime.now(timezone.utc).isoformat()
scope = ('On every finite pure positive balanced rational embedded polyhedral space, every finite-valued function satisfying the printed rational-endpoint PCC inequalities has a unique continuous dominating completion agreeing on the rational locus, equal to its neighborhood upper semicontinuous hull and least continuous majorant; no local bound or continuity premise is assumed. The completion satisfies all real-endpoint PCCs on every witnessing rational structure. Every bounded continuous obstacle and continuous PC reference yields an actual unrestricted envelope that is continuous and nonexpansive, including nonseparable product obstacles. Sharp fan-vertex criteria and an unbalanced nonvertex jump diagnose the scope. Separately specified compact rational integral-affine balanced charts give componentwise constant envelopes; finite bounded rational carrying decompositions give literal rational PA or separately real PA endpoints, with genuine raw positive-dimensional MA and contact zero; dimension zero retains its weighted zero-fold cycle. The entire printed relative PC class has an exact half-unit obstruction to both PA density classes. No general PA regularization, general continuous-envelope raw MA, contact classification, or full original closure is asserted.')
gaps = 'Global PA approximation in each fixed coefficient category; regularizable operator domains and continuity; necessary and sufficient raw contact conditions; reference-compatible global realization and full original P05.1/P05.2 structural classifications remain open.'
canonical.write_text(json.dumps(k, ensure_ascii=False, indent=2)+'\n')
native.write_text(json.dumps(n, ensure_ascii=False, indent=2)+'\n')
b = dict(recorded_utc=now, round=192, atom='P05.2', verdict='PASS', operation_id=k['operationId'], reported_at=k['reportedAt'], canonical_review=str(canonical), canonical_review_sha256=sha(canonical), native_model_final=str(native), native_model_final_sha256=sha(native),
    entire_report_all_premises_and_passages_root_read=True, premises=7, passages=33, all_zero_based_exact_statement_bindings_verified=True, external_coverage=coverage, passage_normalization=normalizations, task_only_passages_excluded_from_external_coverage=[], unindexed_caller_grants_excluded_from_external_coverage=['A224','B225'], kernel_report_premises_and_quotes_equal_native_final=True,
    exact_decoded_native_task_and_argument_equal_entire_frozen_inputs=True, all_nine_whole_math_data_bodies_equal_frozen_sources=True, native_prompt_sha256=hashlib.sha256(req['prompt'].encode()).hexdigest(), frozen_task_sha256=f['task_sha256'], frozen_argument_sha256=f['argument_sha256'], frozen_settings_sha256=f['settings_sha256'], model=req['model'], reasoning=req['reasoning'], child_sandbox=req['sandbox'], caller_grants=['A224','B225'], accepted_partial_scope=scope, whole_partial_manuscript_accepted=True, original_closed=False, new_accepted_scoped_paper=True, residual_original_gaps=gaps, root_recursive_primary_proof_reading_claimed=False, private_active_output_read=False, hot_feedback_sent=False, protected_editor_unchanged=True)
binding.write_text(json.dumps(b, ensure_ascii=False, indent=2)+'\n')
a = dict(recorded_utc=now, atom='P05.2', continuation=230, independent_review_round=192, verdict='PASS', cumulative_accepted_paper_number=75, source=str(D/'P05.2-paper.tex'), source_sha256=sha(D/'P05.2-paper.tex'), source_lf_lines=337, pdf=str(D/'P05.2-paper.pdf'), pdf_sha256=sha(D/'P05.2-paper.pdf'), pdf_pages=13, review_binding=str(binding), review_binding_sha256=sha(binding), accepted_scope=scope, only_caller_grants=['A224','B225'], whole_final_saved_source_root_read=True, whole_independent_report_all_premises_and_passages_root_read=True, fresh_clean_final_local_builds=2, native_compiler_success=True, root_visual_pages_read=[1,13], all_pdf_pages_visually_root_read=False, exact_reviewed_source_preserved=True, fully_solved_original_atoms_count=9, original_closed=False, residual_original_scope=gaps, protected_editor_unchanged_open=True, no_active_private_streams_read=True, no_hot_feedback_sent=True)
P.write_text(json.dumps(a, ensure_ascii=False, indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now, independent_review_round=192, source_sha256=sha(D/'P05.2-paper.tex'), exact_reviewed_source_preserved=True, substantial_mathematical_repair=False, clarifications=['Decreasing can mean nonincreasing; strictly decreasing constant additions are also available in the compact PA case.', 'The symbol q* denotes the neighborhood upper semicontinuous hull, including isolated points.', 'The finite bounded chart-compatible carrying-decomposition hypothesis governs both coefficient branches of the compact PA assertion.', 'Only continuous completed functions receive the compact maximum principle; general continuous envelopes receive no new raw Monge-Ampere operator.']), ensure_ascii=False, indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p = R/name; j = json.loads(p.read_text())
    j.update(historical_reviewed_scoped_papers=75, updated_utc=now, P05_2_accepted_continuous_completion192=a, goal_state='9/42 originals independently accepted;33 open;75 cumulative independently accepted scoped/supporting papers. Complete continuous PCC completion and all-continuous-obstacle envelope continuity are accepted; general PA regularization and contact classification remain open. Continue batches of at most two with regular verified GitHub pushes.', next_work='Native189 independently audits the whole actual genus-zero equation; native193 works on the unchanged full original P16.4 with frozen actual-primary packet. Continue actual model algebraization and later P05 general PA/contact classification using complete accepted224/225/230 bodies and all clarifications.')
    if name == 'checklist-current.json':
        for target in j['targets']:
            if target['id'] == 'P05.2':
                assert not target['fully_solved'] and target['closure'] == 'open'
                target['research_status'] = 'continuous_completion_and_all_continuous_obstacle_envelopes_accepted_classification_open'
                target['current_focus'] = 'Entire230 independently PASS192 after whole224/225 grants; all continuous-obstacle envelopes continuous. General PA approximation, operator regularity, contact and structural classification remain open.'
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2)+'\n')
table = R/'checklist-current.tsv'
with table.open(newline='') as fh:
    reader = csv.DictReader(fh, delimiter='\t'); columns = reader.fieldnames; rows = list(reader)
for row in rows:
    if row['ID'] == 'P05.2': row['Research'] = 'continuous_completion_and_all_continuous_obstacle_envelopes_accepted_classification_open'
with table.open('w', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=columns, delimiter='\t', lineterminator='\n'); writer.writeheader(); writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=75, review_round=192, originals_solved=9, originals_open=33, acceptance_record=str(P), acceptance_sha256=sha(P), review_binding_sha256=sha(binding)), indent=2))
