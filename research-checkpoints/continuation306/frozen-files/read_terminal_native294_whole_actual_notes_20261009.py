"""Display every actual returned field without executing returned material."""
from pathlib import Path
import json, sys

p = Path('/workspace/research/root-checks/round294-raw-native-actual-FINAL.json')
x = json.loads(p.read_text())
selected = set(sys.argv[1:])
assert selected and selected <= {n['id'] for n in x['notes']}
for n in x['notes']:
    if n['id'] in selected:
        assert set(n) == {'id','summary','detailedSummary','text','support'}
        for key in ['id','summary','detailedSummary','text','support']:
            print('\nACTUAL ' + n['id'] + ' FIELD ' + key + '\n')
            print(json.dumps(n[key],ensure_ascii=False) if key == 'support' else n[key])
print('\nACTUAL candidate: ' + json.dumps(x['candidate']))
