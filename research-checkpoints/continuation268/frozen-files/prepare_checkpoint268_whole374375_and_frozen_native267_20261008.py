from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation268-publication-records';M=G/'upload-manifest-continuation268.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation267.json');assert prior['commit_sha']=='d3fe5ddd455ddf4cffdef62207d321c87b202b40'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    x=load(R/n);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==267
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
P374=K/'P16.7-continuation374-constant-meromorphic-field-and-nonalgebraization-working-paper-20261008.tex'
B374=K/'P16.7-continuation374-ROOT-whole-proof-source-scope-and-binding-20261008.json'
D375=K/'public-P02.1-continuation375-residue-cardinality-and-extended-logarithmic-series-whole-candidate'
B375=K/'P02.1-round266-whole-candidate375-ROOT-proof-source-scope-and-binding-20261008.json'
assert sha(P374)=='dd5aa99c2f0977c40bfc96e2542a874059ab14a69fd078eda508e9925df895bc'
assert sha(B374)=='9d5ef3ea90c18388aaea83825655e832fd6ea19b4d9b8f757fb1245ccc24d1d9'
assert sha(D375/'P02.1-paper.tex')=='9e40baaa81c9326382668d0c59dedaf7a1f8cee252610033d54ad7eb3c692bbd'
assert sha(B375)=='4937f35b947ac4d8540aafa98efca5ab29d3a225493c3cd56e64696cbbdc4c92'
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
def freeze(p):
    p=Path(p);rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);assert not dst.exists()
    shutil.copyfile(p,dst);assert sha(dst)==sha(p)
for q in [265,266,267]:
    C=next((R/f'campaigns/round-{q}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    write(S/f'round{q}-public-native-status.json',st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
    if q==267:
        assert sha(C/'input.json')=='266c6d8e83e4f17e6a8ea01ad1b3513714bd895a511ce732c6367df32d265fea'
        for p in sorted(C.glob('*.json')):freeze(p)
        for sub in ['immutable-mathematical-DATA','whole-book-context-DATA']:
            for p in sorted((C/sub).rglob('*')):
                if p.is_file():freeze(p)
assert all(e['status']=='completed' and e['unsettled_calls']==0 for e in items if e['round'] in [265,266])
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for p in [P374,B374,B375,K/'round265-actual-native-final.json',K/'round266-actual-native-final.json']:freeze(p)
for p in sorted(D375.rglob('*')):
    if p.is_file():freeze(p)
helpers=['bind_whole_ROOT374_meromorphic_field_proof_and_primary_reading_20261008.py','fetch_public_period_primary_notes_20261008.py','fetch_public_period_Stacks_and_Gruson_primary_20261008.py','capture_completed_native265_actual_FINAL_20261008.py','capture_completed_native266_actual_FINAL_20261008.py','stage_completed_native266_whole375_ROOT_20261008.py','prepare_native267_whole373374_nonalgebraization_and_original_E1_20261008.py','launch_frozen_native267_whole373374_checked_initialization_20261008.py','record_verified_checkpoint267_20261008.py']
for n in helpers:freeze(R/n)
freeze(G/'push-receipt-continuation267.json');freeze(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py');freeze(Path(__file__))
period=R/'primary-data-LOCALONLY/P16.7-period-algebraization-primary-20261008'
for n in ['public-period-notes-retrieval-records.json','public-period-Stacks-Gruson-retrieval-records.json']:shutil.copyfile(period/n,F/n)
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
    whole374='ENTIRE21246byteROOT standalone proof read and bound with exact applied primary units/source scopes: constant meromorphic field and no separatedfiniteTYPEscheme/algebraicspace algebraization of explicit analytic2torus. UNREVIEWED. General wideannulus-base factoriality FOUNDATION F printedVanDerPut3.4.8 wider than actualGrusonIV5 pureproducts; explicit acceptance gate, not an unconditional audited source grant. GlobalPic infiniteproducts and arbitrarymeromorphic theta fractions and algebraicspace rational injection all included. EntireP16.7 intrinsicE1 equation still OPEN.',
    whole375='ENTIRE31852byteTex/28437bytecompanion, ALL3actual settledFINAL and differentexpandednote fields, source/scope/coverage physically ROOTread. Partial boundary jump sequencecriterion iff residuecountable for eachnontriviallyvaluedK; explicitdecreasingNETeveryK. Givennegativeanalyticlogseries including negativeinfinity has explicitdecreasingrealPLSEQUENCE. Scalar nativejump notpullback. Generalallclassicalpshgeometricclassification OPEN. No original or paper acceptance.',
    source_reading='ROOT freshly read exact GR classical4.1/4.2/4.3 complete immediate proofs, repaired nativeledgerrange ending1202 beforeTheorem4.3starts1204. Other appliedprimaryreading attributednative266, hashes/retention notROOTphysicalreading. ENTIRE374 sourceapplicationunits/proofs and nineactualPDFpixels read previously bound; fullbodies/literalunits/pixels LOCALONLY. Recursivefoundations disclosed.',
    native265='Settled completed candidateFALSE exact53743byte actualFINAL10notes preserved WHOLE as DATA. ROOT entire mathematical reading NOT YET complete at this frozencheckpoint; no correctness verdict. Reports whole370371 reconstruction and fixedACTUALsmoothprimarymodel perfectcharp theorem, conditionalSM all-continuousCE. Higherdimensional/infiniteQ/modelgates OPEN.',
    native267='ONE running Xean native signed-in gpt-6.1-sol xhigh exactinput/task/freeze/launch and ENTIRE64mathfiles1216047bytes/17bookcontexts retained;93wholeprivateprimaryfiles keptLOCALONLY. IndependentWHOLE373374 and foundationgate reconstruction then originalall-supportintrinsicE1 theory. MaxTWO; notes=[]/grants=[]; no active mathreading/hotfeedback.',
    compiler='ROOT final374 request244 and375 request258 pending NOdiagnostics/success; older370125/371146/372178 pending. Native375 build claims retained separately as native observations, not ROOT confirmation. No newtab; protectedP16.4editorOPENUNCHANGED.',
    no_acceptance_or_count_increase=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,source_bodies_pixels_LOCALONLY=True,protected_editor_open_unchanged=True)
write(F/'publication-qualification.json',qual)
(F/'README.md').write_text('''Checkpoint268: whole nonalgebraization working proof and boundary regularization partial draft

16/42 original problems solved,26OPEN,97 accepted papers. No original closure or paper acceptance.

Whole374 proves the complete meromorphic-field route for an explicit analytic two-torus, including compatible global frames, common theta fractions and algebraic-space rational injection. It remains an UNREVIEWED working proof using the explicitly disclosed wideannulus-base factoriality foundationF. The printed Van der Put statement is broader than the newly read Gruson pureproduct theorem, so this source scope is a mandatory acceptance gate. Full intrinsic P16.7 finite-energy operator/equation remains OPEN.

Whole375 gives a sharp residue-countability criterion for sequential regularization of one classical boundary jump and an explicit negative analytic logarithmic-series sector with extended poles. The boundary jump always admits decreasing nets, so its sequence obstruction is not a net obstruction. Every arbitrary classical psh input and the original geometric classification are not covered. Its entire paper/proof, actual settled FINAL, different expanded note variant and all scope/source qualifications are retained. Native source-reading range mismatch at GR Theorem4.3 was freshly repaired by ROOT; other primary reading remains attributed native rather than inferred from hashes.

Native265 completed with candidateFALSE; exact complete FINAL is preserved as DATA before ROOT finishes whole mathematical reading. Native267 independently reconstructs ENTIRE373/374 and all needed foundations before pushing toward full all-support intrinsic finite-energy theory. Its whole frozen64 mathematical files and17 book contexts accompany exact task/input/settings/launch metadata;93 private primary bodies/pixels remain LOCALONLY. At most TWO native campaigns. Supplied/native programs inert DATA never executed/imported; no active mathreading/hotfeedback, no compiler success claimed, protected P16.4 editor OPEN UNCHANGED. Authorized regular NONFORCE GitHub checkpoint requires independent Git tree/allblob/freshref verification.
''')
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=268,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint268 whole374375 and frozennative267. Read ENTIRE settled native265 actualFINAL/paper/source/scope then stage376; continue ONE native267 independent373374/originalP16.7. Next free slot WHOLE372 P21.3 independentcompletion or originalremainingatom after exactscope review.16solved26OPEN97papers; protectededitorOPENUNCHANGED; no activeoutputmath/hotfeedback.');write(p,x);shutil.copyfile(p,F/n)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation268/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/n;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+n,bytes=p.stat().st_size,sha256=sha(p)))
assert len({x['path'] for x in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole nonalgebraization working proof and boundary regularization draft',scope='16solved26OPEN97papers. Whole374 foundationF scope gate; whole375 sharp singlejump sequencecriterion and logarithmicinputsector partialonly. Exactsettled265FINAL preserved beforeROOTwholemathread; frozennative267 ENTIRE373374 independent originalall-supportE1. MaxTWO, no grants/hotfeedback; primarybodies/pixelsLOCALONLY; no countincrease.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
