## New higher-relation obstruction for every fixed real reference

We now remove the rank-one hypothesis. Suppose \(G=G_1\) has a vertex
\(v\) with \(\dim\operatorname{span}K_v\geq2\). Write its incident
actual primitive directions as \(q_i\) and its strictly positive actual
weights as \(w_i\). Interchanging factors treats \(G_2\).
Choose any edge of the other nonempty pure graph \(H\) and a rational point
\(y_0\) in its relative interior. Insert \(y_0\) as a harmless bivalent
vertex. Let \(r\) be its actual primitive tangent vector and \(w_H>0\)
the actual weight of that edge on both sides. Put \(o=(v,y_0)\).

### Proper-support relation and an intrinsic graph cap

The rational cone \(K_v\) is pointed, since it lies in the nonnegative
orthant. Its finite-generation proof above gives a rational extreme-ray
generator \(c\ne0\). An extreme generator cannot have every coordinate
strictly positive. If it did, the equality
\(\operatorname{span}K_v=\ker Q_v\) and rank at least two would give a
kernel vector \(d\) independent of \(c\). For sufficiently small
\(a>0\), both \(c+ad\) and \(c-ad\) are nonnegative kernel vectors.
Their sum is \(2c\), contradicting the defining extreme-ray property
that any such summands belong to its ray. Thus
\[
 I=\{i:c_i>0\}\quad\hbox{is nonempty and proper},\qquad
 s_i=\begin{cases}0&i\in I,\\1&i\notin I,\end{cases}
 \quad c\mathbin{\cdot}s=0,
 \quad M:=\sum_iw_is_i>0.                                  \tag{HR1}
\]
Because \(s_i\geq0\), \(d\mathbin{\cdot}s\geq0\) for every
\(d\in K_v\). This is intrinsic PC data; no ambient extension of \(s\)
is used.

Choose ambient lattice bases and their rational \(\ell^1\) norms. Set
\(\rho_1(x)=\|x-v\|_1\), \(\rho_2(y)=\|y-y_0\|_1\), and
\(\rho=\rho_1+\rho_2\). The homogeneous recession norm is
\(\rho_0(d_1,d_2)=\|d_1\|_1+\|d_2\|_1\).
On \(x=v+tq_i\), \(t\geq0\), the first norm is \(r_it\), where
\(r_i=\|q_i\|_1>0\) is an integer. On the chosen second edge it is
\(\rho_2(y_0+zr)=b|z|\), \(b=\|r\|_1>0\) an integer.
Choose rational \(0<\varepsilon<\min_i r_i\). Choose rational star lengths
\(L_i>0\) before every other graph or norm breakpoint and every bounded
edge endpoint. They can be chosen small enough to avoid all nonincident
carrier pieces. Choose rational
\[
       0<A<\min_i L_i(r_i-\varepsilon s_i),\qquad
       t_i=A/(r_i-\varepsilon s_i)\in(0,L_i).                \tag{HR2}
\]
On this closed star replace \(\rho_1\) by
\[
 F_1(v+tq_i)=\max\{r_it,A+\varepsilon s_it\}\quad(0\leq t\leq L_i),
                                                               \tag{HR3}
\]
and use \(F_1=\rho_1\) elsewhere on **all components** of \(G\).
At \(v\) every piece has value \(A\), so this is continuous. Before
\(t_i\) the slope is \(\varepsilon s_i\), and after it the slope is
\(r_i>\varepsilon s_i\). At \(L_i\) and beyond it is exactly the norm.
The central slope inequalities are (HR1), the only new edge bends are upward,
and every other local test is that of the ambient convex norm. Thus (G1)
proves actual PC at every real centre on every allowed graph structure.
The finitely many \(t_i\), endpoints and norm walls are rational. Its
affine slopes and values in rational coordinates are rational. Hence \(F_1\)
has a finite rational spatial PA structure and is actual PAPC on all ordinary
opens. Globally,
\[
                0\leq F_1-\rho_1\leq A,                   \tag{HR4}
\]
with compact support in the selected star. This is a genuine local intrinsic
cap glued back into the norm, not an ambient convex function in disguise.

By (G2), \(F(x,y)=F_1(x)+\rho_2(y)\) is actual PC and actual PAPC on the
entire product, on finite rational domains, with rational affine coefficients.
It satisfies \(\rho\leq F\leq\rho+A\). In a rational product star of
\(o\) its germ is
\[
                  F(v+tq_i,y_0+zr)=A+\varepsilon s_it+b|z|. \tag{HR5}
\]
Its intrinsic nature causes no product convexity gap: the proof of (G2)
uses factor tangent families, not an ambient extension of the cap slopes.

### Exact sum localization of the prescribed reference

Use the already reconstructed finite rational PC cone and exact decomposition
(FC6) for the **given** real \(\gamma\):
\[
           \gamma=\sum_{j=1}^J\lambda_j\gamma_j,\qquad
           \lambda_j>0,\quad\sum_j\lambda_j=1.              \tag{HR6}
\]
Each \(\gamma_j\) is actual PC with rational coefficients on the same
finite rational complex, retaining **every** strict recession inequality.
Apply (29)--(31), with the present centre \(o\), to each one. Those proofs
use only finite pointed cells and positive recession slopes, so require no
rank or branching hypothesis. They give rational \(m_j>0,B_j\geq0\) such
that \(\gamma_j\geq m_j\rho-B_j\) everywhere on all components.
Choose rational \(0<\delta_j<m_j\) and rational \(C_j\) such that
\(C_j+\delta_jA>\gamma_j(o)+2\). Define
\[
 P_j=\max\{\gamma_j,C_j+\delta_jF\},\qquad
 P=\sum_j\lambda_jP_j,\qquad
 \delta=\sum_j\lambda_j\delta_j>0,
 \quad C=\sum_j\lambda_j(C_j+\delta_jA).                   \tag{HR7}
\]
Maxima of PC functions satisfy every Jensen test. Rational coefficients in
each \(P_j\) give rational comparison walls; common rational refinements
give finite rational domains. The estimate
\[
 \gamma_j-(C_j+\delta_jF)
       \geq(m_j-\delta_j)\rho-B_j-C_j-\delta_jA             \tag{HR8}
\]
shows \(P_j=\gamma_j\) off a compact set. Therefore the positive sum
\(P\) is actual PC, real PA on a finite common rational refinement,
\(P\geq\gamma\), \(P=\gamma\) outside a compact set on the whole
original product, and \(P\in\gamma+O(1)\). We take no maximum with the
real reference, which could create irrational spatial walls. Every strict
reference recession slope persists, since a bounded affine difference on a
common cell has slope zero on every recession vector. Actual PAPC against
all real local one- and two-cycles follows from the proved cycle tests.
The explicit sequence \(P+1/n\) gives uniform decreasing regularization
in the unchanged reference class, with identical recursively defined measures.

Continuity and the strict inequalities defining \(C_j\) give a common
neighbourhood on which all localizers dominate. Within the cap star and the
second-edge interior, the germ is
\[
                 P(v+tq_i,y_0+zr)=C+\delta\varepsilon s_it
                                               +\delta b|z|. \tag{HR9}
\]
This statement is global localization of every real reference, not just an
example of a convenient separable reference. The reference itself and the
function \(P\) away from the chosen germ can be nonseparable.

Choose a finite rational product/function structure \(\Pi\) for all these
functions by cutting by their finitely many rational supporting hyperplanes.
Insert \(o\) in the original product. Choose a sufficiently small rational
\(r_0>0\) so that \(\rho<r_0\) meets only the short original product
star of \(o\), lies in (HR9), and avoids every cutting hyperplane not through
\(o\), every nonincident carrier cell, every cap bend and every other bounded
endpoint. Finiteness and positive distances from the relevant closed sets
give such a radius. All spatial constraints in this neighbourhood are now
homogeneous about \(o\). Every nonzero point admits a short radial expansion
and contraction in its minimal face, so cannot be a vertex. Consequently
\[
                   \Pi^{(0)}\cap\{\rho<r_0\}=\{o\}.        \tag{HR10}
\]
The proof is invariant under all the homogeneous cuts through \(o\), including
those inherited from the original nonseparable real reference's rational
domains. No norm ball is equated with a product star.

### Compact bump, supported pinning and true global raw equality

Choose rational \(T,B,D>0\), \(B<T\), small enough that all segments
\(0\leq t\leq T\), \(|z|\leq D\) on every incident quadrant lie in
\(\rho<r_0\). Explicitly it suffices that
\(\max_i r_iT+bD<r_0\), and the earlier star restrictions can be included
by shrinking these numbers. On these quadrants put
\[
          \beta(v+tq_i,y_0+zr)
                    =\max\{0,1-t/B-|z|/D\},                \tag{HR11}
\]
and set it equal to zero outside the short product star. Its common value
at \(t=0\) agrees on all branches. It is zero before the outer boundary
of that star, so it glues continuously to zero. Its walls and affine
coefficients are rational, it is nonnegative, bounded and compactly supported,
\(\beta(o)=1\), and its support is contained in \(\rho<r_0\).
It vanishes at \(t=T\) for every \(z\). Set
\[
                        u=P-\gamma+\beta.                 \tag{HR12}
\]
This is a nonnegative compactly supported bounded continuous real-PA obstacle
on a finite rational common structure, with \(\gamma+u=P+\beta\).

Let \(q\) be **any actual raw competitor** below \(P+\beta\), with only
\(q\leq\gamma+C_q\) as its growth condition. No continuity or lower growth
bound is assumed. For rational \(z\), \(|z|\leq D\), the endpoints
\[
        x_i(z)=(v+Tq_i,y_0+zr)\quad(i\in I),\qquad
        \alpha_i=c_i/\sum_{k\in I}c_k                       \tag{HR13}
\]
are rational; their barycentre is \((v,y_0+zr)\) since \(\sum c_iq_i=0\).
They form a genuine PCC: on a rational product subdivision their cofaces
are the closed incident strips, with common face the closed fibre over \(v\).
That face contains the centre even when it is not a zero-face. The bump
vanishes at these endpoints. Equations (HR1) and (HR9) give
\[
 q(v,y_0+zr)\leq\sum_i\alpha_iP(x_i(z))
       =P(v,y_0+zr).                                        \tag{HR14}
\]
For rational \(t\in[0,B]\) and rational \(z\in[-D,D]\), the two rational
endpoints \((v,y_0+zr)\), \((v+Tq_i,y_0+zr)\) lie in a common rational
product cell. Their same-cell PCC, (HR14), and affinity of (HR9) in \(t\)
give
\[
              q(v+tq_i,y_0+zr)\leq P(v+tq_i,y_0+zr).        \tag{HR15}
\]
Outside the bump this bound holds directly from its ceiling. Thus it holds
on all rational points of the local product star.

To extend the bound to **every real centre**, take the minimal face of a
rational local quadrant structure (split at \(z=0\)). Its relative interior
has dense rational points. In rational affine coordinates, an arbitrarily
small rational box or simplex enclosing the given real point within that
relative interior expresses it as a real barycentre of rational endpoints
in that same face. This follows by choosing rational coordinate endpoints
strictly on either side of its coordinates; product barycentric coefficients
are nonnegative and sum to one. At dimension zero the point is already
rational. Every endpoint is in the local germ and satisfies (HR15) or the
direct ceiling bound. Since \(P\) is affine on this face, the same-cell PCC
gives \(q(x)\leq P(x)\) exactly. At \(t=0\) use the rational fibre face;
at \(z=0\) use its rational horizontal face. This proves pinning also at
real \(z\), without using irrational endpoints or raw continuity.

On the rest of \(X\), \(\beta=0\), so \(q\leq P\) directly. All remote
vertices, components, ordinary cycles, bounded edges and ends are included.
Conversely \(P\) is a global actual-PC competitor in the allowed upper
growth class. Therefore
\[
                    P_\gamma(u)=P\quad\hbox{on all }X.     \tag{HR16}
\]
The raw upper growth condition was neither strengthened nor needed for this
upper-bound argument. The equality is for the prescribed reference, not for
a substituted one.

### Both actual primitive-normal stages and the complete integral

Write \(k=\delta\varepsilon\), \(l=\delta b\). The local homogeneous
germ after subtracting \(C\) is \(h(tq_i,zr)=ks_it+l|z|\).
Its natural fan has rays
\(a_i=(q_i,0)\), \(b_+=(0,r)\), \(b_-=(0,-r)\), and quadrants
\(\langle a_i,b_\pm\rangle\), with weights \(w_iw_H\).
The saturated lattice in each plane is exactly
\(\mathbb Za_i\oplus\mathbb Zb_+\): an ambient product lattice vector
in that plane has integral coefficients in each primitive factor line.
Thus every axis-plane index is one and the primitive quotient normals are
the other axis vectors. A nonsaturated ray-generated **whole star** span does
not alter these saturated plane lattices.

At \(a_i\) the two primitive normals are \(b_+,b_-\). Their weighted sum
is zero, and (5) gives
\[
                       D_h(a_i)=2l w_iw_H.                 \tag{HR17}
\]
At either \(b_\pm\) the primitive normals are all \(a_i\). Their weighted
sum is \(w_H\sum_iw_i a_i=0\), so the tangential correction is again zero
and
\[
                       D_h(b_\pm)=kMw_H.                  \tag{HR18}
\]
These are **all** rays in this natural germ fan. Their first-cycle balance
holds: its first projection is \(2lw_H\sum_iw_iq_i=0\), and its second
projection is \(kMw_H(r-r)=0\). The function values at primitive rays are
\(h(a_i)=ks_i\), \(h(b_\pm)=l\).
The second divisor (7) therefore has graph-axis contribution
\(\sum_i(2lw_iw_H)(ks_i)=2klMw_H\), and transverse-axis contribution
\(2(kMw_H)l=2klMw_H\). Thus the complete mass is
\[
 \mathrm{MA}_{\mathrm{poly},\mathbb R}(P)\{o\}
       =4klMw_H=4\delta^2\varepsilon bMw_H>0.                \tag{HR19}
\]
The coefficient includes both stages and both axis families. It retains the
factorial \(2!\): the two mixed orders contribute equally. There is no
division, probability normalization or singular-face Alexandrov substitution.
Any extra homogeneous rays from \(\Pi\) retain precisely this coefficient
by the independently proved successive refinement compatibility; their
indices are accounted for by that primitive-normal proof, not ignored.

The complete global PA measure is the finite nonnegative zero-cycle supported
on \(\Pi^{(0)}\). Its exact gap in (HR12) and (HR16) is \(-\beta\), which
is \(-1\) at \(o\) and zero at **every other** \(\Pi\)-vertex by (HR10).
Consequently the full integral, including all remote and refinement strata,
is exactly
\[
 \int_X(P_\gamma(u)-\gamma-u)
              \mathrm{MA}_{\mathrm{poly},\mathbb R}(P_\gamma(u))
                  =-4\delta^2\varepsilon bMw_H<0.           \tag{HR20}
\]
Refining for the rational bump walls can introduce other vertices with
positive \(\beta\); they have zero second coefficient because the PA
measure is inherited from \(\Pi\). No measure lies on open edges or faces.
The operator is the finite PA zero-cycle on \(X\); it has no point at infinity.
The uniform decreasing sequence \(P+1/n\) has identical measures, so adds
no escaping mass or boundary term. This is an actual regularizable exact
raw envelope and a **complete** negative integral, with no regularity-failure
alternative and no inference from an isolated positive atom alone.

## Completion of the arbitrary two-graph criterion

If all cones in both graphs have rank one and one factor is unbranched,
the reconstructed cylinder proof supplies rational-domain actual-PAPC raw
envelopes and complete contact for every bounded real-PA obstacle and every
prescribed real reference. It treats nonseparable data and all components.

If a factor has higher-rank relations, (HR1)--(HR20) apply regardless of the
other factor's relation cones or branching; nonemptiness and pure dimension
one supply its rational edge-interior point. If neither factor has higher
rank, but neither is unbranched, each has a branched junction; the complete
reconstructed rank-one two-branch construction gives \(-8\kappa^2ab<0\).
These alternatives exhaust the failure of the proposed criterion. A branch
in one component and a bad vertex in another cause no issue: any failed
component pair suffices, and the constructions have global compact support
and unchanged reference at infinity. This proves exactly the stated broader
finite two-graph classification, with arbitrary positive actual real weights
and actual saturated lattices.

The source's one-dimensional accessible-mass theorem is neither used as a
premise nor claimed as new. Its proof only pins a vertex and invokes a
one-dimensional envelope theorem. Here pinning is throughout the product
bump, gives the exact full raw envelope directly, and the negative integral
is fully evaluated after both two-dimensional primitive-normal stages.
The original arbitrary-balanced-space P05.2 and the catalogue's other
higher-dimensional residual problems remain open.
