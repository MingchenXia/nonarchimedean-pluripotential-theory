"""Freeze the prepared eleven-source repair and new unreviewed Gauss checks."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation71-publication-records'
reads = R / 'root-checks/continuation71-primary-Gauss-and-variational-reads'
assert not D.exists() and not reads.exists()
receipt = json.loads((G / 'push-receipt-continuation70.json').read_text())
assert receipt['commit_sha'] == '7ca503ebdcf191f401d08dc5c028897875f09bb9'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
D.mkdir()
reads.mkdir()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
sources = {
    'BJ1801v4': R / 'shared-sources/P16-arxiv-1801.08229-20261004.txt',
    'BE1805v3': R / 'shared-sources/P16-arxiv-1805.01016-20261004.txt',
    'GM1608v3': R / 'shared-sources/GM1608.08030v3-20261004-continuation66.txt',
    'Wu2609v1': R / 'shared-sources/new-primary-2609.27610v1-20261004.txt'
}
units = []
for version, label, first, last, scope in [
    ('BJ1801v4', 'BJ-finite-energy-variational-and-strong-measure-criteria', 4968, 5312, 'Actual9.1--9.20 read; uniform differentiation or strict concavity alone does not establish attainment.'),
    ('BJ1801v4', 'BJ-envelope-onto-and-completeness-equivalence', 6033, 6158, 'Whole12.8 proof and12.9; envelope property remains a separate singular gate.'),
    ('BJ1801v4', 'BJ-generated-cone-and-smooth-remark', 2341, 2479, 'Actual4.15/4.16 and smooth-only Remark4.19; not a singular converse.'),
    ('BJ1801v4', 'BJ-general-variety-PL-nef-scope', 1559, 1629, 'Definition3.2 and special-fiber nef criterion; semiample and nef cones distinguished.'),
    ('BJ1801v4', 'BJ-ample-model-construction', 1430, 1468, 'Actual2.33 proof; positive model atoms or regularization need their additional arguments.'),
    ('BJ1801v4', 'BJ-actual-continuous-Gauss-section', 717, 774, 'Gauss formula and continuous section; no surjectivity of sigma onto the entire base extension used.'),
    ('BE1805v3', 'BE-general-variety-nef-model-to-genuine-FS', 2281, 2478, 'Whole7.8 proof and actual7.2/7.6/7.20; ample and nontrivial field retained, H/A and epsilon typos corrected in proposals.'),
    ('GM1608v3', 'GM-actual-PL-definition-and-proper-equivalence', 91, 143, 'Strict G-cover definition and Theorem1.1; not arbitrary real tropical PL.'),
    ('GM1608v3', 'GM-G-cover-formal-construction-and-extension', 271, 590, 'Whole2.10 with cover/blowup construction and PL extension/density; positive approximation not inferred from unrestricted PL density.'),
    ('GM1608v3', 'GM-formal-nef-local-to-global-proof', 650, 820, 'Whole3.11 proof;3.12 only through LF820, not its whole proof.'),
    ('Wu2609v1', 'Wu-Runge-and-Rossi-remaining-regularization-gates', 1578, 1815, 'Whole5.1--5.8 read for diagnosis; its affine regularization application is not accepted on arbitrary singular analytic pieces.')
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
assert len([i for i in items if i['observed_status'] == 'running']) <= 2
write(D / 'current-small-batch-observation.json', {'recorded_utc': now, 'items': items,
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'hot_feedback_sent': False})
prepared = []
for roundno, stem in [
    (62, 'P13.1-public-source-extended-semigroup-and-uniform-energy-differentiation'),
    (63, 'P13.1-public-source-eleven-body-semigroup-and-uniform-differentiation')
]:
    C = R / 'campaigns' / ('round-' + str(roundno)) / stem
    m = json.loads((C / 'input-manifest.json').read_text())
    assert sha(C / 'input.json') == m['input_sha256']
    assert sha(C / 'settings.json') == m['settings_sha256']
    assert not (C / 'campaign.sqlite').exists()
    data = json.loads((C / 'input.json').read_text())
    assert data['notes'] == [] and len(m['public_sources']) == 11
    for src in m['public_sources']:
        assert sha(src['pdf']) == src['pdf_sha256']
        assert sha(src['literal_extract']) == src['extract_sha256']
    for body in m['embedded_context']:
        assert sha(body['path']) == body['sha256']
        assert Path(body['path']).read_text() in data['assignment']
    prepared.append({'round': roundno, 'directory': str(C), 'input_sha256': m['input_sha256'],
        'settings_sha256': m['settings_sha256'], 'source_count': 11,
        'embedded_context_count': len(m['embedded_context']), 'launched': False})
write(D / 'prepared-P13.1-input-bindings.json', {'recorded_utc': now, 'items': prepared,
    'round62_preserved_unlaunched': True, 'round63_assignment_prefix_settings_and_original_task_root_read': True,
    'round63_supersedes_only_source_count_ambiguity': True})
reader = R / 'root-checks/public-P13.1-round-60-final-reader'
assert sha(reader / 'P13.1-paper.tex') == '1a37e8f1091e4247ba08ae3ad4291a2a15c54dbcadfd7f1655eafbe7e9242809'
write(D / 'P13.1-round60-reader-followup.json', {'recorded_utc': now,
    'reader': str(reader), 'whole_argument_four_canonical_notes_and_tex_root_read': True,
    'tex_sha256': sha(reader / 'P13.1-paper.tex'), 'native_compilation': 'PENDING: cell2555; no diagnostics returned at freeze',
    'native_compilation_success_verified': False, 'independent_mathematical_review': 'NOT_LAUNCHED',
    'candidate': False, 'fully_solved_original_atom': False,
    'source_tex_preserved': True, 'formatting_diagnostics': ['Literal qquad/quad without a backslash occur in inherited displayed mathematics; repair in a successor, not in this frozen reader.']})
proposals = sorted((R / 'root-checks').glob('*-20261005-continuation71.md'))
assert len(proposals) == 2
a = json.loads((R / 'active-work.json').read_text())
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42 and sum(len(t['reviewed_papers']) for t in c['targets']) == 40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
a['updated_utc'] = now
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint71: prepared eleven-source P13.1 successor, unreviewed exact Gauss FS descent and strict-cover checks; no new original closure.'
a['current_small_batch']['recorded_utc'] = now
a['current_small_batch']['active_items'] = [i for i in items if i['observed_status'] == 'running']
a['continuation71_unreviewed_root_proposals'] = {'paths': [str(p) for p in proposals],
    'source_read_record': str(reads / 'source-read-record.json'), 'independently_reviewed': False,
    'new_originals_solved': []}
a['P13.1_round60_author_completion']['whole_argument_four_canonical_notes_and_tex_root_read'] = True
c['updated_utc'] = now
c['latest_verified_github_checkpoint'] = receipt
for t in c['targets']:
    if t['id'] == 'P13.1':
        t['current_focus'] = 'Completed unreviewed partial60; exact eleven-source semigroup/obstacle successor63 prepared locally, not launched. Original uniform differentiation remains open.'
write(R / 'active-work.json', a)
write(R / 'checklist-current.json', c)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file()
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation71/' + str(p.relative_to(R)),
        'bytes': p.stat().st_size, 'sha256': sha(p)})
for directory in [D, reads]:
    for p in sorted(directory.rglob('*')):
        if p.is_file(): add(p)
for item in prepared:
    for name in ['input.json', 'settings.json', 'input-manifest.json']: add(Path(item['directory']) / name)
for p in proposals + [R / 'prepare_public_P13_1_extended_semigroup_repair_20261005.py',
    R / 'prepare_public_P13_1_eleven_source_scope_20261005.py',
    G / 'push-receipt-continuation70.json', G / 'prepare_checkpoint_continuation71.py']: add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({f['path'] for f in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 40, 'current_native_batch': items,
    'commit_message': 'Preserve eleven-source semigroup repair and exact Gauss FS descent proposal',
    'scope': 'Unlaunched62/63 exact inputs and helpers, eleven selected primary read units, two unreviewed root proposals and full round60 TeX-read followup. No new accepted original, private transcripts, SQL, auth, Git databases or book-source changes.'}
p = G / 'upload-manifest-continuation71.json'
assert not p.exists()
write(p, payload)
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files),
    'statuses': [(i['atom'], i['observed_status']) for i in items], 'fully_solved_originals': 3}, indent=2))
