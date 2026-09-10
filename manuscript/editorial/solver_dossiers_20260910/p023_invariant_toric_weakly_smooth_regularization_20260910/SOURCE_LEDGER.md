# P02.3 invariant split-toric weakly smooth regularization — source ledger

Status: source-scoped positive companion result.  It applies only to finite
continuous maximal-compact-torus-invariant current-psh functions on an
ordinary open set compactly contained in one ordinary open convex tropical chamber of a split
torus.  It does not identify arbitrary classically psh functions with this
class and does not retire P02.3.

## Claim-to-source map

| Step | Source / direct argument | Scope control |
| --- | --- | --- |
| Decreasing ordinary CLD-smooth psh sequence | `cor:p024-invariant-toric-cld-smooth-regularization` and its source ledger | This imports its finite, continuous, invariant, dense-torus and relatively compact ordinary-open hypotheses without enlargement. |
| Ordinary CLD-smooth forms are weakly smooth | Gubler--Jell--Rabinoff, Proposition 10.14 | This is an inclusion of differential-form sheaves; it supplies the regularity word ``weakly smooth''. |
| Psh is the same current-positivity assertion | Gubler--Jell--Rabinoff, Section 7.13 | The proof does not compare distinct positivity cones: it retains the positive CLD Hessian current already proved in P02.4. |

Primary source for the inclusion and the psh convention: W. Gubler, P. Jell,
and J. Rabinoff, *Forms on Berkovich spaces based on harmonic
tropicalizations*, *Bull. Soc. Math. France* **154** (2026), 135--238,
doi:10.24033/bsmf.2919.

https://gubler.app.uni-regensburg.de/Publikationen/2111.05741v2.pdf

## Deliberate boundaries

1. This is a consequence of the P02.4 sequence; it neither produces a new
   regularization mechanism nor weakens any of P02.4's hypotheses.
2. It does not claim a local-Fubini--Study approximation, a semipositive
   real-PL approximation, or an assertion for arbitrary noninvariant psh
   functions.
3. It uses the CLD-current definition of psh already used in P02.4.  It does
   not assert a separate strong-current or weak-form positivity comparison.
