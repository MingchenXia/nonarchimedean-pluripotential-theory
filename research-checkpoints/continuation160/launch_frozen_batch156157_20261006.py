from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
states = []
for n in (154, 155):
    C = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    assert st['status'] == 'completed' and st['calls']['unsettled'] == 0
    states.append({'round': n, 'public_status': st})
prepared = []
for n in (156, 157):
    C = next((R / f'campaigns/round-{n}').iterdir())
    f = json.loads((C / 'freeze.json').read_text())
    assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
    body, key = ('argument.md', 'argument_sha256') if n == 156 else ('input.json', 'input_sha256')
    for name, field in [('task.json', 'task_sha256'), ('settings.json', 'settings_sha256'), (body, key)]:
        assert sha(C / name) == f[field]
    s = json.loads((C / 'settings.json').read_text())
    model = s['research'] if n == 156 else s['codex']
    assert model['model'] == 'gpt-6.1-sol' and model['reasoning'] == 'xhigh'
    assert len(s['usagePrefix']) <= 91 and s['limits'] == {'concurrency': 1, 'attempts': 1, 'providerCalls': 1}
    if n == 156:
        assert f[key] == 'fb67e4413a45607d2278732a7ea6a93729b57755b66a695100374430aa411e48'
    else:
        assert f[key] == 'fcdbf728dadbf9528888f1284393ee5697d09978d4e7030ed8cd4904f906716d'
        assert f['task_sha256'] == '2e9b9fcb3a4615a698c16190bf7b0a0bc6ef37660faa4be371fb58ed25e06989'
    prepared.append((n, C, f, body, key))
launched = []
for n, C, f, body, key in prepared:
    args = ['bash', 'scripts/cloud.sh', 'xean', '--records']
    if n == 156:
        args += ['review', str(C / 'task.json'), str(C / body), str(C / 'work.sqlite'), str(C / 'settings.json')]
    else:
        args += ['role', 'codex', str(C / body), str(C / 'work.sqlite'), str(C / 'settings.json')]
    with (C / 'controller-output-LOCALONLY.log').open('xb') as out:
        pid = subprocess.Popen(args, cwd='/workspace/xean', stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT, start_new_session=True).pid
    os.kill(pid, 0)
    d = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': n, 'pid': pid, 'argv': args, 'role': 'independent-review' if n == 156 else 'original-author-research', 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'maximum_concurrent_campaigns': 2, 'scoped_review_only': n == 156, 'original_closed': False, 'unchanged_original_task': n == 157, 'frozen_task_sha256': f['task_sha256'], 'frozen_math_input_sha256': f[key], 'frozen_settings_sha256': f['settings_sha256'], 'private_active_output_read': False, 'hot_feedback_sent': False, 'account_auth_runtime_environment_changed': False, 'parent_execution_permissions': 'require_escalated for native-directory initialization, retaining native child sandbox', 'prior_settled_public_states': states, 'reserved_current_batch': [156, 157]}
    (C / 'launch-record.json').write_text(json.dumps(d, indent=2) + '\n')
    launched.append({'round': n, 'pid': pid, 'role': d['role'], 'math_input_sha256': f[key]})
print(json.dumps({'maximum_concurrent_campaigns': 2, 'launched': launched}, indent=2))
