from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation300-publication-records'
M = G / 'upload-manifest-continuation300.json'
D = K / 'public-P12.3-continuation416-excellent-normal-surface-envelopes-in-equal-and-mixed-characteristic-unreviewed'
C = R / 'campaigns/round-290/P12.3-whole416-higher-dimensional-and-conductor-envelope-residual'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation299.json')
assert prior['commit_sha'] == '3e62fd915dcf705bd8ba0c5773dd01561d85fbea' and prior['tree_sha'] == 'fa6ccbf6279f0fc12e515630867939c132676652' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
b = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper'] == 416 and not b['accepted'] and not b['original_closed'] and b['compiler'] == 'NOT_YET_INVOKED_FOR416'
for e in b['public_files']:
    assert sha(e['path']) == e['sha256']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [R / n for n in ['audit_and_stage_native288_whole_paper416_ROOT_20261009.py', 'check_native288_whole_literal_assembly_ROOT_20261009.py', 'prepare_native290_whole416_higher_dimension_envelope_residual_20261009.py', 'launch_frozen_native290_checked_20261009.py', 'record_verified_checkpoint299_20261009.py']]
paths += [C / n for n in ['original-task.json', 'task.json', 'settings.json', 'freeze.json', 'launch-record.json', 'mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation299.json', Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 299 and x['current_active_batch'] == [289, 290]
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
    x.update(updated_utc=now, github_pending_checkpoint=dict(continuation=300, prepared_utc=now, manifest=str(M), expected_parent=prior['commit_sha'], push_complete=False), next_work='Verify NONFORCE300 whole UNREVIEWED416 excellent normal surface envelope proof and qualified native290 metadata. Actual416 desktop compilation pending UNVERIFIED, no success claim; native289/290 active mathematics excluded. Counts/editor unchanged. Continue original P12.3 higher-dimensional/conductor and P16.7 actual analytic representation.')
    write(p, x)
write(F / 'current-research-status.json', dict(recorded_utc=now, fully_solved_original_atoms=x['fully_solved_original_atoms'], solved=16, open=26, accepted_scoped_papers=97, current_active_batch=[289, 290], new_papers=[416], all_four_actual_five_field_notes_and_four_distinct_expanded_proofs_ROOT_physically_read=True, full_immediate_applied_primary_units_ROOT_freshly_read=6, whole_source_and_companion_literal_reconstruction_verified=True, whole416_compilation='UNVERIFIED: actual desktop request pending; historical binding predates invocation', whole415_compilation='UNVERIFIED: first desktop request connection closed before answer; second pending', active_native289_and290_math_NOT_read_or_published=True, UNREVIEWED=True, original_closed=False, accepted=False, primary_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json', dict(recorded_utc=now, paper415=dict(attempt1='connection closed before server request was answered', attempt2='pending, no result or success observed'), paper416=dict(attempt1='pending, no result or success observed'), compilation_verified=False, source_errors_NOT_reported=True, sources_preserved=True, immutable_frozen_campaign_inputs_unchanged=True, no_local_TeX_or_plugin_installation=True, protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint300: excellent normal surface envelopes in equal and mixed characteristic\n\nWhole UNREVIEWED ROOT416 retains all five actual FINAL fields of all FOUR settled native288 notes, all FOUR distinct expanded proofs, the complete274815-byte standalone paper and3899070-byte whole companion, current unique preamble/abstract/ledgers/verdict/residual and four native programs as inert DATA. ROOT physically read every current unique proof and six complete immediate applied Stacks units. Independent literal reconstruction checked the entire source and native companion; current actual FINAL and artifact notes differ by exactly one trailing LF per note. Prior413 and entire qualifiedG331 remain whole, with EVERY inherited source/application/read-limit qualification. Whole retention is not fresh recursive reading. No native program was executed/imported; finite diagnostics are not proof certification.\n\nThe new scoped theorem covers EVERY excellent normal local DOMAIN of dimension TWO, arbitrary residue field, in equal and mixed characteristic. It constructs actual regular PRIMARY refinements, a greatest all-curve-nef exceptional coefficient vector, and geometric envelope equality against every primary ideal competitor on EVERY semivaluation support, using proper centres in valued quotient fields. Signed-model density then proves continuous geometric envelopes for EVERY finite continuous signed obstacle and canonical every-degree uniform convergence. A two-blowup example gives envelope -3v((x^2,y))/2, including Z_p[[u]]. No O(1/m), canonical finite generation or semiampleness follows from rational nef coefficients. General higher-dimensional normal regularity and unrestricted nonnormal/conductor descent are still OPEN. The generic-section-on-an-exceptional-curve argument does not give all-curve-nef divisorial parts in higher dimension.\n\nAll six immediate primary units were freshly ROOT physically read whole at these applications; deeper Lipman surface-resolution dependencies and conventional algebraic foundations remain explicitly qualified. Full primary bodies/pixels/books are LOCALONLY. The protected P16.4 editor is OPEN UNCHANGED. The desktop compiler was invoked for416 but remains pending: compilation is UNVERIFIED. Its binding predates invocation. The first415 request returned connection closed before answer; its second request remains pending. No success is claimed.\n\nNative290 is frozen with WHOLE416/413 and exact qualified sources to address higher-dimensional normal and conductor original residuals. Native289 addresses P16.7 actual analytic representation and prescribed-measure existence. User-selected local Xean plus official signed-in Codex gpt-6.1-sol xhigh, exactly TWO admitted campaigns, no active mathematics or hot feedback read/published. Only qualified frozen/launch metadata are public. Counts16/42 original solved,26OPEN,97accepted scoped papers unchanged. No new original closure or acceptance. NONFORCE checkpoint verifies all blobs, independently constructed Git tree, every actual file binding and final branch/commit.\n')
files = [dict(local=str(p), path='research-checkpoints/continuation300/' + str(p.relative_to(F)), bytes=p.stat().st_size, sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), solved=16, remaining_open=26, accepted_scoped_papers=97, commit_message='Checkpoint geometric excellent normal surface envelopes in equal and mixed characteristic', scope='Whole UNREVIEWED416 and qualified frozen native290 metadata; compiler unverified, active289/290 math excluded, original P12.3 OPEN.'))
items = files + [dict(local=str(M), path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation300.json', bytes=M.stat().st_size, sha256=sha(M))]
git = ['git', '--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation300.index')
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
API = G / 'api-recovery-continuation300'
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
