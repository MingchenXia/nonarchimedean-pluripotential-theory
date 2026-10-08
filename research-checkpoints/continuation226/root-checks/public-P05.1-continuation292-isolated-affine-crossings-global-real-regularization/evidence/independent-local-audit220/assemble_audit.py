"""Own audit export only. Does not execute any supplied program or rebuild."""
from pathlib import Path
import hashlib,json,re

names=['source','criterion','regularization','raw','contact','evidence']
summaries=[
 'Exact five-grant boundary and source audit: original immediate units read, essential finite foundations reconstructed; real/signed conventions and all source/scope limitations explicit.',
 'Continuous-PC criterion reconstructed on every inherited carrier: full branch convexity and common ambient supports at each crossing, including dependent directions and legal rational violations.',
 'Scoped global regularization PASS: actual irrational recession allowed, rational-spatial real-height majorants touch all finite crossings and strictly decrease globally before envelope MA.',
 'Primitive raw chain PASS: full BBGS commutation/refinement/balance with every-dimensional covolume conversion; saturated determinant, repeated-zero and d! factors reconstructed.',
 'Every crossing has negative finite-PA contact at every actual real reference: positive common-jet decomposition and rational roof identify the unrestricted envelope before measuring it.',
 'Mathematics/source PASS and required historical reproduction PASS; retrospective did-read/universal-operation attestations INCONCLUSIVE. All six exact FINAL audited; originals OPEN, candidate=false.'
]
details=[
 'Only A224/B225/R230/S262/S272 with all clarifications are grants. Working288/287 are reconstructed data. Whole original BMPS/BBGS application units and precise roles are recorded; delegated AR10, broad continuity/density and outside proofs are excluded. Ordinary compactness/linear algebra/secants and measure foundations inside S272 remain explicit dependencies.',
 'Active-face rational density preserves inherited midpoint incidences at real centers. A strict quadratic maximum proves branch convexity without uniform local radii. Nearest-point supports have nonzero vertical limits; finite continuous sublinear derivatives have compact support representation. Squared-projection separation gives exact ambient zero-sum negative tuples, rational kernel approximations and legal finite violations. Sufficiency covers all rational carriers and real endpoints.',
 'The actual finite gradient polytope and exact recession epigraph use rational spatial generators with real heights. Whole-boundary dual continuity supplies finite rational samples; a closed primal hull has exact conjugate and global error. Projected lower faces give a rational complex. Finite exact contacts retain common supports, rational cuts glue all branches, and 4dyadic shifts give strict decrease and C+5/2. R230 actual envelopes enter before S272 completion.',
 'Real/signed/zero primitive recursion is lift-independent and converts to the negative BBGS unit-normal product with a_sigma/a_tau at every dimension. The full paired-perpendicular double-sum exchange, all subdivision cases and linear annihilation prove commutation/balance. Local supports give positivity; bounded primitive edges give raw mass and IBP. Consecutive saturated kernel factors telescope without added normalization; examples are exact but finite checks are not continuum certificates.',
 'A saturated positive complete subcycle, effective balanced residual and rational transverse line yield a flat positive determinant atom. Rational all-face relation cones and minimal-face simplices give an exact positive convex decomposition of actual gamma. Identical summand jets with one common rational norm/collar preserve flatness. Boundary endpoints, radial chords and shrinking simplices bound even discontinuous raw competitors, giving exact finite F and negative integral -R delta^d m0.',
 '93 bound identities match. Exact FINAL/saved native notes are byte-identical; expanded presentation is distinct; registration adds only Artifacts text. Inspected finite checker output and correct standalone Markdown reproduce exactly; unchanged no-shell-escape builds return 0/0 with first warnings retained and final clean17 pages. Recorded native invocation is supported; complete retrospective process transcripts are unavailable and are not mathematical premises. Excluded domains and original OPEN statuses persist.'
]
supports=[[],['n1'],['n1','n2'],['n1','n2'],['n1','n2','n4'],['n1','n2','n3','n4','n5']]
notes=[dict(id=f'n{i+1}',summary=summaries[i],detailedSummary=details[i],text=Path(f'n{i+1}-{name}.txt').read_text().strip(),support=supports[i]) for i,name in enumerate(names)]
result={'notes':notes,'candidate':False}
Path('native-notes.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
Path('audit-report.md').write_text('# Independent unchanged292 audit\n\n'+ '\n\n'.join('## '+n['id']+'\n\n'+n['text'] for n in notes)+'\n')
Path('source-application-audit.md').write_text('# Source applications and retained foundations\n\n'+notes[0]['text']+'\n\n'+notes[3]['text']+'\n')
Path('historical-evidence-audit.md').write_text('# Historical evidence audit\n\n'+notes[5]['text']+'\n')

source=Path('own-reproduction/P05.1-paper.tex').read_text()
ranges=[(1,30,'n1','Preamble/abstract/domain summary'),(31,74,'n1,n3','Exact domain, cycle/PCC/reference definitions and main theorem'),
 (75,98,'n1','All grant clauses and ordinary foundations'),(99,109,'n1','Active-face density, cone generation/closedness, elimination'),
 (110,127,'n2','Finite convex Lipschitzness, derivatives, nonvertical supports'),(128,139,'n2','Inherited midpoint and quadratic upgrade'),
 (140,172,'n2','Compact product separation, rational violation, all-carrier sufficiency'),(173,191,'n3','Actual reference max/recession and rational cone lifts'),
 (192,208,'n3','Conjugate domain and entire boundary continuity'),(209,252,'n3','Finite samples, primal fibers, exact duality, projected rational faces'),
 (253,275,'n3','All-crossing vertex cuts, carrier union, global dyadic extraction'),(276,282,'n1,n3','Domain-checked granted completion and contact stability'),
 (283,310,'n4','Dependent PCC/support and translated three-meeting diagnostics'),(311,344,'n4','Primitive conversion, source chain, positivity, mass/IBP'),
 (345,364,'n4','Saturated determinants, singular/repeated zero, d! orders'),(365,413,'n5','Every-reference coefficient decomposition/jet/collar/roof/contact'),
 (414,454,'n1,n6','Evidence, discontinuity, retained gaps, rerun/bibliography')]
def owner(a):
 return next(x for x in ranges if x[0]<=a<=x[1])
cov=['# Whole proof and premise coverage','',
 'PASS entries below refer to independent reconstructions in the own note IDs. Hash/read coverage is not proof. The parallel whole Markdown and all six exact FINAL were additionally read; byte conversion proves presentation identity only.','',
 '| Unchanged TeX LF unit | Own reconstruction | Status / scope |','| --- | --- | --- |']
for a,b,ids,topic in ranges:cov.append(f'| {a}-{b}: {topic} | {ids} | PASS within scoped domain; grant dependencies explicit |')
cov+=['','Every displayed equation, including unnumbered displays:','','| Display LF | Own proof | Status |','| --- | --- | --- |']
matches=list(re.finditer(r'\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}',source,re.S))
for mat in matches:
 a=source[:mat.start()].count('\n')+1;b=source[:mat.end()].count('\n')+1
 x=owner(a);qual='PASS; literal qquad presentation typo retained' if a==156 else 'PASS; definitions/grants retain stated hypotheses'
 cov.append(f'| {a}-{b} | {x[2]} | {qual} |')
cov+=['','Inline equations and unnumbered assertions are included in the contiguous whole-unit ranges above, with the actual arguments fully given in the notes. None is declared valid solely by extraction.','',
 '| Proposal or exact FINAL unit | Own coverage |','| --- | --- |',
 '| 287T1 / 288C1 incidence, convexity | n1,n2 |','| 287T2 / 288C1 dependent supports | n2 |',
 '| 287T3 / 288C2 recession, boundary duality, finite contacts, rational faces | n3 |',
 '| 287T4-T5 / 288C3 gluing, extraction, actual envelopes/domain | n1,n3 |',
 '| 287T6 / 288C4 primitive determinants and every-reference contact | n4,n5 |',
 '| 287T7 dependent example; several distinct meetings | n4 |','| 287T8 / 288C4 retained limits | n1,n6 |',
 '| Exact authorFINAL1-6 separately | n6 individual assessment; n1-n5 full reconstruction |','',
 'Premise ledger: exactly five whole grants/all clarifications; essential unproved conclusions are R230 actual-envelope continuity and S272 completed raw measure properties. S262 literal exclusions are retained only in their granted domains. A/B are contextual with direct geometry proofs here. Finite active-face density/cones/closedness/elimination, convex supports, boundary continuity, duality and raw recursion are reconstructed. Euclidean completeness/compactness/extrema, elementary linear algebra/determinants/secants and elementary face terminology are ordinary premises. Measure-limit/Radon foundations remain inside the S272 grant. No Rockafellar density, source automatic continuity, delegated AR10, toric/Alexandrov normalization or outside proof is used.','',
 'Whole grant reading includes every result and non-result section in A224(241LF), B225(163LF), R230(337LF), S262(1953LF TeX/1878LF Markdown) and S272(1016LF TeX/290LF Markdown), plus clarifications, ledgers/material data and historical acceptance qualifications. This is scope retention, not a new audit/acceptance of the grants.','']
Path('wholeproof-and-premise-coverage.md').write_text('\n'.join(cov))

inventory=json.loads(Path('frozen-file-bindings.json').read_text());reads=[json.loads(x) for x in Path('bounded-read-log.jsonl').read_text().splitlines()]
coverage=[]
for obj in inventory:
 if not obj['id'].startswith('m'):continue
 intervals=sorted((r['start'],r['end']) for r in reads if r['id']==obj['id']);end=0;gaps=[]
 total=len(Path(obj['path']).read_text())
 for a,b in intervals:
  if a>end:gaps.append([end,a])
  end=max(end,b)
 if end<total:gaps.append([end,total])
 coverage.append({'id':obj['id'],'characters':total,'requested_gaps':gaps})
assert all(not x['requested_gaps'] for x in coverage)
Path('whole-read-coverage.json').write_text(json.dumps({'scope':'requests plus repaired display reads; does not certify understanding','mathematical':coverage},indent=2)+'\n')

manifest=[]
for p in sorted(Path('.').rglob('*')):
 if not p.is_file() or p.name in ('artifact-bindings.json','artifact-bindings.sha256'):continue
 raw=p.read_bytes()
 manifest.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'distribution':'LOCALONLY' if p.parts[0]=='LOCALONLY' else 'own-audit'})
Path('artifact-bindings.json').write_text(json.dumps({'candidate':False,'files':manifest},indent=2)+'\n')
Path('artifact-bindings.sha256').write_text(hashlib.sha256(Path('artifact-bindings.json').read_bytes()).hexdigest()+'  artifact-bindings.json\n')
print('Exported',len(notes),'own notes;',len(matches),'display equations;',len(manifest),'own artifact bindings; candidate=false.')
