"""Meaningful own deliverable checks; never executes a checker or compiler."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
required = ['audit-report.md', 'reconstructed-proof.md', 'source-application-ledger.md',
            'whole-proof-coverage.md', 'whole-proof-coverage.json', 'evidence-report.md',
            'notes.json', 'frozen-bindings-verified.json', 'binding-recheck.json',
            'reproduction-report.json', 'historical-evidence-report.json',
            'historical-inventory-subset.json', 'saved-six-lossless-reader.json',
            'lossless-reading-checks.json']
assert all((root / name).is_file() for name in required)
notes = json.loads((root / 'notes.json').read_text())
assert notes['candidate'] is False
seen = set()
for i, n in enumerate(notes['notes'], 1):
    assert n['id'] == f'n{i}' and n['summary'] and n['detailedSummary'] and n['text']
    assert set(n['support']) <= seen
    seen.add(n['id'])
assert len(seen) == 6
coverage = json.loads((root / 'whole-proof-coverage.json').read_text())
assert len(coverage['whole_mathematical_bodies']) == 33
assert len(coverage['new306_parallel_argument_blocks']) == 102
assert len(coverage['actual_FINAL_notes']) == 6
assert coverage['candidate'] is False
assert coverage['original_P05_1'] == coverage['original_P05_2'] == 'OPEN'
bindings = json.loads((root / 'binding-recheck.json').read_text())
assert bindings['all_match'] and bindings['counts'] == {'math': 33, 'evidence': 98, 'primary': 4}
tex = (root / 'reproduction' / 'P05.1-paper.tex').read_bytes()
assert tex == (root / 'reproduction' / 'generated-paper.tex').read_bytes()
assert hashlib.sha256(tex).hexdigest() == '121e25eeb7b89371cc89d54c1bce1b4f1037be9d4a6e38e037c45d8041fec737'
repro = json.loads((root / 'reproduction-report.json').read_text())
assert repro['checker_executions'] == 1 and repro['checker_exact_ROOT_output']
assert repro['exact_Markdown_to_TeX'] and repro['pandoc_exit_code'] == 0
assert [r['exit_code'] for r in repro['build']] == [0, 0, 0]
assert repro['build'][-1]['warnings'] == []
final_log = (root / 'reproduction' / 'reports' / 'pass3.tex.log').read_text()
assert not any('Warning' in s or 'Overfull' in s or 'Underfull' in s or s.startswith('!')
               for s in final_log.split('\n'))
assert '18 pages' in final_log
for path, digest in [
    ('finite/code/checks.py', '0917af33f5a82677a8c2ab402c6ded0496d7a3acd8c38a7bf49889812ed48b3d'),
    ('finite/inputs/check-input.json', '9fef943df42fb03108eee9cca89cb4132476208c4563c3df2ed2a057d672d671'),
    ('finite/reports/checks.stdout.json', 'f5e5733541e00967b33e40ea661c62fb25af3ed14299651ef47b0758442d760e')]:
    assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
assert (root / 'finite/reports/checks.stdout.json').read_bytes() == (
        root / 'finite/reports/exact-checks.json').read_bytes()
assert (root / 'finite/reports/checks.stderr.txt').read_bytes() == b''
inventory = json.loads((root / 'historical-inventory-subset.json').read_text())
assert (inventory['historical_entries'], inventory['supplied_entries'], inventory['matches'],
        inventory['unsupplied_entries_not_opened']) == (160, 73, 73, 87)
report = {'status': 'Own artifact/structure checks passed; not a mathematical proof verifier',
          'notes': 6, 'whole_bodies': 33, 'argument_blocks': 102,
          'bindings': 135, 'supplied_historical_inventory_entries': 73,
          'safe_checker_executions_recorded': 1,
          'exact_Markdown_to_TeX': True, 'build_exits': [0, 0, 0],
          'final_build_warnings': [], 'pages': 18, 'candidate': False,
          'original_P05_1': 'OPEN', 'original_P05_2': 'OPEN'}
(root / 'validation-report.json').write_text(json.dumps(report, indent=2) + '\n')

# Inventory only own visible root files and the three own artifact directories.
# Hidden/protected directories and any external/unbound path are never traversed.
files = [p for p in root.iterdir() if p.is_file() and not p.name.startswith('.')
         and p.name != 'own-artifact-hashes.json']
for name in ('inputs', 'finite', 'reproduction'):
    files.extend(p for p in (root / name).rglob('*') if p.is_file() and not p.is_symlink())
hashes = [{'filename': str(p.relative_to(root)), 'bytes': p.stat().st_size,
           'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]
(root / 'own-artifact-hashes.json').write_text(json.dumps({
    'status': 'Fresh own artifact inventory; mathematical correctness not certified',
    'self_hash': 'Excluded to avoid circularity', 'artifacts': hashes}, indent=2) + '\n')
print(json.dumps(report))
print('own hashed artifacts', len(hashes))
