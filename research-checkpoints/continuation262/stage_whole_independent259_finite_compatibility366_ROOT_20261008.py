from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-259/P12.6-entire-original-candidate362-independent-proof-source-and-scope-review'
A = C / 'artifacts/codex-hd6syC'
D = K / 'public-P12.6-continuation366-whole-original-finite-map-compatibility-after-independent259'
B = K / 'P12.6-round259-whole-original366-ROOT-proof-source-scope-and-binding-20261008.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
def bind(p):
    p = Path(p)
    return dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p))
def write(p, x):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

assert not D.exists() and not B.exists()
protected = K / 'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(protected) == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f = load(C / 'freeze.json')
for name in ['task.json', 'original-task.json', 'input.json', 'settings.json',
             'mathematical-packet-bindings.json', 'book-context-bindings.json',
             'private-primary-packet-bindings.json', 'qualified-imported-note-bindings.json']:
    assert sha(C / name) == f[name.replace('.json', '').replace('-', '_') + '_sha256']
counts = {}
for name in ['mathematical-packet-bindings.json', 'book-context-bindings.json', 'private-primary-packet-bindings.json']:
    entries = load(C / name)
    for e in entries:
        p = Path(e['path'])
        assert sha(p) == e['sha256'] and p.stat().st_size == e['bytes'], str(p)
    counts[name] = len(entries)
audit = load(A / 'evidence/final-audit.json')
for e in audit['own_files']:
    p = A / e['file']
    assert sha(p) == e['sha256'] and p.stat().st_size == e['bytes'], str(p)
counts['native_owned_files'] = len(audit['own_files'])
actual = K / 'round259-actual-native-final.json'
assert sha(actual) == '59e6846887e4a4d439d30ec42faf9a2114441661a35e8f1ce6c2d9a42ec84373'
x, expanded = load(actual), load(A / 'native-notes.json')
assert x == expanded == load(A / 'actual-FINAL.json')
assert x['candidate'] is True and len(x['notes']) == 10
assert actual.read_bytes() != (A / 'actual-FINAL.json').read_bytes()
proof = (A / 'whole-proof.md').read_text()
assert proof == '\n\n'.join(n['text'] for n in expanded['notes'])
paper = (A / 'P12.6-review-paper.tex').read_bytes()
assert len(paper) == 356105 and sha(A / 'P12.6-review-paper.tex') == '494e6bbf24575e98e7da47db95fa6b417b3a544b80fde46ae82de42f28b94048'
mat = load(C / 'mathematical-packet-bindings.json')
grants = list(sorted((A / 'qualified-grants').iterdir()))
assert len(grants) == 14
for p in grants:
    assert any(sha(p) == e['sha256'] and p.stat().st_size == e['bytes'] for e in mat[:14])
    assert p.read_bytes() in paper
remaining = paper
for p in sorted(grants, key=lambda p: p.stat().st_size, reverse=True):
    assert p.read_bytes() in remaining
    remaining = remaining.replace(p.read_bytes(), b'', 1)
fields = []
allowed = {'G331', 'G345'}
for n in expanded['notes']:
    p = A / 'sections' / (n['id'] + '.md')
    assert n['text'] == p.read_text() and p.read_bytes() in remaining
    assert set(n['support']) <= allowed
    allowed.add(n['id'])
    remaining = remaining.replace(p.read_bytes(), b'', 1)
    fields.append(dict(id=n['id'], all_actual_and_expanded_fields_equal=True,
                       entire_section_in_proof_and_paper=True, support=n['support']))
for name in ['whole-source-application-ledger.md', 'whole-proof-coverage.md', 'exact-scope.md',
             'original-scope-and-noncircularity-decision.md']:
    b = (A / name).read_bytes()
    assert b in remaining
    remaining = remaining.replace(b, b'', 1)
decision = load(A / 'acceptance-decision.json')
assert decision['verdict'] == 'WHOLE_ORIGINAL_PASS_WITH_MANDATORY_QUALIFICATIONS'
assert decision['mathematical_gaps'] == [] and not decision['external_acceptance_performed']
assert (C / 'original-task.json').stat().st_size == 17641
assert sha(C / 'original-task.json') == '5dec90e839c4ca9ba081f3bfc8ef4774c433c18f47ffb4a8833b708fd8a1d3ae'
for name in ['active-work.json', 'checklist-current.json']:
    z = load(R / name)
    assert len(z['fully_solved_original_atoms']) == 15 and z['remaining_open_original_atoms'] == 27
    assert z['historical_reviewed_scoped_papers'] == 96 and z['github_pending_checkpoint'] is None
    assert z['current_active_batch'] == [260]

D.mkdir()
for p in A.iterdir():
    if p.is_file() and p.suffix in ['.md', '.json', '.tex'] and p.name != 'actual-FINAL.json':
        shutil.copyfile(p, D / p.name)
for folder in ['sections', 'qualified-grants', 'evidence']:
    shutil.copytree(A / folder, D / folder)
inert = D / 'owned-native-programs-INERT-DATA'
inert.mkdir()
for p in A.glob('*.py'):
    shutil.copyfile(p, inert / p.name)
shutil.copyfile(actual, D / 'actual-native259-final.json')
shutil.copyfile(A / 'actual-FINAL.json', D / 'native-local-actual-FINAL-serialization-DATA.json')
shutil.copyfile(C / 'original-task.json', D / 'original-task.json')
(D / 'ROOT-new-paper-fresh-header-bridges-footer.tex').write_bytes(remaining)
now = datetime.now(timezone.utc).isoformat()
record = dict(recorded_utc=now, atom='P12.6', continuation=366, review_round=259,
    status='Entire independently reconstructed original candidate; ROOT fresh paper bridges pending reading, no acceptance yet',
    paper=bind(D / 'P12.6-review-paper.tex'), whole_proof=bind(D / 'whole-proof.md'),
    actual_FINAL=bind(D / 'actual-native259-final.json'), original_task=bind(D / 'original-task.json'),
    source_ledger=bind(D / 'whole-source-application-ledger.md'), fields=fields, verified_binding_counts=counts,
    ROOT_whole_reading='Whole46155-byteproof physically read0:16200/15700:31600/31100:end with overlap; every actualFINAL field n1-3/n4-7/n8-10 physically read. All10expanded fields exact same as actual, allnontext fields read separately; whole9864ledger/3451scope/3356coverage/3369originalscope/1445decision/572sourceJSON read. Original17641 bytes reread0:9600/9100:end to repair outer combined truncation.',
    current259_actual_qualification='All10actual note fields exactly equal current259 expanded/local pair; only JSON serialization differs in byte count/hash. This is DISTINCT from historical256, where all10 actual proof texts differed from expanded sections. Both actual outputs independently preserved.',
    new_ROOT_source_reading='Full BFJ3.15-3.22 statements and complete3.18 proof physically freshly read at exact closed smooth affine algclosedchar0 scope; setting confirmation pending. Other immediate original256 source readings retained, independent259 new entire source applications attributed to native reviewer; no fabricated new ROOT source-pixel reading.',
    only_grants=['ENTIRE qualified G331', 'ENTIRE qualified G345'],
    mathematical_verdict='Whole mathematical argument and exact original scope currently pass ROOT reading; final actual-paper bridge/source-setting checks pending',
    mandatory_scopes=['Actual primary geometry BEFORE ideal comparisons', 'All supports and full conductor fibres',
        'Reduced generic degree and Artinian supported thickness distinguished', 'Bounded prescribed-D-limit nets only',
        'Current SH17.4.7 finite quotient correction', 'Exact closed smooth affine algclosedchar0 BFJ scope',
        'One arbitrary source slot; full admissibility and both intermediate tower admissibilities',
        'Independent source gauge division and exactly one measure factor',
        'General positive-envelope existence P12.3 remains separate and OPEN'],
    fresh_paper_bridges=bind(D / 'ROOT-new-paper-fresh-header-bridges-footer.tex'),
    entire14qualified_grants_literal=True, supplied_programs_executed_or_imported=False,
    source_bodies_pixels_LOCALONLY=True, original_closed=False, accepted_paper=False,
    compiler_verified=False, protected_editor_open_unchanged=True)
write(B, record)
write(D / 'mandatory-ROOT-source-scope-and-actual-output-qualification-before-acceptance-20261008.json', record)
assert sha(protected) == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(directory=str(D), paper=record['paper'], whole_proof=record['whole_proof'],
    fresh_bridge_bytes=len(remaining), fields_all_equal=True, counts=counts, acceptance=False), indent=2))
