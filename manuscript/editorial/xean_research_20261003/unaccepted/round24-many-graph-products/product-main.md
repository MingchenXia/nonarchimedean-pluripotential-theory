---
title: "Envelope contact on products of finitely many balanced graphs"
author: "P05.2 unverified partial proof draft"
date: "4 October 2026"
---

## Statement, coefficient convention, and scope

Let \(d\geq2\), and let \(G_j\subset N_{j,\mathbb R}\) be nonempty finite
embedded rational pure graphs with strictly positive actual **real** balanced
edge weights. Use the direct product ambient lattice, the actual saturated
tangent lattices, and product weights on \(X=\prod_{j=1}^dG_j\).
Bounded edges, cycles, full lines, ends and disconnected components are allowed.
At a vertex use its actual primitive outgoing vectors \(q_e\), and set
\[
 K_v=\{c\geq0:\sum_e c_eq_e=0\}.
\]
Rank means \(\dim\operatorname{span}_{\mathbb R}K_v\). Branched means that
some carrier junction has valence at least three; rational bivalent subdivision
does not count as branching. A graph presented without vertices is treated by
inserting rational bivalent points.

Real PA throughout means continuous real-affine pieces on a **finite rational
spatial complex**. This is the real scalar extension of the literal PA convention
on each fixed complex. Cycles, including local testing cycles, have real weights.
We retain the source's genuine PCCs: rational endpoints, real nonnegative
coefficients summing to one, and their actual, possibly irrational, barycentre;
on some allowed rational structure a common face containing that centre is a
face of every endpoint coface. Raw PC means every such Jensen inequality.
Raw competitors are finite functions; their continuity is never presumed.

Fix any prescribed continuous rational-domain real-PA actual-PC \(\gamma\)
positive at infinity: on every affine reference cell its slope is positive on
every nonzero recession vector. For bounded continuous rational-domain real-PA
\(u\), set \(f=\gamma+u\), and use exactly the raw envelope
\[
 P_\gamma(u)(x)=\sup\{h(x):h\in\mathrm{PC}(X),\ h\leq f,
                                      h\leq\gamma+C_h\}.
 \tag{E}
\]
The growth restriction here is only an upper bound. PAPC tests the divisor
against every nonnegative real balanced local cycle, in each dimension
\(1,\ldots,d\), on every ordinary open subset. The operator is the complete
recursive zero-cycle \(P^d\cdot[X]\), with no division by \(d!\).

**Theorem (unverified finite-product classification).** For this fixed
\((X,\gamma)\), every bounded continuous rational-domain real-PA obstacle has
a finite continuous rational-domain actual-PAPC raw envelope in
\(\gamma+O(1)\), a uniform decreasing PAPC regularization, and
\[
       \int_X(P_\gamma(u)-\gamma-u)\,
                  \mathrm{MA}_{\mathrm{poly},\mathbb R}(P_\gamma(u))=0
 \tag{C}
\]
if and only if every local cone in every factor has rank one and **at most
one factor is branched**.

When a cone in one factor has higher rank, for each prescribed reference we
construct a compactly supported nonnegative obstacle with exact PAPC raw
envelope \(P\), with \(P=\gamma\) outside a compact subset of the entire
original product, and complete integral
\[
 -d!\,(\delta\varepsilon M)\prod_{j=2}^d(2\delta b_jw_j)<0.
 \tag{H}
\]
When all cones have rank one and two factors branch, the complete integral is
\[
 -\frac{d!}{2!}\,8\kappa^2ab\prod_{j=3}^d(2\kappa b_jw_j)<0.
 \tag{T}
\]
Empty products in these formulas equal one. Every scalar is defined below from
actual weights and actual primitive directions, rather than imposed as a mass
assumption. Both failures have explicit regularization \(P+1/n\).

This closes only the specified finite-product family in the declared real
category. Original P05.2's classification on arbitrary balanced carriers remains
open; status is partial and candidate is false. No literal coefficient result,
analytic realization, general singular-fan contact theorem, or P06.2 conclusion
is claimed. The exact original problem and completion criteria are retained in
`task.json` and `original-scope.txt`, and the complete current assignment in
`assignment.txt`. The predecessor arguments and all five canonical native notes
were read and preserved unchanged. They are fallible evidence, not premises.

## Recursive intersection in every dimension, with saturated quotients

Here and below \(N_\sigma=N\cap\operatorname{span}_{\mathbb R}(\sigma-\sigma)\).
For a facet \(\tau\prec\sigma\), choose an integral lift of the primitive
inward generator of \(N_\sigma/N_\tau\). For a real PA \(h\) and a balanced
real \(k\)-cycle \(z\) define
\[
 (h\cdot z)(\tau)=\sum_{\sigma\succ\tau}z(\sigma)h_\sigma^{\rm lin}(n_{\sigma/\tau})
       -h_\tau^{\rm lin}\left(\sum_{\sigma\succ\tau}z(\sigma)n_{\sigma/\tau}\right).
 \tag{D}
\]
The sum in parentheses is tangential. Lift changes cancel by agreement of linear
parts on \(\tau\). Thus (D) is bilinear, local on ordinary opens, and zero for
ambient affine functions, including real ones.

For refinement examine the minimal old face of a tested new \((k-1)\)-face.
If its dimension is above \(k\), all incident inherited \(k\)-weights vanish.
If it has dimension \(k\), exactly two pieces in that inherited \(k\)-plane
have possibly nonzero weights; they have equal weight and linear part and
opposite primitive quotient classes. All other incident pieces have weight zero.
Their contributions cancel. If it has dimension \(k-1\), its tangent span is
unchanged, and locally there is one inherited incident \(k\)-piece for each old
incident \(k\)-face. The saturated lattices and normal classes are unchanged,
so the coefficient is the old coefficient. These cases also show inherited
balancing. They exhaust the possibilities since the old face contains the new
tested face. The proof applies to signed and real weights and at every recursive
stage. A newly inserted zero-face therefore inherits zero top coefficient unless
it was already an old zero-face.

For balancing of a new divisor, fix a \((k-2)\)-face \(\theta\) for \(k\geq2\).
Translate its germ, subtract an ambient real linear extension of the common
tangential linear part, and quotient by its tangent lattice. Saturation of
\(N_\theta\) follows from its definition. The image \(N_\sigma/N_\theta\)
is saturated in \(N/N_\theta\): if \(m[n]\) belongs to it then
\(mn+t\in N_\sigma\) for \(t\in N_\theta\subset N_\sigma\), hence
\(mn\in N_\sigma\), and saturation implies \(n\in N_\sigma\).
Consequently all primitive normals are precisely those of the actual quotient.
The incident cycle becomes a balanced two-dimensional fan, possibly in a larger
ambient quotient. Rational homogeneous cuts make its two-cones pointed. Such
cuts do not change the divisor by the refinement argument.

For an unordered two-cone bounded by primitive rays \(r,s\), put
\(\chi_{rs}=[N_{C_{rs}}:\mathbb Zr+\mathbb Zs]\) and
\(\omega_{rs}=z(C_{rs})\). Extending \(r\) to a basis of the saturated plane
lattice gives the primitive normal class represented over the reals by
\(s/\chi_{rs}\). The discrepancy from an integral lift is tangential and
cancels in (D). Balancing at a ray and the first divisor say
\[
 \sum_s\frac{\omega_{rs}}{\chi_{rs}}s=t_rr,
 \qquad D_h(r)=\sum_s\frac{\omega_{rs}}{\chi_{rs}}h(s)-t_rh(r).
 \tag{F}
\]
Here the function is homogeneous after subtraction. In
\(\sum_rD_h(r)r\), interchange \(r,s\) in the double first sum; it becomes
\(\sum_r h(r)\sum_s(\omega_{rs}/\chi_{rs})s\), exactly the subtracted sum.
Thus the new divisor is balanced at \(\theta\). For \(k=1\), the new
zero-cycle has no balancing condition. This proves balancing in all dimensions.

For a second function also subtract its ambient tangential affine extension.
The full coefficient of its divisor on this balanced first divisor is
\[
 \sum_{\{r,s\}}\frac{\omega_{rs}}{\chi_{rs}}
                     [h(s)g(r)+h(r)g(s)]
                     -\sum_r t_rh(r)g(r).
 \tag{S}
\]
Both terms are symmetric. In particular the tangential term is retained.
This proves mixed commutativity at every \((k-2)\)-face, hence globally by
refinement and locality. Adjacent transpositions give every order of a mixed
product. Since every intermediate cycle is balanced, an ambient real affine
term in any slot changes no product.

These arguments prove the real coefficient extension directly. Alternatively,
on a fixed rational complex both affine continuity and cycle balancing are
rational homogeneous linear systems: rational bases, with denominators cleared,
span their real solution spaces by integral data. Bilinearity extends identities
from those data. Positivity does **not** follow from a signed-basis expansion;
the full real positivity tests are proved in the next section. The source
Allermann--Rau, arXiv:0709.3705v3, Definition 3.1 through Proposition 3.7, uses
integral functions and integral cycle weights. Its full selected body is included
below for comparison. Its printed short commutativity formula is not used in
place of (S); no extension or dropped tangential term is presumed.

Products of balanced cycles are balanced: their facets lower exactly one
factor, and their actual quotient normal belongs to that factor, multiplied by
the other factor weight. On a product cell,
\(N_{\sigma\times\eta}=N_\sigma\oplus N_\eta\), because the ambient lattice
is a direct sum. For a pulled-back function \(h\) from the first factor,
\[
             h\cdot(z\times z')=(h\cdot z)\times z'.
 \tag{P}
\]
Indeed at \(\tau\times\eta\) both sums in (D) are \(z'(\eta)\) times the
first-factor sums, with primitive class \((n_{\sigma/\tau},0)\). At
\(\sigma\times\tau'\), normals \((0,n_{\eta/\tau'})\) give zero linear
parts and zero correction for \(h\). These are all facets. This remains true
for zero-dimensional factors: then every facet lowers another factor, while the
restricted function is constant, so it contributes zero. This proves the
zero-repeat-factor assertion, without a transversality hypothesis or an index
replacement. The same proof works for every intermediate tensor cycle and
for a two-dimensional first factor.

For any continuous rational-domain real-PA PAPC \(P\), its successive divisors
are balanced and nonnegative; its top measure is the finite zero-cycle on its
domain vertices. Constants have zero linear parts. Thus \(P+1/n\) decreases
uniformly in \(\gamma+O(1)\) and has exactly the same full measures. This
constructs the regularized PA operator used here directly; no general
continuity theorem is required. There is no diffuse mass or point at infinity.

For completeness, bounded reference shifts preserve the total top mass in every
dimension. Mixed commutativity gives
\[
 P^d\cdot[X]-\gamma^d\cdot[X]
 =(P-\gamma)\cdot\sum_{i=0}^{d-1}P^i\gamma^{d-1-i}\cdot[X].
 \tag{M}
\]
The inner cycle is a finite balanced real one-cycle. On a common affine
structure each bounded edge contributes opposite outgoing slopes at its two
endpoints, and each end has zero slope for the bounded affine function
\(P-\gamma\). Full lines can be split rationally and cancel. The total
difference is zero. This mass identity is separate from contact.

## Finite PC cones, real-centre equivalence, and all local positivity tests

The elementary finite-polyhedron proof, all-centre/all-structure finite-PC cone
proof, exact active-face rational-box reference decomposition, intrinsic graph
criterion, and rank-one normalization proofs are supplied in full immediately
after the new theorem proof below. They use neither the two-graph theorem nor
the source's continuity/locality conclusions. Their formulas (FC1)--(FC6),
(G1) and the vertex/recession formula (8) apply in **any** finite embedded
rational complex: none uses dimension two. We explicitly prove the remaining
dimension and coefficient points here.

If a continuous finite rational-domain real-PA \(h\) is actual PC, take any
nonnegative local real \(k\)-cycle on an ordinary open \(U\), for any
\(1\leq k\leq d\). Refine its global rational structure and that of \(h\).
At a tested facet choose rational \(x\in U\cap\operatorname{relint}\tau\).
Possible nonnegative incident weight vectors balanced modulo the saturated
tangent space form a rational polyhedral cone. The supplied finite-generation
proof gives rational generators, so it suffices to test a rational vector
\(c_\sigma\). Write \(S=\sum c_\sigma>0\) and
\(T=\sum c_\sigma n_{\sigma/\tau}\), which is rational and tangential.
For small rational \(\epsilon>0\), the endpoints
\[
              x_\sigma=x+\epsilon(n_{\sigma/\tau}-T/S)
\]
are in their incident cells and \(U\). They are rational and have barycentre
\(x\) with coefficients \(c_\sigma/S\). PC Jensen multiplied by
\(S/\epsilon\) is exactly the nonnegativity of (D). The zero vector gives
zero. Linearity in weights proves every real test. This uses every dimension
and every ordinary open. The multiplier is \(S/\epsilon\).

Conversely, PAPC for continuous PA implies the finite tangent tests (FC3).
For a rational generator \((d_\sigma)\) of the sum-zero tangent-family cone
at a face \(\tau\), choose rational \(y\in\operatorname{relint}\tau\).
Discard zero directions and write each nonzero rational vector
\(d_\sigma=a_\sigma n_\sigma\), with \(a_\sigma>0\) rational and
\(n_\sigma\) a primitive integral vector on its ray. Small initial segments
are inside the corresponding cofaces by (FC1). On a sufficiently small ordinary
ball around \(y\), put weight \(a_\sigma\) on those rays, adding weights
when rays coincide. Extend the segments to rational endpoints outside that
ball. Their local one-cycle is balanced because \(\sum d_\sigma=0\).
Every other subdivision point is bivalent, with equal opposite weights. This
is an allowed local cycle: a finite common ambient rational hyperplane
refinement includes each rational segment and \(y\), and all outer endpoints
are outside the chosen open. PAPC at \(y\) is
\(\sum h_\sigma^{\rm lin}(d_\sigma)\geq0\). If there are no nonzero
directions the assertion is zero. The finite-cone sufficiency proof gives
genuine PC at every real centre and every permitted structure. No irrational
centre is inserted as a rational vertex. This repairs precisely that issue in
a literal reading of the source's Lemma 3.4 proof.

For any number of graph factors, product-face tangent cones are products:
each projected direction has a sufficiently small feasible positive step, and
the minimum of finitely many such step sizes works simultaneously. Given a
sum-zero product tangent family, group its projection by each factor coface.
These grouped vectors belong to convex factor tangent cones and sum to zero.
Each factor PC gives a nonnegative derivative sum. Adding gives (FC3) on the
product. Its all-structure sufficiency proves that a sum of pulled-back
factor-PC functions is actual PC. Zero projected displacements give zero;
no assertion that projected remote cofaces form a factor structure is needed.
The argument works for any finite number of factors, for all real centres,
all allowed cofaces and all real coefficients.

## Positive direction: component reduction with actual real weights

At a rank-one vertex the strictly positive actual weight vector spans the full
kernel of its rational direction matrix: small positive and negative
perturbations of it realize every kernel vector in the span of \(K_v\).
Its sole relation has a positive primitive integer generator. Incident actual
weight ratios are consequently rational. On each connected graph component,
fix one actual edge weight as scale and propagate ratios along finite paths.
Given actual balancing makes these ratios consistent around every cycle.
Thus \(w_e=c r_e\) with \(c>0\) real and \(r_e>0\) rational. At a bivalent
vertex directions are opposite primitive vectors and weights equal. A
rank-one branching vertex has no opposite pair, since that would be another
nonnegative relation.

Each unbranched component is a whole rational affine line: bivalent propagation
stays on one line, a finite endpoint would be one-valent and unbalanced, and a
closed bounded cycle cannot embed in that line. Full-line components already
have this property. When at most one factor branches, every product component
is \(G\times E\), where \(E\) is a complete rational affine space of dimension
\(m=d-1\) with saturated lattice equal to the direct sum of the actual primitive
line lattices. If none branches, choose any one line as \(G\).
Its actual cycle is a single positive scalar
\(c\prod_{j\ne G}w_j\) times the rationally normalized cylinder cycle.
The divisor formula is linear in its initial cycle. Induction shows that this
scalar multiplies the **entire** recursively defined measure once; it is not
raised to the \(d\)-th power. PC competitors and envelopes do not depend on
that scalar.

The complete multivariate cylinder reconstruction is supplied directly below.
It proves the following for connected rank-one rationally weighted \(G\):
for every nonseparable real rational-domain reference and obstacle, the raw
envelope on \(G\times E\) is finite rational-domain PAPC in \(\gamma+O(1)\)
and all noncontact top coefficients vanish. We use its proof, not its previous
review. The proof uses the compact **multivariate** dual polyhedron
\[
 D=\{p\in E^*:p(r_E)\leq\gamma^{\rm lin}(r)
                 \text{ for every vertical reference recession generator}\},
\]
all projected spatial vertices, the greatest assignment in the full graph
incidence system (including every cycle), and rational supergradient polytopes.
Dual chamber vertices may be real. The spatial maximization domains remain
rational because the gradients of the node assignments are rational, not
because of rationality of those dual vertices. These domains have zero-faces
only over graph nodes.

At each possible noncontact atom \((v,z_0)\), its exposed dual face \(C_x\)
has rational affine-hull direction because \(z_0\) is rational and all defining
normals are rational. If \(\dim C_x<m\), the full germ has a common rational
lineality after affine subtraction, and the entire top divisor is zero.
If \(\dim C_x=m\), interior covectors uniquely expose \(z_0\). Noncontact
makes the corresponding node cap strict. Raising only that LP coordinate shows
its graph Laplacian is zero; positivity and concavity then make every outgoing
slope affine in \(p\). The sole star relation factors those slopes through a
real form \(A\) and a rational map \(B\), giving the complete germ
\(A(s)+\operatorname{supp}_{C_x}(z+B(s))\). It factors after affine subtraction
through an \(m\)-dimensional complete rational fan. The full recursive quotient
vanishing proof below makes its \((m+1)\)-st divisor zero. This covers all
junctions, inserted bivalent nodes, tail bases, fibre walls and open-edge strata.
The supplied all-dimensional algebra (D)--(S) validates each affine subtraction
and every intermediate cycle. There is no interpolation or separability
substitute for this multivariate argument.

Restoring each actual scalar proves contact on each component. There are
finitely many components; they are relatively open and closed, and a PCC or
local incident test stays in the component of its common face. The finite
structures, growth constants and measures combine componentwise. This proves
the positive implication of the theorem.

## A localization lemma for every fixed real reference

Use the full finite-PC-cone and active-face box proof below to write exactly
\[
          \gamma=\sum_{a=1}^J\lambda_a\gamma_a,
                \lambda_a>0,\quad\sum_a\lambda_a=1,
 \tag{R}
\]
where every \(\gamma_a\) has rational affine coefficients, is actual PC on
the same finite rational complex, and retains every strict recession inequality.
Choose rational product centre \(o\), ambient lattice bases, and
\(\rho(x)=\sum_j\|x_j-o_j\|_1\), with homogeneous recession norm \(\rho_0\).
For each \(a\), pointed-cell vertex/recession decomposition gives rational
\(m_a>0,Q_a\geq0\) such that \(\gamma_a\geq m_a\rho-Q_a\) everywhere.
Indeed choose \(m_a\) below all positive rational ratios of reference recession
slope to \(\rho_0\); affinity bounds the vertex term below and the triangle
inequality bounds the norm above. Finitely many rational vertex bounds provide
\(Q_a\). No component or end is omitted. This also handles bounded cells.

Suppose a global rational-coefficient rational-domain actual-PC \(F\) satisfies
\(F\leq L\rho+A\) for rational \(L>0,A\). Choose rational
\(0<\delta_a<m_a/L\) and rational \(C_a\) sufficiently large that
\(C_a+\delta_a F(o)>\gamma_a(o)+2\). Define
\[
 P_a=\max\{\gamma_a,C_a+\delta_a F\},\qquad
 P=\sum_a\lambda_a P_a,\qquad \delta=\sum_a\lambda_a\delta_a>0.
 \tag{L}
\]
Maxima preserve all Jensen inequalities by selecting an active function at the
centre; positive sums also preserve them. Each maximum has rational comparison
walls because both operands have rational coefficients. Their common rational
refinement supports the real sum, without any maximum with the original real
\(\gamma\). The estimate
\[
 \gamma_a-(C_a+\delta_aF)
 \geq(m_a-\delta_aL)\rho-Q_a-C_a-\delta_aA
\]
proves \(P=\gamma\) outside a compact subset of the **entire** product and
\(P\geq\gamma\). Thus \(P\in\gamma+O(1)\) is actual PAPC with the
constant-shift regularization and retains each strict recession slope. Its
global compact localization has not modified the given reference.

We can take a common function structure \(\Pi\) by finitely many ambient
rational hyperplanes extending all rational cell walls. Insert the rational
centre as an original product vertex (using bivalent subdivisions in extra
factors). Where all localizers dominate, the germ is a finite homogeneous
rational-domain germ plus a constant. Choose a sufficiently small rational
radius \(r_0>0\) such that \(\rho<r_0\) lies in that germ, encounters no
other factor endpoint, cap bend or nonincident cell, and avoids every cutting
hyperplane not through \(o\). Every retained constraint is homogeneous about
\(o\). A nonzero point has a short radial contraction and expansion within
its minimal face, so is not a vertex. Hence
\[
                    \Pi^{(0)}\cap\{\rho<r_0\}=\{o\}.
 \tag{V}
\]
All inherited homogeneous cuts from the prescribed nonseparable reference are
retained. The norm ball is intersected with the carrier, not identified with
a product star.

## Higher-relation obstruction in any number of factors

Suppose \(G_1\) has rank at least two at \(v\). Choose rational interior
points \(y_j\) of any edges of the other nonempty pure graphs, with actual
primitive tangents \(r_j\) and weights \(w_j>0\), for \(2\leq j\leq d\).
Their small germs are straight intervals even if the graphs branch elsewhere.
Set \(o=(v,y_2,\ldots,y_d)\). Let \(q_i,w_i\) be the first star's actual
directions and weights.

The rational pointed cone \(K_v\) has a rational extreme generator \(c\ne0\)
with nonempty proper support \(I\). If it were strictly positive, an independent
kernel vector would give two small opposite perturbations of \(c\) in the
cone, contradicting extremality. The full kernel equals \(\operatorname{span}K_v\)
by perturbing the strictly positive actual weight vector. Put \(s_i=0\) on
\(I\) and \(s_i=1\) outside; then
\[
       c\cdot s=0,\qquad b\cdot s\geq0\ (b\in K_v),
                  M=\sum_iw_is_i>0.
\]
This is intrinsic graph data; it need not extend to an ambient convex slope.

Set \(\rho_1=\|x_1-v\|_1\), \(\rho_j=\|x_j-y_j\|_1\).
Along the first ray \(\rho_1(v+tq_i)=a_it\), where \(a_i=\|q_i\|_1>0\).
Choose rational \(0<\varepsilon<\min_i a_i\), short rational star lengths
\(L_i\) before every existing endpoint or norm breakpoint, and rational
\(0<A<\min_iL_i(a_i-\varepsilon s_i)\). Replace the norm on this star by
\[
       F_1(v+tq_i)=\max\{a_it,A+\varepsilon s_it\},
\]
and keep the norm elsewhere on every graph component. The comparison points
\(A/(a_i-\varepsilon s_i)\) are rational and before \(L_i\). At the
centre the slopes are \(\varepsilon s_i\); at each new edge bend they
increase to \(a_i\). Values agree at the centre and at the outer gluing
boundary. The intrinsic criterion (G1) proves global actual PC, including
opposite-pair relations and all real centres. It has rational coefficients and
domains, and \(0\leq F_1-\rho_1\leq A\).

Set \(F=F_1+\sum_{j=2}^d\rho_j\). The product tangent-family proof gives
global actual PC and PAPC in every dimension; \(\rho\leq F\leq\rho+A\).
Apply (L) with \(L=1\). On the central germ it gives
\[
 P(v+tq_i,y_2+z_2r_2,\ldots,y_d+z_dr_d)
       =C+\delta\varepsilon s_it+\sum_{j=2}^d\delta b_j|z_j|,
       \qquad b_j=\|r_j\|_1>0,
 \tag{G}
\]
where \(C=\sum_a\lambda_a(C_a+\delta_a A)\). The reference is unchanged
at infinity on all components. Choose the homogeneous rational structure and
radius of (V).

Choose rational \(B,T,D_j>0\), with \(B<T\), so small that
\(\max_i a_iT+\sum_{j=2}^d b_jD_j<r_0\). On this short product star put
\[
 \beta(v+tq_i,y_2+z_2r_2,\ldots)=
            (1-t/B-\sum_{j=2}^d|z_j|/D_j)_+,
 \tag{B}
\]
and extend by zero. It vanishes before each outer boundary and has the same
value on the common first-vertex fibre. Thus it is continuous compactly
supported rational-domain rational-PA, equals one at \(o\), and has support
inside \(\rho<r_0\). Put \(u=P-\gamma+\beta\).

For any raw competitor \(q\leq P+\beta\), first fix a rational tuple
\(z\) with \(|z_j|\leq D_j\). The rational endpoints
\((v+Tq_i,y_2+z_2r_2,\ldots)\), \(i\in I\), with coefficients
\(c_i/\sum c_i\), form a genuine PCC centred on the entire apex fibre:
the supported relation cancels the first displacement and all other
displacements are zero. A permitted coarse rational product structure has the
closed fibre face over \(v\) in each incident strip; refine extra sign
coordinates if desired. The ceiling at these endpoints equals \(P\) because
\(T>B\). Equation (G) and \(c\cdot s=0\) give
\(q(v,z)\leq P(v,z)\). For any rational \(t\in[0,B]\), combine the
rational pinned apex and the endpoint at \(T\) in the same incident strip;
\(P\) is affine in \(t\). Hence \(q\leq P\) there. Outside the bump,
the ceiling gives the same bound directly. We have bounded every rational point
of the whole product, not just the central point.

For a real point with positive bump, choose its minimal face of the local
rational ray/sign-orthant structure, with \(t=0\) and all zero \(z_j\)
as faces. Arbitrarily small rational boxes in rational affine coordinates
enclose it within that face and the germ. Their real barycentric coefficients
give a same-face PCC. Every rational endpoint satisfies the preceding bound,
and (G) is affine on that face, so \(q(x)\leq P(x)\) exactly. Zero-faces
are rational; all boundary cases with zero displacements are thus included.
Elsewhere \(\beta=0\). Conversely \(P\) is an actual-PC upper-growth
competitor below \(P+\beta\). Therefore (E) equals \(P\) on all of \(X\),
without assuming continuity or lower growth for \(q\).

The local cycle is \(Z_1\times\cdots\times Z_d\), where \(Z_1\) is the
actual star and \(Z_j\), \(j\geq2\), is the whole primitive line germ of
weight \(w_j\). Write \(h_1(tq_i)=\delta\varepsilon s_it\) and
\(h_j(z_jr_j)=\delta b_j|z_j|\). Their one-factor divisors are exactly
\[
 h_1\cdot Z_1=(\delta\varepsilon M)[0],\qquad
 h_j\cdot Z_j=(2\delta b_jw_j)[0].
 \tag{A1}
\]
In the first formula the primitive outgoing directions are \(q_i\), and
in the second they are \(r_j,-r_j\). The tangential correction at the
point is zero; these are the complete one-cycles' divisors.

At every product stratum the saturated lattice is the direct sum of the
remaining primitive factor-line lattices. Lowering one factor therefore uses
its actual primitive vector, with index one in that split quotient. This does
not require the whole first-star span to be generated saturately by its rays.
For each \(0\leq r\leq d\), (P) and multilinearity give the complete
intermediate cycle
\[
 (\sum_jh_j)^r\cdot\prod_jZ_j
 =r!\sum_{\substack{I'\subset\{1,\ldots,d\}\\|I'|=r}}
       \prod_{j\in I'}(h_j\cdot Z_j)\times\prod_{j\notin I'}Z_j.
 \tag{A2}
\]
This follows by induction: words with a repeated factor give zero on its
zero-cycle, while every ordering of distinct factors has the same tensor
weights and primitive normals by (P); each subset has \(r!\) such words.
The formula lists every intermediate product stratum, not only its eventual
atom. All cycles are balanced and nonnegative. At \(r=d\) it gives
exactly the positive mass in (H). Additional homogeneous cuts preserve it by
(D)'s refinement proof at **all** stages. This proves the coefficient, including
every order and the factorial.

## Two rank-one branched factors: fibrewise pinning and all stages

Suppose every cone has rank one but \(G_1,G_2\) branch at \(v_1,v_2\).
At their stars write the actual weights as \(a\ell_i\) and \(b m_j\),
where \(\ell,m\) are primitive positive integer relations and \(a,b>0\)
are actual real scales. Choose three nonempty groups \(I_k,J_k\), with
\(S_k=\sum_{i\in I_k}\ell_i\), \(T_k=\sum_{j\in J_k}m_j\), and
tripod vectors \(\nu_1=(1,0),\nu_2=(0,1),\nu_3=(-1,-1)\).
The assignments \(L_1(q_i)=\nu_k/S_k\), \(L_2(r_j)=\nu_k/T_k\)
annihilate their **entire** kernels. They therefore extend to rational
ambient maps by rational linear algebra, without altering the original star
lattices. Set
\[
 H(x_1,x_2)=\|L_1(x_1-v_1)-L_2(x_2-v_2)\|_1.
\]
It is ambient convex rational PA. Choose rational edge-interior \(y_j\)
in every remaining factor, with primitive \(r_j\), actual weight \(w_j\),
and \(b_j=\|r_j\|_1\). Let \(F=H+\sum_{j=3}^d\rho_j\).
Ambient map matrix bounds give \(F\leq L\rho\) for some rational \(L>0\).
Apply (L), denoting its positive sum scale by \(\kappa\). In a full
product germ around \(o=(v_1,v_2,y_3,\ldots,y_d)\),
\[
                    P=C+\kappa H+\sum_{j=3}^d\kappa b_j|z_j|.
 \tag{J}
\]
Choose a homogeneous structure and \(r_0\) satisfying (V). This preserves
\(\gamma\) outside a compact set on the entire original product.

Here is the fibrewise repair of single-point pinning. Let
\(n(x_1,x_2)=\|x_1-v_1\|_1+\|x_2-v_2\|_1\).
Choose rational \(\tau>0\) so all finitely many endpoints
\[
 e_{ij}=(v_1+\tau S_kq_i,v_2+\tau T_kr_j),\quad
 \alpha_{ij}=\ell_i m_j/(3S_kT_k),\quad i\in I_k,j\in J_k
 \tag{Q}
\]
are in their original short cofaces and \(n(e_{ij})<r_0/4\).
They are nonzero, rational, and have \(H(e_{ij})=0\).
Coefficients sum to one and both projected barycentres are the star origins,
by the original relations. Choose rational extra-coordinate widths \(D_j>0\)
with \(\sum_{j=3}^db_jD_j<r_0/4\), and rational \(R\in(0,r_0/4)\).
Choose rational \(B>0\) smaller than \(R\) and every \(n(e_{ij})\).
Put on the whole product
\[
        \beta=(1-n/B-\sum_{j=3}^d\rho_j/(b_jD_j))_+,
                    u=P-\gamma+\beta.
 \tag{K}
\]
For \(d=2\) the sum is empty. Its support is contained in the chosen local
product germ: positive bump implies \(n<B\) and \(|z_j|<D_j\), hence
\(\rho<r_0/2\). This is a continuous compact rational norm tent, with
rational walls and coefficients and \(\beta(o)=1\).

Fix any rational tuple \(z\), \(|z_j|\leq D_j\). Tensor (Q) with those
fixed extra coordinates. It is a genuine PCC whose common face is the whole
bad-pair apex fibre, on the original product structure subdivided rationally
at the extra points. Its endpoints are in (J), and their bump is zero since
\(n(e_{ij})>B\). The ceiling bound and \(H(e_{ij})=0\) pin
\[
                  q(v_1,v_2,z)\leq C+\sum_{j=3}^d\kappa b_j|z_j|
                         =P(v_1,v_2,z).
 \tag{AP}
\]
This pins the full apex fibre, not merely \(o\).

For a rational bad-pair point \(x\ne(v_1,v_2)\) with \(n(x)<B\), choose
one closed homogeneous rational \(H\)-affine cone containing it in the
product of the two short stars. Its closure contains the apex. Define the
rational outer point \(y=(R/n(x))x\) in displacement coordinates. Then
\(n(y)=R>B\), and \(y\), together with each fixed \(z\) under consideration,
is in the exact germ (J): \(R+\sum b_jD_j<r_0/2\).
Both points lie before all original bounded endpoints by the choice of germ.
The tent vanishes there. The point \((x,z)\) is the same-coface PCC of
\((v_1,v_2,z)\) and \((y,z)\), with coefficients
\(1-n(x)/R,n(x)/R\). A rational local subdivision retaining the closed
\(H\)-affine cone and the extra sign faces, extended by ambient rational cuts,
is permitted. We may take that cone cell as common face for a same-cell PCC;
both endpoints lie in it. Affinity of (J), (AP), and the outer ceiling give
\(q(x,z)\leq P(x,z)\). If the bad-pair displacement is zero use (AP),
and if the bump is zero use the ceiling directly. This covers every rational
point, including all cone boundaries and zero extra displacements.

At a real point with positive bump use a small rational enclosing box or
simplex in its minimal face of the homogeneous \(H\)-affine/sign structure.
It stays in the germ; all endpoints are rational and already pinned, and
\(P\) is affine on that face. The real-centre same-face PCC gives
\(q\leq P\) exactly. At zero-faces the point is rational. Elsewhere the
bump vanishes. Since \(P\) itself is an allowed global competitor, this proves
the true equality \(P_\gamma(u)=P\) on the entire product. It requires
neither raw continuity nor a stronger growth condition nor irrational endpoints.

We supply the complete original bad-pair mass calculation below, without a
tripod pushforward. In quadrant \((sq_i,tr_j)\), write
\(q'_i=1/S_k,p'_j=1/T_l,c_k=(1,1,2)_k\). Then
\(H=c_kq'_is+c_lp'_jt\) off-group and
\(H=c_k|q'_is-p'_jt|\) in-group. Actual saturated planes have primitive
axes \(a_i=(q_i,0),b_j=(0,r_j)\). For a common denominator \(D\),
\(Q=Dq'_i,U=Dp'_j,g=\gcd(Q,U)\), the kink ray is the primitive
\(d_{ij}=(U/g)a_i+(Q/g)b_j\), with cone indices \(Q/g,U/g\).
Its first weight is \(2c_kab\ell_i m_jg/D\) and its value is zero.
At an axis the in-group quotient representative is
\(b_j+(p'_j/q'_i)a_i\). The full tangential correction gives first
axis weights \(ab\ell_i(4-2c_k)\), \(ab m_j(4-2c_l)\).
Axis plus kink first contributions have projections
\(4ab\ell_iq_i\), \(4ab m_jr_j\), so their first cycle is balanced.
The second coefficient is \(4ab\) from each axis family and zero from all
kinks, namely \(8ab\). All normals and indices are directly derived in
the included detailed calculation. No shortened version of (S) is used.

Let \(Z\) denote this actual bad-pair two-cycle, \(Z_j\) the extra primitive
line germs, \(h_0=\kappa H\), and \(h_j=\kappa b_j|z_j|\).
For **every** \(0\leq r\leq d\), the entire intermediate cycle is
\[
 (h_0+\sum_{j=3}^dh_j)^r\cdot(Z\times\prod_{j=3}^dZ_j)
 =\sum_{\substack{0\leq n_0\leq2,\ n_j\in\{0,1\}\\n_0+\sum n_j=r}}
       \frac{r!}{n_0!}\,(h_0^{n_0}\cdot Z)
                              \times\prod_{j=3}^d(h_j^{n_j}\cdot Z_j).
 \tag{A3}
\]
The factorial denominator accounts for the two identical bad-pair slots.
Prove this by expansion into words and (P): lowering an extra factor twice is
zero, lowering the bad pair a third time is zero on its zero-cycle, and every
surviving order is the displayed tensor with inherited weights. Product
saturated lattices split; the bad-pair primitive kink quotient normals and
indices remain exactly \(Q/g,U/g\) when extra line lattices are added or
removed. Other quotient normals are the primitive extra tangents. Thus (A3)
retains all axis, kink, multiple-order and zero-repeat contributions. At
\(r=d\) only \(n_0=2,n_j=1\) survives, giving exactly the mass in (T).
This derives its coefficient from all stages rather than guessing a tensor mass.

## Complete integrals and exhaustion of the criterion

In both failures the common old structure \(\Pi\) has only \(o\) as a
zero-face where the bump can be positive, by (V). The actual envelope has
exact gap \(-\beta\), equal to \(-1\) there and zero at every other old
measure vertex. Its measure is the finite nonnegative complete \(d\)-stage
PA zero-cycle. Refining for the obstacle can introduce vertices with positive
bump, but at every stage refinement gives the inherited cycle; any zero-face
that was not an old zero-face inherits zero top coefficient. There is no mass
on open positive-dimensional strata, no diffuse term, and no point at infinity.
The full measures of \(P+1/n\) are identical, so regularization adds no
escaped or boundary mass. Consequently the **entire** contact integrals are
exactly (H) and (T), not merely negative contributions at an isolated atom.
All remote components, cycles, bounded edges and ends have zero gap at their
possible measure atoms. Formula (M) also preserves total reference mass.

If a cone has higher rank the first construction works with arbitrary other
factor graphs, by their rational edge interiors. If every cone has rank one
but two factors branch, the second construction applies with all remaining
factors tested at edge interiors. Otherwise at most one factor branches and
the positive cylinder reduction applies. These alternatives exhaust the
proposed geometric criterion, including failures occurring in different
components of different factors. The localizations are global, so any failed
component tuple suffices against the originally prescribed reference.

There is no intentionally unresolved step within this claimed finite-product
theorem. It is an unverified author proof draft requiring independent mathematical
assessment. The arbitrary-balanced-carrier original atom remains open. The
following complete elementary and cylinder proofs and primary source bodies are
part of this argument; receipts, hashes, diagnostics and compilation do not
grant their correctness.

