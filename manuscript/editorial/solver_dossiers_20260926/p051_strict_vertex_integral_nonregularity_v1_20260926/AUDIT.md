# P05.1 strict-vertex integral nonregularity: audit

Date: 26 September 2026

## Claim audited

For a vertex `v` of a finite one-dimensional balanced rational polyhedral
space, let `K_v` be the cone of nonnegative balancing relations.  If the
outgoing slope vector of a literal integral-slope reference `gamma` is
strictly positive on `K_v \ {0}`, then a bounded literal obstacle has the
exact envelope

```text
gamma(x_e(t)) + (R-t)/N   for 0 <= t <= R,
gamma                     off the closed star.
```

Every literal integral-slope convex piecewise-affine approximant stays at
uniform distance at least `(N-1)R/(2N^2)` from this envelope.  Consequently
the pair is not regular in the literal coefficient category.

If every local relation cone is one-dimensional and `gamma` has positive
degree, some vertex has positive polyhedral Monge--Ampere mass.  Its local
slope vector is strictly positive on the unique relation ray, so the theorem
applies.

## Proof audit

1. The normalized slice of `K_v` is nonempty and compact.  Strict positivity
   has a positive minimum there, so all sufficiently large integers `N`
   preserve nonnegativity after subtracting `1/N` from every outgoing slope.
2. The obstacle is continuous at the centre and outer boundary of the star,
   has only integral slopes `0` and `-1`, and has rational breakpoints.
3. The proposed envelope satisfies the local relation inequalities at `v`.
   At each outer endpoint its slope increases from `s_e-1/N` to `s_e`; all
   other local inequalities are inherited from `gamma`.
4. The proposed envelope lies below the obstacle.  Conversely every
   competitor is bounded on each star segment by the chord through its two
   endpoint bounds, and that chord is exactly the proposed envelope.
5. At `t=R/N`, the left derivative of every literal approximant is an
   integer.  The alternatives `m <= s_e-1` and `m >= s_e` force an error
   difference of magnitude at least `(N-1)R/N^2`, hence a uniform error of
   at least half that amount.
6. In the rank-one corollary, positive total degree supplies a vertex of
   positive mass.  Since `K_v` is a single nonnegative ray, positive mass is
   exactly the strict inequality required by the theorem.

## Boundary audit

The result does not classify all literal graph pairs.  It leaves open the
zero-degree case.  For positive-degree references, any remaining case must
have a higher-rank local relation cone and place the reference slope vector
on a proper face of the dual cone at every positive-mass vertex.  The result
also does not affect the book's positive real-piecewise-affine regularity and
orthogonality theorems, which use a different coefficient category.

The author-supplied PDF is the withdrawn positive draft already recorded in
the repository: 252,482 bytes, SHA-256
`0ad51074108eb2202d4b624637c035610d275c67fd8456dab59282d543d5f5fb`.
Its positive theorem is neither cited nor restored.  The present theorem is
a book-local consequence of the integral-versus-fractional slope conflict.

No model-verifier result is claimed for this packet.

## Result

The statement and proof pass the mathematical boundary audit.  They narrow
P05.1 but do not retire it; the active inventory remains 42 atoms in 12
formal problem environments, with tiers `(0,3,7,15,17)`.
