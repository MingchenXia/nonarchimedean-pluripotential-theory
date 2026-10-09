from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-278/P12.3-whole396-corrected-formal-CE-and-original-residual'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
O=K/'round278-terminal-inspection-LOCALONLY.json';A=K/'round278-raw-native-actual-FINAL.json';Q=K/'round278-terminal-actual-final-ROOT-retention-20261009.json'
assert not A.exists() and not Q.exists()
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status']=='completed' and st['error'] is None and st['calls']['admitted']==st['calls']['settled']==1 and st['calls']['unsettled']==0 and st['work']['active']==0
if not O.exists():
    with O.open('xb') as out:subprocess.run(['bash','scripts/cloud.sh','xean','--records','inspect',str(C/'work.sqlite')],cwd='/workspace/xean',stdout=out,stderr=subprocess.PIPE,check=True)
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
assert not invalid
A.write_bytes(exact);now=datetime.now(timezone.utc).isoformat()
rec=dict(recorded_utc=now,round=278,public_status=st,campaign_result=j['campaign'].get('result'),raw_actual_FINAL=dict(path=str(A),bytes=len(exact),sha256=sha(A),notes=len(x['notes']),candidate=x['candidate'],status='Whole actual settled FINAL retained UNREVIEWED; compare artifact serializations before use'),notes_metadata=[dict(id=note['id'],keys=list(note),text_bytes=len(note['text'].encode()),support=note['support']) for note in x['notes']],full_inspection=dict(path=str(O),bytes=O.stat().st_size,sha256=sha(O),LOCALONLY=True),intermediate_agent_messages_excluded=len(messages)-1,supplied_or_native_programs_executed_or_imported=False,whole_mathematical_bodies_NOT_yet_ROOT_physically_read=True,accepted=False,new_correctness_grant=False,original_closed=False,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
Q.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;y=json.loads(p.read_text());assert 278 in y['current_active_batch']
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
    y.update(updated_utc=now,current_active_batch=[n for n in y['current_active_batch'] if n!=278],native278_terminal_unreviewed_retention=dict(record=str(Q),record_sha256=sha(Q),raw_FINAL=rec['raw_actual_FINAL']),next_work='Whole actual278 FINAL and distinct expanded proofs/ledgers/program-as-DATA reading and independent reconstruction. Prepare native280 whole400398399 actual unbounded P16.7 residual. No acceptance/closure/countchange, protected editor OPEN UNCHANGED.')
    p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(Q),raw_actual_FINAL=rec['raw_actual_FINAL'],notes=rec['notes_metadata'],candidate=x['candidate']),ensure_ascii=False,indent=2))
