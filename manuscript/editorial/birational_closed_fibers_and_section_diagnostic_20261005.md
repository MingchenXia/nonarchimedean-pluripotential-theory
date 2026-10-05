# Closed fibers and a varying-class section diagnostic

Date: 5 October 2026. Baseline: `f65f795`.
This continues the [birational descent dossier](bj22_siu_birational_descent_dossier_20261004.md)
outside active TeX. It checks a published zero-class input and an explicit
failure of termwise descent for a particular defining net. It does not
disprove exact birational psh reflection or critical Siu division. No
independent model receipt, new theorem admission or problem solution is
claimed.

## What the zero-class result gives on algebraic closed fibers

BJ22 Corollary 4.24 states that `PSH(0)` consists of constants on a
connected projective variety. Its proof uses decreasing psh closure,
finiteness at divisorial valuations and divisorial determination; it
precedes the critical Siu argument and does not invoke it. The entire
statement and printed proof were freshly reread, together with
Corollary 4.17's divisorial finiteness proof and the intervening
determination statement. Their deeper antecedents remain named inputs.

Keep an algebraically closed, trivially valued `k` and a projective
birational morphism \(\pi:Y\to X\) of integral projective varieties,
with `X` normal.
Suppose \(r_Y\in\operatorname{PSH}_Y(\pi^*\beta)\). For a closed
point `x` of `X`, let `F_i` be the irreducible components of the reduced
fiber. Each `F_i` is projective over `k`, and its restriction class is
zero because its map to `X` factors through the point `x`.

Apply BJ22 Theorem 4.7(iii) separately to `F_i->Y`. The restriction of
`r_Y` is either zero-class psh, hence a finite constant by Corollary
4.24, or identically negative infinite. Proper birational maps to a
normal target have connected fibers, by the independent Stein-factor
input. Intersecting components have a common analytic point, forcing
their constants in \(\mathbb R\cup\{-\infty\}\) to agree.
The connected component-incidence graph therefore makes `r_Y` constant
on the entire analytification of this closed-point fiber. Nilpotents
do not introduce additional seminorms.

If `r_Y` is homogeneous, the finite constant must be zero: positive-real
scaling preserves the fiber over the trivially valued closed point and
multiplies that constant by every positive scalar. Thus a homogeneous
pullback-class psh function takes either zero or negative infinite on
each such fiber.

This addresses fibers over algebraic closed points with their trivial
residue absolute value. A general analytic base point can have a
nontrivially valued completed residue field. No scalar-extension or
zero-class argument for every such analytic fiber is supplied here.
Even full fiber constancy and usc would still leave the base-space psh
membership task in the earlier dossier.

## A decreasing homogeneous section net on a blowup

For this diagnostic assume in addition that `char(k)=0`. Let
\(X=\mathbf P^2_k\), let `p=[0:0:1]`, let
\(\pi:Y=\operatorname{Bl}_pX\to X\), and let `E` be its exceptional
divisor. Write \(H=\pi^*\mathcal O_X(1)\). Let `L=(X_0=0)` be the
line through `p`, with canonical section `s_L`. Its total transform is
the strict transform plus `E`, each with multiplicity one.

For each integer `n>=2`, the quotient
\[
 \sigma_n=\frac{(\pi^*s_L)^{\otimes n}}{s_E}
       \in H^0(Y,nH-E)
\]
is a regular nonzero section: its effective divisor is
\(n\widetilde L+(n-1)E\). Define
\[
 \varphi_n=\frac1n\log|\sigma_n|
      \in\mathcal H_{\mathrm{hom}}(H-E/n)
      \subset\operatorname{PSH}_Y(H-E/n).
\]
These are the actual source classes; they are not exact pullbacks of
base classes. Here `H|E` is trivial and the blowup tautological line
\(\mathcal O_Y(-E)|_E=\mathcal O_{\mathbf P^1}(1)\), so their degree
on `E` is `1/n`, whereas every pullback from `X` has degree zero there.

At an analytic point whose support is not in `E`, the divisor term is
finite and the legitimate identity is
\[
 \varphi_n=\pi^*\ell_L-\frac1n\ell_E,
 \qquad\ell_E\le0.
\]
It follows that `varphi_n` decreases as `n` increases. If the support is
in `E`, the section vanishes because `n-1>0`, so every `varphi_n` is
negative infinite, as is \(\pi^*\ell_L\). These two cases establish
the all-point limit
\[
 \varphi_n\searrow\pi^*\ell_L,
 \qquad H-E/n\longrightarrow H
\]
without subtracting infinite values at the exceptional pole. The section
product gives the additional safe identity
\[
 \varphi_n+\frac1n\ell_E=\pi^*\ell_L
\]
at every point, including proper support.

Each `varphi_n` is constant on the exceptional analytic fiber, with
value negative infinite. The map is an isomorphism away from `p`, so
every other analytic fiber has a unique point. Hence `varphi_n` really
does descend as a function `g_n` on all of `X^an`. The proper closed
quotient gives an usc descended function, and analytic surjectivity gives
\(g_n\searrow\ell_L\). This example does not fail merely because
the approximants vary along the exceptional fiber.

## The descended terms are not psh in any base class

On the affine chart `X_2!=0`, put \(x=X_0/X_2\) and
\(y=X_1/X_2\). The blowup ideal is `(x,y)`. At the monomial
valuation \(v_{a,b}\), with finite positive weights
\(v(x)=a\), \(v(y)=b\), one has
\[
 \ell_L(v_{a,b})=-a,\qquad
 \log|(x,y)|(v_{a,b})=-\min(a,b).
\]
Pullback of this ideal is `O_Y(-E)`, so the finite-valued trace of the
descended term is
\[
 g_n(v_{a,b})=-a+\frac1n\min(a,b).
\]
At the proper point `p` the value was defined by the descended section
and equals negative infinite. It is not defined by the difference of
the two negative-infinite ideal/divisor terms.

Any psh function on `P^2` has a convex restriction to this fixed positive
monomial cone, directly from BJ22 Definition 4.1. Indeed every rational
line on `P^2` is a rational multiple of `O(1)`. After clearing its
denominator, each nonzero section has a polynomial coefficient in the
frame `X_2^N`. This is a unit frame at the center `p`. For the monomial
valuation the negative valuation of that polynomial is the maximum of
the negative linear forms of its nonzero monomials. Thus every weighted
generically finite Fubini--Study function restricts to a finite maximum
of affine functions of `(a,b)`, which is convex. A defining decreasing
net retains the convex inequality in the finite-valued limit. For the
proposed `g_n` the three values below are finite, so no extended-real
limit ambiguity is involved in this test.

Take `A=(1,2)`, `B=(2,1)` and their midpoint `M=(3/2,3/2)`. Then
\[
 \begin{aligned}
 g_n(A)&=-1+1/n,&g_n(B)&=-2+1/n,\\
 g_n(M)&=-3/2+3/(2n),&
 \frac{g_n(A)+g_n(B)}2&=-3/2+1/n.
 \end{aligned}
\]
The midpoint value exceeds the endpoint average by `1/(2n)>0`.
Therefore `g_n` is not psh for **any** numerical class on `P^2`.
An arbitrary positive base-class buffer does not remove this convexity
violation in the given function. Nevertheless its decreasing limit
\(\ell_L\) is an ordinary homogeneous section function in class
`O(1)`.

There is also an independent check that no hidden exact-pullback
membership has been overlooked. Put
\(D_n=\operatorname{div}(\sigma_n)/n\), an effective rational
Cartier divisor with \(\ell_{D_n}=\varphi_n\). If `varphi_n` were
psh in \(\pi^*\eta\) for any base class `eta`, the independently
established smooth division result on `Y` (BJGreen24 Proposition 17,
using the smooth characteristic-zero all-class envelope theorem) would
give a residual psh in \(\pi^*\eta-[D_n]\). That residual has zero
divisorial trace and is the constant zero by determination. But
\[
 (\pi^*\eta-[D_n])\mathbin{\cdot}E=-1/n<0,
\]
so the class is not nef, contradicting the independent equivalence
\(0\in\operatorname{PSH}(\gamma)\iff\gamma\in\operatorname{Nef}(Y)\)
in BJ22 (4.3). This uses division on the smooth source with an
independent envelope input, not division on every normal variety.

The hypotheses of exact birational reflection require a source function
psh in an **exact pullback class**, which these terms do not satisfy.
This is a diagnostic for the missing inference that a defining
upstairs net with classes merely approaching a pullback automatically
provides termwise psh approximants downstairs. The horizontal-net
requirement in the original dossier cannot be replaced by numerical
closeness, fiber constancy and usc for the chosen terms.

The finite candidate's frame mechanism also has a concrete obstruction
here. The actual line `nH-E` has degree one on `E`, so it cannot be
trivial on the full preimage of any base neighborhood containing `p`.
Stacks Lemma 31.18.1 supplied precisely such frames for a **finite**
map. Degree one of the birational function-field extension does not
give a norm-line pullback isomorphism for this nonhorizontal line;
every pulled-back line has degree zero on `E`.

In this particular example the ideal correction is completely explicit:
\[
 g_n+\frac1n\log|\mathcal I_p|=\ell_L
\]
on all analytic points, as follows from the safe section-product identity
upstairs and analytic surjectivity. At the proper pole both left-hand
summands are negative infinite and their sum is defined. The corrected
function is psh, while `g_n` itself is not. This example-specific
calculation does not provide the increasing-limit or horizontal-net
argument missing in the general birational dossier.

## Exact calculation and admission boundary

The [calculation](research_calculations/birational_section_convexity_20261005.py)
and [result](research_calculations/birational_section_convexity_20261005.json)
pass 216 selected monomial/support trace cases, 180 monotonicity
comparisons and six strict Jensen violations for `n=2,3,5,7,11,19`.
Zero section values are encoded separately; no infinite subtraction is
performed. The symbolic gap `1/(2n)` in the displayed argument applies
to every integer `n>=2`; the program tests only its listed cases.

These are same-agent source and exact-example checks, not independent
verification of a new theorem. The source net, its varying classes,
the additive identity and the failed base convexity inequality have
distinct scopes. The finite candidate, general critical Siu input,
birational existence task and all active problem statuses remain pending
or unchanged as previously recorded. No TeX or catalogue edit is made.
