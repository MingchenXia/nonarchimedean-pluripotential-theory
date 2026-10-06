from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation179.json'
assert not M.exists()
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
prior = json.loads((G / 'push-receipt-continuation178.json').read_text())
assert prior['commit_sha'] == '3b692621da324c500b150c0eaaccbabafcb29870'
assert all(prior[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
C = next((R / 'campaigns/round-169').iterdir())
D = K / 'public-P19.2-continuation211-transcendental-obstruction-reader'
T = K / 'P19.2-transcendental-P-profile-model-obstruction-candidate-20261006-continuation211.tex'
publication = json.loads((D / 'publication-binding.json').read_text())
assert publication['pages'] == 8 and publication['native_final_compile'] == 'SUCCESS' and publication['all8final_visual_pages_root_read']
assert sha(T) == publication['tex_sha256'] and sha(D / 'paper.pdf') == publication['pdf_sha256']
freeze = json.loads((C / 'freeze.json').read_text())
assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
assert freeze['argument_sha256'] == '272f11ecb330f421a1fe516d1efdaeec84dcd1776838771c1610fad79a53723d'
for name, key in [('argument.md', 'argument_sha256'), ('task.json', 'task_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == freeze[key]
S = K / 'small-batch167-168-public-status-20261006-continuation179'
F = G / 'continuation179-publication-records'
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
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': '167 whole corrected P16.5 proof review;168 entire residual P19.2 author research with complete accepted R/T/C/S/E bodies. No new mathematical acceptance. Independent ROOT8-page211 proposes a nonprojective actual weak-ray obstruction for finer dS P profiles; prepared fresh169 whole-original audit remains unlaunched while167168active.'}
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, current_small_batch=batch, P19_2_transcendental_original_counterexample211=publication, prepared_transcendental_full_original_review169=freeze, github_pending_checkpoint='continuation179 frozen', goal_state='8/42 original problems independently accepted;34 open;63 accepted supporting papers. Fresh167 reviews all18 corrected P16.5 pages with G0/G1 only.168 researches unchanged entire residual P19.2 using complete grants R/T/C/S/E, retaining arbitrary weak rays, prescribed starts, finer closed P data and entropy/energy. ROOT8-page211 compiled and all8pages read; its new P/I closure, genuine transcendental product, actual bounded ray and all-model profile obstruction remain unreviewed. Prepared169 whole-original audit frozen and unlaunched. No private active stream reads, no hot feedback, no new original closure.158 settled connection failure without verdict;166 old whole original FAIL preserved.')
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
rows = (R / 'checklist-current.tsv').read_text().splitlines()
for i, row in enumerate(rows):
    cells = row.split('\t')
    if cells[0] == 'P19.2':
        cells[2] = 'Native168 original research active; independent ROOT8page211 proposes transcendental all-model positive-P profile obstruction. Fresh169 whole-original audit frozen/unlaunched pending free slot. Original open;8/42,63 supports.'
    rows[i] = '\t'.join(cells)
(R / 'checklist-current.tsv').write_text('\n'.join(rows) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    shutil.copyfile(R / name, F / name)
(F / 'scope-observation.json').write_text(json.dumps({'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_supporting_papers': 63, 'active_batch': [x['round'] for x in active], 'original_closed': False, 'no_hot_feedback': True, 'existing_editor_unchanged': True, 'ROOT_P19_2_P_I_source_investigation': 'Whole8-page211 source/PDF/primary application record frozen, native compile and all8 visual pages checked; proposed counterexample not certified.169 full-original audit prepared only.'}, indent=2) + '\n')
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.aux', '.out')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation179/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()):
        add(p)
for name in ('argument.md', 'task.json', 'settings.json', 'freeze.json', 'mathematical-data-bindings.json', 'original-task.json'):
    add(C / name)
for p in (T, D / 'paper.pdf', D / 'publication-binding.json', D / 'source-application-register.json', D / 'README.md', R / 'prepare_transcendental_obstruction211_review169_20261006.py', R / 'launch_frozen_transcendental_original_review169_20261006.py', G / 'push-receipt-continuation178.json', R / 'record_verified178_20261006.py', Path(__file__)):
    add(p)
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
M.write_text(json.dumps({'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 63, 'commit_message': 'Preserve transcendental P19.2 finer-profile obstruction and freeze whole audit', 'scope': 'Unreviewed complete8-page211 actual nonprojective/transcendental P-profile obstruction candidate, all raw mixed masses, local Gauss/I-maximal comparison and lower-roof closedness. Frozen whole-original169 native gpt-6.1-sol xhigh review task/argument/settings includes unchanged original family and complete callerR; prepared only, not launched. Public snapshots only for active167/168; no private active outputs, no new mathematical acceptance or original closure. Preserve open P16.4 editor.'}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(files), 'active_batch': [x['round'] for x in active], 'original_closed': False}, indent=2))
