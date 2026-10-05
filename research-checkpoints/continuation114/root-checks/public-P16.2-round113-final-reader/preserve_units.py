#!/usr/bin/env python3
"""Make literal supplied primary passages individually readable and auditable."""
import json, pathlib, hashlib
ROOT = pathlib.Path(__file__).resolve().parent
def main():
    dst = ROOT / 'evidence' / 'units'; dst.mkdir(exist_ok=True)
    records=[]
    def save(name, literal, meta):
        p=dst/(name+'.txt'); p.write_text(literal)
        digest=hashlib.sha256(literal.encode()).hexdigest()
        records.append({'id':name,'file':str(p.relative_to(ROOT)), 'sha256':digest,
                        'supplied_binding_matches_bytes':meta.get('sha256') == digest if 'sha256' in meta else None,
                        'metadata':{k:v for k,v in meta.items() if k!='literal'}})
    for i,(binding,body) in enumerate(json.load(open(ROOT/'evidence/packet-01.json')).items()):
        save(f'whole68-{i:02d}',body,{'supplied_binding':binding})
    for packet,prefix in [('05','existing42'),('17','additional')]:
        for i,record in enumerate(json.load(open(ROOT/f'evidence/packet-{packet}.json'))):
            if 'literal' in record: save(f'{prefix}-{i:02d}',record['literal'],record)
    (ROOT/'evidence/units-index.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    print('Retained',len(records),'literal supplied units; no historical paths opened.')
if __name__=='__main__': main()
