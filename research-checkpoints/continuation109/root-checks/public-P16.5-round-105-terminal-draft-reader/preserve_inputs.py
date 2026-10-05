#!/usr/bin/env python3
"""Preserve the supplied input and literal mathematical units, without following paths."""
import hashlib, json, pathlib, re, shutil
ROOT = pathlib.Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def save(path, b):
    p = ROOT / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
    return {"artifact": path, "sha256": sha(b), "bytes": len(b)}
original = (ROOT / 'input.json').read_bytes()
x = json.loads(original)
records = [save('preserved/input-original.json', original)]
records += [save('preserved/task-original.json', (json.dumps(x['task'], ensure_ascii=False, indent=2)+'\n').encode()),
            save('preserved/assignment-original.txt', x['assignment'].encode())]
s = x['assignment']; blocks = []
pattern = r'(BEGIN MATHEMATICAL DATA[^\n]*)\n(.*?)\nEND MATHEMATICAL DATA'
for i, m in enumerate(re.finditer(pattern, s, re.S)):
    body = m.group(2); parsed = None
    try: parsed = json.loads(body)
    except json.JSONDecodeError: pass
    suffix = 'json' if parsed is not None else 'md'
    path = f'preserved/block-{i:02d}.{suffix}'
    r = save(path, body.encode()); r.update(label=m.group(1), character_interval=[m.start(2), m.end(2)])
    records.append(r); blocks.append((i, parsed))
units = []
def walk(obj, block, key='root'):
    if isinstance(obj, dict):
        if isinstance(obj.get('literal'), str):
            label = str(obj.get('id', obj.get('unit', obj.get('tag', key))))
            safe = re.sub(r'[^a-zA-Z0-9_.-]+', '_', label)[-140:]
            path = f'primary-units/block-{block:02d}-{len(units):03d}-{safe}.txt'
            r = save(path, obj['literal'].encode())
            r.update(supplied_metadata={k:v for k,v in obj.items() if k!='literal'}, block=block,
                     supplied_hash_is_documentary=True)
            units.append(r)
        for k,v in obj.items():
            if k!='literal': walk(v, block, str(k))
    elif isinstance(obj, list):
        for j,v in enumerate(obj): walk(v, block, f'{key}[{j}]')
for i,obj in blocks:
    if obj is not None: walk(obj,i)
save('preserved/manifest.json', (json.dumps(records,ensure_ascii=False,indent=2)+'\n').encode())
save('primary-units/manifest.json',(json.dumps(units,ensure_ascii=False,indent=2)+'\n').encode())
dictionary = json.loads((ROOT/'preserved/block-02.json').read_text())
drecords=[]
for i,(binding,body) in enumerate(dictionary.items()):
    r=save(f'primary-dictionary/{i:03d}-{binding}.txt',body.encode())
    r.update(binding=binding,binding_matches_preserved_body=(binding==r['sha256']))
    drecords.append(r)
save('primary-dictionary/manifest.json',(json.dumps(drecords,indent=2)+'\n').encode())
print(json.dumps({'input_sha256':sha(original),'blocks':len(blocks),'literal_units':len(units),
                  'dictionary_units':len(drecords)},indent=2))
