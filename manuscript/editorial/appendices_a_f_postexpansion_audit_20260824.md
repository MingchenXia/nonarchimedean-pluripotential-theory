# Appendices A--F post-expansion audit

Date: 24 August 2026

## Scope and verdict

This audit covers only:

- appendices/appA_valuation_algebra.tex;
- appendices/appB_birational_geometry.tex;
- appendices/appC_ideals.tex;
- appendices/appD_convexity.tex;
- appendices/appE_nets.tex;
- appendices/appF_intersection_bdivisors.tex.

Appendix J was outside this audit.  Its recent normalization work was used
only as a convention checkpoint.  No source file outside Appendices A--F
was changed.

**Verdict.**  The six appendices are mathematically usable after the
corrections recorded below.  The principal defects were a normalized-Rees
formula stated without normality of the base, ambiguity about projectivity
in the alteration/Stein ledger, unqualified zero indices in asymptotic ideal
limits, a globally over-scoped dualizing-sheaf presentation of test ideals,
a subnet definition contradicting the frontmatter convention, and an
insufficient firewall between absolute Dang--Favre intersections and
relative DVR model intersections.  These were corrected without adding a
new theorem.  Labels, equation numbers, references, and the notation
commands for differentials and exponentials were preserved.

All 77 theorem, proposition, lemma, and corollary environments in the six
files have proof environments.  Appendix C has one additional proof block
attached to the stabilization assertion in a definition.  No exercise and
no optionally named theorem-like environment occurs.

## Primary-source and dependency checks

The audit compared the imported boundaries with the following primary
sources, in addition to the classical books already cited in the text.

- The Stacks Project statements used for finite normalization,
  subintegrality, universal homeomorphisms, admissible blowups, flattening,
  finite locally free modules, Stein factorization, and normality were
  checked at Tags 035S, 0CND, 0EUH, 04DF, 081T, 0815, 02K9, 03H0, and
  035L.  In particular, the hypotheses in the flattening statement agree
  with [Tag 0815](https://stacks.math.columbia.edu/tag/0815).
- De Jong, Theorem 4.1, was checked in the published paper
  [Smoothness, semi-stability and alterations](https://www.numdam.org/item/PMIHES_1996__83__51_0/).
  The theorem gives a regular projective compactification of the alteration
  source.  Properness of the alteration and the graph argument supply the
  projectivity of the morphism; absolute projectivity of the source requires
  the target to be projective.
- Mustata, [The non-nef locus in positive characteristic](https://arxiv.org/abs/1109.3825),
  was checked in source form.  Its graded-sequence order is explicitly a
  limit through indices for which the ideal is nonzero, and its test-ideal
  construction is the stabilized increasing family of Frobenius roots.
- Dang--Favre, [Intersection theory of nef b-divisor classes](https://arxiv.org/abs/2007.04549),
  Theorem 2.1, Proposition--Definition 3.1, and Theorem 3.2 were checked
  against arXiv version 2 and the published scope.  They concern absolute
  smooth projective characteristic-zero models, decreasing nets of nef
  Cartier b-classes, and the top-degree product with exactly dim X divisor
  entries.
- Berndtsson, [Superforms, supercurrents and convex geometry](https://arxiv.org/abs/2501.02896),
  version 3 of 6 August 2026, was checked at Theorems 4.2, 12.3, and 13.3.
  The wedge-product normalization, Lorentzian signature, and
  kernel/solvability input used in Appendix D match the cited statements.

The excluded paper [Deligne--Riemann--Roch Theorems I,
arXiv:1710.09731](https://arxiv.org/abs/1710.09731) is neither cited nor
used in Appendices A--F.  A text and bibliography-key scan found no direct
occurrence.  The imported parts of Dang--Favre and Berndtsson do not depend
on that Deligne--Riemann--Roch paper.  Dang--Favre cites work denoted
Xia17 by Jian Xiao on cone duality; this is a different author and paper.
Berndtsson's current bibliography mentions later b-divisor work, but the
three self-contained results imported here do not invoke arXiv:1710.09731.
No indirect dependency on the excluded source was found.

No change below promotes a new result or requires a new Rethlas receipt.
The edits either restrict a statement to its established domain, complete
an elementary proof, or expose an already cited foundational input.

## Exact source corrections

### Appendix A: valuations, Rees algebras, and normalization

At lines 260--280, the normalized-Rees formula now assumes that A is
normal.  The normalization is described inside K(T), with graded pieces
given by the integral closures of the powers of the ideal.  The text now
records that on a nonnormal base the degree-zero part is the normalization
of A, so the displayed relative Proj over X is not asserted there.  The
later Rees-valuation theorem already assumes a normal base.

The valuative criterion, Rees-valuation reduction, conductor square,
subintegrality/seminormality distinctions, determinant norm, and
Roberts--Singh input were otherwise consistent with their stated
hypotheses.  In particular, the text does not replace integral closure by
an arbitrary saturation and does not take determinant norms before finite
flatness.

### Appendix B: birational geometry and alterations

At lines 386--399, the de Jong import now explains the projectivity
deduction precisely.  The graph in the product of a projective
compactification with X is a locally closed immersion, is proper over X,
and hence is closed.  If X is projective, the alteration source is proper
over the ground field; its open immersion into the regular projective
compactification is then also closed.

At lines 414--439, the Stein ledger no longer calls the intermediate
variety absolutely projective without assuming that X is projective.
It now states that T is normal and integral, that T is projective over the
ground field when X is, and separately that the finite map to X and the
birational map from Y are projective.

The root correction distinguishing relative from absolute Frobenius was
preserved.  The example correctly uses the relative Frobenius
from X to its Frobenius twist as the k-morphism of degree p to the power n,
while warning that the absolute Frobenius need not be a k-morphism.
The flattening hypotheses agree with Stacks Tag 0815, and the text does not
claim that flattening makes the original finite morphism flat.

### Appendix C: multiplier ideals and test ideals

At lines 264--276, the asymptotic valuation limit is now explicitly taken
through nonzero terms.  At lines 280--298 and 445--459, both asymptotic
multiplier ideals and asymptotic test ideals likewise restrict their
maxima and stabilization indices to nonzero terms.  This matches the
source convention that a nonzero graded sequence need only have some
nonzero term.

At lines 410--443, generalized test ideals are now defined locally by the
stabilized increasing Frobenius-root ideals.  The trace formula is stated
only when an invertible dualizing sheaf is available.  This removes the
unsupported global assumption that every regular F-finite scheme in the
initial scope carries a selected invertible dualizing sheaf, while
retaining the trace formulation for the actual schemes
X times the affine line used later.

At lines 512--528, the fixed-twist proposition now identifies the line
bundle L producing the graded base ideals and says explicitly that L, H,
and A are pulled back to the product scheme.  The imported
Castelnuovo--Mumford argument and its bounded residual coefficient are
unchanged.

The analytic/algebraic normalization, strict valuative multiplier
criterion, Skoda threshold, asymptotic subadditivity, Canton discrepancy
bound, and Hara--Yoshida reduction scope were checked.  No
characteristic-free identity between multiplier ideals and test ideals is
asserted.

### Appendix D: convexity, factorials, and mixed volumes

At lines 101--110, Fenchel's inequality is now stated under properness of
the convex function.  This prevents the forbidden expression positive
infinity plus negative infinity for the identically infinite function and
aligns the hypothesis with the equality criterion.

The remainder of Appendix D required no mathematical correction.  The
Minkowski polynomial has coefficient n factorial divided by the
multi-index factorial; Alexandrov Monge--Ampere measure has no extra
n factorial; and the Lagerberg support-current formula places one over
n factorial in front of the n-fold wedge product.  The equal-body and
coefficient-polarization tests agree.  The Alexandrov--Fenchel proof uses
only the cited finite-dimensional Lorentzian input, and the zero-mass
warnings prevent an illicit probability normalization.

### Appendix E: nets and compact upper-envelope calculus

At lines 64--84, a Willard subnet now has an order-preserving indexing map
that is eventually in every tail.  This exactly matches the global
frontmatter convention.  The map need not be injective.  The
order-preserving Moore--Smith terminology is explicitly treated as the
same convention in this book.

At lines 87--98 and 607--616, inheritance of a given limit by a subnet is
separated from uniqueness of limits; uniqueness requires a Hausdorff
space.  At lines 132--150, the divergence-subnet proof now constructs the
directed set of pairs explicitly and verifies that its indexing map is
order preserving and tail cofinal.

The cluster-subnet construction already produces an order-preserving map.
Compactness, Dini's theorem for decreasing nets, Choquet selection,
semicontinuous monotone integration, the measurable-net counterexample,
weak compactness of probability measures, and the extended-real min--max
ledger were checked with the net scopes left intact.  No sequential
convergence theorem is silently applied to an arbitrary net.

### Appendix F: intersection theory and b-divisors

At lines 50--74, nonnegativity of mixed nef intersections on a merely
proper variety is now justified by Chow's lemma: pull back to a projective
birational model, use the degree formula, and approximate there by ample
classes.

At lines 258--272, the non-Cartier Weil b-divisor example now proves
failure of finite determination even when a newly introduced exceptional
coefficient might accidentally agree with pullback along the designated
chain.  Blowing up a general point away from that chain creates a prime on
which the assigned coefficient and the pullback coefficient differ.

At lines 344--366, nefness on a Cartier determination is proved to ascend
and descend under a projective birational morphism.  The descent argument
uses a curve upstairs mapping generically finitely onto each curve
downstairs.  This completes the claimed independence of the chosen
determination.

At lines 510--524, the Dang--Favre theorem is now separated sharply from
the relative model theory.  On an absolute n-dimensional projective
variety its product has exactly n entries and does not define an absolute
self-intersection with n+1 factors.  The n+1-fold model intersections used
over a discrete valuation ring contain an actual vertical divisor factor,
such as a vertical divisor intersected with n model line bundles.  They
are not obtained by appending a formal copy of an absolute b-class.

The one-Weil-factor product is still defined only because all remaining
intersection operators are Cartier.  No product of two arbitrary Weil
b-divisors is introduced.  Dang--Favre upper semicontinuity is stated only
on its nef b-class domain, and decreasing continuity is a net statement in
the projective-limit topology.

## Convention and structural checks

- Existing labels and equation tags A.1--A.11, B.1--B.7, C.1--C.30,
  D.1--D.30, E.1--E.13, and F.1--F.17 were preserved.
- Cross-references introduced by the corrections resolve in the focused
  build.
- No use of the differential macros was rewritten.  The manuscript's
  \rd, \rmi, and \rme conventions remain in place.
- A scan found no unsupported absolute n+1 power outside the new
  prohibition in Appendix F.  The only other n+1 occurrence is the
  Castelnuovo--Mumford positivity bound d at least n+1 in Appendix C.
- No direct or indirect use of arXiv:1710.09731 was found in the audited
  source chain.

## Compilation

The existing driver tmp/pdfs/appendices_audit_slice.tex was compiled from
the manuscript directory with all generated files staged under
/tmp/appendices_a_f_postexpansion_build.  The final build ran pdfLaTeX,
BibTeX, and two further pdfLaTeX passes.  It produced a 212-page PDF.

Final-log checks found:

- no LaTeX error or undefined control sequence;
- no undefined citation or cross-reference;
- no duplicate label or duplicate PDF destination;
- no overfull box.

The compiled text of every edited passage was also inspected through PDF
text extraction, including the normalized-Rees hypothesis, relative
Frobenius example, nonzero-index limits, Frobenius-root definition,
Fenchel properness, subnet convention, and absolute/relative intersection
firewall.

## Residual risks

No known correctness defect remains in Appendices A--F.

Two source-maintenance risks remain visible rather than hidden:

1. The Berndtsson supercurrent input is a current arXiv preprint.  The
   cited theorem numbers and normalization match version 3 dated
   6 August 2026; a later version should be rechecked before publication.
2. The fixed-twist result in Appendix C transparently imports and sketches
   the main-text proposition rather than duplicating its complete
   Castelnuovo--Mumford proof.  This is a documented proof boundary, not an
   unsupported theorem, but a fully standalone appendix would require
   duplicating that main-text argument.

Neither risk involves the excluded Deligne--Riemann--Roch paper or an
unreceipted new claim.
