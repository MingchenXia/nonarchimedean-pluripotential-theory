"""Freeze completed partial61, active63, and the ten-source curve-detection successor."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation72-publication-records'
reads = R / 'root-checks/continuation72-primary-curve-detection-reads'
assert not D.exists() and not reads.exists()
receipt = json.loads((G / 'push-receipt-continuation71.json').read_text())
assert receipt['commit_sha'] == '338e9ed08a6156a4aea470634718758dd07851e8'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
D.mkdir()
reads.mkdir()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
sources = {
    'GR2503v1': R / 'shared-sources/GR2503.05513v1-20261005-continuation72.txt',
    'Ducros-published': R / 'shared-sources/Ducros-published-1250007-20261005-continuation72.txt',
    'GJR2111v3': R / 'shared-sources/GJR2111.05741v3-20261005-continuation72.txt',
    'CLD1204v2': R / 'shared-sources/new-primary-1204.6277v2-20261004-continuation64.txt',
    'GM1608v3': R / 'shared-sources/GM1608.08030v3-20261004-continuation66.txt'
}
units = []
for version, label, first, last, scope in [
    ('GR2503v1', 'GR-field-scope-and-current-warning', 1, 200, 'Introduction and Remark1.8; generic R-PL positive-current converse/pullback is not assumed.'),
    ('GR2503v1', 'GR-polyhedral-coefficient-conventions', 245, 273, 'Actual affine coefficients and beginning affine lifting theorem; not a whole lifting proof.'),
    ('GR2503v1', 'GR-curve-detection-and-pointwise-PL-limit-proofs', 778, 1031, 'Whole5.1,5.3,5.4,5.5,5.6 proofs; strict actual R-PL membership is a prerequisite.'),
    ('Ducros-published', 'Ducros-published-version-title', 1, 150, 'Actual published version and polytope statements; not a generated replacement.'),
    ('Ducros-published', 'Ducros-valued-field-image-A-proof', 1250, 1402, 'Whole1.2 statement and assertion A closedness/dimension proof; C proof is not included.'),
    ('Ducros-published', 'Ducros-compact-strict-polytope-theorem-proof', 2070, 2156, 'Whole3.2; finite rational coefficient polytope image and dimension at most d.'),
    ('GJR2111v3', 'GJR-local-formal-nef-and-field-detection', 2281, 2435, 'Whole7.1,7.4,7.6; actual represented model functions and analytic neighborhood hypotheses.'),
    ('CLD1204v2', 'CLD-Q-polyhedral-tropical-image-conventions', 16731, 16990, 'Actual12.1/12.2 passages; affine constants R in its Q-rational convention. Printed dimension equality is not used.'),
    ('CLD1204v2', 'CLD-valued-field-polyhedral-proof', 13951, 14180, 'Whole10.5.7 proof and definitions, with actual valued-field/model-theory antecedents.'),
    ('CLD1204v2', 'CLD-strict-nef-to-psh-direction', 25535, 25644, '17.8.4 proves nef to psh; not its converse.'),
    ('CLD1204v2', 'CLD-integer-current-field-extension-scope', 27926, 28076, '18.8.4/6/8 actual integer-PL scope; represented integer positive metrics have field-extension theorem.'),
    ('GM1608v3', 'GM-field-nef-and-local-global-model-proof', 650, 782, 'Whole3.3 and3.11 with represented formal metric and separated paracompact strict space.')
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
reader = R / 'root-checks/public-P16.1-round-61-final-reader'
state = json.loads((reader / 'root-preservation-and-read-state-continuation72.json').read_text())
for f in state['original_author_file_bindings']:
    assert sha(reader / f['relative_path']) == f['sha256']
assert state['candidate'] is False and state['whole_argument_root_read']
assert state['entire_completed_native_result_and_four_notes_root_read']
assert sha(state['actual_result']) == state['actual_result_sha256']
followup = {'recorded_utc': now, 'candidate': False, 'fully_solved_original_atom': False,
    'reader': str(reader), 'whole_argument_and_four_canonical_notes_root_read': True,
    'source_application_index_root_read': True, 'whole_tex_root_read': False,
    'all_literal_excerpts_byte_reproduced': True, 'literal_excerpts': 61,
    'all_literal_excerpt_bodies_root_read': False, 'independent_correctness_review': 'NOT_LAUNCHED',
    'root_independent_tex_compilation': 'NOT_RUN', 'native_editor_compilation': 'NOT_REQUESTED',
    'exact_scope': 'Unreviewed general-variety genuine operator/conditional equation, relative-support algebraic-curve theorem, radial trace equality conditional on open extension, model atoms, algebraic collar and finite calibrated-facet statements. Singular EP and original equation remain open.'}
write(D / 'P16.1-round61-completion-followup.json', followup)
write(D / 'P13.1-round60-native-compiler-followup.json', {'recorded_utc': now,
    'source': str(R / 'root-checks/public-P13.1-round-60-final-reader/P13.1-paper.tex'),
    'cell_id': '2555', 'native_compilation': 'UNVERIFIED: no diagnostics returned; service call terminated after repeated no-output waits.',
    'native_compilation_success_verified': False, 'source_preserved': True,
    'mathematical_campaign_cancelled': False})
C64 = R / 'campaigns/round-64/P16.1-public-source-curve-detection-and-singular-globalization'
m64 = json.loads((C64 / 'input-manifest.json').read_text())
assert sha(C64 / 'input.json') == m64['input_sha256']
assert sha(C64 / 'settings.json') == m64['settings_sha256']
assert not (C64 / 'campaign.sqlite').exists()
data = json.loads((C64 / 'input.json').read_text())
old = R / 'campaigns/round-61/P16.1-public-source-calibrated-local-BT-and-unibranch-equation/input.json'
assert data['task'] == json.loads(old.read_text())['task']
assert data['notes'] == [] and len(m64['public_sources']) == 10 and len(m64['embedded_context']) == 7
for s in m64['public_sources']:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
for b in m64['embedded_context']:
    assert sha(b['path']) == b['sha256']
    assert Path(b['path']).read_text() in data['assignment']
write(D / 'prepared-P16.1-round64-input-bindings.json', {'recorded_utc': now,
    'input_sha256': m64['input_sha256'], 'settings_sha256': m64['settings_sha256'],
    'source_count': 10, 'embedded_context_count': 7, 'original_task_unchanged': True,
    'saved_assignment_prefix_settings_and_original_criteria_root_read': True,
    'launched': False, 'scope': 'Fresh proof reconstruction including actual curve detection, rational polytope representation, nef-to-FS and exact Laurent Gauss descent; all singular envelope gates remain required.'})
proposals = sorted((R / 'root-checks').glob('P16.1-*-20261005-continuation72.md'))
assert len(proposals) == 2
a = json.loads((R / 'active-work.json').read_text())
c = json.loads((R / 'checklist-current.json').read_text())
assert len(c['targets']) == 42 and sum(len(t['reviewed_papers']) for t in c['targets']) == 40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved']) == ['P15.1', 'P15.2', 'P16.6']
a['updated_utc'] = now
a['selected_atoms'] = ['P13.1', 'P13.2']
a['github_checkpoint'] = receipt
a['github_pending_checkpoint'] = 'Checkpoint72: completed unreviewed partial61, active63, ten-source curve-detection successor64 prepared; no new original closure.'
a['current_small_batch']['recorded_utc'] = now
a['current_small_batch']['active_items'] = [i for i in items if i['observed_status'] == 'running']
a['P16.1_round61_author_completion'] = followup
a['prepared_P13.1_round63'] = {'directory': items[1]['directory'], 'launched': True,
    'tool_session_id': 73148, 'state': items[1]['observed_status'], 'accepted': False}
a['prepared_P16.1_round64'] = {'directory': str(C64), 'input_sha256': m64['input_sha256'],
    'settings_sha256': m64['settings_sha256'], 'launched': False, 'accepted': False}
a['continuation72_unreviewed_root_proposals'] = {'paths': [str(p) for p in proposals],
    'source_read_record': str(reads / 'source-read-record.json'), 'independently_reviewed': False,
    'new_originals_solved': []}
c['updated_utc'] = now
c['latest_verified_github_checkpoint'] = receipt
c['current_small_batch'] = a['current_small_batch']
for t in c['targets']:
    if t['id'] == 'P13.1':
        t['current_focus'] = 'Eleven-source semigroup/obstacle successor63 running through native Xean gpt-6.1-sol/xhigh. Completed60 remains an unreviewed partial; original uniform differentiation is open.'
    if t['id'] == 'P16.1':
        t['current_focus'] = 'Completed unreviewed partial61 whole argument/four notes read. Ten-source curve-detection and singular-globalization successor64 prepared locally only. Original singular envelope and equation remain open.'
write(R / 'active-work.json', a)
write(R / 'checklist-current.json', c)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    shutil.copyfile(R / name, D / name)
files = []
def add(path, remote=None):
    p = Path(path)
    assert p.is_file()
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation72/' + str(p.relative_to(R)),
        'bytes': p.stat().st_size, 'sha256': sha(p)})
for directory in [D, reads, reader]:
    for p in sorted(directory.rglob('*')):
        if p.is_file(): add(p)
for name in ['input.json', 'settings.json', 'input-manifest.json']: add(C64 / name)
for p in proposals + [R / 'prepare_public_P16_1_curve_detection_repair_20261005.py',
    R / 'prepare_continuation72_completed_P16_1_reader_20261005.py',
    R / 'root-checks/P16.1-round61-actual-result-20261005.json',
    R / 'root-checks/CLD12.2.4-printed-dimension-20261005-continuation72.png',
    G / 'push-receipt-continuation71.json', G / 'prepare_checkpoint_continuation72.py']: add(p)
for name in ['GR2503.05513v1', 'Ducros-published', 'GJR2111.05741v3']:
    p = R / 'shared-sources' / (name + '-primary-authentication-20261005-continuation72.json')
    m = json.loads(p.read_text())
    for src in [p, Path(m['pdf']), Path(m['literal_extract'])]: add(src)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({f['path'] for f in files}) == len(files)
payload = {'generated_utc': now, 'repository': receipt['repository'], 'branch': receipt['branch'],
    'expected_previous_checkpoint': receipt['commit_sha'], 'files': files, 'file_count': len(files),
    'fully_solved_original_atoms': ['P15.1', 'P15.2', 'P16.6'], 'remaining_open_atoms': 39,
    'historical_reviewed_scoped_papers': 40, 'current_native_batch': items,
    'commit_message': 'Preserve partial singular proof and curve-detection globalization repair',
    'scope': 'Completed unreviewed partial61 reader/paper, active63 status, unlaunched64 frozen inputs, two new unreviewed proposals, twelve exact primary read units and three authenticated public sources. No new accepted original, private transcripts, SQL, auth, Git databases or book-source changes.'}
p = G / 'upload-manifest-continuation72.json'
assert not p.exists()
write(p, payload)
print(json.dumps({'manifest': str(p), 'sha256': sha(p), 'files': len(files),
    'statuses': [(i['atom'], i['observed_status']) for i in items], 'fully_solved_originals': 3}, indent=2))
