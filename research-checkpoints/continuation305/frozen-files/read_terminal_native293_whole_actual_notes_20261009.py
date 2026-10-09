"""Display every actual FINAL field in bounded whole-note groups, no input code execution."""
from pathlib import Path
import hashlib, json, sys
p = Path('/workspace/research/root-checks/round293-raw-native-actual-FINAL.json')
assert hashlib.sha256(p.read_bytes()).hexdigest() == 'fbb27b3ba04fc2debba3c0f7f9294b4511ee328a98117783b46296f45feb21df'
x = json.loads(p.read_text())
assert x['candidate'] is False and len(x['notes']) == 4
lo,hi = map(int,sys.argv[1:])
assert 1 <= lo <= hi <= 4
for n in x['notes'][lo-1:hi]:
    assert set(n) == {'id','summary','detailedSummary','text','support'}
    print(json.dumps(n,ensure_ascii=False,indent=2))
