"""Record complete direct reads and reproduce builds in fresh copies only."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil
import subprocess

root = Path('/workspace/research')
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
units = json.loads((root / 'shared-sources/zero-volume-fibration-primary-read-20261004.json').read_text())['selected_units']
primary = root / 'shared-sources/BEGZ-0812.3674v2-20261004.txt'
lines = primary.read_bytes().split(b'\n')
campaigns = [
    ('P15.2', 'round-27/P15.2-relative-zero-volume-operator', '99f4b0eca3ab495d864a21d3b89c81e512ef456e94390bb6032ffe4b3ec718fe', 813),
    ('P15.1', 'round-28/P15.1-relative-zero-volume-energy', '4926fb7f422bd40412f1a3141672f86119273f3dd144a67505d082ff32e93b1d', 292),
]
for atom, relative, main_hash, lf_count in campaigns:
    campaign = root / 'campaigns' / relative
    native_run = json.loads((campaign / 'run.json').read_text())
    result = native_run['campaign']['result']
    workspace = Path(result['workspace'])
    review = Path(str(campaign) + '-review')
    freeze = json.loads((review / 'freeze.json').read_text())
    proof = workspace / (atom + '-argument.md')
    tex = workspace / (atom + '-partial.tex')
    status_path = workspace / 'status.json'
    status = json.loads(status_path.read_text())
    assert sha(proof) == main_hash == freeze['main_argument_sha256'] == freeze['declared_proof_sha256']
    assert len(proof.read_text().split('\n')) == lf_count
    assert sha(tex) == freeze['source_tex_sha256']
    assert sha(status_path) == freeze['source_status_sha256']
    assert sha(review / 'argument.md') == freeze['argument_sha256']
    assert proof.read_text() in (review / 'argument.md').read_text()
    assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
    assert status['id'] == atom and status['status'] == 'partial'
    assert status['proof_file'] == proof.name and result['candidate'] is False
    supplied = json.loads((campaign / 'input.json').read_text())
    received = json.loads((workspace / 'input.json').read_text())
    assert supplied == received
    assert supplied['notes'] == []
    seen = set()
    for note in result['notes']:
        assert set(note) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
        assert note['id'] not in seen
        assert set(note['support']).issubset(seen)
        seen.add(note['id'])
    source_checks = []
    for unit in units:
        body = b'\n'.join(lines[unit['first_lf_line'] - 1:unit['last_lf_line']])
        assert hashlib.sha256(body).hexdigest() == unit['sha256']
        assert body.decode() in supplied['assignment']
        assert body.decode() in (review / 'argument.md').read_text()
        if atom == 'P15.2':
            assert body.decode() in proof.read_text()
        source_checks.append({**unit, 'primary_raw_LF_rebound': True, 'full_direct_read': True})

    check = root / 'root-checks' / ('relative-zero-volume-' + atom + '-phase1')
    check.mkdir(exist_ok=False)
    canonical = {'kind': result['kind'], 'notes': result['notes'], 'candidate': result['candidate'], 'workspace': result['workspace']}
    canonical_path = check / 'canonical-result-record.json'
    canonical_path.write_text(json.dumps(canonical, ensure_ascii=False, indent=2) + '\n')
    record = {
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'atom': atom,
        'state': 'Full author argument and native notes directly read; independent review running; no theorem accepted.',
        'main_argument': str(proof), 'main_argument_sha256': main_hash,
        'all_main_LF_entries_directly_read': lf_count,
        'all_actual_canonical_notes_full_text_directly_read': [note['id'] for note in result['notes']],
        'canonical_result_record_sha256': sha(canonical_path),
        'local_note_file_is_not_assumed_canonical': True,
        'source_tex_sha256': sha(tex), 'status_sha256': sha(status_path),
        'review_argument_sha256': sha(review / 'argument.md'),
        'review_freeze_sha256': sha(review / 'freeze.json'),
        'review_binding_sha256': sha(review / 'source-artifact-binding.json'),
        'review_task_and_settings_fully_read': True,
        'original_decoded_inputs_equal': True,
        'primary_units': source_checks,
        'author_audits_and_build_source_scripts_fully_read': True,
        'standard_foundations': 'Precisely scoped bounded BT, empty-exceptional-set BEGZ IBP, nef products, Stokes and Sard. P15.1 optional descent additionally states analytic resolution; representative interpretation states the ddc lemma. These standard theorems are applied with checked hypotheses, not reproved monographs.',
        'scope': 'Supplied smooth compact Kahler fibration, bounded potentials, calibrated relative base objects only; all original atoms open.',
    }
    (check / 'complete-read-before-review.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    copy = check / 'reproduction'
    shutil.copytree(workspace, copy)
    commands = ['prepare_evidence.py', 'rerun.py'] if atom == 'P15.2' else ['extract_sources.py', 'rerun.py']
    executions = []
    for script in commands:
        executed = subprocess.run(['python', script], cwd=copy, capture_output=True, text=True)
        (check / (script + '.stdout.txt')).write_text(executed.stdout)
        (check / (script + '.stderr.txt')).write_text(executed.stderr)
        executions.append({'argv': ['python', script], 'cwd': str(copy), 'returncode': executed.returncode})
        assert executed.returncode == 0, executed.stderr
    assert sha(copy / proof.name) == sha(proof) == main_hash
    assert sha(copy / tex.name) == sha(tex)
    assert sha(proof) == freeze['main_argument_sha256']
    assert sha(tex) == freeze['source_tex_sha256']
    report = {
        'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'commands': executions, 'success': True,
        'frozen_worker_proof_and_tex_unchanged': True,
        'fresh_generated_tex_byte_identical_to_frozen_author_tex': True,
        'copied_reproduction_proof_sha256': sha(copy / proof.name),
        'copied_reproduction_tex_sha256': sha(copy / tex.name),
        'copied_pdf_sha256': sha(copy / (atom + '-partial.pdf')),
        'diagnostic_and_build_only_not_analytic_verification': True,
        'whole_copied_primary_PDF_text_local_only_not_for_GitHub': True,
    }
    (check / 'reproduction-result.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'atom': atom, 'directory': str(check), 'success': True,
                      'main_argument_sha256': main_hash, 'source_tex_sha256': sha(tex),
                      'review_pending': True}))
