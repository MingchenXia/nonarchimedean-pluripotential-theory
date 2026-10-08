"""Owned artifact builder. Writes sources only; invokes no compiler or supplied code."""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent

INDEX = [
 ('n1', 'Reconstructed all-support raw envelope and actual graded primary-ideal calculus; general normal positivity remains a continuity gap.',
  'Proves raw C=D suprema for finite continuous obstacles, positivity of usc regularization iff raw continuity, norm Lipschitz, actual integrally closed J_k ideals and increasing factorial formula, and exact homogeneous gauge covariance. These are reconstructed prior facts, not a new general normal envelope theorem.', ['G331']),
 ('n2', 'New actual decreasing-D-net closure on every excellent reduced germ, with decreasing energy criterion membership proved first.',
  'Normal zero dichotomy and a strict-majorant insertion construct an actual decreasing C-net for the pointwise infimum of a decreasing D-net. Finite normal centres and full positive conductor descent give all excellent reduced germs. E350 then yields the energy criterion without separately assuming D membership; no arbitrary nondirected infimum or increasing closure is proved.', ['G331','E350','n1']),
 ('n3', 'Exact BFJ smooth continuous-envelope reconstruction on closed affine algebraically closed characteristic-zero germs only.',
  'Uses complete immediate published determining-complex envelope proof, substantive closed-face continuity, all retraction infima and the sign-correct uniform ideal estimate. Rational ideal-difference density extends from determining obstacles to every continuous obstacle. No singular or arbitrary-characteristic multiplier/resolution application is made.', ['G331','n1']),
 ('n4', 'New greatest positive continuous/usc envelopes on normal targets admitting finite dominating domain covers with proved source envelope property.',
  'A positive full-fibre normalized coefficient trace first constructs a continuous target minorant dominating all target D minorants. Positive finite weights force the source envelope to be fibre constant. An actual decreasing continuous-majorant net handles bounded-above extended usc obstacles and partial bottom. Applies concretely to characteristic-zero normal quadratic cones and smooth factors, not all excellent normal germs.', ['G331','E350','n1','n2','n3']),
 ('n5', 'New all-characteristic normal singular convergence diagnostic: bounded energy-maximizing primary profiles have a non-D pointwise limit despite capacity convergence.',
  'On XY=Z^2, I_n=(X^n,XY^(n-1),Y^(2n)) gives u_n increasing from [-2,-1] to -2 at the infinite-X support and -1 elsewhere, hence non-usc. Proves normality, conic reference mass two, capacity error <=2/(1+n epsilon), universal e(I_n)=2n^2+2n and E(u_n)=-1-1/n. Obstacle -1 has positive envelope -1, so this is not a normal-envelope counterexample. Finite diagnostics cover 64 lengths,48 differences,272 profile cases only.', ['G331','B341','E350','n1']),
 ('n6', 'Reconstructed sharp full-fibre conductor criterion, all-characteristic nonnormal failure and geometric curve clipping.',
  'An actual primary conductor mask proves equality on the dense finite-conductor stratum; regularized target positivity is equivalent to continuous fibre-constant source raw envelope. Reconstructs a strictly negative double-plane obstacle with no maximal D minorant. Every excellent reduced-curve geometric envelope is min(phi,0), via actual Cartier/DVR positivity and full descent. No normal residual closure or unrestricted normalization commutation is inferred.', ['G331','E350','n1','n4']),
 ('n7', 'Complete delimited deliverables and honest original judgment: general arbitrary normal higher-dimensional P12.3 remains unresolved; candidate=false.',
  'Records the new decreasing closure, finite-cover singular envelope sector and normal convergence limitation, exact 17,550-byte original and mandatory historical corrigendum, all qualified grant limits, 68/68 retained input matches and bounded finite observations. Missing general normal continuity/uniform all-support estimates and upper-envelope compactness remain explicit. Uncompiled paper and complete proof/source/scope/coverage/decision/native notes are delivered; no publication or catalogue closure claimed.', ['n1','n2','n3','n4','n5','n6'])
]

notes = []
for ident, summary, detailed, support in INDEX:
    body = (HERE/(ident+'.md')).read_text()
    notes.append({'id':ident,'summary':summary,'detailedSummary':detailed,
                  'text':body,'support':support})
native = {'notes':notes,'candidate':False}
(HERE/'native-notes.json').write_text(json.dumps(native,ensure_ascii=False,indent=2)+'\n')
(HERE/'argument.md').write_text('# Geometric envelopes: delimited normal progress and unresolved original\n\n'
    'Candidate=false. Complete proof-bearing local chain, relative only to the entire qualified grants.\n\n'
    +'\n\n'.join(n['text'] for n in notes))

# Preserve exact original bytes; never serialize the augmented object as original.
original = (HERE/'inputs/mathematical/21-21-exact-original-task-after-review245.json').read_bytes()
(HERE/'original-task.json').write_bytes(original)
parsed_original = json.loads(original)
parsed_input = json.loads((HERE/'inputs/current-input.json').read_bytes())
(HERE/'inputs/exact-original-problem.txt').write_text(parsed_original['problem'])
(HERE/'inputs/current-augmented-task.json').write_text(json.dumps(parsed_input['task'],ensure_ascii=False,indent=2)+'\n')
(HERE/'inputs/current-augmented-problem.txt').write_text(parsed_input['task']['problem'])
(HERE/'inputs/bounded-diagnostic-input.json').write_text(json.dumps({
    'length_n':list(range(1,9)),'length_k':list(range(1,9)),
    'profile_n':list(range(1,17)),
    'profile_pairs':[['1',str(j)+'/2'] for j in range(2,10)]+
                    [[str(j)+'/2','1'] for j in range(3,10)]+
                    [['infinity','1'],['1','infinity']],
    'status':'Owned bounded input domain, also explicitly encoded in finite_diagnostics.py'},indent=2)+'\n')

decision = {'task':'Entire unchanged original P12.3', 'candidate':False,
    'original_completed':False, 'verdict':'PARTIAL MATHEMATICAL PROGRESS; ORIGINAL NORMAL GAP REMAINS',
    'status':'Unverified draft; no publication/catalogue acceptance',
    'only_correctness_grants':['Entire qualified G331','Entire qualified B341','Entire qualified E350'],
    'new_results':['Actual decreasing D-net closure on all excellent reduced germs',
                   'Normal finite-domain-cover continuous and extended usc envelopes',
                   'Normal singular energy/capacity convergence-to-membership limitation'],
    'normal_residual_gap':'All excellent normal local domains/semilocal centres of dimension>=2, arbitrary characteristic/residue field/all supports: no general proof of raw continuous-obstacle envelope continuity or different genuine greatest-envelope construction, and no normal residual impossibility theorem.',
    'algebraic_gap':'No uniform all-support J_k graded-ideal estimate or general envelope-continuity theorem beyond the proved finite-cover sector.',
    'variational_gap':'Decreasing closure is proved; increasing compactness, actual all-support obstacle attainment and positive upper-envelope regularization remain unproved.',
    'original_bytes':len(original),'original_sha256':hashlib.sha256(original).hexdigest(),
    'original_problem_unchanged':True,'augmented_assignment_separate':True,
    'historical_336_corrigendum_attached':True,
    'smooth_scope':'Smooth affine CLOSED algclosed char0 n>=2, direct DVR and empty cases',
    'normal_singular_positive_sector':'Finite dominating domain cover with every marked source centre having proved CE; characteristic-zero quadratic cones included',
    'characteristic_independent_results':'Decreasing closure, trace-transfer proof conditional on source CE, raw/conductor calculus, normal diagnostic, nonnormal obstruction, curve clipping',
    'compiler_performed':False,'supplied_code_executed_or_imported':False,
    'extra_agents_native_jobs':False,'heavy_compute':False,
    'protected_P16_editor':'UNACCESSED_UNCHANGED','sources_pixels':'LOCALONLY',
    'execution_not_mathematical_verification':True}
(HERE/'acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')

def escape(text):
    mapping={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','&':r'\&',
             '%':r'\%','$':r'\$','#':r'\#','_':r'\_',
             '^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
    return ''.join(mapping.get(ch,ch) for ch in text)

def to_tex(body):
    # Preserve all literal displayed mathematics. Escape prose separately.
    parts=re.split(r'(\\\[[\s\S]*?\\\])',body)
    output=[]
    for p in parts:
        if p.startswith('\\['):
            output.append(p)
            continue
        lines=[]
        for line in p.splitlines():
            if line.startswith('# '):
                lines.append('\\section{'+escape(line[2:])+'}')
            else:
                lines.append(escape(line))
        output.append('\n'.join(lines))
    return '\n'.join(output)

preamble = r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\emergencystretch=5em
\title{Geometric envelopes on finite-covered normal germs\\
Decreasing completion and the residual normal-envelope gap}
\author{Local mathematical implementation draft for P12.3}
\date{8 October 2026}
\begin{document}
\maketitle
\begin{abstract}
Relative to the fully qualified geometric cone, product and energy theorems,
we construct greatest continuous envelopes on normal excellent targets
admitting finite dominating domain covers with the continuous-envelope
property. Smooth covers in the exact published characteristic-zero range
give explicit normal singular examples. We prove actual closure under
decreasing geometric nets on every excellent reduced germ, and construct
extended upper-semicontinuous envelopes in the positive sector. An explicit
normal singular example in every characteristic shows that bounded energy
maximization and capacity convergence do not establish membership of an
exact increasing pointwise limit. Full gauge and conductor constraints,
the nonnormal obstruction and geometric curve clipping are retained.
The entire arbitrary normal higher-dimensional original remains unresolved;
the candidate flag is false. This standalone source is intentionally uncompiled.
\end{abstract}
\tableofcontents
\newpage
'''
source = preamble+'\n\n'.join(to_tex(n['text']) for n in notes)
source += '\n\\section*{Published application and qualified premise boundary}\n'
source += escape('The sole new envelope publication application is Boucksom--Favre--Jonsson, Valuations and plurisubharmonic singularities, Publ. RIMS 44 (2008), at the smooth affine closed algebraically closed characteristic-zero hypotheses. All exact used facts and proof transitions are stated in n3. The geometric cone, full coefficient trace, bounded kernel and energy/capacity premises are the entire qualified incoming theorems, with hypotheses stated in n1--n6. No prior acceptance record is a mathematical premise. Complete unchanged grant texts and their mandatory ledgers/annotations/scopes accompany this source locally. Recursive published dependencies are disclosed in source-application-ledger.md and not claimed freshly reconstructed.')
source += '\n\\end{document}\n'
(HERE/'P12.3-paper.tex').write_text(source)
(HERE/'evidence/commands.json').write_text(json.dumps({
    'owned_rerun_pipeline':['python retain_inputs.py','python finite_diagnostics.py',
                           'python build_delivery.py','python final_audit.py'],
    'read_only_commands':'rg --files / rg -n / sed -n / wc for explicit bound local text bodies; no supplied program invocation',
    'no_compiler':True,'no_network':True,'no_external_mutation':True},indent=2)+'\n')
print(json.dumps({'notes':len(notes),'candidate':False,'tex_bytes':len(source.encode()),
                  'original_bytes':len(original),'compiled':False}))
