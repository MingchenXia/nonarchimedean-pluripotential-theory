"""Freeze authorized public checkpoint and independently compute every Git object binding."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation305-publication-records'
M = G / 'upload-manifest-continuation305.json'
D = K / 'public-P16.7-continuation424-every-Gauss-Radon-and-strict-projection-gap-unreviewed'
B423 = K / 'P12.3-continuation423-ROOT-whole-paper-source-scope-and-binding-20261009.json'
C = R / 'campaigns/round-295/P16.7-whole424-nonskeletal-equation-and-full-representation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation304.json')
assert prior['commit_sha'] == 'd267b02b6807ca63a69848509c14ad551775e770' and prior['tree_sha'] == 'fd13398a5f899835f1a4f9e2fea4f15b5f020ea3' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for b in [load(B423),load(D / 'ROOT-whole-proof-source-scope-and-binding.json')]:
    assert not b['accepted'] and not b['original_closed']
    for e in b['public_files']:
        assert sha(e['path']) == e['sha256']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in load(B423)['public_files']] + [B423]
paths += [R / n for n in ['audit_and_stage_native293_whole_paper424_ROOT_20261009.py','retain_ROOT423_whole_proof_and_precise_scope_20261009.py','read_terminal_native293_whole_actual_notes_20261009.py','capture_terminal_native293_actual_FINAL_20261009.py','prepare_native295_whole424_nonskeletal_existence_20261009.py','launch_frozen_native295_checked_20261009.py','record_verified_checkpoint304_20261009.py']]
paths += [C / n for n in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation304.json',Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 304 and y['current_active_batch'] == [294,295]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
F.mkdir()
for p in paths:
    rel = p.relative_to(R)
    assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    q = F / 'frozen-files' / rel
    q.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,q)
    assert sha(q) == sha(p)
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=305,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE305 whole UNREVIEWED423424 and qualified frozen295 nonskeletal proposals. Active294295 math excluded. Independently develop conductor-cover generalization; full original residual and compiler remain open, counts/editor unchanged.')
    write(p,y)
write(F / 'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=y['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[294,295],new_papers=[423,424],all_current_actual_five_fields_distinct_expansions_and_unique_scopes_ROOT_physically_read=True,actual293_FINAL_and_native_assembled_notes_structurally_identical_checked=True,actual292_prior_fields_distinct_NOT_confused=True,whole_current_source_and_native_companion_ROOT_literal_reconstruction=True,every202_incoming_math_body_whole_retained_in_ROOT424_companion=True,containment_deduplication_ONLY_storage_NOT_new_reading=True,six_complete_immediate_analytic_units_freshly_ROOT_reread=True,other_nine_reused_immediate_units_NO_fresh_reading_credit=True,ENTIRE_G331_prior420_read_and_current423_application_rejudged=True,full_recursive_deeper_source_audit_NOT_complete=True,compilation_UNVERIFIED=True,frozen295_nonskeletal_and_representation_routes_UNPROVED_proposals_only=True,active294295_mathematics_NOT_read_or_published=True,UNREVIEWED=True,original_closed=False,accepted=False,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json',dict(recorded_utc=now,paper415='first connection closed, second pending',paper416='first pending',paper417='pending prior revision, current unverified',paper418='first pending',paper419='first pending',paper420='first correct-current-source request pending',paper421='first pending',paper422='first pending',paper423='first pending',paper424='first pending; function cell857',compiler_verified=False,no_success_observed=True,source_errors_NOT_reported=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint305: same-centre conductor obstruction and every-Gauss-Radon equation\n\nWHOLE UNREVIEWED ROOT423 gives an irreducible nonnormal threefold with a SINGLE regular local normalization centre and a nonsingleton conductor fibre. In characteristic!=2, R=k[t²,ty,y,s] localized at the origin has conductor yS, conductor quotient k[t²,s] inside k[t,s], and common target valuation u=s² of the lifts t=s and t=-s. The signed actual primary-model obstacle F=-v(m)-v((y(t+s))+m^L)+v((y)+m^L), L>2, has no greatest C/D minorant and non-USC raw envelope. Actual relatively ample primary competitors and a generic normalization monomial valuation prove uniform error>=L-2 for EVERY degree and failure stable under perturbations< (L-2)/2. Added affine variables preserve the obstruction. Pinch surface without s has a bijective normalization boundary and qualified CE; adding one affine line destroys CE. Characteristic2 of this quadratic example remains a radicial boundary-equivalence case. This is a NONNORMAL example, not a general normal higher-dimensional CE counterexample. Whole325LF paper and169927-byte qualified companion are retained. Independently written after294 launch, before any293294 mathematics inspection, never hot-fed294.\n\nWHOLE UNREVIEWED ROOT424 proves every periodic real Radon probability Alexandrov equation by finite Laguerre minimization, correctly directed conjugation and a proved limiting construction, including atoms and singular measures. Actual positive convex convolution, recursive CLD products, primitive degree-one calibration/raw2!factor and every continuous analytic test lift every Gauss-supported rawmass2 Radon target to a bounded original-C solution on the designated INPUT analytic quotient. Normalized range[-1/2,0], energy[-1,0], FULL dual<=1 attained, actual decreasing G presentation and uniqueness against ALL actual generated solutions sharing a bounded solution are proved at the explicitly named conventional analytic foundation boundary. Every fast family in this sector has J=K=0, canonical nu=mu and R=q.\n\nFor EVERY eligible arbitrary-support input, D(mu)>=D(Gauss projection), equality iff skeletal; continuous invariant full-dual attainment iff skeletal. Actual segment variations give a quantified strict gap. A concrete nonskeletal full-point2Dirac is eligible and has D>=1/6+1/25165824, with no invariant maximizer. Its noninvariant equation and general arbitrary-support existence/representation remain OPEN. Weak-to-uniform skeletal stability and W1 dual/I bounds are proved. Whole2390LF115639-byte standalone and6068217-byte ROOT companion retain every202 incoming mathematical body by exact containment. Native11175965-byte companion was independently literally reconstructed and remains LOCALONLY; nested ancestor duplication is removed only in public storage, never as reading credit. All four actual293 FINAL note fields equal assembled fields structurally; both sets retained. All distinct new proof bodies physically ROOT read, six entire immediate source units freshly reread, other nine carry prior full reading with no fresh credit. Three native programs remain inert DATA. Genuine nonalgebraization/coherent descent and full deeper source/book audit remain unproved.\n\nNative295 frozen metadata has ONLY UNPROVED new nonskeletal equation/recognition routes: dominated bounded-MA input and analytic representation; local translated log-max Dirac construction with entire ordinary-boundary/collar and unit-monodromy checks; actual generated recognition. Native294 remains independently active on conductor and normal residual. Signed-in official Xean Codex gpt-6.1-sol xhigh, maximumTWO. No active294295 mathematical output read/published/hot-fed. Desktop requests are pending/unverified; no success claimed. Literal primary bodies/pixels/books LOCALONLY, protected P16.4 editor OPEN UNCHANGED, counts16/42originals solved,26OPEN,97accepted scoped papers. NONFORCE verification binds exact frozen contents, every actual file path/blob/native Git root/parent/tree/final ref.\n')
files = [dict(local=str(p),path='research-checkpoints/continuation305/' + str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint same-centre conductor failure and every-Gauss-Radon equation',scope='Whole UNREVIEWED423424 and qualified frozen295 nonskeletal proposals; active294295 math excluded, compilation unverified, originals OPEN.'))
items = files + [dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation305.json',bytes=M.stat().st_size,sha256=sha(M))]
git = ['git','--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation305.index')
subprocess.run(git + ['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries = []
groups = {}
for e in items:
    data = Path(e['local']).read_bytes()
    data.decode('utf-8')
    assert hashlib.sha256(data).hexdigest() == e['sha256']
    h = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert subprocess.run(git + ['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip() == h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h))
    groups.setdefault(h,e)
    subprocess.run(git + ['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected = subprocess.run(git + ['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API = G / 'api-recovery-continuation305'
API.mkdir()
chunks = []
chunk = []
size = 0
for h,e in groups.items():
    item = dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text())
    n = len(json.dumps(item,ensure_ascii=True).encode())
    if chunk and size + n > 250000:
        chunks.append(chunk)
        chunk = []
        size = 0
    chunk.append(item)
    size += n
if chunk:
    chunks.append(chunk)
sizes = []
for i,ch in enumerate(chunks):
    p = API / f'content-chunk-{i}.json'
    p.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2) + '\n')
    sizes.append(p.stat().st_size)
write(API / 'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=sizes,commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),unique_blobs=len(groups),content_chunks=len(chunks),content_chunk_bytes=sizes,expected_tree=expected,primary_bodies_published=False),indent=2))
