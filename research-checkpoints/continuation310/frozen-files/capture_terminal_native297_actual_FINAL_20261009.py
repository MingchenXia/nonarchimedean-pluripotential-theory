"""Capture settled297 actualFINAL as DATA after independent431 retention and verified309."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

R=Path('/workspace/research')
K=R/'root-checks'
C=R/'campaigns/round-297/P16.7-whole427-whole-dirac-and-actual-analytic-representation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
O=K/'round297-terminal-inspection-LOCALONLY.json'
A=K/'round297-raw-native-actual-FINAL.json'
Q=K/'round297-terminal-actual-final-ROOT-retention-20261009.json'
B=K/'P12.3-continuation431-ROOT-whole-paper-source-scope-and-binding-20261009.json'
assert not A.exists() and not Q.exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
b=json.loads(B.read_text())
assert not b['accepted'] and not b['original_closed']
for e in b['public_files']:
    assert sha(e['path'])==e['sha256']
for name in ['active-work.json','checklist-current.json']:
    y=json.loads((R/name).read_text())
    assert y['current_active_batch']==[298] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==309
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
    assert y['ROOT431_whole_unreviewed']['sha256']==sha(B)
cmd=['bash','scripts/cloud.sh','xean','--records']
st=json.loads(subprocess.run(cmd+['status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status']=='completed' and not st['error']
assert st['calls']['admitted']==st['calls']['settled']==1 and st['calls']['unsettled']==0 and st['work']['active']==0
if not O.exists():
    with O.open('xb') as out:
        subprocess.run(cmd+['inspect',str(C/'work.sqlite')],cwd='/workspace/xean',stdout=out,stderr=subprocess.PIPE,check=True)
j=json.loads(O.read_text())
events=[e for e in j['records'] if e['kind']=='xean.call.settled']
assert len(events)==1
m=events[0]['data']['message']
assert m['exitCode']==0 and not m['failed'] and not m['isCanceled']
messages=[]
for line in m['stdout'].splitlines():
    try:
        v=json.loads(line)
    except ValueError:
        continue
    if v.get('type')=='item.completed' and v.get('item',{}).get('type')=='agent_message':
        messages.append(v['item']['text'])
assert messages
exact=messages[-1].encode()
x=json.loads(exact)
assert set(x)=={'notes','candidate'}
known={n['id'] for n in json.loads((C/'input.json').read_text())['notes']}
invalid=[]
for n in x['notes']:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    for s in n['support']:
        if s not in known:
            invalid.append(dict(note_id=n['id'],support=s))
    known.add(n['id'])
A.write_bytes(exact)
now=datetime.now(timezone.utc).isoformat()
rec=dict(recorded_utc=now,round=297,public_status=st,raw_actual_FINAL=dict(path=str(A),bytes=len(exact),sha256=sha(A),notes=len(x['notes']),candidate=x['candidate'],status='Whole actual settled FINAL retained UNREVIEWED; bodies not yet physically ROOT read'),notes_metadata=[dict(id=n['id'],keys=list(n),text_bytes=len(n['text'].encode()),support=n['support']) for n in x['notes']],invalid_support_references=invalid,full_inspection=dict(path=str(O),bytes=O.stat().st_size,sha256=sha(O),LOCALONLY=True),intermediate_agent_messages_excluded=len(messages)-1,supplied_or_native_programs_executed_or_imported=False,whole_mathematical_bodies_NOT_yet_ROOT_physically_read=True,independentROOT431_retained_BEFORE_native297_mathematical_inspection=True,native298_ACTIVE_mathematics_NOT_read_or_hotfed=True,accepted=False,new_correctness_grant=False,original_closed=False,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
Q.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=json.loads(p.read_text())
    y.update(updated_utc=now,next_work='Terminal297 actualFINAL retainedUNREVIEWED after independent431 wholeproofretention and verifiedNONFORCE309. Physically read ALLactualfivefields and everydistinctformalproof/current scope/exactimmediate sources beforeROOT432 and nextP16.7batch. Native298isolatedactive; maxTWO. Whole431 notyetpublished. Counts/editor unchanged; compiler431unverified.')
    y['native297_terminal_unreviewed_retention']=dict(record=str(Q),record_sha256=sha(Q),raw_FINAL=rec['raw_actual_FINAL'])
    p.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(Q),raw_actual_FINAL=rec['raw_actual_FINAL'],notes=rec['notes_metadata'],invalid_support=invalid,candidate=x['candidate']),ensure_ascii=False,indent=2))
