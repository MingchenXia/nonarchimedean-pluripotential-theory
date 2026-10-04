from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
prefix = 'manuscript/editorial/xean_research_20261003'
sha = lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
saved = G / 'continuation56-local-records'
manifest_path = G / 'upload-manifest-continuation56.json'
assert not saved.exists() and not manifest_path.exists()
receipt = json.loads((G/'push-receipt-continuation43.json').read_text())
assert receipt['commit_sha']=='a14cd6fda7c9c55d314acfd171118b13ebc30b62' and receipt['remote_ref_verified']
saved.mkdir()
stamp = datetime.now(timezone.utc).isoformat()
authorization = saved / 'export-authorization.json'
authorization.write_text(json.dumps({'recorded_utc':stamp,'user_instruction':'授权你上传任何材料',
    'existing_repository_instruction':'MingchenXia/nonarchimedean-pluripotential-theory',
    'branch':'codex/xean-research-20261003','provider_route':'Xean native Codex gpt-6.1-sol/xhigh to OpenAI',
    'effect':'Earlier generated-material export block resolved by explicit broad material authorization. Frozen rejection records remain unchanged.',
    'scope':'This mathematics task research papers, proofs, canonical notes, source extracts and review evidence; credentials/private conversations are not included.'},ensure_ascii=False,indent=2)+'\n')
audits = []
for relative, atom, session in [
    ('campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy-review','P16.6',31053),
    ('campaigns/round-32/P15.2-minimum-reference-full-mass-operator-original-scope-audit','P15.2',71291)]:
    directory = R / relative
    freeze = json.loads((directory/'freeze.json').read_text())
    for key,name in [('argument_sha256','argument.md'),('task_sha256','task.json')]:
        assert sha(directory/name)==freeze[key]
    settings = json.loads((directory/'settings.json').read_text())
    assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
    command = ['/workspace/xean/.xean/cloud/bun/bin/bun','--no-install','--no-env-file',
               '/workspace/xean/packages/cli/src/index.ts','status',str(directory/'review.sqlite')]
    p = subprocess.run(command,cwd='/workspace/xean',capture_output=True,text=True)
    assert p.returncode==0,p.stderr
    status = json.loads(p.stdout)
    status_path = saved/(atom+'-review-native-status.json')
    status_path.write_text(json.dumps(status,indent=2)+'\n')
    audits.append({'atom':atom,'directory':str(directory),'freeze_sha256':sha(directory/'freeze.json'),
        'argument_sha256':sha(directory/'argument.md'),'settings_sha256':sha(directory/'settings.json'),
        'tool_session_id':session,'observed_status':status['status'],'status_file':str(status_path),
        'status_sha256':sha(status_path),'submitted':True,'independently_accepted':False,'original_closed':False})
launch_path = saved/'independent-audit-launch.json'
launch_path.write_text(json.dumps({'recorded_utc':stamp,'authorization_sha256':sha(authorization),
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','audits':audits,
    'batch_size':2,'original_atoms_closed':[],'private_transcripts_or_SQL_included':False},indent=2)+'\n')
active_path = R/'active-work.json'
active = json.loads(active_path.read_text())
assert active['full_solutions']==[]
active.update(updated_utc=stamp,github_checkpoint=receipt,
    export_authorization={'record':str(authorization),'sha256':sha(authorization),'state':'Granted by explicit user instruction; authorization persists.'},
    current_independent_audit_batch={'launch_record':str(launch_path),'sha256':sha(launch_path),'audits':audits},
    goal_state='ACTIVE. All 42 originals remain open; 37 reviewed scoped papers. Explicit material upload authorization received. Exact checkpoint43 uploaded. Two independent native gpt-6.1-sol/xhigh audits active. Checkpoints44-55 being synchronized.',
    next_work='Wait for both audits without feedback; independently read actual full verdicts and source passages, then decide original closure. Advance at most a few problems together and push checkpoints regularly.')
active['github_pending_checkpoint'].update(state='Uploaded successfully after explicit material authorization.',receipt=str(G/'push-receipt-continuation43.json'),commit_sha=receipt['commit_sha'])
for audit in active['pending_original_scope_audits']:
    if audit['atom']=='P15.2': audit.update(state='Submitted after explicit material upload authorization; independent native review active.',launch_record=str(launch_path))
for campaign in active['current_public_P16_characteristic_support_batch']['campaigns']:
    if campaign['atom']=='P16.6': campaign.update(review_submitted=True,review_state='Independent native correctness review active; no verdict read yet.')
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
check_path = R/'checklist-current.json'
check = json.loads(check_path.read_text())
assert len(check['targets'])==42 and all(not t['fully_solved'] for t in check['targets'])
check.update(updated_utc=stamp,current_independent_audit_launch=str(launch_path),active_atoms=['P16.6','P15.2'])
for t in check['targets']:
    if t['id']=='P16.6':
        t['research_status']='independent_review_active'
        t['current_focus']='Round48 exact retained-field arbitrary-support theorem under independent native correctness review; original support-axis scope remains a separate audit.'
    if t['id']=='P15.2':
        t['research_status']='original_scope_audit_active'
        t['current_focus']='Frozen round32 complete original construction proposal submitted to independent native audit; no original closure before full verdict reconstruction.'
check_path.write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
with (R/'checklist-current.tsv').open('w',newline='') as handle:
    writer=csv.writer(handle,delimiter='\t');writer.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
    for t in check['targets']:writer.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    shutil.copyfile(R/name,saved/name)

files = {}
bindings = []
def add(path, remote, expected=None, **metadata):
    path=Path(path);digest=sha(path)
    if expected is not None:assert digest==expected,str(path)
    assert not path.is_symlink() and remote and not remote.startswith('/') and '..' not in Path(remote).parts
    item={'local':str(path),'path':remote,'bytes':path.stat().st_size,'sha256':digest,**metadata}
    if remote in files:assert files[remote]['sha256']==digest,remote
    files[remote]=item
volatile={prefix+'/'+name for name in ['active-work.json','checklist-current.json','checklist-current.tsv','CHECKPOINT.txt']}
for number in range(44,56):
    path=G/f'local-packet-continuation{number}.json'
    data=json.loads(path.read_text())
    bindings.append({'packet':number,'path':str(path),'sha256':sha(path),'files':len(data['files'])})
    for old in data['files']:
        remote=old['path']
        if remote in volatile:remote=f'research-checkpoints/continuation{number}-historical/'+remote
        add(old['local'],remote,old['sha256'],source_local_packet=number,original_declared_remote_path=old['path'])
    add(path,f'research-checkpoints/continuation{number}/LOCAL_PACKET.json')
addenda=G/'local-packet-continuation45-addenda.json'
for old in json.loads(addenda.read_text())['files']:
    add(old['local'],'research-checkpoints/continuation45-addenda/'+Path(old['local']).name,old['sha256'])
add(addenda,'research-checkpoints/continuation45-addenda/LOCAL_PACKET.json')
for path in sorted(saved.iterdir()):
    add(path,'research-checkpoints/continuation56/'+path.name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(saved/name,prefix+'/'+name)
for path in [Path(__file__),G/'push_checkpoint_continuation56.py',G/'push-receipt-continuation43.json']:
    add(path,'research-checkpoints/continuation56/'+path.name)
manifest={'generated_utc':stamp,'repository':'MingchenXia/nonarchimedean-pluripotential-theory',
    'branch':'codex/xean-research-20261003','expected_previous_checkpoint':receipt['commit_sha'],
    'files':list(files.values()),'file_count':len(files),'frozen_local_packet_bindings':bindings,
    'authorization_record_sha256':sha(authorization),'active_audits':audits,
    'fully_solved_original_atoms':[],'reviewed_scoped_papers':37,
    'scope':'Frozen local research checkpoints44-55, preserved addenda and two new audit launch snapshots. Historical status-file collisions are archived individually; current front records reflect authorization and active review. No private transcripts, SQL databases, credentials or complete originally uploaded PDF.'}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(manifest_path),'manifest_sha256':sha(manifest_path),'file_count':len(files),
                  'active_audits':[a['atom'] for a in audits],'unique_contents':len({f['sha256'] for f in files.values()})},indent=2))
