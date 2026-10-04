# Sylvester height slices and explicit local models

Date: 4 October 2026. This is a worked application of the known
triangulation result in Caicedo–Castillo–Juhnke–Poullot,
arXiv:2609.23710v1, Theorem 3.5, physical page 11. It is kept
outside the active book while its integration location and
ordinary source audit are completed. No general CY degeneration,
new priority claim, independently verified theorem or enumeration
is asserted.

## 1. The source family and the part of the proof used

Let s_0=1 and s_i=1+product_{j=0}^{i-1}s_j. Thus s_1=2,
s_2=3 and s_3=7. For integers d>=1 and k>=0, put

    P_d^k = conv(0,s_1 e_1,...,s_{d-1}e_{d-1},
                    (k+1)(s_d-1)e_d).

The source proves existence of a flag, coherent, ambient-unimodular
triangulation. Only its introduction and Section 3.1 proof are
freshly read at this checkpoint, not all 29 pages or its later
Ehrhart results. The proof uses integral chimney functions and
a particular one-point extension with a single visible facet.
The required specific extension is checked below rather than
using its overly broad auxiliary quotation without qualification.

For the base Q_d=conv(0,s_1e_1,...,s_{d-1}e_{d-1}), set

    ell=0,
    u(x)=(k+1)(s_d-1-sum_{j<d}((s_d-1)/s_j)x_j).

Every coefficient is integral, because s_d-1 is the product of
s_1,...,s_{d-1}. The chimney between ell and u over Q_d is
exactly P_d^k: its upper function vanishes at the nonzero
base vertices and has the stated last intercept at zero.

HPPS v3 Theorem 2.8 and its proof, physical pages 20–21,
provide the required existence version: pull back coherent
base weights and choose a full pulling refinement. It is
unimodular, and its minimal nonfaces have no greater size
than those of the base triangulation. Thus a flag coherent
unimodular base gives such a chimney triangulation. The
theorem's literal claim about every full refinement being
regular is not needed and is diagnosed below.

For the induction, Q_d is obtained from P_{d-1}^0 by replacing
its last intercept s_{d-1}-1 by s_{d-1}. Only the facet opposite
zero is visible from the extra point. Write T=s_{d-1}-1
=product_{j<d-1}s_j. That visible facet has primitive integral
normal

    (T/s_1,...,T/s_{d-2},1),

and equation <normal,x>=T. The new point has normal value
T+1. Its lattice distance to the visible facet is exactly one.
Coning any unimodular boundary simplex therefore preserves
ambient unimodularity. For d=2 the visible facet is a point,
and the same distance calculation is the unit-segment case.
For d=1 the initial simplex is [0,k+1], with its ordinary
unit subdivision; Q_1 is a point.

The visible facet's triangulation is a full induced subcomplex
of the original triangulation: a simplex whose vertices lie
in that facet is contained in it. Coning precisely this
subcomplex with the new vertex preserves flagness. Any
clique containing the new vertex has all its other vertices
in the facet; they already form a simplex there. Cliques
without the new vertex are handled by original flagness.

Regularity can be checked with the heights. Retain the old
coherent weights and choose the new vertex's height H
sufficiently large. The old lower simplex planes remain
below the new lifted point. On the visible facet, each
boundary simplex's supporting plane can be extended through
the new lifted point; increasing H drives that plane below
all old vertices off the facet. There are finitely many
inequalities, so one H works for all of them. These old
simplices and the cones over the visible facet cover the
extension and give the prescribed coherent triangulation.
This verifies the special one-visible-facet construction
actually used in Proposition 3.4 and Theorem 3.5.

Induction with the chimney construction now gives the stated
known source result for P_d^k, including d=1 and k=0.
This is a source-aware elaboration of that proof, not a claim
to have checked its independent Ehrhart-unimodality and
magic-positivity assertions.

## 2. A monomial family with this exact height slice

Put q=(k+1)(s_d-1). In coordinates z_0,...,z_d define

    t = z_0 z_d product_{i=1}^{d-1} z_i^{q/s_i}.

All exponents are positive integers. Make the degree-q
parameter cover t=tau^q and normalize. In the earlier local
cyclic-cover calculation the character lattice is

    M' = Z^{d+1}+Z(b/q),
    b=(1,q/s_1,...,q/s_{d-1},1),

and its dual is N'={v in Z^{d+1}:b.v in qZ}. Since b_0=1,
the local ordinary root has only one irreducible factor; no
global connectedness claim is inferred from that local fact.
Every b_i divides q, so the normalized central divisor is
reduced. Its total space need not yet be regular.

The height-one slice is {v>=0:b.v=q}. Project to the last
d coordinates. Then v_0=q-sum_{i=1}^{d-1}(q/s_i)v_i-v_d,
and the projected simplex is exactly P_d^k. Projection of
the difference lattice ker b to Z^d is a lattice isomorphism,
because b_0=1 determines v_0 integrally. This checks the
ambient lattice; using only the vertex-generated lattice
would miss the regularity issue.

Cone over a coherent unimodular triangulation of P_d^k.
Its cones are regular in N' and every primitive generator
has height one for b/q. The normalized toric modification
is projective, its total space is regular and its central
divisor is reduced SNC. On a maximal regular toric chart,
tau is the product of its d+1 boundary coordinates, since
it takes value one on every primitive basis vector.

Projectivity here uses the known coherent-triangulation/toric
support-function dictionary. A compatible integral support
function shifted by a large parameter form gives a vertical
monomial ideal, whose normalized blowup realizes this fan.
It is an isomorphism where tau is nonzero. This is an
explicit local affine model; it does not glue independent
charts of an arbitrary compact degeneration or identify a
global CY metric.

## 3. Dimension three and the exact number of maximal cells

For d=3 the example is

    t=z_0 z_1^{3(k+1)} z_2^{2(k+1)} z_3,
    q=6(k+1),
    P_3^k=conv(0,2e_1,3e_2,6(k+1)e_3).

Its normalized lattice volume is 2*3*6(k+1)=36(k+1).
Every unimodular triangulation therefore has exactly
36(k+1) maximal tetrahedra, by additivity of normalized
volume. This is an exact consequence of unimodularity,
not a computer enumeration of triangulations.

The unrefined normalized cone has primitive boundary
vectors q e_0, 2e_1, 3e_2 and q e_3. The index of their
span in N' is (q*2*3*q)/q=6q=36(k+1), matching the
slice volume. The equality explains why reducedness alone
does not give a smooth total space and why the coherent
unimodular refinement resolves that remaining index.

In general the number of maximal d-simplices is
(k+1)(s_d-1)^2, since product_{i<d}s_i=s_d-1. The d=1
case gives k+1 unit intervals. The zero-dimensional base
of the induction and k=0 are included throughout.

## 4. Two overbroad auxiliary statements are not used

On physical page 10 the Sylvester paper quotes a one-point
extension rule that claims the extension retaining a flag
triangulation and adding cones over visible faces is flag
without a visibility restriction. The prescribed extension
need not have that property. Let P=[0,1]^2, triangulated
along (0,0)--(1,1), and let x=(2,-1). The original two-
triangle triangulation is flag, coherent and unimodular.
The visible facets from x are the bottom and right edges.
The prescribed extension has the edges from x to (0,0)
and (1,1), as well as the old diagonal between these
vertices. Their triple is a clique, but not a triangle
of the extension: (1,0) lies in its interior, and the
prescribed added triangles use the visible bottom/right
edges. Thus its flag conclusion for that triangulation
fails. This does not claim that the larger polygon has
no other flag triangulation. It also does not contradict
the one-visible-facet case used for Sylvester simplices,
whose visible subcomplex is induced as verified above.
The cited CJP25 primary paper has not been inspected.

HPPS v3 Theorem 2.8, page 20, literally says every full
refinement of the integral pullback is regular when the
base triangulation is regular. Its displayed proof only
establishes that a full pulling refinement can be chosen
regular. The stronger literal claim fails as follows.

Take Q=[0,2]^2. Let c=(1,1), and list its boundary lattice
points cyclically as

    v_0=(0,0), v_1=(1,0), v_2=(2,0), v_3=(2,1),
    v_4=(2,2), v_5=(1,2), v_6=(0,2), v_7=(0,1).

The eight triangles conv(c,v_i,v_{i+1}) (indices modulo
eight) are unimodular. They form a regular full base
triangulation: pull c, then pull the boundary midpoints.
Over P=Q times [0,1], triangulate each triangular prism
by the staircase order c<v_i<v_{i+1}. Orders on a shared
edge c--v_i agree, so these prism triangulations glue to
a full refinement of the pullback. Each boundary vertical
quadrilateral over v_i--v_{i+1} has the same cyclic
choice of diagonal.

If weights w(v,j) induced this refinement, write
delta_v=w(v,1)-w(v,0). The chosen diagonals on those
eight quadrilaterals require delta_{v_i}>delta_{v_{i+1}}
for every i, with the reverse common orientation giving
the same impossibility. Summing the strict inequalities
gives 0>0. Thus this refinement is not regular. The
counterexample concerns the universal quantifier on
refinements. The full pulling refinement existence used
above remains exactly the valid input proved in the source.

## 5. Integration boundary

This local example is related to the book's toroidal models,
height slices, reducedness and projective modifications.
It uses a recent known source result and direct explicit
lattice computations. It can be considered as an explanatory
worked example after an ordinary source/integration audit;
no new universal theorem or alteration of the 42 statuses
is suggested. Book admission of any genuinely new statement
still requires the independent exact-byte verification protocol.
