from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv
R=Path('/workspace/research'); K=R/'root-checks'; D=K/'public-P05.2-continuation224-strict-growth-obstruction'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P05.2-round187-whole-partial-review-binding-20261007.json'; b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and not b['original_closed'] and b['caller_grants']==[]
assert b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read']
assert sha(D/'P05.2-paper.tex')=='49c87b02c5fd2269eaae85f4d16537d462ddf1413ab80cbefd4deb8ea6ef5aae'
assert sha(D/'P05.2-paper.pdf')=='0db6c1c3af190fd951f6c2d0dfbba994d2d6a35377e379db756d9bd7b289a949'
repro=json.loads((D/'root-reproduction-binding-20261007.json').read_text()); native=json.loads((D/'native-compiler-and-limited-visual-addendum-20261007.json').read_text())
assert repro['whole_saved_source_root_read'] and repro['fresh_clean_local_builds']==2 and repro['root_finite_check_rerun'] and native['native_compiler_success'] and native['source_sha256']==sha(D/'P05.2-paper.tex')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
P=D/'whole-partial-paper-acceptance187-20261007.json'; Q=D/'harmless-reader-clarifications187-20261007.json'; assert not P.exists() and not Q.exists()
now=datetime.now(timezone.utc).isoformat()
a=dict(recorded_utc=now,atom='P05.2',continuation=224,independent_review_round=187,verdict='PASS',cumulative_accepted_paper_number=73,source=str(D/'P05.2-paper.tex'),source_sha256=sha(D/'P05.2-paper.tex'),pdf=str(D/'P05.2-paper.pdf'),pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=9,review_binding=str(review),review_binding_sha256=sha(review),accepted_scope=b['accepted_partial_scope'],only_caller_grants=[],whole_saved_source_root_read=True,whole_argument_and_source_ledger_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_clean_local_builds=2,native_compiler_success=True,root_finite_check_rerun=True,finite_evidence_is_not_continuum_proof=True,root_visual_pages_read=[1,9],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,original_closed=False,residual_original_scope=b['residual_original_gaps'],protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
P.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=187,source_sha256=sha(D/'P05.2-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,clarifications=['The intersection clause of the local-support lemma applies to PA f on a common carrying structure; the segment and Jensen clauses apply to continuous f. Every actual intersection application uses PA f.', 'For translated cells the tangent space is span(sigma-sigma). The shorthand span(sigma) in the conical note convention applies only to cones; the main manuscript states the correct general convention.', 'Strictness is the explicitly disclosed active-coefficient local-support convention. No claim of the source literal zero-coefficient strictness wording is made.', 'Reviewer independently checked mathematical finite rows/counts. Historical environment/retrieval-hash/compile execution claims are provenance observations, not mathematical premises. ROOT separately reproduced finite checks/builds and exact native source compilation.']),ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text()); assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==72 and j['remaining_open_original_atoms']==33
    j.update(historical_reviewed_scoped_papers=73,updated_utc=now,P05_2_accepted_strict_growth_obstruction187=a,
        goal_state='9/42 originals independently accepted;33 open;73 cumulative independently accepted papers. Whole222 split projective-line equation and whole224 strict-growth polyhedral contact obstruction are proved scoped results. General P16.4 and P05.2 classification remain open. Continue in batches of at most two with verified regular GitHub pushes.',
        next_work='Full originalP16.4 author186 continues using six whole accepted grants; no hot feedback. Whole225 positive balanced support and continuous maximum-principle paper is under independent188 review, with no caller grants. Continue full originalP05.2 classification using exact whole accepted224 scope when a slot frees; real regularity, general local contact and global realization remain unresolved. Preserve all33 original objectives.')
    if name=='checklist-current.json':
        for t in j['targets']:
            if t['id']=='P05.2':
                assert not t['fully_solved'] and t['closure']=='open'
                t['research_status']='strict_growth_Bergman_contact_obstruction_accepted_classification_open'
                t['current_focus']='Whole224 nine-page U(3,4) strict positive-growth contact obstruction and literal regularity failure independentlyPASS187/accepted73, no caller mathematical grants. General structural classification remains open. New whole225 compact-support/fan convex-hull/continuous PCC maximum principle and rational-endpoint continuity counterexample under independent188 review.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as f: reader=csv.DictReader(f,delimiter='\t'); columns=reader.fieldnames; rows=list(reader)
for row in rows:
    if row['ID']=='P05.2': row['Research']='strict_growth_Bergman_contact_obstruction_accepted_classification_open'
with table.open('w',newline='') as f: w=csv.DictWriter(f,fieldnames=columns,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=73,review_round=187,originals_solved=9,originals_open=33,acceptance_record=str(P),acceptance_sha256=sha(P)),indent=2))
