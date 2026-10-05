# Entropy under a change of class: an unverified toric candidate

**Research-only author calculation; production status OPEN.**
This file is not an active TeX input, a theorem receipt, a verified
counterexample, an assertion of novelty or a retirement of a book problem.
It follows the known-result checkpoint `cbae440` and records an explicit
candidate for further adversarial verification. No independent model call
or production-verifier verdict has been obtained for these bytes.

The repository's [verification protocol](../rethlas_verification_protocol.md)
requires an independent production audit before promoting an original
mathematical result. The requested verifier setting is `gpt-6.1-sol xhigh`.
The presently callable cloud tools provide no such production-verifier
entry point. This draft preserves the proposed proof for a future audit;
the ongoing primary-source and known-result work continues separately.

## Question, category and proposed signature

Di Nezza–Trapani–Trusiani ask whether finite Monge–Ampère entropy for a
smooth big form theta survives replacing theta by theta+t tau, with tau
Kähler and t>0. Their published SIGMA 20 (2024), 039, DOI
[10.3842/SIGMA.2024.039](https://sigma-journal.com/2024/039/), contains
Question 1.1 on actual page 3 and the same Question 3.11 on actual page 17.
Proposition 3.12 on actual pages 17–18 keeps a finite-entropy premise at
one positive perturbation. The paper explicitly separates absolute
continuity of the original top measure from that of the mixed measures.

The proposed negative example lives on the connected smooth projective
surface X=(P^1)^2 over C. It would use a genuine smooth Kähler theta and
a globally bounded continuous theta-psh function u. Its original top
measure would have full mass and finite entropy against a smooth positive
probability volume, while the top measure in theta+t tau would have a
nonzero singular part for every t>0. Thus no zero mass, potential pole,
singular variety or non-pluripolar removal is intended to cause the failure.

Use the book convention ddc=i partial partialbar/(2 pi). On the dense
torus put x=log|z_1|^2 and y=log|z_2|^2 and write angular Haar measure as
dH=(d vartheta_1/(2 pi))(d vartheta_2/(2 pi)). All logarithmic-coordinate
densities below are interpreted with this product measure.

## A smooth flat profile and a convex local potential

Set

\[
 \eta(s)=
 \begin{cases}
  \exp[-1/s-1/(2-s)],&0<s<2,\\
  0,&s\notin(0,2),
 \end{cases}
 \qquad L=\int_0^2\eta(s)\,ds<2e^{-2}<1.
\]

Define a_0(s)=0 for s<=0 and
a_0(s)=integral_0^s (s-t) eta(t) dt for s>0. This is a smooth convex
nondecreasing function, with 0<=a_0'<=L, a_0''=eta and
0<=a_0(s)<=L s. It becomes affine after s=2. Set

\[
 a(y)=a_0(|y|-1),\qquad U(x,y)=\sqrt{x^2+a(y)^2},
 \qquad K=\{0\}\times[-1,1].
\]

The absolute value in a causes no lack of smoothness at y=0 because a is
identically zero nearby. Flatness of eta makes a smooth also at y=+/-1
and +/-3. The function a is nonnegative and convex: on each half-line
its derivative is monotone, and it vanishes on [-1,1]. The Euclidean
norm on the positive quadrant is convex and nondecreasing in each
coordinate. Applying it to the convex functions |x| and a(y) proves that
U is convex. It satisfies U<=|x|+L|y| and is smooth off K.

At every point of K its full convex subdifferential is
[-1,1]x{0}. In the interior of the segment this follows from U=|x|
locally. At either endpoint, a_0(s)=o(s) implies that the directional
derivative is |v_x|, so the vertical component is still zero. Consequently
the union of subgradients over K has two-dimensional Lebesgue measure
zero. The Alexandrov top measure charges no part of K, including its
endpoints.

Off K, put R=sqrt(x^2+a^2). Direct differentiation gives

\[
 U_{xx}=\frac{a^2}{R^3},\qquad
 U_{xy}=-\frac{xaa'}{R^3},\qquad
 U_{yy}=\frac{aa''}{R}+\frac{(a')^2x^2}{R^3},\qquad
 F:=\det D^2U=\frac{a^3a''}{(x^2+a^2)^2}.
\]

These formulas also show positivity of the Hessian where R>0. On the
open strip |y|<1, outside x=0, U=|x| and F=0. Thus the only possible
singular Alexandrov measure is on K, where the subgradient calculation
already makes it zero. This last assertion must be checked at the measure
level; simply computing the almost-everywhere determinant would not suffice.

## Global gluing in a genuine Kähler class

Use the torus potential

\[
 \Phi(x,y)=4\log(2\cosh(x/2))+4\log(2\cosh(y/2)),
 \qquad\theta=\ddc\Phi.
\]

Since 4 log(2 cosh(x/2))=4 log(1+|z_1|^2)-2x, its last term is
pluriharmonic on the torus. Hence theta extends to
4(omega_FS,1+omega_FS,2) on (P^1)^2, with each Fubini–Study factor of
area one. It is Kähler and its volume is M=32. Moreover,
Phi>=2(|x|+|y|), Phi_xx=sech^2(x/2)>0 and likewise for y.

Fix delta>0. Let rho_delta be an even smooth convex regularization of
|q|, equal to |q| for |q|>=delta, with |rho_delta'|<=1. For example,
convolve |q| with an even nonnegative smooth probability kernel supported
in (-delta,delta). Define

\[
 \mathcal M_\delta(s,t)=\tfrac12(s+t+\rho_\delta(s-t)),
 \qquad W=\mathcal M_\delta(U,\Phi-C),
 \qquad u=W-\Phi,
\]

where C>max_K Phi+2 delta. The regularized maximum is convex and
nondecreasing in both arguments, so W is convex. On a neighborhood of K
it equals U. Since Phi-C-U>=|x|+|y|-C tends uniformly to infinity,
W=Phi-C outside a compact subset of R^2. The transition region is compact
and disjoint from K, where both input functions are smooth. Thus W is
smooth off K and creates no nonsmooth transition interface.

The function u is bounded and continuous on the torus and equals -C
whenever (x,y) leaves that compact set. It therefore extends by the
constant -C to an open neighborhood of every boundary divisor of (P^1)^2.
On the torus theta+ddc u=ddc W is positive because W is convex; near the
boundary it equals theta. This verifies the proposed global theta-psh
condition without gluing an arbitrary local psh germ directly across a
chart boundary. Its boundedness gives the ordinary Bedford–Taylor
product, full mass M and equality with the non-pluripolar product.

## Real/complex normalization and finite entropy

In the chosen squared-log coordinates a smooth toric potential V has

\[
 (\ddc V)^2=2\det D^2V\,dx\,dy\,dH.
\]

Coman–Guedj–Sahin–Zeriahi, arXiv:1804.03387v1, Lemma 2.2 on actual and
printed pages 6–7, gives the smooth-to-convex approximation that identifies
this with the Alexandrov measure for nonsmooth convex V. Their source
uses log|z| and ddc_s=2 ddc_b. Apply that identity to
V_s(l)=V_b(2l)/2: ddc_s V_s(l)=ddc_b V_b(2l), while the Hessian and
Lebesgue changes give exactly the displayed factor 2. Torus invariance
supplies angular Haar measure. Section 1.1 on actual page 4 records the
bounded Bedford–Taylor mass and convergence properties; actual page 5
records that bounded potentials have full mass. These arXiv locators are
not the pagination of the separately published 2019 article.

Let T=theta+ddc u. Its top measure is smooth with bounded density away
from K in the compact transition region and equals theta^2 outside that
region. Near K its density is 2F, with no extra measure on K. The smooth
reference density B=2 Phi_xx Phi_yy is bounded above and below by positive
constants on any fixed compact logarithmic region. It is therefore enough
to check integral F log_+F dx dy locally near the two endpoints of K.

Write s=|y|-1>0 close to zero. Then a''=eta(s). At x=a t,

\[
 F\,dx=\frac{\eta(s)}{(1+t^2)^2}\,dt,
 \qquad F\leq\frac{\eta(s)}{a(s)},
 \qquad
 \int_{\mathbb R}F\log_+F\,dx
 \leq\frac\pi2\eta(s)\log_+\frac{\eta(s)}{a(s)}.
\]

For 0<s<=1/2 restrict the defining integral for a_0(s) to
t in [s-s^2,s-s^2/2]. There s-t>=s^2/2, the interval length is s^2/2,
and

\[
 \eta(t)\geq e^{-2}\eta(s),\qquad
 a_0(s)\geq\frac{e^{-2}}4s^4\eta(s),\qquad
 \frac{\eta(s)}{a_0(s)}\leq4e^2s^{-4}.
\]

The first inequality follows from 1/t-1/s<=2 and
1/(2-t)<=1/(2-s). The resulting entropy bound is a constant times
eta(s)(1+|log s|), which is integrable. Away from s=0, a is positive
and smooth, so there is no remaining logarithmic singularity. The same
argument applies at both endpoints. For a probability density the negative
entropy part is bounded by 1/e and poses no additional issue.

Set tau=theta/sqrt(32), so nu=tau^2=theta^2/32 is a smooth probability
volume. The original probability measure is mu=T^2/32, with density
g=det D^2W/(Phi_xx Phi_yy) on the torus. The preceding calculation is
the proposed proof that Ent(mu,nu)<infinity.

## The mixed singular measure after perturbation

Choose a small open rectangular neighborhood of (0,0) on which W=U=|x|
and |y|<1. In squared-log coordinates,

\[
 T=2\delta_0(x)\,dx\wedge\frac{d\vartheta_1}{2\pi},
 \qquad T^2=0,
 \qquad
 T\wedge\theta
 =2\Phi_{yy}(y)\delta_0(x)\,dx\,dy\,dH.
\]

The last measure is positive and nonzero on x=0, a smooth-volume null
real hypersurface. It follows either by distributional differentiation of
|x| or by smooth convex approximations there. Its support is not a pole
locus of u, and bounded Bedford–Taylor products do not discard it.

For t>0 put q=t/sqrt(32). Multilinearity for bounded potentials gives

\[
 \langle(\theta+t\tau+\ddc u)^2\rangle
  =(T+q\theta)^2
  =T^2+2qT\wedge\theta+q^2\theta^2.
\]

All summands are positive. Thus the proposed perturbed top measure has
a nonzero singular part for every t>0; no cancellation can remove it.
Its own positive full mass is 32(1+q)^2, and dividing by this mass does
not make the singular part absolutely continuous. Its proposed entropy
against nu is therefore infinity. Subtracting a constant from u to adopt
the source's supremum normalization changes none of these measures.

## Diagnostics, boundaries and pending verification

The symbolic determinant remainder was exactly zero. The profile integral
was pi/2 and the reference slope jump was four. These checks diagnose
algebra and normalization only; they are not an independent proof audit.

An earlier exploratory reference using log(2 cosh x) was unsuitable: in
squared-log coordinates it comes from a branched z^2 pullback and gives
only a semipositive extension at the divisors. The present Phi uses x/2
and the genuine Fubini–Study form. A bare maximum would create another
nonsmooth interface; the compact smooth regularized maximum is essential.
An almost-everywhere Hessian calculation alone would miss a possible
singular Alexandrov measure; the complete subgradient computation over K
is essential. No general conclusion is drawn merely from positivity of a
mixed Monge–Ampère measure.

This candidate tests dimension two. Dimension one has a positive answer
by adding a smooth measure to a finite-entropy measure. The construction
does not address a zero-volume class, a singular/non-normal space,
positive or mixed characteristic, nonprojective Kähler geometry, or the
non-Archimedean setting. Its category is a compact metrizable smooth
complex projective surface with a fixed positive volume and bounded
potential. No sequential compactness outside that category is invoked.

Targeted searches on 5 October 2026 for the source's questions, finite
entropy under class perturbation, mixed absolute continuity and toric
counterexamples did not locate a checked resolution. They did locate the
original source and the toric primary input above. This is not an
exhaustive absence or priority claim. The broader Guedj–Lu and August
uniform-estimate work remains separate.

Before any promotion, an independent verifier must examine the exact
statement/proof bytes, especially global convex gluing, all subgradients
at K's endpoints, identification of the nonsmooth complex top measure,
and the L log L bound. The original Bedford–Taylor/Alexandrov load-bearing
inputs also need full locator clearance for the chosen submission.
The candidate has no production-verifier digest or receipt. In the
protocol's five-verdict ledger, this submission is OPEN; VERIFIED,
CONDITIONAL, DISPROVED and RETRACTED have no production verdict here.
The counterexample wording above describes the proposal, not an admitted
DISPROVED result. All active-book files, the 86-page native catalogue and
all canonical problem statuses retain checkpoint `cbae440`.
