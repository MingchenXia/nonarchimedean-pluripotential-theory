from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation271-publication-records';M=G/'upload-manifest-continuation271.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation270.json');assert prior['commit_sha']=='2730e26317220798fd1695df88a0c7afe0b5abc0'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    x=load(R/n);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==270
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
D379=K/'public-P21.3-continuation379-middle-cone-analytic-trace-and-original-BT-whole-candidate'
B379=K/'P21.3-round268-whole-candidate379-ROOT-proof-source-scope-and-binding-20261008.json'
P380=K/'P12.3-continuation380-relative-regularity-and-Frobenius-generation-working-paper-20261008.tex'
B380=K/'P12.3-continuation380-ROOT-whole-proof-source-scope-and-binding-20261008.json'
assert sha(B379)=='d04fdb0d21c2b2c33b7b680dd334570135942dbdeaabd7a8798bc113ae0b495d'
assert sha(P380)=='6971c895a138d5dec136ecf177d74dad3c01d997fcfd379dbdf01793eeb200e1'
assert sha(B380)=='fa01f551f97d00172f9357bfa5fa4bb113ed2ba8be24a5ae653ecc9f22caeaa3'
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
def freeze(p):
    p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);assert not dst.exists();shutil.copyfile(p,dst);assert sha(dst)==sha(p)
for q in [269,270]:
    C=next((R/f'campaigns/round-{q}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    write(S/f'round{q}-public-native-status.json',st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
    if q==270:
        assert sha(C/'input.json')=='d1c78e45de5408f6e8847aaf0bea375e48eb7fda74f3219d844286790fde9880'
        for p in sorted(C.glob('*.json')):freeze(p)
        for sub in ['immutable-mathematical-DATA','whole-book-context-DATA']:
            for p in sorted((C/sub).rglob('*')):
                if p.is_file():freeze(p)
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for p in sorted(D379.rglob('*')):
    if p.is_file():freeze(p)
for p in [B379,P380,B380]:freeze(p)
for n in ['stage_completed_native268_whole379_ROOT_20261008.py','bind_ROOT380_whole_relative_regularity_20261008.py','prepare_native270_whole378_nonalgebraization_and_intrinsic_E1_20261008.py','launch_frozen_native270_whole378_checked_initialization_20261008.py','record_verified_checkpoint270_20261008.py']:freeze(R/n)
freeze(G/'push-receipt-continuation270.json');freeze(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py');freeze(Path(__file__))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
    whole379='ENTIRE65250-character independent native268 proof, complete four DIFFERENT actualFINAL texts, entire source/application/coverage/verdict ROOT physically read. Full62483-byte TeX exact encoding of read mathematical bodies, no fabricated fresh duplicate reading. Reconstructs all conditional372/369/scalar367/relative368 arguments; off-locus harmonic-approximation extension, actual refined chart FIRST-JET middle PSD bounds, original analytic-dimension finite-fibre foundation. AdditionalF01 complete literal immediate source ROOT freshly read; all other new native primary reading stays native268. Original universal BT-current/pair theorem OPEN. UNREVIEWED; no paper acceptance.',
    whole380='ENTIRE14413-byte ROOT saved paper and all final amendments ROOT physically read. Independent affine-base CM regularity over finite-type algebra of ANY field including finite fields, with no sheaf-flatness. Full faithful-flat/Cech, associated-point hyperplane, dimension/twist/multiplication induction. Perfect-charp Frobenius source finite-list Serre and fixed twist; trace application explicitly CONDITIONAL on finite quotient from arbitrarily late tails, possibly distinct exponents. Veryample H and ample conditions through embedding N; no assumed test-ideal identity, subadditivity or envelope estimate. UNREVIEWED, no original closure or accepted paper. Complete applied currentStacks01YS/02OI/0B5U/0B5T statements/immediateproofs freshly ROOT read, exact retained bodies LOCALONLY; recursive deeper foundations disclosed. Already frozen377/active269 unchanged/no hot feedback.',
    frozen270='ENTIRE99 mathematical files1644648bytes,17 whole book contexts, exact original/task/input/settings/freeze/launch retained. Signed-in Xean native Codex gpt-6.1-sol xhigh; notes=[] zero grants;120 private primary/evidencefilesLOCALONLY. Concrete wide-polyannulus Picard/nonalgebraization foundation plus FULL all-direction intrinsicE1, not restricted separable closure. No active math read or feedback.',
    campaigns='At most TWO: native269 whole377/originalP12.3 and270 whole378/originalP16.7. Inspect only completed no-error zero-unsettled output; preserve exact actual-final versus expanded.',
    compiler='ROOT379 request89 and finalROOT380 request105 pending. ROOT380 earlier98 preceded final amendments. ROOT3747/37751 and older requests unverified. No compiled success/PDF/export/install or newtab claimed; protected P16.4 editor OPEN UNCHANGED.',
    no_count_increase=True,supplied_or_native_programs_executed_or_imported=False,all_full_primary_bodies_literal_units_and_pixels_LOCALONLY=True)
write(F/'publication-qualification.json',qual)
(F/'README.md').write_text('Checkpoint271: complete ordinary-current reconstruction and relative generation lemma\n\nCounts16/42 original problems solved,26 OPEN,97 accepted papers; no increase. Whole379 retains the full independent conditional P21.3 reconstruction, with all four distinct actual/expanded texts, exact middle-cone and analytic-trace hypotheses, and original residual. ROOT physically read the entire proof and additional finite-fibre source. No universal pair theorem or admissible original counterexample.\n\nWhole380 proves relative zero-regularity generation over a finite-type affine base over any field, including finite fields. Its Frobenius corollary gives a fixed generation twist for finite lists of coherent source sheaves. The trace application requires exact arbitrarily late-tail finite quotient presentations; it does not assert test-ideal identities or envelope continuity. Complete proof and primary/source/scope qualifications retained; no hot feedback to active269. Both drafts UNREVIEWED.\n\nFrozen270 contains the complete mathematical packet,17 whole book contexts and exact task/settings/launch. Two native Xean gpt-6.1-sol xhigh campaigns continue on P12.3/P16.7. Full primary bodies, source units and pixels LOCALONLY. Native programs inert DATA. Compiler requests pending, no compiled-success claim. Protected editor unchanged. Regular authorized NONFORCE push requires exact independent Git tree, blob and fresh branch verification.\n')
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=271,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint271 whole379380 and frozen270. Continue TWO native269 P12.3 and270 P16.7; inspect only completed outputs. ROOT independently pursue precise remaining source/model/trace/Picard gates, without active feedback. Counts16/26/97 unchanged; protected editor unchanged.');write(p,x);shutil.copyfile(p,F/n)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation271/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/n;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+n,bytes=p.stat().st_size,sha256=sha(p)))
assert len({x['path'] for x in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint complete ordinary-current reconstruction and relative generation lemma',scope='16 solved,26 OPEN,97 accepted papers. ENTIRE379380 mathematical drafts UNREVIEWED; frozen270 entire99 math and17 book contexts. Native269/270 maxTWO. No acceptance, active feedback, primary-body upload or editor changes.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
