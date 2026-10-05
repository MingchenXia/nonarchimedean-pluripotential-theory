#!/usr/bin/env python3
"""Preserve supplied mathematical data, without accessing historical paths."""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent

def sha(b):
    return hashlib.sha256(b).hexdigest()

def main():
    data = json.loads((ROOT / 'input.json').read_text())
    out = ROOT / 'evidence'
    out.mkdir(exist_ok=True)
    (out / 'assignment.txt').write_text(data['assignment'])
    (out / 'task.json').write_text(json.dumps(data['task'], ensure_ascii=False, indent=2) + '\n')
    s = data['assignment']
    pattern = re.compile(r'BEGIN (MATHEMATICAL DATA: [^\n]*|ADDITIONAL SELECTED PRIMARY UNITS)\n(.*?)\nEND (?:MATHEMATICAL DATA|ADDITIONAL SELECTED PRIMARY UNITS)', re.S)
    index = []
    for i, m in enumerate(pattern.finditer(s)):
        body = m.group(2)
        name = f'packet-{i:02d}.txt'
        (out / name).write_text(body)
        entry = {'id': i, 'title': m.group(1), 'file': f'evidence/{name}',
                 'sha256': sha(body.encode()), 'assignment_characters': [m.start(2), m.end(2)]}
        try:
            obj = json.loads(body)
            (out / f'packet-{i:02d}.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
            entry['parsed_type'] = type(obj).__name__
            if isinstance(obj, dict):
                entry['keys'] = list(obj)
        except json.JSONDecodeError:
            pass
        index.append(entry)
    (out / 'packet-index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(index, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
