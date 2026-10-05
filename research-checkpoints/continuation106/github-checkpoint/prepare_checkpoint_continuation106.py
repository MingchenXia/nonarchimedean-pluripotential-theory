"""Freeze reviewed scoped103 publication, active104 and the unreviewed106 proof."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation106-publication-records'
P = R / 'deliverables/scoped-P21.3-round103'
N = R / 'root-checks/P16.5-fixed-effective-divisor-relative-equations-20261005-continuation106.md'
B = R / 'root-checks/P16.5-continuation106-primary-units'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, d):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


assert not D.exists()
receipt = json.loads((G / 'push-receipt-continuation105.json').read_text())
assert receipt['commit_sha'] == '93c942d6623a547a418549539363954ea3a944f2'
assert sha(G / 'upload-manifest-continuation105.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote',
                              'independent_native_git_tree_verified'])
publication = json.loads((P / 'scoped-publication.json').read_text())
assert publication['scoped_verdict'] == 'PASS' and not publication['original_closed']
assert sha(publication['review']) == publication['review_sha256']
assert sha(publication['source']) == publication['source_sha256']
assert sha(publication['pdf']) == publication['pdf_sha256']
bound = json.loads((B / 'binding.json').read_text())
assert sha(N) == bound['construction_sha256'] and not bound['original_P16_5_closed']
for u in bound['units']:
    assert sha(u['path']) == u['sha256']
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ('P16.5', 'codex', 102, 'P16.5-original-nonample-finite-energy-equation-research', 18947, 'campaign.sqlite'),
    ('P21.3', 'codex', 104, 'P21.3-original-arbitrary-current-exhaustion-research', 63959, 'campaign.sqlite'),
    ('P21.3', 'review', 103, 'P21.3-bounded-generated-mixed-symmetry-scoped-review', 22880, 'review.sqlite'),
]:
    C = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / db)],
                         cwd='/workspace/xean', capture_output=True, text=True, check=True)
    s = json.loads(out.stdout)
    assert s['calls']['admitted'] == 1
    p = D / f'{atom}-round{no}-native-status.json'
    p.write_text(out.stdout)
    items.append({'atom': atom, 'role': role, 'round': no, 'directory': str(C),
                  'tool_session_id': session, 'observed_status': s['status'],
                  'status': str(p), 'status_sha256': sha(p),
                  'original_closed': False, 'hot_feedback_sent': False})
assert items[2]['observed_status'] == 'completed'
now = datetime.now(timezone.utc).isoformat()
batch = {'recorded_utc': now, 'items': items, 'active_items': [i for i in items if i['observed_status'] == 'running'],
         'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
         'focus': 'Two original targets: nonample equation102 and arbitrary-current104. Scoped103 passed; P21.3 remains open.'}
save(D / 'current-small-batch-observation.json', batch)
save(D / 'native-compiler-observation.json', {
    'observed_utc': now, 'native_compilation_success_asserted': False,
    'pending_calls': [
        {'cell_id': '815', 'path': str(R / 'deliverables/original-P13.2/P13.2-paper.tex')},
        {'cell_id': '831', 'path': str(R / 'deliverables/original-P16.1/P16.1-paper.tex')},
        {'cell_id': '885', 'path': str(P / 'P21.3-paper.tex')},
    ],
    'local_exports': 'Each exact source has two successful local TeX export passes; first and last exported pages were visually read.',
    'current_editor': str(R / 'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex'),
    'current_editor_replaced_or_modified': False,
})
save(D / 'P21.3-publication-layout-observation.json', {
    'pdf': str(P / 'P21.3-paper.pdf'), 'sha256': sha(P / 'P21.3-paper.pdf'),
    'pages': 11, 'bytes': (P / 'P21.3-paper.pdf').stat().st_size,
    'first_and_last_pages_root_visually_read': True,
    'source': str(P / 'P21.3-paper.tex'), 'source_sha256': sha(P / 'P21.3-paper.tex'),
    'closing_execution_paragraph_scope': 'The closing author-execution and reproduction statements describe the preserved author100 workspace, not the later actual independent103 review. The current deliverable is a publication copy; original reproduction files are in public-P21.3-round-100-final-reader.',
})
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    d = json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms']) == 6
    if name == 'checklist-current.json':
        assert d['historical_reviewed_scoped_papers'] == 44
    d['updated_utc'] = now
    d['current_small_batch'] = batch
    d['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    d['github_pending_checkpoint'] = 'Checkpoint106: scoped103 PASS and11-page partial paper, original104 running, source-bound unreviewed P16.5 divisor-reference construction. Six originals solved,36 open.'
    d['continuation106_unreviewed_P16_5'] = {'note': str(N), 'sha256': sha(N), 'binding': str(B / 'binding.json'),
                                           'original_closed': False, 'hot_feedback_sent': False}
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
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation106/' + str(rel),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})


for folder in [D, P, B]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            add(p)
for p in [N, R / 'root-checks/P21.3-round103-actual-scoped-review-20261005.json',
          R / 'root-checks/P21.3-round103-canonical-reading-binding-20261005.json',
          R / 'publish_scoped_P21_3_review103_prepare_original104_20261005.py',
          R / 'bind_root_P16_5_continuation106_primary_units_20261005.py',
          G / 'prepare_checkpoint_continuation106.py', G / 'push-receipt-continuation105.json']:
    add(p)
C = R / 'campaigns/round-104/P21.3-original-arbitrary-current-exhaustion-research'
for name in ['input.json', 'task-original.json', 'assignment-original.txt', 'settings.json', 'freeze.json']:
    add(C / name)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
manifest = G / 'upload-manifest-continuation106.json'
save(manifest, {
    'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_atoms': 36,
    'historical_reviewed_scoped_papers': 44,
    'commit_message': 'Publish reviewed generated-current calculus and continue both original targets',
    'scope': 'Actual scoped103 PASS with exact9 premises and44 HTTP bindings, clarified11-page paper, original104 research inputs, unreviewed P16.5 full fixed-divisor cone proof and13 primary units. No full-original closure; actual six originals retained. Compiler pending distinct from local exports; editor unchanged.',
})
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
                  'statuses': [(i['atom'], i['round'], i['observed_status']) for i in items]}, indent=2))
