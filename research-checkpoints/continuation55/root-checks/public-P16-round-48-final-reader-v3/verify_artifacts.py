#!/usr/bin/env python3
"""Check deliverable structure and execution evidence; explicitly not a proof checker."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    input_bytes = (ROOT / 'input.json').read_bytes()
    data = json.loads(input_bytes)
    status = json.loads((ROOT / 'status.json').read_text())
    provenance = json.loads((ROOT / 'source-extracts/source-provenance.json').read_text())
    build = json.loads((ROOT / 'build/build-report.json').read_text())
    notes = json.loads((ROOT / 'notes.json').read_text())
    expected_keys = {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
    support_ok = True
    seen = set()
    for i, note in enumerate(notes['notes'], start=1):
        support_ok &= note['id'] == 'n' + str(i)
        support_ok &= set(note['support']).issubset(seen)
        support_ok &= all(key in note for key in ['id', 'summary', 'detailedSummary', 'text', 'support'])
        seen.add(note['id'])
    checks = {
        'input_original_byte_identical': (ROOT / 'input-original.json').read_bytes() == input_bytes,
        'assignment_decoded_exact': (ROOT / 'assignment-original.txt').read_text() == data['assignment'],
        'task_decoded_exact': json.loads((ROOT / 'task-original.json').read_text()) == data['task'],
        'source_count_exactly_ten': len(provenance['sources']) == 10,
        'all_supplied_source_hashes_match': all(all(s['hash_checks'].values()) for s in provenance['sources']),
        'all_pdf_reextractions_exit_zero': all(s['pdf_extraction_returncode'] == 0 for s in provenance['sources']),
        'all_literal_excerpt_hashes_match': all(digest(ROOT / e['file']) == e['sha256'] for s in provenance['sources'] for e in s['literal_published_extracts']),
        'four_actual_pdf_inspection_images': len(provenance['rendered_pdf_inspections']) == 4 and all((ROOT / i['file']).exists() and digest(ROOT / i['file']) == i['sha256'] for i in provenance['rendered_pdf_inspections']),
        'status_exact_keys': set(status) == expected_keys,
        'status_partial': status['status'] == 'partial',
        'canonical_notes_at_most_four': 1 <= len(notes['notes']) <= 4,
        'canonical_note_ids_and_support': support_ok,
        'candidate_false': notes['candidate'] is False,
        'final_builds_exactly_two_exit_zero': len(build['passes']) == 2 and all(p['returncode'] == 0 for p in build['passes']),
        'actual_build_streams_and_logs_retained': all((ROOT / p[k]).exists() for p in build['passes'] for k in ['stdout_file', 'stderr_file', 'log_file']),
        'final_tex_matches_build_hash': digest(ROOT / 'P16.6-paper.tex') == build['tex_source_sha256'],
        'final_argument_matches_build_hash': digest(ROOT / 'P16.6-argument.md') == build['argument_sha256'],
        'final_pdf_matches_pass_two': digest(ROOT / 'P16.6-paper.pdf') == build['passes'][1]['pdf_sha256'],
        'standalone_tex': r'\begin{document}' in (ROOT / 'P16.6-paper.tex').read_text() and r'\input{' not in (ROOT / 'P16.6-paper.tex').read_text(),
        'no_final_overfull_box': not any('Overfull' in w for w in build['passes'][1]['warnings']),
        'failed_build_diagnostics_preserved': all((ROOT / 'build/failed-missing-mathscr' / ('pass' + str(i)) / 'diagnostics.stdout').exists() for i in [1, 2]),
    }
    report = {'checks': checks, 'all_passed': all(checks.values()),
              'input_sha256': digest(ROOT / 'input.json'),
              'paper_pdf_sha256': digest(ROOT / 'P16.6-paper.pdf'),
              'final_tex_warnings': build['passes'][1]['warnings'],
              'evidence_kind': 'Finite artifact/identity observations only; no mathematical or exhaustive-domain validation.'}
    (ROOT / 'checks.json').write_text(json.dumps(report, indent=2) + '\n')
    manifest = []
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p.name not in ['artifact-manifest.json', 'verification-output.txt']:
            manifest.append({'file': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                             'sha256': digest(p)})
    (ROOT / 'artifact-manifest.json').write_text(json.dumps({'files': manifest, 'mathematical_verification': False}, indent=2) + '\n')
    for key, value in checks.items():
        print(key + ': ' + str(value))
    print('all checks passed:', report['all_passed'])
    print('Mathematical correctness was not checked by this program.')
    if not report['all_passed']:
        raise RuntimeError('An artifact check failed')

if __name__ == '__main__':
    main()
