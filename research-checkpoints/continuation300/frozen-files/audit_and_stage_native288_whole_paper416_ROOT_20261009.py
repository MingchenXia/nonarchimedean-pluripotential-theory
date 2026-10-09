"""Retain independently read current surface proof, with exact qualified scope."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-288/P12.3-whole413-general-excellent-and-characteristic-envelope-residual'
A = C / 'artifacts/codex-mpzScc'
D = K / 'public-P12.3-continuation416-excellent-normal-surface-envelopes-in-equal-and-mixed-characteristic-unreviewed'
U = R / 'primary-data-LOCALONLY/P12.3-ROOT416-normal-surface-resolution-and-primary-model-source-20261009'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round288-raw-native-actual-FINAL.json'
assert sha(raw) == '23646eac1da9aa94325382eb74799d8bc9418a3364cf6409dca2ab36f717c18e'
x = load(raw)
assert not x['candidate'] and len(x['notes']) == 4
assembly = K / 'round288-whole-literal-assembly-and-serialization-ROOT-check-20261009.json'
ar = load(assembly)
assert ar['whole_source_exact_ROOT_literal_reconstruction'] and ar['whole_companion_exact_ROOT_literal_reconstruction'] and not ar['accepted']
assert sha(A / 'P12.3-surface-envelopes.tex') == ar['source_sha256'] == '26da87504d66731d70a749b415515048c1568761c99eac8ae16b5e1e12d41cb8'
assert sha(A / 'proof-companion.md') == ar['companion_sha256'] == 'af65e6666fd5bf14898f1b7c515a3f264e079571df1a381918f8549288ae002f'
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [289] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 299
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
assert not D.exists() and not U.exists()
D.mkdir()
U.mkdir(parents=True)
public = []
def retain(p, name=None):
    q = D / (name or p.name)
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    public.append(q)
    return q
retain(raw, 'native288-actual-FINAL-all-five-fields.json')
retain(assembly)
retain(K / 'round288-terminal-actual-final-ROOT-retention-20261009.json')
retain(C / 'original-task.json', 'ROOT-unchanged-original-task.json')
for name in ['P12.3-surface-envelopes.tex', 'notes.json', 'source-application-reading-ledger.md', 'scoped-verdict.md', 'original-residual.md', 'original-task.json', 'original-completion-criteria.txt']:
    retain(A / name)
known = {'G331'}
for n in x['notes']:
    assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'} and set(n['support']) <= known
    known.add(n['id'])
    p = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(p, n)
    public.append(p)
    retain(A / (n['id'] + '.tex'))
programs = ['build_delivery.py', 'read_data.py', 'check_delivery.py', 'surface_checks.py']
for name in programs:
    retain(A / name, 'native-program-' + name + '.DATA.txt')
primary = load(C / 'private-primary-packet-bindings.json')
fresh = []
for i in [14, 16, 20, 34, 38, 40]:
    e = primary[i]
    p = Path(e['path'])
    assert sha(p) == e['sha256']
    q = U / p.name
    shutil.copyfile(p, q)
    fresh.append(dict(index=i, path=str(q), bytes=q.stat().st_size, sha256=sha(q), LOCALONLY=True, whole_immediate_unit_freshly_ROOT_physically_read=True))
prior413 = load(K / 'public-P12.3-continuation413-algebraic-field-and-Frobenius-root-envelope-descent-unreviewed/ROOT-whole-serialization-source-application-and-scope-audit.json')
for e in prior413['ROOT_fresh_primary_units'] + prior413['ROOT_actual_formula_pixels']:
    assert sha(e['path']) == e['sha256']
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now, paper=416, atom='P12.3', UNREVIEWED=True, accepted=False, original_closed=False, candidate=False, counts=dict(solved=16, open=26, accepted_scoped_papers=97), actual_FINAL=dict(path=str(raw), sha256=sha(raw), all_five_fields_of_every_note_physically_ROOT_read=True, notes=4, support_valid=True), all_four_distinct_expanded_proofs_separately_physically_ROOT_read=True, whole_current_unique_preamble_abstract_ledger_verdict_residual_physically_ROOT_read=True, whole_source_and_companion_literal_reconstruction=ar, prior_current413_all_actual_and_distinct_expanded_proofs_retained_whole_and_physically_ROOT_read_in_prior413_audit=True, whole_prior_retention_NOT_extra_fresh_reading=True, sole_qualified_incoming_grant='ENTIRE G331, with EVERY annotation/source/model/read-limit qualification; no envelope theorem granted', all_four_native_programs_physically_ROOT_read_as_DATA=programs, native_or_supplied_programs_executed_or_imported=False, fresh_primary_units=fresh, prior413_immediate_SH_BFJ_units_and_actual_formula_pixels=prior413['ROOT_fresh_primary_units'] + prior413['ROOT_actual_formula_pixels'], prior413_reading_qualifications_retained_NOT_new_recursive_audit=True, exact_new_source_applications=['Whole Stacks0BGJ54.14.3-5 Lipman: normal projective integral DIMENSION-TWO primary blowup normalization has finite singular locus and normal singular local completions by excellence; local normalized blowups resolve over the marked point. No higher-dimensional resolution premise.', 'Whole01VG29.38.7-8: finite normalization preserves ample negative tautological bundles; composition with sufficiently high pullback powers produces actual effective exceptional E with O(-E) ample and full exceptional support.', 'Whole01PR28.27.11/13: finite affine nonvanishing section charts and exact section localization; explicit finite projective immersion and proper closed-immersion/Rees argument prove Y is an ACTUAL proper-primary blowup.', 'Whole0AY8/37.53.6: proper integral birational Y over normal R has H0(Y,O)=R; all generic/fibre hypotheses checked.', 'Whole0B5Y/33.44.15 and0D2N/30.21.4: positive degree on EVERY one-dimensional component, including the nonreduced full closed fibre, gives ample restriction and relative ampleness over the local base in the concrete two-blowup example.', 'Regular Noetherian local factoriality, normal height-one intersection, projective Rees blowups, proper valuative centres, proper immersions and curve degree/effective zero divisors remain explicitly named conventional foundations at exact hypotheses.', 'Deeper complete-normal-surface resolution, reduction to rational singularities, completion transfer and gluing dependencies of the full immediate Lipman proof remain disclosed published foundations; not a fresh full recursive proof audit.', 'Standalone0BGP is repeated immediate theorem inside full0BGJ, not an independent reading;0AX7 vanishing and0B5S are NOT theorem premises or freshly applied units.'], complete_new_scoped_proof=['Every excellent normal local DOMAIN of dimension TWO, arbitrary residue field and equal or mixed characteristic: actual regular primary refinement dominating any finite primary ideal list INCLUDING the gauge ideal.', 'Finite real exceptional divisor degree matrix has nonnegative off-diagonal entries; feasible z<=min(d,0),Qz>=0 has a greatest vector by compact coordinate maximization and max closure.', 'Greatest divisor is actual negative effective REAL Cartier on an ACTUAL primary model, and has nonnegative degree on EVERY contracted integral curve before envelope identification.', 'Every primary ideal competitor: its divisorial part has a nonzero generated section at each exceptional generic point, hence anti-nef; valued QUOTIENT-field centres control EVERY support and give q<=f_A<=f_Zstar.', 'Signed primary/model obstacles have the exact greatest independently geometric envelope f_Zstar; uniform signed-model density and raw Lipschitz give EVERY finite continuous signed obstacle and uniform convergence in EVERY canonical degree.', 'Concrete equal/mixed-characteristic two-blowup example Q=[[-2,1],[1,-1]],D=-E1-3E2,zstar=(-3/2,-3),actual envelope=-3v((x^2,y))/2; includes Z_p[[u]].'], no_O1m_or_canonical_FG_or_semialmpleness_claim=True, native_finite_225_obstacle_925_vertex_pair_checks_NOT_certification=True, residual=['Original general excellent normal higher-dimensional envelope regularity remains OPEN; surface proof does NOT generalize without new actual all-curve competitor control and resolution/regularity inputs.', 'Unrestricted nonnormal/conductor descent still requires greatest minorant constancy on EVERY actual fibre, including infinite-conductor quotient fibres.', 'Full inherited historical/primary/book audit remains explicitly incomplete; no new original or scoped acceptance.', 'Products, energy and full finite-map operators remain separate original targets.'], compiler='NOT_YET_INVOKED_FOR416', active_native289_mathematics_NOT_inspected_or_hot_fed=True, primary_literal_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp, scope)
public.append(sp)
companion = D / 'proof-companion.md'
companion.write_text('# ENTIRE ROOT416 proof packet; UNREVIEWED, original P12.3 OPEN.\n\n## EXACT captured actual settled FINAL, all five fields\n\n' + raw.read_text() + '\n\n## ENTIRE native288 companion, exact literal reconstruction checked; one artifact trailing LF per note is retained as serialization DATA\n\n' + (A / 'proof-companion.md').read_text() + '\n\n## ENTIRE ROOT416 precise source/application/scope and residual\n\n' + sp.read_text())
public.append(companion)
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B, dict(recorded_utc=now, paper=416, whole_source=dict(path=str(D / 'P12.3-surface-envelopes.tex'), bytes=(D / 'P12.3-surface-envelopes.tex').stat().st_size, sha256=sha(D / 'P12.3-surface-envelopes.tex')), whole_companion=dict(path=str(companion), bytes=companion.stat().st_size, sha256=sha(companion)), public_files=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)) for p in public], UNREVIEWED=True, accepted=False, original_closed=False, compiler='NOT_YET_INVOKED_FOR416', counts=scope['counts'], protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now, ROOT416_whole_unreviewed=dict(binding=str(B), sha256=sha(B)), next_work='Whole ROOT416 excellent normal arbitrary-characteristic surface CE draft reconstructed after all four actual five-field notes/all four expanded proofs/full current unique scope and SIX new complete immediate primary units ROOT read. Compile and record actual outcome, preserve all source qualifications. Then freeze next P12.3 higher-dimensional original residual with whole416+413. Native289 advances P16.7; at mostTWO, no active math/hot feedback; counts/editor unchanged.')
    write(p, y)
print(json.dumps(dict(paper=416, source_bytes=(D / 'P12.3-surface-envelopes.tex').stat().st_size, source_sha256=sha(D / 'P12.3-surface-envelopes.tex'), companion_bytes=companion.stat().st_size, public_files=len(public)+1, fresh_primary_units=6, original_closed=False, accepted=False, binding=str(B)), indent=2))
