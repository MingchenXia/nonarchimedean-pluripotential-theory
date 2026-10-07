from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-200').iterdir())
D=K/'public-P05.2-continuation255-coupled-nonPA-and-regularizable-raw-completion'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round200-settled-inspection-LOCALONLY.json').read_text())
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
k=x['campaign']['result']
assert k['verdict']=='FAIL' and len(k['premises'])==3 and len(k['passages'])==13
req=next(z['data']['payload'] for z in x['records'] if z['kind']=='xean.call.request')
msg=next(z['data']['message'] for z in x['records'] if z['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    z=json.loads(line)
    if z.get('type')=='item.completed' and z.get('item',{}).get('type')=='agent_message':
        try: n=json.loads(z['item']['text'])
        except (ValueError,TypeError): continue
        if isinstance(n,dict) and set(n)=={'verdict','report','premises','passages'}:finals.append(n)
assert len(finals)==1
n=finals[0]
assert all(n[q]==k[q] for q in ('verdict','report','premises'))
assert len(n['passages'])==len(k['passages'])
for a,b in zip(n['passages'],k['passages']):
    assert all(a[q]==b[q] for q in a)
    assert b['statement']==k['premises'][b['premise']]
    assert isinstance(b['premise'],int) and 0<=b['premise']<3
coverage=sorted({p['premise'] for p in k['passages'] if not p['url'].startswith('urn:xean:')})
assert coverage==[0,1,2]
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
prompt=json.loads(req['prompt'])
assert set(prompt)=={'task','argument'}
assert prompt['task']==json.loads((C/'task.json').read_text())
assert prompt['argument']==(C/'argument.md').read_text()
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','read-only',False)
lines=prompt['argument'].splitlines(); units=json.loads((C/'mathematical-data-bindings.json').read_text())
assert len(units)==16
for e in units:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['argument_inclusive_lf']; assert lines[lo-1:hi]==Path(e['source']).read_text().splitlines()
assert sha(D/'P05.2-paper.tex')=='edb6cc4729d7143513636aa66491af3e1805a01bf7c2bd4e5dd800ee50573403'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P05.2-round200-actual-canonical-independent-FAIL-review-20261007.json'
native=K/'P05.2-round200-native-model-final-FAIL-review-20261007.json'
binding=K/'P05.2-round200-whole-coupled-nonPA-FAIL-review-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding,D/'independent-whole-paper-FAIL200-20261007.json'))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n')
native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
b=dict(recorded_utc=now,round=200,continuation=255,atom='P05.2',verdict='FAIL',canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),one_valid_native_structured_final=True,native_final_report_premises_verdict_equal_canonical=True,native_passage_math_equal_canonical=True,kernel_only_passage_additions=['id','statement'],canonical_operation_id=k['operationId'],premises=3,passages=13,external_primary_premise_coverage=coverage,unresolved_primary_premise_indices=[],all_zero_based_exact_statement_bindings_verified=True,task_only_passages_excluded_from_external_coverage=[12],exact_decoded_native_task_and_argument_equal_frozen_input=True,all16_frozen_whole_math_units_and_lf_bindings_verified=True,complete_caller_grants=['A224','B225','R230'],all_unchanged_clarifications_supplied=True,whole_actual_canonical_report_premises_and_all13_passages_root_read=True,whole255_tex1367_argument1371_ledger50_material_changes_and_seven_exact_final_notes_previously_root_read=True,source_sha256=sha(D/'P05.2-paper.tex'),argument_sha256=sha(D/'argument.md'),model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],frozen_task_sha256=f['task_sha256'],frozen_argument_sha256=f['argument_sha256'],frozen_settings_sha256=f['settings_sha256'],material_findings=['Theorem11 uniform-continuous extension and native note n4 unqualified uniform-continuity guarantee are false for global bounded-continuous-test weak uniformity. The proof supplies continuity under uniform convergence and quantitative continuity only with a common bound relative to gamma. This is a MATERIAL scope change.','Literal balanced line gamma=abs(x), A_n=abs(x-2n), B_n=abs(x-2n-1/(8n)): uniform distance1/(8n), raw measures2delta at shifted points, fixed C_b test sin(pi*x^2) separates their integrals by a quantity tending to2.','Real rational-affine category: alternating shifts a_j=4j or4j+1, b_j with opposite shifts, A/B average abs(x-a_j)/n and abs(x-b_j)/n for even n; distance2/n, fixed bounded Lipschitz8-periodic test separates measures by exactly1. Relative bounds grow, so uniformly convergent-family completion remains consistent.'],unresolved_external_certification=[],reader_discussed_other_arguments_but_no_whole_paper_acceptance=True,failed_source_preserved_without_silent_repair=True,new_accepted_paper=False,original_closed=False,no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
(D/'independent-whole-paper-FAIL200-20261007.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==76
    j.update(updated_utc=now,P05_2_latest_whole_independent_review=dict(round=200,continuation=255,verdict='FAIL',binding=str(binding),binding_sha256=sha(binding),material_findings=b['material_findings'],unresolved_external_certification=b['unresolved_external_certification'],new_accepted_paper=False,original_closed=False))
    j['P05_2_latest_unreviewed_native197_paper'].update(independent_verdict='FAIL',new_accepted_paper=False)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=200,verdict='FAIL',binding_sha256=sha(binding),canonical_operation_id=k['operationId'],accepted_papers_unchanged=76,original_closed=False),indent=2))
