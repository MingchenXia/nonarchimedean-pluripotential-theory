from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation269-publication-records';M=G/'upload-manifest-continuation269.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation268.json');assert prior['commit_sha']=='180e0a53dd1e5937036fe1218a385bab3baa8632'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    x=load(R/n);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==268
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
D=K/'public-P12.3-continuation376-perfect-characteristic-smooth-primary-envelope-whole-candidate'
B=K/'P12.3-round265-whole-candidate376-ROOT-proof-source-scope-and-binding-20261008.json'
assert sha(D/'P12.3-paper.tex')=='43480f01e61978fbce6dcb6a2c41ad79612c3b62f8e69e8859de3534b3ec2e01'
assert sha(D/'whole-proof.md')=='e321e064ae871f21a6868d19c2de5ced9b35c5152397e09352d8f03681ff02fa'
assert sha(B)=='df51bbc3ae73f654165bc13d9014c080a1e208dcaf0482fdf6ba38ba43a36f0d'
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
def freeze(p):
    p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);assert not dst.exists();shutil.copyfile(p,dst);assert sha(dst)==sha(p)
for q in [267,268]:
    C=next((R/f'campaigns/round-{q}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    write(S/f'round{q}-public-native-status.json',st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
    if q==268:
        assert sha(C/'input.json')=='2d47ca1faa5fbdbf207997db843f100ac4edae28a9711ce224e4657f4a252eed'
        for p in sorted(C.glob('*.json')):freeze(p)
        for sub in ['immutable-mathematical-DATA','whole-book-context-DATA']:
            for p in sorted((C/sub).rglob('*')):
                if p.is_file():freeze(p)
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for p in sorted(D.rglob('*')):
    if p.is_file():freeze(p)
freeze(B)
for n in ['stage_completed_native265_whole376_ROOT_20261008.py','prepare_native268_whole372_and_original_arbitrary_BT_current_20261008.py','launch_frozen_native268_whole372_checked_initialization_20261008.py','record_verified_checkpoint268_20261008.py']:freeze(R/n)
freeze(G/'push-receipt-continuation268.json');freeze(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py');freeze(Path(__file__))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
    whole376='WHOLE60670byte independent native265 proof ALL10 expanded bodies exactsubstrings, ALL10different actualFINALfields ROOTphysicallyread, entire source/scope/coverage/verdict/search. Full649388byteTex/646429byteMD preserves entireG331/B341/E350 exact qualifiedgrants; ROOTchecked whole encoding/content identity, no fabricatedfreshduplicate physicalreading. New perfectcharp FIXED ACTUALsmoothPRIMARYY integralCartierobstacle uniform0<=p-g_m<=c v(J)/m<=cN/m ALLsupport; fullyquantifiedSM=>allCONTCE proved conditional, surfaceregime established. Generalhigherdim/model/infiniteQscope OPEN. No originalclosure or paperacceptance.',
    source_scope='Native265 complete appliedimmediate units attributednative265, not newROOTwholeprimaryreading. PriorROOT371 fullGJKM4/Mustata3+4.1/Keeler1.5+entirev5erratum preserved. GJKM smoothPERFECTcharp PROJECTIVEoverAFFINE exact; Mustata4.1 projectiveALGclosed alone insufficient; KYonY only. WholeCossartPiltant320page proof notread/applied, primarymodelgate no grant or disproof. Allprimary bodies/literalunits/pixels LOCALONLY.',
    campaigns='TWO signed-in Xean nativeCodex gpt-6.1-sol xhigh:267 whole373374 nonalgebraizationfoundation audit then originalintrinsicall-supportE1;268 whole372 middlecone/scalarformtransfer/analytictrace-removability audit then originalP21.3 arbitrarypositive doubleclosedcurrent. Entire78math1409030bytes/4bookcontext and exact268task/input/settings/freeze/launch retained;75privateprimaryfiles LOCALONLY. notes=[]/grants=[] maxTWO; noactiveoutputmathread orhotfeedback.',
    compiler='Built-in ROOT376 request282 pending NOdiagnostics/success. Final374244/375258 and older370125/371146/372178 also pending; noPDFexport or newtab. Native376 requiresfontspec/fvextra/DejaVu; savedsource preserved, no localcompilerinstallation. ProtectedP16.4editorOPENUNCHANGED.',
    no_count_increase=True,source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,protected_editor_open_unchanged=True)
write(F/'publication-qualification.json',qual)
(F/'README.md').write_text('''Checkpoint269: whole perfect-characteristic smooth-primary envelope draft and two campaigns

16/42 original problems solved,26OPEN,97 accepted papers. No original closure or paper acceptance.

Whole376 independently reconstructs all earlier surface/isolated-characteristic-zero/smooth/finite-cover/conductor/curve envelope arguments and all energy/capacity diagnostics. Its new theorem proves uniform geometric approximation on ALL support quotients for integral Cartier obstacles on a FIXED ACTUAL smooth primary model over a perfect characteristic-p field. The fully quantified common smooth-primary-model condition SM implies all-continuous envelopes, then extended USC/decreasing-net theory; normal algebraic surfaces satisfy SM. Higher-dimensional model existence, general characteristic-zero infinite-Q supports, mixed characteristic and arbitrary nonalgebraic/nonclosed normal excellent scope remain OPEN.

The complete ten new proof bodies and all ten different actual settled FINAL objects have been read. Full manuscript/TeX includes exact whole qualified G331/B341/E350 grants; content/encoding identity is recorded separately from fresh physical reading. Entire source application/scope/coverage/decision and corrected source hypotheses are retained. Current native primary reading is attributed native265, with previous ROOT371 reading preserved; hashes do not become fresh reading. Whole Cossart-Piltant proof was not read/applied. Primary bodies, literal source units and PDF pixels remain LOCALONLY. Native programs inert DATA never executed/imported. Compiler requests still pending, no success/PDFexport claimed.

Two native Xean signed-in gpt-6.1-sol xhigh campaigns continue:267 independent whole373374 nonalgebraization foundations and full P16.7 intrinsic finite-energy theory;268 independent whole372 middle-cone and analytic-trace removability and original P21.3 arbitrary positive doubly closed currents. Entire frozen268 mathematical packet, book contexts, exact original/task/input/settings/launch metadata are included. At most TWO campaigns; no active mathematical output reading/hotfeedback. Protected P16.4 editor OPEN UNCHANGED. Authorized regular NONFORCE checkpoint requires independent Git tree/allblob/freshref verification.
''')
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=269,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint269 ENTIRE376 and frozennative268; continue TWO native267/P16.7 and268/P21.3. Inspect ONLYsettledcomplete output. Research residualP12.3 source/model gates independently while waiting; no active math/hotfeedback.16solved26OPEN97papers; protectededitorOPENUNCHANGED.');write(p,x);shutil.copyfile(p,F/n)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation269/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/n;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+n,bytes=p.stat().st_size,sha256=sha(p)))
assert len({x['path'] for x in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole perfect-characteristic smooth-primary envelope draft and two campaigns',scope='16solved26OPEN97papers. ENTIRE376 proof/Tex/qualifiedgrants/actualFINAL/source-scope remainUNREVIEWED; fixedACTUALsmoothprimarymodel theorem, conditionalSM allCONTCE; higherdim/model/infiniteQ OPEN. Frozen268 whole372/originalP21.3 and267 whole373374/originalP16.7 nativegpt6.1xhigh maxTWO; sourcebodies/pixelsLOCALONLY, noacceptance/hotfeedback.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
