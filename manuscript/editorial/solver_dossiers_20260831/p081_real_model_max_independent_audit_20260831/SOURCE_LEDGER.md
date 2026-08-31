# Exact source ledger: real-model maximum audit

Date: 2026-08-31. Auditor: /root/p082_independent_reaudit.
No production acceptance or novelty claim.

## Primary BFJ source

Boucksom, Favre, Jonsson, Singular semipositive metrics in
non-Archimedean geometry. Published reference:
Journal of Algebraic Geometry 25(1) (2016), 77--139,
[DOI 10.1090/jag/656](https://doi.org/10.1090/jag/656).
The live bibliography entry BFJ16 is in
manuscript/bibliography/ComplexGeometry.bib, not NonArchimedean.bib.

The directly inspected primary version is
[arXiv:1201.0187v2](https://arxiv.org/abs/1201.0187v2),
downloaded through [the arXiv PDF](https://arxiv.org/pdf/1201.0187).
It has 49 pages. The margin says version 2, 21 January 2014;
the title page's internal date says 22 October 2018. These source facts
are recorded without attempting to reconcile the dates. Citations below
use this exact version's numbering and internal page numbers, not assumed
page offsets into the 2016 journal.

PDF path:
/private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf

PDF SHA256:
8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270

Text path:
/private/tmp/BFJ_singular_1201.0187_audit_20260831.txt

Text SHA256:
df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f

The text was extracted with pdftotext -layout. Its extraction control
characters remain part of the original derived source and were never
copied into authored TeX or Markdown.

| Exact source location | Checked interface | Excluded overreading |
| --- | --- | --- |
| Section 1.1, p. 6; Section 2.4, p. 9 | Complete DVR, residue characteristic zero, smooth connected projective X, normal projective flat models | No algebraic closedness of K is assumed |
| Definition 1.3, p. 7; Section 5.1, pp. 22--23 | Real numerical classes and nefness by degrees on vertical curves | Real theta does not make every real-coefficient potential a rational model |
| Lemma 1.4 and Corollary 1.5, pp. 7--8 | Positive extensions on sufficiently high models | Does not make pullback of an ample class ample on an arbitrary refinement |
| Definition 2.1, p. 10 | D(X)=D(X)_Q; D_Z and D_R are separately mentioned | D_R is not declared a vector lattice |
| Proposition 2.2, pp. 10--11 | Integral model functions are differences of ideal logarithms; integral maxima remain integral models | The corresponding statement for finite real spans is not asserted |
| (3.2)--(3.4), pp. 14--15 | Formal monomial expansion with integral exponents | Rational cuts are proved from exponents; not inferred from generic piecewise affineness |
| Proposition 3.12 and Corollary 3.13, pp. 15--16 | Restrictions of rational model functions are piecewise affine | Only Corollary3.13's first assertion is used |
| Proposition 5.2, p. 23 | A positive representative on sufficiently high models when generic class is ample | Its written proof constructs a real divisor; rational choices are obtained by explicit openness if needed |
| Definition 5.5, p. 23 | theta-psh model means an element of D(X)=D_Q with semipositive curvature | No implicit switch to D_R |
| Lemma 5.6, p. 24 | A globally generated twisted ideal yields a nef rational-model curvature | No global generation for irrational line bundles is asserted |
| Proposition 5.8, pp. 24--25 | D_Q theta-psh class is Q-convex and max-stable for arbitrary real theta | Real convexity/max closure of D_R is not its statement |
| Proposition 5.9, p. 25 | Rational theta-psh models satisfy convexity/retraction | Real extension requires a separate approximation argument |
| Theorem 5.11, p. 25 and proof thereafter | Closedness in D(X), for pointwise divisorial convergence whose limit lies there | Does not promote arbitrary uniform limits to model functions |
| Definition 7.1, pp. 32--33 | Skeletal uniform closure plus usc/retraction, with ample generic theta | The model approximants use the preceding rational convention |
| Proposition 7.4, p. 33 | Full PSH is real-convex and max-stable | Different class from D_R |

Full relevant statements were read, including proofs of
Propositions2.2,3.12,5.2,5.8 and the proof structure surrounding
Definition7.1/Proposition7.4. Theorem5.11 was used only to delimit its
statement, not as an unproved limit-identification step.

Full PDF pages 10,15,16,23,24,25,33 were rendered and visually inspected.
This confirmed the coefficient qualifiers and displayed formulas.
The source was not edited or re-exported as a new PDF.

## Audited manuscript interfaces

Worktree /private/tmp/nappt_p071_20260827:

| File / locus | Finding |
| --- | --- |
| ch20_model_forms.tex, eq:ch20-model-functions and def:ch20-ddc | Explicit finite real vertical-Cartier convention |
| ch20_model_forms.tex, eq:ch20-sign | Positive divisor function, special fibre constant +1 |
| ch20_model_forms.tex, prop:ch20-model-max | Real convexity valid; pointwise real-model max closure false |
| ch20_model_forms.tex, prop:ch20-curve-lattice | Componentwise vertex maximum is a different, valid finite-dimensional operation |
| ch20_model_forms.tex, thm:ch20-model-envelope item directedness | False for the explicitly real-model obstacle family |
| ch21_bfj_psh.tex, def:ch21-bfj-psh | Its real/rational approximation conventions coincide under the stated ample generic hypothesis, by the supplied density proof |
| ch21_bfj_psh.tex, thm:ch21-stability maximum proof | Invalid real-model step; full BFJ maximum statement has a valid rational-approximation repair |
| ch21_bfj_psh.tex, lem:ch21-model-skeletal-properties real-case paragraph | Needs an explicit density/perturbation justification, not the false max-closure paragraph |
| ch24_bfj_ma.tex, prop:model-maximum-principle, lines 2329--2394 | Real maximum need not have a common model; rational-input checkpoint avoids this defect |
| ch24_bfj_ma.tex, cor:ch24-model-locality-open, lines 2398 onward | Separate direct locality proof does not take a maximum; not refuted here |
| ch26_energy.tex, prop:bounded-energy-identities, lines 836--843 | Minimum does not preserve psh; cofinal compactness tail supplies boundedness without truncation |
| ch30_functoriality.tex, lem:ch30-pullback-model-calculus, lines 354--361 | Composition/max equality is pointwise true, but real-model membership is false |
| ch30_functoriality.tex, bounded projection proof, lines 831--838 | Lower clamp equals the original approximant; a tail provides uniform upper control |
| ch30_functoriality.tex, def:ch30-model-descent-property and thm:ch30-continuous-descent | Explicit descent property is D_Q; real approximants require a rational approximation interface |
| ch30_functoriality.tex, sec:ch30-descent-limits, lines 2833--2838 | Finite averaging already preserves decreasing order; finite minima can destroy nefness even in D_Q |

Exact source hashes are recorded in INDEPENDENT_AUDIT.md and SHA256SUMS.
Line locators refer to those exact bytes, not future edited versions.

## Mathematical contribution and limits

The blowup intersection calculation and rational-breakpoint argument are
given in full in the audit. They verify a proposed elementary
counterexample; no claim that this is a novel theorem is made.
The maximum theorem on PSH is a primary-source result. The rational
density argument explains how to repair the book's real-model convention
without reducing the original BFJ scope of that maximum theorem.

No conclusion about an arbitrary merely nef generic theta is extracted
from the ample-representative argument. In particular, Chapter20's broader
semipositive model-envelope signature is not silently certified.
No CLD comparison, arbitrary-field extension, or general envelope theorem
is used.
