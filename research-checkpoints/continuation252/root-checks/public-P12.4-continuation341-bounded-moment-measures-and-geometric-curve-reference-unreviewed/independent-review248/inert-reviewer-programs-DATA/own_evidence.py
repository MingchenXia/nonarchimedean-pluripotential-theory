"""Fresh finite checks and documentary comparisons; supplied programs stay inert."""
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def load(name):
    return json.loads((ROOT / name).read_text())
def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2) + '\n')

data = load('bounded-evidence-input.json')
curve = []
for degree, order, power in itertools.product(data['curve']['degrees'], data['curve']['orders'], data['curve']['powers']):
    monomials = {('constant', 0, 0)}
    monomials.update(('branch', exponent, coefficient) for exponent in range(1, order * power)
                     for coefficient in range(degree))
    count = len(monomials)
    assert count == 1 + degree * (order * power - 1)
    curve.append({'d': degree, 'r': order, 'N': power, 'count': count})
nil = []
for power in data['nilpotent']['powers']:
    basis = {(exponent, epsilon) for exponent in range(power) for epsilon in (0, 1)}
    assert len(basis) == 2 * power
    nil.append({'N': power, 'reduced': power, 'thickened': len(basis)})
gauge = []
for old, new, test in itertools.product(data['gauge']['old'], data['gauge']['new'], data['gauge']['test']):
    transported = [Fraction(a) * Fraction(b, a) for a, b in zip(old, new)]
    before = sum(Fraction(a) * Fraction(j, a) for a, j in zip(old, test))
    after = sum(mass * Fraction(j, b) for mass, j, b in zip(transported, test, new))
    assert before == after == sum(test)
    gauge.append({'old': old, 'new': new, 'test': test, 'moment': str(after)})
assert 2 != 3
write('reports/own-exact-diagnostics.json', {'status': 'PASS', 'curve_cases': len(curve),
      'nilpotent_cases': len(nil), 'gauge_cases': len(gauge), 'curve': curve,
      'nilpotent': nil, 'gauge': gauge, 'toy_masses': [2, 3], 'limits': data['limits']})

current = load('input.json')
controller = load('inputs/historical/00-input.json')
worker = load('inputs/historical/07-input.json')
grant = load('inputs/mathematical/08-G331-qualified-grant.json')
identity = {'controller_worker_decoded_whole_equal': controller == worker,
            'current_grant_equals_bound': current['notes'][0] == grant,
            'controller_grant_equals_bound': controller['notes'][0] == grant,
            'worker_grant_equals_bound': worker['notes'][0] == grant,
            'original_family_prefix_equal': current['task']['problem'].split('ROOT AUTHORIZED')[0]
                 == controller['task']['problem'].split('ROOT AUTHORIZED')[0],
            'current_augmented_task_equals_original_assignment': current['task'] == controller['task'],
            'original_task_file_not_supplied': True}
markers = {
 '09-G331-paper.tex': ('BEGIN ENTIRE P12.2-paper.tex', 'END ENTIRE P12.2-paper.tex'),
 '10-G331-mandatory-source-scope.json': ('BEGIN ENTIRE mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json', 'END ENTIRE mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json'),
 '11-G331-source-application-ledger.md': ('BEGIN ENTIRE source-application-ledger.md', 'END ENTIRE source-application-ledger.md'),
 '12-G331-exact-scope.md': ('BEGIN ENTIRE exact-scope.md', 'END ENTIRE exact-scope.md')}
for name, (start, end) in markers.items():
    body = (ROOT / 'inputs/mathematical' / name).read_bytes()
    embedded = grant['text'].split(start, 1)[1].split(end, 1)[0].strip()
    identity[name] = {'matches_embedded_body_after_boundary_whitespace': embedded == body.decode().strip(),
                     'sha256': hashlib.sha256(body).hexdigest()}
write('reports/task-grant-identity.json', identity)

available = load('reports/input-bindings.json')
byhash = {r['sha256']: r['local'] for r in available}
historical = load('inputs/historical/08-own-bindings.json')['files']
matched, missing = [], []
for row in historical:
    (matched if row['sha256'] in byhash else missing).append(row['path'])
# Note bodies are available in the expanded JSON, even though standalone paths are absent.
expanded = load('inputs/mathematical/06-native-notes.json')
body_hits = []
for note in expanded['notes']:
    digest = hashlib.sha256(note['text'].encode()).hexdigest()
    for row in historical:
        if row['path'] == note['id'] + '.md' and row['sha256'] == digest:
            body_hits.append(row['path'])
write('reports/historical-coverage.json', {'declared_records': len(historical),
      'direct_hash_matched': matched, 'not_directly_available': missing,
      'note_bodies_recovered_and_matched_from_expanded_json': body_hits,
      'limits': 'Missing paths were not opened. Historical execution/provider claims are not freshly attested.'})

build = load('inputs/historical/12-build-results.json')
summary = []
for command in build['commands']:
    summary.append({'argv': command['argv'], 'attempt': command.get('attempt'),
       'exit_code': command['exit_code'], 'diagnostic_lines': [line for line in command['stdout'].splitlines()
       if any(x in line for x in ['Underfull', 'Overfull', 'LaTeX Warning', 'Output written'])]})
proc = subprocess.run(['pdfinfo', str(ROOT / 'inputs/historical/14-P12.4-paper.pdf')],
                      text=True, capture_output=True, check=True)
write('reports/pdf-build-observations.json', {'fresh_pdfinfo': proc.stdout,
      'historical_build_commands': summary, 'fresh_compilation': False,
      'reason': 'ROOT owns compilation; no TeX or supplied builder was executed.'})
print(json.dumps({'status': 'PASS', 'curve': len(curve), 'nilpotent': len(nil), 'gauge': len(gauge),
                  'bound_bodies': len(available), 'historical_direct_matches': len(matched),
                  'recovered_notes': len(body_hits)}))
