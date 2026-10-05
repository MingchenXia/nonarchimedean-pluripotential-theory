"""Freeze completed104, scoped106 and the actual divisor-polar proof108."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation108-publication-records'
P = R / 'root-checks/public-P21.3-round-104-final-reader'
C = R / 'campaigns/round-106/P21.3-fixed-neighborhood-dual-criteria-scoped-review'
B = R / 'root-checks/P16.5-continuation108-primary-units'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


assert not D.exists()
receipt = json.loads((G / 'push-receipt-continuation107.json').read_text())
assert receipt['commit_sha'] == '8d44aebef757ea326e923e16c7af7141d091deef'
assert sha(G / 'upload-manifest-continuation107.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote',
                              'independent_native_git_tree_verified'])
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'),
                  ('task-original.json', 'original_task_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
canonical = R / 'root-checks/P21.3-round104-canonical-native-result-20261005.json'
v = json.loads(canonical.read_text())
assert v['candidate'] is False and len(v['notes']) == 2
b = json.loads((B / 'binding.json').read_text())
assert sha(b['note']) == b['note_sha256'] and not b['independent_review_performed']
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ('P21.3', 'codex', 104, 'P21.3-original-arbitrary-current-exhaustion-research', 63959, 'campaign.sqlite'),
    ('P16.5', 'codex', 105, 'P16.5-original-full-big-divisor-reference-research', 72229, 'campaign.sqlite'),
    ('P21.3', 'review', 106, 'P21.3-fixed-neighborhood-dual-criteria-scoped-review', 34814, 'review.sqlite'),
]:
    A = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(A / db)],
                         cwd='/workspace/xean', capture_output=True, text=True, check=True)
    s = json.loads(out.stdout)
    assert s['calls']['admitted'] == 1
    p = D / f'{atom}-round{no}-native-status.json'
    p.write_text(out.stdout)
    items.append({'atom': atom, 'role': role, 'round': no, 'directory': str(A),
                  'tool_session_id': session, 'observed_status': s['status'],
                  'status': str(p), 'status_sha256': sha(p),
                  'original_closed': False, 'hot_feedback_sent': False})
assert items[0]['observed_status'] == 'completed'
now = datetime.now(timezone.utc).isoformat()
batch = {'recorded_utc': now, 'items': items,
         'active_items': [i for i in items if i['observed_status'] == 'running'],
         'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
         'focus': 'Full-big original105 and scoped P21.3 proof audit106; original104 completed incomplete. New original-scope theorem or counterexample is not asserted.'}
save(D / 'current-small-batch-observation.json', batch)
save(D / 'actual104-and-root108-observation.json', {
    'recorded_utc': now, 'canonical': str(canonical), 'canonical_sha256': sha(canonical),
    'canonical_notes': 2, 'candidate': False, 'original_closed': False,
    'public_reader': str(P), 'native_pdf_pages': 9, 'native_pdf_sha256': sha(P / 'P21.3-paper.pdf'),
    'whole239_LF_new_proofs_root_read': True, 'independent_review': str(C),
    'new_math': b['note'], 'new_math_sha256': b['note_sha256'],
    'new_math_independently_reviewed': False,
    'new_math_result': 'The retained divisor reference is its own normalized constrained envelope; one explicit actual ample E1 polar test excludes the entire fixed divisor from every finite-relative-dual target.',
    'hot_feedback_to_active105_sent': False,
    'editor': '/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_or_replaced': False,
})
shutil.copyfile(G / 'continuation107-publication-records/native-compiler-observation.json', D / 'native-compiler-observation.json')
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    d = json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms']) == 6
    if name == 'checklist-current.json':
        assert d['historical_reviewed_scoped_papers'] == 44
    d['updated_utc'] = now
    d['current_small_batch'] = batch
    d['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    d['github_pending_checkpoint'] = 'Checkpoint108: incomplete104 actual two notes and9-page criterion paper, exact29 primary units and6 selected literature bindings, scoped106 frozen audit; new P16.5 constrained-envelope and polar-test proof with6 bindings. Six originals solved,36 open;44 reviewed scoped papers.'
    d['continuation108_unreviewed_P16_5'] = {'note': b['note'], 'sha256': b['note_sha256'],
                                           'binding': str(B / 'binding.json'), 'original_closed': False,
                                           'hot_feedback_to_active105_sent': False}
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
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation108/' + str(rel),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})


for folder in [D, P, B]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            add(p)
for p in [Path(b['note']), canonical, R / 'root-checks/P21.3-round104-root-reading-binding-20261005.json',
          R / 'preserve_round104_prepare_round106_P21_scoped_review_20261005.py',
          R / 'bind_root_P16_5_continuation108_primary_units_20261005.py',
          G / 'prepare_checkpoint_continuation108.py',
          G / 'record_verified_continuation107_live_fronts_20261005.py', G / 'push-receipt-continuation107.json']:
    add(p)
for name in ['task.json', 'task-original.json', 'argument.md', 'settings.json', 'freeze.json']:
    add(C / name)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
manifest = G / 'upload-manifest-continuation108.json'
save(manifest, {
    'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_atoms': 36,
    'historical_reviewed_scoped_papers': 44,
    'commit_message': 'Preserve ordinary-current dual criteria and prove divisor-reference polar exclusions',
    'scope': 'Actual incomplete104 canonical two notes and9-page paper, ordinary-test bipolar and compact-mass scalar criteria without density or a counterexample; source-bound scoped106 audit inputs; new unreviewed P16.5 constrained-reference envelope and direct E1 polar-test proof. No original closure. Current P16.4 editor unchanged.',
})
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
                  'statuses': [(i['atom'], i['round'], i['observed_status']) for i in items]}, indent=2))
