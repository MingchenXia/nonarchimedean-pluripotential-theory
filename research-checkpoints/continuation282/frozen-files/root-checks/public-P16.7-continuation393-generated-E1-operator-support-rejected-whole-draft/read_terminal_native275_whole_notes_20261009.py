from pathlib import Path
import json,sys
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator'
st=json.loads((K/'P16.7-native275-terminal-support-rejection-and-data-retention-20261009.json').read_text())
assert st['public_status']['status']=='blocked' and st['public_status']['calls']['unsettled']==0
a=json.loads((K/'round275-raw-native-final-REJECTED-support.json').read_text())
if len(sys.argv)==1:
    j=json.loads((K/'round275-terminal-inspection-LOCALONLY.json').read_text())
    print(json.dumps(dict(campaign_result=j['campaign'].get('result'),notes=[dict(id=n['id'],keys=list(n),text_bytes=len(n['text'].encode())) for n in a['notes']],candidate=a['candidate'],status='REJECTED support; DATA only, no grant'),ensure_ascii=False,indent=2))
else:
    lo,hi=map(int,sys.argv[1:]);assert 1<=lo<=hi<=len(a['notes'])
    for n in a['notes'][lo-1:hi]:print(json.dumps(n,ensure_ascii=False,indent=2))
