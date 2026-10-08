"""Fresh byte/data audit. Never imports or executes supplied programs."""
import hashlib, json, pathlib, platform, sys, os, re
BASE=pathlib.Path('/workspace/research/campaigns/round-251/P12.4-original-supported-Cartier-locality-whole-paper-independent-review')
OUT=pathlib.Path(__file__).resolve().parent
def digest(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def audit():
    reports=OUT/'evidence'; reports.mkdir(exist_ok=True)
    results=[]
    for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:
        manifest=BASE/name
        for row in json.loads(manifest.read_text()):
            p=pathlib.Path(row['path'])
            if p.is_file():
                d=digest(p);d['size_match']=d['bytes']==row['bytes'];d['hash_match']=d['sha256']==row['sha256']
            else:d={'path':str(p),'available':False}
            d['manifest']=name;results.append(d)
    (reports/'current-bindings.json').write_text(json.dumps(results,indent=2)+'\n')
    env={'python':sys.version,'platform':platform.platform(),'cwd':str(OUT),'manifests':[digest(BASE/f) for f in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']],'input':digest(OUT/'input.json')}
    (reports/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
    data=BASE/'immutable-mathematical-DATA'
    native=(data/'05-native-origin-P12.4-paper.tex').read_text()
    reader=(data/'06-P12.4-paper.tex').read_text()
    body_results=[]
    for i in range(1,10):
        s=(data/f'{17+i:02d}-n{i}.tex').read_text()
        body_results.append({'note':i,'native_occurrences':native.count(s),'reader_occurrences':reader.count(s)})
    final=json.loads((data/'12-actual-native-FINAL.json').read_text())
    expanded=json.loads((data/'11-native-notes.json').read_text())
    (reports/'actual-final-fields.json').write_text(json.dumps({'candidate':final.get('candidate'),'note_count':len(final['notes']),'notes':final['notes']},indent=2)+'\n')
    structure={'native_bytes':len(native.encode()),'reader_bytes':len(reader.encode()),'new_bodies':body_results,'actual_final_note_count':len(final['notes']),'actual_final_ids':[n['id'] for n in final['notes']],'expanded_type':type(expanded).__name__}
    (reports/'paper-structure.json').write_text(json.dumps(structure,indent=2)+'\n')
    print(json.dumps({'files':len(results),'matching':sum(r.get('hash_match',False) and r.get('size_match',False) for r in results),'unavailable':sum(r.get('available') is False for r in results),'structure':structure},indent=2))
def show(name,start=1,end=None):
    p=BASE/'immutable-mathematical-DATA'/name
    lines=p.read_text().splitlines()
    end=end or len(lines)
    print(f'{name}: total {len(lines)} lines; displaying {start}..{min(end,len(lines))}')
    for i in range(start-1,min(end,len(lines))):print(f'{i+1}: {lines[i]}')
if __name__=='__main__':
    if len(sys.argv)==1:audit()
    else:show(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 1,int(sys.argv[3]) if len(sys.argv)>3 else None)
