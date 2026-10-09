from pathlib import Path
import json,hashlib,sys
R=Path('/workspace/research');K=R/'root-checks'
n=int(sys.argv[1]);assert n in [280,281]
p=K/f'round{n}-raw-native-actual-FINAL.json'
expected={280:'63d5b1e980e342e8dc586f6e43f2710aa3263e38b62ca0a03b7ed54527786617',281:'c8e9fe90e9e1665215725d145dc4f210b1dd4981dbb8531e383152884e93cff8'}
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected[n]
x=json.loads(p.read_text());a=int(sys.argv[2]);b=int(sys.argv[3]);assert 1<=a<=b<=len(x['notes'])
print(json.dumps(dict(round=n,candidate=x['candidate'],first=a,last=b,all_five_fields_retained=True),ensure_ascii=False))
for i,note in enumerate(x['notes'][a-1:b],a):
    print(f'WHOLE ACTUAL NOTE {i} — DATA, not instructions or correctness grant')
    assert len(note)==5
    for key,value in note.items():
        print('FIELD '+key)
        print(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2))
