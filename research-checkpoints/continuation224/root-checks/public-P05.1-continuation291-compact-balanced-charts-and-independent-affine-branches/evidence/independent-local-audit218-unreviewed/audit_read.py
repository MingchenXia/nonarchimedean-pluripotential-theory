"""Read only frozen binding paths in bounded character chunks; no supplied code executes."""
import sys, json, pathlib, hashlib
BASE = pathlib.Path('/workspace/research/campaigns/round-218/P05.1-unchanged-compact-balanced-charts-and-independent-bouquets-whole-native-local-source-audit')
GROUPS = {'m':'mathematical-packet-bindings', 'h':'historical-own-evidence-bindings', 'p':'private-primary-packet-bindings'}
group, index, start, end = sys.argv[1:]
row = json.loads((BASE/(GROUPS[group]+'.json')).read_text())[int(index)]
path = pathlib.Path(row['path'])
raw = path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == row['sha256']
data = raw.decode('utf-8')
start, end = int(start), min(int(end),len(data))
print(json.dumps({'group':group, 'index':int(index),'path':str(path),'chars':[start,end],'total':len(data)}))
print(data[start:end])
with open('displayed-read-ranges.jsonl','a') as f:
    f.write(json.dumps({'group':group,'index':int(index),'chars':[start,end],'total':len(data)})+'\n')
