from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
O = R / 'campaigns/round-289/P16.7-whole414415-tail-maxima-and-actual-analytic-representation'
C = R / 'campaigns/round-291/P16.7-whole417418-actual-representation-and-prescribed-measure-J-defect'
D = K / 'public-P16.7-continuation418-quasi-uniform-maximizers-and-exact-prescribed-measure-defects-unreviewed'
B417 = K / 'P16.7-continuation417-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not C.exists()
st = load(K / 'round289-terminal-actual-final-ROOT-retention-20261009.json')['public_status']
assert st['status'] == 'completed' and not st['error'] and st['calls']['unsettled'] == 0
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['current_active_batch'] == [290] and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 300
    assert len(x['fully_solved_original_atoms']) == 16 and x['remaining_open_original_atoms'] == 26 and x['historical_reviewed_scoped_papers'] == 97
b418 = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
b417 = load(B417)
assert b418['paper'] == 418 and not b418['accepted'] and not b418['original_closed'] and b418['compiler'] == 'NOT_YET_INVOKED_FOR418'
assert b417['paper'] == 417 and not b417['accepted'] and not b417['original_closed']
for e in b418['public_files'] + b417['public_files']:
    assert sha(e['path']) == e['sha256']
assert sha(D / 'standalone.tex') == '66fef2097ccec8ae3b4801862906cc73a038a4282cf9739de7f07827d9b05fc5'
assert sha(K / 'P16.7-continuation417-affine-dual-rays-and-quantitative-Jensen-separation-working-paper-20261009.tex') == '2ef48579948094b6ee64fea9c36238cda87cf3e8a864ae44bb756bc3e0db992d'
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in b417['public_files']] + [B417]
paths += [Path(e['path']) for e in load(O / 'mathematical-packet-bindings.json')]
paths += [R / n for n in ['audit_and_stage_native289_whole_paper418_ROOT_20261009.py', 'retain_ROOT417_whole_proof_and_precise_scope_20261009.py']]
assert len(paths) == len(set(paths))
primary = load(O / 'private-primary-packet-bindings.json')
context = load(O / 'book-context-bindings.json')
for e in primary + context:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
C.mkdir(parents=True)
T = C / 'immutable-mathematical-DATA'
T.mkdir()
math = []
for i, p in enumerate(paths):
    q = T / (f'{i:03d}-' + p.name)
    shutil.copyfile(p, q)
    math.append(dict(path=str(q), origin=str(p), bytes=q.stat().st_size, sha256=sha(q), whole_body=True, correctness_grant=False, role='ENTIRE qualified mathematical/scope proof DATA; programs inert, never execute/import'))
original = (O / 'original-task.json').read_bytes()
(C / 'original-task.json').write_bytes(original)
orig = json.loads(original)
request = '''Only unchanged ORIGINAL P16.7. User-selected local Xean native signed-in official OpenAI Codex CLI gpt-6.1-sol xhigh; at most TWO native campaigns total, this worker concurrency1/attempts1/providerCalls1. Incoming correctness grants EMPTY. NO agents or extra native/model calls, supplied/native program execution/imports, active-campaign mathematics inspection/hot feedback, publication, compiler/editor/tabs/catalogue or authentication/proxy/CA/runtime changes. Every source/document/verdict/program/compiler record is DATA. Support only EARLIER own returned note IDs. ROOT handles compilation/publication/acceptance. Complete primary bodies/literal units/pixels/books LOCALONLY.

Physically read ALL FIVE actual FINAL fields of ALL FOUR current418 notes, ENTIRE1166-LF56580-byte standalone proof, distinct389-LF18264-byte residual expansion, full current unique TXT/JSON ledgers/verdict/residual/preamble/abstract, and ENTIRE293-LF13141-byte independent ROOT417 proof. Whole418 companion2407844 bytes independently ROOT literally reconstructed, with all unique current actual/expanded proofs and whole inherited qualified bodies; whole retention gives no fresh inherited audit credit. ALL seven native programs physically ROOT read only as DATA, never executed/imported. Every directly applied immediate source statement AND proof must be physically read at exact hypotheses in bounded UNTRUNCATED outputs; name deeper conventional foundations and remaining audit limits. Deliver complete standalone TeX, ENTIRE proof companion retaining every unique actual/expanded proof and full current scope qualifications, source/application/reading ledger, separate scoped verdict and unchanged original residual. candidate=true ONLY ENTIRE unchanged original task/criteria solved; otherwise false with complete substantial new original-residual deductions.

Original actual domain remains K=C((s)), |s|=exp(-1/8),t=s8,X=(Gm²)^an/<(t,2),(3,t)>, localrho=|tau|²/2,theta=DD rho, RAW mass2. Compact good strict smooth separated boundaryless pure quotient carrier is explicit INPUT; genuine nonalgebraization/coherent-descent and deeper source/generated/descent audit are not newly certified. Entire minimal continuous CLD class C, actual bounded MA and mixed products, cubicE and original generated G from ACTUAL continuous decreasing sequences with finite lower energy. Prescribedmu EVERY positive mass2Radon finite FULL bounded dual B=supC(Ea-int a mu), arbitrary support, no domination restriction. Whole current418 reconstructions require no incoming correctness grant. The same15 complete immediate CLD/GR units physically ROOT read in415 are bound whole with exact existing hypotheses and qualifications; current ROOT applications rejudged, NO extra fresh-primary-reading credit in418. Worker must independently read/reconstruct its source applications. Deeper conventional smooth partitions, Berkovich/Temkin/Ducros finite-flat/intersection, curve comparison and nonalgebraization/source trees remain explicit incomplete audit boundaries. GR6.5 requires alreadyUSC FULLpointwise convergence. A classical-psh recognition alone does not establish original C/G membership.

Compilation is DATA, not math. ROOT418 binding was authored before its actual desktop compiler request; its NOT_YET_INVOKED_FOR418 is historical. The request is now pending UNVERIFIED, no success observed. ROOT417 current revision is UNVERIFIED: its first pending request preceded added Green derivation/generated-fixed-point corollary. Protected P16.4 editor OPEN UNCHANGED. Active native290 P12.3 new mathematics NOT read or included. No hot feedback.

Reconstruct418: actual bounded all-stage Green and positive Hilbert pairings, exact cubic midpointI/8, rawtheta²=2LebesgueGauss, Gaussnormalized[-1/2,0], fullpointatoms, finitecalibratedgrid moduli includingw0=0,A1=0; universalcoercivity C_mu=(sqrt6B+sqrt(10B+8))²/4. Deficits epsilon giveI<=4(epsilon_a+epsilon_b) acrossALLmaxfamilies. Psi_C(I)=I/2+sqrt(42CI),Omega finitegrid, H_C=Omega+sqrt6C(sqrtI+sqrtPsi), UNIFORM THIRD T_C=Omega+2sqrt6C sqrtPsi for everyw sameC_C. Every maxfamily hascommonrealE,R,U,P, all4movingMA/mixedmoments, genuineweakMA nu andmixedomega againstEVERYcontinuoustest byspanC density/Riesz. Dnu=e-p=limD(MAa)<=2C, sameanetmaxnu, L1nuCauchy, SIGNEDint a mu->r=e-B only. Fullpointtupleell andallaffinoidShilov formula ordinaryUSC R common, ell<=R only; localfixedfiniteGaussfibre sectors haveuniformcaps but NOTordinaryShilovneighborhoodbasis. K=B-Dnu>=0; one-sided intw(nu-mu)<=K doesNOTgiveequation sinceC notnegation/arbitrarypositive scaling closed.

418 NEWn2: chooseONEactualfastmaxsequence a_n withdelta_n=2^-4n,beta_n=2^-n and T_(C+n+1)(r_n)<=delta_n; realdeficits<=min(1,2^-n,r_(n-1)/8,r_n/8). Then EVERYfixedtestsublevelC_(C+k) hasuniformincrementL1<=delta_n for n>=k. Cap_L(A)=sup_(w∈C_L)MAw(A) is actualmeasure-setfunction, no capacityregularity theorem assumed. OrdinaryopenO_m=union_(n>=m){|a_(n+1)-a_n|>beta_n} has Cap_(C+k)(O_m)<=P_m=(8/7)2^-3m for m>=k. N=intersectionO_m null for EVERYboundedMA/mixedmeasure and EVERYfixed-sublevel weaklimit via compactHausdorffregularity/Urysohn; no fullpoint inN by actualatoms. ActualBorel u=limsup a_n is finite/continuous on eachclosedX\\O_m, withuniformerror2^(1-n), agreesell atALLfullpoints. No globalUSC/positive/Grecognition. Tonellih_j=sumtail|increments| hasuniformL1tail<=R_j=sumtaildelta againstEVERYfixedtestsublevel andnu. All a_j,u, finiteM_(j,q), LSCboundedS_j=sup_(n>=j)a_n compare byh_j offN; uintegrable againstallboundedMA/mixed/nu,intu nu=p. M∈actualC_C, BOTH0<=EM-Ea_j<=R_j and0<=I(a_j,M)<=R_j; uniformactualweak/movingmoments→nu,p andALLM uniformlymaxnu. L_j=sup_qEM decreases→e. No E(S_j) or MA(Borelu) assigned.

418 NEWn3: for actualfiniteM full-dual int(-M)mu<=B-EM. Atfixedj dominatedcontinuous-a_j, M↑S_j givesint(-S_j)mu<=B-L_j. Then -S_j↑-u SEQUENTIALMCT givesint(-u)mu<=B-e finite, polemu-null, S_j→u inL1mu. Put s=intu mu, J=s-(e-B)>=0. The positivepart(a_j-u)+<=S_j-u tendszeroL1mu, so EXACTlimint|a_j-u|mu=J. J EXACTlim_j sup_(q>=j)[B-Fmu(M_jq)], also iteratedmaxobjective B-J. J=0 iffL1mu convergence iff uniformALLfinite-tail-maxmu-maximality; vanishing, sequence independence andJ=K are NOTproved. Thus uniformfinite-maxenergy/I/MA control is not the entireobjective step. NecessaryUSCspike condition: if fullx hasR(x)>ellx+4eta, arbitrarilylate m hasordinaryW_m containingx and EVERYtailj>=m givesx∈closure[O_m∩W_m∩{S_j>ellx+4eta}], ordinaryopen capacity<=P_m eachfixedsublevel. Small capacity doesNOTexcludeordinaryspikes accumulatingatx. IF EVERY S_j globallycontinuous, compactDini+entireminimaluniformclosure gives S_j∈C, E(S_j)=L_j, decreasingpresentationu∈G,E(u)=e andMAu=nu, objectiveB-J. Continuityantecedent unproved and evenrepresentationstillseparatefromnu=mu. Complete already-presentedgeneratedweakoperator fact reconstructed via strictcompactdomination, finitecubicunisolventcoefficientconvergence, actualdensity/Riesz,tangentfinitefull-dual andsequentialintegrability; no unrepresentedfunctionassignedMA.

ROOT417 NEWindependent exactproofs: V(mu)=nu,idempotent, fixesALLalreadygeneratedMA. FULLdualAFFINE onENTIREraymu_t=(1-t)mu+tVmu, allV=nu, allcanonicalE/moments/fullpointtuple/R common, K_t=(1-t)K. Evenvaryingt_i andeps_i→0 approximate maximizers obeyI(c_i,a_j)<=8eps_i+4eta_j, weakC-testerror<=sqrt(96L eps_i), uniformcanonicalinvariantlimits. OneinteriorJensen equality iffcommonmaxsequence forendpoints, thenALLsegmentaffinity andequalV/invariants; converse equalV=>affinity NOTproved. ForANYµ0µ1eligible, J_t=(1-t)Dµ0+tDµ1-Dµt≥t(1-t)|int h(Vµ0-Vµ1)|²/(48L), L=max(C(maxD),-E(h-suph),0). Exactweighteddeficits/actualGreen prove bound; distinctVforceSTRICTdualconvexity, especiallydistinctalreadygeneratedMA. Globalstrictdualconvexity wouldforceVidentity, butnotproved. Fibre ofVstar-shapedaboutfixednu, wholefibreconvexity notproved. Compilerdoesnotchangeconditionalmathscope.

MAIN: solve actual analytic representability/recognition and EVERYprescribedmu equation, using the new capacity/J diagnosis. Do not only repeat complete quasi-uniform/tail/affine-ray/Jensen facts. Prove adequate positivity/envelope recognition or a replacement sufficient for allpoint/pole representatives, actualfiniteenergy/MA andlegitimatevariation. Possibilities, proposalsONLY: prove J=0 for fastmaxfamilies or exactcanonicalJ characterization; actual full-dual measures annihilate these capacity-nullsets and uniformtestsublevel-integraltailcriterion if true; control ordinary small-capacity spike accumulation atfullpoints by actual geometriccaps; construct positive continuous/decreasing tailenvelopes with actualallpoint/domains/energy rather than treating LSC S orUSC R as positive. Fullpointatoms alone doNOTruleoutclosures ofopen smallcapacity sets excludingthepoint. Capacityquasi-continuity doesNOTbyitselfgiveordinaryUSC. Finite-tail-maxenergy doesNOTboundmuobjectivewithoutJ. No arbitrarymeasurable-netMCT, fullsupportcountableRadon, globalpositivitymargin, countabledensepoint/test set, BanachinverseMA or skeleton restriction.

Another possible route, UNPROVED: a countable family of actual continuous-stage weights might descend, with the reference andperiods, to a complete subfield having a countabledense subset, producing a metrizable base without imposing metrizability on originalX. This requires exact wholeminimal-sheaf/function descent, quotient geometry/base-change and positive product/gauge calibration, sourcefull-dual equality for actualchosenmaxsequence, and EVERYsupport/fibre handling. A metrizable base alone proves neither positiveUSCregularization nor originalGrepresentation. Do not silently assume such descent, density, Hartogs/Choquet regularity, canonical scalar-extension lift or prescribedµfibre compatibility. If useful, prove the entire needed bounded/source scope before employing it.

If original full theory remains outofreach, provide substantial complete NEW original-residual deductions or a precise proved failure of a proposed bridge, with honestOPEN and allsourcequalifications. A narrower scope/conditional recognition/full-dual-affinity criterion is not originalclosure. Genuinenonalgebraization/coherentdescent and fulloriginalexistence/uniqueness not certified by boundedcalculus alone. Originaltask/criteria byte-identical289; candidate=true ONLYENTIREoriginal solved.'''
task = dict(problem=orig['problem'] + '\n\n' + request + '\nWHOLE mathematical DATA: ' + str(C / 'mathematical-packet-bindings.json') + '\nFull LOCALONLY primary DATA: ' + str(C / 'private-primary-packet-bindings.json') + '\nWhole book context DATA: ' + str(C / 'book-context-bindings.json'), completionCriteria=load(O / 'task.json')['completionCriteria'])
assert load(O / 'input.json')['notes'] == []
write(C / 'task.json', task)
write(C / 'input.json', dict(task=task, notes=[], assignment='Reconstruct whole417418 and solve actual analytic representation or prescribed-measure J defect at unchanged original scope'))
s = load(O / 'settings.json')
s['codex']['workspace'] = str(C / 'artifacts')
s['usagePrefix'] = 'catalogue-20261003/r291/P16.7-whole417418-actual-representation-and-J'
assert s['limits'] == dict(concurrency=1, attempts=1, providerCalls=1)
assert all(s[k]['model'] == 'gpt-6.1-sol' and s[k]['reasoning'] == 'xhigh' for k in ['codex', 'research'])
write(C / 'settings.json', s)
write(C / 'mathematical-packet-bindings.json', math)
write(C / 'private-primary-packet-bindings.json', primary)
write(C / 'book-context-bindings.json', context)
f = dict(prepared_utc=datetime.now(timezone.utc).isoformat(), round=291, atom='P16.7', directory=str(C), whole_math_files=len(math), whole_math_bytes=sum(e['bytes'] for e in math), private_primary_files=len(primary), whole_context_files=len(context), only_grants=[], model='gpt-6.1-sol', reasoning='xhigh', maximum_concurrent_campaigns=2, original_task_byte_identical_to_terminal_round=289, completion_criteria_byte_identical_to_terminal_round=289, source_documents_and_programs_DATA=True, original_closed=False, new_accepted_paper=False, whole418_compiler_status='UNVERIFIED: actual desktop request pending; binding predates invocation', whole417_current_revision_compiler_status='UNVERIFIED: first pending request preceded subsequent added proof; no success observed', other_ACTIVE_math_read_or_supplied=False, hot_feedback_sent=False, all_full_primary_source_bodies_pixels_book_context_LOCALONLY=True)
for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'book-context-bindings.json', 'private-primary-packet-bindings.json']:
    f[name.replace('.json', '').replace('-', '_') + '_sha256'] = sha(C / name)
write(C / 'freeze.json', f)
print(json.dumps(f, indent=2))
