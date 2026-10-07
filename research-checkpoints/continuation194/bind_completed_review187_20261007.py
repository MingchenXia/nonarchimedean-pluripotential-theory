from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'; C=next((R/'campaigns/round-187').iterdir())
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round187-completed-inspection-LOCALONLY.json').read_text()); ca=x['campaign']
assert ca['status']=='completed' and ca['error'] is None
k=ca['result']; assert k['verdict']=='PASS'
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request'); msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    t=json.loads(line)
    if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
        try: n=json.loads(t['item']['text'])
        except (ValueError,TypeError): continue
        if isinstance(n,dict) and set(n)=={'verdict','report','premises','passages'}: finals.append(n)
assert len(finals)==1; n=finals[0]; assert all(k[q]==n[q] for q in ('verdict','report','premises'))
assert len(k['premises'])==8 and len(k['passages'])==len(n['passages'])==10
normalizations=[]
for i,(a,b) in enumerate(zip(n['passages'],k['passages'])):
    assert {q:b[q] for q in ('premise','url','quote')}==a
    assert b['id']==k['operationId']+'/'+str(i)
    assert 0<=b['premise']<8 and b['statement']==k['premises'][b['premise']]
    normalizations.append(dict(index=i,id=b['id'],unchanged_model_fields=['premise','url','quote'],kernel_added_fields=['id','statement']))
coverage=[]
for i,premise in enumerate(k['premises']):
    ps=[p for p in k['passages'] if p['premise']==i and p['url'].startswith(('https://','http://'))]; assert ps
    coverage.append(dict(premise_index=i,exact_statement=premise,external_passage_ids=[p['id'] for p in ps],primary_urls=sorted({p['url'] for p in ps})))
prompt=json.loads(req['prompt']); assert set(prompt)=={'task','argument'}
assert prompt['task']==json.loads((C/'task.json').read_text()) and prompt['argument']==(C/'argument.md').read_text()
assert req['model']=='gpt-6.1-sol' and req['reasoning']=='xhigh' and req['sandbox']=='read-only' and req['shell'] is False
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
canonical=K/'P05.2-round187-actual-canonical-independent-review-20261007.json'; native=K/'P05.2-round187-native-model-final-review-20261007.json'; binding=K/'P05.2-round187-whole-partial-review-binding-20261007.json'
assert not any(p.exists() for p in (canonical,native,binding))
canonical.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n'); native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=187,atom='P05.2',verdict='PASS',operation_id=k['operationId'],reported_at=k['reportedAt'],canonical_review=str(canonical),canonical_review_sha256=sha(canonical),native_model_final=str(native),native_model_final_sha256=sha(native),
    entire_report_all_premises_and_passages_root_read=True,premises=8,passages=10,all_zero_based_exact_statement_bindings_verified=True,external_coverage=coverage,passage_normalization=normalizations,task_only_passages_excluded_from_external_coverage=[],kernel_report_premises_and_quotes_equal_native_final=True,
    exact_decoded_native_task_and_argument_equal_entire_frozen_inputs=True,native_prompt_sha256=hashlib.sha256(req['prompt'].encode()).hexdigest(),frozen_task_sha256=f['task_sha256'],frozen_argument_sha256=f['argument_sha256'],frozen_settings_sha256=f['settings_sha256'],model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],caller_grants=[],
    accepted_partial_scope='On the saturated unit-weight U(3,4) fan, for A>=0,B>0,C>B real and rational epsilon>0, reference Gamma=Aeta+Bh has explicit strict local supports in the disclosed active-coefficient convention and positive recession slopes; its exact all-competitor envelope P=Gamma+Bu_epsilon is finite real PA on a rational structure, with raw masses4(A+B)^2 and twice B(4A+3B), degree4A^2+16AB+10B^2, contact integral-4(C-B)epsilon(A+B)^2. Integral parameters give literal integral-slope/rational-constant endpoints and the literal raw finite operator. Separate obstacles v_n for Gamma=h have exact nonintegral envelopes Q_n and uniform literal approximation gap>=1/(4n). No general real operator extension or all-obstacle pair regularity is assumed.',
    whole_partial_manuscript_accepted=True,original_closed=False,new_accepted_scoped_paper=True,residual_original_gaps='General necessary-and-sufficient structural characterization of all balanced pairs and admissible obstacles remains open. All-obstacle real regularity on this fan and stronger unspecified smoothness hypotheses are not proved or disproved. The simplest literal pair is nonregular, while its selected main endpoint has a valid raw measure.',root_recursive_primary_proof_reading_claimed=False,private_active_output_read=False,hot_feedback_sent=False,protected_editor_unchanged=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=187,verdict='PASS',binding=str(binding),binding_sha256=sha(binding),original_closed=False),indent=2))
