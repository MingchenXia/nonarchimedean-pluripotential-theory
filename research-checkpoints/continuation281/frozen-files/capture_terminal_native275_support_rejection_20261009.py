from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator'
O=K/'round275-terminal-inspection-LOCALONLY.json'; A=K/'round275-raw-native-final-REJECTED-support.json'
Q=K/'P16.7-native275-terminal-support-rejection-and-data-retention-20261009.json'
assert not O.exists() and not A.exists() and not Q.exists()
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status']=='blocked' and st['calls']['admitted']==st['calls']['settled']==1 and st['calls']['unsettled']==0
assert st['work']['active']==0 and st['work']['failed']==1 and st['error'].startswith('Unknown, dead, or forward support:')
with O.open('xb') as out:subprocess.run(['bash','scripts/cloud.sh','xean','--records','inspect',str(C/'work.sqlite')],cwd='/workspace/xean',stdout=out,stderr=subprocess.PIPE,check=True)
j=json.loads(O.read_text()); settled=[e for e in j['records'] if e['kind']=='xean.call.settled']; assert len(settled)==1
m=settled[0]['data']['message']; assert m['exitCode']==0 and not m['failed'] and not m['isCanceled']
messages=[]
for line in m['stdout'].splitlines():
    try:v=json.loads(line)
    except ValueError:continue
    if v.get('type')=='item.completed' and v.get('item',{}).get('type')=='agent_message':messages.append(v['item']['text'])
assert messages; exact=messages[-1].encode(); x=json.loads(exact); assert set(x)=={'notes','candidate'}
known={n['id'] for n in json.loads((C/'input.json').read_text())['notes']}; invalid=[]
for n in x['notes']:
    for s in n['support']:
        if s not in known:invalid.append(dict(note_id=n['id'],support=s))
    known.add(n['id'])
assert invalid; A.write_bytes(exact); sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest(); now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=275,public_status=st,reason='One native call completed but Xean rejected its FINAL support identifiers. No retry, runtime bypass, note import, acceptance, grant or original closure.',raw_FINAL=dict(path=str(A),bytes=len(exact),sha256=sha(A),notes=len(x['notes']),candidate=x['candidate'],status='REJECTED support; mathematical bodies not yet ROOT physically read'),invalid_supports=invalid,full_inspection=dict(path=str(O),bytes=O.stat().st_size,sha256=sha(O),LOCALONLY=True),intermediate_agent_messages_excluded=len(messages)-1,other_campaign_active_math_not_read=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97),protected_editor_OPEN_UNCHANGED=True)
Q.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; a=json.loads(p.read_text()); assert a['current_active_batch']==[275] and a['github_pending_checkpoint'] is None
    a.update(updated_utc=now,current_active_batch=[],native275_terminal_rejection=dict(record=str(Q),sha256=sha(Q),status='BLOCKED terminal support validation',admitted=1,settled=1,unsettled=0,accepted=False,original_closed=False));p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(Q),record_sha256=sha(Q),raw_FINAL_bytes=len(exact),notes=len(x['notes']),candidate=x['candidate'],invalid_supports=invalid,current_active_batch=[]),ensure_ascii=False,indent=2))
