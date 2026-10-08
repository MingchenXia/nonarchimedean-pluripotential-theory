from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks'
C0=next((R/'campaigns/round-243').iterdir());C=R/'campaigns/round-244/P03.1-original-normal-full-envelope-positivity-PDF-control-repair'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not C.exists()and not(C0/'work.sqlite').exists()
state=Path('/proc/563614/stat').read_text().split()[2];assert state=='Z'
log=C0/'controller-output-LOCALONLY.log';assert 'must match pattern'in log.read_text()and '/task/problem'in log.read_text()
inp=json.loads((C0/'input.json').read_text());oldtext=inp['task']['problem']
bad=[dict(index=i,codepoint=ord(c))for i,c in enumerate(oldtext)if ord(c)<9 or 14<=ord(c)<=31 or ord(c)==127]
assert bad and all(e['codepoint']==1 for e in bad)
inp['task']['problem']=''.join(c for c in oldtext if not(ord(c)<9 or 14<=ord(c)<=31 or ord(c)==127))
assert inp['notes']==[]
C.mkdir(parents=True);T=C/'immutable-mathematical-DATA';T.mkdir();math=[]
for e in json.loads((C0/'mathematical-packet-bindings.json').read_text()):
    p=Path(e['path']);assert sha(p)==e['sha256'];q=T/p.name;shutil.copyfile(p,q);z=dict(e,path=str(q));math.append(z)
for name in ['original-task.json','private-primary-packet-bindings.json']:shutil.copyfile(C0/name,C/name)
write(C/'mathematical-packet-bindings.json',math)
inp['task']['problem']=inp['task']['problem'].replace(str(C0/'mathematical-packet-bindings.json'),str(C/'mathematical-packet-bindings.json')).replace(str(C0/'private-primary-packet-bindings.json'),str(C/'private-primary-packet-bindings.json'))
write(C/'task.json',inp['task']);write(C/'input.json',inp)
s=json.loads((C0/'settings.json').read_text());s['codex']['workspace']=str(C/'artifacts');s['usagePrefix']='catalogue-20261003/r244/P03.1-original-normal-envelope-PDF-control-repair';write(C/'settings.json',s)
now=datetime.now(timezone.utc).isoformat()
failure=dict(recorded_utc=now,round=243,directory=str(C0),launch_pid=563614,process_state='Z',work_database_created=False,model_call_admitted=False,failure='Input schema rejected task.problem containing PDF U+0001 control characters',control_positions_in_original_frozen_task=bad,failed_input_sha256=sha(C0/'input.json'),failed_log_sha256=sha(log),failed_log_bytes=log.stat().st_size,frozen_records_unchanged=True,mathematical_verdict=None,counts_changed=False,repair_round=244,repair='Remove only these PDF control characters from the operational task string; keep exact original-task.json and frozen mathematical bodies unchanged; update only manifest/settings path references for the fresh worker workspace.')
write(K/'P03.1-round243-before-model-input-schema-failure-and-repair244-20261008.json',failure);write(C/'PDF-control-reader-qualification.json',failure)
write(C/'freeze.json',dict(prepared_utc=now,round=244,atom='P03.1',directory=str(C),task_sha256=sha(C/'task.json'),original_task_sha256=sha(C/'original-task.json'),input_sha256=sha(C/'input.json'),settings_sha256=sha(C/'settings.json'),mathematical_packet_bindings_sha256=sha(C/'mathematical-packet-bindings.json'),private_primary_packet_bindings_sha256=sha(C/'private-primary-packet-bindings.json'),PDF_control_qualification_sha256=sha(C/'PDF-control-reader-qualification.json'),whole_math_files=len(math),whole_math_bytes=sum(e['bytes']for e in math),private_primary_files=10,only_grants=[],model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,new_accepted_paper=False,original_closed=False,protected_editor_unchanged_open=True,prior_round243_no_model_input_failure_preserved=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91
    x.update(updated_utc=now,current_active_batch=[242],P03_1_round243_before_model_startup_failure=failure,P03_1_original_normal_geometric_envelope243=dict(round=243,status='input schema failed before campaign database or model call; immutable failure preserved; repaired fresh244 input prepared',original_closed=False),next_work='Launch repaired P03.1 original244 native input; continue P12.3 original242; max2 actual native campaigns; verify checkpoint247.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=244,input_sha256=sha(C/'input.json'),controls_removed=len(bad),round243_no_model_call=True,current_active_batch=[242]),indent=2))
