from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation270-publication-records';M=G/'upload-manifest-continuation270.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation269.json')
assert prior['commit_sha']=='420a9e9014de25faf2f401497c3d718985cbf6d4'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    x=load(R/n);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==269
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
P377=K/'P12.3-continuation377-isolated-positive-characteristic-envelopes-working-paper-20261008.tex'
B377=K/'P12.3-continuation377-ROOT-whole-proof-source-scope-and-binding-20261008.json'
assert sha(P377)=='fac848124b413caa4b5d2184e0aa268d31f54b611126a1cfb7c2e17dc571ec68'
assert sha(B377)=='c59a55ed707b90f261999d3e94d6af3b9a64d397fe0a4f5ae236509c8d050870'
D378=K/'public-P16.7-continuation378-conditional-nonalgebraization-and-divergent-branch-energy-whole-candidate'
B378=K/'P16.7-round267-whole-candidate378-ROOT-proof-source-scope-and-binding-20261008.json'
assert sha(B378)=='b514f388156dc3ada84af02405b8c5a090b9df6da7aa9d0bd55fad903ca492b9'
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
def freeze(p):
    p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);assert not dst.exists();shutil.copyfile(p,dst);assert sha(dst)==sha(p)
for q in [267,268,269]:
    C=next((R/f'campaigns/round-{q}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    write(S/f'round{q}-public-native-status.json',st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
    if q==269:
        assert sha(C/'input.json')=='bbc5a62333c28094d6675c58da293c4b6083c439560066143971d8053b00948e'
        for p in sorted(C.glob('*.json')):freeze(p)
        for sub in ['immutable-mathematical-DATA','whole-book-context-DATA']:
            for p in sorted((C/sub).rglob('*')):
                if p.is_file():freeze(p)
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for p in sorted(D378.rglob('*')):
    if p.is_file():freeze(p)
for p in [P377,B377,B378,K/'round268-actual-native-final.json']:freeze(p)
SOURCES=R/'primary-data-LOCALONLY/P12.3-singular-test-ideal-generation-primary-20261008'
T=F/'public-primary-retrieval-METADATA-ONLY';T.mkdir()
for n in ['public-singular-test-generation-primary-retrieval-records.json','public-Fitting-and-Takagi-primary-retrieval-records.json']:
    shutil.copyfile(SOURCES/n,T/n)
for n in ['bind_ROOT377_whole_proof_source_scope_20261008.py','fetch_public_singular_test_ideal_generation_primary_20261008.py','fetch_public_Fitting_and_Takagi_primary_20261008.py','prepare_native269_whole377_isolated_characteristic_p_20261008.py','launch_frozen_native269_whole377_checked_initialization_20261008.py','capture_completed_native267_actual_FINAL_20261008.py','capture_completed_native268_actual_FINAL_20261008.py','stage_completed_native267_whole378_ROOT_20261008.py','record_verified_checkpoint269_20261008.py']:freeze(R/n)
freeze(G/'push-receipt-continuation269.json');freeze(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py');freeze(Path(__file__))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
    ROOT377='ENTIRE 24904-byte working TeX and source/scope binding ROOT physically read. Proposed canonical-Fitting normal-primary model, paired asymptotic test ideals, singular corrected subadditivity, affine-base trace/Serre generation and ALL-support O(1/m) envelope estimate for normal perfect-charp affine varieties regular off a closed isolated point. UNREVIEWED, native269 independently reconstructing. Relative CM theorem is cited foundation without fresh whole BS book proof; Smolkin finite-field descent printed issue needs independent repair. No original closure or accepted paper.',
    whole378='ENTIRE 58595-byte proof and all five different actual FINAL texts ROOT physically read; full standalone partial and conditional papers retained with exact content-identity coverage. Exact bounded branch energy E(U_N)=-1/6-N/3 and rigid objective 1/6+5N/3 diverges. Rigid atom inadmissible for this bounded dual; full intrinsic E1 remains OPEN. Nonalgebraization conditional on finite-wide-polyannulus Picard gate F_L. All source reading qualifications preserved; native267 new primary claims attributed native267, not ROOT fresh reading.',
    completed268='Exact actual settled native268 FINAL captured from completed/no-error/zero-unsettled state with seven intermediate messages excluded; candidateFALSE. Full ROOT paper and source review still underway, not accepted or closed.',
    frozen269='ENTIRE 152 mathematical files, 4161159 bytes, three whole book contexts, exact original/task/input/settings/freeze/launch retained. Signed-in native Xean Codex gpt-6.1-sol xhigh. Three whole qualified grants unchanged. Ninety full private primary files LOCALONLY. No active mathematical outputs read, hot feedback or supplied/native program execution.',
    compiler='ROOT374 built-in cell7 and ROOT377 cell51 pending. Earlier requests not verified successful. No new tab, source export or installation. Protected P16.4 editor OPEN UNCHANGED.',
    no_count_increase=True,source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,all_full_primary_bodies_literal_source_units_and_pixels_LOCALONLY=True)
write(F/'publication-qualification.json',qual)
(F/'README.md').write_text('Checkpoint270: isolated positive-characteristic envelope draft and full branch-energy paper\n\n16/42 original problems solved, 26 OPEN, 97 accepted papers; no increase. Whole ROOT377 proposes continuity of envelopes for isolated normal perfect-characteristic-p varieties using canonical flattening, paired test ideals, corrected singular subadditivity and an affine-base generation proof. Its full saved proof and source qualifications are retained and independently checked by native269. No acceptance is asserted.\n\nWhole378 preserves the entire conditional nonalgebraization proof, bounded analytic mixed theory, exact circle equations and new branch-energy divergence. The rigid atom has infinite bounded dual energy despite restricted separable finiteness. This is a proved-sector draft with explicit Picard and intrinsic E1 gaps, not an original closure. All actual FINAL and expanded texts are retained separately with complete ROOT reading qualifications.\n\nThe exact completed268 FINAL is captured but its whole paper review is underway. Frozen269 includes the entire mathematical packet and whole book contexts. At most two native campaigns; no active math or hot feedback. Full primary bodies, literal units and pixels remain LOCALONLY; public retrieval files contain only metadata. Native programs are inert DATA. Compiler requests remain unverified; protected editor is unchanged. Authorized NONFORCE push requires exact independent Git tree, blob and fresh branch verification.\n')
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=270,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint270 whole377378 and frozen269. Continue native269 P12.3; prepare independent whole378 P16.7 continuation as second campaign. Read completed268 whole proof/source on bounded chunks; counts16/26/97 unchanged, protected editor unchanged.');write(p,x);shutil.copyfile(p,F/n)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation270/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/n;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+n,bytes=p.stat().st_size,sha256=sha(p)))
assert len({x['path'] for x in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint isolated positive-characteristic envelope draft and full branch-energy paper',scope='16 solved,26 OPEN,97 accepted papers. ENTIRE377378 mathematical drafts UNREVIEWED; frozen269 entire152 math and book contexts. Completed268 actual FINAL captured, whole review ongoing. No acceptance, active math feedback, primary-body upload or editor changes.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
