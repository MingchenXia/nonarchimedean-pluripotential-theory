from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation275-publication-records'; M=G/'upload-manifest-continuation275.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation274.json'); assert prior['commit_sha']=='1d9276b93a30c6ad00d030b3a8d4521e0975b284'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==274
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
binders=[K/'P16.7-continuation385-ROOT-whole-proof-source-scope-and-binding-20261009.json',K/'P12.3-round271-whole-candidate386-ROOT-proof-source-scope-and-binding-20261009.json',K/'P16.7-round272-whole-candidate387-ROOT-proof-source-scope-and-binding-20261009.json']
assert [sha(p) for p in binders]==['2b5eac68918f10ccb5423ff982318051dbb431e5131c9008705661411ce830a9','6b4a9f44944eb42e7b125320bea939d2ebe9a5a2bb43236077b79f7dff58ec90','d3ce5e9f3aff42c2d6755481f1197706b95067cea2001400491b276a32192769']
for p in binders:assert not load(p)['whole_original_solved'] and not load(p)['new_accepted_paper']
C=R/'campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1'; fr=load(C/'freeze.json')
assert fr['input_sha256']=='f730f0a2b17a5bb4eb18307e8ed48b8121c183c70775ce7016f546f73c5e6ad3' and not (C/'work.sqlite').exists()
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    assert sha(C/name)==fr[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
F.mkdir(); S=F/'frozen-status-only'; S.mkdir(); items=[]
for q in [271,272]:
    c=next((R/f'campaigns/round-{q}').iterdir()); st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert st['status']=='completed' and not st['error'] and st['calls']['unsettled']==0
    write(S/f'round{q}-public-native-status.json',st); items.append(dict(round=q,status='completed',unsettled_calls=0,observed_utc=st['observedAt']))
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    assert 'primary-data' not in str(rel) and 'immutable-book-context' not in str(rel)
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
for p in binders+[K/'P16.7-continuation385-generated-radial-finite-energy-equations-working-paper-20261009.tex',R/'bind_ROOT385_whole_generated_radial_E1_20261009.py',R/'capture_completed_native271_actual_FINAL_20261009.py',R/'read_entire_native271_actual_notes_20261009.py',R/'read_whole_native271_artifacts_without_execution_20261009.py',R/'audit_native271_whole_proof_and_literal_TeX_identity_20261009.py',R/'stage_completed_native271_whole386_ROOT_20261009.py',R/'capture_completed_native272_actual_FINAL_20261009.py',R/'read_completed_native272_whole_fields_20261009.py',R/'audit_native272_whole_proof_and_literal_TeX_identity_20261009.py',R/'stage_completed_native272_whole387_ROOT_20261009.py',R/'prepare_native273_whole385387_full_bounded_dual_20261009.py',R/'record_verified_checkpoint274_20261009.py',G/'push-receipt-continuation274.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]:freeze(p)
for dirname in [K/'public-P12.3-continuation386-repaired-perfect-charp-and-Jensen-residual-whole-candidate',K/'public-P16.7-continuation387-two-atom-and-nonpluripolar-radial-whole-candidate',C/'immutable-mathematical-DATA']:
    for p in sorted(dirname.rglob('*')):
        if p.is_file():freeze(p)
for p in sorted(C.glob('*.json')):freeze(p)
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,solved=16,open=26,accepted_papers=97,status='Complete385386387 UNREVIEWED; no original closure or new acceptance',papers=dict(ROOT385='Conditional continuous-Stieltjes generated radial E1/comparison/variableconstantdecreasing continuity/separatedcompactness/equationrange; fullproofROOTread; all-direction recognition not proved',native271_whole386='Generatorwise HH repair replaces flawed382 arbitraryelement/imperfect extension route; exact isolated perfectcharp/cover/conductor chain; new Jensen subprobability dual and CE iff weaklowerhemicontinuity, generalgate stillOPEN',native272_whole387='Whole independent383 scopedpositive under disclosed foundations; new allrealdepth twoactualGaussatoms, finite/countable radial equations, genuine nonpluripolargrid fullmass; fulloriginal all-direction/arbitrarysupportOPEN'),all_five_native272_actual_FINAL_fields_and_DIFFERENT_expanded_proofs_ROOT_read=True,all_nine_native271_actual_FINAL_fields_and_DIFFERENT_expanded_proofs_ROOT_read=True,whole_TeX_and_companion_identity_not_new_duplicate_physical_reading=True,all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,source_reading_boundaries='New exact native readings attributed native, not fresh ROOT wholeproof-tree. Fresh ROOT CLDv2 full8.8.6/12.2.7-10/5.2.5 units retainedLOCALONLY. Deep[50]Theorem3.4 notfreshfullproof. Native272 rawCT/DucrosPDFretrievalfailed; complete appliedunits retained. ROOT priorHH02 entire3.4 correction retained; historical deepHH/Kunz/duality background qualified.',next_campaign=dict(round=273,status='FROZEN NOT LAUNCHED',model='gpt-6.1-sol',reasoning='xhigh',only_grants=[],whole_math_files=183,target='Independentwhole384385387383; prove FULL boundedCtheta IBP/variation/concavity and exact FULLCtheta radial finite-dual admissibility, then fulloriginal intrinsicE1'),compiler='ROOT385 request5,386 request26,387 request47 pending with no diagnostics/success/PDF. Other requests pending/unverified. No new tab/editor change.',supplied_or_native_programs_executed_or_imported=False,no_active_math_feedback=True,no_count_increase=True,maximum_concurrent_campaigns=2))
(F/'README.md').write_text('Checkpoint275: repaired envelopes and intrinsic radial analytic equations\n\n16/42 original problems solved;26 OPEN;97 accepted scoped papers unchanged. Complete working papers385,386,387 remain UNREVIEWED. The P12.3 repair applies Jacobian normalization generator by generator and proves a Jensen-measure continuity criterion; the general lower-hemicontinuity gate is unresolved. The P16.7 papers construct continuous-Stieltjes and discrete radial energy domains, identify both actual Gauss atoms, and solve explicit bounded/countable branch measures through genuine products. They do not solve the original full all-direction arbitrary-support equation.\n\nNext native273 is frozen, not launched. It independently verifies the complete new proofs and investigates the full bounded Ctheta tangent inequality and full-class finite dual for genuine radial solution measures. Maximum TWO native campaigns, signed-in gpt-6.1-sol xhigh; no active mathematics feedback. Full primary bodies, literal units, pixels and book-context bodies remain LOCALONLY. Programs are inert DATA. Built-in compilation remains unverified; protected editor OPEN UNCHANGED. NONFORCE upload requires exact native tree, remote file bindings and fresh branch verification.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=[],current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2,next_frozen_rounds=[273]),github_pending_checkpoint=dict(continuation=275,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify275 entire385386387 and frozen273 before launch. Then native273 whole independent radial/IBP/fullCtheta dual gate; prepare next P12.3 Jensen residual, at mostTWO. Fulloriginal counts16solved26OPEN97accepted unchanged; protected editor unchanged.'); write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv'); files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation275/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint complete repaired envelopes and intrinsic radial analytic equations',scope='Entire385386387 UNREVIEWED and frozen273; exact genuine branch products and HHrepair/Jensen residual. Full originalsOPEN;16solved26OPEN97accepted unchanged. All primary/book bodies LOCALONLY; no nativeprogram execution or editor change.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),next_frozen_round=273,solved=16,open=26,papers=97),indent=2))
