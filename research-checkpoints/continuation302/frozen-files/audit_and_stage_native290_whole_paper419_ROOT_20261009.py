"""ROOT literal assembly check and retention; native programs remain inert DATA."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-290/P12.3-whole416-higher-dimensional-and-conductor-envelope-residual'
A = C / 'artifacts/codex-00KKBZ'
D = K / 'public-P12.3-continuation419-conductor-descent-cusp-envelopes-and-threefold-obstruction-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round290-raw-native-actual-FINAL.json'
assert sha(raw) == '85592e3863ee63c7e91ebe4940f2c9c57a545973d4af1efec81ee4876dae41bd'
x = load(raw)
assert not x['candidate'] and len(x['notes']) == 5
assert load(A / 'notes.json') == x
assert sha(A / 'P12.3-conductor-and-threefold.tex') == '47430ddc0d2d5bdecbc313a64a052bbda70c1d13e1c2aa3963befc54581d493a'
assert sha(A / 'proof-companion.md') == '9a564c0e7f321621ae8cce17bf6ea8ddf7c17ef8778d9e82704e3522d1dc7f66'
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [291] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 301
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
assert not D.exists()

def esc(s):
    mp = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '#': r'\#', '$': r'\$', '%': r'\%', '&': r'\&', '_': r'\_', '^': r'\textasciicircum{}', '~': r'\textasciitilde{}', '<': r'\textless{}', '>': r'\textgreater{}'}
    return ''.join(mp.get(c, c) for c in s)

source = (A / 'P12.3-conductor-and-threefold.tex').read_text()
preamble, rest = source.split('\\section{n1.', 1)
assert preamble.endswith('\\tableofcontents\n') and len(preamble.splitlines()) == 33
known = {'G331'}
sections = []
for n in x['notes']:
    assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'} and set(n['support']) <= known
    known.add(n['id'])
    assert (A / (n['id'] + '.md')).read_text() == n['text'] + '\n'
    t = (A / (n['id'] + '.tex')).read_text().removesuffix('\n')
    prefix = '\\section{' + esc(n['id'] + '. ' + n['summary']) + '}\n\\textit{Supports: ' + esc(', '.join(n['support'])) + '.}\n\n' + '\n\n'.join(esc(p) for p in n['text'].split('\n\n')) + '\n\n'
    assert t.startswith(prefix) and t[len(prefix):].startswith('\\subsection*{Expanded ')
    sections.append(t)
grant = load(A / 'qualified-G331.json')
assert grant['id'] == 'G331' and (A / 'qualified-G331.txt').read_text() == grant['text']
old = (A / 'retained/whole416-source.tex.DATA').read_text()
oldcomp = (A / 'retained/whole416-companion.md.DATA').read_text()
assert old == (K / 'public-P12.3-continuation416-excellent-normal-surface-envelopes-in-equal-and-mixed-characteristic-unreviewed/P12.3-surface-envelopes.tex').read_text()
assert oldcomp == (K / 'public-P12.3-continuation416-excellent-normal-surface-envelopes-in-equal-and-mixed-characteristic-unreviewed/proof-companion.md').read_text()
ledger = (A / 'source-application-reading-ledger.md').read_text()
verdict = (A / 'scoped-verdict.md').read_text()
residual = (A / 'original-residual.md').read_text()
# Residual equality is established against its frozen actual carrier, not TeX rendering.
assert (A / 'original-residual.md').read_bytes() == (C / 'immutable-mathematical-DATA/019-original-residual.md').read_bytes()
tail = '\n\\section*{Current source, reading and execution qualifications}\n' + esc(ledger) + '\n\\section*{Separate scoped verdict}\n' + esc(verdict) + '\n\\section*{Byte-unchanged original residual retained as DATA}\n' + esc(residual)
tail += '\n\\appendix\n\\section{Entire qualified incoming G331, including all annotations}\n\\begin{EntireQualifiedG331}\n' + grant['text'] + '\n\\end{EntireQualifiedG331}\n'
tail += '\n\\section{Entire current416 standalone source, retained literally as DATA}\n\\begin{Retained416Source}\n' + old + '\n\\end{Retained416Source}\n\\end{document}\n'
assert source == preamble + '\n\n'.join(sections) + tail
comp = ['# ENTIRE scoped proof companion; unverified, candidate=false\n']
for n in x['notes']:
    comp.extend(['## Actual local FINAL fields ' + n['id'] + '\n', json.dumps(n, ensure_ascii=False, indent=2) + '\n', '## Distinct expanded exposition ' + n['id'] + '\n', (A / (n['id'] + '.tex')).read_text()])
inp = load(A / 'input.json')
for title, body in [('ENTIRE qualified G331', grant['text']), ('ENTIRE incoming task and family dossier', json.dumps(inp['task'], ensure_ascii=False, indent=2)), ('ENTIRE current416 source', old), ('ENTIRE current416 companion', oldcomp), ('ENTIRE current416 qualifications', (A / 'retained/whole416-qualifications.json').read_text()), ('ENTIRE current416 binding', (A / 'retained/whole416-binding.json').read_text()), ('New source-reading-execution ledger', ledger), ('Separate scoped verdict', verdict), ('Unchanged original residual', residual)]:
    comp.extend(['\n## ' + title + '\n\n', body, '\n'])
assert (A / 'proof-companion.md').read_text() == ''.join(comp)
prior = load(K / 'public-P12.3-continuation416-excellent-normal-surface-envelopes-in-equal-and-mixed-characteristic-unreviewed/ROOT-whole-proof-source-application-scope-and-residual.json')
for e in prior['fresh_primary_units'] + prior['prior413_immediate_SH_BFJ_units_and_actual_formula_pixels']:
    assert sha(e['path']) == e['sha256']
assert load(C / 'original-task.json')['problem'] in load(A / 'original-task.json')['problem']
D.mkdir()
public = []
def retain(p, name=None):
    q = D / (name or p.name)
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    public.append(q)
    return q
retain(raw, 'native290-actual-FINAL-all-five-fields.json')
retain(K / 'round290-terminal-actual-final-ROOT-retention-20261009.json')
retain(C / 'original-task.json', 'ROOT-unchanged-original-task.json')
for name in ['P12.3-conductor-and-threefold.tex', 'notes.json', 'source-application-reading-ledger.md', 'scoped-verdict.md', 'original-residual.md', 'original-task.json', 'original-completion-criteria.txt', 'qualified-G331.json', 'qualified-G331.txt', 'diagnostics-input.json']:
    retain(A / name)
for n in x['notes']:
    p = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(p, n)
    public.append(p)
    retain(A / (n['id'] + '.tex'))
programs = ['assemble.py', 'finite_diagnostics.py', 'verify.py']
for name in programs:
    retain(A / name, 'native-program-' + name + '.DATA.txt')
for name in ['finite-diagnostics.json', 'environment.json', 'observed-execution.json', 'verification.json', 'retention.json', 'input-hashes.json', 'own-hashes.json']:
    retain(A / 'reports' / name, 'native-reported-' + name)
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now, paper=419, atom='P12.3', UNREVIEWED=True, accepted=False, original_closed=False, candidate=False, counts=dict(solved=16, open=26, accepted_scoped_papers=97), actual_FINAL=dict(path=str(raw), sha256=sha(raw), all_five_fields_of_all_five_notes_physically_ROOT_read=True), all_five_distinct_expanded_proofs_separately_physically_ROOT_read=True, complete_current_unique_preamble_abstract_ledger_verdict_original_residual_physically_ROOT_read=True, initial_source_1_150_display_truncated_NO_extra_credit=True, whole_source_exact_ROOT_literal_reconstruction=True, whole_native_companion_exact_ROOT_literal_reconstruction=True, all_three_native_programs_physically_ROOT_read_only_as_DATA=programs, native_or_supplied_programs_executed_or_imported=False, sole_incoming_correctness_grant='ENTIRE qualified G331, every geometric/model/support/descent/source/audit limitation retained', inherited_surface_and_SH_BFJ_immediate_primary_units_bound_whole=prior['fresh_primary_units'] + prior['prior413_immediate_SH_BFJ_units_and_actual_formula_pixels'], new_fresh_primary_reading_credit=0, every_current_application_ROOT_rejudged=True, immediate_new_source_applications=['Stacks01VG composition ampleness at explicit regular THREEFOLD two-point blowup; Stacks0AY8 proper integral birational H0 over normal regular base; Stacks01PR finite affine-section localization and closed-immersion/Rees argument. Complete units already ROOT read416, reused at checked current hypotheses, not new reading.', 'Normal excellent surface proof uses complete immediate Lipman54.14.3-5 at dimension TWO and disclosed deeper surface-resolution/completion/gluing foundations; not higher-dimensional resolution.', 'Published BFJ smooth affine CLOSED/algebraically closed/characteristic-zero source theorem only; no positive/mixed-characteristic higher-dimensional CE conclusion.', 'Radicial residue-field valuation uniqueness, exact numerical-semigroup conductor, explicit cusp all-support ideal bounds and point-blowup intersection computation proved directly, no new published premise.'], complete_new_scoped_deductions=['Full boundary-bijective normalization gives order/isometric C/D envelope equivalence; primary conductor or finite radicial reduced conductor quotients are explicit sufficient conditions. All infinite-conductor supports retained.', 'Every-dimensional numerical-semigroup cusp CE over algebraically closed characteristic zero; dimension TWO over every field; mixed-characteristic Z_p[[t^2,t^3]] CE with nonempty infinite-conductor boundary.', 'Explicit K_m gives EVERY-degree canonical uniform envelope error at most2/m on every support, in every dimension and characteristic; characteristic-zero two-point raw finite REAL ideal-cone separation proves canonical non-FG.', 'Explicit ACTUAL primary regular threefold model: I=(z)+m^2 divisorial part E1+2E2+2E3 has degree -1 on joining line, disproving generic-section-to-all-curve-nef inference; NOT a CE counterexample.'], native_184_cases_5888_values_64_cancellations_NOT_ROOT_execution_or_certification=True, residual=['General normal excellent dimension>=3 appropriate continuous-envelope regularity or qualifying failure OPEN.', 'Unrestricted nonsingleton conductor fibre envelope constancy OPEN.', 'Complete inherited historical/whole-book/source audit still qualified and incomplete; no original closure or new acceptance.', 'Products, energy and full finite-map operators remain separate.'], compiler='NOT_YET_INVOKED_FOR419', active_native291_mathematics_NOT_read_or_supplied=True, primary_literal_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp, scope)
public.append(sp)
companion = D / 'proof-companion.md'
companion.write_text('# ENTIRE ROOT419 proof packet; UNREVIEWED, original P12.3 OPEN.\n\n## Exact actual settled FINAL, ALL five fields\n\n' + raw.read_text() + '\n\n## ENTIRE native290 companion; independent literal reconstruction checked\n\n' + (A / 'proof-companion.md').read_text() + '\n\n## ENTIRE ROOT419 precise application/scope/residual\n\n' + sp.read_text())
public.append(companion)
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B, dict(recorded_utc=now, paper=419, whole_source=dict(path=str(D / 'P12.3-conductor-and-threefold.tex'), bytes=(D / 'P12.3-conductor-and-threefold.tex').stat().st_size, sha256=sha(D / 'P12.3-conductor-and-threefold.tex')), whole_companion=dict(path=str(companion), bytes=companion.stat().st_size, sha256=sha(companion)), public_files=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)) for p in public], UNREVIEWED=True, accepted=False, original_closed=False, compiler='NOT_YET_INVOKED_FOR419', counts=scope['counts'], protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now, ROOT419_whole_unreviewed=dict(binding=str(B), sha256=sha(B)), next_work='Whole ROOT419 conductor/cusp/threefold draft retained after ALL five actual five-field notes/ALL five distinct expanded proofs/complete current scope ROOT read and literal reconstruction. Request compiler; freeze next P12.3 original residual with whole419+416. Native291 advances P16.7; at most TWO, no active math or hot feedback. Counts and protected editor unchanged.')
    write(p, y)
print(json.dumps(dict(paper=419, source_bytes=(D / 'P12.3-conductor-and-threefold.tex').stat().st_size, companion_bytes=companion.stat().st_size, public_files=len(public) + 1, literal_reconstruction=True, original_closed=False, accepted=False, binding=str(B)), indent=2))
