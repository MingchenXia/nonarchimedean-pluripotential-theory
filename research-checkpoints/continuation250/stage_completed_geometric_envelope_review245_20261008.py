from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = next((R / 'campaigns/round-245').iterdir())
A = C / 'artifacts/codex-xaNUnj'
D = K / 'public-P12.3-continuation340-exact-conductor-envelope-criterion'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
def save(p, x):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
def verify(entries):
    for e in entries:
        p = Path(e['path'])
        if not p.is_absolute():
            p = A / p
        assert p.is_file() and p.stat().st_size == e['bytes'] and sha(p) == e['sha256'], str(p)
        if 'expected_sha256' in e:
            assert e['expected_sha256'] == e['sha256'] and e['expected_bytes'] == e['bytes']
    return len(entries)

assert not D.exists()
counts = {n: verify(load(C / n)) for n in [
    'mathematical-packet-bindings.json', 'private-primary-packet-bindings.json',
    'historical-own-evidence-bindings.json']}
counts['review_own_records'] = verify(load(A / 'own-bindings.json')['records'])
counts['review_input_records'] = verify(load(A / 'input-bindings.json'))
assert load(C / 'input.json') == load(A / 'input.json')
grant = load(C / 'input.json')['notes'][0]
assert grant == load(A / 'G331-qualified-grant.json')
assert load(A / 'original-task.json') == load(C / 'original-task.json')
assert sha(A / 'original-task.json') == 'd524b816c1462a6909a85bd0e39b84ab34ca04be27ec99eccbfde7ffcc0316a8'
actual_path = K / 'round245-actual-native-final.json'
actual = load(actual_path)
expanded = load(A / 'native-notes.json')
assert actual['candidate'] is False and expanded['candidate'] is False
assert [(n['id'], n['support']) for n in actual['notes']] == [(n['id'], n['support']) for n in expanded['notes']]
historical = next((R / 'campaigns/round-242').iterdir())
assigned = load(historical / 'input.json')['task']
exact = load(C / 'original-task.json')
reconstructed = (json.dumps(assigned, ensure_ascii=False, indent=2) + '\n').encode()
assert len(reconstructed) == 21927
assert hashlib.sha256(reconstructed).hexdigest() == '370ab1eb8319a773be4e7df91270e48e235ff16930fed4e961f0b00eea2ef2e7'
assert assigned['problem'].startswith(exact['problem']) and assigned['completionCriteria'].startswith(exact['completionCriteria'])
assert assigned != exact

D.mkdir()
review = D / 'independent-review245'
review.mkdir()
for e in load(A / 'own-bindings.json')['records']:
    rel = Path(e['path'])
    assert not rel.is_absolute() and '..' not in rel.parts
    target = review / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(A / rel, target)
shutil.copyfile(A / 'own-bindings.json', review / 'own-bindings.json')
shutil.copyfile(actual_path, review / 'actual-native-FINAL.json')
for name in ['G331-qualified-grant.json', 'G331-mandatory-source-scope.json',
             'G331-source-application-ledger.md', 'G331-exact-scope.md',
             'original-task.json', 'whole-source-application-ledger.md',
             'original-scope-and-noncircularity.md', 'whole-proof-coverage.md']:
    shutil.copyfile(A / name, D / name)
source = (A / 'P12.3-conductor-criterion-paper.tex').read_text()
old = r'\operatorname{ord}_i/operatorname{ord}_i(\aideal)'
new = r'\operatorname{ord}_i/\operatorname{ord}_i(\aideal)'
assert source.count(old) == 1
(D / 'P12.3-conductor-criterion-paper.tex').write_text(source.replace(old, new))
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), round=245, continuation=340,
    status='ROOT whole proof/source/scope read; compilation and final acceptance pending',
    originals_solved=13, originals_open=29, accepted_papers=91, original_closed=False,
    review_actual_FINAL_sha256=sha(actual_path), whole_review_controller_native_decoded_equal=True,
    whole_qualified_grant_equal=True, verified_binding_counts=counts,
    actual_expanded_whole_equal=actual == expanded,
    actual_expanded_fields_equal=[{k:n[k] == m[k] for k in n} for n,m in zip(actual['notes'], expanded['notes'])],
    ROOT_whole_reads=['All seven actual FINAL notes and every field', 'Whole independent-review.md',
        'Whole whole-proof.md: characters0:18000 and18000:end',
        'Whole supplemental TeX: characters0:14000,14000:28000,28000:end',
        'Whole application ledger, coverage, original scope, evidence audit and acceptance decision'],
    supplemental_source_origin_sha256=sha(A / 'P12.3-conductor-criterion-paper.tex'),
    supplemental_source_current_sha256=sha(D / 'P12.3-conductor-criterion-paper.tex'),
    source_change='One missing backslash in the DVR normalized-order notation; all proof arguments retained.',
    documentary_corrigendum_reconstructed_independently=True,
    original_author_source_and_reviewer_source_unchanged=True,
    source_bodies_extracts_pixels_and_private_provider_logs_not_copied=True,
    supplied_author_or_reviewer_programs_ROOT_executed_or_imported=False,
    private_ACTIVE_outputs_ROOT_read=False, protected_editor_open_unchanged=True)
save(D / 'ROOT-whole-reading-and-binding-20261008.json', record)
(D / 'ROOT-README.md').write_text('Separate complete-proof P12.3 conductor-criterion supplement. ROOT has read all actual review notes, whole independent proof, whole TeX source and full source/scope/evidence deliverables. Compilation and final acceptance are pending. The original remains OPEN. Only one missing backslash in normalized DVR order was corrected in this publication copy; immutable native source is retained under independent-review245. G331 must accompany imports with its entire mandatory annotation and source ledger. Supplied reviewer programs are inert DATA, never ROOT-executed/imported; academic primary bodies/extracts/pixels and provider logs remain local.\n')
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(directory=str(D), verified_counts=counts, original_closed=False), indent=2))
