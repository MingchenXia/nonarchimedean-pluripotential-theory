"""Preserve unlaunched62 and freeze an unambiguous eleven-source scope for63."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-62/P13.1-public-source-extended-semigroup-and-uniform-energy-differentiation'
C = R / 'campaigns/round-63/P13.1-public-source-eleven-body-semigroup-and-uniform-differentiation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
m = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == m['input_sha256']
assert sha(old / 'settings.json') == m['settings_sha256']
assert not (old / 'campaign.sqlite').exists()
d = json.loads((old / 'input.json').read_text())
a = d['assignment']
for before, after in [
    ('ten actual public primary sources', 'eleven actual public primary sources'),
    ('ten listed actual public primary caches', 'eleven listed actual public primary caches')
]:
    assert a.count(before) == 1
    a = a.replace(before, after)
d['assignment'] = a
assert d['task'] == json.loads((old / 'input.json').read_text())['task']
assert d['notes'] == [] and len(m['public_sources']) == 11
for s in m['public_sources']:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
for item in m['embedded_context']:
    assert sha(item['path']) == item['sha256']
    assert Path(item['path']).read_text() in a
C.mkdir(parents=True, exist_ok=False)
(C / 'input.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
s = json.loads((old / 'settings.json').read_text())
s['usagePrefix'] = 'catalogue-20261003/r63/P13.1-eleven-body-semigroup-and-uniform-differentiation'
s['codex']['workspace'] = str(C / 'artifacts')
(C / 'settings.json').write_text(json.dumps(s, indent=2) + '\n')
manifest = {**m, 'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 63,
    'directory': str(C), 'input_sha256': sha(C / 'input.json'), 'settings_sha256': sha(C / 'settings.json'),
    'supersedes_unlaunched_round62': True, 'unlaunched_round62_input_sha256': sha(old / 'input.json'),
    'scope_repair': 'Both inherited source-read clauses now explicitly permit all eleven actual primary caches.',
    'state': 'PREPARED LOCAL ONLY; not launched. Wait for a free slot in the two-item native batch.'}
(C / 'input-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'directory': str(C), 'input_sha256': manifest['input_sha256'],
                  'settings_sha256': manifest['settings_sha256'], 'bytes': (C / 'input.json').stat().st_size,
                  'sources': 11, 'context_bodies': len(m['embedded_context']),
                  'original_task_unchanged': True, 'launched': False}, indent=2))
