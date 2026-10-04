from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
JOBS = [(43, 'P02.3', 'P02.3-public-source-decreasing-weakly-smooth', 1758, '2026-10-04 14:42:42 UTC'),
        (44, 'P02.4', 'P02.4-public-source-decreasing-ordinary-smooth', 1739, '2026-10-04 14:31:16 UTC')]

def bind(p):
    data = Path(p).read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

for number, atom, slug, cell, request_time in JOBS:
    reader = R / 'root-checks' / f'public-smooth-round-{number}-final-reader'
    campaign = R / 'campaigns' / f'round-{number}' / slug
    result = json.loads((campaign / 'run.json').read_text())['campaign']['result']
    notes = json.loads((reader / 'actual-canonical-notes.json').read_text())
    assert result['notes'] == notes and result['candidate'] is False
    assert len(notes) == 4
    origin = Path(result['workspace'])
    for name in [f'{atom}-argument.md', f'{atom}-paper.tex']:
        assert (reader / name).read_bytes() == (origin / name).read_bytes()
    reproduction = json.loads((reader / 'reproduction-result.json').read_text())
    assert all(c['identical'] for c in reproduction['comparisons'])
    native_path = reader / 'native-request-unresponsive.json'
    out = reader / 'complete-root-read.json'
    assert not out.exists() and not native_path.exists()
    native = {'source': bind(reader / f'{atom}-paper.tex'), 'exec_cell': cell,
              'request_started_utc': request_time, 'recorded_utc': datetime.now(timezone.utc).isoformat(),
              'open_request_returned_result': False, 'handler_error_returned': False,
              'diagnostics_returned': False, 'dependent_compile_request_reached': False,
              'unresponsive_exec_cell_terminated': True, 'editor_close_requested': False,
              'source_preserved': True,
              'interpretation': 'Native open request unresponsive. No native compilation result is claimed. Local two-pass reproduction recorded separately.'}
    native_path.write_text(json.dumps(native, indent=2) + '\n')
    helpers = ['collect_sources.py', 'make_paper.py', 'build_paper.py', 'audit_artifacts.py'] if number == 43 else ['verify_sources.py', 'build_and_check.py']
    record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': number, 'atom': atom,
              'entire_final_argument_root_read': True, 'entire_standalone_tex_root_read': True,
              'all_actual_canonical_notes_all_fields_and_support_root_read': True,
              'source_provenance_versions_and_all_application_checks_root_read': True,
              'executed_author_helpers_fully_root_read_before_execution': [bind(reader / h) for h in helpers],
              'assemble_notes_helper_executed_by_root': False,
              'argument': bind(reader / f'{atom}-argument.md'), 'tex': bind(reader / f'{atom}-paper.tex'),
              'actual_canon': bind(reader / 'actual-canonical-notes.json'),
              'source_provenance': bind(reader / 'source-extracts/source-provenance.json'),
              'reproduction': bind(reader / 'reproduction-result.json'),
              'native_editor': bind(native_path), 'paper_pages': 10,
              'first_pdf_page_visually_read': True, 'whole_pdf_visually_read': False,
              'source_cache_entirely_read_this_turn': False,
              'proof_reconstruction_scope': 'All claimed scoped mathematical arguments read and reconstructed with exact published hypotheses; no original sharp classification follows.',
              'independent_mathematical_acceptance': False, 'original_target_closed': False,
              'scope_limit': 'Saturated proper-fiber domains do not cover arbitrary nonsaturated higher-dimensional psh germs.',
              'mathematical_concerns': (['The ambient positivity-cone shortcut needs the explicit cellwise reconstruction in the separately bound root clarification; independent reviewer must assess the frozen text.'] if number == 43 else []),
              'root_clarification': (bind(R / 'root-checks/P02.3-round43-current-positivity-clarification-20261004.md') if number == 43 else None),
              'interpretation': 'Read and reproduction evidence, not an independent PASS or original-task closure.'}
    out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'round': number, 'record': bind(out)}))

units = [('GJR-2111.05741.txt', 550, 705), ('GJR-2111.05741.txt', 2360, 2515),
         ('GJR-2111.05741.txt', 3800, 3918), ('GJR-2111.05741.txt', 4075, 4118),
         ('GR-2506.13548v2-20261004.txt', 560, 670), ('GR-2506.13548v2-20261004.txt', 1618, 1653),
         ('CD-1204.6277v2-20261004.txt', 950, 993), ('CD-1204.6277v2-20261004.txt', 994, 1025),
         ('CD-1204.6277v2-20261004.txt', 7337, 7356), ('Thuillier-tel-00010990v1.txt', 3587, 3722)]
source_out = R / 'shared-sources/P02-smooth-final-additional-primary-root-read-20261004.json'
assert not source_out.exists()
source_records = []
for name, first, last in units:
    p = R / 'shared-sources' / name
    data = b'\n'.join(p.read_bytes().split(b'\n')[first-1:last]) + b'\n'
    source_records.append({'source': bind(p), 'LF_first': first, 'LF_last': last,
                           'unit_bytes': len(data), 'unit_sha256': hashlib.sha256(data).hexdigest()})
source_out.write_text(json.dumps({'recorded_utc': datetime.now(timezone.utc).isoformat(), 'units': source_records,
    'read_scope': 'Exact LF units read in full this turn; claims only for complete named proofs inside those ranges. Other source foundations retain their earlier bindings.',
    'primary_pdf_visual_this_turn': ['Thuillier actual PDF pages 72 and 73'],
    'mathematical_acceptance': False}, indent=2) + '\n')
print(json.dumps({'source_read': bind(source_out)}))
