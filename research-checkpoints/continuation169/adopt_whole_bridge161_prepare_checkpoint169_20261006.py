from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

V = K / 'P16.5-round161-actual-canonical-independent-review-20261006.json'
review = json.loads(V.read_text())
assert sha(V) == '154187816ab04a65bd383eff22545ddc470b6cef451c6cee64557b9c0e51a066'
assert review['verdict'] == 'PASS' and len(review['premises']) == 11 and len(review['passages']) == 19
C = next((R / 'campaigns/round-161').iterdir())
task = json.loads((C / 'task.json').read_text())
inspection = json.loads((K / 'round161-completed-inspection-LOCALONLY.json').read_text())
assert inspection['campaign']['status'] == 'completed' and inspection['campaign']['result'] == review
request = next(x['data']['payload'] for x in inspection['records'] if x['kind'] == 'xean.call.request')
decoded = json.loads(request['prompt'])
assert decoded == {'task': task, 'argument': (C / 'argument.md').read_text()}
assert request['model'] == 'gpt-6.1-sol' and request['reasoning'] == 'xhigh' and request['sandbox'] == 'read-only'
coverage = []
for i, premise in enumerate(review['premises']):
    external = [p for p in review['passages'] if p['premise'] == i and p['url'].startswith('https://')]
    assert external and all(p['statement'] == premise and p['quote'] for p in external)
    coverage.append({'premise_index': i, 'exact_statement': premise, 'independent_external_passage_ids': [p['id'] for p in external], 'primary_urls': sorted({p['url'] for p in external})})
task_passages = [p for p in review['passages'] if p['url'] == 'urn:xean:task']
assert len(task_passages) == 2 and all(p['quote'] in task['problem'] or p['quote'] in task['completionCriteria'] for p in task_passages)
data = json.loads((C / 'mathematical-data-bindings.json').read_text())
for item in data['supplied']:
    assert sha(item['file']) == item['sha256']

clarifications = {
    'whole201': 'Strict locality extends to unequal additive constants by repeating its proof with the second actual auxiliary weights shifted by that constant. For v-epsilon the window is enlarged by epsilon, the bundle and horizontal factor stay fixed, e_A shifts by -epsilon*V_A and the measure is constant invariant. Use normalized costs after restoring each fixed generic value; all canonical ordered errors have unchanged generic values. The same fixed collar, finite ordered-gap and fixed-ramp estimates therefore prove locality for max(u,v-epsilon). Equal raw V then gives the stated strict comparison. Constant invariance alone is not its locality proof.',
    'whole202': 'Display (1) applies to generically normalized potentials. For arbitrary u,v write u0=u-u(v0), v0=v-v(v0), w0=w-w(v0), and use |u-v|<=|u0-v0|+|u(v0)-v(v0)|. Since M(w)=M(w0) has raw mass V, restore the extra term V*|u(v0)-v(v0)| and use B(u0),B(v0),B(w0). Midpoint defect is invariant under separate constants. Zero simplex entries are omitted. The simultaneous changing-test proof already retains its generic error.'
}
A = K / 'P16.5-round161-whole-review-acceptance-and-scope-binding-20261006.json'
prior_front = json.loads((R / 'active-work.json').read_text())
specs = [
    ('P16_5_completed_partial159', 'WHOLE159', 'Whole finite Hodge/absolute/raw midpoint and repaired signed Taylor proofs; conditional entire target/output integrability, supporting planes, actual variational attainment and every-solution uniqueness under S1-S3/M1-M2.'),
    ('P16_5_scalar_negligible_big_pole160', 'WHOLE160', 'Actual all-point one-net scalar closure, obstacle envelopes and normalized compactness from G0/G1; literal ample raw-supremum embedding, actual big-class pole transfer; conditional E1 pole covering and non-Borel outer-nullness; finite raw polarization and numerical-zero safeguards.'),
    ('P16_5_conditional_bounded_maxima_Borel_transfer201', 'WHOLE201', 'Conditional shared full-system moving maxima and uniform nef collars, retained-mass energy/measure identification, genuine decreasing weak continuity, fixed-ramp strict Borel locality/comparison and PSH-pole nullness.'),
    ('P16_5_conditional_filtered_trace_and_genuine_mixed202', 'WHOLE202', 'Finite exact filtered quotient trace and positive missing-volume derivative; conditional uniformly bounded physical identification, positive genuine full-domain mixed measures, all canonical weighted decreasing-net continuity and full mixed energy identity.')
]
accepted = []
for key, label, scope in specs:
    bp = Path(prior_front[key]['pdf']).parent / 'publication-binding.json'
    original = json.loads(bp.read_text())
    b = dict(original)
    frozen = next(x for x in data['supplied'] if x['label'] == label)
    assert sha(b['tex']) == b['tex_sha256'] == frozen['sha256']
    assert sha(b['pdf']) == b['pdf_sha256'] and b['native_compile_success_observed']
    assert not original['independent_acceptance']
    b.update(recorded_utc=now, classification='Independently accepted exactly scoped supporting paper; conditional antecedents remain unproved on the nonample domain.', independent_acceptance=True, review_verdict='PASS', review=str(V), review_sha256=sha(V), review_acceptance_binding=str(A), review_scope=scope, original_closed=False, accepted_paper_count=63)
    b.pop('accepted_paper_count_unchanged', None)
    if label.lower() in clarifications:
        b['harmless_application_clarification'] = clarifications[label.lower()]
    bp.write_text(json.dumps(b, ensure_ascii=False, indent=2) + '\n')
    accepted.append({'front_key': key, 'label': label, 'publication_binding': str(bp), 'paper_binding': b, 'scope': scope})
save(A, {
    'recorded_utc': now, 'classification': 'Acceptance of all four complete supporting manuscripts in exact finite/unconditional/conditional scopes only.',
    'canonical_review': str(V), 'canonical_review_sha256': sha(V), 'review_operation_id': review['operationId'],
    'whole_report_all11premises_all19passages_root_read': True, 'external_coverage_valid': True, 'external_coverage': coverage,
    'excluded_task_passage_ids': [p['id'] for p in task_passages],
    'reviewer_primary_read_scope': 'Independently opened complete applied statement/proof units and dependencies: BJ v4 separator and negligible-to-polar, BFJ v2 positive products/C1/Morse, published LM asymptotics and complete-base Fujita, Wlodarczyk principalization/functoriality, Vakil numerical ampleness/openness, and Stacks normal birational descent and Serre generation, as specified in the complete canonical report.',
    'root_read_scope': 'Complete canonical report, all11 standalone premises, all19 passages and their source-index mappings. Whole four frozen papers and own application ledgers previously read; pertinent201 shifted-comparison and202 normalization units reread. No claim ROOT independently read every reviewer primary or all recursive sources.',
    'primary_quotations_republished_in_this_ledger': False,
    'native_decoded_worker_input_equals_entire_frozen_task_and_argument': True,
    'native_prompt_sha256': hashlib.sha256(request['prompt'].encode()).hexdigest(),
    'frozen_task_sha256': sha(C / 'task.json'), 'frozen_argument_sha256': sha(C / 'argument.md'),
    'whole_reviewed_pages': 40, 'accepted_papers': accepted, 'harmless_application_clarifications': clarifications,
    'accepted_count_before': 59, 'accepted_count_after': 63, 'originals_solved': 8, 'originals_open': 34, 'new_original_closure': None,
    'actual_nonample_conditional_antecedents_established_by_review': False,
    'unbounded_physical_fixed_original_test_identification_established': False,
    'active_private_outputs_read': False, 'hot_feedback_sent': False, 'existing_editor_unchanged': True
})

diag = K / 'P16.5-continuations203204-exact-finite-diagnostic-results-20261006.json'
save(diag, {
    'recorded_utc': now, 'classification': 'Previously observed exact Fraction arithmetic diagnostics, not theorem certification.',
    'P1': {'script': str(K / 'P16.5-continuations203204-exact-P1-diagnostics-20261006.py'), 'execution_utc_approx': '2026-10-06T13:50:00Z', 'potentials': 18, 'raw_fourpoint_squared_checks': 5832, 'exact_midpoint_I_over_8_checks': 324, 'raw_TV_truncation_checks': 54, 'ordered_cap_gap_checks': 363, 'generic_constants_retained': True, 'all_passed': True},
    'projective_models': {'script': str(K / 'P16.5-continuations203204-exact-projective-model-diagnostics-20261006.py'), 'execution_utc': '2026-10-06T14:02:47Z', 'dimensions': list(range(1, 7)), 'actual_polarization_degrees': [1, 2], 'raw_masses': [{'n': n, 'd': d, 'V': d**n} for n in range(1, 7) for d in (1, 2)], 'energy_gradient_raw_measure_checks': 48, 'midpoint_I_checks': 192, 'fourpoint_squared_power_checks': 768, 'TV_cap_checks': 144, 'ordered_cap_energy_checks': 360, 'all_raw_masses_retained': True, 'diagnostic_constant': '4n on the specified finite grid only', 'all_passed': True},
    'script_sha256': {p.name: sha(p) for p in K.glob('P16.5-continuations203204-exact-*-diagnostics-20261006.py')},
    'scripts_rerun_for_this_record': False, 'independent_acceptance': False, 'original_closed': False
})

S = K / 'small-batch158163-public-status-20261006-continuation169'
S.mkdir()
items = []
for n in (158, 161, 163):
    c = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'
    save(p, st)
    items.append({'round': n, 'atom': 'P16.5', 'directory': str(c), 'observed_status': st['status'], 'observed_utc': st['observedAt'], 'public_status': str(p), 'public_status_sha256': sha(p), 'private_active_output_read': False, 'hot_feedback_sent': False, 'original_closed': False})
active = [x for x in items if x['observed_status'] == 'running']
assert len(active) <= 2 and next(x for x in items if x['round'] == 161)['observed_status'] == 'completed'
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': 'Actual foundation158 audit and unchanged full original163 author with whole66-page packet. Completed whole40-page bridge161 accepted only as scoped support.'}
prior = json.loads((G / 'push-receipt-continuation168.json').read_text())
assert prior['commit_sha'] == 'f777c2225e651f92ed02cc0c2bc327418397a4a0'
assert all(prior[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
F = G / 'continuation169-publication-records'
F.mkdir()
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 59 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, historical_reviewed_scoped_papers=63, current_small_batch=batch, P16_5_whole_supporting_review161=str(A), current_original_campaign163=json.loads((next((R / 'campaigns/round-163').iterdir()) / 'launch-record.json').read_text()), github_pending_checkpoint='continuation169 frozen', goal_state='8/42 originals solved;34 open;63 independently accepted supporting papers. Whole159160201202 PASS161 in exactly stated finite/unconditional/conditional scopes. Actual foundation158 review and unchanged whole66-page original163 research running; maximum two campaigns. Actual nonample foundations and unbounded physical fixed-original-test defect remain open.')
    for a in accepted:
        j[a['front_key']] = a['paper_binding']
    j['prepared_next_original_campaign']['prepared_only'] = False
    j['prepared_next_original_campaign']['launched_utc'] = j['current_original_campaign163']['recorded_utc']
    for target in j.get('targets', []):
        if target['id'] == 'P16.5':
            target.update(research_status='actual_foundation158_review_and_full_original163_research', current_focus=batch['focus'] + ' Actual foundations still unresolved; no original closure.', current_native_research=j['current_original_campaign163'])
            target['current_remaining_gaps'] = ['Entire actual energy/output/full-list moving foundations from G0/G1.', 'Every proof needed for full original equation and all-solution uniqueness on the unchanged task domain.', 'Physical fixed-original-unbounded-test reference defect, to the extent required by the original construction; further nonzero zero-volume theory is not inferred.']
            for a in accepted:
                assert not any(x.get('source') == a['paper_binding']['tex'] for x in target['reviewed_papers'])
                target['reviewed_papers'].append({'round': 161, 'supporting_body': a['label'], 'scope': a['scope'], 'source': a['paper_binding']['tex'], 'pdf': a['paper_binding']['pdf'], 'review': str(V), 'accepted': True, 'full_original_atom_solved': False})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
lines = (R / 'checklist-current.tsv').read_text().splitlines()
for i, line in enumerate(lines):
    row = line.split('\t')
    if row[0] == 'P16.5':
        row[2] = 'Whole159160201202 independent PASS161 in finite/unconditional/conditional scopes;63 supporting papers overall. Actual foundation158 audit and unchanged full original163 active; at most two campaigns. Original remains open.'
    lines[i] = '\t'.join(row)
(R / 'checklist-current.tsv').write_text('\n'.join(lines) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    shutil.copyfile(R / name, F / name)
save(F / 'scope-observation.json', {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_papers': 63, 'new_independent_supporting_acceptance': [159, 160, 201, 202], 'review_round': 161, 'new_original_closure': None, 'active_batch': [x['round'] for x in active], 'active_private_outputs_read': False, 'hot_feedback_sent': False, 'existing_editor_unchanged': True})
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.aux', '.out')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation169/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()):
        add(p)
for p in (V, A, diag, G / 'push-receipt-continuation168.json', R / 'record_verified168_20261006.py', R / 'launch_frozen_original163_20261006.py', Path(__file__)):
    add(p)
for a in accepted:
    for p in (a['paper_binding']['tex'], a['paper_binding']['pdf'], a['publication_binding']):
        add(p)
for p in K.glob('P16.5-continuations203204-exact-*-diagnostics-20261006.py'):
    add(p)
add(next((R / 'campaigns/round-163').iterdir()) / 'launch-record.json')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
M = G / 'upload-manifest-continuation169.json'
save(M, {'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': prior_front['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 63, 'commit_message': 'Accept four complete supporting proofs and continue full nonample equation research', 'scope': 'Whole40-page review161 PASS159160201202 only in exact finite/unconditional/conditional scopes, all11 premises and19 passages ROOT read and externally indexed; two harmless application clarifications explicit. Four support acceptances increase59 to63, originals remain8/42. Unchanged full original163 launched beside foundation158 audit; maximum two campaigns. Previously observed exact finite diagnostics retained separately from proof/acceptance. All frozen mathematical input bytes retained; no active private reads/hot feedback.'})
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(files), 'accepted_papers': 63, 'originals_solved': 8, 'statuses': [{'round': x['round'], 'status': x['observed_status']} for x in items]}, indent=2))
