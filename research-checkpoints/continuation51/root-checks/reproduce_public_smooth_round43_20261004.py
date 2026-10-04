from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research/root-checks/public-smooth-round-43-final-reader')
P = R / 'reproduction'
assert not P.exists()
shutil.copytree(R, P)
out = R / 'reproduction-result.json'
assert not out.exists()

def bind(p):
    data = Path(p).read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

runs = []
for helper in ['collect_sources.py', 'make_paper.py', 'build_paper.py', 'audit_artifacts.py']:
    result = subprocess.run(['python', helper], cwd=P, capture_output=True, text=True)
    transcript = P / ('root-' + helper + '.txt')
    transcript.write_text(result.stdout + result.stderr)
    runs.append({'helper': helper, 'returncode': result.returncode, 'transcript': bind(transcript)})
    assert result.returncode == 0, helper

compared = []
paths = [Path('P02.3-argument.md'), Path('P02.3-paper.tex'), Path('source-extracts/source-provenance.json')]
paths.extend(p.relative_to(R) for p in sorted((R / 'source-extracts').rglob('*.txt')))
for relative in paths:
    assert (R / relative).read_bytes() == (P / relative).read_bytes(), str(relative)
    compared.append({'relative': str(relative), 'identical': True, 'reproduced': bind(P / relative)})
diagnostics = json.loads((P / 'build-diagnostics.json').read_text())
audit = json.loads((P / 'artifact-audit.json').read_text())
assert diagnostics['both_successful'] and audit['all_passed']
assert all(x['returncode'] == 0 for x in diagnostics['builds'])
record = {'created_utc': datetime.now(timezone.utc).isoformat(),
          'helpers_fully_root_read_before_execution': True, 'runs': runs, 'comparisons': compared,
          'build_diagnostics': diagnostics, 'artifact_audit': audit, 'pdf': bind(P / 'P02.3-paper.pdf'),
          'mathematical_acceptance': False, 'original_target_closed': False,
          'interpretation': 'Source integrity and fresh two-pass reproduction only; not correctness certification.'}
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'record': bind(out), 'identical_units': len(compared), 'pdf': record['pdf'],
                  'tex_codes': [x['returncode'] for x in diagnostics['builds']],
                  'diagnostics': [x.get('diagnostics', []) for x in diagnostics['builds']]}))
