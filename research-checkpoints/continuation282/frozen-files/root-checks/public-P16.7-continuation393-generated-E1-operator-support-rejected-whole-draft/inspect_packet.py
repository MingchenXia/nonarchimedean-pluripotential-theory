#!/usr/bin/env python3
"""Bounded, read-only packet inspection; never executes packet programs."""
import argparse
import difflib
import hashlib
import json
import pathlib
import platform
import sys

BASE = pathlib.Path('/workspace/research/campaigns/round-275/P16.7-whole390388389-general-E1-operator')
DATA = BASE / 'immutable-mathematical-DATA'
OUT = pathlib.Path(__file__).resolve().parent
LIMIT = 32 * 1024 * 1024

def get(path):
    p = pathlib.Path(path)
    if not p.is_absolute():
        matches = sorted(DATA.glob(path + '*'))
        p = matches[0] if len(matches) == 1 else OUT / path
    b = p.read_bytes()
    if len(b) > LIMIT:
        raise ValueError('inspection byte limit')
    return p, b

def leaves(x, key='$'):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from leaves(v, key + '.' + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from leaves(v, key + '[' + str(i) + ']')
    else:
        yield key, x

def main():
    a = argparse.ArgumentParser()
    a.add_argument('mode', choices=['bindings', 'read', 'structure', 'decode', 'diff', 'verify', 'environment'])
    a.add_argument('paths', nargs='*')
    a.add_argument('--start', type=int, default=0)
    a.add_argument('--end', type=int, default=20000)
    z = a.parse_args()
    if z.mode == 'environment':
        print(json.dumps({'python': sys.version, 'platform': platform.platform(), 'cwd': str(OUT),
                          'supplied_programs_executed': False, 'heavy_compute': False}, indent=2))
    elif z.mode == 'bindings':
        for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
            rows = json.loads((BASE / name).read_text())
            print(name, 'entries', len(rows))
            for i, row in enumerate(rows):
                if z.start <= i < z.end:
                    print(i, row['bytes'], row['path'])
    elif z.mode == 'verify':
        report = []
        for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
            rows = json.loads((BASE / name).read_text())
            bad = []
            for i, row in enumerate(rows):
                p, b = get(row['path'])
                if len(b) != row['bytes'] or hashlib.sha256(b).hexdigest() != row['sha256']:
                    bad.append(i)
            report.append({'binding': name, 'entries': len(rows), 'mismatches': bad})
        (OUT / 'binding-check.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps(report, indent=2))
    elif z.mode == 'read':
        for name in z.paths:
            p, b = get(name)
            s = b.decode('utf-8')
            print('FILE', p.name, 'bytes', len(b), 'chars', len(s), 'slice', z.start, min(z.end,len(s)))
            print(s[z.start:z.end])
    elif z.mode == 'structure':
        for name in z.paths:
            p, b = get(name)
            x = json.loads(b)
            print('FILE',p.name)
            for key, v in leaves(x):
                if isinstance(v, str):
                    print(key, 'str', len(v), repr(v[:110]))
                else:
                    print(key, repr(v))
    elif z.mode == 'decode':
        for name in z.paths:
            p, b = get(name)
            x = json.loads(b)
            result = '\n'.join(key + '\n' + (v if isinstance(v,str) else json.dumps(v)) for key,v in leaves(x))
            dest = OUT / (p.name + '.decoded.txt')
            dest.write_text(result + '\n')
            print(dest.name, 'chars', len(result))
    elif z.mode == 'diff':
        p, b = get(z.paths[0])
        q, c = get(z.paths[1])
        left, right = b.decode('utf-8'), c.decode('utf-8')
        seq = difflib.SequenceMatcher(None, left, right, autojunk=False)
        blocks = []
        matched = 0
        for tag, i,j,k,l in seq.get_opcodes():
            if tag == 'equal':
                matched += j-i
            else:
                blocks.append({'tag':tag,'left':[i,j],'right':[k,l], 'left_text':left[i:j], 'right_text':right[k:l]})
        dest = OUT / (p.name + '--' + q.name + '.diff.json')
        dest.write_text(json.dumps({'left':p.name,'right':q.name,'matched_chars':matched,'blocks':blocks},ensure_ascii=False,indent=2)+'\n')
        print(dest.name, 'matched_chars',matched,'left_chars',len(left),'right_chars',len(right))
        for block in blocks:
            print(json.dumps(block,ensure_ascii=False))

if __name__ == '__main__':
    main()
