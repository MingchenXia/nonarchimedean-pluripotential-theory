# P21.3 upstairs cross: four-punctured smooth-curve obstruction

## Verdict

The proposed smooth connected curve is a valid realization of the *unit*
cross and, unlike the earlier reducible nodal realization, it puts the two
curvature atoms at the same analytic point.  It therefore passes the
potential side of the test:

\[
X=(\mathbf P^1_K\setminus\{a,b,c,d\})^{\mathrm{an}},\qquad
\mathrm d'\mathrm d''[2|s|]
=\mathrm d'\mathrm d''[|s|+|t|]=4\delta_q.
\]

It fails exactly on the current side.  No positive closed intrinsic
top-dimensional analytic current, and no delta-current with the same
visible CLD weights, can give horizontal weights two and vertical weights
one.  The obstruction is exposed by one mandatory chart refinement.

This is a complete negative theorem for the concrete candidate, not a
solution of the unrestricted residual problem.

## Construction and exact calculation

Assume that the reductions of `a,b,c,d` are pairwise distinct and set

\[
f=\frac{z-a}{z-b},\qquad g=\frac{z-c}{z-d},\qquad
(s,t)=(-\log|f|,-\log|g|).
\]

The four puncture directions at the Gauss point map to
`e1,-e1,e2,-e2`, with unit primitive indices and unit fundamental weights.
Both coordinates are constant off the four-ended skeleton.  Hence the
tropical image is the full cross.  The M\"obius coordinate `x=f` writes
`g=C(x-alpha)/(x-beta)`, so the image is a closed curve in the torus and the
tropicalization is proper.

The outgoing slope table at the single analytic vertex is

| potential | `a` | `b` | `c` | `d` | sum |
|---|---:|---:|---:|---:|---:|
| `U=2|s|` | 2 | 2 | 0 | 0 | 4 |
| `V=|s|+|t|` | 1 | 1 | 1 | 1 | 4 |
| `H=U-V` | 1 | 1 | -1 | -1 | 0 |

The punctures are absent from `X`, and the functions are affine or constant
everywhere else.  Thus the analytic and delta-current curvatures of `U` and
`V` are both exactly `4 delta_q`.  Ambient square-root regularizations give
decreasing smooth psh approximants, so this is an equality inside the actual
CLD psh category, not merely a graph-Laplacian slogan.

## Why the weighted current is illegal

The coarse cross hides a third slope coordinate.  Add the unit

\[
k=\frac{z-a}{z-c},\qquad r=-\log|k|.
\]

In the refined tropicalization `(s,t,r)`, the primitive rays become

\[
(1,0,1),\quad(-1,0,0),\quad(0,1,-1),\quad(0,-1,0).
\]

If a proper pushforward of a positive closed order-zero current has ray
weights `wa,wb,wc,wd`, closedness forces balancing in every refined chart:

\[
(w_a-w_b,\;w_c-w_d,\;w_a-w_c)=0.
\]

Therefore all four weights are equal.  The desired weights `(2,2,1,1)`
have refined defect `(0,0,1)`.  They balance only after forgetting the
`r`-coordinate, so the coarse fan current cannot be pulled back or promoted
to an intrinsic current on the smooth curve.

This proof uses only proper pushforward (transpose against target test
forms); it never invokes the nonexistent pullback of an arbitrary current.

## Delta-current legality

A positive closed delta-current restricts to a positive closed CLD current,
and restriction commutes with both differentials.  Smooth top-degree test
forms supported in ray interiors detect all four one-dimensional weights.
Consequently an invisible delta-current summand cannot repair the refined
balancing defect.

There is a separate wording issue in the live residual problem: multiplying
an arbitrary delta-current by an arbitrary *continuous* function is not part
of the delta-current module structure without an explicit order-zero
extension.  Multiplication is automatically legal here because `H` is real
PL, hence a degree-zero delta-form.  Future statements should either keep
that PL hypothesis, restrict to delta-currents induced by delta-forms, or
define the required continuous-coefficient extension.

## Rejected routes preserved

1. The earlier reducible curve
   `V((x-1)(y-1))^an` supports the analytic cycle
   `2[Y_h]+[Y_v]`, but its two Gauss points are distinct; curvature equality
   appears only after tropical pushforward.
2. The four-punctured smooth curve identifies the curvature vertex
   correctly, but the proposed unequal calibration fails after adjoining
   `(z-a)/(z-c)`.
3. Declaring the coarse cross weights balanced is insufficient: chart
   refinement is part of both the CLD and delta-form definitions.
4. Pulling the abstract weighted fan current back along the tropicalization
   is not legal; arbitrary currents have no such pullback.

No rejection artifact from the preceding production runs is superseded or
deleted by this dossier.

## Minimal remaining workaround

The exact cross-PL strategy cannot work on this smooth curve.  The smallest
plausible separated analytic loophole is now:

- analytic dimension at least two;
- a positive closed **CLD** current not already controlled by a delta-form
  module calculation; and
- a continuous distributionally pluriharmonic difference `H=U-V` for which
  no locally uniform smooth pluriharmonic approximation is available.

This is precisely the regularization gap left open in the CLD
Bedford--Taylor definition.  A higher-dimensional delta-current does not by
itself help when `H` is a delta-form and its delta curvature vanishes, since
the delta-form module and the Leibniz rule then force
`d'd''(H T)=0`.  A nonseparated or relative-boundary gluing could evade some
balancing hypotheses, but would require a new legal definition of global
integration/pushforward and is not presently a verified construction.

The P06.2 round-one production receipt is `final/wrong`: its localization
step did not justify separating the support of an arbitrary test form from
the analytic boundary.  That rejection remains controlling for the rejected
proof and is preserved.  At the time of this audit, the narrower skeletal
round-two packet had no final correct receipt.  It subsequently passed run
`20260825T032958Z_3a27f19be958`, closing the separated, boundaryless, pure
real-PL zero-current scope.  Neither the rejected proof nor the later result
is used as an input in the P21 theorem frozen here.

## Frozen packet

- `p21_upstairs_cross_curve_obstruction_statement_exact_20260825.tex`
- `p21_upstairs_cross_curve_obstruction_source_aware_proof_exact_20260825.tex`

## Live integration

After the guarded production verdict, the exact statement and complete proof
were integrated into Chapter 69 as
`prop:verified-four-punctured-cross-obstruction`.  Chapter 72 records only
the candidate-level obstruction: `P21.3` remains open and its atom remains in
the queue.  At that integration stage, the `20/61` inventory counts were
unchanged.  The research
ledger, major-problem program, atomic inventory, verified-results ledger,
theorem-provenance ledger, and Appendix L carry the same scope firewall.

The live TeX is a house-style rendering of the frozen proof, not a claim of
post-integration byte identity.  It uses `cref`/`eqref`, upright differential
macros, and an unnamed proposition.  The focused Chapter 69/Chapter 72/
Appendix L build exited `0`; the PDF SHA-256 is
`e454b413779d00dd90e6f28f19a6cc4d9e39e123fd9f012451c12e323f4b5089`
and the log SHA-256 is
`4660228a78ff741a6260f77a5860c8d651226decb8824a34f54832bafb30b73c`.
The log contains no TeX error, fatal error, duplicate label, duplicate
destination, or unresolved reference to a label introduced by this
integration.  The slice intentionally omits most chapters, so unrelated
external cross-references remain unresolved.  Exact live-file hashes and
the controlling frozen hashes are preserved in
`rethlas_receipts_20260825/p21_upstairs_cross_curve_obstruction_live_integration_receipt_20260825.md`.
