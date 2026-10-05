from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

R = Path('/workspace/research'); G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt = json.loads((G / 'push-receipt-continuation119.json').read_text())
assert receipt['commit_sha'] == '74e2817bd0424ec2388e406cd345819ca8b11902'
assert receipt['parent_sha'] == '2eb53b52095157d9876068cdd4a5297aac863a11'
assert sha(G / 'upload-manifest-continuation119.json') == receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
K = R / 'root-checks/current-small-batch116-117-20261005'
assert not K.exists(); K.mkdir()
items = []
for no, atom, stem, session in [
    (116, 'P16.3', 'P16.3-original-full-residue-characteristic-reconstruction', 39792),
    (117, 'P16.5', 'P16.5-original-general-reference-and-pseudoeffective-research', 91517)]:
    C = R / f'campaigns/round-{no}' / stem
    out = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')],
                         cwd='/workspace/xean', capture_output=True, text=True, check=True)
    status = json.loads(out.stdout)
    assert status['calls']['admitted'] == 1
    p = K / f'{atom}-round{no}-public-native-status.json'; p.write_text(out.stdout)
    items.append({'round': no, 'atom': atom, 'directory': str(C), 'tool_session_id': session,
                  'observed_status': status['status'], 'public_status': str(p), 'public_status_sha256': sha(p),
                  'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False})
now = datetime.now(timezone.utc).isoformat()
batch = {'recorded_utc': now, 'items': items,
         'active_items': [i for i in items if i['observed_status'] == 'running'],
         'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
         'focus': 'Full original P16.3 and residual full original P16.5, two research tasks at a time. Completed114 canonical INCONCLUSIVE preserved.'}
(K / 'launch-and-public-status-record.json').write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n')
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; a = json.loads(p.read_text()); assert len(a['fully_solved_original_atoms']) == 7
    if name == 'checklist-current.json':
        assert a['historical_reviewed_scoped_papers'] == 44
        a['active_atoms'] = ['P16.3', 'P16.5']
    a['updated_utc'] = now
    a['github_checkpoint' if name == 'active-work.json' else 'latest_verified_github_checkpoint'] = receipt
    a['github_pending_checkpoint'] = None
    a['current_small_batch'] = batch
    C117 = R / 'campaigns/round-117/P16.5-original-general-reference-and-pseudoeffective-research'
    a['prepared_full_original_research117'] = {'directory': str(C117), 'freeze': str(C117 / 'freeze.json'),
        'status': items[1]['observed_status'], 'original_closed': False}
    a['prepared_full_original_research116']['status'] = items[0]['observed_status']
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_checkpoint': receipt['commit_sha'], 'batch': [(i['round'], i['atom'], i['observed_status']) for i in items],
                  'original_count_unchanged': 7, 'remaining_open_originals': 35}, indent=2))
