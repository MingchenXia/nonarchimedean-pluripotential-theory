from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, subprocess

R=Path('/workspace/research');K=R/'root-checks';D=R/'deliverables/scoped-P15.3-round120'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,a):
 assert not p.exists(),str(p)
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
canon=K/'P15.3-round120-actual-scoped-independent-review-20261005.json'
assert sha(canon)=='066f08ead04b8404c592256c8781ad26d9da8131b0efb6144cf77ddf34051f2b'
c=json.loads(canon.read_text());assert c['verdict']=='PASS'
assert len(c['premises'])==10 and len(c['passages'])==12
for p in c['passages']:
 assert p['statement']==c['premises'][p['premise']] and p['url'].startswith('https://')
review_binding=K/'P15.3-round120-actual-scoped-review-root-reading-binding-20261005.json'
scope='Curve-free two-torus with dense null line, rank-one transcendental nef form and smooth ordinary P-type zero; genuine potential rigidity and unrescaled collapse for every fixed smooth Kahler model/flag/positive path. One-point blowup exceptional flag: genuine exact trapezoid, all displayed scalar and fixed diagonal-power asymptotics and retained scale dependence. Only the indispensable historical local blowup calculation is imported. Arbitrary prescribed P-types, enriched carriers and general original P15.3 remain open.'
save(review_binding,{'recorded_utc':now,'canonical_result':str(canon),'sha256':sha(canon),
 'operation_id':c['operationId'],'reported_utc':c['reportedAt'],'verdict':'PASS',
 'entire_actual_report_premises_and_passages_root_read':True,'premises':10,'passages':12,
 'actual_exact_zero_based_statement_bindings_verified':True,'actual_https_passages':12,'actual_urn_passages':0,
 'accepted_scope':scope,'original_closed':False,'scoped_paper_count_increment':1,
 'two_harmless_Deng_clarifications_applied_in_publication':True,
 'review_limit':'Independent source-aware native model reconstruction, not formal certification or priority.'})
build=json.loads((D/'build-manifest.json').read_text())
assert [x['exit_code'] for x in build['compilations']]==[0,0]
for n,h in build['artifact_sha256'].items():assert sha(D/n)==h
log=(D/'compile-2.tex.log').read_text();assert 'Missing character' not in log and 'Overfull' not in log
info=subprocess.run(['pdfinfo',str(D/'P15.3-paper.pdf')],capture_output=True,text=True,check=True).stdout
(D/'pdfinfo.txt').write_text(info);assert 'Pages:           16' in info
layout=K/'P15.3-round120-publication-layout-20261005'
save(D/'publication-preparation.json',{'prepared_utc':now,'atom':'P15.3','accepted_scope':scope,
 'argument_sha256':sha(D/'P15.3-argument.md'),'source_sha256':sha(D/'P15.3-paper.tex'),'pdf_sha256':sha(D/'P15.3-paper.pdf'),'pages':16,
 'whole_final_argument_root_read':True,'literal_LF_read_units':[[1,80],[81,160],[161,282]],
 'changed_LF162_178_184_188_204_214_218_root_reread':True,
 'whole_generated_TeX_source_root_read_claimed':False,
 'local_compilations':[x['exit_code'] for x in build['compilations']],
 'final_missing_glyph_or_overfull_diagnostics':[],
 'visually_read_final_PDF_pages':[1,12,16],
 'layout_images':[{'path':str(layout/f'page-{n}.png'),'sha256':sha(layout/f'page-{n}.png')} for n in [1,12,16]],
 'native_compiler':'PENDING; no success asserted','native_compile_initial_cell':'1472',
 'native_compiler_final_saved_source_request_record':'native-compiler-final-source-request-20261005.json',
 'review':str(canon),'review_sha256':sha(canon),'actual_root_review_binding':str(review_binding),
 'original_closed':False,'unreviewed_new_mathematical_premise_imported':False,
 'editorial_changes_after_assembly':['Typeset variables and unchanged blowup equations.','Repair undefined historical letter S to M and display preceq in math mode.'],
 'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False})

C=R/'campaigns/round-121/P16.5-original-minimal-reference-and-nonbig-carrier-research'
freeze=json.loads((C/'freeze.json').read_text());assert sha(C/'input.json')==freeze['input_sha256']
assert freeze['unchanged_original_task'] and freeze['original_closed'] is False
units=json.loads((C/'mathematical-data-bindings.json').read_text())['units']
for n in [130,131]:
 u=next(x for x in units if x['label']==f'New unreviewed own proposal{n}')
 assert sha(u['path'])==u['sha256']
 save(K/f'P16.5-root-continuation{n}-final-own-proof-reading-and-input-binding.json',{
  'recorded_utc':now,'note':u['path'],'sha256':u['sha256'],'bytes':u['bytes'],
  'whole_final_own_mathematical_note_root_read':True,
  'primary_reading_claim':'Only the selected BJ v4 printed units recorded in frozen121; not whole-book or recursive-foundation verification.',
  'new_nonample_grant_used':False,'independent_acceptance':False,'original_closed':False,
  'frozen_author121_input_sha256':freeze['input_sha256'],'active_scoped119_input_modified_or_hot_feedback_sent':False})

B=K/'current-small-batch119-121-20261005';assert not B.exists();B.mkdir()
items=[]
for no,atom,stem,db,session,scoped in [
 (119,'P16.5','P16.5-bounded-reference-and-numerical-zero-independent-review','review.sqlite',83713,True),
 (121,'P16.5','P16.5-original-minimal-reference-and-nonbig-carrier-research','work.sqlite',86086,False)]:
 P=R/f'campaigns/round-{no}'/stem
 out=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(P/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 obs=json.loads(out.stdout);assert obs['status'] in ['running','completed']
 status=B/f'{atom}-round{no}-public-native-status.json';status.write_text(out.stdout)
 items.append({'round':no,'atom':atom,'directory':str(P),'tool_session_id':session,'observed_status':obs['status'],
 'public_status':str(status),'public_status_sha256':sha(status),'scoped_review_only':scoped,
 'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
 'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'focus':'Independent scoped119 review plus unchanged original121 research on minimal-reference nonample/nonbig cases.'}
save(B/'launch-and-public-status-record.json',batch)
accepted={'atom':'P15.3','round':120,'verdict':'PASS','canonical_result':str(canon),'canonical_sha256':sha(canon),
 'operation_id':c['operationId'],'root_reading_binding':str(review_binding),'exact_scope':scope,
 'standalone_paper':str(D/'P15.3-paper.tex'),'pdf':str(D/'P15.3-paper.pdf'),'pages':16,
 'original_closed':False,'scoped_paper_count_increment':1}
for name in ['active-work.json','checklist-current.json']:
 p=R/name;a=json.loads(p.read_text());assert len(a['fully_solved_original_atoms'])==7
 assert 'P15_3_actual_scoped120' not in a
 if name=='checklist-current.json':assert a['historical_reviewed_scoped_papers']==44
 a['historical_reviewed_scoped_papers']=45;a['P15_3_actual_scoped120']=accepted
 a['current_small_batch']=batch;a['updated_utc']=now;a['remaining_open_original_atoms']=35
 a['prepared_scoped_independent_review119']=items[0]
 a['prepared_scoped_independent_review120'].update({'observed_status':'completed','verdict':'PASS','original_closed':False,'canonical_result':str(canon)})
 a['prepared_full_original_research121']=items[1]
 a['continuation129_actual_scoped_acceptance120']=accepted
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';rows=p.read_text().split('\n');found=0
for i,row in enumerate(rows):
 cells=row.split('\t')
 if cells[0]=='P15.3':
  assert cells[1]=='open' and cells[3]=='1';cells[2]='scoped120_PASS_all_flag_collapse_and_exact_trapezoid_original_open';cells[3]='2';rows[i]='\t'.join(cells);found+=1
 if cells[0]=='P16.5':cells[2]='scoped119_review_running_original121_minimal_reference_and_nonbig_research';rows[i]='\t'.join(cells)
assert found==1;p.write_text('\n'.join(rows))
print(json.dumps({'new_scoped120_verdict':'PASS','reviewed_scoped_papers':45,'fully_solved_originals':7,'remaining_open_originals':35,'active_items':[i['round'] for i in batch['active_items']]},indent=2))
