from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R = Path('/workspace/research')
C = R / 'campaigns/round-155/P19.2-original-all-ray-relative-profile-approximation-after-singular-start'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
f = json.loads((C / 'freeze.json').read_text())
assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
for name, key in [('input.json', 'input_sha256'), ('task.json', 'task_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
assert f['task_sha256'] == 'ab34124f46c030751e42bac4aed0e9ac214303cf3415ffc7b2588cae8f8559f8'
assert f['input_sha256'] == '6cbc7db4e19014119959a97097c87b6d0204ebe36eff02a758f960cbe341a47e'
s = json.loads((C / 'settings.json').read_text())
assert s['codex']['model'] == 'gpt-6.1-sol' and s['codex']['reasoning'] == 'xhigh'
assert len(s['usagePrefix']) <= 91 and s['limits'] == {'concurrency': 1, 'attempts': 1, 'providerCalls': 1}
states = []
for n in (151, 152, 153, 154):
    other = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(other / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    if n in (151, 152):
        assert st['status'] == 'completed' and st['calls']['unsettled'] == 0
    if n == 153:
        assert st['status'] == 'blocked' and st['calls']['unsettled'] == 0
    states.append({'round': n, 'public_status': st})
assert len([x for x in states if x['public_status']['status'] == 'running']) <= 1
args = ['bash', 'scripts/cloud.sh', 'xean', '--records', 'role', 'codex', str(C / 'input.json'), str(C / 'work.sqlite'), str(C / 'settings.json')]
with (C / 'controller-output-LOCALONLY.log').open('xb') as out:
    pid = subprocess.Popen(args, cwd='/workspace/xean', stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT, start_new_session=True).pid
os.kill(pid, 0)
d = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': 155, 'pid': pid, 'argv': args, 'role': 'original-author-research', 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'maximum_concurrent_campaigns': 2, 'original_closed': False, 'unchanged_original_family_task': True, 'sole_original_target': 'P19.2', 'frozen_task_sha256': sha(C / 'task.json'), 'frozen_math_input_sha256': sha(C / 'input.json'), 'frozen_settings_sha256': sha(C / 'settings.json'), 'private_active_output_read': False, 'hot_feedback_sent': False, 'account_auth_runtime_environment_changed': False, 'parent_execution_permissions': 'require_escalated for native-directory initialization, retaining the worker sandbox', 'prior_public_states': states}
(C / 'launch-record.json').write_text(json.dumps(d, indent=2) + '\n')
print(json.dumps({'round': 155, 'pid': pid, 'input_sha256': f['input_sha256'], 'input_bytes': f['input_bytes']}, indent=2))
