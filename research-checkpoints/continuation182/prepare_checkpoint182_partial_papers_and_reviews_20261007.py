from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'; G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation182.json'
F = G / 'continuation182-publication-records'
S = K / 'small-batch173175-public-status-20261007-continuation182'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
assert not any(p.exists() for p in (M, F, S))
prior = json.loads((G / 'push-receipt-continuation181.json').read_text())
assert prior['commit_sha'] == '58b4babd53dd05f9899b81b4ba4537024a8be0b4'
assert all(prior[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
F.mkdir(); S.mkdir(); items = []
for n, atom in ((171, 'P16.4'), (172, 'P14.4'), (173, 'P16.4'), (175, 'P14.4')):
    c = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    if st['status'] == 'blocked': assert st['calls']['unsettled'] == st['work']['active'] == st['work']['queued'] == 0
    p = S / f'round{n}-public-native-status.json'; p.write_text(json.dumps(st, indent=2) + '\n')
    items.append({'round': n, 'atom': atom, 'directory': str(c), 'observed_status': st['status'], 'observed_utc': st['observedAt'], 'public_status': str(p), 'public_status_sha256': sha(p), 'unsettled_calls': st['calls']['unsettled'], 'private_active_output_read': False, 'hot_feedback_sent': False, 'original_closed': False})
active = [x for x in items if x['unsettled_calls'] > 0]; assert len(active) <= 2
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': '173 whole171 all-dimensional arbitrary-trivial-characteristic-zero genuine E1 descent review;175 whole172 restricted polar-measure geometry and entire-smooth-modification-tower review. Only full accepted B grant.172 native result unaccepted after unregistered B support label failure.174 pre-admission usagePrefix failure retained;175 identical task/math, shorter valid prefix. Both original atoms remain open.'}
bindings = {n: json.loads((K / f'{atom}-round{n}-settled-partial-author-input-binding-20261007.json').read_text()) for n, atom in ((171, 'P16.4'), (172, 'P14.4'))}
focus = {'P16.4': 'Round171 complete12-page unverified partial theorem for arbitrary trivially valued characteristic-zero ground fields, all dimensions, genuine ample E1 mixed operator and original arbitrary-support targets. Entire source/all notes read,2 clean exports. Independent173 running. Nontrivial/nondiscrete field axis remains open.', 'P14.4': 'Round172 complete10-page unverified restricted polar-measure sector and claimed all-smooth-modification-tower equal-ideal/equal-product/equal-mass/different-P example. Native submission settled but kernel publication blocked on unregistered B support; no canonical author result. Entire source/all notes read,2 clean exports. Independent175 running after174 pre-admission prefix failure. Arbitrary big transcendental/nonprojective positivity remains open.'}
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name; j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 64
    j.update(updated_utc=now, current_small_batch=batch)
    j['P16_4_completed_partial_author171'] = bindings[171]
    j['P14_4_settled_unpublished_partial_author172'] = bindings[172]
    j['P14_4_review174_pre_admission_failure'] = json.loads((K / 'P14.4-round174-pre-admission-prefix-validation-failure-20261007.json').read_text())
    if name == 'checklist-current.json':
        for target in j['targets']:
            if target['id'] in focus:
                assert not target['fully_solved'] and target['closure'] == 'open'
                target['current_focus'] = focus[target['id']]
                target['research_status'] = 'new_partial_complete_source_read_independent_review_running'
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
table = R / 'checklist-current.tsv'
with table.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t'); columns = reader.fieldnames; rows = list(reader)
for row in rows:
    if row['ID'] in focus: row['Research'] = 'new_partial_complete_source_read_independent_review_running'
with table.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=columns, delimiter='\t', lineterminator='\n'); writer.writeheader(); writer.writerows(rows)
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'): shutil.copyfile(R / name, F / name)
(F / 'scope-observation.json').write_text(json.dumps({'recorded_utc': now, 'originals_solved': 9, 'originals_open': 33, 'cumulative_independently_accepted_research_papers': 64, 'new_original_closure': None, 'new_partial_papers_independently_accepted': False, 'active_batch': [x['round'] for x in active], '173_175_partial_correctness_not_original_closure': True, '172_native_unpublished_failure_preserved': True, '174_pre_admission_failure_preserved': True, 'native_paper_compiler_results_pending': True, 'no_hot_feedback': True, 'existing_editor_unchanged': True}, indent=2) + '\n')
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json', '.md', '.tsv', '.tex', '.pdf', '.py')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation182/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S, K / 'public-P16.4-round171-partial-reader', K / 'public-P14.4-round172-partial-reader'):
    for p in sorted(folder.iterdir()):
        if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json', '.md', '.tsv', '.tex', '.pdf'): add(p)
for n in (172, 173, 174, 175):
    c = next((R / f'campaigns/round-{n}').iterdir())
    names = ['task.json', 'settings.json', 'freeze.json', 'mathematical-data-bindings.json', 'launch-record.json']
    names += ['input.json'] if n == 172 else ['argument.md', 'original-task.json']
    for name in names: add(c / name)
for n, atom in ((171, 'P16.4'), (172, 'P14.4')):
    add(K / f'{atom}-round{n}-native-model-final-author-result-20261007.json')
    add(K / f'{atom}-round{n}-settled-partial-author-input-binding-20261007.json')
add(K / 'P16.4-round171-actual-canonical-author-result-20261007.json')
add(K / 'P14.4-round174-pre-admission-prefix-validation-failure-20261007.json')
for name in ('prepare_original_P14_4_richer_positivity172_20261006.py', 'launch_frozen_original_P14_4_172_20261006.py', 'bind_settled_authors171172_and_prepare_readers_20261007.py', 'record_readers171172_reproduction_20261007.py', 'prepare_partial_independent_reviews173174_20261007.py', 'launch_frozen_partial_review173174_20261007.py', 'prepare_and_launch_repaired_review175_20261007.py', 'record_verified181_20261006.py'): add(R / name)
add(G / 'push-receipt-continuation181.json'); add(Path(__file__))
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'): add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
front = json.loads((R / 'active-work.json').read_text())
M.write_text(json.dumps({'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': front['fully_solved_original_atoms'], 'remaining_open_atoms': 33, 'historical_reviewed_scoped_papers': 64, 'commit_message': 'Publish partial field-descent and polar-geometry papers for independent review', 'scope': 'Complete12-page171 P16.4 all-dimensional trivial-ground-field equation draft and10-page172 P14.4 restricted polar geometry/entire-modification-tower draft. Whole sources/every native note read, native-input/frozen grant bindings exact,2 clean local exports and first/last visual pages.173 and175 exact whole-paper independent partial reviews launched,only accepted B; no new acceptance or original closure.172 native result unpublished after support-label failure;174 failed pre-admission on prefix length;175 math unchanged,valid short prefix. Regular checkpoint preserves every failed frozen declaration,public statuses only, no active private streams, no source PDF copying,no auth changes,existing P16.4 editor unchanged/open. Counts9/42 and64 cumulative accepted papers.'}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'listed_files': len(files), 'active_batch': [x['round'] for x in active], 'counts_unchanged': True}, indent=2))
