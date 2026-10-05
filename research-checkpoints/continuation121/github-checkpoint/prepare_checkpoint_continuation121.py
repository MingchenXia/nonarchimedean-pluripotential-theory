from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); G = R / 'github-checkpoint'; K = R / 'root-checks'
D = G / 'continuation121-publication-records'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
previous = G / 'push-receipt-continuation120.json'; receipt = json.loads(previous.read_text())
assert receipt['commit_sha'] == '3dec2b22580439036cf5c566223292a1b9c5b953'
assert sha(G / 'upload-manifest-continuation120.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
assert not D.exists(); D.mkdir()
batch = json.loads((K / 'current-small-batch119-120-20261005/launch-and-public-status-record.json').read_text())
assert [i['round'] for i in batch['items']] == [119, 120]
for item in batch['items']:
    p = Path(item['public_status']); assert sha(p) == item['public_status_sha256']; shutil.copyfile(p, D / p.name)
save(D / 'current-small-batch-observation.json', batch)
readers = []
for no, atom, stem, expected_canon in [(117, 'P16.5', 'P16.5-original-general-reference-and-pseudoeffective-research', '54da16e2ba6af237bc7082506ce7625b15ee80d3e06b26e258538501ff1ea072'),
                                       (118, 'P15.3', 'P15.3-original-general-P-type-and-numerical-carrier-research', 'dbd1cf542b41d8f3a958fcd7ea6581455db47b274402e3ebc1f97e9b8c058f19')]:
    P = K / f'public-{atom}-round{no}-final-reader'
    canonical = K / f'{atom}-round{no}-actual-native-author-result-20261005.json'
    assert sha(canonical) == expected_canon and json.loads(canonical.read_text())['candidate'] is False
    reader = json.loads((P / 'root-reading-and-layout-binding-20261005.json').read_text())
    for name, key in [(f'{atom}-argument.md', 'argument_sha256'), (f'{atom}-paper.tex', 'source_sha256'), (f'{atom}-paper.pdf', 'pdf_sha256')]: assert sha(P / name) == reader[key]
    assert reader[f"original_{atom.replace('.', '_')}_closed"] is False
    C = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')],
        cwd='/workspace/xean', capture_output=True, text=True, check=True)
    assert json.loads(out.stdout)['status'] == 'completed'
    (D / f'{atom}-round{no}-public-native-status.json').write_text(out.stdout)
    readers.append(P)
now = datetime.now(timezone.utc).isoformat()
save(D / 'accepted-original-and-open-scope-observation.json', {'recorded_utc': now,
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_originals': 35,
    'historical_reviewed_scoped_papers': 44, 'native117_118_candidates': [False, False],
    'native117_118_new_independent_acceptance': False, 'native117_118_standalone_pages': [18, 23],
    'native117_118_local_build_passes': [[0, 0], [0, 0]], 'native_compiler_success_asserted': False,
    'note129_independent_acceptance_claimed': False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened': False,
    'third_party_papers_images_or_extended_web_responses_uploaded': False,
    'active_frozen_inputs_modified_or_hot_feedback_sent': False})
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']: shutil.copyfile(R / name, D / name)
files = []
allowed_pdfs = {p / (p.name.split('public-')[1].split('-round')[0] + '-paper.pdf') for p in readers}
def add(p, remote=None):
    p = Path(p); assert p.is_file() and not p.is_symlink(); rel = p.relative_to(R)
    assert not any(x in {'.git', '.codex', '.aws', '.env', 'auth.json', 'run.json', 'artifacts', 'shared-sources'} for x in rel.parts)
    assert p.suffix not in {'.sqlite', '.jsonl', '.png', '.aux', '.log'}
    if p.suffix == '.pdf': assert p in allowed_pdfs
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation121/' + str(rel), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file(): add(p)
for P in readers:
    for p in sorted(P.iterdir()):
        if p.is_file(): add(p)
for name in ['P16.5-round117-actual-native-author-result-20261005.json', 'P15.3-round118-actual-native-author-result-20261005.json',
             'P15.3-exact-exceptional-flag-trapezoid-and-rescaling-draft-20261005-continuation129.md',
             'P15.3-root-continuation129-exact-trapezoid-reading-binding.json',
             'P15.3-surface-geometry-public-primary-download-binding-20261005.json']: add(K / name)
for no, stem in [(119, 'P16.5-bounded-reference-and-numerical-zero-independent-review'),
                 (120, 'P15.3-all-flag-collapse-and-exact-rescaling-independent-review')]:
    C = R / f'campaigns/round-{no}' / stem; freeze = json.loads((C / 'freeze.json').read_text())
    for n, key in [('argument.md', 'argument_sha256'), ('task.json', 'task_sha256'), ('settings.json', 'settings_sha256')]: assert sha(C / n) == freeze[key]
    for name in ['settings.json', 'task.json', 'task-original.json', 'freeze.json', 'mathematical-data-bindings.json']: add(C / name)
for p in [previous, R / 'record_verified120_20261005.py', R / 'prepare_reader117_and_scoped_review119_20261005.py',
          R / 'prepare_reader118_and_scoped_review120_20261005.py', R / 'record_readers117_118_and_review_batch119_120_20261005.py',
          R / 'download_P15_3_surface_geometry_primary_20261005.py', G / 'prepare_checkpoint_continuation121.py']: add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']: add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({f['path'] for f in files}) == len(files)
manifest = G / 'upload-manifest-continuation121.json'
save(manifest, {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_atoms': 35,
    'historical_reviewed_scoped_papers': 44,
    'commit_message': 'Publish bounded-reference and torus-collapse partial papers with independent checks',
    'scope': 'Native117 partial P16.5 18-page paper and native118 partial P15.3 23-page paper; new unreviewed exact exceptional-flag trapezoid/rescaling proposal129. Active scoped119/120 independent checks. Seven originals solved,35 open,44 reviewed scoped; no count increment.'})
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files), 'own_PDFs': len(allowed_pdfs)}, indent=2))
