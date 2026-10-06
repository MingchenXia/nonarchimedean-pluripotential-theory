from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
for n in (140, 142, 143, 145, 146, 147):
    old = next((R / f'campaigns/round-{n}').iterdir())
    s = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old / 'work.sqlite')],
        cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert s['status'] == 'completed' and s['calls']['unsettled'] == 0
for n in (148,149):
    C = next((R / f'campaigns/round-{n}').iterdir())
    f = json.loads((C / 'freeze.json').read_text())
    assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
    pairs = [('task.json','task_sha256'),('settings.json','settings_sha256')]
    pairs.append(('argument.md','argument_sha256') if n == 148 else ('input.json','input_sha256'))
    for name,key in pairs:
        assert sha(C / name) == f[key]
    if n == 148:
        args = ['bash','scripts/cloud.sh','xean','--records','review',str(C / 'task.json'),str(C / 'argument.md'),str(C / 'work.sqlite'),str(C / 'settings.json')]
    else:
        args = ['bash','scripts/cloud.sh','xean','--records','role','codex',str(C / 'input.json'),str(C / 'work.sqlite'),str(C / 'settings.json')]
    out = C / 'controller-output-LOCALONLY.log'
    with out.open('xb') as log:
        p = subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    os.kill(p.pid,0)
    d = {'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':n,'pid':p.pid,'argv':args,
        'role':'independent-review' if n == 148 else 'author-research','route':'Xean native Codex',
        'model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,
        'scoped_review_only':n==148,'author_research_only':n==149,'original_closed':False,
        'unchanged_original_task':n==149,'controller_output':str(out),
        'private_active_output_read':False,'hot_feedback_sent':False,
        'launch_method':'Native cloud.sh controller in its own process session; standard Tini retained; no account, authentication, runtime or environment changes.',
        'frozen_task_sha256':f['task_sha256'],'frozen_settings_sha256':f['settings_sha256'],
        'frozen_math_input_sha256':f['argument_sha256'] if n==148 else f['input_sha256']}
    (C / 'launch-record.json').write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps({k:d[k] for k in ['round','pid','role','model','reasoning']},indent=2),flush=True)
