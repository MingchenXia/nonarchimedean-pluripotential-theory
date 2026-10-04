from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest = R / 'public-smooth-regularization-batch-manifest-20261004.json'
assert sha(manifest) == '4bdca04487ae823401d4da87959c81313b9339fc6aca2c0d7f857840b2cd0ab2'
prepared = json.loads(manifest.read_text())
records = []
for campaign, session in zip(prepared['campaigns'], [81850, 2830]):
    c = dict(campaign)
    d = Path(c['directory'])
    assert sha(d / 'input.json') == c['input_sha256'] and sha(d / 'settings.json') == c['settings_sha256']
    assert (d / 'run.json').exists() and (d / 'run.stderr').exists()
    c.update(tool_session_id=session, state='Native author launched on original question and seven published-source pointers only; no result or acceptance yet.')
    records.append(c)
stamp = datetime.now(timezone.utc).isoformat()
launch = R / 'public-smooth-regularization-batch-launch-20261004.json'
assert not launch.exists()
data = {'launched_utc': stamp, 'preparation_manifest': str(manifest), 'preparation_manifest_sha256': sha(manifest),
        'selected_atoms': ['P02.3', 'P02.4'], 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
        'fully_solved_original_atoms': [], 'campaigns': records,
        'blocked_generated_export_attempted': False, 'hot_feedback_sent': False}
launch.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
active['updated_utc'] = stamp
active['selected_atoms'] = ['P02.3', 'P02.4']
active['batch_manifest'] = str(manifest)
active['current_public_smooth_regularization_batch'] = {**data, 'launch_record': str(launch), 'launch_record_sha256': sha(launch)}
for c in active['current_public_regularization_batch']['campaigns']:
    n = c['round']
    reader = R / 'root-checks' / f'public-regularization-round-{n}-final-reader'
    review = Path(c['directory']).with_name(Path(c['directory']).name + '-review')
    read = json.loads((reader / 'complete-root-read.json').read_text())
    assert read['all_actual_canonical_notes_all_fields_and_support_root_read']
    c.update(state='Completed, candidate=false; full final proof, all actual canonical notes, TeX and executed helpers read; fresh local reproduction succeeded. Scoped draft, original target still open.',
             root_read_record=str(reader / 'complete-root-read.json'), root_read_record_sha256=sha(reader / 'complete-root-read.json'),
             reproduction_result=str(reader / 'reproduction-result.json'), reproduction_result_sha256=sha(reader / 'reproduction-result.json'),
             independent_acceptance=False, review_state='Exact review prepared locally only; never submitted.',
             review_freeze=str(review / 'freeze.json'), review_freeze_sha256=sha(review / 'freeze.json'))
for c in active.get('research', []):
    if '/round-37/' in c.get('directory', ''):
        c['research_state'] = 'Completed scoped geometric draft, candidate=false; full proof/canonical notes/TeX read and locally reproduced. Original sharp target remains open.'
        c['review_state'] = 'Exact scoped review prepared locally only; never submitted.'
active['goal_state'] = 'ACTIVE. All 42 original targets remain open. Current small batch P02.3/P02.4 native authors launched. R41/R42 scoped final papers and canonical notes read and locally reproduced; exact reviews prepared locally only. R39 subsidiary stage-3 gap remains preserved. Four earlier automatically rejected exports await specific approval; none retried.'
active['next_work'] = 'Observe current authors without hot feedback; continue local requirements and proof checks. Preserve regular local checkpoints. Submit or push already blocked payloads only after their pending specific approvals arrive.'
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')
check_path = R / 'checklist-current.json'
check = json.loads(check_path.read_text())
assert check['fully_solved_original_atoms'] == [] and len(check['targets']) == 42
check['updated_utc'] = stamp
check['active_atoms'] = ['P02.3', 'P02.4']
check['current_batch_launch_record'] = str(launch)
for target in check['targets']:
    if target['id'] in ['P02.1', 'P02.2']:
        target['research_status'] = 'partial'
        target['current_focus'] = 'Completed native draft in round ' + str(41 if target['id'] == 'P02.1' else 42) + ': fixed-domain curve regularization and a saturated proper-fibre sector. Entire proof, actual canonical notes and standalone TeX read; fresh local build reproduced. P02.2 additionally gives a boundary sequence obstruction. Exact review prepared locally only, independent acceptance pending. Original sharp characterization remains open.'
    elif target['id'] in ['P02.3', 'P02.4']:
        target['research_status'] = 'active'
        target['current_focus'] = 'Fresh native Xean gpt-6.1-sol/xhigh author in round ' + str(43 if target['id'] == 'P02.3' else 44) + ', with original full regularization dossier and seven published-source pointers only. Seeks the actual requested weakly/ordinary smooth decreasing psh class for arbitrary original targets. No result or acceptance yet.'
check_path.write_text(json.dumps(check, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'launch_record': str(launch), 'sha256': sha(launch), 'sessions': [81850, 2830], 'original_atoms_closed': 0}, indent=2))
