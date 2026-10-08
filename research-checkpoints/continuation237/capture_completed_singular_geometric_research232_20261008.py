from pathlib import Path
import hashlib,json,subprocess
R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-232').iterdir())
out=K/'round232-completed-inspection-LOCALONLY.json';actual_out=K/'round232-actual-native-final.json'
assert not out.exists() and not actual_out.exists()
args=['bash','scripts/cloud.sh','xean','--records','inspect',str(C/'work.sqlite')]
with out.open('xb') as f:subprocess.run(args,cwd='/workspace/xean',stdout=f,stderr=subprocess.PIPE,check=True)
j=json.loads(out.read_text());assert j['campaign']['status']=='completed' and not j['campaign']['error']
records=[r for r in j['records'] if r['kind']=='xean.call.settled'];assert len(records)==1
m=records[0]['data']['message'];assert m['exitCode']==0 and not m['failed'] and not m['isCanceled']
messages=[]
for line in m['stdout'].splitlines():
 try:v=json.loads(line)
 except ValueError:continue
 if v.get('type')=='item.completed' and v.get('item',{}).get('type')=='agent_message':messages.append(v['item']['text'])
exact=messages[-1].encode();x=json.loads(exact);actual_out.write_bytes(exact)
print(json.dumps(dict(status=j['campaign']['status'],inspection_path=str(out),inspection_bytes=out.stat().st_size,actual_FINAL_path=str(actual_out),actual_FINAL_bytes=len(exact),actual_FINAL_sha256=hashlib.sha256(exact).hexdigest(),candidate=x['candidate'],notes=[dict(id=n['id'],summary=n['summary'],support=n['support'],text_bytes=len(n['text'].encode()),detail_bytes=len(n['detailedSummary'].encode())) for n in x['notes']],intermediate_messages_excluded=len(messages)-1),indent=2))
