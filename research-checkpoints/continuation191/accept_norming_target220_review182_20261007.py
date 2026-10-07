from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
R=Path('/workspace/research');K=R/'root-checks';D=K/'public-P16.4-continuation220-norming-reference-target-criterion'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P16.4-round182-whole-partial-review-binding-20261007.json';b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and not b['original_closed']
assert b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read'] and b['caller_grants']==['O']
assert sha(D/'P16.4-paper.tex')=='28f5dc2bf4cbcdbcc415e5694f0f0deec7f028ac253ea85c844a0efe1b49ae7d'
assert sha(D/'P16.4-paper.pdf')=='d3bcb00d7204cc55cf5be51d7fe13e5a0c0aef64e1e0bbaecad4fc6c39bc91e1'
native=json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text());assert native['native_compiler_success'] and native['source_sha256']==sha(D/'P16.4-paper.tex')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
P=D/'whole-partial-paper-acceptance182-20261007.json';Q=D/'harmless-reader-clarifications182-20261007.json';assert not P.exists() and not Q.exists()
now=datetime.now(timezone.utc).isoformat()
a=dict(recorded_utc=now,atom='P16.4',continuation=220,independent_review_round=182,verdict='PASS',cumulative_accepted_paper_number=71,
 source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=5,
 review_binding=str(review),review_binding_sha256=sha(review),accepted_scope=b['accepted_partial_scope'],only_caller_grants=['O'],
 whole_saved_source_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_clean_local_builds=2,native_compiler_success=True,
 root_visual_pages_read=[1,5],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,
 original_closed=False,residual_original_scope=b['residual_original_gaps'],protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
P.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=182,source_sha256=sha(D/'P16.4-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,
 clarifications=['BE Example8.11 pointer to CLD6.9.2 identifies atomic support; exact atomic coefficients are furnished by CLD6.9.3-6.9.4 and6.9.6. The reviewer independently checked those units; standard smooth projective space upstairs has coefficient factor1.',
 'The decreasing-closure metric index is naturally a preorder; quotient equal metrics if a partially ordered directed index is desired.',
 'The report calls the task-only O passage unindexed, but its actual native structured premise index is4. Native/canonical fields are unchanged; the task passage is excluded from external coverage, and premise4 has its own primary BE passage.',
 'This paper does not import or prove strict locality/comparison. Those now independently established results are recorded separately in whole218/PASS181 and are not needed here.']),ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==70 and j['remaining_open_original_atoms']==33
 j.update(historical_reviewed_scoped_papers=71,updated_utc=now,P16_4_accepted_norming_reference_target_criterion182=a,
 goal_state='9/42 original problems independently accepted;33 remain open;71 cumulative independently accepted research papers. General all-field E1 operator217 and locality/comparison218, and norming-reference target criterion220, are verified supporting results. General-field prescribed-target equation remains open. Continue originals in batches of at most two with regular verified GitHub pushes.',
 next_work='Continue all remaining originals. Full originalP05.2 author184 active after preserving pre-admission183 schema failure. Accepted220 intrinsic target equivalence and coercivity hold under its explicit norming-reference hypothesis, concretely standard P^n/O(1) allK, without equation attainment. Develop actual equation construction and every-solution uniqueness, preserving generalX gaps and all33 original scopes. Completed180 remains unreviewed candidate=false.')
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open'
    t['research_status']='all_field_operator_comparison_and_norming_target_accepted_equation_open'
    t['current_focus']='Whole217 PASS179/accepted69; whole218 PASS181/accepted70; whole220 conditional norming-reference intrinsic target criterion PASS182/accepted71, concrete standard P^n/O(1) allK. Finite-dual coercivity does not assert actual equation attainment. GeneralX reference estimates, compactness/EP/outer derivative/target converse/attainment/every-solution uniqueness remain open. Completed180 unreviewed candidate=false.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as stream: reader=csv.DictReader(stream,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['ID']=='P16.4':row['Research']='all_field_operator_comparison_and_norming_target_accepted_equation_open'
with table.open('w',newline='') as stream: writer=csv.DictWriter(stream,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=71,review_round=182,originals_solved=9,originals_open=33,acceptance_record=str(P),acceptance_sha256=sha(P)),indent=2))
