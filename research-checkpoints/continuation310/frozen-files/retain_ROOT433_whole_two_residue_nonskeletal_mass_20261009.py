"""Retain independent433 before any settled298 or active299 math inspection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research')
K=R/'root-checks'
P=K/'P16.7-continuation433-two-residue-full-mass-nonskeletal-equations-working-paper-20261009.tex'
Q=K/'P16.7-continuation433-ROOT-source-scope-and-residual-20261009.json'
O=K/'P16.7-continuation433-desktop-compiler-observation-20261009.json'
T=K/'P16.7-continuation433-entire-proof-companion-20261009.txt'
B=K/'P16.7-continuation433-ROOT-whole-paper-source-scope-and-binding-20261009.json'
D=K/'public-P16.7-continuation432-nested-nonskeletal-radon-equations-and-fan-obstruction-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert all(not p.exists() for p in [Q,O,T,B])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['current_active_batch']==[299] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==309
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
text=P.read_text()
assert len(text.encode())==17788 and text.count('\n')==364 and '\\end{document}' in text
assert not any(ord(c)<32 and c not in '\n\t\r' for c in text)
old=load(D/'ROOT-whole-proof-source-scope-and-binding.json')
assert not old['accepted'] and not old['original_closed']
for e in old['public_files']:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
prior=load(D/'ROOT-whole-proof-source-application-scope-and-residual.json')
units=prior['all15_complete_immediate_primary_units_fresh_ROOT_physically_read']
for e in units:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=433,atom='P16.7',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),whole_current_source_ROOT_physically_read=True,reading_outputs=['f2aa95:wholeinitial17757B363LF','10c2fe:wholecorrected17788B364LF4447tokens untruncated'],proof_origin='Independent ROOT derivation after native299 launch, before ANY active299 mathematics and ANY settled298 mathematics inspection. The frozen299 request already contained the unproved two-residue polynomial proposal; current433 formal proof/results were not supplied or hotfed.',incoming_correctness_grants=[],
    complete_new_scoped_deductions=['For norm-one a_i,b_i with unit coordinate differences, two bilinear polynomials and four depth-selective cap slots give exact all-actual-point potential identity H-H0=v1+v2. Actual localconvexunit-log maxima andordinarycollar establishENTIRE-C positivity beforeproducts, despite coefficientsum2.', 'MA(q12)=delta_x1,c1+delta_x2,c2 for EVERYpositive realdepth; actualfixedcoordinatefibres give singletoncoefficient1 on each ordinaryresiduebidisc; elsewhere two-unit ratio max top-squarezero, includingg. Thus entire rawmass2 is nonskeletal.', 'Actualsignedcross-current ddv1 ddv2=0, B(q1,q2)=2delta_g. FOURpositivecornerconvexcombination permits independentlambda_i in[0,1] and EACH m_i<=1, notsum<=1; MA=(2-m1-m2)g+m1x1+m2x2.', 'Alltwo-branchRadondepthlaws with EACHmass<=1: FULLDfinite IFF S=sum int tail_i^(3/2) finite, actualoriginal-Ccutoffs viaPRODUCTconvexdistribution/atomicuniformapprox, actualdecreasingGsolution andfullMA, E=-1/3-S/3,D=1/6+2S/3.', 'Bothmasses1 give noGaussatom. Depth1/8 at(1,1),(2,3): E-5/12,D1/3. Both c^-2dc[1,infinity): S6,E-7/3,D25/6,cutoffE=-7/3+4/(3sqrt n), actualextendedcontinuousinfiniteonlyP1P2,no targetmassP_i.', 'Generateduniqueness/nonorderedrepresentation withinTHISalreadyconstructedsector retainsqualifiedboundedcalculus/fullpoint/finiteShilov antecedents, notgeneralarbitraryrecognition.'],
    all15_complete_immediate_primary_units_reused_ZEROnew_reading_credit=units,previous_fresh_complete_ROOT432_primary_reading_outputs=prior['primary_reading_outputs'],exact_new_primary_applications='CLD15.7.1 separatedpureboundaryless input;8.1.7-8 and8.2.4 actualsix-slotunitmax/FOURcorners/PRODUCTconvexfinitechoices/localuniformatomicclosure;8.5/8.7/8.8 actualsignedcrossproducts andrankonevanishing;18.6.2 coordinateisomorphisms ofordinaryopenbidiscs EACHsingletoncoefficient1 ALLrealradii; withinbranchfixedratioGausscurve/H(eta1)curve primitiveintegerdet1;7.2.8-13 allcontinuousanalyticRadontests;5.11.1 smoothGreen atqualifiedreconstructedboundedboundary;GR1.2/4.1-4.2/6.3-4 onlyalreadyactualcontinuouspresentationpotentials. GR6.5NOTrecognition, CLD8.6.7NOTapplied.',
    wholeROOT432companion_separately_retained_and_bound_NOTfresh_reading_or_correctness_credit=True,entire_current427_standalone_and_recursive_historical_book_primary_geometry_audit_INCOMPLETE=True,genuine_nonalgebraization_and_coherent_descent_NOT_certified=True,
    residual=['Distinctresidues in BOTHcoordinates essential; coalescedwhole2delta_xONEpoint remainsOPEN.', 'Generaleligiblearbitrarysupportexistence/generaldominatedrecognition/generalenvelopesvariations/fulloriginalP16.7 OPEN.', 'Actualinputgeometry anddeeperindependentrecursiveaudit remainqualifiedOPEN.'],compiler='UNVERIFIED notyetrequested433 atretention',native298_terminal_math_NOT_read=True,native299_ACTIVE_math_NOT_read=True,hot_feedback=False,supplied_or_native_programs_executed_or_imported=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,scope)
write(O,dict(recorded_utc=now,paper=433,source_path=str(P),source_sha256=sha(P),actual_builtin_compile_request_invoked=False,compilation_verified=False,result='Not yet requested at retention; no success observed',source_preserved=True,no_local_TeX_plugin=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
components=[('ENTIREindependent433',P),('ENTIRE432standalone includingALL427formal foundations andcurrent552LFproof',Path(old['whole_source']['path'])),('ENTIRE432distinctnewproof',D/'new-residual-proofs.tex'),('ENTIREactualsettled297 ALLfour ALLfivefields',D/'native297-actual-FINAL-all-five-fields.json'),('ENTIRE432JSONreadingledger',D/'source-application-reading-ledger.json'),('ENTIRE432TXTreadingledger',D/'source-application-reading-ledger.txt'),('ENTIRE432ROOTsourcequalifications',D/'ROOT-whole-proof-source-application-scope-and-residual.json'),('ENTIRE432scopedverdict',D/'scoped-verdict.json'),('ENTIREunchangedoriginalresidual',D/'original-residual.txt'),('ENTIREunchangedoriginaltask',D/'unchanged-original-task.json'),('ENTIRE432source-scope binding toseparatelyretainedwholehistoricalcompanion',D/'ROOT-whole-proof-source-scope-and-binding.json'),('ENTIRE433source qualifications',Q),('Compiler observation UNVERIFIED',O)]
parts=['ENTIRE ROOT433 mathematical packet. UNREVIEWED originalP16.7 OPEN; completeprimaryliteralbodies/pixels/books LOCALONLY.\n']
for title,p in components:
    parts.extend(['\n===== '+title+' =====\n',p.read_text(),'\n'])
T.write_text(''.join(parts))
body=T.read_bytes()
assert all(p.read_bytes() in body for _,p in components)
assert all(Path(e['path']).read_bytes() not in body for e in units)
public=[P,Q,O,T]
write(B,dict(recorded_utc=now,paper=433,whole_source=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),whole_companion=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],primary_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    y.update(updated_utc=now,ROOT433_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='WHOLEindependent433 positivepolynomialfullnonskeletalrawmass2/twoRadonbranches retainedbeforeANYsettled298 oractive299 mathematics. PublishNONFORCE310WHOLE431432433andfrozen299 thencaptureonlysettled298actualFINAL. Native299isolatedactive, maxTWO; nohotfeedback. FulloriginalsOPEN,counts/editor unchanged, compilerunverified.')
    write(p,y)
print(json.dumps(dict(paper=433,source_bytes=P.stat().st_size,source_LF=text.count('\n'),source_sha256=sha(P),companion_bytes=T.stat().st_size,public_files=5,binding=str(B),accepted=False,original_closed=False),indent=2))
