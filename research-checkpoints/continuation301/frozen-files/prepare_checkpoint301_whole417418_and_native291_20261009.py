from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation301-publication-records'
M = G / 'upload-manifest-continuation301.json'
D = K / 'public-P16.7-continuation418-quasi-uniform-maximizers-and-exact-prescribed-measure-defects-unreviewed'
B417 = K / 'P16.7-continuation417-ROOT-whole-paper-source-scope-and-binding-20261009.json'
C = R / 'campaigns/round-291/P16.7-whole417418-actual-representation-and-prescribed-measure-J-defect'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation300.json')
assert prior['commit_sha'] == 'a1a39b2333d07b8d69619d528c671754323fb467' and prior['tree_sha'] == 'c3bec6604e666c7021d08432c5f5c5ff7cee3ee6' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
b418 = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
b417 = load(B417)
assert b418['paper'] == 418 and not b418['accepted'] and not b418['original_closed'] and b418['compiler'] == 'NOT_YET_INVOKED_FOR418'
assert b417['paper'] == 417 and not b417['accepted'] and not b417['original_closed']
for e in b418['public_files'] + b417['public_files']:
    assert sha(e['path']) == e['sha256']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in b417['public_files']] + [B417]
paths += [R / n for n in ['audit_and_stage_native289_whole_paper418_ROOT_20261009.py', 'retain_ROOT417_whole_proof_and_precise_scope_20261009.py', 'prepare_native291_whole417418_actual_representation_and_J_defect_20261009.py', 'launch_frozen_native291_checked_20261009.py', 'record_verified_checkpoint300_20261009.py', 'capture_terminal_native290_actual_FINAL_20261009.py']]
paths += [C / n for n in ['original-task.json', 'task.json', 'settings.json', 'freeze.json', 'launch-record.json', 'mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation300.json', Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 300 and x['current_active_batch'] == [291]
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
    x.update(updated_utc=now, github_pending_checkpoint=dict(continuation=301, prepared_utc=now, manifest=str(M), expected_parent=prior['commit_sha'], push_complete=False), next_work='Verify NONFORCE301 whole UNREVIEWED417418 affine dual rays/quantitative Jensen separation and quasi-uniform maximizing sequences/exact prescribed-mu J loss, plus qualified native291 metadata. Native291 active mathematics excluded, native290 terminal five-note mathematics unread and excluded. Compiler unverified; counts/editor unchanged.')
    write(p, x)
write(F / 'current-research-status.json', dict(recorded_utc=now, fully_solved_original_atoms=x['fully_solved_original_atoms'], solved=16, open=26, accepted_scoped_papers=97, current_active_batch=[291], new_papers=[417,418], whole_unique_current_proofs_ROOT_physically_read=True, native289_ALL_actual_four_five_field_notes_and1166_line_source_and_distinct389_line_expansion_read=True, native289_whole_source_and_companion_ROOT_literally_reconstructed=True, ROOT417_complete_293_line_source_read=True, new_primary_reading_credit_in418=0, existing15_whole_primary_unit_reading_and_exact_application_qualifications_retained=True, current_compilation='UNVERIFIED: current418 request pending,417 pending request predates added proof, no success observed', native290_terminal_new_mathematics_NOT_read_or_published=True, active_native291_mathematics_NOT_read_or_published=True, UNREVIEWED=True, original_closed=False, accepted=False, primary_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json', dict(recorded_utc=now, paper415='first actual request connection closed before answer; second pending, no success observed', paper416='first actual request pending, no success observed', paper417='first pending request preceded added Green derivation/generated-fixed-point corollary; current revision UNVERIFIED', paper418='first actual request on current unchanged source pending, no success observed', compiler_verified=False, source_errors_NOT_reported=True, sources_preserved=True, no_local_TeX_or_plugin_install=True, protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint301: quasi-uniform maximizers, exact prescribed-measure loss and dual convexity\n\nWhole UNREVIEWED ROOT418 retains every actual FINAL field of FOUR settled native289 notes, the entire1166-line56580-byte source, distinct389-line18264-byte residual expansion,2407844-byte whole companion, current complete TXT/JSON ledgers/verdict/residual and seven native programs as inert DATA. ROOT physically read every current unique proof. Independent literal reconstruction verified the whole source and native companion; every artifact note differs from actual FINAL by one trailing LF only. The same15 complete immediate primary units were ROOT read in415, with their exact current application judgment and qualifications retained. This gives no extra fresh-primary-reading credit, and inherited recursive/geometric/nonalgebraization/generated/descent audits remain incomplete.\n\nA single actual fast maximizing sequence has simultaneous quasi-uniform convergence outside ordinary open sets of arbitrarily small bounded-MA capacity on every fixed test-energy sublevel. It yields a Borel limsup, uniform integral tails, and actual finite maxima with energy AND I error bounded by the summable tail. Those maxima uniformly maximize the limiting MA measure. For EVERY arbitrary-support finite-full-dual prescribed measure mu, the Borel limsup is mu-integrable and the absolute-integral distance tends EXACTLY to J, equal to the finite-max objective loss. J=0 is equivalent to the missing L1(mu)/full-objective step, but has not been proved. Any full-point USC excess requires small-capacity open spikes accumulating there; small capacity alone cannot exclude this. Continuity of all tail suprema would give an actual original generated representative with MA=nu, but the antecedent and nu=mu remain unproved.\n\nWhole independent ROOT417 gives affine full-dual rays from mu to Vmu, all canonical invariants along them, uniform convergence of approximate maximizers with varying ray parameters, and the actual-test lower bound J_t>=t(1-t)|int h(Vmu0-Vmu1)|^2/(48L). Distinct weak-limit images force strict dual convexity; global strict convexity would imply V identity but is not established. Both complete proofs and qualified source/scope records are retained. No new original closure or acceptance.\n\nNative291 includes WHOLE417418 and qualified sources to pursue original analytic representation and prescribed-measure existence. User-selected local Xean with official signed-in Codex gpt-6.1-sol xhigh, ONE running campaign, at mostTWO. Only frozen/launch metadata are published, no active mathematics or hot feedback. Native290 completed and its five-note actual FINAL is retained unread, excluded until independent full review. Desktop compile requests remain pending/unverified;417 request predates its final added proof. No success is claimed. Full literal primary bodies/pixels/books LOCALONLY, protected P16.4 editor OPEN UNCHANGED. Counts16/42 original solved,26OPEN,97accepted scoped papers unchanged. NONFORCE checkpoint verifies all blobs, native Git root, every actual file path and branch/commit.\n')
files = [dict(local=str(p), path='research-checkpoints/continuation301/' + str(p.relative_to(F)), bytes=p.stat().st_size, sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), solved=16, remaining_open=26, accepted_scoped_papers=97, commit_message='Checkpoint quasi-uniform maximizers, exact prescribed-measure loss and quantitative dual separation', scope='Whole UNREVIEWED417418 and qualified frozen native291; compiler unverified, active291 and unread290 mathematics excluded, original P16.7 OPEN.'))
items = files + [dict(local=str(M), path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation301.json', bytes=M.stat().st_size, sha256=sha(M))]
git = ['git', '--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation301.index')
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
API = G / 'api-recovery-continuation301'
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
