# theorem thm:p143-dominated-divisorial-density-v4-interface-explicit

## statement

Let `X` be a connected compact Kähler manifold. Let `X^beth` be the space
of semivaluations of coherent ideal sheaves, with pointwise-convergence
topology into `[0,+infinity]`. Write `q≤v` when `q(a)≤v(a)` for every
coherent ideal `a⊆O_X`. Let `X^div` consist of the trivial valuation and
nonnegative rational multiples of orders along prime divisors on proper
bimeromorphic models of `X` (the convention of [MP24, Definition 2.3.1]).

**Theorem.** For every `v∈X^beth`,

`v ∈ closure({q∈X^div : q≤v}).`

Equivalently, there is a net of rational divisorial points `q_λ→v` with
`q_λ≤v` for every `λ`. The assertion includes semivaluations with proper
support and semivaluations taking `+∞` on nonzero ideals; the net is not
claimed to be increasing.

**Comparison corollary.** Let `α` be a Kähler class and let
`F:X^beth→[-∞,c]` be upper semicontinuous and antitone for the above ideal
order: `q≤v` implies `F(q)≥F(v)`. If an MP potential `φ∈PSH_MP(α)` agrees
with `F` on `X^div`, then `F=φ` on `X^beth`.

**Conditional finite-energy corollary.** Assume (i) the P14.2 conclusion
that the raw ideal-valuative transform below is upper semicontinuous on all
of `X^beth`, and (ii) the normalized finite-energy comparison interface:
for every finite-energy DXZ non-Archimedean metric `Γ` in a Kähler class
`[ω]`, with `c=Γ_max`, its MP finite-energy potential `φ` satisfies
`φ(q)=F_Γ(q)` for every `q∈X^div` and `φ(0)=c`, where

`F_Γ(v)=sup_{τ<c}{τ-sup_{m≥1}(1/m)v(I(mΓ_τ))}.`

Then `F_Γ` is the MP finite-energy potential corresponding to `Γ` at every
point of `X^beth`, not only at rational divisorial points. The interface in
(ii) is the separate ray/normalization calculation of frozen Chapter 71,
equations (71.39)--(71.40); it is named here as a premise, so this corollary
does not silently infer it from the two source correspondences. The
corollary asserts neither an arbitrary pseudoeffective MP-cone statement nor
an unrestricted Kähler bijection.

The exact primary-source excerpts used by the proof are appended to its
frozen V3 packet: Mesquita--Piccione, arXiv:2409.06221v2, for the
semivaluation/divisorial facts and the divisorial comparison principle; and
Darvas--Xia--Zhang, arXiv:2302.02541v3, solely to identify the
finite-energy ray vocabulary. The normalized finite-energy equality remains
the explicit premise (ii), not an inference from either extract.

## proof

### Scope of this repaired packet

The first two assertions are proved below.  The finite-energy assertion has
two explicitly separated inputs: P14.2 supplies upper semicontinuity, and
the stated normalized interface supplies divisorial equality with the MP
potential.  It therefore proves the all-point extension of that interface,
not the interface itself.  A divisor-value sum below is over positive
coefficients only; no expression `0·(+∞)` occurs.

### 1. A dominated monomial valuation on an SNC model

Let `π:Y→X` be a proper bimeromorphic morphism of connected compact Kähler
manifolds. Pullback induces a continuous `π^beth:Y^beth→X^beth`. Its image
is closed because the source is compact and the target Hausdorff; it contains
every divisorial point by [MP24, Remark 2.3.2]. Ordinary divisorial density
[MP24, Theorem 2.3.6] then makes it all of `X^beth`. Thus each `v` has a
lift `v_tilde∈Y^beth`, including when its support is proper.

Let `B_1,…,B_k` be smooth SNC prime divisors with `v_tilde(B_i)>0`, and
choose finite rational `0<a_i≤v_tilde(B_i)`. Let `Z` be the central variety
of `v_tilde`. Its ideal is maximal among coherent ideals of positive value
[MP24, Lemma 2.1.1]; hence `Z⊆B_i`. Let `W` be the component of their
intersection containing `Z`, and let `q` be the monomial valuation along
`W` with weights `a_i`. By [MP24, Proposition 2.3.4 and Remark 2.3.5], it
is a rational divisorial point.

For `s>0` put

`c_s=sum_{β∈Z_{≥0}^k, sum_i a_iβ_i≥s} O_Y(-sum_i β_iB_i).`

After redundant generators are removed this is a finite coherent sum: its
exponent set is upward closed and every minimal exponent has
`β_i≤ceil(s/a_i)`. The semivaluation rules give

`v_tilde(c_s)=min_β sum_{i:β_i>0}β_i v_tilde(B_i) ≥ s.`

If `j` is a nonzero coherent ideal and `0<s<q(j)`, SNC coordinates show
that every transverse Taylor coefficient of weighted degree below `s`
vanishes identically along `W`; the finite set of such coefficients gives
`j⊆c_s` near `W`. Set `Q=(j+c_s)/c_s` and `k=Ann(Q)`. Then `k` is the unit
ideal near `W`, `k j⊆c_s` globally, and `v_tilde(k)=0`: otherwise maximality
of the central ideal would imply `k⊆I_Z`, impossible near `Z⊆W`. Hence

`v_tilde(j)=v_tilde(kj)≥v_tilde(c_s)≥s.`

Letting `s↑q(j)` proves `q(j)≤v_tilde(j)`; the cases `q(j)=0` and `j=0`
are immediate. Thus `q≤v_tilde` on every coherent ideal.

### 2. Finite-set approximation and the net

Fix nonzero coherent ideals `a_1,…,a_l` on `X`. Simultaneous analytic
principalization gives `π:Y→X`, with `Y` smooth compact Kähler and

`a_jO_Y=O_Y(-D_j)`, `D_j=sum_i d_{ji}B_i`, `d_{ji}∈Z_{≥0}`,

where the `B_i` form an SNC divisor. Lift `v`, and write
`w_i=v_tilde(B_i)`. Retain exactly `w_i>0`; choose positive rational
`a_i≤w_i` there and give all other components weight zero. If none remains,
use the trivial valuation. Otherwise the preceding construction gives
`q_Y≤v_tilde`; in either case `q_X=π^beth(q_Y)` is rational divisorial and
`q_X≤v`.

Multiplicativity yields

`v(a_j)=sum_{i:d_{ji}>0}d_{ji}w_i`,
`q_X(a_j)=sum_{i:d_{ji}>0}d_{ji}a_i`.

A discarded zero-weight component cannot contain `W`: because `Z⊆W`, that
would make its ideal a subideal of `I_Z` and force positive value. Its
monomial value is therefore zero, which proves the second displayed formula.
Let the finite positive weights increase rationally to `w_i`, and the
infinite weights tend to infinity. The finite sums converge in
`[0,+∞]`. For a finite set `S` and integer `N≥1`, choose the weights so
finite values in `S` are within `1/N` from below and infinite values exceed
`N`. Direct `(S,N)` by inclusion and the usual order. The resulting
`q_{S,N}≤v` converges pointwise to `v`; no relation among distinct choices
is asserted. This proves the dominated divisorial approximation theorem.

### 3. Comparison and finite-energy consequences

For the comparison corollary, fix `v` and a dominated divisorial net
`q_λ→v`. Antitonicity and divisorial agreement give
`F(v)≤F(q_λ)=φ(q_λ)`. Upper semicontinuity of `φ` gives `F(v)≤φ(v)`, also at
`φ(v)=-∞` by testing finite upper thresholds. Conversely [MP24, Theorem
4.3.8] promotes the divisorial inequality `φ≤F` to all of `X^beth`, since
`F` is upper semicontinuous. Therefore `F=φ`.

For `F_Γ`, the ideal order gives
`q(I(mΓ_τ))≤v(I(mΓ_τ))` when `q≤v`; taking the two suprema in its definition
shows `F_Γ(q)≥F_Γ(v)`. It is upper semicontinuous by premise (i), and it
agrees with the corresponding MP finite-energy potential on `X^div` by
premise (ii), including the trivial point. The comparison corollary therefore
gives `F_Γ=φ` on all of `X^beth`, as claimed.


## Attached immutable source excerpts

The following minimal excerpts are copied from the immutable local primary
texts identified below. Full-file SHA-256 values bind the excerpts to their
source copies. They are the only external interfaces used by this V3 proof:
the finite-energy equality itself remains premise (ii).

### Mesquita--Piccione — semivaluations, divisorial points, and comparison

Source: `mp_2409.06221v2.txt`
SHA-256: `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62`

> Lemma 2.1.1: for a semivaluation (v), the ideals of infinite value and
> of positive value have unique maximal coherent representatives; both are
> prime. Definition 2.1.2 calls the subvariety of the latter the central
> variety.

> Proposition 2.1.6: if (pi:Y\to X) is bimeromorphic, then
> (pi^{\beth}:Y^{\beth}\to X^{\beth}) induces a bijection
> (Y^{\rm val}\simeq X^{\rm val}).

> Definition 2.3.1 defines (X^{\rm div}) by rational nonnegative
> multiples of divisor orders, including the trivial valuation. Remark 2.3.2
> says these divisorial valuations are birationally invariant and that
> (f^{\beth}|_{Y^{\rm div}}:Y^{\rm div}\to X^{\rm div}) is bijective.

> Proposition 2.3.4 says the monomial valuation obtained from a point of the
> relevant stratum is independent of the point. Remark 2.3.5 says a monomial
> valuation attached to a rational point is divisorial.

> Theorem 2.3.6: (X^{\rm div}) is dense in (X^{\beth}).

> Theorem 4.3.8: for (phi\in\operatorname{PSH}(\alpha)) and usc
> (psi:X^{\beth}\to\mathbb R\cup\{-\infty\}),
> (phi\leq\psi) on (X^{\rm div}) if and only if
> (phi\leq\psi) on (X^{\beth}).

These excerpts supply precisely the named MP facts in Sections 1--3:
central-ideal maximality, birational divisorial transport, rational
monomial divisoriality, ordinary divisorial density, and promotion of a
divisorial inequality. The dominated approximation itself is proved in the
packet.

### Darvas--Xia--Zhang — finite-energy ray vocabulary only

Source: `dxz_2302.02541v3.txt`
SHA-256: `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244`

> Theorem 2.6(iii) gives a bijection between finite-energy maximal test
> curves and finite-energy psh geodesic rays, and identifies the radial
> (I_\theta) functional with the energy of the test curve.

This identifies the finite-energy DXZ terminology in the conditional
corollary. No statement here derives the normalized divisorial equality
(F_\Gamma=\phi); that equality is premise (ii), explicitly outside the
scope of this source-bound packet.


