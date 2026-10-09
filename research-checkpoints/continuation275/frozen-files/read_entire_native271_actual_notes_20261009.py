from pathlib import Path
import hashlib, json, sys
P=Path('/workspace/research/root-checks/round271-actual-native-final.json')
assert hashlib.sha256(P.read_bytes()).hexdigest()=='0b22c4a1b088c3e8015c6b6ba572ef219d3bb5f08ecd0699d0f971f4f612cad1'
x=json.loads(P.read_text()); assert len(sys.argv)==3 and len(x['notes'])==9
a,b=map(int,sys.argv[1:]); assert 0<=a<b<=9 and b-a<=3
print(json.dumps(dict(candidate=x['candidate'],entire_notes=x['notes'][a:b]),ensure_ascii=False,indent=2))
