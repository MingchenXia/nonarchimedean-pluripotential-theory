"""Owned artifact builder. Reads bound data, never executes supplied programs."""
from pathlib import Path
import json
import shutil

ROOT=Path(__file__).resolve().parent
meta=[
 ('Raw all-support envelopes, graded ideals and actual decreasing-D closure.',
  'Raw positivity iff continuity, actual J_k/factorial formula, strict insertion before energy, and exact one-factor gauge; no increasing closure.', ['G331','E350']),
 ('Excellent normal surface regular models are actual primary blowups.',
  'Exact current surface hypotheses, connected full fibre, residue-weighted matrix/SPD/inverses, strict integral ample boundary and identical punctured graph, all characteristics.', ['G331','n1']),
 ('Full normal surface envelopes from nef projection and a greatest vector.',
  'Actual Cartier pushforward and exceptional negativity dominate every core/C/bounded-D competitor on all supports; clamps and density give every continuous obstacle.', ['G331','n1','n2']),
 ('Continuous envelopes on isolated normal closed algebraic characteristic-zero germs.',
  'Qualified THREE-author BdFF upper coefficient approximation, finite determining-trace repair, all-support uniform C limit and ONE C net per D competitor; exact isolated/algclosed/char0 domain.', ['G331','n1']),
 ('Exact BFJ smooth specialization and one-net USC envelopes.',
  'Closed-face continuity/all retractions and fixed-complex section estimate; ONE C-majorant net handles poles and all decreasing-obstacle nets only after CE is established.', ['G331','E350','n1','n3','n4']),
 ('Finite normal dominating covers transfer positive envelopes.',
  'Full-fibre Galois-orbit MAX and positive trace preserve C/D and give pullback commutation; source CE and absence of vertical components are required, nonflat/nonisolated examples included.', ['G331','n1','n3','n4','n5']),
 ('Explicit full-normalization formula and exact finite-continuous positive domain.',
  'Primary conductor masks, dense finite-conductor continuity and compact quotient give fibre MAX under normal-centre CE; all conductor fibres retained; no unconditional USC/pole formula.', ['G331','n1','n3','n4','n5','n6']),
 ('All-characteristic nonnormal negative obstacle has no maximal D minorant.',
  'Double-plane raw envelope is not USC although source is continuous; exact no-maximal and nonpositive regularization conclusion, not a normal residual counterexample.', ['G331','n1','n7']),
 ('All excellent reduced-curve geometric envelopes equal ideal clipping.',
  'Actual Cartier/DVR positivity and full descent yield all extended branch vectors and min(phi,0), including mixed zeros and bottoms, exact gauge and qualified reference.', ['G331','E350','n1']),
 ('Correct energy signs and universal convergence diagnostics.',
  'Smooth graded staircase and normal parity multiplicities give F=integral(-u)dmu, B=F, negative increasing energies, capacity convergence but non-D exact increasing limits; good envelopes remain.', ['G331','B341','E350','n1']),
 ('Higher-dimensional residual attempted; a sufficient criterion and failed Jacobian bound.',
  'Primary source-nef UPPER approximants would prove CE; nonisolated Jacobian values are unbounded even while an actual smooth cover proves CE on that example. General normal >=3 remains unresolved.', [f'n{i}' for i in range(1,11)]),
 ('Complete scoped deliverable with an impartial incomplete-original judgment.',
  'Surface/isolated/smooth/cover/normalization/curve proofs and evidence delivered. General normal higher-dimensional sectors remain; candidate=false; finite/static results are not mathematical verification.', [f'n{i}' for i in range(1,12)])
]
notes=[]
for i,(summary,detail,support) in enumerate(meta,1):
    body=(ROOT/f'n{i}.md').read_text()
    notes.append(dict(id=f'n{i}',summary=summary,detailedSummary=detail,text=body,support=support))
payload={'notes':notes,'candidate':False}
for name in ['native-notes.json','actual-FINAL.json']:
    (ROOT/name).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')

title='# Geometric obstacle envelopes: normal surfaces, isolated normal germs, and full normalization\n\n'
abstract=('Standalone unverified mathematical reconstruction, 8 October 2026. '
          'Only ENTIRE qualified G331/B341/E350 are incoming grants. '
          'The surface and isolated characteristic-zero sectors and full finite-continuous normalization calculus are proved below; '
          'arbitrary excellent normal dimension>=3 outside the listed sectors remains unresolved. Candidate=false.\n\n')
argument=title+abstract+'\n\n'.join(n['text'] for n in notes)
(ROOT/'argument.md').write_text(argument)
paper=argument+'\n\n'+(ROOT/'exact-scope.md').read_text()+'\n\n'+(ROOT/'whole-source-application-ledger.md').read_text()+'\n\n'+(ROOT/'whole-proof-coverage.md').read_text()+'\n\n'+(ROOT/'original-scope-and-noncircularity-decision.md').read_text()
(ROOT/'P12.3-paper.md').write_text(paper)

def esc(s):
    table={'\\':'\\textbackslash{}','{':'\\{','}':'\\}','_':'\\_','#':'\\#',
           '%':'\\%','&':'\\&','$':'\\$','^':'\\textasciicircum{}','~':'\\textasciitilde{}'}
    return ''.join(table.get(c,c) for c in s)
tex=['\\documentclass[11pt]{article}','\\usepackage[T1]{fontenc}',
     '\\usepackage[utf8]{inputenc}','\\usepackage[margin=1in]{geometry}',
     '\\setlength{\\parindent}{0pt}','\\setlength{\\parskip}{0.5em}',
     '\\emergencystretch=4em','\\title{Geometric obstacle envelopes on normal surfaces and isolated normal germs}',
     '\\author{Independent reconstruction of P12.3}','\\date{8 October 2026}',
     '\\begin{document}\\maketitle',esc(abstract.strip())]
for line in paper.splitlines()[4:]:
    if line.startswith('# '):tex.append('\\section*{'+esc(line[2:])+'}')
    elif line.startswith('## '):tex.append('\\subsection*{'+esc(line[3:])+'}')
    else:tex.append(esc(line))
tex.append('\\end{document}')
(ROOT/'P12.3-paper.tex').write_text('\n'.join(tex)+'\n')

records=json.loads((ROOT/'reports/input-hashes.json').read_text())
orig=next(r for r in records if r['key']=='m21')
shutil.copyfile(ROOT/orig['local'],ROOT/'original-task.json')
decision={
 'task':'Entire original P12.3 and independent reconstruction deliverable',
 'candidate':False,'original_verdict':'INCOMPLETE',
 'status':'Unverified scoped mathematical draft; no publication/catalogue acceptance',
 'only_grants':['G331','B341','E350'],
 'proved_sectors':['Excellent normal surfaces all fields/characteristics including mixed',
                  'Normal isolated closed algebraic germs over algebraically closed characteristic zero',
                  'Exact BFJ smooth closed affine algebraically closed characteristic-zero range',
                  'Actual finite dominating covers with source CE',
                  'Full finite-continuous normalization formula and exact positive domain under normal-centre CE',
                  'Every excellent reduced curve geometric/ideal clipping'],
 'residual':['General nonisolated normal dimension>=3 outside actual-cover sectors',
             'Higher-dimensional positive/mixed characteristic and other excellent normal sectors',
             'No unconditional extended-USC/pole normalization fibre-MAX formula'],
 'historical_native257_candidate_false_immutable':True,
 'seven_historical_254_duplicates_not_current_eleven_257':True,
 'exact_original_bytes':orig['actual_bytes'],'exact_original_sha256':orig['actual_sha256'],
 'compilation_performed':False,'execution_not_mathematical_verification':True,
 'protected_P16_4_unaccessed_unchanged':True}
(ROOT/'acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')
print(json.dumps({'notes':len(notes),'paper_bytes':len(paper.encode()),'candidate':False,'compiled':False}))
