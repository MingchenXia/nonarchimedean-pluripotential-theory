from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
pending = G / 'upload-manifest-continuation43.json'
assert sha(pending) == '2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'
previous = G / 'local-packet-continuation51.json'
assert sha(previous) == 'c9b94cc4b939e754bc52784e78da49fb21cb7b719c08bb4ae289aff236749636'
launch = R / 'public-P16-equation-batch-launch-20261004.json'
assert sha(launch) == '907070b11ccb794fed3031efdbbfcf9c3f4376d3494cb1203992a79e5e6ad9f2'
out = G / 'local-packet-continuation52.json'
saved = G / 'continuation52-local-records'
assert not out.exists() and not saved.exists()
paper = R / 'root-checks/P02.4-reduced-curve-ordinary-paper-20261004'
build = json.loads((paper / 'build-layout-result.json').read_text())
assert build['native_compile_success'] and build['commands'][1]['returncode'] == 0
assert build['commands'][1]['warnings'] == []
assert sha(build['pdf']['path']) == '1be6d58f178cb9ebd8fc8d805ea12b8fa3983614be1f881983a855377ccd4821'
final_record = paper / 'root-final-read-and-visual.json'
assert not final_record.exists()
stamp = datetime.now(timezone.utc).isoformat()
final_record.write_text(json.dumps({'recorded_utc': stamp,
    'proof_markdown': str(R / 'root-checks/P02.4-reduced-curve-ordinary-smoothing-20261004.md'),
    'proof_markdown_sha256': sha(R / 'root-checks/P02.4-reduced-curve-ordinary-smoothing-20261004.md'),
    'entire_new_markdown_proof_root_read': True,
    'original_tex_full_read_LF': [1,508], 'layout_changes_exactly_reconstructed_and_read': True,
    'actual_visual_pages': [1,7], 'visual_result': 'Both displayed pages legible with no clipping; reference layout fixed. Whole-PDF visual inspection is not asserted.',
    'native_compile_success': True, 'native_open_result': 'Queued; actual editor opening not independently observed.',
    'final_local_pdf': build['pdf'], 'build_record_sha256': sha(paper / 'build-layout-result.json'),
    'imported_finite_tree_foundation_origin_explicit': True,
    'independent_mathematical_acceptance': False, 'original_catalogue_closure': False,
    'external_export_attempted': False, 'hot_feedback_sent': False}, indent=2) + '\n')
saved.mkdir()
statuses = []
batch = json.loads(launch.read_text())
for c in batch['campaigns']:
    d = Path(c['directory'])
    assert sha(d / 'input.json') == c['input_sha256']
    assert sha(d / 'settings.json') == c['settings_sha256']
    cmd = ['/workspace/xean/.xean/cloud/bun/bin/bun', '--no-install', '--no-env-file',
        '/workspace/xean/packages/cli/src/index.ts', 'status', str(d / 'campaign.sqlite')]
    run = subprocess.run(cmd, cwd='/workspace/xean', capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    status = json.loads(run.stdout)
    p = saved / (c['atom'] + '-native-status.json')
    p.write_text(json.dumps(status, indent=2) + '\n')
    statuses.append({'atom': c['atom'], 'round': c['round'], 'status': status['status'],
        'status_file': str(p), 'status_sha256': sha(p)})
active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
assert active['full_solutions'] == []
active['updated_utc'] = stamp
active['prepared_local_followup_packet_52'] = str(out)
active['new_local_ordinary_reduced_curve_paper'] = {
    'final_tex': str(paper / 'P02.4-reduced-curve-ordinary-paper-layout.tex'),
    'final_pdf': build['pdf'], 'root_final_record': str(final_record),
    'native_compile_success': True, 'independently_accepted': False,
    'imported_foundation': 'Exact local p063 finite-tree smoothing proposition; origin and full source hashes explicit.',
    'result_scope': 'Fixed-neighborhood ordinary smooth psh nets on reduced proper algebraic curves over algebraically closed complete nontrivially valued K; multibranch descent and all poles. Compact F_sigma criterion and countably dense-field sequences. Saturated projective bundles only.',
    'original_target_closed': False, 'submitted_to_provider_or_GitHub': False}
active['current_public_P16_equation_batch']['status_checkpoint'] = statuses
active['goal_state'] = 'ACTIVE. All 42 originals remain open. The current small native batch is P16.1/P16.4. A new root ordinary-smooth reduced-curve paper is fully read and compiled with native success and a clean exported seven-page PDF; its imported foundation is explicit and independent acceptance is pending. Four earlier rejected exports remain pending specific approval; none retried.'
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')
check_path = R / 'checklist-current.json'
check = json.loads(check_path.read_text())
assert len(check['targets']) == 42 and check['fully_solved_original_atoms'] == []
assert all(t['fully_solved'] is False and t['closure'] == 'open' for t in check['targets'])
check['updated_utc'] = stamp
for t in check['targets']:
    if t['id'] == 'P02.4':
        t.setdefault('local_unaccepted_drafts', []).append({
            'origin': 'Root local reduced-curve continuation with explicit imported finite-tree theorem.',
            'paper_tex': str(paper / 'P02.4-reduced-curve-ordinary-paper-layout.tex'),
            'paper_pdf': build['pdf']['path'], 'root_read': str(final_record),
            'native_compile_success': True, 'independently_accepted': False, 'original_target_closed': False})
check_path.write_text(json.dumps(check, ensure_ascii=False, indent=2) + '\n')
with (R / 'checklist-current.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['ID', 'Closure', 'Research', 'Reviewed_papers', 'Title'])
    for t in check['targets']:
        w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
files = [Path(__file__), R / 'prepare_public_P16_equation_batch_20261004.py',
    R / 'record_public_P16_equation_launch_20261004.py',
    R / 'public-P16-equation-batch-manifest-20261004.json', launch,
    R / 'shared-sources/cache_P16_public_primary_20261004.py',
    R / 'shared-sources/P16-public-primary-cache-20261004.json',
    R / 'root-checks/P02.4-reduced-curve-ordinary-smoothing-20261004.md',
    R / 'root-checks/prepare_reduced_curve_ordinary_paper_20261004.py',
    R / 'root-checks/build_reduced_curve_ordinary_paper_20261004.py',
    R / 'root-checks/prepare_reduced_curve_ordinary_layout_20261004.py',
    R / 'root-checks/build_reduced_curve_ordinary_layout_20261004.py']
cache = json.loads((R / 'shared-sources/P16-public-primary-cache-20261004.json').read_text())
for s in cache['sources']:
    files.extend(Path(s[k]) for k in ('abstract_html','pdf','literal_extract'))
for c in batch['campaigns']:
    d = Path(c['directory'])
    files.extend(d / name for name in ('input.json','settings.json','input-manifest.json'))
files.extend(p for p in paper.rglob('*') if p.is_file() and p.suffix in
    {'.tex','.json','.stdout','.stderr','.log','.pdf','.txt','.png'})
files.extend(saved / (c['atom'] + '-native-status.json') for c in batch['campaigns'])
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    destination = saved / name
    shutil.copyfile(R / name, destination)
    assert sha(destination) == sha(R / name)
    files.append(destination)
assert len(files) == len(set(files))
entries = []
for p in files:
    assert p.is_file() and not p.is_symlink(), str(p)
    entries.append({'local': str(p), 'path': 'research-checkpoints/continuation52/' + str(p.relative_to(R)),
        'bytes': p.stat().st_size, 'sha256': sha(p)})
packet = {'prepared_utc': stamp, 'state': 'LOCAL ONLY; no GitHub mutation or provider export.',
    'files': entries, 'file_count': len(entries), 'original_atoms': 42,
    'fully_solved_original_atoms': [], 'active_native_batch': ['P16.1','P16.4'],
    'native_status_snapshot': statuses, 'new_root_paper_independently_accepted': False,
    'new_root_paper_native_compile_success': True, 'new_root_paper_local_pdf_pages': 7,
    'previous_local_packet': str(previous), 'previous_local_packet_sha256': sha(previous),
    'last_verified_remote_commit': '604fea852c6a27d4cdc83d97f17393ea67087301',
    'pending_GitHub43_manifest_sha256': sha(pending), 'blocked_exports_not_resubmitted': True,
    'whole_uploaded_PDF_or_extract_included': False, 'book_source_proofs_copied_included': False,
    'imported_foundation_statement_and_origin_explicit_in_new_local_paper': True,
    'private_transcripts_sql_auth_runtime_included': False,
    'active_author_outputs_included': False,
    'verification_limit': 'New paper completely root read with explicit imported foundation; native compiler success and clean local export. No independent mathematical PASS or original catalogue closure.'}
out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(out), 'files': len(entries), 'sha256': sha(out),
    'native_status': statuses, 'uploaded': False, 'original_atoms_closed': 0}, indent=2))
