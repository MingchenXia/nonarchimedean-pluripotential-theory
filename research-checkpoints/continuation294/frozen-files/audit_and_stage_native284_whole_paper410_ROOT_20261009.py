from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, shutil

R = Path('/workspace/research'); K = R / 'root-checks'
C = R / 'campaigns/round-284/P12.3-whole408-canonical-filtration-and-general-envelope-residual'
A = C / 'artifacts/codex-mbPlj4'
D = K / 'public-P12.3-continuation410-finite-smooth-quotient-continuous-envelopes-unreviewed'
OLD = K / 'public-P12.3-continuation408-canonical-obstacle-filtration-and-finite-generation-envelopes-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
write = lambda p, x: Path(p).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
assert not D.exists()
raw = load(K / 'round284-raw-native-actual-FINAL.json')
expanded = load(A / 'notes.json'); incoming = load(C / 'input.json')
assert incoming == load(A / 'input.json') and len(incoming['notes']) == 1
assert incoming['notes'][0]['id'] == 'G331'
assert raw['candidate'] is expanded['candidate'] is False and len(raw['notes']) == 4
assert len(expanded['notes']) == 4
known = {'G331'}; pairs = []
for a, e in zip(raw['notes'], expanded['notes']):
    assert set(a) == set(e) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
    assert a == e and set(a['support']) <= known
    assert (A / ('final-' + a['id'] + '.txt')).read_text() == a['text']
    assert (A / (a['id'] + '.md')).read_text() == a['text']
    known.add(a['id'])
    t = A / (a['id'] + '.tex')
    pairs.append(dict(id=a['id'],actual_five_fields_ROOT_physically_read=True,
        distinct_expanded_TeX_ROOT_physically_read=True,actual_text_bytes=len(a['text'].encode()),
        expanded_TeX_bytes=t.stat().st_size,expanded_TeX_sha256=sha(t),
        actual_and_expanded_TeX_NOT_claimed_identical=True))
task = incoming['task']; assert task == load(A / 'original-task.json')
assert (A / 'original-problem.txt').read_text() == task['problem']
assert (A / 'original-completion-criteria.txt').read_text() == task['completionCriteria']
for x, y in [('000-P12.3-obstacle-filtration.tex','P12.3-obstacle-filtration.tex'),
    ('011-proof-companion.md','proof-companion.md'),('010-original-residual.md','original-residual.md')]:
    assert (A / 'retained' / x).read_bytes() == (OLD / y).read_bytes()
assert (A / 'original-residual.md').read_bytes() == (OLD / 'original-residual.md').read_bytes()
assert load(A / 'retained/012-raw-native-actual-FINAL.json') == load(OLD / 'raw-native-actual-FINAL.json')
assert load(A / 'retained/009-notes.json') == load(OLD / 'notes.json')
grant = incoming['notes'][0]['text']
assert (A / 'retained/G331-qualified.txt').read_text() == grant and len(grant.encode()) == 93375
# Read native source as DATA and extract one literal preamble by inert syntax inspection only.
values = []
for node in ast.walk(ast.parse((A / 'build_delivery.py').read_text())):
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'preamble' for t in node.targets):
        assert isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
        values.append(node.value.value)
assert len(values) == 1
bodies = '\n\n'.join((A / f'n{i}.tex').read_text() for i in range(1,5))
def retained(title, content):
    assert '\\end{RetainedDATA}' not in content
    return '\n\\section*{' + title + '}\n\\begin{RetainedDATA}\n' + content + '\n\\end{RetainedDATA}\n'
paper = values[0] + bodies
for title, fn in [('Entire source/application/reading ledger','source-application-reading-ledger.md'),
    ('Scoped verdict','scoped-verdict.md'),('Unchanged incoming original residual','original-residual.md')]:
    paper += retained(title, (A / fn).read_text())
paper += retained('ENTIRE qualified G331: all source, annotation, ledger and scope', grant)
paper += retained('Exact unchanged original task DATA (JSON Unicode escapes)', json.dumps(task, ensure_ascii=True, indent=2))
paper += retained('Actual current408 FINAL DATA; distinct from expansions',(A / 'retained/012-raw-native-actual-FINAL.json').read_text())
paper += retained('Expanded current408 FINAL DATA',(A / 'retained/009-notes.json').read_text())
paper += '\n\\end{document}\n'
assert paper == (A / 'P12.3-quotient-envelopes.tex').read_text()
companion = '# ENTIRE own proof companion; historical and primary DATA are LOCALONLY\n\nAll own proofs follow without omitted steps. G331 alone is an incoming correctness grant with every qualification. Retention of the inherited full source does not mean a fresh whole historical audit.\n\n'
companion += '\n\n'.join(n['text'] for n in expanded['notes'])
companion += '\n\n# ENTIRE distinct own expanded TeX proofs\n\n' + bodies
for title, content in [('ENTIRE own source/application/reading ledger',(A / 'source-application-reading-ledger.md').read_text()),
    ('ENTIRE own scoped verdict',(A / 'scoped-verdict.md').read_text()),
    ('ENTIRE unchanged original residual',(A / 'original-residual.md').read_text()),
    ('ENTIRE literal qualified G331',grant),('ENTIRE exact unchanged original task DATA',(A / 'original-task.json').read_text()),
    ('ENTIRE actual current408 FINAL DATA',(A / 'retained/012-raw-native-actual-FINAL.json').read_text()),
    ('ENTIRE expanded current408 FINAL DATA',(A / 'retained/009-notes.json').read_text()),
    ('ENTIRE retained current408 companion DATA; inherited audit incomplete',(A / 'retained/011-proof-companion.md').read_text()),
    ('ENTIRE retained current408 standalone DATA; inherited audit incomplete',(A / 'retained/000-P12.3-obstacle-filtration.tex').read_text())]:
    companion += '\n\n# ' + title + '\n\n' + content
assert companion == (A / 'proof-companion.md').read_text()
captured = load(K / 'round284-terminal-actual-final-ROOT-retention-20261009.json')
assert captured['public_status']['status'] == 'completed' and captured['public_status']['calls']['unsettled'] == 0
assert captured['campaign_result']['candidate'] is False
tails = []
for a, c in zip(raw['notes'], captured['campaign_result']['notes']):
    assert all(a[k] == c[k] for k in ['id','summary','detailedSummary','support']) and c['text'].startswith(a['text'])
    tails.append(dict(id=a['id'],tail=c['text'][len(a['text']):]))
for name in ['active-work.json','checklist-current.json']:
    x = load(R / name)
    assert x['github_pending_checkpoint'] is None and x['current_active_batch'] == [285]
    assert x['latest_verified_github_checkpoint']['continuation'] == 293
    assert len(x['fully_solved_original_atoms']) == 16 and x['remaining_open_original_atoms'] == 26 and x['historical_reviewed_scoped_papers'] == 97
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
S = R / 'campaigns/round-232/P12.2-original-excellent-singular-geometric-cone-and-model-nef-comparison/frozen-primary-data-LOCALONLY/BFJ-valuations-psh.txt'
assert S.read_bytes() == (A / 'LOCALONLY/BFJ-valuations-psh.txt').read_bytes()
U = R / 'primary-data-LOCALONLY/P12.3-ROOT410-smooth-envelope-estimate-source-20261009'
assert not U.exists(); U.mkdir(); lines = S.read_bytes().split(b'\n'); units = []
for label, lo, hi in [('BFJ-setting-and-modification-domain',346,389),('BFJ-simple-modification-domain',583,615),
    ('BFJ-1.10-1.15-whole-immediate-chain',686,837),('BFJ-2.1-2.8-whole-immediate-chain',849,1019),
    ('BFJ-3.1-3.14-whole-immediate-chain',1020,1233),('BFJ-3.15-3.25-whole-model-envelope-and-immediate-proofs',1234,1413)]:
    p = U / (label + '.txt'); p.write_bytes(b'\n'.join(lines[lo-1:hi]) + b'\n')
    units.append(dict(carrier=str(S),carrier_sha256=sha(S),real_LF=[lo,hi],unit=str(p),bytes=p.stat().st_size,
        sha256=sha(p),ROOT_immediate_applied_bodies_physically_read=True,irrelevant_partial_neighbor_units_NOT_claimed_applied=True,LOCALONLY=True))
programs = [A / x for x in ['build_delivery.py','reconstruct.py','record_sources.py','verify_delivery.py','finite_diagnostic.py']]
now = datetime.now(timezone.utc).isoformat(); D.mkdir()
for fn in ['P12.3-quotient-envelopes.tex','proof-companion.md','notes.json','source-application-reading-ledger.md','scoped-verdict.md','original-residual.md']:
    shutil.copyfile(A / fn, D / fn)
for i in range(1,5):
    for pattern in ['final-n{}.txt','n{}.tex']:
        fn = pattern.format(i); shutil.copyfile(A / fn,D / fn)
shutil.copyfile(K / 'round284-raw-native-actual-FINAL.json', D / 'raw-native-actual-FINAL.json')
shutil.copyfile(K / 'round284-terminal-actual-final-ROOT-retention-20261009.json',D / 'terminal-actual-FINAL-retention.json')
audit = dict(recorded_utc=now,paper=410,round=284,UNREVIEWED=True,accepted=False,original_closed=False,
    actual_expanded_pairs=pairs,all_current_unique_proofs_preamble_ledger_verdict_residual_physically_read=True,
    whole_standalone_and_companion_component_identity=True,whole_repeated_historical_material_NOT_a_fresh_recursive_audit=True,
    incoming_correctness_grants=['ENTIRE qualified G331 only; all mandatory qualifications retained'],
    ROOT_fresh_primary_units=units,ROOT_previously_read_complete_SH_units_reused_without_extra_independent_reading_credit=True,
    historical_native_reading_claims_NOT_ROOT_fresh_reading_receipts=True,
    native_programs_physically_read_as_DATA=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in programs],
    native_or_supplied_programs_executed_or_imported=False,terminal_tails=tails,
    new_ROOT_mathematical_reconstruction=['Canonical all-index ideals and raw full-support envelope, with exact finite-generation equivalence at its stated scope',
        'Weak nef envelope bounded by a constant; BFJ closed-simplex continuity and all-retraction extension identify the full raw geometric envelope',
        'Complete BFJ3.18 inequality at t=m+C gives (1+C/m)W<=W_m<=W and all-support uniform CM/m without finite generation',
        'Exact primary contraction includes nonminimal supports via (g)+m^N; fixed-complex thinness only',
        'Uniform signed-model obstacle density and raw Lipschitz stability give all continuous obstacles on the exact smooth published domain',
        'Finite-group fixed-field proof plus qualified G331 full-support trace identify EVERY restriction fibre with a full group orbit',
        'Invariant envelope positive full-fibre descent; norm coefficient ideals, canonical contraction and residue degrees give full downstairs O(1/k)',
        'Actual normal nonisolated A1-product local invariant ring and two valuations verify signed nonlinear cancellation example'],
    named_deeper_foundations_not_recursively_reproved=['Hironaka smooth principalization at the exact algebraically closed characteristic-zero smooth affine CLOSED germ domain',
        'Multiplier-ideal subadditivity and smooth Izumi/thinness inputs in BFJ with their disclosed external references',
        'Excellent/Nagata finite normalization and previously qualified SH and geometric G331 foundations'],
    unresolved=['Arbitrary normal nonisolated excellent germs beyond finite smooth quotient covers',
        'Imperfect residue fields and mixed-characteristic higher-dimensional arbitrary continuous obstacles',
        'Qualifying normal continuous-obstacle counterexample or complete general regularity theorem',
        'Complete fresh inherited historical405/401/392/B341/E350 recursive primary audit'],
    compiler_pending=True,primary_bodies_pixels_books_LOCALONLY=True,
    counts=dict(solved=16,open=26,accepted_scoped_papers=97),protected_editor_OPEN_UNCHANGED=True)
write(D / 'ROOT-whole-serialization-source-application-and-scope-audit.json',audit)
(D / 'ROOT-review-scope.md').write_text('Whole working paper410, UNREVIEWED; original P12.3 remains OPEN. All four actual FINALs including ALL five fields and all four distinct expanded TeX proofs, full unique ledger/verdict/residual and preamble were ROOT physically read. Full standalone and companion components were reconstructed exactly; historical duplicate retention does not establish a fresh historical recursive audit. Native programs were physically read only as DATA and NEVER executed/imported.\n\nThe new proof establishes continuous independently geometric envelopes for every continuous signed obstacle on finite invariant quotients of smooth affine CLOSED germs over an algebraically closed characteristic-zero field, relative to the ENTIRE qualified G331 and exact BFJ immediate units. Fixed signed model obstacles have a full canonical degree O(1/m) estimate without finite generation. All semivaluation supports and EVERY fibre are retained. Actual normal nonisolated A1-product germs are included. General excellent/mixed/imperfect scope remains unresolved. Fresh complete applied BFJ units were ROOT read; deeper principalization, multiplier and Izumi inputs remain named conventional foundations. No original closure or new independent acceptance is claimed. Compiler pending. Counts16solved26OPEN97accepted unchanged. Primary bodies/pixels/books LOCALONLY; protected P16.4 editor OPEN UNCHANGED.\n')
B = D / 'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=410,round=284,whole_paper=dict(path=str(D / 'P12.3-quotient-envelopes.tex'),bytes=len(paper.encode()),sha256=sha(D / 'P12.3-quotient-envelopes.tex')),
    public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.iterdir()) if p.is_file()],
    UNREVIEWED=True,accepted=False,original_closed=False,compiler=dict(kind='pending'),counts=audit['counts'],primary_bodies_not_published=True,protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p = R / name; x = load(p)
    x.update(updated_utc=now,native284_whole_unreviewed_paper410=dict(directory=str(D),binding=str(B),sha256=sha(B)),
        next_work='Compile whole410, freeze286 original general P12.3 residual with whole410 and sole fullG331; native285 continues P16.7. Verify regular NONFORCE294, at mostTWO native campaigns, no hot feedback; counts and protected editor unchanged.')
    write(p,x)
print(json.dumps(dict(paper=410,directory=str(D),whole_source_bytes=len(paper.encode()),whole_source_sha256=sha(D / 'P12.3-quotient-envelopes.tex'),
    whole_companion_bytes=len(companion.encode()),primary_units=len(units),terminal_tails=tails,compiler='pending',original_closed=False),ensure_ascii=False,indent=2))
