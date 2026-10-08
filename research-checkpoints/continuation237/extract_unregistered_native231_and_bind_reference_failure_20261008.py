from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-231').iterdir());A=C/'artifacts/codex-kyWw2M'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
src=K/'round231-blocked-settled-inspection-LOCALONLY.json';j=json.loads(src.read_text())
assert j['campaign']['status']=='blocked' and j['campaign']['error']=='Unknown, dead, or forward support: S306' and j['campaign']['result'] is None
settled=[v for v in j['records'] if v['kind']=='xean.call.settled'];assert len(settled)==1
message=settled[0]['data']['message'];assert message['exitCode']==0 and not message['failed'] and not message['isCanceled']
items=[]
for line in message['stdout'].splitlines():
 try:v=json.loads(line)
 except ValueError:continue
 if v.get('type')=='item.completed' and v.get('item',{}).get('type')=='agent_message':items.append(v['item']['text'])
exact=items[-1].encode();actual=json.loads(exact);assert not actual['candidate'] and len(actual['notes'])==5
saved=json.loads((A/'native-notes.json').read_text());assert len(saved['notes'])==5 and not saved['candidate']
known=set();external=set()
for n,s in zip(actual['notes'],saved['notes']):
 assert n['id']==s['id'] and n['support']==s['support']
 for dependency in n['support']:
  if dependency not in known:external.add(dependency)
 known.add(n['id'])
assert external=={'S306','B225','R230'}
assert json.loads((C/'input.json').read_text())['notes']==[]
rows=json.loads((A/'artifact-hashes.json').read_text());assert len(rows)==42
for e in rows:
 p=A/e['path'];assert p.is_relative_to(A) and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
for filename,count in [('mathematical-packet-bindings.json',24),('private-primary-packet-bindings.json',4)]:
 rows=json.loads((C/filename).read_text());assert len(rows)==count
 for e in rows:assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
out=K/'round231-unregistered-actual-native-final.json';binding=K/'round231-unregistered-final-and-reference-failure-binding-20261008.json'
assert not out.exists() and not binding.exists();out.write_bytes(exact)
value=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=231,source_inspection_sha256=sha(src),actual_FINAL_path=str(out),actual_FINAL_sha256=sha(out),actual_FINAL_bytes=len(exact),notes=5,intermediate_agent_messages_excluded=len(items)-1,native_workspace=str(A),provider_process_exit_code=0,provider_generation_completed=True,xean_role_status='blocked',xean_error=j['campaign']['error'],registered_native_result_exists=False,input_structured_notes_count=0,task_text_declared_grants=['B225','R230','S306','S307','S298'],external_support_ids_in_FINAL=sorted(external),cause='Accepted supporting material was supplied in task/files but omitted from CodexInput.notes registry; native validateNotes rejected the declared external support',historical_input_result_and_SQLite_not_mutated=True,remedy='Register complete qualified trusted Note objects in a NEW frozen continuation input. Reuse this mathematical output only as unreviewed DATA; do not rewrite the actual FINAL or fabricate successful registration.',own_artifact_bindings_verified=42,frozen_math_primary_bindings_verified=28,actual_saved_equal=actual==saved,whole_actual_math_read_not_yet_claimed=True,source_sha256=sha(A/'P05.1-paper.tex'),pdf_sha256=sha(A/'P05.1-paper.pdf'),author_pages=13,new_accepted_paper=False,original_closed=False,private_ACTIVE_output_read=False,supplied_scripts_not_executed_or_imported=True)
binding.write_text(json.dumps(value,indent=2)+'\n')
for filename in ['active-work.json','checklist-current.json']:
 p=R/filename;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint'] is None
 x['native231_reference_registration_failure']=value;p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(value,indent=2))
