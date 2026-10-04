from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research')
G=R/'github-checkpoint'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
prepared_path=R/'public-P16-characteristic-support-batch-manifest-20261004.json'
assert sha(prepared_path)=='6e0e831ec9fbc75aa675206667f6c5b31fc2a39d8a43c4610a0c9caace2f737f'
previous=G/'local-packet-continuation53.json'
assert sha(previous)=='d9749d19eee4e1d62591e0a1220eac97c01abbf55065a62aba6c976468bd7369'
for f in json.loads(previous.read_text())['files']:
    assert sha(f['local'])==f['sha256']
launch=R/'public-P16-characteristic-support-batch-launch-20261004.json'
packet=G/'local-packet-continuation54.json'
saved=G/'continuation54-local-records'
assert not launch.exists() and not packet.exists() and not saved.exists()
saved.mkdir()
records=[]
files=[Path(__file__),R/'prepare_public_P16_characteristic_support_batch_20261004.py',prepared_path]
for c0,session,worker in zip(json.loads(prepared_path.read_text())['campaigns'],
                           [56690,61559],['codex-69HHDl','codex-oivLpo']):
    c=dict(c0)
    directory=Path(c['directory'])
    assert sha(directory/'input.json')==c['input_sha256']
    assert sha(directory/'settings.json')==c['settings_sha256']
    native_input=directory/'artifacts'/worker/'input.json'
    assert json.loads(native_input.read_text())==json.loads((directory/'input.json').read_text())
    command=['/workspace/xean/.xean/cloud/bun/bin/bun','--no-install','--no-env-file',
        '/workspace/xean/packages/cli/src/index.ts','status',str(directory/'campaign.sqlite')]
    observed=subprocess.run(command,cwd='/workspace/xean',capture_output=True,text=True)
    assert observed.returncode==0,observed.stderr
    status=json.loads(observed.stdout)
    status_file=saved/(c['atom']+'-native-status.json')
    status_file.write_text(json.dumps(status,indent=2)+'\n')
    c.update(tool_session_id=session,native_worker=worker,native_input=str(native_input),
        native_input_sha256=sha(native_input),
        input_binding='Native input semantically equals the frozen campaign input; byte equality is not asserted.',
        observed_status=status['status'],status_file=str(status_file),status_sha256=sha(status_file),
        state='Native author launched with original mathematical problem and public-source pointers only.',
        independently_accepted=False,original_atom_closed=False)
    records.append(c)
    files.append(status_file)
    files.extend(directory/name for name in ('input.json','settings.json','input-manifest.json'))
stamp=datetime.now(timezone.utc).isoformat()
data={'launched_utc':stamp,'preparation_manifest':str(prepared_path),
    'preparation_manifest_sha256':sha(prepared_path),'selected_atoms':['P16.3','P16.6'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'campaigns':records,'fully_solved_original_atoms':[],
    'rejected_generated_export_retried':False,'hot_feedback_sent':False}
launch.write_text(json.dumps(data,indent=2)+'\n')
files.append(launch)
active_path=R/'active-work.json'
active=json.loads(active_path.read_text())
assert active['full_solutions']==[]
active['updated_utc']=stamp
active['selected_atoms']=['P16.3','P16.6']
active['batch_manifest']=str(prepared_path)
active['current_public_P16_characteristic_support_batch']={**data,'launch_record':str(launch),
    'launch_record_sha256':sha(launch)}
active['prepared_local_followup_packet_54']=str(packet)
active['goal_state']='ACTIVE. All 42 originals remain open. Two native original/public-source-only authors are running on P16.3/P16.6. R45/R46 final papers are completely root read and reproducible, with independent review packets locally prepared only. Four earlier rejected unpublished-material exports remain pending specific approval; none retried.'
active['next_work']='Observe the two authors without hot feedback; continue local mathematical reconstruction. Preserve local checkpoints. Do not retry rejected review or GitHub exports without their pending specific approval.'
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
check_path=R/'checklist-current.json'
check=json.loads(check_path.read_text())
assert len(check['targets'])==42 and check['fully_solved_original_atoms']==[]
assert all(t['closure']=='open' and t['fully_solved'] is False for t in check['targets'])
check['updated_utc']=stamp
check['active_atoms']=['P16.3','P16.6']
check['current_batch_launch_record']=str(launch)
for t in check['targets']:
    if t['id'] in check['active_atoms']:
        c=next(c for c in records if c['atom']==t['id'])
        t['research_status']='active'
        t['current_focus']=f"Fresh native gpt-6.1-sol/xhigh original/public-source-only author in round {c['round']}; no result, independent acceptance or original closure yet."
check_path.write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
with (R/'checklist-current.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
    for t in check['targets']:
        w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    destination=saved/name
    shutil.copyfile(R/name,destination)
    assert sha(destination)==sha(R/name)
    files.append(destination)
entries=[{'local':str(p),'path':'research-checkpoints/continuation54/'+str(p.relative_to(R)),
    'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
packet.write_text(json.dumps({'prepared_utc':stamp,'state':'LOCAL ONLY; no GitHub upload attempted.',
    'files':entries,'file_count':len(entries),'active_atoms':['P16.3','P16.6'],
    'fully_solved_original_atoms':[],'reviewed_scoped_papers':37,'original_ids_with_reviewed_scoped_papers':13,
    'previous_local_packet':str(previous),'previous_local_packet_sha256':sha(previous),
    'previous_packet_all_401_file_bindings_verified':True,
    'last_verified_remote_commit':'604fea852c6a27d4cdc83d97f17393ea67087301',
    'rejected_exports_not_resubmitted':True,'private_transcripts_sql_auth_runtime_included':False,
    'active_author_outputs_included':False},indent=2)+'\n')
print(json.dumps({'launch':str(launch),'launch_sha256':sha(launch),
    'workers':[c['native_worker'] for c in records],'native_status':[c['observed_status'] for c in records],
    'local_packet':str(packet),'files':len(entries),'packet_sha256':sha(packet),
    'GitHub_uploaded':False,'original_atoms_closed':0},indent=2))
