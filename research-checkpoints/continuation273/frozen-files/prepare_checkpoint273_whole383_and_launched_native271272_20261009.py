from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation273-publication-records'; M=G/'upload-manifest-continuation273.json'
C=R/'campaigns/round-272/P16.7-whole383-intrinsic-E1-and-actual-branch-Dirac'
C271=R/'campaigns/round-271/P12.3-whole382380381-independent-proof-and-original-residual'
SP=R/'primary-data-LOCALONLY/P16.7-polyannulus-Picard-primary-20261008'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation272.json')
assert prior['commit_sha']=='06e845d734fa4d48a49a8bfea49c0faeef62c836'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==272
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
assert sha(C/'input.json')=='d98824a4c86633e8ff598cd649c90b03966b4ea9c515b5da1c0899b3e1a8bd3c'
assert load(C/'input.json')['notes']==[]
assert load(C/'launch-record.json')['frozen_input_sha256']==sha(C/'input.json')
assert load(C271/'launch-record.json')['frozen_input_sha256']=='9bf31584728af7c8df71f390c7629bb3f8b07dedf35dbe9afa14dec9be5e770b'
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
D=K/'public-P16.7-continuation383-finite-Picard-nonalgebraization-and-constant-branch-energy-whole-candidate'
B=K/'P16.7-round270-whole-candidate383-ROOT-proof-source-scope-and-binding-20261008.json'
assert sha(B)=='539cb545b31945c40dccf3b09ecf82af4e9f4e2681fc8d2a916a00748dec0151'
assert len([p for p in D.rglob('*') if p.is_file()])==37
assert not load(B)['whole_original_solved'] and not load(B)['new_accepted_paper']
items=[]; statuses=[]
for q,c in [(271,C271),(272,C)]:
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    statuses.append((q,st)); items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
active=[e['round'] for e in items if e['unsettled_calls']]; assert len(active)<=2
F.mkdir(); S=F/'frozen-status-only'; S.mkdir(); frozen=set()
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    assert 'immutable-book-context' not in str(rel) and 'primary-data' not in str(rel)
    if str(rel) in frozen:return
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst)
    assert sha(dst)==sha(p); frozen.add(str(rel))
for q,st in statuses:write(S/f'round{q}-public-native-status.json',st)
for p in sorted(C.glob('*.json')):freeze(p)
for p in sorted((C/'immutable-mathematical-DATA').rglob('*')):
    if p.is_file():freeze(p)
for p in sorted(D.rglob('*')):
    if p.is_file():freeze(p)
freeze(B); freeze(C271/'launch-record.json')
metadata=SP/'public-primary-candidate-retrieval-and-author-correction.json'
dest=F/'public-primary-metadata'; dest.mkdir(); shutil.copyfile(metadata,dest/metadata.name)
for name in ['capture_completed_native270_actual_FINAL_20261008.py','stage_completed_native270_whole383_ROOT_20261008.py','prepare_native272_whole383_intrinsic_E1_and_branch_Dirac_20261008.py','launch_frozen_native272_whole383_checked_20261008.py','launch_frozen_native271_whole382380381_checked_20261008.py','record_verified_checkpoint272_20261008.py','fetch_polyannulus_Picard_primary_candidates_20261008.py']:freeze(R/name)
freeze(G/'push-receipt-continuation272.json'); freeze(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py'); freeze(Path(__file__))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
    whole383='UNREVIEWED entire five-note native270 draft. All five distinct actual/expanded texts and outside fields ROOT physically read; entire66573-character companion/source ledger read in four untruncated overlapping chunks. Entire71651-byteTeX proof bodies verified exact encoding; preamble and three displayed new statements physically read. Identical repeated bodies do not constitute new physical reading.',
    new_mathematics='BaseK C((s)) finite-product discs/circles/wide-annuli Pic=0 by pure-factor SK0/determinant and coherent rational-cover hole filling. Full compatible frames/pole ideals and algebraic-space comparison exclude all separated finite-type baseK algebraizations of the explicit quotient. No arbitrary extension claim. Bounded ordinary generated Ctheta raw mass2 branch pencil: E=-1/6-a^3N/3; constant-energy normalized family disproves UNIFORM compactness. Finite-dual necessary bidisc mass decay N^(-2/3) is not sufficiency/existence.',
    full_original_residual='Intrinsic unbounded all-direction psh/E1, full-mass products/decreasing continuity, useful separated weak compactness, all analytic obstacles/orthogonality, full first variation, sufficient admissibility, EVERY admissible mass2 measure existence and full uniqueness remain OPEN. Restricted circle/separated dual and excluded rigid atom do not solve original P16.7.',
    ROOT_primary='Fresh entire Gruson IV5 immediate unit/disc-circle definitions and Van der Put2.14-2.16.3 unit ROOT physically read. Actual PDF page10 printedJ7-09 entire2.16 descent diagram ROOT visually read; prior page11 printedJ7-10 is not evidence for2.16. Deeper recursive Kiehl/graded foundations not newly completely read. Other fresh source readings/views attributed native270.',
    new_source_candidates='Gerritzen1977, Fresnel/van der Put1983, Kerz/Saito/Tamme2016August full publicPDF/text retained LOCALONLY. Not full proof read/applied. Corrected discovery author attribution: 1983 formal-localization paper is Fresnel/van der Put, NOT Gerritzen. Pro-Picard invariance is not ordinary Pic invariance.',
    frozen_and_launched272='Exact frozen137math2202960bytes/321primary/17wholebook contexts; zero incoming correctness grants. Existing native signed-in gpt-6.1-sol xhigh launchedPID632074, maximum TWO with271. Entire383 independent proof/source review then original intrinsicE1 and UNPROVED finite-depth analyticGauss Dirac investigation. No arbitrary atom cap/admissibility claim.',
    launched271='Existing native signed-in gpt-6.1-sol xhigh PID630586, exact212 whole math and only qualified entireG331/B341/E350 grants. Independent382380381/HH02 generator-perfect-field gates then full originalP12.3. Launch record now public; no active mathematics read or feedback.',
    compiler='Saved standalone source and built-in request177 pending; earlier requests unverified. No success/PDF/export/install/new editor tab claimed. Protected P16.4 editor OPEN UNCHANGED.',
    supplied_or_native_programs_executed_or_imported=False,all_full_primary_bodies_literal_units_source_pixels_and_new_full_book_context_LOCALONLY=True,no_other_ACTIVE_math_read_or_feedback=True,no_count_increase=True)
write(F/'publication-qualification.json',qual)
(F/'README.md').write_text('Checkpoint273: full finite-Picard and branch-energy draft\n\n16/42 original problems solved,26 OPEN,97 accepted papers unchanged. Whole383 is an UNREVIEWED complete five-note draft with every distinct actual/expanded text and source/scope evidence retained. Base-field finite Picard and nonalgebraization are new claims undergoing independent verification. The normalized constant-energy branch family excludes uniform compactness; its finite-dual mass bound is necessary only. Full intrinsic P16.7 remains OPEN.\n\nFrozen and launched native272 independently reviews all383 then seeks intrinsicE1/actual finite-depth analyticDirac progress. Launched271 independently reviews the entire positive-characteristic envelope chain. Both use the existing signed-in native Codex gpt-6.1-sol xhigh; maximum TWO, no active mathematics feedback.\n\nFull public Picard primary candidates retained locally; no full proof reading or application claimed. Bibliographic discovery correction identifies Fresnel/van der Put as the 1983 authors. All full primary bodies/units/pixels and new whole book contexts LOCALONLY; public manifests are metadata. Native programs inert DATA. Compiler pending; protected editor unchanged. Authorized NONFORCE push will verify the independent tree, every blob and fresh branch ref.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=273,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify273 full383/frozen and launched272/271 launch. Continue intrinsicE1 and exact primary proof work without reading or feeding active mathematics. Capture completed only.16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.'); write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation273/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({x['path'] for x in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint full finite Picard proof and constant-energy branch family',scope='16solved26OPEN97accepted unchanged. ENTIRE383 UNREVIEWED and frozen/started272;271launch. Exact finite Picard/nonnalgebraization and energy-bounded branch claims. All primary and new full book contexts LOCALONLY. No active feedback/editor change.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
