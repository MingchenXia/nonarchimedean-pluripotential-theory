from pathlib import Path
import hashlib,json,sys
P=Path('/workspace/research/root-checks/round285-raw-native-actual-FINAL.json')
assert hashlib.sha256(P.read_bytes()).hexdigest()=='012f7e6f74a5dc311b5812c99b80dfe995a4500e6c6767cbd3af18d48b5617a6'
x=json.loads(P.read_text());assert x['candidate'] is False and len(x['notes'])==4
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
