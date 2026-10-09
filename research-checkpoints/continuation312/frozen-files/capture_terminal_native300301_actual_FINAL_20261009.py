"""Extract only settled native final messages as inert DATA; no mathematical verdict."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess

R=Path('/workspace/research');K=R/'root-checks'
suffix={300:'P12.3-whole435-normal-nonisolated-and-conductor-classification',301:'P16.7-whole434436437-isotropic-dirac-and-actual-recognition'}
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for number in [300,301]:
    C=R/f'campaigns/round-{number}'/suffix[number]
    A=K/f'round{number}-raw-native-actual-FINAL.json'
    O=K/f'round{number}-terminal-inspection-LOCALONLY.json'
    Q=K/f'round{number}-terminal-actual-final-ROOT-retention-20261009.json'
    assert not Q.exists() and not O.exists()
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert st['status']=='completed' and not st['error'] and st['work']['active']==0
    assert st['calls']['admitted']==st['calls']['settled']==1 and st['calls']['unsettled']==0
    raw=A.read_bytes();j=json.loads(raw);events=[e for e in j['records'] if e['kind']=='xean.call.settled'];assert len(events)==1
    m=events[0]['data']['message'];assert m['exitCode']==0 and not m['failed'] and not m['isCanceled']
    messages=[]
    for line in m['stdout'].splitlines():
        try:v=json.loads(line)
        except ValueError:continue
        if v.get('type')=='item.completed' and v.get('item',{}).get('type')=='agent_message':messages.append(v['item']['text'])
    assert messages
    exact=messages[-1].encode();x=json.loads(exact);assert set(x)=={'notes','candidate'}
    known={n['id'] for n in load(C/'input.json')['notes']};invalid=[]
    for n in x['notes']:
        assert set(n)=={'id','summary','detailedSummary','text','support'}
        for s in n['support']:
            if s not in known:invalid.append(dict(note_id=n['id'],support=s))
        known.add(n['id'])
    assert not invalid
    O.write_bytes(raw);A.write_bytes(exact)
    rec=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=number,public_status=st,raw_actual_FINAL=dict(path=str(A),bytes=len(exact),sha256=sha(A),notes=len(x['notes']),candidate=x['candidate']),notes_metadata=[dict(id=n['id'],keys=list(n),text_bytes=len(n['text'].encode()),support=n['support']) for n in x['notes']],invalid_support_references=invalid,full_inspection=dict(path=str(O),bytes=len(raw),sha256=sha(O),LOCALONLY=True),intermediate_agent_messages_excluded=len(messages)-1,mathematical_bodies_physically_ROOT_read=False,accepted=False,new_correctness_grant=False,original_closed=False,supplied_or_native_programs_executed_or_imported=False,independent438_retained_BEFORE_any300301_math=True,hot_feedback=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),compiler_UNVERIFIED=True,protected_editor_OPEN_UNCHANGED=True)
    Q.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(round=number,record=str(Q),actual=rec['raw_actual_FINAL'],metadata=rec['notes_metadata']),ensure_ascii=False,indent=2))
