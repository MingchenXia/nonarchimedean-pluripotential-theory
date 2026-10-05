"""Freeze completed round60, launched61, primary reads and unreviewed repair proposals."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation70-publication-records'
reads = R / 'root-checks/continuation70-primary-local-BT-and-filtration-reads'
assert not D.exists() and not reads.exists()
receipt = json.loads((G / 'push-receipt-continuation69.json').read_text())
assert receipt['commit_sha'] == 'c31d537dae2a7e89d226a9ebf474f021f48bfee5'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
D.mkdir()
reads.mkdir()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
sources = {
    'BJ1801v4': R / 'shared-sources/P16-arxiv-1801.08229-20261004.txt',
    'CLD1204v2': R / 'shared-sources/new-primary-1204.6277v2-20261004-continuation64.txt',
    'ThuillierHALv1': R / 'shared-sources/Thuillier-tel-00010990v1.txt',
    'Wanner1801v3': R / 'shared-sources/Wanner-1801.04713v3-20261004.txt',
    'Wu2609v1': R / 'shared-sources/new-primary-2609.27610v1-20261004.txt',
    'BJ1805v1': R / 'shared-sources/new-primary-1805.11160v1-20261004-continuation64.txt',
    'Reboulet2004v1': R / 'shared-sources/Reboulet-2004.11635v1-20261005-continuation70.txt'
}
units = []
for version, label, first, last, scope in [
    ('BJ1801v4', 'BJ-smooth-generated-psh-and-model-nef', 2453, 2479, 'Actual4.19 smooth scope; not a singular converse.'),
    ('BJ1801v4', 'BJ-divisorial-models-and-flag-ideals', 861, 943, 'Actual divisorial valuations and whole2.12 statement; relative integral closure retained.'),
    ('BJ1801v4', 'BJ-flag-ideal-realization-proof', 1051, 1110, 'Actual2.12 proof of divisorial realization by a flag-ideal determination.'),
    ('BJ1801v4', 'BJ-ample-model-on-chosen-test-configuration', 1411, 1468, 'Whole2.33 ample-model construction; proposed positive model atom needs exact weights.'),
    ('BJ1801v4', 'BJ-outer-energy-and-obstacle-volume-approximation', 4818, 4966, 'Actual8.5--8.8 chain; E-downarrow differentiation separate from envelope equality; corrected Lipschitz squeeze.'),
    ('BJ1801v4', 'BJ-divisorial-finite-energy-and-growth-topology', 5771, 5915, 'Finite dual energy and divisorial growth; not a Dirac-equation theorem.'),
    ('CLD1204v2', 'CLD-strict-integer-PL-residual-nef', 25535, 25644, 'Whole17.8.4 strict integer PL residual-nef proof and metric definitions.'),
    ('CLD1204v2', 'CLD-curvature-and-proper-curve-mass', 25721, 25880, 'Actual18.1 curvature/curve mass proof; higher general local BT not inferred.'),
    ('CLD1204v2', 'CLD-approachability-and-printed-integer-PL-converse', 27926, 28076, 'Whole18.8.4/6/8 and its actual printed integer PL scope; strictness gate disclosed.'),
    ('CLD1204v2', 'CLD-continuous-BT-and-uniform-only-continuity', 10414, 10538, 'Whole8.7.1--5;8.7.2 requires locally uniform convergence, not decreasing bounded limits.'),
    ('ThuillierHALv1', 'Thuillier-unit-logarithms-and-skeletal-Laplacian', 2897, 2974, 'Whole2.2.24 unit-logarithm Poincare-Lelong proof on smooth nontrivial curves.'),
    ('ThuillierHALv1', 'Thuillier-harmonic-units-and-local-point-types', 3576, 3615, 'Whole2.3.20 and start2.3.21; the whole latter proof is not claimed read.'),
    ('Wanner1801v3', 'Wanner-positive-local-current-criterion', 825, 928, 'Whole4.2/4.3 proof,4.4 start only; actual smooth proper compactification scope.'),
    ('Wu2609v1', 'Wu-bounded-negative-floor-and-divisorial-determination', 1035, 1117, 'Actual3.28/3.29; proposed common reference/scalar repair remains unreviewed.'),
    ('Wu2609v1', 'Wu-mass-comparison-domination-and-globalization', 1395, 1576, 'Full chain read for diagnosis; no circular regularization or singular envelope result accepted.'),
    ('BJ1805v1', 'BJ-asymptotic-FS-and-external-lattice-gate', 1086, 1420, 'Whole4.13/4.15; standing smooth scope and external lattice saturation cannot be ignored.'),
    ('Reboulet2004v1', 'Reboulet-actual-title-scope-and-separate-envelope-hypothesis', 1, 307, 'Geometrically integral projective scope; introduction asymptotic-envelope claims add EP.'),
    ('Reboulet2004v1', 'Reboulet-regular-point-valuation-and-Chebyshev-functions', 1291, 1421, 'Regular rational point, one-dimensional leaves, linear growth and field scope.'),
    ('Reboulet2004v1', 'Reboulet-lattice-Fujita-and-volume-approximation', 1421, 1720, 'Whole4.3.1/4.3.2/4.5.3 and most4.5.4 proof; printed normalization/monotonicity slips retained.'),
    ('Reboulet2004v1', 'Reboulet-FS-energy-approximation-proof-and-field-passage', 1721, 1890, 'Whole4.5.4 end and5.1.1 proof; no use of printed decreasing direction or omitted factorial.')
]:
    src = sources[version]
    literal = '\n'.join(src.read_bytes().decode('utf-8').split('\n')[first-1:last])
    p = reads / (label + '.txt')
    p.write_text(literal)
    assert p.read_bytes().decode('utf-8') == literal
    units.append({'id': label, 'source': str(src), 'source_sha256': sha(src), 'version': version,
                  'one_based_inclusive_LF_range': [first, last], 'literal_file': str(p),
                  'literal_sha256': sha(p), 'selected_body_root_read': True,
                  'whole_primary_body_root_read': False, 'scope_and_limits': scope})
write(reads / 'source-read-record.json', {'recorded_utc': now,
    'line_convention': 'UTF-8 bytes decode and split("\\n"), inclusive LF range',
    'units': units, 'mathematical_applications_independently_reviewed': False})
items = []
for atom, roundno, stem, role, db, session in [
    ('P13.1', 60, 'P13.1-public-source-relative-volume-and-uniform-Reeb-energy', 'completed partial author', 'campaign.sqlite', 76327),
    ('P13.2', 51, 'P13.2-public-source-fixed-Reeb-mathematical-review-v3', 'mathematical partial review', 'review.sqlite', 21616),
    ('P16.1', 61, 'P16.1-public-source-calibrated-local-BT-and-unibranch-equation', 'author', 'campaign.sqlite', 38834)
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
active = [i for i in items if i['observed_status'] == 'running']
assert len(active) <= 2 and items[0]['observed_status'] == 'completed'
obs = D / 'current-small-batch-observation.json'
write(obs, {'recorded_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
            'reasoning': 'xhigh', 'items': items, 'hot_feedback_sent': False})
completed60 = {'candidate': False, 'fully_solved_original_atom': False,
    'reader': str(R / 'root-checks/public-P13.1-round-60-final-reader'),
    'whole_argument_and_four_canonical_notes_root_read': True, 'literal_bindings_reproduced': 64,
    'all_selected_literal_bodies_root_read': False, 'independent_review': 'NOT_LAUNCHED',
    'state': 'COMPLETED partial: signed genuine energy/root comparison, bounded obstacle continuity and relative-volume remainder. Singular-quotient obstacle-volume approximation remains unproved.'}
a = json.loads((R / 'active-work.json').read_text())
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42 and sum(len(t['reviewed_papers']) for t in c['targets']) == 40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
proposals = sorted((R / 'root-checks').glob('*-20261005-continuation70.md'))
assert len(proposals) == 4
a['updated_utc'] = now
a['selected_atoms'] = [i['atom'] for i in active]
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint70: completed partial60, launched61, new primary and unreviewed local-BT/filtration repair proposals. No new original closure.'
a['current_small_batch'] = {'recorded_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
    'reasoning': 'xhigh', 'active_items': active,
    'completed_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'hot_feedback_sent': False}
a['prepared_P13.1_round60']['state'] = completed60['state']
a['P13.1_round60_author_completion'] = completed60
a['prepared_P16.1_round61'] = items[2]
a['P13.2_round51_mathematical_review_v3'] = items[1]
a['continuation70_unreviewed_root_proposals'] = {'paths': [str(p) for p in proposals],
    'source_read_record': str(reads / 'source-read-record.json'), 'independently_reviewed': False,
    'new_originals_solved': []}
c['updated_utc'] = now
c['latest_verified_github_checkpoint'] = receipt
c['active_atoms'] = [i['atom'] for i in active]
c['current_small_batch_launch'] = str(obs)
c['current_small_batch_launch_sha256'] = sha(obs)
for t in c['targets']:
    if t['id'] == 'P13.1': t['current_focus'] = completed60['state'] + ' New unreviewed extended-semigroup route targets the exact remaining gate; no new campaign launched.'
    if t['id'] == 'P16.1': t['current_focus'] = 'Exact-original round61 author launched: calibrated local positivity, common bounded BT representation, model-atom domination and unibranch envelope/equation reconstruction.'
write(R / 'active-work.json', a)
write(R / 'checklist-current.json', c)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file()
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation70/' + str(p.relative_to(R)),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})
for directory in [D, reads, R / 'root-checks/public-P13.1-round-60-final-reader']:
    for p in sorted(directory.rglob('*')):
        if p.is_file(): add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
C61 = R / 'campaigns/round-61/P16.1-public-source-calibrated-local-BT-and-unibranch-equation'
for name in ['input.json', 'settings.json', 'input-manifest.json']: add(C61 / name)
meta = R / 'shared-sources/Reboulet-primary-cache-20261005-continuation70.json'
s = json.loads(meta.read_text())
for path_key, hash_key in [('pdf', 'pdf_sha256'), ('literal_extract', 'extract_sha256'), ('html', 'html_sha256')]:
    assert sha(s[path_key]) == s[hash_key]
    add(s[path_key])
for p in proposals + [meta,
    R / 'shared-sources/Reboulet-asymptotic-FS-search-20261005-continuation70.html',
    R / 'prepare_public_P16_1_calibrated_local_BT_repair_20261005.py',
    R / 'prepare_continuation70_completed_P13_1_reader_20261005.py',
    R / 'root-checks/P13.1-round60-actual-result-20261005.json',
    G / 'push-receipt-continuation69.json', G / 'prepare_checkpoint_continuation70.py']: add(p)
assert len({f['path'] for f in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 40, 'current_native_batch': active,
    'commit_message': 'Preserve signed cone energy partial and reconstruct local BT and obstacle approximation',
    'scope': 'Completed unreviewed partial60 exact reader; launched61; twenty selected primary read units; exact Rebouletv1 public source and four unreviewed root proposals. No accepted original closure; no private transcripts, SQL, authentication, Git databases or book-source edits.'}
p = G / 'upload-manifest-continuation70.json'
assert not p.exists()
write(p, payload)
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files),
                  'statuses': [(i['atom'], i['observed_status']) for i in items],
                  'fully_solved_originals': 3}, indent=2))
