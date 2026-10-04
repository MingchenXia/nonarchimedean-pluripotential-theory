"""Read-only source snapshots, original inputs, and LF-only primary extraction."""
from pathlib import Path
import hashlib, json, shutil, subprocess, platform, sys

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'sources'; OUT.mkdir(exist_ok=True)
two=Path('/workspace/research/campaigns/round-22/P05.2-arbitrary-graph-product-continuation')
cyl=Path('/workspace/research/campaigns/round-10/P05.2-cyclic-graph-cylinder-continuation')
ar=Path('/workspace/research/shared-sources/many-graph-product-intersection-20261004')
pairs={
 'product-proposal.md':Path('/workspace/research/P05.2-finite-many-graph-product-proposal.md'),
 'intersection-evidence.md':Path('/workspace/research/P05.2-many-graph-intersection-primary-evidence.md'),
 'two-graph-argument.md':two/'artifacts/codex-ODSVkE/P05.2-argument.md',
 'two-graph-run.json':two/'run.json',
 'cylinder-argument.md':Path('/workspace/research/deliverables/round-14/P05.2-finite-graph-cylinders-argument.md'),
 'cylinder-review-provenance.json':Path('/workspace/research/deliverables/round-14/P05.2-finite-graph-cylinders-review.json'),
 'cylinder-original-argument.md':cyl/'artifacts/codex-7TYVqa/P05.2-argument.md',
 'cylinder-run.json':cyl/'run.json',
 'BMPS2603.08664v1.pdf':two/'artifacts/codex-ODSVkE/sources/BMPS2603.08664v1.pdf',
 'BMPS2603.08664v1.txt':two/'artifacts/codex-ODSVkE/sources/BMPS2603.08664v1.txt',
 'Allermann-Rau-0709.3705.pdf':ar/'Allermann-Rau-0709.3705.pdf',
 'Allermann-Rau-0709.3705.txt':ar/'Allermann-Rau-0709.3705.txt',
 'AR-source-retrieval.json':ar/'Allermann-Rau-0709.3705.pdf-retrieval.json',
 'AR-source-record.html':ar/'arxiv-record.html',
 'AR-selected-provenance.json':ar/'root-primary-read-and-evidence.json',
 'one-dimensional-STATEMENT.tex':two/'artifacts/codex-ODSVkE/sources/one-dimensional-STATEMENT.tex',
 'one-dimensional-PROOF.tex':two/'artifacts/codex-ODSVkE/sources/one-dimensional-PROOF.tex',
 'ch72_major_open_problems.tex':Path('/workspace/research/book-source/manuscript/parts/part6/ch72_major_open_problems.tex'),
 'appM_ch18_frontiers.tex':two/'artifacts/codex-ODSVkE/sources/appM_ch18_frontiers.tex',
}
records=[]
for name,origin in pairs.items():
 data=origin.read_bytes(); (OUT/name).write_bytes(data)
 records.append({'file':'sources/'+name,'origin':str(origin),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
expected={'product-proposal.md':'f4943ea1a919694d445533b8f38f7d3a934ea20c129d39f5fb667a1d22822623',
          'intersection-evidence.md':'c164063db379133ae2dc43238fce52adf34481997e0930ace1817651512ffe89'}
for r in records:
 if Path(r['file']).name in expected: assert r['sha256']==expected[Path(r['file']).name]
for name in ['two-graph','cylinder']:
 r=json.loads((OUT/(name+'-run.json')).read_text())
 notes=r['campaign']['result']['notes']
 (OUT/('canonical-'+name+'-notes.json')).write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
 for n in notes:
  (OUT/('canonical-'+name+'-'+n['id']+'.md')).write_text(n['text']+'\n')
inp=json.loads((ROOT/'input.json').read_text())
# The native input is preserved unchanged; task and assignment are copied, not edited.
(ROOT/'task.json').write_text(json.dumps(inp['task'],ensure_ascii=False,indent=2)+'\n')
(ROOT/'original-scope.txt').write_text(inp['task']['problem']+'\n\n'+inp['task']['completionCriteria']+'\n')
(ROOT/'assignment.txt').write_text(inp['assignment']+'\n')
(ROOT/'source-hashes.json').write_text(json.dumps(records,indent=2)+'\n')
ranges={'BMPS2603.08664v1.txt':[(1,43),(257,295),(420,629),(691,786),(886,892),(985,989),(1005,1030),(1354,1391),(1741,1743),(2261,2293)],
        'Allermann-Rau-0709.3705.txt':[(1,35),(297,536)]}
excerpts=[]
for name,spans in ranges.items():
 # Explicit LF split: PDF formfeeds are retained inside lines.
 lines=(OUT/name).read_text().split('\n')
 for lo,hi in spans:
  body='\n'.join(lines[lo-1:hi])+'\n'
  target=name.removesuffix('.txt')+f'-LF-{lo}-{hi}.txt'
  (OUT/target).write_text(body)
  excerpts.append({'source':name,'LF_first':lo,'LF_last':hi,'file':'sources/'+target,'sha256':hashlib.sha256(body.encode()).hexdigest()})
(ROOT/'source-excerpts.json').write_text(json.dumps(excerpts,indent=2)+'\n')
authentication=[]
for name in ['BMPS2603.08664v1','Allermann-Rau-0709.3705']:
 direct=OUT/(name+'-from-pdf.txt')
 command=['pdftotext','-layout',str(OUT/(name+'.pdf')),str(direct)]
 run=subprocess.run(command,capture_output=True)
 assert run.returncode==0
 cached=(OUT/(name+'.txt')).read_bytes(); extracted=direct.read_bytes()
 selected=[]
 for ex in excerpts:
  if ex['source']==name+'.txt' and ex['LF_first']>43:
   body=(ROOT/ex['file']).read_bytes()
   selected.append({'LF_first':ex['LF_first'],'LF_last':ex['LF_last'],'exact_body_present_in_fresh_extraction':body in extracted})
 authentication.append({'source':name,'command':command,'exit_code':run.returncode,
  'matches_cached_text_bytes':cached==extracted,
  'extracted_sha256':hashlib.sha256(extracted).hexdigest(),
  'cached_sha256':hashlib.sha256(cached).hexdigest(),
  'selected_body_checks':selected,
  'limit':'Local PDF/text consistency and cached version provenance, not network authentication or mathematical verification.'})
(ROOT/'source-authentication.json').write_text(json.dumps(authentication,indent=2)+'\n')
environment={'python':sys.version,'platform':platform.platform(),'cwd':str(ROOT),'network_used':False,'subagents_used':False,'supervised_heavy_compute_service':'not exposed; no heavy compute needed or launched'}
for tool in ['pdftotext','pandoc','xelatex']:
 r=subprocess.run([tool,'--version'] if tool!='pdftotext' else [tool,'-v'],capture_output=True,text=True)
 environment[tool]=(r.stdout+r.stderr).split('\n')[0]
(ROOT/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
print(json.dumps({'snapshots':len(records),'canonical_notes':{'two-graph':3,'cylinder':2},'LF_excerpts':len(excerpts),'original_input_retained':True},indent=2))
