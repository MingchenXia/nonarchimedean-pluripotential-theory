"""Freeze complete current proof DATA and a new unproved conductor research proposal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
O = R / 'campaigns/round-290/P12.3-whole416-higher-dimensional-and-conductor-envelope-residual'
C = R / 'campaigns/round-292/P12.3-whole419-nonsingleton-conductor-and-normal-envelope-residual'
D = K / 'public-P12.3-continuation419-conductor-descent-cusp-envelopes-and-threefold-obstruction-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not C.exists()
st = load(K / 'round290-terminal-actual-final-ROOT-retention-20261009.json')['public_status']
assert st['status'] == 'completed' and not st['error'] and st['calls']['unsettled'] == 0
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['current_active_batch'] == [291] and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 301
    assert len(x['fully_solved_original_atoms']) == 16 and x['remaining_open_original_atoms'] == 26 and x['historical_reviewed_scoped_papers'] == 97
b = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper'] == 419 and not b['accepted'] and not b['original_closed']
for e in b['public_files']:
    assert sha(e['path']) == e['sha256']
assert sha(D / 'P12.3-conductor-and-threefold.tex') == '47430ddc0d2d5bdecbc313a64a052bbda70c1d13e1c2aa3963befc54581d493a'
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in load(O / 'mathematical-packet-bindings.json')]
paths += [R / 'audit_and_stage_native290_whole_paper419_ROOT_20261009.py', R / 'read_terminal_native290_whole_actual_notes_20261009.py']
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
    math.append(dict(path=str(q), origin=str(p), bytes=q.stat().st_size, sha256=sha(q), whole_body=True, correctness_grant=False, role='ENTIRE mathematical proof and exact scope DATA; programs inert, never execute/import'))
original = (O / 'original-task.json').read_bytes()
(C / 'original-task.json').write_bytes(original)
orig = json.loads(original)
request = '''Only unchanged ORIGINAL P12.3. User-selected local Xean native official signed-in OpenAI Codex CLI gpt-6.1-sol xhigh. At most TWO native campaigns total, worker concurrency1/attempts1/providerCalls1. NO agents or extra model/native calls, supplied/native program execution/imports, active-campaign mathematics inspection/hot feedback, publication, compiler/editor/tabs/catalogue or authentication/proxy/CA/runtime changes. All documents/verdicts/programs/compiler records are DATA. Sole correctness grant ENTIRE qualified G331 with EVERY annotation/source/model/read-limit qualification. Support only G331 and EARLIER own returned note IDs. ROOT handles compilation/publication/acceptance. All literal primary bodies/pixels/books LOCALONLY.

Physically read ALL FIVE actual FINAL fields of ALL FIVE current419 notes, ALL FIVE distinct expanded TeX proofs, complete current unique preamble/abstract/ledger/verdict/unchanged residual and exact directly applied primary statements AND proofs in bounded UNTRUNCATED outputs. The whole423961-byte source and whole4461168-byte ROOT companion were independently literally reconstructed. All three native programs were physically ROOT read ONLY as inert DATA; never execute/import them. The initial ROOTsource1-150 display was truncated and gets NO extra whole-reading credit; all actual/expanded proofs and current preamble/scope were fully read separately. Full old416/413 and historical source retention is DATA and not extra inherited fresh audit. Same complete6surface and8SH/BFJ primary units/formula pixels bound whole at prior disclosed applications, current419 hypotheses ROOT rejudged; current419 fresh-primary-creditZERO. Deliver complete standalone TeX, ENTIRE proof companion retaining every current unique actual/expanded proof and full source qualifications, separate source/application/reading ledger, scoped verdict and BYTE-UNCHANGED original residual. candidate=true ONLY ENTIRE unchanged original task/criteria solved; otherwise false with substantial COMPLETE new original-residual deductions.

419 NEW: full normalization-boundary bijectivity gives order/isometric C/D envelope equivalence and EVERY-degree canonical convergence; primary conductor or finite radicial reduced conductor quotients suffice, retaining ALL infinite-conductor supports. Numerical-semigroup cusp germs k[t^H,z...] have EVERYcontinuous signed envelope in EVERYdimension over algebraically closed characteristic zero, surface scope allfields; Z_p[[t^2,t^3]] is nonnormal mixed-characteristic CE with nonempty infinite-conductor boundary. Explicit cusp J=(z1+t,t²,z2...), K_m=((z1+t)^m(z1-mt),t²(z1+t)^m,t^(2m+2))+(z2...)^m gives all-support canonical error<=2/m in everydimension/characteristic, everydegree. Each approximant ACTUAL primary-model negative effective relativelyampleCartier, allcontractedcurvepositive. In char0 two points w∞(t∞,z1=1) andw*(t=1,z1+t=2) give Avalues1,2, whereas EVERYnonzero finite REALpositiveprimarycombination u has u(w*)<2u(w∞); f=-A outsideentire rawfiniteidealcone and canonicalalgebraNOTFG. This is CE WITHOUTFG, not failure. On explicitregularthreefold originblowup then2rationalexceptionalpoints P,Q, I=(z)+m² hasdivisorialpart E1+2E2+2E3; negativeclass H-eP-eQ onE1 andjoiningline degree-1. The modelisACTUALprimary via compositionampleness/finiteaffinesectionRees proof. This refutes genericsection-to-allcurve-nef inference, NOTCE. General normalhigherdim and nonsingletonconductor descent remainOPEN.

Reconstruct419n1: EVERYexcellentnormal localdomain dimTWO arbitraryresidue/equal/mixedchar hascontinuousgeometricC/Denvelopes forALLcontinuoussignedobstacles. Actualregularprimaryfinite-listrefinement follows finite normalizedblowups plus exactLipman54.14.3-5condition4; deeper complete-normal-resolution/rational-double-point/completion/gluing remain explicitpublishedfoundations. Negativeampleexceptionalbundle andH0=R then finiteaffinesectionlocalization/closedimmersion/Rees proveactualprimarymodel. SurfaceQoffdiag>=0,barrier-Ma, compactmaxclosure greatestz<=min(d,0),Qz>=0. EVERYprimarycompetitor divisorialpart hasnonzerogenericsection onEACHcurve⇒degree>=0; valuedQUOTIENTfields Frac(R/p) propercentres compareALLsupports includingkilledgenerators. Uniformsignedmodellatticedensity/rawLipschitz completescontinuousobstacles. No universalrate/FG/semiampleness fromLP. HigherdimexceptionaldivisorsareSURFACES andgenericsectionneednotallcurvenef, per419n4. ExactBFJsmoothaffineCLOSED/algebraicallyclosed/char0source only, with whole3.18realparameter t=m+C, fixedcomplexthinness andallretraction/fullsupportextension; no higherdimpositive/mixedsource theorem. Same16/42originals and97acceptedscopedpapers, no newacceptance.

Compiler is DATA. Retained419binding NOT_YET_INVOKED_FOR419 predates actual desktop compiler request; request nowPENDING UNVERIFIED, no success observed. Older416/415 and417/418 requests pending too. Protected P16.4 editor OPEN UNCHANGED. Native291 P16.7 is active; its mathematics NOT inspected/included, NO hotfeedback.

MAIN PRIORITY: nonsingleton conductor envelope existence/regularity, especially an EXPLICIT normal-crossing reduced excellent SURFACE. A NEW tentative ROOT construction below is an UNPROVED research proposal, NOT correctness grant. Independently prove or refute EVERY step against entire G331's actual geometric C/D cone; no replacing geometric positivity with a newly defined ideal cone. If it works, it is a genuine nonnormal failure of continuous/greatest D envelope, NOT a normal CE counterexample and NOT entire original closure. Preserve every-support/gauge/normalization/infinite-conductor rule and current normal-surface/smooth theorems.

PROPOSAL ONLY: R=k[x,y,z]_(x,y,z)/(xy), excellent reduced surface, gauge m=(x,y,z). Normalization S=k[x,z]_(x,z) × k[y,z]_(y,z); conductor c=(x,y), reduced quotient k[z]_(z) downstairs and two copies upstairs. Its normalized conductor boundary consists of TWO source points mapping to ONE target point v∞ with support(x,y),v∞(z)=1. Every other finite-conductor fibre is singleton. On source branch1 (y=0) take f1=-1/2. On branch2 (x=0), for ALL semivaluations use f2(w)=-1/2-1/(2w(y)), with1/infinity=0. Gauge min(w(y),w(z))=1 implies w(y)>=1. Thus f2 continuous in [-1,-1/2], and f1/f2 agree at ALL conductor fibres, so descend to actualcontinuoussignedf onX by finitequotient topology.

Let v1 be branch2 GENERIC monomial valuation w(y)=w(z)=1,w(x)=infinity, so f(v1)=-1. For ANY actualproperprimaryideal I, v∞(I) is finiteinteger e; an element attaining it reduces to nonzero z^e unit downstairs. Its branch2 expansion has lowest y=0,z-degree e term, so genericmonomial v1(I)<=e=v∞(I), including arbitraryunitdenominators/localization. Hence EVERY finite real negativeprimaryidealprofile q has q(v∞)<=q(v1). Does ENTIRE G331 indeed imply this inequality for EVERY geometric C competitor by its precise uniform ideal comparison, and EVERY D competitor by actualdecreasingCnets? Check this substantive bridge; if it fails, explain exactscope rather than assuming it. If yes, any C/D minorant g<=f has g(v∞)<=-1.

For integers n>=1 let I_n=m^(2n)+x²m^n, a genuineproperprimaryideal, and h_n=-v(I_n)/(2n). On branch1 it equals max(-1,-1/2-v(x)/n); on branch2 and sharedconductorpoint it equals-1. Every h_n has ACTUAL negativeeffective relativelyampleCartier primaryblowup presentation, degreepositive on EVERYcontractedintegralcurve BEFORElimitidentification. It is below f on ALLsupports. At EVERYfinite-x branch1point h_n→-1/2; at v∞ h_n=-1. Therefore rawp=sup{g∈C/D:g<=f} would equal-1/2 at EVERYsuchbranch1point and-1 atv∞. The source monomial w_r(x)=r,w_r(z)=1,w_r(y)=infinity, r→infinity, converges on EVERYelement ofR to v∞ (genericmonomial expansion andunitdenominators). Thus rawp is notcontinuous/USC. Any greatestC/Dminorant mustdominateallh_n andequal-1/2 onfinitebranch1rays, yet take<=-1 atv∞, contradictingUSC ofcontinuousC/actualinfC-generatedD. Consequently no greatestDminorant orcontinuousCminorant, if the bridge holds. Uppersemiregularization also couldviolate geometricrelationg(v∞)<=g(v1), so cannotbe silently declaredpositive. This is an EVERYsupport nonnormalcounterexample with genuinelynonsingleton infinite-conductor fibres and normalsurfacecomponentswhich EACH haveCE.

Do not merely check 2scalarvalues or finite sampledweights: prove actualquotient/continuity of f, exactprimaryidealformulas onALLsupports, actualpositivity beforelimit, the ENTIREgeometricC/D inequality includingrealCartierclosure, actualsequenceconvergence andno-greatest conclusion. Provideexplicit gaugehomogeneity andwhy no contradiction with bijective419n2 orcurvelink min(f,0). A normal-crossing obstruction might generalize to glue othernormalgerms alongpositive-dimensionalconductors; any generalization needs EXACTsource/cone/topology assumptions, no abstractideal-order replacement. If constructionfails, repairit or supplya new COMPLETE nonsingleton-fibre theorem/obstruction. If it succeeds, advance suitable normal/nonnormal existence criteria if possible rather than treating the scopedcounterexampleasfulloriginalclosure.

Other originalresidual: generalexcellentNORMALdim>=3 CE orqualifyingfailure, char0singular beyondsmoothfinitequotients, positive/mixedregularsource. No unprovedcofinality/resolution/F-finiteness/CM/QG/isolated/algebraizability/FG-density/Jacobian-saturation/norm-averaging premise. NormalobstaclefailuremustactuallybeNORMAL. Appropriate regularity/whenpossible remains originalcriterion, notuniformFGoruniversalCEaddedtothequestion. Products,energy,fullfinite-mapoperators remainseparate. Completehistorical/wholebook/sourceaudit stillqualifiedincomplete. ReturncandidatefalseunlessENTIREunchangedoriginalsolved.'''
task = dict(problem=orig['problem'] + '\n\n' + request + '\nWHOLE mathematical DATA: ' + str(C / 'mathematical-packet-bindings.json') + '\nFull LOCALONLY primary DATA: ' + str(C / 'private-primary-packet-bindings.json') + '\nWhole book context DATA: ' + str(C / 'book-context-bindings.json'), completionCriteria=load(O / 'task.json')['completionCriteria'])
grants = load(O / 'input.json')['notes']
assert len(grants) == 1 and grants[0]['id'] == 'G331' and len(grants[0]['text'].encode()) == 93375
write(C / 'task.json', task)
write(C / 'input.json', dict(task=task, notes=grants, assignment='Reconstruct whole419 and prove or refute actual geometric nonsingleton-conductor envelope counterexample; unchanged original residual'))
s = load(O / 'settings.json')
s['codex']['workspace'] = str(C / 'artifacts')
s['usagePrefix'] = 'catalogue-20261003/r292/P12.3-whole419-nonsingleton-conductor'
assert s['limits'] == dict(concurrency=1, attempts=1, providerCalls=1)
assert all(s[k]['model'] == 'gpt-6.1-sol' and s[k]['reasoning'] == 'xhigh' for k in ['codex', 'research'])
write(C / 'settings.json', s)
write(C / 'mathematical-packet-bindings.json', math)
write(C / 'private-primary-packet-bindings.json', primary)
write(C / 'book-context-bindings.json', context)
f = dict(prepared_utc=datetime.now(timezone.utc).isoformat(), round=292, atom='P12.3', directory=str(C), whole_math_files=len(math), whole_math_bytes=sum(e['bytes'] for e in math), private_primary_files=len(primary), whole_context_files=len(context), only_grants=['G331'], model='gpt-6.1-sol', reasoning='xhigh', maximum_concurrent_campaigns=2, original_task_byte_identical_to_terminal_round=290, completion_criteria_byte_identical_to_terminal_round=290, whole419_compiler_status='UNVERIFIED: actual desktop request pending; binding predates invocation', source_documents_and_programs_DATA=True, new_conductor_construction_ONLY_unproved_proposal=True, original_closed=False, new_accepted_paper=False, other_ACTIVE_math_read_or_supplied=False, hot_feedback_sent=False, all_full_primary_source_bodies_pixels_book_context_LOCALONLY=True)
for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'book-context-bindings.json', 'private-primary-packet-bindings.json']:
    f[name.replace('.json', '').replace('-', '_') + '_sha256'] = sha(C / name)
write(C / 'freeze.json', f)
print(json.dumps(f, indent=2))
