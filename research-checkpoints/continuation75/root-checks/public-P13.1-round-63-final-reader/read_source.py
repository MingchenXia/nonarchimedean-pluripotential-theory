import json,sys
from pathlib import Path
sources=json.loads(Path('sources.json').read_text())
key=sys.argv[1];source=next(x for x in sources if x['local_id']==key)
lines=Path(source['literal_extract']).read_text().split('\n')
for spec in sys.argv[2:]:
 lo,hi=map(int,spec.split(':'));print(f'\nSOURCE {key} {source["saved_version"]} LF {lo}--{hi}')
 for i in range(lo,hi+1):print(f'{i}: {lines[i-1]}')
