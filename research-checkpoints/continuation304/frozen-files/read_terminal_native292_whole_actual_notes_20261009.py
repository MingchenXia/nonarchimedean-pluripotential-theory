"""Display every actual FINAL field in bounded whole-note groups; native files stay inert."""
from pathlib import Path
import hashlib, json, sys
p = Path('/workspace/research/root-checks/round292-raw-native-actual-FINAL.json')
assert hashlib.sha256(p.read_bytes()).hexdigest() == '3af45446009c52dc1aef8039b36dee440db8935bd49f1fd2c4f5e34c29da2a9f'
x = json.loads(p.read_text())
assert x['candidate'] is False and len(x['notes']) == 5
lo, hi = map(int, sys.argv[1:])
assert 1 <= lo <= hi <= 5
for n in x['notes'][lo-1:hi]:
    assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
    print(json.dumps(n, ensure_ascii=False, indent=2))
