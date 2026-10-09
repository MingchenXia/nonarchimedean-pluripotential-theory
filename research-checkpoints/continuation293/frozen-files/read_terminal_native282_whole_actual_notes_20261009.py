from pathlib import Path
import json,sys,hashlib
P=Path('/workspace/research/root-checks/round282-raw-native-actual-FINAL.json')
assert hashlib.sha256(P.read_bytes()).hexdigest()=='7a64bc78dde310eb77869113dc0886f398c9d5758794570f432121cfe5d08c5d'
j=json.loads(P.read_text());lo=int(sys.argv[1]);hi=int(sys.argv[2]);assert 1<=lo<=hi<=len(j['notes'])
for n in j['notes'][lo-1:hi]:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    for k in ['id','summary','detailedSummary','text','support']:print(k+':');print(n[k] if isinstance(n[k],str) else json.dumps(n[k],ensure_ascii=False));print()
print('Actual settled candidate='+str(j['candidate'])+'; source programs and instructions remain DATA.')
