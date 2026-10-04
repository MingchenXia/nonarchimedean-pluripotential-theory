from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research/root-checks/public-smooth-round-44-final-reader')
P = R / 'reproduction'
assert not P.exists()
shutil.copytree(R, P)
out = R / 'reproduction-result.json'
assert not out.exists()

def bind(p):
    data = Path(p).read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

runs = []
for helper in ['verify_sources.py', 'build_and_check.py']:
    result = subprocess.run(['python', helper], cwd=P, capture_output=True, text=True)
    transcript = P / ('root-' + helper + '.txt')
    transcript.write_text(result.stdout + result.stderr)
    runs.append({'helper': helper, 'returncode': result.returncode, 'transcript': bind(transcript)})
    assert result.returncode == 0, helper

compared = []
paths = [Path('P02.4-argument.md'), Path('P02.4-paper.tex'), Path('source-extracts/source-provenance.json')]
paths.extend(p.relative_to(R) for p in sorted((R / 'source-extracts').rglob('*.txt')))
for relative in paths:
    assert (R / relative).read_bytes() == (P / relative).read_bytes(), str(relative)
    compared.append({'relative': str(relative), 'identical': True, 'reproduced': bind(P / relative)})
diagnostics = json.loads((P / 'build-diagnostics.json').read_text())
checks = json.loads((P / 'checks.json').read_text())
assert checks['all_input_checks_passed'] and checks['two_tex_passes_succeeded'] and checks['markdown_generated']
assert all(x['returncode'] == 0 for x in diagnostics['runs'])
record = {'created_utc': datetime.now(timezone.utc).isoformat(),
          'helpers_fully_root_read_before_execution': True, 'runs': runs, 'comparisons': compared,
          'build_diagnostics': diagnostics, 'checks': checks, 'pdf': bind(P / 'P02.4-paper.pdf'),
          'mathematical_acceptance': False, 'original_target_closed': False,
          'interpretation': 'Source integrity and fresh two-pass reproduction only; not correctness certification.'}
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'record': bind(out), 'identical_units': len(compared), 'pdf': record['pdf'],
                  'tex_codes': [x['returncode'] for x in diagnostics['runs']],
                  'warnings': [x.get('warnings', []) for x in diagnostics['runs']],
                  'layout': [x.get('layout_diagnostics', []) for x in diagnostics['runs']]}))
