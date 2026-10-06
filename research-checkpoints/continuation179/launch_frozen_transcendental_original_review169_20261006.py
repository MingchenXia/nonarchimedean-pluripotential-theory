from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R = Path('/workspace/research')
C = next((R / 'campaigns/round-169').iterdir())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
assert 'P19.2' not in json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms']
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
assert f['argument_sha256'] == '272f11ecb330f421a1fe516d1efdaeec84dcd1776838771c1610fad79a53723d'
assert f['task_sha256'] == 'e49c527c1c9fce930f541e812b652e70fec8490c6163afd2c6cef40b4af05de7'
s = json.loads((C / 'settings.json').read_text())
assert s['research']['model'] == 'gpt-6.1-sol' and s['research']['reasoning'] == 'xhigh'
assert s['limits'] == {'concurrency': 1, 'attempts': 1, 'providerCalls': 1}
states = []
for n in (167, 168):
    other = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(other / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    assert st['status'] in ('running', 'completed', 'blocked')
    if st['status'] == 'blocked':
        assert st['calls']['unsettled'] == 0 and st['work']['active'] == 0 and st['work']['queued'] == 0
    states.append({'round': n, 'public_status': st})
assert sum(x['public_status']['calls']['unsettled'] for x in states) <= 1, 'Two campaigns are already active.'
args = ['bash', 'scripts/cloud.sh', 'xean', '--records', 'review', str(C / 'task.json'), str(C / 'argument.md'), str(C / 'work.sqlite'), str(C / 'settings.json')]
with (C / 'controller-output-LOCALONLY.log').open('xb') as out:
    pid = subprocess.Popen(args, cwd='/workspace/xean', stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT, start_new_session=True).pid
os.kill(pid, 0)
record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': 169, 'pid': pid, 'argv': args, 'role': 'independent-review', 'scope': 'Whole eight-page transcendental P19.2 analytic counterexample and exact original signature audit.', 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'maximum_concurrent_campaigns': 2, 'frozen_task_sha256': f['task_sha256'], 'frozen_math_input_sha256': f['argument_sha256'], 'frozen_settings_sha256': f['settings_sha256'], 'only_mathematical_grants': ['R'], 'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False, 'account_auth_runtime_environment_changed': False, 'parent_execution_permissions': 'require_escalated for exact authorized native initialization, preserving native child research sandbox', 'prior_public_states': states, 'reserved_current_batch': [x['round'] for x in states if x['public_status']['calls']['unsettled'] > 0] + [169]}
(C / 'launch-record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'round': 169, 'pid': pid, 'argument_sha256': f['argument_sha256'], 'maximum_concurrent_campaigns': 2}, indent=2))
