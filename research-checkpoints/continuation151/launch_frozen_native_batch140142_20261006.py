from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,os
R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
F=K/'interrupted-native137138-public-recovery-20261006';F.mkdir(exist_ok=False)
for n in [137,138]:
    c=next((R/f'campaigns/round-{n}').iterdir());f=json.loads((c/'freeze.json').read_text())
    for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(c/name)==f[key]
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(r.stdout);assert d['status']=='blocked' and d['work']['active']==0 and d['work']['failed']==1
    save(F/f'round{n}-public-native-status.json',d)
save(F/'recovery-scope.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':52,
 'interrupted_rounds':[137,138],'mathematical_verdicts':None,'partial_private_review_outputs_read':False,
 'cause_observed':'Public controller/worker processes no longer running; official native resume recovered attempt-limit failures. No completed canonical review result.',
 'native_invocation_history_preserved':True,'frozen_inputs_changed':False,
 'next_batch':[140,142],'review142_mathematical_inputs_byte_identical_to138':True,
 'exceptional_family137_retry_deferred_until_a_slot_frees':True})
labels={140:'P19.2-original-endpoint-preserving-model-approximation-research',142:'P16.5-entire-big-surface-relative-equation-independent-review-retry1'}
launched=[]
for n,label in labels.items():
    c=R/f'campaigns/round-{n}'/label;f=json.loads((c/'freeze.json').read_text())
    assert not (c/'work.sqlite').exists() and not (c/'launch-record.json').exists()
    for name,key in [('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(c/name)==f[key]
    if n==140:
        assert sha(c/'input.json')==f['input_sha256']
        args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(c/'input.json'),str(c/'work.sqlite'),str(c/'settings.json')]
    else:
        assert sha(c/'argument.md')==f['argument_sha256']
        args=['bash','scripts/cloud.sh','xean','--records','review',str(c/'task.json'),str(c/'argument.md'),str(c/'work.sqlite'),str(c/'settings.json')]
    output=c/'controller-output-LOCALONLY.log'
    with output.open('xb') as log:
        process=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    os.kill(process.pid,0)
    entry={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':n,'pid':process.pid,'argv':args,
           'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
           'role':'author-research' if n==140 else 'independent-review','scoped_review_only':n==142,
           'maximum_concurrent_campaigns':2,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,
           'launch_method':'Native cloud.sh controller in its own process session with retained output; standard Tini child cleanup preserved. No runtime/authentication/environment changes.',
           'controller_output':str(output),'frozen_task_sha256':f['task_sha256'],'frozen_settings_sha256':f['settings_sha256'],
           'frozen_math_input_sha256':f['input_sha256'] if n==140 else f['argument_sha256']}
    save(c/'launch-record.json',entry);launched.append(entry)
print(json.dumps({'launched':[{k:x[k] for k in ['round','pid','role','route','model','reasoning']} for x in launched],
                  'previous_interrupted_statuses_preserved':str(F),'native_standard_cleanup_preserved':True},indent=2))
