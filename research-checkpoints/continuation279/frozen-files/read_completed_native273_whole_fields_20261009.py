from pathlib import Path
import hashlib, json, sys
K=Path('/workspace/research/root-checks'); P=K/'round273-actual-native-final.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='5c4a45988933d63930e4aa145a5844818c11d45d1822002369b3b8ea397cfb01'
x=json.loads(P.read_text()); assert len(x['notes'])==4
mode=sys.argv[1]
if mode=='actual':
    a,b=map(int,sys.argv[2:]); assert 0<=a<b<=4 and b-a<=2
    print(json.dumps(dict(candidate=x['candidate'],entire_notes=x['notes'][a:b]),ensure_ascii=False,indent=2))
elif mode=='info':
    A=Path('/workspace/research/campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1/artifacts/codex-Bxz0sA')
    print(json.dumps([dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(A.rglob('*')) if p.is_file()],indent=2))
elif mode=='proof':
    P=Path('/workspace/research/campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1/artifacts/codex-Bxz0sA/proof-companion.md')
    t=P.read_text(); a,b=map(int,sys.argv[2:]); assert 0<=a<b<=len(t) and b-a<=19000
    print(json.dumps(dict(path=str(P),bytes=P.stat().st_size,sha256=hashlib.sha256(P.read_bytes()).hexdigest(),entire_chars=len(t),interval=[a,b]),indent=2));print(t[a:b])
else:raise ValueError(mode)
