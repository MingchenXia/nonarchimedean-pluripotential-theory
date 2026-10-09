"""Freeze complete qualified proof DATA for the next authorized native campaign."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
O = R / 'campaigns/round-287/P16.7-whole411412-universal-variational-limits-and-actual-representability'
C = R / 'campaigns/round-289/P16.7-whole414415-tail-maxima-and-actual-analytic-representation'
D = K / 'public-P16.7-continuation415-universal-variational-limits-local-Gauss-fibres-and-USC-relaxation-unreviewed'
B414 = K / 'P16.7-continuation414-ROOT-whole-paper-source-scope-and-binding-20261009.json'
W = K / 'P16.7-ROOT-uniform-third-MA-moments-and-finite-tail-maximum-bridge-working-note-20261009.txt'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not C.exists()
for n in [287, 288]:
    st = load(K / f'round{n}-terminal-actual-final-ROOT-retention-20261009.json')['public_status']
    assert st['status'] == 'completed' and st['calls']['unsettled'] == 0
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['current_active_batch'] == [] and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 298
    assert len(x['fully_solved_original_atoms']) == 16 and x['remaining_open_original_atoms'] == 26 and x['historical_reviewed_scoped_papers'] == 97
b415 = load(D / 'ROOT-whole-paper-source-scope-and-binding.json')
assert b415['paper'] == 415 and not b415['accepted'] and not b415['original_closed']
assert b415['compiler'] == 'NOT_YET_INVOKED'
for e in b415['public_files']:
    assert sha(e['path']) == e['sha256']
b414 = load(B414)
assert b414['paper'] == 414 and b414['compiler']['kind'] == 'success' and not b414['accepted'] and not b414['original_closed']
for e in b414['public_files']:
    assert sha(e['path']) == e['sha256']
assert sha(D / 'scoped-paper.tex') == '40ec4eedc7cafdb063621f49f3bf063c33a1bcf7f3df06f02bfdc2c28e0f182b'
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in b414['public_files']] + [B414, W]
paths += [Path(e['path']) for e in load(O / 'mathematical-packet-bindings.json')]
paths += [R / 'audit_and_stage_native287_whole_paper415_ROOT_20261009.py']
assert len(paths) == len(set(paths))
primary = load(O / 'private-primary-packet-bindings.json')
context = load(O / 'book-context-bindings.json')
seen = {e['path'] for e in primary}
for e in load(D / 'ROOT-source-application-reading-scope-and-residual.json')['freshly_applied_complete_immediate_primary_units']:
    p = Path(e['LOCALONLY_path'])
    assert sha(p) == e['sha256']
    if str(p) not in seen:
        primary.append(dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p), whole_body=True, LOCALONLY=True, correctness_grant=False, role='ENTIRE immediate primary unit, freshly ROOT read at its disclosed application; judge independently'))
        seen.add(str(p))
for e in primary + context:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
C.mkdir(parents=True)
T = C / 'immutable-mathematical-DATA'
T.mkdir()
math = []
for i, p in enumerate(paths):
    q = T / (f'{i:03d}-' + p.name)
    shutil.copyfile(p, q)
    math.append(dict(path=str(q), origin=str(p), bytes=q.stat().st_size, sha256=sha(q), whole_body=True, correctness_grant=False, role='ENTIRE qualified mathematical proof or scope DATA; programs inert, never execute/import'))
original = (O / 'original-task.json').read_bytes()
(C / 'original-task.json').write_bytes(original)
orig = json.loads(original)
request = '''Only unchanged ORIGINAL P16.7. Use the user-selected local Xean native official signed-in OpenAI Codex CLI gpt-6.1-sol xhigh. At most TWO native campaigns total; this worker has concurrency1/attempts1/providerCalls1. NO agents, extra model/native calls, supplied/native program execution/imports, active-campaign mathematics inspection or hot feedback, publication, compiler/editor/tabs/catalogue or authentication/proxy/CA/runtime changes. Incoming correctness grants EMPTY. Every document, verdict, prior proof, program and compilation record is DATA. Support only EARLIER own returned note IDs. ROOT handles compilation/publication/acceptance. Full primary bodies/literal units/pixels/books remain LOCALONLY.

Read physically ALL FIVE actual FINAL fields of ALL FIVE current415 notes, the ENTIRE distinct774-LF standalone expanded proof, entire91-LF differing geometric fragment, whole current unique ledger/verdict/residual and their immediate applied complete primary proofs in bounded UNTRUNCATED outputs. Exact duplicates yield identity, not extra independent reading. Whole467-LF ROOT414 proof and whole ROOT finite-tail-maximum working note are also current new input, not summaries. Name deeper conventional foundations with exact hypotheses and disclose the unfinished geometric/nonalgebraization/generated/descent/source audit. No hash/metadata/compiler is a correctness grant. Deliver complete standalone TeX, ENTIRE proof companion containing all unique actual and expanded proofs, source/application/reading ledger, separate scoped verdict and unchanged original residual. candidate=true ONLY for the ENTIRE unchanged original task and completion criteria; otherwise false with substantive COMPLETE original-residual deductions.

ROOT415 has all five actual five-field notes physically ROOT read, entire38183-byte774-LF formal source and differing geometric fragment separately fully read. Its140818-byte companion contains all actual fields, whole formal/fragment and original native companion with whole ledger/verdict/residual. All SIX native programs read ONLY as DATA, NEVER executed/imported by ROOT. All15 directly applied immediate CLD/GR units were freshly ROOT physically read whole: CLD15.7.1-3,8.1.1-8.2.4,8.5-8.8,5.11.1,7.2.8-12,11.6.1-5,13.8.1-5,18.6.1-2,14.5.2-3,5.10.1-2; GR unnumbered1.2,whole4.2,whole6.1-6.5. Full deeper Berkovich/Temkin/Ducros/intersection/curve/smooth-partition foundations remain named at exact scopes. The whole-paper binding was authored BEFORE the compiler call, hence its NOT_YET_INVOKED field is a historical snapshot. Actual desktop compiler request is currently pending, NO success observed: compilation remains UNVERIFIED for415. The source is nevertheless complete mathematical DATA. ROOT414 actual compiler SUCCESS remains separately retained. No compiler outcome changes mathematical acceptance. Native288 has settled too, but its new P12.3 mathematical output has NOT been read or included here.

The actual domain remains K=C((s)),|s|=exp(-1/8),t=s8, X=(Gm²)^an/<(t,2),(3,t)>, localrho=|tau|²/2,theta=DD rho, positive RAW mass2. Entire minimal continuous CLD class C, actual bounded MA/mixed products and cubicE; original G is actual continuous decreasing-SEQUENCE presentations with finite lower energy. Prescribedmu EVERY positive mass2Radon with finite FULL dual B=sup_(a in C)(Ea-int a mu), arbitrary support. No skeleton, alreadyMA, atomic or bounded-MA domination restriction. The specified compact good smooth separated boundaryless quotient carrier is explicitly retained analytic input; full genuine nonalgebraization/coherent descent is not newly certified merely by current proofs.

414/415 independently reconstruct universal coercivity: normalizeda,C=-Ea,A=int(-a)theta²<=1,q0=Qtheta(a),q1=Qtheta_a(a), C=A+2q0/3+q1/3; -E(ta)=tA+t²(1-t/3)q0+t³q1/3<=t+1.5t²C. Every finiteFULLdualB gives int(-a)mu<=1+B+sqrt(6BC), and every full normalized maximizing tail Fmu>=-1 has common C_mu=(sqrt(6B)+sqrt(10B+8))²/4. Exact midpoint I/8 gives I(a,b)<=4(epsilon_a+epsilon_b), ALSO across different maximizing families. Nonordered moduli Psi_C(q)=q/2+sqrt(42Cq), Omega_C from actual finite Gauss grids includingw0=0,A1=0, H_C=Omega_C+sqrt(6C)(sqrt q+sqrt Psi_C). BOTH moving endpoint absolute MA moments and BOTH max energy gains <=H_C(I); difference of gains gives |Ea-Eb|<=H_C(I), WITHOUT L1mu. Complete proofs and actual fixed-fibre calibration are in full packet.

415 NEW same-sublevel UNIFORM THIRD TEST: for EVERY a,b,w in C_C, int|a-b|MAw<=T_C(I)=Omega_C(I)+2sqrt(6C)sqrt(Psi_C(I)). Actual smooth absolute-value ramps and continuous derivative multipliers only; no Borel/indicator gradient calculus or signedRadonDD(|f|T) assumption. Actual cap separation and finite-cover vector-lattice proof make span_R C uniformly dense in actual C(X), without metrizability/countabletests. Green then gives genuine weak limits MAa_i->nu and B(a_i,0)->omega against EVERY continuous test, positiveRadonmass2. Real E, referenceR=int a theta², U=int a B(a,0), P=int a MAa all converge, with |Ua-Ub|<=T_C(I) and |Pa-Pb|<=H_C(I)+sqrt(12CI). ALL4 crossMA moments and relevant movingmixedB moments converge to p. D(nu)=e-p=limD(MAa_i)<=2C EXACT, samea_i also maximizesnu, and UNIFORM THIRD TEST proves a_i L1(nu)-Cauchy. Only SIGNED int a_i mu->e-B; NO L1mu conclusion. For fixedt actualMA(ta_i) weak->(1-t)²theta²+2t(1-t)omega+t²nu; exact scalar cubic coefficients converge.

WHOLE ROOT414 additionally proves the canonical measure map V(mu)=nu is independent of EVERY normalized maximizing net, has D(Vmu)<=D(mu) by exact cubic one-sided Taylor, is IDEMPOTENT V(Vmu)=Vmu because samea-net maximizesnu, and fixes EVERY already sequence-generated actualMA(u). Every FIXED generatedu moment int u MAa_i converges by uniform ordered presentation errors; normalized presentations need NOT decrease. A fixed point is NOT proved sufficient for generated representation. 415 exact defect K=p-(e-B)=B-D(nu)>=0 and one-sided segments only give int w(nu-mu)<=K for w in C. C is NOT closed under arbitrary positive scaling/negation. A precise UNPROVED actual two-sided late perturbation condition on a dense vector test space would implynu=mu, but theta degenerates away from its coordinate skeleton so a positivity margin cannot be assumed.

415 LOCAL GEOMETRIC SECTOR is proved with fixed LaurentP1,P2 at full2x and ONE compact finite-flat representativef:V->U with singleton weightedGauss fibrex, degreeD. Properness concentrates EVERY point above nearby Gauss parameters atx. One compact parameterrectangle, larger basepolyannulus, collar,delta/epsilon,M produces actual bounded global capswr with normalizedenergy>=-2M and MAwr>=epsilon²*d_y delta_y at EVERY finite fibre point; d_y positiveINTEGER>=1,sumd_y=D, no extra field-extension factor. Therefore every fullmaximizing net is uniformly Cauchy/continuous on compactTheta of these finite fibres. IMPORTANT: shrinking coordinate radialpolyannuli need NOT fit the ordinary target neighborhoodU, because U can exclude same-radius cancellation points. Properness plus caps gives NO proved affinoid-neighborhood basis whose ENTIRE Shilov boundaries lie inTheta. The raw separate fragment says misleadingly finitely many fibres; the complete scoped paper correctly says finite fibres over a parameter family. Do not infer global upper control from this.

415 all-affinoidShilovformula constructs an ACTUAL canonical USC normalized upper relaxation R, independent of maxfamily, not an abstract functional weight. For full2tupleell(x)=lima_i(x), rho(x)+R(x)=inf_(affinoid neighborhood A ofx) max_(xi inGamma_A)[rho(xi)+ell(xi)]. Whole immediateGR6.3 ensures every pure2Shilovpoint is full2;6.4 bounds each originalcontinuouspositiveweight. Direct ordinary-tail regularization proves the formula in BOTH directions. R agrees with uniform equiLipschitzGauss limitg and R(y)<=g(tauy),maxR=0; ONLY ell(x)<=R(x) at full2. Equality at EVERY full2point, positivity/classicallypsh and ORIGINAL C/G or adequate independentlyproved analyticdomain remain UNKNOWN. GR6.5 REQUIRES alreadyUSC FULLPOINTWISE limit, so cannot close this gap. All residuals remain.

WHOLE ROOT WORKING NOTE independently proves a useful actual FINITE-tail-maximality bridge. Uniform thirdMA boundT_C permits an actual fast maximizing SEQUENCEa_n with I(a_n,a_(n+1))<=r_n and T_C(r_n)<=summabledelta_n, by selecting deficits<=min(r_(n-1),r_n)/8; no cofinality claim. Every M_(j,N)=max(a_j,...,a_N) lies in actualC_C. Actual orderM_(j,N)>=a_N plus tangent and uniformthirdtest gives 0<=E(M_(j,N+1))-E(M_(j,N))<=delta_N. Thus 0<=E(M_(j,N))-Ea_j<=R_j=sum_(n>=j)delta_n, L_j=sup_NE(M_(j,N)) decreasesj and tends toe. PointwiseS_j=suptaila_n is bounded finiteLSC and full2values decrease toell; ordinaryUSC U_j decreases too. NO positivity or C/G membership for S_j/U_j follows. Existing409 decreasing-net closure applies ONLY to actual generated positiveweights, not these topologicalregularizations. Finite maxima energy control is complete; passage to an actual analytic representative is the MAIN remaining step.

MAIN: SOLVE actual representability and EVERY arbitrary-support prescribed-measure equation, not only repeat already complete universal weak/moment/USC facts. Try a sufficient original analytic domain recognition, actual envelopes/orthogonality or legitimate variation replacement. The finite-tail-maxima control may give a precise sufficient compactness/regularizedenvelope bridge; prove required positivity, allpoint/pole representatives, energy and actualMA identification at exact domain, rather than defining an operator on a Banach completion. GR classicallypsh recognition alone is NOT enough to claim original minimalCLD/G membership without proof. No fullsupportcountableRadon, metrizability, densecountablepointset, arbitrary measurable-netMCT, minimumpositivity, unprovedpositiveUSCregularization or abstractinverseMA.

One geometric research proposal ONLY: examine whether affinoid neighborhoods near full2x can be described by finitely many FIXED analytic/Laurent moments such that EVERY nearby Shilovpoint lies in one of finitely many compact finiteGauss-fibre families with UNIFORM energy/atom coefficients. GR6.3 stratifies Shilov boundaries from generators of graded reductions, but a rational-domain presentation does NOT automatically supply uniform spectral graded generators as radii vary. Prove all necessary fixed-menu/finite-flat/interior/calibration claims or expose their precise failure. A finite tuple menu with common caps could give uniform upper control needed for R=ell; it still needs analytic positivity/recognition. Do not assume toricpolyannuli form an ordinaryGauss-neighborhoodbasis. Another proposal: derive actual two-sided variational inputs or sufficient envelopes from bounded-calculus and summabletailmaxcontrol. If impossible at current scope, provide a substantial new COMPLETE residual theorem or precise proved obstruction with honest originalOPEN status, not a narrower solved label. Root414 fibrewise measure interpolation consequences may be derived, but those alone do NOT solve originalrepresentation.

Original task/hypotheses/criteria byte-identical to terminal287. Need actualu in a justified analytic finiteenergydomain (includingpoles), MAu=EVERY eligiblemu, uniquenessmodconstants and all sufficient compactness/envelope/energy/comparison replacements. Full historical geometric/source audit retains its existing qualifications. Candidate=true only complete ORIGINAL; scoped advances candidate=false.'''
task = dict(problem=orig['problem'] + '\n\n' + request + '\nWHOLE mathematical DATA: ' + str(C / 'mathematical-packet-bindings.json') + '\nFull LOCALONLY primary DATA: ' + str(C / 'private-primary-packet-bindings.json') + '\nWhole book context DATA: ' + str(C / 'book-context-bindings.json'), completionCriteria=load(O / 'task.json')['completionCriteria'])
write(C / 'task.json', task)
write(C / 'input.json', dict(task=task, notes=[], assignment='Reconstruct whole414415 and finite-tail-maxima; solve actual analytic representation and arbitrary-support original MA existence'))
s = load(O / 'settings.json')
s['codex']['workspace'] = str(C / 'artifacts')
s['usagePrefix'] = 'catalogue-20261003/r289/P16.7-whole414415-actual-analytic-representation'
assert s['limits'] == dict(concurrency=1, attempts=1, providerCalls=1)
assert all(s[k]['model'] == 'gpt-6.1-sol' and s[k]['reasoning'] == 'xhigh' for k in ['codex', 'research'])
write(C / 'settings.json', s)
write(C / 'mathematical-packet-bindings.json', math)
write(C / 'private-primary-packet-bindings.json', primary)
write(C / 'book-context-bindings.json', context)
f = dict(prepared_utc=datetime.now(timezone.utc).isoformat(), round=289, atom='P16.7', directory=str(C), whole_math_files=len(math), whole_math_bytes=sum(e['bytes'] for e in math), private_primary_files=len(primary), whole_context_files=len(context), only_grants=[], model='gpt-6.1-sol', reasoning='xhigh', maximum_concurrent_campaigns=2, original_task_byte_identical_to_terminal_round=287, completion_criteria_byte_identical_to_terminal_round=287, source_documents_and_programs_DATA=True, original_closed=False, new_accepted_paper=False, whole414_compiler_status='success observed', whole415_compiler_status='UNVERIFIED: actual desktop request pending; retained binding predates invocation', other_native288_math_NOT_read_or_supplied=True, other_ACTIVE_math_read_or_supplied=False, hot_feedback_sent=False, all_full_primary_source_bodies_pixels_book_context_LOCALONLY=True)
for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'book-context-bindings.json', 'private-primary-packet-bindings.json']:
    f[name.replace('.json', '').replace('-', '_') + '_sha256'] = sha(C / name)
write(C / 'freeze.json', f)
print(json.dumps(f, indent=2))
