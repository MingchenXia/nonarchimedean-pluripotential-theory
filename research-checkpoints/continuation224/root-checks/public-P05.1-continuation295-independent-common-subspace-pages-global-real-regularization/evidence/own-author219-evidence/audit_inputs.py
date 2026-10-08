#!/usr/bin/env python3
"""Read only the explicitly bound sources; never execute supplied code."""
import hashlib,json,pathlib,platform,subprocess,shutil
BASE=pathlib.Path('/workspace/research/campaigns/round-219/P05.1-common-subspace-independent-normal-pages-all-continuous-real-regularization-paper')
OUT=pathlib.Path(__file__).resolve().parent
math=json.loads((BASE/'mathematical-packet-bindings.json').read_text())
primary=json.loads((BASE/'private-primary-packet-bindings.json').read_text())
rows=[]
for kind,entries in [('math',math),('primary',primary)]:
 for i,e in enumerate(entries):
  b=pathlib.Path(e['path']).read_bytes(); h=hashlib.sha256(b).hexdigest()
  assert h==e['sha256'],(kind,i,'hash mismatch')
  rows.append({'kind':kind,'index':i,'label':e['label'],'format':e.get('format'),'path':e['path'],'bytes':len(b),'LF_lines':b.count(b'\n'),'sha256':h,'verified':True})
(OUT/'source-byte-bindings.json').write_text(json.dumps(rows,indent=2)+'\n')
units={'BMPS':[(254,301,'Definitions 2.1--2.4'),(418,638,'Definitions 2.18--2.31; Lemma 2.24; normal independence; full Lemma 2.34; delegated Lemma 2.35 not imported'),(691,852,'PCC/PA-PC definitions 3.1--3.5, full Lemma 3.4, Proposition 3.7, strictness domain'),(1005,1034,'Proposition 3.22 and Definition 3.23, full proof unit'),(1354,1503,'Definitions 4.4--4.7; Lemma 4.6; Proposition 4.8; full Lemma 4.9 and Lemma 4.11'),(1741,1747,'Definition 4.15 only'),(2253,2360,'Definitions/envelope statements 6.2--6.9, full immediate units')], 'BBGS':[(196,250,'Definitions 2.1--2.3; beginning of 2.4 is not used'),(379,420,'Definitions 2.14--2.15; unused following definition begins'),(443,598,'Definitions 3.1--3.9, Remark 3.6, full Proposition 3.12'),(604,704,'Full Proposition 3.15, Lemma 3.18, Proposition 3.19'),(1515,1555,'Whole Definition 5.1; following examples not applied'),(1913,1993,'Whole Lemma 6.1/Theorem 6.2, inspected endpoint-continuity domain only')]}
(OUT/'primary-unit-coverage.json').write_text(json.dumps({'line_convention':'one-based LF splitting; form-feed does not increment LF number','units':units,'pdfs':'All PDF bytes hash-bound; pertinent proof units read in corresponding bound LF text. No PDF pixels or passages published.'},indent=2)+'\n')
records=[json.loads(x) for x in (OUT/'read-coverage.jsonl').read_text().splitlines()]
coverage=[]
for i,e in enumerate(math):
 s=pathlib.Path(e['path']).read_text(); intervals=sorted((r['start'],r['stop']) for r in records if r['packet']=='math' and r['index']==i)
 end=0
 for a,b in intervals:
  assert a<=end,(i,'coverage gap',end,a)
  end=max(end,b)
 assert end>=len(s),(i,end,len(s))
 coverage.append({'index':i,'label':e['label'],'characters':len(s),'covered_to':end,'intervals':intervals,'whole_body_read':True})
(OUT/'whole-read-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
def version(name):
 p=shutil.which(name)
 return {'path':p,'version':subprocess.run([p,'--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0] if p else None}
env={'python':platform.python_version(),'platform':platform.platform(),'cwd':str(OUT),'pdflatex':version('pdflatex'),'pandoc':version('pandoc'),'supervised_compute':'not exposed; no resource-heavy work launched','agents':'none','network':'unused','provider_calls':'none nested','model_label':'operator requested Codex gpt-6.1-sol xhigh; not independently verifiable from process environment','supplied_programs_executed':False}
(OUT/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
print('Verified 25 mathematical entries and 4 primary byte bindings.')
print('Whole mathematical text coverage: 25/25; source LF units recorded.')
print('No supplied program executed; read-only source audit complete.')
