from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
summary = []
for n, atom, verdict, np, nq in ((167, 'P16.5', 'PASS', 13, 18), (169, 'P19.2', 'INCONCLUSIVE', 12, 62)):
    C = next((R / f'campaigns/round-{n}').iterdir())
    inspection = json.loads((K / f'round{n}-completed-inspection-LOCALONLY.json').read_text())
    ca = inspection['campaign']
    assert ca['status'] == 'completed' and ca['error'] is None
    kernel = ca['result']
    request = next(x['data']['payload'] for x in inspection['records'] if x['kind'] == 'xean.call.request')
    message = next(x['data']['message'] for x in inspection['records'] if x['kind'] == 'xean.call.settled')
    assert message['exitCode'] == 0 and not message['failed'] and not message['isCanceled']
    finals = []
    for line in message['stdout'].splitlines():
        item = json.loads(line)
        if item.get('type') == 'item.completed' and item.get('item', {}).get('type') == 'agent_message':
            try:
                candidate = json.loads(item['item']['text'])
            except (ValueError, TypeError):
                continue
            if isinstance(candidate, dict) and set(candidate) == {'verdict', 'report', 'premises', 'passages'}:
                finals.append(candidate)
    assert len(finals) == 1
    native = finals[0]
    assert native['verdict'] == kernel['verdict'] == verdict
    assert native['report'] == kernel['report'] and native['premises'] == kernel['premises']
    assert len(kernel['premises']) == np and len(native['passages']) == len(kernel['passages']) == nq
    normalizations = []
    for i, (a, b) in enumerate(zip(native['passages'], kernel['passages'])):
        assert {k: b[k] for k in ('premise', 'url', 'quote')} == a
        assert b['id'] == kernel['operationId'] + '/' + str(i)
        assert 0 <= b['premise'] < np and b['statement'] == kernel['premises'][b['premise']]
        normalizations.append({'index': i, 'id': b['id'], 'unchanged_model_fields': ['premise', 'url', 'quote'], 'kernel_added_fields': ['id', 'statement']})
    coverage = []
    for i, statement in enumerate(kernel['premises']):
        passages = [p for p in kernel['passages'] if p['premise'] == i and p['url'].startswith(('https://', 'http://'))]
        assert passages
        coverage.append({'premise_index': i, 'exact_statement': statement, 'external_passage_ids': [p['id'] for p in passages], 'primary_urls': sorted(set(p['url'] for p in passages))})
    prompt = json.loads(request['prompt'])
    assert set(prompt) == {'task', 'argument'}
    assert prompt['task'] == json.loads((C / 'task.json').read_text())
    assert prompt['argument'] == (C / 'argument.md').read_text()
    assert request['model'] == 'gpt-6.1-sol' and request['reasoning'] == 'xhigh'
    assert request['sandbox'] == 'read-only' and request['shell'] is False
    freeze = json.loads((C / 'freeze.json').read_text())
    for filename, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
        assert sha(C / filename) == freeze[key]
    canonical = K / f'{atom}-round{n}-actual-canonical-independent-review-20261006.json'
    native_file = K / f'{atom}-round{n}-native-model-final-review-20261006.json'
    binding = K / f'{atom}-round{n}-whole-original-review-binding-20261006.json'
    assert not any(p.exists() for p in (canonical, native_file, binding))
    canonical.write_text(json.dumps(kernel, ensure_ascii=False, indent=2) + '\n')
    native_file.write_text(json.dumps(native, ensure_ascii=False, indent=2) + '\n')
    record = {
        'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': n, 'atom': atom,
        'verdict': verdict, 'operation_id': kernel['operationId'], 'reported_at': kernel['reportedAt'],
        'canonical_review': str(canonical), 'canonical_review_sha256': sha(canonical),
        'native_model_final': str(native_file), 'native_model_final_sha256': sha(native_file),
        'entire_report_all_premises_and_passages_root_read': True,
        'premises': np, 'passages': nq, 'all_zero_based_exact_statement_bindings_verified': True,
        'external_coverage': coverage, 'passage_normalization': normalizations,
        'task_only_passages_excluded_from_external_coverage': [p['id'] for p in kernel['passages'] if not p['url'].startswith(('http://', 'https://'))],
        'kernel_report_premises_and_quotes_equal_native_final': True,
        'exact_decoded_native_task_and_argument_equal_entire_frozen_inputs': True,
        'native_prompt_sha256': hashlib.sha256(request['prompt'].encode()).hexdigest(),
        'frozen_task_sha256': freeze['task_sha256'], 'frozen_argument_sha256': freeze['argument_sha256'],
        'frozen_settings_sha256': freeze['settings_sha256'], 'model': request['model'],
        'reasoning': request['reasoning'], 'child_sandbox': request['sandbox'],
        'caller_grants': ['G0', 'G1'] if n == 167 else ['R'],
        'original_scope_accepted_by_review': n == 167, 'catalogue_closure_recorded_separately': True,
        'scope_limit': 'Full actual-big rational-bundle range; additional entire numerically trivial zero-volume range; stronger fixed-original-unbounded physical-output test assertion explicitly not proved or required.' if n == 167 else 'Mathematical finer-dS-P-profile obstruction checked; exact original P19.2 signature/model-universe identification unresolved. No original closure or new accepted supporting paper.',
        'root_primary_reading_limit': 'ROOT read the complete result and evidence bindings; this record does not claim ROOT freshly read every independently retrieved primary proof or every recursive source foundation.',
        'private_active_output_read': False, 'hot_feedback_sent': False, 'existing_editor_unchanged': True
    }
    binding.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    summary.append({'round': n, 'verdict': verdict, 'binding': str(binding), 'binding_sha256': sha(binding), 'canonical_sha256': sha(canonical)})
print(json.dumps(summary, indent=2))
