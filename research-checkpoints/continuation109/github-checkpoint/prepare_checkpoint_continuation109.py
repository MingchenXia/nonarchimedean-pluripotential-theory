"""Freeze terminal105, actual106, contract repair and proper-nonprojective proof109."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation109-publication-records'
P = R / 'root-checks/public-P16.5-round-105-terminal-draft-reader'
B = R / 'root-checks/P16.2-continuation109-primary-units'
S = R / 'root-checks/P16.2-continuation109-stacks-primary'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


assert not D.exists()
receipt = json.loads((G / 'push-receipt-continuation108.json').read_text())
assert receipt['commit_sha'] == 'c7efec2cb60159cdd3ac8e698fd4648c853944e7'
assert sha(G / 'upload-manifest-continuation108.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote',
                              'independent_native_git_tree_verified'])
review = R / 'root-checks/P21.3-round106-actual-scoped-inconclusive-review-20261005.json'
v = json.loads(review.read_text())
assert v['verdict'] == 'INCONCLUSIVE' and len(v['premises']) == 7
obs = json.loads((P / 'root-terminal-artifact-observation.json').read_text())
assert not obs['native_canonical_result_returned'] and obs['author_file_claims_candidate']
assert len(obs['artifacts']) == 160
for u in obs['artifacts']:
    assert sha(P / u['path']) == u['sha256'] and (P / u['path']).stat().st_size == u['bytes']
b = json.loads((B / 'binding.json').read_text())
assert sha(b['note']) == b['note_sha256'] and not b['independent_review_performed']
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ('P16.5', 'codex', 105, 'P16.5-original-full-big-divisor-reference-research', 72229, 'campaign.sqlite'),
    ('P21.3', 'review', 106, 'P21.3-fixed-neighborhood-dual-criteria-scoped-review', 34814, 'review.sqlite'),
    ('P16.2', 'codex', 107, 'P16.2-original-proper-nonprojective-equation-research', 74889, 'campaign.sqlite'),
    ('P16.5', 'review', 108, 'P16.5-original-full-big-reference-independent-review', 93046, 'review.sqlite'),
    ('P16.2', 'codex', 109, 'P16.2-original-proper-nonprojective-input-repair-research', 25239, 'campaign.sqlite'),
]:
    A = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(A / db)],
                         cwd='/workspace/xean', capture_output=True, text=True, check=True)
    status = json.loads(out.stdout)
    assert status['calls']['admitted'] == 1
    p = D / f'{atom}-round{no}-native-status.json'
    p.write_text(out.stdout)
    items.append({'atom': atom, 'role': role, 'round': no, 'directory': str(A),
                  'tool_session_id': session, 'observed_status': status['status'],
                  'status': str(p), 'status_sha256': sha(p),
                  'original_closed': False, 'hot_feedback_sent': False})
assert [i['observed_status'] for i in items[:3]] == ['blocked', 'completed', 'cancelled']
now = datetime.now(timezone.utc).isoformat()
batch = {'recorded_utc': now, 'items': items, 'active_items': [i for i in items if i['observed_status'] == 'running'],
         'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
         'focus': 'Full-original P16.5 review108 and repaired full-original P16.2 research109. No new original closure.'}
save(D / 'current-small-batch-observation.json', batch)
save(D / 'actual105-106-and-original109-observation.json', {
    'recorded_utc': now, 'terminal105_reader': str(P), 'whole482_LF_paper_root_read': True,
    'terminal105_recording_failure': 'Missing mandatory CodexInput.notes; no native canonical result returned.',
    'file_local105_candidate_claim': True, 'native105_candidate_committed': False,
    'native105_pdf_pages': 14, 'native105_pdf_sha256': sha(P / 'P16.5-paper.pdf'),
    'review106': str(review), 'review106_sha256': sha(review), 'verdict106': 'INCONCLUSIVE',
    'review106_text_assesses_scoped_reductions_correct': True,
    'review106_machine_source_evidence_rejection_preserved': True,
    'scoped_count_incremented': False,
    'new_nonprojective_note': b['note'], 'new_note_sha256': b['note_sha256'],
    'new_note_independently_reviewed': False, 'native109_mandatory_notes_array': True,
    'cancelled107_private_outputs_read_or_used': False,
    'editor': '/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_or_replaced': False,
})
save(D / 'native-compiler-observation.json', {
    'observed_utc': now, 'pending_cells': [815, 831, 885],
    'last_waits_returned_still_running': True, 'native_success_asserted': False,
    'original_P13_2_local_two_pass_export': True,
    'original_P16_1_local_two_pass_export': True,
    'scoped_P21_3_round103_local_two_pass_export': True,
    'editor_modified_or_replaced': False,
})
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    d = json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms']) == 6
    if name == 'checklist-current.json':
        assert d['historical_reviewed_scoped_papers'] == 44
        d['active_atoms'] = ['P16.2', 'P16.5']
        for target in d['targets']:
            if target['id'] == 'P16.2':
                target['current_focus'] = 'Actual proper nonprojective polar-modification datum; new109 unreviewed full-domain proposal and native109 reconstruction.107 cancelled to repair missing mandatory notes input; exact mathematics unchanged. Original open.'
            if target['id'] == 'P16.5':
                target['current_focus'] = 'Terminal105 full-big prescribed-reference draft14 pages, file-local candidate true but result registration failed due caller missing notes. Full unchanged original independently audited108. No closure yet.'
            if target['id'] == 'P21.3':
                target['current_focus'] = 'Actual106 review INCONCLUSIVE from source-evidence validation despite text assessing104 scoped dual reductions correct. Original arbitrary-current antecedents remain unproved; no additional scoped acceptance counted.'
    d['updated_utc'] = now
    d['current_small_batch'] = batch
    d['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    d['github_pending_checkpoint'] = 'Checkpoint109: terminal105 full-big14-page draft and actual106 INCONCLUSIVE; new proper-nonprojective proof109 with exact sources, native108 full-original audit and109 corrected research. Six originals solved,36 open;44 reviewed scoped papers.'
    d['P21_3_actual_scoped106'] = {'review': str(review), 'sha256': sha(review), 'verdict': 'INCONCLUSIVE',
                                'original_closed': False, 'scoped_acceptance_asserted': False}
    d['P16_5_terminal105'] = {'reader': str(P), 'campaign_status': 'blocked', 'native_canonical_result_returned': False,
                            'paper_root_read': True, 'file_local_candidate_claim': True, 'original_closed': False}
    d['continuation109_unreviewed_P16_2'] = {'note': b['note'], 'sha256': b['note_sha256'],
                                          'binding': str(B / 'binding.json'), 'original_closed': False}
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
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation109/' + str(rel),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})


for folder in [D, P, B, S]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            add(p)
for p in [Path(b['note']), review,
          R / 'root-checks/P21.3-round106-root-reading-binding-20261005.json',
          R / 'root-checks/P16.5-round105-terminal-draft-reading-binding-20261005.json',
          R / 'preserve_review106_bind109_prepare_original107_20261005.py',
          R / 'preserve_blocked105_prepare_review108_and_repair109_20261005.py',
          R / 'fetch_P16_2_continuation109_stacks_primary_20261005.py',
          G / 'prepare_checkpoint_continuation109.py', G / 'push-receipt-continuation108.json',
          G / 'record_verified_continuation108_live_fronts_20261005.py']:
    add(p)
for i in items[2:]:
    A = Path(i['directory'])
    names = ['task-original.json', 'settings.json', 'freeze.json']
    names += ['task.json', 'argument.md'] if i['role'] == 'review' else ['assignment-original.txt', 'input.json', 'primary-literal-unit-bundle.json']
    for name in names:
        add(A / name)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
manifest = G / 'upload-manifest-continuation109.json'
save(manifest, {
    'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': receipt['fully_solved_original_atoms'], 'remaining_open_atoms': 36,
    'historical_reviewed_scoped_papers': 44,
    'commit_message': 'Preserve full big-reference draft and reconstruct proper nonprojective equations',
    'scope': 'Terminal105 full-big14-page unaccepted draft, explicit missing-notes failure and preserved evidence; actual106 scoped INCONCLUSIVE with exact seven premises and ten passage records; new proper-nonprojective polar-modification construction109 and literal sources; full-original review108 and corrected author109 frozen inputs. No new original or scoped acceptance. Existing editor unchanged.',
})
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
                  'statuses': [(i['atom'], i['round'], i['observed_status']) for i in items]}, indent=2))
