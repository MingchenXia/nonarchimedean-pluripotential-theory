"""Freeze completed102, actual107 proof/source work and active original105."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation107-publication-records'
P = R / 'root-checks/public-P16.5-round-102-final-reader'
C = R / 'campaigns/round-105/P16.5-original-full-big-divisor-reference-research'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


assert not D.exists()
receipt = json.loads((G / 'push-receipt-continuation106.json').read_text())
assert receipt['commit_sha'] == 'ccac501dfe57626dc9f9895a579299638984fd7e'
assert sha(G / 'upload-manifest-continuation106.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote',
                              'independent_native_git_tree_verified'])
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('input.json', 'input_sha256'), ('task-original.json', 'task_sha256'),
                  ('assignment-original.txt', 'assignment_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
assert f['model'] == 'gpt-6.1-sol' and f['reasoning'] == 'xhigh' and not f['original_closed']
canonical = R / 'root-checks/P16.5-round102-canonical-native-result-20261005.json'
assert json.loads(canonical.read_text())['candidate'] is False
binding = R / 'root-checks/P16.5-continuation107-primary-units/binding.json'
b = json.loads(binding.read_text())
assert sha(b['note']) == b['note_sha256'] and not b['independently_reviewed']
for u in b['units']:
    assert sha(u['path']) == u['sha256'] and sha(u['source']) == u['source_sha256']
for u in b['stacks_selected_bodies']:
    assert sha(u['selected_mathematical_body']) == u['body_sha256']
D.mkdir()
items = []
for atom, no, stem, session in [
    ('P16.5', 102, 'P16.5-original-nonample-finite-energy-equation-research', 18947),
    ('P21.3', 104, 'P21.3-original-arbitrary-current-exhaustion-research', 63959),
    ('P16.5', 105, 'P16.5-original-full-big-divisor-reference-research', 72229),
]:
    A = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(A / 'campaign.sqlite')],
                         cwd='/workspace/xean', capture_output=True, text=True, check=True)
    s = json.loads(out.stdout)
    assert s['calls']['admitted'] == 1
    p = D / f'{atom}-round{no}-native-status.json'
    p.write_text(out.stdout)
    items.append({'atom': atom, 'role': 'codex', 'round': no, 'directory': str(A),
                  'tool_session_id': session, 'observed_status': s['status'],
                  'status': str(p), 'status_sha256': sha(p), 'original_closed': False,
                  'hot_feedback_sent': False})
assert items[0]['observed_status'] == 'completed'
assert items[2]['observed_status'] in {'running', 'completed'}
now = datetime.now(timezone.utc).isoformat()
batch = {'recorded_utc': now, 'items': items,
         'active_items': [i for i in items if i['observed_status'] == 'running'],
         'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
         'focus': 'Two original targets: arbitrary-current104 and full-big retained-reference105. Completed102 candidate=false is preserved; no new original closure.'}
save(D / 'current-small-batch-observation.json', batch)
save(D / 'completed102-and-new107-observation.json', {
    'recorded_utc': now, 'canonical': str(canonical), 'canonical_sha256': sha(canonical),
    'canonical_notes': 4, 'candidate': False, 'original_closed': False,
    'public_reader': str(P), 'native_pdf_pages': 11,
    'native_pdf_sha256': sha(P / 'P16.5-paper.pdf'),
    'actual_full_argument_root_read': True, 'independent_endpoint_review_performed': False,
    'new_math': str(b['note']), 'new_math_sha256': b['note_sha256'],
    'new_math_independently_reviewed': False,
    'published_foundation': 'Version-pinned BJ2206.07183v2 TheoremA full printed proof and Corollaries2.1-2.3 read; entire retained numerical envelope/compactness foundation established, without a big energy conclusion.',
    'proof_work': 'Every actual big bundle has ample/effective actual data without Bertini or finite generation. Full retained-reference cone and original-carrier local products are proposed and supplied to unchanged original105 for reconstruction and scope assessment.',
    'editor': '/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_or_replaced': False,
})
shutil.copyfile(G / 'continuation106-publication-records/native-compiler-observation.json', D / 'native-compiler-observation.json')
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    d = json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms']) == 6
    if name == 'checklist-current.json':
        assert d['historical_reviewed_scoped_papers'] == 44
    d['updated_utc'] = now
    d['current_small_batch'] = batch
    d['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    d['github_pending_checkpoint'] = 'Checkpoint107: completed incomplete102 paper and actual canonical notes, full numerical envelope foundation, source-bound new full-big divisor-reference construction, unchanged original105 active. Six originals solved,36 open;44 reviewed scoped papers.'
    d['continuation107_unreviewed_P16_5'] = {'note': b['note'], 'sha256': b['note_sha256'],
                                           'binding': str(binding), 'original_closed': False,
                                           'native_reconstruction': str(C), 'hot_feedback_sent_to_active104': False}
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    shutil.copyfile(p, D / name)
shutil.copyfile(R / 'checklist-current.tsv', D / 'checklist-current.tsv')
files = []


def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {'.sqlite', '.jsonl'}
    assert not any(x in {'.git', '.codex', '.aws', '.env', 'auth.json', 'run.json'} for x in rel.parts)
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation107/' + str(rel),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})


for folder in [D, P, binding.parent, R / 'root-checks/P16.5-continuation107-stacks-primary']:
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            add(p)
for p in [Path(b['note']), canonical, R / 'root-checks/P16.5-round102-root-reading-binding-20261005.json',
          R / 'preserve_P16_5_round102_prepare_107_evidence_20261005.py',
          R / 'prepare_round105_P16_5_full_big_divisor_reference_research_20261005.py',
          R / 'fetch_P16_5_continuation107_stacks_primary_20261005.py',
          G / 'prepare_checkpoint_continuation107.py', G / 'push-receipt-continuation106.json']:
    add(p)
for name in ['input.json', 'task-original.json', 'assignment-original.txt', 'settings.json', 'freeze.json',
             'primary-literal-unit-bundle.json']:
    add(C / name)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
manifest = G / 'upload-manifest-continuation107.json'
save(manifest, {
    'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_atoms': 36,
    'historical_reviewed_scoped_papers': 44,
    'commit_message': 'Preserve nonample envelope foundation and reconstruct full big reference equations',
    'scope': 'Actual incomplete102 canonical four notes and11-page draft with all178 native artifact bindings independently verified; BJ addendum full numerical envelope proof; new no-Bertini big decomposition, fixed reference cone and genuine local-product work with exact primary units; original105 active alongside104. No full-original closure. Existing editor unchanged.',
})
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
                  'statuses': [(i['atom'], i['round'], i['observed_status']) for i in items]}, indent=2))
