from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R = Path('/workspace/research'); K = R / 'root-checks'
C = next((R / 'campaigns/round-158').iterdir())
P = K / 'P16.5-round158-settled-native-connection-failure-binding-20261006.json'
assert not P.exists()
x = json.loads((K / 'round158-settled-failure-inspection-LOCALONLY.json').read_text())
assert x['campaign']['status'] == 'blocked' and x['campaign']['result'] is None
s = next(z['data']['message'] for z in x['records'] if z['kind'] == 'xean.call.settled')
assert s['exitCode'] == 1 and s['failed'] and not s['isCanceled']
events = []
for line in s['stdout'].splitlines():
    try: e = json.loads(line)
    except ValueError: continue
    if e.get('type') in ('error', 'turn.failed', 'turn.completed'):
        events.append(e)
assert events[-1]['type'] == 'turn.failed'
payload = next(z['data']['payload'] for z in x['records'] if z['kind'] == 'xean.call.request')
prompt = json.loads(payload['prompt'])
assert prompt['task'] == json.loads((C / 'task.json').read_text()) and prompt['argument'] == (C / 'argument.md').read_text()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
P.write_text(json.dumps({
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'round': 158, 'classification': 'Settled native connection failure; no final review verdict.',
    'campaign': str(C), 'native_exit_code': s['exitCode'], 'cancelled': False,
    'canonical_result': None, 'mathematical_verdict': None,
    'terminal_errors': events,
    'whole_terminal_error_sequence_root_read': True,
    'raw_partial_mathematical_stream_published': False,
    'partial_mathematical_stream_treated_as_review': False,
    'exact_decoded_native_task_and_argument_equal_frozen_inputs': True,
    'frozen_task_sha256': sha(C / 'task.json'), 'frozen_argument_sha256': sha(C / 'argument.md'), 'frozen_settings_sha256': sha(C / 'settings.json'),
    'route': 'Xean native Codex', 'model': payload['model'], 'reasoning': payload['reasoning'],
    'reused_as_axiom_or_acceptance': False, 'original_closed': False,
    'next_full_original_review': 167,
    'next_review_scope': 'Entire corrected18-page original P16.5 proof, including genuine foundations and its appendix; only G0/G1 grants.',
    'private_active_outputs_read': False, 'hot_feedback_sent': False,
    'originals_solved': 8, 'originals_open': 34, 'accepted_supporting_papers': 63,
    'account_auth_runtime_environment_changed': False,
}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'round': 158, 'verdict': None, 'binding': str(P), 'sha256': sha(P)}, indent=2))
