from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation178.json'
assert not M.exists()
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
prior = json.loads((G / 'push-receipt-continuation177.json').read_text())
assert prior['commit_sha'] == 'e7676dc3d24345ff355245d835485b44efe8333d'
assert all(prior[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
C = next((R / 'campaigns/round-168').iterdir())
freeze = json.loads((C / 'freeze.json').read_text())
launch = json.loads((C / 'launch-record.json').read_text())
assert freeze['input_sha256'] == launch['frozen_math_input_sha256'] == '16862f135d05608a734623a38d5e2d7b953e34747d6f356d2e1d6b724fde1fae'
for name, key in [('input.json', 'input_sha256'), ('task.json', 'task_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == freeze[key]
S = K / 'small-batch167-168-public-status-20261006-continuation178'
F = G / 'continuation178-publication-records'
S.mkdir()
F.mkdir()
items = []
for n, atom in [(167, 'P16.5'), (168, 'P19.2')]:
    c = next((R / f'campaigns/round-{n}').iterdir())
    status = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'
    p.write_text(json.dumps(status, indent=2) + '\n')
    items.append({'round': n, 'atom': atom, 'directory': str(c), 'observed_status': status['status'], 'observed_utc': status['observedAt'], 'public_status': str(p), 'public_status_sha256': sha(p), 'unsettled_calls': status['calls']['unsettled'], 'private_active_output_read': False, 'hot_feedback_sent': False, 'original_closed': False})
active = [x for x in items if x['unsettled_calls'] > 0]
assert len(active) <= 2
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': '167 whole corrected P16.5 proof review;168 entire residual P19.2 author research with complete accepted R/T/C/S/E bodies. No new mathematical acceptance. Independent ROOT P/I source investigation has not been sent into either active worker.'}
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, current_small_batch=batch, P19_2_launched_remaining_original_research168=launch, github_pending_checkpoint='continuation178 frozen', goal_state='8/42 original problems independently accepted;34 open;63 accepted supporting papers. Fresh167 reviews all18 corrected P16.5 pages with G0/G1 only.168 researches unchanged entire residual P19.2 using complete grants R/T/C/S/E, retaining arbitrary weak rays, prescribed starts, finer closed P data and entropy/energy. No private active stream reads, no hot feedback, no new original closure.158 settled connection failure without verdict;166 old whole original FAIL preserved.')
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
rows = (R / 'checklist-current.tsv').read_text().splitlines()
for i, row in enumerate(rows):
    cells = row.split('\t')
    if cells[0] == 'P19.2':
        cells[2] = 'Fresh168 entire residual original research active with complete R/T/C/S/E grants; closed finer P data and arbitrary weak rays retained. Original open;8/42,63 supports.'
    rows[i] = '\t'.join(cells)
(R / 'checklist-current.tsv').write_text('\n'.join(rows) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    shutil.copyfile(R / name, F / name)
(F / 'scope-observation.json').write_text(json.dumps({'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_supporting_papers': 63, 'active_batch': [x['round'] for x in active], 'original_closed': False, 'no_hot_feedback': True, 'existing_editor_unchanged': True, 'ROOT_P19_2_P_I_source_investigation': 'Unpublished independent work; no new theorem or obstruction certified.'}, indent=2) + '\n')
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.aux', '.out')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation178/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()):
        add(p)
for name in ('input.json', 'task.json', 'settings.json', 'freeze.json', 'mathematical-data-bindings.json', 'launch-record.json'):
    add(C / name)
for p in (R / 'prepare_original_P19_2_research168_20261006.py', R / 'launch_frozen_original_research168_20261006.py', G / 'push-receipt-continuation177.json', R / 'record_verified177_20261006.py', Path(__file__)):
    add(p)
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
M.write_text(json.dumps({'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 63, 'commit_message': 'Launch remaining P19.2 research with complete fixed-start joint entropy grant', 'scope': 'Entire unchanged P19.2 original family and task, all complete R/T/C/S/E grants, byte-bound frozen native gpt-6.1-sol xhigh author input/settings and exact launch evidence. Public snapshots only for active167/168; no private active outputs, no new mathematical acceptance or original closure. Preserve open P16.4 editor.'}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(files), 'active_batch': [x['round'] for x in active], 'original_closed': False}, indent=2))
