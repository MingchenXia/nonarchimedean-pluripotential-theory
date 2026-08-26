# P09.2 product--Gauss candidate: novelty and natural-framework audit

Date: 26 August 2026

This is an isolated editorial audit.  It makes no novelty or priority claim
and does not promote the candidate before production Rethlas verification.

## Literature separation

The controlling published source is Gubler--Jell--Rabinoff, *Forms on
Berkovich spaces based on harmonic tropicalizations*, Remark 16.4.  It
retracts the old use of smoothness in Gubler--K\"unnemann, Example 8.15 and
Example 9.17, and explicitly leaves ordinary delta-metricity of canonical
metrics on abelian varieties open.  Section 17 supplies a non-smooth
canonical tropicalization in mixed reduction.

Chambert-Loir--Ducros, arXiv:1204.6277v2 (25 July 2025), supplies three
ingredients but does not state the candidate conclusion: Remark 19.2.3
identifies smoothness of all Raynaud tropical coordinates with isotriviality
of the residual extension; Proposition 19.2.5 gives the exact quadratic
metric-weight formula; Theorem B.6.4 gives positive definiteness of the
Raynaud quadratic form for an ample line bundle.

Searches performed on 26 August 2026 included the exact phrases
`canonical metrics delta-metrics abelian varieties`, `ordinary
delta-metric`, `isotrivial delta-metric Raynaud`, and combinations of
`cubical metric`, `harmonic tropicalization`, and `product Gauss`, restricted
where possible to arXiv and journal sites.  They recovered the old GK claim,
the GJR correction/open question, the CLD-v2 structure theory, and work on
toric metrics and canonical measures, but no later primary source settling
the ordinary delta-metric question or stating the product--Gauss criterion.

The correct editorial classification, if the proof is verified, is therefore
`new candidate theorem resolving a published open question`.  The book will
make no priority claim without external expert confirmation.

## Natural-framework test

- Smoothness, normality, properness, projectivity, and characteristic-zero
  assumptions on the abstract algebraic variety are not used.  The frozen
  statement therefore allows an arbitrary algebraic variety over the stated
  field.  The proof is local in the analytic topology.
- Algebraic closedness and nontriviality of the valuation are used
  substantially: the value group is nonzero, divisible, and dense, the
  residue field is infinite, and every chosen rational polyradius is realized
  by a (K)-point.  The proof does not claim the same result over a general
  ground field or in the trivially valued case.
- Splitness of the torus is used to adjoin a character basis and to obtain
  the product Gauss directions.  In the Raynaud application the algebraically
  closed setup is split.  CLD \S B.5.14 warns that the nonsplit quotient map
  need not be a local analytic isomorphism.
- Local integral piecewise affinity of (h) is the exact scope in which the
  cited finite-moment factorization and algebraization are applied.  No
  unproved extension to arbitrary real-PL or merely harmonic maps is made.
- Symmetry and nondegeneracy of the quadratic Hessian are essential to the
  contraction.  If the Hessian is degenerate, only coordinates in the image
  of (b^\sharp) can be recovered; an undetected nonsmooth PL coordinate may
  be added in a null direction.  Ampleness makes the Raynaud polarization
  positive definite and hence supplies the required nondegeneracy.
- Symmetry of the line bundle is not used.  CLD Proposition 19.2.5 and
  Theorem B.6.4 apply to every ample rigidified line bundle, so the Raynaud
  conclusion is stated in that generality.  The ample symmetric case in the
  published open question is an immediate subcase.
- Every cubical metric on a fixed line bundle is a positive constant multiple
  of the normalized one by CLD \S19.1.  Since a constant weight is smooth,
  all cubical metrics have the same ordinary delta-metricity status.

## Failed routes kept separate

The earlier Hessian-only candidate incorrectly treated arbitrary
piecewise-smooth forms on a tropical support as full-ambient codimension-zero
GK delta-preforms.  The earlier residue candidate also lacked a proof that a
one-point Gauss residue equals the global residual Raynaud line bundle.  Both
routes are retracted.  The product--Gauss proof uses neither assertion: it
obtains torus lineality by pulling back along the algebraic action and returns
to the original germ through a genuine constant algebraic section.
