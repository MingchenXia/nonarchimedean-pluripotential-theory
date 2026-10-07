from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
d=json.loads((G/'push-receipt-continuation184.json').read_text())
assert d['commit_sha']=='5f47319803bed86628375cc6a98b0fdae6160946' and d['parent_sha']=='2172fcf78d2a07d688989902e89d0e5f9617d890'
assert d['tree_sha']=='540def311f57e37a7761d70cfefe9e90cd40ff2e' and d['files']==40 and not d['force_update']
assert d['manifest_sha256']==sha(G/'upload-manifest-continuation184.json')
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
review=K/'P16.4-round173-whole-partial-review-binding-20261007.json';b=json.loads(review.read_text())
assert b['verdict']=='PASS' and b['whole_partial_manuscript_accepted'] and not b['original_closed']
assert b['exact_decoded_native_task_and_argument_equal_entire_frozen_inputs'] and b['entire_report_all_premises_and_passages_root_read']
D=K/'public-P16.4-round171-partial-reader'
assert sha(D/'P16.4-paper.tex')=='5501f07febccc59850c980f1183b5d954c55ba1b42bf631786ac2fb71ff30206'
assert sha(D/'P16.4-paper.pdf')=='382dad057916755e7472894ac8ad02fd41c2ddd8fa39b36bfee8f9572ba26d87'
native=json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text());assert native['native_compiler_success'] and native['source_sha256']==sha(D/'P16.4-paper.tex')
P=D/'whole-partial-paper-acceptance173-20261007.json';assert not P.exists()
accept={'recorded_utc':datetime.now(timezone.utc).isoformat(),'atom':'P16.4','author_round':171,'independent_review_round':173,'verdict':'PASS','cumulative_accepted_paper_number':65,
 'source':str(D/'P16.4-paper.tex'),'source_sha256':sha(D/'P16.4-paper.tex'),'pdf':str(D/'P16.4-paper.pdf'),'pdf_sha256':sha(D/'P16.4-paper.pdf'),'pdf_pages':12,
 'review_binding':str(review),'review_binding_sha256':sha(review),'accepted_scope':b['accepted_partial_scope'],'only_caller_grants':['B'],
 'whole_source_and_all_native_author_note_fields_root_read':True,'whole_independent_report_all_premises_and_passages_root_read':True,'fresh_clean_local_builds':2,'native_compiler_success':True,
 'root_visual_pages_read':[1,12],'all_pdf_pages_visually_root_read':False,
 'historical_unverified_draft_heading_preserved_in_exact_reviewed_source':True,'n3_nonessential_script_provenance_not_freshly_authenticated':True,
 'fully_solved_original_atoms_count':9,'original_closed':False,'residual_original_scope':b['residual_original_gaps'],
 'protected_editor_unchanged_open':True,'no_active_private_streams_read':True,'no_hot_feedback_sent':True}
P.write_text(json.dumps(accept,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==64 and j['remaining_open_original_atoms']==33
 j.update(github_checkpoint=d,github_pending_checkpoint=None,historical_reviewed_scoped_papers=65,updated_utc=datetime.now(timezone.utc).isoformat())
 j['P16_4_accepted_trivial_ground_field_partial173']=accept
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open'
    t['research_status']='all_trivial_char0_ground_fields_full_ample_equation_partial_accepted'
    t['current_focus']='Whole17112-page arbitrary-trivial-characteristic-zero-ground-field all-dimensional genuine ample E1 equation theorem independently PASS173, source/native/frozen-input exact,all8premises/12passages read and bound;accepted cumulative paper65. Entire original remains open on nontrivial/nondiscrete fields. New2148-page completed-closure singular-psh/extended-energy/continuous-test-dual descent draft independently176 active;no general unbounded mixed operator or full variational closure.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as stream:
 reader=csv.DictReader(stream,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['ID']=='P16.4':row['Research']='all_trivial_char0_ground_fields_full_ample_equation_partial_accepted'
 if row['ID']=='P14.4':row['Research']='partial_review_FAIL_scope_repaired_entire_reaudit_active'
with table.open('w',newline='') as stream:
 writer=csv.DictWriter(stream,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps({'verified_checkpoint':184,'accepted_scoped_paper':65,'atom':'P16.4','originals_solved':9,'originals_open':33,'acceptance_record':str(P),'acceptance_sha256':sha(P)},indent=2))
