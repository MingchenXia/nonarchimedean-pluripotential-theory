"""Freeze authorized whole-proof publication and independently calculate native Git objects."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
F = G / 'continuation306-publication-records'
M = G / 'upload-manifest-continuation306.json'
D = K / 'public-P12.3-continuation426-irreducible-centres-exact-filtration-and-surface-criterion-unreviewed'
B425 = K / 'P12.3-continuation425-ROOT-whole-paper-source-scope-and-binding-20261009.json'
C = R / 'campaigns/round-296/P12.3-whole425426-same-centre-and-normal-quotient-envelopes'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2) + '\n')
assert not F.exists() and not M.exists()
prior = load(G / 'push-receipt-continuation305.json')
assert prior['commit_sha'] == 'd91fed0faba2f946f7488c2e2534424dccd8bc48' and prior['tree_sha'] == '68017fa634fe8f9cd9d9bc13e8bc10ce081c5c5e' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for b in [load(B425),load(D / 'ROOT-whole-proof-source-scope-and-binding.json')]:
    assert not b['accepted'] and not b['original_closed']
    for e in b['public_files']:
        assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in load(B425)['public_files']] + [B425]
paths += [R / n for n in ['audit_and_stage_native294_whole_paper426_ROOT_20261009.py','retain_ROOT425_whole_proof_and_precise_scope_20261009.py','read_terminal_native294_whole_actual_notes_20261009.py','capture_terminal_native294_actual_FINAL_20261009.py','prepare_native296_whole425426_conductor_and_normal_quotient_20261009.py','launch_frozen_native296_checked_20261009.py','record_verified_checkpoint305_20261009.py']]
paths += [C / n for n in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [G / 'push-receipt-continuation305.json',Path(__file__)]
assert len(paths) == len(set(paths))
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 305 and y['current_active_batch'] == [296]
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
launch = load(C / 'launch-record.json')
assert launch['current_active_batch'] == [296] and launch['public_status']['calls']['admitted'] == 1
assert [e['status']['status'] for e in launch['previous_campaign_compact_statuses']] == ['completed','completed']
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
    y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=306,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE306 whole UNREVIEWED425426 plus frozen296. Native295 terminal compact status only, mathematics not yet read/published; capture after checkpoint. Native296 isolated active, no hot feedback; compiler unverified, counts/editor unchanged.')
    write(p,y)
write(F / 'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=y['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[296],native295_terminal_math_NOT_yet_read_or_published=True,new_papers=[425,426],whole_current_five_actual_notes_all_five_fields_and_five_distinct_expanded_proofs_ROOT_physically_read=True,current294_actual_vs_assembled_fields_DISTINCT_retained_separately=True,whole426_source_and_native_companion_ROOT_passive_literal_reconstruction=True,every43_incoming_math_body_whole_retained_in_ROOT426_companion=True,whole_independent425_proof_physically_ROOT_read_and_retained_before294_math_inspection=True,containment_deduplication_ONLY_storage_NOT_new_reading=True,ENTIRE_G331_prior420_whole_read_and_exact_current_application_rejudged=True,current_G331_boundary_density_sections_freshly_reread=True,current_fresh_literal_primary_or_formula_pixel_reading_credit=0,full_recursive_deeper_source_audit_NOT_complete=True,compilation_UNVERIFIED=True,frozen296_general_conductor_and_normal_quotient_routes_UNPROVED_proposals_only=True,active296_mathematics_NOT_read_or_published=True,UNREVIEWED=True,original_closed=False,accepted=False,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F / 'desktop-compiler-observations.json',dict(recorded_utc=now,paper425='actual native desktop request pending, cell886',paper426='actual native desktop request pending, cell919',compiler_verified=False,no_success_observed=True,source_errors_NOT_reported=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
(F / 'README.md').write_text('Checkpoint306: conductor-cover dichotomy and irreducible-centre envelope criterion\n\nWhole UNREVIEWED ROOT425 proves the single-centre conductor-power-cover family over EVERY field, including fields with no nontrivial ground-field roots of unity. R=k[t^e,y,yt,...,yt^(e-1),s,Z] at the origin has a single regular local finite normalization S=k[t,y,s,Z], exact conductor yS and conductor quotient k[t^e,s,Z] inside k[t,s,Z]. If the exponent has nontrivial prime-to-characteristic part, a finite coefficient extension supplies two actual centred semivaluations t=s and t=zeta*s on the ORIGINAL ring, not a change of the base problem. For every dimension>=3 an actual signed primary-model obstacle has no greatest C/D minorant, non-USC raw envelope and EVERY-degree canonical uniform error>=L-2, L>2. All competitors have actual relatively ample primary Cartier presentations before limits. Pure p-power exponents in characteristic p have a bijective full normalization boundary by a direct Frobenius formula even over imperfect fields; CE is equivalent to the regular normal source, without an unproved higher-dimensional positive-characteristic CE assertion. Without the extra affine parameter s, every exponent over every field gives qualified surface CE by the single conductor DVR boundary. Adding one affine line destroys CE in the separable cases. Complete formal-power-series analogues and exact primary-gauge transport are proved. Whole374LF17763-byte paper and201875-byte qualified companion retained. This independent proof was completed and retained before294 mathematics inspection and was never hot-fed.\n\nWhole UNREVIEWED ROOT426 proves a general obstruction whenever one full normalization fibre joins DISTINCT marked normal centres, even for a DOMAIN semilocal normalization. Actual CRT separators/conductor multipliers, every-support primary inequalities and all-curve-positive competitors give a positive uniform canonical gap in every degree and quantified perturbation stability. For the irreducible self-crossing v^2=u^2(1+u), characteristic!=2, it gives the complete raw envelope, EVERY-degree canonical ideal and exact uniform error ceil(3m/2)/m-1>=1/2, in every dimension>=2; excellent DVR surfaces with2 invertible have the same formulas. For EVERY continuous signed obstacle on its surface, greatest C/D existence is equivalent to equality of the two normal-source envelope values on the conductor. Positive primary truncation/descent proves the formula. Exact pinch normalization/conductor/same-centre fibre and normal-centre uniform coercivity are proved. The coercivity barrier only blocks the distinct-centre CRT method at one centre, and does not contradict independent425: its divisorial bound depends on deep weightL. No normal higher-dimensional counterexample is asserted.\n\nEntire5030LF906751-byte426 standalone, all FIVE ACTUAL settled FINAL notes with ALL FIVE fields, all FIVE DISTINCT expanded proofs, exact current scopes and7085210-byte ROOT whole companion are retained. Actual and assembled summary/detail/text DIFFER and remain separate. Every43 incoming mathematical body is retained WHOLE by exact containment. Native whole companion was passively literally reconstructed and remains LOCALONLY; containment deduplication is solely storage, not new reading/audit/correctness credit. FOUR native programs were physically read as inert DATA, never executed/imported. ENTIRE qualified G331 is the sole incoming correctness grant, including all model/support/radial/source/audit qualifications. Same fourteen complete immediate source units and two formula pixels carry earlier ROOT reading; current fresh primary/pixel credit0. Exact applications independently rejudged, current G331 boundary/density sections reread, deeper recursive source/book audit remains OPEN.\n\nNative296 frozen input contains WHOLE425426 and explicitly UNPROVED general-conductor and genuinely NORMAL finite-group-quotient routes. It runs the user-authorized signed-in official Xean native Codex gpt-6.1-sol xhigh, maximumTWO campaigns. At launch295 had completed; only its compact status was observed, no mathematical output read or published here. Native296 active mathematics excluded and no hot feedback. All desktop compilation requests remain pending/unverified; no success claimed. Full originalP12.3 universal regularity/classification and other original targets remain OPEN. Literal primary bodies/pixels/books LOCALONLY, protected P16.4 editor OPEN UNCHANGED, counts16/42originals solved,26OPEN,97accepted scoped papers. NONFORCE publication binds exact frozen contents, every actual path/blob/native Git root/parent/tree/final ref.\n')
files = [dict(local=str(p),path='research-checkpoints/continuation306/' + str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint conductor-cover dichotomy and irreducible-centre envelope criterion',scope='Whole UNREVIEWED425426 and qualified frozen296; terminal295 and active296 math excluded, compilation unverified, originals OPEN.'))
items = files + [dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation306.json',bytes=M.stat().st_size,sha256=sha(M))]
git = ['git','--git-dir=' + str(G / 'native-continuation56.git')]
env = dict(os.environ)
env['GIT_INDEX_FILE'] = str(G / 'native-continuation306.index')
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
API = G / 'api-recovery-continuation306'
API.mkdir()
chunks, chunk, size = [], [], 0
for h,e in groups.items():
    item = dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text())
    n = len(json.dumps(item,ensure_ascii=True).encode())
    if chunk and size + n > 250000:
        chunks.append(chunk)
        chunk, size = [], 0
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
