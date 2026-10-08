from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';F=G/'continuation266-publication-records';M=G/'upload-manifest-continuation266.json'
P=K/'P12.3-continuation371-test-ideal-uniform-approximation-on-smooth-primary-models-working-paper-20261008.tex'
B=K/'P12.3-continuation371-ROOT-whole-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation265.json');assert prior['commit_sha']=='b9950c6e2b21fb9c3018f8557c1e97190d24333b'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(P)=='152b79a85a21a0fc70011d758982d7c85366ca9f69a239369609e9302f750506' and sha(B)=='4377ebc1025b2f2dad6fb00d46cf0aa6bcf64778b99b0e086d8f365c431acdba'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
 x=load(R/n);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==265
 assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
for q in [263,264]:
 C=next((R/f'campaigns/round-{q}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed'];write(S/f'round{q}-public-native-status.json',st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
retrieval=R/'primary-data-LOCALONLY/P12.3-test-ideal-uniform-approximation-20261008/public-retrieval-record.json'
shutil.copyfile(retrieval,F/'Mustata-public-primary-retrieval-metadata.json')
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
 proof='ENTIRE17741byteROOT371 unreviewed standalone proof plus ENTIRE10350byteproof/source/scopebinding; allprimaryunit application metadata published, literal whole primary bodies/pixelsLOCALONLY. Whole final mathematical proof ROOT physically read.',
 exact_result='Perfect positive-char k, normal CLOSED affine algebraic germ dim>=2, FIXED ACTUAL smooth primary blowup carrying Cartier obstacle and principalizing gauge: actual primary profiles with0<=P(f_C)-g_m<=c v(J)/m on ALL supports. Raw section-ideal envelope identification by actual normal Cartier order and rational-primary-density, Fekete allindex limit, smooth asymptotic testideals, globalgeneration and fixed ample canonical-twist cancellation. UniformC membership beforeD/energy.',
 sources='Authentic retained WHOLE GJKMv3 Section4/all4.6 immediateproof and fresh PUBLIC Mustata1109.3825v2 Section3 explicitlyperfect/all3.1--3.3 immediateproofs and entire4.1 proof read; latterUGscopeprojectivealgclosed kept, GJKM4.6 gives finite-typeaffinebase/perfect extension. CorrectedKeeler v5 entire1.5 immediateproof and ENTIREerratum freshly read, E2.5 validates uniformvanishing. Recursive BMS/CM/Serre/Hartogs/alteration foundations disclosed.',
 missing='ALL continuous obstacles need actual smooth primary finiteideal principalization hypothesisSM, not proved. NO unconditionalCP3model construction, arbitrarypropercofinality, normal nonisolated/higherdim excellent or mixedchar extension, energy/equation theorem, originalP12.3/P16.3closure or paper/count increase.',
 active_feedback='Whole371held for FUTURE independent native reconstruction, NOT supplied to ACTIVE263or264. At most TWO native gpt-6.1-sol xhigh campaigns, originalsP21.3/P16.7 stillpending.',
 compiler='Built-in requests125/370 and146/371 still pending at source-binding snapshot; no diagnostics/success, source unchanged after146 request, no newtabs/exportPDF.',
 primary_bodies_pixels_LOCALONLY=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,protected_editor_open_unchanged=True))
(F/'README.md').write_text('''Checkpoint266: whole test-ideal envelope approximation working proof

16/42 original problems solved,26OPEN,97 accepted papers. No new acceptance or original closure.

Entire ROOT371 constructs actual primary ideal profiles with uniform error0<=P(f_C)-g_m<=c v(J)/m over ALL semivaluation supports, for a Cartier obstacle on a FIXED ACTUAL smooth primary blowup of a normal CLOSED algebraic germ over a perfect positive-characteristic field. It proves the raw section-ideal envelope identity and all-index Fekete convergence, then uses smooth asymptotic test ideals/global generation plus one fixed ample twist to give uniform geometricC convergence. It supplies no singular test-ideal subadditivity or source-nef recognition.

The extension to ALL finite continuous obstacles requires propertySM: every finiteprimaryidealcollection/gauge admits an ACTUAL smooth primary common blowup. SM is not proved here; merely citing dimension-three resolution, an arbitrary regular alteration or a nonprimary model is insufficient. No unconditional originalP12.3/P16.3 closure or finite-energy analytic equation is claimed. Entire proof/source/scopebinding accompanies the paper; sources are freshly checked at their exact perfect-field/projective/affine-base distinctions, with entire correctedKeeler erratum. Full primary bodies/pixels remainLOCALONLY.

P21.3/native263 and P16.7/native264 continue via signed-in Xean native Codex gpt-6.1-sol xhigh, at most TWO campaigns and ZERO incoming grants. New371 is held for FUTURE independent reconstruction, no ACTIVE feedback or mathematical output reading. No successful compilation/formal certification. Protected P16.4 editor OPEN UNCHANGED, no new tabs/exportPDF. Supplied programs inert DATA never executed. Authorized regular NONFORCE checkpoint verified by independent Git tree/all blobs/fresh reference.
''')
for n in ['active-work.json','checklist-current.json']:
 p=R/n;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=266,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint266 ENTIREnew371 uniformtestidealproof/source/scope. Continue TWO native263/P21.3 and264/P16.7, inspect ONLY settled COMPLETE outputs; next freed slot whole370/371 independent completion/model gate.16solved26OPEN97papers; protected editor OPEN UNCHANGED; no hot feedback.');write(p,x);shutil.copyfile(p,F/n)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 target=target or 'research-checkpoints/continuation266/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for p in sorted(F.rglob('*')):
 if p.is_file():add(p)
add(P);add(B)
for n in ['bind_whole_ROOT371_test_ideal_proof_and_primary_reading_20261008.py','fetch_public_Mustata_test_ideal_primary_20261008.py','record_verified_checkpoint265_20261008.py']:add(R/n)
add(G/'push-receipt-continuation265.json');add(Path(__file__))
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/n,'manuscript/editorial/xean_research_20261003/'+n)
x=load(R/'active-work.json');write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole smooth-primary-model test-ideal envelope approximation proof',scope='16solved26OPEN97papers. ENTIREunreviewed17741byte371 uniformall-supporttestidealproof/fullsource/scopebinding. SM model hypothesis explicit/notproved, no original/energy/equation closure or count increase. Source bodies/pixelsLOCALONLY. Continue263/264 maxTWO, no active feedback.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
