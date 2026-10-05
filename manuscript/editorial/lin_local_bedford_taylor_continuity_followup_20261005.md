# Local Bedford–Taylor continuity after the coefficient check — 5 October 2026

This follow-up completes the selected-source convention checks left open in
[the coefficient-domain note](lin_polyhedral_coefficient_boundary_20261005.md).
It records a direct route to the conclusion of Lin v1 Proposition 8.3 using
the ambient Lagerberg Bedford–Taylor theorem and Mihatsch's divisor product.
It is a research derivation from identified literature inputs, outside the
active TeX closure. No independent production-verifier receipt, new theorem
promotion, repair of Lin's complete main theorem, or solution of the general
Siu problem is claimed.

## Sources and exact comparison

The controlling intersection source is Andreas Mihatsch, *On tropical
intersection theory*, Selecta Mathematica (2023) 29:17,
[DOI 10.1007/s00029-022-00818-7](https://doi.org/10.1007/s00029-022-00818-7).
The publisher PDF was acquired successfully and its title, DOI, page count
and digest checked. Its Definition 2.1 and Example 2.2, page 7, allow real
polyhedra with weights; Proposition 2.8, page 10, is the Stokes identity.
Theorem 3.3, pages 12–14, identifies balanced polyhedral currents with
delta-forms. Lemma 3.7 and Example 3.8, page 15, allow multiplication by
piecewise smooth functions. Definition 4.6 and Remark 4.7, page 22, give
the potential formula for a closed current; Lemma 4.9, page 23, gives its
facet coefficients. Theorem 4.1, pages 18–19, identifies the full wedge
formalism; its proof's Leibniz step is on pages 27–28. The divisor formula
needed below already has a direct definition in 4.6 and reduction in 4.7.

The controlling Bedford–Taylor witness remains Burgos Gil–Gubler–Jell–
Künnemann, [arXiv:2102.07392v1](https://arxiv.org/abs/2102.07392v1),
Definition 3.1.2 and Theorem 4.1.2, physical pages 13 and 20–21. The
theorem and its complete printed proof were read in the preceding check.
No identity with the inaccessible published 2025 PDF is asserted.

For the current conventions, an additional primary witness was acquired:
the same authors, *A comparison of positivity in complex and tropical
toric geometry*, [arXiv:2003.08644v1](https://arxiv.org/abs/2003.08644v1).
Remark 3.2.9 and the integration definition on page 19 give exactly the
same derivative signs and lattice integral as Mihatsch's equations
(2.5), (2.7) and (2.11). Proposition 5.1.16, page 32, identifies positive
top-degree currents with positive Radon measures. Proposition 5.2.6,
page 33, proves that positive Lagerberg currents have Radon measure
co-coefficients. These selected statements and their printed proofs were
read. Examples 5.2.7–5.2.8, page 34, explicitly warn that the analogous
assertion for merely weakly positive currents is false. Positivity below
is the source's positive cone, not only its weakly positive cone.

Lin's [arXiv:2609.12969v1](https://arxiv.org/abs/2609.12969v1),
Definition 8.1, page 18, defines the piecewise affine measure by precisely
Mihatsch's wedge product. Proposition 8.3, pages 22–23, asks for continuity
for convex functions on the entire ambient vector space. The compatibility
calculation in Proposition 8.5, equation (11), page 24, is the same
potential identity used below. Here that identification is made before
the limit is taken; equation (12), whose printed proof invokes 8.3, is
not used as an input to prove 8.3.

## Setting and integration current

Fix a lattice \(N\simeq\mathbf Z^n\), its real vector space
\(N_{\mathbf R}\), and an ambient open subset \(\Omega\). Let \(C\) be
the restriction to \(\Omega\) of a locally finite balanced weighted
\((\mathbf Z,\mathbf R)\)-polyhedral complex of pure dimension \(d\),
with nonnegative real weights \(m_\sigma\) on its maximal faces. Facet
positions may be real. The tangent lattice is
\(N_\sigma=N\cap\operatorname{span}_{\mathbf R}(\sigma-\sigma)\).
Normalize face integration by a basis of this lattice, so

\[
 T=\delta_C=\sum_{\dim\sigma=d}m_\sigma[\sigma,\mu_\sigma]
\]

has bidegree \((n-d,n-d)\). Local finiteness ensures that this is a
well-defined order-zero current. The locally finite support is closed
relative to \(\Omega\). Subdividing a face preserves its integral and
tangent lattice and hence this current.

The current is symmetric and positive in the BGJK sense. Indeed, a
positive test form restricted to the tangent space of a face is a sum
of nonnegative scalar squares times its positive lattice volume form;
integration against \(m_\sigma\geq0\) preserves that sign. The
Lagerberg involution gives the required symmetry on each face. This
checks the actual positive cone used in the imported theorem.

Both derivatives of \(T\) vanish. In Mihatsch's terminology \(T\) has
tridegree \((0,0,n-d)\). Its coefficients are constant, so its
polyhedral derivatives vanish. Theorem 3.3 applies by balancing, while
the boundary operators have tridegrees that would give a negative
form degree in this case; equivalently all contractions of the scalar
coefficients in equation (3.9) vanish. Thus

\[
 d'S=d''S=0\quad\text{for }S=T.
\]

This is also the facet cancellation in Proposition 2.8: the sum of
weighted normals is tangent to the facet and its contraction of the
test form restricts to zero there. No rationality of the affine constants
is needed. This clears the real-facet issue left explicit in the earlier
note, without changing the book's existing rational Stokes statement.

## Potential identity before continuity

Let \(h\) be a finite convex continuous piecewise affine function on
the ambient space. Rational or integral slopes are not needed for the
identity. Let \(S\) be a positive closed polyhedral delta-form on
\(\Omega\). Its measure coefficients allow the ordinary multiplication
\(hS\). In particular, Mihatsch's piecewise smooth product in Example
3.8 is exactly this multiplication for the scalar continuous function
\(h\); it is not a product of arbitrary distributions.

The two constructions satisfy

\[
 (d'd''h)\wedge_{\rm BT}S
       =d'd''(hS)
       =(d'd''h)\wedge_\delta S.                     \tag{1}
\]

For the first equality, work on a relatively compact ambient ball and
smooth the convex function by convolution with a nonnegative compactly
supported smoothing kernel. On a smaller ball the smooth convex
functions \(h_\varepsilon\) converge uniformly to \(h\). For each
smooth approximant, the usual current product rule and closure of
\(S\) give

\[
 (d'd''h_\varepsilon)\wedge S=d'd''(h_\varepsilon S).
\]

BGJK v1 Theorem 4.1.2(ii) identifies the limit on the left with the
Bedford–Taylor product. On the right, locally uniform convergence and
the order-zero property give \(h_\varepsilon S\to hS\) as currents;
distributional differentiation is continuous. This proves the first
equality locally and hence on \(\Omega\). This step uses the fixed
current \(S\), not continuity of polyhedral intersection measures.

For the second equality, apply Mihatsch Definition 4.6 with
\(D=d'd''h\). Remark 4.7 removes all three terms containing derivatives
of \(S\) because \(d'S=d''S=0\). Its result is the delta-form divisor
product and agrees with the wedge of Theorem 4.1. Lemma 4.9 computes
the same coefficients on facets, with the chosen lattice calibration.
Thus (1) matches Lin Definition 8.1 literally at the piecewise affine
stage. The potential is already supplied here; no general existence
claim about potentials for arbitrary divisors is required.

Starting with \(S_0=T\), define the mixed products inductively. If
\(h_1,\ldots,h_j\) are convex piecewise affine, equation (1) gives

\[
 S_j=(d'd''h_j)\wedge_{\rm BT}S_{j-1}
     =(d'd''h_j)\wedge_\delta S_{j-1}.
\]

The Bedford–Taylor construction supplies positivity and closure; the
delta-form side supplies a polyhedral current, so the hypotheses needed
at the next step are retained. Induction up to \(j=d\) therefore
identifies the top-degree mixed current, and in particular

\[
 \operatorname{MA}_{{\rm poly},C}(h)
   =(d'd''h)^{\wedge_\delta d}\wedge_\delta\delta_C
   =(d'd''h)^{\wedge_{\rm BT}d}\wedge_{\rm BT}\delta_C. \tag{2}
\]

## Limit and locality

Use the smooth fan \(\{0\}\), whose tropical toric space is
\(N_{\mathbf R}\). There is no toric boundary condition to check.
Finite convex ambient functions are finite continuous psh functions in
BGJK v1 Definition 3.1.2. Set \(p=n-d\) and \(q=d\) in Theorem
4.1.2. For a locally uniformly convergent sequence of finite convex
functions \(f_i\to f\), with \(T\) fixed, its part (ii) gives

\[
 (d'd''f_i)^{\wedge_{\rm BT}d}\wedge_{\rm BT}T
     \longrightarrow
 (d'd''f)^{\wedge_{\rm BT}d}\wedge_{\rm BT}T.        \tag{3}
\]

These are positive top-degree currents, hence positive Radon measures
by BGJK20 v1 Proposition 5.1.16. They are supported on \(|C|\):
the starting current vanishes outside \(|C|\), and both the local
product and its limit vanish on every open subset where it vanishes.
If the \(f_i\) are piecewise affine, equation (2) identifies the left
side of (3) with the measures in Lin Proposition 8.3. Its global uniform
convergence assumption is more than the local uniform convergence
required here. Its bounded difference from a rational reference is
not needed for this local measure conclusion.

Weak convergence on smooth ambient test functions gives the exact
continuous-test convergence requested there. If \(\varphi\in
C_c(|C|)\), extend it continuously to the ambient space and multiply
by a compactly supported cutoff equal to one on its support. The
result agrees with \(\varphi\) on \(|C|\). Approximate this extension
uniformly by smooth functions with support in one fixed compact set
\(K\subset\Omega\). Choose a nonnegative smooth cutoff at least one
on \(K\). Current convergence on that cutoff bounds all sufficiently
late approximating measures' masses on \(K\); the finitely many earlier
terms also have finite mass there. The uniform approximation error in
the integrals is bounded by that common mass times the uniform error.
This proves convergence against \(\varphi\), and identifies its limit
with the positive Radon measure on the right of (3). The latter depends
only on \(f\) and \(T\), proving independence of the approximating
sequence.

Locality also follows directly from Theorem 4.1.2. Equal functions and
equal weighted integration currents on an ambient open set give equal
products there. This supplies the comparison required by Lin Definition
8.4 without passing through BMPS regularizability. For \(d=0\), the
measure is simply the fixed weighted zero-cycle \(T\); no Bedford–Taylor
factor is needed. Zero weights and the zero current are included.

## Calibration and exclusions

In lattice coordinates, both sources integrate
\(a\,d'x_1\wedge d''x_1\wedge\cdots\wedge d'x_n\wedge d''x_n\)
as the lattice-normalized Lebesgue integral of \(a\). Their derivative
signs agree. Thus in dimension one
\(d'd''\max\{0,x-a\}=\delta_a\). In dimension two, with weight-one
ambient cycle and

\[
 h(x,y)=\max\{0,x-a\}+\max\{0,y-b\},
\]

the two transverse unit-weight divisor factors and graded commutativity
give \((d'd''h)^2=2\delta_{(a,b)}\). The factor is \(2!\), matching the
area-one subgradient square. Mihatsch Lemma 4.17, page 29, provides the
transverse calibration as well. Replacing \(h\) by \(h/2\) gives
\(\tfrac12\delta_{(a,b)}\); clearing the denominator and dividing the
result by \(2^2\) recovers the same measure. In general the top-degree
tensor-exponent factor is \(m^d\), not \(m\). These are symbolic
normalization checks, not a new computational verifier receipt.

The argument uses finite continuous convex ambient functions, positive
closed currents and locally uniform sequence convergence. It makes no
assertion about singular infinite-valued potentials, monotone nets of
arbitrary psh functions, signed unbalanced cycles, obstacle envelopes,
or metrics near added toric boundary strata. It does not establish the
analytic germ, skeleton or pullback inputs of Lin Theorem 10.2. It does
not identify the corrected ambient product with BMPS's literal integral-
slope uniform closure, and does not remove that coefficient diagnostic.
No step imports BJ22 Theorem 6.21 or any conditional Siu/envelope result.

## Evidence and admission boundary

Twenty-two additional selected primary pages were actually viewed in
six contact sheets: sixteen from the published Mihatsch PDF and six
from BGJK20 v1. The earlier selected BGJK21 v1 and Lin views remain
dated evidence; they were not all freshly rendered again. Relevant
target statements and printed proofs were read, including the Stokes/
balancing reduction, piecewise smooth multiplication, divisor potential
and facet identities, current integration signs, positive coefficient
measures and the continuous-test extension. Full fresh readings of
Mihatsch and BGJK20 are not claimed. The deep complex comparison and
complex Bedford–Taylor proofs imported by BGJK21 are not all newly
audited here.

The companion manifest preserves source hashes, locators, actual page
views, the proof order and unchanged active-source/artifact checks.
This is an explicit derivation from known inputs and a reordering of
the compatibility calculation already in Lin Proposition 8.5, with no
priority claim. A new general book-level result, if proposed as one,
must still meet the repository's verification protocol. No model call,
independent admission verdict, changed active problem status, active
TeX insertion or rebuilt book is recorded by this follow-up. Continue
the revision-sensitive arXiv search and noncircular Siu investigation.
