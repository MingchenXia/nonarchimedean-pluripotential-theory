from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, o):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(o, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
prev = G / 'push-receipt-continuation159.json'
old = json.loads(prev.read_text())
assert old['commit_sha'] == '9a3d143842ff9c1709492752873ae859d4e0983d'
assert all(old[x] for x in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
readers = {154: K / 'public-P16.5-round154-partial-corrected-model-moments-reader', 155: K / 'public-P19.2-round155-partial-joint-entropy-reader', 196: K / 'public-P16.5-continuation196-general-output-reader', 197: K / 'public-P16.5-continuation197-intrinsic-target-reader'}
bindings = {}
for n, d in readers.items():
    p = d / 'publication-binding.json'
    b = json.loads(p.read_text())
    assert sha(b['tex']) == b['tex_sha256'] and sha(b['pdf']) == b['pdf_sha256']
    assert not b['independent_acceptance'] and not b['original_closed'] and b['warnings'] == b['overfull'] == b['undefined'] == 0
    if n in (154, 155):
        b.update(actual_visual_pages=[1, 4, 7, 10] if n == 154 else [1, 4, 6, 8], native_compile_request_cell='361' if n == 154 else '362', native_compile_success_observed=False, existing_editor_unchanged=True)
        p.write_text(json.dumps(b, indent=2) + '\n')
    bindings[n] = b
erratum = K / 'P16.5-continuation194-coefficient-orientation-erratum-and-corrected154-binding-20261006.json'
err = json.loads(erratum.read_text())
assert sha(err['historical_tex']) == err['historical_tex_sha256'] and err['historical_source_immutable']
S = K / 'small-batch156157-public-status-20261006-continuation160'
S.mkdir()
items = []
for n in (154, 155, 156, 157):
    C = next((R / f'campaigns/round-{n}').iterdir())
    f = json.loads((C / 'freeze.json').read_text())
    launch = json.loads((C / 'launch-record.json').read_text())
    for name, key in [('task.json', 'task_sha256'), ('settings.json', 'settings_sha256'), ('argument.md', 'argument_sha256') if n == 156 else ('input.json', 'input_sha256')]:
        assert sha(C / name) == f[key]
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    if n in (154, 155):
        assert st['status'] == 'completed' and st['calls']['unsettled'] == 0
    if st['status'] == 'running':
        assert st['calls']['admitted'] == st['calls']['unsettled'] == 1
    sp = S / f'round{n}-public-native-status.json'
    save(sp, st)
    items.append({'round': n, 'atom': 'P19.2' if n in (155, 156) else 'P16.5', 'directory': str(C), 'observed_status': st['status'], 'observed_utc': st['observedAt'], 'public_status': str(sp), 'public_status_sha256': sha(sp), 'launch_record': launch, 'frozen_metadata': f, 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False})
active = [x for x in items if x['observed_status'] == 'running']
assert len(active) <= 2 and all(x['round'] in (156, 157) for x in active)
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': 'Independent whole general fixed-start joint entropy review156 and entire unchanged original big-class equation author157 with corrected finite moments and new reference/target bridges.'}
D = G / 'continuation160-publication-records'
D.mkdir()
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34 and j['historical_reviewed_scoped_papers'] == 58
    j.update(updated_utc=now, current_small_batch=batch, github_pending_checkpoint='continuation160 frozen', P16_5_completed_partial154=bindings[154], P19_2_completed_partial155=bindings[155], P16_5_general_output_integrability196=bindings[196], P16_5_intrinsic_target_algebraic_nullness197=bindings[197], P16_5_historical194_material_coefficient_erratum=err, goal_state='8/42 originals solved;34 open;58 independently accepted papers. Four newly published partial/conditional papers do not change counts. Whole original equations and approximation remain open; continue two-problem batches.')
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
states = {x['round']: x['observed_status'] for x in items}
lines = (R / 'checklist-current.tsv').read_text().splitlines()
for i, line in enumerate(lines):
    row = line.split('\t')
    if row[0] == 'P16.5':
        row[2] = 'Completed15410-page partial corrects finite energy coefficient order and gives discrepancy-controlled general squeeze. New conditional1964-page output integrability and1973-page intrinsic-target algebraic nullness unreviewed. Full original157 ' + states[157] + '. Full original open.'
    if row[0] == 'P19.2':
        row[2] = 'Completed1558-page partial general joint entropy theorem for maximal rays with fixed actual finite-H start; closed P-profile and nonmaximal branch remain open. Whole scoped review156 ' + states[156] + '.58 accepted supporting papers overall; full original open.'
    lines[i] = '\t'.join(row)
(R / 'checklist-current.tsv').write_text('\n'.join(lines) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    shutil.copyfile(R / name, D / name)
save(D / 'scope-observation.json', {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_papers': 58, 'new_original_closure': None, 'new_independent_acceptance': None, 'new_papers': [{'id': n, 'pages': b['pages'], 'independent_acceptance': False, 'scope': b.get('scope', b.get('new_proof'))} for n, b in bindings.items()], 'historical194_identity_materially_incorrect': True, 'historical194_preserved_immutable': True, 'corrected_finite_identity_in154': True, 'active_batch': [x['round'] for x in active], 'active_private_outputs_read': False, 'hot_feedback_sent': False, 'native_compiler_success_observed': False, 'existing_editor_unchanged': True, 'whole_goal_blocked': False})
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.out', '.aux')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation160/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (D, S):
    for p in sorted(folder.iterdir()):
        add(p)
for n, d in readers.items():
    b = bindings[n]
    for p in (Path(b['tex']), Path(b['pdf']), d / 'publication-binding.json'):
        add(p)
    if n in (154, 155):
        for name in ('source-application-ledger.json' if n == 154 else 'source-applications.json', 'remaining-gaps.json', 'status.json'):
            add(d / name)
        atom = 'P16.5' if n == 154 else 'P19.2'
        add(K / f'{atom}-round{n}-actual-canonical-author-result-20261006.json')
        add(K / f'{atom}-round{n}-completed-partial-root-reading-and-scope-record-20261006.json')
    else:
        add(K / f'P16.5-continuation{n}-root-source-application-and-read-scope-20261006.json')
add(erratum)
for n in (156, 157):
    C = next((R / f'campaigns/round-{n}').iterdir())
    for name in ('task.json', 'settings.json', 'freeze.json', 'mathematical-data-bindings.json', 'launch-record.json', 'argument.md' if n == 156 else 'input.json'):
        add(C / name)
for p in (prev, R / 'record_verified159_20261006.py', R / 'publish_partials154155_prepare_batch156157_20261006.py', R / 'launch_frozen_batch156157_20261006.py', Path(__file__)):
    add(p)
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
M = G / 'upload-manifest-continuation160.json'
save(M, {'generated_utc': now, 'repository': old['repository'], 'branch': old['branch'], 'expected_previous_checkpoint': old['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 58, 'commit_message': 'Correct finite model energy identity and record new integrability bridges', 'scope': 'Completed15410-page corrected finite moments/general discrepancy squeeze and1558-page general maximal joint entropy partial. New explicitly conditional1964-page reference-section/general-output integrability and1973-page intrinsic-target algebraic nullness. Historical194 false coefficient identity preserved with material erratum and actual blowup witness. Whole original157 and independent scoped156 launched, at most two active;8/42 originals and58 accepted papers unchanged. No native compiler success claimed; all final sources and listed visual pages checked, own quote-free source ledgers, no active private output reads or hot feedback.'})
print(json.dumps({'manifest': str(M), 'sha256': sha(M), 'files': len(files), 'statuses': [{k: x[k] for k in ('round', 'observed_status', 'observed_utc')} for x in items]}, indent=2))
