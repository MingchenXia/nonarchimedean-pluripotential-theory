"""ROOT passive literal reconstruction and whole-proof retention. Native code is DATA."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-293/P16.7-whole421-actual-Gauss-Radon-existence-and-general-attainment'
A = C / 'artifacts/codex-FcrcG8'
D = K / 'public-P16.7-continuation424-every-Gauss-Radon-and-strict-projection-gap-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round293-raw-native-actual-FINAL.json'
assert sha(raw) == 'fbb27b3ba04fc2debba3c0f7f9294b4511ee328a98117783b46296f45feb21df'
x = load(raw)
assembled = load(A / 'final-notes.json')
assert x['candidate'] is False and len(x['notes']) == 4
assert not D.exists()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [294] and y['github_pending_checkpoint'] is None
    assert y['latest_verified_github_checkpoint']['continuation'] == 304
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
known = set()
differences = []
for n, m in zip(x['notes'], assembled['notes']):
    assert set(n) == set(m) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
    assert n['id'] == m['id'] and n['support'] == m['support'] and set(n['support']) <= known
    known.add(n['id'])
    assert load(A / ('actual-' + m['id'] + '-all-five-fields.json')) == m
    assert (A / (m['id'] + '.txt')).read_text() == m['text'] + '\n'
    differences.append(dict(id=n['id'], different_fields=[key for key in n if n[key] != m[key]]))
bindings = load(C / 'mathematical-packet-bindings.json')
assert len(bindings) == 202
for e in bindings:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
data = lambda i: Path(bindings[i]['path']).read_bytes()
assert (A / 'original-residual.txt').read_bytes() == data(20)
assert (A / 'unchanged-original-task.json').read_bytes() == data(0)
source = data(27).decode()
i = source.index('\\title{')
j = source.index('\\author{', i)
source = source[:i] + '\\title{Every Gauss-supported Radon equation on the designated analytic quotient\\\\and strict full-dual separation of nonskeletal measures}\n' + source[j:]
i = source.index('\\begin{abstract}')
j = source.index('\\end{abstract}', i) + len('\\end{abstract}')
source = source[:i] + r'''\begin{abstract}
We retain the full qualified 421 proof body, then prove periodic real
Alexandrov existence and uniqueness for every Radon probability by
finite Laguerre cells, Legendre conjugation and a proved weak-limit
argument. Positive convex convolution and actual recursive CLD products
lift these solutions to bounded continuous weights in the original
entire CLD class on the designated input quotient. Every raw-mass-two
Gauss-supported Radon target, including atoms and singular measures,
therefore has an actual solution and full-dual attainment at the explicit
conventional analytic foundation boundary. A direct presentation argument
gives uniqueness against all actual generated solutions. For arbitrary
eligible support, equality of the full dual with the dual of the Gauss
projection holds exactly for skeletal measures; a nonskeletal measure has
a strictly positive quantified gap. General arbitrary-support existence,
genuine nonalgebraization/coherent descent, and the deeper recursive audit
remain open. All material is an unverified local draft.
\end{abstract}''' + source[j:]
marker = '\\begin{thebibliography}{9}'
assert source.count(marker) == 1
source = source.replace(marker, '\n' + (A / 'new-residual-proofs.tex').read_text() + '\n' + marker)
assert source == (A / 'standalone.tex').read_text()
assert len(source.encode()) == 115639 and source.count('\n') == 2390
components = ['standalone.tex','new-residual-proofs.tex','n1.txt','n2.txt','n3.txt','n4.txt','final-notes.json',
              'return-n1.txt','return-n2.txt','return-n3.txt','return-n4.txt',
              'expanded-note-n1.txt','expanded-note-n2.txt','expanded-note-n3.txt',
              'source-application-reading-ledger.json','source-application-reading-ledger.txt','scoped-verdict.json',
              'original-residual.txt','unchanged-original-task.json','binding-audit-output.json','finite-check-output.json',
              'environment.json','commands.txt','assemble_local.py','verify_local.py','package_local.py',
              'assemble-local-run.log','verify-local-run.log']
parts = [b'WHOLE LOCALONLY UNVERIFIED PROOF COMPANION. ORIGINAL P16.7 OPEN.\nRetention and hashing supply no independent reading/audit/correctness credit.\n']
hashbytes = lambda b: hashlib.sha256(b).hexdigest()
for name in components:
    b = (A / name).read_bytes()
    parts += [f'\n===== WHOLE OWN COMPONENT {name}, {len(b)} bytes, SHA256 {hashbytes(b)} =====\n'.encode(), b]
seen = set()
for i, e in enumerate(bindings):
    if e['sha256'] not in seen:
        seen.add(e['sha256'])
        b = data(i)
        parts += [f'\n===== WHOLE SUPPLIED INERT DATA {i}, {Path(e["path"]).name}, {len(b)} bytes =====\n'.encode(), b]
assert b'\n'.join(parts) == (A / 'proof-companion.txt').read_bytes()
assert (A / 'proof-companion.txt').stat().st_size == 11175965
primary = [e for e in load(C / 'private-primary-packet-bindings.json') if 'P16.7-ROOT415-bounded-calculus-local-Gauss-and-Shilov-source' in e['path']]
assert len(primary) == 15
for e in primary:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
fresh_prefixes = {'1152', '1153', '1180', '1221', '1223', '1226'}
fresh = [e for e in primary if Path(e['path']).name[:4] in fresh_prefixes]
assert len(fresh) == 6
D.mkdir()
public = []
def retain(p, name=None):
    q = D / (name or p.name)
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    public.append(q)
retain(raw, 'native293-actual-FINAL-all-five-fields.json')
retain(C / 'original-task.json', 'ROOT-unchanged-original-task.json')
for name in components:
    if name == 'final-notes.json':
        target = 'native-assembled-final-notes-distinct-from-actual.json'
    elif name.startswith('return-'):
        target = 'native-assembled-' + name
    elif name.startswith('n') and name[1:2].isdigit():
        target = 'native-assembled-' + name
    elif name.endswith('.py'):
        target = 'native-program-' + name + '.DATA.txt'
    else:
        target = name
    retain(A / name, target)
for n, m in zip(x['notes'], assembled['notes']):
    p = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(p, n)
    public.append(p)
    retain(A / ('actual-' + m['id'] + '-all-five-fields.json'), 'native-assembled-' + m['id'] + '-all-five-fields.json')
for name in ['delivery-check-output.json', 'artifact-bindings.json', 'companion-component-manifest.json']:
    retain(A / name)
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now, paper=424, atom='P16.7', UNREVIEWED=True, accepted=False, original_closed=False, candidate=False,
    counts=dict(solved=16, open=26, accepted_scoped_papers=97),
    actual_FINAL=dict(path=str(raw), sha256=sha(raw), all_four_actual_notes_all_five_fields_physically_ROOT_read=True),
    actual_vs_assembled_note_field_comparison=differences,
    assembled_notes_retained_separately=True,
    entire_new_actual_and_distinct_expanded_mathematics_physically_ROOT_read=True,
    expanded_n1_8510_bytes_full=True, expanded_n2_441_LF_23166_bytes_full=True, expanded_n3_157_LF_7563_bytes_full=True,
    new_588_LF_formal_proof_body_separately_physically_ROOT_read=True,
    full_current_JSON_and_TXT_ledger_verdict_and_residual_physically_ROOT_read=True,
    entire_three_native_programs_physically_ROOT_read_ONLY_as_DATA=True,
    source_exact_ROOT_literal_reconstruction=True, native_companion_exact_ROOT_literal_reconstruction=True,
    inherited_whole421_proof_physically_ROOT_read_previously=True,
    changed_current_preamble_physically_ROOT_read=True,
    supplied_or_native_programs_executed_or_imported=False, incoming_correctness_grants=[],
    inherited_fifteen_complete_immediate_primary_units=primary,
    six_current_ROOT_freshly_reread_whole_immediate_primary_units=fresh,
    fresh_1180_display='raw LF 1:190 and 191:361, including final non-LF text; not Python splitlines convention',
    other_nine_current_ROOT_fresh_primary_reading_credit=0,
    source_applications_ROOT_rejudged=True,
    primary_scope='All fifteen complete immediate units previously physically ROOT read415. Six freshly reread here: entire minimal CLD sheaf/convex closure, positive Radon/coefficient currents and smooth-test density, actual recursive product/continuity and smooth-null gluing/support, primitive degree-one calibration and top Radon reconstruction, entire GR6.1--6.5 chain for finite full-dimensional affinoid Shilov maximum. Remaining nine reapplied at the same bounded-calculus/full-point conventional foundation boundary, without new fresh reading credit. No full recursive source/book/coherent descent audit.',
    complete_conditional_deductions=[
        'Independent periodic real Alexandrov existence and uniqueness for EVERY Radon probability via compact finite Laguerre minimization, correctly directed Legendre conjugation, measurable subgradient images, finite-grid approximation and proved conjugate-gradient continuity.',
        'Actual positive convex smooth convolution lifts every Gauss-supported raw-mass-two Radon target to original entire C, actual recursive MA equality on EVERY analytic continuous test, normalized range[-1/2,0], E[-1,0], full dual D<=1 and actual decreasing G presentation.',
        'Uniqueness against ALL actual generated solutions sharing a bounded solution measure, by full-dual generated calibration, full-point moduli, USC/dense full points and actual finite Shilov maximum; no Borel recognition theorem presumed.',
        'Every fast family for a skeletal target has J=K=0, canonical nu=mu and R=q; no positivity assigned to remaining Borel limit points.',
        'EVERY eligible arbitrary-support mu has D(mu)>=D(sigma_*tau_*mu), equality exactly for skeletal mu. Continuous invariant full-dual attainment iff skeletal; actual segment gap>=min(Delta/2,Delta^2/(96C0)).',
        'Concrete nonskeletal full-point2Dirac has finite FULL dual and strict gap>=1/25165824 beyond skeletal dual1/6; no invariant maximizer, no noninvariant existence theorem.',
        'Weak-to-uniform normalized skeletal solution stability, |D0-D1|<=W1 and I<=8W1 with raw mass2; explicit Gauss atom E=-1/3,D=1/6.'],
    residual=['General arbitrary-support existence/attainment, nonordered actual C/G representation and adequate envelopes/variations remain OPEN.',
              'Genuine nonalgebraization/coherent descent of the input quotient and deeper recursive analytic source audit remain unproved.'],
    finite_observations_NOT_proofs=load(A / 'finite-check-output.json'),
    compiler='NOT_YET_INVOKED_FOR424',
    native294_active_math_NOT_read_or_supplied=True, hot_feedback=False,
    primary_literal_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True,
    truncated_scope_and_inventory_outputs_add_no_reading_credit=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp, scope)
public.append(sp)
# Retain every supplied mathematical body whole while avoiding duplicated ancestor bodies.
# Containment is only a storage optimization; it provides zero body-reading credit.
rootparts = [b'WHOLE ROOT424 proof packet. UNREVIEWED; original P16.7 OPEN.\n', raw.read_bytes(), sp.read_bytes()]
retained_records = []
for p in public:
    if p not in [D / 'native293-actual-FINAL-all-five-fields.json', sp]:
        rootparts += [f'\n===== WHOLE CURRENT PUBLIC COMPONENT {p.name} =====\n'.encode(), p.read_bytes()]
incoming_by_size = sorted(enumerate(bindings), key=lambda pair: pair[1]['bytes'], reverse=True)
for i, e in incoming_by_size:
    b = data(i)
    present = any(b in part for part in rootparts)
    if not present:
        rootparts += [f'\n===== WHOLE SUPPLIED INERT MATHEMATICAL BODY {i}: {Path(e["path"]).name} =====\n'.encode(), b]
    retained_records.append(dict(index=i, bytes=len(b), sha256=e['sha256'], whole_body_retained=True, embedded_in_an_existing_whole_component=present, freshness_credit=0))
companion = D / 'proof-companion.txt'
companion.write_bytes(b'\n'.join(rootparts))
for i, e in enumerate(bindings):
    assert data(i) in companion.read_bytes()
public.append(companion)
containment = D / 'ROOT-whole-companion-containment-ledger.json'
write(containment, dict(storage_only_NOT_new_reading_or_correctness_credit=True, records=retained_records, native_whole_companion_retained_LOCALONLY=dict(path=str(A / 'proof-companion.txt'), bytes=11175965, sha256=sha(A / 'proof-companion.txt'), exact_literal_reconstruction_checked=True)))
public.append(containment)
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B, dict(recorded_utc=now, paper=424, whole_source=dict(path=str(D / 'standalone.tex'), bytes=len(source.encode()), sha256=sha(D / 'standalone.tex')), whole_companion=dict(path=str(companion), bytes=companion.stat().st_size, sha256=sha(companion)), public_files=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)) for p in public], UNREVIEWED=True, accepted=False, original_closed=False, compiler='NOT_YET_INVOKED_FOR424', counts=scope['counts'], protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now, ROOT424_whole_unreviewed=dict(binding=str(B), sha256=sha(B)), next_work='Whole actual293 and distinct expansions read and qualified ROOT424 literally reconstructed; request native standalone compiler then freeze next small P16.7 batch toward actual nonskeletal/full-support existence. Native294 isolated active; no math inspection or hot feedback. Publish NONFORCE305 whole423424 plus qualified frozen295; counts/editor unchanged.')
    write(p, y)
print(json.dumps(dict(paper=424, source_bytes=len(source.encode()), source_LF=source.count('\n'), companion_bytes=companion.stat().st_size, public_files=len(public)+1, actual_vs_assembled_note_fields=differences, literal_reconstruction=True, every_202_math_body_retained_whole=True, original_closed=False, accepted=False, binding=str(B)), indent=2))
