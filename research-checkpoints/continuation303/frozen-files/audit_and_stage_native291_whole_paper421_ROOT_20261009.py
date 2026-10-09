"""ROOT passive whole-proof reconstruction and precise scope retention. No input code runs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-291/P16.7-whole417418-actual-representation-and-prescribed-measure-J-defect'
A = C / 'artifacts/codex-hb0eMU'
D = K / 'public-P16.7-continuation421-concentration-defects-and-invariant-attainment-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round291-raw-native-actual-FINAL.json'
assert sha(raw) == '27d7b2d51bdb57c9e627a59e6ed6194a2569e3521344558eb606297acc28784e'
x = load(raw)
assert x == load(A / 'final-notes.json') and x['candidate'] is False and len(x['notes']) == 4
assert not D.exists()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [292] and y['github_pending_checkpoint'] is None
    assert y['latest_verified_github_checkpoint']['continuation'] == 302
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
known = set()
for n in x['notes']:
    assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'} and set(n['support']) <= known
    known.add(n['id'])
    assert load(A / ('actual-' + n['id'] + '-all-five-fields.json')) == n
    assert (A / (n['id'] + '.txt')).read_text() == n['text'] + '\n'
bindings = load(C / 'mathematical-packet-bindings.json')
assert len(bindings) == 172
for e in bindings:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
data = lambda i: Path(bindings[i]['path']).read_bytes()
assert (A / 'original-residual.txt').read_bytes() == data(23)
assert (A / 'unchanged-original-task.json').read_bytes() == data(0)
source = data(29).decode()
i = source.index('\\title{')
j = source.index('\\author{', i)
source = source[:i] + '\\title{Concentration defects of actual variational maximizers\\\\and an invariant-variation equation slice}\n' + source[j:]
i = source.index('\\begin{abstract}')
j = source.index('\\end{abstract}', i) + len('\\end{abstract}')
source = source[:i] + r'''\begin{abstract}
We retain and rejudge the entire qualified 418 bounded and generated
reconstruction and the distinct 417 variational proofs. New deductions
identify the prescribed-measure loss as a positive Radon concentration
defect supported on the intersection of closures of exceptional open
sets. An exact split separates bounded oscillation on the exceptional
set from deep negative tails. Bounded attainment removes the loss for
every fast maximizing sequence. Actual two-sided invariant variations
identify the equation at a smooth strictly convex invariant attained
weight, and show that zero full dual characterizes the reference
measure among all eligible arbitrary-support measures. None of these
results proves general analytic representation or prescribed-measure
existence. The original P16.7 and the deeper source audit remain open.
\end{abstract}''' + source[j:]
source = source.replace('\\newcommand{\\Q}{\\mathcal Q}', '\\newcommand{\\Q}{\\mathcal Q}\n\\newcommand{\\M}{\\mathfrak M}\n\\newcommand{\\V}{\\mathcal V}')
retained = data(31).decode()
retained = retained[retained.index('\\section{Actual domain'):retained.index('\\end{document}')]
retained = re.sub(r'\\(label|ref|eqref)\{([^}]+)\}', lambda m: '\\' + m[1] + '{ret417:' + m[2] + '}', retained)
retained = retained.replace('\\section{', '\\section{Retained 417 reconstruction: ')
retained = '\n\\begingroup\n\\renewcommand{\\B}{\\mathcal B}\n' + retained + '\n\\endgroup\n'
marker = '\\section{Separate scoped verdict and unchanged original problem}'
assert source.count(marker) == 1
source = source.replace(marker, retained + '\n' + (A / 'new-residual-proofs.tex').read_text() + '\n' + marker)
source = source.replace('\\ {\nm affinoid', '\\ {\\rm affinoid')
assert source == (A / 'standalone.tex').read_text()
assert len(source.encode()) == 85806 and len(source.splitlines()) == 1797
components = ['standalone.tex', 'new-residual-proofs.tex', 'final-notes.json', 'source-application-reading-ledger.txt', 'source-application-reading-ledger.json', 'scoped-verdict.json', 'original-residual.txt', 'unchanged-original-task.json', 'binding-audit-output.json', 'finite-check-output.json', 'environment.json', 'commands.txt', 'reading-commands.txt', 'prepare_artifacts.py', 'verify_artifacts.py', 'finish_artifacts.py']
parts = [b'ENTIRE LOCALONLY UNVERIFIED PROOF COMPANION. ORIGINAL P16.7 OPEN.\nRetention of a complete body is not independent audit or correctness credit.\n']
for name in components:
    parts += [f'\n===== WHOLE OWN COMPONENT {name} =====\n'.encode(), (A / name).read_bytes()]
seen = set()
for i, e in enumerate(bindings):
    b = data(i)
    if e['sha256'] not in seen:
        seen.add(e['sha256'])
        parts += [f'\n===== WHOLE SUPPLIED DATA {i}: {Path(e["path"]).name} =====\n'.encode(), b]
assert b'\n'.join(parts) == (A / 'proof-companion.txt').read_bytes()
primary = [e for e in load(C / 'private-primary-packet-bindings.json') if 'P16.7-ROOT415-bounded-calculus-local-Gauss-and-Shilov-source' in e['path']]
assert len(primary) == 15
for e in primary:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
D.mkdir()
public = []
def retain(p, name=None):
    q = D / (name or p.name)
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    public.append(q)
retain(raw, 'native291-actual-FINAL-all-five-fields.json')
retain(K / 'round291-terminal-actual-final-ROOT-retention-20261009.json')
retain(C / 'original-task.json', 'ROOT-unchanged-original-task.json')
for name in components:
    retain(A / name, 'native-program-' + name + '.DATA.txt' if name.endswith('.py') else name)
for n in x['notes']:
    retain(A / ('actual-' + n['id'] + '-all-five-fields.json'))
for name in ['delivery-check-output.json', 'artifact-bindings.json', 'companion-component-manifest.json']:
    retain(A / name)
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now, paper=421, atom='P16.7', UNREVIEWED=True, accepted=False, original_closed=False, candidate=False, counts=dict(solved=16, open=26, accepted_scoped_papers=97), actual_FINAL=dict(path=str(raw), sha256=sha(raw), all_five_fields_of_all_four_notes_physically_ROOT_read=True), complete_current_1797_LF_standalone_physically_ROOT_read=True, complete_distinct_367_LF_new_expansion_separately_physically_ROOT_read=True, complete_TXT_and_718_LF_JSON_ledgers_and_verdict_and_unchanged_residual_physically_ROOT_read=True, complete_three_native_programs_physically_ROOT_read_ONLY_as_DATA=True, supplied_or_native_programs_executed_or_imported=False, whole_source_exact_ROOT_literal_reconstruction=True, whole_native_companion_exact_ROOT_literal_reconstruction=True, sole_incoming_correctness_grants=[], inherited_fifteen_complete_immediate_CLD_GR_primary_units=primary, current_ROOT_fresh_primary_reading_credit=0, current_applications_ROOT_rejudged=True, primary_scope='Same fifteen complete immediate units physically ROOT read415, reapplied at the same compact good strict smooth separated boundaryless mass-two torus and minimal CLD domain. First variation/calibration/local coordinate dimension and actual two-sided periodic positive-Hessian variations rejudged. Not a new independent deeper recursive source audit; GR6.5 still requires already-USC FULL pointwise convergence.', complete_new_conditional_deductions=['Prescribed-measure defect measures have mass J and support in intersection of closures of exceptional open sets, not necessarily their intersection. Total variation and weak convergence to u times mu equivalent to J=0.', 'Exact truncation split J=A+ +Q-=A- +Q+; J=0 iff uniform integrability AND bounded truncation L1 convergence. If mu(N)=0, J is the iterated ordinary-limit tail defect. Positive cluster decomposition and J-K Borel identity.', 'Actual bounded full-dual attainment implies J=0 for every fast sequence and canonical R=q, nu=MA(q), mu-a.e. agreement; no arbitrary-support equation from bare attainment.', 'Smooth invariant attained q with everywhere positive definite coordinate Hessian implies actual equation mu=MA(q) via two-sided periodic first variation, Gauss dominance, segment derivative and dense tests.', 'Full D(mu)=0 iff mu=theta^2 over ENTIRE eligible arbitrary-support class.'], diagnostic_scalar_bump_NOT_actual_psh_or_maximizer_counterexample=True, residual=['General attainment, general J=0, actual C/G representation of nonordered Borel limits and every-measure prescribed equation existence/uniqueness OPEN.', 'Genuine nonalgebraization/coherent descent and deeper recursive primary/source audit remain qualified and incomplete.'], compiler='NOT_YET_INVOKED_FOR421', active_native292_math_NOT_read_or_supplied=True, hot_feedback=False, primary_literal_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp, scope)
public.append(sp)
companion = D / 'proof-companion.txt'
companion.write_text('ENTIRE ROOT421 proof packet; UNREVIEWED, original P16.7 OPEN.\n\nENTIRE settled native291 actual FINAL:\n' + raw.read_text() + '\n\nENTIRE native companion, ROOT literal identity checked:\n' + (A / 'proof-companion.txt').read_text() + '\n\nENTIRE ROOT precise current application/scope/residual:\n' + sp.read_text())
public.append(companion)
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B, dict(recorded_utc=now, paper=421, whole_source=dict(path=str(D / 'standalone.tex'), bytes=len(source.encode()), sha256=sha(D / 'standalone.tex')), whole_companion=dict(path=str(companion), bytes=companion.stat().st_size, sha256=sha(companion)), public_files=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)) for p in public], UNREVIEWED=True, accepted=False, original_closed=False, compiler='NOT_YET_INVOKED_FOR421', counts=scope['counts'], protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now, ROOT421_whole_unreviewed=dict(binding=str(B), sha256=sha(B)), next_work='Whole ROOT421 read and literally reconstructed; request native compiler and freeze next small P16.7 batch on actual existence/attainment. Native292 remains isolated, no active math or hot feedback. Publish regular NONFORCE303 whole420421 and qualified frozen293; counts/editor unchanged.')
    write(p, y)
print(json.dumps(dict(paper=421, source_bytes=len(source.encode()), companion_bytes=companion.stat().st_size, public_files=len(public)+1, literal_reconstruction=True, original_closed=False, accepted=False, binding=str(B)), indent=2))
