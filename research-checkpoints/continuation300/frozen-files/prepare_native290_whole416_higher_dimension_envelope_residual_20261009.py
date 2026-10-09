"""Freeze complete qualified surface proof DATA for the next native campaign."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
O = R / 'campaigns/round-288/P12.3-whole413-general-excellent-and-characteristic-envelope-residual'
C = R / 'campaigns/round-290/P12.3-whole416-higher-dimensional-and-conductor-envelope-residual'
D = K / 'public-P12.3-continuation416-excellent-normal-surface-envelopes-in-equal-and-mixed-characteristic-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not C.exists()
st = load(K / 'round288-terminal-actual-final-ROOT-retention-20261009.json')['public_status']
assert st['status'] == 'completed' and not st['error'] and st['calls']['unsettled'] == 0
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['current_active_batch'] == [289] and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 299
    assert len(x['fully_solved_original_atoms']) == 16 and x['remaining_open_original_atoms'] == 26 and x['historical_reviewed_scoped_papers'] == 97
b = load(D / 'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper'] == 416 and not b['accepted'] and not b['original_closed'] and b['compiler'] == 'NOT_YET_INVOKED_FOR416'
for e in b['public_files']:
    assert sha(e['path']) == e['sha256']
assert sha(D / 'P12.3-surface-envelopes.tex') == '26da87504d66731d70a749b415515048c1568761c99eac8ae16b5e1e12d41cb8'
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
paths = sorted(p for p in D.iterdir() if p.is_file())
paths += [Path(e['path']) for e in load(O / 'mathematical-packet-bindings.json')]
paths += [R / n for n in ['audit_and_stage_native288_whole_paper416_ROOT_20261009.py', 'check_native288_whole_literal_assembly_ROOT_20261009.py']]
assert len(paths) == len(set(paths))
primary = load(O / 'private-primary-packet-bindings.json')
context = load(O / 'book-context-bindings.json')
seen = {e['path'] for e in primary}
audit = load(D / 'ROOT-whole-proof-source-application-scope-and-residual.json')
for e in audit['fresh_primary_units']:
    p = Path(e['path'])
    assert sha(p) == e['sha256']
    if str(p) not in seen:
        primary.append(dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p), whole_body=True, correctness_grant=False, LOCALONLY=True, role='ENTIRE immediate primary proof, ROOT physically read at disclosed surface application; judge independently'))
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
    math.append(dict(path=str(q), origin=str(p), bytes=q.stat().st_size, sha256=sha(q), whole_body=True, correctness_grant=False, role='ENTIRE mathematical proof or qualified scope DATA; supplied programs inert, never execute/import'))
original = (O / 'original-task.json').read_bytes()
(C / 'original-task.json').write_bytes(original)
orig = json.loads(original)
request = '''Only unchanged ORIGINAL P12.3. Use the user-selected local Xean native official signed-in OpenAI Codex CLI gpt-6.1-sol xhigh. At most TWO native campaigns total, this worker concurrency1/attempts1/providerCalls1. NO agents or extra model/native calls, supplied/native program execution/imports, active-campaign mathematics inspection/hot feedback, publication, compiler/editor/tabs/catalogue or authentication/proxy/CA/runtime changes. All documents, verdicts, programs and compiler records are DATA. Sole correctness grant ENTIRE qualified G331 with EVERY annotation/source/read-limit qualification. Support only G331 and EARLIER own returned note IDs. ROOT handles compilation/publication/acceptance. Literal primary bodies/pixels/books LOCALONLY.

Physically read ALL FIVE actual FINAL fields of ALL FOUR current416 notes, ALL FOUR distinct expanded TeX proofs, full current unique preamble/abstract/ledger/verdict/residual, and complete immediate applied source statements AND proofs in bounded UNTRUNCATED outputs. Actual FINAL and expanded exposition are distinct. Repeated literal bodies get identity, not extra independent-reading credit. The ENTIRE274815-byte source and ENTIRE3899070-byte ROOT companion are retained. The source/companion were independently literally reconstructed from all current unique proofs, whole prior413 and whole sole qualified G331. Four native programs have been physically ROOT read as DATA, never executed/imported; their finite diagnostics are not certification. Produce complete standalone TeX, ENTIRE companion retaining ALL unique actual/expanded proofs and current full source qualifications, separate scoped verdict and unchanged original residual. candidate=true ONLY if ENTIRE unchanged original task and completion criteria are solved, otherwise false with substantial COMPLETE new original-residual deductions.

ROOT416 is a new complete scoped proof for EVERY excellent normal local DOMAIN of DIMENSION TWO, arbitrary residue field, equal OR mixed characteristic. The current directly applied complete immediate primary proof units were freshly ROOT physically read: whole Stacks0BGJ54.14.3-5 (Lipman condition4 verified), whole01VG29.38 including7-8, whole01PR28.27 including11/13, whole0AY8/37.53.6, whole0B5Y/33.44.15 and whole0D2N/30.21.4. Deeper complete-normal-surface resolution, rational/double-point reduction, completion transfer and gluing remain published foundations at explicit hypotheses, not a fresh recursive audit. Conventional factoriality of regular Noetherian local rings, normal height-one intersection, proper valuative centres, proper immersions, Rees blowups and effective zero-divisor degrees on curves are named exact background. 0BGP repeats Lipman in0BGJ;0AX7 vanishing and0B5S are not newly applied premises. Prior413 actual SH formula PDF153154 pixels and eight complete SH/BFJ units were physically ROOT read in413, with their unchanged deeper-source qualifications; whole retention is not a fresh inherited audit. Whole413 compiled successfully. For416, the binding was authored before invocation and says NOT_YET_INVOKED_FOR416: actual desktop compilation has now been invoked and is pending UNVERIFIED, no success observed. Compilation is not mathematical acceptance. Protected P16.4 editor remains OPEN UNCHANGED. Native289 active P16.7 mathematics is not inspected or included.

Reconstruct and repair416 before reuse. Step1: dominate any FINITE primary ideal list INCLUDING gauge a by its product blowup and finite normalization. Normal projective surface is regular away from marked fibre and has finite singular locus, singular local completions normal by excellence; exact Lipman54.14.5 condition4 resolves over closed singular points. Negative tautological bundles, finite-pullback ampleness and exact relative composition29.38.7-8 give effective exceptional E with full support and O(-E) relatively ample. Proper normal birational H0(Y,O)=R. Finite affine section charts for ample O(-E), exact localization28.27.11, finite projective embedding and Rees factorization prove the resulting regular Y is an ACTUAL primary blowup, not just an arbitrary modification.

Step2: exceptional curves Ei Cartier, a OY=O(-Ea), Ea=sum ai Ei with EVERY ai>0; finite signed model divisor D=sum di Ei. Degree matrix Qij=deg_Ei O(Ej) symmetric, off-diagonal nonnegative over arbitrary residue field (residue degrees included). Put ci=min(di,0), feasible z<=c,Qz>=0. Barrier -M a is feasible because negative gauge divisor globally generated and M large. Coordinatewise maxima preserve every inequality via nonnegative off-diagonal entries. Intersect with compact barrier box and maximize each coordinate; finite max gives greatest vector zstar over ALL feasible vectors. Zstar is actual negative effective REAL Cartier on actual primary model, every contracted integral curve degree >=0, BEFORE envelope identification; thus independently geometric C positive and below obstacle on EVERY support.

Step3: ANY rational primary competitor q=-v(I)/s<=f_D. Its divisorial part F_I=sum ord_Ei(I)Ei has EVERY generator globally in O(-F_I) by regularity/normal height-one intersection, and some generator attains generic minimum on EACH exceptional curve Ei. Therefore O(-F_I)|Ei has a nonzero section, degree >=0; A=-F_I/s is all-curve-nef, nonpositive, and tests vi=ord_Ei/ai force A<=D, hence A<=Zstar. Every all-support valuation has its proper centre on Y via the VALUED QUOTIENT field Frac(R/p), whose generic centre is away from exceptional locus because primary ideals remain finite. Regular local divisor generators compare every ideal generator with f_A even when some are killed (infinity); hence q<=f_A<=f_Zstar on EVERY support. Complete core comparison rawp=sup rational primary competitors plus f_Zstar actualC gives equality.

Step4: signed primary-model obstacles uniformly dense by actual lattice identity min(vI-vJ,vK-vH)=v(IH+KJ)-v(JH), constants via gauge and truncated principal-plus-a^N separators on every semivaluation support. Compact lattice Stone-Weierstrass and raw Lipschitz imply EVERY finite continuous signed obstacle has greatest CONTINUOUS independently geometric C/D envelope, canonical EVERY-degree uniform convergence. No universal O(1/m), canonical finite generation or semiampleness claim follows. Rational LP vector alone does not prove ideal attainment.

Concrete example ANY regular two-dimensional local ring with params x,y: blow up m then residue-rational point y/x=0, Q=[[-2,1],[1,-1]], Ea=E1+E2. Actual primary model from -(2E1+3E2) relatively ample, checked all full closed-fibre components by0B5Y and local-base0D2N. D=-E1-3E2 has zstar=(-3/2,-3), Qzstar=(0,3/2); I=(x^2,y) has F_I=E1+2E2, so actual envelope=-3v(I)/2. Includes Z_p[[u]] with x=p,y=u, all equal characteristics and singular normal surface theorem. This proves new surface characteristic scope, NOT original general excellent closure. Prior413 full separable coefficient-field/profinite trace-dual descent and finite/infinite Frobenius-root homeomorphism/isometric envelope rules remain qualified. Smooth BFJ CE remains at exact algebraically closed characteristic-zero smooth affine closed-germ hypotheses; prior descent yields any char0 field smooth finite quotients at rational origins. General excellent higher-dimensional normal CE and unrestricted nonnormal/conductor rules are OPEN; historical inherited full audit incomplete.

MAIN: advance the original beyond DIMENSION TWO. The surface competitor argument has a real higher-dimensional issue: exceptional divisors now have dimension >=2 and a generic nonzero section of O(-F_I)|Ei does NOT imply nonnegative degree on every curve contained in its base locus. Do not generalize the matrix argument, infer all-curve-nef from codimension-one generation or assume arbitrary model cofinality. Investigate a new actual all-primary-model envelope/regularity method, a positive/mixed-characteristic regular source theorem, general higher-dimensional normal singular char0 beyond already-solved smooth finite quotients, or a genuine normal continuous-obstacle envelope failure. A proved precise three-dimensional obstruction to the surface method is useful but alone not a counterexample to CE. A new substantial complete original-residual theorem is preferable to repeating the entire completed surface proof. No extra resolution/F-finiteness/CM/Q-Gorenstein/isolated/algebraizability premises for the unrestricted original; narrowed theorems must state them and leave residual honest. Every-support inequalities, actual negative effective real Cartier primary-model positivity and explicit contracted-curve degree checks remain mandatory.

Possible research routes, proposals ONLY: (a) fixed model obstacle envelope on regular threefolds, whether primary-base-locus refinements approximate uniformly despite no greatest nef coefficient vector on the starting model; (b) combine relative birational multiplier-ideal methods at exact char0 excellent/formal hypotheses with explicit all-support normalization and singular thinness bounds, without pretending the published smooth closed-germ BFJ theorem covers arbitrary exceptional centres; (c) special isolated/quotient higher-dimensional normal classes beyond already complete smooth finite quotients; (d) genuine nonnormal surface normalization/conductor envelope comparison, proving actual greatest minorant constancy on EVERY actual fibre, including infinite-conductor support strata. Nonnormal fibrewise minimum is not automatically psh or continuous. Do not infer canonical FG from nef rationality, general FG-density, Jacobian saturation, colon(tau_m:tau0), or norm averaging. Exact primary gauges and conductor rules, curve min{f,0} versus literal radial CLD obstruction remain in unchanged original.

No new paper acceptance/original closure is authorized by a solver's verdict; ROOT reviews complete source proofs. Original criterion when possible/appropriate regularity remains unchanged, and products/energy/full finite-map operators are separate targets. Return candidate=true only for ENTIRE original; otherwise candidate=false with complete new deductions and precise unsolved scope.'''
task = dict(problem=orig['problem'] + '\n\n' + request + '\nWHOLE mathematical DATA: ' + str(C / 'mathematical-packet-bindings.json') + '\nFull LOCALONLY primary DATA: ' + str(C / 'private-primary-packet-bindings.json') + '\nWhole book context DATA: ' + str(C / 'book-context-bindings.json'), completionCriteria=load(O / 'task.json')['completionCriteria'])
grants = load(O / 'input.json')['notes']
assert len(grants) == 1 and grants[0]['id'] == 'G331' and len(grants[0]['text'].encode()) == 93375
write(C / 'task.json', task)
write(C / 'input.json', dict(task=task, notes=grants, assignment='Reconstruct whole416 and advance unchanged higher-dimensional normal/conductor geometric envelope residual'))
s = load(O / 'settings.json')
s['codex']['workspace'] = str(C / 'artifacts')
s['usagePrefix'] = 'catalogue-20261003/r290/P12.3-whole416-higher-dimensional-envelope'
assert s['limits'] == dict(concurrency=1, attempts=1, providerCalls=1)
assert all(s[k]['model'] == 'gpt-6.1-sol' and s[k]['reasoning'] == 'xhigh' for k in ['codex', 'research'])
write(C / 'settings.json', s)
write(C / 'mathematical-packet-bindings.json', math)
write(C / 'private-primary-packet-bindings.json', primary)
write(C / 'book-context-bindings.json', context)
f = dict(prepared_utc=datetime.now(timezone.utc).isoformat(), round=290, atom='P12.3', directory=str(C), whole_math_files=len(math), whole_math_bytes=sum(e['bytes'] for e in math), private_primary_files=len(primary), whole_context_files=len(context), only_grants=['G331'], model='gpt-6.1-sol', reasoning='xhigh', maximum_concurrent_campaigns=2, original_task_byte_identical_to_terminal_round=288, completion_criteria_byte_identical_to_terminal_round=288, whole416_compiler_status='UNVERIFIED: actual desktop request pending; retained binding predates invocation', source_documents_and_programs_DATA=True, original_closed=False, new_accepted_paper=False, other_ACTIVE_math_read_or_supplied=False, hot_feedback_sent=False, all_full_primary_source_bodies_pixels_book_context_LOCALONLY=True)
for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'book-context-bindings.json', 'private-primary-packet-bindings.json']:
    f[name.replace('.json', '').replace('-', '_') + '_sha256'] = sha(C / name)
write(C / 'freeze.json', f)
print(json.dumps(f, indent=2))
