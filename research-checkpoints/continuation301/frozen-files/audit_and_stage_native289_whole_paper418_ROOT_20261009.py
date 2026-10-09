"""Independently assemble passive literal proof DATA and retain exact scope."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-289/P16.7-whole414415-tail-maxima-and-actual-analytic-representation'
A = C / 'artifacts/codex-YK6QPt'
D = K / 'public-P16.7-continuation418-quasi-uniform-maximizers-and-exact-prescribed-measure-defects-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round289-raw-native-actual-FINAL.json'
assert sha(raw) == '0810b552311fc0703e5b55d9d558e0cd45282515ae9f3adbaaa8a83c50305f41'
x = load(raw)
assert not x['candidate'] and len(x['notes']) == 4
assert x == load(A / 'final-notes.json')
known = set()
for n in x['notes']:
    assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'} and set(n['support']) <= known
    known.add(n['id'])
    assert (A / (n['id'] + '.txt')).read_text() == n['text'] + '\n'
math = load(C / 'mathematical-packet-bindings.json')
assert len(math) == 134
for e in math:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
source = (A / 'standalone.tex').read_text()
expanded = (A / 'new-residual-proofs.tex').read_text()
assert len(source.splitlines()) == 1166 and len(expanded.splitlines()) == 389
assert source.count(expanded) == 1
old = Path(math[20]['path']).read_text()
rebuilt = old.replace('\\title{Universal variational limits and their analytic representation gap}', '\\title{Quasi-uniform maximizing sequences, finite tail maxima,\\\\and exact remaining analytic defects}')
rebuilt = rebuilt.replace('\\author{Independent scoped proof draft; not an original P16.7 solution}', '\\author{Independent conditional reconstruction and new residual deductions}')
start = rebuilt.index('\\begin{abstract}')
stop = rebuilt.index('\\end{abstract}', start) + len('\\end{abstract}')
new_start = source.index('\\begin{abstract}')
new_stop = source.index('\\end{abstract}', new_start) + len('\\end{abstract}')
rebuilt = rebuilt[:start] + source[new_start:new_stop] + rebuilt[stop:]
rebuilt = rebuilt.replace('\\nm affinoid', '\\rm affinoid')
marker = '\\section{Separate scoped verdict and unchanged original problem}'
assert rebuilt.count(marker) == 1
rebuilt = rebuilt.replace(marker, expanded + '\n' + marker)
rebuilt = rebuilt.replace('The new conditional results are universal variational energy and moment', 'The reconstructed conditional results are universal variational energy and moment')
rebuilt = rebuilt.replace('All prescribed measures retain arbitrary support, positive raw mass two,', 'The additional deductions are those in the preceding new scoped status.\nAll prescribed measures retain arbitrary support, positive raw mass two,')
assert rebuilt == source, 'Retain failure evidence; no supplied assembly execution'
parts = [b'ENTIRE LOCALONLY PROOF COMPANION. UNVERIFIED DRAFT. ORIGINAL P16.7 OPEN.\nHistorical mathematical bodies are DATA; retention is not audit credit.\n']
own_components = ['standalone.tex', 'new-residual-proofs.tex', 'final-notes.json', 'source-application-reading-ledger.txt', 'source-application-reading-ledger.json', 'scoped-verdict.json', 'original-residual.txt', 'finite-check-output.json', 'binding-audit-output.json', 'unique-companion-framing-output.json', 'environment.json']
for name in own_components:
    parts.extend([f'\n===== ENTIRE OWN COMPONENT {name} =====\n'.encode(), (A / name).read_bytes()])
seen = {}
for i, e in enumerate(math):
    p = Path(e['path'])
    data = p.read_bytes()
    h = hashlib.sha256(data).hexdigest()
    if h in seen:
        assert data == seen[h]
        continue
    seen[h] = data
    parts.extend([f'\n===== ENTIRE SUPPLIED MATHEMATICAL DATA {i}: {p.name}; NO CORRECTNESS GRANT =====\n'.encode(), data])
assert b'\n'.join(parts) == (A / 'proof-companion.txt').read_bytes()
assert (A / 'original-residual.txt').read_bytes() == Path(math[17]['path']).read_bytes()
primary = [e for e in load(C / 'private-primary-packet-bindings.json') if 'P16.7-ROOT415-bounded-calculus-local-Gauss-and-Shilov-source' in e['path']]
assert len(primary) == 15
for e in primary:
    assert sha(e['path']) == e['sha256']
    assert Path(e['path']).read_bytes() not in (A / 'proof-companion.txt').read_bytes()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [290] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 300
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
assert not D.exists()
D.mkdir()
public = []
def retain(p, name=None):
    q = D / (name or p.name)
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    public.append(q)
    return q
retain(raw, 'native289-actual-FINAL-all-five-fields.json')
retain(K / 'round289-terminal-actual-final-ROOT-retention-20261009.json')
retain(C / 'original-task.json', 'ROOT-unchanged-original-task.json')
for name in ['standalone.tex', 'new-residual-proofs.tex', 'final-notes.json', 'source-application-reading-ledger.txt', 'source-application-reading-ledger.json', 'scoped-verdict.json', 'original-residual.txt', 'companion-component-manifest.json', 'finite-check-output.json', 'unique-companion-framing-output.json']:
    retain(A / name)
for n in x['notes']:
    p = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(p, n)
    public.append(p)
    retain(A / (n['id'] + '.txt'))
programs = ['packet_audit.py', 'component_framing.py', 'assemble_paper.py', 'verify_finite.py', 'write_return.py', 'build_companion.py', 'read_selected.py']
for name in programs:
    retain(A / name, 'native-program-' + name + '.DATA.txt')
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now, paper=418, atom='P16.7', UNREVIEWED=True, candidate=False, accepted=False, original_closed=False, counts=dict(solved=16, open=26, accepted_scoped_papers=97), actual_FINAL=dict(path=str(raw), sha256=sha(raw), all_four_actual_five_field_notes_ROOT_physically_read=True, support_valid=True), full_1166_line_standalone_ROOT_physically_read=True, full_389_line_expanded_new_residual_proof_separately_ROOT_physically_read=True, full_current_unique_TXT_and_JSON_ledgers_verdict_residual_preamble_abstract_ROOT_physically_read=True, native_programs_ALL_ROOT_physically_read_as_DATA=programs, supplied_or_native_programs_executed_or_imported=False, exact_whole_source_and_companion_independently_ROOT_literally_reconstructed=True, whole_reconstruction_NOT_extra_reading_or_correctness_grant=True, artifact_note_texts_differ_from_actual_FINAL_by_exactly_one_trailing_LF=True, qualified_applied_immediate_primary_units=primary, all_15_complete_immediate_units_ROOT_physically_read_in_prior415_review_at_disclosed_exact_hypotheses=True, current_applications_ROOT_rejudged_and_qualifications_retained=True, fresh_primary_reading_credit_this_record=0, deeper_recursive_primary_geometric_nonalgebraization_generated_descent_audit_NOT_complete=True, new_complete_scoped_proofs=['One actual fast sequence simultaneously on EVERY fixed bounded-test energy sublevel: ordinary open O_m with Cap_(C+k)(O_m)<=8*2^(-3m)/7; quasi-uniform Borel limsup u, null N for every bounded MA/mixed measure and fixed-sublevel weak limit, NO full point in N', 'Uniform Tonelli variation/integral tails R_j for bounded MA tests and nu; actual finite maxima remain C_C and have both energy and I error<=R_j, uniformly weak/moving-moment convergence to nu and maximize nu', 'EVERY arbitrary-support prescribed mu: actual Borel u is integrable, -infinity locus mu-null, S_j->u in L1(mu), lim int|a_j-u|mu=J>=0', 'J EXACTLY equals lim_j sup_(q>=j)[B-Fmu(M_jq)] and finite-max asymptotic objective loss; J=0 iff L1(mu) convergence iff uniform prescribed-mu maximality of ALL finite tail maxima', 'Any full-point USC excess requires arbitrarily small-capacity ordinary open spikes accumulating at that point; necessary condition only', 'IF every actual S_j continuous, Dini/minimal uniform closure gives S_j in C, decreasing presentation u in original G, E(u)=e and actual MAu=nu; complete generated weak-operator reconstruction at already-presented scope'], residual=['J=0 not proved; no sequence independence or identity J=K asserted', 'Global ordinary USC, positive analytic or original C/G recognition of Borel u, S_j, regularizations unproved', 'Small capacity alone gives no ordinary neighborhood exclusion; R=ell full-point equality and fixed-menu Shilov basis unproved', 'Even conditional recognition MAu=nu does NOT prove nu=EVERY prescribed mu; original arbitrary-support existence/uniqueness and full geometric/source audit remain OPEN'], finite_checks_NOT_ROOT_executed_and_NOT_certification=True, compiler='NOT_YET_INVOKED_FOR418', protected_editor_OPEN_UNCHANGED=True, active_native290_mathematics_NOT_inspected_or_hot_fed=True, new_ROOT417_proof_is_separate_NOT_native289_input=True, full_primary_literal_units_pixels_books_LOCALONLY=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp, scope)
public.append(sp)
comp = D / 'proof-companion.txt'
comp.write_bytes(b'ENTIRE ROOT418 proof packet. UNREVIEWED, original P16.7 OPEN.\n\nEXACT captured actual settled FINAL, ALL FIVE fields:\n\n' + raw.read_bytes() + b'\n\nENTIRE native289 proof companion, independently literal reconstruction checked:\n\n' + (A / 'proof-companion.txt').read_bytes() + b'\n\nENTIRE ROOT418 application/scope/residual:\n\n' + sp.read_bytes())
public.append(comp)
b = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(b, dict(recorded_utc=now, paper=418, whole_source=dict(path=str(D / 'standalone.tex'), bytes=(D / 'standalone.tex').stat().st_size, sha256=sha(D / 'standalone.tex')), whole_companion=dict(path=str(comp), bytes=comp.stat().st_size, sha256=sha(comp)), public_files=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)) for p in public], UNREVIEWED=True, accepted=False, original_closed=False, compiler='NOT_YET_INVOKED_FOR418', counts=scope['counts'], protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now, ROOT418_whole_unreviewed=dict(binding=str(b), sha256=sha(b)), next_work='Whole ROOT418 complete actual four-note FINAL/all1166-LF source/distinct389-LF residual proof/current unique ledgers ROOT read and source+companion literally reconstructed; same fifteen full prior ROOT415 primary units retain exact application qualifications, no extra reading credit. Compile actual source, then freeze next P16.7 analytic representation and exact J defect with whole418+417. Native290 P12.3 active; at mostTWO, no active math/hot feedback; regular NONFORCE301 whole proof checkpoint; counts/editor unchanged.')
    write(p, y)
print(json.dumps(dict(paper=418, source_bytes=(D / 'standalone.tex').stat().st_size, source_sha256=sha(D / 'standalone.tex'), companion_bytes=comp.stat().st_size, public_files=len(public)+1, primary_units_reused_with_qualifications=15, fresh_primary_reading_credit=0, original_closed=False, accepted=False, binding=str(b)), indent=2))
