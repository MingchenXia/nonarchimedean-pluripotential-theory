"""Own read-only identity checks. Never import or execute supplied programs."""
import hashlib
import json
import pathlib
import platform
import sys

BASE = pathlib.Path('/workspace/research/campaigns/round-241/P05.2-original-carrier-tree-primitive-polynomial-independent-whole-proof-and-scope-review')
OLD = pathlib.Path('/workspace/research/campaigns/round-239/P05.2-original-finite-carrier-PCC-tree-and-raw-contact-classification')

def read_json(path):
    return json.loads(pathlib.Path(path).read_text())

def binding(path):
    path = pathlib.Path(path)
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def verify(row):
    got = binding(row['path'])
    got['matches'] = got['bytes'] == row['bytes'] and got['sha256'] == row['sha256']
    return got

math = read_json(BASE / 'mathematical-packet-bindings.json')
primary = read_json(BASE / 'private-primary-packet-bindings.json')
history = read_json(BASE / 'historical-own-evidence-bindings.json')
own_history = read_json(history[0]['path'])
input_history = read_json(history[1]['path'])
own_rows = [verify(row) for row in own_history['files']]
stream_rows = [verify(row) for row in input_history['immutable_streams']]
control_rows = [verify(input_history[key]) for key in ('initial_input', 'original', 'packet_manifest', 'primary_manifest')]
controller = read_json(OLD / 'input.json')
native = read_json(input_history['initial_input']['path'])
current = read_json('input.json')
text_rows = []
for wanted in read_json(BASE / 'qualified-imported-note-bindings.json'):
    note = next(n for n in current['notes'] if n['id'] == wanted['id'])
    data = note['text'].encode('utf-8')
    text_rows.append({'id': note['id'], 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                      'matches': len(data) == wanted['text_bytes'] and hashlib.sha256(data).hexdigest() == wanted['text_sha256'],
                      'checks_empty': note.get('checks') == []})
actual_path = pathlib.Path(math[44]['path'])
actual = read_json(actual_path)
saved_path = next(pathlib.Path(row['path']) for row in own_history['files'] if row['path'].endswith('/native-notes.json'))
saved = read_json(saved_path)
actual_bytes, saved_bytes = actual_path.read_bytes(), saved_path.read_bytes()
object_fields = [{'id': a['id'], 'all_fields_equal': a == s, 'keys': sorted(a)} for a, s in zip(actual['notes'], saved['notes'])]
component_rows = []
for i, row in enumerate(math[:38]):
    body = pathlib.Path(row['path']).read_text()
    owners = [n['id'] for n in current['notes'] if body in n['text']]
    component_rows.append({'index': i, 'path': row['path'], 'exact_body_contained_in_supplied_notes': owners})
results = {
    'mathematical_packet': [verify(row) for row in math],
    'private_primaries': [verify(row) for row in primary],
    'historical_evidence_files': [verify(row) for row in history],
    'historical_author_owned_33': own_rows,
    'historical_frozen_43': stream_rows,
    'historical_input_controls_4': control_rows,
    'qualified_note_text_bindings': text_rows,
    'qualified_component_containment': component_rows,
    'input_identity': {
        'controller': binding(OLD / 'input.json'), 'native': binding(input_history['initial_input']['path']),
        'task_equal': controller['task'] == native['task'], 'notes_equal': controller['notes'] == native['notes'],
        'assignment_equal': controller['assignment'] == native['assignment'],
        'byte_equal': (OLD / 'input.json').read_bytes() == pathlib.Path(input_history['initial_input']['path']).read_bytes(),
        'current_qualified_notes_equal_frozen_author_notes': current['notes'] == native['notes'],
        'current_original_problem_chars': len(read_json(BASE / 'original-task.json')['problem']),
        'original_task_equal_author_original': read_json(BASE / 'original-task.json') == read_json(input_history['original']['path'])
    },
    'actual_saved_identity': {
        'actual': binding(actual_path), 'saved': binding(saved_path),
        'objects_equal': actual == saved, 'candidate_equal': actual['candidate'] == saved['candidate'],
        'candidate': actual['candidate'], 'all_five_fields': object_fields,
        'byte_equal': actual_bytes == saved_bytes,
        'saved_is_actual_plus_one_newline': saved_bytes == actual_bytes + b'\n'
    },
    'controls': [binding(BASE / name) for name in ('original-task.json', 'input.json', 'task.json', 'mathematical-packet-bindings.json', 'private-primary-packet-bindings.json', 'historical-own-evidence-bindings.json', 'qualified-imported-note-bindings.json')] + [binding('input.json')],
    'environment': {'python': sys.version, 'platform': platform.platform(), 'cwd': str(pathlib.Path.cwd()),
                    'provider_identity': 'not independently attested', 'supplied_programs_executed_or_imported': False}
}
pathlib.Path('input-bindings.json').write_text(json.dumps(results, indent=2, ensure_ascii=False) + '\n')
summary = {'groups': {key: {'verified': len(results[key]), 'all_match': all(r['matches'] for r in results[key])}
                     for key in ('mathematical_packet', 'private_primaries', 'historical_evidence_files', 'historical_author_owned_33', 'historical_frozen_43', 'historical_input_controls_4', 'qualified_note_text_bindings')},
           'input_identity': results['input_identity'], 'actual_saved_identity': results['actual_saved_identity'],
           'qualified_components_in_notes': sum(bool(r['exact_body_contained_in_supplied_notes']) for r in component_rows)}
pathlib.Path('identity-output.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(summary, indent=2, ensure_ascii=False))
