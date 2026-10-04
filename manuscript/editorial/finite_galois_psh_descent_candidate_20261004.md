# Candidate finite psh descent through orbit coefficients

Date: 4 October 2026. Baseline: `c5f7bf7`.
Status: exploratory candidate, outside the active TeX closure.
There is no independent production-model receipt. The normal Siu input,
the book's conditional interfaces and all 42 problem statuses are unchanged.
The argument below needs an independent adversarial check, including its
norm-line identifications, numerical-class passage, support-stratum formula
and purely inseparable reduction. It is not an admitted theorem or a
completed repair of BJ22 Theorem 6.21.

The proposed route addresses a **finite** morphism. It does not provide
the exact descent along a projective birational resolution left open in
the [birational-descent dossier](bj22_siu_birational_descent_dossier_20261004.md).
It also does not claim a norm compatible with arbitrary base change for
a nonflat finite algebra. The proposed coefficient calculation is made on
the original normal target.

## Proposed target

Let `k` be an algebraically closed, trivially valued field. Let
\(f:T\to X\) be finite surjective between normal integral projective
varieties, and let \(\theta\in N^1(X)_{\mathbb R}\).
The candidate target is: if a function `u` on \(X^{\mathrm{an}}\)
satisfies
\[
 f^*u\in\operatorname{PSH}_T(f^*\theta),
\]
then \(u\in\operatorname{PSH}_X(\theta)\), with no assumed envelope
property and no critical Siu input. This is stronger than the first
fixed-ample-class test considered during exploration, and is therefore
kept explicitly provisional.

The proposed proof uses decreasing Fubini--Study approximations upstairs.
In a Galois cover, averaging the **functions** over the finite group is
division by a positive real integer, not an operator on sections over `k`.
Products of sections encode that sum. Coefficients of orbit polynomials
then encode an orbit maximum of each product. No inversion of the group
order in `k` is intended.

## Norm lines on a Galois cover

First suppose \(q:S\to X\) is the normalization in a finite Galois
extension of function fields, with group `G` and degree
\(d=|G|\). The independent algebraic/analytic quotient argument in
Chapter 41 identifies every analytic fiber with a `G`-orbit, including
points with nonzero support kernel. This is a named input at this stage;
its deep valuation and prime-transitivity antecedents are not newly
reaudited here.

Stacks Section 31.18 gives two relevant constructions that do not need
flatness. An invertible sheaf is trivial on the full inverse image of
sufficiently small base opens (Lemma 31.18.1). A multiplicative norm of
degree `d` glues a homomorphism on Picard groups (Lemma 31.18.2).
The generic field norm extends over an integral normal target
(Lemma 31.18.7, Tag 0BD3).

Choose frames `e_a` of a line bundle `M` on full preimages of base opens,
with \(e_a=v_{ab}e_b\). The proposed canonical frame identification is
\[
 q^*\mathrm N_q(M)\simeq
 \bigotimes_{\sigma\in G}\sigma^*M,
\]
because its transition functions on both sides are
\(\prod_{\sigma\in G}\sigma^*v_{ab}\).
This is a line-bundle identification on all of `S`, not an equality only
of generic divisorial traces. The frame argument and its compatibility
with the book's trivial reference metrics still require independent
verification.

It also suggests the needed numerical-class control without assuming an
unrestricted Cartier-class pushforward for arbitrary proper maps.
Pullback \(q^*:N^1(X)\to N^1(S)\) is injective: every integral base curve
has an integral curve upstairs mapping finitely onto it, and degrees of
pullback line bundles multiply by that curve degree. If `M` is numerically
trivial, the displayed identification shows that
\(q^*\mathrm N_q(M)\) is numerically trivial, and injectivity gives
numerical triviality of \(\mathrm N_q(M)\).
The same argument applies to real linear relations between line-bundle
classes. Thus the candidate norm map on numerical classes has
\[
 q^*c_1(\mathrm N_q(M))
   =\sum_{\sigma\in G}\sigma^*c_1(M).
\]
This reasoning is restricted to the Galois cover and to the later
purely inseparable case. It is not a claim that an arbitrary proper map
has such an `N1` pushforward.

## Descent of invariant section maxima in an exact pullback line

Let `B` be a rational line bundle on `X` and choose `m` clearing its
denominator. On `S`, suppose
\[
 F=\frac1m\max_j\{\log|s_j|+\lambda_j\},
 \qquad s_j\in H^0(S,mq^*B),\quad\lambda_j\in\mathbb R,
\]
is `G`-invariant and generically finite. Choose a base frame of `mB`
and write \(s_j=b_jq^*e\) over its full preimage. Since `q` is finite,
the coefficient `b_j` is integral over the base ring. Form
\[
 P_j(Z)=\prod_{\sigma\in G}(Z-\sigma^*b_j)
       =Z^d+\sum_{r=1}^d a_{j,r}Z^{d-r}.
\]
Each coefficient is invariant and regular, hence belongs to the base
ring: for a normal base affine domain `A` and its integral closure `C`
in the Galois extension, \(C^G=A\). Changing the base frame shows that
the coefficients glue as sections
\(a_{j,r}\in H^0(X,rmB)\). Zero sections are discarded.

The scalar identity proposed for use at every analytic point is
\[
 \max_{\sigma\in G}\log|\sigma^*b_j(y)|
     =\max_{1\le r\le d}\frac1r\log|a_{j,r}(q(y))|.
\]
For completeness, it follows from the elementary monic-polynomial root
bound. If roots `z_i` have maximum absolute value `R`, coefficients of
degree `r` have absolute value at most \(R^r\). Conversely, writing
\(A=\max_r|a_r|^{1/r}\), a root with absolute value greater than `A`
would contradict its monic polynomial equation by the ultrametric
inequality. If all roots vanish, both sides have logarithmic value
\(-\infty\). Evaluation at `y` is in its residue field and uses an
identity of regular functions; it does not first pass to a valuation of
the generic function field.

Since `F` is invariant and fibers are orbits, the proposed descended
function is
\[
 F_X=\max_{j,r}
       \left\{\frac1{mr}\log|a_{j,r}|+\frac{\lambda_j}{m}\right\}.
\]
With \(N=m\operatorname{lcm}(1,\ldots,d)\), this is a single
Fubini--Study expression for `B`: replace `a_{j,r}` by its power
\(N/(mr)\), a section of `NB`, and use weight \(N\lambda_j/m\).
This is an orbit **maximum**, not a field-norm average over the distinct
points of a possibly nonreduced fiber. Its treatment of nonflat and
proper-support points is one of the required checks.

## Turning an arbitrary upstairs approximant into a horizontal one

Write a decreasing approximation of the invariant target function
\(q^*u\) as
\[
 \varphi_i\in\mathcal H^{\mathrm{gf}}_{\mathbb R}(M_i),
 \qquad \varphi_i\searrow q^*u,
 \qquad c_1(M_i)\longrightarrow q^*\theta,
\]
where `M_i` are rational line bundles on `S`. Define
\[
 \Phi_i=\frac1d\sum_{\sigma\in G}\sigma^*\varphi_i.
\]
The sum decreases to \(q^*u\), because the group is finite and the
target is invariant. All summands have only real or negative infinite
values, so there is no cancellation of infinite values. At the generic
trivial valuation, the finite target value supplies generic finiteness.

If
\(\varphi_i=m_i^{-1}\max_j(\log|s_{i,j}|+\lambda_{i,j})\),
distributing the finite sum of maxima gives products
\[
 t_{i,\mathbf j}=
     \bigotimes_{\sigma\in G}\sigma^*s_{i,j_\sigma}
  \in H^0\!\left(S,m_i\bigotimes_{\sigma\in G}\sigma^*M_i\right).
\]
The proposed norm-line identification makes these sections of
\(m_iq^*\mathrm N_q(M_i)\). Their weights are
\(\sum_\sigma\lambda_{i,j_\sigma}\), and the outer denominator
is `d m_i`. Therefore `Phi_i` is an invariant Fubini--Study function
for the **exact pullback** of
\[
 R_i=\frac1d\mathrm N_q(M_i)\in\operatorname{Pic}(X)_{\mathbb Q}.
\]
The preceding coefficient construction would descend it as a generically
finite Fubini--Study function `g_i` for `R_i`.

Surjectivity makes the `g_i` decreasing. The proposed class identity gives
\[
 q^*c_1(R_i)
   =\frac1d\sum_{\sigma\in G}\sigma^*c_1(M_i)
   \longrightarrow q^*\theta.
\]
Injectivity and the finite-dimensional topology of numerical-class spaces
would then give \(c_1(R_i)\to\theta\). The pointwise limit downstairs
is `u`, since its pullback is \(q^*u\). Definition 4.1 would conclude
psh membership. This is the candidate's central passage; it requires
checking that the norm identifications and coefficient construction
really retain the asserted rational line bundles and reference metrics.

## Purely inseparable and general finite extensions

For a finite purely inseparable map `q` of degree `d` between integral
normal varieties, the generic field norm is \(b\mapsto b^d\).
The same full-preimage frame construction suggests
\[
 q^*\mathrm N_q(M)\simeq M^{\otimes d},
 \qquad q^*\mathrm N_q(s)=s^{\otimes d}.
\]
Hence a section expression for a rational `M_i` upstairs would descend
directly by taking norm sections, multiplying its weights by `d`, and
using denominator `d m_i`. Its base line bundle is again
\(\mathrm N_q(M_i)/d\). The injective numerical pullback argument
would control its class limit. No group average or division by `d` in
the field is used. The candidate must verify these identities for
non-simple purely inseparable extensions and at all support strata.

For a general finite extension, the proposed reduction first factors
through its maximal separable intermediate field. The normalization in
that field is finite; the remaining map is purely inseparable and
radicial. After the purely inseparable descent, use a finite Galois
closure of the separable part, pull the function back there, and apply
the Galois argument. Normality, finiteness, projectivity and the
all-point analytic surjections must be checked at each factor.

If the candidate descent target survives verification, combining it with
the already independent analytic openness calculation would supply a
finite envelope descent step. This potential consequence is not an
admitted result. It would leave the birational reflection/descent problem
and the critical Siu endpoint unresolved.

## Current evidence and pending checks

The cached full Tag 0BD3 statement/proof was freshly read. Newly acquired
Stacks Section 31.18 (Tag 0BCX) was read in full, including the full-preimage
frame and Picard norm constructions. The target statement/proof of
Tag 00H7 was freshly read. The complete web responses and lookup dates
are preserved under `source_material/finite_galois_descent_20261004/`.
The book's independent quotient, radicial and openness proofs were read
at the selected Chapter 41 scopes; these are reused manuscript arguments,
not freshly reacquired proofs of every Stacks/valuation antecedent.

Before any admission, perform explicit separable, wild and purely
inseparable section tests, a proper-support zero test, the nonflat quadric
cone test, and a frame-transition check. Recheck normalization when a
rational `M_i` is cleared, and the continuity of the induced numerical norm
map. Then obtain the repository-required independent verification and
determine whether this is an existing source result or a new argument.
There is no basis yet for deleting an `(SD)_k` assumption from the book.

The first [exact boundary calculation](research_calculations/finite_galois_descent_boundaries_20261004.py)
and its [result](research_calculations/finite_galois_descent_boundaries_20261004.json)
pass fourteen polynomial identities: four Artin--Schreier orbit polynomials,
six purely inseparable norm polynomials, and four cone section products.
There are 32 selected spectral/average valuation cases, 48 purely
inseparable valuation cases, 27 cone weight/support cases, and 25 cyclic
decreasing zero-branch cases. Proper-support zero values are encoded as
infinite valuations, with no undefined subtraction.

On the cone vertex chart, the quotient
\(k[a,b]/(a^2,ab,b^2)\) has the three monomial basis elements
\(1,a,b\), versus generic degree two. The invariant section maximum
test uses \(X^2,Y^2,Z\), not an average over a guessed set of two
ordinary points. These are finite boundary calculations; they do not
verify line gluing, numerical-class descent, the full generic proof,
every analytic support stratum, or independent book admission.
