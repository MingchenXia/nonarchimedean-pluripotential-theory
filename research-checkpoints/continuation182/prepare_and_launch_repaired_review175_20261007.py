from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'
old = next((R / 'campaigns/round-174').iterdir())
C = R / 'campaigns/round-175/P14.4-geometric-polar-sector-birational-independent-partial-review'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not C.exists() and not (old / 'work.sqlite').exists()
launch = json.loads((old / 'launch-record.json').read_text())
state = Path(f'/proc/{launch["pid"]}/stat')
assert not state.exists() or state.read_text().split(') ', 1)[1].startswith('Z ')
error = (old / 'controller-output-LOCALONLY.log').read_text()
assert '/settings/usagePrefix: must not have more than 91 characters' in error
old_freeze = json.loads((old / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]: assert sha(old / name) == old_freeze[key]
failure = K / 'P14.4-round174-pre-admission-prefix-validation-failure-20261007.json'
assert not failure.exists()
failure.write_text(json.dumps({'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': 174, 'pid': launch['pid'], 'process_terminated_before_campaign_database_creation': True, 'public_campaign_database_exists': False, 'provider_call_admitted': False, 'canonical_result': None, 'mathematical_verdict': None, 'reason': 'settings.usagePrefix exceeds 91-character native declaration limit', 'frozen_settings_sha256': old_freeze['settings_sha256'], 'frozen_task_sha256': old_freeze['task_sha256'], 'frozen_argument_sha256': old_freeze['argument_sha256'], 'failed_inputs_unchanged': True, 'replacement_round': 175, 'private_active_output_read': False, 'ended_controller_error_read': True, 'account_auth_runtime_changed': False, 'protected_editor_unchanged': True}, indent=2) + '\n')
C.mkdir(parents=True)
for name in ('task.json', 'argument.md', 'original-task.json', 'mathematical-data-bindings.json'):
    (C / name).write_bytes((old / name).read_bytes())
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r175/P14.4-polar-birational-partial-review'
assert len(settings['usagePrefix']) <= 91
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
freeze = dict(old_freeze)
freeze.update(prepared_utc=datetime.now(timezone.utc).isoformat(), round=175, directory=str(C), settings_sha256=sha(C / 'settings.json'), prepared_only=True, replacement_for_pre_admission_failure=174, task_and_entire_mathematics_byte_identical_to174=True)
(C / 'freeze.json').write_text(json.dumps(freeze, indent=2) + '\n')
assert sha(C / 'task.json') == old_freeze['task_sha256'] and sha(C / 'argument.md') == old_freeze['argument_sha256']
states = []
for n in (171, 172, 173):
    p = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(p / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    if st['status'] == 'blocked': assert st['calls']['unsettled'] == st['work']['active'] == st['work']['queued'] == 0
    states.append({'round': n, 'public_status': st})
assert sum(z['public_status']['calls']['unsettled'] for z in states) <= 1
assert settings['research']['model'] == 'gpt-6.1-sol' and settings['research']['reasoning'] == 'xhigh'
args = ['bash', 'scripts/cloud.sh', 'xean', '--records', 'review', str(C / 'task.json'), str(C / 'argument.md'), str(C / 'work.sqlite'), str(C / 'settings.json')]
with (C / 'controller-output-LOCALONLY.log').open('xb') as stream:
    pid = subprocess.Popen(args, cwd='/workspace/xean', stdin=subprocess.DEVNULL, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True).pid
os.kill(pid, 0)
record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': 175, 'pid': pid, 'argv': args, 'role': 'independent-partial-review', 'replacement_for_pre_admission_failure': 174, 'task_and_mathematical_argument_byte_identical_to174': True, 'scope': 'Complete new P14.4 partial sector and entire smooth-modification-tower argument; original remains open.', 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'maximum_concurrent_campaigns': 2, 'frozen_task_sha256': freeze['task_sha256'], 'frozen_math_input_sha256': freeze['argument_sha256'], 'frozen_settings_sha256': freeze['settings_sha256'], 'only_mathematical_grants': ['B'], 'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False, 'account_auth_runtime_environment_changed': False, 'parent_execution_permissions': 'require_escalated for authorized native initialization, preserving native read-only source-review sandbox', 'prior_public_states': states, 'reserved_current_batch': [z['round'] for z in states if z['public_status']['calls']['unsettled'] > 0] + [175]}
(C / 'launch-record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'round': 175, 'pid': pid, 'argument_sha256': freeze['argument_sha256'], 'reserved_current_batch': record['reserved_current_batch']}, indent=2))
