from pathlib import Path
import hashlib, json, sys
K=Path('/workspace/research/root-checks')
P=K/'round272-actual-native-final.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='5e123c2fc531184ef5572511e2ccaf874b3bdd15dd5b83aff02f2ad92f5a9df4'
x=json.loads(P.read_text()); assert len(x['notes'])==5
mode=sys.argv[1]
if mode=='actual':
    a,b=map(int,sys.argv[2:]); assert 0<=a<b<=5 and b-a<=2
    print(json.dumps(dict(candidate=x['candidate'],entire_notes=x['notes'][a:b]),ensure_ascii=False,indent=2))
elif mode=='info':
    A=Path('/workspace/research/campaigns/round-272/P16.7-whole383-intrinsic-E1-and-actual-branch-Dirac/artifacts/codex-hhK319')
    print(json.dumps([dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(A.rglob('*')) if p.is_file()],indent=2))
elif mode=='proof':
    P=Path('/workspace/research/campaigns/round-272/P16.7-whole383-intrinsic-E1-and-actual-branch-Dirac/artifacts/codex-hhK319/proof-companion.md')
    assert hashlib.sha256(P.read_bytes()).hexdigest()=='af5de296d5b29031b29c4a18cfee282f751d81f00337fde45dcb8682eb2eaa36'
    t=P.read_text(); a,b=map(int,sys.argv[2:]); assert 0<=a<b<=len(t) and b-a<=19000
    print(json.dumps(dict(path=str(P),entire_chars=len(t),interval=[a,b]),indent=2)); print(t[a:b])
else: raise ValueError(mode)
