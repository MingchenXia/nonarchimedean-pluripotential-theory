# Repeated components, trace descent and the conditional ramified route

Date: 4 October 2026. This book-external note identifies the precise
failure of the reduced local argument on repeated components, proves
a continuous-psh descent reduction for \(\mathbb C((t))\subset
\mathbb C((\tau))\), \(t=\tau^q\), using finite FS families and traces,
and records a conditional hybrid-cover route. It claims no independent
verification receipt, priority, general semistable construction or
promotion of a book result or an open-problem status.

## The angular fibre and its two character lattices

For an adapted chart \(t=\prod_{i=0}^m z_i^{b_i}\), the angular fibre
is a torsor for

\[
 G_b=\ker\left((S^1)^{m+1}\longrightarrow S^1,
                          u\longmapsto\prod_i u_i^{b_i}\right).
                                                               \tag{1}
\]

If \(g=\gcd(b_i)\), it has \(g\) connected components. Its identity
component is the kernel of the primitive character \(b/g\).
This is explicitly stated in Boucksom, arXiv:2510.10239v2, physical
p. 8, Example 1.7 and (1.9). Smith normal form, or an integral change
of torus coordinates carrying \(b/g\) to a coordinate, gives (1) as
\((S^1)^m\times\mu_g\).

For an integral monomial character with exponent \(\alpha\), its
integral over the normalized Haar measure of the **whole** fibre
vanishes unless

\[
                         \alpha\in\mathbb Z b.           \tag{2}
\]

Indeed a nontrivial character has zero Haar integral by translating
with an element on which it is not one. In the torus coordinates just
described, triviality requires zero exponents in the \(m\) continuous
directions and an exponent divisible by \(g\) in the finite direction.
On a single component, the corresponding condition instead is
\(\alpha\in\mathbb Z(b/g)\). Distinct formal leading classes modulo
\(\mathbb Zb\) can therefore alias on one component.

The elementary local diagnostic \(b=(2,2)\) makes this visible.
The formal \(\mathbb C((t))\)-space spanned by \(1,z_0z_1\) has
leading values \(0,1/2\) on \(2x_0+2x_1=1\). They cannot cancel
with integer-order field coefficients. But on the single complex
component \(z_0z_1=\sqrt t\), the tuple \((\sqrt t,-1)\) cancels
identically. Whole-fibre averaging over the two signs restores
orthogonality. This is a local formal leading-mode diagnostic. It is
not asserted to be the restriction of a globally independent basis on
one geometrically integral CY family, and is not a principal-theorem
counterexample.

## Why energy alone does not repair the parent estimate

A Poincaré estimate against the mean over all components fails. A
function constant \(+1\) on one component and \(-1\) on the other
has zero local gradient and positive variance. Poincaré on each connected
component remains possible, but supplies separate means. The local
energy estimate and fibrewise psh property do not bound the difference
between these means by \(O(\sqrt T)\); a global \(O(T)\) oscillation
bound is insufficient for the later \(o(T)\) Hilbert error.

Meanwhile (2), needed for the full formal Fourier/Gram lower bound,
uses all components. Restricting to the component containing the
comparison point loses that lattice; using all components needs the
missing comparison of their potential levels. Thus inserting factors
\(b_i\) into the logarithmic metric or volume constants does not extend
the earlier reduced-SNC proof. No cross-component estimate is inferred
from a Haar average, from probability-volume convergence, or from
nonnegative curvature alone.

## A finite trace calculation for continuous psh descent

The following reduction concerns a different, global question. Let
\(K=\mathbb C((t))\), \(K'=\mathbb C((\tau))\), \(t=\tau^q\),
with \(q\geq1\). In this section use the **extended** absolute value
\(|t|=e^{-1}\), \(|\tau|=e^{-1/q}\). Let \(X/K\) be projective
and geometrically integral, and \(L\) ample. Scalar extension for
global sections, the analytic quotient
\(X_{K'}^{\mathrm{an}}/G\simeq X^{\mathrm{an}}\), and uniform FS
approximation of continuous psh metrics are explicit inputs.
Here \(G=\mu_q\) acts semilinearly and fixes \(L\).
The quotient is anchored by published BJ Section 5.9, physical p. 37;
the FS class and approximation are the imports already recorded in
`li_hybrid_limit_passage_20261004.md`. Proper field base change for
sections is also covered by the existing geometric module audit.

Let \(\Psi'\) be a \(G\)-invariant continuous psh metric on \(L_{K'}\).
Take a real-weight FS approximant using a finite globally generating
family \(s_i'\in H^0(X_{K'},lL_{K'})\), with log weights \(a_i\).
For local weights, suppress a frame of \(L\) defined over \(K\).
Its average over \(G\) is again FS: with

\[
 D=ql,\quad P_I'=\prod_{g\in G}g(s'_{i_g}),\quad
 A_I=\sum_{g\in G}a_{i_g},
 \quad I=(i_g)_{g\in G},
                                                               \tag{3}
\]

the averaged weight is

\[
 \frac1q\sum_g\frac1l\log\max_i e^{a_i}|g(s_i')|
            =\frac1D\log\max_I e^{A_I}|P_I'|.            \tag{4}
\]

The family in (3) is finite, globally generating and permuted by
\(G\), preserving \(A_I\). Products and sections are tensor products
in the indicated powers of \(L\); the displayed weights transform
correctly when the \(K\)-frame is changed.

The trace-dual coefficient formulas are

\[
 T_{Ij}=q^{-1}\operatorname{Tr}_{K'/K}(\tau^{-j}P_I')
       \in H^0(X,DL),\quad 0\leq j<q,
 \qquad P_I'=\sum_{j=0}^{q-1}\tau^jT_{Ij}.              \tag{5}
\]

To check (5), expand in the \(K\)-basis \(1,\tau,\ldots,\tau^{q-1}\).
For \(0\leq j,k<q\), the trace of \(\tau^{k-j}\) is zero if
\(k\ne j\) and equals \(q\) if \(k=j\). This remains true for
negative exponents in that range. Flat field base change identifies
the section space with \(H^0(X,DL)\otimes_KK'\).

At every analytic point upstairs, put
\(M=\max_I e^{A_I}|P_I'|\). The ultrametric inequality and (5) give

\[
 M\leq\max_{I,j}e^{A_I}|\tau|^j|T_{Ij}|.               \tag{6}
\]

Conversely, in the trace sum \(|q|=1\) and
\(|g(\tau^{-j})|=|\tau|^{-j}\). Since \(gP_I'\) is another member
with the same weight,

\[
 e^{A_I}|\tau|^j|T_{Ij}|
 \leq\max_g e^{A_I}|gP_I'|\leq M.                      \tag{7}
\]

Thus (6)–(7) are an **exact equality**, not a degree-dependent
comparability estimate. Formula (4) is the pullback of the FS metric
over \(K\) with generating sections \(T_{Ij}\) and log weights
\(A_I+j\log|\tau|\). Sections identically zero can be omitted.
They have no common zero: otherwise all \(P_I'\) would vanish by
(5), contrary to generation. Faithful scalar extension transfers
this generation back to \(X\). Rational input weights give rational
output weights since \(\log|\tau|=-1/q\); real weights also pose no
problem and admit uniform rational approximation.

Averaging an FS approximant cannot increase its uniform distance to
the invariant metric \(\Psi'\). Its exact descended FS metric has
the same uniform distance to the descended continuous metric, because
the analytic quotient map is onto. Taking a uniformly convergent
sequence proves that the latter metric is continuous psh. This proves
the required positivity descent in this particular cyclic, residue-
characteristic-zero extension without assuming descent of arbitrary
model functions. It does not remove Chapter 30's general model-descent
condition for arbitrary fields, noncontinuous metrics or all model
functions. No claim for wild or mixed characteristic is made; \(|q|=1\)
and the trace-dual basis are used explicitly.

## Normalize the ramified hybrid map before descending

Now return to a meromorphic complex family. Assume a supplied finite
cover \(t=\tau^q\), followed by proper model modifications, has a
**regular reduced SNC projective model**, and that all inputs of the
previous reduced-model analytic/FS/hybrid derivations have been checked
for that cover. This is a conditional input, not a construction here.
Normalized base change of an SNC model is merely toroidal in BJ
Section 5.9. It need not already be regular or reduced. The existence
of semistable reduction is an explicit KKMSD import in BJ Remark 7.2,
physical p. 45; the KKMSD primary proof is not newly checked here.

Use the original reference metric pulled back on nonzero complex
fibres, and put

\[
 T_t=qT_\tau,\qquad
 u'_\tau=\varphi_{\tau^q}/T_\tau=q\,u_{\tau^q}.          \tag{8}
\]

If a positive reference on the modified cover is used for the analytic
estimates, the passage back to this reference must also be checked.
A smooth hybrid model-reference difference has a continuous scaled
limit. Add it to the resulting continuous normalized potential and
normalize by its fibre supremum. Properness and the every-small-fibre
central-neighborhood property from the prior hybrid proof show that
these suprema converge to the central supremum: properness bounds the
limsup, and a neighborhood of a central maximizer bounds the liminf.
This gives the same continuous extension in the original reference.
An unverified \(O(T)\) reference bound alone would not suffice for
this continuity step. Smooth punctured-family dependence is also
retained as an explicit input.

Let \(Y',Y\) be the compact Hausdorff hybrid spaces over matched
closed discs. The natural map \(P:Y'\to Y\) sends a nonzero complex
point to the same fibre point at \(t=\tau^q\). On the central fibre,
source valuations normalized by \(\operatorname{ord}(\tau)=1\)
are restricted to the original field and divided by \(q\), to
normalize \(\operatorname{ord}(t)=1\). The published identity

\[
                   \phi_{\rho^*D}=q\,p^*\phi_D           \tag{9}
\]

in BJ (5.7), physical p. 37, is precisely this convention for model
functions. It differs from base extension with the already extended
absolute value used in (3)–(7).

Continuity of \(P\) follows by the model/FS description of the hybrid
topology: a pulled-back model or section log test on the complex
part is the original log test multiplied by \(q\) under the source
\(1/T_\tau\) scaling; on the centre (9) gives the same factor.
The parameter map is \(\tau\mapsto\tau^q\). Cofinality of common
models supplies these tests in every chart; their topology and
compatibility are the prior explicit imports. The analytic central
quotient and the complex cover show that \(P\) is onto and its fibres
are precisely \(G\)-orbits. Hence the induced continuous bijection
\(Y'/G\to Y\) is a homeomorphism, by compactness and Hausdorffness.
No first-countability or sequential compactness is used.

The earlier conditional chain yields a continuous extension of
\(u'\) on \(Y'\), with central semipositive metric. On the punctured
part \(u'\) is \(G\)-invariant by (8). Density of that part and
continuity imply invariance on the whole space. Therefore
\(u'/q\) descends to a continuous function on \(Y\), equal to the
original \(u_t\) for \(t\ne0\), with central potential

\[
                        v\circ p=v'/q.                 \tag{10}
\]

To check central positivity, first renormalize the entire child metric
(reference and potential together) from \(|\tau|=e^{-1}\) to
\(|\tau|=e^{-1/q}\). All local log weights divide by \(q\), so
FS metrics and their uniform closure remain psh. This is a metric
on the same line bundle over the extended absolute value, not a
division of the potential while leaving the reference unchanged.
Apply the trace descent (3)–(7) to this invariant continuous psh
metric. It gives the continuous psh parent metric in (10).

## Probability measures and the equation after descent

The complex probabilities on corresponding fibres are identical.
The raw-volume discrepancy has \(\kappa'=q\kappa\), while
\(T_t=qT_\tau\). Consistently, BJ Theorem 6.7, physical p. 42,
states for its unnormalized skeletal measures

\[
                         p_*\Lambda'_0=q^m\Lambda_0.   \tag{11}
\]

Its residue calculation uses \(dt/t=q\,d\tau/\tau\);
Lemma 6.8, physical pp. 42–43, keeps the associated squared factor.
Dividing both measures by their own total masses cancels \(q^m\):
\(p_*\mu'_0=\mu_0\). This is independent volume convergence,
not a consequence of potential compactness.

The descended full-family continuous hybrid psh metric meets the
hypotheses of the prior MA passage, including its convention and test
function checks. Boucksom's Theorem 7.11 in the already checked version
then identifies its probability MA with \(\mu_0\), and NA uniqueness
identifies the normalized central potential. Equivalently the book's
finite-ground-field MA pushforward with the extended absolute value
gives this equation. Neither route introduces an extra \(q^n\) into
a probability measure.

## Remaining gates and boundary checks

This removes the disconnected angular obstruction by applying the
analytic argument on a supplied reduced model and descending its
**continuous** limit. It does not solve that obstruction directly on
the original nonreduced chart. The trace argument also allows a point
or \(q=1\); the dyadic analytic application still requires
\(1\leq m\leq n\), positive probability mass and the smooth connected
projective CY/section hypotheses. Nonprojective families, wild or mixed
characteristic, unbounded psh descent and generic singular/disconnected
families are outside the signature.

The semistable/projective model and meromorphic bundle presentations,
proper analytic/cohomological comparisons, uniform Skoda, potential
regularity and the cited hybrid/MA imports remain application gates.
All earlier fixed-degree radii remain degree dependent. A complete
model-category application and exact-current independent verification
are required before any general CY result enters the book. Chapter 30's
existing conditional statements and all 42 problem statuses remain
unchanged; the trace calculation is a research reduction here.
