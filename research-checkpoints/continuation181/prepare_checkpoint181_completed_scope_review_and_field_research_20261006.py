from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'; G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation181.json'
F = G / 'continuation181-publication-records'
S = K / 'small-batch171-public-status-20261006-continuation181'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
assert not any(p.exists() for p in (M, F, S))
prior = json.loads((G / 'push-receipt-continuation180.json').read_text())
assert prior['commit_sha'] == '31c17e9d0e7206511df07710f31b98fef8bc8a77'
assert all(prior[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
review = json.loads((K / 'P19.2-round170-whole-original-review-binding-20261006.json').read_text())
assert review['verdict'] == 'INCONCLUSIVE' and review['entire_report_all_premises_and_passages_root_read']
F.mkdir(); S.mkdir(); items = []
for n, atom in ((170, 'P19.2'), (171, 'P16.4')):
    c = next((R / f'campaigns/round-{n}').iterdir())
    status = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'; p.write_text(json.dumps(status, indent=2) + '\n')
    items.append({'round': n, 'atom': atom, 'directory': str(c), 'observed_status': status['status'], 'observed_utc': status['observedAt'], 'public_status': str(p), 'public_status_sha256': sha(p), 'unsettled_calls': status['calls']['unsettled'], 'private_active_output_read': False, 'hot_feedback_sent': False, 'original_closed': False})
active = [x for x in items if x['unsettled_calls'] > 0]; assert len(active) <= 2
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': '171 entire arbitrary-complete-valued-field P16.4 research, only full accepted original P16.5 grantB.170 completed INCONCLUSIVE: minimal raw-mass obstruction checked in verified categories, exact original signature/category unresolved and normal-space extension unverified. No closure. Optional original-signature clarification pending; independent research continues.'}
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name; j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 64
    j.update(updated_utc=now, current_small_batch=batch)
    j['P19_2_actual_original_scope_review170'] = review
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    shutil.copyfile(p, F / name)
shutil.copyfile(R / 'checklist-current.tsv', F / 'checklist-current.tsv')
(F / 'scope-observation.json').write_text(json.dumps({'recorded_utc': now, 'originals_solved': 9, 'originals_open': 33, 'cumulative_independently_accepted_research_papers': 64, 'P19_2_original_closed': False, 'round170_new_supporting_paper_accepted': False, 'unverified_premise': 11, 'active_batch': [x['round'] for x in active], 'no_hot_feedback': True, 'existing_editor_unchanged': True}, indent=2) + '\n')
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json', '.md', '.tsv', '.tex', '.pdf', '.py')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation181/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()): add(p)
C = next((R / 'campaigns/round-171').iterdir())
for name in ('input.json', 'task.json', 'settings.json', 'freeze.json', 'mathematical-data-bindings.json', 'launch-record.json'): add(C / name)
for suffix in ('actual-canonical-independent-review', 'native-model-final-review', 'whole-original-review-binding'): add(K / f'P19.2-round170-{suffix}-20261006.json')
for name in ('bind_completed_review170_20261006.py', 'prepare_original_arbitrary_field171_20261006.py', 'launch_frozen_original_arbitrary_field171_20261006.py', 'record_verified180_20261006.py'): add(R / name)
add(G / 'push-receipt-continuation180.json'); add(Path(__file__))
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'): add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
front = json.loads((R / 'active-work.json').read_text())
M.write_text(json.dumps({'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': front['fully_solved_original_atoms'], 'remaining_open_atoms': 33, 'historical_reviewed_scoped_papers': 64, 'commit_message': 'Record whole P19.2 scope review and launch arbitrary-field P16.4 research', 'scope': 'Complete170 actual canonical/native review and exact evidence/native prompt/frozen input bindings. INCONCLUSIVE: no original closure and no newly accepted paper. Minimal obstruction checked in verified categories; normal model extension remains unverified. Entire171 original P16.4 frozen native author input, only accepted full originalP16.5 grantB and complete unreviewed46 research data with domains explicit. Public statuses only; no private active streams, hot feedback, credentials or full third-party source PDFs. Existing P16.4 editor unchanged/open. Counts9/42 and64 cumulative accepted research papers.'}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'listed_files': len(files), 'active_batch': [x['round'] for x in active]}, indent=2))
