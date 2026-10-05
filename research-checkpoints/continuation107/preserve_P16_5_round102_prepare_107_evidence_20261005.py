"""Preserve completed102 and bind the additional actual107 primary readings."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

R = Path('/workspace/research')
C = R / 'campaigns/round-102/P16.5-original-nonample-finite-energy-equation-research'
W = C / 'artifacts/codex-HN1jzb'
P = R / 'root-checks/public-P16.5-round-102-final-reader'
B = R / 'root-checks/P16.5-continuation107-primary-units'
N = R / 'root-checks/P16.5-fixed-divisor-local-products-20261005-continuation107.md'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


assert not P.exists() and not B.exists()
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('input.json', 'input_sha256'), ('task-original.json', 'task_sha256'),
                  ('assignment-original.txt', 'assignment_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
v = json.loads((C / 'run.json').read_text())['campaign']
assert v['status'] == 'completed'
result = v['result']
assert result['kind'] == 'notes' and result['candidate'] is False
assert result['workspace'] == str(W) and len(result['notes']) == 4
seen = []
for n in result['notes']:
    assert n['id'] not in seen and all(s in seen for s in n['support'])
    seen.append(n['id'])
assert json.loads((W / 'input-original.json').read_text()) == json.loads((C / 'input.json').read_text())
assert (W / 'task-original.json').read_bytes() == (C / 'task-original.json').read_bytes()
assert (W / 'assignment-original.txt').read_bytes() == (C / 'assignment-original.txt').read_bytes()
manifest = json.loads((W / 'artifact-manifest.json').read_text())
assert len(manifest['files']) == 178
for item in manifest['files']:
    p = W / item['path']
    assert p.stat().st_size == item['bytes'] and sha(p) == item['sha256']
premises = json.loads((W / 'external-premises.json').read_text())['premises']
assert [p['index'] for p in premises] == list(range(10))
unit_count = 0
for premise in premises:
    for u in premise['passages']:
        assert u['url'].startswith('https://') and sha(W / u['artifact']) == u['sha256']
        assert (W / u['artifact']).read_text() == u['literal']
        unit_count += 1
artifacts = []
for p in sorted(W.rglob('*')):
    assert not p.is_symlink()
    if p.is_file():
        parts = p.relative_to(W).parts
        assert p.suffix not in {'.sqlite', '.jsonl'}
        assert not any(x in {'.git', '.codex', '.aws', '.env', 'auth.json', 'run.json'} for x in parts)
        artifacts.append({'path': str(p.relative_to(W)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
shutil.copytree(W, P)
save(P / 'root-independent-artifact-manifest.json', {
    'original_workspace': str(W), 'artifacts': artifacts,
    'native178_manifest_bindings_verified': True, 'literal_passage_bindings_checked': unit_count,
    'mathematical_acceptance_asserted': False,
})
canonical = R / 'root-checks/P16.5-round102-canonical-native-result-20261005.json'
save(canonical, result)
save(R / 'root-checks/P16.5-round102-root-reading-binding-20261005.json', {
    'canonical_result': str(canonical), 'sha256': sha(canonical),
    'whole4_canonical_notes_root_read': True, 'whole360_LF_argument_root_read': True,
    'all10_full_external_premise_records_root_read': False,
    'all_literal_passage_bytes_verified': True, 'all_primary_bodies_root_read': False,
    'BJ_addendum_Theorem_A_statement_full_proof_and_Corollaries_2_1_to_2_3_root_read': True,
    'input_json_values_equal': True, 'input_bytes_equal': False,
    'frozen_input_sha256': sha(C / 'input.json'), 'artifact_input_sha256': sha(P / 'input-original.json'),
    'original_task_assignment_bytes_equal': True, 'candidate': False,
    'independent_review_performed': False, 'original_closed': False,
})
B.mkdir()
units = []
for origin, label, url, intervals in [
    ('root-checks/public-P16.1-round-92-final-reader/sources/S1-literal_extract.txt', 'BJ1801.08229v4',
     'https://arxiv.org/pdf/1801.08229v4', [('locality-7-40-and-comparison-proof', 4530, 4600)]),
    ('root-checks/public-P16.1-round-92-final-reader/sources/S7-literal_extract.txt', 'BE1805.01016v3',
     'https://arxiv.org/pdf/1805.01016v3', [('semiample-regularization', 2320, 2390),
      ('continuous-mixed-measures-proof', 2610, 2760), ('section-integrability-and-Poincare-Lelong', 2760, 2935)]),
    ('root-checks/public-P21.3-round-100-final-reader/sources/cld-v2-full.txt', 'CLD1204.6277v2',
     'https://arxiv.org/pdf/1204.6277v2', [('frame-invariance-and-Poincare-Lelong', 25720, 25830),
      ('actual-cycle-metric-products', 26675, 26790), ('local-paralinear-unit-weights', 10485, 10593)]),
]:
    source = R / origin
    lines = source.read_text().split('\n')
    for uid, lo, hi in intervals:
        p = B / (uid + '.txt')
        p.write_text('\n'.join(lines[lo - 1:hi]) + '\n')
        units.append({'id': uid, 'path': str(p), 'sha256': sha(p),
                      'source': str(source), 'source_sha256': sha(source), 'version': label,
                      'url': url, 'inclusive_one_based_LF': [lo, hi],
                      'selected_interval_root_read': True, 'whole_primary_root_read': False})
stacks = json.loads((R / 'root-checks/P16.5-continuation107-stacks-primary/retrieval-manifest.json').read_text())
for s in stacks:
    assert sha(s['raw_html']) == s['raw_html_sha256']
    assert sha(s['selected_mathematical_body']) == s['body_sha256']
    s['selected_body_root_read'] = True
    s['whole_raw_page_root_read'] = False
save(B / 'binding.json', {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'note': str(N), 'note_sha256': sha(N), 'note_entire_root_read': True,
    'independently_reviewed': False, 'original_closed': False,
    'units': units, 'stacks_selected_bodies': stacks,
    'reading_limit': 'Selected literal intervals were read. Whole primary documents were not. Stacks31.16.1 prints an omitted proof and hint; no full printed proof is claimed.',
})
print(json.dumps({'public_reader': str(P), 'canonical': str(canonical),
                  'artifact_entries': len(artifacts), 'native_manifest_entries': 178,
                  'literal_passage_bindings': unit_count, 'new_primary_units': len(units),
                  'candidate': False, 'original_closed': False}, indent=2))
