from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,os
R=Path('/workspace/research');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();old=next((R/'campaigns/round-150').iterdir());f=json.loads((old/'freeze.json').read_text())
assert not (old/'work.sqlite').exists();p=json.loads((old/'launch-record.json').read_text())['pid'];state=subprocess.run(['ps','-o','stat=','-p',str(p)],capture_output=True,text=True).stdout.strip();assert not state or state.startswith('Z')
log=(old/'controller-output-LOCALONLY.log').read_text();assert 'usagePrefix: must not have more than 91 characters' in log
K=R/'root-checks';record=K/'P16.5-round150-preprovider-prefix-schema-failure-20261006.json';assert not record.exists();record.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':150,'classification':'Native declaration rejected before campaign database or provider call.','failure':'usagePrefix exceeded maximum91 characters.','database_created':False,'provider_call_admitted':False,'controller_observed_exited':True,'source_frozen_input_sha256':f['input_sha256'],'frozen_settings_sha256':f['settings_sha256'],'mathematical_result':None,'original_closed':False,'retry_round':151},indent=2)+'\n')
C=R/'campaigns/round-151/P16.5-original-big-class-entire-equation-generation-moving-trace-retry1';C.mkdir(parents=True,exist_ok=False)
(C/'task.json').write_bytes((old/'task.json').read_bytes());inp=json.loads((old/'input.json').read_text())
inp['assignment']+='\n\nNative result schema requirement: the supplied notes array is empty. In the returned notes, support may contain ONLY valid ids of earlier notes in that same ordered response, never G0/G1, R/T/C, a theorem label, file path, hash or catalogue id. State the exact mathematical grants in the proof text and source ledger. Do not invent registered support records for caller-granted theorems. Return the canonical role result shape required by Xean.\n'
(C/'input.json').write_text(json.dumps(inp,ensure_ascii=False,indent=2)+'\n')
s=json.loads((old/'settings.json').read_text());s['usagePrefix']='catalogue-20261003/r151/P16.5-original-big-entire-equation';s['codex']['workspace']=str(C/'artifacts');assert len(s['usagePrefix'])<=91
(C/'settings.json').write_text(json.dumps(s,indent=2)+'\n');(C/'mathematical-data-bindings.json').write_bytes((old/'mathematical-data-bindings.json').read_bytes())
f.update({'prepared_utc':datetime.now(timezone.utc).isoformat(),'round':151,'directory':str(C),'input_sha256':sha(C/'input.json'),'input_bytes':(C/'input.json').stat().st_size,'assignment_characters':len(inp['assignment']),'settings_sha256':sha(C/'settings.json'),'retry_of_round':150,'original_task_unchanged':True,'schema_repair_only':'Shorter legal native usagePrefix and explicit earlier-note-only support format; all mathematical grants/data and unchanged original task retained.'})
(C/'freeze.json').write_text(json.dumps(f,indent=2)+'\n')
other=next((R/'campaigns/round-149').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(other/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert st['status']=='blocked' and st['calls']['unsettled']==0
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
out=C/'controller-output-LOCALONLY.log'
with out.open('xb') as log:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
d={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':151,'pid':pid,'argv':args,'role':'author-research','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'original_closed':False,'unchanged_original_task':True,'retry_of_round':150,'frozen_task_sha256':sha(C/'task.json'),'frozen_math_input_sha256':sha(C/'input.json'),'frozen_settings_sha256':sha(C/'settings.json'),'private_active_output_read':False,'hot_feedback_sent':False,'account_auth_runtime_environment_changed':False}
(C/'launch-record.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'round':151,'pid':pid,'input_bytes':f['input_bytes'],'input_sha256':f['input_sha256'],'settings_sha256':f['settings_sha256']},indent=2))
