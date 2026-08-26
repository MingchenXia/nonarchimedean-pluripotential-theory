# Part II post-expansion mathematical and source audit (24 August 2026)

## Scope and source firewall

This audit covers Chapters 9--19, from Lagerberg superforms through the CLD,
delta-form, tropical-toric, and harmonic-tropicalization examples.  It is a
mathematical-correctness, normalization, terminology, and provenance audit;
none of the corrections below is promoted as a new result.

The pass checked signs for \(\dprime,\ddprime\), current bidegrees, lattice
indices, primitive-normal conventions, max-plus versus valuation
coordinates, pullback and pushforward hypotheses, Poincare--Lelong, tropical
balancing, and the factorial in real and CLD Monge--Ampere measures.  The
abstract tropical terminology remains in the max-plus convention and uses
primitive outgoing vectors and weighted balancing in the quotient lattice,
compatible with Gathmann's and Mikhalkin--Rau's usage; analytic coordinates
remain \(u=-\log|f|\), with the manuscript's explicit reflection firewall.

The principal source boundaries checked were CLD25; GK17, especially
Proposition 1.12, Proposition 2.16, and Corollary 3.19; GK19, Theorem 6.10;
GJR26, Theorem 9.7; Wanner19, Theorem 4.7 and Corollaries 4.8 and 5.4; and
the toric comparison statements in BGJKK25.  The prohibited
Deligne--Riemann--Roch source was not used and does not occur in the audited
chapters or in this report.

## Corrections integrated

### Chapters 9 and 11: no direct correction

The superform sign table, involution, wedge signs, Stokes orientations,
lattice measure, balancing defect, and projection formula were checked
against the conventions used downstream.  No high-confidence mathematical
error requiring a direct edit was found.

### Chapter 10: pushforward balancing

The detailed proof of balancing under tropical pushforward formerly factored
one target primitive normal from all source facets over a target wall.  That
is not legitimate when the source facets map to different target facets.  It
now keeps the vector sum

\[
 \sum_{\sigma\supset\tau}m_\sigma
 [N'_{\sigma'(\sigma)}:F(N_\sigma)]
 u_{\sigma'(\sigma)/\tau'}
\]

and only then regroups over source walls.  The lattice-index relation and the
pushforward weights are unchanged.

### Chapter 12: image scope and graded dimension

The introduction no longer calls every tropical image a single rational
polyhedron.  It states the correct local rational-polyhedral conclusion and,
on a compact analytic domain, a finite rational polyhedral set.

The residual-degree lemma formerly asserted equality after every surjective
torus homomorphism, using the false implication that a surjection has
injective character map with finite cokernel.  Equality is now restricted to
isogenies; the general inequality remains valid.

The proof of the \(d_K\)-bound no longer counts the rational-rank contribution
twice.  The manuscript's \(d_K(x)\) is already the graded transcendence
degree, so the proof now invokes the graded Abhyankar inequality directly.

### Chapter 13: the chart category and the role of properness

The canonical tropical-chart object is terminal, not initial.  The morphism
direction in the cofiltered comparison was corrected accordingly: the
minimal-image object maps to a presentation with a larger ambient
polyhedral neighborhood.

Properness is now described as the hypothesis needed for the global
calibrated tropical pushforward and integral, not as a condition for a
tropical image to exist at all.  Local tropical images on nonproper opens
remain meaningful.

### Chapter 14: bidegrees, support, homogeneity, and pushforward

The introductory bidegree of the current carried by a codimension-\(r\)
smooth cycle was corrected to \((n-r,n-r)\).

The rigid-support argument no longer assumes that the rigid locus is locally
closed or is itself a closed weakly analytic subset.  It applies
extension-by-zero to the closed support of the hypothetical current, whose
points all have local tropical dimension zero.

The proof that the Hessian current of a degree-one homogeneous convex
function is strongly homogeneous no longer claims that ordinary convolution
preserves degree-one homogeneity.  It uses the distributional Euler identity
\(\sum_i x_i\partial_i h=h\), differentiates it, and obtains the required
contraction identities for the distributional Hessian.

For a current with merely \(g\)-compact support, the pushforward support is
now contained in \(\overline{g(\operatorname{Supp}T)}\).  The closure may be
removed when \(g\) is proper.  This aligns the theorem with its proof and
with the elementary topology.

### Chapter 15: Hessian sign and the CLD/Wanner terminology firewall

For an affine function of the annular coordinate, the displayed local
formula now has
\(\dprimeddprime\varphi=\varphi''\dprime t\wedge\ddprime t=0\); the stray
minus sign was removed.

The curve discussion now distinguishes three notions.  The manuscript's
approximation-generated CLD class implies positivity of the current;
Wanner's use of ``psh'' means positivity of that current and is equivalent,
for continuous functions on the stated algebraic curves, to Thuillier
subharmonicity.  The reverse implication into the manuscript's CLD hierarchy
requires an additional CLD-smooth regularization theorem and is not asserted
in general.  The text also no longer says categorically that no
regularization exists on any Berkovich space; it says that there is no
general convolution analogue.

### Chapter 16: the curve comparison boundary

The transfer ledger now says exactly what the cited sources give on curves:
Wanner identifies current positivity with Thuillier subharmonicity, while
the metric-graph Laplacian formula is asserted for model or skeletal
potentials.  It no longer identifies two general Monge--Ampere constructions
through a fixed graph Laplacian.

### Chapter 17: the Alexandrov factorial

For the maximum of \(r\) affine functions on
\(\mathbf R^r/\mathbf R(1,\ldots,1)\), the standard simplex has lattice
volume \(1/(r-1)!\).  Thus its Alexandrov measure is
\(1/(r-1)!\) times the Dirac mass, and the Lagerberg/CLD top wedge, which is
\((r-1)!\) times the Alexandrov measure, is the unit Dirac mass.  The former
text incorrectly assigned unit mass to the unscaled Alexandrov measure.

### Chapter 18: smooth weights and corner balancing

The smooth-weight warning now reflects GK17, Proposition 2.16: underlying
tropicalizations have constant weights unless stated otherwise, but the
corner locus of a piecewise smooth function generally has smooth weights,
and derivatives of those weights contribute to the differential of its
integration current.

The earlier proof that the corner locus is balanced incorrectly treated the
facewise-Hessian current as separately \(\dprime\)-closed.  Smooth
facewise coefficients can contribute derivative terms, so that argument was
invalid.  Balancing is now imported at the correct source boundary from
GK17, Proposition 1.12.  The current identity itself remains the tropical
Poincare--Lelong formula of GK17, Corollary 3.19.

The delta-preform algebra proof is likewise marked as an imported
construction from GK17, Sections 1--3.  The manuscript records the
proper-intersection formula and the essential pullback restriction without
presenting the independence of fan displacement and the full smooth-weight
Leibniz calculus as a short self-contained proof.

### Chapter 19: curves, Wanner, and fixed skeleta

Several statements had silently changed Wanner's current-positive meaning of
``psh'' into the manuscript's approximation-generated CLD hierarchy.  The
comparison theorem now states only

\[
 \dprimeddprime[u]\geq0
 \quad\Longleftrightarrow\quad
 u\text{ is Thuillier-subharmonic}
\]

for continuous \(u\) under Wanner's hypotheses, followed by the valid
consequence CLD-psh \(\Rightarrow\) Thuillier-subharmonic.  The converse into
the CLD hierarchy is asserted only under the supplementary hypotheses of
Wanner's monotone CLD-smooth regularization result.  The former multi-step
argument purporting to prove the stronger equivalence was removed and
replaced by an explicit source boundary.

The chapter also no longer says that an arbitrary subharmonic function on a
disc is determined by boundary data or factors through one fixed skeleton.
Slope inequalities at finitely many vertices and the graph-Laplacian formula
are confined to model or piecewise-affine skeletal functions.  In the
projective-line example, Wanner supplies current positivity; membership in
the manuscript's CLD hierarchy is supplied separately by the toric
approximation theorem.

### Post-audit ledger reconciliation

A book-wide terminology scan found that the old stronger wording survived in
the Chapter 18 transition paragraph, the Chapter 19 comparison ledger, the
Chapter 31 master table, and Appendix L even though the Chapter 19 theorem
itself had been corrected.  Those four summaries now make the same
distinction as the theorem: current positivity is equivalent to Thuillier
subharmonicity; approximation-generated CLD-psh implies that condition; the
reverse implication requires a separate CLD-smooth regularization input.
The Chapter 31 curve row is consequently one-way unless Wanner's
supplementary regularization hypotheses are imposed.

## Checks

- Two full `pdflatex` passes of `book.tex` completed successfully in an
  isolated output directory.  The second pass produced a 3059-page PDF with
  no undefined citation or cross-reference warning; only the ordinary
  request for another label-stabilization pass remained.
- No duplicate Part II labels were found.
- No raw `\\ref` or `\\autoref` occurs in Part II; references remain through
  `\\cref`, `\\Cref`, and `\\eqref`.
- No exercise environment or exercise section occurs in Part II.
- No forbidden source identifier occurs in Part II or this report.
- Focused scans found no use of `\\mathrm{i}`, `\\mathrm{e}`, or
  `\\operatorname{d}` in place of the manuscript's established
  `\\rmi`, `\\rme`, and `\\rd` conventions.

## Residual provenance and scope risks

1. The long GJR26 survey blocks cite many individual propositions beyond the
   balancing theorem.  The central theorem and several numbered statements
   were spot-checked against the published version, but any future
   renumbering of that source should trigger a mechanical citation-number
   audit of Chapters 18--19.
2. The global delta-form product and positivity theorems are now clearly
   source-boundary imports.  Their explanatory paragraphs are not substitutes
   for GK17 and GK19 when one needs the full independence, descent, or
   functoriality proofs.
3. The BGJKK25 toric existence statements have deliberately retained their
   invariant, compact toric hypotheses.  They should not be reused for
   non-invariant metrics, noncompact tropical toric spaces, or general CLD
   potentials without a new source.
4. Wanner19 closes the current-positive/Thuillier comparison on curves, not
   the general approximation-generated CLD hierarchy.  This distinction is
   now explicit but remains a dependency boundary for every later use of the
   phrase ``CLD-psh on a curve.''

## Later 24 August addendum: GJR cohomology question

The literal unrestricted isomorphism question in GJR Section 1.15 is now
closed negatively in Chapter 18.  The constant good-reduction elliptic curve
has trivial Raynaud torus and hence zero invariant source in bidegree
`(1,1)`, whereas GJR Theorem 1.14 gives a one-dimensional weakly smooth
cohomology target.  The exact current proposition and source-aware proof
context passed production Rethlas run `20260824T123617Z_fcddc3abc33d` with
`gpt-5.6-sol` at `xhigh`, final `correct`, zero critical errors, and zero
gaps.  The source check used the published Theorem 1.14 and Section 1.15 and
the standard good-reduction extreme of Raynaud uniformization.  The result is
a direct source synthesis, carries no priority claim, and does not decide the
totally degenerate restriction.

## Later 24 August addendum: semipositive integral decomposition

Chapter 18 now proves the natural positive-cone form of the GJR integral-
decomposition question at every point of residual dimension at most one.  It
includes every good strict analytic curve, permits boundary points, and
requires neither algebraic closedness nor a relation between the coefficient
group and the value group.  The proof passes to a common residue model, uses
degree as the sole nef inequality on a proper residual curve, and splits the
primitive integral degree functional; all but at most one integral summand
are harmonic.  The exact live statement and adjacent proof passed production
run `20260824T135721Z_81346238f7dd` with `gpt-5.6-sol` at `xhigh`, final
`correct`, zero critical errors, and zero gaps.  Arbitrary residual dimension
remains open because the nef cone need not be one rational half-space.  This
is recorded as a dated book-level derivation without a novelty or priority
claim.  This final sentence records the 24 August status and is superseded
as of 25 August: signed generation by semipositive integral germs holds in
every residual dimension, while the natural nonnegative-coefficient
assertion fails in residual dimension two on a constant good-reduction
abelian surface.  The exact frozen blocks passed production runs
`20260825T130036Z_c1607c25ec38` and
`20260825T130707Z_4c4a1f2c885f`, both with `gpt-5.6-sol` at `xhigh`, final
`correct`, zero critical errors, and zero gaps.  P09.1 is retired, and no
novelty or priority claim is made.

## Later 25 August addendum: canonical cubical delta-metricity

Chapter 19 now includes the exact source-derived reduction theorem verified
in production run `20260825T145229Z_b37e13478cc7`, item
`pi_10f6228b6e69e780dad8b17b`.  It proves ordinary GK delta-metricity for
all cubical metrics on `Pic^0(A)`, the exact induced
symmetric/antisymmetric square splitting, and equivalence of the universal
fixed-abelian-variety question with the ample symmetric case.  The run used
`gpt-5.6-sol` at `xhigh` and returned final `correct`, zero critical errors,
and zero gaps.  Good, totally degenerate, and isotrivial residual-extension
cases remain separately recorded.  The result does not close P09.2: the
ample symmetric non-isotrivial mixed-reduction range remains open.  No
novelty or priority claim is made.

## Later 26 August addendum: the four layers of a delta-metric

The former Chapter 18 gluing lemma incorrectly treated the global
piecewise-smooth Chern form, the residual codimension-one generalized
delta-form, the ambient codimension-zero Hessian lift, and the ambient
bidegree after intersection with a tropical cycle as one assertion.  The
replacement states and proves these four layers separately from the exact
GK17 sources.  In particular, Proposition 9.8 uniqueness is used only with
its universal algebraic-pullback characterization, and the degree
calculation is made on an ambient neighbourhood whose tropical-cycle
intersection lies inside the chosen chart domain.

The first exact production submission was rejected for omitting precisely
those two quantifiers.  After their repair, the frozen statement and
source-aware proof passed run 20260826T011701Z_1e7c96932016, item
pi_a860454e8a0004aa4767207c, with gpt-5.6-sol at xhigh, final
correct, zero critical errors, and zero gaps.  Chapter 18 inputs the
verified files directly.  This is a correctness repair and source
reconstruction, not a new theorem or priority claim.
