"""Freeze the ample-collar, Rossi and controlled-affine repair proposals."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation73-publication-records'
reads = R / 'root-checks/continuation73-primary-collar-and-regularization-reads'
assert not D.exists() and not reads.exists()
receipt = json.loads((G / 'push-receipt-continuation72.json').read_text())
assert receipt['commit_sha'] == 'a4f8146014a6d2b07756dfe5ce38a66721650800'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
D.mkdir()
reads.mkdir()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
sources = {
    'GR2503v1': R / 'shared-sources/GR2503.05513v1-20261005-continuation72.txt',
    'Wu2609v1': R / 'shared-sources/new-primary-2609.27610v1-20261004.txt',
    'BJ1801v4': R / 'shared-sources/P16-arxiv-1801.08229-20261004.txt'
}
units = []
for version, label, first, last, scope in [
    ('GR2503v1', 'GR-actual-strict-PL-definition', 230, 245, 'Actual2.5 strict G-local analytic-unit definition and model equivalence.'),
    ('GR2503v1', 'GR-residual-dimensional-analytic-lifting-proof', 489, 777, 'Whole4.1,4.3 and proof; residual dimensions, reduction of germs and finite multisections, with explicit external theorem hypotheses.'),
    ('Wu2609v1', 'Wu-rational-local-definitions-and-approximation', 639, 759, 'Actual rational default and finite affine convention; omitted contact constant repaired only in auxiliary class.'),
    ('Wu2609v1', 'Wu-affine-FS-generator-and-compactification-definitions', 763, 847, 'Actual generator/floor class and3.17/3.18; upper growth and controlled approximations still require their independent proof.'),
    ('Wu2609v1', 'Wu-bounded-collar-and-divisorial-application', 1035, 1115, 'Actual3.28/3.29; negative floor, scaling and global membership must be repaired.'),
    ('Wu2609v1', 'Wu-pole-damping-and-smooth-removable-extension', 1117, 1195, 'Whole3.30/3.31 proof; controlled3.25(2) antecedent and smooth EP remain visible.3.32 proof only begins.'),
    ('Wu2609v1', 'Wu-actual-Rossi-glued-function', 1696, 1728, 'Whole5.6 proof; compact perturbation FS bridge replaces the circular general regularization appeal if independently reconstructed.'),
    ('BJ1801v4', 'BJ-maximum-and-continuous-uniform-FS-density', 2341, 2442, 'Actual4.7 maximum stability and4.16 uniform density; decreasing-net regularization does not silently supply an unbounded sequence.'),
    ('BJ1801v4', 'BJ-EP-compactness-and-birational-onto-hypotheses', 2819, 2873, 'Whole5.11 and5.13: target-side classes with EP are required; smooth resolution alone does not give singular onto descent.')
]:
    src = sources[version]
    literal = '\n'.join(src.read_bytes().decode('utf-8').split('\n')[first-1:last])
    p = reads / (label + '.txt')
    p.write_text(literal)
    assert p.read_bytes().decode() == literal
    units.append({'id': label, 'source': str(src), 'source_sha256': sha(src), 'version': version,
        'one_based_inclusive_LF_range': [first, last], 'literal_file': str(p),
        'literal_sha256': sha(p), 'selected_body_root_read': True,
        'whole_primary_body_root_read': False, 'scope_and_limits': scope})
write(reads / 'source-read-record.json', {'recorded_utc': now,
    'line_convention': 'UTF-8 bytes decode and split("\\n"), inclusive LF range',
    'units': units, 'new_mathematical_applications_independently_reviewed': False})
items = []
for atom, roundno, stem, role, db, session in [
    ('P13.2', 51, 'P13.2-public-source-fixed-Reeb-mathematical-review-v3', 'mathematical partial review', 'review.sqlite', 21616),
    ('P13.1', 63, 'P13.1-public-source-eleven-body-semigroup-and-uniform-differentiation', 'author', 'campaign.sqlite', 73148)
]:
    C = R / 'campaigns' / ('round-' + str(roundno)) / stem
    proc = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / db)],
        cwd='/workspace/xean', capture_output=True, text=True, check=True)
    p = D / (atom + '-native-status.json')
    p.write_text(proc.stdout)
    items.append({'atom': atom, 'round': roundno, 'role': role, 'directory': str(C),
        'tool_session_id': session, 'observed_status': json.loads(proc.stdout)['status'],
        'status': str(p), 'status_sha256': sha(p), 'settings_sha256': sha(C / 'settings.json'),
        'accepted': False})
assert len([i for i in items if i['observed_status'] == 'running']) <= 2
write(D / 'current-small-batch-observation.json', {'recorded_utc': now, 'items': items,
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'hot_feedback_sent': False})
prepared = []
original = json.loads((R / 'campaigns/round-61/P16.1-public-source-calibrated-local-BT-and-unibranch-equation/input.json').read_text())['task']
for roundno, stem, bodies in [
    (65, 'P16.1-public-source-ample-collars-Rossi-and-unibranch-equation', 8),
    (66, 'P16.1-public-source-controlled-affine-Rossi-and-unibranch-equation', 9)
]:
    C = R / 'campaigns' / ('round-' + str(roundno)) / stem
    m = json.loads((C / 'input-manifest.json').read_text())
    assert sha(C / 'input.json') == m['input_sha256']
    assert sha(C / 'settings.json') == m['settings_sha256']
    assert not (C / 'campaign.sqlite').exists()
    data = json.loads((C / 'input.json').read_text())
    assert data['task'] == original and data['notes'] == []
    assert len(m['public_sources']) == 10 and len(m['embedded_context']) == bodies
    for s in m['public_sources']:
        assert sha(s['pdf']) == s['pdf_sha256']
        assert sha(s['literal_extract']) == s['extract_sha256']
    for b in m['embedded_context']:
        assert sha(b['path']) == b['sha256']
        assert Path(b['path']).read_text() in data['assignment']
    prepared.append({'round': roundno, 'directory': str(C), 'input_sha256': m['input_sha256'],
        'settings_sha256': m['settings_sha256'], 'source_count': 10,
        'embedded_context_count': bodies, 'launched': False})
write(D / 'prepared-P16.1-Rossi-and-controlled-input-bindings.json', {'recorded_utc': now,
    'items': prepared, 'round64_and_round65_preserved_unlaunched': True,
    'round66_saved_assignment_prefix_settings_original_criteria_and_new_proposal_root_read': True,
    'original_task_unchanged': True, 'independently_reviewed': False})
proposals = sorted((R / 'root-checks').glob('P16.1-*-20261005-continuation73.md'))
assert len(proposals) == 2
a = json.loads((R / 'active-work.json').read_text())
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42 and sum(len(t['reviewed_papers']) for t in c['targets']) == 40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
a['updated_utc'] = now
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint73: unreviewed ample collars, Rossi compact perturbation and controlled affine moving-truncation proposals; original closure unchanged.'
a['current_small_batch']['recorded_utc'] = now
a['current_small_batch']['active_items'] = [i for i in items if i['observed_status'] == 'running']
a['prepared_P16.1_round65'] = prepared[0]
a['prepared_P16.1_round66'] = prepared[1]
a['continuation73_unreviewed_root_proposals'] = {'paths': [str(p) for p in proposals],
    'source_read_record': str(reads / 'source-read-record.json'), 'independently_reviewed': False,
    'new_originals_solved': []}
c['updated_utc'] = now
c['latest_verified_github_checkpoint'] = receipt
c['current_small_batch'] = a['current_small_batch']
for t in c['targets']:
    if t['id'] == 'P16.1':
        t['current_focus'] = 'Completed unreviewed partial61; ten-source successor66 prepared locally with ample collar, direct Rossi FS bridge and controlled affine pole-damping reconstruction.64/65 retained unlaunched. Original singular EP and equation remain open.'
write(R / 'active-work.json', a)
write(R / 'checklist-current.json', c)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file()
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation73/' + str(p.relative_to(R)),
        'bytes': p.stat().st_size, 'sha256': sha(p)})
for directory in [D, reads]:
    for p in sorted(directory.rglob('*')):
        if p.is_file(): add(p)
for item in prepared:
    for name in ['input.json', 'settings.json', 'input-manifest.json']: add(Path(item['directory']) / name)
for p in proposals + [R / 'prepare_public_P16_1_Rossi_bridge_repair_20261005.py',
    R / 'prepare_public_P16_1_controlled_affine_repair_20261005.py',
    G / 'record_verified_checkpoint72.py', G / 'push-receipt-continuation72.json',
    G / 'prepare_checkpoint_continuation73.py']: add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({f['path'] for f in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 40, 'current_native_batch': items,
    'commit_message': 'Preserve ample collar and controlled affine Rossi proof repairs',
    'scope': 'Unlaunched65/66 frozen inputs and helpers, two unreviewed root proposals and nine literal primary read units. No new accepted original, private transcripts, SQL, auth, Git databases or book-source changes.'}
p = G / 'upload-manifest-continuation73.json'
assert not p.exists()
write(p, payload)
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files),
    'statuses': [(i['atom'], i['observed_status']) for i in items], 'fully_solved_originals': 3}, indent=2))
