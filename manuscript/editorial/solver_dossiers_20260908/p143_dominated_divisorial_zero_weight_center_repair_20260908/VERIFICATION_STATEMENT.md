# P14.3 v3 candidate — statement prepared for independent review

Let `X` be a connected compact Kähler manifold.  Let `X^beth` be the
space of semivaluations of coherent ideal sheaves, with the pointwise
topology into `[0,+infinity]`.  Write `q <= v` when
`q(a) <= v(a)` for every coherent ideal `a subset O_X`.  Let `X^div`
consist of the trivial valuation and nonnegative rational multiples of
orders along prime divisors on proper bimeromorphic models of `X`, in the
convention of [MP24, Definition 2.3.1].

**Theorem.**  For every `v in X^beth`,

`v in closure({q in X^div : q <= v}).`

Equivalently, there is a net of rational divisorial points
`q_lambda -> v` with `q_lambda <= v` for every `lambda`.  This includes
semivaluations with proper support and semivaluations taking `+infinity`
on nonzero ideals; the net is not asserted to be increasing.

**Comparison corollary.**  Let `alpha` be a Kähler class and let
`F:X^beth -> [-infinity,c]` be upper semicontinuous and antitone for the
above ideal order.  If an MP potential `phi in PSH_MP(alpha)` agrees with
`F` on `X^div`, then `F=phi` on `X^beth`.

**Conditional finite-energy corollary.**  Assume the P14.2 conclusion
that the raw ideal-valuative transform is upper semicontinuous on all of
`X^beth`.  For a finite-energy DXZ non-Archimedean metric `Gamma` in a
Kähler class `[omega]`, with `c=Gamma_max`, define

`F_Gamma(v)=sup_{tau<c}{tau-sup_{m>=1}(1/m)v(I(mGamma_tau))}.`

Then `F_Gamma` is the corresponding MP finite-energy potential at every
point of `X^beth`, not only at rational divisorial points.  This remains
conditional on P14.2; it asserts neither an arbitrary pseudoeffective
MP-cone statement nor an unrestricted Kähler bijection.

This v3 statement is unchanged from v2.  The v3 proof postimage has
SHA-256 `1392f87e1ef47a1dde1c8b17ee7e264ed4a1b926e031ea35a9fb711e91f83d87`.
The only proof change is the direct central-ideal argument recorded in
`V2_TO_V3.patch`.  Sources: [MP24] (Boucksom--Jonsson,
arXiv:2409.06221v2) and [DXZ23] (Darvas--Xia--Zhang,
arXiv:2302.02541v3).
