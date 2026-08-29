# P07.1 infinite-endpoint source and hostile audit (staging only)

## Primary-source scope

- Local CLD source: `/private/tmp/cld25_source/esptrop.tex`, especially the
  subsection “Un autre type de segment” (around source lines 969–993).
- The source defines an interval in the extended real line, makes parlinear
  functions constant near endpoints, and says that affine functions on a
  connected domain meeting an endpoint are constant.
- It explicitly identifies \([ -\infty,0)\) with the G-tropical model of the
  open unit disc over a trivially valued field.
- CLD §§6.1.1 and 6.1.6 make tropical charts affine and their scalar
  coordinate functions affine; smooth forms are then defined in
  Definition 6.2.1.  On an endpoint collar every scalar affine coordinate is
  constant; on the finite stratum the ordinary real affine coordinate
  applies.  Thus the packet's smooth sheaf is the source model, not an
  invented enlargement.
- The generated psh sheaf and its ordinal filtration are those of CLD
  Definition 8.1.1 and Lemma 8.1.4 in
  `/private/tmp/cld25_source/bt-trop.tex`.

## Hostile checks performed

1. **Downward endpoint jump.**  A class defined only by convexity on the
   finite stratum and `u(-∞) ≤ u(t)` is too large.  Every generator is
   continuous at the endpoint and nondecreasing.  For a decreasing sequence,
   choosing one term whose endpoint value is close to the limiting endpoint
   value forces the finite-side limsup down to the same value.  Hence the
   exact trace equality is necessary and is stable under all generating
   operations.

2. **False finite-endpoint dichotomy.**  The finite-endpoint implication
   `u(endpoint)=-∞ => u is locally -∞` fails here.  The function `u(t)=t`
   has trace \(-\infty\), is finite on every finite point, and is convex.
   The proof treats it and all analogous functions separately from the
   identically \(-\infty\) case.

3. **Monotonicity at the endpoint.**  Convexity alone does not imply
   nondecreasing behavior on a general real interval.  Here it does only
   because a decreasing secant slope would force the value to tend to
   \(+\infty\) as `t -> -∞`, contradicting the required trace in
   `R union {-∞}`.  This argument is included explicitly.

4. **Gaussian integrability.**  The right affine extension has all secant
   slopes in `[0,m]`, hence is globally Lipschitz and has at most linear
   growth.  Gaussian convolution is therefore finite and smooth.  The same
   Lipschitz bound supplies a uniform heat error of order `sqrt(s)`.

5. **Actual monotonicity of the approximants.**  Heat convolution of a
   convex function increases with heat time.  Since `1/(n+1) < 1/n`, the
   heat factors decrease with `n`.  The exact clamps also decrease because
   their second arguments are `-n`.  Coordinate monotonicity of the heat
   regularizations gives the two-step inequality proving `F_{n+1} <= F_n`.
   This avoids an invalid appeal to uniform convergence when the endpoint
   value is \(-\infty\).

6. **Exact collar, not asymptotic flatness.**  The compactly smoothed maximum
   equals its second argument whenever that argument dominates by more than
   twice the smoothing radius.  Thus the clamp is literally constant for
   `t < -n-2 eta`, and each approximant belongs to the source smooth sheaf.

7. **Endpoint convergence.**  The endpoint value is
   `A_{1/n}(-n)`.  The global Lipschitz estimate makes its difference from
   `u(-n)` tend to zero, while the trace condition sends `u(-n)` to the
   prescribed finite value or to \(-\infty\).

8. **Sheaf and transfinite firewall.**  Local convexity glues on an interval;
   the endpoint trace is detected on any cover member containing the
   endpoint.  The proof separately verifies preservation of the trace under
   decreasing limits, so the comparison class really contains the entire
   transfinite generated sheaf, not just stage one.

9. **Scope firewall.**  The result concerns one extended-real interval only.
   It neither treats the CLD stars nor establishes first-stage collapse on an
   arbitrary G-tropical or Berkovich space.  P07.1 therefore remains active
   unless and until the inventory is deliberately split after production
   verification.

10. **Early clamp indices.**  If the right endpoint of the tail is below
    \(-1\), the expression \(u(-n)\) is defined only for sufficiently large
    \(n\).  The convergence proof now states that quantifier explicitly; no
    assertion about the discarded finite initial segment is used.

## Verification status

No production-Rethlas verdict has been obtained.  This packet must remain
quarantined from the live manuscript until the exact statement and proof
bytes receive an independent source-aware audit and a production
gpt-5.6-sol/xhigh verdict of `correct` with zero critical errors and zero
gaps.
