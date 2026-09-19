# Chapter 16 weighted and polar proof rewrite status

Date opened: 1 September 2026.
Date closed: 14 September 2026.
Live source comparison base at opening: 6795dfd917d591b1ede108d8d9afe3b1a032bc29.

**Status: all five identified repairs are present in the live manuscript and
have been re-derived independently.** The repairs landed in commit `10ccff9`
("Integrate verified P21.3 partial advances", 8 September 2026) as a side
effect of the Chapter 72 work; this note was not updated at that time and
overstated the outstanding work for six days. It is corrected below.

This note records a line-by-line re-derivation of the repaired arguments. It
is not a production Rethlas gate and does not authorize any theorem promotion
or problem retirement.

## Repair 1 --- barrier sublevel formulation: DONE

`thm:ch16-barrier` (Section 16.7) no longer asserts that rho is negative on
its whole domain with compact nonpositive sublevel. It now gives an ordinary
open Y inside the prescribed neighbourhood, a smooth psh rho on Y, and
delta>0 with rho(x)<0 and K_delta = {rho <= delta} compact in Y; U = {rho<0}
is then nonempty and relatively compact. The section preamble states
explicitly why the literal earlier pair of requirements is impossible on a
positive-dimensional open space.

Re-derivation. With a_i = log(|f_i/g|/lambda_i) and t = log mu, the bound
rho <= delta = t/4 forces M_eps <= 3t/4, hence a_i <= 3t/4 for every i since
M_eps dominates the coordinatewise maximum. Therefore
K_delta is contained in W_{mu^{3/4}}, which is contained in W_mu, which is
contained in Int(A). The no-common-zero condition gives g nonvanishing on
W_mu, so W_mu is contained in Y and K_delta is closed in a compact rational
domain, hence compact. At x all a_i <= 0, so rho(x) <= eps - t/2 < 0 because
eps < t/8. Correct as stated.

Simultaneous numerator zeros are handled: the constant branch a_0 = -1 keeps
the regularized maximum bounded below when every f_i vanishes, and at any
point where a subset of the f_i vanish those coordinates fall more than
2 eps below the maximum and are ignored, the surviving coordinates being
logarithms of analytic functions nonvanishing near that point. rho therefore
extends smoothly across the whole numerator-zero locus.

## Repair 2 --- beta regularity and derivative factors: DONE

`def:ch16-weight-forms` now fixes a *real* parameter a>1 rather than an
integer, and `lem:ch16-beta-properties` carries b_k = 2 for k<n and b_n = 1.
The proof regularizes only F, F', F'' for F(t) = max{-t,0}^l, and states
explicitly that the assertion does not require all coefficients of beta_k to
be C^2 and that beta_0 is never differentiated. The old error --- treating an
integer positive-part power as having that many continuous derivatives --- is
gone, and the closing paragraph now records that the factor two must not be
inserted at k=n.

Re-derivation. With l = k+a > 2 for k >= 1 and a > 1, both
F'(t) = -l max{-t,0}^{l-1} and F''(t) = l(l-1) max{-t,0}^{l-2} are
continuous, so F is genuinely C^2 and the exponent bookkeeping is sound.
Substituting F' = -l r^{l-1} and F'' = l(l-1) r^{l-2} into
ddprime beta_{k,eps} = b_k F'(rho) ddprime rho ^ theta^q and
dprimeddprime beta_{k,eps} = b_k (F'(rho) theta^{q+1} + F''(rho) eta ^ theta^q)
reproduces the two displayed limit formulas exactly. For the sandwich bound,
beta_{k-1} = r^{l-1} theta^{n-k+1} + (l-1) r^{l-2} eta ^ theta^{n-k}; keeping
one term of the exact derivative at a time and using b_k <= 2 gives the
asserted two-sided bound by 2(k+a) beta_{k-1}. Correct as stated.

## Repair 3 --- weighted theorem support-boundary integration: DONE

`thm:ch16-weighted-cln` now hypothesizes V smooth psh **on a neighbourhood of
K_delta** and negative on U, not merely smooth on U. Step 1 of the proof
carries the regularization through one fixed compact K_delta, performs the
limit first, and states that no sign of V on the collar 0 < rho < eps is
used and that inequalities are applied only after the limiting identity.
The apparently order-one term is rewritten through
`eq:ch16-energy-mixed-derivative` as one fixed signed Radon measure against
uniformly convergent coefficients, rather than as an extension of an
order-one current to arbitrary continuous tests.

Re-derivation. The cross-term factor 2bl is correct: dprimeddprime of a
product contributes two cross terms, each evaluating to
bl (-V) r^{l-1} Gamma_Q(z,rho). Young's inequality with the stated weights
r^{l/2} z^{-1/2} and bl z^{1/2} r^{(l-2)/2} gives
`eq:ch16-cln-cauchy` since the exponents combine to r^{l-1} and the z powers
cancel. Collecting the surviving coefficients yields
bl r^{l-1} theta^{n-k+1} + bl((b-1)l+1) r^{l-2} eta ^ theta^{n-k}, which is
2l and 2l(l+1) at b=2 and l and l at b=1, and is dominated by
c_l beta_{k-1} with c_l = 2l(l+1)/(l-1) --- with equality in the second
coefficient at b=2. In Step 3 the substitution z = exp(B u_k) makes
`eq:ch16-energy-exp-combined` an identity whose energy term cancels exactly
against the one produced in Step 2, before any estimate is relaxed; with
B = 1/(2M) the recursion constant is 4e l(l+1)/(l-1), and the telescoping
product reproduces C(k,a) = (4e)^k a^{-1}(k+a)(2+a)...(k+1+a), consistent with
C(0,a) = 1. Correct as stated.

## Repair 4 --- polar proof fixed-helper limit: DONE

The proof of `thm:cld-polar-negligibility` no longer moves the approximating
potential and the approximating measures together. It applies the weighted
theorem for each fixed p against **one fixed** positive Monge-Ampere measure,
bounds the right-hand side by the p-independent integral of (-V) beta_0 using
-V_p <= -V after the common shift, and only then lets p tend to infinity by
monotone convergence. The text states that all coefficient regularizations
are taken with p fixed and that the bound uses no derivative of V_p.

Re-derivation. V_p decreasing to V gives -V_p <= -V, so the right-hand side
is uniform in p; beta_0 has compact continuous coefficients dominated on
fixed compact charts by finitely many smooth positive top forms, against
which V is integrable by hypothesis, so the bound is finite. On a compact
neighbourhood of x inside U the factor r^{n+a} is bounded below by a positive
constant, which converts the weighted bound into local integrability.
Correct as stated.

## Repair 5 --- overclaimed approachability remark: DONE

The blanket claim that the continuous factors' approachability cannot be
removed is gone. The section preamble now says local approachability is
retained only for the possibly unbounded auxiliary V, that the continuous
curvature factors u_i may belong to the full minimal uniform-closure sheaf
CPsh_X, and that no collapse at stage one is asserted or needed. The
paragraph after `cor:ch16-cpsh-analytic-nullity` states the residual scope
honestly: the auxiliary polar function remains locally approachable and
canonically locally integrable, the result is not a blanket pluripolar
negligibility assertion, and it does not define products of unbounded
potentials.

## Supporting inputs checked

The repaired weighted proof depends on four identities in
Section 16.6. All four are stated and proved in the live source, and none is
an unproved import: `eq:ch16-energy-exp-combined`
(`prop:ch16-energy-exponential`), `eq:ch16-energy-schwarz`,
`eq:ch16-energy-mixed-derivative` and `eq:ch16-energy-closed-factor`
(all `lem:ch16-energy-schwarz`). The exponential identity is used in Step 3
only through the inequality direction obtained from z >= exp(-BM) and
positivity of dprimeddprime(u_k S), which is legitimate.

## What is still not claimed

This note certifies internal consistency of the repaired arguments, not a
production gate. The unpromoted material referenced in the original note ---
the full-CPsh research dossier, the real-parameter weight draft preserved in
`p213_weight_parameter_extension_independent_audit_20260901`, and the
Chapter 14 component-curvature insertion candidates --- keeps its earlier
status. The two production acceptance audits that disclosed execution-
compliance exceptions are still not clean promotion gates. No frozen
verification record has been altered, and no theorem or problem retirement is
authorized here.
