#!/usr/bin/env python3
"""Export the source-dated standalone 42-item catalogue from a built book.

Requires the current book aux and bbl files. Existing proofs are omitted;
problem statements, known-result statements, source discussions and locators
are retained. This performs no literature search or mathematical verification.
"""
from pathlib import Path
import re, json, hashlib, subprocess, importlib.util
from collections import Counter

ROOT = Path(__file__).resolve().parents[3]
M = ROOT/'manuscript'
OUT = ROOT/'output/open_problems_catalogue_2026-10-02.tex'
spec=importlib.util.spec_from_file_location('inventory',M/'editorial/tools/check_open_problem_inventory.py')
inv=importlib.util.module_from_spec(spec);spec.loader.exec_module(inv);report=inv.audit()
tier_map=dict(inv.ACTIVE.findall(inv.INVENTORY.read_text()))
groups=[{'label':label,'atoms':[{'id':atom,'tier':tier_map[atom]} for atom in atoms]} for label,atoms in inv.EXPECTED_GROUPS]
assert tuple((g['label'],tuple(a['id'] for a in g['atoms'])) for g in groups)==inv.EXPECTED_GROUPS

# Compact independent targets. Detailed hypotheses and current results follow
# each family, taken from the active Chapter 72 closure without proof bodies.
TARGETS = {
'P02.1':('Decreasing semipositive real-PL regularization',r'Characterize the higher-dimensional good strict analytic spaces on which every classically psh function is, near every point, the pointwise decreasing limit of semipositive real PL functions. The starting function is arbitrary in the classical curve-test class; invariant continuous toric functions form only a known special case.'),
'P02.2':('Decreasing locally Fubini--Study regularization',r'For the same arbitrary classical psh starting class, characterize the spaces admitting local decreasing approximations by locally Fubini--Study functions. This asks for the Fubini--Study conclusion itself, rather than merely real-PL or smooth approximation.'),
'P02.3':('Decreasing weakly smooth psh regularization',r'Characterize the higher-dimensional good strict spaces on which every classically psh function has local decreasing weakly smooth psh approximants. Weak smoothness is defined through harmonic tropicalizations and must not be identified with ordinary CLD smoothness.'),
'P02.4':('Decreasing ordinary CLD-smooth psh regularization',r'Characterize the spaces on which every classical psh function has local decreasing approximations by ordinary CLD-smooth psh functions. The ordinary smooth requirement is part of the target; a weakly smooth sequence alone does not solve it.'),
'P03.1':('Classical positivity of regularized local envelopes',r'Find sharp normal or geometrically unibranch higher-dimensional hypotheses under which the upper-semicontinuous regularization of the local-Fubini--Study/semipositive-real-PL envelope is classically psh for every upper-semicontinuous obstacle. The perfected-unibranch reduced strict curve range is already proved. Necessity must account for the branched, nonsplit-node, and codimension-two pinching obstructions.'),
'P03.2':('CLD-v2 positivity of regularized local envelopes',r'For the same obstacle envelope, determine the additional hypotheses ensuring that its upper-semicontinuous regularization belongs to the second CLD psh stage for every upper-semicontinuous obstacle. Classical positivity alone is not the requested conclusion.'),
'P03.3':('Continuity of local obstacle envelopes',r'For every finite continuous obstacle, determine sharp additional hypotheses ensuring continuity of the regularized local-Fubini--Study/semipositive-real-PL envelope. A modulus-controlled subfamily or an invariant toric envelope does not establish continuity of the full competitor family.'),
'P04.1':('Common local products beyond algebraizable modifications',r'Extend the existing CLD/formal-BFJ common-model comparison to arbitrary nonalgebraizable analytic modifications. Specify the carrier, boundary datum, raw mass, and the precise class of compatible potentials.'),
'P04.2':('Bounded products for arbitrary classical psh functions',r'Construct a common local Monge--Ampère product for arbitrary bounded classically psh functions outside the jointly realizable model closure. Prove compatibility with each existing endpoint rather than declaring a product by classical positivity alone.'),
'P04.3':('Finite-energy and unbounded local products',r'Construct a finite-energy or unbounded extension of the common local product, with an explicit polar-mass rule. Distinguish a nonpluripolar extension from an extension retaining polar mass and state the hypotheses under which uniqueness is intended.'),
'P04.4':('Common local products on singular and nonnormal germs',r'Extend the local construction to singular and nonnormal germs, compatibly with normalization and conductor descent. The analytic local product and the normalized-link product have different dimensions and must be compared with their exact boundary normalizers.'),
'P05.1':('Polyhedral regularity, with coefficient conventions fixed',r'Characterize balanced rational polyhedral pairs \((\mathbf X,\gamma)\) for which the BMPS envelope regularity property holds. Treat the literal integral-slope/rational-constant class and its explicit real scalar extension separately. Literal regularity is classified in dimension one and fails on every noncompact finite rational polyhedral space; the compact higher-dimensional literal case, higher-dimensional real-PA case, and arbitrary nonseparable obstacles remain.'),
'P05.2':('Polyhedral envelope orthogonality',r'Characterize the pairs for which the regularized polyhedral envelope satisfies the exact contact identity \(\int(P_\gamma(u)-(\gamma+u))\,\MA_{\mathrm{poly}}(P_\gamma(u))=0\) for all admissible obstacles. Positive growth at infinity, balancing, or correct total mass alone does not establish orthogonality.'),
'P05.5':('Global polarized realization of polyhedral measures',r'Characterize polarized Monge--Ampère realizations of \((\mathbf X,\gamma)\). Construct global semipositive lifts of the relative potentials \(a_i-\gamma\) in a named BFJ domain, prove intersection-mass and component-calibration identities, and compare global non-Archimedean and polyhedral measures, including mixed products and boundary terms. Local recursive CLD/delta comparison is an established subcase, not the full target.'),
'P06.2':('Recognition of continuous zero-Hessian functions',r'Let \(K\) be complete and nontrivially valued and \(X\) good, separated, strict and boundaryless. Outside the verified scopes, decide whether every continuous \(h\) with \(\dprimeddprime[h]=0\) is classically pluriharmonic (or harmonic where that notion is available), or give a counterexample in this scope. Scalar ascent of the current equation and regularization of both signs are separate missing gates. The unrestricted arbitrary-radius product extension is false.'),
'P12.2':('An independently geometric singular valuative psh cone',r'On the intrinsic normalized boundary of an excellent singular or nonnormal germ, construct a valuative psh class with independent geometric meaning and the correct smooth-germ specialization. Identify its relation to the existing ideal-generated cone. Defining another order-theoretic completion does not by itself supply that identification.'),
'P12.3':('An independently geometric singular envelope theory',r'Construct obstacle envelopes for the independently geometric singular psh cone, establish their positivity and the appropriate regularity, and compare them with the complete ideal-psh envelope already known on reduced-curve links.'),
'P12.4':('Model-independent bounded singular-local products',r'Construct bounded mixed Monge--Ampère products on singular and nonnormal normalized local boundaries, with model independence, the correct intersection comparison, locality and continuity. The existing compact boundary construction alone supplies no such product.'),
'P12.5':('Finite energy on singular local boundaries',r'Construct an energy functional, finite-energy class, and its Monge--Ampère calculus for excellent singular and nonnormal germs. Specify reference data, changes of primary gauge, and the relation between bounded approximation and finite-energy limits.'),
'P12.6':('Geometric finite-map functoriality and conductor descent',r'Establish compatibility of independently geometric singular psh cones, envelopes and Monge--Ampère products with finite maps, normalization and conductor descent. Finite restriction, ideal-cone extrema, normal-domain norm traces, finite-flat determinant traces and their tower/gauge rules are known. They do not identify the geometric operators; an unrestricted continuous degree trace is obstructed.'),
'P13.1':('Comparison for nonproportional Reeb polarizations',r'For a normal polarized affine cone \((X,T;\xi)\) over an algebraically closed trivially valued characteristic-zero field, compare \(\PSH(\xi)\) and \(\PSH(\xi^{\prime})\) for nonproportional Reeb fields. Obtain the estimates strong enough for uniform differentiability of energy. Identities along one proportional Reeb ray do not answer this question.'),
'P13.2':('The image of the fixed-Reeb Monge--Ampère operator',r'Characterize precisely the image of \(\MA_\xi:\mathcal E^1(\xi)/\mathbf R\to\mathcal M^1(\xi)\) and the measures admitting a solution. Retain the invariant carrier \(X_0^T\) and the affine-cone probability normalization. The operator is already bi-Lipschitz onto its image, so uniqueness there is established; the residual is the image and existence characterization.'),
'P14.1':('Intrinsic raw-transform image beyond the known regimes',r'For a pseudoeffective class \(\alpha\) on a compact K\"ahler manifold, intrinsically characterize the image of the perturbation-independent raw ideal-valuative DXZ transform on the MP spectrum. The full K\"ahler image and the projective ample rational-line-bundle regime are established. The big non-nef image remains open; the full real N\'eron--Severi DXZ--BJ comparison does not assert the same literal ideal formula outside the rational-line-bundle case.'),
'P14.4':('A P-sensitive big non-nef positivity theory',r'Construct a positivity theory for big non-nef classes retaining \(P\)-singularity data, movable-positive-part data, or equally informative additional structure. A relatively nef total-space model cannot represent a non-nef generic class. The raw ideal-valuative transform is only \(\mathcal I\)-level data and cannot by itself distinguish \(P\)-types or recover raw mass.'),
'P14.5':('Monge--Ampère measures in the big non-nef realization',r'Construct the Monge--Ampère measure theory corresponding to a valid big non-nef, \(P\)-sensitive realization, with the correct mass and comparison with existing positive-volume DXZ and MP operators in their common scopes.'),
'P14.6':('Energy in the big non-nef realization',r'Construct the corresponding intrinsic energy theory and its continuity, differentiation and measure compatibility. State which additional singularity data and reference choices it needs; positive-volume \(\mathcal I\)-level energy alone does not supply a \(P\)-sensitive theory.'),
'P14.8':('Zero-mass and formal-data reconstruction',r'Go beyond the established realizable-\(\mathcal I\)-data dichotomy: formulate and solve arbitrary formal-data realization, a general all-semivaluation reconstruction formula, or the remaining zero-mass strict-interior reconstruction range with precise admissibility conditions. A canonical normalized \(\mathcal I\)-model can be recovered from realizable data, but raw representatives and raw mass cannot descend to the \(\mathcal I\)-quotient. The terminal DXZ left-limit result does not create a second zero-mass interval.'),
'P15.1':('Path-independent unnormalized zero-volume energy',r'For a pseudoeffective class \(\alpha\) with \(\operatorname{vol}(\alpha)=0\), choose the minimum necessary reference scale and construct a path-independent unnormalized energy theory. If K\"ahler perturbations and a leading volume coefficient are used, prove independence of the stated perturbation choices. Division by zero volume is not an admissible normalization.'),
'P15.2':('Path-independent zero-volume Monge--Ampère theory',r'Construct a path-independent zero-volume Monge--Ampère theory with its carrier, dimension, mass and reference choices explicitly stated. A family of perturbative probability measures is not automatically a canonical limiting operator, and raw mass cannot be recovered from \(\mathcal I\)-equivalence alone.'),
'P15.3':('P-sensitive lower-dimensional transcendental Okounkov bodies',r'Construct a transcendental Okounkov body retaining a prescribed \(P\)-singularity type and encoding lower-dimensional numerical data at zero volume. A class-level compact body of zero ambient volume is already known; it does not identify numerical dimension or retain the requested \(P\)-type.'),
'P16.1':('Finite-energy equations on singular or unibranch varieties',r'Extend the finite-energy non-Archimedean Monge--Ampère operator and its existence-and-uniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in compactness, envelopes, energy differentiation and comparison. State all retained polarization and field hypotheses.'),
'P16.2':('Proper nonprojective algebraizable equation theories',r'Construct an appropriate replacement positivity datum and the associated psh, finite-energy, comparison and equation theory on proper nonprojective algebraizable spaces. A proper algebraic scheme with an ample line bundle is already projective, so retaining that datum while dropping projectivity is not a new case.'),
'P16.3':('Finite-energy equations in positive residue characteristic',r'Construct the required finite-energy operator and prove existence and uniqueness when the original residue-characteristic restriction is removed. Replace the resolution, model-regularity and envelope inputs wherever they are used rather than merely changing the standing field hypothesis.'),
'P16.4':('Finite-energy equations over arbitrary complete valued fields',r'Extend the operator and existence theorem to nondiscrete valuations and arbitrary complete non-Archimedean fields outside the established invariant-toric, skeleton-supported endpoint. A definition of the finite-energy space alone does not establish the operator or the equation.'),
'P16.5':('Finite-energy equations for nonample positivity classes',r'Extend the equation theory to big or pseudoeffective nonample classes, specifying the psh cone, reference singularity type, energy and total mass. At zero volume, the existing probability normalization must be replaced rather than retained unchanged.'),
'P16.6':('Arbitrary-support finite-energy measures',r'Prove the operator and existence-and-uniqueness theorem for arbitrary finite-energy measure support beyond the known toric skeletal regime. Measures must satisfy the correct mass and energy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine Monge--Ampère measure by another inverse measure construction.'),
'P16.7':('Finite-energy equations on nonalgebraizable analytic spaces',r'Construct the finite-energy operator and its existence-and-uniqueness theory on genuinely nonalgebraizable analytic spaces, with an explicit positivity datum and the necessary compactness, envelope and comparison replacements.'),
'P19.1':('Entropy slopes of arbitrary finite-energy weak rays',r'Prove the remaining entropy-slope statement for arbitrary finite-energy weak rays on a compact K\"ahler manifold, outside the stated smooth polarized projective maximal-ray results. State the non-Archimedean datum, the entropy normalization and the precise ray hypotheses.'),
'P19.2':('Approximation preserving energy, entropy and singularities',r'Construct model approximations in the residual hybrid programme that preserve all required energy, entropy and singularity data. Convergence of energy alone is insufficient, and the published/source-stated projective Fujita regimes are established subcases.'),
'P19.3':('Hybrid compactness and measures for degenerating families',r'Prove the compactness and measure-continuity statements needed along genuinely degenerating families of compact K\"ahler manifolds. A fixed quasi-projective variety hybridized with explicit scale factors is a different known endpoint.'),
'P19.4':('Equivariant, transcendental and singular hybrid extensions',r'Establish the required automorphism-equivariant transcendental and singular extensions, with the exact stability and metric signatures specified. Retain the residual distinctions from the cited smooth polarized projective and static K\"ahler-class correspondences.'),
'P21.3':('Bedford--Taylor independence for continuous equal-curvature pairs',r'For a complete non-Archimedean field and a good separated strict boundaryless pure \(n\)-dimensional analytic space, \(n\ge2\), decide whether every positive \(\dprime\)- and \(\ddprime\)-closed CLD \((p,p)\)-current, \(0\le p\le n-1\), has Bedford--Taylor independence on every ordinary open for continuous psh pairs with equal Hessian currents. The full quantified equations appear below. A negative answer must give an analytic counterexample in this scope, not just a defective abstract tropical pushforward.')
}
assert tuple(TARGETS)==inv.EXPECTED_IDENTIFIERS
FAMILY_TITLES=[
'Regularization of arbitrary classical psh functions',
'Upper-semicontinuous local obstacle envelopes',
'A common local Monge--Ampère product',
'Balanced polyhedral regularity and realization',
'Recognizing continuous zero-Hessian functions',
'A geometric local theory on singular germs',
'Finite-energy equations on polarized affine cones',
'Pseudoeffective DXZ--MP realization',
'Zero-volume energy, measures and convex bodies',
'The general non-Archimedean Monge--Ampère equation',
'Residual hybrid entropy and YTD questions',
'Continuous-pair Bedford--Taylor independence']
CRITERIA=[
 r'Give precise geometric hypotheses for the requested local approximation, a construction in the specified approximant class and a proof of decreasing convergence, or counterexamples that establish the sharp failure range. Treat scalar extension and overlaps explicitly; a net must not be silently replaced by a sequence.',
 r'Prove the asserted conclusion for the full competitor family and every obstacle in the stated class. Account for branches, curve pullback, scalar extension and relative boundary, and distinguish positivity from continuity. A sufficient property of one selected equicontinuous subfamily is not a classification of all envelopes.',
 r'Every extension must specify its boundary datum and prove model independence, monotone continuity, locality and functoriality in its exact domain. Match the raw intersection normalization on the known common-model locus. State the polar rule before claiming an unbounded extension; literal restriction cannot preserve an unchanged probability normalization.',
 r'Fix the PA coefficient convention before stating regularity. Orthogonality requires the contact integral, not just total mass. A global BFJ comparison must name the polarization, operator domain, lifts, saturated lattice indices, intersection normalization and boundary terms; the already resolved local recursive comparisons are not new atoms.',
 r'Prove recognition for general continuous zero-Hessian functions in a new stated scope, or construct a counterexample satisfying the original strict ambient hypotheses. Make scalar-current ascent and two-sign regularization separate obligations. Ordinary smooth, weakly smooth and G-local real-PL conclusions have distinct consequences.',
 r'The requested geometric cone, envelopes, bounded products, finite energy and map compatibility are separate targets. Prove their smooth-germ specialization, primary-gauge changes and normalization/conductor rules. Do not identify an ideal-generated order completion with a geometric pluripotential theory without an additional comparison theorem.',
 r'For P13.1 the estimates must compare nonproportional Reeb fields and have the uniformity actually needed for energy differentiation. For P13.2 state necessary and sufficient conditions on measures on the invariant carrier, respecting the existing probability convention; bi-Lipschitzness onto the image does not imply surjectivity.',
 r'Identify the data retained by the proposed realization and prove its order, homogeneity, approximation and operator comparisons in the named positivity class. Distinguish \(\mathcal I\)-data from \(P\)-data. Known upper semicontinuity, the full K\"ahler image and strict-interior filtration maximality must not be relisted as unresolved. P14.8 must respect the verified raw-data obstruction.',
 r'Name the reference scale, dimensional carrier and retained singularity data, then prove independence of all claimed perturbation choices. Do not normalize zero mass to a probability. A class-level body with zero ambient volume does not supply a \(P\)-sensitive numerical-dimension theorem or an energy/operator construction.',
 r'For each axis, state the retained hypotheses and construct the finite-energy operator together with the corresponding existence-and-uniqueness theorem. Specify the measure mass and finite-energy condition, uniqueness modulo constants and the replacement inputs for compactness, envelopes, energy differentiation and comparison. An endpoint solving a special toric measure class does not remove a general axis.',
 r'Freeze the exact ray, approximation, family or equivariant signature and prove the residual statement with its entropy and energy normalizations. Keep recent preprint claims in their stated smooth polarized scope. The four targets are independent residual hybrid goals; they are not prerequisites for the already cited static uniform-model-stability-to-cscK implication.',
 r'Prove the quantified every-open, every-current continuous-pair assertion, or supply an analytic counterexample with all ambient hypotheses. A fixed polycylinder, a cover of one specified open and a genuine ordinary-open basis give different conclusions. Weak approximability is a sufficient condition, not a density theorem for arbitrary currents.']

sources={}
def expand(t):
 def sub(z):
  p=M/z[1];p=p if p.suffix else p.with_suffix('.tex');sources[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest();return expand(p.read_text())
 return re.sub(r'\\input\{([^}]+)\}',sub,t)
chapter=M/'parts/part6/ch72_major_open_problems.tex';sources[str(chapter.relative_to(ROOT))]=hashlib.sha256(chapter.read_bytes()).hexdigest()
original=chapter.read_text();expanded=expand(original)
# Strip proof environments only; retain every statement and all discussion.
expanded=re.sub(r'\\begin\{proof\}(?:\[[^]]*\])?.*?\\end\{proof\}','',expanded,flags=re.S)
subheads=list(re.finditer(r'\\subsection\{([^\n]+)\}',expanded))
family_sections=[]
for g in groups:
 marker=r'\label{'+g['label']+'}'
 pos=expanded.index(marker)
 head=max((h for h in subheads if h.start()<pos),key=lambda h:h.start())
 end=next((h.start() for h in subheads if h.start()>pos),len(expanded))
 # Final family is followed by the closing section, not a subsection.
 nxt=re.search(r'\\section\{',expanded[pos:end])
 if nxt:end=pos+nxt.start()
 body=expanded[head.end():end]
 # Strip editorial comments, leaving mathematical and source-status text.
 body=re.sub(r'(?<!\\)%[^\n]*','',body)
 family_sections.append(body.strip())
assert len(family_sections)==12
assert sum(t.count(r'\begin{problem}') for t in family_sections)==12

# Exact external references are rendered as Book <type> <number>.
# No external aux file or additional project file is needed at compile time.
aux={};types={};origins={}
for p in M.rglob('*.aux'):
 auxtext=p.read_text(errors='replace')
 chapter_match=re.search(r'\\newlabel\{(?:chap:|app:)[^}]+\}\{\{([^{}]+)\}',auxtext)
 chapter_number=chapter_match[1] if chapter_match else None
 for line in auxtext.splitlines():
  z=re.match(r'\\newlabel\{([^}]+)\}\{\{(\{?[^{}]*\}?)\}',line)
  if z and not z[1].endswith('@cref'):
   aux[z[1]]=z[2].strip('{}')
   if chapter_number:origins[z[1]]=chapter_number
  z=re.match(r'\\newlabel\{([^}]+)@cref\}\{\{\[([^]]+)\]',line)
  if z:types[z[1]]=z[2]
local=set(re.findall(r'\\label\{([^}]+)\}','\n'.join(family_sections)))
# Only included statement/discussion labels remain local after proof removal.
external=set();missing=set()
names={'chapter':'Chapter','section':'Section','subsection':'Section','subsubsection':'Section','appendix':'Appendix','subappendix':'Appendix section','theorem':'Theorem','lemma':'Lemma','proposition':'Proposition','corollary':'Corollary','definition':'Definition','example':'Example','remark':'Remark','warning':'Warning','problem':'Problem','equation':'Equation','figure':'Figure','table':'Table','part':'Part','enumi':'Item','enumii':'Item','enumiii':'Item'}
def bookref(key,eq=False):
 external.add(key)
 if key not in aux:missing.add(key);return r'\textbf{MISSING BOOK REFERENCE: '+key+'}'
 if eq:
  if not re.search(r'[0-9]',aux[key]) and key in origins:return r'\textup{(Book Chapter~'+origins[key]+', '+aux[key]+')}'
  return r'\textup{(Book '+aux[key]+')}'
 return 'Book '+names.get(types.get(key,''),'result')+'~'+aux[key]
def replace_ref(z):
 command=z[1];keys=[x.strip() for x in re.sub(r'(?<!\\)%[^\n]*','',z[2]).split(',')]
 pieces=[]
 for k in keys:
  if k in local:pieces.append('\\'+command+'{'+k+'}')
  else:pieces.append(bookref(k,command=='eqref'))
 return ', '.join(pieces)
family_sections=[re.sub(r'\\(Cref|cref|eqref|ref)\{([^}]+)\}',replace_ref,b) for b in family_sections]
assert not missing,sorted(missing)
# Preserve existing source locators and bibliography entries, without BibTeX.
citations=set()
for b in family_sections:
 for z in re.finditer(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}',b):citations.update(k.strip() for k in z[1].split(','))
bbl=(M/'book.bbl').read_text();matches=list(re.finditer(r'\\bibitem(?:\[[^\n]*\])?\{([^}]+)\}',bbl))
bibs=[];found=set()
for i,z in enumerate(matches):
 if z[1] in citations:
  end=matches[i+1].start() if i+1<len(matches) else bbl.index(r'\end{thebibliography}',z.end())
  bibs.append(bbl[z.start():end].strip());found.add(z[1])
assert found==citations,sorted(citations-found)

preamble=r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,aliascnt}
\usepackage{enumitem,booktabs,longtable,tabularx,xcolor}
\usepackage[final]{microtype}
\usepackage[unicode]{hyperref}
\usepackage[nameinlink,capitalize,noabbrev]{cleveref}
\usepackage{xurl}
\setlength{\emergencystretch}{2em}
\hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=green!35!black,urlcolor=blue!50!black,pdftitle={Complete Active Open-Problem Catalogue: Non-Archimedean Pluripotential Theory},pdfauthor={}}
\setcounter{tocdepth}{2}
\setlist[enumerate,1]{label=\textup{(\arabic*)},ref=\textup{(\arabic*)}}
\setlist[description]{style=nextline,leftmargin=1.5em,labelindent=0pt,itemsep=.35\baselineskip}
\newtheorem{theorem}{Theorem}[section]
\newaliascnt{proposition}{theorem}
\newtheorem{proposition}[proposition]{Proposition}
\aliascntresetthe{proposition}
\newaliascnt{lemma}{theorem}
\newtheorem{lemma}[lemma]{Lemma}
\aliascntresetthe{lemma}
\newaliascnt{corollary}{theorem}
\newtheorem{corollary}[corollary]{Corollary}
\aliascntresetthe{corollary}
\theoremstyle{definition}
\newtheorem{problem}{Problem}[section]
\newaliascnt{definition}{theorem}
\newtheorem{definition}[definition]{Definition}
\aliascntresetthe{definition}
\newaliascnt{example}{theorem}
\newtheorem{example}[example]{Example}
\aliascntresetthe{example}
\theoremstyle{remark}
\newaliascnt{remark}{theorem}
\newtheorem{remark}[remark]{Remark}
\aliascntresetthe{remark}
\crefname{problem}{problem}{problems}
\Crefname{problem}{Problem}{Problems}
\renewcommand{\index}[1]{}
\newcommand{\etalchar}[1]{$^{#1}$}
'''
notation=(M/'style/notations.tex').read_text().replace(r'\newcommand{\one}{\mathds 1}',r'\newcommand{\one}{\mathbf 1}')
sources['manuscript/style/notations.tex']=hashlib.sha256((M/'style/notations.tex').read_bytes()).hexdigest()
front=r'''
\title{Complete Active Open-Problem Catalogue\\[.5em]\large Non-Archimedean Pluripotential Theory}
\author{}
\date{Repository snapshot: 2 October 2026}
\begin{document}
\maketitle
\begin{abstract}
This standalone catalogue contains every active open-problem item in the
current book: 42 separately addressable targets in twelve mathematical
families. Each family includes its full problem statement, individual
atomic targets, completion criteria, and the detailed state of knowledge
recorded in the manuscript, with positive cases, negative obstructions,
remaining gaps and primary-source locators. The catalogue preserves
conditional and source-scoped results and does not assert that a recent
preprint claim has been independently proved in the book.
\end{abstract}
\tableofcontents
\clearpage
\section*{Scope, dates and how to read this catalogue}
\addcontentsline{toc}{section}{Scope, dates and how to read this catalogue}
``Complete'' refers to the active problem inventory of this book. The list
is selective as a survey of the whole subject. Stable IDs such as P02.1
are editorial addresses, not theorem numbers; gaps in the numbering are
retired or historically skipped targets and are not reassigned.

The general literature search in Chapter 72 has a cutoff of 24 August
2026, with targeted source updates through 19 September 2026 and dated
verification records and author-supplied integrations through 26 September
2026. The 2 October editorial reconciliation does not constitute a new
exhaustive literature search. ``Open'' below means open in the exact
residual scope recorded by those sources. No new research campaign or
solution is claimed by this export.

Each family begins with concise atomic descriptions and completion
criteria. Its full mathematical statement and detailed state-of-the-art
record follow. The latter is drawn from the active Chapter 72 text and its
included statement fragments. Proof bodies are omitted; mathematical
statements, conventions, source locators and domain restrictions are
retained. Dated verification paragraphs are historical evidence, not new
verdicts. Later supplied-source retirements supersede earlier checkpoint
residuals, as the surrounding text explicitly records.

References of the form ``Book Theorem 70.2.1'' point to the accompanying
monograph. References without the word ``Book'' point inside this catalogue.
The bibliography is embedded, so this file needs neither external TeX
inputs nor an external bibliography database. Local theorem numbering is
specific to this catalogue. The twelve problem families remain genuinely
open; a settled boundary case inside a family does not settle the family.

\section*{Common notation and formulation boundaries}
\addcontentsline{toc}{section}{Common notation and formulation boundaries}
\begin{description}
\item[Fields and analytic spaces.]
\(K\) denotes a complete non-Archimedean field. Trivial or nontrivial valuation,
strictness, goodness, separatedness, pure dimension and relative boundary
are retained exactly where a statement requires them. \(X^{\mathrm{an}}\)
is Berkovich analytification. ``Ordinary open'' refers to its ordinary
topology, rather than an admissible G-cover. A statement on one fixed
polycylinder is weaker than an every-open statement obtained from an actual
basis.
\item[Semivaluations and normalized local boundaries.]
We use \(v=-\log|\cdot|\), allow \(+\infty\) on the support of a
semivaluation, and retain that support. For a local ring \(R\) and a primary
ideal \(\mathfrak a\), a normalized link is a section
\(\{v:v\text{ is centered},\ v(\mathfrak a)=1\}\).
Changing \(\mathfrak a\) is a radial change with a stated cocycle; it is not
an identification of all normalizers. The symbol \(X^\beth\) denotes the
valuative/trivially valued carrier used by the raw ideal transform.
\item[Positivity classes.]
\(\PSH\) means the specified plurisubharmonic class in each theory.
Classical psh is the upper-semicontinuous curve-test notion, with the
extended \(-\infty\) convention where stated. Real PL means the real linear
extension of the local integral piecewise-linear class. Semipositivity is
its residue/model nefness condition. Locally Fubini--Study is the local
finite logarithmic-max class with its prescribed denominators.
Ordinary CLD smoothness uses smooth tropicalizations; weak smoothness
permits harmonic tropicalizations. These classes are distinct.
CLD-v2 denotes the second generated CLD psh stage in the book.
\item[Currents and products.]
\(\dprimeddprime=\dprime\ddprime\) is the CLD Hessian. A continuous
function defines the order-zero current \([h]\). CLD means
Chambert--Loir--Ducros; GJR means Gubler--Jell--Rabinoff; BFJ means
Boucksom--Favre--Jonsson. Positivity of one Hessian current does not, by
itself, construct mixed wedge products or prove classical psh recognition.
\item[Global energy and mass.]
\(\mathcal E^1\) denotes the finite-energy class of the named theory.
Reference weights, raw intersection mass and probability normalization
must be fixed before comparing energies or measures. Quotienting by
\(\mathbf R\) means uniqueness modulo additive constants. Zero top mass
cannot be divided into a probability measure. The affine-cone probability
operator is an explicitly separate convention.
\item[Complex singularity data.]
\(\alpha\in H^{1,1}_{\mathrm{BC}}(X,\mathbf R)\) is a real Bott--Chern class.
MP means Mesquita--Piccione, DXZ means Darvas--Xia--Zhang, and BJ means
Boucksom--Jonsson. \(\mathcal I\)-equivalence records multiplier-ideal data;
\(P\)-equivalence records the finer envelope/singularity data. The latter
cannot generally be recovered from the former, even at positive mass.
\item[Polyhedral normalization.]
PA denotes piecewise-affine functions. BMPS means
Botero--Mazzon--Pille-Schneider. Literal integral slopes and the real scalar
extension are separate conventions. In dimension \(d\), the polyhedral
intersection convention differs from the real Alexandrov measure by the
factor \(d!\) and the face multiplicity. Saturated tangent lattices and
analytic multiplicities are part of an analytic comparison.
\end{description}

\section*{All 42 active items}
\addcontentsline{toc}{section}{All 42 active items}
All entries below have status \textbf{Open} in their residual scope.
The tier distribution is
\[ (T1,T2,T3,T4,T5)=(0,3,7,15,17). \]
Tiers are editorial difficulty classes: T2 denotes a focused missing
bridge, T3 a substantial theorem in a developed framework, T4 coupled
comparison inputs, and T5 a foundational or programme-level target.
They do not constitute mathematical conclusions.
\begin{longtable}{@{}p{.105\textwidth}p{.07\textwidth}p{.76\textwidth}@{}}
\toprule ID & Tier & Target (links to its full dossier)\\\midrule\endfirsthead
\toprule ID & Tier & Target\\\midrule\endhead
\bottomrule\endfoot
'''
rows=[]
for g in groups:
 for a in g['atoms']:
  title,_=TARGETS[a['id']]
  rows.append(r'\hyperref[atom:'+a['id']+']{'+a['id']+'} & '+a['tier']+' & '+title+r'\\')
front+='\n'.join(rows)+'\n\\end{longtable}\n'

body=[]
for i,(g,title,criterion,detail) in enumerate(zip(groups,FAMILY_TITLES,CRITERIA,family_sections),1):
 family=r'\clearpage\section{'+title+'}\n'+r'\label{family:'+str(i)+'}\n'
 family+=r'\noindent\textbf{Active items:} '+', '.join(a['id'] for a in g['atoms'])+r'. \textbf{Status: Open in the residual scope.}'+'\n\n'
 family+=r'\subsection{Atomic targets}'+'\n'
 for a in g['atoms']:
  t,d=TARGETS[a['id']]
  family+=r'\subsubsection*{'+a['id']+' ('+a['tier']+'): '+t+'}\n'+r'\label{atom:'+a['id']+'}\n'+r'\addcontentsline{toc}{subsection}{'+a['id']+': '+t+'}\n'+d+'\n\n'
 family+=r'\subsection{What constitutes a solution}'+'\n'+criterion+'\n\n'
 family+=r'\subsection{Full statement and detailed state of the art}'+'\n'+detail+'\n'
 body.append(family)

retired=r'''
\clearpage
\section*{Settled questions excluded from the active count}
\addcontentsline{toc}{section}{Settled questions excluded from the active count}
The active list does not revive questions already retired in the repository.
Important excluded signatures include the ample-class full-cone comparison;
real-PL positive-current/residue-nefness comparison; ordinary CLD-smooth
curve regularization; singular classical-pluriharmonic real-PL regularity
(P06.1); the uniform hierarchy bound (P07.2) and the supplied unrestricted
first-stage counterexample (P07.1); global ordinary smooth psh metric
approximation (P08.1, negative); the unrestricted proper analytic
parlinear/global-dpsh extension (P08.2, negative); delta-metricity and signed
PL decomposition/positive-cone obstructions; generalized-Lelong separation;
the global BJ Radon--Riesz implication (negative); excellent-germ normalized
boundaries (P12.1); raw-transform upper semicontinuity (P14.2), full
K\"ahler DXZ--MP comparison (P14.3), and strict-interior raw-filtration
maximality (P14.7); Banach-family raw Monge--Ampère continuity (P17.1);
both listed Favre endpoint-continuity signatures (negative); real-toric
mixed products; and the original cross-fan realization questions.
Local recursive projection and algebraic-chart comparisons P05.3/P05.4
are also retired, with the corrected operator-domain assumptions retained.

A negative unrestricted statement can coexist with the open task of
classifying its valid range. Thus the unconditional nodal-envelope failures
do not retire P03.1--P03.3; nor do zero-volume probability and
\(\mathcal I\)-only mass obstructions retire a theory with new appropriate
data. The recent smooth polarized projective entropy and YTD claims are
kept in their exact preprint scopes and are not relisted as residual atoms.

\section*{Source and verification note}
\addcontentsline{toc}{section}{Source and verification note}
The controlling sources are Chapter 72 and its active inputs, the atomic
inventory, and the dated editorial source/verification ledgers in the
repository \url{https://github.com/chaoxu/nonarchimedean-pluripotential-theory}.
The exact repository URL is specified in the export manifest; this catalogue
is a local source export, not a claim of remote publication.
The extraction retains all twelve formal problem statements and the full
state-of-knowledge discussions for those families, while omitting proof
bodies. External book references are resolved from the successful current
book build; all bibliography entries used here are embedded verbatim.
The 42 atomic IDs, placement and tiers are checked against the exact active
inventory. This catalogue supplies no new independent mathematical verdict
and no new literature search beyond the dated source coverage.

\clearpage
\begin{thebibliography}{EGA IV$_4$}
'''
# Use the actual configured remote, not a guessed book repository URL.
remote=subprocess.check_output(['git','remote','get-url','origin'],cwd=ROOT,text=True).strip()
url=re.sub(r'^git@github.com:','https://github.com/',remote).removesuffix('.git')
retired=retired.replace('https://github.com/chaoxu/nonarchimedean-pluripotential-theory',url)
text=preamble+notation+front+'\n'.join(body)+retired+'\n\n'.join(bibs)+'\n\\end{thebibliography}\n\\end{document}\n'
# Internal source has no project includes or bibliography dependencies.
assert not re.search(r'\\(?:input|include|bibliography)\{',text)
assert text.count(r'\begin{problem}')==12
assert len(re.findall(r'\\label\{atom:P\d+\.\d+\}',text))==42
assert len(re.findall(r'\\label\{([^}]+)\}',text))==len(set(re.findall(r'\\label\{([^}]+)\}',text)))
text=re.sub(r'\\texttt\{([0-9a-f\s]+(?:\\allowbreak[0-9a-f\s]+)+)\}',lambda z:r'\nolinkurl{'+re.sub(r'\\allowbreak|\s+','',z[1])+'}',text)
text=re.sub(r'(Theorem|Proposition|Corollary|Lemma|Example|Definition|Remark|Chapter|Section|Appendix)[\s~]+Book \1~',lambda z:'Book '+z[1]+'~',text)
text=text.replace(r'\begin{thebibliography}{EGA IV$_4$}',r'\phantomsection'+ '\n'+r'\addcontentsline{toc}{section}{References}'+ '\n'+r'\begin{thebibliography}{EGA IV$_4$}')
OUT.write_text(text)
manifest={
 'snapshot_date':'2026-10-02','repository_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'remote':remote,
 'scope':'all active open-problem items in the book, not an exhaustive subject bibliography',
 'general_literature_cutoff':'2026-08-24','targeted_updates_through':'2026-09-19','dated_records_and_supplied_integrations_through':'2026-09-26',
 'active_atoms':report['active_atomic_questions'],'families':report['formal_problem_environments'],'tiers':report['tiers'],'identifiers':report['identifiers'],
 'read_source_inputs_before_proof_omission':sources,'external_book_references':len(external),'bibliography_entries':len(bibs),'tex_bytes':OUT.stat().st_size,'tex_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
 'exact_formal_problem_statements':'12/12 preserved from active Chapter 72, with external references rendered as resolved Book numbers',
 'state_of_art':'all discussions and statements in the twelve corresponding Chapter 72 subsections; proof bodies omitted',
 'new_mathematical_results':False,'native_compilation':'PENDING','visual_review':'PENDING'}
(ROOT/'output/open_problems_catalogue_2026-10-02_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({k:manifest[k] for k in ['active_atoms','families','tiers','external_book_references','bibliography_entries','tex_bytes','tex_sha256']},indent=2))
