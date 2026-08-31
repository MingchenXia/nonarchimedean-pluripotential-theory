# Independent bounded check: fixed P1/O(2) capacity example

Date: 31 August 2026. Reviewer did not originate or author this new example.
The reviewer previously authored the broader Chapter 25 weighted-capacity
repair; this is therefore an independent check of the new example only,
not an independent audit of that entire earlier packet.

Reviewed exact bytes in
`../p081_ch25_weighted_capacity_repair_20260831/revised1/`:

- `fixed_reference_example.tex`: SHA-256
  `e5b8c7817ca8eb0ffd56f686f9efc36ae47c44edd2c95ebaa84071b005add9fa`.
- `patched/ch25_capacity.tex`: SHA-256
  `4f66e1358ede7c8d9afff6b8b3c0fbaf53a27247d9741ce02f890fe24a0959a7`.
- `MANIFEST.json`: SHA-256
  `c1aa7dad837b6a06e0470c1442a7b9966dff398816f9b6cc378f09e0bff32287`.

Verdict: no mathematical gap found in this example within the original
normalized-DVR scope, relative to the stated bounded curve-pushforward
input. It really fixes both C=P1_K and the standard O(2) reference form.
It proves Cap_theta({v_N})=1/N, not merely small capacities for varying
reference forms.

## Direct calculation

Each blowup is at the smooth point where the strict section T=0 meets
the latest component. It is not a node blowup. In the chart following
the section, the coordinate is T/pi^j after j steps; hence the newest
component has normalized valuation v_N(T)=N. All components have
multiplicity one, and neighboring intersections are residue-rational.
The skeleton has N edges of length and conductance one. No extension of
K, geometric splitting assumption, or nonreduced subdivision is needed.

Write the components in order as C_0,...,C_N. The adjacent intersection
numbers are one. The endpoints have self-intersection -1 and the internal
components have self-intersection -2, as follows also by intersecting the
principal fibre sum with each component. The pullback of O(2) has degrees
(2,0,...,0). For the rational vertical divisor

\[
 D_N=-\sum_{j=0}^N(j/N)C_j,
\]

the intersections are -1/N at C_0, zero internally, and 1/N at C_N:
the internal expression is
(-(j-1)+2j-(j+1))/N=0 and the final one is
(-(N-1)+N)/N=1/N. Thus the modified bundle's degrees are
(2-1/N,0,...,0,1/N), all nonnegative for N>=1. The associated actual
rational model potential is -s/N on the skeleton and its retraction
pullback on the analytic curve; it lies in [-1,0] and is theta-psh.
Since all multiplicities are one, its atomic masses are exactly these
degrees. This proves the point-capacity lower bound 1/N.

For the upper bound, take any bounded theta-psh capacity competitor u.
The bounded curve-pushforward identity in the reviewed full Chapter 25
gives a positive graph measure
2 delta_0 + Delta(F), where F=u|_[0,N] lies in [-1,0]. The segment
description `eq:ch25-segment-class` makes F convex, and
`eq:ch25-segment-measure` gives its mass at N as -F'(N-). Convexity gives

\[
 F'(N-)\geq\frac{F(N)-F(0)}{N}\geq-\frac1N.
\]

Consequently MA_theta(u)(p_N^{-1}({v_N}))<=1/N for every competitor,
and the same upper bound holds for the subset {v_N}. Together with the
explicit model this proves equality for both the point and its tube in
this example. It does not assume general point/tube capacity equality.

Only the varying divisorial point and its determining model depend on N.
The analytic curve, the reference metric/form, and the capacity functional
do not. The conclusion rules out a positive uniform lower bound over all
divisorial points for this one fixed pair; it does not say any of these
individual point capacities vanishes.

## Scope of the check

The full example, its embedding, the endpoint formula, the segment measure
and convexity statements, and the preceding curve-capacity/pushforward
interface were read. The new example does not need the converse graph
potential construction to realize its lower bound: its divisor is explicit.
The upper bound still uses the previously gated all-bounded-potential
pushforward theorem. No independent certification of that earlier
author-created theorem, no production verdict, and no integration approval
is claimed. The production Rethlas sol/xhigh gate remains required. No live
or frozen source files were edited, and no production calls were made.
