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
