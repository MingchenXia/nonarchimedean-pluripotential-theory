from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
R=Path('/workspace/research');K=R/'root-checks';D=K/'public-P16.4-continuation217-general-E1-mixed-operator'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P16.4-round179-whole-partial-review-binding-20261007.json';b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and not b['original_closed']
assert b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read'] and b['caller_grants']==[]
assert sha(D/'P16.4-paper.tex')=='e2483fd11d384bdc15e60347f5c4f3568dd718c2ccfd2fd3d4bafb9d5dd1a440'
assert sha(D/'P16.4-paper.pdf')=='742ce408284f9ab20eb8f819d99d2c771f350c1b443a869bd6ee4b442523d1ca'
native=json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text());assert native['native_compiler_success'] and native['source_sha256']==sha(D/'P16.4-paper.tex')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();P=D/'whole-partial-paper-acceptance179-20261007.json';Q=D/'harmless-reader-clarifications179-20261007.json';assert not P.exists() and not Q.exists()
accept=dict(recorded_utc=now,atom='P16.4',continuation=217,independent_review_round=179,verdict='PASS',cumulative_accepted_paper_number=69,
 source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=8,
 review_binding=str(review),review_binding_sha256=sha(review),accepted_scope=b['accepted_partial_scope'],only_caller_grants=[],
 whole_saved_source_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_clean_local_builds=2,native_compiler_success=True,
 root_visual_pages_read=[1,8],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,original_closed=False,residual_original_scope=b['residual_original_gaps'],protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
P.write_text(json.dumps(accept,ensure_ascii=False,indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=179,source_sha256=sha(D/'P16.4-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,
 clarifications=['Nonpositive endpoints need not have nonpositive defining approximants in the original reference. For epsilon>0, compactness puts all finite-family tails below epsilon. Shift psi to psi+epsilon and all scalars q to q-epsilon; the majorant cocycle gives costs B(q)+epsilonV, and curvature is unchanged. The proof yields int(-w)MA+epsilonV<=C_n[B(w)+sum_r B(u_r)+(n+1)epsilonV]. Let epsilon decrease to zero to recover the displayed exact bound. This introduces no constrained approximation or EP premise.', 'The uniform-closure proof uses a summable-error subsequence before adding decreasing constants.', 'The last expanded summand in BE Lemma8.6 has a minus sign; the correct signed identity still implies its stated absolute-value estimate.', 'Affine curvature dependence is on admissible convex combinations of actual fixed-bundle slots; zero coefficients are omitted at poles.']),ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==68 and j['remaining_open_original_atoms']==33
 j.update(historical_reviewed_scoped_papers=69,updated_utc=now,P16_4_accepted_all_field_general_mixed_operator179=accept)
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open';t['research_status']='all_complete_field_general_E1_mixed_operator_accepted_equation_open'
    t['current_focus']='Whole2178-page direct all-complete-field arbitrary-dimensional genuine E1 mixed operator independentlyPASS179, full report/all8premises/14passages ROOT read, native/frozen/source bindings exact;accepted paper69. Source-preserving epsilon-normalization clarification recorded. Exact domain includes trivial/nondiscrete fields, all-point potentials, all-E1 tests and arbitrary jointly weighted nets. Entire218 strict locality/open locality/mixed and pure comparison awaits independent review relative only the complete accepted217 theorem. Original-equation author180 continues its frozen task without hot feedback; full original compactness/EP/outer derivative/target characterization/attainment/every-solution uniqueness remain open.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as stream:
 reader=csv.DictReader(stream,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['ID']=='P16.4':row['Research']='all_complete_field_general_E1_mixed_operator_accepted_equation_open'
with table.open('w',newline='') as stream:
 writer=csv.DictWriter(stream,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_scoped_paper=69,review_round=179,originals_solved=9,originals_open=33,acceptance_record=str(P),acceptance_sha256=sha(P)),indent=2))
