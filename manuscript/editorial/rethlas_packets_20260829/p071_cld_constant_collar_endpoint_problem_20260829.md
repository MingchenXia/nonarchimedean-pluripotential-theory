# P07.1 staging problem: the constant-collar endpoint

Status: isolated candidate only.  Nothing in this directory is a live-book
input, and no item is to be removed from the open-problem inventory before an
exact-byte production Rethlas verdict of `correct` with zero critical errors
and zero gaps.

## Residual atom

Chapter 72 asks whether the transfinite CLD psh hierarchy collapses at its
first decreasing-limit stage.  Two classes have already passed production
verification: tropical toric partial compactifications with their standard
Lagerberg smooth structure, and finite ambient-induced real-affine stars.
Neither result applies to the nonambient endpoint smooth structure of
Chambert--Loir--Ducros, Example 6.7.2.

## Exact candidate subproblem

At a finite endpoint, use the ordinary inward real coordinate on the finite
stratum, extend it topologically by the value `0` at the endpoint, and
identify a neighbourhood with `[0,R)`.  This is not a nonconstant affine
chart through the endpoint: CLD-affine functions on a connected endpoint
neighbourhood are constant.  Smooth functions in the Example 6.7.2 structure
are ordinary smooth profiles which are exactly constant on some endpoint
collar.  Determine the full psh sheaf generated from the profiles with
nonnegative second derivative, and determine whether every generated germ is
already a decreasing limit of such smooth profiles on one fixed
neighbourhood.

The candidate answer is the sheaf of extended-real convex functions for
which the endpoint is a minimum.  The proposed proof must separately justify:

1. the exact source identification of the smooth and stage-zero sheaves;
2. locality of extended-real convexity and the endpoint-minimum condition;
3. the `-infinity` alternative at the endpoint;
4. fixed-domain smooth convex regularization with an exact constant collar;
5. conversion of uniform approximation into a decreasing sequence without
   changing the generator class.

## Scope firewall

The candidate concerns finite endpoints only.  It does not treat the
`-infinity` endpoint in the trivially valued open-disc realization, the
infinite star of CLD Section 6.7.3, positive-sedentarity toric charts outside
the already verified toric theorem, or any higher-dimensional tropical
space.
