from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
R=Path('/workspace/research');K=R/'root-checks';D=K/'public-P05.2-continuation225-balanced-support-maximum-principle'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P05.2-round188-whole-partial-review-binding-20261007.json';b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and b['caller_grants']==[] and b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read']
assert sha(D/'P05.2-paper.tex')=='796ef33eda780e65164664944d3b6daa46485ce852904d31e9424b6a5284ce01'
assert sha(D/'P05.2-paper.pdf')=='d9e5483a1b5db3276d4eb1be7e3161822899ec1984a23afae6a9590f630c85d7'
repro=json.loads((D/'root-reproduction-binding-20261007.json').read_text());assert repro['whole_final_saved_source_root_read'] and repro['native_compiler_success'] and repro['fresh_clean_final_local_builds']==2 and repro['final_warning_count']==0
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
P=D/'whole-partial-paper-acceptance188-20261007.json';Q=D/'harmless-reader-clarifications188-20261007.json';assert not P.exists() and not Q.exists()
now=datetime.now(timezone.utc).isoformat()
a=dict(recorded_utc=now,atom='P05.2',continuation=225,independent_review_round=188,verdict='PASS',cumulative_accepted_paper_number=74,source=str(D/'P05.2-paper.tex'),source_sha256=sha(D/'P05.2-paper.tex'),source_lf_lines=163,pdf=str(D/'P05.2-paper.pdf'),pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=5,review_binding=str(review),review_binding_sha256=sha(review),accepted_scope=b['accepted_partial_scope'],only_caller_grants=[],whole_final_saved_source_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_clean_final_local_builds=2,native_compiler_success=True,root_visual_pages_read=[1,5],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,original_closed=False,residual_original_scope=b['residual_original_gaps'],protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
P.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=188,source_sha256=sha(D/'P05.2-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,clarifications=['In abstract local charts, the closed-star conclusion means its portion inside the chart; all endpoints remain inside the chart as already required.', 'The maximum principle and compact-envelope results require continuous PC competitors. The rational-endpoint counterexample refutes automatic continuity but does not assert a discontinuous envelope.', 'Rational constant literal-PA compact-envelope claims require the stated finite BOUNDED rational cell decomposition compatible with charts. No extended operator for arbitrary continuous functions on arbitrary abstract spaces is imported.']),indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==73 and j['remaining_open_original_atoms']==33
    j.update(historical_reviewed_scoped_papers=74,updated_utc=now,P05_2_accepted_balanced_support_maximum188=a,goal_state='9/42 originals independently accepted;33 open;74 cumulative independently accepted scoped/supporting papers. Positive balancing geometry and continuous PCC maximum principle are proved scoped results; full original P05.2/P16.4 remain open. Continue in batches of at most two with verified regular GitHub pushes.',next_work='Independent189 audits the entire actual genus-zero equation manuscript. Continue original P05.2 classification using complete accepted224/225 bodies with all clarifications; continuous representative route226 remains unproved data. Preserve all33 original goals.')
    if name=='checklist-current.json':
        for t in j['targets']:
            if t['id']=='P05.2':
                assert not t['fully_solved'] and t['closure']=='open';t['research_status']='strict_growth_obstruction_and_continuous_maximum_principle_accepted_classification_open';t['current_focus']='Entire224 and225 independently PASS187/188; unrestricted rational-endpoint competitor envelope continuity/real regularity/general contact and structural classification remain open.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as f:reader=csv.DictReader(f,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['ID']=='P05.2':row['Research']='strict_growth_obstruction_and_continuous_maximum_principle_accepted_classification_open'
with table.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=columns,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=74,review_round=188,originals_solved=9,originals_open=33,acceptance_record=str(P),acceptance_sha256=sha(P)),indent=2))
