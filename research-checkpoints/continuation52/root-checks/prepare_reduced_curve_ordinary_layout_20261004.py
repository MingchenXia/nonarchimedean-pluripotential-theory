from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

d = Path('/workspace/research/root-checks/P02.4-reduced-curve-ordinary-paper-20261004')
source = d / 'P02.4-reduced-curve-ordinary-paper.tex'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(source) == 'b433f1288f19689ffe6c3649bade5b9cfb70bbaa9bf6e2bfc904499539328ea3'
out = d / 'P02.4-reduced-curve-ordinary-paper-layout.tex'
assert not out.exists()
literal_names = [
    'p063_curve_cld_monotone_regularization_statement_20260827.tex',
    'p063_curve_cld_monotone_regularization_proof_20260827.tex',
    '767cbf81c723279c1218df4136f8e299465240b325f41f6b0663d001fb5d8a68',
    'd1db3c2db861d920598697fdad5d002a2b1ce947dbdbd95ad9b78b8f9f312bd8',
    'P02.4-fixed-domain-net-and-sequence-bridge-20261004.md']
s = source.read_text()
changes = []
for name in literal_names:
    old = '\\texttt{' + name.replace('_', '\\_') + '}'
    new = '\\nolinkurl{' + name + '}'
    assert s.count(old) == 1
    s = s.replace(old, new)
    changes.append({'old': old, 'new': new, 'purpose': 'Allow line breaks in literal reference names and hashes without changing text or mathematics.'})
out.write_text(s)
record = {'prepared_utc': datetime.now(timezone.utc).isoformat(),
    'original_source': str(source), 'original_source_sha256': sha(source),
    'layout_source': str(out), 'layout_source_sha256': sha(out),
    'exact_changes': changes, 'mathematical_changes': [],
    'original_compiled_source_preserved': True, 'independent_acceptance': False,
    'original_atoms_closed': []}
(d / 'layout-only-successor.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
