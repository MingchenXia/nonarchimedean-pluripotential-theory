from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R = Path('/workspace/research')
C = R / 'campaigns/round-227/P05.1-balanced-cellwise-Lipschitz-and-single-cell-real-majorants-independent-whole-source-audit'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('original-task.json', 'original_task_sha256'), ('input.json', 'input_sha256'), ('settings.json', 'settings_sha256'), ('mathematical-packet-bindings.json', 'mathematical_packet_bindings_sha256'), ('historical-own-evidence-bindings.json', 'historical_own_evidence_bindings_sha256'), ('private-primary-packet-bindings.json', 'private_primary_packet_bindings_sha256')]: assert sha(C / name) == f[key]
for name in ['mathematical-packet-bindings.json', 'historical-own-evidence-bindings.json', 'private-primary-packet-bindings.json']:
    for e in json.loads((C / name).read_text()): assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
states = []
for n in [225, 226]:
    old = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(old / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    states.append(dict(round=n, public_status=st))
assert all(e['public_status']['status'] == 'completed' and e['public_status']['calls']['unsettled'] == 0 for e in states if e['round'] == 225)
assert sum(e['public_status']['status'] not in ['completed', 'failed', 'cancelled'] or e['public_status']['calls']['unsettled'] > 0 for e in states) <= 1
s = json.loads((C / 'settings.json').read_text())
assert s['codex']['model'] == 'gpt-6.1-sol' and s['codex']['reasoning'] == 'xhigh'
assert s['limits'] == dict(concurrency=1, attempts=1, providerCalls=1)
assert f['only_grants'] == ['A224', 'B225', 'R230', 'S262', 'S272', 'S291']
args = ['bash', 'scripts/cloud.sh', 'xean', '--records', 'role', 'codex', str(C / 'input.json'), str(C / 'work.sqlite'), str(C / 'settings.json')]
with (C / 'controller-output-LOCALONLY.log').open('xb') as out:
    pid = subprocess.Popen(args, cwd='/workspace/xean', stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT, start_new_session=True).pid
os.kill(pid, 0)
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), round=227, pid=pid, argv=args, model='gpt-6.1-sol', reasoning='xhigh', native_role=f['native_role'], frozen_input_sha256=f['input_sha256'], only_grants=f['only_grants'], whole_math_files=f['whole_math_files'], own_evidence_files=f['own_evidence_files'], private_primary_files=4, maximum_concurrent_campaigns=2, prior_public_states=states, reserved_current_batch=[226, 227], native225226_and_new304305_outputs_not_fed=True, original_closed=False, new_accepted_paper=False, private_active_output_read=False, hot_feedback_sent=False, account_auth_runtime_environment_changed=False, protected_editor_unchanged_open=True)
(C / 'launch-record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(dict(round=227, pid=pid, reserved_current_batch=[226, 227], input_sha256=f['input_sha256']), indent=2))
