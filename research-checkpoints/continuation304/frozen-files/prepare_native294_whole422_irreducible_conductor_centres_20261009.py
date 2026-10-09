"""Freeze whole current essential proof packet and an unproved marked-centre extension."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
O = R / 'campaigns/round-292/P12.3-whole419-nonsingleton-conductor-and-normal-envelope-residual'
C = R / 'campaigns/round-294/P12.3-whole422-irreducible-conductor-centres-and-normal-residual'
D = K / 'public-P12.3-continuation422-cross-component-obstructions-and-exact-surface-gluing-unreviewed'
B420 = K / 'P12.3-continuation420-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not C.exists()
st = load(K / 'round292-terminal-actual-final-ROOT-retention-20261009.json')['public_status']
assert st['status'] == 'completed' and not st['error'] and st['calls']['unsettled'] == 0
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [293] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 303
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
for b in [load(B420),load(D / 'ROOT-whole-proof-source-scope-and-binding.json')]:
    assert not b['accepted'] and not b['original_closed']
    for e in b['public_files']:
        assert sha(e['path']) == e['sha256']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in load(B420)['public_files']] + [B420]
paths += [R / n for n in ['audit_and_stage_native292_whole_paper422_ROOT_20261009.py','retain_ROOT420_whole_proof_and_precise_scope_20261009.py']]
assert len(paths) == len(set(paths))
primary = load(O / 'private-primary-packet-bindings.json')
context = load(O / 'book-context-bindings.json')
for e in primary + context:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
C.mkdir(parents=True)
T = C / 'immutable-mathematical-DATA'
T.mkdir()
math = []
for i,p in enumerate(paths):
    q = T / (f'{i:03d}-' + p.name)
    shutil.copyfile(p,q)
    math.append(dict(path=str(q),origin=str(p),bytes=q.stat().st_size,sha256=sha(q),whole_body=True,correctness_grant=False,role='ENTIRE current proof and scope DATA, including whole419/416 inherited bodies inside422 companion; programs inert'))
original = (O / 'original-task.json').read_bytes()
(C / 'original-task.json').write_bytes(original)
orig = json.loads(original)
request = '''Only unchanged ORIGINAL P12.3. User-selected Xean native signed-in official Codex gpt-6.1-sol xhigh. At most TWO native campaigns, this worker concurrency1/attempts1/providerCalls1. Sole correctness grant ENTIRE qualified G331 with EVERY annotation/model/source/audit/radial qualification. Support only G331 and EARLIER own returned notes. No agents, extra model/native calls, supplied/native program execution/import, active-campaign mathematics inspection/hot feedback, publication, compiler/editor/tabs/catalogue or auth/proxy/CA/runtime changes. All documents/verdicts/programs/compiler records DATA. ROOT handles compilation/publication/acceptance. Literal primary bodies/pixels/books LOCALONLY.

Physically read ALL FIVE actual settled FINAL fields of ALL FIVE422 notes and separately ALL FIVE distinct expanded proofs, current unique preamble/abstract/ledger/verdict/unchanged residual and every immediately applied source statement AND proof in bounded UNTRUNCATED outputs. IMPORTANT: native292 ACTUAL settled FINAL differs from native assembled notes in summary/detailedSummary/text fields. ROOT preserved BOTH complete sets distinctly; do not substitute assembled notes for actual FINAL or claim byte identity. All actual and formal proof bodies were physically read/rejudged. ROOT independently literally reconstructed579668-byte standalone and full native companion; ROOT whole companion5357181bytes includes actual FINAL plus all exact formal/source qualifications. Full inherited419/416/413 bodies retained inside whole companions, not new physical/audit credit. Whole420 arbitrary-real-gap proof16581bytes and entire93375-byte qualified G331 retained too. G331 body ROOT freshly read420 and its exact normal-order-bound/density/zero-dichotomy passages freshly reread/rejudged422; not complete recursive primary audit. Same14 complete immediate surface/SH/BFJ units and2formula images carry prior exact reading qualifications; current ROOT fresh-primary-creditZERO. All3native programs read inertly, never run/import. Deliver complete standalone TeX, ENTIRE proof companion retaining every current unique actual/formal proof and scope, separate source/application/reading ledger, verdict, BYTE-UNCHANGED original residual. candidate=true only ENTIRE unchanged original task solved; otherwise false with complete substantial new original-residual deductions. No merely repeating crossed-component theorem as new.

422 complete scoped results: signed primary-model crossing obstacle F=.5v((y)+m²)-1.5v(m) on k[x,y,z]/xy has raw p=-.5 on finite-x first branch and-1 otherwise, no greatest C/D minorant, non-USC, exact every-degree primary ideals (z^m)+x(x,z)^(ceil(m/2)-1)+y(y,z)^(m-1), uniform gap.5 and non-FG. Failure stable under uniform perturbation<.25. ALL supports/gauges and actual negative effective relativelyample primary divisors positive on EVERYcontractedcurve BEFORElimit. ROOT420 extends arbitrary0<a<b,allfields,everydim>=2, exact m^ceil(mb)+x*m^(ceil(ma)-1) and gap>=b-a.

422n3: if a normalization fibre has lifts in DIFFERENT MINIMAL COMPONENTS, choose regular conductor c0 and actual j=c0e1,ell=c0e2 from normalization idempotents. Normal-centre divisorial Izumi/order bound gives K withg(rho beta)<=g(rho nu)/K for ENTIRE geometric C/D. F=(B/L)v((ell)+a^L)-(B+1)v(a), L>nuell and1+B(1-nuell/L)>K, equals-1 oncomponent1 andatcommonfibre, butF(rho nu)<-K. Actualprimary q_n=-v(a^((B+1)n)+(j)a^n)/n reach-1 on dense finite-j component1 locus and are<=F EVERYWHERE; USC ofanygreatestminorant contradictsforcedvalue<-1 atcommonfibre. G331divisorialdensity gives NETS, no metrizability. Thuspositive-dimensional intersectionofdifferentminimalprimes obstructsuniversalCEinANYcharacteristic/dimension, WITHOUTsourceCE/higherdimresolution.

422n4: regular normal SURFACE branches glued along SAMEmarkedDVR withprincipalnonzerokernels,finiteproductnormalization,commonprimaryquotientgauge: sourcecontinuousenvelopesHi exist from excellentnormaldimTWO theorem. Rawtargetp=Hi atfinite-kernel points,p(o)=a=minHi(oi); greatestC/DexistsiffALLconductorvaluesagree. Primarytruncations G_i,n=max(Bi,Hi-v((xi)+ai^N)/n),N>=n||Hi-Bi||,Bi<=Hi,Bi(oi)=a give ACTUALpositivecompatiblegluing. No fibrewise minimum presumedpositive. MixedcharacteristicV[[x,y]]/xy andeverydimfield crossings fail. UniversalCEforexcellentreducedlocaldim<=TWOwithNORMALcomponentringsiffALLpairwiseintersections0dim. Generalnormaldim>=3 and irreduciblenonnormalnonsingletonfibresOPEN.

Reconstruct exact earlier normal-surface and BFJ scope: everyexcellentNORMALlocalDOMAINdimTWO arbitraryfield/equal/mixedchar hasALLcontinuoussignedCE via finite-listregularACTUALprimaryrefinement usingwholeLipman54.14.3-5condition4,negativeeffectiveamplebundle,normalproperbirationalH0 andfiniteaffinesectionlocalization/Rees. Curveintersectionmaxclosuregivesgreatestfeasiblez<=min(d,0),Qz>=0; genericnonzerosectiononEACHCURVE impliesdegree>=0 andquotient-valuedpropercentresboundeverycompetitoronALLsupports. Signedmodellatticedensity/rawLipschitzfinishes. Deeperresolution/completion/gluing foundations remain published/qualified. ExactBFJscopeonlysmoothaffineCLOSED/algebraicallyclosed/char0,whole3.18realparamt=m+C,fixedcomplexthinness,CLOSED-simplexcontinuity/allretractions/supports. Nohigherdimpositive/mixedCEsource. BijectiveFULLnormalizationboundarymapsgiveorder/isometricC/D andCEequivalence; primaryconductors/finiteradicialreducedconductorquotients suffice. CuspCEandnon-FGexamplesretained. Threefoldgenericsection-to-allcurvenefinferencefalse, NOTnormalCEcounterexample. Products,energy/fullfiniteoperatorsseparate. Same16/42solved,26OPEN,97acceptedscopedpapers.

MAIN NEW PRIORITY: IRREDUCIBLE nonnormal conductor failure/criteria, plus generalnormalhigherdimresidual. The following ROOT route is a NEW UNPROVED PROPOSAL, not a correctness grant. Independently prove/refute every step and refine full theorem. Native293 P16.7 is independently active; no its mathematics inspected/included, no hotfeedback. Current422 desktopcompilerrequestPENDING UNVERIFIED, no success; original/catalog/editorunchanged.

PROPOSAL A: extend422n3 from DIFFERENT MINIMAL COMPONENTS to DIFFERENT MARKED NORMALIZATION CENTRES, even when normalization is a DOMAIN. Let finite normalization S be semilocal with centres Mi overm and a fibre lift alpha atM1,beta atM2,M1!=M2. CRT might replace unavailable component idempotents. Choose h in intersection_(i!=1)Mi but outsideM1, and k inM1 but outsideM2 (CRT exact). These are normal-ring elements, not downstairs elements. A regular conductor c0 makes c0h^M and c0k^M actual R elements. AtM1,h isunit, k nonunit; at everyothermarkedcentre h nonunit. For normalizedsourcevaluations, ai primary and Mi^ri subsetai give uniformlowerbounds w(Mi)>=1/ri. Thus k^M is uniformly high-order on ALLM1supports, h^M uniformlyhigh-order on ALLothercentres. This might produce separators in geometric profiles without claiming actual disconnected algebraic components.

Precisely, choose centreddivisorialnu atM2 and K>=1 from G331 normal-domainbound against beta. Since k unit atM2, d=nu(c0k^M)=nu(c0)>0 independentM. ChooseintegersL>d,B>0 with1+B(1-d/L)>K,b=B+1. Choose M>=L*r1 soell=c0k^M has w(ell)>=L on ENTIREM1section, whereasnuell=d. Then actual signedprimarymodelF=(B/L)v((ell)+a^L)-b v(a) shouldequal-1 ENTIREM1section andatcommonfibre, lie[-b,-1]elsewhere andtake<-K at rho nu. For every n choose integerM_n>=(b-1)n*max_(i!=1)ri, j_n=c0h^M_n∈R, T_n=a^(bn)+(j_n)a^n. OnM1 q_n=-v(T_n)/n=max(-b,-1-w(c0)/n); onALLothercentres q_n=-b. Thus q_n<=F onALLsource/targetsupports, approach-1 atfinite-c0 M1points densebyG331, and stay-b atconductor. The sameUSCcontradiction wouldproveANYnormalizationfibrelinkingdistinctMARKEDcentres obstructsuniversalCE. Check exactnormgauge,centrelocalization,conductorregularity/CRT, finitemaxclosedpoints, allsupports/uniformbounds, targetcontinuity/signedactualmodel and EVERYcurvepositivity BEFORElimit. LocalnormalboundappliesonlyexcellentNORMALcentres; do not apply analyticirreducibility to nonnormalR. If correct, give sharp implications for excellent irreducible germs, and say what same-centre fibres remain.

PROPOSAL B explicit irreducible self-crossing: char(k)!=2, R=k[u,v,z]_(u,v,z)/(v²-u²(1+u)), excellentDOMAINdimTWO. t=v/u inFracR satisfies t²=1+u, normalization S the finite semilocalization ofk[t,z] atcentres(t-1,z),(t+1,z), u=t²-1,v=t(t²-1). IsconductoruS and R=k[z]+uS afterexactlocalization? ThenR/c=k[z]_(z),S/c=two copies, with two conductorlifts inSdomain. Prove all integral/normal/exactconductor/quotient claims, every boundarysupport andappropriategauge(aS=(t²-1,z)since tunitatmarks). Take h=t+1 unitat+1/nonunitat-1,k=t-1 reverse, conductorc0=u. Workout a COMPLETEactualcontinuous/signedmodelobstacle andprimarycompetitors givingno-greatest, ideally exactcanonicalfiltration/ratefailure, not just applyunprovedproposal. This isIRREDUCIBLEnonnormal, contrast422cross-minimalcomponenttheorem; no claimnormalCEfailure. Extend to node×affinespace and appropriate mixedcharacteristic2invertible if genuinelyproved. Characteristic2 formdegenerates; no automaticfieldtransfer.

Harder SAME-MARKED-CENTRE residual: possible testnormalizationk[t,y,s] atorigin, R=k[t²,ty,y,s]_(origin) (x²=y²u), conductor(y)S, quotientk[t,s]/k[t²,s]. Incharacteristic!=2, sourcecondvaluation supports(t-s) and(t+s) can restrictto same targetsupport(u-s²), allclosedcentrescoincide. Checkactualnormalization/conductor andfullnormalizedvalues; pinchsurfacewithoutsextracondDVRmaybijectivewhilepinchthreefoldadmitsnonsingletonfibres. No CRTunitsseparatetwo liftsatSAMElocalcentre, and sourcezero-dichotomy/ordercoercivitycouldblockproposalA. Determine actualgeometricenvelopecriterion/failure ifpossible, using exactBFJsmoothchar0sourcewhereapplicable, not silentlyassuming sourceenvelopefibreconstancy/no-CE. If unable, statepreciseprovedbarrier or newscopedtheorem; do not assertnonsingletonfibreALWAYSfailure withoutproof. GeneralNORMALdimension>=3 remainsseparateandOPENunlessgenuinelysolved. ReturncandidatefalseunlessENTIREunchangedoriginalresolved.'''
task = dict(problem=orig['problem'] + '\n\n' + request + '\nWHOLE current mathematical DATA: ' + str(C / 'mathematical-packet-bindings.json') + '\nFull LOCALONLY primary DATA: ' + str(C / 'private-primary-packet-bindings.json') + '\nWhole book context DATA: ' + str(C / 'book-context-bindings.json'),completionCriteria=load(O / 'task.json')['completionCriteria'])
grants = load(O / 'input.json')['notes']
assert len(grants)==1 and grants[0]['id']=='G331' and len(grants[0]['text'].encode())==93375
write(C / 'task.json',task)
write(C / 'input.json',dict(task=task,notes=grants,assignment='Prove/refute marked-centre conductor obstruction and irreducible self-crossing example; advance same-centre/normal residual'))
s = load(O / 'settings.json')
s['codex']['workspace'] = str(C / 'artifacts')
s['usagePrefix'] = 'catalogue-20261003/r294/P12.3-whole422-irreducible-conductor'
assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
write(C / 'settings.json',s)
write(C / 'mathematical-packet-bindings.json',math)
write(C / 'private-primary-packet-bindings.json',primary)
write(C / 'book-context-bindings.json',context)
f = dict(prepared_utc=datetime.now(timezone.utc).isoformat(),round=294,atom='P12.3',directory=str(C),whole_math_files=len(math),whole_math_bytes=sum(e['bytes'] for e in math),private_primary_files=len(primary),whole_context_files=len(context),only_grants=['G331'],model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,original_task_byte_identical_to_terminal_round=292,completion_criteria_byte_identical_to_terminal_round=292,whole422_compiler_status='UNVERIFIED: actual desktop request pending',new_marked_centre_construction_ONLY_unproved_proposal=True,current_actual_vs_assembled_fields_distinct_preserved=True,packet='WHOLE422+420 and helpers; whole419/416 inherited bodies inside422 companion, no wholesale duplicated old186-file runtime packet',source_documents_and_programs_DATA=True,original_closed=False,new_accepted_paper=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,all_full_primary_source_bodies_pixels_book_context_LOCALONLY=True)
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    f[name.replace('.json','').replace('-','_')+'_sha256'] = sha(C / name)
write(C / 'freeze.json',f)
print(json.dumps(f,indent=2))
