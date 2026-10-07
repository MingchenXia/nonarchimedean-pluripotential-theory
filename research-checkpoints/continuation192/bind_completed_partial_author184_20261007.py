from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'; C=next((R/'campaigns/round-184').iterdir())
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round184-completed-inspection-LOCALONLY.json').read_text()); ca=x['campaign']
assert ca['status']=='completed' and ca['error'] is None
k=ca['result']; assert k['candidate'] is False and len(k['notes'])==3
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    t=json.loads(line)
    if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
        try: n=json.loads(t['item']['text'])
        except (ValueError,TypeError): continue
        if isinstance(n,dict) and set(n)=={'notes','candidate'}: finals.append(n)
assert len(finals)==1; n=finals[0]; assert n['candidate'] is False and len(n['notes'])==3
for a,b in zip(n['notes'],k['notes']):
    assert all(a[q]==b[q] for q in ('id','summary','detailedSummary','support'))
    assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
ids={a['id'] for a in n['notes']}; assert all(set(a['support'])<=ids for a in n['notes'])
prompt=json.loads(req['prompt']); frozen=json.loads((C/'input.json').read_text())
assert set(prompt)==set(frozen)|{'workspace'} and all(prompt[q]==frozen[q] for q in frozen) and prompt['workspace']==k['workspace']
D=Path(k['workspace']); assert json.loads((D/'input.json').read_text())==frozen
assert req['model']=='gpt-6.1-sol' and req['reasoning']=='xhigh' and req['sandbox']=='workspace-write' and req['shell'] is True
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
actual=K/'P05.2-round184-completed-actual-author-result-20261007.json'; native=K/'P05.2-round184-native-model-final-partial-author-20261007.json'; binding=K/'P05.2-round184-settled-partial-author-binding-20261007.json'
assert not any(p.exists() for p in (actual,native,binding))
actual.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n'); native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
b=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=184,atom='P05.2',candidate=False,
    canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
    exact_decoded_native_task_assignment_notes_equal_frozen_input=True,retained_workspace_added_to_prompt=True,native_artifact_input_equal_frozen_input=True,
    all_native_note_math_equal_canonical=True,kernel_only_text_addition='Two newlines and Artifacts: followed by the retained workspace',all_support_ids_valid_local=True,
    whole_three_canonical_notes_root_read=True,whole_saved_tex_source_root_read=True,root_tex_read_lf_ranges=[[1,125],[126,250]],
    whole_argument_root_read=True,whole_source_application_ledger_root_read=True,source_lf_lines=241,source_sha256=sha(D/'P05.2-paper.tex'),pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=9,
    root_native_exact_source_compiler_success=True,root_local_rebuild_performed=False,pdf_visually_root_read=False,
    model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],caller_grants=[],
    independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
    scope='Strictly convex positive-growth U(3,4) fan contact obstruction with actual finite PA endpoint, explicit parameter family and separate literal regularity failure. No necessary-and-sufficient classification of general pairs; candidate=false.',
    protected_editor_unchanged_open=True,no_private_active_output_read=True,no_hot_feedback_sent=True)
binding.write_text(json.dumps(b,indent=2)+'\n')
print(json.dumps(dict(round=184,candidate=False,binding=str(binding),binding_sha256=sha(binding),original_closed=False),indent=2))
