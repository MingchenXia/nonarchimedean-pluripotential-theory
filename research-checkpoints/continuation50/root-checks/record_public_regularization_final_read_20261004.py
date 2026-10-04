from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')

def bind(p):
    data = p.read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

source_units = [
    ('GJR-2111.05741.txt', 2152, 2283, '6.13--6.19: germ reductions, complete 6.14 proof, 6.15 statement, residue definition, complete 6.17 and 6.18 proofs, 6.19 functoriality.'),
    ('Thuillier-tel-00010990v1.txt', 5379, 5470, '3.4.6 complete statement and proof, 3.4.7, polar discussion, 3.4.10 complete statement and proof.'),
    ('GR-2506.13548v2-20261004.txt', 499, 530, 'Curve convention and complete 3.5 property statement; subsequent remarks only. Boundary-spike application checks 3.5(3).'),
    ('GR-2506.13548v2-20261004.txt', 1100, 1125, 'Complete classical definition and 4.1.2 equivalence; only start of 4.2 statement.'),
    ('Thuillier-tel-00010990v1.txt', 2420, 2515, 'Earlier root read: 2.2.15 complete proof and retraction construction prefix; no full later proof claim.'),
    ('GJR-2111.05741.txt', 1990, 2065, 'Earlier root read: 6.4 tail, 6.5 and 6.6 complete, 6.7, 6.8 statement and initial proof only.'),
    ('Thuillier-tel-00010990v1.txt', 10020, 10130, 'Earlier root read: 5.1.4 full statement, 5.1.5 statement and initial proof including algebraically closed omitted open-disc components.'),
    ('Thuillier-tel-00010990v1.txt', 2310, 2421, 'Earlier root read: 2.2.10 statement, complete 2.2.11 and 2.2.12 proofs, 2.2.13--2.2.14.'),
    ('GJR-2111.05741.txt', 2340, 2415, 'Earlier root read: 7.3 tail, complete 7.4--7.5 proofs, 7.6 statement and proof prefix only.'),
    ('Thuillier-tel-00010990v1.txt', 3858, 3985, 'Earlier root read: 3.1.11 through 3.1.15, complete 3.1.12--3.1.14 proofs; 3.1.16 proof prefix only.'),
]
units = []
for name, first, last, scope in source_units:
    source = R / 'shared-sources' / name
    data = '\n'.join(source.read_text().split('\n')[first-1:last]).encode()
    units.append({'source': bind(source), 'LF_first': first, 'LF_last': last,
                  'unit_bytes': len(data), 'unit_sha256': hashlib.sha256(data).hexdigest(),
                  'root_read_scope': scope})
source_record = R / 'shared-sources' / 'P02-regularization-additional-primary-root-read-20261004.json'
assert not source_record.exists()
source_record.write_text(json.dumps({'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'units': units, 'published_foundations_not_reproved': True,
    'mathematical_acceptance': False, 'original_target_closed': False}, indent=2) + '\n')

for n, atom in [(41, 'P02.1'), (42, 'P02.2')]:
    p = R / 'root-checks' / f'public-regularization-round-{n}-final-reader'
    preliminary = R / 'root-checks' / f'public-regularization-round-{n}-preliminary-reader'
    result = json.loads((p / 'reproduction-result.json').read_text())
    assert result['all_script_steps_succeeded']
    assert result['core_tex_provenance_and_literal_units_identical']
    native = {
        'path': str(p / f'{atom}-paper.tex'),
        'open_in_codex_requested': True,
        'exec_cell_id': '1676' if n == 41 else '1678',
        'request_clock_output': None if n == 41 else '2026-10-04 13:43:50 UTC',
        'open_result_received': False, 'compile_latex_document_reached': False,
        'error_or_handler_diagnostics_received': False,
        'unresponsive_orchestration_cell_terminated': True,
        'source_preserved': True, 'editor_close_requested': False,
        'native_compilation_verified': False,
        'local_compilation': 'Two successful fresh pdfLaTeX passes; separate evidence.',
    }
    native_path = p / 'native-request-unresponsive.json'
    assert not native_path.exists()
    native_path.write_text(json.dumps(native, indent=2) + '\n')
    scripts = (['retain_input.py', 'retain_sources.py', 'rerun.py', 'graph_diagnostic.py', 'verify_artifacts.py']
               if n == 41 else ['collect_sources.py', 'finite_diagnostics.py', 'build_documents.py', 'verify_artifacts.py'])
    files = [f'{atom}-argument.md', f'{atom}-paper.tex', 'actual-canonical-notes.json',
             'status.json', 'source-extracts/source-provenance.json', 'campaign-input.json',
             'campaign-settings.json', 'reproduction-result.json'] + scripts
    report = {
        'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': n, 'atom': atom,
        'bindings': [bind(p / name) for name in files],
        'preliminary_argument_binding': bind(preliminary / f'{atom}-argument.md'),
        'entire_preliminary_argument_root_read': True,
        'entire_final_argument_diff_root_read': True,
        'final_core_read_method': 'Complete preliminary proof plus whole final diff; R42 core unchanged.',
        'entire_standalone_tex_root_read': True,
        'all_actual_canonical_notes_all_fields_and_support_root_read': True,
        'truncated_aggregate_reads_repaired_by_smaller_untruncated_reads': True,
        'root_executed_generated_helpers_fully_read': scripts,
        'canonical_packagers_not_executed_by_root': ['assemble_notes.py'] if n == 41 else [],
        'source_provenance_administration_and_application_checks_root_read': True,
        'all_embedded_literal_primary_pages_claimed_fully_read': False,
        'primary_additional_read_record': bind(source_record),
        'full_proof_reconstruction_observation':
            'No substantive gap identified within the expressly stated sufficient scope. '
            'The boundary obstruction in R42 is a sequence obstruction only. '
            'Positive higher-dimensional scope requires entire proper fibres or saturated domains.',
        'reproduction': result,
        'first_pdf_page_visually_inspected': True,
        'first_page_observation': 'Legible text and formulas; no visible clipping. Whole-PDF visual inspection not claimed.',
        'native_editor_attempt': native,
        'independent_review_submitted': False,
        'independent_acceptance': False, 'original_target_closed': False,
        'execution_not_mathematical_certificate': True,
    }
    target = p / 'complete-root-read.json'
    assert not target.exists()
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'round': n, 'root_read': bind(target), 'source_read': bind(source_record)}))
