from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
K = R / 'root-checks'
M = G / 'upload-manifest-continuation179.json'
F = G / 'continuation179-publication-records'
S = K / 'small-batch167-168-public-status-20261006-continuation179'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(M) == 'a2f998d77de5e6e58e6c76f5e54c8c350762bf8ff8cdc9165e585338d32ad107'
assert not (G / 'push-receipt-continuation179.json').exists()
old = M.read_bytes()
(G / 'upload-manifest-continuation179-prelaunch-draft-LOCALONLY.json').write_bytes(old)
now = datetime.now(timezone.utc).isoformat()
C = next((R / 'campaigns/round-169').iterdir())
launch = json.loads((C / 'launch-record.json').read_text())
freeze = json.loads((C / 'freeze.json').read_text())
assert launch['frozen_math_input_sha256'] == freeze['argument_sha256'] == '272f11ecb330f421a1fe516d1efdaeec84dcd1776838771c1610fad79a53723d'
items = []
for n, atom in [(167, 'P16.5'), (168, 'P19.2'), (169, 'P19.2')]:
    c = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'
    p.write_text(json.dumps(st, indent=2) + '\n')
    items.append({'round': n, 'atom': atom, 'directory': str(c), 'observed_status': st['status'], 'observed_utc': st['observedAt'], 'public_status': str(p), 'public_status_sha256': sha(p), 'unsettled_calls': st['calls']['unsettled'], 'private_active_output_read': False, 'hot_feedback_sent': False, 'original_closed': False})
assert next(x for x in items if x['round'] == 168)['observed_status'] == 'completed'
active = [x for x in items if x['unsettled_calls'] > 0]
assert len(active) <= 2
focus = '167 whole corrected P16.5 proof audit and169 whole original P19.2 counterexample audit.168 author research completed; complete canonical output reading and acceptance remain separate.211 whole8-page counterexample/source/PDF/primary reading ledger frozen and169 launched with only complete R grant. No review feedback or active private stream reads.'
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': focus}
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, current_small_batch=batch, P19_2_launched_transcendental_full_original_review169=launch, github_pending_checkpoint='continuation179 final frozen', goal_state='8/42 originals independently accepted;34 open;63 supporting papers. ' + focus + ' No new mathematical acceptance or original closure. Source211 and entire169 argument unchanged after168 completion. Existing P16.4 editor preserved.')
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    shutil.copyfile(p, F / name)
rows = (R / 'checklist-current.tsv').read_text().splitlines()
for i, row in enumerate(rows):
    cells = row.split('\t')
    if cells[0] == 'P19.2':
        cells[2] = '168 author research completed;169 whole-original review of ROOT8-page transcendental P-profile obstruction active with R only. Exact original scope judgment pending. Original open;8/42,63 supports.'
    rows[i] = '\t'.join(cells)
(R / 'checklist-current.tsv').write_text('\n'.join(rows) + '\n')
shutil.copyfile(R / 'checklist-current.tsv', F / 'checklist-current.tsv')
observation = {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_supporting_papers': 63, 'active_batch': [x['round'] for x in active], 'original_closed': False, 'no_hot_feedback': True, 'existing_editor_unchanged': True, 'review169_launched': True, 'research168_completed': True, 'mathematical_input169_unchanged_after168_completion': True, 'root211_full_manuscript_verified_for_compile_and_reading_only': True}
(F / 'scope-observation.json').write_text(json.dumps(observation, indent=2) + '\n')
binding = {'finalized_utc': now, 'prior_prelaunch_manifest_sha256': hashlib.sha256(old).hexdigest(), 'reason': 'Author168 settled during checkpoint preparation; update final unpublished front/status records and add fresh169 launch evidence before remote publication.', 'active_batch': [x['round'] for x in active], 'whole_original_review_argument169_sha256': sha(C / 'argument.md'), 'mathematical_inputs_changed': False, 'original_closed': False}
B = F / 'checkpoint-finalization-binding.json'
B.write_text(json.dumps(binding, indent=2) + '\n')
j = json.loads(old)
for p in (S / 'round169-public-native-status.json', C / 'launch-record.json', B, Path(__file__)):
    j['files'].append({'local': str(p), 'path': 'research-checkpoints/continuation179/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for f in j['files']:
    f.update(bytes=Path(f['local']).stat().st_size, sha256=sha(f['local']))
j.update(generated_utc=now, file_count=len(j['files']))
j['scope'] = j['scope'].replace('prepared only, not launched.', 'launched only after public168 completion, with identical frozen input and no168 output supplied.').replace('Public snapshots only for active167/168;', 'Public snapshots for167/168/169;168 completed and169 active;')
M.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(j['files']), 'active_batch': [x['round'] for x in active]}, indent=2))
