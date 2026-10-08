#!/usr/bin/env python3
"""Own bounded immutable-packet reader and binding inventory. No supplied code runs."""
import argparse
import hashlib
import json
from pathlib import Path

BASE = Path('/workspace/research/campaigns/round-223/P05.1-unchanged-dependent-common-subspace-pages-whole-independent-native-local-source-audit')
MANIFESTS = {'math': 'mathematical-packet-bindings.json',
             'history': 'historical-own-evidence-bindings.json',
             'primary': 'private-primary-packet-bindings.json'}

def rows(kind):
    return json.loads((BASE / MANIFESTS[kind]).read_text())

def read(kind, index, start, end):
    r = rows(kind)[index]
    data = Path(r['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == r['sha256']
    s = data.decode('utf-8')
    assert 0 <= start <= end <= len(s)
    assert end - start <= 20000
    record = {'kind': kind, 'index': index, 'path': r['path'],
              'start_character': start, 'end_character': end,
              'characters': len(s), 'sha256': r['sha256'],
              'status': 'requested display; inspect tool output for truncation'}
    with Path('display-requests.jsonl').open('a') as f:
        f.write(json.dumps(record) + '\n')
    print(json.dumps(record))
    print(s[start:end])

def inventory():
    out = []
    for kind in MANIFESTS:
        for i, r in enumerate(rows(kind)):
            data = Path(r['path']).read_bytes()
            sha = hashlib.sha256(data).hexdigest()
            out.append(dict(kind=kind,index=i,path=r['path'],sha256=sha,
                            bytes=len(data), LF_lines=data.count(b'\n'),
                            matches=(sha==r['sha256'] and len(data)==r['bytes'])))
    Path('frozen-verification.json').write_text(json.dumps(out,indent=2)+'\n')
    for kind, name in MANIFESTS.items():
        Path('frozen-'+name).write_bytes((BASE/name).read_bytes())
    print(json.dumps({'bindings':len(out),'mismatches':[r for r in out if not r['matches']]}))

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['inventory','read'])
    p.add_argument('kind',nargs='?',choices=list(MANIFESTS))
    p.add_argument('index',nargs='?',type=int)
    p.add_argument('start',nargs='?',type=int)
    p.add_argument('end',nargs='?',type=int)
    a=p.parse_args()
    if a.mode=='inventory': inventory()
    else: read(a.kind,a.index,a.start,a.end)
