"""Owned deterministic delivery builder; no supplied imports or compilation."""
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent
META = [
    ('n1','All-field primary mixed-multiplicity kernel on the reduced excellent germ; unused labels, same superficial quotients and closure invariance proved.',
     'Reconstructs symmetry, every product/power law including unused/repeated/unit labels, integral-closure invariance by finite graded exponents, and monotonicity by simultaneous superficial reductions in one common quotient. R(z) preserves lengths and dimensions. Colon and top-form additivity arguments retain embedded/nonpure behavior. Uses G331 only for the full-support boundary and primary valuative criterion; ordinary primary Hilbert/superficial dependencies are disclosed.',
     ['G331']),
    ('n2','Positive bounded moment measures on the whole G331 D domain, independent of every representation; actual prescribed-limit decreasing NET and uniform weak continuity.',
     'Proves test/function relation independence on all supports, real positive Riesz extension, exact mass and binomial perturbation bound. Uniform C extension and arbitrary actual decreasing C representations yield bounded D products. Compact directed covers prove every representation independent and give the C-majorant supremum. Actual decreasing bounded D nets converge when the specified limit is in D. No increasing closure, net flattening or order of measures is assumed.',
     ['G331','n1']),
    ('n3','Independent supported Cartier intersections on primary models: mixed-characteristic thickenings, actual Koszul symmetry, cycle projection and raw Rees equality.',
     'Defines local intersection by R-length Euler polynomials on proper effective exceptional Cartier thickenings. The m-filtration supplies all generic thickness weights without coefficient fields. Actual supported Koszul complexes establish full symmetry. Proper integral top-component divisor-cycle projection proves refinements and normalization invariance before any global Chow quotient. Rees eventual sections and vanishing prove the diagonal and polynomial polarization proves every raw mixed-ideal equality.',
     ['G331','n1']),
    ('n4','Independent positive geometric atom measures and refinement invariance, then full real-core/ideal moment comparison by an ACTUAL fixed-model image identity.',
     'Constructs positive atom weights from real curve-nef geometry before ideal moments. Independently proves atomic refinement invariance via DVR centers, divisor-cycle projection and zero lower-image intersections. On the fixed refinement Bl_(I c0), generated section ideals satisfy Jq O=O(qL+D0) as actual invertible images, giving the map to Bl_Jq. A common-model polynomial limit, with fixed primary uniform error, identifies all real Cartier-core moments and presentations with the bounded operator.',
     ['G331','n1','n2','n3']),
    ('n5','Full bounded ordinary open-set locality on all supports, from actual ratio subideals and two compact-cover limits.',
     'Simultaneous invertibility of A,B,A+B gives ratio subideals L,M with sum O. Strict inequality at an exceptional prime makes M vanish on the entire integral prime, so L restricts trivially and mixed atom weights agree. Extends to C and other bounded D slots using fixed supported continuous tests. Two successive compact-cover decreasing limits and known-domain uniform continuity prove locality for arbitrary bounded D tuples agreeing on any open set. No plurifine claim or unproved closure is used.',
     ['G331','n2','n4']),
    ('n6','Exact one-factor gauge covariance, full weighted normalization/conductor rules, actual zero-arity curve degree and all reduction/degeneracy conventions.',
     'Proves measure gauge factor v_a(b), reference mass, top-dimensional normalization pushforward with closed residue degrees including inseparability, and full G331 conductor quotient behavior while retaining every support and lower-dimensional point with zero top-degree contribution. Curves have an independently Cartier reference measure; the finite residue extension example R=k+t l[[t]] has mass [l:k]. Empty dimension zero, units, zeros, bottom and extra nilpotent data are explicitly handled.',
     ['G331','n1','n2','n3','n4']),
    ('n7','Exact BFJ smooth OPERATOR specialization only in its published closed affine algebraically closed characteristic-zero range, including net topology.',
     'Reads the complete Section 4. Generic joint-reduction parameter colength equals polynomial mixed multiplicity in the regular/CM ring. Ideal moments, uniform shifts and coefficient-topology upper semicontinuity plus monotonicity identify the whole bounded operator through arbitrary decreasing nets. Multiplier-dependent addition and resolution remain confined to the published smooth scope; 4.8 sequences alone are not treated as a net theorem.',
     ['G331','n1','n2','n6']),
    ('n8','Reproducibility and diagnostic limits: all 54 bound files match, five source pages inspected, 6765 exact Newton checks pass; no computation certifies the proof.',
     'Records independently owned byte audit, exact formula pixels, bounded finite Newton arithmetic and residue examples. Separates observations from universal arguments and preserves rejected shortcuts and the corrected TeX escaping failure. No supplied program, agent/native job, unbound campaign, compilation, account/editor or catalogue mutation occurred. No supervised heavy-compute facility was exposed or needed.',
     ['G331','n1','n2','n3','n4','n5','n6','n7']),
    ('n9','Complete ORIGINAL P12.4 solution candidate relative to entire qualified G331, with all proofs, exact scope and unchanged grant attachments; independent ROOT review remains.',
     'Claims the full bounded geometric primary-model operator, independent core intersections and presentations, exact ideal comparison, all bounded open locality and actual decreasing-NET continuity, gauge and full normalization/conductor rules, low-dimensional conventions, and exact published smooth specialization. Entire standalone proof and unchanged qualified grant are delivered. Energy, general finite-map calculus, arbitrary-model cofinality and literal radial extension identification remain separate. This is an unverified complete-solution claim, not acceptance or publication.',
     ['G331','n1','n2','n3','n4','n5','n6','n7','n8'])
]

THEOREM = r"""
\section*{Original target and reconstruction assignment}
The unchanged atomic target is P12.4 (T5): construct bounded mixed
Monge--Ampere products on singular and nonnormal normalized local boundaries,
with model independence, the correct intersection comparison, locality and
continuity. Compactness of the boundary alone supplies no such product.
The entire original family dossier and the augmented reconstruction assignment
are retained separately and literally in the accompanying task files.
The augmented request specifies proof audits; it changes no atomic target.
The sole incoming theorem is the entire qualified G331.

\section*{Theorem}
Let \(A\) be excellent local, \(R=A_{\rm red}\), and \(n=\dim R\).
Choose a proper primary \(\mathfrak a\) when \(n\ge1\). On the FULL
normalized centered semivaluation boundary, with every support retained,
there is a unique mixed positive Radon operator of arity \(p=n-1\)
on the bounded G331 geometric class \(D\), extending the independently
defined Cartier core and satisfying uniform weak and actual bounded
decreasing-net continuity. Decreasing-net limits are prescribed members of
\(D\). The operator is symmetric, additive and nonnegatively real homogeneous
in every nonpositive input. For actual negative-effective real curve-nef
primary-model Cartier cores its measure is
\[
\sum_Z \operatorname{ord}_Z(\mathfrak a)
 (D_1|Z\cdots D_p|Z\cdot Z)\,
 \delta_{\operatorname{ord}_Z/\operatorname{ord}_Z(\mathfrak a)}.
\]
Its pairing with every exceptional real Cartier test \(F\) on any common
primary refinement is the independently supported local degree
\(Q(D_1,\ldots,D_p,F)\). It depends only on the input functions.
For rational primary profiles the exact moments are
\[
\int v(J)\,d\mu(-v(I_1)/q_1,\ldots,-v(I_p)/q_p)
=\frac{e_R(I_1,\ldots,I_p,J)}{\prod q_i}.
\]
The reference tuple \((-1)^{[p]}\) has mass \(e_R(\mathfrak a)\).
The operator is local on every open set where corresponding bounded tuples
agree. Primary change \(T(v)=v/v(\mathfrak b)\), with transported inputs
\(u_{\mathfrak b}(Tv)=u_{\mathfrak a}(v)/v(\mathfrak b)\), obeys
\(\mu_{\mathfrak b}=T_*[v(\mathfrak b)\mu_{\mathfrak a}]\).
Finite normalization obeys closed residue-field weighted pushforward from
top-dimensional normal centers, with every conductor fiber retained and
lower-dimensional top-degree contribution zero. The curve operator has
zero inputs and is its actual Cartier reference measure; dimension zero
has empty boundary and zero measure, without negative arity.
The operator specializes exactly to published BFJ Section 4 at its smooth
affine CLOSED algebraically closed characteristic-zero hypotheses.

The theorem uses reduced top degree and G331's directed PRIMARY model system.
It supplies neither nilpotent generic lengths nor arbitrary-model cofinality,
general envelopes, energy, arbitrary finite-map calculus, or a literal
classical/CLD radial-extension identification. The mixed-zero obstruction
remains. This is an unverified complete original-solution candidate.
"""

def main():
    raw = json.loads((OUT/'input.json').read_text())
    problem = raw['task']['problem']
    marker = 'ROOT AUTHORIZED WHOLE ORIGINAL RECONSTRUCTION'
    original, augmented = problem.split(marker, 1)
    (OUT/'original-task-statement.txt').write_text(original)
    (OUT/'augmented-assignment.txt').write_text(marker+augmented)
    (OUT/'original-task.json').write_text(json.dumps(raw['task'],indent=2,ensure_ascii=False)+'\n')
    notes = []
    for id_, summary, detail, support in META:
        notes.append({'id':id_, 'summary':summary, 'detailedSummary':detail,
                      'text':(OUT/(id_+'.tex')).read_text(), 'support':support})
    result = {'notes': notes, 'candidate': True}
    (OUT/'native-notes.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    preamble = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{fvextra}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\emergencystretch=4em
\title{Bounded geometric local products on excellent reduced germs\\Supported Cartier intersections and ordinary open locality}
\author{Independent whole-original P12.4 reconstruction}
\date{8 October 2026}
\begin{document}
\maketitle
"""
    paper = preamble + THEOREM
    for note in notes:
        paper += '\n\\section{'+note['id']+'. '+note['summary'].replace('_',r'\_').replace('&',r'\&')+'}\n'
        paper += '\\textit{Supports: '+', '.join(note['support'])+'.}\n\n'+note['text']
    paper += r"""
\appendix
\section{Entire qualified G331 source, unchanged literal DATA}
The following complete bound source is supplied unchanged as an attachment.
Its no-operator qualification is preserved; the NEW proofs above supply the
intersection and locality theorems rather than importing them.
\VerbatimInput[breaklines,fontsize=\tiny]{attachments/00-P12.2-paper.tex}
\section{Mandatory source and scope annotation, unchanged}
\VerbatimInput[breaklines,fontsize=\tiny]{attachments/01-mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json}
\section{G331 source ledger, unchanged}
\VerbatimInput[breaklines,fontsize=\tiny]{attachments/02-source-application-ledger.md}
\section{G331 exact scope, unchanged}
\VerbatimInput[breaklines,fontsize=\tiny]{attachments/03-exact-scope.md}
\end{document}
"""
    (OUT/'P12.4-paper.tex').write_text(paper)
    print(json.dumps({'notes':len(notes),'candidate':True,'paper_bytes':len(paper.encode()),'compilation_run':False}))

if __name__ == '__main__':
    main()
