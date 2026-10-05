#!/usr/bin/env python3
"""Artifact checks only; no claim to verify the mathematics."""
import hashlib,json,pathlib,re
R=pathlib.Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
frozen=json.loads((R/'input-manifest.json').read_text())
for p,h in frozen.items():assert sha((R/p).read_bytes())==h,p
assert (R/'input.json').read_bytes()==(R/'input-original.json').read_bytes()
m=json.loads((R/'source-manifest.json').read_text())
sources={s['id']:s for s in m['sources']}
for s in m['sources']:
 if 'path' in s:assert sha((R/s['path']).read_bytes())==s['sha256']
 for p in s.get('raw_responses',[]):assert sha((R/p['path']).read_bytes())==p['sha256']
for u in m['units']:
 b=(R/u['path']).read_bytes();assert sha(b)==u['sha256'],u['id']
 if u['source']!='gr-web':
  a=(R/sources[u['source']]['path']).read_bytes().decode('utf8').split('\n')
  assert b=='\n'.join(a[u['lf_first']-1:u['lf_last_inclusive']]).encode('utf8'),u['id']
 else:assert len(b.decode('utf8').split('\n'))==u['lf_last_inclusive']
p=json.loads((R/'premises.json').read_text());assert [x['index'] for x in p]==list(range(9))
for x in p:
 assert x['statement'] and x['applicability'] and x['passages']
 for z in x['passages']:assert z['premise']==x['index'] and z['url'].startswith('https://')
s=json.loads((R/'status.json').read_text());assert set(s)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert s['id']=='P21.3' and s['status']=='partial' and len(s['concrete_gaps'])>=1
d=json.loads((R/'canonical-notes.json').read_text());assert d['candidate'] is False and 1<=len(d['notes'])<=4
seen=set()
for n in d['notes']:
 assert set(n)=={'id','summary','detailedSummary','text','support'}
 assert re.fullmatch(r'n[1-9][0-9]*',n['id']) and n['id'] not in seen
 assert set(n['support'])<=seen
 seen.add(n['id'])
for p in ['P21.3-argument.md','P21.3-paper.tex','P21.3-paper.pdf','P21.3-primary-evidence.md']:
 assert (R/p).exists() and (R/p).stat().st_size>1000,p
assert (R/'P21.3-paper.pdf').read_bytes().startswith(b'%PDF-')
ex=(R/'logs/P21.3-paper-extracted.txt').read_text()
for term in ['Original P21.3 remains unresolved','bounded-generated','closed subspaces','Concrete unresolved']:
 assert term.lower() in ex.lower(),term
art={str(p.relative_to(R)):sha(p.read_bytes()) for p in R.iterdir() if p.is_file() and p.name not in ['artifact-manifest.json']}
(R/'artifact-manifest.json').write_text(json.dumps(art,indent=2)+'\n')
print(f'PASS: inputs unchanged; {len(m["units"])} literal primary units; 9 premise indices; status/notes schemas; standalone PDF present.')
print('These checks prove source/artifact integrity and successful compilation only. The mathematical drafts are unverified and P21.3 remains unresolved.')
