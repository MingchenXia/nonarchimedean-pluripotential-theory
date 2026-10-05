"""Preserve pre-worker declaration rejection; repair only the bounded usage label."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import shutil

R=Path('/workspace/research')
old=R/'campaigns/round-78/P13.2-public-source-reviewed-estimate-to-actual-finite-energy-realization'
C=R/'campaigns/round-79/P13.2-public-source-actual-finite-energy-realization'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not C.exists() and not (old/'campaign.sqlite').exists()
m=json.loads((old/'input-manifest.json').read_text())
assert sha(old/'input.json')==m['input_sha256'] and sha(old/'settings.json')==m['settings_sha256']
s=json.loads((old/'settings.json').read_text()); assert len(s['usagePrefix'])>91
write(old/'prelaunch-validation-failure.json',{'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'stage':'Declaration schema validation before worker admission','native_error':'/settings/usagePrefix: must not have more than 91 characters',
    'settings_sha256':sha(old/'settings.json'),'input_sha256':sha(old/'input.json'),
    'worker_started':False,'database_exists':False,'auth_failure':False,
    'original_task_and_mathematics_unchanged':True,'runtime_modified':False})
C.mkdir(parents=True)
for name in ['input.json','assignment-new-prefix.txt']: shutil.copyfile(old/name,C/name)
s['usagePrefix']='catalogue-20261003/r79/P13.2-actual-finite-energy-realization'
s['codex']['workspace']=str(C/'artifacts'); assert len(s['usagePrefix'])<=91
write(C/'settings.json',s)
m.update({'prepared_utc':datetime.now(timezone.utc).isoformat(),'round':79,'directory':str(C),
    'settings_sha256':sha(C/'settings.json'),'input_sha256':sha(C/'input.json'),
    'same_mathematical_input_as_round78':True,'rejected_prelaunch_round':78,
    'repair':'Only usagePrefix length and fresh worker workspace; no task, source, mathematical grant or runtime changes.',
    'state':'PREPARED; exact same saved input, new settings require root-reading before launch.'})
write(C/'input-manifest.json',m)
print(json.dumps({'directory':str(C),'input_sha256':sha(C/'input.json'),'settings_sha256':sha(C/'settings.json'),'usagePrefix_length':len(s['usagePrefix']),'worker_started':False},indent=2))
