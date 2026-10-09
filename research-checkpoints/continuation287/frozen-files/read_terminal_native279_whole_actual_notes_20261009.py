from pathlib import Path
import json,sys
K=Path('/workspace/research/root-checks')
assert len(sys.argv)==3
lo,hi=map(int,sys.argv[1:])
q=json.loads((K/'round279-terminal-actual-final-ROOT-retention-20261009.json').read_text())
assert q['public_status']['status']=='completed' and q['public_status']['calls']['unsettled']==0
a=json.loads((K/'round279-raw-native-actual-FINAL.json').read_text())
assert 1<=lo<=hi<=len(a['notes'])
for note in a['notes'][lo-1:hi]:print(json.dumps(note,ensure_ascii=False,indent=2))
