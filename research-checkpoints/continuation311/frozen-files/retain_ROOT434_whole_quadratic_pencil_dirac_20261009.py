"""Retain independent434 before reading either settled298 or settled299 mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess

R=Path('/workspace/research');K=R/'root-checks'
P=K/'P16.7-continuation434-quadratic-pencil-whole-nonskeletal-dirac-working-paper-20261009.tex'
Q=K/'P16.7-continuation434-ROOT-source-scope-and-residual-20261009.json'
O=K/'P16.7-continuation434-desktop-compiler-observation-20261009.json'
T=K/'P16.7-continuation434-entire-proof-companion-20261009.txt'
B=K/'P16.7-continuation434-ROOT-whole-paper-source-scope-and-binding-20261009.json'
B433=K/'P16.7-continuation433-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert not (K/'round298-raw-native-actual-FINAL.json').exists() and not (K/'round299-raw-native-actual-FINAL.json').exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
 y=load(R/n);assert y['current_active_batch']==[299] and y['latest_verified_github_checkpoint']['continuation']==309 and y['github_pending_checkpoint']['continuation']==310
 assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
parent=load(B433)
assert not parent['accepted'] and not parent['original_closed']
for e in parent['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
ps=load(K/'P16.7-continuation433-ROOT-source-scope-and-residual-20261009.json')
units=ps['all15_complete_immediate_primary_units_reused_ZEROnew_reading_credit']
for e in units:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
fresh_names=['1224-1216-CLD-18.6.1-LF27560-27607-LOCALONLY.txt','1225-1217-CLD-18.6.2-LF27608-27671-LOCALONLY.txt','1203-CLD-11.6.1-5-finite-flat-local-and-full-proof-LOCALONLY.txt']
fresh=[e for e in units if Path(e['path']).name in fresh_names];assert len(fresh)==3
text=P.read_text();assert '\\end{document}' in text and not any(ord(c)<32 and c not in '\n\t\r' for c in text)
C=R/'campaigns/round-299/P16.7-whole432-two-point-mass-and-whole-dirac'
st=load(C/'launch-record.json')
compact=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert compact['status']=='completed' and compact['error'] is None and compact['calls']['admitted']==compact['calls']['settled']==1 and compact['calls']['unsettled']==0
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=434,atom='P16.7',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),whole_current_source_ROOT_physically_read=True,reading_output='25b5d4: entire434 source4248tokens untruncated',parent433_whole_source_fresh_ROOT_read='3a653d: entire364LF17788Bsource4447tokens untruncated',incoming_correctness_grants=[],proof_origin='Independent ROOT after compact-only settled299 status, before ANY settled298 or299 mathematics. No hot feedback.',
 complete_new_scoped_deductions=['Actual GLOBAL positive three-slot bidegree(1,1) pencil Hc=logmax(|uv|,|u+v|,e^-c), for norm-one centres, equals H0 on EVERY actual point outside the residue bidisc. Smoothconvexunitmax andordinarycollar prove originalENTIRE-C positivity before products; deck2/3 preserved.', 'WithinW linearcoordinates x=u+v,y=u-v have Hc=logmax(R,|x|,|y|^2). ACTUALfinite-flatdegree2 map(x,y)->(x,y^2) and gradedGauss odd Y-divisor prove WHOLEunique fibre over eta_(R,R) is xi_c=(xR,y sqrtR), arbitraryrealR. Integrationcurrent is NOT probabilityDirac; no primitive-degree1 substitution.', 'Whole18.6.2 putsalllocalmass at xi_c; elsewhere actualratio-top-squarezero. Positivity andglobalboundedStokes totalrawmass2 calibrate MA(Qc)=2delta_xi_c, NOgatom. B(q0,Qc)=2g via actualfixedcoordinateGauss fibres, and MA(q0+h wc)=2(1-h^2)g+2h^2xi_c.', 'Actual E(Qc)=-1/3-2c/3 and FULLD(2delta_xi_c)=1/6+4c/3 attained. c1/8 givesE-5/12,D1/3. xi_(1/8) is NOT the oldequal-radius x_(1/8).', 'Nested B(Qc,Qd)=2delta_xi_min via whole18.6.1 finite-flat pullback ofactualfixed-ratio targetidentity; ALLdegree2 fibre andglobalmixedmass2 calibrated.', 'ANYRadondepthlaw TOTALM<=2: actualCpositivefiniteatomiccombination beta sumsqrt(M/2)<=1, uniformcutoffs andactualGdecreasingpresentation. FULLDfinite IFF S=(1/sqrt2)intT^(3/2) finite; MA=(2-M)g+pushzeta,E=-1/3-S/3,D=1/6+2S/3. M2 placesALLmass onONE nonskeletal branch.', 'zeta=2c^-2dc[1,infinity) givesM2,S6,E-7/3,D25/6,cutoffE=-7/3+4/(3sqrt n), actualunboundedsingle-centresolution,no massrigidP.'],
 all15_immediate_primary_units_reused_ZEROextra_credit=units,three_complete_units_fresh_ROOT_physically_read=fresh,fresh_primary_reading_outputs=['ee928c:WHOLE18.6.1','9c9bfa:WHOLE18.6.2','692c26:WHOLE11.6.1-5'],exact_new_primary_application='Actual ordinary boundaryless separated good residuebidisc; actualfiniteflat freebasis1,y degree2;18.6.2 wholeGaussfibreintegrationcurrent not probability;18.6.1 mixed pulledmetrics; allpositiverealR includingoutsidevaluegroup. Coefficient2 independently calibrated by actualboundedStokes rather than assuming fibrepoint coefficient1.',parent_recursive_foundations_genuine_geometry_and_deeper_book_audit_INCOMPLETE=True,retention_hashing_NOTreading_or_correctness_credit=True,
 residual=['Prescribed whole2delta_oldisotropicx_(1/8) remainsOPEN; explicitxi isunequalradiusinlinearcoordinates.', 'Generaleligiblearbitrarysupport/recognition/envelopes/variations/fullP16.7 OPEN.', 'Genuine nonalgebraization/coherentdescent andentiredeeperindependentfoundationaudit remainqualifiedOPEN.'],native299_compact_only_status=compact,native298_and299_terminal_math_NOT_read=True,hot_feedback=False,supplied_or_native_programs_executed_or_imported=False,compiler='UNVERIFIED not yet requested at retention',primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=434,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=False,compilation_verified=False,result='Not yet requested at retention; no success observed',source_preserved=True,no_local_TeX_plugin=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
components=[('WHOLEindependent434',P),('WHOLE433entireproofcompanion including432standalone/currentactualnotes/sourcequalifications',Path(parent['whole_companion']['path'])),('WHOLE433source-scope-and-wholebinding',B433),('WHOLE434scope',Q),('434compiler UNVERIFIED',O)]
T.write_text('ENTIREindependentROOT434packet. UNREVIEWED originalOPEN; primarybodies/pixels/books LOCALONLY.\n'+''.join('\n===== '+title+' =====\n'+p.read_text()+'\n' for title,p in components))
body=T.read_bytes();assert all(p.read_bytes() in body for _,p in components)
assert all(Path(e['path']).read_bytes() not in body for e in units)
public=[P,Q,O,T]
write(B,dict(recorded_utc=now,paper=434,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],primary_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
for n in ['active-work.json','checklist-current.json']:
 p=R/n;y=load(p);y.update(updated_utc=now,ROOT434_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='VerifyNONFORCE310v2 segmentedbyteexactWHOLE431432433. IndependentWHOLE434quadraticpencilwhole2Dirac andmass2Radonbranch retainedBEFOREANYnative298/299math. Then inspectonlysettled298actualFINAL. Both298299completedcompactonly, nohotfeedback,maxTWO,counts/editor unchanged, fulloriginalsOPEN,compileunverified.');write(p,y)
print(json.dumps(dict(paper=434,source_bytes=P.stat().st_size,source_LF=text.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
