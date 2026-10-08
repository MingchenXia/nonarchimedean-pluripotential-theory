import json,re,hashlib
from pathlib import Path
spec=[
('n1','Actual PRIMARY geometric pullback and compact quotient regularization; full-support continuous kernels force openness.','Uses entire qualified G331/G345 at their exact scopes. Proves actual source blowup closed in finite base change, all-support Cartier pullback, literal closed image, compact fibre-maximum USC identity without openness, and open pointwise identity. Normal-domain kernels give openness only when every source minimal component dominates.', ['G331','G345']),
('n2','Reduced finite-flat determinant Artinian kernels, genuine PRIMARY coefficient maxima, and actual C/D transfer.','Basis/family/base-change norm trace retains every special-fibre nilpotent and inseparable length. Dense all-function tests prove full support and continuity; finite sums preserve actual decreasing D. Direct characteristic coefficients plus primary truncation prove positive maxima. Normal/no-vertical maxima are reconstructed through normal splitting and full descent.', ['G331','n1']),
('n3','Specified whole-section USC E, selected positive domain, open-map equality and exact general constrained-conductor rule.','All bounded-above extended USC obstacles including partial bottom. E positive iff actual greatest D competitor; finite continuous raw C=D, positivity iff raw continuous, then C. Normal/no-vertical and reduced flat maps have exact regularized equality/positive-domain equivalence. Arbitrary injections use full fibre maximum and require constrained regularization both D and fibre constant.', ['G331','n1','n2']),
('n4','Entire all-field node: source actual C(-1,-2), downstairs E nonD, reversed ONE lift inequality.','All conductor fibres checked. Genuine primary h_N competitors give raw -1 first offnode and -2 entire second. Whole-section regularization raises shared point to -1 and violates second-plane regular order domination. Positive constrained upstairs(-1,-2) is not fibre constant; compact quotient identity holds exactly.', ['G331','n1','n3']),
('n5','Closed-image and normal-target vertical counterexamples have positive continuous envelopes at both ends.','Surface f=-1/v(x) has ambient E=-1, quotient node E=(-1,0), gap ONE and no D extension by normal zero dichotomy. Vertical injection R->R times R/(xy) has nonopen isolated source point and same positive gap. Intrinsic curve and ambient surface product arities remain distinct.', ['G331','G345','n1','n3','n4']),
('n6','Full bounded geometric finite projection with varying reduced top degrees and closed residue weights.','Actual primary-model Cartier cycle projection precedes module forms and Chow; proper FIELD numerical projection retains all Artinian thickness/inseparability. SH finite homogeneous generation, rational-ray squeeze, exact quotient sequence and prime filtration prove varying degree moments. Dense all-support tests and prescribed-limit net continuity give bounded D identity. Lower-dimensional points stay with zero ambient weight.', ['G331','G345','n1']),
('n7','Full conductor-admissible ONE arbitrary source-slot geometric product theorem; reduced flat admissibility automatic.','Normal splitting-field group trace and all-pulled projection prove one-slot identity with no extra degree. C=(B tensor S)_red injects over both rings; generic degree one over top B and full normalization pushforward prove the conductor theorem. ALL fibres including lower supports determine admissibility. Determinant base change gives every bounded source D admissible in reduced flat case. Noninjective trace remains intrinsic on literal image.', ['G331','G345','n1','n2','n6']),
('n8','Unnormalized tower and precise ONE-factor primary/separate-source gauge rules, with sharp normalized/multiple-slot failures.','Intermediate FULL admissibilities required in general; flat Artinian layer lengths compose on every support. Generic and closed degrees multiply. All-field varying ranks give -2/3 versus -1/2 and common trace -2; two arbitrary slots fail. E transports by homogeneous gauge, measures by one factor, separate trace slot is H_c/lambda.', ['G331','G345','n1','n2','n3','n5','n6','n7']),
('n9','Impartial whole-original P12.6 completion assessment, separate from P12.3 existence and P12.5 energy.','Claims complete corrected compatibility for the exact specified E and bounded geometric products, combining actual positive transfer, exact constrained general rule, arbitrary finite projection and full conductor one-slot theorem. Does not infer completion from one false universal assertion or silently demand all P12.3. Retains precise source/model/smooth/bounded/reference and nonclaimed operator limitations.', ['G331','G345']+[f'n{i}' for i in range(1,9)]),
('n10','Complete exact P12.6 draft claim with standalone deliverables and bounded evidence; independent acceptance pending.','Claims the whole corrected original finite-map/conductor scope relative only to full G331/G345. General envelope existence and energy remain separate. All89 inputs matched, full required bodies/actual-expanded fields read with repaired truncations. 15467 finite arithmetic observations had zero failures; no computation certifies mathematics. No supplied code/agents/heavy compute/network/publication/catalogue actions; compilation not run.', ['G331','G345']+[f'n{i}' for i in range(1,10)])]
notes=[]
for i,s,d,sup in spec:
 notes.append({'id':i,'summary':s,'detailedSummary':d,'text':Path(f'sections/{i}.tex').read_text(),'support':sup})
obj={'notes':notes,'candidate':True}
for name in ['native-notes.json','actual-FINAL.json']:Path(name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
argument='# Complete new P12.6 argument\n\nOnly entire qualified G331 and G345 are imported correctness grants. All other mathematical packets and verdicts are data. The full proofs follow.\n\n'
for n in notes:argument+='## '+n['id']+'\n\nSupports: '+', '.join(n['support'])+'\n\n'+n['text']+'\n'
Path('argument.md').write_text(argument)
n9=notes[8]['text'];n9=re.sub(r'^\\section\{[^\n]*\}\n','',n9);n9=re.sub(r'\\textit\{([^\n]*)\}\n',r'\1\n',n9)
Path('original-scope-and-noncircularity-decision.md').write_text('# Original scope and noncircularity decision\n\n'+n9)
head=r'''\documentclass[11pt]{article}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setmonofont{DejaVu Sans Mono}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[margin=1in]{geometry}
\usepackage{fvextra}
\usepackage[hidelinks]{hyperref}
\DefineVerbatimEnvironment{GrantLiteral}{Verbatim}{breaklines,fontsize=\tiny}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em}
\emergencystretch=4em
\title{Geometric finite-map compatibility on excellent local germs\\Whole-section USC envelopes, full conductor descent, and bounded products}
\author{New independent P12.6 reconstruction, relative to qualified G331 and G345}
\date{8 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We prove actual primary-model geometric pullback, full varying-degree bounded
product projection, a conductor-admissible one-source-slot trace theorem,
and exact compatibility of the specified whole-section USC-regularized
obstacle operator on its geometric positive domain. Normal-domain maps without
vertical components and reduced finite-flat maps are open on the full
semivaluation section and commute pointwise with the regularized operator
for extended USC obstacles. Arbitrary injections have an exact constrained
full-fibre quotient formula. Entire all-field node, closed-image, and
vertical-component calculations show why stronger unrestricted assertions
fail. This is a complete corrected original P12.6 draft claim, not independent
acceptance; general envelope existence and finite energy remain separate.
\end{abstract}
\section*{Exact original atom and theorem map}
P12.6 (T4): Establish compatibility of independently geometric singular psh
cones, envelopes and Monge--Ampere products with finite maps, normalization
and conductor descent. Known ideal/valuative transfer alone does not identify
these geometric operators, and unrestricted continuous degree trace is
obstructed. We use only the entire qualified G331/G345 comparisons and
geometric products. Sections 1--8 prove the new operators and their exact
limits; Section 9 assesses the original scope independently; Section 10
states the complete draft claim and evidence. The unchanged exact task and
family are retained in LOCALONLY/original-task.json. Nothing in their ROOT
or reviewer prose supplies an additional correctness premise.
\tableofcontents
'''
paper=head+''.join(n['text']+'\n' for n in notes)
# All fourteen full components, including duplicate grant bodies, are literal.
paper+='\n\\appendix\n\\section{Entire qualified grants and mandatory source/scope records}\nThese are unchanged local supplied theorem components, with metadata kept distinct from correctness. Published primary source bodies and pixels remain LOCALONLY.\n'
for p in sorted(Path('grants').iterdir()):
 paper+='\n\\subsection*{Qualified component '+p.name.split('-')[0]+'}\n\\begin{GrantLiteral}\n'+p.read_text()+'\n\\end{GrantLiteral}\n'
paper+='\n\\end{document}\n'
Path('P12.6-paper.tex').write_text(paper)
decision={'verdict':'COMPLETE_EXACT_P12_6_CORRECTED_COMPATIBILITY_DRAFT_CLAIM','candidate':True,'independently_accepted':False,'formal_verification':False,'mathematical_grants':['G331','G345'],'original_statement_unchanged':True,'scope_interpretation':'P12.6 compatibility for the specified geometric operator on its selected positive domain, with exact constrained/general failure rules; universal P12.3 existence is separate','remaining_P12_6_obligations_at_assessed_scope':[],'separate_unresolved':['P12.3 positive-envelope existence/regularity beyond the selected domain','P12.5 energy and unbounded products'],'not_claimed':['universal geometric positivity of E','universal normalization equality','arbitrary-model cofinality','generic nilpotent original rank','literalCLD/radial identification','multiple arbitrary traced slots','unrestricted continuous degree trace'],'finite_diagnostics_are_proofs':False,'compilation_run':False,'publication':False,'catalogue_mutation':False,'protected_P16_4':'OPEN UNCHANGED','subagents_or_native_jobs':False,'supplied_scripts_executed_or_imported':False,'supervised_heavy_compute':'No service exposed; no resource-heavy work needed or launched','independent_review_required':True,'prior_candidate_false_preserved_as_history':['native253','native255'],'whole_family_closed':False}
Path('acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')
print('built',len(notes),'complete notes;',len(paper.encode()),'paper bytes; compilation NOT RUN')
