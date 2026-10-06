from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess
R = Path('/workspace/research')
C = next((R / 'campaigns/round-165').iterdir())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
states = []
for n in (158, 163):
    c = next((R / f'campaigns/round-{n}').iterdir())
    s = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    states.append({'round': n, 'public_status': s})
assert all(x['public_status']['status'] in ('completed', 'running') for x in states)
assert sum(x['public_status']['calls']['unsettled'] for x in states) <= 1, 'Two campaigns remain active.'
if states[1]['public_status']['status'] == 'completed':
    p = R / 'root-checks/P16.5-round163-actual-canonical-author-result-20261006.json'
    assert p.exists(), 'Read the complete canonical author result before choosing the next campaign.'
    assert json.loads(p.read_text())['candidate'] is False, 'Full original candidate review has priority over a separate supporting audit.'
assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
f = json.loads((C / 'freeze.json').read_text())
s = json.loads((C / 'settings.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
assert f['argument_sha256'] == '61e4427d538d637dcbdff709c5713e7a865c7895dfdb08a7ceb6432d41b65c0d'
assert s['research']['model'] == 'gpt-6.1-sol' and s['research']['reasoning'] == 'xhigh'
assert s['limits'] == {'concurrency': 1, 'attempts': 1, 'providerCalls': 1}
args = ['bash', 'scripts/cloud.sh', 'xean', '--records', 'review', str(C / 'task.json'), str(C / 'argument.md'), str(C / 'work.sqlite'), str(C / 'settings.json')]
with (C / 'controller-output-LOCALONLY.log').open('xb') as out:
    pid = subprocess.Popen(args, cwd='/workspace/xean', stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT, start_new_session=True).pid
os.kill(pid, 0)
record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': 165, 'pid': pid, 'argv': args, 'role': 'independent-review', 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'maximum_concurrent_campaigns': 2, 'whole_new_papers': [203, 204, 205], 'whole_new_pages': 17, 'frozen_task_sha256': f['task_sha256'], 'frozen_math_input_sha256': f['argument_sha256'], 'frozen_settings_sha256': f['settings_sha256'], 'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False, 'account_auth_runtime_environment_changed': False, 'parent_execution_permissions': 'require_escalated for native-directory initialization, retaining native child sandbox', 'prior_public_states': states, 'reserved_current_batch': [x['round'] for x in states if x['public_status']['status'] == 'running'] + [165]}
(C / 'launch-record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'round': 165, 'pid': pid, 'frozen_argument_sha256': f['argument_sha256'], 'maximum_concurrent_campaigns': 2}, indent=2))
