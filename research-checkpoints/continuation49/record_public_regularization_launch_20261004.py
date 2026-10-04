from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest=R/'public-regularization-batch-manifest-20261004.json'
assert sha(manifest)=='460ed7a6414ceb02d9a1e047e4675d6056188df71ec4911665345f846ab7bb0b'
prepared=json.loads(manifest.read_text())
records=[]
for campaign,session in zip(prepared['campaigns'],[3501,10208]):
    c=dict(campaign); d=Path(c['directory'])
    assert sha(d/'input.json')==c['input_sha256'] and sha(d/'settings.json')==c['settings_sha256']
    assert (d/'run.json').exists() and (d/'run.stderr').exists()
    c.update(tool_session_id=session,state='Native author launched on original question and seven published-source pointers only; no result or acceptance yet.')
    records.append(c)
stamp=datetime.now(timezone.utc).isoformat()
launch=R/'public-regularization-batch-launch-20261004.json'; assert not launch.exists()
data={'launched_utc':stamp,'preparation_manifest':str(manifest),'preparation_manifest_sha256':sha(manifest),
      'selected_atoms':['P02.1','P02.2'],'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
      'fully_solved_original_atoms':[],'campaigns':records,
      'blocked_generated_export_attempted':False,'hot_feedback_sent':False}
launch.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
active_path=R/'active-work.json'; active=json.loads(active_path.read_text())
active['updated_utc']=stamp; active['selected_atoms']=['P02.1','P02.2']; active['batch_manifest']=str(manifest)
active['current_public_regularization_batch']={**data,'launch_record':str(launch),'launch_record_sha256':sha(launch)}
for c in active['current_public_curves_and_CLD_batch']['campaigns']:
    review=Path(c['directory']).with_name(Path(c['directory']).name+'-review')
    c.update(review_state='Exact review prepared locally only; never submitted.',
             review_freeze=str(review/'freeze.json'),review_freeze_sha256=sha(review/'freeze.json'))
active['goal_state']='ACTIVE. All 42 original targets remain open. Current small batch P02.1/P02.2 native authors launched. R39/R40 final drafts and canonical notes read and locally reproduced; R39 stage-3 gap is preserved. Exact reviews prepared locally only. Four earlier automatically rejected exports await specific approval; none retried.'
active['next_work']='Observe the current native regularization authors without hot feedback; continue independent published-source and local mathematical checks. Preserve a local checkpoint. Submit or push an already blocked payload only after its pending specific approval arrives.'
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
check_path=R/'checklist-current.json'; check=json.loads(check_path.read_text())
assert check['fully_solved_original_atoms']==[] and len(check['targets'])==42
check['updated_utc']=stamp; check['active_atoms']=['P02.1','P02.2']; check['current_batch_launch_record']=str(launch)
for target in check['targets']:
    if target['id'] in ['P02.1','P02.2']:
        target['research_status']='active'
        target['current_focus']='Fresh native Xean gpt-6.1-sol/xhigh author in round '+str(41 if target['id']=='P02.1' else 42)+', using the original full regularization dossier and seven published-source pointers only. Targets arbitrary classical psh functions, actual requested approximant class, fixed ordinary neighborhoods, monotonicity and scalar/overlap compatibility. No result or acceptance yet.'
check_path.write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'launch_record':str(launch),'sha256':sha(launch),'sessions':[3501,10208],'original_atoms_closed':0},indent=2))
