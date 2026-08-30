# Independent exact-byte audit of the P07.1 `X_B` germ obstruction

Date: 30 August 2026

Audited frozen files:

| file | SHA-256 |
|---|---|
| `p071_counterexample_search_20260830/candidate_statement.tex` | `563bd314d2ee0ce12c487df565e2e3c6ad222789e9acace8e550b03b386309ed` |
| `p071_counterexample_search_20260830/candidate_proof.tex` | `5d36861cef1d8861bf51ca49ef1ecf8619c4e7975a6322aaed071eee54f058c4` |

The packet's `SHA256SUMS` check passes.  This document is an independent
hostile audit, not a Rethlas receipt and not authorization for live
integration.

## Verdict

**PASS, with the scope firewall in the frozen statement essential.**  I find
zero mathematical errors and zero proof gaps in the exact frozen bytes.  The
result proves failure of simultaneous realization for a prescribed countable
family of smooth-psh germs.  It does not construct a rank-two psh function and
does not settle P07.1.

## Exact CLD topology and domain checks

CLD Section 6.7.3 defines a centre open set by two conditions: each branch
slice is open in `[-infinity,0]`, and all but finitely many branch slices are
full.  It defines domains analogously.  Therefore

```
(U_n)_{b_j}=(-1,0]       (j<=n),
(U_n)_b=[-infinity,0]    otherwise
```

is a legal standard open neighbourhood.  The endpoint interval `(-1,0]` is
open in the order topology at the maximal endpoint `0`.  Adding one truncated
branch proves `U_{n+1} subset U_n`.  Their intersection truncates every
`b_j`, so it cannot contain a centre neighbourhood, since such a neighbourhood
has only finitely many nonfull branches.

The proof does not assume that a hypothetical common neighbourhood is
standard.  Every centre neighbourhood contains a standard one, and
restriction of smooth psh functions preserves smoothness and positivity.

## Smoothness and psh checks

The chosen `q` is smooth, nondecreasing, zero on `(-infinity,-2]`, and one on
`[-1,infinity)`.  Hence

```
psi(t)=integral_0^t q(s) ds
```

is smooth, convex, exactly constant on a full collar of `-infinity`, satisfies
`psi(0)=0`, and has centre derivative `1`.

For fixed `n`, the only nonconstant profiles are `psi` on the full branch
`b_+` and `-t` on the exceptional collar of `b_n`.  The latter is an affine,
hence convex, smooth profile, and the full-endpoint collar condition does not
apply because `-infinity` is not in that branch slice.  All other full branch
profiles are constant.  There are only finitely many nonfull branches in
`U_n` and only two nonconstant profiles.  The centre derivative sum is exactly

```
                         1 + (-1) = 0.
```

This is the CLD smooth balance condition.  Branchwise second derivatives are
nonnegative, so the exact verified description of smooth psh functions on
this `X_B` puts `f_n` in `Psh_{X_B,0}(U_n)`.

No boundary-current term has been omitted: the centre balance is precisely
what cancels it for a smooth function, and the full endpoint profiles are
constant on collars.

## Germ derivative contradiction

After restriction to a standard common neighbourhood `W_0`, its exceptional
set `A` is finite.  Choose `n` with `b_n notin A`; then the `b_n` slice of
`W_0` is full.  Equality of germs supplies equality with `-t` on some centre
collar, even if the smaller equality neighbourhood itself declares `b_n`
exceptional.  Ordinary differentiation at `0` therefore gives derivative
`-1`.

CLD smoothness on the full `b_n` branch makes the representative constant
near `-infinity`, so its derivative is zero on a left collar.  Psh positivity
makes the profile convex, hence its derivative is nondecreasing.  It cannot
have derivative `0` on the left and `-1` at the right endpoint.  This proves
the no-common-representative assertion without any hidden quotient-topology
or analytic-realization assumption.

## The `2^{-k}(f_n+3)` quantifiers

Because `0<=q<=1` and `q=0` left of `-2`,

```
                         -2 <= psi <= 0.
```

On the truncated branch, `0<=-t<1`; all other profiles vanish.  Hence the
single constant `C=3`, independent of both `n` and `k`, satisfies
`f_n+3>0` everywhere on `U_n`.  Addition of a constant leaves the Hessian
unchanged, and positive scaling preserves smooth psh positivity.  Therefore,
for each fixed `n`,

```
v_{n,k}=2^{-k}(f_n+3)
```

is pointwise decreasing in `k` and converges pointwise to zero on `U_n`.

If the full two-index family of germs had representatives on one
neighbourhood, the subfamily with `k=1` would.  Multiplication by `2` and
subtraction of the smooth constant `3` preserve smoothness and psh positivity
and would give common representatives of all `[f_n]_eta`, already proved
impossible.  Thus the two-index quantifier is correct.

For every `n`, the row limit is the restriction of the same global function
`u_n=0`; the outer sequence `u_n` is decreasing and has limit zero.  Yet zero
has the global row of positive constants `2^{-k}`.  This verifies, rather than
weakens, the frozen warning: the obstruction depends on the selected rows.

## Counterexample firewall

The construction cannot be promoted by declaring the `f_n` global.  On a
global full `b_n` branch, the negative centre derivative would contradict the
same constant-collar convexity argument.  More importantly, stage-one
membership asks for the existence of *some* local row.  The zero target has a
global constant row.  Thus none of the following follows from the packet:

- `Psh_{X_B,2} != Psh_{X_B,1}`;
- failure of first-stage collapse on `X_B`;
- failure of existential re-selection for an arbitrary decreasing family;
- retirement of P07.1.

The exact proved conclusion is narrower and useful: the sheaf/stalk axioms
cannot commonize arbitrary prescribed countable smooth-psh germs or arbitrary
prescribed first-stage rows.
