# Uniform comparison bound by truncation — 4 October 2026

This continues the [strict-sublevel argument](li_strict_sublevel_repair_20261004.md).
The extra uniform C⁰ bound for the original comparison potential can be
replaced by a uniform bound for a truncated comparison. The proof uses
Li's published Acta Math. 229 (2022), Theorem 2.7(ii) and Corollary 2.12,
both freshly read at the preceding source checkpoint. It is recorded as a
derived conditional argument outside the active book, with no novelty,
external-model verification or principal convergence claim.

## Hypotheses

Let (X,ω) be a compact Kähler n-fold, n≥1, let φ,ψ be continuous ω-psh,
and suppose μ=ω_φ^n/∫ω^n is absolutely continuous. Assume fixed α,A>0
such that

\[
 \int_Xe^{-\alpha u}\,d\mu\le A
 \quad\text{for every }u\in\operatorname{PSH}(X,\omega),\quad\sup_Xu=0.
\]

Normalize sup_X φ=0. Suppose φ≥ψ on a measurable set U and
μ(X\U)≤η≤1/2. No uniform lower bound for ψ is assumed. Taking u=0
shows A≥1.

## Upper bound for the comparison and a bounded truncation

Theorem 2.7(ii) gives −C_φ≤φ≤0, where C_φ depends only on n,α,A.
Set M=sup_X ψ, which is finite because ψ is continuous on compact X.
The test ψ−M is ω-psh with zero supremum. On U, ψ≤φ≤0, hence

\[
 A\ge\int_Xe^{-\alpha(\psi-M)}\,d\mu
 \ge\mu(U)e^{\alpha M}
 \ge(1-\eta)e^{\alpha M}.
\]

Therefore

\[
 M\le\alpha^{-1}\log\frac{A}{1-\eta}
 \le\alpha^{-1}\log(2A)=:C_\psi.
\]

Define ψ̂=max{ψ,−C_φ}. Maxima of two continuous ω-psh potentials are
continuous ω-psh: after adding a local potential of ω, this is the usual
maximum property for psh functions. Consequently

\[
 -C_\varphi\le\widehat\psi\le C_\psi,\qquad
 \|\widehat\psi\|_{C^0}\le A':=\max\{C_\varphi,C_\psi\}.
\]

This A′ depends only on n,α,A, including for a varying family with uniform
Skoda data. Also φ≥ψ̂ on U, since φ≥ψ there and φ≥−C_φ everywhere.
The truncation may have a corner; the cited stability corollary explicitly
allows continuous comparison potentials.

## Uniform approximate domination

Let B=B(n,α,A,A′) be the constant in Corollary 2.12. If additionally
η<(2B)^{-2n}, then for every a>0,

\[
 \{\varphi-\widehat\psi\le-a\}\subset X\setminus U.
\]

The corollary gives

\[
 \min_X(\varphi-\widehat\psi)
 \ge-a-(4B+1)\eta^{1/(2n)}.
\]

Let a decrease to zero. Since ψ̂≥ψ, one has pointwise
φ−ψ≥φ−ψ̂. It follows that

\[
 \min_X(\varphi-\psi)\ge-(4B+1)\eta^{1/(2n)},
\]

with B depending only on n,α,A. The conclusion includes η=0.
For η=C₀δ, multiplying scaled potentials by T=|log|t|| gives the
Tδ^{1/(2n)} lower-bound scale. No constant acquires a tensor-degree
dependence through an unproved lower bound for ψ.

## Normalization in the canonical-basis construction

At a fixed fibre, adding the same scalar to φ and ψ leaves φ−ψ and their
curvatures unchanged. In the Section 4.4 construction, changing the
Calabi–Yau potential by a scalar changes the defining supremum coefficients
and the max-Fubini–Study potential by exactly the corresponding scalar.
Thus both can be shifted together to impose sup φ=0, while keeping φ≥ψ
on the generic region. This scalar change is made in the scaled potential
convention. It neither imposes parameter-psh dependence nor changes the
normalized Calabi–Yau measure.

Provided the constructed comparison is globally continuous ω-psh (in
particular, its section family has no common zero on the fibre), and the
uniform Skoda estimate and generic-region mass estimate have their stated
hypotheses, the lower-bound step no longer needs a separate uniform
comparison-potential lower bound. Those section-generation, geometric
mass and Skoda inputs remain explicit. For a fixed sufficiently large
tensor power, the convergent chamber transfer and inverse-minor family
address the finite section-generation route separately.

This argument does not verify the general global Bergman estimate, all
hybrid approximation hypotheses or the principal claim of
arXiv:2505.11087v1. It changes no book theorem, verifier receipt or
open-problem status. No finite numerical calculation is needed for this
threshold and truncation argument.
