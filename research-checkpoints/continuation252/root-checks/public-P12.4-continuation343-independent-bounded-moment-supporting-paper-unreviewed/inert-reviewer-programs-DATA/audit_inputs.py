#!/usr/bin/env python3
"""Fresh owned helper: read only explicitly bound inputs as data; never import them."""
import hashlib, json, platform, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
MANIFESTS = ('mathematical-packet-bindings.json', 'private-primary-packet-bindings.json')
for directory in ('inputs', 'inputs/G331', 'inputs/working', 'evidence', 'evidence/source-units', 'evidence/source-pages'):
    (HERE / directory).mkdir(parents=True, exist_ok=True)
records = []
for manifest in MANIFESTS:
    path = BASE / manifest
    raw = path.read_bytes()
    (HERE / 'inputs' / manifest).write_bytes(raw)
    entries = json.loads(raw)
    for entry in entries:
        source = Path(entry['path'])
        body = source.read_bytes()
        digest = hashlib.sha256(body).hexdigest()
        good = len(body) == entry['bytes'] and digest == entry['sha256']
        records.append({'manifest': manifest, 'path': str(source), 'bytes': len(body), 'sha256': digest, 'matches': good})
        if not good:
            raise RuntimeError('Bound input mismatch: ' + str(source))
        if manifest == MANIFESTS[0]:
            group = 'G331' if source.name[:2] in ('00','01','02','03','04') else 'working'
            (HERE / 'inputs' / group / source.name).write_bytes(body)
        elif source.name == 'Swanson-Huneke-author-book.txt':
            lines = body.decode().splitlines(keepends=True)
            for name, first, last in [('SH-17.1.6-17.2',16025,16178),('SH-17.4',16315,16638),('SH-17.5',16640,16830),('SH-8.4.2',7745,7808),('SH-6.8',6540,6632)]:
                unit = ''.join(lines[first-1:last])
                (HERE / 'evidence/source-units' / (name + '.txt')).write_text(unit)
        elif source.name == 'BFJ-valuations-psh.txt':
            lines = body.decode().splitlines(keepends=True)
            for name, first, last in [('BFJ-setting',335,362),('BFJ-section4',1395,1640)]:
                (HERE / 'evidence/source-units' / (name + '.txt')).write_text(''.join(lines[first-1:last]))
(HERE / 'evidence/input-audit.json').write_text(json.dumps(records, indent=2)+'\n')
task_path=HERE/'input.json'
if task_path.is_file():
    raw=task_path.read_bytes()
    (HERE/'evidence/local-task-input.json').write_text(json.dumps({'path':'input.json','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'treatment':'Complete supplied original problem, family dossier, G331 and assignment data; unchanged'},indent=2)+'\n')
(HERE / 'evidence/environment.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'cwd':str(HERE),'network_used':False,'supplied_programs_executed_or_imported':False,'subagents_used':False,'compilation_performed':False,'supervised_compute':'No supervised compute tool exposed; none needed for these bounded checks.','cloud_runtime_status':'The skill-required environment_status tool is absent from ALL_TOOLS; no readiness inferred.'},indent=2)+'\n')
print(json.dumps({'bound_files':len(records),'matched':sum(r['matches'] for r in records),'copied_math_files':8,'local_task_input_retained':task_path.is_file(),'compilation':False}))
