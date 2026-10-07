from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-181').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round181-completed-inspection-LOCALONLY.json').read_text());ca=x['campaign']
assert ca['status']=='completed' and ca['error'] is None
kernel=ca['result'];assert kernel['verdict']=='PASS'
request=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
message=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert message['exitCode']==0 and not message['failed'] and not message['isCanceled']
finals=[]
for line in message['stdout'].splitlines():
 item=json.loads(line)
 if item.get('type')=='item.completed' and item.get('item',{}).get('type')=='agent_message':
  try:f=json.loads(item['item']['text'])
  except (ValueError,TypeError):continue
  if isinstance(f,dict) and set(f)=={'verdict','report','premises','passages'}:finals.append(f)
assert len(finals)==1;native=finals[0]
assert native['verdict']==kernel['verdict'] and native['report']==kernel['report'] and native['premises']==kernel['premises']
assert len(kernel['premises'])==7 and len(native['passages'])==len(kernel['passages'])==12
normalizations=[]
for i,(a,b) in enumerate(zip(native['passages'],kernel['passages'])):
 assert {k:b[k] for k in ('premise','url','quote')}==a
 assert b['id']==kernel['operationId']+'/'+str(i)
 assert 0<=b['premise']<7 and b['statement']==kernel['premises'][b['premise']]
 normalizations.append({'index':i,'id':b['id'],'unchanged_model_fields':['premise','url','quote'],'kernel_added_fields':['id','statement']})
coverage=[]
for i,statement in enumerate(kernel['premises']):
 passages=[p for p in kernel['passages'] if p['premise']==i and p['url'].startswith(('http://','https://'))];assert passages
 coverage.append({'premise_index':i,'exact_statement':statement,'external_passage_ids':[p['id'] for p in passages],'primary_urls':sorted(set(p['url'] for p in passages))})
prompt=json.loads(request['prompt']);assert set(prompt)=={'task','argument'}
assert prompt['task']==json.loads((C/'task.json').read_text()) and prompt['argument']==(C/'argument.md').read_text()
assert request['model']=='gpt-6.1-sol' and request['reasoning']=='xhigh' and request['sandbox']=='read-only' and request['shell'] is False
freeze=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==freeze[key]
canonical=K/'P16.4-round181-actual-canonical-independent-review-20261007.json'
native_file=K/'P16.4-round181-native-model-final-review-20261007.json'
binding=K/'P16.4-round181-whole-partial-review-binding-20261007.json'
assert not any(p.exists() for p in (canonical,native_file,binding))
canonical.write_text(json.dumps(kernel,ensure_ascii=False,indent=2)+'\n');native_file.write_text(json.dumps(native,ensure_ascii=False,indent=2)+'\n')
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':181,'atom':'P16.4','verdict':'PASS','operation_id':kernel['operationId'],'reported_at':kernel['reportedAt'],
 'canonical_review':str(canonical),'canonical_review_sha256':sha(canonical),'native_model_final':str(native_file),'native_model_final_sha256':sha(native_file),
 'entire_report_all_premises_and_passages_root_read':True,'premises':7,'passages':12,'all_zero_based_exact_statement_bindings_verified':True,'external_coverage':coverage,'passage_normalization':normalizations,
 'task_only_passages_excluded_from_external_coverage':[p['id'] for p in kernel['passages'] if not p['url'].startswith(('http://','https://'))],
 'kernel_report_premises_and_quotes_equal_native_final':True,'exact_decoded_native_task_and_argument_equal_entire_frozen_inputs':True,
 'native_prompt_sha256':hashlib.sha256(request['prompt'].encode()).hexdigest(),'frozen_task_sha256':freeze['task_sha256'],'frozen_argument_sha256':freeze['argument_sha256'],'frozen_settings_sha256':freeze['settings_sha256'],
 'model':request['model'],'reasoning':request['reasoning'],'child_sandbox':request['sandbox'],'caller_grants':['O'],
 'accepted_partial_scope':'All complete characteristic-zero real-valued non-Archimedean fields, including trivial/discrete/nondiscrete valuations without algebraic-closure or residue-characteristic-zero restrictions; smooth geometrically integral projective X of positive dimension and actual ample rational L. Actual all-point E1 strict Borel winner mixed locality, ordinary open locality, mixed comparison and separately slotwise pure comparison, conditional only on entire already independently accepted O217 operator and its harmless normalization clarifications; raw mass V unchanged.',
 'whole_partial_manuscript_accepted':True,'original_closed':False,'new_accepted_scoped_paper':True,
 'residual_original_gaps':'Normalized actual-potential compactness, general-field envelope/orthogonality/both-sign outer differentiation, intrinsic prescribed-target finite-energy/finite-dual characterization, actual attainment and every-solution uniqueness remain unestablished. No original equation closure follows from locality/comparison.',
 'task_passage_observation':'Report calls the O task passage unindexed, but the actual native structured passage has premise0. Its actual canonical/native fields are preserved. This task-only passage is excluded from external premise coverage; premise0 is independently covered by its two primary BE passages. No synthetic passage or external O source was added.','root_recursive_primary_proof_reading_claimed':False,'private_active_output_read':False,'hot_feedback_sent':False,'protected_editor_unchanged':True}
binding.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'round':181,'verdict':'PASS','binding':str(binding),'binding_sha256':sha(binding),'original_closed':False,'whole_partial_paper_accepted':True},indent=2))
