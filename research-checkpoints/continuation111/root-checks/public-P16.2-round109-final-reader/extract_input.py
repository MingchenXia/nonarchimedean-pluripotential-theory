"""Preserve the supplied mathematical data without reading any external workspace."""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
inp = json.loads((ROOT / 'input.json').read_text())
out = ROOT / 'supplied'
out.mkdir(exist_ok=True)
(out / 'task.json').write_text(json.dumps(inp['task'], ensure_ascii=False, indent=2) + '\n')
(out / 'assignment.txt').write_text(inp['assignment'])
blocks = []
for i, m in enumerate(re.finditer(r'^BEGIN MATHEMATICAL DATA: (.*?)\n(.*?)^END MATHEMATICAL DATA', inp['assignment'], re.M | re.S)):
    title, body = m.groups()
    suffix = '.txt'
    try:
        data = json.loads(body)
        suffix = '.json'
    except json.JSONDecodeError:
        data = None
    path = out / f'block-{i:02d}{suffix}'
    path.write_text(body)
    blocks.append(dict(title=title, file=str(path.relative_to(ROOT)), sha256=hashlib.sha256(body.encode()).hexdigest()))
    if isinstance(data, list) and 'primary statements' in title:
        directory = ROOT / 'evidence' / 'supplied-new'
        directory.mkdir(parents=True, exist_ok=True)
        records = []
        for j, record in enumerate(data):
            literal = record.get('literal', '')
            local = directory / f'unit-{j:02d}.txt'
            local.write_text(literal)
            metadata = {k: v for k, v in record.items() if k != 'literal'}
            metadata.update(local_file=str(local.relative_to(ROOT)), local_sha256=hashlib.sha256(literal.encode()).hexdigest(), locally_read=False)
            records.append(metadata)
        (directory / 'index.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    if isinstance(data, dict) and 'Whole68' in title:
        directory = ROOT / 'evidence' / 'ample-primary'
        directory.mkdir(parents=True, exist_ok=True)
        for key, record in data.items():
            (directory / f'{key}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
(out / 'index.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(blocks, ensure_ascii=False, indent=2))
