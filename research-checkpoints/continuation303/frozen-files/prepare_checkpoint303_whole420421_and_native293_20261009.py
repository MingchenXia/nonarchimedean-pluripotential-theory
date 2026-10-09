from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation303-publication-records'
M = G / 'upload-manifest-continuation303.json'
D = K / 'public-P16.7-continuation421-concentration-defects-and-invariant-attainment-unreviewed'
C = R / 'campaigns/round-293/P16.7-whole421-actual-Gauss-Radon-existence-and-general-attainment'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation302.json')
assert prior['commit_sha'] == '1aeb16838fc957d36947eb70664cab1ea15335e6' and prior['tree_sha'] == '385fa2a14f07af6eba6eac2096fc1cba09e68ced' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
b421 = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
B420 = K / 'P12.3-continuation420-ROOT-whole-paper-source-scope-and-binding-20261009.json'
b420 = load(B420)
for b in [b420, b421]:
    assert not b['accepted'] and not b['original_closed']
    for e in b['public_files']:
        assert sha(e['path']) == e['sha256']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in b420['public_files']] + [B420]
paths += [R / n for n in ['audit_and_stage_native291_whole_paper421_ROOT_20261009.py', 'retain_ROOT420_whole_proof_and_precise_scope_20261009.py', 'capture_terminal_native291_actual_FINAL_20261009.py', 'prepare_native293_whole421_actual_Gauss_Radon_existence_20261009.py', 'launch_frozen_native293_checked_20261009.py', 'record_verified_checkpoint302_20261009.py']]
paths += [C / n for n in ['original-task.json', 'task.json', 'settings.json', 'freeze.json', 'launch-record.json', 'mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation302.json', Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 302 and y['current_active_batch'] == [292, 293]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
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
    y = load(p)
    y.update(updated_utc=now, github_pending_checkpoint=dict(continuation=303, prepared_utc=now, manifest=str(M), expected_parent=prior['commit_sha'], push_complete=False), next_work='Verify NONFORCE303 WHOLE UNREVIEWED420421 and frozen293 metadata including ONLY unproved existence proposal. Active292293 math excluded. Continue exact original residual; compiler unverified, counts/editor unchanged.')
    write(p, y)
write(F / 'current-research-status.json', dict(recorded_utc=now, fully_solved_original_atoms=y['fully_solved_original_atoms'], solved=16, open=26, accepted_scoped_papers=97, current_active_batch=[292,293], new_papers=[420,421], all_current_actual_fields_whole_proofs_distinct_expansions_and_unique_scopes_ROOT_physically_read=True, source_and_companion_ROOT_literal_reconstruction=True, ROOT420_entire_qualified_G331_freshly_read_at_application=True, ROOT421_current_fresh_primary_credit=0, ROOT421_prior_fifteen_complete_CLD_GR_units_same_domain_reapplied_with_qualifications=True, full_recursive_deeper_source_audit_NOT_complete=True, compilation_UNVERIFIED=True, new_native293_actual_Radon_existence_route_UNPROVED_proposal_only=True, active_native292293_mathematics_NOT_read_or_published=True, UNREVIEWED=True, original_closed=False, accepted=False, primary_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json', dict(recorded_utc=now, paper415='first connection closed before answer; second pending', paper416='first pending', paper417='pending prior revision; current revision unverified', paper418='first pending', paper419='first pending', paper420='first correct-current-source actual request pending', paper421='first actual source request pending', compiler_verified=False, no_success_observed=True, source_errors_NOT_reported=True, sources_preserved=True, no_local_TeX_or_plugin_install=True, protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint303: normal-crossing envelope failure and actual maximizer concentration defects\n\nWHOLE UNREVIEWED ROOT420 proves an actual nonnormal envelope obstruction in every dimension>=2 over every field. For R=k[x,y,z...]_(origin)/(xy), the continuous obstacle equals -a on one branch and -a-(b-a)/v(y) on the other, for arbitrary0<a<b. The exact canonical primary filtration is m^ceil(mb)+x*m^(ceil(ma)-1). Every approximant is an ACTUAL negative effective relatively ample primary-model divisor, positive on every contracted integral curve before taking limits. The full qualified G331 geometric comparison proves raw C/D envelopes equal -a at finite-x points and -b on the x-infinite branch. A sequence converges on EVERY ring element to the infinite-conductor point, proving raw non-USC, no greatest C/D minorant, uniform canonical gap>=b-a and failure of positivity of USC regularization. Normalized source envelopes differ on conductor fibres. The proof includes all supports, arbitrary gauges and the dimension-one distinction. This is a genuine nonnormal failure, not a normal higher-dimensional CE counterexample or full original P12.3 solution. Entire93375-byte qualified G331 physically ROOT read at current application; deeper audit remains qualified.\n\nWHOLE UNREVIEWED ROOT421 retains all four native291 five-field FINAL notes, entire85806-byte1797-LF standalone and distinct17296-byte367-LF new proofs, complete current TXT/JSON ledgers/verdict/unchanged residual and three native programs as inert DATA. ROOT physically read all current actual/formal bodies and independently literally reconstructed source and5321683-byte native companion; entire5347835-byte ROOT companion includes exact ROOT application limits. Fifteen prior complete immediate CLD/GR units reapplied at the same analytic torus hypotheses, with ZERO new fresh-primary-reading credit or complete deeper recursive audit. Positive prescribed-measure concentration clusters have massJ and support in the intersection of closures of exceptional opens. Exact truncation identities separate bounded exceptional-set oscillation and deep negative tails. Actual bounded full-dual attainment impliesJ0 for every fast family. An attained smooth invariant strictly positive coordinate Hessian identifies the equation by actual variations and Gauss dominance. FULL Dmu0 iffmu=theta² for EVERY eligible arbitrary-support measure. General attainment, representation and every-measure existence remain open.\n\nFrozen native293 metadata contains an UNPROVED proposal to construct ACTUAL CLD solutions for every Gauss-supported Radon measure, including atoms, via periodic Alexandrov/Laguerre construction and fully checked analytic lift, while advancing general original attainment/recognition. No narrowed sector is counted as original closure. Native292 independently continues its frozen P12.3 conductor/normal residual. Both use user-selected Xean signed-in official Codex gpt-6.1-sol xhigh; maximumTWO. No active292293 mathematics or hot feedback published. Desktop requests420421 and earlier drafts remain pending/unverified; no successful compilation claimed. Literal primary bodies/pixels/books LOCALONLY. Protected P16.4 editor OPEN UNCHANGED. Counts16/42 originals solved,26OPEN,97accepted scoped papers. NONFORCE publication independently verifies native Git root, every unique blob, actual file-path binding, parent/tree and final ref.\n')
files = [dict(local=str(p), path='research-checkpoints/continuation303/' + str(p.relative_to(F)), bytes=p.stat().st_size, sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), solved=16, remaining_open=26, accepted_scoped_papers=97, commit_message='Checkpoint nonnormal envelope counterexample and variational concentration defects', scope='Whole UNREVIEWED420421 and frozen293 unproved existence proposal; active292293 math excluded, compilation unverified, originals OPEN.'))
items = files + [dict(local=str(M), path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation303.json', bytes=M.stat().st_size, sha256=sha(M))]
git = ['git', '--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation303.index')
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
API = G / 'api-recovery-continuation303'
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
