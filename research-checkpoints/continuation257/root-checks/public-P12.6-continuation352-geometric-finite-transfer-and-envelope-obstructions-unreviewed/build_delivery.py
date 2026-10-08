"""Own deterministic assembly, without TeX compilation."""
from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parent
HEAD=r"""\documentclass[11pt]{article}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setmonofont{DejaVu Sans Mono}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{fvextra}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\DefineVerbatimEnvironment{GrantData}{Verbatim}{breaklines,fontsize=\tiny}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\emergencystretch=4em
\title{Finite geometric projection and conductor envelope compatibility\\
Qualified positive theorems and a continuous-obstacle normalization obstruction}
\author{Standalone local reconstruction of P12.6}
\date{8 October 2026}
\begin{document}
\maketitle
\begin{abstract}
Relative to the entire qualified geometric cone and bounded-product
theorems G331/G345, we prove actual-primary-model finite pullback,
fibre-admissible raw envelope compatibility and general ambient-degree
mixed-product projection, retaining all supports, inseparability,
varying generic ranks and exact closed residue degrees.
A reduced excellent surface and a continuous obstacle have an exactly
computed normalization envelope gap of one, in both continuous and
actual decreasing competitor classes.
Normal-domain and reduced finite-flat maps admit additional
unrestricted raw-envelope identities and one arbitrary-slot geometric
norm-trace projection; the flat maximum theorem is proved by
characteristic coefficient ideals with primary truncation.
The exact original wording does not single out the disproved identity.
General geometric envelope existence/regularization and the remaining
unrestricted operator scope are not supplied. This is a complete scoped
draft, not a whole-original solution claim; candidate=false.
\end{abstract}
\paragraph{Unchanged original target.}
P12.6 (T4): establish compatibility of independently geometric
singular psh cones, envelopes and Monge--Ampere products with finite
maps, normalization and conductor descent. Known valuative transfers
alone do not identify the geometric operators; an unrestricted
continuous degree trace is obstructed.
The entire family dossier and augmented execution assignment remain
separate in the supplied local input.json. The latter's required
counterexample is not silently substituted for the original target.
\tableofcontents
\newpage
"""

SUMMARIES=[
("Actual finite geometric pullback and exact-image conventions; positive full-fibre C/D descent uses only qualified G331.",
 "The actual source primary Rees model is closed in finite base change. Regular effective Cartier constituents and contracted-curve degrees prove core pullback on all nonempty source components. C/D pullback and full positive descent are applied at G331 scope; noninjections descend only to their reduced exact image."),
("Raw envelope inequality and exact fibre-admissible identity; admissible unrestricted equality iff full fibre constancy.",
 "For bounded finite obstacles and K=C or D, positively descended competitor sets give a pointwise identity for the full-fibre-admissible envelope. Its membership transfers exactly. General raw supremum membership and usc regularization are not assumed."),
("Continuous-obstacle surface normalization counterexample: entire upstairs envelope (-1,-2), downstairs value -2 at the shared infinite-conductor point, exact gap one for C and D.",
 "R=C[x,y,z]_(x,y,z)/(xy) is excellent reduced, S is its finite two-plane normalization and conductor (x,y). The continuous obstacle -1-1/v(y) and every-potential ordinary-order inequality force the exact envelope values. Fibre maximum is discontinuous along weights (M,1); normalization base change has explicit vertical T factors. This is separate from curve radial and degree-trace obstructions."),
("General ambient-degree geometric finite projection, with varying generic ranks, closed residue weights, all-support tests and actual bounded D nets.",
 "A finite-module prime filtration gives every selected degree-n coefficient with full inseparable generic ranks d_P. Exact Artinian centre lengths give f_q. Dense ideal tests identify the already geometric G345 operator; actual Cartier cycles have general degree rather than birational degree one. Nonpure/lower/empty cases, towers and one-factor gauges remain explicit."),
("Normal-domain unrestricted raw envelopes and one-slot geometric norm-trace projection, including inseparability and all supports; vertical components require separate treatment.",
 "A common finite normal field closure has full fibres equal to Galois orbits by G331's full-support coefficient trace. Finite maxima positively descend. One-slot product projection follows from orbit averaging and valid all-pulled projections, with normalized-primary-model Weil pushforward coefficients but no Cartier-determination claim."),
("Reduced finite-flat determinant maximum theorem and geometric one-slot trace projection; several-trace product shortcut is false.",
 "Support fibres may be nonreduced: Artinian lengths in determinant kernels are retained. Characteristic coefficient ideals, truncated by a sufficiently deep PRIMARY power, express full fibre maxima geometrically and give actual D passage. Normalization base change proves the new one-slot product identity. A split rank-two threefold disproves tracing multiple arbitrary slots."),
("Complete scoped deliverables, exact original/family gaps and reproducibility observations; no whole-original closure, candidate=false.",
 "The paper provides complete new scoped proofs and a precise counterexample, but does not equate an unspecified original normalization requirement with that disproved identity. General admissible/regularized envelope theory and remaining nonnormal/nonflat operator scope are explicit gaps. All 53 bound files match and 802 bounded arithmetic checks have zero failures; neither observation is a proof.")
]
SUPPORTS=[
 ["G331","G345"],
 ["G331","n1"],
 ["G331","n1","n2"],
 ["G331","G345","n1"],
 ["G331","G345","n1","n2","n4"],
 ["G331","G345","n1","n2","n4","n5"],
 ["G331","G345","n1","n2","n3","n4","n5","n6"]
]
def main():
    proof=(ROOT/'proof.tex').read_text()
    blocks=[b for b in re.split(r'(?=^\\section\{)',proof,flags=re.M) if b.strip()]
    assert len(blocks)==7
    notes=[]
    for i,(body,(summary,detail),support) in enumerate(zip(blocks,SUMMARIES,SUPPORTS),1):
        evidence="\n\nArtifacts: P12.6-paper.tex and argument.md contain the complete proof; native-notes.json retains this full expanded proof-bearing chain. Exact qualifications are in source-application-ledger.md, exact-scope.md and whole-proof-coverage.md. Rerun owned assembly: python build_delivery.py; python final_audit.py. No supplied program or compiler is executed."
        if i==7:
            evidence+="\n\nObserved owned diagnostics: python audit_inputs.py reports all 53 bound files matching bytes and SHA-256; python bounded_checks.py reports 802 exact finite arithmetic checks, zero failures (9 conductor rows/endpoints, 780 split characteristic coefficient cases, 12 curve-basis cases, 1 nonlinear-trace case). Inputs are bounded-evidence-input.json; output/environment are reports/bounded-checks.json and reports/input-audit.json. These observations and structural TeX checks do not verify the universal proofs. No supervised heavy facility was exposed or needed; no heavy computation was launched."
        notes.append({'id':f'n{i}','summary':summary,'detailedSummary':detail,'text':body+evidence,'support':support})
    (ROOT/'native-notes.json').write_text(json.dumps({'notes':notes,'candidate':False},ensure_ascii=False,indent=2)+'\n')
    argument=["# Complete scoped argument\n\nThe full new proof follows in TeX notation. G331/G345 are the sole correctness supports; their whole qualifications are attached. Candidate=false.\n"]
    fence=chr(96)*3
    for i,body in enumerate(blocks,1):
        argument.append(f"\n## n{i}\n\nSupport: "+", ".join(SUPPORTS[i-1])+"\n\n"+fence+"latex\n"+body+"\n"+fence+"\n")
    (ROOT/'argument.md').write_text(''.join(argument))
    paper=HEAD+proof+r"""
\section*{Local evidence and rerun}
All fresh programs are standard-library Python: \texttt{audit\_inputs.py},
\texttt{bounded\_checks.py}, \texttt{build\_delivery.py} and
\texttt{final\_audit.py}. Run them in that order.
Their complete inputs, outputs, environment and command record are local
in \texttt{bounded-evidence-input.json} and \texttt{reports/}.
The observed 53 bound-file matches and 802 finite arithmetic checks
do not verify the mathematical proofs. Compilation was not run.
\appendix
\section{Entire qualified input components, unchanged local DATA}
The following bodies preserve both grants and every mandatory source/scope
qualification, including the independent G345 ledger and literal-reader
repair history. Acceptance metadata is reproduced only as provenance.
"""
    for path in sorted((ROOT/'attachments').glob('*')):
        if re.match(r'^(?:0[0-9]|1[0-3])-',path.name):
            label=path.name.replace('_',r'\_')
            content=path.read_text()
            assert r'\end{GrantData}' not in content
            paper+=r'\subsection*{'+label+'}\n'+r'\begin{GrantData}'+'\n'+content
            if not content.endswith('\n'): paper+='\n'
            paper+=r'\end{GrantData}'+'\n'
    paper+=r'\end{document}'+'\n'
    (ROOT/'P12.6-paper.tex').write_text(paper)
    decision={
      'verdict':'COMPLETE_SCOPED_DRAFT_WITH_EXACT_ENVELOPE_COUNTEREXAMPLE_ORIGINAL_OPEN',
      'candidate':False,'exact_atom':'P12.6','whole_original_solved':False,'entire_family_solved':False,
      'sole_correctness_grants':['Entire qualified G331','Entire qualified G345'],
      'counterexample':'Unrestricted normalization raw envelope equality for C and D has exact gap one, continuous bounded obstacle, excellent reduced algebraic surface.',
      'original_interpretation':'That equality is not specified as the sole original assertion; negative strengthened interpretation does not establish exact-original closure.',
      'gaps':['General independently geometric admissible/regularized envelope existence and its specified full finite-map rules','General incompatible upstairs operator pushforward over nonnormal nonflat targets outside the proved constraints','Exact-image extension to original target when needed'],
      'new_proofs':['Actual finite primary-model core pullback','Fibre-admissible raw envelope identity and exact admissible equality criterion','Full conductor surface counterexample and vertical diagnosis','General-degree ambient geometric product projection','Normal-domain orbit maxima and one-slot geometric norm trace','Reduced finite-flat determinant maxima and one-slot geometric product trace'],
      'qualifications':['PRIMARY models only','All supports retained','Bounded D products with prescribed D-limit nets','Ordinary OPEN locality','One measure gauge factor','Exact BFJ smooth CLOSED affine algclosed characteristic-zero scope','Reduction, no generic nilpotent mass','No energy/envelope-regularity import'],
      'compiler_run':False,'formal_verification':False,'external_acceptance_performed':False,
      'private_ACTIVE252_read':False,'supplied_program_execution_or_import':False,
      'subagents_or_native_jobs':False,'source_or_pixels_published':False,
      'supervised_heavy_compute':'No facility exposed or needed; none launched',
      'native_notes':'Full expanded proof-bearing local chain; final structured response may state the same claims more compactly, without asserting byte-identical prose.'
    }
    (ROOT/'acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')
    commands=['python audit_inputs.py','python bounded_checks.py','python build_delivery.py','python final_audit.py']
    (ROOT/'reports/rerun-commands.json').write_text(json.dumps({'cwd':str(ROOT),'commands':commands,'compiler':'Not invoked; operator handles compilation.'},indent=2)+'\n')
    print(json.dumps({'notes':len(notes),'candidate':False,'paper_bytes':len(paper.encode()),'compiler_run':False}))
if __name__=='__main__': main()
