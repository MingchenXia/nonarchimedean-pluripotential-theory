#!/usr/bin/env python3
"""Preserve the supplied input bytes and the exact assignment string/task object."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
data = (root / 'input.json').read_bytes()
original = root / 'input-original.json'
if original.exists():
    assert original.read_bytes() == data, 'Do not replace a differing retained original.'
else:
    original.write_bytes(data)
obj = json.loads(data)
assignment = root / 'assignment-original.txt'
if assignment.exists():
    assert assignment.read_text() == obj['assignment']
else:
    assignment.write_text(obj['assignment'])
task = root / 'task-original.json'
if task.exists():
    assert json.loads(task.read_text()) == obj['task']
else:
    task.write_text(json.dumps(obj['task'], ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'input_sha256':hashlib.sha256(data).hexdigest(),
                  'byte_identity':True, 'assignment_string_identity':True,
                  'task_object_identity':True}))
