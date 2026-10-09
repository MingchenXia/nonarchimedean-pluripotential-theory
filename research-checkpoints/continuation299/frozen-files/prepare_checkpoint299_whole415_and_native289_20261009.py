from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation299-publication-records'
M = G / 'upload-manifest-continuation299.json'
D = K / 'public-P16.7-continuation415-universal-variational-limits-local-Gauss-fibres-and-USC-relaxation-unreviewed'
C = R / 'campaigns/round-289/P16.7-whole414415-tail-maxima-and-actual-analytic-representation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation298.json')
assert prior['commit_sha'] == '400982936d6d43813d426c8e86541a624efdbf8b' and prior['tree_sha'] == '2eeaf083da64cbd05b5b38efcfa56d0cce91ebdf' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
b = load(D / 'ROOT-whole-paper-source-scope-and-binding.json')
assert b['paper'] == 415 and not b['accepted'] and not b['original_closed']
assert b['compiler'] == 'NOT_YET_INVOKED'
for e in b['public_files']:
    assert sha(e['path']) == e['sha256']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [K / 'P16.7-ROOT-uniform-third-MA-moments-and-finite-tail-maximum-bridge-working-note-20261009.txt']
paths += [R / n for n in ['audit_and_stage_native287_whole_paper415_ROOT_20261009.py', 'prepare_native289_whole414415_actual_analytic_representability_20261009.py', 'launch_frozen_native289_checked_20261009.py', 'capture_terminal_native288_actual_FINAL_20261009.py', 'record_verified_checkpoint298_20261009.py']]
paths += [C / n for n in ['original-task.json', 'task.json', 'settings.json', 'freeze.json', 'launch-record.json', 'mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation298.json', Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 298 and x['current_active_batch'] == [289]
    assert len(x['fully_solved_original_atoms']) == 16 and x['remaining_open_original_atoms'] == 26 and x['historical_reviewed_scoped_papers'] == 97
F.mkdir()
for p in paths:
    rel = p.relative_to(R)
    assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    q = F / 'frozen-files' / rel
    q.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p, q)
    assert sha(q) == sha(p)
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    x = load(p)
    x.update(updated_utc=now, github_pending_checkpoint=dict(continuation=299, prepared_utc=now, manifest=str(M), expected_parent=prior['commit_sha'], push_complete=False), next_work='Verify NONFORCE299 whole UNREVIEWED415 and finite-tail-maximum proof plus qualified native289 frozen/launch metadata. Actual415 desktop compilation pending UNVERIFIED, no success claim; native289 running, active math excluded. Native288 terminal four-note FINAL retained unread until whole physical audit and separate reconstruction. Counts/editor unchanged.')
    write(p, x)
write(F / 'current-research-status.json', dict(recorded_utc=now, fully_solved_original_atoms=x['fully_solved_original_atoms'], solved=16, open=26, accepted_scoped_papers=97, current_active_batch=[289], new_papers=[415], whole_new_actual_fields_and_distinct_expanded_proofs_ROOT_physically_read=True, full_immediate_applied_primary_units_ROOT_read=15, whole415_compilation='UNVERIFIED; actual desktop request pending; historical binding predates invocation', whole414_compilation='success observed in prior298', native288_terminal_math_NOT_read_or_published=True, active_native289_math_NOT_read_or_published=True, UNREVIEWED=True, original_closed=False, accepted=False, source_bodies_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint299: universal variational limits, local finite Gauss fibres and the actual representation gap\n\nWhole UNREVIEWED ROOT415 retains ALL FIVE actual FINAL fields of ALL FIVE settled native287 notes, the complete774-LF standalone expanded proof and distinct91-LF geometric fragment, entire proof companion, unique ledgers/verdict/residual and six native programs as inert DATA. ROOT physically read every unique actual/expanded proof and all15 directly applied complete immediate CLD/GR source units. Complete deeper historical/geometric/generated/descent audit remains qualified unfinished. The native source is unchanged. The desktop compiler was invoked but has not returned: compilation is UNVERIFIED, not a claimed success. Its whole-paper binding predates that invocation. Whole ROOT414 compiled successfully and was already verified in298.\n\nThe conditional bounded deductions give common real/moving moments and genuine all-continuous-test Radon weak limits for EVERY normalized finite-FULL-dual mass-two maximizing net. Uniform third-slot absolute MA moments give L1 of the limiting MA measure, exact limiting full dual and nonnegative prescribed-measure defect. Fixed Laurent finite-flat local Gauss-fibre families have common bounded caps and uniform positive atoms at every fibre point, hence uniform maximizing convergence on that compact local sector. ALL affinoid Shilov values define a canonical actual normalized USC upper relaxation. This does not establish its positivity or original finite-energy membership, full-point agreement, or equality of the weak MA limit with EVERY prescribed measure. Ordinary Gauss neighborhoods can exclude same-radius cancellation points; shrinking radial polyannuli do not prove the needed Shilov-neighborhood basis.\n\nThe complete independent ROOT finite-tail-maximum working note uses the uniform third-test modulus and a summably fast actual maximizing sequence. Every FINITE tail maximum remains in original C with energy gain at most the summable tail error; the suprema of these REAL energies decrease to the common maximizing energy. Infinite tail suprema/USC regularizations are not thereby positive or in C/G. Native289 includes WHOLE415/414, this complete deduction and qualified sources to address actual analytic representation, recognition and arbitrary-support original existence. User-selected local Xean plus signed-in official Codex gpt-6.1-sol xhigh, ONE running campaign now, at mostTWO. Only frozen/launch metadata are published, no active mathematics. Native288 terminal new P12.3 mathematics is still unread and excluded. Counts16/42 solved,26OPEN,97accepted scoped papers unchanged. No new acceptance or original closure. Full primary literal bodies/pixels/books LOCALONLY; protected P16.4 editor OPEN UNCHANGED. NONFORCE upload verifies remote blob/tree/file/ref bindings.\n')
files = [dict(local=str(p), path='research-checkpoints/continuation299/' + str(p.relative_to(F)), bytes=p.stat().st_size, sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), solved=16, remaining_open=26, accepted_scoped_papers=97, commit_message='Checkpoint universal variational limits, local Gauss fibres and actual representation residual', scope='Whole UNREVIEWED415 and finite-tail-maxima proof;415 compilation unverified, native289 active mathematics excluded, native288 terminal mathematics unread, original OPEN.'))
items = files + [dict(local=str(M), path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation299.json', bytes=M.stat().st_size, sha256=sha(M))]
git = ['git', '--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation299.index')
subprocess.run(git + ['read-tree', prior['tree_sha']], env=env, capture_output=True, check=True)
entries = []
groups = {}
for e in items:
    data = Path(e['local']).read_bytes()
    data.decode('utf-8')
    assert hashlib.sha256(data).hexdigest() == e['sha256']
    h = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert subprocess.run(git + ['hash-object', '-w', e['local']], capture_output=True, text=True, check=True).stdout.strip() == h
    entries.append(dict(path=e['path'], mode='100644', type='blob', sha=h))
    groups.setdefault(h, e)
    subprocess.run(git + ['update-index', '--add', '--cacheinfo', '100644', h, e['path']], env=env, capture_output=True, check=True)
expected = subprocess.run(git + ['write-tree'], env=env, capture_output=True, text=True, check=True).stdout.strip()
API = G / 'api-recovery-continuation299'
API.mkdir()
chunks = []
chunk = []
size = 0
for h, e in groups.items():
    item = dict(path=h, mode='100644', type='blob', content=Path(e['local']).read_text())
    n = len(json.dumps(item, ensure_ascii=True).encode())
    if chunk and size + n > 250000:
        chunks.append(chunk)
        chunk = []
        size = 0
    chunk.append(item)
    size += n
if chunk:
    chunks.append(chunk)
sizes = []
for i, ch in enumerate(chunks):
    p = API / f'content-chunk-{i}.json'
    p.write_text(json.dumps(dict(tree=ch), ensure_ascii=True, indent=2) + '\n')
    sizes.append(p.stat().st_size)
write(API / 'connector-plan.json', dict(repository=prior['repository'], branch=prior['branch'], parent=prior['commit_sha'], base_tree=prior['tree_sha'], expected_tree=expected, manifest_sha256=sha(M), entries=entries, content_chunks=len(chunks), content_chunk_bytes=sizes, commit_message=load(M)['commit_message'], force=False))
print(json.dumps(dict(manifest=str(M), manifest_sha256=sha(M), listed_files=len(files), actual_files=len(items), content_chunks=len(chunks), content_chunk_bytes=sizes, expected_tree=expected, primary_bodies_published=False), indent=2))
