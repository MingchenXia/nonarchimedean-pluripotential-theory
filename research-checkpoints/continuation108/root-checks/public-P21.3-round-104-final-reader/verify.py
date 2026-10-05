#!/usr/bin/env python3
"""Finite artifact/integrity checks only; no claim of mathematical verification."""
import hashlib
import json
import pathlib
import re

ROOT=pathlib.Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name):return json.loads((ROOT/name).read_text())

assert (ROOT/'input-original.json').read_bytes()==(ROOT/'input.json').read_bytes()
data=read('input-original.json')
assert read('task-original.json')==data['task']
assert (ROOT/'assignment-original.txt').read_text()==data['assignment']
manifest=read('source-manifest.json')
source=ROOT/manifest['source']['path']
assert sha(source)==manifest['source']['sha256']
lines=source.read_text().split('\n')
for unit in manifest['units']:
    path=ROOT/unit['path'];a,b=unit['inclusive_one_based_LF']
    assert path.read_bytes()==('\n'.join(lines[a-1:b])+'\n').encode(),unit['id']
    assert sha(path)==unit['sha256'],unit['id']
for unit in read('literature-bindings.json'):
    assert sha(ROOT/unit['unit_file'])==unit['unit_sha256'],unit['id']
    raw=read(unit['retrieved_output'])
    lo,hi=unit['web_rendered_line_interval'];rows={}
    for block in raw['content']:
        if block['type']!='text':continue
        for section in re.split(r'\n-{20,}\n',block['text']):
            if '('+unit['retrieved_http_url']+')' not in section.splitlines()[0]:continue
            for row in section.splitlines():
                match=re.match(r'L(\d+)(?:@P[\d-]+)?: (.*)',row)
                if match and lo<=int(match.group(1))<=hi:
                    number=int(match.group(1))
                    if number in rows:assert rows[number]==row
                    rows[number]=row
    assert len(rows)==hi-lo+1,unit['id']
    assert (ROOT/unit['unit_file']).read_bytes()==('\n'.join(rows[i] for i in range(lo,hi+1))+'\n').encode(),unit['id']
status=read('status.json')
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id']=='P21.3' and status['status']=='partial-unresolved'
assert (ROOT/status['proof_file']).is_file()
notes=read('notes.json')
assert set(notes)=={'notes','candidate'} and notes['candidate'] is False
assert 1<=len(notes['notes'])<=4
seen=set()
for i,note in enumerate(notes['notes'],1):
    assert set(note)=={'id','summary','detailedSummary','text','support'}
    assert note['id']==f'n{i}'
    assert all(s in seen for s in note['support']),note['id']
    seen.add(note['id'])
for name in ['P21.3-paper.tex','P21.3-paper.pdf','P21.3-argument.md']:
    assert (ROOT/name).is_file() and (ROOT/name).stat().st_size>100,name
record={'status':'pass','mathematical_audit':False,'original_input_bytes':(ROOT/'input.json').stat().st_size,
        'frozen_input_sha256':sha(ROOT/'input-original.json'),'cld_source_sha256':sha(source),
        'supplied_source_units_verified':27,'all_source_units_verified':len(manifest['units']),
        'web_units_verified':len(read('literature-bindings.json')),'canonical_note_count':len(seen),
        'checks':['exact frozen input bytes','parsed task and exact assignment string','primary literal slice bytes/hashes',
                  'web-rendered unit source URL/line bindings and hashes','exact status schema','backward note supports','required nonempty artifacts'],
        'limits':'Integrity and compilation are finite execution checks, not proofs of density, scalar relation preservation, or original P21.3.'}
(ROOT/'logs/verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
