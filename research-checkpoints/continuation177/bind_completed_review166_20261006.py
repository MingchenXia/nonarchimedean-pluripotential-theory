from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = next((R / 'campaigns/round-166').iterdir())
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
P = K / 'P16.5-round166-actual-canonical-independent-review-20261006.json'
N = K / 'P16.5-round166-native-model-final-review-20261006.json'
B = K / 'P16.5-round166-whole-original-failure-and-correction-binding-20261006.json'
assert not N.exists() and not B.exists()
assert sha(P) == '4309d3da3c990a17fdca6f7bcc3945d5eaf220e624149a7f550d341dc9c73d79'
native = json.loads(P.read_text())
inspection = json.loads((K / 'round166-completed-inspection-LOCALONLY.json').read_text())
campaign = inspection['campaign']
kernel = campaign['result']
assert campaign['status'] == 'completed' and campaign['error'] is None
assert kernel['verdict'] == native['verdict'] == 'FAIL'
assert kernel['report'] == native['report'] and kernel['premises'] == native['premises']
assert len(kernel['premises']) == 9 and len(kernel['passages']) == len(native['passages']) == 15
normalization = []
coverage = []
for i, (a, b) in enumerate(zip(native['passages'], kernel['passages'])):
    assert {k: b[k] for k in ('premise', 'url', 'quote')} == a
    assert b['id'] == kernel['operationId'] + '/' + str(i)
    assert b['statement'] == kernel['premises'][a['premise']]
    normalization.append({'index': i, 'id': b['id'], 'unchanged_model_fields': ['premise', 'url', 'quote'], 'added_kernel_fields': ['id', 'statement']})
for i, statement in enumerate(kernel['premises']):
    passages = [z for z in kernel['passages'] if z['premise'] == i and z['url'].startswith(('https://', 'http://'))]
    assert passages
    coverage.append({'premise_index': i, 'exact_statement': statement, 'external_passage_ids': [z['id'] for z in passages], 'primary_urls': sorted(set(z['url'] for z in passages))})
payload = next(z['data']['payload'] for z in inspection['records'] if z['kind'] == 'xean.call.request')
prompt = json.loads(payload['prompt'])
assert set(prompt) == {'task', 'argument'}
assert prompt['task'] == json.loads((C / 'task.json').read_text())
assert prompt['argument'] == (C / 'argument.md').read_text()
assert payload['model'] == 'gpt-6.1-sol' and payload['reasoning'] == 'xhigh'
assert payload['sandbox'] == 'read-only' and payload['shell'] is False
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
assert f['argument_sha256'] == 'db36b292eeeae5589a8a2e3cd13e6b6ddaf6451bc73cb7f844b537be965a7a07'
shutil.copyfile(P, N)
P.write_text(json.dumps(kernel, ensure_ascii=False, indent=2) + '\n')
corrected = K / 'P16.5-original-big-equation-with-retained-vertical-moving-factors-candidate-20261006-continuation210.tex'
assert sha(corrected) == 'd1473f933a5c08096a97df253c259c1d8a7dae583132e35bd5ab2c3b7da9b5f7'
record = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'classification': 'Completed independent whole-original review FAIL; no acceptance or original closure.',
    'round': 166,
    'canonical_review': str(P), 'canonical_review_sha256': sha(P),
    'native_model_final_preserved': str(N), 'native_model_final_sha256': sha(N),
    'operation_id': kernel['operationId'], 'reported_at': kernel['reportedAt'],
    'verdict': kernel['verdict'],
    'whole_report_all9premises_all15passages_root_read': True,
    'kernel_metadata_and_all15_normalized_passages_root_read': True,
    'kernel_report_premises_and_quotes_equal_native_final': True,
    'passage_normalization': normalization,
    'external_coverage_valid': True, 'external_coverage': coverage,
    'task_only_passage_ids_excluded_from_external_coverage': [z['id'] for z in kernel['passages'] if not z['url'].startswith(('https://', 'http://'))],
    'exact_decoded_native_task_and_argument_equal_entire_frozen_inputs': True,
    'native_prompt_sha256': hashlib.sha256(payload['prompt'].encode()).hexdigest(),
    'frozen_task_sha256': f['task_sha256'], 'frozen_argument_sha256': f['argument_sha256'], 'frozen_settings_sha256': f['settings_sha256'],
    'model': payload['model'], 'reasoning': payload['reasoning'], 'child_sandbox': payload['sandbox'],
    'actual_grants': ['G0 complete actual ample theory', 'G1 complete actual relative-generation/one-FS-net theory'],
    'decisive_failure': 'Author163 equation5.2 removes the entire pulled generic fixed divisor and loses its vertical part T_m^ver. On Bl_p(P2) with L=H+E and the time blowup of E times0, D=-G, all full-system weights are zero: the actual auxiliary output is zero, moving class p*H+cF and raw energy0. The claimed class p*H-G+cF instead has cube3c-1 and raw energy-1/3. Thus5.4 and ensuing unconditional foundations/equation conclusions fail.',
    'repair': 'Corrected210 equation5.2 retains T_m^ver and removes only horizontal fixed components, then resolves the actual effective residual vertical base ideal. AppendixA proves actual full section-space division and the finite counterexample independently.',
    'root_counterexample_preceded_completed_review_read': True,
    'corrected_source': str(corrected), 'corrected_source_sha256': sha(corrected),
    'fresh_whole_corrected_independent_review': 167,
    'fresh_review_status_at_binding': 'Prepared and frozen, not yet launched.',
    'positive_observations_are_not_standalone_theorem_grants': True,
    'stronger_unbounded_physical_fixed_original_test_claim': 'Reviewer confirms it is not explicit in original completion criteria; it remains unproved and is not used as a granted foundation.',
    'ordinary_background_review_limit': 'Reviewer identified the characteristic-zero principalization statements and equivariance application, but did not exhaustively reconstruct the complete algorithmic proof. The finite decisive counterexample requires no such reconstruction. ROOT read the whole canonical report and all premises/passages, not every independently retrieved primary or recursive source.',
    'independent_acceptance': False, 'original_closed': False,
    'originals_solved': 8, 'originals_open': 34, 'accepted_supporting_papers': 63,
    'private_active_outputs_read': False, 'hot_feedback_sent': False, 'existing_editor_unchanged': True,
}
B.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verdict': kernel['verdict'], 'canonical_sha256': sha(P), 'binding': str(B), 'binding_sha256': sha(B), 'normalization': 'Only passage id/statement and result metadata added by kernel; all source-index/URL/quote tuples unchanged.', 'original_closed': False}, indent=2))
