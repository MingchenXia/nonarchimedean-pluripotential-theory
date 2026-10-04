"""Freeze the third original paper and the next two-item research/review batch."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation58-publication-records'
D.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
receipt = json.loads((G / 'push-receipt-continuation57.json').read_text())
assert receipt['commit_sha'] == '3a00996040461eb5181b28587d65101e68e14a1e'
assert receipt['all_file_blob_bindings_verified_remote']
items = []
for atom, round_number, stem, db, session, role in [
    ('P15.3', 50, 'P15.3-public-source-zero-volume-P-sensitive-bodies', 'campaign.sqlite', 19544, 'author'),
    ('P16.3', 49, 'P16.3-public-source-positive-residue-geometric-inputs-review', 'review.sqlite', 90333, 'correctness review'),
]:
    directory = R / 'campaigns' / ('round-' + str(round_number)) / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(directory / db)],
                         cwd='/workspace/xean', capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    p = D / (atom + '-native-status.json')
    p.write_text(out.stdout)
    items.append({'atom': atom, 'role': role, 'round': round_number, 'directory': str(directory),
                  'tool_session_id': session, 'observed_status': json.loads(out.stdout)['status'],
                  'status': str(p), 'status_sha256': sha(p),
                  'input_or_argument_sha256': sha(directory / ('input.json' if role == 'author' else 'argument.md')),
                  'settings_sha256': sha(directory / 'settings.json'), 'accepted': False})
launch = D / 'current-small-batch-launch-and-observation.json'
launch.write_text(json.dumps({'observed_utc': now, 'route': 'Xean native Codex',
                             'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'items': items,
                             'hot_feedback_sent': False, 'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6']}, indent=2) + '\n')
a = json.loads((R / 'active-work.json').read_text())
a['updated_utc'] = now
a['selected_atoms'] = ['P15.3', 'P16.3']
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint58: final original P15.1 paper/review, exact primary checks, P16.3 surface proof and independent review, P15.3 public-source author, current 3/42 closure ledger.'
a['current_small_batch'] = {'recorded_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
                          'reasoning': 'xhigh', 'active_items': items,
                          'completed_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'hot_feedback_sent': False}
a['goal_state'] = 'ACTIVE: 3/42 unchanged original atoms solved; 39 remain open. Continue in small batches. No stop or all-solved declaration.'
a['next_work'] = 'Read the complete P16.3 actual independent verdict when published; assess the P15.3 author proof against the unchanged original, then proceed to the next small batch. Publish completed research checkpoints regularly.'
a['native_publication_compile_addenda'] = [str(R / ('root-checks/' + atom + '-native-publication-compile-unverified-20261004.json')) for atom in ['P15.1', 'P16.6']]
a['P16.3_round49_completed_partial'] = {'reader': str(R / 'root-checks/public-P16-round-49-final-reader'),
    'root_read_sha256': sha(R / 'root-checks/public-P16-round-49-final-reader/complete-root-read.json'),
    'state': 'Whole argument and all three actual canonical notes root read; 33 literal primary bindings and two TeX passes reproduced. Surface theorem correctness review running; original still open.',
    'original_atom_solved': False, 'candidate': False, 'review_session_id': 90333}
(R / 'active-work.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
c['updated_utc'] = now
c['active_atoms'] = ['P15.3', 'P16.3']
c['current_small_batch_launch'] = str(launch)
c['current_small_batch_launch_sha256'] = sha(launch)
for t in c['targets']:
    if t['id'] == 'P15.3':
        t['research_status'] = 'native_public_primary_zero_volume_P_sensitive_author_active'
        t['current_focus'] = 'Round50 unchanged original and four actual public primary sources; complete P-sensitive transcendental numerical-dimension construction sought. No new proof accepted.'
        t['current_unreviewed_campaign_round50'] = items[0]
    if t['id'] == 'P16.3':
        t['research_status'] = 'geometric_equal_characteristic_surface_correctness_review_active_original_open'
        t['current_focus'] = 'Round49 general surface arbitrary-support E1 draft: whole proof/root reproduction done; independent correctness review running. Mixed characteristic, unproved higher-dimensional resolution and unrestricted geometric origin remain original gaps.'
        t['current_unreviewed_campaign_round49'] = a['P16.3_round49_completed_partial']
        t['current_review_round49'] = items[1]
(R / 'checklist-current.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
with (R / 'checklist-current.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['ID', 'Closure', 'Research', 'Reviewed_papers', 'Title'])
    for t in c['targets']:
        w.writerow([t['id'], t['closure'], t['research_status'], len(t['reviewed_papers']), t['title']])
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file()
    remote = remote or 'research-checkpoints/continuation58/' + str(p.relative_to(R))
    files.append({'local': str(p), 'path': remote, 'bytes': p.stat().st_size, 'sha256': sha(p)})
def add_directory(directory, manuscript=False):
    for p in sorted(directory.rglob('*')):
        if p.is_file() and p.suffix in {'.tex', '.pdf', '.json', '.md', '.log', '.txt', '.png', '.py'}:
            add(p, 'manuscript/editorial/xean_research_20261003/' + str(p.relative_to(R)) if manuscript else None)
add_directory(R / 'deliverables/original-P15.1', True)
for directory in [D, G / 'continuation58-local-records',
                  R / 'root-checks/public-P16-round-49-final-reader',
                  R / 'root-checks/P16.3-geometric-inputs-source-read-20261004',
                  R / 'root-checks/P15.3-public-primary-read-20261004']:
    add_directory(directory)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
for atom in ['P15.1', 'P16.6']:
    add(R / ('root-checks/' + atom + '-native-publication-compile-unverified-20261004.json'))
for p in sorted((R / 'shared-sources').glob('P15.3-*')):
    add(p)
for directory, names in [
    (R / 'campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs-review', ['task.json', 'argument.md', 'settings.json', 'freeze.json']),
    (R / 'campaigns/round-50/P15.3-public-source-zero-volume-P-sensitive-bodies', ['input.json', 'settings.json', 'input-manifest.json']),
]:
    for name in names:
        add(directory / name)
for name in ['publish_original_P15_1_paper_20261004.py', 'prepare_public_P15_3_zero_volume_20261004.py',
             'prepare_public_P16_3_geometric_surface_review_20261004.py']:
    add(R / name)
for name in ['push-receipt-continuation57.json', 'push_checkpoint_continuation57_bulk.py',
             'prepare_checkpoint_continuation58.py', 'push_frozen_checkpoint_bulk_20261004.py']:
    add(G / name)
assert len({f['path'] for f in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
           'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
           'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
           'historical_reviewed_scoped_papers': 37, 'current_native_batch': items,
           'commit_message': 'Publish original P15.1 paper and audit; continue P15.3 construction and P16.3 surface proof review',
           'scope': 'Third original paper and actual complete review, selected literal primary bodies and source checks, public surface proof and independent review, fresh four-public-source author. No private transcripts, SQL, credentials, native Git object databases or complete originally uploaded PDF.'}
p = G / 'upload-manifest-continuation58.json'
assert not p.exists()
p.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files),
                  'fully_solved_original_atoms': payload['fully_solved_original_atoms'],
                  'active_items': [(x['atom'], x['role'], x['observed_status']) for x in items]}, indent=2))
