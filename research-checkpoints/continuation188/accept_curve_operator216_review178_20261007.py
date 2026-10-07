from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
R=Path('/workspace/research');K=R/'root-checks';D=K/'public-P16.4-continuation216-all-field-curve-operator'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review=K/'P16.4-round178-whole-partial-review-binding-20261007.json';b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and not b['original_closed']
assert b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read'] and b['caller_grants']==[]
assert sha(D/'P16.4-paper.tex')=='f853c0ac1908b8e0bb0b84a49088572cb77337acab382fc3a0899fd8eb85358b'
assert sha(D/'P16.4-paper.pdf')=='47f40edbfddf54d59cee7fc5dbfb40a0383712d2963158cf0c4aa7e02cb53e07'
native=json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text());assert native['native_compiler_success'] and native['source_sha256']==sha(D/'P16.4-paper.tex')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();P=D/'whole-partial-paper-acceptance178-20261007.json';Q=D/'harmless-reader-clarifications178-20261007.json';assert not P.exists() and not Q.exists()
accept=dict(recorded_utc=now,atom='P16.4',continuation=216,independent_review_round=178,verdict='PASS',cumulative_accepted_paper_number=68,
 source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=7,
 review_binding=str(review),review_binding_sha256=sha(review),accepted_scope=b['accepted_partial_scope'],only_caller_grants=[],
 whole_saved_source_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_clean_local_builds=2,native_compiler_success=True,
 root_visual_pages_read=[1,7],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,original_closed=False,residual_original_scope=b['residual_original_gaps'],protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
P.write_text(json.dumps(accept,ensure_ascii=False,indent=2)+'\n')
Q.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=178,source_sha256=sha(D/'P16.4-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,
 clarifications=['Under reference psi -> psi+c, the scalar becomes u-c and relative energy becomes E(u)-cV.', 'Take common approximation tail bounds from a continuous majorant of one stage or from the compact-majorant lemma.', 'Apply the increasing Radon-net lemma to the normalized nonnegative tail -w_j, or to C-w_j.', 'Set affine endpoints u_0=u and u_1=v explicitly, omitting zero coefficients at poles; no 0*(-infinity) is evaluated.']),ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==67 and j['remaining_open_original_atoms']==33
 j.update(historical_reviewed_scoped_papers=68,updated_utc=now,P16_4_accepted_all_field_curve_operator178=accept)
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open';t['research_status']='all_complete_field_curve_operator_accepted_general_operator_review_active'
    t['current_focus']='Whole2167-page direct genuine E1 curve curvature operator independentlyPASS178, all7premises/16passages ROOT read, exact frozen-input/native/source bindings verified; accepted scoped paper68. All complete char0 fields and arbitrary genus, no residue-char0/algebraic-closure restriction. Entire217 arbitrary-dimensional mixed operator independently179 active and not a grant. Full original target characterization/attainment/every-solution uniqueness, normalized compactness and general EP/orthogonality/outer differentiation remain open; strict locality/comparison follow-up218 is unreviewed.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as stream:
 reader=csv.DictReader(stream,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['ID']=='P16.4':row['Research']='all_complete_field_curve_operator_accepted_general_operator_review_active'
with table.open('w',newline='') as stream:
 writer=csv.DictWriter(stream,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_scoped_paper=68,review_round=178,originals_solved=9,originals_open=33,acceptance_record=str(P),acceptance_sha256=sha(P)),indent=2))
