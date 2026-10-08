#!/usr/bin/env python3
"""Owned bounded artifact/support audit. Does not test mathematical truth."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

def bind(p):
    b = p.read_bytes()
    return {'path': str(p.relative_to(HERE)), 'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest()}

def main():
    incoming = json.loads((HERE / 'input.json').read_text())
    grant = json.loads((HERE / 'G331-qualified-grant.json').read_text())
    result = json.loads((HERE / 'native-notes.json').read_text())
    checks = {'original_task_unchanged': json.loads((HERE / 'original-task.json').read_text()) == incoming['task'],
              'grant_unchanged': grant == incoming['notes'][0],
              'candidate_false': result['candidate'] is False,
              'all_input_hashes_match': json.loads((HERE / 'input-bindings.json').read_text())['all_match']}
    seen = {'G331'}
    for n in result['notes']:
        checks[n['id'] + '_supports_ordered'] = set(n['support']) <= seen
        checks[n['id'] + '_full_body_matches'] = n['text'] == (HERE / (n['id'] + '.md')).read_text()
        checks[n['id'] + '_no_artifact_in_support'] = all(re.fullmatch(r'G331|n[1-9][0-9]*', x) for x in n['support'])
        seen.add(n['id'])
    build = json.loads((HERE / 'evidence' / 'build.json').read_text())
    checks['local_tex_build_pass'] = build['status'] == 'pass'
    checks['pdf_exists'] = (HERE / 'P12.3-paper.pdf').is_file()
    required = ['P12.3-paper.tex', 'argument.md', 'source-application-ledger.md', 'exact-scope.md',
                'whole-proof-coverage.md', 'original-scope-and-noncircularity-decision.md',
                'native-notes.json', 'input-bindings.json']
    checks['required_files_present'] = all((HERE / n).is_file() for n in required)
    files = []
    for p in sorted(HERE.rglob('*')):
        if not p.is_file() or p.name in {'input.json', 'own-bindings.json', 'final-audit.json'}:
            continue
        if p.suffix in {'.aux', '.log', '.out', '.toc'}:
            continue
        files.append(bind(p))
    own = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'records': files,
           'excluded': ['input.json (bound separately)', 'own-bindings.json (self)', 'evidence/final-audit.json (audit report)',
                        'TeX auxiliary files'],
           'meaning': 'Local artifact binding; no theorem verification.'}
    (HERE / 'own-bindings.json').write_text(json.dumps(own, indent=2) + '\n')
    report = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'checks': checks,
              'all_pass': all(checks.values()), 'owned_records': len(files),
              'mathematical_correctness_checked': False}
    (HERE / 'evidence' / 'final-audit.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'all_pass': report['all_pass'], 'checks': len(checks), 'owned_records': len(files),
                      'candidate': result['candidate']}))
    return 0 if report['all_pass'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
