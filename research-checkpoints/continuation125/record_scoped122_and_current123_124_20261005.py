from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
R=Path('/workspace/research');K=R/'root-checks';D=R/'deliverables/scoped-P16.5-round122'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,d):
 assert not p.exists(),str(p);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
c=K/'P16.5-round122-actual-scoped-independent-review-20261005.json';a=json.loads(c.read_text())
assert a['verdict']=='PASS' and len(a['premises'])==18 and len(a['passages'])==30
assert all(p['statement']==a['premises'][p['premise']] for p in a['passages'])
assert sum(p['url'].startswith('https://') for p in a['passages'])==29
assert sum(p['url']=='urn:xean:task' and p['premise']==17 for p in a['passages'])==1
m=json.loads((D/'publication-preparation.json').read_text())
for n,k in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(D/n)==m[k]
assert m['whole_final_publication_argument_separately_root_read'] and m['final_local_build_returns']==[0,0,0]
assert m['actual_visual_pages']==[1,4,7]
m.update({'PDF_pages':7,'native_compiler_final_source_pending_cell':1581})
(D/'publication-preparation.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
save(D/'native-compiler-final-source-request-20261005.json',{'requested_utc':now,'source':str(D/'P16.5-paper.tex'),'source_sha256':sha(D/'P16.5-paper.tex'),'tool_cell_id':1581,'status':'PENDING','observed_success':False})
b={'recorded_utc':now,'atom':'P16.5','round':122,'verdict':'PASS','original_closed':False,'scope':m['scope'],
 'canonical_report':str(c),'canonical_report_sha256':sha(c),'whole_report_all18_premises_and_all30_literal_passages_root_read':True,
 'external_premises':17,'external_https_passages':29,'inline_G0_grant_premises':1,'inline_task_URI_passages':1,
 'inline_task_URI':'urn:xean:task','all30_statements_match_indexed_premises':True,'all_urls_https_claimed':False,
 'final_publication_argument_sha256':sha(D/'P16.5-argument.md'),'final_publication_tex_sha256':sha(D/'P16.5-paper.tex'),
 'final_publication_pdf_sha256':sha(D/'P16.5-paper.pdf'),'whole_final_argument_root_read':True,
 'PDF_pages':7,'actual_visual_pages':[1,4,7],'local_final_build_returns':[0,0,0],
 'native_compiler_success_asserted':False,'larger_intrinsic_extension_certified_by122':False}
save(K/'P16.5-round122-actual-scoped-review-root-reading-and-publication-binding-20261005.json',b)
Q=K/'current-small-batch123-124-20261005';Q.mkdir(exist_ok=False);items=[]
for rd,label,db,pty,scoped in [(123,'P16.5-original-intrinsic-nef-variational-and-general-reference-research','work.sqlite',59957,False),(124,'P16.5-entire-intrinsic-nef-weighted-outer-and-dual-independent-review','review.sqlite',49744,True)]:
 C=R/f'campaigns/round-{rd}'/label
 out=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 st=json.loads(out.stdout);p=Q/f'P16.5-round{rd}-public-native-status.json';save(p,st)
 assert st['status'] in ['running','completed']
 items.append({'round':rd,'atom':'P16.5','directory':str(C),'database':db,'tool_session_id':pty,'observed_status':st['status'],'public_status':str(p),'public_status_sha256':sha(p),'scoped_review_only':scoped,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','focus':'Original123 general intrinsic variational and reference research plus independent124 full intrinsic nef operator, weighted nets, outer derivatives, weak-usc and dual/coercivity review.'}
save(Q/'launch-and-public-status-record.json',batch)
p=K/'P16.5-nef-polar-capacity-and-original-observable-control-draft-20261005-continuation136.md'
z={'recorded_utc':now,'own_proposal':str(p),'own_proposal_sha256':sha(p),'whole_final_own_proof_root_read':True,'independently_accepted':False,'original_closed':False,'active123_124_frozen_inputs_modified':False,'hot_feedback_sent':False,'scope':'Positive-mass intrinsic nef pole capacity, finite-energy polar test, uniform polar estimates, and conditional actual ample-plus-divisor PL-observable control for I-Cauchy energy-bounded nets; no attainment or uniqueness.'}
save(K/'P16.5-root-continuation136-final-own-proof-reading-and-source-binding.json',z)
for n in ['active-work.json','checklist-current.json']:
 p=R/n;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==7 and x['historical_reviewed_scoped_papers']==46
 x.update({'updated_utc':now,'historical_reviewed_scoped_papers':47,'current_small_batch':batch,'P16_5_actual_scoped122':b,'continuation136_unreviewed_nef_proposal':z,'goal_state':'7/42 original problems solved;35 remain open;47 independently reviewed scoped papers. Continue small batches until the requested goal.','github_pending_checkpoint':'continuation125 preparation'})
 if n=='active-work.json':x['next_work']='Publish reviewed bounded-nef standalone paper and unreviewed polar proposal; read native123/124 canonical results when complete; continue full original variational attainment and uniqueness.'
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';ls=p.read_text().split('\n')
for i,line in enumerate(ls):
 if line.startswith('P16.5\t'):
  row=line.split('\t');assert row[1]=='open';row[2]='Scoped122 PASS: all nef bounded products and continuous-obstacle both-sign derivatives; full original123 and intrinsic scoped124 active; own136 polar proposal unreviewed.';row[3]=str(int(row[3])+1);ls[i]='\t'.join(row)
p.write_text('\n'.join(ls))
print(json.dumps({'scoped122':'PASS','scoped_count':47,'original_count':7,'open_originals':35,'native_batch':[123,124]},indent=2))
