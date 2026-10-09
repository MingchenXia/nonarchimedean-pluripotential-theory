"""Display each entire actual note, all five fields, in bounded independent chunks."""
from pathlib import Path
import hashlib, json, sys

p = Path('/workspace/research/root-checks/round295-raw-native-actual-FINAL.json')
assert hashlib.sha256(p.read_bytes()).hexdigest() == '86ce7e9d34c72d42640bcf77d27dad7d9113e124f3ade798679ad81abb597c05'
x = json.loads(p.read_text())
assert len(x['notes']) == 4 and x['candidate'] is False
for ident in sys.argv[1:]:
    n = next(n for n in x['notes'] if n['id'] == ident)
    assert set(n) == {'id','summary','detailedSummary','text','support'}
    for key in ['id','summary','detailedSummary','support','text']:
        print('\nACTUAL NOTE FIELD ' + key + '\n')
        print(n[key] if isinstance(n[key],str) else json.dumps(n[key],ensure_ascii=False))
