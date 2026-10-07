from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
R=Path('/workspace/research');K=R/'root-checks';D=K/'public-P16.4-continuation218-strict-locality-comparison'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P16.4-round181-whole-partial-review-binding-20261007.json';b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and not b['original_closed']
assert b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read'] and b['caller_grants']==['O']
assert sha(D/'P16.4-paper.tex')=='88c38bd1e77617c8be66d90faa6d2c207d1c46f8e55f56883025b879072b8977'
assert sha(D/'P16.4-paper.pdf')=='98d74633c2f466b2fa54fdc6410c92f83ead2a045c80b626b3f46c444d95343b'
native=json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text())
assert native['native_compiler_success'] and native['source_sha256']==sha(D/'P16.4-paper.tex')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
P=D/'whole-partial-paper-acceptance181-20261007.json';Q=D/'harmless-reader-clarifications181-20261007.json';assert not P.exists() and not Q.exists()
now=datetime.now(timezone.utc).isoformat()
a=dict(recorded_utc=now,atom='P16.4',continuation=218,independent_review_round=181,verdict='PASS',cumulative_accepted_paper_number=70,
    source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=6,
    review_binding=str(review),review_binding_sha256=sha(review),accepted_scope=b['accepted_partial_scope'],only_caller_grants=['O'],
    whole_saved_source_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_clean_local_builds=2,native_compiler_success=True,
    root_visual_pages_read=[1,6],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,
    original_closed=False,residual_original_scope=b['residual_original_gaps'],protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
P.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=181,source_sha256=sha(D/'P16.4-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,
    clarifications=['Historical O-unreviewed wording is superseded by the explicit whole accepted217 caller grant in frozen181 input; no locality/comparison is imported from O.',
        'Finite E1 maxima are established in218 from actual BE psh maximum closure and energy-majorant monotonicity; they need not be attributed to the statement of O.',
        'For continuous endpoints select a uniformly convergent smooth sequence with errors2^-j from the regularization net; no cofinal sequence is presumed. Trivialize dL and divide weights/products by their exact rational scaling.',
        'CLD5.6.6 is used as a measure statement in top degree only. The reviewer reconstructed the needed local product estimate by weak domination, keeping both positive dominating parts, without importing broader unrelated strong-decomposition claims in CLDv1.',
        'The native structured task-only O passage has premise0 although the report calls it unindexed. Its native/canonical fields are preserved and it is excluded from external coverage; the two primary BE passages independently cover premise0.']),ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==69 and j['remaining_open_original_atoms']==33
    j.update(historical_reviewed_scoped_papers=70,updated_utc=now,P16_4_accepted_all_field_strict_locality_comparison181=a,
        goal_state='9/42 original problems independently accepted;33 remain open;70 cumulative independently accepted research papers. General all-field E1 operator217 and strict locality/comparison218 are verified supporting results. General-field prescribed-target equation remains open. Continue original problems in batches of at most two with regular verified GitHub pushes.',
        next_work='Continue all remaining original problems in batches of at most two. Use complete accepted all-field operator and locality/comparison with exact hypotheses; prove remaining actual compactness/envelope/target/attainment/uniqueness requirements. Whole220 norming-reference target criterion is under independent182 review, not yet a grant. Completed180 is candidate=false and does not close P16.4.')
    if name=='checklist-current.json':
        for t in j['targets']:
            if t['id']=='P16.4':
                assert not t['fully_solved'] and t['closure']=='open';t['research_status']='all_complete_field_E1_operator_and_comparison_accepted_equation_open'
                t['current_focus']='Entire217 general operator PASS179/accepted69 and entire218 strict Borel winner locality/open locality/mixed+pure comparison PASS181/accepted70, exact complete bindings verified. Whole220 norming atomic reference target criterion independently182 active; explicit P^n sector only, no target attainment. Original-equation author180 settled candidate=false with a12-page unreviewed partial manuscript and additional every-solution variational consequences; whole notes ROOT read, artifact manuscript still under ROOT reading. General original compactness/EP/outer derivative/intrinsic target equivalence/actual attainment/every-solution uniqueness remain open.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['ID']=='P16.4':row['Research']='all_complete_field_E1_operator_and_comparison_accepted_equation_open'
with table.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=70,review_round=181,originals_solved=9,originals_open=33,acceptance_record=str(P),acceptance_sha256=sha(P)),indent=2))
