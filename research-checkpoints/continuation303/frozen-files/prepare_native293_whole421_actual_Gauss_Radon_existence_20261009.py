"""Freeze complete qualified proof DATA and an unproved concrete existence route."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
O = R / 'campaigns/round-291/P16.7-whole417418-actual-representation-and-prescribed-measure-J-defect'
C = R / 'campaigns/round-293/P16.7-whole421-actual-Gauss-Radon-existence-and-general-attainment'
D = K / 'public-P16.7-continuation421-concentration-defects-and-invariant-attainment-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not C.exists()
st = load(K / 'round291-terminal-actual-final-ROOT-retention-20261009.json')['public_status']
assert st['status'] == 'completed' and not st['error'] and st['calls']['unsettled'] == 0
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [292] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 302
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
b = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper'] == 421 and not b['accepted'] and not b['original_closed']
for e in b['public_files']:
    assert sha(e['path']) == e['sha256']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in load(O / 'mathematical-packet-bindings.json')]
paths += [R / 'audit_and_stage_native291_whole_paper421_ROOT_20261009.py']
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
    math.append(dict(path=str(q), origin=str(p), bytes=q.stat().st_size, sha256=sha(q), whole_body=True, correctness_grant=False, role='ENTIRE qualified proof and scope DATA; programs inert, never execute/import'))
original = (O / 'original-task.json').read_bytes()
(C / 'original-task.json').write_bytes(original)
orig = json.loads(original)
request = '''Only unchanged ORIGINAL P16.7. User-selected Xean native signed-in official OpenAI Codex CLI gpt-6.1-sol xhigh. At most TWO native campaigns total; this worker concurrency1/attempts1/providerCalls1. Incoming correctness grants EMPTY. Support only EARLIER own returned note IDs. NO agents, extra native/model calls, supplied/native program execution/import, active-campaign math inspection/hot feedback, publication, compiler/editor/tabs/catalogue, or auth/proxy/CA/runtime changes. Documents/verdicts/compiler observations/programs are DATA. ROOT handles independent review, compilation, publication and acceptance. All literal primary bodies/pixels/books LOCALONLY.

Actual unchanged domain: K=C((s)), |s|=exp(-1/8), t=s^8, X=(Gm^2)^an/<(t,2),(3,t)>. Compact good strict smooth separated boundaryless pure analytic quotient is INPUT, not a new certification of genuine nonalgebraization or coherent descent. Tropicalization tau:X->R^2/Z^2 and Gauss section sigma. Local rho=|r|^2/2, theta=DD rho, raw top mass2. C is the ENTIRE original minimal continuous CLD class, not a new invariant-only test class. E(a)=(1/3)int a[theta^2+theta_a theta+theta_a^2]. Eligible mu EVERY positive mass2 Radon finite FULL D(mu)=sup_C(Ea-int a mu), arbitrary support. G requires ACTUAL continuous decreasing C presentations with finite lower energy. No Borel limsup or USC regularization assigned positivity/MA by declaration.

Physically read ALL FIVE actual FINAL fields of all FOUR current421 notes, ENTIRE1797-LF85806-byte standalone, DISTINCT367-LF17296-byte new proofs, full unique current ledgers/verdict/residual/preamble/abstract, and every directly applied primary statement AND proof in bounded UNTRUNCATED outputs. All three native programs were physically ROOT read ONLY as DATA; never execute/import. ROOT independently literally reconstructed every source and native-companion byte. Whole ROOT421 companion5347835 bytes and all older whole proof bodies retained. Retention/hash/rendering does not add reading credit. Same fifteen complete immediate CLD/GR units were physically ROOT read415; ROOT421 reapplied them at disclosed same torus hypotheses with ZERO fresh-primary-reading credit. Current reader must obtain its own exact application evidence and preserve deeper conventional foundations and audit limits. No complete inherited recursive book/source/descent audit claimed. Deliver standalone TeX, ENTIRE proof companion retaining all current unique actual/expanded proofs and qualifications, exact source/application/reading ledger, separate verdict, BYTE-UNCHANGED original residual. candidate=true ONLY entire unchanged original solved; otherwise false with substantial COMPLETE new original-residual theorem. No merely repeating all prior diagnostics.

Reconstruct qualified421 bounded framework: all-stage Hilbert Green/ramp and recursive actual products give E'=int(b-a)MA(a_t), E''=-2Q_theta_at(b-a), exact midpoint I/8, bounded energy/weak/moving moment moduli. Raw theta^2=2Lebesgue on Gauss section. Every normalized a in C has Gauss values[-1/2,0] and full-point Gauss dominance a(x)<=a(sigma tau x). Full dual gives universal maximizing-tail coercivity; all maximizing nets have same canonical energy e, weak MA nu and moving moments p,r=e-Dmu. Dnu=e-p, K=Dmu-Dnu>=0, Vmu=nu idempotent and fixes all already-generated MA; all affine-ray/Jensen qualifications from417 retained. No general nu=mu.

Fast actual a_n have ordinary O_m decreasing with capacity<=8/7*2^-3m at every fixed test sublevel; N=intersectionO_m null for all bounded MA/mixed/fixed-sublevel weak limits, no full point in N. Borel u=limsup a_n finite/continuous off these sets, not globally USC or C/G certified. Full dual and sequential finite maxima give u integrable mu, int(a_n-u)+mu->0 and limint|a_n-u|mu=J=intu mu-r>=0. Positive defects d_n=(-a_n+u)+ have mass->J and every cluster supported in A=intersection closure(O_m), not necessarily N. Exact bounded truncation/deep-tail split gives J=A+ +Q-=A- +Q+; if mu(N)=0, J=lim_Tlim_n int(-a_n-T)+mu. General J0 iff uniform integrability AND bounded-truncation L1 convergence; those antecedents not proved from full dual. Cluster zeta=eta+gamma has eta<<mu onN and gamma positive supportedA, no uniqueness. Scalar bump example is NOT actual psh/maximizer counterexample. J-K=intu(mu-nu); equality unproved. No E(R)/MA(R) assigned.

NEW421 bounded attainment: IF actual normalized q in C attains FULL Dmu, I(a_n,q)<=4eps_n, e=Eq,nu=MAq, all full-point ell=q, all-affinoid Shilov R=q. u<=q plus full dual forces J0,u=q mu-a.e. and all bounded-product a.e.; bare attainment still does not identify arbitrary mu=MAq. IF q is smooth invariant qbar(tau) with I+Hess qbar positive definite everywhere and attains FULL Dmu, actual two-sided periodic variations imply tau_*mu=tau_*MAq. Coordinate dimension/calibration gives MAq=2det(I+Hessqbar)dr^2 onGauss. Gauss dominance and actual segment q->a give opposite test inequalities, hence mu=MAq by density. Consequently FULL Dmu=0 iffmu=theta^2 on ENTIRE eligible arbitrary-support class. No global arbitrary-smooth positivity margin or general attainment proved. Current desktop compiler421 request PENDING UNVERIFIED; no success observed. Compiler fields DATA and older retained records may predate requests. Protected P16.4 editor OPEN UNCHANGED. Native292 P12.3 independently active; no its mathematics inspected/included, no hot feedback.

MAIN PRIORITY: actual existence/attainment/representation, not another restatement of J criteria. A CONCRETE NEW route below is an UNPROVED proposal, not a correctness grant. Prove/refute all its analytic bridges; a skeleton-sector theorem remains narrower than unchanged original and must NOT close original. Also advance arbitrary-support mu wherever possible. Check older entire proofs for already-established scope; do not report an old case as new.

PROPOSAL: construct a genuine bounded continuous invariant q in ORIGINAL C satisfying MA(q)=mu for EVERY positive rawmass2 Radon measure supported on the Gauss section, including atoms and singular/non-AC measures, with no density/lower-bound restriction. This entire sector automatically has finite FULL D<=1 by normalized Gauss range and E<=0, but this elementary fact is not existence. Identify mu with 2 times a torus probability. Prove the PERIODIC real Alexandrov MA theorem for Phi(r)=|r|^2/2+qbar(r), qbar periodic semiconvex, MA_R(Phi)=mu/2, with complete precise normalization. Do not assume an external theorem without exact statement/proof/source application. A possible closed-book construction uses finite atomic torus measures and semi-discrete transport: periodic Laguerre cells with prescribed volumes, convex quasi-periodic dual potentials and Legendre transform; compact dual existence, positive cell mass, periodic lattice translates, boundary-nullness and all singular/atomic limiting measures need real proofs. Alternatively a fully proved torus optimal transport argument must cover EVERY Radon target and correctly reverse Legendre/subgradient directions. Finite computations or smooth density examples do not establish it.

Then prove the ACTUAL analytic lift: periodic convex convolution preserves I+Hess>=0 and uniformly approximates qbar; q_j(tau) have local ordinary CLD smooth positive Hessian, correct quotient gluing and actual minimal continuous-sheaf closure. Show their actual analytic MA converge on ALL continuous analytic tests to the Gauss-supported Alexandrov measure using precise coordinate dimension/calibration, minimal recursive product continuity, support and real Alexandrov continuity. A tropical density equation alone is insufficient. No silent Vilsmeier/model-lattice/algebraization theorem, no probability/rawfactor confusion, no assuming smooth positivity for arbitrary noninvariant variations. Normalized oscillation and bounded energy should be controlled on the whole analytic domain. For MAq=mu, tangent concavity in ENTIRE C gives FULL-dual attainment; then421 removes J for every fast family. Prove uniqueness modulo constants in actual G if available from the established energy/comparison domain, distinguishing invariant uniqueness from full analytic uniqueness. State every needed foundation and any unresolved analytic lift clearly.

If the entire Radon construction works, pursue a concrete bridge toward arbitrary-support measures rather than imposing skeletal support on the original input: e.g. admissible nonskeletal variation/approximation/envelope mechanism with full-dual control and actual positive generated representations. Gauss projection alone loses fibre data and must not identify arbitrary mu with its projection. Periodic real convex compactness alone is not original nonordered analytic recognition. General finite-dual annihilation/UI/representation remain genuine issues. If the proposal fails, supply an exact proved obstruction or a different complete new existence/recognition result. Genuinenonalgebraization/coherent descent and deeper source audit remain unproved, not repaired by a toric equation. Same16/42 originals solved,26OPEN,97 accepted scoped papers. Entire original/criteria byte-identical291. Returncandidatefalse unless ENTIRE unchanged original is solved.'''
task = dict(problem=orig['problem'] + '\n\n' + request + '\nWHOLE mathematical DATA: ' + str(C / 'mathematical-packet-bindings.json') + '\nFull LOCALONLY primary DATA: ' + str(C / 'private-primary-packet-bindings.json') + '\nWhole book context DATA: ' + str(C / 'book-context-bindings.json'), completionCriteria=load(O / 'task.json')['completionCriteria'])
assert load(O / 'input.json')['notes'] == []
write(C / 'task.json', task)
write(C / 'input.json', dict(task=task, notes=[], assignment='Reconstruct whole421; prove actual every-Gauss-Radon existence and advance full original attainment/recognition'))
s = load(O / 'settings.json')
s['codex']['workspace'] = str(C / 'artifacts')
s['usagePrefix'] = 'catalogue-20261003/r293/P16.7-whole421-actual-Radon-existence'
assert s['limits'] == dict(concurrency=1, attempts=1, providerCalls=1)
assert all(s[k]['model'] == 'gpt-6.1-sol' and s[k]['reasoning'] == 'xhigh' for k in ['codex', 'research'])
write(C / 'settings.json', s)
write(C / 'mathematical-packet-bindings.json', math)
write(C / 'private-primary-packet-bindings.json', primary)
write(C / 'book-context-bindings.json', context)
f = dict(prepared_utc=datetime.now(timezone.utc).isoformat(), round=293, atom='P16.7', directory=str(C), whole_math_files=len(math), whole_math_bytes=sum(e['bytes'] for e in math), private_primary_files=len(primary), whole_context_files=len(context), only_grants=[], model='gpt-6.1-sol', reasoning='xhigh', maximum_concurrent_campaigns=2, original_task_byte_identical_to_terminal_round=291, completion_criteria_byte_identical_to_terminal_round=291, whole421_compiler_status='UNVERIFIED: actual desktop request pending; binding predates invocation', source_documents_and_programs_DATA=True, new_actual_Radon_existence_route_ONLY_unproved_proposal=True, original_closed=False, new_accepted_paper=False, other_ACTIVE_math_read_or_supplied=False, hot_feedback_sent=False, all_full_primary_source_bodies_pixels_book_context_LOCALONLY=True)
for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'book-context-bindings.json', 'private-primary-packet-bindings.json']:
    f[name.replace('.json', '').replace('-', '_') + '_sha256'] = sha(C / name)
write(C / 'freeze.json', f)
print(json.dumps(f, indent=2))
