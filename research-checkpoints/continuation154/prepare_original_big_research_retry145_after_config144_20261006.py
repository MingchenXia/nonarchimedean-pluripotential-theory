from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
old=R/'campaigns/round-144/P16.5-original-big-class-relative-floor-closure-and-entire-equation-research'
f=json.loads((old/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(old/name)==f[key]
d=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert d['status']=='blocked' and d['error']=='Codex worker is not configured' and d['calls']['admitted']==0
F=K/'original144-pre-model-configuration-failure-public-20261006';F.mkdir(exist_ok=False);save(F/'round144-public-native-status.json',d)
save(F/'failure-scope.json',{'recorded_utc':datetime.now(timezone.utc).isoformat(),'cause':'Author campaign copied review settings and omitted the required codex worker section.',
    'mathematical_verdict':None,'provider_calls_admitted':0,'frozen_math_input_changed':False,'runtime_account_authentication_changed':False,
    'fresh_author_retry':145,'successful_author_configuration_template':140,'originals_solved':8,'originals_open':34,'accepted_papers':53,
    'prepared_checkpoint153_uploaded':False,'prepared_checkpoint153_superseded_by154':True,
    'checkpoint153_supersession_reason':'Its static live-front text said running while the recorded public observation correctly said blocked. Preserve it locally; publish corrected new checkpoint154.'})
C=R/'campaigns/round-145/P16.5-original-big-class-relative-floor-closure-and-entire-equation-research-retry1';C.mkdir(parents=True,exist_ok=False)
for name in ['task.json','input.json']:shutil.copyfile(old/name,C/name)
good=R/'campaigns/round-140/P19.2-original-endpoint-preserving-model-approximation-research/settings.json'
settings=json.loads(good.read_text());assert settings['codex']['model']=='gpt-6.1-sol' and settings['codex']['reasoning']=='xhigh'
settings['codex']['workspace']=str(C/'artifacts');settings['usagePrefix']='catalogue-20261003/r145/P16.5-original-big-closure-and-entire-equation-research-retry1';save(C/'settings.json',settings)
save(C/'mathematical-data-bindings.json',{'classification':'Exact mathematical input retry; no new source grant or worker feedback.',
    'previous_input_sha256':f['input_sha256'],'fresh_input_sha256':sha(C/'input.json'),'previous_task_sha256':f['task_sha256'],'fresh_task_sha256':sha(C/'task.json'),
    'input_and_task_byte_identical':True,'previous_mathematical_bindings_sha256':sha(old/'mathematical-data-bindings.json'),
    'previous_model_calls_admitted':0,'active_campaign143_private_outputs_read':False,'successful_author_settings_template_sha256':sha(good),
    'global_runtime_accounts_authentication_changed':False})
save(C/'freeze.json',{'prepared_utc':datetime.now(timezone.utc).isoformat(),'round':145,'atom':'P16.5','directory':str(C),
    'input_sha256':sha(C/'input.json'),'input_bytes':(C/'input.json').stat().st_size,'assignment_characters':f['assignment_characters'],
    'task_sha256':sha(C/'task.json'),'unchanged_original_task_sha256':f['task_sha256'],'unchanged_original_task':True,
    'settings_sha256':sha(C/'settings.json'),'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'prepared_only':True,'original_closed':False,'independent_acceptance':False,'maximum_concurrent_campaigns':2,
    'retry_of_pre_model_configuration_failure144':True,'mathematical_input_byte_identical':True,'existing_editor_unchanged':True})
print(json.dumps({'directory':str(C),'input_sha256':sha(C/'input.json'),'input_byte_identical':True,'calls_admitted_in144':0},indent=2))
