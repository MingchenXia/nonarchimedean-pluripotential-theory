#!/usr/bin/env python3
"""Final integrity checks, without rerunning mathematical work or TeX."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def sha(b):
    return hashlib.sha256(b).hexdigest()

def main():
    inp = (ROOT / 'input.json').read_bytes()
    assert inp == (ROOT / 'input-original.json').read_bytes()
    status = json.loads((ROOT / 'status.json').read_text())
    assert list(status) == ['id', 'status', 'exact_result', 'proof_file', 'concrete_gaps']
    assert status['status'] == 'incomplete'
    notes = json.loads((ROOT / 'notes.json').read_text())
    assert notes['candidate'] is False and 1 <= len(notes['notes']) <= 4
    seen = set()
    for number, note in enumerate(notes['notes'], start=1):
        assert set(note) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
        assert note['id'] == f'n{number}'
        assert set(note['support']) <= seen
        seen.add(note['id'])
    report = json.loads((ROOT / 'checks/check-report.json').read_text())
    assert report['all_checks_passed'] is True
    assert len(report['tex_runs']) == 2
    assert all(run['returncode'] == 0 for run in report['tex_runs'])
    for run in report['tex_runs']:
        assert (ROOT / run['stdout']).exists()
        assert (ROOT / run['stderr']).exists()
        log = (ROOT / run['tex_log']).read_bytes()
        assert b'Output written on P13.2-paper.pdf' in log
        assert b'Undefined control sequence' not in log
        assert b'undefined references' not in log
    source = json.loads((ROOT / 'source-extracts/source-provenance.json').read_text())
    assert len(source['sources']) == 4
    assert all(s['hash_matches_supplied'] for s in source['sources'])
    result = {'input_sha256': sha(inp), 'canonical_notes': len(notes['notes']),
              'earlier_local_support_only': True, 'status': status['status'],
              'source_versions': [s['saved_version'] for s in source['sources']],
              'final_tex_returncodes': [r['returncode'] for r in report['tex_runs']],
              'mathematics_verified': False}
    (ROOT / 'checks/final-integrity.json').write_text(json.dumps(result, indent=2) + '\n')
    manifest = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())}
                for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name != 'artifact-manifest.json']
    (ROOT / 'artifact-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
