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
prev = G / 'push-receipt-continuation158.json'
old = json.loads(prev.read_text())
assert old['commit_sha'] == 'cfefa17e769d0677d99121ee3a77bad90d8f90db'
assert all(old[x] for x in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
paper = R / 'deliverables/scoped-P19.2-singular-start-relative-profile'
bp = json.loads((paper / 'publication-binding.json').read_text())
assert bp['review_verdict'] == 'PASS' and bp['independent_acceptance'] and not bp['original_closed']
assert bp['accepted_paper_count'] == 58 and bp['pages'] == 10
for key in ('tex', 'pdf'):
    assert sha(bp[key]) == bp[key + '_sha256']
assert sha(paper / 'P19.2-paper.md') == bp['md_sha256'] and sha(bp['review']) == bp['review_sha256']
reader = K / 'public-P16.5-round151-partial-foundations-reader'
br = json.loads((reader / 'publication-binding.json').read_text())
assert br['pages'] == 14 and not br['candidate'] and not br['independent_acceptance'] and not br['original_closed']
for key in ('tex', 'pdf'):
    assert sha(br[key]) == br[key + '_sha256']
assert br['whole_actual_canonical_all4_notes_root_read'] and br['whole_final_1135_line_tex_root_read']
assert br['build_log_warning_count'] == 1 and br['overfull'] == br['undefined'] == 0
br.update(native_compile_request_cell='304', native_compile_success_observed=False, existing_editor_unchanged=True)
(reader / 'publication-binding.json').write_text(json.dumps(br, indent=2) + '\n')
S = K / 'small-batch154155-public-status-20261006-continuation159'
S.mkdir()
items = []
for n in (151, 152, 153, 154, 155):
    C = next((R / f'campaigns/round-{n}').iterdir())
    f = json.loads((C / 'freeze.json').read_text())
    launch = json.loads((C / 'launch-record.json').read_text())
    for name, key in [('task.json', 'task_sha256'), ('settings.json', 'settings_sha256'), ('argument.md', 'argument_sha256') if n == 152 else ('input.json', 'input_sha256')]:
        assert sha(C / name) == f[key], (n, name)
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    if n in (151, 152):
        assert st['status'] == 'completed' and st['calls']['unsettled'] == 0
    if n == 153:
        assert st['status'] == 'blocked' and st['calls']['admitted'] == st['calls']['settled'] == st['calls']['unknownUsage'] == 1
        assert st['calls']['unsettled'] == 0
    ps = subprocess.run(['ps', '-o', 'stat=,comm=', '-p', str(launch['pid'])], capture_output=True, text=True).stdout.strip()
    alive = bool(ps) and not ps.startswith('Z')
    if st['status'] == 'running':
        assert alive and st['calls']['admitted'] == st['calls']['unsettled'] == 1
    sp = S / f'round{n}-public-native-status.json'
    save(sp, st)
    items.append({'round': n, 'atom': 'P19.2' if n in (152, 155) else 'P16.5', 'directory': str(C), 'observed_status': st['status'], 'observed_utc': st['observedAt'], 'native_controller_process_observed_alive': alive, 'public_status': str(sp), 'public_status_sha256': sha(sp), 'launch_record': launch, 'frozen_metadata': f, 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'original_closed': False, 'private_active_output_read': False, 'hot_feedback_sent': False})
active = [x for x in items if x['observed_status'] == 'running']
assert len(active) <= 2 and all(x['round'] in (154, 155) for x in active)
states = {x['round']: x['observed_status'] for x in items}
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': 'Entire unchanged original P16.5 author154 and entire unchanged original P19.2 author155 after independently accepted scoped singular-start theorem.'}
D = G / 'continuation159-publication-records'
D.mkdir()
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34 and j['historical_reviewed_scoped_papers'] == 58
    j.update(updated_utc=now, current_small_batch=batch, github_pending_checkpoint='continuation159 frozen', P16_5_completed_partial151=br, P19_2_accepted_singular_start152=bp, goal_state='8/42 originals solved;34 open;58 independently accepted papers. New scoped singular-start paper accepted; full P19.2 and P16.5 remain open. Continue two-problem batches.')
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
lines = (R / 'checklist-current.tsv').read_text().splitlines()
for i, line in enumerate(lines):
    row = line.split('\t')
    if row[0] == 'P16.5':
        row[2] = 'Completed15114-page partial foundations and outer-energy measure, candidate=false;194/195 finite-nef and finite-atomic weighted drafts unreviewed. Native original154 ' + states[154] + ' at this checkpoint. Full original open.'
    if row[0] == 'P19.2':
        row[2] = 'Whole scoped singular-start relative-profile paper PASS152,58 accepted papers overall; explicit CPn n>=2 singular start, closed relative ceilings/raw masses and joint entropy. Native original155 ' + states[155] + ' at this checkpoint. Full original open.'
        row[3] = '4'
    lines[i] = '\t'.join(row)
(R / 'checklist-current.tsv').write_text('\n'.join(lines) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    shutil.copyfile(R / name, D / name)
save(D / 'scope-observation.json', {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_papers_before': 57, 'accepted_papers_after': 58, 'new_original_closure': None, 'new_independent_acceptance': {'round': 152, 'scope': bp['review_scope'], 'whole_review_root_read': True}, 'partial151': {'candidate': False, 'whole_paper_and_all4canonical_notes_root_read': True, 'pages': 14, 'local_harmless_amsmath_warnings': 1, 'compiler_errors': 0}, 'failed153': {'native_calls_admitted': 1, 'settled': 1, 'unknown_usage': 1, 'no_mathematical_result': True, 'repair': 'Exact native parent launch permission; unchanged math/task154, child sandbox and authentication retained.'}, 'active_batch': [x['round'] for x in active], 'active_private_outputs_read': False, 'hot_feedback_sent': False, 'native_compiler_success_observed': False, 'existing_editor_unchanged': True, 'whole_goal_blocked': False})
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.out', '.aux')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation159/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (D, S):
    for p in sorted(folder.iterdir()):
        add(p)
for name in ('P19.2-paper.md', 'P19.2-paper.tex', 'P19.2-paper.pdf', 'source-application-ledger.json', 'publication-binding.json'):
    add(paper / name)
for name in ('P16.5-paper.tex', 'P16.5-paper.pdf', 'source-ledger.json', 'remaining-gaps.json', 'status.json', 'publication-binding.json'):
    add(reader / name)
for name in ('P16.5-round151-actual-canonical-author-result-20261006.json', 'P16.5-round151-completed-partial-root-reading-and-scope-record-20261006.json', 'P19.2-round152-actual-scoped-independent-review-20261006.json', 'P19.2-round152-singular-start-acceptance-and-original-scope-record-20261006.json', 'P16.5-round153-native-directory-initialization-failure-20261006.json'):
    add(K / name)
for n in (153, 154, 155):
    C = next((R / f'campaigns/round-{n}').iterdir())
    for name in ('input.json', 'task.json', 'settings.json', 'freeze.json', 'mathematical-data-bindings.json', 'launch-record.json'):
        add(C / name)
for name in ('record_verified158_20261006.py', 'publish_partial151_prepare_weighted_original153_20261006.py', 'launch_frozen_weighted_original153_20261006.py', 'retry_weighted_original154_native_permissions_20261006.py', 'prepare_accepted_singular_start152_final_20261006.py', 'adopt_singular_start152_prepare_original155_20261006.py', 'launch_frozen_all_ray_original155_20261006.py'):
    add(R / name)
add(prev)
add(Path(__file__))
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(D / name, 'manuscript/editorial/xean_research_20261003/' + name)
M = G / 'upload-manifest-continuation159.json'
save(M, {'generated_utc': now, 'repository': old['repository'], 'branch': old['branch'], 'expected_previous_checkpoint': old['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 58, 'commit_message': 'Accept singular-start relative-profile paper and continue full original equations', 'scope': 'Exactly scoped PASS152 supporting paper58,10-page final with harmless clarifications and whole canonical review. Completed15114-page candidate=false partial foundations/outer-energy measure and exact remaining gaps. Native153 initialization failure preserved;154 unchanged math permission retry and155 whole original approximation launched. At most two active campaigns;8/42 originals solved,34 open. No native compiler success claimed, no active private output reads or hot feedback.'})
print(json.dumps({'manifest': str(M), 'sha256': sha(M), 'files': len(files), 'statuses': [{k: x[k] for k in ('round', 'observed_status', 'observed_utc')} for x in items]}, indent=2))
