from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
C = next((R / 'campaigns/round-245').iterdir())
A = C / 'artifacts/codex-xaNUnj'
D = K / 'public-P12.3-continuation340-exact-conductor-envelope-criterion'
O = K / 'public-P12.3-continuation336-geometric-envelope-obstruction-and-positive-sectors-unreviewed'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
def bound(p):
    return dict(path=str(p), bytes=Path(p).stat().st_size, sha256=sha(p))
def save(p, x):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

assert sha(O / 'P12.3-paper.tex') == 'b3c02f921900d2ecb492ffee9088f92306490c0a9e6327ab789eff3b1aeb6a6d'
assert sha(O / 'P12.3-paper.pdf') == '41ac0c2b6824ace55d67e17b9338fd25210e7c20bba39046e23d144700cc1f26'
reading = load(D / 'ROOT-whole-reading-and-binding-20261008.json')
assert reading['supplemental_source_current_sha256'] == sha(D / 'P12.3-conductor-criterion-paper.tex')
assert load(D / 'ROOT-built-in-compile-20261008.json')['tool_result']['kind'] == 'success'
decision = load(A / 'acceptance-decision.json')
assert all(x['mathematics'] == 'PASS' for x in decision['actual242'])
assert all(x['judgment'] == 'PASS' for x in decision['ROOT335'])
assert decision['entire_original_P12_3']['candidate'] is False
for name in ['active-work.json', 'checklist-current.json']:
    x = load(R / name)
    assert len(x['fully_solved_original_atoms']) == 13 and x['remaining_open_original_atoms'] == 29
    assert x['historical_reviewed_scoped_papers'] == 91 and x['github_pending_checkpoint'] is None
st = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],
    cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
assert st['status'] == 'completed' and st['calls']['unsettled'] == 0
now = datetime.now(timezone.utc).isoformat()

shutil.copyfile(C / 'original-task.json', O / 'exact-original-task-after-review245.json')
corrigendum = dict(recorded_utc=now, status='Mandatory documentary corrigendum accompanying accepted mathematical content',
    exact_original=bound(O / 'exact-original-task-after-review245.json'),
    author_saved_original=bound(O / 'original-task.json'),
    author_saved_object_is_unchanged_exact_original=False,
    author_saved_object_is_augmented_assignment=True,
    entire_original_problem_and_criteria_survive_as_prefixes=True,
    correction='Native242 saved the augmented research assignment under original-task.json. Its unchanged-original assertion in actual/expanded n1 and n6 and paper preservation prose is false. The exact original is attached separately. All mathematical proofs are independently correct at their stated scopes.',
    author_source_and_pdf_unchanged=True,
    source_grant='Only complete qualified G331 with its full mandatory annotation, source ledger and exact scope',
    mathematical_scope='Full-family strictly negative double-plane obstruction and no maximal minorant; compact raw envelope calculus; every continuous obstacle in the published smooth affine closed algebraically closed characteristic-zero range; extended USC inputs conditional on an established continuous-envelope property; all excellent reduced-curve clipping; exact constrained normalization and primary-gauge formulas.',
    residual_original_scope='General excellent normal singular higher-dimensional envelope construction/regularity and arbitrary-characteristic normal/smooth positivity remain unresolved.',
    historical_provider_and_unavailable_build_attestations_not_newly_certified=True,
    actual_and_expanded_prose_distinct=True,
    reviewer_missing_historical_files_not_misrepresented='Independent245 only received 23 of31 checkable author-own entries; ROOT separately checked all31 against actual completed242 artifacts before staging336.',
    ROOT_whole_author_notes_and_source_read_before_review=True,
    ROOT_whole_independent_review_notes_proof_source_scope_read=True,
    binding=bound(D / 'ROOT-whole-reading-and-binding-20261008.json'),
    full_corrigendum_and_G331_qualifications_required_on_import=True,
    original_closed=False)
save(O / 'mandatory-documentary-source-scope-corrigendum-after-review245-20261008.json', corrigendum)
annotation = dict(recorded_utc=now, source_change=reading['source_change'],
    source_origin_sha256=reading['supplemental_source_origin_sha256'],
    source_current_sha256=reading['supplemental_source_current_sha256'],
    grant='Only exact qualified G331, with whole mandatory annotation and whole source ledger',
    scope='Every excellent reduced local positive-dimensional germ and primary gauge: raw-C/raw-D equality; regularization iff continuity; exact J_k/factorial formula; full normalization criterion iff separated raw envelope continuous and fibre-constant; different-normal-centre obstruction. All-characteristic explicit double plane. All excellent reduced curves. Published smooth affine CLOSED algebraically closed characteristic-zero BFJ continuous-envelope range.',
    source_application='BFJ complete immediate proofs at their exact hypotheses; historical resolution/multiplier and G331 algebraic foundations disclosed as published background, not recursively freshly reconstructed.',
    normal_continuity_is_condition_not_conclusion=True,
    no_increasing_D_closure_or_nested_net_flattening=True,
    no_classification_of_internal_normalization_fibres=True,
    no_singular_multiplier_or_arbitrary_model_cofinality_or_literal_radial_identification=True,
    no_products_energy_or_full_P12_6_operators=True,
    original_closed=False, all_supports_and_full_conductor_fibres_retained=True,
    immutable_author_reviewer_sources_unchanged=True,
    incoming_G331_annotation_and_source_ledger_required_on_import=True,
    full_current_annotation_required_on_import=True)
save(D / 'mandatory-source-scope-and-reader-qualifications-after-review245-20261008.json', annotation)
accepted = []
for directory, number, continuation, source, scope in [
    (O,92,336,'P12.3-paper.tex',corrigendum['mathematical_scope']),
    (D,93,340,'P12.3-conductor-criterion-paper.tex',annotation['scope'])]:
    rec = dict(recorded_utc=now, atom='P12.3', continuation=continuation,
        cumulative_accepted_paper_number=number, original_closed=False,
        fully_solved_original_atom=False, mathematical_verdict='PASS entire delimited paper after independent245 and ROOT whole proof/source/scope review',
        exact_scope=scope, source=bound(directory/source),
        review_actual_FINAL=bound(K/'round245-actual-native-final.json'),
        review_binding=bound(D/'ROOT-whole-reading-and-binding-20261008.json'),
        mandatory_qualification=bound(directory/('mandatory-documentary-source-scope-corrigendum-after-review245-20261008.json' if directory==O else 'mandatory-source-scope-and-reader-qualifications-after-review245-20261008.json')),
        whole_G331_qualifications_and_source_ledger_required=True,
        builtin_source_compilation_success=True, compilation_not_mathematical_acceptance=True,
        originals_solved=13, originals_open=29)
    if directory==O:
        rec.update(pdf=bound(O/'P12.3-paper.pdf'), pages=23)
    else:
        rec.update(pdf_exported=False)
    save(directory/'scoped-paper-acceptance-after-review245-20261008.json',rec)
    accepted.append(rec)
    (directory/'ROOT-README.md').write_text('Accepted delimited P12.3 mathematical paper after independent native245 and ROOT whole proof/source/scope review. The whole original P12.3 remains OPEN.13/42 originals solved;29 OPEN;93 accepted papers in total.\n\nThe exact scope and mandatory qualifications are attached. Native242 must always be read with its documentary corrigendum and exact-original attachment. The separate conductor supplement proves both directions of the criterion but does not establish normal higher-dimensional envelope continuity in arbitrary characteristic. G331 requires its whole annotation and source ledger. Primary bodies/extracts/pixels and private provider/controller output remain local; supplied author/reviewer programs are inert DATA. Compilation and hashes are observations, not mathematical proofs. The protected P16.4 editor stays open unchanged.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p)
    x.update(updated_utc=now,historical_reviewed_scoped_papers=93,current_active_batch=[246],
        P12_3_scoped_envelope_papers_after_review245=accepted,
        P12_3_geometric_envelope_review245=dict(round=245,status='completed; all actual notes and whole independent proof/source/scope ROOT read; two delimited papers accepted with mandatory qualifications',original_closed=False),
        next_work='Continue original P12.4 native246 and independent review of the completed bounded-product proof when available; max2 native campaigns.13solved29OPEN93accepted. Verify regular GitHub checkpoint250 with accepted P12.3 scopes/corrigendum and local ROOT339 working proof.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv'; lines=p.read_text().splitlines(); hits=0
for i,line in enumerate(lines):
    fields=line.split('\t')
    if fields[0]=='P12.3':
        assert fields[1]=='open'
        fields[2]='partial_scoped_envelopes_and_exact_conductor_criterion_after_independent245'
        fields[3]=str(int(fields[3])+2)
        lines[i]='\t'.join(fields); hits+=1
assert hits==1
p.write_text('\n'.join(lines)+'\n')
status_path=O/'ROOT-public-draft-status-20261008.json'; x=load(status_path)
x.update(updated_utc=now,status='Delimited mathematical paper accepted after independent245 with mandatory documentary corrigendum; original OPEN',paper_accepted=True,accepted_paper_number=92,original_closed=False)
status_path.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(accepted_papers=[92,93],originals_solved=13,originals_open=29,current_active_batch=[246]),indent=2))
