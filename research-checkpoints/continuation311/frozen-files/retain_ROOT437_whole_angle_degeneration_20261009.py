"""Retain whole independent angle proof and complete current qualifications."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks'
P=K/'P16.7-continuation437-angle-degeneration-and-isotropic-dual-bound-working-paper-20261009.tex'
Q=K/'P16.7-continuation437-ROOT-source-scope-and-residual-20261009.json'
O=K/'P16.7-continuation437-desktop-compiler-observation-20261009.json'
T=K/'P16.7-continuation437-entire-proof-companion-20261009.txt'
B=K/'P16.7-continuation437-ROOT-whole-paper-source-scope-and-binding-20261009.json'
B434=K/'P16.7-continuation434-ROOT-whole-paper-source-scope-and-binding-20261009.json'
D436=K/'public-P16.7-continuation436-two-residue-radon-and-family-limit-unreviewed'
B436=D436/'ROOT-whole-proof-source-scope-and-binding.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    y=load(R/n);assert y['current_active_batch']==[] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==310
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
for b in [B434,B436]:
    z=load(b);assert not z['accepted'] and not z['original_closed']
    for e in z['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
u=load(K/'P16.7-continuation434-ROOT-source-scope-and-residual-20261009.json')['all15_immediate_primary_units_reused_ZEROextra_credit']
for e in u:assert sha(e['path'])==e['sha256']
s=P.read_text();assert s.endswith('\\end{document}\n') and not any(ord(c)<32 and c not in '\r\n\t' for c in s)
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=437,atom='P16.7',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),incoming_correctness_grants=[],whole_current_source_ROOT_physically_read=True,reading_output='2222b4 WHOLE437 source3853tokens untruncated',whole434_source_fresh_ROOT_physically_read='4a55d7 WHOLE367LF16990B source4248tokens untruncated; previouscombinedoutputaec458wasgloballytruncated and receivesZEROwholecredit',whole436_corrected_source_ROOT_physically_read=['c9e757 LF1-285','8fcbc8 LF286-565'],proof_origin='Independent ROOT after both298299completed and allactual299notes reviewed; no activecampaign inspection/hotfeedback/delegation.',new_scoped_deductions=['ActualGLOBAL quadraticpencil extends to EVERYconstantnorm-one anglealpha: actualC positivity/ordinarycollar, explicitfiniteflatdegree2 map andWHOLEuniqueGaussfibre, MA=2delta_xi_calpha,E=-1/3-2c/3,FULLD=1/6+4c/3.', 'At c=2a anddistinctconstant residuesalphaj, anisotropicGaussxi_j converges inACTUALanalyticsemivaluationtopology tooldisotropicx_a. EACHfixedpolynomial normeventuallyequal: normalizedleadinghomogeneousycoefficient nonzeroresidueLaurentpolynomial excludesonlyfinitelymanyangles. ALLcontinuousanalytic weakmeasuretests follow.', 'FULLD weakLSC yieldsnewupper1/6+8a/3, actualsinglewellcompetitorlower1/6+5a/3. OLDoriginaldepth1/8 improved3/8<=D<=1/2; finitenessONLY, noexistence/attainment.', 'AtEVERYactualpoint atmostONEQj differs q*=oldsinglewellq2a; pairwisemax=q*, pairwiseincomparable, exactsupdistancea. UniformlyboundedunorderedpointwiseQj->q*, butMAQj->2delta_x_a DIFFERENTfromMAq*=g+x2a, energyjump2a/3.', 'Actualconvexaverages A_N convergeUNIFORMLY withEXACTnorma/N; actualMAA_N->g+x2a andenergyerror<=2a/N bypositivecubicmixedmass2. No contradictiontoactualuniform/monotonecontinuity.', 'AgainstOLDtarget2delta_x_a, eachQjobjective1/6+2a/3, maximizinggap>=a; constantscannotremoveit. Weakapproximatingsolvedequations areNOTmaximizingsequence.'],all15_complete_primary_units_reused_ZEROnew_reading_credit=u,exact_current_primary_application='Sameexplicitdegree2 finiteflatordinaryunitbidisc as434, nowdeterminant-2alpha normone. Complete18.6.1/2 and11.6.1-5 applications rejudged; noGaussfibreprobabilityinterpretation. Whole436qualifiedboundedGreen/concavity/positivemixedmass anduniformcontinuity retained. NewGaussconvergence provenfromfinitepolynomialsemivaluationformula; weakLSCfromsupcontinuousaffine, noexternallimitrecognition theorem.',fresh6_2_source_reused_ZEROextra_credit=load(D436/'ROOT-whole-proof-source-application-scope-and-residual.json')['fresh_entire_CLD6_2_1_9_statement_and_immediate_proof'],whole436_companion_retained_separately_and_to_be_public_in311_NOTduplicated_inside437=True,wholehistorical_books_recursivefoundations_genuine_geometry_INCOMPLETE=True,residual=['OLDspecifiedisotropicwholeDirac existence/attainment stillOPEN despiteimprovedfullDfinitebound.', 'Generalanalyticrecognition/arbitraryeligiblemeasure/envelopecompactness/variations/comparison/fullP16.7 OPEN.', 'Genuine nonalgebraization/coherentdescent andwholedeeperaudit remainqualifiedOPEN.'],supplied_or_native_programs_executed_or_imported=False,hot_feedback=False,compiler='UNVERIFIED notyetrequested437',primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=437,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=False,compilation_verified=False,result='Notyetrequestedatretention; nosuccessobserved',source_preserved=True,no_local_TeX_plugin=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
components=[('WHOLEindependent437',P),('WHOLE434entireproofcompanion',Path(load(B434)['whole_companion']['path'])),('WHOLE434binding',B434),('WHOLE436binding',B436),('WHOLE437scope',Q),('437compilerUNVERIFIED',O)]
for n in ['P16.7-two-residue-radon-and-family-limit.tex','native-standalone-DATA.tex','native299-actual-FINAL-all-five-fields.json','native299-assembled-notes-separate-from-actual.json','native-source-application-reading-ledger.json','native-source-application-reading-ledger.txt','native-scoped-verdict.json','ROOT-whole-proof-source-application-scope-and-residual.json','ROOT-whole-companion-containment-ledger.json','native-original-residual.txt','native-unchanged-original-task.json']:
    components.append(('WHOLE436current '+n,D436/n))
T.write_text('ENTIREindependentROOT437 mathematical packet. UNREVIEWED originalOPEN; 436entirecompanion separatelyretained/public311, notduplicatedhere. Literalprimary/pixels/booksLOCALONLY.\n'+''.join('\n===== '+title+' =====\n'+p.read_text()+'\n' for title,p in components))
body=T.read_bytes();assert all(p.read_bytes() in body for _,p in components) and all(Path(e['path']).read_bytes() not in body for e in u)
public=[P,Q,O,T]
write(B,dict(recorded_utc=now,paper=437,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],primary_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
for n in ['active-work.json','checklist-current.json']:
    p=R/n;y=load(p);y.update(updated_utc=now,ROOT437_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='WHOLEindependent437 angulardegeneration givesoldisotropic3/8<=FULLD<=1/2, unorderedpointwiseMA/energyfailure, exacta/Nuniformconvexaverages andfixeddualmaximizinggap>=a. OriginalexistencestillOPEN. Freeze smallnextnative300301 withWHOLE434435436437 andqualifiedsources, officialgpt6.1solxhighmaxTWO, thenNONFORCE311boundedsegmentpublication; counts/editor unchanged.');write(p,y)
print(json.dumps(dict(paper=437,source_bytes=P.stat().st_size,source_LF=s.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
