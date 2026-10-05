from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess

R=Path('/workspace/research');K=R/'root-checks';D=R/'deliverables/scoped-P16.5-round119'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,a):
 assert not p.exists(),str(p);p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
canonical=K/'P16.5-round119-actual-scoped-independent-review-20261005.json'
d=json.loads(canonical.read_text());assert d['verdict']=='PASS'
assert d['operationId']=='3d43dcae-5261-4bd5-be54-c14f2644119c'
assert len(d['premises'])==10 and len(d['passages'])==2694
assert all(p['statement']==d['premises'][p['premise']] and p['url'].startswith('https://') for p in d['passages'])
groups=K/'P16.5-round119-lossless-unique-passage-reading-groups-20261005.json';g=json.loads(groups.read_text())
assert g['canonical_result_sha256']==sha(canonical) and len(g['unique_groups'])==156
assert sum(p['multiplicity'] for p in g['unique_groups'])==2694
ids=[i for p in g['unique_groups'] for i in p['passage_ids']]
assert len(ids)==len(set(ids))==2694 and set(ids)=={p['id'] for p in d['passages']}
pub=json.loads((D/'publication-preparation.json').read_text())
for name,key in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(D/name)==pub[key]
pub['actually_visually_read_final_PDF_pages']=[1,8,15]
pub['native_compiler_final_source_pending_cell']=1553
(D/'publication-preparation.json').write_text(json.dumps(pub,indent=2)+'\n')
save(D/'native-compiler-final-source-request-20261005.json',{'requested_utc':now,'source':str(D/'P16.5-paper.tex'),'source_sha256':sha(D/'P16.5-paper.tex'),'tool_cell_id':1553,'observed_success':False,'status':'PENDING'})
b={'recorded_utc':now,'atom':'P16.5','round':119,'verdict':'PASS','canonical_report':str(canonical),'canonical_report_sha256':sha(canonical),
 'whole_actual_report_and_all10_premises_root_read':True,'all156_unique_lossless_passage_groups_root_read':True,
 'actual_passage_count':2694,'distinct_exact_passage_groups':156,'lossless_groups_path':str(groups),'lossless_groups_sha256':sha(groups),
 'every_actual_passage_id_covered_exactly_once':True,'all_indexed_statements_match':True,'all_actual_urls_https':True,
 'actual_passage_minus_one_count':0,'report_minus_one_sentence_discrepancy_preserved':True,
 'missing_passage_or_premise_not_invented':True,'publication':str(D),'publication_argument_sha256':sha(D/'P16.5-argument.md'),
 'publication_source_sha256':sha(D/'P16.5-paper.tex'),'publication_pdf_sha256':sha(D/'P16.5-paper.pdf'),'publication_PDF_pages':15,
 'whole_final_argument_root_read':True,'actual_visual_PDF_pages':[1,8,15],'local_compiles':[0,0],
 'scoped_only':True,'original_closed':False,'original114_verdict_preserved':'INCONCLUSIVE','native117_candidate_preserved':False,
 'scope':'Every bounded genuine prescribed-divisorial reference change and every actual numerical-zero rational bundle, with every indispensable Section1--8 construction, original metric operator, energy, targets, both continuous signs, attainment and uniqueness in the proved cones.'}
save(K/'P16.5-round119-actual-scoped-review-root-reading-and-publication-binding-20261005.json',b)
Q=K/'current-small-batch122-123-20261005';Q.mkdir(exist_ok=False);items=[]
for rd,label,db,pty,scoped in [(122,'P16.5-nef-bounded-products-and-continuous-obstacle-independent-review','review.sqlite',82906,True),(123,'P16.5-original-intrinsic-nef-variational-and-general-reference-research','work.sqlite',59957,False)]:
 c=R/f'campaigns/round-{rd}'/label
 out=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 d=json.loads(out.stdout);p=Q/f'P16.5-round{rd}-public-native-status.json';save(p,d)
 assert d['status'] in ['running','completed']
 items.append({'round':rd,'atom':'P16.5','directory':str(c),'database':db,'tool_session_id':pty,'observed_status':d['status'],
  'public_status':str(p),'public_status_sha256':sha(p),'scoped_review_only':scoped,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'focus':'Independent scoped122 bounded-nef review plus unchanged original123 research on entire intrinsic nef variational attainment and general reference/nonbig gates.'}
save(Q/'launch-and-public-status-record.json',batch)
for name in ['active-work.json','checklist-current.json']:
 p=R/name;a=json.loads(p.read_text());assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==45
 a['historical_reviewed_scoped_papers']=46;a['updated_utc']=now;a['current_small_batch']=batch;a['P16_5_actual_scoped119']=b
 a['prepared_full_original_research123']=json.loads((R/'campaigns/round-123/P16.5-original-intrinsic-nef-variational-and-general-reference-research/freeze.json').read_text())
 for no in [134,135]:a[f'continuation{no}_unreviewed_nef_proposal']=json.loads((K/f'P16.5-root-continuation{no}-final-own-proof-reading-and-native-input-binding.json').read_text())
 a['goal_state']='7/42 original problems solved;35 remain open;46 independently reviewed scoped papers. Continue small batches until the requested goal.'
 a['github_pending_checkpoint']='continuation124 preparation'
 if name=='active-work.json':a['next_work']='Publish exact scoped119 paper; read native122/123 canonical results when complete and continue entire original equations without promoting partial scopes.'
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().split('\n')
for i,line in enumerate(lines):
 if line.startswith('P16.5\t'):
  row=line.split('\t');assert row[1]=='open';row[2]='Scoped119 PASS: bounded reference changes and entire actual numerical-zero equation; original121 partial; original123 active.';row[3]=str(int(row[3])+1);lines[i]='\t'.join(row)
p.write_text('\n'.join(lines))
print(json.dumps({'new_scoped119_verdict':'PASS','scoped_count':46,'original_count':7,'remaining_originals':35,'current_native_batch':[i['round'] for i in items]},indent=2))
