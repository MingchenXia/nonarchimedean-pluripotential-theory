"""Freeze the completed Reeb draft and the next small unibranch batch."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation61-publication-records'
D.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
receipt = json.loads((G / 'push-receipt-continuation60.json').read_text())
assert receipt['commit_sha'] == '9a5783ad70cce7de47b3fddddf6559215809b459'
assert receipt['all_file_blob_bindings_verified_remote']

items = []
for atom, number, stem, database, session, role in [
    ('P16.1', 53, 'P16.1-public-source-unibranch-finite-energy-equation', 'campaign.sqlite', 49503, 'author'),
    ('P13.2', 51, 'P13.2-public-source-fixed-Reeb-image-review-v2', 'review.sqlite', 3702, 'correctness review'),
]:
    directory = R / 'campaigns' / ('round-' + str(number)) / stem
    q = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(directory / database)],
                       cwd='/workspace/xean', capture_output=True, text=True, check=True)
    p = D / (atom + '-native-status.json')
    p.write_text(q.stdout)
    items.append({'atom': atom, 'round': number, 'role': role, 'directory': str(directory),
                  'tool_session_id': session, 'observed_status': json.loads(q.stdout)['status'],
                  'status': str(p), 'status_sha256': sha(p),
                  'input_or_argument_sha256': sha(directory / ('input.json' if role == 'author' else 'argument.md')),
                  'settings_sha256': sha(directory / 'settings.json'), 'accepted': False})
launch = D / 'current-small-batch-observation.json'
launch.write_text(json.dumps({'observed_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
                             'reasoning': 'xhigh', 'items': items, 'hot_feedback_sent': False,
                             'original_completed': ['P15.1', 'P15.2', 'P16.6']}, indent=2) + '\n')

P = R / 'root-checks/public-P13.1-round-52-final-reader'
read = json.loads((P / 'complete-root-read.json').read_text())
assert read['entire_argument_read'] and read['all_four_actual_canonical_notes_read']
assert read['literal_primary_units'] == 43 and read['root_tex_pass_returncodes'] == [0, 0]
assert not read['mathematical_correctness_verified'] and not read['original_atom_solved']
review = R / 'campaigns/round-52/P13.1-public-source-new-unibranch-envelope-Reeb-calculus-review'
freeze = json.loads((review / 'freeze.json').read_text())
assert sha(review / 'argument.md') == freeze['argument_sha256']
assert sha(review / 'task.json') == freeze['task_sha256']
assert sha(review / 'settings.json') == freeze['settings_sha256']
queued = {'directory': str(review), 'freeze': str(review / 'freeze.json'),
          'freeze_sha256': sha(review / 'freeze.json'), 'task_and_settings_entire_root_read': True,
          'state': 'Prepared exact partial review; not launched at this checkpoint; two active native items.',
          'provider_submission_attempted': False, 'fully_solved_original_atom': False}
(D / 'P13.1-completed-partial-and-prepared-review.json').write_text(json.dumps({
    'reader': str(P), 'reader_record_sha256': sha(P / 'complete-root-read.json'),
    'complete_proof_and_all_four_canonical_notes_read': True, 'literal_units': 43,
    'root_tex_pass_returncodes': [0, 0], 'finite_diagnostics': '63 roots,252 slopes,32 finite filtration counts; not infinite-domain proof verification',
    'result': 'Canonical order bijections on H/CPSH/PSH and quantified bounded comparison; nonnegative filtration comparison; conditional envelope transfer.',
    'missing_original_obligations': 'Cross-Reeb E1 preservation and energy comparison, moving-MA uniform tails, energy extension and uniform differentiation.',
    'independent_correctness_verdict': None, 'original_closed': False, 'prepared_review': queued,
}, indent=2) + '\n')

literature = D / 'additional-primary-root-reads'
literature.mkdir()
sources = []
for name, ranges, whole_math_body in [
    ('new-primary-2609.27610v1-20261004.txt', [(639,750), (754,774), (998,1038), (1964,2048), (408,455)], False),
    ('new-primary-2203.12282v3-20261004.txt', [(1,180), (181,301), (302,448), (449,530), (531,660)], True),
    ('new-primary-2509.09442v1-20261004.txt', [(1,180)], False),
    ('new-primary-2302.02541v3-20261004.txt', [(1,110)], False),
]:
    p = R / 'shared-sources' / name
    lines = p.read_text().split('\n')
    units = []
    for a, b in ranges:
        assert 1 <= a <= b <= len(lines)
        e = literature / (p.stem + '-LF' + str(a) + '-' + str(b) + '.txt')
        e.write_text('\n'.join(lines[a-1:b]))
        units.append({'LF_start': a, 'LF_end': b, 'literal_file': str(e), 'sha256': sha(e), 'entire_selected_unit_root_read': True})
    sources.append({'primary_file': str(p), 'sha256': sha(p), 'LF_line_count': len(lines), 'units': units,
                    'whole_mathematical_body_root_read': whole_math_body, 'whole_document_including_references_root_read': False})
(literature / 'read-record.json').write_text(json.dumps({'recorded_utc': now, 'sources': sources,
    'application_limits': [
        'FGK mixed-characteristic envelope result retains projective resolution; MA theorem also retains embedded resolution. Surface projectivity gap is explicit.',
        'Mesquita-Piccione/Witt Nystrom intro has Kahler hypotheses; no big-class or arbitrary-Berkovich equation inferred.',
        'Darvas/Xia/Zhang intro does not by itself prove zero-volume or general big-class MA equations.',
        'Lyuhui Wu local definitions have a lower/upper logarithmic-growth convention inconsistency; explicit tropical barrier and local decreasing PL replacement are unreviewed root deductions.',
    ], 'new_material_sent_to_active_author_or_review': False}, ensure_ascii=False, indent=2) + '\n')

a = json.loads((R / 'active-work.json').read_text())
a['updated_utc'] = now
a['selected_atoms'] = ['P16.1', 'P13.2']
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint61: completed unreviewed P13.1 partial proof; exact review queue; P16.1 new unibranch author; source bridge and explicit tropical deductions. Originals remain3/42.'
a['current_small_batch'] = {'recorded_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
                          'reasoning': 'xhigh', 'active_items': items, 'completed_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'hot_feedback_sent': False}
a['prepared_P13.1_round52_review'] = queued
a['prepared_P16.1_round53']['state'] = 'Native author launched; inspect current_small_batch for live observed status. No mathematical result accepted.'
a['P13.1_round52_author_completion']['state'] = 'Completed partial; complete proof and all four notes read;43 literal units and two TeX passes reproduced. Exact review prepared. E1/uniform differentiation original remains open.'
a['new_unreviewed_tropical_barrier_repair'] = {'path': str(R / 'root-checks/P16.1-explicit-tropical-barrier-repair-20261004.md'),
    'sha256': sha(R / 'root-checks/P16.1-explicit-tropical-barrier-repair-20261004.md'), 'independently_reviewed': False, 'sent_to_active_author': False, 'closes_original': False}
a['P15.3_round50_reviewed_partial']['native_compile'] = 'UNVERIFIED: owned built-in compiler I/O terminated after no returned diagnostics; two local passes succeeded.'
a['native_publication_compile_addendum_round50'] = str(R / 'root-checks/P15.3-round50-reviewed-edition-native-compile-addendum.json')
a['next_work'] = 'Read actual P13.2 review and P16.1 author outputs when complete, launch the queued P13.1 exact review in a free slot, reconstruct missing genuine energy/envelope steps, and push regular reviewed or explicitly unreviewed checkpoints.'
assert a['fully_solved_original_atoms'] == ['P15.1', 'P15.2', 'P16.6']
(R / 'active-work.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42 and sum(len(t['reviewed_papers']) for t in c['targets']) == 39
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
c['updated_utc'] = now
c['active_atoms'] = ['P16.1', 'P13.2']
c['current_small_batch_launch'] = str(launch)
c['current_small_batch_launch_sha256'] = sha(launch)
for t in c['targets']:
    if t['id'] == 'P13.1':
        t['current_completed_campaign_round52'] = a['P13.1_round52_author_completion']
        t['current_review_round52'] = queued
    elif t['id'] == 'P13.2':
        t['current_review_round51'] = items[1]
    elif t['id'] == 'P16.1':
        t['current_native_campaign_round53'] = items[0]
(R / 'checklist-current.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
with (R / 'checklist-current.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['ID', 'Closure', 'Research', 'Reviewed_papers', 'Title'])
    for t in c['targets']: w.writerow([t['id'], t['closure'], t['research_status'], len(t['reviewed_papers']), t['title']])
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']: shutil.copyfile(R / name, D / name)

files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file()
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation61/' + str(p.relative_to(R)),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})
def add_directory(directory):
    for p in sorted(directory.rglob('*')):
        if p.is_file() and p.suffix in {'.tex','.pdf','.json','.md','.log','.txt','.png','.py','.stdout','.stderr'}: add(p)
for directory in [D, P, R / 'root-checks/P16.1-new-source-bridge-primary-read-20261004']: add_directory(directory)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
for directory, names in [
    (review, ['task.json','argument.md','settings.json','freeze.json']),
    (R / 'campaigns/round-53/P16.1-public-source-unibranch-finite-energy-equation', ['input.json','settings.json','input-manifest.json']),
]:
    for name in names: add(directory / name)
for pattern in ['*-20261004-continuation61.html','*-20261004-continuation61.json','*-20261004-continuation61.pdf','*-20261004-continuation61.txt','new-public-primary-cache-20261004-continuation61-additions.json']:
    for p in sorted((R / 'shared-sources').glob(pattern)): add(p)
for p in [R / 'root-checks/P16.1-explicit-tropical-barrier-repair-20261004.md',
          R / 'root-checks/P15.3-round50-reviewed-edition-native-compile-addendum.json',
          R / 'prepare_public_P13_1_orbit_comparison_review_20261004.py',
          R / 'prepare_public_P16_1_unibranch_equation_20261004.py',
          G / 'push-receipt-continuation60.json', G / 'prepare_checkpoint_continuation61.py']: add(p)
assert len({x['path'] for x in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1','P15.2','P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 39, 'current_native_batch': items,
    'commit_message': 'Checkpoint canonical Reeb transport draft and continue unibranch finite-energy equation',
    'scope': 'Completed unreviewed P13.1 partial proof and all canonical notes; prepared exact review; fresh P16.1 native author inputs; literal source bridge and cold public literature reads; unreviewed explicit tropical barrier/local PL deductions. No new original closure, private transcripts, SQL, credentials, Git databases, generated book-source or complete uploaded PDF.'}
manifest = G / 'upload-manifest-continuation61.json'
assert not manifest.exists()
manifest.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
                  'originals_solved': 3, 'originals_open': 39, 'reviewed_scoped_papers': 39,
                  'active_items': [(x['atom'],x['role'],x['observed_status']) for x in items]}, indent=2))
