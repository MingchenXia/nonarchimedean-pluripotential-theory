from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); G = R / 'github-checkpoint'; K = R / 'root-checks'
D = G / 'continuation119-publication-records'; P = R / 'deliverables/original-P16.2'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, v):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
previous = G / 'push-receipt-continuation118.json'
receipt = json.loads(previous.read_text())
assert receipt['commit_sha'] == '2eb53b52095157d9876068cdd4a5297aac863a11'
assert sha(G / 'upload-manifest-continuation118.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
closure = json.loads((P / 'P16.2-original-closure.json').read_text())
for key in ['source', 'pdf', 'argument', 'review']:
    assert sha(closure[key]) == closure[key + '_sha256']
review = json.loads((K / 'P16.5-round114-actual-full-original-review-20261005.json').read_text())
assert review['verdict'] == 'INCONCLUSIVE'
assert not D.exists(); D.mkdir()
items = []
for no, atom, stem, db, session in [
    (114, 'P16.5', 'P16.5-original-direct-foundation-and-local-operator-independent-review', 'review.sqlite', 12418),
    (116, 'P16.3', 'P16.3-original-full-residue-characteristic-reconstruction', 'work.sqlite', 39792)]:
    C = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / db)],
                         cwd='/workspace/xean', capture_output=True, text=True, check=True)
    status = json.loads(out.stdout); assert status['calls']['admitted'] == 1
    f = D / f'{atom}-round{no}-native-status.json'; f.write_text(out.stdout)
    items.append({'round': no, 'atom': atom, 'directory': str(C), 'tool_session_id': session,
                  'observed_status': status['status'], 'public_status': str(f), 'public_status_sha256': sha(f),
                  'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False})
now = datetime.now(timezone.utc).isoformat()
batch = {'recorded_utc': now, 'items': items,
         'active_items': [i for i in items if i['observed_status'] == 'running'],
         'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
         'focus': 'Original P16.5 canonical114 inconclusive with exact residual scope; original P16.3 research116 running. Next free slot seeks remaining original scope.'}
save(D / 'current-small-batch-observation.json', batch)
save(D / 'accepted-original-and-open-scope-observation.json', {
    'recorded_utc': now, 'fully_solved_original_atoms': receipt['fully_solved_original_atoms'],
    'remaining_open_originals': 35, 'historical_reviewed_scoped_papers': 44,
    'P16_2_current_edition_source_sha256': closure['source_sha256'],
    'P16_2_current_edition_PDF_sha256': closure['pdf_sha256'], 'pages': 28,
    'review114_verdict': review['verdict'], 'review114_operation_id': review['operationId'],
    'review114_original_count_increment': False,
    'new_notes125_126_independent_acceptance_claimed': False,
    'native_compiler_success_asserted': False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened': False,
    'third_party_papers_images_or_extended_web_responses_uploaded': False})
C116 = R / 'campaigns/round-116/P16.3-original-full-residue-characteristic-reconstruction'
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; a = json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms']) == 7
    a['updated_utc'] = now; a['current_small_batch'] = batch
    a['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    a['github_pending_checkpoint'] = 'Checkpoint119: P16.2 reviewed scope clarification; full-original P16.5 INCONCLUSIVE114; P16.3 native research116; own unreviewed observations125/126. Seven originals solved,35 open.'
    a['prepared_full_original_review114'].update({'status': 'completed_INCONCLUSIVE_original_open', 'original_closed': False,
        'canonical_review': str(K / 'P16.5-round114-actual-full-original-review-20261005.json')})
    a['prepared_full_original_research116'] = {'directory': str(C116), 'freeze': str(C116 / 'freeze.json'),
        'status': items[1]['observed_status'], 'original_closed': False}
    if name == 'checklist-current.json':
        assert a['historical_reviewed_scoped_papers'] == 44
        a['active_atoms'] = ['P16.3']
        t = next(t for t in a['targets'] if t['id'] == 'P16.5')
        t['current_focus'] = 'Canonical full-original114 INCONCLUSIVE. Full prescribed divisorial-reference big domain supported; general pseudoeffective and broader reference theories remain open.'
        t['current_remaining_gaps'] = json.loads((K / 'P16.5-round114-canonical-reading-and-open-scope-binding-20261005.json').read_text())['remaining_original_obligations']
    else:
        a['next_work'] = 'Continue native116 original P16.3 and launch one research task for remaining original P16.5 scope; publish actual results without overriding inconclusive judgments.'
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n'); shutil.copyfile(p, D / name)
shutil.copyfile(R / 'checklist-current.tsv', D / 'checklist-current.tsv')
files = []
def add(p, remote=None):
    p = Path(p); assert p.is_file() and not p.is_symlink(); rel = p.relative_to(R)
    assert not any(x in {'.git', '.codex', '.aws', '.env', 'auth.json', 'run.json', 'artifacts'} for x in rel.parts)
    assert p.suffix not in {'.sqlite', '.jsonl', '.png', '.aux', '.log'}
    if p.suffix == '.pdf': assert p == P / 'P16.2-paper.pdf'
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation119/' + str(rel),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file(): add(p)
for name in ['P16.2-core.md', 'P16.2-paper.tex', 'P16.2-paper.pdf', 'P16.2-original-closure.json',
             'publication-build-and-root-reading.json', 'publication-reviewed-scope-edition-build-20261005.json',
             'publication-reviewed-log-coordinate-scope-clarification.json', 'P16.2-core.reviewed-log-coordinate-scope.patch']:
    add(P / name)
for name in ['P16.2-original-reviewed-scope-edition-closure-20261005.json',
             'P16-continuous-local-products-and-signed-CLN-estimate-20261005-continuation125.md',
             'P16-root-continuation125-continuous-products-reading-binding.json',
             'P16.3-fixed-vertical-test-ideal-defect-and-envelope-estimate-20261005-continuation126.md',
             'P16.3-root-continuation126-vertical-defect-reading-binding.json',
             'P16.5-round114-actual-full-original-review-20261005.json',
             'P16.5-round114-canonical-reading-and-open-scope-binding-20261005.json']:
    add(K / name)
for name in ['settings.json', 'task.json', 'task-original.json', 'freeze.json']:
    add(C116 / name)
for p in [previous, R / 'record_verified118_20261005.py',
          R / 'record_original_P16_2_reviewed_scope_edition_20261005.py',
          R / 'clarify_original_P16_2_reviewed_log_coordinate_scope_20261005.py',
          R / 'record_root125_126_and_review114_20261005.py',
          R / 'prepare_original_P16_3_full_residue_characteristic_research116_20261005.py',
          G / 'prepare_checkpoint_continuation119.py']:
    add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({f['path'] for f in files}) == len(files)
manifest = G / 'upload-manifest-continuation119.json'
save(manifest, {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_atoms': 35,
    'historical_reviewed_scoped_papers': 44,
    'commit_message': 'Clarify reviewed P16.2 scope and record residual P16.5 judgment',
    'scope': 'Current P16.2 28-page edition states the already reviewed log-coordinate factorization. Original P16.5 remains open under canonical INCONCLUSIVE114. P16.3 native research116 continues; own source observations125/126 unreviewed. Seven originals solved,35 open,44 scoped; no count increment.'})
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
                  'statuses': [(i['round'], i['atom'], i['observed_status']) for i in items]}, indent=2))
