#!/usr/bin/env python3
"""Check artifact integrity and execution facts, not mathematical validity."""
import hashlib
import json
import subprocess
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


record = json.loads(Path('input-preservation.json').read_text())
assert sha('input.json') == record['input.json_sha256']
assert Path('input.json').read_bytes() == Path('input-original.json').read_bytes()
input_data = json.loads(Path('input.json').read_text())
assert json.loads(Path('task-original.json').read_text()) == input_data['task']
assert Path('assignment-original.txt').read_text() == input_data['assignment']
status = json.loads(Path('status.json').read_text())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert status['status'] == 'partial' and status['concrete_gaps']
finite = json.loads(Path('finite-graph-output.json').read_text())
assert finite['passed'] and len(finite['examples']) == 8
build = json.loads(Path('build-record.json').read_text())
assert build['both_passes_succeeded'] and len(build['runs']) == 2
assert all(r['exit_code'] == 0 for r in build['runs'])
provenance = json.loads(Path('source-provenance.json').read_text())
assert provenance['primary_theorems_applied'] == []
notes = json.loads(Path('notes.json').read_text())
assert notes['candidate'] is False and 1 <= len(notes['notes']) <= 4
seen = set()
for note in notes['notes']:
    assert set(note) == {'id','summary','detailedSummary','text','support'}
    assert all(s in seen for s in note['support'])
    assert note['id'] not in seen
    seen.add(note['id'])
for name in ['P03.3-argument.md','P03.3-paper.tex','status.json','notes.json']:
    b = Path(name).read_bytes()
    assert not any(c < 32 and c not in (9,10,13) for c in b), name
# Preserve a human-readable PDF extraction for checking that the whole argument
# was rendered. No interpretation of the original task's OCR markers is made.
subprocess.run(['pdftotext','P03.3-paper.pdf','P03.3-paper-rendered.txt'], check=True, timeout=20)
rendered = Path('P03.3-paper-rendered.txt').read_text()
assert 'sharp classification' in rendered
assert 'Proper fibres' in rendered
assert 'Scalar extensions' in rendered
assert 'Reproducibility' in rendered
required = ['input.json','input-original.json','task-original.json','assignment-original.txt',
            'P03.3-argument.md','P03.3-paper.tex','P03.3-paper.pdf','finite_graph_envelope.py',
            'finite-graph-input.json','finite-graph-output.json','source-provenance.json',
            'status.json','notes.json','build-record.json','environment.json','commands.json']
result = {'input_preserved': True, 'status_schema_exact': True,
          'notes_supports_earlier_local_ids_only': True, 'candidate': False,
          'finite_graph_examples_passed': 8,
          'contact_sets_enumerated_in_original_examples': sum(e['enumerated_contact_sets'] for e in finite['examples']),
          'contact_sets_enumerated_in_translation_checks': sum(e['enumerated_contact_sets'] for e in finite['examples']),
          'tex_passes_succeeded': 2, 'paper_rendered_sections_checked': True,
          'hashes': {name: sha(name) for name in required},
          'scope': 'Artifact integrity and finite execution checks only; no certificate of mathematical or analytic correctness.'}
Path('verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k != 'hashes'}, indent=2))
