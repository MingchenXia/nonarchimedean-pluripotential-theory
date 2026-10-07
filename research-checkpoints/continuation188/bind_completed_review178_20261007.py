from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-178').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round178-completed-inspection-second-LOCALONLY.json').read_text());ca=x['campaign']
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
assert len(kernel['premises'])==7 and len(native['passages'])==len(kernel['passages'])==16
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
canonical=K/'P16.4-round178-actual-canonical-independent-review-20261007.json'
native_file=K/'P16.4-round178-native-model-final-review-20261007.json'
binding=K/'P16.4-round178-whole-partial-review-binding-20261007.json'
assert not any(p.exists() for p in (canonical,native_file,binding))
canonical.write_text(json.dumps(kernel,ensure_ascii=False,indent=2)+'\n');native_file.write_text(json.dumps(native,ensure_ascii=False,indent=2)+'\n')
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':178,'atom':'P16.4','verdict':'PASS','operation_id':kernel['operationId'],'reported_at':kernel['reportedAt'],
 'canonical_review':str(canonical),'canonical_review_sha256':sha(canonical),'native_model_final':str(native_file),'native_model_final_sha256':sha(native_file),
 'entire_report_all_premises_and_passages_root_read':True,'premises':7,'passages':16,'all_zero_based_exact_statement_bindings_verified':True,'external_coverage':coverage,'passage_normalization':normalizations,
 'task_only_passages_excluded_from_external_coverage':[p['id'] for p in kernel['passages'] if not p['url'].startswith(('http://','https://'))],
 'kernel_report_premises_and_quotes_equal_native_final':True,'exact_decoded_native_task_and_argument_equal_entire_frozen_inputs':True,
 'native_prompt_sha256':hashlib.sha256(request['prompt'].encode()).hexdigest(),'frozen_task_sha256':freeze['task_sha256'],'frozen_argument_sha256':freeze['argument_sha256'],'frozen_settings_sha256':freeze['settings_sha256'],
 'model':request['model'],'reasoning':request['reasoning'],'child_sandbox':request['sandbox'],'caller_grants':[],
 'accepted_partial_scope':'All complete characteristic-zero non-Archimedean real-valued fields, including trivial/discrete/nondiscrete valuations and positive residue characteristic, arbitrary-genus smooth geometrically integral projective curves and actual ample rational L. Genuine raw-degree all-point E1 curvature operator, every-E1-test integrability, weighted energy identity and arbitrary joint decreasing-net continuity, actual affine finite-energy segment derivative, reference covariance and complete-field pushforward. No residue-characteristic-zero or algebraic-closure hypothesis.',
 'whole_partial_manuscript_accepted':True,'original_closed':False,'new_accepted_scoped_paper':True,
 'residual_original_gaps':'Arbitrary-dimensional finite-energy operators, original target characterization/attainment/every-solution uniqueness, strict locality/comparison, normalized actual-potential compactness and general envelope continuity/orthogonality/both-sign outer differentiation are not supplied by this curve manuscript. Separate217 general mixed-operator manuscript remains independently179 active and is not granted here.',
 'root_recursive_primary_proof_reading_claimed':False,'private_active_output_read':False,'hot_feedback_sent':False,'protected_editor_unchanged':True}
binding.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'round':178,'verdict':'PASS','binding':str(binding),'binding_sha256':sha(binding),'original_closed':False,'whole_partial_paper_accepted':True},indent=2))
