# Lin's polyhedral coefficient boundary — 5 October 2026

This is a source and research note outside the active TeX closure. It
checks the literal BMPS coefficient convention used in Lin v1 Section 8
and records an alternative Bedford–Taylor route for the required local
continuity statement. It does not claim a counterexample to Lin's main
Theorem 10.2, a repair of critical Siu division, or a new solved problem.
The active book, standalone catalogue and current PDF artifacts are
unchanged by this note.

## Exact source issue

BMPS, arXiv:2603.08664v1, Definition 2.28 on physical page 11 requires
**integral** linear parts in its space `PA`. Definition 2.29 preserves
that coefficient convention under subdivisions. Definitions 3.1 and
3.20, Proposition 3.22 and Definition 3.23, on pages 14 and 20–21,
therefore define literal `PC_reg(X,gamma)` through uniform limits of
integral-slope polyhedrally convex functions in the fixed reference
class. Theorem 4.13, pages 30–31, and Corollary 4.18, page 36, act on
that declared regularizable domain. The paper also uses real convex
combinations and real affine regularization in other arguments; the
book already separates those intended relaxed arguments from the literal
integral-slope definitions.

Lin, arXiv:2609.12969v1, Proposition 8.2 on page 19, asserts that a convex
piecewise affine function with **rational slopes**, bounded relative to
a rational piecewise affine reference, is PC-regularizable in the sense
of BMPS. The first paragraph of its proof on page 20 changes affine
constants to rational constants and retains the original rational
slopes. This does not put the approximants in BMPS's printed `PA` space.
Proposition 8.3 on page 22 then uses that membership assertion to invoke
BMPS Theorem 4.13 on translated stars.

The issue is the coefficient domain, independently of whether affine
constants lie in `Q`, an arbitrary value group, or `R`. A subdivision
does not replace the fixed tangent lattice by a different lattice.
Clearing one denominator and dividing a measure afterward defines a
rational extension; it does not make the original function an element
of the printed integral-slope uniform closure.

## A known one-dimensional separation applied to this clause

Take the balanced line `X=R` with lattice `Z` and weight one. Set

\[
 \gamma(x)=|x|,\qquad
 f(x)=\tfrac12|x|+\tfrac12\max\{|x|,1\}
     =\max\{-x,x,-x/2+1/2,x/2+1/2\}.
\]

The function `f` is globally convex and rational piecewise affine, and
`0 <= f-gamma <= 1/2`. The reference is integral piecewise affine and
positive at infinity. Thus these data satisfy the explicit hypotheses
of Lin Proposition 8.2, even with rational constants and a particularly
simple fixed integral reference.

On `[0,1]`, `f(x)=1/2+x/2`. For every literal integral-slope convex
piecewise affine function `h`, let `m` be its left derivative at `1/2`.
It is an integer. If `m<=0`, convexity gives

\[
 h(1/2)-h(0)\leq0,
 \qquad f(1/2)-f(0)=1/4.
\]

If `m>=1`, monotonicity of the one-sided derivatives gives

\[
 h(1)-h(1/2)\geq1/2,
 \qquad f(1)-f(1/2)=1/4.
\]

Either way, two pointwise errors differ by at least `1/4`, so

\[
  \|h-f\|_{L^\infty([0,1])}\geq1/8.
\]

In particular, `f` is not a uniform limit of literal PAPC functions,
and is not in the PC-regularizable space defined by BMPS v1. This is
the midpoint slope-separation argument already used in the book's
verified one-dimensional literal classification. Here `f` is precisely
the convex combination with `C=1` and `N=2` appearing in that existing
result. No new classification or priority claim is made.

The bound is also sharp for this example on the entire line: the
literal function

\[
 h_*(x)=\max\{|x|,1/2\}+1/8
\]

is integral piecewise affine in the same bounded reference class, and
`||h_*-f||_infinity=1/8`. This is checked directly on the intervals
cut by `-1,-1/2,0,1/2,1` and on the two exterior rays. It is a worked
calculation, not an independent model-verifier receipt.

The resulting diagnostic concerns the **literal membership clause**
of Proposition 8.2. If a rational or real PA convention is intended,
that is a different function space and needs its own continuity and
identification statement. Nothing here refutes the intended tropical
intersection measure or the analytic main theorem.

There is a concrete normalization check. The real one-dimensional
Monge–Ampère measure of `f`, and the rational tropical intersection
measure obtained by clearing the denominator, are

\[
 f''=\tfrac12\delta_{-1}+\delta_0+\tfrac12\delta_1,
 \qquad (2f)''=\delta_{-1}+2\delta_0+\delta_1.
\]

They have masses two and four. Dividing the latter measure by two is
the dimension-one tensor-power normalization, not a density statement
in the fixed integral-slope class. On `P^1` the recession function
`|x|` corresponds to a degree-two toric line bundle; over a normalized
nontrivially valued field with these rational constants in its value
group, `f` is a valid rational toric model-metric weight after exponent
two. This distinction explains how a genuine toric model metric can
fall outside the literal polyhedral regularizable category.

## An alternative local continuity route to check

The following route uses the ambient Lagerberg Bedford–Taylor product
instead of a claim of integral-slope density. Its controlling source
in this note is **BGJK arXiv:2102.07392v1**, Theorem 4.1.2, pages 20–21;
identity with the published 2025 PDF is not asserted. The source's full
theorem and printed proof have been read. Its imported complex
Bedford–Taylor and BGJK20 comparison inputs are named published inputs,
not newly full-paper-audited proofs here. This route remains a research
proof comparison outside active TeX, without a new independent receipt.

Let `C` be a locally finite balanced weighted `(Z,R)`-polyhedral complex
of pure dimension `d` in `N_R=R^n`, with nonnegative weights. On an
ambient open set `Omega`, its integration current `T=delta_C` has
bidegree `(n-d,n-d)`. Nonnegative weights give positivity; balancing
gives closure under both real differentials. The latter follows from
the polyhedral Stokes identity: facet boundary terms cancel by the
balancing sums. Real affine constants do not enter those sums. The
book's rational Stokes/current interface is byte-preserved; extending
its exact formulation to arbitrary real facet positions must be made
explicit in an admission proof rather than hidden in a citation.

Use the smooth fan `{0}`. Its tropical toric space is `N_R`, with no
added toric boundary. Every finite convex function on `Omega` is a
locally bounded psh function in BGJK's Definition 3.1.2. Set `p=n-d`
and `q=d` in Theorem 4.1.2. It constructs a positive top-degree current

\[
   \mu_f^{\rm BT}=(d'd''f)^{\wedge d}\wedge_{\rm BT}\delta_C.
\]

It is a Radon measure and is local in `f` and `T`. If convex functions
`f_i` converge locally uniformly to `f`, Theorem 4.1.2(ii), with the
current kept fixed, gives weak convergence of these currents. There is
no integral-slope approximation hypothesis on the `f_i`, and no
asymptotic reference is needed for this local assertion.

For a convex piecewise affine `h`, the remaining identification to
check is with the specified delta-form tropical intersection product.
Its usual closed-current potential identity is

\[
 (d'd''h)\wedge_{\rm BT} S=d'd''(hS)
                         =(d'd''h)\wedge_\delta S,
 \qquad d'S=d''S=0.
\]

The first equality follows from the smooth product rule and locally
uniform convex smoothing in the already constructed Bedford–Taylor
product. Positive closed currents have measure coefficients, so
multiplication by the continuous function `h` is defined. The second
equality is the delta-form product rule; it is the same compatibility
calculation displayed by Lin in Proposition 8.5, equation (11), page 24.
It is important to check this identity for the actual polyhedral
delta-form convention, including its calibration and closedness, before
claiming a complete alternate proof. It is not an arbitrary product
of two distributional currents.

Starting with `S=delta_C`, iterate the identity. At each stage the
Bedford–Taylor product supplies positivity and closedness; the
delta-form side supplies the piecewise affine intersection current.
This identifies the measure of each convex piecewise affine `f_i`
with `mu_(f_i)^BT` without invoking Lin Proposition 8.3. Then
Theorem 4.1.2(ii) supplies the locally uniform limit directly. In this
ordering, the equation-(11) compatibility argument precedes the
continuity theorem, avoiding dependence on the continuity statement
one is trying to establish.

To pass from convergence on smooth ambient test functions to vague
convergence against continuous compactly supported functions on `|C|`,
choose a smooth cutoff that is at least one on a given compact set.
The convergence on that cutoff bounds the measures' masses there.
Extend and uniformly approximate the continuous test function in the
ambient space, and use this mass bound. This step also keeps the Radon
and support assertions explicit. For `d=0`, the product is simply
`delta_C` and the argument is immediate. Zero weights cause no issue.

This route concerns finite continuous convex ambient functions and
locally uniform sequence limits. It gives no statement about singular
infinite-valued potentials, arbitrary analytic psh functions, or a
polyhedral obstacle envelope. It does not resolve any of the missing
analytic germ or skeleton inputs in Lin's main theorem, and does not
enter the book's general Siu/envelope chain.

## Source, version and admission record

Fifteen actual selected primary pages in four contact sheets were
freshly viewed: BMPS 11, 14, 20, 21, 30, 31, 36; Lin 19, 20, 21, 22,
24; BGJK v1 13, 20, 21. The controlling PDF digests are preserved in
the companion manifest. These are selected-source checks, not fresh
full readings of the three papers. The existing complete Lin reading
and older Chapter 72 BMPS checks remain dated evidence.

The identifier API returned HTTP 429. Subsequent ordinary official
abstract pages returned HTTP 200 and list only v1 for BMPS, Lin and
BGJK. Those are bounded version checks on 5 October, not an exhaustive
search for errata, journal revisions, related papers or the planned
BMPS sequel. The publisher metadata for BGJK was obtained through
Crossref; its linked article endpoint returned an Incapsula block
document despite HTTP 200. No published primary PDF was acquired and
no access control was bypassed. This limits the source comparison to
the pinned arXiv witness.

Before importing a general alternate continuity proof, bind the exact
real-facet Stokes and delta-form potential identities, confirm the
controlling source locators, and preserve the required independent
admission evidence if a new book-level assertion is proposed. The
worked coefficient diagnostic itself applies an existing verified
book argument. No receipt, theorem promotion, general Siu repair or
changed active problem status is claimed by this research note.
