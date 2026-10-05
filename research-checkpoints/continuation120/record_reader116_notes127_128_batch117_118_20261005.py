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
P = K / 'public-P16.3-round116-final-reader'
old = P / 'root-terminal-reader-observation.json'
shutil.copyfile(old, P / 'initial-root-terminal-reader-observation.json')
reader = json.loads(old.read_text())
assert reader['canonical_candidate'] is False and reader['original_P16_3_closed'] is False
assert sha(P / 'P16.3-paper.pdf') == reader['pdf_sha256']
reader['recorded_utc'] = now
reader['native_compilation'] = {'requested': True, 'exec_cell_id': '1368', 'status': 'Pending; no success or diagnostics returned.', 'success_asserted': False, 'editor_opened': False}
reader['visual_reading'] = {'actual_pages_root_visually_read': [1, 8, 16], 'whole_PDF_visually_read': False,
    'current_PDF_sha256': reader['pdf_sha256'], 'local_only_page_images': [binding(K / f'P16.3-round116-reader-layout-20261005/page-{n}.png') for n in [1, 8, 16]]}
old.write_text(json.dumps(reader, ensure_ascii=False, indent=2) + '\n')
save(P / 'root-reading-and-layout-binding-20261005.json', reader)

common = {'recorded_utc': now, 'whole_final_own_note_root_read': True, 'independently_reviewed': False,
    'new_original_closure': False, 'original_count_incremented': False, 'scoped_count_incremented': False,
    'whole_primary_work_or_recursive_background_read': False, 'whole_third_party_PDF_images_or_extended_responses_uploaded': False,
    'active_frozen117_118_modified_or_hot_feedback_sent': False}
note127 = K / 'P16.5-big-energy-source-and-zero-mass-obligations-20261005-continuation127.md'
source127 = R / 'shared-sources/DXZ-2302.02541v3-20261005'
save(K / 'P16.5-root-continuation127-source-and-obligation-reading-binding.json', dict(common,
    own_note=binding(note127), source='Darvas--Xia--Zhang arXiv2302.02541v3, published CMH100(2025), DOI10.4171/CMH/586',
    primary_PDF_local_only=binding(Path(str(source127) + '.pdf')), literal_extract_local_only=binding(Path(str(source127) + '.txt')),
    LF_coordinate_convention='Literal split on LF; form feeds retained inside lines.',
    selected_complete_statement_and_printed_proof_readings=[{'LF_range': [810, 960], 'units': 'Definition3.3 and Theorem3.4'},
        {'LF_range': [1160, 1330], 'units': 'Theorem3.14, Corollary3.16 and Section3.4/Theorem3.17'},
        {'LF_range': [1560, 1820], 'units': 'Lemmas4.12--4.13 and Theorem4.14; adjacent earlier context is not recursive verification.'}],
    exact_limits='Positive-volume complex projective/Kahler energy correspondence does not supply the original arbitrary-support Berkovich equation or a zero-volume formula. Own zero-mass uniqueness criterion and pullback-test identity are unreviewed elementary obligations.',
    supplied_to_active117=False))
C118 = R / 'campaigns/round-118/P15.3-original-general-P-type-and-numerical-carrier-research'
freeze118 = json.loads((C118 / 'freeze.json').read_text())
note128 = K / 'P15.3-dense-null-leaf-torus-and-all-flag-collapse-draft-20261005-continuation128.md'
assert sha(note128) == freeze118['unreviewed_root_proposal_sha256']
save(K / 'P15.3-root-continuation128-all-flag-draft-reading-binding.json', dict(common,
    own_note=binding(note128), native118_inline_proposal_sha256=freeze118['unreviewed_root_proposal_sha256'],
    native118_input_sha256=freeze118['input_sha256'],
    public_primary_source_bindings=freeze118['public_primary_sources'],
    LF_coordinate_convention='Literal split on LF; form feeds retained inside lines.',
    selected_complete_statement_and_printed_proof_readings=[
        {'saved_version': '2309.07584v3', 'LF_range': [227, 357], 'units': 'Basic definitions, Lemma2.1 proof and Lemma2.5 proof; nonbig extension is own checked argument, not a source claim.'},
        {'saved_version': '2309.07584v3', 'LF_range': [561, 715], 'units': 'Definition3.2, Lemma3.1, Propositions3.3--3.5 and nonbig perturbation definition.'},
        {'saved_version': '1210.5692v1', 'LF_range': [270, 300], 'units': 'Cao current Definition3 and distinct line-bundle Definition4; transcendental class is not called a line bundle.'}],
    exact_limits='Proposed dense-null-leaf rank1 torus obstruction concerns every usual unrescaled perturbative current-valuation limit on smooth modifications and flags. It neither rules out every richer carrier/construction nor closes P15.3. Native118 must independently test or refute it.',
    supplied_to_active118_at_initial_freeze=True))

receipt = json.loads((G / 'push-receipt-continuation119.json').read_text())
assert receipt['commit_sha'] == '74e2817bd0424ec2388e406cd345819ca8b11902'
assert sha(G / 'upload-manifest-continuation119.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
B = K / 'current-small-batch117-118-20261005'; assert not B.exists(); B.mkdir()
items = []
for no, atom, stem, session in [(117, 'P16.5', 'P16.5-original-general-reference-and-pseudoeffective-research', 91517),
                               (118, 'P15.3', 'P15.3-original-general-P-type-and-numerical-carrier-research', 43936)]:
    C = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')],
        cwd='/workspace/xean', capture_output=True, text=True, check=True)
    status = json.loads(out.stdout); assert status['calls']['admitted'] == 1
    p = B / f'{atom}-round{no}-public-native-status.json'; p.write_text(out.stdout)
    items.append({'round': no, 'atom': atom, 'directory': str(C), 'tool_session_id': session,
        'observed_status': status['status'], 'public_status': str(p), 'public_status_sha256': sha(p),
        'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False})
batch = {'recorded_utc': now, 'items': items, 'active_items': [i for i in items if i['observed_status'] == 'running'],
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
    'focus': 'Residual original P16.5 and full general original P15.3, two research tasks at a time. Completed116 partial and canonical114 INCONCLUSIVE preserved.'}
save(B / 'launch-and-public-status-record.json', batch)
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; a = json.loads(p.read_text()); assert len(a['fully_solved_original_atoms']) == 7
    a['updated_utc'] = now; a['current_small_batch'] = batch
    a['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    a['github_pending_checkpoint'] = 'Checkpoint120: completed partial P16.3 native116 with 16-page paper; active original P16.5 native117 and P15.3 native118; unreviewed own source/obstruction notes127/128. Counts remain7 solved originals,35 open,44 reviewed scoped papers.'
    a['prepared_full_original_research116'].update({'status': 'completed_partial_candidate_false', 'original_closed': False,
        'canonical_result': str(K / 'P16.3-round116-actual-native-author-result-20261005.json'), 'public_reader': str(P)})
    for item in items:
        a[f"prepared_full_original_research{item['round']}"] = {'directory': item['directory'],
            'freeze': str(Path(item['directory']) / 'freeze.json'), 'status': item['observed_status'], 'original_closed': False}
    if name == 'checklist-current.json':
        assert a['historical_reviewed_scoped_papers'] == 44
        a['active_atoms'] = [i['atom'] for i in batch['active_items']]
        t = next(t for t in a['targets'] if t['id'] == 'P16.3')
        t['current_focus'] = 'Native116 completed partial, candidate=false: all-field model-test strong density, conditional mixed-characteristic equations and exact finite-cover averaging counterexample; full original remains open.'
        t['current_remaining_gaps'] = json.loads((P / 'status.json').read_text())['concrete_gaps']
        next(t for t in a['targets'] if t['id'] == 'P15.3')['current_focus'] = 'Native118 general original research running; own all-flag dense-null-leaf torus obstruction is initially frozen unreviewed input, not an original solution.'
    else:
        a['next_work'] = 'Continue native117 original P16.5 and native118 original P15.3. Read canonical completions, prepare standalone papers and independently review exact original scope; retain partial and inconclusive judgments.'
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'reader_visual_pages': [1, 8, 16], 'native_compiler_success_asserted': False,
    'batch': [(i['round'], i['atom'], i['observed_status']) for i in items], 'counts': [7, 35, 44]}, indent=2))
