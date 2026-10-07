from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'; C=next((R/'campaigns/round-180').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round180-completed-inspection-LOCALONLY.json').read_text()); c=x['campaign']
assert c['status']=='completed' and c['error'] is None
k=c['result']; assert k['candidate'] is False and len(k['notes'])==5
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
 t=json.loads(line)
 if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
  try: v=json.loads(t['item']['text'])
  except (ValueError,TypeError): continue
  if isinstance(v,dict) and set(v)=={'notes','candidate'}: finals.append(v)
assert len(finals)==1; n=finals[0]; assert n['candidate'] is False
for a,b in zip(n['notes'],k['notes']):
 assert {q:a[q] for q in ('id','summary','detailedSummary','support')}=={q:b[q] for q in ('id','summary','detailedSummary','support')}
 assert b['text']==a['text']+'\n\nArtifacts: '+k['workspace']
ids={a['id'] for a in n['notes']}; assert all(set(a['support'])<=ids for a in n['notes'])
prompt=json.loads(req['prompt']); frozen=json.loads((C/'input.json').read_text())
assert set(prompt)==set(frozen)|{'workspace'} and all(prompt[q]==frozen[q] for q in frozen)
assert prompt['workspace']==k['workspace']
assert json.loads((Path(k['workspace'])/'input.json').read_text())==frozen
assert req['model']=='gpt-6.1-sol' and req['reasoning']=='xhigh' and req['sandbox']=='workspace-write' and req['shell'] is True
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
actual=K/'P16.4-round180-completed-actual-author-result-20261007.json'
assert json.loads(actual.read_text())==k
native=K/'P16.4-round180-native-model-final-partial-author-20261007.json'
binding=K/'P16.4-round180-settled-partial-author-binding-20261007.json'
assert not native.exists() and not binding.exists()
native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
D=Path(k['workspace'])
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=180,atom='P16.4',candidate=False,
 canonical_result=str(actual),canonical_result_sha256=sha(actual),native_final=str(native),native_final_sha256=sha(native),
 exact_decoded_native_task_assignment_notes_equal_frozen_input=True,retained_workspace_added_to_prompt=True,
 native_artifact_input_equal_frozen_input=True,all_native_note_math_equal_canonical=True,
 kernel_only_text_addition='Two newlines and Artifacts: followed by the retained artifact directory',
 all_support_ids_valid_local=True,whole_five_canonical_notes_root_read=True,
 whole_saved_tex_source_root_read=True,root_tex_read_lf_ranges=[[1,337],[338,673],[674,1010]],
 source_sha256=sha(D/'P16.4-paper.tex'),source_bytes=(D/'P16.4-paper.tex').stat().st_size,
 pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=12,pdf_visually_root_read=False,
 whole_source_ledger_independently_root_read=False,root_local_rebuild_performed=False,
 native_build_claims_are_author_observations_only=True,model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],
 frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
 caller_grants=['G1:whole171','G2:whole214','G3:whole216'],
 operator217_and_comparison218_were_unreviewed_data_at_frozen_launch=True,no_hot_feedback_sent=True,
 independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,
 scope='Twelve-page unreviewed supporting reconstruction and new variational consequences; no full prescribed-target equation. Candidate=false explicitly retains compactness, envelope/outer derivative, intrinsic target converse, attainment and every-solution uniqueness gaps.',
 protected_editor_unchanged_open=True,no_private_active_output_read=True)
binding.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(round=180,candidate=False,binding=str(binding),sha256=sha(binding),original_closed=False),indent=2))
