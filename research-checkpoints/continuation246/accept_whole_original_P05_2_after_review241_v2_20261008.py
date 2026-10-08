from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-241/P05.2-original-carrier-tree-primitive-polynomial-independent-whole-proof-and-scope-review'
A = C / 'artifacts/codex-DHljck'
C239 = R / 'campaigns/round-239/P05.2-original-finite-carrier-PCC-tree-and-raw-contact-classification'
A239 = C239 / 'artifacts/codex-hcfWTS'
D = K / 'public-P05.2-continuation332-carrier-tree-primitive-polynomial-whole-original-candidate'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
def save(p, obj):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
def bound(p):
    p = Path(p)
    return dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p))
def verify(records):
    for e in records:
        p = Path(e['path'])
        if not p.is_absolute():
            p = A / p
        assert p.stat().st_size == e['bytes'] and sha(p) == e['sha256'], str(p)
    return len(records)

protected = K / 'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(protected) == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f = load(C / 'freeze.json')
names = [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]
for name, key in names:
    assert sha(C / name) == f[key], name
counts = {name:verify(load(C / name)) for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json']}
b = load(A / 'input-bindings.json')
for key in ['mathematical_packet','private_primaries','historical_evidence_files','historical_author_owned_33','historical_frozen_43','historical_input_controls_4','controls']:
    counts[key] = verify(b[key])
counts['review_owned'] = verify(load(A / 'own-bindings.json')['files'])
inp = load(C / 'input.json')
original_inp = load(C239 / 'input.json')
native_inp = load(A239 / 'input.json')
assert original_inp == native_inp
assert inp['notes'] == original_inp['notes']
assert [n['id'] for n in inp['notes']] == f['only_grants']
note_bindings = load(C / 'qualified-imported-note-bindings.json')
for e, n in zip(note_bindings, inp['notes']):
    assert e['id'] == n['id'] and hashlib.sha256(n['text'].encode()).hexdigest() == e['text_sha256']
    assert len(n['text'].encode()) == e['text_bytes'] and n['checks'] == []
for e, n in zip(b['qualified_note_text_bindings'], inp['notes']):
    assert e['id'] == n['id'] and hashlib.sha256(n['text'].encode()).hexdigest() == e['sha256']
    assert len(n['text'].encode()) == e['bytes']
actual = load(K / 'round241-actual-native-final.json')
saved = load(A / 'review-notes.json')
assert actual['candidate'] and saved['candidate'] and len(actual['notes']) == len(saved['notes']) == 8
forwarded = set(f['only_grants'])
for n in actual['notes']:
    assert set(n['support']) <= forwarded
    forwarded.add(n['id'])
field_comparison = [dict(id=n['id'], fields_equal={k:n[k] == s.get(k) for k in n}) for n,s in zip(actual['notes'],saved['notes'])]
assert all(x['fields_equal']['id'] and x['fields_equal']['support'] for x in field_comparison)
author_actual = load(K / 'round239-actual-native-final.json')
author_saved = load(A239 / 'native-notes.json')
assert author_actual == author_saved and len(author_actual['notes']) == 5
assert (A239 / 'native-notes.json').read_bytes() == (K / 'round239-actual-native-final.json').read_bytes() + b'\n'
assert sha(D / 'P05.2-paper.tex') == 'd6fbbffcaaa533a425524e9b582e2c7eb1712cfbe63d3e8fbe745c3108a3b896'
assert sha(D / 'P05.2-paper.pdf') == 'b7ce4fe7d6c3860c0a6b211e25cd3bdf137baa6ea0c942f1431e302d13a62a08'
old_binding = K / 'round239-whole-candidate-ROOT-reading-and-independent-review-binding-20261008.json'
now = datetime.now(timezone.utc).isoformat()

correction = D / 'mandatory-evidence-and-reader-qualifications-after-review241-20261008.json'
save(correction, dict(recorded_utc=now, atom='P05.2', applies_to_continuation=332,
    mathematical_source_unchanged=True, original_statement_unchanged=True,
    evidence_correction=dict(erroneous_assertion='controller/native assignment differs',
        corrected_observation='Entire decoded input objects are equal: task, all eight notes, and assignment. Only serialized bytes differ.',
        ROOT_independently_compared_decoded_objects=True,
        controller=bound(C239/'input.json'), native=bound(A239/'input.json'),
        historically_erroneous_ROOT_binding=bound(old_binding),
        specific_historical_assertion_verdict='FAIL',
        mathematical_forwarding_intact=True,
        frozen_inputs_and_published_historical_records_unchanged=True),
    reader_precision='Localized auxiliary tests only need the explicitly constructed dense compact AMBIENT rational-PA restrictions, at S272 exact scope; no broader intrinsic test grant is imported.',
    optional_ROOT328='Finite-vertex pair criterion independently PASS as an optional consequence, NOT a frozen author239 premise. Translating back to actual all-root trees uses a smaller tolerance for strict margin; infima need not attain a same-tolerance bound.',
    later_ROOT333334='New unreviewed working proofs, not author239 or reviewer241 inputs, not retrospective acceptance premises.',
    retained_limits=['Infinite structural characterization, no terminating algorithm, finite taxonomy, bounded tree depth or universal real orthogonality claim',
        'Exact finite globally embedded all-face balanced category; no invented compact atlas category or P05.5 closure',
        'All existing eight qualified caller assumptions and their mandatory annotations retained',
        'Historical source FAIL/combined FAIL, retrospective read/provider INCONCLUSIVE, and native231 registration failure unchanged'],
    qualified_import_requires_this_entire_annotation=True,
    hashes_compilation_and_finite_diagnostics_are_not_mathematical_proofs=True))

review_dir = D / 'independent-review241'
assert not review_dir.exists()
review_dir.mkdir()
for name in ['independent-review.md','whole-proof-coverage.md','whole-source-application-ledger.md','original-scope-and-noncircularity.md','original-scope-decision.md','bounded-evidence-report.json','input-bindings.json','own-bindings.json','identity-output.json','read-coverage.json','read-events.jsonl','commands.json','environment.json','validation-output.json','review-notes.json','verify-review-inputs.py','finalize-review.py','review-reader.py']:
    shutil.copyfile(A / name, review_dir / name)
shutil.copyfile(K / 'round241-actual-native-final.json', review_dir / 'actual-native-FINAL.json')

binding_path = K / 'P05.2-round241-whole-original-carrier-tree-classification332-ROOT-binding-20261008.json'
save(binding_path, dict(recorded_utc=now, atom='P05.2', review_round=241,
    authoritative_paper=bound(D/'P05.2-paper.tex'), author_PDF=bound(D/'P05.2-paper.pdf'),
    author_actual_FINAL=bound(K/'round239-actual-native-final.json'),
    review_actual_FINAL=bound(K/'round241-actual-native-final.json'),
    review_saved_expanded_notes=bound(A/'review-notes.json'),
    review_actual_saved_field_comparison=field_comparison,
    saved_review_prose_is_distinct_from_actual_FINAL=True,
    ROOT_whole_read_units=['Authoritative 343-LF paper', 'All five actual author FINAL note objects and fields',
        'Author source ledger, exact scope, coverage, noncircularity decision',
        'Complete original 55562-character family and completion criteria',
        'All eight actual reviewer FINAL note objects and fields',
        'Complete independent-review.md, whole-source-application-ledger.md, whole-proof-coverage.md, original-scope-and-noncircularity.md, original-scope-decision.md, bounded-evidence-report.json'],
    separate_parallel_author_argument_ROOT_whole_read_claimed=False,
    separate_saved_review_expanded_notes_ROOT_whole_read_claimed=False,
    semantic_reading_inferred_from_hashes=False, independently_verified_binding_counts=counts,
    unchanged_qualified_imported_note_texts=8,
    mathematical_verdict='PASS all five author proofs', essential_new_source_verdict='PASS',
    whole_original_scope_and_noncircularity_verdict='PASS exact defined category; explicit infinite structural certificate',
    bounded_evidence_verdict='PASS current identities; FAIL erroneous historical assignment inequality; retrospective/provider INCONCLUSIVE',
    mandatory_annotation=bound(correction),
    optional_ROOT328_not_essential=True, later_ROOT333334_not_supplied_or_used=True,
    supplied_author_reviewer_programs_executed_or_imported=False,
    only_fresh_ROOT_standard_library_identity_and_record_program_executed=True,
    protected_editor_open_unchanged=True))

acceptance = D / 'whole-original-paper-acceptance-after-review241-20261008.json'
save(acceptance, dict(recorded_utc=now, atom='P05.2', grant_label='O332',
    cumulative_accepted_paper_number=90, continuation=332, fully_solved_original_atom=True,
    original_closed=True, completion='Coefficient-separated full orthogonality classification: genuine-real pairs iff explicit infinite carrier/tree/primitive-polynomial criterion, equivalently all PA and all C_b simultaneous domain/contact; literal/dimension-zero/empty/compact branches resolved',
    mathematical_verdict='PASS entire original with mandatory evidence/reader annotation',
    source=bound(D/'P05.2-paper.tex'), pdf=bound(D/'P05.2-paper.pdf'), pages=14,
    review_binding=bound(binding_path), mandatory_annotation=bound(correction),
    annotation_required_on_import=True, original_statement_unchanged=True,
    other_P05_original_atoms_closed=False, canonical_automatic_acceptance=False,
    builtin_current_source_compile_success=True, originals_solved=12, originals_open=30))

for name in ['active-work.json','checklist-current.json']:
    p = R / name; x = load(p)
    assert len(x['fully_solved_original_atoms']) == 11 and x['remaining_open_original_atoms'] == 31 and x['historical_reviewed_scoped_papers'] == 89
    assert x['github_pending_checkpoint'] is None
    x['fully_solved_original_atoms'] = sorted(x['fully_solved_original_atoms'] + ['P05.2'])
    x.update(updated_utc=now, remaining_open_original_atoms=30, historical_reviewed_scoped_papers=90,
        current_active_batch=[240], P05_2_original_full_solution=load(acceptance),
        P05_2_original_whole_review241=dict(round=241,status='completed; all eight actual FINAL notes and whole independent proof/source/scope/evidence ROOT read; original accepted with mandatory annotation', original_closed=True, review_binding=str(binding_path)),
        P05_2_candidate239=dict(status='Whole original accepted after independent241 and ROOT reconstruction', candidate=True, original_closed=True, public_directory=str(D), mandatory_annotation=str(correction)),
        P05_2_original_contact_certificate239=dict(round=239,status='whole original accepted after independent241', original_closed=True),
        next_work='Continue remaining30 original problems in at most2 native gpt-6.1-sol xhigh campaigns; P12.2 review240 active; publish verified checkpoint246.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
p = R / 'checklist-current.tsv'; lines = p.read_text().splitlines(); hits = 0
for i,l in enumerate(lines):
    a=l.split('\t')
    if a[0]=='P05.2':
        assert a[1]=='open';a[1]='solved';a[2]='whole_original_14p_carrier_tree_primitive_polynomial_classification332_accepted_after_independent241_with_mandatory_annotation';a[3]=str(int(a[3])+1);lines[i]='\t'.join(a);hits+=1
assert hits==1;p.write_text('\n'.join(lines)+'\n')
p=D/'ROOT-public-candidate-status-20261008.json';x=load(p);x.update(updated_utc=now,status='Whole original P05.2 accepted after independent241 and ROOT whole proof/source/scope reconstruction with mandatory annotation',infinite_structural_meaningfulness_pending=False,new_accepted_paper=True,original_closed=True,accepted_paper_number=90,mandatory_annotation=str(correction),originals_solved=12,originals_open=30);p.write_text(json.dumps(x,indent=2)+'\n')
p=D/'ROOT-README.md';p.write_text('Accepted14-page whole-original P05.2 solution, native239 / continuation332, after independent241 and ROOT whole proof/source/scope reconstruction.\n\n12/42 originals solved;30 OPEN;90 accepted papers. Import O332 only with the entire mandatory-evidence-and-reader-qualifications-after-review241-20261008.json and all underlying qualified caller assumptions. Entire decoded controller/native inputs, including assignment, are equal; serialization bytes differ. Historical erroneous records remain unchanged and are explicitly qualified.\n\nReal pairs are characterized by an explicit infinite carrier/tree/primitive-polynomial criterion iff genuine endpoint domain and exact contact for ALL bounded continuous obstacles. Literal positive-dimensional pairs fail the admitted-obstacle domain antecedent; dimensionzero and empty support are direct; compact positive-dimensional objects are absent in the exact globally embedded all-face balanced category. No finite decision algorithm, universal-real theorem, invented compact atlas category or P05.5 result is claimed.\n\nThe authoritative TeX and14-page PDF are unchanged and compiled successfully with the builtin compiler. All five actual author FINAL notes and all eight actual reviewer FINAL notes were ROOT read, with whole independent proof/source/scope/evidence ledgers. Reviewer saved expanded notes have distinct prose and are not passed off as actual FINAL. ROOT328 is an independently valid optional consequence with the smaller-tolerance margin qualification; ROOT333334 are later UNREVIEWED working proofs absent from both frozen inputs and acceptance premises. Protected P16.4 editor remains open unchanged.\n')
assert sha(protected)=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(atom='P05.2',original_closed=True,originals_solved=12,originals_open=30,accepted_papers=90,review_binding=str(binding_path),mandatory_annotation=str(correction),binding_counts=counts),indent=2))
