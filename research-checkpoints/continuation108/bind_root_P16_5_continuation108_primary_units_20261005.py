"""Bind only the actual selected primary bodies read for the new108 note."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
N = R / 'root-checks/P16.5-divisor-reference-envelope-and-polar-test-20261005-continuation108.md'
D = R / 'root-checks/P16.5-continuation108-primary-units'
P = R / 'root-checks/public-P16.5-round-102-final-reader'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
D.mkdir()
premises = json.loads((P / 'external-premises.json').read_text())['premises']
units = []
for u in premises[9]['passages']:
    assert sha(P / u['artifact']) == u['sha256']
    assert (P / u['artifact']).read_text() == u['literal']
    units.append({**u, 'original_artifact': str(P / u['artifact']),
                  'entire_selected_unit_root_read': True, 'whole_primary_root_read': False})
for name, uid in [('P16.5-continuation106-primary-units', 'maximum-principle-4-12'),
                  ('P16.5-continuation106-primary-units', 'divisorial-determination-4-22')]:
    b = json.loads((R / 'root-checks' / name / 'binding.json').read_text())
    matching = [u for u in b['units'] if u['id'] == uid]
    assert len(matching) == 1, (uid, [u['id'] for u in b['units']])
    u = matching[0]
    assert sha(u['path']) == u['sha256']
    units.append({**u, 'literal': Path(u['path']).read_text(),
                  'entire_selected_unit_root_read': True, 'whole_primary_root_read': False})
b = json.loads((R / 'root-checks/P16.5-continuation107-primary-units/binding.json').read_text())
u = next(s for s in b['stacks_selected_bodies'] if s['tag'] == '01Q3')
assert sha(u['selected_mathematical_body']) == u['body_sha256']
units.append({**u, 'literal': Path(u['selected_mathematical_body']).read_text()})
record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'note': str(N),
          'note_sha256': sha(N), 'entire_note_root_read': True,
          'independent_review_performed': False, 'original_closed': False,
          'hot_feedback_to_active105_sent': False, 'units': units,
          'capacity_exponent': 'Only alpha=1/(n+2) is used; larger printed Corollary7.48 exponent range is not assumed.'}
(D / 'binding.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'note_sha256': sha(N), 'selected_units': len(units), 'original_closed': False}, indent=2))
