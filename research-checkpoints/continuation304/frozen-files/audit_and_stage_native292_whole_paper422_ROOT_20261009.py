"""ROOT passive exact-source retention. Distinct final/assembled notes are kept distinct."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-292/P12.3-whole419-nonsingleton-conductor-and-normal-envelope-residual'
A = C / 'artifacts/codex-e1qB9F'
D = K / 'public-P12.3-continuation422-cross-component-obstructions-and-exact-surface-gluing-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
raw = K / 'round292-raw-native-actual-FINAL.json'
assert sha(raw) == '3af45446009c52dc1aef8039b36dee440db8935bd49f1fd2c4f5e34c29da2a9f'
x = load(raw)
assembled = load(A / 'notes.json')
assert not x['candidate'] and not assembled['candidate'] and len(x['notes']) == len(assembled['notes']) == 5
assert not D.exists()
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json', 'checklist-current.json']:
    y = load(R / name)
    assert y['current_active_batch'] == [293] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation'] == 303
    assert len(y['fully_solved_original_atoms']) == 16 and y['remaining_open_original_atoms'] == 26 and y['historical_reviewed_scoped_papers'] == 97
for out in [x, assembled]:
    known = {'G331'}
    for n in out['notes']:
        assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'} and set(n['support']) <= known
        known.add(n['id'])
differences = [dict(id=n['id'], distinct_fields=[k for k in n if n[k] != a[k]]) for n,a in zip(x['notes'], assembled['notes'])]
assert [n['id'] for n in x['notes']] == [n['id'] for n in assembled['notes']]
rows = load(C / 'mathematical-packet-bindings.json')
literal = lambda i: Path(rows[i]['path']).read_text()
for e in rows:
    assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
grant = load(A / 'qualified-G331.json')
assert grant == load(C / 'input.json')['notes'][0] and grant['id'] == 'G331'
assert (A / 'qualified-G331.txt').read_text() == grant['text'] == literal(32)
assert (A / 'original-residual.md').read_text() == literal(28)
assert (A / 'original-task.json').read_text() == literal(1)
old = K / 'public-P12.3-continuation419-conductor-descent-cusp-envelopes-and-threefold-obstruction-unreviewed'
assert literal(0) == (old / 'P12.3-conductor-and-threefold.tex').read_text()
assert literal(30) == (old / 'proof-companion.md').read_text()
def escape(t):
    mp = {'\\':r'\textbackslash{}','{':r'\{','}':r'\}','$':r'\$','&':r'\&','%':r'\%','#':r'\#','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}','<':r'\textless{}','>':r'\textgreater{}'}
    return ''.join(mp.get(c,c) for c in t)
source = (A / 'P12.3-nonsingleton-conductor.tex').read_text()
header = source.split('\\section{n1.',1)[0]
assert header.endswith('\\tableofcontents\n') and len(header.splitlines()) == 57
chapters = []
for n in assembled['notes']:
    assert (A / (n['id'] + '.md')).read_text().strip() == n['text']
    body = (A / (n['id'] + '.tex')).read_text()
    prefix = '\\section{' + escape(n['id'] + '. ' + n['summary']) + '}\n\\textit{Supports: ' + escape(', '.join(n['support'])) + '.}\n\n' + escape(n['text']) + '\n'
    assert body.startswith(prefix) and body[len(prefix):].startswith('\n\\subsection*{')
    chapters.append(body)
ledger = (A / 'source-application-reading-ledger.md').read_text()
verdict = (A / 'scoped-verdict.md').read_text()
tail = '\n\\section*{Source, application and reading ledger}\n' + escape(ledger)
tail += '\n\\section*{Scoped verdict}\n' + escape(verdict)
tail += '\n\\section*{Byte-unchanged original residual as DATA}\n' + escape(literal(28))
tail += '\n\\appendix\n\\section{ENTIRE qualified G331, all annotations}\n\\begin{FullQualifiedGrantData}\n' + literal(32) + '\n\\end{FullQualifiedGrantData}\n'
tail += '\\section{ENTIRE current419 source, literal inert DATA}\n\\begin{Full419Data}\n' + literal(0) + '\n\\end{Full419Data}\n\\end{document}\n'
assert source == header + '\n'.join(chapters) + tail
parts = ['# ENTIRE proof companion: unverified scoped progress, candidate=false\n']
for n in assembled['notes']:
    parts += ['\n## New actual FINAL fields ' + n['id'] + '\n', json.dumps(n, ensure_ascii=False, indent=2) + '\n', '\n## New distinct expanded TeX ' + n['id'] + '\n', (A / (n['id'] + '.tex')).read_text()]
for i in [4,5,6,7,8,10,11,12,13,14,1,2,3,31,32,34,35,27,28,0,30]:
    parts += ['\n## ENTIRE incoming DATA ' + Path(rows[i]['path']).name + '\n\n', literal(i), '\n']
for name in ['source-application-reading-ledger.md','scoped-verdict.md']:
    parts += ['\n## New ' + name + '\n\n', (A / name).read_text(), '\n']
assert (A / 'proof-companion.md').read_text() == ''.join(parts)
prior = load(old / 'ROOT-whole-proof-source-application-scope-and-residual.json')
for e in prior['inherited_surface_and_SH_BFJ_immediate_primary_units_bound_whole']:
    assert sha(e['path']) == e['sha256']
D.mkdir()
public = []
def retain(p, name=None):
    q = D / (name or p.name)
    shutil.copyfile(p, q)
    assert sha(p) == sha(q)
    public.append(q)
retain(raw,'native292-ACTUAL-SETTLED-FINAL-all-five-fields.json')
retain(K / 'round292-terminal-actual-final-ROOT-retention-20261009.json')
retain(C / 'original-task.json','ROOT-unchanged-original-task.json')
for name in ['P12.3-nonsingleton-conductor.tex','notes.json','source-application-reading-ledger.md','scoped-verdict.md','original-residual.md','original-task.json','original-completion-criteria.txt','qualified-G331.json','qualified-G331.txt','diagnostics-input.json']:
    retain(A / name,'native-assembled-notes-DISTINCT-from-actual-FINAL.json' if name=='notes.json' else name)
for n in x['notes']:
    q = D / ('actual-' + n['id'] + '-all-five-fields.json')
    write(q,n)
    public.append(q)
    retain(A / (n['id'] + '.tex'))
for name in ['deliver.py','diagnostics.py','check_delivery.py']:
    retain(A / name,'native-program-' + name + '.DATA.txt')
for name in ['diagnostics.json','environment.json','observed-commands.json','check-delivery.json','retention.json','input-hashes.json','own-hashes.json']:
    retain(A / 'reports' / name,'native-reported-' + name)
now = datetime.now(timezone.utc).isoformat()
scope = dict(recorded_utc=now,paper=422,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),actual_FINAL=dict(path=str(raw),sha256=sha(raw),all_five_actual_fields_of_all_five_notes_physically_ROOT_read=True),native_assembled_notes_DIFFER_FROM_actual_FINAL=any(e['distinct_fields'] for e in differences),distinct_actual_and_assembled_fields=differences,all_distinct_actual_and_expanded_current_proofs_physically_ROOT_read_and_REJUDGED=True,complete_57_LF_unique_preamble_abstract_and_unique_ledger_verdict_residual_read=True,all_three_native_programs_physically_ROOT_read_ONLY_as_DATA=True,supplied_or_native_programs_executed_or_imported=False,whole_source_and_native_companion_exact_ROOT_literal_reconstruction=True,sole_correctness_grant='ENTIRE qualified G331; full mandatory model/support/source/audit annotation retained. ENTIRE93375-byte body freshly ROOT read420; exact normal-order-bound and all-support density/zero-dichotomy applications freshly reread/rejudged422, no recursive historical audit credit.',prior_fourteen_complete_immediate_surface_SH_BFJ_units_and_two_formula_pixels=prior['inherited_surface_and_SH_BFJ_immediate_primary_units_bound_whole'],current_fresh_primary_reading_credit=0,current_application_scope=['G331 normal-domain divisorial bound applies to excellent NORMAL local centres in finite normalization, hence analytically irreducible; never applied to nonnormal R. Units handled separately; primary ideal values finite on every support.', 'G331 all-support divisorial density supplies dense generic-support loci and convergent NETS; no metrizability/countable extraction or omitted infinite-conductor supports.', 'Surface CE retained at exact excellent normal local DOMAIN dimensionTWO arbitrary equal/mixed characteristic, with disclosed deeper resolution/completion/gluing foundations; higher-dimensional source CE not inferred.', 'Conductor idempotent separation uses actual regular conductor element and S-ideal property. Exact positive surface/DVR gluing uses actual primary truncation, cone operations and full-fibre positive descent; finite arithmetic is not proof.', 'Native program/ledger metadata initial combined display truncated; both diagnostics/checker reread completely in bounded untruncated output. Unique source scopes fully read separately.'],complete_new_scoped_deductions=['Signed primary-model obstacle on crossing surface: exact canonical every-degree gap1/2, no greatest C/D minorant, non-USC, non-FG and open neighbourhood of failures.', 'Any cross-minimal-component normalization fibre gives signed primary-model obstruction, hence every positive-dimensional intersection of distinct minimal components obstructs universal CE, in every dimension/characteristic/residue field.', 'Exact raw envelope and greatest-minorant criterion for qualified regular surface branches glued along a marked DVR: all source-envelope conductor values must agree; primary truncation proves actual positive gluing.', 'Mixed-characteristic crossing failures and every-dimensional field crossing formulas on ALL supports.', 'Excellent reduced local dimension<=TWO with normal component rings: universal CE iff all pairwise component intersections are zero-dimensional.'],residual=['General excellent NORMAL dimension>=3 CE/qualifying failure and higher-dimensional positive/mixed-characteristic source CE OPEN.', 'Irreducible nonnormal nonsingleton normalization fibres and unrestricted higher-dimensional conductor compatibility remain OPEN.', 'Complete inherited/deeper recursive source/book audit remains qualified and incomplete; original closure and acceptance unchanged.'],compiler='NOT_YET_INVOKED_FOR422',active_native293_mathematics_NOT_read_or_supplied=True,hot_feedback=False,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
sp = D / 'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp,scope)
public.append(sp)
comp = D / 'proof-companion.md'
comp.write_text('# ENTIRE ROOT422 UNREVIEWED packet; original P12.3 OPEN.\n\n## ACTUAL settled FINAL, distinct from assembled note fields\n\n' + raw.read_text() + '\n\n## ENTIRE native companion with assembled fields and whole inherited DATA; exact ROOT reconstruction checked\n\n' + (A / 'proof-companion.md').read_text() + '\n\n## ENTIRE ROOT exact application and residual\n\n' + sp.read_text())
public.append(comp)
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=422,whole_source=dict(path=str(D / 'P12.3-nonsingleton-conductor.tex'),bytes=(D / 'P12.3-nonsingleton-conductor.tex').stat().st_size,sha256=sha(D / 'P12.3-nonsingleton-conductor.tex')),whole_companion=dict(path=str(comp),bytes=comp.stat().st_size,sha256=sha(comp)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler='NOT_YET_INVOKED_FOR422',counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p = R / name
    y = load(p)
    y.update(updated_utc=now,ROOT422_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='Whole ROOT422 actual/formal notes read and exact source/native companion reconstructed; distinct final/assembled fields preserved explicitly. Request compiler; freeze next P12.3 batch on irreducible conductor/normal higherdim residual. Native293 remains isolated on existence. Publish regular NONFORCE304 when concrete new batch ready; counts/editor unchanged.')
    write(p,y)
print(json.dumps(dict(paper=422,source_bytes=len(source.encode()),companion_bytes=comp.stat().st_size,public_files=len(public)+1,actual_and_assembled_DIFFER=True,literal_reconstruction=True,accepted=False,original_closed=False,binding=str(B)),indent=2))
