"""ROOT data retention after physical proof reading; no native-code execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-287/P16.7-whole411412-universal-variational-limits-and-actual-representability'
A = C / 'artifacts/codex-oHP4qV'
D = K / 'public-P16.7-continuation415-universal-variational-limits-local-Gauss-fibres-and-USC-relaxation-unreviewed'
U = R / 'primary-data-LOCALONLY/P16.7-ROOT415-bounded-calculus-local-Gauss-and-Shilov-source-20261009'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round287-raw-native-actual-FINAL.json'
assert sha(raw) == 'd361d45e9a36837c1152f43687e0a5477412f75d228cb12a481400f52888fb89'
x = json.loads(raw.read_text())
assert x['candidate'] is False and len(x['notes']) == 5
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = json.loads((R / name).read_text())
    assert y['current_active_batch'] == [] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 298
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
retain(raw, 'native287-actual-FINAL-all-five-fields.json')
retain(K / 'round287-terminal-actual-final-ROOT-retention-20261009.json')
known = set()
for n in x['notes']:
    assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
    assert set(n['support']) <= known
    known.add(n['id'])
    p = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(p, n)
    public.append(p)
names = ['scoped-paper.tex', 'geometric-family-fragment.tex', 'source-application-reading-ledger.txt', 'source-application-reading-ledger.json', 'scoped-verdict.json', 'original-residual.txt', 'proof-companion.txt']
for name in names:
    retain(A / name, 'native287-original-proof-companion.txt' if name == 'proof-companion.txt' else name)
programs = ['build_deliverables.py', 'verify_progress.py', 'read_data.py', 'input_analysis.py', 'check_delivery_own.py', 'write_notes.py']
for name in programs:
    retain(A / name, 'native-program-' + name + '.DATA.txt')
primary = []
for p in sorted((A / 'LOCALONLY-primary').iterdir()):
    assert p.is_file()
    q = U / p.name
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    primary.append(dict(name=p.name, LOCALONLY_path=str(q), bytes=q.stat().st_size, sha256=sha(q), full_immediate_unit_physically_ROOT_read=True))
assert len(primary) == 15
comp = (A / 'proof-companion.txt').read_text()
unique = comp
for name in ['scoped-paper.tex', 'source-application-reading-ledger.txt', 'original-residual.txt', 'scoped-verdict.json']:
    s = (A / name).read_text()
    assert comp.count(s) == 1
    unique = unique.replace(s, '[WHOLE COMPONENT ALREADY PHYSICALLY READ: ' + name + ']')
framing = D / 'ROOT-native-companion-unique-framing.txt'
framing.write_text(unique)
public.append(framing)
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now, paper=415, atom='P16.7', UNREVIEWED=True, accepted=False, original_closed=False, counts=dict(solved=16, open=26, accepted_scoped_papers=97), actual_FINAL=dict(path=str(raw), bytes=raw.stat().st_size, sha256=sha(raw), candidate=False, all_five_fields_of_every_note_physically_ROOT_read=True, note_ids=[n['id'] for n in x['notes']], support_valid=True), distinct_expanded_proofs=dict(whole_scoped_paper_LF_ranges=[[1, 220], [221, 440], [441, 660], [661, 774]], whole_geometric_fragment_LF_ranges=[[1, 91]], independently_physically_ROOT_read=True, fragment_difference='The fragment uses the misleading phrase finitely many fibres; the complete scoped paper correctly says finite fibres over a compact parameter family. Raw originals retained separately.'), native_ledger_text_and_JSON_whole_ROOT_read=True, whole_residual_and_verdict_ROOT_read=True, program_DATA=dict(all_six_programs_physically_ROOT_read=programs, native_or_supplied_programs_executed_or_imported=False), freshly_applied_complete_immediate_primary_units=primary, actual_primary_carriers_not_read_whole=True, complete_recursive_historical_and_geometric_audit=False, source_application_boundary=['CLD15.7.1-3: pure separated analytic surface and compatible calibrated calculus; smooth partition/approximation foundations remain named', 'CLD8.1.1-8.2.4: ENTIRE minimal continuous sheaf and transfinite uniform closure, actual convex/max gluing', 'CLD8.5-8.8: actual positive closed products, uniform continuity, dpsh extension and smooth null-reference invariance; arbitrary-multiplier closedness8.6.7 NOT applied', 'CLD5.11.1 and7.2.8-12: boundaryless smooth Green/Stokes, positive top Radon/coefficient measures; whole immediate proofs read', 'CLD11.6.1-5 and13.8.1-5: full graded dimension and fixed Laurent initials; relative interior and reduced target give local finite-flat singleton-Gauss representative', 'CLD18.6.1-2 and14.5.2-3: boundaryless fixed-residue-field fibre current, positive integer local degree, NO second extension-degree factor; relative intersection deeper foundations named', 'CLD5.10.1-2: actual top Radon reconstruction/calibrated raw factor2; OCR inequality in part(a) is not applied', 'GR unnumbered1.2, whole4.2 and6.1-6.5: CLD-to-classical bridge, actual all-support maximum at every affinoid Shilov boundary; 6.5 still REQUIRES already USC FULL pointwise limit', 'The compact good smooth separated boundaryless quotient carrier is explicitly geometric input; genuine nonalgebraization and original generated/descent source chains are not newly independently certified'], complete_new_conditional_proofs=['Uniform third-MA absolute moments on each same energy sublevel', 'Every normalized finite-FULL-dual maximizing net: universal energy/self/mixed/reference and cross moving-moment limits', 'Actual MA and mixed B(a,0) have common genuine Radon weak limits against EVERY continuous test, without countability or metrizability', 'Exact limiting full dual D(nu)=e-p and L1(nu) convergence; prescribed-measure signed integrals ONLY', 'Fixed Laurent finite-flat local Gauss-fibre families have common bounded caps and uniform positive atoms at EVERY fibre point; uniform maximizing-net convergence in this compact local sector', 'All affinoid Shilov values construct the same actual normalized USC upper relaxation; no asserted positivity or finite-energy recognition', 'Exact nonnegative prescribed-measure dual defect and precise sufficient UNPROVED two-sided variation condition'], ROOT414_separate_result_not_hot_fed_to_native287=True, residual=['Actual USC relaxation must be proved positive/in original analytic finite-energy domain and equal to full-point tuple', 'Local Gauss-fibre sector does NOT provide needed Shilov-neighborhood basis: ordinary neighborhoods can exclude cancellation points with same coordinate radii', 'Actual weak limit nu must be shown to equal EVERY arbitrary-support prescribed mu, or another proved original-operator existence mechanism', 'No L1(mu) convergence follows from signed integral convergence', 'Full original P16.7 and complete requested historical/primary audit OPEN'], no_new_correctness_grant=True, compiler_NOT_yet_invoked=True, primary_literal_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True)
sp = D / 'ROOT-source-application-reading-scope-and-residual.json'
write(sp, scope)
public.append(sp)
whole = D / 'proof-companion.txt'
parts = ['ENTIRE ROOT415 retained proof packet. UNREVIEWED conditional deductions; original P16.7 OPEN. Identities/compilation never confer correctness.\n']
for n in x['notes']:
    parts += ['===== COMPLETE ACTUAL FINAL NOTE: ALL FIVE FIELDS =====\n', json.dumps(n, ensure_ascii=False, indent=2)]
parts += ['===== WHOLE DISTINCT EXPANDED STANDALONE PROOF =====\n', (D / 'scoped-paper.tex').read_text(), '===== WHOLE DISTINCT LOCAL GEOMETRIC FRAGMENT: RAW DATA =====\n', (D / 'geometric-family-fragment.tex').read_text(), '===== WHOLE NATIVE COMPANION WITH ITS UNIQUE FRAMING =====\n', comp, '===== WHOLE ROOT415 SOURCE APPLICATION SCOPE / RESIDUAL =====\n', sp.read_text()]
whole.write_text('\n'.join(parts))
public.append(whole)
binding = D / 'ROOT-whole-paper-source-scope-and-binding.json'
write(binding, dict(recorded_utc=now, paper=415, whole_source=dict(path=str(D / 'scoped-paper.tex'), bytes=(D / 'scoped-paper.tex').stat().st_size, sha256=sha(D / 'scoped-paper.tex')), whole_companion=dict(path=str(whole), bytes=whole.stat().st_size, sha256=sha(whole)), public_files=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)) for p in public], UNREVIEWED=True, accepted=False, original_closed=False, compiler='NOT_YET_INVOKED', counts=scope['counts'], protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = json.loads(p.read_text())
    y.update(updated_utc=now, ROOT415_whole_unreviewed=dict(binding=str(binding), sha256=sha(binding)), next_work='Physically read ROOT415 unique companion framing, compile whole standalone415 and retain actual result. Then freeze289 with WHOLE415/414 and complete ROOT tail-maximum note plus qualified current original residual. Native288 actual terminal FINAL retained unread; no original or scoped acceptance. Counts/editor unchanged.')
    write(p, y)
print(json.dumps(dict(paper=415, public_files=len(public)+1, source_bytes=(D / 'scoped-paper.tex').stat().st_size, source_sha256=sha(D / 'scoped-paper.tex'), companion_bytes=whole.stat().st_size, full_primary_units_read=15, candidate=False, unique_native_companion_framing=unique, binding=str(binding)), ensure_ascii=False, indent=2))
