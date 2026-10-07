from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-207').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round207-settled-inspection-LOCALONLY.json').read_text());r=x['campaign']['result']
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
assert r['verdict']=='INCONCLUSIVE' and len(r['premises'])==25 and len(r['passages'])==27
req=next(z['data']['payload'] for z in x['records'] if z['kind']=='xean.call.request')
msg=next(z['data']['message'] for z in x['records'] if z['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
n=json.loads((K/'round207-exact-native-FINAL-for-root-LOCALONLY.json').read_text())
assert n['verdict']==r['verdict'] and n['report']==r['report'] and n['premises']==r['premises']
assert len(n['passages'])==len(r['passages'])+1==28
excluded=n['passages'][-1]
assert excluded['url']=='urn:xean:task' and excluded['premise']==25
for a,b in zip(n['passages'],r['passages']):
    assert all(a[q]==b[q] for q in ['premise','url','quote'])
    assert b['statement']==r['premises'][b['premise']]
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','read-only',False)
p=json.loads(req['prompt']);assert p['task']==json.loads((C/'task.json').read_text())
assert p['argument']==(C/'argument.md').read_text()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256'),('original-task.json','original_task_sha256')]:assert sha(C/name)==f[key]
for e in json.loads((C/'mathematical-data-bindings.json').read_text()):
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['argument_inclusive_lf'];assert p['argument'].splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
covered=sorted({a['premise'] for a in r['passages'] if not a['url'].startswith('urn:')})
missing=sorted(set(range(25))-set(covered));assert missing==[4,8,9]
for a in r['passages']:assert 0<=a['premise']<25 and a['quote']
actual=K/'P16.4-round207-actual-canonical-independent-INCONCLUSIVE-review-20261007.json'
native=K/'P16.4-round207-exact-native-model-final-INCONCLUSIVE-review-20261007.json'
binding=K/'P16.4-round207-whole-all-genus-curve-INCONCLUSIVE-review-binding-20261007.json'
assert not any(a.exists() for a in [actual,native,binding])
actual.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=207,continuation=269,atom='P16.4',
verdict='INCONCLUSIVE',operation_id=r['operationId'],reported_utc=r['reportedAt'],
canonical_review=str(actual),canonical_review_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
entire_report_all25premises_all27registered_and28native_passages_root_read=True,exact_native_canonical_report_and_premises_equal=True,
first27_exact_native_passages_equal_kernel_registered=True,
native_extra_task_grant_authorization_at_invalid_external_index25=excluded,
extra_task_only_grant_authorization_excluded_by_kernel_and_not_primary_coverage=True,
first_root_attempt_pre_mutation_detected_native_kernel_task_passage_difference=True,
all33_frozen_whole_math_units_bound=True,
actual_decoded_native_task_and_full_argument_equal_frozen=True,all25_premise_indices_valid=True,
primary_indices_with_identifying_passages=covered,primary_indices_without_evidence=missing,
short_identifying_passages_not_whole_application_proof=True,
unresolved_primary_units=['BL85 original node/slope proof','RG original actual-base-flat proof','Berkovich1993 original same-carrier H0 comparison'],
reader_reported_complete_local_frozen_source_and_primary_access_unavailable=True,
mathematical_counterexample_identified=False,conditional_coherent_steps_not_accepted_grants=True,
only_mathematical_grants=['O217','D214','N220','T171','Q222','C218','G227','M257'],all_unchanged_clarifications_supplied=True,
source_unchanged=True,new_accepted_paper=False,original_closed=False,
next_action='Use supported fresh native Codex worker with native file/shell tools for independent WHOLE local-file proof/source/application audit of EXACT unchanged269. No runtime modification; research shell-disabled role remains unchanged. Preserve whole207 INCONCLUSIVE; no application silently discharged.',
no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,indent=2)+'\n')
print(json.dumps(dict(binding=str(binding),sha256=sha(binding),verdict=r['verdict'],unresolved_indices=missing,new_accepted_paper=False,original_closed=False),indent=2))
