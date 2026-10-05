from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); G = R / 'github-checkpoint'; K = R / 'root-checks'
D = G / 'continuation120-publication-records'; P = K / 'public-P16.3-round116-final-reader'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
previous = G / 'push-receipt-continuation119.json'; receipt = json.loads(previous.read_text())
assert receipt['commit_sha'] == '74e2817bd0424ec2388e406cd345819ca8b11902'
assert sha(G / 'upload-manifest-continuation119.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
canonical = K / 'P16.3-round116-actual-native-author-result-20261005.json'
assert sha(canonical) == '11cc64118dbac74b7b84ac6c1db0a30e936583dfa1773fcf53f92675ee91449b'
assert json.loads(canonical.read_text())['candidate'] is False
reader = json.loads((P / 'root-reading-and-layout-binding-20261005.json').read_text())
assert reader['original_P16_3_closed'] is False
for name, key in [('P16.3-argument.md', 'argument_sha256'), ('P16.3-paper.tex', 'source_sha256'), ('P16.3-paper.pdf', 'pdf_sha256')]:
    assert sha(P / name) == reader[key]
assert not D.exists(); D.mkdir()
batch = json.loads((K / 'current-small-batch117-118-20261005/launch-and-public-status-record.json').read_text())
assert [i['round'] for i in batch['items']] == [117, 118]
for item in batch['items']:
    p = Path(item['public_status']); assert sha(p) == item['public_status_sha256']
    shutil.copyfile(p, D / p.name)
save(D / 'current-small-batch-observation.json', batch)
C116 = R / 'campaigns/round-116/P16.3-original-full-residue-characteristic-reconstruction'
out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C116 / 'work.sqlite')],
    cwd='/workspace/xean', capture_output=True, text=True, check=True)
status = json.loads(out.stdout); assert status['status'] == 'completed'
(D / 'P16.3-round116-public-native-status.json').write_text(out.stdout)
now = datetime.now(timezone.utc).isoformat()
save(D / 'accepted-original-and-open-scope-observation.json', {'recorded_utc': now,
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_originals': 35,
    'historical_reviewed_scoped_papers': 44, 'native116_candidate': False, 'native116_independent_acceptance': False,
    'native116_current_standalone_pages': 16, 'native116_local_build_passes': [0, 0],
    'native116_root_visually_read_pages': [1, 8, 16], 'native116_whole_PDF_visually_read': False,
    'native_compiler_success_asserted': False, 'notes127_128_independent_acceptance_claimed': False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened': False,
    'third_party_papers_images_or_extended_web_responses_uploaded': False,
    'active_frozen_inputs_modified_or_hot_feedback_sent': False})
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(p, remote=None):
    p = Path(p); assert p.is_file() and not p.is_symlink(); rel = p.relative_to(R)
    assert not any(x in {'.git', '.codex', '.aws', '.env', 'auth.json', 'run.json', 'artifacts', 'shared-sources'} for x in rel.parts)
    assert p.suffix not in {'.sqlite', '.jsonl', '.png', '.aux', '.log'}
    if p.suffix == '.pdf': assert p == P / 'P16.3-paper.pdf'
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation120/' + str(rel),
        'bytes': p.stat().st_size, 'sha256': sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file(): add(p)
for p in sorted(P.iterdir()):
    if p.is_file(): add(p)
add(canonical)
for name in ['P16.5-big-energy-source-and-zero-mass-obligations-20261005-continuation127.md',
             'P16.5-root-continuation127-source-and-obligation-reading-binding.json',
             'P15.3-dense-null-leaf-torus-and-all-flag-collapse-draft-20261005-continuation128.md',
             'P15.3-root-continuation128-all-flag-draft-reading-binding.json']:
    add(K / name)
for no, stem in [(117, 'P16.5-original-general-reference-and-pseudoeffective-research'),
                 (118, 'P15.3-original-general-P-type-and-numerical-carrier-research')]:
    C = R / f'campaigns/round-{no}' / stem
    freeze = json.loads((C / 'freeze.json').read_text())
    assert sha(C / 'input.json') == freeze['input_sha256']
    assert sha(C / 'task.json') == freeze['task_sha256']
    assert sha(C / 'settings.json') == freeze['settings_sha256']
    for name in ['settings.json', 'task.json', 'task-original.json', 'freeze.json']: add(C / name)
for p in [previous, R / 'record_verified119_and_current_batch116_117_20261005.py',
          R / 'record_reader116_notes127_128_batch117_118_20261005.py',
          R / 'prepare_P16_3_round116_public_reader_20261005.py',
          R / 'prepare_original_P16_5_general_reference_research117_20261005.py',
          R / 'prepare_original_P15_3_general_P_type_research118_20261005.py',
          G / 'prepare_checkpoint_continuation120.py']:
    add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({f['path'] for f in files}) == len(files)
manifest = G / 'upload-manifest-continuation120.json'
save(manifest, {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_atoms': 35,
    'historical_reviewed_scoped_papers': 44,
    'commit_message': 'Publish partial P16.3 reconstruction and continue general P16.5 and P15.3',
    'scope': 'Completed native116 remains partial with a 16-page standalone paper, explicit resolution assumptions and a finite-cover averaging counterexample. Native117 and118 pursue unchanged original P16.5 and P15.3. Own notes127/128 unreviewed. Seven originals solved,35 open,44 reviewed scoped; no count increment.'})
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
    'current_batch': [(i['round'], i['atom'], i['observed_status']) for i in batch['items']]}, indent=2))
