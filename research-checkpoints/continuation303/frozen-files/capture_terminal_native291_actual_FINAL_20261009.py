from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-291/P16.7-whole417418-actual-representation-and-prescribed-measure-J-defect'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
O = K / 'round291-terminal-inspection-LOCALONLY.json'
A = K / 'round291-raw-native-actual-FINAL.json'
Q = K / 'round291-terminal-actual-final-ROOT-retention-20261009.json'
assert not A.exists() and not Q.exists()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
cmd = ['bash', 'scripts/cloud.sh', 'xean', '--records']
st = json.loads(subprocess.run(cmd + ['status', str(C / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
assert st['status'] == 'completed' and not st['error']
assert st['calls']['admitted'] == st['calls']['settled'] == 1 and st['calls']['unsettled'] == 0 and st['work']['active'] == 0
for name in ['active-work.json', 'checklist-current.json']:
    y = json.loads((R / name).read_text())
    assert y['current_active_batch'] == [291,292] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 302
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
if not O.exists():
    with O.open('xb') as out:
        subprocess.run(cmd + ['inspect', str(C / 'work.sqlite')], cwd='/workspace/xean', stdout=out, stderr=subprocess.PIPE, check=True)
j = json.loads(O.read_text())
events = [e for e in j['records'] if e['kind'] == 'xean.call.settled']
assert len(events) == 1
m = events[0]['data']['message']
assert m['exitCode'] == 0 and not m['failed'] and not m['isCanceled']
messages = []
for line in m['stdout'].splitlines():
    try:
        v = json.loads(line)
    except ValueError:
        continue
    if v.get('type') == 'item.completed' and v.get('item', {}).get('type') == 'agent_message':
        messages.append(v['item']['text'])
assert messages
exact = messages[-1].encode()
x = json.loads(exact)
assert set(x) == {'notes', 'candidate'}
known = {n['id'] for n in json.loads((C / 'input.json').read_text())['notes']}
invalid = []
for n in x['notes']:
    assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
    for s in n['support']:
        if s not in known:
            invalid.append(dict(note_id=n['id'], support=s))
    known.add(n['id'])
A.write_bytes(exact)
now = datetime.now(timezone.utc).isoformat()
rec = dict(recorded_utc=now, round=291, public_status=st, campaign_result=j['campaign'].get('result'), raw_actual_FINAL=dict(path=str(A), bytes=len(exact), sha256=sha(A), notes=len(x['notes']), candidate=x['candidate'], status='Whole actual settled FINAL retained UNREVIEWED; mathematical bodies not yet physically read'), notes_metadata=[dict(id=n['id'], keys=list(n), text_bytes=len(n['text'].encode()), support=n['support']) for n in x['notes']], invalid_support_references=invalid, full_inspection=dict(path=str(O), bytes=O.stat().st_size, sha256=sha(O), LOCALONLY=True), intermediate_agent_messages_excluded=len(messages)-1, supplied_or_native_programs_executed_or_imported=False, whole_mathematical_bodies_NOT_yet_ROOT_physically_read=True, accepted=False, new_correctness_grant=False, original_closed=False, protected_editor_OPEN_UNCHANGED=True, counts=dict(solved=16, open=26, accepted_scoped_papers=97))
Q.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = json.loads(p.read_text())
    y.update(updated_utc=now, current_active_batch=[292], next_work='Native291 terminal actual FINAL retained unread UNREVIEWED. Physically read ALL actual five-field notes, every distinct expanded proof/current unique scope/immediate applied sources before ROOT421 and next P16.7 worker. Native292 remains active on frozen original nonsingleton-conductor proposal; ROOT420 independently complete and retained, excluded from active292 hot feedback. Prepare regular NONFORCE303 after reviewed proof ready; compiler unverified, counts/editor unchanged.')
    y['native291_terminal_unreviewed_retention'] = dict(record=str(Q), record_sha256=sha(Q), raw_FINAL=rec['raw_actual_FINAL'])
    p.write_text(json.dumps(y, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(record=str(Q), raw_actual_FINAL=rec['raw_actual_FINAL'], notes=rec['notes_metadata'], invalid_support=invalid, candidate=x['candidate']), ensure_ascii=False, indent=2))
