from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

K = Path('/workspace/research/root-checks')
sha = lambda b: hashlib.sha256(b).hexdigest()
n, expected = 227, 6
src = K / f'round{n}-settled-inspection-LOCALONLY.json'
j = json.loads(src.read_text())
assert j['campaign']['status'] == 'completed'
settled = [r for r in j['records'] if r['kind'] == 'xean.call.settled']
assert len(settled) == 1
message = settled[0]['data']['message']
assert message['exitCode'] == 0 and not message['failed'] and not message['isCanceled']
items = []
for line in message['stdout'].splitlines():
    try:
        record = json.loads(line)
    except ValueError:
        continue
    if record.get('type') == 'item.completed' and record.get('item', {}).get('type') == 'agent_message':
        items.append(record['item']['text'])
exact = items[-1].encode()
final = json.loads(exact)
assert final['candidate'] is False and len(final['notes']) == expected
registered = j['campaign']['result']
assert registered['kind'] == 'notes' and len(registered['notes']) == expected
workspaces = set()
for a, b in zip(final['notes'], registered['notes']):
    assert {k: v for k, v in a.items() if k != 'text'} == {k: v for k, v in b.items() if k != 'text'}
    assert b['text'].startswith(a['text'] + '\n\nArtifacts: ')
    suffix = b['text'][len(a['text'] + '\n\nArtifacts: '):]
    assert '\n' not in suffix
    workspace = Path(suffix)
    assert workspace.is_dir() and str(workspace).startswith(f'/workspace/research/campaigns/round-{n}/')
    workspaces.add(str(workspace))
assert len(workspaces) == 1
out = K / f'round{n}-actual-native-final.json'
assert not out.exists()
out.write_bytes(exact)
reg = K / f'round{n}-registered-native-result.json'
assert not reg.exists()
reg.write_text(json.dumps(registered, ensure_ascii=False, indent=2) + '\n')
binding = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), round=n, source_inspection_sha256=sha(src.read_bytes()), actual_FINAL_path=str(out), actual_FINAL_sha256=sha(exact), actual_FINAL_bytes=len(exact), notes=expected, native_workspace=next(iter(workspaces)), registered_result_only_artifacts_suffix=True, intermediate_agent_messages_not_FINAL=len(items)-1, author_candidate=final['candidate'], original_closed=False, new_accepted_paper=False, private_active_output_read=False, saved_artifact_equality_not_yet_checked=True)
bp = K / f'round{n}-actual-final-extraction-binding-20261008.json'
assert not bp.exists()
bp.write_text(json.dumps(binding, indent=2) + '\n')
print(json.dumps(binding, indent=2))
