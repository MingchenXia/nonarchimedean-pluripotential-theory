"""Passive ROOT retention and literal reconstruction; native programs remain DATA."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-294/P12.3-whole422-irreducible-conductor-centres-and-normal-residual'
A = C / 'artifacts/codex-PHQboi'
D = K / 'public-P12.3-continuation426-irreducible-centres-exact-filtration-and-surface-criterion-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round294-raw-native-actual-FINAL.json'
assert sha(raw) == '9f69f6faef649e07d7a6fa2ea6518c13b0c1212030b857c5755f5a10a07641ab'
assert not D.exists()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [295] and y['github_pending_checkpoint'] is None
    assert y['latest_verified_github_checkpoint']['continuation'] == 305
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
actual, assembled = load(raw), load(A / 'notes.json')
assert actual['candidate'] is False and assembled['candidate'] is False
assert len(actual['notes']) == len(assembled['notes']) == 5
known = {'G331'}
differences = []
for n, m in zip(actual['notes'], assembled['notes']):
    assert set(n) == set(m) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
    assert n['id'] == m['id'] and n['support'] == m['support'] and set(n['support']) <= known
    known.add(n['id'])
    assert (A / (m['id'] + '.md')).read_text().strip() == m['text']
    differences.append(dict(id=n['id'], different_fields=[key for key in n if n[key] != m[key]]))
bindings = load(C / 'mathematical-packet-bindings.json')
assert len(bindings) == 43
for e in bindings:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
data = lambda i: Path(bindings[i]['path']).read_bytes()
assert (A / 'original-residual.md').read_bytes() == data(28)
assert (A / 'original-task.json').read_bytes() == data(1)
assert (A / 'original-completion-criteria.txt').read_bytes() == data(27)
assert (A / 'qualified-G331.json').read_bytes() == data(31)
assert (A / 'qualified-G331.txt').read_bytes() == data(32)
mapping = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '^': r'\textasciicircum{}', '~': r'\textasciitilde{}', '<': r'\textless{}', '>': r'\textgreater{}'}
escape = lambda text: ''.join(mapping.get(ch, ch) for ch in text)
old = data(0).decode()
source = (A / 'P12.3-marked-centres.tex').read_text()
split = source.index('\\section{n1.')
header = source[:split]
base = old[:old.index('\\title{')]
assert header.startswith(base + '\\DefineVerbatimEnvironment{Full422Data}{Verbatim}{fontsize=\\tiny}\n' + '\\DeclareUnicodeCharacter{00B1}{\\ensuremath{\\pm}}\n')
assert header.endswith('\\tableofcontents\n')
assert header.count('\\begin{abstract}') == header.count('\\end{abstract}') == 1
chapters = [(A / (n['id'] + '.tex')).read_text() for n in assembled['notes']]
for n, chapter in zip(assembled['notes'], chapters):
    prefix = '\\section{' + escape(n['id'] + '. ' + n['summary']) + '}\n'
    prefix += '\\textit{Supports: ' + escape(', '.join(n['support'])) + '.}\n\n'
    assert chapter.startswith(prefix + escape(n['text']) + '\n')
tail = '\n'
for name in ['source-application-reading-ledger.md', 'scoped-verdict.md']:
    tail += '\\section*{' + escape(name) + '}\n' + escape((A / name).read_text()) + '\n'
tail += '\\appendix\n'
for i in [4,5,6,7,8,15,26,2,3,27,28,32,36,37,0]:
    body = data(i).decode()
    assert '\\end{Full422Data}' not in body
    tail += '\\section{ENTIRE retained DATA: ' + escape(Path(bindings[i]['path']).name) + '}\n'
    tail += '\\begin{Full422Data}\n' + body + '\n\\end{Full422Data}\n'
tail += '\\end{document}\n'
assert header + '\n'.join(chapters) + tail == source
assert len(source.encode()) == 906751 and source.count('\n') == 5030
parts = ['# Complete proof companion; unverified scoped deductions, candidate=false\n']
for n in assembled['notes']:
    parts += ['\n## New actual fields ' + n['id'] + '\n\n', json.dumps(n, ensure_ascii=False, indent=2) + '\n', '\n## New expanded TeX ' + n['id'] + '\n\n', (A / (n['id'] + '.tex')).read_text()]
for i, e in enumerate(bindings):
    parts += ['\n## ENTIRE retained incoming DATA ' + Path(e['path']).name + '\n\n', data(i).decode(), '\n']
for name in ['source-application-reading-ledger.md', 'scoped-verdict.md']:
    parts += ['\n## Current ' + name + '\n\n', (A / name).read_text()]
assert ''.join(parts) == (A / 'proof-companion.md').read_text()
primary = load(C / 'private-primary-packet-bindings.json')
assert len(primary) == 1260
qualified_primary = primary[1244:1260]
for e in qualified_primary:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
D.mkdir()
public = []
def retain(p, name=None):
    q = D / (name or p.name)
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    public.append(q)
retain(raw, 'native294-actual-FINAL-all-five-fields.json')
retain(A / 'notes.json', 'native294-assembled-notes-separate-from-actual.json')
for name in ['P12.3-marked-centres.tex','original-task.json','original-completion-criteria.txt','original-residual.md','qualified-G331.json','qualified-G331.txt','source-application-reading-ledger.md','scoped-verdict.md','diagnostics-input.json']:
    retain(A / name)
for n in actual['notes']:
    p = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(p, n)
    public.append(p)
    retain(A / (n['id'] + '.md'), 'native-assembled-' + n['id'] + '.md')
    retain(A / (n['id'] + '.tex'))
for name in ['assemble.py','diagnostics.py','verify_delivery.py','read_data.py']:
    retain(A / name, 'native-program-' + name + '.DATA.txt')
for name in ['diagnostics.json','verification.json','environment.json']:
    retain(A / 'reports' / name, 'native-report-' + name)
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now, paper=426, atom='P12.3', UNREVIEWED=True, accepted=False, original_closed=False, candidate=False,
    counts=dict(solved=16,open=26,accepted_scoped_papers=97), actual_FINAL=dict(path=str(raw),sha256=sha(raw),all_five_actual_notes_all_five_fields_physically_ROOT_read=True),
    actual_vs_assembled_note_field_comparison=differences, all_distinct_expanded_proofs_physically_ROOT_read=True,
    expanded_proof_bytes=[(A / (n['id'] + '.tex')).stat().st_size for n in assembled['notes']],
    complete_unique_current_preamble_ledger_verdict_residual_physically_ROOT_read=True,
    entire_FOUR_native_programs_physically_ROOT_read_ONLY_as_DATA=True,
    source_ROOT_passive_literal_reconstruction=True, native_companion_ROOT_passive_literal_reconstruction=True,
    inherited_entire422_and420_proof_bodies_physically_ROOT_read_previously=True,
    supplied_or_native_programs_executed_or_imported=False, incoming_correctness_grants=['ENTIRE qualified G331 ONLY'],
    full_G331_93375_bytes_physically_ROOT_read420=True, current_G331_boundary_and_density_sections_freshly_reread=True,
    G331_normal_order_bound_and_semilocal_product_exact_applications_ROOT_rejudged=True,
    inherited_fourteen_complete_primary_units_and_two_formula_images=qualified_primary, current_fresh_primary_body_or_pixel_reading_credit=0,
    primary_scope='Same fourteen entire immediate source units and two actual formula pixels previously ROOT read at normal-surface/all-support BFJ/primary-model scope. Current applications independently rejudged; native fresh reading is not ROOT fresh credit. Recursive resolution/formal-functions/Izumi/BFJ historical and whole-book audit remains qualified and OPEN.',
    complete_conditional_deductions=[
        'Every full normalization fibre joining distinct marked normal centres obstructs greatest C/D minorants, including domain semilocal normalization. Actual CRT conductor multipliers and all-curve-positive primary competitors prove every-degree uniform gap and stable signed failure.',
        'Irreducible self-crossing over every char!=2 field in dimensions>=2, and excellent DVR surfaces with2 invertible: exact raw envelope, every-degree canonical ideals, exact error ceil(3m/2)/m-1>=1/2 and non-FG. No normal failure asserted.',
        'For every continuous signed obstacle on the irreducible self-crossing surface, greatest C/D existence iff two normal-envelope conductor values agree, with positive primary truncation and full-fibre descent.',
        'Pinch normalization, conductor, exact same-centre two-point fibre in char!=2, arbitrary-field pinch-surface CE and characteristic2 radicial boundary transport.',
        'Uniform normal-centre divisorial coercivity bounds every raw negative envelope away fromzero without proving continuity/attainment. Distinct-centre CRT method cannot simply transfer to one centre.'],
    compatibility_with_independent_ROOT425='ROOT425 was proved and retained before any294 mathematics inspection, and was never hot-fed. Its same-centre conductor-power failure does not contradict n4: its chosen divisorial comparison constant depends on deep weightL, and n4 forbids only a plateau under D>K_nu. Read425 separately, without treating native294 remaining-open annotations as current classification.',
    residual=['General excellent NORMAL dimension>=3 envelope regularity or qualifying normal failure remains OPEN.','General same-centre nonsingleton-fibre classification and full recursive original audit remain OPEN. Independent425 resolves its explicit conductor-power family only.'],
    native_finite_observations_NOT_mathematical_certification=load(A / 'reports/diagnostics.json'),
    native_verification_report_is_DATA_not_new_acceptance=True, compiler='NOT_YET_INVOKED_FOR426',
    native295_ACTIVE_math_NOT_read_or_supplied=True, hot_feedback=False,
    primary_literal_bodies_pixels_books_LOCALONLY=True, protected_editor_OPEN_UNCHANGED=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp, scope)
public.append(sp)
rootparts = [b'WHOLE ROOT426 proof packet. UNREVIEWED; original P12.3 OPEN. Retention gives no new reading/correctness credit.\n']
for p in public:
    rootparts += [f'\n===== WHOLE CURRENT PUBLIC COMPONENT {p.name} =====\n'.encode(), p.read_bytes()]
retained = []
for i, e in sorted(enumerate(bindings), key=lambda pair: pair[1]['bytes'], reverse=True):
    b = data(i)
    present = any(b in part for part in rootparts)
    if not present:
        rootparts += [f'\n===== WHOLE SUPPLIED INERT MATHEMATICAL DATA {i}: {Path(e["path"]).name} =====\n'.encode(), b]
    retained.append(dict(index=i,bytes=len(b),sha256=e['sha256'],whole_body_retained=True,embedded_in_existing_whole_component=present,fresh_reading_credit=0))
comp = D / 'proof-companion.txt'
comp.write_bytes(b'\n'.join(rootparts))
whole = comp.read_bytes()
assert all(data(i) in whole for i in range(len(bindings)))
public.append(comp)
cp = D / 'ROOT-whole-companion-containment-ledger.json'
write(cp, dict(storage_only_NOT_reading_or_correctness_credit=True,records=retained,native_whole_companion_retained_LOCALONLY=dict(path=str(A / 'proof-companion.md'),bytes=(A / 'proof-companion.md').stat().st_size,sha256=sha(A / 'proof-companion.md'),exact_literal_reconstruction_checked=True)))
public.append(cp)
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B, dict(recorded_utc=now,paper=426,whole_source=dict(path=str(D / 'P12.3-marked-centres.tex'),bytes=len(source.encode()),sha256=sha(D / 'P12.3-marked-centres.tex')),whole_companion=dict(path=str(comp),bytes=comp.stat().st_size,sha256=sha(comp)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler='NOT_YET_INVOKED_FOR426',counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now,ROOT426_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='Whole actual294 and every distinct expansion read; ROOT426 passively reconstructed at precise full G331 qualifications. Invoke native desktop compiler, freeze small296 on WHOLE425426 toward same-centre/general-normal residual. Native295 isolated active, no hot feedback. Publish NONFORCE306, counts/editor unchanged.')
    write(p, y)
print(json.dumps(dict(paper=426,source_bytes=len(source.encode()),source_LF=source.count('\n'),companion_bytes=comp.stat().st_size,public_files=len(public)+1,actual_vs_assembled=differences,every_43_incoming_math_body_retained_whole=True,accepted=False,original_closed=False,binding=str(B)),indent=2))
