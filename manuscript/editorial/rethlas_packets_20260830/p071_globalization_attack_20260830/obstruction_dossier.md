# P07.1 fixed-neighbourhood globalization attack

Date: 30 August 2026

Status: staging only; no live-book modification; no Rethlas claim.

## Verdict

The remaining bridge cannot be deduced from the bare CLD affine
`G`-tropical axioms or from the smooth cutoff and smooth-extension results in
CLD Sections 6.2--6.3.  The exact CLD star `X_B` supplies a source-legal
obstruction: a countable family of smooth-psh germs need not admit
smooth-psh representatives on one common neighbourhood.  This rules out
commonizing arbitrary *chosen* rows.

It does **not** rule out an existential re-selection theorem for rows of a
given locally approachable section.  It therefore does not disprove P07.1,
does not produce an element of `Psh_2 \ Psh_1`, and does not conflict with the
already verified first-stage collapse on the exact CLD star `X_B`.

The remaining positive target is a relative de-sheafification or
positivity-preserving fusion theorem strong enough to supply the common-core
hypothesis of the already verified
`prop:p071-fixed-core-flattening`.  No such theorem is present in the cited
CLD source at the required generality.

## Source audit

The source used for this audit is the local copy of Chambert--Loir--Ducros,
SHA-256

`f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`.

The relevant source statements have the following exact force.

1. CLD Section 3.1.1 assumes that the underlying space is Hausdorff and
   locally compact and has a basis of open sets that are countable at
   infinity.  It does not say that a countable intersection of
   neighbourhoods is a neighbourhood.  Even on the standard tropical line,
   the legitimate neighbourhoods `(-1/n,1/n)` have no common
   neighbourhood of `0`.

2. CLD Lemma 8.1.4 defines a successor stage by **local** decreasing
   presentations and then sheafifies.  It supplies no common domain for a
   countable family of such presentations.

3. CLD Corollary 6.2.4 and Proposition 6.2.7 construct smooth plateau
   functions and smooth partitions of unity under local differential
   separation.  They assert smoothness, not
   `\mathrm d'\mathrm d''`-positivity.

4. CLD Proposition 6.3.2 extends smooth forms under decency (and uses smooth
   partitions for the global extension).  It does not assert that a smooth
   psh function has a psh extension.

5. For analytic spaces, CLD Proposition 12.4.7 gives decency under the stated
   almost-good hypothesis, and Corollary 15.2.4 gives local differential
   separation under local holomorphic separation.  These hypotheses make
   the smooth cutoff machinery available but still do not turn its cutoffs
   into psh functions.

6. CLD Proposition 8.2.1 shows that a smooth convex coordinatewise
   nondecreasing function of smooth psh functions is psh.  Hence a
   regularized maximum preserves positivity where all of its branches are
   already defined.  This does not solve the domain problem: exact agreement
   with one branch near each boundary component requires quantitative
   dominance collars.

## Exact obstruction on the CLD star

The independently frozen packet
`p071_counterexample_search_20260830/candidate_statement.tex` /
`candidate_proof.tex`, with SHA-256
`563bd314d2ee0ce12c487df565e2e3c6ad222789e9acace8e550b03b386309ed` /
`5d36861cef1d8861bf51ca49ef1ecf8619c4e7975a6322aaed071eee54f058c4`,
gives a complete construction.  The file
`independent_exact_byte_audit_20260830.md` records a separate zero-error,
zero-gap hostile audit.  In brief, choose one branch `b_+` and infinitely
many branches `b_n`.  On the standard neighbourhood truncating
`b_1,...,b_n`, take a convex full-branch profile on `b_+` with endpoint
derivative `+1`, the affine profile `-t` on the exceptional `b_n`-collar,
and constants on all other branches.  The centre derivatives balance:

```
                         (+1) + (-1) = 0.
```

If all germs had psh representatives on one standard neighbourhood `W`, then
all but finitely many `b_n` would be full branches of `W`.  A smooth psh
function on a full branch is convex and constant near `-infinity`, so its
endpoint derivative is nonnegative.  The prescribed germ has derivative
`-1`, a contradiction.  For every fixed `n`, scaling the positive function
`f_n+3` by `2^{-k}` gives a decreasing `k`-row converging to zero.  The outer
family of row limits is the decreasing global zero sequence.  No decrease in
the index `n` is asserted.

This is stronger than the purely topological observation that prescribed row
domains may shrink: even allowing extensions, positivity blocks a common
representative domain.  Its logical boundary is equally important.  Stage-one
membership is existential, so a function may possess other rows which avoid
the obstructed germs.

## Why smooth cutoffs do not repair the obstruction

On the standard affine tropical line, smooth psh functions are ordinary
smooth convex functions.  If a smooth convex function `h` on `R` has compact
support, then `h'=0` on both tails.  Since `h'` is nondecreasing, it vanishes
everywhere, and compact support forces `h=0`.  Therefore:

- a nontrivial CLD plateau function cannot be psh;
- there is no nonzero compactly supported smooth psh partition of unity even
  in this basic model;
- multiplying a local psh function by the CLD cutoff is not a
  positivity-preserving extension procedure.

The last point is also visible directly:

```
d'd''(chi v)
 = chi d'd''v + v d'd''chi
   + d'chi wedge d''v + d'v wedge d''chi,
```

and the last three terms have no fixed sign.  This argument only excludes the
cutoff/partition route; it does not exclude every possible nonlinear fusion
operator.

An unrestricted right inverse to restriction is also impossible.  For
example, `v(t)=(1-t)^{-1}` is smooth and strictly convex on `(-1,1)`, but it
cannot extend as a finite smooth function, hence cannot extend as a smooth psh
function, across `t=1`.  Any viable extension theorem must shrink the domain
on which exact agreement is demanded and must quantitatively control the
transition.

## Pointwise rows cannot be synchronized by Dini's theorem

The obstruction is not merely a missing sentence about compactness.  On the
standard interval `[0,1]`, put

```
f_k(t) = exp(-k t),             g_l(t) = 1/(1+l t).
```

Both rows consist of smooth strictly convex functions and decrease
pointwise to the same psh function

```
u(0)=1,                         u(t)=0 for t>0.
```

Nevertheless, the two rows cannot be made uniformly close.  Define

```
c_0 = min_{r in [0,+infinity]}
      max(|exp(-1)-(1+r)^(-1)|,
          |exp(-2)-(1+2r)^(-1)|).
```

The minimum exists and is positive.  Indeed, a zero would force both
`r=e-1` and `r=(e^2-1)/2`, whose equality is equivalent to
`(e-1)^2=0`.  For `k>=2`, evaluation at `t=1/k` and `t=2/k`, with
`r=l/k`, gives

```
                         ||f_k-g_l||_infinity >= c_0
```

for every `l`.  Thus the continuous-limit hypothesis in Dini's theorem is a
real hypothesis, not a removable convenience.  This example is not a
counterexample to first-stage collapse: `u` is itself in stage one, by either
displayed row.  It only blocks a fusion proof that silently replaces
pointwise monotone convergence by uniform synchronization.

## Regularized-maximum audit

The `regularized-max-negativity-budget` research card confirms the exact
local formula.  For a smooth convex coordinatewise nondecreasing,
translation-equivariant regularized maximum `M`,

```
d'd'' M(v,w)
 = a d'd''v + b d'd''w + P,
```

where `a,b>=0`, `a+b=1`, and `P>=0`.  Thus there is no hidden loss of
positivity in the transition once both branches exist on the overlap.

The card also explicitly separates this signature calculation from **exact
branch agreement**.  To define the glued function beyond an overlap, one
branch must dominate by more than the smoothing width near the boundary of
the other branch's domain.  CLD's local presentations give pointwise
decreasing rows but no such two-sided collar inequalities.  Smooth cutoffs
would create them only at the cost of the uncontrolled terms displayed
above.  Hence the method stops at its exact-branch hypothesis and supplies no
globalization theorem here.

## Exact remaining positive criterion

The already verified `prop:p071-fixed-core-flattening` gives the clean
reduction.  It would be enough to prove that, for each decreasing family
`w_n in Psh_{X,1}(U)` and each point of `U`, the rows can be re-selected on
neighbourhoods of one common compact core.  A stronger geometric sufficient
input would say that, for every pair `V compactly contained in U` and every
`w in Psh_{X,1}(U)`, the restriction `w|V` has one decreasing stage-zero row
on a neighbourhood of `closure(V)`.  Either input, combined with the
verified finite-square diagonal, yields

```
                         Psh_{X,1} = Psh_X.
```

This is a criterion, not a new theorem beyond the fixed-core proposition.
It holds in the already settled models because their proofs construct rows on
a fixed domain directly.  In a general higher-dimensional affine
`G`-tropical space, proving it would require at least one of the following new
inputs:

- a positivity-preserving Richberg fusion theorem with quantitative
  dominance collars and no continuity assumption on the limit;
- a faithful finite polyhedral chart together with a strictly psh barrier and
  a proof that its negativity budget absorbs every cutoff error;
- an intrinsic comparison-sheaf characterization stable under decreasing
  limits, followed by a fixed-domain smooth regularization theorem.

Piecewise-affine regularity alone does not provide the last smooth step; this
is exactly the higher-dimensional face-compatibility boundary already
identified in the live Chapter 16 scope firewall.

## Release decision

Keep P07.1 open.  The fixed-core diagonal theorem is valid and eliminates the
order-theoretic cross-row defect.  The present attack proves that arbitrary
chosen local rows cannot be commonized, even on the exact CLD star, and that
the standard CLD cutoff/extension results do not preserve positivity.  What
remains is an existential re-selection/fusion theorem, not a formal
consequence of CLD Sections 6.1--6.3.
