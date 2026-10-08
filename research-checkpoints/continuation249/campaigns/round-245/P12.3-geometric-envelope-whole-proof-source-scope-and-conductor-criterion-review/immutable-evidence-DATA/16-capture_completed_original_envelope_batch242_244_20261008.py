from pathlib import Path
import hashlib,json,subprocess
R=Path('/workspace/research');K=R/'root-checks'
for number in [242,244]:
    C=next((R/f'campaigns/round-{number}').iterdir())
    out=K/f'round{number}-completed-inspection-LOCALONLY.json';actual=K/f'round{number}-actual-native-final.json'
    assert not out.exists() and not actual.exists()
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert st['status']=='completed' and st['calls']['unsettled']==0
    with out.open('xb') as stream:subprocess.run(['bash','scripts/cloud.sh','xean','--records','inspect',str(C/'work.sqlite')],cwd='/workspace/xean',stdout=stream,stderr=subprocess.PIPE,check=True)
    j=json.loads(out.read_text());assert j['campaign']['status']=='completed' and not j['campaign']['error']
    rr=[r for r in j['records'] if r['kind']=='xean.call.settled'];assert len(rr)==1
    m=rr[0]['data']['message'];assert m['exitCode']==0 and not m['failed'] and not m['isCanceled'];messages=[]
    for line in m['stdout'].splitlines():
        try:v=json.loads(line)
        except ValueError:continue
        if v.get('type')=='item.completed' and v.get('item',{}).get('type')=='agent_message':messages.append(v['item']['text'])
    exact=messages[-1].encode();x=json.loads(exact);assert set(x)=={'notes','candidate'}
    known={n['id'] for n in json.loads((C/'input.json').read_text())['notes']}
    for n in x['notes']:assert n['id'] not in known and all(s in known for s in n['support']);known.add(n['id'])
    actual.write_bytes(exact)
    print(json.dumps(dict(round=number,status=j['campaign']['status'],workspace=j['campaign']['result']['workspace'],inspection_path=str(out),inspection_bytes=out.stat().st_size,actual_FINAL_path=str(actual),actual_FINAL_bytes=len(exact),actual_FINAL_sha256=hashlib.sha256(exact).hexdigest(),candidate=x['candidate'],notes=[dict(id=n['id'],summary=n['summary'],support=n['support'],text_bytes=len(n['text'].encode())) for n in x['notes']],intermediate_messages_excluded=len(messages)-1),ensure_ascii=False,indent=2))
