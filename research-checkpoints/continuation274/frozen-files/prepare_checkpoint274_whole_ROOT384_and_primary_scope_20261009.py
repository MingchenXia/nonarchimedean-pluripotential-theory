from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation274-publication-records'; M=G/'upload-manifest-continuation274.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation273.json')
assert prior['commit_sha']=='8e30699ac521247446811756102a57dcd8b1ee9c'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==273
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
P=K/'P16.7-continuation384-multiscale-branch-dual-and-critical-tail-working-paper-20261009.tex'
B=K/'P16.7-continuation384-ROOT-whole-proof-source-scope-and-binding-20261009.json'
assert sha(P)=='ab3ba82088c0105adf7bfe8a10e887dbc443b7a19e236956cc3ca09dfbde9990'
assert sha(B)=='104270b5de7f5e67e9421c5d0755ba445c86c47a726756da33f005e5f3fa6f95'
assert not load(B)['whole_original_solved'] and not load(B)['new_accepted_paper']
items=[]; statuses=[]
for q in [271,272]:
    c=next((R/f'campaigns/round-{q}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    statuses.append((q,st)); items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
active=[e['round'] for e in items if e['unsettled_calls']]; assert len(active)<=2
F.mkdir(); S=F/'frozen-status-only'; S.mkdir()
for q,st in statuses:write(S/f'round{q}-public-native-status.json',st)
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    assert 'primary-data' not in str(rel) and 'immutable-book-context' not in str(rel)
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
for p in [P,B,R/'bind_ROOT384_whole_multiscale_branch_dual_20261009.py',R/'record_ROOT_Gerritzen1977_full_text_and_Picard_decomposition_pixels_20261009.py',R/'record_verified_checkpoint273_20261009.py',G/'push-receipt-continuation273.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]:freeze(p)
meta=R/'primary-data-LOCALONLY/P16.7-polyannulus-Picard-primary-20261008/public-ROOT-Gerritzen1977-full-text-and-decomposition-reading.json'
assert sha(meta)=='83b666ebc5477f3ae9a6733734ae503cc0e655997325dcae31df48c8d9a1c94a'
dest=F/'public-primary-metadata'; dest.mkdir(); shutil.copyfile(meta,dest/meta.name)
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,solved=16,open=26,accepted_papers=97,status='UNREVIEWED complete conditional ROOT384; no original closure/acceptance',entire_new_proof='All initial saved source ROOT physically read in two untruncated intervals, final zero-profile amendment fully read; unchanged body identity not separate new reading. Every finite branch combination, full calibrated softmax-gradient proof and analytic tests, exact cubic energy, exact pencil/radial duals and sharp critical atomic family retained.',conditional_inputs='Exactly enumerated quotient geometry and ordinary generated bounded calculus/reference products/calibration from whole383, itself under independent native272 review. No new correctness grant. Full proof establishes implication from those assumptions.',new_measure_result='Single-pencil finite iff weak tail O(t^(-2/3)); finite-combination radial dual finite iff tail in L^(3/2)(dt). Countable actual analytic atom family critical beta2/3 passes pencil but has infinite conditional full bounded dual. Excluded-energy measure is not an original admissible counterexample.',finite_depth_atom='Pencil and radial restricted dual for raw mass2 at fixed analyticGauss depthN0 both1/6+5N0/3. Neither full bounded admissibility nor solution nor atom-cap claim.',primary_reading='Fresh complete CLDv2 5.8.1-6 immediate integration unit ROOT read; full literal retained LOCALONLY. Whole Gerritzen1977 retained OCR text read untruncated plus final formfeed, printed31-33 whole pixels repair entire3.1-3.2 formulas/immediate proofs. Section2 local-triviality deeper dependency not fully source-pixel repaired; no new global Pic correctness grant.',compiler='ROOT384 request213 pending, no diagnostic/success/PDF returned. Existing requests pending/unverified; protected P16.4 editor OPEN UNCHANGED.',all_full_primary_bodies_literal_units_pixels_and_new_full_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,no_active_native271272_math_read_or_hot_feedback=True,no_count_increase=True))
(F/'README.md').write_text('Checkpoint274: multiscale branch energy and critical tail\n\n16/42 original problems solved,26 OPEN,97 accepted papers unchanged. Complete ROOT384 is a conditional UNREVIEWED working paper. It proves the exact multiscale cubic energy/analytic atom formula and distinguishes a weak tail bound from the stronger L^(3/2) tail condition. A critical countable analytic atomic measure has finite pencil dual but infinite conditional full bounded dual. It is therefore excluded by energy, not an admissible counterexample to the original equation.\n\nExact bounded calculus and quotient assumptions from whole383 are stated openly; independent native272 review continues. Native271 continues the envelope chain, maximum TWO, no active mathematics feedback. Fixed finite-depth atomic restricted dual is calculated exactly; full admissibility and existence remain OPEN.\n\nFresh full CLD immediate integration unit and Gerritzen1977 OCR/full decomposition pixels retained locally, with precise dependency boundaries. All primary bodies/units/pixels/book context bodies LOCALONLY; public source records are metadata. Source programs inert DATA. Compiler pending, protected editor unchanged. NONFORCE upload requires exact independent tree, file bindings and fresh branch verification.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=274,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify274 whole conditional ROOT384/source boundaries. Independent native271/272 continue, maximum TWO; capture completed only. Future full independent384 review required; no hot feedback or full-admissibility shortcut.16solved26OPEN97accepted unchanged; protected editor unchanged.'); write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation274/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint complete multiscale branch dual and critical analytic tail',scope='Entire conditional ROOT384 proof UNREVIEWED; rawmass2 actual analytic tests, exact radial L^(3/2) criterion and excluded critical measure. Full P16.7 OPEN;16solved26OPEN97accepted unchanged. Full primary and book bodies LOCALONLY; no active feedback/editor change.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
