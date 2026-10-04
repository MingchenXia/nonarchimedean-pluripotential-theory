from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest = R / 'public-P16-equation-batch-manifest-20261004.json'
assert sha(manifest) == 'c9c87c2b1998ba9e02b15c803fc1888496660dbfc9471face75726f4f59bb451'
prepared = json.loads(manifest.read_text())
records = []
for c0, session, worker in zip(prepared['campaigns'], [66035, 47682], ['codex-ZDgZTo', 'codex-cC7tVd']):
    c = dict(c0)
    d = Path(c['directory'])
    assert sha(d / 'input.json') == c['input_sha256']
    assert sha(d / 'settings.json') == c['settings_sha256']
    native_input = d / 'artifacts' / worker / 'input.json'
    assert json.loads(native_input.read_text()) == json.loads((d / 'input.json').read_text())
    assert (d / 'run.json').exists() and (d / 'run.stderr').exists()
    c.update(tool_session_id=session, native_worker=worker,
        native_input=str(native_input), native_input_sha256=sha(native_input),
        input_binding='Native reserialization is semantically equal to the frozen campaign input; byte equality is not asserted.',
        state='Native author launched on original problem and ten public source pointers only; no result or acceptance yet.')
    records.append(c)
stamp = datetime.now(timezone.utc).isoformat()
launch = R / 'public-P16-equation-batch-launch-20261004.json'
assert not launch.exists()
data = {'launched_utc': stamp, 'preparation_manifest': str(manifest),
    'preparation_manifest_sha256': sha(manifest), 'selected_atoms': ['P16.1', 'P16.4'],
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
    'fully_solved_original_atoms': [], 'campaigns': records,
    'blocked_generated_export_attempted': False, 'hot_feedback_sent': False}
launch.write_text(json.dumps(data, indent=2) + '\n')
active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
assert len(active['full_solutions']) == 0
active['updated_utc'] = stamp
active['selected_atoms'] = ['P16.1', 'P16.4']
active['batch_manifest'] = str(manifest)
active['current_public_P16_equation_batch'] = {**data, 'launch_record': str(launch), 'launch_record_sha256': sha(launch)}
active['goal_state'] = 'ACTIVE. All 42 original targets remain open. Two native original/public-source authors are running on P16.1/P16.4. R43/R44 final proofs, actual canonical notes and papers were read and freshly reproduced; exact reviews remain prepared locally only. Four earlier rejected exports remain pending specific approval; none retried.'
active['next_work'] = 'Observe the current two authors without hot feedback; continue local mathematical reconstruction and paper preparation. Preserve regular local checkpoints; retry no rejected review or GitHub export without its pending specific approval.'
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')
check_path = R / 'checklist-current.json'
check = json.loads(check_path.read_text())
assert check['fully_solved_original_atoms'] == [] and len(check['targets']) == 42
assert all(t['closure'] == 'open' for t in check['targets'])
check['updated_utc'] = stamp
check['active_atoms'] = ['P16.1', 'P16.4']
check['current_batch_launch_record'] = str(launch)
for t in check['targets']:
    if t['id'] in ('P16.1', 'P16.4'):
        t['research_status'] = 'active'
        n = 45 if t['id'] == 'P16.1' else 46
        t['current_focus'] = f'Fresh native Xean gpt-6.1-sol/xhigh author in round {n}, with the complete original equation-family dossier and ten public primary-source pointers only. No generated preceding mathematical payload, result, independent acceptance or original closure.'
check_path.write_text(json.dumps(check, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'launch_record': str(launch), 'sha256': sha(launch),
    'workers': [c['native_worker'] for c in records], 'sessions': [66035, 47682], 'original_atoms_closed': 0}, indent=2))
