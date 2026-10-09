from pathlib import Path
import hashlib, json, sys
K=Path('/workspace/research/root-checks'); P=K/'round274-actual-native-final.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='b0ba56d2c9a57c645f073050b3fb1d63216bfb85e29b7d754c2c7f73c40a6cac'
x=json.loads(P.read_text()); assert len(x['notes'])==5
A=Path('/workspace/research/campaigns/round-274/P12.3-whole386-Jensen-completion-and-original-residual/artifacts/codex-gTwO5f')
mode=sys.argv[1]
if mode=='actual':
    a,b=map(int,sys.argv[2:]); assert 0<=a<b<=5 and b-a<=2
    print(json.dumps(dict(candidate=x['candidate'],entire_notes=x['notes'][a:b]),ensure_ascii=False,indent=2))
elif mode=='body':
    p=A/sys.argv[2]; assert p.name==sys.argv[2] and p.suffix in ['.md','.json','.py']
    t=p.read_text(); a,b=map(int,sys.argv[3:]); assert 0<=a<b<=len(t) and b-a<=19000
    print(json.dumps(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),entire_chars=len(t),interval=[a,b]),indent=2)); print(t[a:b])
else:raise ValueError(mode)
