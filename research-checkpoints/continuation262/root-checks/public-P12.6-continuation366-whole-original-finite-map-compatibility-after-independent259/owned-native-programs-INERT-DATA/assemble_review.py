"""Owned assembly of full reconstructed proofs and literal bound grants; no supplied code."""
import hashlib,json,pathlib

HERE=pathlib.Path.cwd()
BASE=HERE.parent.parent
mat=json.loads((BASE/'mathematical-packet-bindings.json').read_text())
pri=json.loads((BASE/'private-primary-packet-bindings.json').read_text())
context=json.loads((BASE/'book-context-bindings.json').read_text())
def read(index):return pathlib.Path(mat[index]['path']).read_text()
def sha(b):return hashlib.sha256(b).hexdigest()
summaries=[
 ('Actual primary finite pullback, full compact quotient regularization, and openness criterion.',
  'Rees base change uses global finite semilocal B, actual regular Cartier image divisors and support quotient lattices before G331 completions. Full-fibre MAX regularization needs no openness; continuous full-support kernels on every continuous test imply openness. Normal targets require every minimal source component dominating.'),
 ('Reduced-flat determinant kernels and positive full-fibre maxima on C and actual D nets.',
  'Every Artinian valuation fibre retains inseparable/nilpotent lengths. Coefficient ideals give norm/minimum identities, all-support test density gives choice independence/full support/continuity, and actual primary coefficient truncations preserve the minimum. Normal nonvertical maxima descend via splitting orbits.'),
 ('Selected E on all stated USC obstacles, exact positivity/quotient laws and smooth BFJ identification.',
  'E is positive iff raw has an actual greatest D minorant. Finite continuous obstacles reduce to continuous raw C envelopes. Open positive-MAX maps commute for all obstacles; arbitrary injections have the constrained full-fibre-MAX rule. BFJ identification is only the closed smooth affine algclosed characteristic-zero fixed-dual-complex signature.'),
 ('All-field node: selected envelope loses positivity and has reverse gap ONE under normalization.',
  'The two-plane conductor quotient and exact primary masks determine the raw and USC envelopes. Constrained upstairs regularization is continuous (-1,-2) but not fibre constant; the second shared lift gives gap ONE. Full source schemes include off-diagonal vertical self-base-change components.'),
 ('Normal exact-image and vertical-injection obstructions, with both envelopes positive.',
  'For k[[x,y]]/(xy) the intrinsic envelope is (-1,0), while ambient E=-1 and no D extension exists by the normal zero dichotomy. R->R times quotient is nonopen and fails envelope commutation despite positivity on both sides; lower curve support is retained with ambient top product zero.'),
 ('Full all-pulled product projection, actual supported cycles and multigraded module bridge.',
  'Proper equal-delta top-component cycles precede Chow/multiplicity; Artinian layers retain all thicknesses and field degrees. Current SH multi-Rees intersection squeeze, rational rays and prime filtration give the complete top-polynomial identity without coefficient ordering; dense moments and prescribed bounded D nets yield all arities.'),
 ('ONE arbitrary source slot: normal traces and full conductor-admissible projection.',
  'Splitting orbits retain generic inseparable lengths, d/|G| and ed cancellation. General reduced injections use both normalization base-change injections and every normal centre; full fibre constancy is exact admissibility. Reduced-flat base change is reduced and determinant base change proves automatic full admissibility on all supports.'),
 ('Unnormalized towers, sharp normalized/multiple-slot failures and exact independent gauges.',
  'General conductor towers require both intermediate admissibilities. Flat Artinian tower lengths multiply; varying branch averages are -2/3 versus -1/2 with trace -2. Multiple arbitrary slots fail with masses 0,1,1/4. Function division and exactly one measure factor are mandatory for independent gauges.'),
 ('Whole manuscript/source audit, actual-versus-expanded FINAL qualification, and finite evidence.',
  'Entire current argument/ten sections, all ten separately captured actual fields, full ledger/scope/coverage/decisions/qualification and bound context were read. Local expanded artifact is not captured FINAL; all ten actual texts differ. Complete immediate new sources were read; finite diagnostics/119 byte matches are observations only.'),
 ('Complete qualified ORIGINAL P12.6 solution and independent whole-review verdict.',
  'All finite-map cone, specified selected-envelope, bounded-product, normalization/conductor/tower/gauge cases are reconstructed, with sharp necessary failures and exact smooth scope. General P12.3 positivity and outside theories are not imported. No exact original gap retained; draft PASS does not perform external acceptance/count/publication/compiler changes.')]
supports=[['G331','G345'],['G331','n1'],['G331','G345','n1','n2'],
 ['G331','n1','n3'],['G331','G345','n1','n3','n4'],
 ['G331','G345','n1','n2'],['G331','G345','n1','n2','n6'],
 ['G331','G345','n1','n2','n3','n6','n7'],
 ['G331','G345']+[f'n{i}' for i in range(1,9)],
 ['G331','G345']+[f'n{i}' for i in range(1,10)]]
notes=[]
for i,(summary,detail) in enumerate(summaries,1):
 body=(HERE/'sections'/f'n{i}.md').read_text()
 notes.append({'id':f'n{i}','summary':summary,'detailedSummary':detail,'text':body,'support':supports[i-1]})
result={'notes':notes,'candidate':True}
for name in ['native-notes.json','actual-FINAL.json']:
 (HERE/name).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(HERE/'whole-proof.md').write_text('\n\n'.join(n['text'] for n in notes))
grantdir=HERE/'qualified-grants';grantdir.mkdir(exist_ok=True)
header=r'''\documentclass[11pt]{article}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setmonofont{DejaVu Sans Mono}
\usepackage{amsmath,amssymb,geometry,fvextra}
\geometry{margin=1in}
\DefineVerbatimEnvironment{ReviewBody}{Verbatim}{breaklines,fontsize=\small}
\DefineVerbatimEnvironment{GrantBody}{Verbatim}{breaklines,fontsize=\tiny}
\title{P12.6: Independent whole-original review\\Full reconstructed finite-map proof and literal qualified grants}
\author{Independent review; unverified mathematical draft}
\date{8 October 2026}
\begin{document}
\maketitle
The following ten complete proof sections, source ledger, coverage and scope decisions constitute a standalone review. Only ENTIRE qualified G331/G345 are correctness grants. Current362 and actual native256 verdicts are DATA. No compilation or external acceptance is claimed.
\tableofcontents
'''
tex=[header]
for n in notes:
 tex+=['\n\\section{'+n['id']+'}\n','\\textit{Supports: '+', '.join(n['support'])+'.}\n',
       '\\begin{ReviewBody}\n',n['text'],'\\end{ReviewBody}\n']
for name in ['whole-source-application-ledger.md','whole-proof-coverage.md','exact-scope.md','original-scope-and-noncircularity-decision.md']:
 tex+=['\n\\section{'+name.replace('-',' ')+'}\n','\\begin{ReviewBody}\n',(HERE/name).read_text(),'\\end{ReviewBody}\n']
tex.append('\n\\appendix\n')
literal=[]
for i in range(14):
 p=pathlib.Path(mat[i]['path']);b=p.read_bytes()
 dest=grantdir/(f'{i:02d}-'+p.name);dest.write_bytes(b)
 text=b.decode()
 assert '\\end{GrantBody}' not in text
 tex+=['\n\\section{Literal qualified component '+str(i)+'}\n','\\begin{GrantBody}\n',text,
        '\n\\end{GrantBody}\n']
 literal.append({'index':i,'file':str(dest.relative_to(HERE)),'bytes':len(b),'sha256':sha(b)})
tex.append('\n\\end{document}\n')
(HERE/'P12.6-review-paper.tex').write_text(''.join(tex))
paper=pathlib.Path(mat[48]['path']).read_bytes();argument=pathlib.Path(mat[49]['path']).read_bytes()
expanded=json.loads(read(50));actual=json.loads(read(51))
section_checks=[]
for i in range(60,70):
 b=pathlib.Path(mat[i]['path']).read_bytes();n=pathlib.Path(mat[i]['path']).stem
 section_checks.append({'index':i,'name':n,'in_current_paper':b in paper,'in_argument':b in argument})
remaining=paper
for i in sorted(range(14),key=lambda j:mat[j]['bytes'],reverse=True):
 b=pathlib.Path(mat[i]['path']).read_bytes();assert b in remaining
 remaining=remaining.replace(b,b'',1)
for i in range(60,70):
 b=pathlib.Path(mat[i]['path']).read_bytes();assert b in remaining
 remaining=remaining.replace(b,b'',1)
(HERE/'read-data/current-paper-fresh-bridges.tex').write_bytes(remaining)
doc={'current_sections':section_checks,'all_grants_in_current':all(pathlib.Path(mat[i]['path']).read_bytes() in paper for i in range(14)),
 'all_actual_texts_differ':all(a['text']!=e['text'] for a,e in zip(actual['notes'],expanded['notes'])),
 'local_expanded_pair_equal':pathlib.Path(mat[50]['path']).read_bytes()==pathlib.Path(mat[52]['path']).read_bytes(),
 'captured_FINAL_is_distinct':pathlib.Path(mat[51]['path']).read_bytes()!=pathlib.Path(mat[52]['path']).read_bytes(),
 'fresh_bridge_bytes':len(remaining),'literal_grants':literal}
(HERE/'evidence/assembly.json').write_text(json.dumps(doc,indent=2)+'\n')
decision={'verdict':'WHOLE_ORIGINAL_PASS_WITH_MANDATORY_QUALIFICATIONS','candidate':True,
 'exact_atom':'P12.6','review_complete':True,'external_acceptance_performed':False,
 'mathematical_gaps':[],'reconstruction_addition':'Explicit BFJ fixed-dual-complex selected-envelope comparison in n3',
 'grants':['ENTIRE qualified G331','ENTIRE qualified G345'],
 'mandatory_qualifications':['Actual primary models only','All support points and full conductor fibres',
 'Bounded prescribed-D-limit decreasing nets','Reduced generic ranks/full field degrees and supported thicknesses',
 'Current SH17.4.7 finite CURRENT quotient correction','Closed smooth affine algclosed characteristic-zero BFJ scope',
 'Captured actual native256 FINAL distinct from local expanded artifact',
 'Only ONE arbitrary source slot','Both intermediate conductor tower admissibilities','Exactly ONE measure gauge factor'],
 'P12_3_general_positive_envelopes_closed':False,'P12_5_energy_imported':False,
 'P12_5_external_status':'Already accepted E350/paper96; outside this grant/review',
 'protected_P16_4_unchanged':True,'catalogue_mutation':False,'publication':False,
 'compiler_run':False,'formal_verification':False,'supplied_program_execution_or_import':False,
 'subagents_or_model_jobs':False,'heavy_compute':'No exposed facility; none launched or needed'}
(HERE/'acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')
(HERE/'whole-source-application-ledger.json').write_text(json.dumps({'ledger':'whole-source-application-ledger.md',
 'scope':'exact-scope.md','coverage':'whole-proof-coverage.md','decision':'acceptance-decision.json',
 'immediate_sources':{'Stacks':['01OF31.33.1-14','0AYA42.26.1-4','02QL42.7.1','0BEL33.45.1-13','0BD2CURRENT31.18.6','00HS10.39.19'],
 'SH_CURRENT':['17.1.6','17.2.1-4 context','17.4.1-7'],'BFJ':['Setting','3.15-3.22 and proof3.18']},
 'historical_foundations_recursively_freshly_read':False},indent=2)+'\n')
print(json.dumps({'notes':len(notes),'proof_bytes':len((HERE/'whole-proof.md').read_bytes()),
 'paper_bytes':len((HERE/'P12.6-review-paper.tex').read_bytes()),'all_actual_texts_differ':doc['all_actual_texts_differ'],
 'whole_draft_verdict':decision['verdict'],'compiler_run':False},indent=2))
