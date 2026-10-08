#!/usr/bin/env python3
"""Own read-only bound-input reader; fresh local bookkeeping only."""
import sys,json,hashlib,pathlib
BASE=pathlib.Path('/workspace/research/campaigns/round-222/P05.1-unchanged-independent-common-subspace-pages-whole-native-local-source-audit')
HERE=pathlib.Path(__file__).resolve().parent
GROUPS={'math':'mathematical-packet-bindings.json','history':'historical-own-evidence-bindings.json','primary':'private-primary-packet-bindings.json'}
def rows(group):
    data=json.loads((BASE/GROUPS[group]).read_text())
    return data if isinstance(data,list) else data
def initialize():
    result={}
    for group in GROUPS:
        data=rows(group)
        if not isinstance(data,list):
            result[group]=data; continue
        out=[]
        for i,row in enumerate(data):
            p=pathlib.Path(row['path']); b=p.read_bytes()
            out.append({'index':i,**row,'actual_sha256':hashlib.sha256(b).hexdigest(),'actual_bytes':len(b),'match':hashlib.sha256(b).hexdigest()==row['sha256'],'characters':len(b.decode('utf8',errors='replace'))})
        result[group]=out
    (HERE/'frozen-bindings.json').write_text(json.dumps(result,indent=2)+'\n')
    for g,data in result.items():
        if isinstance(data,list):
            for r in data: print(g,r['index'],r['bytes'],r['match'],pathlib.Path(r['path']).name)
        else: print(g,json.dumps(data))
def read(group,index,start,end):
    r=rows(group)[index]; p=pathlib.Path(r['path'])
    s=p.read_text(errors='replace'); end=min(end,len(s))
    print(f'BEGIN {group}[{index}] {p.name} CHARS [{start},{end})/{len(s)}')
    print(s[start:end]); print(f'END {group}[{index}] [{start},{end})')
    with (HERE/'display-requests.jsonl').open('a') as f:
        f.write(json.dumps({'group':group,'index':index,'start':start,'end':end,'total':len(s),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'requested; inspect output for truncation'})+'\n')
if __name__=='__main__':
    if sys.argv[1]=='init': initialize()
    elif sys.argv[1]=='lines':
        group=sys.argv[2]; index=int(sys.argv[3]); lo=int(sys.argv[4]); hi=int(sys.argv[5])
        r=rows(group)[index]; s=pathlib.Path(r['path']).read_text(errors='replace'); lines=s.split('\n')
        read(group,index,sum(len(v)+1 for v in lines[:lo-1]),sum(len(v)+1 for v in lines[:hi]))
    else: read(sys.argv[1],*map(int,sys.argv[2:]))
