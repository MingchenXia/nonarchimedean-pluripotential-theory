"""Display explicit retained text windows, with byte/line metadata; no supplied code."""
import json, sys
from pathlib import Path
rows=json.loads(Path('reports/input-hashes.json').read_text())
key=sys.argv[1]
p=Path(next(r['local'] for r in rows if r['key']==key))
lines=p.read_text().splitlines()
start=int(sys.argv[2]) if len(sys.argv)>2 else 1
end=int(sys.argv[3]) if len(sys.argv)>3 else len(lines)
print(f'{key} {p} lines {start}..{min(end,len(lines))}/{len(lines)}')
for i in range(start-1,min(end,len(lines))): print(f'{i+1}: {lines[i]}')
