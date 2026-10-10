# Strict-sublevel approximate domination — 4 October 2026

This is a conditional repair of the set-theoretic step in
arXiv:2505.11087v1, Proposition 4.8. It remains outside the active book.
Its analytic input is Li's published Fermat-family paper, Acta Math. 229
(2022), 1–53, Corollary 2.12, whose statement and proof were freshly read
together with Theorem 2.7 and its capacity argument. The input itself is a
general compact Kähler stability estimate; the Fermat geometry is not a
hypothesis of that corollary. The separately pinned acquisition record
records the publisher PDF, not an old arXiv substitute.

## Exact conditional statement

Let (X,ω) be a compact Kähler n-fold, n≥1, and write
V=∫_X ω^n. Use the same positive dd^c convention for all forms below.
Let φ,ψ be continuous ω-psh potentials. Suppose ω_φ^n is absolutely
continuous and set μ=V^{-1}ω_φ^n. Assume constants α,A,A′>0 such that

\[
 \int_X e^{-\alpha u}\,d\mu\le A
 \quad\text{for every }u\in\operatorname{PSH}(X,\omega),\quad
 \sup_Xu=0,\qquad \|\psi\|_{C^0(X)}\le A'.
\]

The absolute normalization of ψ in this display is part of the hypothesis.
Let U be measurable, suppose φ≥ψ on U, and assume μ(X\U)≤η. There is a
constant B=B(n,α,A,A′), furnished by the cited corollary. If
0≤η<(2B)^{-2n}, then

\[
 \min_X(\varphi-\psi)\ge -(4B+1)\eta^{1/(2n)}.
\]

For a varying family the conclusion is uniform if n,α,A,A′ are uniform.
Neither smoothness of ψ nor strict positivity of ω_ψ is silently imposed.
Those issues are handled by the continuous-potential form of the cited
corollary, rather than by pretending that ω_ψ is automatically a smooth
Kähler background.

## Proof and the equality-set issue

For every a>0, the closed sublevel set

\[
 E_a=\{\varphi-\psi\le -a\}
\]

is contained in X\U. The condition φ≥ψ on U is exactly enough for this
inclusion because −a<0. In contrast, it does not imply the inclusion
{φ−ψ≤0}⊂X\U: equality points in U remain in that set.
Thus μ(E_a)≤η<(2B)^{-2n}. Apply Corollary 2.12 with t₀=a to obtain

\[
 \min_X(\varphi-\psi)
 \ge -a-(4B+1)\mu(E_a)^{1/(2n)}
 \ge -a-(4B+1)\eta^{1/(2n)}.
\]

The constants do not depend on a. Sending a down to zero proves the
claim, including η=0. No assertion that the zero-level set has small
measure is needed. This is a threshold argument using the established
stability estimate, not a new analytic estimate or novelty claim.

## Application at the degeneration scale

Let T=|log|t|| and let ω_{0,t}=T^{-1}ω_{h,t} be a smooth Kähler background
on a compact fibre. Suppose the scaled potentials
φ_t=T^{-1}φ_{CY,t} and ψ_t=T^{-1}φ_{l,t} are continuous ω_{0,t}-psh,
with their scalar choices fixed by the construction. Suppose the stated
Skoda estimate holds for μ_t=ω_{φ_t}^n/∫ω_{0,t}^n with uniform α,A, and
the comparison potentials satisfy ∥ψ_t∥_{C⁰}≤A′ uniformly in all parameters
for which a uniform conclusion is requested. If φ_t≥ψ_t on U_{t,δ} and
μ_t(X_t\U_{t,δ})≤C₀δ, then for C₀δ<(2B)^{-2n},

\[
 \varphi_{CY,t}-\varphi_{l,t}
 \ge -(4B+1)C_0^{1/(2n)}T\delta^{1/(2n)}.
\]

This has the advertised scale and exponent in Proposition 4.8. Uniformity
in l requires the comparison bound A′ to be uniform in l. A proof that only
establishes A′_l for each fixed tensor power gives constants depending on l.
Transferring a Skoda bound from a background by a uniformly bounded
potential changes constants in a controlled way; it does not manufacture
such a potential bound. The required comparison-potential normalization and
uniform bound therefore remain geometric gates for the original general
argument.

## Source and admission limits

Published Theorem 2.7 first bounds a potential by the small mass of a
sublevel set under a Skoda estimate for its own normalized Monge–Ampère
measure. Corollary 2.12 states the comparison version for continuous
potentials, with constants also depending on A′. Its proof changes the
background in the smooth case and uses decreasing smooth approximation and
Dini convergence for continuous ψ. The source imports capacity and
regularization results; reading its proof is not independent certification
of all those primary dependencies.

This dossier repairs the literal closed-zero-sublevel mistake under
explicit analytic hypotheses. It does not prove the missing uniform
comparison bound, convergent meromorphic chamber bases, the general
Bergman approximation, or the principal global hybrid limit theorem.
No finite calculation is needed for the set inclusion and threshold limit.
No external model verification, new receipt, solved problem or active-book
formal theorem is claimed.
