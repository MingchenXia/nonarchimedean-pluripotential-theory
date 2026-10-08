import sys,json,hashlib,pathlib,platform,subprocess
BASE=pathlib.Path('/workspace/research/campaigns/round-228/P05.1-compatible-affine-reference-extension-and-sharp-distance-independent-whole-source-audit')
ROOT=pathlib.Path.cwd()
def bindings():
    out=[]
    for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:
        data=json.loads((BASE/name).read_bytes())
        for i,e in enumerate(data):
            b=pathlib.Path(e['path']).read_bytes()
            got=hashlib.sha256(b).hexdigest()
            out.append(dict(packet=name,index=i,path=e['path'],bytes=len(b),sha256=got,LF_lines=len(b.split(b'\n'))-bool(b.endswith(b'\n')),match=(len(b)==e['bytes'] and got==e['sha256'])))
    (ROOT/'input-binding-verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
def read(which,index,start,end):
    names={'m':'mathematical-packet-bindings.json','e':'historical-own-evidence-bindings.json','p':'private-primary-packet-bindings.json'}
    entry=json.loads((BASE/names[which]).read_bytes())[index]
    raw=pathlib.Path(entry['path']).read_bytes()
    # Strict literal LF indexing; form feeds are retained inside a line.
    lines=raw.decode().split('\n')
    if lines[-1]=='': lines.pop()
    if end>len(lines):
        print(f'BOUND REQUEST {end} CLAMPED TO ACTUAL EOF {len(lines)}')
        end=len(lines)
    print(f"FILE {entry['path']} LF {start}--{end} OF {len(lines)}")
    for n in range(start,end+1): print(f'{n}: {lines[n-1]}')
    with (ROOT/'own-read-displays.jsonl').open('a') as f:
        f.write(json.dumps(dict(packet=which,index=index,start=start,end=end,total=len(lines),sha256=hashlib.sha256(raw).hexdigest(),display='requested; check tool output for truncation'))+'\n')
if __name__=='__main__':
    if sys.argv[1]=='bindings': bindings()
    elif sys.argv[1]=='read': read(sys.argv[2],*[int(x) for x in sys.argv[3:]])
    elif sys.argv[1]=='decode':
        data=json.loads((BASE/'mathematical-packet-bindings.json').read_bytes())
        def leaves(o,p='$'):
            if isinstance(o,dict):
                for k,v in o.items(): yield from leaves(v,p+'.'+k)
            elif isinstance(o,list):
                if not o: yield p+' = []'
                for k,v in enumerate(o): yield from leaves(v,p+f'[{k}]')
            else: yield p+' = '+(o if isinstance(o,str) else json.dumps(o))
        for i in [0,1,2,3,8]:
            s='\n\n'.join(leaves(json.loads(pathlib.Path(data[i]['path']).read_bytes())))+'\n'
            (ROOT/f'decoded-math-{i}.txt').write_text(s)
            print(i,len(s.encode()),len(s.split('\n'))-1)
    elif sys.argv[1]=='local':
        name=sys.argv[2];start,end=map(int,sys.argv[3:5])
        lines=(ROOT/name).read_text().split('\n')
        print(f'LOCAL {name} LF {start}--{end}')
        for n in range(start,end+1): print(f'{n}: {lines[n-1]}')
        with (ROOT/'own-read-displays.jsonl').open('a') as f:
            f.write(json.dumps(dict(derived_file=name,start=start,end=end))+'\n')
