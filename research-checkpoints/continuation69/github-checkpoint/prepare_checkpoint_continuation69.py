"""Freeze completed partial58, actual review51, relative-volume sources and native fronts."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation69-publication-records'
reads = R / 'root-checks/continuation69-primary-relative-volume-and-local-current-reads'
assert not D.exists() and not reads.exists()
receipt = json.loads((G / 'push-receipt-continuation68.json').read_text())
assert receipt['commit_sha'] == 'c14af1cec22d54b4165186a3b6c5e0c3a01a74bf'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
D.mkdir()
reads.mkdir()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
metadata = R / 'shared-sources/P13-relative-volume-primary-cache-20261005-continuation69.json'
sources = {s['saved_version']: s for s in json.loads(metadata.read_text())}
sources.update({
    '1801.04713v3': {'literal_extract': str(R / 'shared-sources/Wanner-1801.04713v3-20261004.txt')},
    '2609.27610v1': {'literal_extract': str(R / 'shared-sources/new-primary-2609.27610v1-20261004.txt')},
    '1204.6277v2': {'literal_extract': str(R / 'shared-sources/new-primary-1204.6277v2-20261004-continuation64.txt')}
})
units = []
for version, label, first, last, scope in [
    ('2004.03847v1', 'BGM-standing-general-scheme-and-differentiation', 1, 135, 'Complete non-Archimedean field including trivial, geometrically reduced projective scheme, ample line bundle.'),
    ('2004.03847v1', 'BGM-energy-volume-and-asymptotic-Riemann-Roch', 390, 631, 'Actual raw energy, determinant volume, whole Theorem2.4 proof; EP is separately introduced.'),
    ('2004.03847v1', 'BGM-uniform-two-sided-estimate-and-proof', 632, 850, 'Whole Lemma3.2 and Theorem3.1 proof, without EP; later envelope statements must not be confused with this scope.'),
    ('1805.01016v3', 'BE-actual-v3-title-and-standing-scope', 1, 65, 'Actual v3 title/header and general field scope; bibliography v2 title is not the retained version.'),
    ('1805.01016v3', 'BE-actual-psh-FS-and-nef-restriction', 2280, 2353, 'Definition7.2 and Corollary7.6; model-nef equivalence7.8 only over nontrivially valued fields.'),
    ('1805.01016v3', 'BE-graded-and-bounded-relative-volume-proof', 3329, 3481, 'Whole Theorem9.5 proof and bounded-metric existence9.8; not by itself an obstacle-energy equality.'),
    ('1805.01016v3', 'BE-continuous-psh-energy-equality-and-envelope-limit', 3590, 3677, 'Whole9.15 continuous-psh E=vol proof without EP;9.16 adds envelope assumptions.'),
    ('1801.04713v3', 'Wanner-lisse-slopes-harmonic-comparison', 198, 330, 'Exact skeletal/lisse Laplacian and positive-measure criterion; smooth nontrivially valued curve scope retained.'),
    ('1801.04713v3', 'Wanner-current-psh-definition', 502, 531, 'Continuous functions locally integrable, positive current definition; does not assert all current-psh are locally smooth-approachable.'),
    ('2609.27610v1', 'Wu-tropical-image-local-support-and-definitions', 639, 759, 'Actual local definitions; missing additive constant corrected in proposed arguments, not in the primary file.'),
    ('2609.27610v1', 'Wu-local-bounded-BT-and-overlap-proof', 1190, 1340, 'Actual mixed-measure chain and local/global reference/scaling obligations; printed winning-locus measure needs correction.'),
    ('1204.6277v2', 'CLD-harmonic-balancing-and-boundary-proof', 9511, 9729, 'Whole harmonic-chart balance and boundary-current proof, with calibrated facet slope relation.'),
    ('1204.6277v2', 'CLD-psh-approachability-ordinal-and-continuity', 9729, 9905, 'Actual CPsh/psh generated sheaf and approachability distinction; positive current alone is not the stated smooth-generated cone.')
]:
    s = sources[version]
    src = Path(s['literal_extract'])
    if 'extract_sha256' in s:
        assert sha(src) == s['extract_sha256'] and sha(s['pdf']) == s['pdf_sha256']
        assert sha(s['html']) == s['html_sha256']
    p = reads / (label + '.txt')
    literal = '\n'.join(src.read_bytes().decode('utf-8').split('\n')[first-1:last])
    p.write_text(literal)
    assert p.read_bytes().decode('utf-8') == literal
    units.append({'id': label, 'source': str(src), 'source_sha256': sha(src),
                  'version': version, 'one_based_inclusive_LF_range': [first, last],
                  'literal_file': str(p), 'literal_sha256': sha(p),
                  'selected_body_root_read': True, 'whole_primary_body_root_read': False,
                  'scope_and_limits': scope})
write(reads / 'source-read-record.json', {
    'recorded_utc': now, 'line_convention': 'UTF-8 bytes decode and split("\\n"), inclusive LF range',
    'units': units, 'mathematical_applications_independently_reviewed': False
})
items = []
for atom, roundno, stem, role, db, session in [
    ('P13.1', 60, 'P13.1-public-source-relative-volume-and-uniform-Reeb-energy', 'author', 'campaign.sqlite', 76327),
    ('P13.2', 51, 'P13.2-public-source-fixed-Reeb-mathematical-review-v3', 'mathematical partial review', 'review.sqlite', 21616),
    ('P16.1', 58, 'P16.1-public-source-algebraic-collar-trace-and-unibranch-equation', 'completed author', 'campaign.sqlite', 60905)
]:
    C = R / 'campaigns' / ('round-' + str(roundno)) / stem
    proc = subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / db)], cwd='/workspace/xean', capture_output=True, text=True, check=True)
    p = D / (atom + '-native-status.json')
    p.write_text(proc.stdout)
    items.append({'atom': atom, 'round': roundno, 'role': role, 'directory': str(C),
                  'tool_session_id': session, 'observed_status': json.loads(proc.stdout)['status'],
                  'status': str(p), 'status_sha256': sha(p),
                  'settings_sha256': sha(C / 'settings.json'), 'accepted': False})
active = [i for i in items if i['observed_status'] == 'running']
assert len(active) <= 2 and items[2]['observed_status'] == 'completed'
obs = D / 'current-small-batch-observation.json'
write(obs, {'recorded_utc': now, 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol',
            'reasoning': 'xhigh', 'items': items, 'hot_feedback_sent': False})
completed58 = {'candidate': False, 'fully_solved_original_atom': False,
    'reader': str(R / 'root-checks/public-P16.1-round-58-final-reader'),
    'whole_argument_and_four_canonical_notes_root_read': True,
    'literal_bindings_reproduced': 56, 'all_selected_literal_bodies_root_read': False,
    'independent_review': 'NOT_LAUNCHED',
    'state': 'COMPLETED partial. Algebraic collars and trace repairs retained; local BT/globalization, Rossi/Runge and singular envelopes remain unresolved.'}
a = json.loads((R / 'active-work.json').read_text())
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42 and sum(len(t['reviewed_papers']) for t in c['targets']) == 40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
a['updated_utc'] = now
a['selected_atoms'] = [i['atom'] for i in active]
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint69: completed P16.1 partial58 and exact reader; actual P13.2 INCONCLUSIVE report and bindings; fresh mathematical-only audit and relative-volume primary sources. No new original closure.'
a['current_small_batch'] = {'recorded_utc': now, 'route': 'Xean native Codex',
    'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'active_items': active,
    'completed_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'hot_feedback_sent': False}
a['prepared_P16.1_round58']['state'] = 'COMPLETED partial, candidate=false; whole argument/four notes read and reader preserved; original remains open.'
a['P16.1_round58_author_completion'] = completed58
a['P13.2_round51_mathematical_review_v3'] = items[1]
c['updated_utc'] = now
c['latest_verified_github_checkpoint'] = receipt
c['active_atoms'] = [i['atom'] for i in active]
c['current_small_batch_launch'] = str(obs)
c['current_small_batch_launch_sha256'] = sha(obs)
for t in c['targets']:
    if t['id'] == 'P16.1':
        t['current_focus'] = completed58['state']
    if t['id'] == 'P13.2':
        t['current_focus'] = 'Actual v2 review INCONCLUSIVE from unavailable local-file operational checks; mathematical-only v3 audit launched, unchanged whole partial proof. Original image/existence remains open.'
write(R / 'active-work.json', a)
write(R / 'checklist-current.json', c)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file()
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation69/' + str(p.relative_to(R)),
                  'bytes': p.stat().st_size, 'sha256': sha(p)})
for directory in [D, reads, R / 'root-checks/public-P16.1-round-58-final-reader']:
    for p in sorted(directory.rglob('*')):
        if p.is_file():
            add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
C60 = R / 'campaigns/round-60/P13.1-public-source-relative-volume-and-uniform-Reeb-energy'
C51 = R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-mathematical-review-v3'
for C, names in [(C60, ['input.json', 'settings.json', 'input-manifest.json']),
                 (C51, ['argument.md', 'task.json', 'settings.json', 'freeze.json'])]:
    for name in names:
        add(C / name)
for s in json.loads(metadata.read_text()):
    for k in ['pdf', 'literal_extract', 'html']:
        add(s[k])
    if 'fresh_official_versioned_pdf' in s:
        assert Path(s['pdf']).read_bytes() == Path(s['fresh_official_versioned_pdf']).read_bytes()
        add(s['fresh_official_versioned_pdf'])
for p in [metadata, R / 'prepare_continuation69_completed_readers_20261005.py',
          R / 'prepare_public_P13_2_mathematical_partial_review_v3_20261005.py',
          R / 'prepare_public_P13_1_relative_volume_repair_20261005.py',
          R / 'root-checks/P16.1-round58-actual-result-20261005.json',
          R / 'root-checks/P13.2-round51-v2-actual-review-result-20261005.json',
          R / 'root-checks/P13.2-round51-v2-root-review-read-and-bindings-continuation69.json',
          G / 'push-receipt-continuation68.json', G / 'prepare_checkpoint_continuation69.py']:
    add(p)
assert len({f['path'] for f in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 40, 'current_native_batch': active,
    'commit_message': 'Preserve algebraic collar partial proof and relative-volume primary reconstruction',
    'scope': 'Unreviewed partial58 exact reader; actual INCONCLUSIVE51 report; new mathematical-only partial audit; launched60; thirteen literal source read units. No new accepted paper or original closure; no private transcripts, SQL, authentication, Git databases or book-source edits.'}
p = G / 'upload-manifest-continuation69.json'
assert not p.exists()
write(p, payload)
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files),
                  'statuses': [(i['atom'], i['observed_status']) for i in items],
                  'fully_solved_originals': 3}, indent=2))
