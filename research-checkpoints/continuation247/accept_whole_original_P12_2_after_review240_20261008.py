from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-240/P12.2-original-geometric-primary-model-and-full-conductor-independent-whole-review'
A=C/'artifacts/codex-ZLc6As'
C238=R/'campaigns/round-238/P12.2-original-geometric-source-completion-and-whole-conductor-reconstruction'
A238=C238/'artifacts/codex-2eREYM'
D=K/'public-P12.2-continuation331-geometric-primary-model-and-full-conductor-original-candidate'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def bound(p):return dict(path=str(p),bytes=Path(p).stat().st_size,sha256=sha(p))
def save(p,x):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def verify(es):
    for e in es:
        p=Path(e['path']);p=p if p.is_absolute()else A/p
        assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],str(p)
        if 'expected_sha256'in e:assert e['expected_sha256']==e['sha256']
    return len(es)
protected=K/'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(protected)=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f=load(C/'freeze.json')
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256')]:assert sha(C/name)==f[key],name
counts={name:verify(load(C/name))for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json']}
counts['independent_review_input_records']=verify(load(A/'exact-input-hashes.json'))
counts['independent_review_owned']=verify(load(A/'own-hashes.json')['artifacts'])
counts['historical_original_inventory']=verify(load(A/'historical-inventory-rehash.json'))
assert load(C/'input.json')['notes']==[]
actual=load(K/'round240-actual-native-final.json');saved=load(A/'native-review-notes.json')
assert actual['candidate'] and saved['candidate'] and len(actual['notes'])==len(saved['notes'])==12
known=set()
for n in actual['notes']:
    assert set(n['support'])<=known and n['id']not in known
    known.add(n['id'])
review_comparison=[dict(id=n['id'],fields_equal={k:n[k]==s.get(k)for k in n})for n,s in zip(actual['notes'],saved['notes'])]
author_actual=load(K/'round238-actual-native-final.json');author_saved=load(A238/'native-notes.json')
author_comparison=[dict(id=n['id'],fields_equal={k:n[k]==s.get(k)for k in n})for n,s in zip(author_actual['notes'],author_saved['notes'])]
assert len(author_comparison)==12 and all(e['fields_equal']['id']and e['fields_equal']['support']for e in author_comparison+review_comparison)
assert sha(D/'P12.2-paper.tex')=='dadc8d064c849b80bbcb55d2c68217cd20a8c3056e3ca10ae729ac7b03537b80'
assert sha(D/'P12.2-paper.pdf')=='51defecf1170ee53d6beba51d4124df9efe923038476e1c04b37c39b3f0930aa'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert len(x['fully_solved_original_atoms'])==12 and x['remaining_open_original_atoms']==30 and x['historical_reviewed_scoped_papers']==90 and x['github_pending_checkpoint']is None
now=datetime.now(timezone.utc).isoformat()
annotation=D/'mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json'
save(annotation,dict(recorded_utc=now,atom='P12.2',continuation=331,source_unchanged=True,original_statement_unchanged=True,
    independent_geometry='Actual primary blowups; actual negative effective finite REAL Cartier presentations; nonnegative degree on EVERY contracted proper integral curve, defined before ideal completion. Uniform comparison and actual decreasing-net comparison then proved.',
    exact_general_scope='Every excellent reduced singular/nonnormal local ring in positive dimension, arbitrary characteristic and residue field; nilpotents invisible, zero-dimensional local reduction boundary empty; ALL semivaluation supports retained.',
    model_system_scope='Directed actual primary blowups with pullback and arbitrary-support evaluations. Cofinality among ALL proper birational models and a full arbitrary-model b-divisor classification are unproved and unclaimed.',
    smooth_specialization_scope='Published BFJ smooth affine CLOSED germs over an algebraically closed characteristic-zero field, dimension>=2, plus direct DVR/empty cases. ALL-retraction extension, closed-face continuity, eventual proper-primary approximation, zero/unit and bottom exceptions retained. No singular/positive-characteristic SNC transfer.',
    normalization_and_finite_scope='Full conductor quotient; finite OPEN singleton stratum and CLOSED infinite-value quotient stratum; positive C and actual decreasing-net D descent, including mixed zero/partial bottom. Full finite-source fibres retained; generic trace only on actual generic-dominating domain components; no vertical generic degree invented.',
    raw_cones='Only Q subset normalization-compatible raw family subset C and equal uniform closures; no raw equality. Fixed PRIMARY c0 gives uniform section-ideal error; nonprimary conductor errors not uniform.',
    source_precision=['Use Keeler corrected v5 and ENTIRE 2018 erratum, replacing false old Lemma3.3; full possibly nonreduced closed fibre and arbitrary residue field retained.',
        'Use current July2024 Swanson-Huneke immediate units, including full10.2.2 continuation10.2.3, Rees residue/dimension/formal-equidimensionality hypotheses.',
        'Normal-domain Izumi bound applies to nonunits; units separate; no analytically irreducible nonnormal completion assertion.',
        'BdFFU printed positive retraction sign is concretely false; used diagnostically only, not as positivity premise.',
        'Complete immediate source proofs and application hypotheses checked; recursive EGA/de Jong/Rees/Ratliff/Izumi/Hironaka/multiplier foundations disclosed as published background at their exact hypotheses, not recursively freshly reproved.'],
    other_original_targets='P12.3 envelopes, P12.4 products, P12.5 energy and P12.6 geometric operator compatibility remain OPEN and separate.',
    literal_radial_distinction='Geometric valuative boundary class can contain nodal(-1,0); this does not identify it with literal classical/CLD logarithmic radial extension class, whose mixed-zero obstruction remains.',
    actual_and_expanded_prose_distinct=True, supplied_programs_ROOT_executed_or_imported=False,
    hashes_finite_diagnostics_and_compilation_not_mathematical_proofs=True,
    full_annotation_and_source_ledger_required_on_import=True))
Q=D/'independent-review240';assert not Q.exists();Q.mkdir()
public_names=['whole-proof.md','whole-proof-coverage.md','whole-source-application-ledger.md','original-scope-and-noncircularity.md','original-scope-decision.md','bounded-evidence-report.json','native-review-notes.json','per-note-verdicts.json','actual-versus-expanded.json','exact-input-hashes.json','historical-inventory-rehash.json','own-hashes.json','review-environment.json','fresh-check-output.json','rerun-commands.md','review_audit.py','audit_historical_inventory.py','extract_bound_html.py','inspect_bound_pages.py','assemble_review.py','verify_review.py','source-pixel-commands.json']
for name in public_names:shutil.copyfile(A/name,Q/name)
shutil.copyfile(K/'round240-actual-native-final.json',Q/'actual-native-FINAL.json')
binding=K/'P12.2-round240-whole-original-geometric-primary-model331-ROOT-binding-20261008.json'
save(binding,dict(recorded_utc=now,atom='P12.2',review_round=240,
    authoritative_paper=bound(D/'P12.2-paper.tex'),author_PDF=bound(D/'P12.2-paper.pdf'),
    author_actual_FINAL=bound(K/'round238-actual-native-final.json'),review_actual_FINAL=bound(K/'round240-actual-native-final.json'),
    author_actual_saved_comparison=author_comparison,review_actual_saved_comparison=review_comparison,
    ROOT_whole_read_units=['Authoritative496-LF23-page paper','All twelve actual author FINAL note objects and fields','Author source ledger, exact scope, coverage, original scope decision','Complete governing original task/family/completionCriteria',
        'All twelve actual independent240 FINAL note objects and fields','Whole independent63090-character proof at explicit0:19000,19000:38000,38000:57000,57000:end chunks','Whole independent source ledger, coverage, noncircularity, original scope decision and bounded evidence'],
    separate_author_parallel_argument_ROOT_whole_read_claimed=False,
    separate_author_saved_expanded_notes_ROOT_whole_read_claimed=False,
    separate_review_saved_expanded_notes_ROOT_whole_read_claimed=False,
    zero_incoming_grants=True,independently_verified_binding_counts=counts,
    mathematical_verdict='PASS entire12-note construction/comparison',essential_new_source_verdict='PASS at disclosed published-background level',whole_original_scope_and_noncircularity_verdict='PASS independently defined actual Cartier/curve-nef geometry plus genuine comparison; exact original scope',bounded_evidence_verdict='PASS current identities and bounded observations; no provider/retrospective certification',
    mandatory_annotation=bound(annotation),supplied_author_reviewer_programs_executed_or_imported=False,
    protected_editor_open_unchanged=True))
acceptance=D/'whole-original-paper-acceptance-after-review240-20261008.json'
save(acceptance,dict(recorded_utc=now,atom='P12.2',grant_label='G331',cumulative_accepted_paper_number=91,continuation=331,fully_solved_original_atom=True,original_closed=True,
    completion='Independently geometric singular/nonnormal psh cone on actual primary models by Cartier effectivity and every contracted-curve degree; proved Cgeom=Cideal and Dgeom=Dideal, full conductor descent and exact published BFJ smooth specialization',
    mathematical_verdict='PASS entire original with mandatory source/scope annotation and source ledger',source=bound(D/'P12.2-paper.tex'),pdf=bound(D/'P12.2-paper.pdf'),pages=23,review_binding=bound(binding),mandatory_annotation=bound(annotation),source_ledger=bound(D/'source-application-ledger.md'),annotation_and_source_ledger_required_on_import=True,original_statement_unchanged=True,other_P12_original_atoms_closed=False,canonical_automatic_acceptance=False,builtin_current_source_compile_success=True,originals_solved=13,originals_open=29))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x['fully_solved_original_atoms']=sorted(x['fully_solved_original_atoms']+['P12.2'])
    x.update(updated_utc=now,remaining_open_original_atoms=29,historical_reviewed_scoped_papers=91,current_active_batch=[],P12_2_original_full_solution=load(acceptance),P12_2_original_whole_review240=dict(round=240,status='completed; all12 actual FINAL notes and whole independent proof/source/scope ROOT read; original accepted with mandatory source/scope annotation',original_closed=True,review_binding=str(binding)),P12_2_candidate238=dict(status='Whole original accepted after independent240 and ROOT whole reconstruction',candidate=True,original_closed=True,public_directory=str(D),mandatory_annotation=str(annotation)),next_work='Continue all remaining29 originals in at most2 native gpt-6.1-sol xhigh campaigns; next original P12.3 envelopes; regular verified checkpoint247.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines();hits=0
for i,l in enumerate(lines):
    a=l.split('\t')
    if a[0]=='P12.2':assert a[1]=='open';a[1]='solved';a[2]='whole_original_23p_geometric_primary_model_full_conductor_and_BFJ_comparison331_accepted_after_independent240';a[3]=str(int(a[3])+1);lines[i]='\t'.join(a);hits+=1
assert hits==1;p.write_text('\n'.join(lines)+'\n')
p=D/'ROOT-public-candidate-status-20261008.json';x=load(p);x.update(updated_utc=now,status='Whole original P12.2 accepted after independent240 and ROOT whole reconstruction with mandatory source/scope annotation',new_accepted_paper=True,original_closed=True,accepted_paper_number=91,mandatory_annotation=str(annotation),originals_solved=13,originals_open=29);p.write_text(json.dumps(x,indent=2)+'\n')
p=D/'ROOT-README.md';p.write_text('Accepted23-page whole-original P12.2 solution, native238 / continuation331, after independent240 and ROOT whole reconstruction.\n\n13/42 originals solved;29 OPEN;91 accepted papers. Import G331 only with the entire mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json and whole source ledger. Actual primary blowups, actual negative effective finite REAL Cartier presentations and EVERY contracted curve degree define positivity before ideal closure; a genuine uniform section-ideal comparison proves Cgeom=Cideal and Dgeom=Dideal. Full conductor descent and exact published BFJ smooth specialization proved. No arbitrary-model cofinality, singular SNC transfer, literal radial equality or P12.3--6 operators are claimed.\n\nAuthoritative source/PDF unchanged and builtin compilation successful. All12 actual author and12 actual independent review FINAL notes and full independent proof/source/scope/evidence ROOT read. Saved expanded prose remains distinct from actual FINAL; hashes, finite checks and compilation are observations, not proofs. Primary bodies/pixels and provider/controller logs remain LOCALONLY. Protected P16.4 editor remains open unchanged.\n')
assert sha(protected)=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
print(json.dumps(dict(atom='P12.2',original_closed=True,originals_solved=13,originals_open=29,accepted_papers=91,review_binding=str(binding),verified_counts=counts),indent=2))
