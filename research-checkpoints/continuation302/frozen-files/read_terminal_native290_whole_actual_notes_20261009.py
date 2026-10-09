from pathlib import Path
import hashlib, json, sys
P = Path('/workspace/research/root-checks/round290-raw-native-actual-FINAL.json')
assert hashlib.sha256(P.read_bytes()).hexdigest() == '85592e3863ee63c7e91ebe4940f2c9c57a545973d4af1efec81ee4876dae41bd'
x = json.loads(P.read_text())
assert not x['candidate'] and len(x['notes']) == 5
ids = sys.argv[1:]
assert ids and len(ids) == len(set(ids)) and set(ids) <= {n['id'] for n in x['notes']}
for n in x['notes']:
    if n['id'] in ids:
        assert set(n) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
        print(json.dumps(n, ensure_ascii=False, indent=2))
