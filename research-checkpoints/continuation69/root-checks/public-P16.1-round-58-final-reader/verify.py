#!/usr/bin/env python3
"""Required preservation/build verification only; no mathematical oracle."""
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parent
checks=[]
def check(label,predicate):
 ok=bool(predicate);checks.append({'check':label,'passed':ok})
 if not ok: raise AssertionError(label)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
b=(ROOT/'input.json').read_bytes();original=(ROOT/'input-original.json').read_bytes();inp=json.loads(b)
check('input preservation byte identity',b==original)
check('original input supplied hash',hashlib.sha256(b).hexdigest()=='11b47ecad0c8cc8933bf66d01493f7afdd07b90f9faef17e12e041ae14700782')
check('assignment value preserved',(ROOT/'assignment-original.txt').read_text()==inp['assignment'])
check('task values preserved',json.loads((ROOT/'task-original.json').read_text())==inp['task'])
status=json.loads((ROOT/'status.json').read_text())
check('exact five status keys',set(status)=={'id','status','exact_result','proof_file','concrete_gaps'})
check('status partial',status['status']=='partial' and status['id']=='P16.1' and len(status['concrete_gaps'])==4)
check('proof file exists',(ROOT/status['proof_file']).is_file())
prov=json.loads((ROOT/'source-extracts/source-provenance.json').read_text())
for source in prov['sources']:
 for f in source['files']:
  check(f"{source['id']} {Path(f['artifact']).suffix} hash",digest(ROOT/f['artifact'])==f['sha256'])
  check(f"{source['id']} {Path(f['artifact']).suffix} byte count",(ROOT/f['artifact']).stat().st_size==f['bytes'])
for e in prov['excerpts']:
 start,end=e['inclusive_one_based_LF_range']
 lines=(ROOT/'sources'/f"{e['source']}.txt").read_text(encoding='utf-8').split('\n')
 literal='\n'.join(lines[start-1:end])
 check(e['id']+' exact LF and artifact',literal==e['literal_statement_and_relevant_proof_body']==(ROOT/e['artifact']).read_text())
 check(e['id']+' application and concrete limit',bool(e['checked_application']) and bool(e['concrete_limit']))
records=json.loads((ROOT/'build-results.json').read_text())
check('one render and two compile records',len(records)==3 and all(r['returncode']==0 for r in records))
for r in records:
 for f in [r['stdout'],r['stderr']]+([r['tex_log']] if r['tex_log'] else []):
  check(f+' retained',(ROOT/f).is_file())
for run in [1,2]:
 log=(ROOT/f'tex-run-{run}.log').read_text(errors='replace')
 check(f'TeX run {run} wrote PDF','Output written on P16.1-paper.pdf' in log)
 check(f'TeX run {run} no fatal error','Fatal error' not in log and '! LaTeX Error' not in log)
check('standalone TeX',r'\documentclass' in (ROOT/'P16.1-paper.tex').read_text() and r'\begin{document}' in (ROOT/'P16.1-paper.tex').read_text())
check('PDF header',(ROOT/'P16.1-paper.pdf').read_bytes().startswith(b'%PDF-'))
argument=(ROOT/'P16.1-argument.md').read_text()
check('paper explicit target incomplete','not established in this paper' in argument and 'onto normalization remain unresolved' in argument)
check('no claimed generic punctured limit','**not** an ordinary punctured-neighborhood limit' in argument)
report={'kind':'observed preservation/extraction/schema/build checks, not a mathematical verdict','passed':len(checks),'failed':sum(not x['passed'] for x in checks),'checks':checks,'input_sha256':hashlib.sha256(b).hexdigest(),'pdf_sha256':digest(ROOT/'P16.1-paper.pdf'),'pdf_pages':int(re.search(r'^Pages:\s+(\d+)',(ROOT/'pdfinfo.stdout.txt').read_text(),re.M).group(1)),'candidate':False}
(ROOT/'verification-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['passed','failed','pdf_pages','input_sha256','pdf_sha256','candidate']}))
