from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation302-publication-records'
M = G / 'upload-manifest-continuation302.json'
D = K / 'public-P12.3-continuation419-conductor-descent-cusp-envelopes-and-threefold-obstruction-unreviewed'
C = R / 'campaigns/round-292/P12.3-whole419-nonsingleton-conductor-and-normal-envelope-residual'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation301.json')
assert prior['commit_sha'] == '359819768bb095ba106e3510cce15eaf3c663118' and prior['tree_sha'] == 'd7d757540a979bc5e41463a59bb3befac380a0fa' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
b = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper'] == 419 and not b['accepted'] and not b['original_closed'] and b['compiler'] == 'NOT_YET_INVOKED_FOR419'
for e in b['public_files']:
    assert sha(e['path']) == e['sha256']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [R / n for n in ['audit_and_stage_native290_whole_paper419_ROOT_20261009.py', 'read_terminal_native290_whole_actual_notes_20261009.py', 'prepare_native292_whole419_nonsingleton_conductor_counterexample_20261009.py', 'launch_frozen_native292_checked_20261009.py', 'record_verified_checkpoint301_20261009.py']]
paths += [C / n for n in ['original-task.json', 'task.json', 'settings.json', 'freeze.json', 'launch-record.json', 'mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation301.json', Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 301 and x['current_active_batch'] == [291, 292]
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
    x.update(updated_utc=now, github_pending_checkpoint=dict(continuation=302, prepared_utc=now, manifest=str(M), expected_parent=prior['commit_sha'], push_complete=False), next_work='Verify NONFORCE302 whole UNREVIEWED419 conductor/cusp envelopes and precise actual-primary threefold obstruction, plus frozen native292 metadata containing ONLY unproved ROOT conductor proposal. Active291292 mathematics excluded. Compiler unverified, counts/editor unchanged.')
    write(p, x)
write(F / 'current-research-status.json', dict(recorded_utc=now, fully_solved_original_atoms=x['fully_solved_original_atoms'], solved=16, open=26, accepted_scoped_papers=97, current_active_batch=[291,292], new_papers=[419], all_five_actual_five_field_notes_and_all_five_distinct_expanded_proofs_ROOT_physically_read=True, complete_current_unique_preamble_abstract_ledger_verdict_residual_read=True, whole_source_and_native_companion_ROOT_literally_reconstructed=True, new_fresh_primary_reading_credit=0, prior14_complete_surface_SH_BFJ_units_and_formula_pixels_bound_with_qualifications=True, current_applications_ROOT_rejudged=True, current_compilation='UNVERIFIED: actual419 desktop request pending, no success observed', new_native292_conductor_construction_UNPROVED_ROOT_proposal_only=True, active_native291292_mathematics_NOT_read_or_published=True, UNREVIEWED=True, original_closed=False, accepted=False, primary_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json', dict(recorded_utc=now, paper415='first actual request connection closed before answer; second pending', paper416='first actual request pending', paper417='first pending request preceded final added proof, current revision unverified', paper418='first actual unchanged-source request pending', paper419='first actual unchanged-source request pending', compiler_verified=False, no_success_observed=True, source_errors_NOT_reported=True, sources_preserved=True, no_local_TeX_or_plugin_install=True, protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint302: full-boundary conductor descent, cusp envelopes and an actual threefold obstruction\n\nWhole UNREVIEWED ROOT419 retains every actual FINAL field of FIVE terminal native290 notes, all FIVE distinct expanded proofs, entire423961-byte standalone source and4461168-byte ROOT companion, complete unique current source ledger/verdict/unchanged original residual and three native programs as inert DATA. ROOT read all unique actual/expanded proofs and current scope, and independently reconstructed every byte of the whole source and native companion. An initial source1-150 display was truncated; all needed units were read separately and that display gives no extra reading credit. Full14 immediate surface/SH/BFJ units and actual formula pixels retain prior reading qualifications; current applications rejudged, no new fresh-primary-reading credit or full recursive historical audit.\n\nFull boundary-bijective normalization gives order/isometric C/D envelope equivalence, including primary-conductor and finite-radicial reduced-conductor-quotient criteria. All infinite-conductor supports remain. Numerical-semigroup cusp germs have continuous geometric envelopes in every dimension at exact algebraically closed characteristic-zero smooth source hypotheses; dimension-two scope works over every field and Z_p[[t^2,t^3]] provides a nonnormal mixed-characteristic case. A cancellation-sensitive cusp obstacle has canonical uniform error<=2/m in EVERY degree, dimension and characteristic; in characteristic zero it has no finite-real raw ideal presentation and its canonical algebra is not finitely generated. Every positive approximant is an actual negative effective relatively ample primary-model Cartier divisor, positive on every contracted integral curve.\n\nOn an explicit ACTUAL primary regular threefold model, the negative divisorial part of I=(z)+m^2 restricts to H-eP-eQ and has degree-1 on the joining line. This disproves the higher-dimensional generic-section-to-all-curve-nef step, not continuous-envelope regularity. General normal higher-dimensional and nonsingleton-conductor envelope questions remain open, and no original closure or new paper acceptance is claimed.\n\nNative292 receives WHOLE419/416/413 and a new UNPROVED ROOT proposal: two smooth surfaces glued along a curve might have a continuous obstacle with no greatest geometric C/D minorant. The worker must independently prove or refute full geometric cone comparison, all-support continuity/positivity, infinite-conductor gluing and the non-USC/no-greatest conclusion. The proposal in frozen task metadata is not a terminal result or accepted premise. Native291 advances original P16.7 representation/J/equation. User-selected Xean signed-in official Codex gpt-6.1-sol xhigh, at most TWO; active mathematics and hot feedback excluded. Desktop requests remain pending/unverified, no successful compilation claimed. Full primary literal bodies/pixels/books LOCALONLY; protected P16.4 editor OPEN UNCHANGED. Counts16/42 original solved,26OPEN,97accepted scoped papers. NONFORCE publication verifies all blobs, native Git root, every actual file path and branch/commit.\n')
files = [dict(local=str(p), path='research-checkpoints/continuation302/' + str(p.relative_to(F)), bytes=p.stat().st_size, sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), solved=16, remaining_open=26, accepted_scoped_papers=97, commit_message='Checkpoint conductor descent, quantitative cusp envelopes and actual threefold obstruction', scope='Whole UNREVIEWED419 and qualified frozen native292 including unproved ROOT conductor proposal; active291292 mathematics excluded, compiler unverified, original P12.3 OPEN.'))
items = files + [dict(local=str(M), path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation302.json', bytes=M.stat().st_size, sha256=sha(M))]
git = ['git', '--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation302.index')
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
API = G / 'api-recovery-continuation302'
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
