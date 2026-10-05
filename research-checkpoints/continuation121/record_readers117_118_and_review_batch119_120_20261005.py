from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'; G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def binding(p):
    p = Path(p)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}
def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
for no, atom, pages, cell in [(117, 'P16.5', [1, 10, 18], '1413'), (118, 'P15.3', [1, 12, 23], '1430')]:
    P = K / f'public-{atom}-round{no}-final-reader'
    old = P / 'root-terminal-reader-observation.json'
    shutil.copyfile(old, P / 'initial-root-terminal-reader-observation.json')
    reader = json.loads(old.read_text()); assert reader['canonical_candidate'] is False
    assert sha(P / f'{atom}-paper.pdf') == reader['pdf_sha256']
    reader['recorded_utc'] = now
    reader['state'] = 'Completed native partial author, candidate=false; new scoped independent review launched. No original acceptance.'
    reader['native_compilation'] = {'requested': True, 'exec_cell_id': cell,
        'status': 'Pending; no success or diagnostics returned.', 'success_asserted': False, 'editor_opened': False}
    reader['visual_reading'] = {'actual_pages_root_visually_read': pages, 'whole_PDF_visually_read': False,
        'current_PDF_sha256': reader['pdf_sha256'],
        'local_only_page_images': [binding(K / f'{atom}-round{no}-reader-layout-20261005/page-{n}.png') for n in pages]}
    old.write_text(json.dumps(reader, ensure_ascii=False, indent=2) + '\n')
    save(P / 'root-reading-and-layout-binding-20261005.json', reader)
receipt = json.loads((G / 'push-receipt-continuation120.json').read_text())
assert receipt['commit_sha'] == '3dec2b22580439036cf5c566223292a1b9c5b953'
assert sha(G / 'upload-manifest-continuation120.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
B = K / 'current-small-batch119-120-20261005'; assert not B.exists(); B.mkdir()
items = []
for no, atom, stem, session in [(119, 'P16.5', 'P16.5-bounded-reference-and-numerical-zero-independent-review', 83713),
                               (120, 'P15.3', 'P15.3-all-flag-collapse-and-exact-rescaling-independent-review', 81742)]:
    C = R / f'campaigns/round-{no}' / stem
    freeze = json.loads((C / 'freeze.json').read_text())
    for n, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
        assert sha(C / n) == freeze[key]
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'review.sqlite')],
        cwd='/workspace/xean', capture_output=True, text=True, check=True)
    status = json.loads(out.stdout); assert status['calls']['admitted'] == 1
    p = B / f'{atom}-round{no}-public-native-status.json'; p.write_text(out.stdout)
    items.append({'round': no, 'atom': atom, 'directory': str(C), 'tool_session_id': session,
        'observed_status': status['status'], 'public_status': str(p), 'public_status_sha256': sha(p),
        'scoped_review_only': True, 'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False})
batch = {'recorded_utc': now, 'items': items, 'active_items': [i for i in items if i['observed_status'] == 'running'],
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
    'focus': 'Two independent scoped checks of completed partial117/118 and new exact-body proposal129; general original tasks remain open.'}
save(B / 'launch-and-public-status-record.json', batch)
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; a = json.loads(p.read_text()); assert len(a['fully_solved_original_atoms']) == 7
    a['updated_utc'] = now; a['current_small_batch'] = batch
    a['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    a['github_pending_checkpoint'] = 'Checkpoint121: partial P16.5 native117 18-page paper, partial P15.3 native118 23-page paper, unreviewed own exact exceptional-flag/rescaling proposal129, active scoped reviews119/120. Counts remain7 originals solved,35 open,44 reviewed scoped papers.'
    for no, atom, stem in [(117, 'P16.5', 'P16.5-original-general-reference-and-pseudoeffective-research'),
                           (118, 'P15.3', 'P15.3-original-general-P-type-and-numerical-carrier-research')]:
        a[f'prepared_full_original_research{no}'].update({'status': 'completed_partial_candidate_false', 'original_closed': False,
            'canonical_result': str(K / f'{atom}-round{no}-actual-native-author-result-20261005.json'),
            'public_reader': str(K / f'public-{atom}-round{no}-final-reader')})
    for item in items:
        a[f"prepared_scoped_independent_review{item['round']}"] = item
    a['continuation129_unreviewed_exact_P15_3_body'] = {'note': str(K / 'P15.3-exact-exceptional-flag-trapezoid-and-rescaling-draft-20261005-continuation129.md'),
        'binding': str(K / 'P15.3-root-continuation129-exact-trapezoid-reading-binding.json'), 'reviewed': False, 'original_closed': False}
    if name == 'checklist-current.json':
        assert a['historical_reviewed_scoped_papers'] == 44
        a['active_atoms'] = [i['atom'] for i in batch['active_items']]
        for atom, no, text in [('P16.5', 117, 'Native117 partial: bounded genuine reference compatibility and all actual numerically trivial rational bundles; new scoped review119 active. General minimal-big and nonzero numerical pseudoeffective equations remain open.'),
                               ('P15.3', 118, 'Native118 partial: dense-null-leaf torus rigidity and all-fixed-model/flag unrescaled collapse; new scoped review120 also checks proposed exact exceptional-flag/rescaling body129. General arbitrary-P carrier construction remains open.')]:
            t = next(t for t in a['targets'] if t['id'] == atom)
            t['current_focus'] = text
            t['current_remaining_gaps'] = json.loads((K / f'public-{atom}-round{no}-final-reader/status.json').read_text())['concrete_gaps']
    else:
        a['next_work'] = 'Continue scoped independent119/120 checks, publish exact results without full-original promotion, and pursue remaining original general constructions in small batches.'
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
tsv = R / 'checklist-current.tsv'; rows = tsv.read_text().split('\n')
for i, row in enumerate(rows):
    fields = row.split('\t')
    if fields[0] == 'P15.3': fields[2] = 'partial118_all_flag_collapse_scoped120_review_running_original_open'; rows[i] = '\t'.join(fields)
    if fields[0] == 'P16.5': fields[2] = 'partial117_bounded_reference_and_numerical_zero_scoped119_review_running_original_open'; rows[i] = '\t'.join(fields)
tsv.write_text('\n'.join(rows))
print(json.dumps({'batch': [(i['round'], i['atom'], i['observed_status']) for i in items],
    'counts': [7, 35, 44], 'native_compiler_success_asserted': False}, indent=2))
