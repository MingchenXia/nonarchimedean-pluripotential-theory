from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
C=next((R/'campaigns/round-196').iterdir())
D=K/'public-P05.2-continuation247-finite-PA-contact-circuits-and-plane-counterexample'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round196-settled-inspection-LOCALONLY.json').read_text())
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
k=x['campaign']['result'];assert k['verdict']=='FAIL' and len(k['premises'])==3 and len(k['passages'])==11
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    t=json.loads(line)
    if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
        try:n=json.loads(t['item']['text'])
        except (ValueError,TypeError):continue
        if isinstance(n,dict) and set(n)=={'verdict','report','premises','passages'}:finals.append(n)
assert len(finals)==1
n=finals[0]
assert all(n[q]==k[q] for q in ('verdict','report','premises'))
assert len(n['passages'])==len(k['passages'])
for a,b in zip(n['passages'],k['passages']):
    assert all(a[q]==b[q] for q in a)
    assert b['statement']==k['premises'][b['premise']]
    assert isinstance(b['premise'],int) and 0<=b['premise']<3
assert {p['premise'] for p in k['passages'] if not p['url'].startswith('urn:xean:')}=={0,1,2}
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
p=json.loads(req['prompt']);assert set(p)=={'task','argument'}
assert p['task']==json.loads((C/'task.json').read_text()) and p['argument']==(C/'argument.md').read_text()
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','read-only',False)
lines=p['argument'].splitlines();mb=json.loads((C/'mathematical-data-bindings.json').read_text())
for e in mb:
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['argument_inclusive_lf'];assert lines[lo-1:hi]==Path(e['source']).read_text().splitlines()
assert sha(D/'P05.2-paper.tex')=='6cd62476334083dad3496bea5fe35d27ea083e5c23ac29c96e0d263d7aeba082'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
actual=K/'P05.2-round196-actual-canonical-independent-FAIL-review-20261007.json'
native=K/'P05.2-round196-native-model-final-FAIL-review-20261007.json'
binding=K/'P05.2-round196-whole-finite-contact-FAIL-review-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=196,continuation=247,atom='P05.2',verdict='FAIL',canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),one_valid_native_structured_final=True,native_final_report_premises_verdict_equal_canonical=True,native_passage_math_equal_canonical=True,kernel_only_passage_additions=['id','statement'],canonical_operation_id=k['operationId'],premises=3,passages=11,all_premises_have_indexed_external_source_coverage=True,task_only_passage_excluded_from_external_coverage=True,exact_decoded_native_task_and_argument_equal_frozen_input=True,all_frozen_whole_math_units_and_lf_bindings_verified=True,complete_caller_grants=['A224','B225','R230'],all_harmless_clarifications_supplied=True,whole_actual_canonical_report_premises_and_passages_root_read=True,whole247_tex693_argument710_ledger62_and_five_native_final_notes_previously_root_read=True,source_sha256=sha(D/'P05.2-paper.tex'),argument_sha256=sha(D/'argument.md'),model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],frozen_task_sha256=f['task_sha256'],frozen_argument_sha256=f['argument_sha256'],frozen_settings_sha256=f['settings_sha256'],new_accepted_paper=False,original_closed=False,material_findings=['Unconditional Lemma3 Strict affine floor lacks PA PC/nonnegative relation-cost hypothesis. Relative PA on the balanced line with local slopes(-1,-1) has no zero-cost relation but no strict floor. The hypothesis must be explicitly repaired.','The old endpoint is separable on the product of the cross with the z-line; its roof obstacle is nonseparable. It does not supply the expressly requested nonseparable endpoint.'],reader_checked_remaining_mathematics_but_no_whole_paper_acceptance=True,native194_registration_failure_preserved=True,source_preserved_without_silent_repair=True,no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
(D/'independent-whole-paper-FAIL196-20261007.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==76
    j['P05_2_latest_whole_independent_review']=dict(round=196,continuation=247,verdict='FAIL',binding=str(binding),binding_sha256=sha(binding),material_findings=b['material_findings'],new_accepted_paper=False,original_closed=False)
    j['updated_utc']=datetime.now(timezone.utc).isoformat()
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=196,verdict='FAIL',binding_sha256=sha(binding),canonical_operation_id=k['operationId'],accepted_papers_unchanged=76,original_closed=False),indent=2))
