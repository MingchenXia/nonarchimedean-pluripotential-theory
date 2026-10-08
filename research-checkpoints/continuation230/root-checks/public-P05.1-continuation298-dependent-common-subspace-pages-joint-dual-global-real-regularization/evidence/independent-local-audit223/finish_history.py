"""Own read-only historical comparisons; never execute supplied programs."""
import difflib
import hashlib
import json
import subprocess
from pathlib import Path

hist = json.loads(Path('frozen-historical-own-evidence-bindings.json').read_text())
math = json.loads(Path('frozen-mathematical-packet-bindings.json').read_text())
prim = json.loads(Path('frozen-private-primary-packet-bindings.json').read_text())
raw = [Path(r['path']).read_bytes() for r in hist]
assert all(len(b) == r['bytes'] and hashlib.sha256(b).hexdigest() == r['sha256']
           for b, r in zip(raw, hist))
groups = {}
for i, r in enumerate(hist):
    groups.setdefault(r['sha256'], []).append(i)
report = {'entries': len(hist), 'unique_byte_bodies': len(groups),
          'byte_aliases': list(groups.values()), 'empty_entries': [],
          'math_aliases': [], 'primary_extracts': [], 'engine_differences': [],
          'stdout_differences': [], 'binding_inputs': [], 'binding_artifacts': []}
for i, b in enumerate(raw):
    if not b:
        report['empty_entries'].append(i)
    for j, m in enumerate(math):
        if b == Path(m['path']).read_bytes():
            report['math_aliases'].append({'history': i, 'math': j})
            break
for i in range(13):
    text = raw[i].decode()
    header, body = text.split('\n', 1)
    fields = header.split()
    label, first, last = fields[1], int(fields[3].split('..')[0]), int(fields[3].split('..')[1])
    p = next(r for r in prim if r.get('label') == label and r['path'].endswith('.txt'))
    lines = Path(p['path']).read_text().split('\n')
    expected = '\n'.join(f'{j}: {lines[j-1]}' for j in range(first, last+1))+'\n'
    assert body == expected
    assert fields[-1] == p['sha256']
    report['primary_extracts'].append({'history': i, 'label': label, 'LF': [first, last],
                                      'entire_numbered_body_exact': True})
for key, canonical in [('engine_differences', 14), ('stdout_differences', 30)]:
    a = raw[canonical].decode().split('\n')
    for indices in groups.values():
        i = indices[0]
        name = hist[i]['path']
        eligible = (name.endswith('.engine.log') or name.endswith('P05.1-paper.log')) if canonical == 14 else (name.endswith('.stdout.log') and 'tex-pass-' in name)
        if not eligible or raw[i] == raw[canonical]:
            continue
        b = raw[i].decode().split('\n')
        chunks = []
        for tag, a0, a1, b0, b1 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag != 'equal':
                chunks.append({'tag': tag, 'canonical_lines': [a0+1,a1+1],
                               'other_lines': [b0+1,b1+1],
                               'removed': a[a0:a1], 'added': b[b0:b1]})
        report[key].append({'canonical': canonical, 'history_aliases': indices, 'changes': chunks})
bind = json.loads(raw[82])
report['binding_wrapper'] = {k:v for k,v in bind.items() if k not in ['inputs','artifacts']}
for r in bind['inputs']:
    matches = [{'kind': kind,'index': i} for kind, rows in [('math', math),('primary',prim)]
               for i,s in enumerate(rows) if s['sha256']==r['sha256'] and s['bytes']==r['bytes']]
    assert matches
    report['binding_inputs'].append({'label': r['label'], 'recorded_path': r['path'],
                                    'bytes':r['bytes'], 'sha256':r['sha256'], 'bound_matches':matches})
for r in bind['artifacts']:
    matches = [i for i,s in enumerate(hist) if s['path'].endswith('/author221/'+r['file'])]
    assert len(matches)==1, (r,matches)
    i=matches[0]
    assert hist[i]['sha256']==r['sha256'] and hist[i]['bytes']==r['bytes']
    report['binding_artifacts'].append(dict(r, history=i, exact_match=True))
report['pdf_text_comparisons'] = []
own = Path('P05.1-paper.pdf')
for i, source in [(None,own),(16,Path(hist[16]['path'])),(99,Path(hist[99]['path']))]:
    target=Path('historical-pdf-text-own.txt' if i is None else f'historical-pdf-text-{i}.txt')
    argv=['pdftotext','-layout',str(source),str(target)]
    cp=subprocess.run(argv,capture_output=True,text=True,check=False)
    assert cp.returncode==0
    t=target.read_bytes()
    report['pdf_text_comparisons'].append({'history':i,'argv':argv,'exit_code':cp.returncode,
      'stderr':cp.stderr,'text_bytes':len(t),'text_sha256':hashlib.sha256(t).hexdigest(),
      'formfeed_pages':t.count(b'\x0c')})
assert Path('historical-pdf-text-own.txt').read_bytes()==Path('historical-pdf-text-16.txt').read_bytes()==Path('historical-pdf-text-99.txt').read_bytes()
report['pdf_text_equal'] = True
report['limits'] = 'Lossless byte aliases/differences and PDF text equality are mechanical evidence, not direct display of every alias, PDF pixels, historical comprehension or universal chronology.'
Path('whole-historical-comparison.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:len(v) for k,v in report.items() if isinstance(v,list)},indent=2))
