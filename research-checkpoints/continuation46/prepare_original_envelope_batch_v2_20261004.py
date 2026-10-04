"""Preserve the rejected original input; render forbidden OCR controls visibly.

The first P03.1 process stopped at schema validation before any provider call.
No mathematical interpretation of the OCR characters is made.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest = json.loads((R / 'original-envelope-batch-manifest-20261004.json').read_text())
forbidden = re.compile(r'[\x00-\x08\x0e-\x1f\x7f]')
records = []
for rec in manifest['campaigns']:
    directory = Path(rec['directory'])
    old = json.loads((directory / 'input.json').read_text())
    original = old['task']['problem']
    controls = [{'character_offset': m.start(), 'codepoint': f'U+{ord(m.group()):04X}',
                 'replacement': f'[OCR control U+{ord(m.group()):04X}]'} for m in forbidden.finditer(original)]
    assert controls
    new = json.loads(json.dumps(old))
    new['task']['problem'] = forbidden.sub(lambda m: f'[OCR control U+{ord(m.group()):04X}]', original)
    new['assignment'] += '\nPDF extraction contains forbidden control characters. The task displays each as [OCR control U+XXXX]; no mathematical interpretation is supplied. All other dossier characters are unchanged.\n'
    assert not forbidden.search(new['task']['problem'])
    assert new['notes'] == []
    out = directory / 'input-v2.json'
    assert not out.exists()
    out.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
    correction = {'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'original_input': str(directory / 'input.json'), 'original_sha256': sha(directory / 'input.json'),
                  'selected_input': str(out), 'selected_sha256': sha(out),
                  'changes': controls, 'mathematical_text_otherwise_unchanged': True,
                  'original_provider_call_occurred': False,
                  'reason': 'Xean rejected task.problem control characters at input schema validation before launch.'}
    (directory / 'input-v2-correction.json').write_text(json.dumps(correction, indent=2) + '\n')
    if rec['atom'] == 'P03.1':
        assert (directory / 'run.json').stat().st_size == 0
        assert 'must match pattern' in (directory / 'run.stderr').read_text()
        (directory / 'launch-v1-schema-failure.json').write_text(json.dumps({
            'recorded_utc': correction['recorded_utc'], 'stderr_sha256': sha(directory / 'run.stderr'),
            'exit_code': 1, 'provider_started': False, 'campaign_sqlite_created': (directory / 'campaign.sqlite').exists()
        }, indent=2) + '\n')
    records.append({**rec, 'selected_input': str(out), 'input_sha256': sha(out),
                    'input_bytes': out.stat().st_size, 'state': 'PREPARED_V2_LOCAL_ONLY',
                    'ocr_control_count': len(controls)})
out = R / 'original-envelope-batch-v2-manifest-20261004.json'
assert not out.exists()
out.write_text(json.dumps({**manifest, 'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                          'campaigns': records, 'ocr_controls_displayed_explicitly': True,
                          'first_launch_failed_before_provider_call': True}, indent=2) + '\n')
print(json.dumps({'manifest': str(out), 'sha256': sha(out), 'campaigns': records}, indent=2))
