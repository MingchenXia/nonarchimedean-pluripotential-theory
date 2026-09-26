# P05.1 one-dimensional literal regularity classification: audit

Date: 26 September 2026

## Claim audited

Let `X` be a one-dimensional balanced rational polyhedral space with finite
structure and let `gamma` be a literal integral-slope polyhedrally convex
reference positive at infinity.  Then literal regularity holds exactly when
`deg(gamma)=0`, equivalently exactly when `X` is compact.

The positive-degree obstruction uses

```text
phi = max(gamma,C),
P   = (1-1/N)gamma + (1/N)phi.
```

An edgewise integral-slope concave roof over `(phi-gamma)/N` is a bounded
literal obstacle whose exact envelope is `P`.  A nonintegral slope of `P` on
one bounded cell gives a uniform positive separation from every literal
convex piecewise-affine function.

## Mathematical audit

1. A rational constant is a literal affine convex function, and a finite
   maximum preserves every polyhedral Jensen inequality.  Thus
   `phi=max(gamma,C)` is literal and convex.
2. Positivity at infinity makes `gamma` tend to `+infinity` on each
   unbounded end.  Hence `phi=gamma` on every sufficiently remote tail and
   `phi-gamma` is bounded.  Integral slopes and rational affine constants
   make all nontrivial crossing points with `C` rational.
3. Choosing `C>gamma(v)` in a noncompact component makes `phi-gamma`
   nonconstant.  Since it vanishes on the unbounded tails, some bounded
   rational edge cell has a nonzero integral slope `k`.
4. On an oriented cell, a rational affine slope `r` is the average of the
   consecutive integers `floor(r)+1` and `floor(r)`.  Placing the larger
   slope first produces a concave integral-slope roof with the same endpoint
   values as the affine chord.  Rationality of the cell length and of `r`
   makes the new breakpoint rational.  The construction also covers
   negative `r`; if `r` is integral, the chord itself is already literal.
5. The roofs glue because their endpoint values are prescribed by the same
   global function.  They vanish on the chosen unbounded cells, so the
   resulting obstacle is bounded and literal.
6. The rational convex combination `P` is a convex envelope competitor under
   the roof.  Every other competitor is bounded by `P` at every subdivision
   vertex.  Ordinary convexity on each bounded edge then bounds it by the
   endpoint chord, which is exactly `P`; on unbounded cells the obstacle
   already equals `P`.  This proves the exact envelope identity.
7. On the selected cell, the slope is an integer plus `k/N`.  Taking
   `N>|k|` makes it nonintegral.  At the midpoint, the left derivative of any
   literal convex approximant is an integer.  The two alternatives relative
   to the floor and ceiling of the target slope give the stated lower bound
   `L*dist(q,Z)/4`.
8. The separation excludes every uniform literal regularization, hence also
   every decreasing one.  The earlier zero-degree theorem supplies the
   converse and the equivalence with compactness.

## Exceptional cases and scope

- If the noncompact component initially has no vertex, inserting a rational
  point gives a finite refinement and does not change the space or the
  regularity question.
- Disconnected spaces cause no issue: the construction is nonconstant on one
  noncompact component and remains bounded on all other components.
- No dimension, extremality, or face hypothesis on a local balancing-relation
  cone is used.
- The theorem is one-dimensional.  Higher-dimensional literal and real-PA
  classifications, nonseparable product obstacles, and the source
  coefficient-convention repair remain open.

No model-verifier result is claimed for this packet.

## Result

The statement, proof, rationality assertions, envelope maximality,
separation estimate, and boundary description pass the automatic second
audit.  P05.1 remains active only because of its higher-dimensional and
source-convention scopes.  The inventory remains 42 atoms in 12 formal
problem environments, with tiers `(0,3,7,15,17)`.
