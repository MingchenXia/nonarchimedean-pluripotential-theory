# Global sections and finite factorization in the descent candidate

Date: 4 October 2026. Baseline: `775dc66`.
This is a same-agent completion of the argument proposed in the
[finite candidate](finite_galois_psh_descent_candidate_20261004.md),
following the [frame check](finite_galois_norm_line_followup_20261004.md).
It is an unadmitted proof draft, outside active TeX. Independent adversarial
verification and identification of its precise literature status remain
pending. It supplies no production-model receipt, changes no problem
status, and removes no critical Siu or envelope hypothesis from the book.

## Exact target and inputs

Keep the candidate's ambient category: an algebraically closed, trivially
valued field `k`, a finite surjection \(f:T\to X\) of normal integral
projective `k`-varieties, and \(\theta\in N^1(X)_{\mathbb R}\).
Given \(u:X^{\mathrm{an}}\to\mathbb R\cup\{-\infty\}\) with
\(f^*u\in\operatorname{PSH}_T(f^*\theta)\), the proposed conclusion is
\(u\in\operatorname{PSH}_X(\theta)\). The proof draft below is for
finite maps only. It does not descend psh functions along a resolution.

The imported inputs are BJ22 Definition 4.1 and the pullback statement in
Theorem 4.7(iii); the finite-dimensional numerical-class spaces and the
curve-degree characterization of numerical equivalence; finiteness of
integral closure in finite function-field extensions for finite-type
schemes over a field; extension of a real absolute value to a finite
residue-field extension; and Stacks Section 31.18's generic norm and
full-preimage frame constructions. The last two give a norm on Picard
groups and on sections even when the finite map is not flat, provided
the target is integral and normal.

The current field-factorization source is
[Stacks Tag 030K](https://stacks.math.columbia.edu/tag/030K),
Lemma 9.14.6, whose entire target statement and printed proof were read.
It applies to every algebraic field extension: the separable subextension
comes first, followed by a purely inseparable extension. Tag 030M states
the stronger two-order decomposition for a **normal** extension; its
omitted details are not a fresh verification of that stronger statement.
Tag 030N's primitive-element statement/proof was also read at the target
scope, but is not needed in the proof draft below.

Tag 035S is the finiteness statement for normalization in the scheme's
own function field. Relative normalization in a finite extension uses
the stronger Nagata integral-closure input just named; this follow-up
does not pretend that the wording of Tag 035S alone states it. The
deep Nagata and valuation-extension antecedents are reused inputs,
not newly completed whole-source audits.

## Direct coefficient construction without the analytic quotient theorem

Let \(q:S\to X\) be normalization in a finite Galois extension `E/F`,
with group `G` and \(d=|G|\). The action extends over the normalization.
For a base affine normal domain `A` and its integral closure `C` in `E`,
\(C^G=A\): an invariant element lies in \(E^G=F\), is integral over
`A`, and hence belongs to `A`. No assertion about analytic fibers is
needed for this ring identity.

Let `B` be a rational line bundle on `X`, and choose a positive integer
`m` for which `mB` is an actual line bundle. Suppose an invariant function
has the section expression
\[
 F=\frac1m\max_j\{\log|s_j|+\lambda_j\},
 \qquad s_j\in H^0(S,q^*(mB)),\quad\lambda_j\in\mathbb R.
\]
Discard identically zero sections. In a base frame `e` of `mB`, write
\(s_j=b_jq^*e\) on the full preimage. Define
\[
 \prod_{\sigma\in G}(Z-\sigma^*b_j)
       =Z^d+\sum_{r=1}^d a_{j,r}Z^{d-r}.
\]
These are invariant regular coefficients, so `a_j,r` belongs to the
base ring. On an overlap, if \(e'=w e\), then
\(b'_j=w^{-1}b_j\) and \(a'_{j,r}=w^{-r}a_{j,r}\).
Thus \(a_{j,r}e^{\otimes r}\) glues to a section of `rmB` on `X`.
This proves the global section assertion, rather than only producing
rational coefficients on a dense open.

At an analytic point `y` use a base frame near the center of `q(y)`;
all its translates are defined near the centers of `sigma(y)`. Evaluate
the polynomial identity in the residue field at `y`. If its roots have
maximum absolute value `R`, its degree-`r` coefficient has absolute
value at most \(R^r\). Conversely, put
\(A_0=\max_r|a_{j,r}(q(y))|^{1/r}\). A root `z` with
\(|z|>A_0\) would make the leading term in its monic equation strictly
larger than every other term, contradicting the ultrametric inequality.
If `R=0`, all roots and coefficients vanish. Hence
\[
 \max_{\sigma\in G}\log|\sigma^*b_j(y)|
   =\max_{1\le r\le d}\frac1r\log|a_{j,r}(q(y))|,
\]
including zero values as \(-\infty\).

Let \(L=\operatorname{lcm}(1,\ldots,d)\), and discard zero
coefficient sections. The explicit base function
\[
 g=\frac1{mL}\max_{j,r}
       \{\log|a_{j,r}^{\otimes L/r}|+L\lambda_j\}
     \in\mathcal H^{\mathrm{gf}}_{\mathbb R}(B)
\]
has pullback
\[
 q^*g=\max_{\sigma\in G}\sigma^*F=F.
\]
For a nonzero `s_j`, the coefficient `a_j,d` is nonzero at the generic
point, because it is the signed field norm of its nonzero generic
coefficient. This supplies generic finiteness of `g`.

The displayed all-point pullback equality constructs the descended
function directly. It does **not** require prior transitivity on analytic
fibers, prime-transitivity or valuation conjugacy. Those inputs remain
relevant to the independent openness calculation in Chapter 41; they can
be removed from this candidate's coefficient-descent step. Analytic
surjectivity is still used later to compare and identify base functions.

Reference metrics are compatible with this calculation. Frame changes
are units at the analytic center; the unit and its inverse belong to
the dominated local ring, giving absolute value one. The above
coefficient transformation is the transformation of a genuine section
of `rmB`. No rational frame factor with nonzero valuation is treated as
a reference-metric unit. At nonflat or proper-support points the
evaluated polynomial still has degree `d`; it is not declared to be the
characteristic polynomial of the possibly larger fiber algebra.

## Galois descent of the defining net

Let a defining net for \(q^*u\) be
\[
 \varphi_i=\frac1{m_i}\max_j
       \{\log|s_{i,j}|+\lambda_{i,j}\}
 \searrow q^*u,
 \quad s_{i,j}\in H^0(S,L_i),
 \quad \frac{c_1(L_i)}{m_i}\longrightarrow q^*\theta,
\]
where each `L_i` is an actual line bundle and each `m_i` is a positive
integer. Using actual lines here keeps every denominator explicit.
Choose full-preimage frames as in Stacks Lemma 31.18.1. The norm line
\(N_i=\mathrm N_q(L_i)\) satisfies
\[
 q^*N_i\simeq\bigotimes_{\sigma\in G}\sigma^*L_i.
\]
Indeed the two sides have the same transition functions
\(\prod_\sigma\sigma^*v_{ab}\) in the norm construction of
Lemma 31.18.2. This frame isomorphism also respects the trivial reference
metrics; it is not obtained by applying a determinant to a nonflat
fiber algebra.

Set
\[
 \Phi_i=\frac1d\sum_{\sigma\in G}\sigma^*\varphi_i,
 \qquad B_i=\frac1{dm_i}N_i\in\operatorname{Pic}(X)_{\mathbb Q}.
\]
The average is invariant. Distributing the sum of finite maxima gives
\[
 \Phi_i=\frac1{dm_i}\max_{\mathbf j}
    \{\log|t_{i,\mathbf j}|+\Lambda_{i,\mathbf j}\},
 \quad
 t_{i,\mathbf j}=\bigotimes_{\sigma\in G}\sigma^*s_{i,j_\sigma}
     \in H^0(S,q^*N_i),
 \quad
 \Lambda_{i,\mathbf j}=\sum_\sigma\lambda_{i,j_\sigma}.
\]
Thus the preceding construction applies with `m=dm_i` and `B=B_i`.
Its degree-`r` coefficient sections belong to `rN_i`; their powers
belong to `LN_i`, and its final denominator is `dm_i L`.
These are exactly sections of \((dm_i L)B_i\), with weights
\(L\Lambda_{i,\mathbf j}\). No line-class buffer is introduced.
It yields \(g_i\in\mathcal H^{\mathrm{gf}}_{\mathbb R}(B_i)\)
with \(q^*g_i=\Phi_i\).

The net `Phi_i` decreases to `q*u`. At a point with finite target,
finite sums commute with the decreasing limit. At a point with target
\(-\infty\), all group translates have that same limit; a tail is
bounded above by one fixed approximant in each summand, and a common
upper index for finitely many summands makes their sum arbitrarily
negative. There is no positive infinity and no undefined cancellation.
The original directed index set is retained; no sequential replacement
or countable cofinality is assumed.

Finite analytic surjectivity then gives `g_i` decreasing and
\(g_i\searrow u\) at every base point. Its infimum is upper
semicontinuous. At the generic trivial valuation,
\(u(v_{\mathrm{triv},X})=(q^*u)(v_{\mathrm{triv},S})\) is finite,
so the limit is generically finite.

For completeness, finite pullback on numerical classes is injective:
each integral base curve `C` has an integral curve `C'` above it that
maps finitely and surjectively to `C`. On their normalizations,
\[
 \deg(q^*A|_{C'})=[k(C'):k(C)]\deg(A|_C).
\]
Thus a class whose pullback is numerically zero has zero degree on all
base curves. The norm line identity implies
\[
 q^*c_1(B_i)=\frac1d\sum_{\sigma\in G}
                 \sigma^*\left(\frac{c_1(L_i)}{m_i}\right)
       \longrightarrow q^*\theta.
\]
The average tends to `q*theta` because that class is invariant.
An injective linear map between finite-dimensional real numerical spaces
is a homeomorphism onto its image, so \(c_1(B_i)\to\theta\).
Together with the preceding decreasing net, this is the proposed
application of Definition 4.1. This version does not need a separately
defined general proper pushforward on `N1` or a norm map on all real
classes: the actual norm lines and injectivity already control the
particular class limit.

## Purely inseparable descent and its degree

Suppose `q:S->X` is finite purely inseparable of field degree `d`.
The field norm is \(b\mapsto b^d\), including non-simple extensions.
The full-preimage norm frames therefore give
\[
 q^*\mathrm N_q(L_i)\simeq L_i^{\otimes d},
 \qquad q^*\mathrm N_q(s_{i,j})=s_{i,j}^{\otimes d}.
\]
A base section expression with norm sections, denominator `dm_i`,
and weights \(d\lambda_{i,j}\) pulls back exactly to `varphi_i`.
Its rational base line is
\(B_i=\mathrm N_q(L_i)/(dm_i)\), and
\(q^*c_1(B_i)=c_1(L_i)/m_i\). The same injectivity, surjectivity,
generic-finiteness and decreasing-net argument would complete this case.

Here `d` is the **field degree**, not the least power killing the
inseparability. In
\[
 F=\mathbb F_p(x,y),\qquad E=F(u,v),\qquad u^p=x,\quad v^p=y,
\]
the degree is `p^2`, whereas the exponent is `p`. For example,
\(\mathrm N_{E/F}(u)=u^{p^2}=x^p\). Replacing this by `x` while
keeping the degree denominator would give the wrong function.

The new [calculation](research_calculations/finite_galois_nonsimple_norms_20261004.py)
and [result](research_calculations/finite_galois_nonsimple_norms_20261004.json)
construct the multiplication matrices over \(\mathbb F_p(x,y)\)
for eight selected coefficients in characteristics two and three. Their
full characteristic polynomials and field norms agree with the
degree-`p^2` formulas. Three mixed separable/pure towers, ninety exact
weighted/support cases, and three degree/exponent diagnostics also pass.
These test the named examples; they do not verify the geometric proof
draft or provide an independent receipt.

## Normalization maps in the general finite case

Write \(F=k(X)\), \(E=k(T)\), and let \(E_s\) be the subfield
of elements separable over `F`. Tag 030K gives `E_s/F` separable and
`E/E_s` purely inseparable. Let `X_s` be normalization of `X` in `E_s`.
On a base affine `Spec A`, write `C` for its integral closure in `E`
and `B` for its integral closure in `E_s`. Normality of `T` and
finiteness over `X` identify its affine ring with `C`: an element of
`E` integral over `A` is integral over that normal affine ring, and
hence already lies in it.

We have \(A\subset B\subset C\). The Nagata input makes `B`
finite over `A`; the finite `A`-module generators of `C` also generate
it over `B`, so `C` is finite over `B`. Both inclusions are integral
and dominant, giving finite surjections
\[
 T\xrightarrow{h_2}X_s\xrightarrow{h_1}X.
\]
All three schemes are integral and normal. Finite morphisms are
projective; their compositions with the projective structure morphism
make `X_s` projective over `k`. For a fixed purely inseparable exponent,
every `c` in `C` has a power `c^(p^r)` in `E_s` and integral over `B`,
hence in `B`. After base change to any field, this power condition gives
at most one geometric point and purely inseparable residue extensions.
Thus `h_2` is radicial; its analytic map is a homeomorphism by the
independent Chapter 41 argument. The proof draft itself only needs its
analytic surjectivity.

Set \(v=h_1^*u\). The assumed pullback is \(h_2^*v\), so the pure
case would give \(v\in\operatorname{PSH}_{X_s}(h_1^*\theta)\).
Take a finite Galois closure `M/F` of `E_s/F`, and let `S` be
normalization of `X` in `M`. Integral closures give finite surjections
\(\rho:S\to X_s\) and \(q=h_1\rho:S\to X\), with `S` normal,
integral and projective. Pullback preserves psh membership here: `rho`
is dominant, and the finite value at the generic trivial valuation
prevents an identically negative-infinite component. Hence
\(q^*u=\rho^*v\) is psh and the Galois case would give the target
conclusion. No psh or envelope theorem on the Galois closure is assumed.

## Literature comparison and limits of this draft

The cached published BE21 PDF was freshly inspected at selected targets:
Proposition 8.22 and its full printed proof, Proposition 8.24 and its
proof, Lemma 8.25 and its proof, and Theorem A.21 with its printed
discussion. Five actual physical pages, 86--88 and 121--122, were
visually checked. The source has a cover page: printed pages are one
less than these physical page numbers. Text extraction emitted PDF
dictionary warnings; the selected rendered pages were used to check the
target statements and locators. No full BE21 or Ducrot proof audit is
claimed.

BE21 Proposition 8.22 assumes a finite **flat** map of projective
geometrically reduced schemes, an **ample** rational line upstairs,
and a **continuous** psh metric. Proposition 8.24 and Lemma 8.25 treat
finite-flat pullback/envelope and fiber-maximum constructions for
continuous metrics. Theorem A.21 has a flat, projective, finitely
presented morphism as a displayed hypothesis for its base-change
compatible determinant structure. These selected results do not state
the present arbitrary-real-class, possibly unbounded, nonflat target.
They are relevant antecedents, not an authenticated citation for that
full target and not permission to use determinant base change at the
cone vertex. The precise known-result/new-argument classification still
requires a broader primary-source check.

Normality of the source can be removed **conditionally on this draft**:
normalize an integral projective source, pull back its assumed psh
function by the dominant finite normalization, and apply the normal
case to the composite. Target normality is used in the generic norm
and in `C^G=A`; failure of those steps for a nonnormal target is not a
counterexample to the statement. The zero-dimensional case in the
stated algebraically closed category is the identity point case, with
`N1=0`. No nonprojective, nontrivially valued, mixed-characteristic,
reducible or nonnormal-target extension has been verified here.

Even if this proof survives independent review, it only separates the
finite reflection/descending-net step from critical Siu division. General
envelope descent would additionally use the independently established
finite openness calculation. Exact birational descent, and thus the
critical normal Siu endpoint in the book's present dependency route,
would still require a separate argument. All admission gates remain
pending under the repository verification protocol.
