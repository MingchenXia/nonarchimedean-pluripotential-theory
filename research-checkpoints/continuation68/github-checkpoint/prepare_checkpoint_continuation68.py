"""Freeze completed partial work, two proposals and exact native campaign state."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation68-publication-records'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt = json.loads((G / 'push-receipt-continuation67.json').read_text())
assert receipt['commit_sha'] == '5f6e25a20f6ed55b6ec147d9ae8213e65e89dba0'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
D.mkdir(exist_ok=False)
now = datetime.now(timezone.utc).isoformat()
reads = R / 'root-checks/continuation68-primary-model-energy-and-operator-reads'
reads.mkdir(exist_ok=False)
sources = json.loads((R / 'campaigns/round-55/P13.1-public-source-expanded-signed-energy-uniform-Reeb-differentiation/input-manifest.json').read_text())['public_sources']
source_by_version = {s['saved_version']: s for s in sources}
units = []
for version, label, first, last, limit in [
    ('1801.08229v4', 'BJ-model-PL-vector-lattice', 943, 1004, 'Selected algebraic PL and flag-ideal definitions; whole article not read.'),
    ('1801.08229v4', 'BJ-actual-basepoint-free-FS-definitions', 1158, 1212, 'Exact generator/basepoint convention; whole article not read.'),
    ('1801.08229v4', 'BJ-uniform-outer-energy-differentiation', 4841, 4966, 'Complete differentiation statements and local proof chain8.7/8.8, with explicit imported volume results still to verify.'),
    ('2406.13684v1', 'Wu-genuine-energy-and-mixed-operator', 930, 1144, 'Actual definitions5.9/6.1, energy properties and entire6.3 proof; printed index/J slips require mathematical correction.'),
    ('1504.06568v3', 'BHJ-finite-filtration-and-Rees-definition', 365, 425, 'Finite signed norms and Rees finite-generation definition.'),
    ('1504.06568v3', 'BHJ-actual-test-configuration-correspondence', 945, 997, 'Entire Proposition2.15 proof plus adjacent filtration statements.'),
    ('1504.06568v3', 'BHJ-model-metric-operations', 2141, 2175, 'Model metric definition, differences, pullback and initial scaling convention.'),
    ('1504.06568v3', 'BHJ-intersections-and-actual-integral-normalization', 2260, 2313, 'Intersection pairing6.11/6.12, projection degree and Hodge inequality proof.'),
    ('1504.06568v3', 'BHJ-actual-intersection-energy', 2372, 2435, 'Actual definitions7.1/7.2, DH mean, telescoping energy and printed extra-volume convention.'),
]:
    s = source_by_version[version]
    source = Path(s['literal_extract'])
    assert sha(source) == s['extract_sha256'] and sha(s['pdf']) == s['pdf_sha256']
    p = reads / (label + '.txt')
    p.write_text('\n'.join(source.read_bytes().decode('utf-8').split('\n')[first - 1:last]))
    units.append({'id': label, 'source': str(source), 'source_version': version,
                  'source_sha256': sha(source), 'LF_one_based_inclusive': [first, last],
                  'extract': str(p), 'extract_sha256': sha(p),
                  'exact_selected_body_root_read': True, 'whole_primary_body_root_read': False,
                  'scope_and_limits': limit})
(reads / 'source-read-record.json').write_text(json.dumps({'recorded_utc': now,
    'line_convention': 'UTF-8 bytes decode and split("\\n"), inclusive one-based LF',
    'units': units, 'new_mathematical_claims_independently_reviewed': False}, ensure_ascii=False, indent=2) + '\n')
items = []
for atom, roundno, stem, role, db, session in [
    ('P13.1', 55, 'P13.1-public-source-expanded-signed-energy-uniform-Reeb-differentiation', 'completed author', 'campaign.sqlite', 92187),
    ('P16.1', 58, 'P16.1-public-source-algebraic-collar-trace-and-unibranch-equation', 'author', 'campaign.sqlite', 60905),
    ('P13.2', 51, 'P13.2-public-source-fixed-Reeb-image-review-v2', 'correctness review', 'review.sqlite', 3702),
]:
    directory = R / 'campaigns' / ('round-' + str(roundno)) / stem
    proc = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(directory / db)], cwd='/workspace/xean', capture_output=True, text=True, check=True)
    p = D / (atom + '-native-status.json')
    p.write_text(proc.stdout)
    items.append({'atom': atom, 'round': roundno, 'role': role, 'directory': str(directory),
                  'tool_session_id': session, 'observed_status': json.loads(proc.stdout)['status'],
                  'status': str(p), 'status_sha256': sha(p),
                  'settings_sha256': sha(directory / 'settings.json'), 'accepted': False})
assert items[0]['observed_status'] == 'completed'
active = [i for i in items[1:] if i['observed_status'] == 'running']
assert len(active) <= 2
C59 = R / 'campaigns/round-59/P13.1-public-source-signed-cone-energy-and-uniform-outer-differentiation'
m59 = json.loads((C59 / 'input-manifest.json').read_text())
assert not (C59 / 'campaign.sqlite').exists()
for C in [R / 'campaigns/round-58/P16.1-public-source-algebraic-collar-trace-and-unibranch-equation', C59]:
    m = json.loads((C / 'input-manifest.json').read_text())
    assert sha(C / 'input.json') == m['input_sha256'] and sha(C / 'settings.json') == m['settings_sha256']
    inp = json.loads((C / 'input.json').read_text())
    assert inp['notes'] == []
    for context in m['embedded_context']:
        assert sha(context['path']) == context['sha256'] and not context['accepted_dependency']
        assert Path(context['path']).read_text() in inp['assignment']
obs = D / 'current-small-batch-observation.json'
obs.write_text(json.dumps({'recorded_utc': now, 'route': 'Xean native Codex',
    'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'items': items,
    'next_prepared_round': 59, 'next_task_launched': False, 'hot_feedback_sent': False}, indent=2) + '\n')
prepared = {'round': 59, 'atom': 'P13.1', 'directory': str(C59),
    'input_sha256': m59['input_sha256'], 'settings_sha256': m59['settings_sha256'],
    'original_task_unchanged': True, 'notes_imported': [], 'source_count': 8,
    'embedded_diagnostic_bodies': 5, 'saved_assignment_prefix_and_settings_root_read': True,
    'embedded_whole_bodies_already_root_read_and_byte_reproduced': True,
    'state': 'PREPARED LOCAL ONLY; not launched. Await a free slot in the native two-item batch.',
    'fully_solved_original_atom': False}
(D / 'round59-preparation-and-binding.json').write_text(json.dumps(prepared, indent=2) + '\n')
a = json.loads((R / 'active-work.json').read_text())
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42 and sum(len(t['reviewed_papers']) for t in c['targets']) == 40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
a['updated_utc'] = now
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint68: completed unreviewed P13.1 partial paper and whole reader, two new unreviewed algebraic collar/outer-energy proposals, launched round58 and prepared round59. No new original closure.'
a['prepared_P13.1_round59'] = prepared
a['current_small_batch'] = {'recorded_utc': now, 'route': 'Xean native Codex',
    'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'active_items': active,
    'completed_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'hot_feedback_sent': False}
a['continuation68_unreviewed_root_proposals'] = {'paths': [str(p) for p in sorted((R / 'root-checks').glob('*-20261005-continuation68.md'))],
    'source_read_record': str(reads / 'source-read-record.json'), 'independently_reviewed': False, 'new_originals_solved': []}
c['updated_utc'] = now
c['latest_verified_github_checkpoint'] = receipt
c['active_atoms'] = [i['atom'] for i in active]
c['current_small_batch_launch'] = str(obs)
c['current_small_batch_launch_sha256'] = sha(obs)
for t in c['targets']:
    if t['id'] == 'P13.1':
        t['current_focus'] = 'Round55 completed partial, whole argument/TeX/four notes read and two local builds pass; new signed cone energy and uniform outer-extension repair round59 prepared, not launched. Original remains open.'
    if t['id'] == 'P16.1':
        t['current_focus'] = 'Exact-domain round58 author active; explicit algebraic collar formula, direct affine FS/determinant trace and curve boundary proposals remain unreviewed. Original remains open.'
(R / 'active-work.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
(R / 'checklist-current.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file()
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation68/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for directory in [D, reads, R / 'root-checks/public-P13.1-round-55-final-reader', R / 'root-checks/P13.1-round55-reader-followup-continuation68']:
    for p in sorted(directory.rglob('*')):
        if p.is_file():
            add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
for C in [R / 'campaigns/round-58/P16.1-public-source-algebraic-collar-trace-and-unibranch-equation', C59]:
    for name in ['input.json', 'settings.json', 'input-manifest.json']:
        add(C / name)
for p in sorted((R / 'root-checks').glob('*-20261005-continuation68.md')):
    add(p)
for p in [R / 'prepare_public_P16_1_algebraic_collar_repair_20261005.py',
          R / 'prepare_public_P13_1_outer_energy_repair_20261005.py',
          R / 'prepare_public_P13_1_round55_reader_20261005.py',
          R / 'root-checks/P13.1-round55-actual-result-20261005.json',
          G / 'push-receipt-continuation67.json', G / 'prepare_checkpoint_continuation68.py']:
    add(p)
assert len({f['path'] for f in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 40, 'current_native_batch': active,
    'commit_message': 'Preserve signed Reeb partial paper and develop uniform outer-energy reconstruction',
    'scope': 'Unreviewed completed partial and whole reader; two root proof proposals; nine literal primary units; exact round58 author active and round59 repair unlaunched. No new accepted paper/original closure, private transcripts, SQL, credentials, Git databases or book-source changes.'}
p = G / 'upload-manifest-continuation68.json'
assert not p.exists()
p.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files),
    'originals_solved': 3, 'reviewed_scoped_papers': 40,
    'statuses': [(x['atom'], x['observed_status']) for x in items]}, indent=2))
