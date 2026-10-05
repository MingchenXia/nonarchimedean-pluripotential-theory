#!/usr/bin/env python3
"""Finite provenance/schema checks. This does not certify a mathematical proof."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    original_bytes = (ROOT / 'input-original.json').read_bytes()
    original = json.loads(original_bytes)
    assert original_bytes == (ROOT / 'input.json').read_bytes()
    assert original['task'] == json.loads((ROOT / 'task-original.json').read_text())
    assert original['assignment'] == (ROOT / 'assignment-original.txt').read_text()
    original_hashes = json.loads((ROOT / 'input-manifest.json').read_text())
    for path, expected in original_hashes.items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
    print('PASS: original input bytes, exact task/assignment extractions, and frozen hashes.')
    manifest = json.loads((ROOT / 'source-manifest.json').read_text())
    source = (ROOT / manifest['source']['path']).read_bytes()
    assert hashlib.sha256(source).hexdigest() == manifest['source']['sha256']
    lines = source.decode().split('\n')
    for unit in manifest['units']:
        lo, hi = unit['inclusive_one_based_LF']
        b = (ROOT / unit['path']).read_bytes()
        assert b.decode() == '\n'.join(lines[lo-1:hi]) + '\n'
        assert hashlib.sha256(b).hexdigest() == unit['sha256']
    print('PASS:', len(manifest['units']), 'literal primary slices and full-source hash.')
    bound = manifest['bound_primary_units'][0]
    bound_bytes = (ROOT / bound['path']).read_bytes()
    assert hashlib.sha256(bound_bytes).hexdigest() == bound['sha256']
    assert (ROOT / 'sources/cld-weak-multiplier.txt').read_bytes() == bound_bytes + b'\n'
    print('PASS: explicitly bound weak-multiplier bytes; trailing-newline normalization distinguished.')
    premises = json.loads((ROOT / 'premises.json').read_text())
    assert [p['id'] for p in premises] == [f'P{i}' for i in range(9)]
    status = json.loads((ROOT / 'status.json').read_text())
    assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
    assert status['id'] == 'P21.3' and status['status'] == 'partial'
    assert status['concrete_gaps'] and (ROOT / status['proof_file']).is_file()
    notes = json.loads((ROOT / 'notes.json').read_text())
    assert notes['candidate'] is False and 0 < len(notes['notes']) <= 4
    earlier = set()
    for i, note in enumerate(notes['notes'], 1):
        assert set(note) == {'id','summary','detailedSummary','text','support'}
        assert note['id'] == f'n{i}'
        assert set(note['support']) <= earlier
        assert all(isinstance(note[k],str) and note[k] for k in
                   ['summary','detailedSummary','text'])
        earlier.add(note['id'])
    print('PASS: 9 premise records; exact status keys; 4-or-fewer backward-supported notes; candidate=false.')
    # Integer formula verification is a finite transcription check, not the support argument.
    def mul(a,b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))
    a=((1,1),(0,1));b=((1,0),(1,1));ident=((1,0),(0,1))
    aa=bb=ident
    for k in range(101):
        assert aa == ((1,k),(0,1)) and bb == ((1,0),(k,1))
        aa=mul(aa,a);bb=mul(bb,b)
    print('PASS: exact shear-power formula transcription for k=0,...,100 (finite check only).')
    if (ROOT / 'P21.3-paper.pdf').exists():
        assert (ROOT / 'P21.3-paper.pdf').read_bytes().startswith(b'%PDF-')
        print('PASS: generated PDF has a PDF header.')
    print('No finite check proves original P21.3, current density, or the transfinite claims.')


if __name__ == '__main__':
    main()
