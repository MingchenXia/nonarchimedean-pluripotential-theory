from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'; C=next((R/'campaigns/round-185').iterdir())
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round185-completed-inspection-LOCALONLY.json').read_text()); ca=x['campaign']
assert ca['status']=='completed' and ca['error'] is None
k=ca['result']; assert k['verdict']=='PASS'
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    t=json.loads(line)
    if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
        try: n=json.loads(t['item']['text'])
        except (ValueError,TypeError): continue
        if isinstance(n,dict) and set(n)=={'verdict','report','premises','passages'}: finals.append(n)
assert len(finals)==1; n=finals[0]
assert all(k[q]==n[q] for q in ('verdict','report','premises'))
assert len(k['premises'])==1 and len(k['passages'])==len(n['passages'])==4
normalizations=[]
for i,(a,b) in enumerate(zip(n['passages'],k['passages'])):
    assert {q:b[q] for q in ('premise','url','quote')}==a
    assert b['id']==k['operationId']+'/'+str(i)
    assert b['premise']==0 and b['statement']==k['premises'][0]
    normalizations.append(dict(index=i,id=b['id'],unchanged_model_fields=['premise','url','quote'],kernel_added_fields=['id','statement']))
external=[p for p in k['passages'] if p['url'].startswith(('https://','http://'))]; assert len(external)==3
prompt=json.loads(req['prompt']); assert set(prompt)=={'task','argument'}
assert prompt['task']==json.loads((C/'task.json').read_text()) and prompt['argument']==(C/'argument.md').read_text()
assert req['model']=='gpt-6.1-sol' and req['reasoning']=='xhigh' and req['sandbox']=='read-only' and req['shell'] is False
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
canonical=K/'P16.4-round185-actual-canonical-independent-review-20261007.json'
native=K/'P16.4-round185-native-model-final-review-20261007.json'
binding=K/'P16.4-round185-whole-partial-review-binding-20261007.json'
assert not any(p.exists() for p in (canonical,native,binding))
canonical.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n'); native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=185,atom='P16.4',verdict='PASS',operation_id=k['operationId'],reported_at=k['reportedAt'],
    canonical_review=str(canonical),canonical_review_sha256=sha(canonical),native_model_final=str(native),native_model_final_sha256=sha(native),
    entire_report_all_premises_and_passages_root_read=True,premises=1,passages=4,all_zero_based_exact_statement_bindings_verified=True,
    external_coverage=[dict(premise_index=0,exact_statement=k['premises'][0],external_passage_ids=[p['id'] for p in external],primary_urls=sorted({p['url'] for p in external}))],passage_normalization=normalizations,
    task_only_passages_excluded_from_external_coverage=[p['id'] for p in k['passages'] if not p['url'].startswith(('https://','http://'))],
    kernel_report_premises_and_quotes_equal_native_final=True,exact_decoded_native_task_and_argument_equal_entire_frozen_inputs=True,
    native_prompt_sha256=hashlib.sha256(req['prompt'].encode()).hexdigest(),frozen_task_sha256=f['task_sha256'],frozen_argument_sha256=f['argument_sha256'],frozen_settings_sha256=f['settings_sha256'],
    model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],caller_grants=['O','D','N','T'],
    accepted_partial_scope='On split P^1_K over every complete characteristic-zero real-valued non-Archimedean field K, every actual ample rational line bundle and continuous psh reference, every positive Radon target of raw mass deg L: all actual E1-test integrability iff finite continuous dual iff an actual E1 solution exists. Every solution is unique modulo a finite constant at every analytic point, including common poles, and is a variational maximizer. Includes trivial/nontrivial/nondiscrete/non-algebraically-closed fields and positive residue characteristic, without target support or invariance restrictions. Natural-log kernel dual identities are for the standard anchored upstairs construction; rational energy/dual scale quadratically and raw measure linearly.',
    whole_partial_manuscript_accepted=True,original_closed=False,new_accepted_scoped_paper=True,
    residual_original_gaps='No nontrivially valued higher-genus or nonsplit genus-zero curve equation, general-variety prescribed-target equation, or general compactness/envelope replacement. Separate singular/nonample/nonprojective/nonalgebraizable axes remain open.',
    root_recursive_primary_proof_reading_claimed=False,private_active_output_read=False,hot_feedback_sent=False,protected_editor_unchanged=True)
binding.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=185,verdict='PASS',binding=str(binding),binding_sha256=sha(binding),original_closed=False),indent=2))
