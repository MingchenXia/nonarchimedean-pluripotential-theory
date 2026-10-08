#!/usr/bin/env python3
"""Own delivery consistency checks; no mathematical acceptance assertion."""
import pathlib,json,hashlib,re,subprocess
P=pathlib.Path(__file__).resolve().parent
m=json.loads((P/'artifact-bindings.json').read_text())
for e in m['artifacts']:
 b=(P/e['name']).read_bytes();assert len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256'],e['name']
obj=json.loads((P/'native-notes.json').read_text());assert obj['candidate'] is False
seen=set()
for n in obj['notes']:
 assert n['id'] not in seen
 assert set(n['support'])<=seen
 assert all(n.get(k) for k in ['summary','detailedSummary','text'])
 seen.add(n['id'])
assert len(seen)==6
tex=(P/'P05.1-paper.tex').read_text();md=(P/'argument.md').read_text()
sections=re.findall(r'\\section\{([^}]*)\}',tex)
assert len(sections)==12
for s in sections:assert '# '+s in md,s
assert 'candidate=false' in tex and 'Original P05.1/P05.2 remain' in tex
log=(P/'build-pass-3.tex.log').read_text()
for bad in ['Undefined control sequence','There were undefined references','Label(s) may have changed','Overfull','Underfull','Fatal error']:assert bad not in log,bad
assert 'Shell escape feature is not enabled' in log
assert re.search(r'Output written on P05.1-paper.pdf \(14 pages',log)
r=subprocess.run(['python3','exact_checks.py'],cwd=P,capture_output=True,text=True,check=True)
assert r.stdout==(P/'exact-check-output.txt').read_text()
assert all(e['returncode']==0 for e in json.loads((P/'build-runs.json').read_text()))
print(f'Artifact hashes verified: {len(m["artifacts"])}.')
print('Six notes: valid strictly earlier support IDs; candidate=false.')
print('Full Markdown conversion: all 12 TeX sections retained.')
print('Final PDF: 14 pages; references/layout settled; intentional disabled-shell-escape notice retained.')
print('Exact finite output reproduces byte-for-byte. No continuum or independent-acceptance conclusion.')
