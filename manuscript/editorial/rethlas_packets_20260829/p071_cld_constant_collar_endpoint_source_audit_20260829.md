# P07.1 primary-source scope audit

Status: source map for an isolated candidate; not a verification receipt.

## Primary source

Antoine Chambert--Loir and Antoine Ducros, *Formes differentielles reelles et
courants sur les espaces de Berkovich*, arXiv:1204.6277v2 (25 July 2025).

- Example 6.7.2, printed pages 151--152, equips an interval with a tropical
  structure in which parlinear functions are constant near each boundary
  endpoint.  On a connected domain meeting such an endpoint, every affine
  function is constant.  At a finite endpoint this gives, in the ordinary
  inward real coordinate on the finite stratum, extended topologically to
  the endpoint, precisely ordinary smooth profiles which are constant on
  some endpoint collar.  The coordinate is not a nonconstant affine chart
  through the endpoint.
- Sections 6.1.1 and 6.1.6 make tropical charts affine and their scalar
  coordinate functions affine.  Hence every such coordinate is constant
  after shrinking to a connected neighbourhood of the endpoint.
- Definition 6.2.1 constructs smooth forms from smooth coefficients in
  tropical charts.  In bidegree `(0,0)`, the preceding constant-chart fact and
  the ordinary interior chart give the claimed smooth-function description.
- Definition 8.1.1 defines the psh sheaf as the smallest subsheaf containing
  smooth functions with positive `d'd''` and stable under decreasing
  sequences.
- Lemma 8.1.4 gives the transfinite filtration and identifies its eventual
  value with that generated sheaf.
- Lemma 8.1.10 is the uniform-to-monotone subsequence device used after the
  fixed-domain regularization.

The exact source text used for this audit is preserved locally in
`/private/tmp/cld25_source/esptrop.tex`,
`/private/tmp/cld25_source/espgtrop.tex`, and
`/private/tmp/cld25_source/bt-trop.tex`; the corresponding extracted PDF text
is `/private/tmp/p21_bridge_sources/cld25.txt`.

## Derived, not imported

The source does not state the candidate first-stage collapse.  The following
parts are book-level deductions and therefore require full proof and exact
Rethlas verification:

- the endpoint-minimum characterization;
- stability and sheaf locality of the comparison class;
- the extended-real component dichotomy;
- the buffered regularized-maximum construction producing an exact collar;
- the fixed-neighbourhood decreasing approximation and the resulting collapse
  of the hierarchy in this model.

## Excluded sources and false shortcuts

- The verified finite-star theorem uses an ambient-induced smooth structure;
  a homeomorphism to a ray does not identify it with the constant-collar
  structure.
- The regularization theorem on standard tropical toric partial
  compactifications does not identify the Example 6.7.2 affine sheaf with the
  standard toric one.
- Piecewise-affine regularity and weakly smooth curve regularization do not by
  themselves produce ordinary CLD-smooth profiles which are exactly constant
  on an endpoint collar.
