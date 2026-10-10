# Chapter 15: second reading audit

Date: 3 October 2026. The original 4,920-line main source and all 57
direct inputs, totalling 5,795 lines, were freshly read continuously.
The four replacement reader fragments, totalling 269 lines, were also
read in full. The final main source has 4,996 lines and preserves all
164 labels. Compared with the completed scope-correction/catalogue
checkpoint `3514ab3`, all 139 formal environments, including proofs and
warnings, retain their order: 81 are byte-identical and 58 change. The
complete mathematical diff and final edited contexts were reviewed.

The [input ledger](second_reading_ch15_input_ledger_20261003.json) records
all original paths, hashes and reading coverage. All 57 original files
remain byte-identical. Fifty-three remain active; four historical v39/v40
inputs are replaced in the active chapter by the four corrected reader
fragments. Their frozen packets and verifier receipts are preserved.
The [LFS scope-correction audit](ch15_lfs_descent_scope_correction_audit_20261003.md)
records the earlier correction and its Chapter 72 reconciliation. That
checkpoint and the standalone open-problem catalogue are already committed.

## Mathematical architecture and repairs

The opening now distinguishes graded residue dimension from dimension of
an analytic germ, ordinary analytic moment coordinates from their reflected
logarithmic coordinates, and internal reductions from substantial published
imports. It includes the three supplied exposition sections in its roadmap.
Real-variable convolution in a fixed moment chart and the supplied
first-stage theorem on good analytic spaces are no longer contradicted by
blanket claims that regularization is unavailable.

The formal Poincare--Lelong reduction no longer treats a local depth-one
condition as the Serre S1 condition, or claims that shrinking proves it.
Unit and quotient reductions are proved; the remaining reduction is
explicitly imported from CLD25 16.7.5. The analytic Hauptidealsatz and
semicontinuity control relative dimension, while the ambient S1 step is a
separate published input. The nilpotent example computes the different
naive quotient length and integration multiplicity. Dimension zero is
handled separately.

The six-step analytic proof now computes J and the symmetric test
projection with the correct dimension signs. Test support lies in the
relative interior. Compact support below a logarithmic cutoff gives a
strictly smaller radius for the next reduction. Graded residue bounds
kill the relevant test-form germs on the divisor. The inherited boundary
and new level face are removed separately. The final logarithmic coordinate
is reflected together with its calibration, and the inner-face sign is
computed in that coordinate. On lateral faces the surviving first degree
exceeds the face dimension; balancing is not substituted for this
degree calculation.

The constant in the one-variable formula is detected by a radial compact
test. Ordinary smooth germs at a K-rational rigid point are locally
constant because they use finitely many analytic units; support in that
point then gives the evaluation functional without asserting that every
bidimension-(0,0) current is a measure. The closed-disc test includes the
Gauss boundary term. A zero on a curve is now explicitly K-rational when
its numerical mass is stated as one. In the quartic computation, the
absolute value is rescaled consistently, the five model blowups are made
over the discretely valued base before scalar extension, and the four
zero masses and the opposite valuation signs are checked. A nonmonic
leading factor may be harmonic without having constant norm.

The Bochner--Martinelli statement includes the nonempty regular-sequence
and codimension hypotheses. A depth-at-points condition is distinguished
from Serre Sd. The zero-extension assertion uses the graded-residue bound
and the test-space topology. For arbitrary positive real cutoff radius,
the truncated potential is continuous CLD-psh; membership in the stricter
real-PL class is not inferred. Fibre integration carries the analytic
multiplicities and calibration of the relative Monge--Ampere result,
rather than an arbitrary pullback of a Dirac current. Stabilization remains
the exact CLD25 18.7.3 import, with relative dimension n minus d. Finite
G-additivity is distinguished from an ordinary partition of Borel
coefficients. The nonregular example has its actual smaller codimension.

Levine's potential has a unique zero extension in the indicated test
degree; the earlier warning against uniqueness was incorrect. On the
blowup, the section goes from L_b to L_a and its divisor is E, giving
dd''h = A - B - delta_E. The blowup map is denoted pi to avoid overloading
the integer p. Products with h are constructed in the special
CLD25 18.3.8--18.3.9 setting using common-chart coefficient measures and
their supports, not by arbitrary multiplication of an unbounded function
and a current. B to the p vanishes by the metrized pullback construction
and the projective dimension. Pushforward uses the exact metric-current
projection formula and vertical degree one. Both the support and extension
degrees are made explicit.

The transfinite construction starts with all real constants and includes
minus infinity by a decreasing sequence. Its minimality proof does not
identify an unnecessarily large comparison class with Psh. Stabilization
is a fixed-point assertion for the whole sheaf, using one set of all
open-section pairs, rather than a possible stall on one open set. Uniform
limits use finite tail errors or an exact subsequence. First-stage
collapse on good analytic spaces is retained at its supplied scope and
is distinguished from the abstract tropical counterexample.

Regularized maxima ignore an entry when it cannot exceed the others,
allowing ties. The Hessian calculation uses a pointwise covector
diagonalization and evaluates derivatives at the vector of arguments.
The internally proved composition reduction uses all of real space;
the proper convex-domain version is explicitly the published CLD25 8.2.1
input. Pointwise convergence alone is not said to keep approximants in
one prescribed proper domain. The distributional convexity statement
keeps its continuous representative, and full extended-real Psh is
distinguished from finite convex functions. Centered even convolution
kernels suffice; radial symmetry is not required.

The smooth positive-current converse retains very-richness, with the
analytic case supplied by CLD25 16.4.4. The curve/current and
ordinary-smooth approximation results remain within their verified
scopes. The meromorphic logarithm is pointwise a difference only on the
common invertibility locus, while the current identity holds on the
whole presentation domain. The cusp example shows why an effective
divisor or a psh logarithmic extension does not by itself prove analytic
extension on a nonnormal space. The two-variable polar example uses the
canonical Bochner--Martinelli zero extension; no undefined untruncated
Bedford--Taylor square is claimed.

At a vertex, an unbalanced correction is a derivative-evaluation
functional. It is not written as a Dirac measure with a test-dependent
coefficient. The one-dimensional abstract maximum theorem specifies the
ambient-induced balanced, locally finite polyhedral model and finite
embedded stars. Analytic boundary examples keep their boundary and
valuation hypotheses.

The general analytic maximum principle is broader: GR25a Theorem 6.1
works on any analytic space over any complete non-Archimedean field,
at analytic interior points. The statement, roadmap, warnings and
dictionary now agree on that scope. Compact connected spaces are
constant when boundaryless. Goodness, strictness and nontrivial valuation
remain in the separate real-PL comparison, where those source hypotheses
are needed. The extended curve-test definition includes the identically
minus-infinity alternative. The final table gives definitions and proved
implications without adding false converses or a uniqueness claim for
regularization kernels.

## LFS correction and research boundary

For real coefficients, GJR section 7.9 does not make LFS closed under
finite maxima. GJR Example 5.3, applied to the two-sheet fold, disproves
the former inference. The corrected local split-envelope comparison
transports an individual sheet and needs no maximum closure. It compares
envelopes formed on the displayed domains, not restrictions of global
envelopes. Rational semipositive-PL maximum descent is retained. The
real-PL version assumes that the orbit maximum is already real PL; the
stronger LFS-to-base-PL envelope inequality is conditional on that same
property for every relevant competitor.

The later squeezing arguments need only the weaker valid inequalities
and their other stated equalities, so their unchanged frozen proofs
remain applicable. The rational finite-flat, local approximation,
section-palette, conservation, collar, scalar-section, supplied gluing
and pinched-bidisc arguments were all read in full. They do not need the
withdrawn real-maximum closure. Chapter 72 and the separate catalogue
already reflect these boundaries. The general maximum-principle
correction introduces no new research claim or problem retirement.

These are definition, proof, scope, example and exact source-import
repairs. Old independent verifier verdicts retain their original scopes;
they do not validate changed statements. No new independent verdict,
new original research result or solved open problem is claimed.
Semantic, dependency, delimiter and structural checks replace the
unavailable legacy writing tool.

## Primary checks and final gates

Fresh CLD25 text checks cover 16.1.4, 16.7.1--16.7.5, 8.1.4,
8.2.1--8.2.4, 8.3.1--8.3.2, 18.3.8--18.3.9, 18.6.2 and
18.7.3--18.7.5. All twenty selected physical pages were actually
viewed: 436--437, 460--462, 196, 198--202, 516--518 and 533--538.
The stored PDF SHA-256 is
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
The source's depth shortcut is not promoted to a general ring theorem;
its dimension, line-bundle arrow and sign misprints are identified
explicitly. Chapter 14's primary check of 16.4.4 and earlier calibrated
Stokes evidence are reused.

Fresh GR25a arXiv-v2 text checks cover Definitions 3.4 and 4.1,
Proposition 4.2, Theorems 5.4, 6.1 and 7.6, including the complete
maximum-principle proof and the stated CLD implication. All eleven
selected pages were viewed: 3, 10--11, 21, 25, 28--31 and 35--36.
Its PDF SHA-256 is
`83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`.
The prior correction audit records the freshly checked GJR-v3
Example 5.3, section 7.9 and Propositions 5.11 and 7.6, with physical
pages 31, 34, 46--47 viewed. No fresh exhaustive literature search,
full published GJR reading or full Thuillier primary audit is claimed.

The final full-book build has 4,178 pages and 19,513,475 bytes, SHA-256
`a0e643f829fe9ebb3d0461254c5769c86abe34dd0866e8a2c2535a9a1dd45b45`.
There are zero TeX errors, LaTeX/package warnings, overfull boxes,
unresolved references/citations or rerun requests, and 866 nonfatal
underfull boxes. All 158 Chapter 15 physical pages 675--832 and seams
674/833 were viewed in forty initial contact sheets. A dictionary-width
problem and two small scope clarifications were repaired; all three
changed final sheets were viewed again, and the remaining 37 are
bitmap-identical to the reviewed baseline. Formulas, proofs, warnings,
tables and seams show no clipping, collision or detached heading.

Post-render references and structure pass for 425 active inputs and
12,564 unique labels, with no missing input, duplicate or dangling
reference. The inventory remains 42 atoms in twelve families, with
tiers `(0,3,7,15,17)`. Exact hashes and coverage are recorded in
[the manifest](second_reading_ch15_manifest_20261003.json). The review
PDF is
`/workspace/book-completion-drafts/second-reading/Ch15_Review_2026-10-03.pdf`.
Chapter 15 passes this second-reading gate. Chapter 16 is next;
no later chapter has yet been marked reread. The whole-book continuation
remains in the cloud, without Xean or default-branch publication.
