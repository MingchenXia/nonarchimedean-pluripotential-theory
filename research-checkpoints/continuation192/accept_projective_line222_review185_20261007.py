from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv
R=Path('/workspace/research'); K=R/'root-checks'; D=K/'public-P16.4-continuation222-projective-line-kernel-equation'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P16.4-round185-whole-partial-review-binding-20261007.json'; b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and not b['original_closed']
assert b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read'] and b['caller_grants']==['O','D','N','T']
assert sha(D/'P16.4-paper.tex')=='da4c92c7d3a4593adf7a11d642e6d46767e697793d63fb706730954f7b61af5f'
assert sha(D/'P16.4-paper.pdf')=='fd77f81a79ccab57929aafafca3d9b1bf3ce2a65aa02d7969d7c4d87f15a4f5b'
repro=json.loads((D/'root-reproduction-and-publication-binding-20261007.json').read_text())
assert repro['whole_saved_source_root_read'] and repro['native_compiler_success'] and repro['source_sha256']==sha(D/'P16.4-paper.tex')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
P=D/'whole-partial-paper-acceptance185-20261007.json'; Q=D/'harmless-reader-clarifications185-20261007.json'; assert not P.exists() and not Q.exists()
now=datetime.now(timezone.utc).isoformat()
a=dict(recorded_utc=now,atom='P16.4',continuation=222,independent_review_round=185,verdict='PASS',cumulative_accepted_paper_number=72,
    source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=7,
    review_binding=str(review),review_binding_sha256=sha(review),accepted_scope=b['accepted_partial_scope'],only_caller_grants=['O','D','N','T'],
    whole_saved_source_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_clean_local_builds=2,native_compiler_success=True,
    root_visual_pages_read=[1,7],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,
    original_closed=False,residual_original_scope=b['residual_original_gaps'],protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
P.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=185,source_sha256=sha(D/'P16.4-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,
    clarifications=['In the tree sections Z is (P^1_C)^an. A finite disk point has positive finite radius and excludes radius-zero classical points. Terminal ancestors are directed outward.',
    'BE8.11/CLD6.9.2 identifies atomic support; coefficients use CLD6.9.3-6.9.4 and6.9.6, independently checked by the reviewer.',
    'The reference to a remaining positive-residue-characteristic axis concerns the general geometric scope; this split projective-line theorem itself includes positive residue characteristic.',
    'The task-only grant passage has native/canonical premise0 and is preserved but excluded from external source coverage. The same premise has three literal primary passages.']),ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text()); assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==71 and j['remaining_open_original_atoms']==33
    j.update(historical_reviewed_scoped_papers=72,updated_utc=now,P16_4_accepted_projective_line_equation185=a,
        goal_state='9/42 originals independently accepted;33 open;72 cumulative independently accepted papers. The all-complete-field split projective-line actual equation222 is proved, in addition to operator217, comparison218 and criterion220. Full general-variety P16.4 and all remaining originals stay open. Continue in batches of at most two, regularly pushing verified GitHub checkpoints.',
        next_work='Completed185 PASS accepts whole222 P^1_K equation. Extend to actual general curves and pursue full originalP16.4 without assuming graph potentials are actual FS metrics. Completed184 candidate=false proves a new U(3,4) strict-growth contact obstruction; independently review the whole new paper, then continue full originalP05.2 classification. No original is newly closed.')
    if name=='checklist-current.json':
        for t in j['targets']:
            if t['id']=='P16.4':
                assert not t['fully_solved'] and t['closure']=='open'
                t['research_status']='all_field_projective_line_equation_accepted_general_equation_open'
                t['current_focus']='Whole222 PASS185/accepted72 proves the split P^1_K actual finite-energy equation, intrinsic target criterion and every-solution allpoint uniqueness for all complete characteristic-zero fields and actual ample rational bundles. Whole217/218/220 remain accepted supporting results. General curves, nonsplit genus-zero and higher-dimensional prescribed-target equations remain open.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as f: reader=csv.DictReader(f,delimiter='\t'); columns=reader.fieldnames; rows=list(reader)
for row in rows:
    if row['ID']=='P16.4': row['Research']='all_field_projective_line_equation_accepted_general_equation_open'
with table.open('w',newline='') as f: w=csv.DictWriter(f,fieldnames=columns,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=72,review_round=185,originals_solved=9,originals_open=33,acceptance_record=str(P),acceptance_sha256=sha(P)),indent=2))
