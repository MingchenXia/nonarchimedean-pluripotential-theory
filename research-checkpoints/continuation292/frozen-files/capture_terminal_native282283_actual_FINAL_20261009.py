from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys
R=Path('/workspace/research');K=R/'root-checks'
n=int(sys.argv[1]);assert n in [282,283]
labels={282:'P16.7-whole402403404-generated-uniqueness-and-compactness',283:'P12.3-whole405-contact-and-arbitrary-envelope-residual'}
C=R/f'campaigns/round-{n}'/labels[n]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
O=K/f'round{n}-terminal-inspection-LOCALONLY.json';A=K/f'round{n}-raw-native-actual-FINAL.json';Q=K/f'round{n}-terminal-actual-final-ROOT-retention-20261009.json'
assert not A.exists() and not Q.exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
command=['bash','scripts/cloud.sh','xean','--records']
st=json.loads(subprocess.run(command+['status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status']=='completed' and st['error'] is None and st['calls']['admitted']==st['calls']['settled']==1 and st['calls']['unsettled']==0 and st['work']['active']==0
if not O.exists():
    with O.open('xb') as out:subprocess.run(command+['inspect',str(C/'work.sqlite')],cwd='/workspace/xean',stdout=out,stderr=subprocess.PIPE,check=True)
j=json.loads(O.read_text());settled=[e for e in j['records'] if e['kind']=='xean.call.settled'];assert len(settled)==1
m=settled[0]['data']['message'];assert m['exitCode']==0 and not m['failed'] and not m['isCanceled']
messages=[]
for line in m['stdout'].splitlines():
    try:v=json.loads(line)
    except ValueError:continue
    if v.get('type')=='item.completed' and v.get('item',{}).get('type')=='agent_message':messages.append(v['item']['text'])
assert messages;exact=messages[-1].encode();x=json.loads(exact);assert set(x)=={'notes','candidate'}
known={note['id'] for note in json.loads((C/'input.json').read_text())['notes']};invalid=[]
for note in x['notes']:
    assert {'id','text','support'}.issubset(note) and len(note)==5
    for s in note['support']:
        if s not in known:invalid.append(dict(note_id=note['id'],support=s))
    known.add(note['id'])
A.write_bytes(exact);now=datetime.now(timezone.utc).isoformat()
rec=dict(recorded_utc=now,round=n,public_status=st,campaign_result=j['campaign'].get('result'),raw_actual_FINAL=dict(path=str(A),bytes=len(exact),sha256=sha(A),notes=len(x['notes']),candidate=x['candidate'],status='Whole actual settled FINAL retained UNREVIEWED; mathematical bodies not yet physically read'),notes_metadata=[dict(id=note['id'],keys=list(note),text_bytes=len(note['text'].encode()),support=note['support']) for note in x['notes']],invalid_support_references=invalid,full_inspection=dict(path=str(O),bytes=O.stat().st_size,sha256=sha(O),LOCALONLY=True),intermediate_agent_messages_excluded=len(messages)-1,supplied_or_native_programs_executed_or_imported=False,whole_mathematical_bodies_NOT_yet_ROOT_physically_read=True,accepted=False,new_correctness_grant=False,original_closed=False,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
Q.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;y=json.loads(p.read_text());assert n in y['current_active_batch'] and y['github_pending_checkpoint'] is None
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
    y.update(updated_utc=now,current_active_batch=[r for r in y['current_active_batch'] if r!=n],next_work='Publish whole407. Physically read actual terminal282283 all fields and every distinct expanded mathematical body/ledger/program-as-DATA before independent reconstruction and frozen follow-up. Maintain at mostTWO campaigns and verified NONFORCE checkpoints; no count change, protected editor OPEN UNCHANGED.')
    y[f'native{n}_terminal_unreviewed_retention']=dict(record=str(Q),record_sha256=sha(Q),raw_FINAL=rec['raw_actual_FINAL'])
    p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(Q),raw_actual_FINAL=rec['raw_actual_FINAL'],notes=rec['notes_metadata'],invalid_support=invalid,candidate=x['candidate']),ensure_ascii=False,indent=2))
