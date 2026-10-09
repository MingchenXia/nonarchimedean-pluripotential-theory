"""Passive ROOT literal reconstruction; all supplied/native programs remain DATA."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-295/P16.7-whole424-nonskeletal-equation-and-full-representation'
A = C / 'artifacts/codex-36Pd4E'
D = K / 'public-P16.7-continuation427-prescribed-nonskeletal-two-atom-equation-and-dominated-L1-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
hashbytes = lambda b: hashlib.sha256(b).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2) + '\n')
raw = K / 'round295-raw-native-actual-FINAL.json'
assert sha(raw) == '86ce7e9d34c72d42640bcf77d27dad7d9113e124f3ade798679ad81abb597c05'
assert not D.exists()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [296] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 306
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
actual, assembled = load(raw), load(A / 'final-notes.json')
assert actual['candidate'] is False and assembled['candidate'] is False
assert len(actual['notes']) == len(assembled['notes']) == 4
known, differences = set(), []
for n,m in zip(actual['notes'],assembled['notes']):
    assert set(n) == set(m) == {'id','summary','detailedSummary','text','support'}
    assert n['id'] == m['id'] and n['support'] == m['support'] and set(n['support']) <= known
    known.add(n['id'])
    assert load(A / ('actual-' + m['id'] + '-all-five-fields.json')) == m
    assert (A / ('note-' + m['id'] + '.txt')).read_text().strip() == m['text']
    differences.append(dict(id=n['id'],different_fields=[key for key in n if n[key] != m[key]]))
bindings = load(C / 'mathematical-packet-bindings.json')
assert len(bindings) == 46
for e in bindings:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
data = lambda i: Path(bindings[i]['path']).read_bytes()
assert (A / 'original-residual.txt').read_bytes() == data(37)
assert (A / 'unchanged-original-task.json').read_bytes() == data(43)
old = data(42).decode()
start, stop = old.index('\\title{'), old.index('\\author{')
source = old[:start] + '\\title{A prescribed nonskeletal two-atom equation sector\\\\on the designated analytic quotient}\n' + old[stop:]
start = source.index('\\begin{abstract}')
stop = source.index('\\end{abstract}',start) + len('\\end{abstract}')
abstract = r'''\begin{abstract}
We retain the complete qualified current424 proof body and its source
limitations, then construct actual continuous weights solving the
prescribed nonskeletal targets $(2-m)\delta_g+m\delta_{x_c}$ for
$c>0$, $0\le m\le1$. A finite logarithmic maximum glues across an
ordinary collar. Exact CLD fixed-fibre products identify every atom and
the mixed product, giving the equation, full-dual attainment, energy,
generated uniqueness, and actual representation of the canonical tuple
from nonordered maximizing families. Domination by a fixed bounded MA
measure gives quantitative prescribed-measure $L^1$ convergence and
zero integral defect, including for the unchanged input $2\delta_x$.
That whole-mass Dirac equation, general nonordered representation,
arbitrary-support existence and genuine nonalgebraization/descent remain
open. All material is an unverified local draft.
\end{abstract}'''
source = source[:start] + abstract + source[stop:]
marker = '\\begin{thebibliography}{9}'
assert source.count(marker) == 1
source = source.replace(marker,(A / 'new-residual-proofs.tex').read_text() + '\n' + marker)
assert source == (A / 'standalone.tex').read_text()
assert len(source.encode()) == 137655 and source.count('\n') == 2820
assert (A / 'new-residual-proofs.tex').stat().st_size == 22233
assert (A / 'new-residual-proofs.tex').read_bytes().count(b'\n') == 431
own_names = ['standalone.tex','new-residual-proofs.tex','note-n1.txt','note-n2.txt','note-n3.txt','note-n4.txt',
             'actual-n1-all-five-fields.json','actual-n2-all-five-fields.json','actual-n3-all-five-fields.json','actual-n4-all-five-fields.json',
             'final-notes.json','source-application-reading-ledger.json','source-application-reading-ledger.txt','scoped-verdict.json','original-residual.txt','unchanged-original-task.json','binding-audit-output.json','check-output.json','environment.json','commands.txt','prepare_delivery.py','assemble_delivery.py','check_delivery.py','package_delivery.py','prepare-delivery.log','assemble-delivery.log','check-delivery.log','input.json']
parts = [b'WHOLE LOCALONLY UNVERIFIED PROOF COMPANION. UNCHANGED ORIGINAL P16.7 OPEN.\nAll supplied programs are inert DATA. Retention is not reading or correctness.\n']
for name in own_names:
    b = (A / name).read_bytes()
    parts += [f'\n===== WHOLE OWN BODY {name}; bytes {len(b)}; SHA256 {hashbytes(b)} =====\n'.encode(),b]
seen = {}
for i,e in enumerate(bindings):
    b,h = data(i),e['sha256']
    if h not in seen:
        seen[h] = i
        parts += [f'\n===== WHOLE SUPPLIED INERT BODY {i}; {Path(e["path"]).name}; bytes {len(b)}; SHA256 {h} =====\n'.encode(),b]
primary = [e for e in load(C / 'private-primary-packet-bindings.json') if 'P16.7-ROOT415-bounded-calculus-local-Gauss-and-Shilov-source' in e['path']]
assert len(primary) == 15
for local in sorted((A / 'LOCALONLY-primary').iterdir()):
    b = local.read_bytes()
    assert any(e['sha256'] == hashbytes(b) and e['bytes'] == len(b) for e in primary)
    parts += [f'\n===== WHOLE PRIMARY LOCALONLY {local.name}; bytes {len(b)}; SHA256 {hashbytes(b)} =====\n'.encode(),b]
assert b'\n'.join(parts) == (A / 'proof-companion.txt').read_bytes()
assert (A / 'proof-companion.txt').stat().st_size == 7161787
D.mkdir()
public = []
def retain(p,name=None):
    q = D / (name or p.name)
    shutil.copyfile(p,q)
    assert sha(p) == sha(q)
    public.append(q)
retain(raw,'native295-actual-FINAL-all-five-fields.json')
retain(A / 'final-notes.json','native295-assembled-notes-separate-from-actual.json')
for name in own_names:
    if name in ['final-notes.json','input.json']:
        continue
    target = 'native-program-' + name + '.DATA.txt' if name.endswith('.py') else 'native-assembled-' + name if name.startswith('note-') or name.startswith('actual-') else name
    retain(A / name,target)
for n in actual['notes']:
    p = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(p,n)
    public.append(p)
for name in ['delivery-check-output.json','artifact-bindings.json','companion-component-manifest.json']:
    retain(A / name)
now = datetime.now(timezone.utc).isoformat()
fresh = [e for e in primary if Path(e['path']).name[:4] in ['1224','1225']]
assert len(fresh) == 2
scope = dict(recorded_utc=now,paper=427,atom='P16.7',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,
    counts=dict(solved=16,open=26,accepted_scoped_papers=97),actual_FINAL=dict(path=str(raw),sha256=sha(raw),all_four_actual_notes_all_five_fields_physically_ROOT_read=True),actual_vs_assembled_note_field_comparison=differences,assembled_notes_retained_separately=True,
    entire431_LF_22233_byte_distinct_new_formal_proof_physically_ROOT_read=True,
    complete_unique_current_preamble_JSON_and_TXT_ledger_verdict_and_residual_physically_ROOT_read=True,
    native_programs_entire_FOUR_physically_ROOT_read_ONLY_as_DATA=True,
    initial_oversize_combined_program_display_NO_full_reading_credit=True,prepare_and_assemble_complete_untruncated_reread=True,
    source_ROOT_exact_passive_literal_reconstruction=True,native_LOCALONLY_companion_ROOT_exact_passive_literal_reconstruction=True,
    whole_inherited424_2390_LF_physically_ROOT_read_previously=True,incoming_correctness_grants=[],
    all_fifteen_complete_immediate_primary_units=primary,two_current_ROOT_freshly_reread_whole_units=fresh,
    other_thirteen_units_current_fresh_ROOT_reading_credit=0,
    source_applications_ROOT_rejudged=True,
    primary_scope='Exact CLD18.6.1/18.6.2 statements and whole proofs freshly physically ROOT reread: ordinary open boundaryless separated equidimensional charts, positive radii, translations/inversions actual isomorphisms, fixed completed-residue-field curve, degree1/current coefficient1 not2. Typographic prose slips in the literal primary are excluded. Same entire minimal-sheaf/local-uniform/convex-max/recursive-current/fixed-restriction/continuous-test/primitive-calibration/Green/full-Shilov units retain ROOT415/424 prior full reading and conventional deeper CLD/Berkovich/Temkin/Ducros/Wanner/Thuillier foundations. No deeper recursive audit or genuine nonalgebraization/coherent descent certification.',
    complete_conditional_deductions=[
        'Actual original-C nonskeletal equation MA(q_m,c)=(2-m)delta_g+m delta_xc for EVERYc>0,0<=m<=1, via finite logarithmic maximum and genuine ordinary collar gluing, exact degree1 fixed fibres and mixed product2delta_g.',
        'Explicit q=q0+sqrt(m)v_c, normalized range[-1/4-csqrt(m),0], E=-1/3-cm^(3/2)/3, FULL dual D=1/6+2cm^(3/2)/3 attained, actual decreasing G presentation and uniqueness among ALL actual G solutions.',
        'Canonical nonordered full-point tuple/ordinary upper relaxation represented by actual explicit bounded solution in this sector; weak MA convergence, every fast J=K0, remaining raw Borel points not declared positive.',
        'For lambda>1 the extended explicit segment has negative curve curvature and is outsideC; this is a route obstruction, not no-existence theorem for whole2Dirac.',
        'EVERYrawmass2 mu<=A MA(w), fixedboundedw: FULLD<=A(1+Bw)+1.5A²Bw, canonical L1(mu) maximizing limit, every fast actual Borel u has late L1error<=(16A/15)2^(-4j), UI/truncation convergence and J0. No actual analytic representation or MA=mu inferred.',
        'Specified whole2delta_x<=2MA(q_1,1/8), every fast J0, rigorous full dual3/8<=D<=4; its actual equation remains OPEN.'],
    residual=['Whole-mass2Dirac and every arbitrary-support original input equation remain OPEN.','General nonordered analytic recognition/envelopes/adequate variational perturbations and genuine nonalgebraization/coherent descent/deeper recursive audit remain OPEN.'],
    native_finite_checks_ONLY_observations=load(A / 'check-output.json'),compiler='NOT_YET_INVOKED_FOR427',
    native296_ACTIVE_math_NOT_read_or_supplied=True,hot_feedback=False,
    native_companion_CONTAINS_fifteen_literal_primary_bodies_and_is_LOCALONLY=True,
    public_companion_rebuilt_from_mathematics_only_NO_literal_primary_bodies=True,
    supplied_or_native_programs_executed_or_imported=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp,scope)
public.append(sp)
rootparts = [b'WHOLE ROOT427 mathematical proof packet. UNREVIEWED; originalP16.7 OPEN. No literal primary bodies. Retention supplies no reading/correctness credit.\n']
for p in public:
    rootparts += [f'\n===== WHOLE CURRENT PUBLIC COMPONENT {p.name} =====\n'.encode(),p.read_bytes()]
retained = []
for i,e in sorted(enumerate(bindings),key=lambda pair: pair[1]['bytes'],reverse=True):
    b = data(i)
    present = any(b in part for part in rootparts)
    if not present:
        rootparts += [f'\n===== WHOLE SUPPLIED INERT MATHEMATICAL BODY {i}: {Path(e["path"]).name} =====\n'.encode(),b]
    retained.append(dict(index=i,bytes=len(b),sha256=e['sha256'],whole_body_retained=True,embedded_in_existing_whole_component=present,fresh_reading_credit=0))
comp = D / 'proof-companion.txt'
comp.write_bytes(b'\n'.join(rootparts))
whole = comp.read_bytes()
assert all(data(i) in whole for i in range(len(bindings)))
assert all(Path(e['path']).read_bytes() not in whole for e in primary)
public.append(comp)
cp = D / 'ROOT-whole-companion-containment-ledger.json'
write(cp,dict(storage_only_NOT_reading_or_correctness_credit=True,records=retained,all_fifteen_literal_primary_carriers_excluded_from_public_companion=True,native_whole_companion_LOCALONLY=dict(path=str(A / 'proof-companion.txt'),bytes=7161787,sha256=sha(A / 'proof-companion.txt'),exact_literal_reconstruction_checked=True,CONTAINS_literal_primary_bodies=True)))
public.append(cp)
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=427,whole_source=dict(path=str(D / 'standalone.tex'),bytes=len(source.encode()),sha256=sha(D / 'standalone.tex')),whole_companion=dict(path=str(comp),bytes=comp.stat().st_size,sha256=sha(comp)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler='NOT_YET_INVOKED_FOR427',counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now,ROOT427_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='Whole actual295 and distinct431LF new proof read and ROOT427 passively reconstructed at exact fixed-fibre source applications. Native companion contains literalprimary LOCALONLY; public entire-math companion excludes all15literalcarriers. Invoke desktop compiler then freeze small297 toward whole-massDirac/generalnonorderedrepresentation; native296 isolated active. NONFORCE307 next; counts/editor unchanged.')
    write(p,y)
print(json.dumps(dict(paper=427,source_bytes=len(source.encode()),source_LF=source.count('\n'),companion_bytes=comp.stat().st_size,public_files=len(public)+1,actual_vs_assembled=differences,every46_math_body_retained_whole=True,all15literal_primary_bodies_excluded=True,accepted=False,original_closed=False,binding=str(B)),indent=2))
