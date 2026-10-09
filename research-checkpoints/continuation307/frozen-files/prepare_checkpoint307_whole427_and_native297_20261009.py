"""Freeze complete427 publication and compute native Git bindings independently."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation307-publication-records'
M = G / 'upload-manifest-continuation307.json'
D = K / 'public-P16.7-continuation427-prescribed-nonskeletal-two-atom-equation-and-dominated-L1-unreviewed'
C = R / 'campaigns/round-297/P16.7-whole427-whole-dirac-and-actual-analytic-representation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p,x: Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation306.json')
assert prior['commit_sha'] == '47246110a56af214776920dc8d4822bed2b38c83' and prior['tree_sha'] == '547946a39592e2da829c623ab3b24a779f0ef8b0' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert not b['accepted'] and not b['original_closed']
for e in b['public_files']:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [R / n for n in ['audit_and_stage_native295_whole_paper427_ROOT_20261009.py','read_terminal_native295_whole_actual_notes_20261009.py','capture_terminal_native295_actual_FINAL_20261009.py','prepare_native297_whole427_whole_dirac_and_actual_representation_20261009.py','launch_frozen_native297_checked_20261009.py','record_verified_checkpoint306_20261009.py']]
paths += [C / n for n in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation306.json',Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 306 and y['current_active_batch'] == [296,297]
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
    y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=307,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE307 WHOLE427 nonskeletal equation and dominatedL1 plus frozen297 unproved original-residual routes. Native296297 isolated active, no mathematics inspection/hot feedback. Compiler unverified, counts/editor unchanged.')
    write(p,y)
write(F / 'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=y['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[296,297],new_papers=[427],whole_current_four_actual_notes_all_five_fields_and_distinct431LF_formal_proof_ROOT_physically_read=True,current295_actual_vs_assembled_fields_structurally_identical_retained_separately=True,whole427_source_and_native_companion_ROOT_passive_literal_reconstruction=True,every46_incoming_math_body_whole_retained_in_ROOT427_companion=True,native_companion_CONTAINS_literal_primary_bodies_and_remains_LOCALONLY=True,all15_literal_primary_carriers_excluded_from_public_companion=True,containment_deduplication_ONLY_storage_NOT_new_reading=True,exact_fixed_fibre_source_applications_ROOT_rejudged=True,two_complete_CLD18_6_units_freshly_ROOT_reread=True,other_thirteen_immediate_units_reused_NO_fresh_reading_credit=True,full_recursive_deeper_source_audit_NOT_complete=True,compilation_UNVERIFIED=True,frozen297_whole_Dirac_multiple_budges_and_recognition_routes_UNPROVED_proposals_only=True,active296297_mathematics_NOT_read_or_published=True,UNREVIEWED=True,original_closed=False,accepted=False,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json',dict(recorded_utc=now,paper427='actual native desktop request pending, cell959',compiler_verified=False,no_success_observed=True,source_errors_NOT_reported=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint307: prescribed nonskeletal equation and dominated-measure convergence\n\nWhole UNREVIEWED ROOT427 constructs an ACTUAL original-C solution for EVERY positive rawmass2 target (2-m)delta_g+m delta_xc, c>0,0<=m<=1, where g is the joint quotient Gauss point and x_c is the Gauss bidisc |zi-1|<=exp(-c). For m>0 the prescribed input is nonskeletal. A finite logarithmic maximum glues on an ORDINARY open collar, not merely at Shilov vertices. Actual degree1 fixed CLD fibres identify MA(q_c)=delta_g+delta_xc and mixed B(q0,qc)=2delta_g. The solution q=q0+sqrt(m)v_c is normalized, has actual decreasing G presentation, E=-1/3-cm^(3/2)/3 and FULL dual D=1/6+2cm^(3/2)/3 attained. Uniqueness holds among ALL actual G solutions, and the canonical nonordered full-point tuple/ordinary upper relaxation is represented by the explicit actual weight in this sector. No positivity is assigned to remaining raw Borel points. The specified half-mixture MA(q)=delta_g+delta_x has E=-3/8,D=1/4. Stretching the explicit segment past its positive range gives an exact negative curve atom, an obstruction to this route only.\n\nEVERY positive rawmass2 input mu dominated by A MA(w), fixed actual bounded w, has finite FULL dual bounded by A(1+Bw)+3A²Bw/2. All maximizing families have a canonical L1(mu) limit. Every fast actual Borel limit u has late quantitative L1 error <=(16A/15)2^(-4j), uniform integrability, bounded-truncation convergence and J=0. This does not create an actual analytic representative or prove MA=mu. The original whole2delta_x is dominated by twice the explicit half-mixture, so its fast integral defect vanishes and its FULL dual lies between3/8 and4; its actual equation remains OPEN.\n\nWhole2820LF137655-byte standalone, complete431LF22233-byte new formal proof, ALL FOUR actual FINAL notes with ALL FIVE fields and separate assembled records, current ledgers/verdict/byte-unchanged residual and6551521-byte ROOT mathematical companion retained. Current actual/assembled fields are structurally identical, independently checked. Every46 supplied mathematical body remains WHOLE by exact containment. Native7161787-byte companion was passively literally reconstructed and remains LOCALONLY because it embeds fifteen literal primary bodies. Public mathematical companion excludes every one of those fifteen carriers. Retention/hashes/finite checks/storage deduplication are not new body-reading or correctness credit. FOUR native programs physically read as inert DATA, never executed/imported. Exact CLD18.6.1/18.6.2 complete statements and proofs freshly ROOT reread for positive radii, ordinary boundaryless separated equidimensional charts, actual translations/inversions and fixed completed-residue-field curves, degree1 coefficient1. Other thirteen entire immediate units carry prior ROOT415/424 reading with no fresh credit; exact applications rejudged. Deeper conventional analytic foundations and genuine nonalgebraization/coherent descent remain unproved here. Original P16.7 remains OPEN.\n\nNative297 frozen metadata contains explicitly UNPROVED routes toward whole-mass nonskeletal Dirac, broader fan/Dirichlet patches, multiple residual bidiscs and actual dominated-measure analytic recognition. Native296 independently pursues normal quotient/conductor geometry. User-selected signed-in official Xean native Codex gpt-6.1-sol xhigh, maximumTWO. No active296297 mathematical output read/published or hot-fed. Desktop compiler requests pending/unverified, no success claimed. Literal primary bodies/pixels/books LOCALONLY, protected P16.4 editor OPEN UNCHANGED, counts16/42originals solved,26OPEN,97accepted scoped papers. NONFORCE publication independently binds exact frozen contents, every file path/blob/native Git root/parent/tree/final ref.\n')
files = [dict(local=str(p),path='research-checkpoints/continuation307/' + str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint prescribed nonskeletal equation and dominated-measure convergence',scope='WHOLE UNREVIEWED427 and qualified frozen297; active296297 math excluded, compiler unverified, original OPEN.'))
items = files + [dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation307.json',bytes=M.stat().st_size,sha256=sha(M))]
git = ['git','--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation307.index')
subprocess.run(git + ['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries, groups = [], {}
for e in items:
    body = Path(e['local']).read_bytes()
    body.decode('utf-8')
    assert hashlib.sha256(body).hexdigest() == e['sha256']
    h = hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()
    assert subprocess.run(git + ['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip() == h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h))
    groups.setdefault(h,e)
    subprocess.run(git + ['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected = subprocess.run(git + ['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API = G / 'api-recovery-continuation307'
API.mkdir()
chunks, chunk, size = [], [], 0
for h,e in groups.items():
    item = dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text())
    n = len(json.dumps(item,ensure_ascii=True).encode())
    if chunk and size+n > 250000:
        chunks.append(chunk)
        chunk,size = [],0
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
