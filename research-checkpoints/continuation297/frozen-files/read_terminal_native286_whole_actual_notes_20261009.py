from pathlib import Path
import hashlib,json,sys
P=Path('/workspace/research/root-checks/round286-raw-native-actual-FINAL.json')
assert hashlib.sha256(P.read_bytes()).hexdigest()=='8dc923d36fd115d795aab12bf1221a79ddf18307fe8acd3ef07766f39e31a585'
x=json.loads(P.read_text());assert x['candidate'] is False and len(x['notes'])==5
ids=sys.argv[1:];assert ids and set(ids)<=set(n['id'] for n in x['notes'])
print('Actual candidate:',x['candidate'])
for n in x['notes']:
    if n['id'] not in ids:continue
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    print('\nID:',n['id'])
    print('SUMMARY:',n['summary'])
    print('DETAILED SUMMARY:',n['detailedSummary'])
    print('SUPPORT:',json.dumps(n['support'],ensure_ascii=False))
    print('ENTIRE ACTUAL TEXT:')
    print(n['text'])
    print('END ACTUAL NOTE:',n['id'])
