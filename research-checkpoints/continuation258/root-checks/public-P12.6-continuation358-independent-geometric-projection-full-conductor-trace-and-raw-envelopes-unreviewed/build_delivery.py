import json,pathlib,hashlib,shutil
root=pathlib.Path('/workspace/research/campaigns/round-255/P12.6-whole-original-finite-transfer-independent-reconstruction'); out=pathlib.Path.cwd()
manifest=json.loads((root/'mathematical-packet-bindings.json').read_text()); attach=out/'attachments';attach.mkdir(exist_ok=True)
for row in manifest[:14]:shutil.copyfile(row['path'],attach/pathlib.Path(row['path']).name)
shutil.copyfile(root/'original-task.json',out/'original-task.json')
meta=[
('Actual finite primary-model pullback and full positive injection descent; noninjective exact-image restriction need not extend.', 'All supports, conductor-infinite and partial-bottom fibres are retained. The source blowup is CLOSED in base change by a Rees surjection. Independent Cartier effectivity, curve degrees and support-quotient lattices prove geometric pullback before comparison.', ['G331','G345']),
('Universal raw C/D envelope inequality and exact fibre-admissible identity, with precise positivity transfer.', 'The competitor sets are bijective by full geometric descent. No arbitrary supremum membership, USC regularization or increasing closure is assumed. Admissible unrestricted equality holds exactly when the actual upstairs envelope is full-fibre constant.', ['G331','n1']),
('Exact continuous-obstacle normalization gap one on an excellent reduced xy surface, at the entire shared conductor-infinite fibre.', 'The normalization and conductor are computed explicitly. Every second-plane C/D competitor obeys the regular-order bound. The entire upstairs envelope is a genuine primary profile (-1,-2); downstairs value at the shared point is -2. Vertical factors and maximum discontinuity are explicit.', ['G331','n1','n2']),
('Every-field noninjective smooth-target quotient obstruction with positive continuous envelopes on BOTH spaces and no D ambient extension.', 'On R=k[x,y]_(x,y), f=-1/v(x) has P_R=-1 on FULL X_R; on Q=R/(xy) its envelope is (-1,0), obtained from genuine primary ideals. Normal zero dichotomy disproves extension despite injective boundary restriction. Gauge, non-USC increasing limit and different intrinsic arities are proved.', ['G331','G345','n1','n2']),
('General varying-component ambient-degree projection for independently geometric bounded products, before module comparison.', 'General-degree actual cycle projection and closed residue numerical projection precede multigraded Artin--Rees/prime-filtration coefficients. Full field degrees include inseparability and zero for missing components. Dense all-support tests and actual bounded prescribed-limit nets prove the Radon identity.', ['G331','G345','n1']),
('Normal-domain full orbit maxima, unrestricted RAW envelope identity and ONE arbitrary-slot unnormalized geometric trace projection.', 'The common normal closure identity has coefficient d/|G| including inseparability on every support. Orbit linearity plus valid E/B and E/A projections give the target trace product with NO extra d. Vertical components are excluded from maxima, retained with zero ambient degree in dominating trace sums.', ['G331','G345','n1','n2','n5']),
('General reduced finite injections admit a geometric ONE-slot trace formula on the exact FULL conductor-admissible domain.', 'With C=(B tensor_R S)_red, vertical/lower components stay. Generic dominating branch trace tuples must be constant on EVERY S/R fibre, including infinite conductor and lower-centre points. Full G331 descent, C/B top degree one and exact G345 normalization residue weights give the formula.', ['G331','G345','n1','n5','n6']),
('Reduced finite-flat determinant full-support kernels and coefficient maxima give automatic full conductor admissibility and geometric ONE-slot projection.', 'Projective determinant norms and genuine characteristic coefficient ideals are basis/family independent and commute with base change. Artinian support-fibre lengths and inseparability are retained. Deep PRIMARY truncation gives exact min/max functions; finite-fibre actual decreasing nets give D membership. Generic reduced plus torsion-free base change and going-down supply the geometric formula.', ['G331','G345','n1','n2','n5','n6','n7']),
('Whole scoped proof PASS with qualifications; whole-original completion INCONCLUSIVE, candidate=false. Towers/gauges and exact remaining envelope operator issue are explicit.', 'Unnormalized trace towers require intermediate full admissibility, flat determinant towers compose, generic/closed degrees multiply. Varying normalized averages and multiple arbitrary traced slots are false. Separate source gauges have ONE measure factor and precisely rescaled trace slot. New n4/n7 repair author scope; no automatic all-P12.3 prerequisite or forced closure.', ['G331','G345']+[f'n{i}' for i in range(1,9)])]
texts=[];notes=[]
for i,(summary,detail,support) in enumerate(meta,1):
 text=(out/'sections'/f'n{i}.tex').read_text();texts.append(text)
 tail=f'\n\nArtifacts: sections/n{i}.tex, proof.tex, whole-proof.md, argument.md and P12.6-paper.tex contain this complete argument. Full qualifications: whole-source-application-ledger.md, exact-scope.md, whole-proof-coverage.md and original-scope-and-noncircularity-decision.md. Rerun: python audit_inputs.py; python bounded_checks.py; python build_delivery.py; python final_audit.py. No supplied script or compiler is executed.'
 if i==9:tail+=' Observations: 74 bound files match; 2201 exact finite arithmetic cases have zero failures. These and artifact checks are not mathematical verification. No supervised heavy facility was exposed or needed; no heavy computation, native job, agent, active254 reading, external acceptance or publication was performed.'
 notes.append(dict(id=f'n{i}',summary=summary,detailedSummary=detail,text=text+tail,support=support))
proof='\n\n'.join(texts);(out/'proof.tex').write_text(proof)
(out/'whole-proof.md').write_text('# Complete independently reconstructed proof\n\n'+proof)
(out/'argument.md').write_text('# Complete local argument and qualifications\n\n'+proof+'\n\n'+(out/'whole-source-application-ledger.md').read_text()+'\n\n'+(out/'exact-scope.md').read_text())
(out/'native-notes.json').write_text(json.dumps({'notes':notes,'candidate':False},ensure_ascii=False,indent=2))
head=r'''\documentclass[11pt]{article}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setmonofont{DejaVu Sans Mono}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{fvextra}
\DefineVerbatimEnvironment{GrantData}{Verbatim}{breaklines,fontsize=\tiny}
\setlength{\parindent}{0pt}\setlength{\parskip}{0.6em}\emergencystretch=4em
\title{Geometric finite transfer on the full singular boundary\\Independent reconstruction, one-slot conductor traces, and exact envelope obstructions}
\author{Independent whole-original P12.6 review and completion attempt}
\date{8 October 2026}
\begin{document}\maketitle
\begin{abstract}
Using only the entire qualified G331 and G345, we reconstruct actual-primary finite pullback, full positive descent and varying-component geometric bounded-product projection. A single arbitrary source slot has an unnormalized geometric trace formula on the exact full conductor-admissible domain, automatically for reduced finite-flat maps. Normal-domain and flat raw envelopes commute, while exact continuous-obstacle normalization and noninjective quotient counterexamples give gap one. The quotient example has positive envelopes on both spaces and disproves ambient extension. Every support, inseparable and Artinian fibre multiplicity, closed residue weight, actual prescribed-limit net and one-factor gauge rule is retained. The scoped proof judgment is PASS with source qualifications; exact-original completion is INCONCLUSIVE because the residual specified positive/regularized envelope operator calculus is not identified by the raw package. Candidate=false; no automatic all-P12.3 requirement and no forced original closure.
\end{abstract}
\paragraph{Original target.} P12.6 asks compatibility of independently geometric singular psh cones, envelopes and Monge--Ampere products with finite maps, normalization and conductor descent. Known valuative transfer is not itself geometric operator identification. Family6.2 separates envelope existence from map compatibility; family6.3 says construct when possible. The entire unchanged original task/family is in the appendix. The execution assignment is separate and supplies no theorem grants beyond G331/G345.
\tableofcontents\newpage
'''
paper=head+proof+'\n\\appendix\n\\section{Fresh source, scope, coverage and decision qualifications}\n'
for name in ['whole-source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md','original-task.json']:
 paper+='\\subsection*{'+name.replace('_',r'\_')+'}\n\\begin{GrantData}\n'+(out/name).read_text()+'\n\\end{GrantData}\n'
paper+='\\section{Entire qualified grants, unchanged literal components}\nAcceptance metadata below is preserved history, not an additional mathematical premise. Nested duplicates are retained unchanged.\n'
for row in manifest[:14]:
 name=pathlib.Path(row['path']).name;paper+='\\subsection*{'+name.replace('_',r'\_')+'}\n\\begin{GrantData}\n'+(attach/name).read_text()+'\n\\end{GrantData}\n'
paper+='\\end{document}\n';(out/'P12.6-paper.tex').write_text(paper)
print(json.dumps({'proof_bytes':len(proof.encode()),'paper_bytes':len(paper.encode()),'notes':len(notes),'candidate':False,'compiler_run':False},indent=2))
