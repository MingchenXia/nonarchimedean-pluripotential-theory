"""Owned bounded byte-retention audit; never executes or imports supplied code."""
import hashlib
import json
import pathlib
import platform
import sys

ROOT = pathlib.Path('/workspace/research/campaigns/round-254/P12.3-original-normal-envelope-positivity-after-full-energy-capacity-calculus')
HERE = pathlib.Path(__file__).resolve().parent
records = []
for manifest, category in [('mathematical-packet-bindings.json', 'mathematical'),
                           ('private-primary-packet-bindings.json', 'primary-LOCALONLY'),
                           ('book-context-bindings.json', 'context-LOCALONLY')]:
    raw = (ROOT / manifest).read_bytes()
    folder = HERE / 'inputs' / category
    folder.mkdir(parents=True, exist_ok=True)
    (HERE / 'inputs' / manifest).write_bytes(raw)
    for index, item in enumerate(json.loads(raw)):
        path = pathlib.Path(item['path'])
        body = path.read_bytes()
        digest = hashlib.sha256(body).hexdigest()
        target = folder / (f'{index:02d}-' + path.name)
        target.write_bytes(body)
        records.append(dict(item, local_path=str(target.relative_to(HERE)),
                            observed_bytes=len(body), observed_sha256=digest,
                            matched=len(body)==item['bytes'] and digest==item['sha256']))
inp = (HERE / 'input.json').read_bytes()
(HERE / 'inputs' / 'current-input.json').write_bytes(inp)
parsed = json.loads(inp)
grants = HERE / 'inputs' / 'grants'
grants.mkdir(exist_ok=True)
for note in parsed['notes']:
    (grants / (note['id'] + '.json')).write_text(json.dumps(note, ensure_ascii=False, indent=2)+'\n')
    (grants / (note['id'] + '.txt')).write_text(note['text'])
(HERE / 'inputs' / 'current-augmented-assignment.txt').write_text(parsed['assignment'])
reports = HERE / 'evidence'
reports.mkdir(exist_ok=True)
(reports / 'input-audit.json').write_text(json.dumps({'records': records,
    'count': len(records), 'all_matched': all(r['matched'] for r in records),
    'current_input_sha256': hashlib.sha256(inp).hexdigest()}, indent=2)+'\n')
(reports / 'execution-configuration.json').write_text(json.dumps({
    'python':sys.version, 'platform':platform.platform(), 'cwd':str(HERE),
    'shell':'bash', 'date_from_operator':'2026-10-08', 'timezone':'Etc/UTC',
    'permissions':'workspace-write; approval never; network restricted',
    'operator_constraints':'No supplied code execution/import, agents/native jobs, heavy compute, compiler, editor or external mutation; sources LOCALONLY',
    'supervised_compute_service':'None provided; not required by bounded diagnostics',
    'commands':['python retain_inputs.py'],
    'mathematical_status':'Unverified draft; retention does not validate mathematics'}, indent=2)+'\n')
print(json.dumps({'records':len(records),'matched':sum(r['matched'] for r in records)}))
if not all(r['matched'] for r in records):
    raise SystemExit(1)
