from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
K = R / 'root-checks'
P = K / 'P16.7-continuation417-affine-dual-rays-and-quantitative-Jensen-separation-working-paper-20261009.tex'
S = K / 'P16.7-continuation417-ROOT-source-application-scope-and-residual-20261009.json'
F = K / 'P16.7-continuation417-entire-proof-companion-20261009.txt'
B = K / 'P16.7-continuation417-ROOT-whole-paper-source-scope-and-binding-20261009.json'
Q = K / 'P16.7-continuation417-ROOT-compiler-observation-20261009.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert all(not p.exists() for p in [S, F, B, Q])
assert P.read_text().startswith('\\documentclass') and P.read_text().endswith('\\end{document}\n')
assert 'J_t\\ge\\frac{t(1-t)}{48L}' in P.read_text()
sources = [dict(path=str(K / 'P16.7-continuation414-universal-variational-measure-limits-and-calibrated-dual-retraction-working-paper-20261009.tex'), sha256='91712ca482abeb89a19f79e93464c579f1b6c8feed318b9fc88250bf71ef0d17', current_application_lines=[[1,269],[270,467]], application='Whole source: universal coercivity, exact midpoint, actual Green, all canonical family limits, same-net dual calibration, idempotence and generated fixed points'), dict(path=str(K / 'public-P16.7-continuation415-universal-variational-limits-local-Gauss-fibres-and-USC-relaxation-unreviewed/scoped-paper.tex'), sha256='40ec4eedc7cafdb063621f49f3bf06f02bfdc2c28e0f182b', current_application_lines=[[388,579],[570,774]], application='Whole current universal/moving-moment, exact dual calibration, defect and all-Shilov USC-relaxation statements AND complete immediate proofs; earlier bounded foundations retain existing full-source audit qualifications')]
# Exact retained formal source identity; this is not fresh reading credit.
sources[1]['sha256'] = '40ec4eedc7cafdb063621f49f3bf063c33a1bcf7f3df06f02bfdc2c28e0f182b'
for e in sources:
    assert sha(e['path']) == e['sha256']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert x['current_active_batch'] == [290] and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation'] == 300
    assert len(x['fully_solved_original_atoms']) == 16 and x['remaining_open_original_atoms'] == 26 and x['historical_reviewed_scoped_papers'] == 97
now = datetime.now(timezone.utc).isoformat()
write(Q, dict(recorded_utc=now, paper=417, current_source=str(P), current_source_sha256=sha(P), tool='codex_app.compile_latex_document', attempt1='Actual request pending; was invoked before the subsequent added Green derivation and generated-fixed-point corollary', current_revision_compilation='UNVERIFIED', actual_success_observed=False, no_local_TeX_or_plugin_install=True, protected_editor_OPEN_UNCHANGED=True, mathematical_certification=False))
scope = dict(recorded_utc=now, paper=417, atom='P16.7', UNREVIEWED=True, accepted=False, original_closed=False, whole_formal_source_ROOT_authored_and_physically_read_in_full=True, qualified_current_applications=sources, primary_recursive_chain_NOT_newly_independently_audited=True, original_primary_and_geometric_reading_limits_retained=True, complete_new_scoped_proofs=['Every finite-full-dual mass2 measure mu: B((1-t)mu+tVmu)=(1-t)Bmu+tB(Vmu), V constant along ENTIRE closed segment; all canonical moments/full-point tuple/ordinaryUSCrelaxation common; defect=(1-t)K', 'Arbitrarily varying parameter approximate maximizers: I(c_i,a_j)<=8epsilon_i+4eta_j, actual weak error on each C test <=sqrt(96L epsilon_i); ALL continuous tests and scalar/full-point limits follow uniformly', 'One interior dual-affinity equality iff a common normalized maximizing sequence for endpoints; implies whole-segment affinity and equal canonical invariants, NOT converse from equal V images', 'EVERY two eligible measures: actual-test Jensen gap J_t>=t(1-t)|int h(Vmu0-Vmu1)|^2/(48L), by exact weighted deficits and actual Green; distinct V images force strict convexity', 'Strict dual convexity on distinct already-generated MA endpoints; global strict convexity would force V identity, but is not proved for entire eligible class'], no_new_native_or_model_call_or_subagent_for_this_ROOT_deduction=True, active_native_campaigns_at_retention=[290], active_mathematics_inspected_or_hot_feedback_sent=False, native289_terminal_mathematics_is_separate_not_used_here=True, supplied_or_native_programs_executed_or_imported=False, residual=['Actual positive analytic representation/recognition of the canonical full-point tuple and ordinary USC relaxation', 'V(mu)=mu for EVERY eligible arbitrary-support measure, sufficient exact analytic variation/envelope replacement and original existence/uniqueness', 'Whole V fibre convexity and converse equal-images=>dual-affinity NOT proved', 'Global strict dual convexity is only a sufficient conditional criterion, NOT proved', 'Full deeper historical/geometric/nonalgebraization/primary/generated/descent audit remains qualified unfinished'], counts=dict(solved=16, open=26, accepted_scoped_papers=97), current_revision_compilation='UNVERIFIED; actual prior-revision request pending', primary_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True)
write(S, scope)
F.write_text('ENTIRE ROOT417 formal proof; qualified inherited foundations and exact original residual follow.\n\n' + P.read_text() + '\nENTIRE directly applied ROOT414 proof DATA, not new correctness grant:\n\n' + Path(sources[0]['path']).read_text() + '\nENTIRE directly applied ROOT415 source DATA, not new correctness grant:\n\n' + Path(sources[1]['path']).read_text() + '\nENTIRE ROOT417 precise application/scope/residual:\n\n' + S.read_text())
write(B, dict(recorded_utc=now, paper=417, whole_paper=dict(path=str(P), bytes=P.stat().st_size, sha256=sha(P)), public_files=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)) for p in [P, S, F, Q]], UNREVIEWED=True, accepted=False, original_closed=False, compiler='UNVERIFIED; actual prior-revision request pending', counts=scope['counts'], primary_bodies_not_published=True, protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    x = load(p)
    x.update(updated_utc=now, ROOT417_whole_unreviewed=dict(source=str(P), binding=str(B), sha256=sha(B)), next_work='Whole ROOT417 affine dual rays and quantitative Jensen separation retained UNREVIEWED; current source compilation unverified. Read ALL terminal289 actual five-field notes/whole unique standalone and expanded residual proofs/unique ledgers/immediate source applications before ROOT418 and next P16.7 follow-up. Native290 active P12.3 higher-dimensional/conductor, no active mathematics or hot feedback. Publish regular NONFORCE301 only complete read proofs; counts/editor unchanged.')
    write(p, x)
print(json.dumps(dict(paper=417, source_bytes=P.stat().st_size, source_sha256=sha(P), source_lines=len(P.read_bytes().splitlines()), companion_bytes=F.stat().st_size, original_closed=False, accepted=False, compiler='current revision UNVERIFIED', binding=str(B)), indent=2))
