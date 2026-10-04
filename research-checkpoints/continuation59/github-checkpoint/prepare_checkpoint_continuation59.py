"""Freeze the reviewed P16.3 surface paper and next two-item research batch."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation59-publication-records'
D.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
receipt = json.loads((G / 'push-receipt-continuation58.json').read_text())
assert receipt['commit_sha'] == '55ff4035283a156871a80be27f920edfe81274e8'
assert receipt['all_file_blob_bindings_verified_remote']
paper = R / 'deliverables/scoped-P16.3-round49'
publication = json.loads((paper / 'publication-preparation.json').read_text())
assert publication['verdict'] == 'PASS' and not publication['fully_solved_original_atom']
publication['first_and_last_pages_visually_read'] = True
publication['native_compile'] = 'Built-in compile requested; service has not returned diagnostics. No native success asserted. Two local passes succeeded.'
(paper / 'publication-preparation.json').write_text(json.dumps(publication, ensure_ascii=False, indent=2) + '\n')
visual = R / 'root-checks/P16.3-round49-reader-visual-addendum/visual-read.json'
visual.write_text(json.dumps({'observed_utc': now,
    'original_author_pages_visually_read': [1, 11], 'publication_pages_visually_read': [1, 12],
    'publication_source_sha256': publication['source_sha256'],
    'publication_pdf_sha256': publication['pdf_sha256'],
    'mathematical_verification_is_separate_from_visual_inspection': True}, indent=2) + '\n')
items = []
for atom, round_number, stem, database, session, role in [
    ('P13.2', 51, 'P13.2-public-source-fixed-Reeb-image', 'campaign.sqlite', 26899, 'author'),
    ('P15.3', 50, 'P15.3-public-source-zero-volume-P-sensitive-bodies-review', 'review.sqlite', 4974, 'correctness review'),
]:
    directory = R / 'campaigns' / ('round-' + str(round_number)) / stem
    proc = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(directory / database)],
                          cwd='/workspace/xean', capture_output=True, text=True, check=True)
    path = D / (atom + '-native-status.json')
    path.write_text(proc.stdout)
    items.append({'atom': atom, 'round': round_number, 'role': role, 'directory': str(directory),
                  'tool_session_id': session, 'observed_status': json.loads(proc.stdout)['status'],
                  'status': str(path), 'status_sha256': sha(path),
                  'input_or_argument_sha256': sha(directory / ('input.json' if role == 'author' else 'argument.md')),
                  'settings_sha256': sha(directory / 'settings.json'), 'accepted': False})
launch = D / 'current-small-batch-launch-and-observation.json'
launch.write_text(json.dumps({'observed_utc': now, 'route': 'Xean native Codex',
    'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'items': items,
    'hot_feedback_sent': False, 'original_completed': ['P15.1', 'P15.2', 'P16.6']}, indent=2) + '\n')
author_reader = R / 'root-checks/public-P15.3-round-50-final-reader-v2'
author_read = json.loads((author_reader / 'complete-root-read.json').read_text())
author_completion = {'reader': str(author_reader), 'root_read_sha256': sha(author_reader / 'complete-root-read.json'),
    'state': 'Native author completed candidate=false. Entire proof and all four canonical notes read; 23 literal primary units and two TeX passes reproduced. Fresh independent correctness review active.',
    'fully_solved_original_atom': False, 'candidate': False, 'review_session_id': 4974,
    'argument_sha256': author_read['author_argument_sha256'],
    'canonical_result_sha256': author_read['canonical_result_sha256']}
reviewed = {'scope': publication['scope'], 'source': publication['source'],
    'source_sha256': publication['source_sha256'], 'pdf': publication['pdf'],
    'pdf_sha256': publication['pdf_sha256'], 'pages': publication['pages'],
    'argument': str(paper / 'P16.3-argument.md'), 'review': publication['review'],
    'review_sha256': publication['review_sha256'], 'verdict': 'PASS',
    'operation_id': publication['operation_id'], 'full_original_atom_solved': False,
    'entire_report_premises_and_passages_root_read': True,
    'exact_all_premise_bindings_verified': True, 'first_and_last_pages_visually_read': True,
    'source_annex': str(paper / 'P16.3-source-review-annex.md'),
    'native_compile': publication['native_compile'], 'local_two_pass_compilation': 'SUCCESS'}
a = json.loads((R / 'active-work.json').read_text())
a['updated_utc'] = now
a['selected_atoms'] = ['P13.2', 'P15.3']
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint59: exact P16.3 surface PASS with corrected paper and source annex; P15.3 actual partial proof/review; P13.2 native author and public primary sources. Originals remain 3/42.'
a['current_small_batch'] = {'recorded_utc': now, 'route': 'Xean native Codex',
    'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'active_items': items,
    'completed_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'hot_feedback_sent': False}
a['P16.3_round49_reviewed_partial'] = reviewed
a['P16.3_round49_completed_partial']['state'] = 'Retained geometric-origin surface theorem correctness PASS; entire actual review read and bound. Original P16.3 remains open.'
a['P15.3_round50_completed_partial'] = author_completion
a['goal_state'] = 'ACTIVE: 3/42 unchanged originals solved; 39 open. 38 reviewed scoped papers, which are not 38 original solutions. Continue in small batches.'
a['next_work'] = 'Read P15.3 actual independent correctness report and P13.2 native proof after publication; retain original gaps and continue the next small batch. Push regularly.'
for solution in a['full_solutions']:
    if solution['atom'] in ['P15.1', 'P16.6']:
        solution['native_compilation'] = 'UNVERIFIED: built-in service failed or returned no diagnostics; two local passes succeeded. See preserved native-publication addendum.'
(R / 'active-work.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
assert sum(len(t['reviewed_papers']) for t in c['targets']) == 37
c['updated_utc'] = now
c['active_atoms'] = ['P13.2', 'P15.3']
c['current_small_batch_launch'] = str(launch)
c['current_small_batch_launch_sha256'] = sha(launch)
for t in c['targets']:
    if t['id'] == 'P16.3':
        assert not t['fully_solved']
        t['reviewed_papers'].append(reviewed)
        t['research_status'] = 'geometric_equal_characteristic_surface_correctness_PASS_original_open'
        t['current_focus'] = 'Surface theorem independently reviewed and published with exact raw normalization; mixed characteristic, unproved higher resolution and geometric-origin removal remain original gaps.'
        t['current_review_round49'] = reviewed
        t['current_unreviewed_campaign_round49']['state'] = a['P16.3_round49_completed_partial']['state']
    elif t['id'] == 'P15.3':
        t['research_status'] = 'divisorial_transcendental_partial_proof_independent_review_active_original_open'
        t['current_focus'] = 'Restricted divisorial body construction, zero-class-volume transcendental product example and dense-pole obstruction to direct analytic domination. All four actual notes/full proof read; independent review active.'
        t['current_completed_campaign_round50'] = author_completion
        t['current_review_round50'] = items[1]
    elif t['id'] == 'P13.2':
        t['research_status'] = 'native_public_primary_fixed_Reeb_image_author_active'
        t['current_focus'] = 'Unchanged all-normal affine cone fixed-Reeb image problem, including irrational Reeb fields, invariant carrier and probability convention. Actual Wu/BJ primary sources only; no proof accepted.'
        t['current_unreviewed_campaign_round51'] = items[0]
assert sum(len(t['reviewed_papers']) for t in c['targets']) == 38
c['historical_reviewed_scoped_papers'] = 38
c['unpublished_drafts'] = [x for x in c['unpublished_drafts'] if x['atom'] not in ['P15.1', 'P15.2', 'P16.6']]
(R / 'checklist-current.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
with (R / 'checklist-current.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['ID', 'Closure', 'Research', 'Reviewed_papers', 'Title'])
    for t in c['targets']:
        w.writerow([t['id'], t['closure'], t['research_status'], len(t['reviewed_papers']), t['title']])
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    path = Path(path)
    assert path.is_file()
    files.append({'local': str(path), 'path': remote or 'research-checkpoints/continuation59/' + str(path.relative_to(R)),
                  'bytes': path.stat().st_size, 'sha256': sha(path)})
def add_directory(directory, manuscript=False):
    for path in sorted(directory.rglob('*')):
        if path.is_file() and path.suffix in {'.tex', '.pdf', '.json', '.md', '.log', '.txt', '.png', '.py', '.stdout', '.stderr'}:
            add(path, 'manuscript/editorial/xean_research_20261003/' + str(path.relative_to(R)) if manuscript else None)
add_directory(paper, True)
for directory in [D, author_reader,
    R / 'root-checks/P16.3-round49-reader-visual-addendum',
    R / 'root-checks/P13-primary-source-read-20261004']:
    add_directory(directory)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
for prefix in ['P13-Wu-', 'P16.3-Stacks-']:
    for path in sorted((R / 'shared-sources').glob(prefix + '*')):add(path)
for directory, names in [
    (R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-image', ['input.json', 'settings.json', 'input-manifest.json']),
    (R / 'campaigns/round-50/P15.3-public-source-zero-volume-P-sensitive-bodies-review', ['task.json', 'argument.md', 'settings.json', 'freeze.json']),
]:
    for name in names:add(directory / name)
for path in [R / 'root-checks/P13-fixed-Reeb-source-diagnostic-20261004.md',
    R / 'root-checks/P15.3-round50-reader-preparation-failure.json',
    R / 'root-checks/P16.3-round49-actual-correctness-review.json',
    R / 'publish_scoped_P16_3_round49_20261004.py',
    R / 'prepare_public_fixed_Reeb_image_20261004.py',
    R / 'prepare_public_P15_3_divisorial_review_20261004.py',
    R / 'prepare_public_P15_3_divisorial_review_v2_20261004.py',
    G / 'push-receipt-continuation58.json', G / 'prepare_checkpoint_continuation59.py']:
    add(path)
assert len({x['path'] for x in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 38, 'current_native_batch': items,
    'commit_message': 'Publish reviewed P16.3 surface theorem; audit P15.3 bodies and research fixed-Reeb image',
    'scope': 'Reviewed partial surface paper, actual complete correctness report and primary annex; fresh P15.3 partial proof and frozen exact review with four public papers; P13.2 author and source checks. No private transcripts, SQL, credentials, native Git object databases, generated book-source or complete originally uploaded PDF.'}
manifest = G / 'upload-manifest-continuation59.json'
assert not manifest.exists()
manifest.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files),
    'reviewed_scoped_papers': 38, 'fully_solved_original_atoms': payload['fully_solved_original_atoms'],
    'active_items': [(x['atom'], x['role'], x['observed_status']) for x in items]}, indent=2))
