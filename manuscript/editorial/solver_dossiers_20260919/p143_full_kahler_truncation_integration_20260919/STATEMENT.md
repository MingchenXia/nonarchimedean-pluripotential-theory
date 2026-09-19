# P14.3 full Kähler truncation closure — production statement

Let `X` be a connected compact Kähler manifold, let `alpha=[omega]` be a
Kähler class, and let `K=X^beth` be the compact space of semivaluations of
coherent ideal sheaves.  Assume the all-point P14.2 conclusion: the literal
raw ideal-valuative transform of every DXZ non-Archimedean psh object is upper
semicontinuous on `K`.

The following previously established interfaces are part of the statement's
context.

1. The MP cone `PSH_MP(alpha)` is the decreasing-net completion of rational
   PL model psh functions.  Rational translations preserve the model cone.
2. Rational divisorial semivaluations, including the trivial semivaluation,
   approximate every semivaluation from below in ideal order.  Consequently,
   an upper-semicontinuous ideal-antitone function that agrees divisorially
   with an MP psh function agrees with it everywhere.
3. DXZ objects admit maxima with constant objects and decreasing infima when
   their endpoints have a finite lower bound.  On rational divisorial points,
   the raw transform sends a maximum to the pointwise maximum and a decreasing
   infimum to the pointwise infimum; at the trivial semivaluation it equals
   the endpoint.  Divisorial raw-transform values determine the DXZ object
   and reflect order.
4. In a Kähler class, positive-volume DXZ objects are recovered by
   unperturbed positive-mass test curves.  The finite-energy DXZ--MP
   correspondence is bijective and preserves energy; the literal raw
   transform of a finite-energy object equals its MP image at every
   semivaluation.
5. The constant DXZ object of value `a` has test-curve level zero below `a`
   in every Kähler perturbation component.  Every normalized model level is
   at most zero.
6. The previously verified MP-section theorem constructs a unique map
   `S_alpha:PSH_MP(alpha)->PSH_DXZ^NA(X,omega)` on the full MP cone, without
   a finite-energy restriction, and proves
   `T_alpha(S_alpha(phi))=phi` at every semivaluation.  This section preserves
   and reflects pointwise order.

## Decreasing-stability lemma

If `(phi_j)_{j>=1}` is a decreasing sequence in `PSH_MP(alpha)` and
`phi=inf_j phi_j` is not identically minus infinity, then
`phi in PSH_MP(alpha)`.

## Kähler truncation theorem

Under the preceding hypotheses, the literal raw ideal-valuative transform is
an order isomorphism

`T_alpha: PSH_DXZ^NA(X,omega) -> PSH_MP(alpha)`.

Its inverse is the previously constructed MP-to-DXZ section.  More precisely,
for a DXZ object `Gamma`, let `0` be the constant zero object and put

`Gamma^(j) = Gamma vee (0-j)`.

Then every `Gamma^(j)` has finite energy,
`Gamma^(j) downarrow Gamma`, and

`T_Gamma = inf_j T_{Gamma^(j)}`

on all of `K`, with every function on the right in `E^1_MP(alpha)`.  On the
finite-energy locus this order isomorphism is the existing finite-energy
DXZ--MP correspondence and the energies agree.

## Scope

The theorem is conditional only in the explicit sense above: it uses the
all-point P14.2 upper-semicontinuity conclusion.  It removes the independent
P14.3 residual in Kähler classes without projectivity, rationality, or a
finite-energy hypothesis.  It does not extend the relatively nef MP cone
unchanged to a big non-nef class and does not construct an unnormalized
energy or Monge--Ampère operator in a zero-volume class.
