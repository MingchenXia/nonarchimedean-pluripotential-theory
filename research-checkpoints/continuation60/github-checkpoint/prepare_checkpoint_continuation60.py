"""Freeze reviewed P15.3, exact P13.2 review repair and new envelope research."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation60-publication-records'
D.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
receipt = json.loads((G / 'push-receipt-continuation59.json').read_text())
assert receipt['commit_sha'] == 'b82dcfdbefe875fc172c93321911f770f62b9db4'
assert receipt['all_file_blob_bindings_verified_remote']
paper = R / 'deliverables/scoped-P15.3-round50'
publication = json.loads((paper / 'publication-preparation.json').read_text())
assert publication['verdict'] == 'PASS' and not publication['fully_solved_original_atom']
publication['first_and_last_pages_visually_read'] = True
publication['native_compile'] = 'Built-in compile requested for this reviewed edition; no returned diagnostics yet. No native success asserted; two fresh local passes succeeded.'
(paper / 'publication-preparation.json').write_text(json.dumps(publication, ensure_ascii=False, indent=2) + '\n')
addenda = R / 'root-checks/native-compile-publication-addenda-20261004-continuation60.json'
addenda.write_text(json.dumps({'recorded_utc': now, 'editor_remains': '/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'items': [
        {'source': '/workspace/research/deliverables/scoped-P16.3-round49/P16.3-paper.tex', 'functions_cell': '2102', 'native_status': 'UNVERIFIED', 'observed_error': 'connection closed before server request was answered', 'local_two_pass_status': 'SUCCESS'},
        {'source': '/workspace/research/root-checks/public-P15.3-round-50-final-reader-v2/P15.3-paper.tex', 'functions_cell': '2129', 'native_status': 'UNVERIFIED', 'observation': 'Owned compiler I/O cell terminated after no returned diagnostics; source and local successful builds preserved.'},
        {'source': str(paper / 'P15.3-paper.tex'), 'functions_cell': '2158', 'native_status': 'PENDING_NO_DIAGNOSTICS', 'local_two_pass_status': 'SUCCESS'},
    ], 'compiler_io_does_not_change_mathematical_scope_or_verdict': True}, indent=2) + '\n')
items = []
for atom, round_number, stem, database, session, role in [
    ('P13.1', 52, 'P13.1-public-source-new-unibranch-envelope-Reeb-calculus', 'campaign.sqlite', 4905, 'author'),
    ('P13.2', 51, 'P13.2-public-source-fixed-Reeb-image-review-v2', 'review.sqlite', 3702, 'correctness review'),
]:
    directory = R / 'campaigns' / ('round-' + str(round_number)) / stem
    proc = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(directory / database)], cwd='/workspace/xean', capture_output=True, text=True, check=True)
    path = D / (atom + '-native-status.json')
    path.write_text(proc.stdout)
    items.append({'atom': atom, 'round': round_number, 'role': role, 'directory': str(directory),
        'tool_session_id': session, 'observed_status': json.loads(proc.stdout)['status'],
        'status': str(path), 'status_sha256': sha(path),
        'input_or_argument_sha256': sha(directory / ('input.json' if role == 'author' else 'argument.md')),
        'settings_sha256': sha(directory / 'settings.json'), 'accepted': False})
launch = D / 'current-small-batch-launch-and-observation.json'
launch.write_text(json.dumps({'observed_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
    'reasoning': 'xhigh', 'items': items, 'hot_feedback_sent': False,
    'original_completed': ['P15.1', 'P15.2', 'P16.6']}, indent=2) + '\n')
reader = R / 'root-checks/public-P13.2-round-51-final-reader'
root_read = json.loads((reader / 'complete-root-read.json').read_text())
completion = {'reader': str(reader), 'root_read_sha256': sha(reader / 'complete-root-read.json'),
    'state': 'Native author completed candidate=false. Entire proof, four actual canonical notes and provenance application metadata read; all31 primary literal units reproduced and two fresh TeX passes succeeded. Exact review active after transport-only size repair.',
    'fully_solved_original_atom': False, 'candidate': False, 'review_session_id': 3702,
    'argument_sha256': root_read['author_argument_sha256'], 'canonical_result_sha256': root_read['canonical_result_sha256']}
reviewed = {'scope': publication['scope'], 'source': publication['source'], 'source_sha256': publication['source_sha256'],
    'pdf': publication['pdf'], 'pdf_sha256': publication['pdf_sha256'], 'pages': publication['pages'],
    'argument': str(paper / 'P15.3-argument.md'), 'review': publication['review'],
    'review_sha256': publication['review_sha256'], 'verdict': 'PASS', 'operation_id': publication['operation_id'],
    'full_original_atom_solved': False, 'entire_report_premises_and_passages_root_read': True,
    'exact_all_premise_bindings_verified': True, 'first_and_last_pages_visually_read': True,
    'source_annex': str(paper / 'P15.3-source-review-annex.md'), 'native_compile': publication['native_compile'],
    'local_two_pass_compilation': 'SUCCESS'}
public_cache = []
for identifier, version, title in [
    ('2609.27610', 'v1', 'On the local theory of non-archimedean psh functions'),
    ('2203.12282', 'v3', 'On the non-archimedean Monge-Ampere equation in mixed characteristic'),
    ('2509.09442', 'v1', 'A transcendental non-Archimedean Calabi-Yau Theorem with applications to the cscK problem'),
    ('2302.02541', 'v3', 'A transcendental approach to non-Archimedean metrics of pseudoeffective classes'),
]:
    paths = [R / 'shared-sources' / ('new-primary-' + identifier + version + '-20261004.' + ext) for ext in ['pdf', 'txt']]
    paths.append(R / 'shared-sources' / ('new-primary-' + identifier + '-20261004.html'))
    public_cache.append({'id': identifier + version, 'title': title, 'url': 'https://arxiv.org/pdf/' + identifier + version,
        'files': [{'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)} for p in paths],
        'abstract_read': True, 'whole_body_root_read': False,
        'selected_body_root_read': identifier == '2609.27610'})
cache_record = R / 'shared-sources/new-public-primary-cache-20261004-continuation60.json'
cache_record.write_text(json.dumps({'recorded_utc': now, 'sources': public_cache,
    'application_limits': 'No theorem is applied from an abstract alone. Lyuhui Wu selected envelope theorem/proof read; projective-to-cone transfer and irrational uniformity remain obligations. Unlocated APW26a/b preprints are not automatically discharged.'}, ensure_ascii=False, indent=2) + '\n')
a = json.loads((R / 'active-work.json').read_text())
a['updated_utc'] = now
a['selected_atoms'] = ['P13.1', 'P13.2']
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint60: reviewed P15.3 partial paper; P13.2 full partial proof and transport-size repair; new public envelope sources and P13.1 native author. Originals remain3/42.'
a['current_small_batch'] = {'recorded_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
    'reasoning': 'xhigh', 'active_items': items, 'completed_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'hot_feedback_sent': False}
a['P15.3_round50_reviewed_partial'] = reviewed
a['P15.3_round50_completed_partial']['state'] = 'Retained divisorial/transcendental partial proof and dense-pole obstruction correctness PASS; entire actual review read and bound. Original remains open.'
a['P13.2_round51_completed_partial'] = completion
a['new_public_envelope_sources'] = {'cache': str(cache_record), 'new_root_bounded_obstacle_comparison': str(R / 'root-checks/P13.1-bounded-obstacle-Reeb-comparison-20261004.md'), 'root_lemma_independently_reviewed': False, 'sent_to_active_author': False}
a['goal_state'] = 'ACTIVE: 3/42 unchanged originals solved; 39 open. 39 reviewed scoped papers, which are not39 original solutions. Continue in small batches.'
a['next_work'] = 'Read the completed P13.1 proof and P13.2 exact actual review when available; resolve genuine envelope/quotient and irrational energy comparisons using new primary literature. Preserve original scope and push regularly.'
a['native_publication_compile_addendum_continuation60'] = str(addenda)
(R / 'active-work.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
assert sum(len(t['reviewed_papers']) for t in c['targets']) == 38
c['updated_utc'] = now
c['active_atoms'] = ['P13.1', 'P13.2']
c['current_small_batch_launch'] = str(launch)
c['current_small_batch_launch_sha256'] = sha(launch)
for t in c['targets']:
    if t['id'] == 'P15.3':
        assert not t['fully_solved']
        t['reviewed_papers'].append(reviewed)
        t['research_status'] = 'divisorial_transcendental_partial_correctness_PASS_original_open'
        t['current_focus'] = 'Reviewed divisorial construction, exact transcendental dimension-two example and dense-pole obstruction. Arbitrary nonanalytic P-data and general numerical/flag/modification obligations remain.'
        t['current_review_round50'] = reviewed
        t['current_completed_campaign_round50']['state'] = a['P15.3_round50_completed_partial']['state']
    elif t['id'] == 'P13.2':
        t['research_status'] = 'fixed_Reeb_partial_exact_review_active_original_open'
        t['current_focus'] = 'Carrier, density, source corrections, mixed-integrability and I-Cauchy estimates proved in an unreviewed partial draft. Genuine limit-potential realization and image/existence closure remain open.'
        t['current_completed_campaign_round51'] = completion
        t['current_review_round51'] = items[1]
    elif t['id'] == 'P13.1':
        t['research_status'] = 'native_new_unibranch_envelope_Reeb_author_active_original_open'
        t['current_focus'] = 'Use actual new projective unibranch envelope theorem with verified hypotheses; prove cone/quotient transfer and quantitative all-Reeb finite-energy comparison rather than assume them.'
        t['current_unreviewed_campaign_round52'] = items[0]
assert sum(len(t['reviewed_papers']) for t in c['targets']) == 39
c['historical_reviewed_scoped_papers'] = 39
(R / 'checklist-current.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
with (R / 'checklist-current.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(['ID', 'Closure', 'Research', 'Reviewed_papers', 'Title'])
    for t in c['targets']:w.writerow([t['id'], t['closure'], t['research_status'], len(t['reviewed_papers']), t['title']])
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    path = Path(path); assert path.is_file()
    files.append({'local': str(path), 'path': remote or 'research-checkpoints/continuation60/' + str(path.relative_to(R)), 'bytes': path.stat().st_size, 'sha256': sha(path)})
def add_directory(directory, manuscript=False):
    for path in sorted(directory.rglob('*')):
        if path.is_file() and path.suffix in {'.tex', '.pdf', '.json', '.md', '.log', '.txt', '.png', '.py', '.stdout', '.stderr'}:
            add(path, 'manuscript/editorial/xean_research_20261003/' + str(path.relative_to(R)) if manuscript else None)
add_directory(paper, True)
for directory in [D, reader, R / 'root-checks/P13-new-envelope-primary-read-20261004']:add_directory(directory)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
for path in sorted((R / 'shared-sources').glob('new-primary-*')):add(path)
add(cache_record)
for directory, names in [
    (R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-image-review', ['task.json', 'argument.md', 'settings.json', 'freeze.json']),
    (R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-image-review-v2', ['task.json', 'argument.md', 'settings.json', 'freeze.json']),
    (R / 'campaigns/round-52/P13.1-public-source-new-unibranch-envelope-Reeb-calculus', ['input.json', 'settings.json', 'input-manifest.json']),
]:
    for name in names:add(directory / name)
for pattern in ['P16.5-new-literature-search*', 'P13-new-affine-cones-search*', 'P16.1-new-envelope-search*', 'APW26a-title-search*', 'APW26b-title-search*']:
    for path in sorted((R / 'shared-sources').glob(pattern)):add(path)
for path in [addenda, R / 'root-checks/P13.2-round51-review-native-status-20261004.json',
    R / 'root-checks/P15.3-round50-actual-correctness-review.json',
    R / 'root-checks/P13.1-bounded-obstacle-Reeb-comparison-20261004.md',
    R / 'publish_scoped_P15_3_round50_20261004.py', R / 'prepare_public_P13_2_fixed_image_review_20261004.py',
    R / 'prepare_public_P13_2_fixed_image_review_v2_20261004.py', R / 'prepare_public_P13_1_new_envelope_20261004.py',
    G / 'push-receipt-continuation59.json', G / 'prepare_checkpoint_continuation60.py']:add(path)
assert len({x['path'] for x in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 39, 'current_native_batch': items,
    'commit_message': 'Publish reviewed zero-volume divisorial bodies; continue Reeb envelope and image proofs',
    'scope': 'P15.3 reviewed partial paper and actual report; P13.2 full retained partial proof and exact review transport repair; new public primary caches, explicit application limits and P13.1 native author. No private transcripts, SQL, credentials, Git databases, generated book-source or complete uploaded PDF.'}
manifest = G / 'upload-manifest-continuation60.json'; assert not manifest.exists()
manifest.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(manifest), 'sha256': sha(manifest), 'files': len(files), 'reviewed_scoped_papers': 39,
    'fully_solved_original_atoms': payload['fully_solved_original_atoms'],
    'active_items': [(x['atom'], x['role'], x['observed_status']) for x in items]}, indent=2))
