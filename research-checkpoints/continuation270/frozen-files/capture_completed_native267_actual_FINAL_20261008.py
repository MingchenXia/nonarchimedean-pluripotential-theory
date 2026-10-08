from pathlib import Path
import hashlib, json, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'
C = R / 'campaigns/round-267/P16.7-whole373374-nonalgebraization-and-intrinsic-E1'
O = K / 'round267-completed-inspection-LOCALONLY.json'
A = K / 'round267-actual-native-final.json'
assert not O.exists() and not A.exists()
st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
assert st['status'] == 'completed' and st['calls']['unsettled'] == 0 and not st['error']
with O.open('xb') as out:
    subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'inspect', str(C / 'work.sqlite')], cwd='/workspace/xean', stdout=out, stderr=subprocess.PIPE, check=True)
j = json.loads(O.read_text())
assert j['campaign']['status'] == 'completed' and not j['campaign']['error']
settled = [e for e in j['records'] if e['kind'] == 'xean.call.settled']
assert len(settled) == 1
m = settled[0]['data']['message']
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
exact = messages[-1].encode(); x = json.loads(exact)
assert set(x) == {'notes', 'candidate'}
known = {n['id'] for n in json.loads((C / 'input.json').read_text())['notes']}
for n in x['notes']:
    assert n['id'] not in known and all(s in known for s in n['support'])
    known.add(n['id'])
A.write_bytes(exact)
print(json.dumps(dict(round=267, status=j['campaign']['status'], workspace=j['campaign']['result']['workspace'], inspection_bytes=O.stat().st_size, actual_FINAL=str(A), actual_FINAL_bytes=len(exact), actual_FINAL_sha256=hashlib.sha256(exact).hexdigest(), candidate=x['candidate'], notes=[dict(id=n['id'], summary=n['summary'], support=n['support'], text_bytes=len(n['text'].encode())) for n in x['notes']], intermediate_messages_excluded=len(messages)-1), ensure_ascii=False, indent=2))
