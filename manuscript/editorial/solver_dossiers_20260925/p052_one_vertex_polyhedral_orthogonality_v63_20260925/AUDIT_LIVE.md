# Mathematical and source audit

Date: 25 September 2026.
Baseline: `4ab75e05a227b8a85ca478861562c43410bb0628`.

The original three-page author-supplied PDF was read in full.  It was later
superseded by the explicitly withdrawn replacement now preserved byte for
byte, SHA-256
`0ad51074108eb2202d4b624637c035610d275c67fd8456dab59282d543d5f5fb`.
The corresponding BMPS v1 PDF was checked directly at Definition 2.28,
Definitions 3.2--3.3, Proposition 6.13, Definition 6.15, Proposition 6.17
and Definition 6.9.

## Convention repair

BMPS Definition 2.28 says that a piecewise-affine function has integral
linear parts and rational constants.  Later arguments treat the same spaces
as real vector spaces, and Proposition 6.13 asserts envelope closure.  These
claims cannot all hold literally.  On `X=R`, with `gamma=|x|` and the bounded
integral-piecewise-affine obstacle

```text
u(x)=0          for x<=1,
u(x)=1-x        for 1<=x<=2,
u(x)=-1         for x>=2,
```

the envelope has slopes `-1`, `1/2`, and `1`.  The chord joining `(0,0)` to
`(2,1)` proves maximality.  Thus the integral-slope class is not closed under
the asserted envelope operation.

The live theorem now defines `PA_R` as the real scalar extension on a finite
rational polyhedral structure and defines the one-dimensional real
Monge--Ampere measure as the weighted Laplacian.  It classifies this repaired
category and does not claim to repair the literal integral-slope formulation.

## Proof audit

The local convexity lemma uses the incident-face condition in the definition
of a polyhedral convex combination.  Primitive ray generators fix the
integral-affine normalization in the vertex-mass formula.  A positive
balancing vector lies in the relative interior of the relation cone, so its
dimension is `r-rank(span{u_i})`.

In the rank-one case, the one-dimensional real-affine envelope is supported
on a finite subdivision.  At an interior noncontact atom, raising the vertex
and interpolating preserves the two slope inequalities.  At the fan vertex,
the new slopes are `s_i-delta/rho`; positivity of their weighted sum and
`K=R_{≥0}w` preserve polyhedral convexity.  Hence every positive mass is
on the contact set.

When the relation cone has higher dimension, an extreme relation has proper
support.  The explicit function with a delayed bend on that support is the
exact envelope of its bumped obstacle.  Its vertex mass is positive while
the bump is one at the origin and zero at every other positive atom, so the
orthogonality integral is strictly negative.  Bounded reference shift gives
the arbitrary finite real-piecewise-affine positive reference.  The
nonsaturated tripod confirms that lattice saturation is unnecessary in this
repaired category.

The archived dependency-closed statement and proof passed the local
gpt-6-astra/xhigh verifier with verdict `correct`, zero critical errors and
zero gaps.  The two earlier negative responses are preserved because they
caused the primitive normalization, full definitions and integral/real
convention repair.  The later withdrawal edit to the live preamble is not
covered by that exact-byte receipt, and no new verifier result is claimed.

P05.2 remains active.  Later book-local arguments classify real-PA
orthogonality on finite graphs; the literal source convention and
higher-dimensional singular fans are not classified.  The active inventory
remains 42 atoms in 12 formal problem environments, with tiers
`(0,3,7,15,17)`.
