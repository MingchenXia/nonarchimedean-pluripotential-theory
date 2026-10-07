from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-208').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round208-settled-inspection-LOCALONLY.json').read_text());r=x['campaign']['result']
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
assert r['verdict']=='INCONCLUSIVE' and len(r['premises'])==2 and len(r['passages'])==6
req=next(z['data']['payload'] for z in x['records'] if z['kind']=='xean.call.request')
msg=next(z['data']['message'] for z in x['records'] if z['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
n=json.loads((K/'round208-exact-native-FINAL-for-root-LOCALONLY.json').read_text())
assert n['verdict']==r['verdict'] and n['report']==r['report'] and n['premises']==r['premises']
assert len(n['passages'])==len(r['passages'])
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
assert sorted({a['premise'] for a in r['passages']})==[0,1]
assert '116863 tokens truncated' in r['report']
actual=K/'P05.2-round208-actual-canonical-independent-INCONCLUSIVE-review-20261007.json'
native=K/'P05.2-round208-exact-native-model-final-INCONCLUSIVE-review-20261007.json'
binding=K/'P05.2-round208-whole-arbitrary-reference-INCONCLUSIVE-review-binding-20261007.json'
assert not any(a.exists() for a in [actual,native,binding])
actual.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=208,continuation=272,atom='P05.2',
verdict='INCONCLUSIVE',operation_id=r['operationId'],reported_utc=r['reportedAt'],
canonical_review=str(actual),canonical_review_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
entire_report_all2premises_all6passages_root_read=True,exact_native_canonical_report_premises_passages_equal=True,
all30_frozen_whole_math_units_bound=True,actual_decoded_native_task_and_full_argument_equal_frozen=True,
all_premise_indices_valid=True,primary_premise_indices_with_original_passages=[0,1],
reader_reported_visible13proofunits_reconstructed_no_concrete_defect=True,
reader_exposed_argument_omission_text='116863 tokens truncated',
full_registered_argument_retained_but_reader_complete_file_access_unavailable=True,
whole_grant_bodies_and_complete_unchanged_source_not_independently_audited=True,
visible_reconstruction_is_not_accepted_grant=True,
review_task_checklist_cutoff_gap_j_plus_c_wrong_paper_gap_j_correct=True,
task_formula_correction_to_match_unchanged_paper_required_for_next_audit=True,
only_mathematical_grants=['A224','B225','R230','S262'],all_clarifications_supplied=True,
source_unchanged=True,new_accepted_paper=False,original_closed=False,
next_action='Fresh supported native Codex worker with file/shell tools reads every unchanged272 source/grant/primary in bounded chunks. Preserve whole208INCONCLUSIVE; newROOT276not supplied as premise or source repair. Native worker audit is not canonical research review or automatic acceptance.',
no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,indent=2)+'\n')
print(json.dumps(dict(binding=str(binding),sha256=sha(binding),verdict=r['verdict'],source_unchanged=True,new_accepted_paper=False),indent=2))

