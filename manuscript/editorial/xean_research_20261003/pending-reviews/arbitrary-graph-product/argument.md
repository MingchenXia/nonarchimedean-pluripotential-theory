---
title: "Envelope contact on arbitrary finite balanced graph products"
author: "Unverified P05.2 partial proof draft"
date: "4 October 2026"
---

## Exact broader theorem and original residual scope

Let \(G_i\subset N_{i,\mathbb R}\), \(i=1,2\), be any two nonempty finite
embedded balanced rational pure graphs. Use the actual ambient lattices,
their saturated face lattices, arbitrary strictly positive actual real edge
weights, and product weights on \(X=G_1\times G_2\). All bounded edges,
cycles, ends, full lines, and finitely many disconnected components are retained.
At a graph vertex \(v\), let \(q_e\) be its actual primitive outgoing
directions and put
\[
 K_v=\{c\in\mathbb R_{\geq0}^{E(v)}:\sum_e c_eq_e=0\}.
                                                               \tag{1}
\]
Its rank is the dimension of its real span. A graph is unbranched if every
carrier junction is bivalent, including a component presented as a whole line.
Artificial rational bivalent vertices may be inserted.

Fix **each prescribed** continuous real-coefficient actual-PC reference
\(\gamma\), affine on a finite rational spatial structure and positive at
infinity. Functions use the explicit real scalar extension of PA on finite
rational spatial domains; local cycles and actual balancing weights use real
coefficients. Rational spatial domains are not inferred from real affine
comparison coefficients.

**Theorem (unverified broader special-case proof).** The following property of
this fixed \((X,\gamma)\) holds if and only if both graphs have rank-one
local nonnegative relation cones at every vertex and at least one graph is
unbranched: for every bounded continuous real-PA rational-domain obstacle
\(u\), the actual raw envelope \(P_\gamma(u)\) is continuous actual PAPC
on a finite rational spatial structure, belongs to \(\gamma+O(1)\), has a
uniform decreasing actual-PAPC regularization, and satisfies complete contact
\[
 \int_X(P_\gamma(u)-\gamma-u)
       \mathrm{MA}_{\mathrm{poly},\mathbb R}(P_\gamma(u))=0.      \tag{2}
\]
The operator is \(P\cdot(P\cdot[X])\), with no division by \(2!\).

In particular, if either graph has a vertex \(v\) with rank at least two,
then for **every prescribed** such real reference and every rational interior
point \(y_0\) of an edge of the other graph there is a nonnegative compactly
supported bounded continuous real-PA rational-domain obstacle \(u\) with an
exact actual-PAPC raw envelope \(P\), unchanged reference at infinity,
explicit regularization \(P+1/n\), and full negative contact integral
\[
 P_\gamma(u)=P,\qquad
 \int_X(P-\gamma-u)\,\mathrm{MA}_{\mathrm{poly},\mathbb R}(P)
       =-4\delta^2\varepsilon b M w_H<0.                       \tag{HR0}
\]
Here \(\delta,\varepsilon,b>0\), \(w_H>0\) is the actual other-edge
weight, and \(M>0\) is an explicitly constructed positive actual first-factor
slope mass. Both intermediate contributions to the coefficient are included.
If instead both graphs have rank-one cones but both branch, the reconstructed
supporting construction below gives the full integral \(-8\kappa^2ab<0\).

The new result removes the local rank-one hypothesis from the finite
two-graph classification. The known one-dimensional classification and the
earlier rank-one two-graph classification are **not** presented as new results.
Their relevant supporting proofs, including the positive cylinder argument,
are reconstructed in full here. No source-dependent conclusion, canonical
note, accepted rendering, receipt, review or hash is a mathematical premise.

This is a substantial special case of the original P05.2, with status
**partial** and candidate **false**. The arbitrary balanced-space atom remains
open. No literal coefficient classification, analytic realization, additional
factor theorem, general singular-fan contact theorem, or P06.2 conclusion is
claimed. The exact original task and completion criteria are preserved as
unaltered strings in `task.json` and `original-scope.txt`; the current assignment
is in `assignment.txt`. Those strings define the original residual scope.
All results are unverified drafts. Same-model author audit, compilation and
finite arithmetic diagnostics do not establish mathematical correctness or
priority.


## Definitions, source checks, and actual intersection algebra

The controlling book files are Chapter 72, `ch72_major_open_problems.tex` (polyhedral section, original problem and residual scope), and Appendix M, `appM_ch18_frontiers.tex` (analytic zero-current catalogue, no product theorem used). Their complete paths and read-only-origin snapshots of the current read-only origins are in `sources/` and `source-hashes.json`. The exact original
problem and completion criteria are preserved verbatim as JSON strings in `task.json`,
and the execution assignment in `assignment.txt`. Neither book status nor prior review
is a proof input. Appendix M concerns the analytic continuous zero-current frontier;
no P06.2 result is used or claimed. BMPS, *Monge--Ampère measures on balanced polyhedral spaces*, arXiv:2603.08664v1, dated 10 March 2026, supplies definitions only. The explicit extension used here has real function coefficients and real cycle weights; BMPS Definition 2.28 itself has integral slopes/rational constants. On any fixed finite rational complex, affine-piece continuity is a rational linear system; its real solution space has a rational basis, each made literal by clearing slope denominators. Thus this convention is the real scalar extension on that complex.

A PCC (BMPS Definitions 3.2--3.3) has rational endpoints \(x_i\in X\cap N_{\mathbb{Q}}\), real coefficients \(\alpha_i\geq0\), \(\sum\alpha_i=1\), and the actual, possibly irrational, centre \(x=\sum\alpha_i x_i\). On some allowed rational structure there must be faces \(\tau\preceq\sigma_i\) containing \(x\) and \(x_i\). A finite raw PC function satisfies Jensen for **every** such combination, across all allowed structures and remote endpoints. No continuity of raw competitors is assumed.

With \(f=\gamma+u\), the raw envelope (Definition 6.2) is
\[
 P_\gamma(u)(x)=\sup\{q(x):q\in\mathrm{PC}(X),\ q\leq f,
                          \ q\leq\gamma+C_q\text{ for some constant}\}.
                                                               \tag{4}
\]
The last condition is only upper growth. The regularization class has two-sided growth (Definitions 3.14, 3.23). Positive at infinity (Definition 4.15) means strictly positive slope on every nonzero recession vector of every affine reference cell. PAPC (Definition 3.1, here with real weights) tests \(h\cdot z\geq0\) for every nonnegative balanced real local cycle on every ordinary open, in every positive dimension. On this two-dimensional carrier only dimensions one and two can be nonzero.

Use the actual lattice \(N_\sigma=N\cap\operatorname{span}_{\mathbb{R}}(\sigma-\sigma)\). For a facet \(\tau\prec\sigma\), \(n_{\sigma/\tau}\) lifts the primitive positive class in \(N_\sigma/N_\tau\). The divisor formula (Definition 2.31) is
\[
 (h\cdot z)(\tau)=\sum_{\sigma\succ\tau}z(\sigma)h_\sigma(n_{\sigma/\tau})
       -h_\tau\left(\sum_{\sigma\succ\tau}z(\sigma)n_{\sigma/\tau}\right).
                                                               \tag{5}
\]
The second sum is tangential by balancing. Changes of lift cancel because the linear parts agree on tangents. Formula (5) is real bilinear, depends only on incident germs, and annihilates ambient affine functions.

Here is a direct reconstruction of refinement and balancing, rather than an appeal to source intersection theory. For a new tested facet in a refinement, take its minimal old face. If its dimension exceeds the cycle dimension, inherited incident cycle weights are zero. If its dimension equals the cycle dimension, the two inherited pieces in that plane have equal weights and affine parts and opposite primitive quotient normals, so cancel. If its dimension equals the tested facet dimension, the actual tangent lattice and incident normal classes agree with the old ones, so the old coefficient is inherited. These cases prove refinement compatibility and inherited balancing. They apply successively to both divisors; in particular new vertices in affine edges cannot create a zero-cycle coefficient.

For balancing of the first divisor of a two-cycle, translate a vertex to zero and take a pointed rational local fan, adding harmless rational cuts if necessary. In a two-cone with primitive rays \(r,s\), let
\[
 \chi_{rs}=[N_C:\mathbb{Z}r+\mathbb{Z}s],\qquad \omega_{rs}=z(C).
\]
Extending primitive \(r\) to a basis of the saturated plane lattice shows that its inward primitive quotient normal is represented by \(s/\chi_{rs}\). A nonintegral representative has only a tangential discrepancy from an integral lift, which cancels in (5). Top balancing and the first weight are
\[
 \sum_{C\succ r}(\omega_{rs}/\chi_{rs})s=t_r r,
 \qquad D_h(r)=\sum_{C\succ r}(\omega_{rs}/\chi_{rs})h(s)-t_rh(r). \tag{6}
\]
Summing \(D_h(r)r\), the first terms, once per unordered cone, are
\(\omega_{rs}(h(s)r+h(r)s)/\chi_{rs}\). Substituting top balancing into the subtracted terms gives exactly the same sum. Hence \(\sum_rD_h(r)r=0\). This proves first-divisor balancing for real weights in every germ. The full second coefficient is
\[
                       (h^2\cdot[X])\{0\}=\sum_rD_h(r)h(r).     \tag{7}
\]
Every intermediate ray, including zero-weight or zero-value rays, belongs to this formula.

The same fan calculation proves **mixed commutativity**, rather than importing
BMPS Lemma 2.35's external intersection premise. At a common structure vertex,
write both affine germs as homogeneous functions \(h,g\) after subtracting
their values. Applying (5) to the balanced one-cycle from (6) gives
\[
 \begin{split}
 (g\cdot(h\cdot z))\{0\}
  &=\sum_{\{r,s\}}\frac{\omega_{rs}}{\chi_{rs}}
                 \bigl(h(s)g(r)+h(r)g(s)\bigr)
                   -\sum_r t_r h(r)g(r).
 \end{split}                                               \tag{M}
\]
The right side is symmetric in \(h,g\), and includes all rays and their
actual saturated indices. For a one-cycle, its divisor is a zero-cycle,
whose balancing has no condition. Thus all recursive stages needed on this
two-dimensional carrier are balanced. Refinement compatibility at each stage
globalizes (M) and proves locality at every zero-face. Adding an ambient affine
function to either slot changes no first divisor and gives zero against the
balanced intermediate one-cycle in the second slot, so also changes no mixed
coefficient. This justifies every affine subtraction in the contact proof.
At a nonvertex, any rational refinement that inserts a zero-face inherits zero
second weight unless the old structure already had that vertex. Consequently
there is no hidden measure on open lower faces or top-face interiors.

 Product balancing
itself holds in the actual lattice: at an edge times a graph vertex, the quotient
primitive normals are the primitive directions of the second graph, and the weights
are the first edge weight times its balanced incident weights; the other type of
facet is symmetric. Interior subdivision facets have equal weights and opposite
normal classes. Thus the product is the actual balanced real two-cycle used here. Definition 4.4's complete measure is the resulting finite zero-cycle on structure vertices. On a unit complete plane, \(|s|+|t|\) has first weight two on each axis ray, and (7) gives eight: \(2!\) times the slope-square area four. No factorial division, probability normalization, or singular-face Alexandrov substitution is used.

If a continuous real PA function is actual PC, it is PAPC against **all** required cycles. Indeed, refine a local cycle and the function, choose a rational point \(x\) in the ordinary open and relative interior of its tested facet \(\tau\), and first take nonnegative rational balanced incident weights \(c_\sigma\). Put \(S=\sum c_\sigma>0\) and \(T=\sum c_\sigma n_{\sigma/\tau}\in N_{\tau,\mathbb{Q}}\). For small rational \(\varepsilon>0\),
\[
 x_\sigma=x+\varepsilon(n_{\sigma/\tau}-T/S)
\]
lies in its actual incident cell and open: the correction is tangential and the quotient direction is inward. These rational endpoints, with coefficients \(c_\sigma/S\), give an actual PCC centred at \(x\). Jensen gives \(0\leq\varepsilon(\sum c_\sigma h_\sigma(n_{\sigma/\tau})-h_\tau(T))\), precisely (5). The cone of nonnegative balanced incident vectors is a rational polyhedral cone, so has rational generators, as proved below. Linearity extends the result to every real incident vector. The zero vector gives zero. This proves all ordinary-open, all-dimension PAPC tests. Balancing just proved and this positivity allow both recursive divisors.

For all envelopes constructed here, \(P+1/n\) is decreasing uniform PAPC approximation in \(\gamma+O(1)\). Constants have zero divisor; the approximant measures are identical to \(P^2\cdot[X]\). Thus the regularized operator is concretely the already defined PA operator, without an approximation, gluing, locality or continuity theorem imported from the source. The authentic proof bodies of BMPS Lemmas 2.34--2.35, Lemma 3.4, Proposition 3.22 and Proposition 6.3 were inspected as comparison data. Their external locality/intersection dependencies are not used. There are **no essential external theorem premises** in the argument that follows.


The total mass for any constructed \(P\in\gamma+O(1)\) also equals the
raw reference degree, directly. Mixed commutativity (M) gives
\[
 P\cdot(P\cdot[X])-\gamma\cdot(\gamma\cdot[X])
      =(P-\gamma)\cdot((P+\gamma)\cdot[X]).                 \tag{Deg}
\]
The inner divisor is a balanced finite real one-cycle on a common rational
structure. Sum its outer coefficients over all vertices. Every bounded edge
occurs twice with equal inherited weight and opposite primitive outgoing
directions, so its slopes cancel. Every unbounded edge has zero slope for the
bounded affine function \(P-\gamma\). Full lines have no endpoint contribution.
Thus the difference has total degree zero. This is the whole mass identity,
including every actual intermediate edge and end, with no probability
normalization. It is not used to infer contact. The explicit constant-shift
regularization has these same measures at every stage.

## Elementary finite-dimensional facts used in the reconstruction

A polyhedral cone has finitely many generators; for rational inequalities these can be rational. Remove its lineality (a rational subspace for rational data) and work in the pointed quotient. The sum of its nonnegative defining forms is strictly positive away from zero: otherwise all forms vanish on a nonzero vector and its negative. The section of value one is bounded, since an unbounded sequence, normalized to the unit sphere, would yield a nonzero cone vector of value zero. A bounded polyhedron is the convex hull of its vertices: in the minimal face of any nonvertex, a line ends on smaller faces, and induction reduces dimension. Its vertices are the finitely many full-rank active-system solutions, rational for rational data. Lift back and add both signs of a lineality basis. Homogenizing a nonempty pointed rational polyhedron therefore proves
\[
 \sigma=\operatorname{conv}\{v_1,\ldots,v_l\}
                    +\operatorname{cone}\{r_1,\ldots,r_m\},     \tag{8}
\]
with rational vertices and recession vectors and at least one vertex: the height-one slice needs a positive-height extreme ray, whose extremality gives an original vertex. The homogenized cone is pointed because any line has height zero and would give original lineality. The same proof holds over real data without rational coordinates.

Eliminating a variable from finitely many nonstrict linear inequalities compares every lower bound with every upper bound and retains variable-independent conditions. A one-sided family imposes no further conditions. Repetition proves that projections of polyhedra are polyhedra; variable coefficients stay rational if originally rational, even with real constants. It also proves closedness of finite convex-hull-plus-cone sets by projecting their coefficient representation.

Needed separations can be proved by nearest points. A point outside a nonempty closed convex set has a nearest point after restriction to a sufficiently large compact ball. Differentiating squared distance along segments gives a separating normal. A compact convex set disjoint from a closed convex set has positive attained distance, with the same compact restriction for the second set; differentiating in both sets strictly separates them. If the latter is a cone, a finite supremum of the separating functional on it is zero. This proves the cone/polytope separations used here.

If the pointed cone quotient is zero-dimensional, only its zero vector and the lifted lineality basis are needed. The elementary fact about a bounded polyhedron used above also covers its
zero-dimensional case. Pointedness ensures the homogenized cone has no lineality;
its zero-height extreme rays give recession generators and its positive-height
extreme rays give exactly the normalized vertices. This proves (8) without an
unstated decomposition theorem.

A finite rationally convex function on \(\mathbb{Q}\) has a unique continuous convex extension on any interval interior. Rational endpoint values bound it above on a rational compact interval. Reflection about a rational centre bounds it below on a smaller interval. Bounds \(L\leq F\leq M\) on a larger rational interval imply a Lipschitz bound on a smaller one: extend the rational segment from \(y\) through \(z\) by a rational factor \(R/|z-y|\) staying in the larger interval and use Jensen, then reverse \(y,z\). Density gives the completion and convexity. A finite convex function on \(\mathbb{R}\) is continuous by this argument, and has a touching affine support at each point: its left and right secant limits are finite, ordered, and any slope between them gives the support.

For \(b(p)=\min_j(c_j+g_jp)\), the supergradient interval at \(p_0\) is the convex hull of the active \(g_j\). Its directional derivative is the minimum of their products with the direction. Separating a candidate outside that interval disproves its supergradient property. Expanding sums of finite minima proves that supergradients of nonnegative sums are the corresponding weighted Minkowski sums, also when coefficients vanish. The outward normal cone of a polytope is generated by active inequality normals: an alleged normal outside their finitely generated closed cone can be separated to give a direction satisfying the active inequalities and increasing the alleged normal; a sufficiently small step also satisfies inactive inequalities, a contradiction. These proofs retain rational normal generators whenever inequality coefficients are rational, even if constants are real.

## A finite rational cone for actual PC on a fixed complex

This lemma concerns a **fixed** finite embedded rational complex \(\Sigma\).
It does not assert regularity on its carrier. Let \(A(\Sigma)\) be the real
vector space of continuous functions affine on each cell, with real affine
coefficients. Choose rational affine coordinates on each cell's affine span.
Agreement on each common face is a finite rational homogeneous linear system:
test agreement on a rational affine basis of that face. These tests suffice
because the difference is affine. Thus \(A(\Sigma)\) has a rational basis,
including when cells have lineality or are lower dimensional. Clearing slope
denominators in a rational basis element puts it in the literal PA class.
This proves that the declared function space is its real scalar extension.

For every nonempty face \(\tau\), every coface \(\sigma\succeq\tau\), and
\(y\in\operatorname{relint}(\tau)\), define
\[
 T_{\tau\sigma}=\operatorname{cone}(\sigma-y).                 \tag{FC1}
\]
Here cone means nonnegative scalar multiples; this set is already a closed
convex polyhedral cone. To prove this, write \(\sigma\) using rational affine
equalities and inequalities \(a_k(z)+b_k\geq0\). At \(y\), an inequality is
active if and only if it vanishes identically on \(\tau\): a nonnegative affine
function on \(\tau\) cannot vanish at a relative-interior point unless its
restriction is zero, by taking short steps in both tangent directions. A vector
\(d\) is in (FC1) exactly when it satisfies the homogeneous equalities and
\(a_k(d)\geq0\) for all active inequalities. Necessity follows by substitution.
For sufficiency, every inactive inequality has positive slack at \(y\); there
are finitely many, so a sufficiently small positive step \(y+t d\) satisfies
all of them, as well as the active constraints. Therefore \(y+t d\in\sigma\).
This also proves that each such direction stays in \(\sigma\) for every
sufficiently small positive step. The same active constraints hold at every
real point in \(\operatorname{relint}(\tau)\), proving independence of the
chosen centre, rationality, and inclusion of the whole tangent space of
\(\tau\) as lineality. No boundedness, pointedness, or full dimension was used.

Form the cone of vector families, indexed by **all** cofaces including \(\tau\),
\[
 B_\tau=\{(d_\sigma):d_\sigma\in T_{\tau\sigma},\quad
                              \sum_{\sigma\succeq\tau}d_\sigma=0\}.
                                                               \tag{FC2}
\]
It is a rational polyhedral cone and has finitely many rational generators,
with both signs of a rational lineality basis retained. The finite-generation
proof above applies to the product of the tangent cones and the rational
sum-zero equations. Impose, for every generator and every \(\tau\),
\[
                \sum_{\sigma\succeq\tau}h_\sigma^{\rm lin}(d_\sigma)
                                  \geq0.                       \tag{FC3}
\]
These are rational homogeneous linear inequalities in \(A(\Sigma)\).

**Claim.** Their solution cone \(C(\Sigma)\) equals
\(A(\Sigma)\cap\mathrm{PC}(X)\), with actual PC tested against all allowed
rational structures, all real centres, and remote rational endpoints.

For necessity choose a rational \(y\in\operatorname{relint}(\tau)\).
Such a point exists: rational affine coordinates identify the relative
interior with a nonempty open subset cut out by rational constraints, and
rational points are dense in its affine span. Given a rational generator of
\(B_\tau\), let \(m\) be the number of cofaces. A sufficiently small rational
\(t>0\) puts all rational endpoints \(y+mt d_\sigma\) in their cofaces.
Their equal coefficients \(1/m\) give a genuine \(\Sigma\)-PCC centred at
\(y\). Since every piece agrees at \(y\), Jensen is precisely (FC3) after
division by \(t\). The zero family causes no difficulty. Linear combination
extends the inequalities from generators to every real family in \(B_\tau\).

For sufficiency first take any straight segment contained in the carrier,
with endpoints allowed to be real. Each cell intersects it in an interval,
so a finite subdivision makes \(h\) affine on each subinterval. At an interior
breakpoint \(x\in\operatorname{relint}(\tau)\), let \(d\) be the forward
direction. Its incoming \(-d\) and outgoing \(d\) lie in the tangent cones of
their respective initial cells, which contain \(\tau\) as a face. Put them
in the corresponding slots of (FC2). If the slots coincide, sum them in that
slot; both derivatives then come from the same affine piece and agree. In
all cases (FC3) gives
\(h'_+(x;d)-h'_-(x;d)\geq0\). A continuous PA function with nondecreasing
successive slopes is convex: the secant slope over an interval is a weighted
average of its piece slopes, so left secants do not exceed right secants.
Thus \(h\) is convex on every contained straight segment.

Now take any genuine PCC \((x,(x_i),(\alpha_i))\) on **another** permitted
structure. Each segment \([x,x_i]\) lies in its permitted convex coface and
hence in \(X\). If \(d_i=x_i-x\ne0\), its initial short segment lies in some
\(\Sigma\)-cell containing \(x\); finiteness of the segment subdivision
ensures such a cell exists. The minimal \(\Sigma\)-face \(\tau\) of \(x\)
is a face of that cell, and \(d_i\in T_{\tau\sigma_i}\) by (FC1).
Continuity and affine agreement make the initial derivative unambiguous.
Convexity along the segment gives
\(h(x_i)-h(x)\geq h'_{x}(d_i)\). Group
\(D_\sigma=\sum_{i:\sigma_i=\sigma}\alpha_i d_i\).
Each group stays in its convex tangent cone, and
\(\sum D_\sigma=\sum\alpha_i(x_i-x)=0\). Therefore (FC3) gives
\[
 \sum_i\alpha_i(h(x_i)-h(x))\geq
 \sum_\sigma h_\sigma^{\rm lin}(D_\sigma)\geq0.              \tag{FC4}
\]
Zero displacements and zero coefficients contribute zero. This proves the
claim at **every real centre**, with no insertion of irrational endpoints
or cycles into the source definitions.

## Exact positive-growth decomposition of the prescribed real reference

Choose a common finite rational affine structure \(\Sigma\) for the product
and the prescribed real \(\gamma\). Since \(\gamma\) is positive at infinity,
each cell is pointed: nonzero lineality would put both \(r\) and \(-r\) in
its recession cone, requiring opposite affine slopes both positive.
By (8), each recession cone has finitely many nonzero rational generators.
Its positive-growth conditions are exactly the finite strict inequalities
\[
       h_\sigma^{\rm lin}(r)>0\quad
       \text{for all chosen nonzero recession generators}.     \tag{FC5}
\]
A nonzero recession vector is a nonnegative combination with at least one
positive coefficient, so these inequalities suffice as well as being necessary.
Bounded cells impose none.

Write \(C(\Sigma)\) by its finite inequalities \(L_i\geq0\) in the rational
space \(A(\Sigma)\), and let
\(I=\{i:L_i(\gamma)=0\}\), \(S=\bigcap_{i\in I}\ker L_i\).
Then \(F=C(\Sigma)\cap S\) is the minimal face containing \(\gamma\).
Indeed it is a face by nonnegativity of the \(L_i\). In \(S\), all other
inequalities are strictly positive at \(\gamma\), so a small relative ball
about \(\gamma\) lies in \(F\). Hence \(\operatorname{span}F=S\) and
\(\gamma\in\operatorname{relint}F\). Any face containing \(\gamma\)
contains that ball: for \(z\in F\) a short step from \(\gamma\) opposite
\(z-\gamma\) stays in the ball, expressing \(\gamma\) as a strict convex
combination of \(z\) and another point of \(F\); the defining face property
then includes \(z\). This proves minimality without a face theorem.
The subspace \(S\) is rational, even when the cone has lineality.

Choose a rational basis of \(S\), and use it as coordinates. If its dimension
is \(d>0\), choose rational endpoints \(a_k<t_k<b_k\) about the real
coordinates \(t_k\) of \(\gamma\), so close that their entire box lies
in the preceding relative ball and satisfies every strict inequality (FC5).
Density of the rationals and finiteness of all constraints give such a box.
All its \(2^d\) vertices \(\gamma_j\) have rational affine coefficients,
belong to \(C(\Sigma)\), and retain every strict recession slope. Put
\(\theta_k=(t_k-a_k)/(b_k-a_k)\in(0,1)\). The product weights obtained by
choosing \(\theta_k\) at an upper endpoint and \(1-\theta_k\) at a lower
endpoint are strictly positive and sum to one. Their coordinate averages
are exactly \(t_k\). Thus, **as functions on the entire unchanged carrier**,
\[
                 \gamma=\sum_{j=1}^{J}\lambda_j\gamma_j,
                 \lambda_j>0,\qquad\sum_j\lambda_j=1.        \tag{FC6}
\]
Each \(\gamma_j\) is actual PC against every structure by (FC4), not just
feasible in a nodal relaxation. If \(d=0\), then \(\gamma=0\) in this
space; use the single rational reference \(0\) with weight one. In that
case (FC5), if nonempty, would exclude \(0\), so this case can occur only
when there are no nonzero recession directions. This handles the degenerate
case without claiming growth where it is impossible. No approximation,
reference replacement, or lost strict recession inequality occurs in (FC6).


## Intrinsic graph convexity and product projection, without rank assumptions

This section supplies the graph and projection lemmas used in the new
higher-relation case. It does not invoke the existing one-dimensional
classification.

For a continuous finite PA function \(h\) on a finite rational graph structure,
actual PC is equivalent to edgewise convexity and
\[
             c\mathbin{\cdot}s_v(h)\geq0\quad(c\in K_v)       \tag{G1}
\]
at every vertex, including function breakpoints. To prove this equivalence,
use (FC1)--(FC4) on that graph structure. At an edge interior the only
coface tangent cone is its full line, so a tangent family of sum zero has
zero affine derivative sum. At a vertex the one-face tangent cones are the
nonnegative primitive rays; every family is \((t_eq_e)_e\), \(t_e\geq0\),
with \(t\in K_v\), and the zero-face contributes zero. Thus its tests are
exactly (G1). At a bivalent affine breakpoint \(K_v\) is generated by
\((1,1)\), and (G1) says the right derivative is at least the left derivative.
These inequalities imply edgewise convexity by monotone successive slopes.
Conversely all such tests imply (FC3), which proves PC for every real centre,
remote rational endpoint and allowed coface structure. At original vertices
one need not replace the cone \(K_v\) by the single actual weight relation.
All its real members are tested.

For completeness this also proves convexity on any contained straight segment
passing through a higher-rank branching vertex: its incoming and outgoing
opposite primitive directions give a member of \(K_v\), so its successive
slopes cannot decrease. No ambient affine extension of \(s_v(h)\) is asserted.

If \(h_i\) are continuous actual-PC rational-domain PA functions on the two
graphs, then
\[
                  h(x,y)=h_1(x)+h_2(y)                       \tag{G2}
\]
is actual PC on their full product. Here is the precise projection argument,
which does not assume that arbitrary projected cofaces themselves form a
graph structure. Choose fixed rational function structures \(\Sigma_i\).
For a product face \(\tau_1\times\tau_2\) and a product coface
\(\sigma_1\times\sigma_2\), the tangent cone (FC1) is the direct product
\(T_{\tau_1\sigma_1}\times T_{\tau_2\sigma_2}\). Indeed each projected
direction admits a sufficiently small positive feasible step, so both admit
a common small step; the reverse inclusion follows by projection.

For a product tangent family of sum zero, project its vectors and group them
over \(\sigma_1\). The grouped first-factor vectors stay in their convex
tangent cones and sum to zero. Factor PC and (FC3) give a nonnegative
first-factor derivative sum. Grouping over \(\sigma_2\) gives a nonnegative
second-factor sum. Their sum is the product test. Consequently (FC4) proves
(G2) against every genuine product PCC on every other allowed structure.
More explicitly, project the segments of such a PCC, use factor convexity
along each projected segment, and group their initial directions in the fixed
factor tangent cones. The projected barycentre equations give precisely
these sum-zero families. A zero projected displacement has derivative zero;
all projected distances and all real coefficients are retained. This explains
why projection is valid even when a projected distant segment crosses a
vertex. It does not make an unsupported assertion about projected faces.

By the all-ordinary-open PC-to-PAPC proof above, (G2) and every PC function
constructed below are PAPC against every nonnegative real local one- or
two-cycle. Product balancing and the actual saturated primitive-normal
recursion, refinement and locality have already been reconstructed.

Every balanced graph has a strictly positive vector \(w\in K_v\). Hence
\(\operatorname{span}K_v=\ker Q_v\), where \(Q_v\) has columns \(q_e\):
any kernel vector can be added to and subtracted from \(w\) after a sufficiently
small scaling while preserving nonnegativity. This proves the equality and
shows that a rank-one cone is precisely the sole positive kernel relation.
It also shows that higher rank cannot be hidden by irrational actual weights.
Rational bivalent subdivisions have rank one and do not change any original
relation cone or the carrier branching property. These are local geometric
conditions independent of the chosen finite refinement.



## Rank-one supporting graph geometry, real weights, and genuine cofaces

From this point through the two-branch reconstruction, assume all local relation cones in both graphs have rank one. This is a supporting case, not a new hypothesis in the broader theorem. At a vertex the full kernel of the rational direction matrix is one-dimensional. Otherwise perturb its strictly positive actual weight vector by a sufficiently small nonproportional kernel vector; positivity persists, contradicting the rank-one condition. The kernel therefore has a primitive positive integer generator \(\lambda_v\), and the actual incident vector is \(a_v\lambda_v\), \(a_v>0\). At a bivalent vertex the directions are opposite primitive vectors and weights equal. At a branched vertex there is no opposite pair, since that pair would give another nonnegative relation. No one-valent vertex can balance.

On a connected graph all edge weights are a single positive real scalar times positive rational weights. Fix one edge weight. At each adjacent vertex the ratios of incident weights equal ratios of positive integers in \(\lambda_v\); propagate along paths through the finite graph. Existing actual weights ensure consistency around every cycle. This yields rational normalized weights \(r_e\) with \(w_e=c r_e\). Full-line components have one arbitrary positive scalar weight. Rational subdivision preserves these statements. This reduction is essential: it makes the incidence elimination below have rational variable coefficients, without supposing the given real scale rational.

Every connected unbranched component is a complete rational affine line. Propagating through bivalent vertices keeps every edge on the same affine line with equal weight. The component is a connected finite closed union of intervals/rays on that line. Any finite endpoint of its union would be one-valent, contrary to balancing. It therefore covers the whole line; a bounded cycle cannot be embedded into this line as a pure polyhedral graph. A component supplied already as a full line has the same conclusion. Its tangent lattice is the saturated primitive line lattice \(\mathbb{Z}v\), independently of the ambient lattice's complementary directions.

For the all-coface PCC tests on a cylinder \(G\times\mathbb{R}\), any convex cell projects to a convex subset of the graph. A segment cannot pass a branched vertex since it would need an opposite pair there. Thus its graph projection is in a single straight chain through bivalent subdivisions or in a vertex. If the centre's graph coordinate is in a straight-chain interior, all cofaces containing the common face remain in that chain and the graph test is ordinary one-variable convexity. At a branched centre \(v\), each coface projects into one incident straight chain; every endpoint displacement has the form \(t_i v_e\), \(t_i\geq0\), up to the next branched vertex. Grouping the barycentric displacements gives
\[
 b_e=\sum_{i\text{ in }e}\alpha_i t_i,
 \qquad\sum_e b_ev_e=0,\qquad b_e=c r_e,\ c\geq0.           \tag{9}
\]
This argument uses actual cofaces on arbitrary rational structures, not merely a prescribed product subdivision. Distant endpoints and inserted bivalent vertices are included. Zero graph displacements cause no contribution.

## Positive direction: full graph-cylinder reconstruction in dimension two

Suppose both factors have rank-one relation cones and one factor is unbranched. Its components are complete rational affine lines of constant positive real weights. Work first on one connected component \(G\times\mathbb{R}_z\). Use its actual primitive coordinate \(z\), and normalize graph weights to positive rational \(r_e\); the actual product two-cycle is a positive scalar multiple of these normalized weights. This scalar affects neither raw PC nor contact and will be restored in the measure. No hypothesis of separability or ambient convex extension of the data is made.

**Scalar graph lemma.** A finite function on rational graph points satisfying rational-coefficient graph PCCs has a continuous edgewise-convex completion \(k\) with finite outgoing derivatives and
\[
                              \sum_e r_e k'_e(v+)\geq0.        \tag{10}
\]
Complete it on edge interiors by the rational convex fact. The one-sided limit at an endpoint is finite and at most its specified endpoint value: endpoint secants give the upper bound and a fixed interior secant gives a lower bound. For small rational \(t>0\), the points \(v+t v_e\), with rational coefficients \(r_e/\sum r_e\), form an actual vertex PCC. Its inequality and those endpoint upper bounds force every limit to equal \(k(v)\). Each outgoing derivative is bounded above by a finite secant. Dividing the same PCC by \(t\) prevents any derivative from being \(-\infty\), and yields (10).

Conversely, any continuous edgewise-convex \(k\) satisfying (10), plus \(pz\) for any real \(p\), satisfies **every** actual cylinder PCC. On a chain this is convexity (the bivalent inequality joins the derivatives). At a branched centre use (9) and \(k(q_i)-k(v)\geq t_i k'_e(v+)\); summation gives \(c\sum r_e k'_e(v+)\geq0\). Affine \(z\) terms cancel by the barycentre identity. This includes arbitrary real centres/coefficients and every coface structure.

For an arbitrary finite raw cylinder PC function \(h\), define on rational graph points
\[
 k_{h,p}(q)=\inf_{z\in\mathbb{Q}}(h(q,z)-pz).                 \tag{11}
\]
It satisfies rational graph PCCs: choose rational \(z_i\) tending to each endpoint infimum, apply the product PCC with rational coefficients at \((q,\sum\alpha_i z_i)\), subtract its affine term, and take the infimum. A \(-\infty\) endpoint is handled by varying that endpoint alone. If (11) is finite at one rational graph point, it is finite throughout the component. From an edge-interior finite centre any other rational edge point can be a positively weighted endpoint, with the other endpoint on the opposite side. From a finite vertex, an arbitrary rational point \(v+t_ev_e\) on an incident edge is an endpoint in a positive rational vertex PCC: choose positive rational distances on the other edges and coefficients proportional to \(r_e/t_e\). No endpoint of a finite centre's such inequality can be \(-\infty\). Propagation across the connected graph includes every cycle and end. Thus the scalar lemma applies whenever (11) is finite anywhere.

Put \(f=\gamma+u\), \(C=\|u\|_\infty\), and take a common finite rational spatial structure for \(\gamma,f\), refined by edge strips. Split full-line edge components at a rational point if needed. Every cell is pointed: lineality would give opposite nonzero reference recession vectors with opposite affine slopes, both supposedly positive. Define
\[
 D=\{p\in\mathbb{R}:p r_z\leq s_r\text{ for every cell recession generator}
                                      \ r\text{ with }r_G=0\},           \tag{12}
\]
where \(s_r\) is the affine obstacle slope. Bounded \(u\) has zero recession slope, so these are the same constraints for \(\gamma\). They are finite, have rational variable coefficients and real constants, and give a closed interval with zero in its interior by strict growth. For \(p\in D\),
\[
                         F_p(q)=\inf_{z\in\mathbb{R}}(f(q,z)-pz)          \tag{13}
\]
is finite and attained at a vertex of some spatial cell fibre. The fibre is pointed. Its recession cone is generated by zero-graph cell rays: on a bounded strip all graph recession is zero; on an end strip it is nonnegative, so positive graph rays cannot combine to yield zero graph recession. The objective is nonnegative on the fibre recession cone, so (8) supplies a minimizing vertex. There are finitely many cells. If \(p\notin D\), a violating rational ray based at a rational cell point gives \(F_p(q)=-\infty\) at a rational graph point. The interval \(D\) is bounded: at any fixed rational graph point, finitely many pieces give \(f(q,z)\leq M|z|+B\); if \(|p|>M\), (13) is \(-\infty\). Therefore \(D\) is compact.

Subdivide graph edges at the projections of all spatial vertices. These projections are rational and finite. Between consecutive projections, a fibre vertex lies on a spatial one-face: intersection with the slicing hyperplane lowers its minimal-face dimension by at most one, so a fibre vertex's minimal face has dimension at most one. Such a traversing face has rational trace \(z(t)=z_i+t b_i\); its affine obstacle height has real coefficients. Its feasibility throughout that interval is constant, since changes occur only at projected face vertices. Consequently
\[
 F_p(t)=\min_i(A_i(p)+tB_i(p)),                              \tag{14}
\]
with finitely many indices independent of \(p\), and affine \(A_i,B_i\) with rational \(p\)-gradients and real constants. At a graph node, direct fibre slicing gives the same kind of finite affine minimum. Formula (14) extends continuously and concavely to the finite endpoints: finite candidate limits have objectives at least \(F_p(v)\); conversely, fixing any finite \(z\) and using continuity of \(f\) gives \(\limsup F_p(t)\leq f(v,z)-pz\), then take its infimum. Thus changes of endpoint fibre type are retained.

After the last projected vertex on an end, take its primitive parameter \(t\geq0\) from that node. Define
\[
 \theta_e(p)=\min_iB_i(p)=\lim_{t\to\infty}F_p(t)/t.          \tag{15}
\]
Every \(B_i-\theta_e\geq0\), so \(F_p(t)-t\theta_e\) is nondecreasing. Hence the line with slope \(\theta_e\) starting below \(F_p(0)\) lies below the entire tail obstacle. All tails and pure/mixed recession constraints are included.

For fixed \(p\in D\), on the finite graph node set \(V\) impose the incidence system
\[
 a_v\leq F_p(v),\qquad
 L_v(a,p)=\sum_{e=vw\text{ bounded}}\frac{r_e}{\ell_e}(a_w-a_v)
              +\sum_{e\text{ tail at }v}r_e\theta_e(p)\geq0.             \tag{16}
\]
The actual primitive lengths \(\ell_e\) are positive rational numbers. Every bounded cycle edge appears in this system; no graph is unfolded.

It is feasible. The global competitor \(\gamma-C\leq f\) is actual PC. Its partial infimum is finite on \(D\) by (12)--(13), and the scalar lemma applies. Replace it on every bounded interval by its endpoint chord and on every tail by its endpoint line of slope \(\theta_e\). Convexity makes these replacements dominate it. Concavity of (14) keeps the chords below \(F_p\); (15) keeps the tail lines below it. At both endpoints the new outgoing chord derivative is at least the old derivative. Convexity and the tail asymptotic upper bound force all old tail secants to be at most \(\theta_e\), so its outgoing derivative also increases. This proves (16).

Coordinatewise maxima preserve feasibility: at a node chosen from one vector all neighbour values only increase, so its \(L_v\) does not decrease. Choose a feasible witness \(b\); maximize \(\sum a_v\) in the compact box \(b_v\leq a_v\leq F_p(v)\). If any feasible vector exceeds a maximizing vector in one coordinate, their coordinatewise maximum is feasible in that box and increases the objective. There is therefore a greatest feasible vector \(a(p)\). Its chord/tail interpolation \(k_p(q)\) is continuous, obeys (10), lies below \(F_p\), and dominates every scalar function (11) lying below \(F_p\), by the same chord/tail replacements.

Each \(a_v\) is a finite concave PA function on \(D\) with rational gradients. Expand all caps into their affine minima and each weighted sum of tail minima into a minimum over all choices of pieces. This turns (16) into finitely many linear inequalities in \((a,p)\) with rational variable coefficients and real constants. Eliminate all \(a_w\), \(w\ne v\), by the proved elimination procedure. For fixed \(p\), the section is \((-\infty,a_v(p)]\), since uniformly lowering all node values preserves the Laplacians. Thus all nontrivial bounds on \(a_v\) are upper bounds; zero-coefficient inequalities only restrict \(D\). Dividing positive rational coefficients yields
\[
                       a_v(p)=\min_j(c_{v,j}+g_{v,j}p),\quad
                       g_{v,j}\in\mathbb{Q}.                 \tag{17}
\]
This proves continuity through the boundary of \(D\), as well as rational gradients. The same holds for \(\theta_e\).

Set
\[
                            Q(q,z)=\sup_{p\in D}(k_p(q)+pz).             \tag{18}
\]
It is finite by compactness and continuity and actual PC by the scalar lemma and the supremum Jensen inequality. It is at most \(f\). For any raw \(h\leq f\) at rational \((q,z)\), the rational slice \(h(q,\cdot)\) has the continuous convex completion proved above. A touching affine support of slope \(p\) gives \(h(q,z)=k_{h,p}(q)+pz\). The partial infimum is finite there, hence throughout the component by propagation. A violating recession ray would contradict \(h\leq f\), so \(p\in D\). Greatest-assignment domination gives \(h(q,z)\leq Q(q,z)\).

Partition \(D\) at the finitely many breakpoints of (17) and (15); let \(J\) be the finite set of chamber endpoints. They may be real. On any graph interval, \(k_p(q)+pz\) is affine in \(p\) on each chamber; therefore (18) is the maximum over \(p\in J\) of finitely many real affine strip functions. These agree at graph nodes. Hence \(Q\) is continuous. At any real carrier point choose its minimal face on a rational structure; unless it is a rational zero-face, rational vertices of arbitrarily small enclosing simplices in that face have the point as a real barycentre. The same-cell PCC and continuity of \(Q\) extend \(h\leq Q\) to that point, without raw continuity. Applying this to \(h=\gamma-C\) gives
\[
                         \gamma-C\leq Q\leq f\leq\gamma+C.              \tag{19}
\]
Thus \(Q\) itself is a raw competitor and bounds all competitors, proving \(P_\gamma(u)=Q\) exactly.

**Rational spatial domains.** A finite real affine maximum alone does not justify rational walls. Fix \(p_0\in J\). Let \(A_v\) be the supergradient interval of \(a_v\) at \(p_0\), \(B_e\) that of \(\theta_e\), and \(N_D\) the outward normal cone of \(D\) there. Endpoints of \(A_v,B_e\) are rational by (17), and \(N_D\) has rational generators by (12). For finite concave polyhedral \(b\), \(p_0\) maximizes \(b(p)+pz\) on \(D\) exactly when
\[
                                z\in-\partial^+b(p_0)+N_D.             \tag{20}
\]
Sufficiency is the supergradient/normal inequality. If necessity failed, separating the compact interval \(z+\partial^+b\) from the closed cone \(N_D\) gives a direction nonpositive on all active normals and strictly positive on every objective directional term. A small feasible step raises the objective, a contradiction. This proves the boundary cases too.

On a bounded edge \(0\leq t\leq\ell\), its full maximization domain is
\[
 z\in-(1-t/\ell)A_v-(t/\ell)A_w+N_D.                       \tag{21}
\]
It is the convex hull of rational points \((0,-\operatorname{Vert}A_v)\), \((\ell,-\operatorname{Vert}A_w)\), plus the cone of rational vertical normal generators. On a tail the domain is
\[
 t\geq0,\qquad z\in-A_v-tB_e+N_D,                         \tag{22}
\]
generated by rational base points and rational rays \((1,-\operatorname{Vert}B_e)\) and vertical normal rays. Expanding the finite weighted minima proves these supergradient formulas even at zero coefficients. The domains are finite rational spatial polyhedra. Maxima domains meet in equality faces; including their faces and removing duplicates gives a rational complex. At a graph node every incident formula has the same fibre domain \(-A_v+N_D\), so complexes glue. Generated bounded-strip domains have vertices only at graph endpoints, and tail domains only at their base. Thus **every** possible zero-cycle vertex lies over a node of \(V\); there are no omitted open-edge or distant-tail vertices.

By the PC-to-PAPC argument following (7), \(P\) is PAPC against all local real cycles. The full recursive measure is finite and nonnegative. The sequence \(P+1/n\) proves actual regularizability with exactly this measure.

**Complete contact.** At any possible atom \(x=(v,z_0)\), suppose \(P(x)<f(x)\). Define the nonempty compact exposed interval
\[
 C_x=\{p\in D:a_v(p)+pz_0=P(v,z_0)\}.                      \tag{23}
\]
It is convex because \(a_v\) is concave and the displayed expression never exceeds its maximum. On \(C_x\), \(a_v=P(x)-pz_0\) is affine. Put
\[
 s_e(p)=(a_w(p)-a_v(p))/\ell_e\quad\text{on bounded outgoing edges},
 \qquad s_e(p)=\theta_e(p)\quad\text{on tails}.              \tag{24}
\]
These are continuous concave polyhedral functions on \(C_x\), and \(\sum r_es_e\geq0\). In local outgoing coordinates \(t\geq0\), \(\zeta=z-z_0\), the homogeneous germ is
\[
                            h_e(t,\zeta)=\max_{p\in C_x}(p\zeta+ts_e(p)).\tag{25}
\]
Indeed the finite set \(J\) expresses all strip functions. Inactive planes at \(x\) have positive gaps and stay inactive locally. Every \(p\in C_x\) is a convex combination of endpoints of a chamber on which all terms are affine; equality at the maximum forces its relevant endpoints to be active. This proves the exact germ identity.

If \(C_x\) is a single point \(p_0\), after subtracting \(p_0\zeta\) the germ is independent of \(\zeta\) on every branch. Its first divisor is a constant-weight vertical line over the graph vertex (all interior branch planes are affine); the function restricts to an affine function on that line. Formula (5) gives zero second coefficient, or equivalently its two opposite primitive vertical rays in (7) cancel. This retains artificial cuts and all first faces by refinement compatibility.

If \(C_x\) is a nondegenerate interval, for every interior \(p\) choose \(\eta>0\) with \([p-\eta,p+\eta]\subset C_x\). Globally in the vertex fibre,
\[
 P(v,y)-py\geq P(v,z_0)-pz_0+\eta|y-z_0|.                 \tag{26}
\]
Thus continuous \(f(v,y)-py\) is coercive and attains its minimum. If \(a_v(p)=F_p(v)\), (26) forces its minimizing point to be \(z_0\) and equality \(f(x)=P(x)\), a contradiction. Hence \(a_v(p)<F_p(v)\) throughout the interval interior. Greatest-assignment maximality forces \(L_v(a(p),p)=0\): if positive, increase only \(a_v\) by a small amount preserving its strict cap and that Laplacian. Every neighbour Laplacian increases, tails are unchanged, and feasibility persists, contradicting maximality. If there are no bounded incident edges, such an increase changes no Laplacian and already contradicts the strict cap. Continuity now gives \(\sum r_es_e=0\) on all of \(C_x\).

Positive weights and concavity force every \(s_e\) affine on this interval: their nonnegative Jensen deficits have weighted sum zero. Its affine gradient is rational, because an interior subinterval avoids the finitely many walls of (17) and (15), whose gradients and primitive lengths are rational. Write \(s_e(p)=\alpha_e+\beta_ep\), \(\beta_e\in\mathbb{Q}\), \(\alpha_e\in\mathbb{R}\). The zero sum gives \(\sum r_e\alpha_e=\sum r_e\beta_e=0\). Since the star direction kernel is exactly this one relation, there exist a real linear form \(A\) and a rational linear form \(B\) on its actual rational span, with \(A(v_e)=\alpha_e\), \(B(v_e)=\beta_e\). This follows by factoring the prescribed values through the rational direction matrix, not by substituting a ray-generated lattice.

The full star germ is therefore
\[
                              A(s)+\operatorname{supp}_{C_x}(\zeta+B(s)).\tag{27}
\]
Extend these forms to the ambient space, rationally for \(B\). After removing \(A\) and an affine multiple of the rational form \(\ell=\zeta+B(s)\), the residual is a one-variable convex homogeneous function, affine on \(\ell\geq0\) and \(\ell\leq0\), and zero on \(\ell=0\). Refine the actual fan by this rational hyperplane. Its first divisor vanishes away from \(\ell=0\), since the residual is ambient affine there. On the entire support of the first divisor the residual is zero, so its second divisor is zero by (5). This is the complete recursion, including singular axes and all indices; it is not a top-face-interior comparison. Consequently every noncontact atom has coefficient zero. Finite support and bounded gap (19) prove (2).

For finitely many components construct the data, envelopes and measures separately. A PCC's cells all contain its common face, so lie in one connected component; a local cycle can similarly be treated componentwise. Components are disjoint finite closed polyhedral subsets and are open relative to their union. The finite component constructions give a finite rational structure, a maximum of their finitely many growth constants, and measures whose contact integrals add. Restore the actual positive real product scalar on each component; zero stays zero. This finishes the positive direction for all stipulated data. This proof was
reconstructed here in full; its predecessor's accepted review is not invoked.

## Auxiliary rational-reference localization: whole-space growth

In this auxiliary construction only, write \(\eta\) for any rational-coefficient positive-growth actual-PC reference. Its elementary construction will be applied separately to every component \(\gamma_j\) of (FC6); it is not a replacement of the prescribed real reference.

The following whole-space growth estimate applies to every product, with no rank condition. Choose any rational centre \(A,B\); in the rank-one two-branch construction these will be original branched vertices.
All objects in this construction remain on the **entire original product**.
Choose ambient lattice bases and put
\[
\rho(p,q)=\|p-A\|_1+\|q-B\|_1,\qquad
\rho_0(r)=\|r_1\|_1+\|r_2\|_1.                               \tag{28}
\]
The second is the **homogeneous recession norm**, not the translated function
\(\rho\). Refine the original product and \(\eta\) into a common finite
rational structure \(\Sigma\), splitting any full-line carrier pieces if needed.
Each nonempty cell is pointed. Indeed a lineality vector \(r\ne0\) and \(-r\)
would both be recession vectors of an affine reference cell, and its affine
slopes on them are opposite; they cannot both be strictly positive. Any subcell
inherits positive slopes on its nonzero recession vectors.

By (8), write every cell as the convex hull of finitely many rational vertices
\(v_i\) plus the cone of finitely many nonzero rational recession generators
\(r_j\). Its affine slope \(\eta_\sigma^{\mathrm{lin}}(r_j)\) is a positive
rational number. Select one rational \(m>0\) no larger than any of the finitely
many ratios
\[
       \eta_\sigma^{\mathrm{lin}}(r_j)/\rho_0(r_j).            \tag{29}
\]
If there are no recession generators, choose any rational \(m>0\). For
\(x=\sum_i\beta_iv_i+\sum_jt_jr_j\), \(\beta_i,t_j\geq0\),
\(\sum_i\beta_i=1\), affinity and the norm triangle inequality give
\[
\begin{split}
\eta(x)&\geq\min_i\eta(v_i)+m\sum_jt_j\rho_0(r_j),\\
\rho(x)&\leq\max_i\rho(v_i)+\sum_jt_j\rho_0(r_j).
\end{split}                                                        \tag{30}
\]
Choose rational
\[
B=\max\bigl(0,\ \max_{\sigma\in\Sigma}
                 [m\max_{v\in\operatorname{Vert}\sigma}\rho(v)
                        -\min_{v\in\operatorname{Vert}\sigma}\eta(v)]\bigr).
\]
The finite vertex sets are nonempty, and all values in this expression are
rational. Equations (30) prove on **all** components, bounded cells and ends that
\[
                         \eta\geq m\rho-B.                 \tag{31}
\]
This derives the needed coercivity from the exact recession hypothesis, rather
than assuming a global growth theorem or using a conveniently chosen reference.

## Supporting rank-one two-branch obstruction: maps on the original stars

For this supporting construction assume both graphs have rank-one cones and choose branched vertices \(A,B\). By the graph kernel proof, the primitive directions at \(A,B\) have sole
primitive positive integer relations \(\lambda_i,\mu_j\), and actual incident
weights \(a\lambda_i,b\mu_j\), \(a,b>0\). Partition each incident index set into
three nonempty groups \(I_k,J_k\), \(k=1,2,3\). Set
\[
 S_k=\sum_{i\in I_k}\lambda_i,\quad T_k=\sum_{j\in J_k}\mu_j,
 \quad\nu_1=(1,0),\ \nu_2=(0,1),\ \nu_3=(-1,-1),\quad c_k=1,1,2.
\]
Prescribe on the original directions
\[
L_1(v_i)=\nu_k/S_k\quad(i\in I_k),\qquad
L_2(w_j)=\nu_k/T_k\quad(j\in J_k).                            \tag{32}
\]
Their weighted sums are \(\sum_k\nu_k=0\). Since the **entire** rational direction
kernel is the single relation, these assignments annihilate it, factor through
the actual rational spans, and extend to rational ambient linear maps by rational
basis extension. This is linear algebra on the original spans, not a lattice or
cycle substitution.

Define the global ambient convex rational-PA function
\[
             H(p,q)=\|L_1(p-A)-L_2(q-B)\|_1.                 \tag{33}
\]
For a matrix \(T\), the triangle inequality proves
\(\|Tx\|_1\leq(\max_j\sum_i|T_{ij}|)\|x\|_1\).
Choose positive rational \(L\) at least the two indicated matrix norms; then
\(H\leq L\rho\). Select rational \(0<\varepsilon<m/L\), and rational
\(C>\max\{0,\eta(A,B)+2\}\). Put
\[
                  P=\max\{\eta,\varepsilon H+C\}.          \tag{34}
\]
Ambient affine functions have equality in every admitted PCC, and their finite
maximum gives Jensen; thus \(H\) is actual PC. A maximum of two PC functions is
PC: at any centre select an active function, apply its Jensen inequality, and
bound each endpoint value by the maximum. Hence \(P\) satisfies **every genuine
PCC**, not just coarse product or nodal tests. Both functions in (34) have rational
affine coefficients. On a common rational structure their comparisons are
rational affine inequalities. Subdividing by these inequalities and the finitely
many rational affine-piece walls, then including faces, gives a finite rational
structure \(\Pi\) on which \(P,\eta,H\) are affine. The same observation proves
all rational-domain assertions below. The same assertion about comparisons would fail for arbitrary real coefficients; (FC6) and the positive sum below avoid that assertion.

By (31),
\[
 \eta-(\varepsilon H+C)\geq(m-\varepsilon L)\rho-B-C.
\]
Take a rational \(R>(B+C)/(m-\varepsilon L)\). Then \(P=\eta\) on \(\rho>R\).
Consequently \(P-\eta\geq0\) is bounded and compactly supported in the
closed finite polyhedral carrier intersected with \(\rho\leq R\), a compact
Euclidean set. It follows that \(P\in\eta+O(1)\). On every common affine
cell and recession vector, the affine difference \(P-\eta\) has slope zero,
since it is globally bounded; therefore \(P\) retains positive slopes at infinity.
Its cells are pointed by the same opposite-vector argument. The PC-to-PAPC and
two-stage reconstruction above show that \(P\) is actual
\(\mathrm{PAPC}_{\mathbb{R}}\), with finite nonnegative PA operator, and
\(P+1/n\) is decreasing uniform PAPC regularization in the fixed
\(\eta+O(1)\) class, with exactly the same measures. This proves the operator
domain without an unavailable approximation theorem.

## Positive sums of rational localizations

We now apply the auxiliary construction (28)--(34) to **each** rational
reference \(\eta=\gamma_j\) in (FC6), using the **same** selected original
branched junctions \(A,B\), groups and rational maps defining \(H\).
For each \(j\), choose its rational \(m_j,B_j,\varepsilon_j,C_j\) as in
(29)--(34), and obtain
\[
 P_j=\max\{\gamma_j,\varepsilon_j H+C_j\},\quad
 P=\sum_j\lambda_jP_j,\quad
 C=\sum_j\lambda_jC_j,\quad
 \varepsilon=\sum_j\lambda_j\varepsilon_j>0.                \tag{RS1}
\]
Each \(P_j\) is actual PC and rational PA on a finite rational structure,
dominates \(\gamma_j\), and equals \(\gamma_j\) off a compact set.
Positive sums preserve every Jensen inequality. Taking a common rational
refinement of the finitely many \(P_j\) structures, the **sum** \(P\) is
continuous real PA on finite rational domains and actual PC. We never
take \(\max\{\gamma,\varepsilon H+C\}\), nor infer rational walls from
the coefficients of a real maximum. Equations (FC6) and (RS1) prove
\(P\geq\gamma\), \(P=\gamma\) outside the finite union of those compact
sets, and \(P\in\gamma+O(1)\). On a common affine cell, boundedness of
\(P-\gamma\) makes its slope zero on every recession vector, so \(P\)
retains the prescribed strictly positive recession slopes. Its cells are
pointed. The all-local-cycle PC-to-PAPC proof and explicit \(P+1/n\)
regularization apply without any arithmetic restriction on \(\lambda_j\).

## A common original product junction and the compact obstacle

For every \(j\), the choice \(C_j>\gamma_j(o)+2\), \(o=(A,B)\), and
continuity give \(\gamma_j-C_j<0\) near \(o\). In that neighbourhood
\(P_j=C_j+\varepsilon_jH\), hence \(P=C+\varepsilon H\).
Choose the common rational structure \(\Pi\) by cutting the original
product with a finite global collection of rational affine hyperplanes
extending the fixed spatial domains of all \(\gamma_j\), the \(H\) walls,
and their rational comparison walls. This procedure refines each function
structure: cut by all supporting hyperplanes of its cell boundaries; a
new open cell cannot cross any such boundary, so is contained in an old
cell. Intersections and faces remain finite and rational. It introduces
no wall depending on the real \(\lambda_j\).

Keep \(o\) as a vertex of the original product. Choose rational \(r_0>0\)
small enough for all \(j\) inequalities above, for the carrier inside
\(\rho<r_0\) to be its original short product star, and to avoid all
hyperplanes not passing through \(o\), all nonincident cells and all
incident bounded endpoints. These finitely many closed sets not containing
\(o\) have positive distances from it; take the minimum with the finitely
many continuity radii. Within this ball every active spatial constraint
is homogeneous about \(o\). At any \(x\ne o\), small expansion and
contraction along the radial line stay in its minimal face: homogeneous
equalities remain equalities and the remaining strict inequalities stay
strict. Thus \(x\) is not a vertex, and
\[
 P=C+\varepsilon H\quad(\rho<r_0),\qquad
                  \Pi^{(0)}\cap\{\rho<r_0\}=\{o\}.           \tag{35}
\]
The ball is always intersected with the original carrier. This argument
does not equate an ambient ball with a product star.

Choose a sufficiently small rational \(\tau>0\) so that
\[
 z_{ij}=(A+\tau S_kv_i,\ B+\tau T_kw_j),\qquad
 \alpha_{ij}=\frac{\lambda_i\mu_j}{3S_kT_k},
 \quad i\in I_k,\ j\in J_k                                  \tag{36}
\]
lie in their original product cofaces, before bounded endpoints, and in
\(\rho<r_0\). In (36), \(\lambda_i,\mu_j\) are the **integer star
relations**, distinct from the real convex-decomposition weights in (RS1).
Each group has total coefficient \(1/3\); the sum is one. The first
weighted displacement is \(\tau\sum_i\lambda_iv_i/3=0\), and the second
is \(\tau\sum_j\mu_jw_j/3=0\). Thus this is a genuine original-product
PCC with common face \(o\). Both maps at an endpoint give \(\tau\nu_k\),
so \(H(z_{ij})=0\) and \(P(z_{ij})=C=P(o)\). The rational endpoints
need not be in a common fine \(P\)-coface, since raw PC also tests the
original rational structure.

Choose integer \(M\) with \(1/M<r_0\) and
\(M\rho(z_{ij})\geq1\) at every nonzero endpoint. Put
\[
             b_0=(1-M\rho)_+,\qquad u=P-\gamma+b_0.           \tag{37}
\]
The norm has rational spatial walls and rational coefficients, and cutting
by \(\rho=1/M\) on its finitely many pieces remains rational. Therefore
\(u\) is nonnegative, bounded, continuous real PA on a finite rational
structure, with compact support. Its ceiling for the **unchanged original
real reference** is \(\gamma+u=P+b_0\). The bump is one at \(o\), zero
at every endpoint (36), and zero at every other \(\Pi\)-vertex. The
reference and potential agree at infinity on every component.


## Exact raw envelope on all components, cycles and ends

For any raw competitor \(q\leq\gamma+u=P+b_0\), the endpoint values in (36)
are at most \(C\). Their genuine PCC gives \(q(o)\leq C=P(o)\). At every other
vertex of \(\Pi\), the bump is zero, giving \(q(v)\leq P(v)\).
The **sole upper growth** condition is
\(q\leq\gamma+C_q\leq P+C_q\). No continuity, lower bound, local gluing or
graph unfolding is imposed on \(q\).

Let \(x\) be an arbitrary real point of any \(\Pi\)-cell \(\sigma\). Use its
rational vertex/recession representation (8),
\[
 x=\sum_i\beta_iv_i+\sum_jt_jr_j,\qquad
 \beta_i,t_j\geq0,\quad\sum_i\beta_i=1.
\]
Select \(i_0\) with \(\beta_{i_0}>0\), set \(T=\sum_jt_j\), and take integers
\(K\to\infty\) with \(T/K\leq\beta_{i_0}\). Replace \(T/K\) of that vertex
coefficient by coefficients \(t_j/K\) on the rational endpoints
\(v_{i_0}+Kr_j\in\sigma\). This is a same-cell PCC with centre **exactly**
\(x\), with permitted real coefficients. Affinity of \(P\) on \(\sigma\),
the vertex bounds and the upper growth bound at the far endpoints give
\[
             q(x)\leq P(x)+(T/K)\max\{C_q,0\}.               \tag{38}
\]
For \(T=0\) the ordinary vertex PCC already suffices. In general let
\(K\to\infty\) to get \(q(x)\leq P(x)\). This treats every bounded edge,
cycle, unbounded end and other component, with actual allowed cofaces and
all real centres. Conversely \(P\) is an actual PC global competitor below
\(P+b_0\), and \(P\leq\gamma+O(1)\). Therefore
\[
                             P_\gamma(u)=P\quad\hbox{on all }X.       \tag{39}
\]
This is the raw envelope equality, not an envelope for a replacement reference.

## Complete primitive-normal junction computation

In the original product quadrant \((s v_i,t w_j)\), \(s,t\geq0\), put \(q_i=1/S_k\) if \(i\in I_k\), \(p_j=1/T_l\) if \(j\in J_l\). Directly from the three specified tripod directions,
\[
 H=c_kq_i s+c_lp_j t\quad(k\ne l),\qquad
 H=c_k|q_i s-p_jt|\quad(k=l).                              \tag{40}
\]
Let \(a_i=(v_i,0)\), \(b_j=(0,w_j)\). The actual saturated plane lattice is \(\mathbb{Z}a_i\oplus\mathbb{Z}b_j\): a vector in this plane belongs to the direct product ambient lattice exactly when its two primitive factor-line coefficients are integral. Factor star spans may be nonsaturated in their ray generators; this does not alter these actual plane lattices.

Off-group quadrants are affine and have index-one axis cones. For a same-group pair take a positive integer denominator \(D\), \(Q=Dq_i\), \(P=Dp_j\), \(g=\gcd(Q,P)\). Its zero kink ray has actual primitive vector
\[
                            d_{ij}=(P/g)a_i+(Q/g)b_j.        \tag{41}
\]
The integer coefficients are coprime; primitiveness follows also in the whole ambient lattice because both factor vectors are primitive. The two actual saturated cone indices are
\[
                    \chi_{a_i,d_{ij}}=Q/g,\qquad
                    \chi_{b_j,d_{ij}}=P/g.                 \tag{42}
\]
All top cone weights are \(\Omega_{ij}=ab\lambda_i\mu_j\), inherited from the original graph product. At a kink, (6) and \(H(d_{ij})=0\) give the full first weight
\[
 D_H(d_{ij})=\Omega_{ij}\left(\frac gQ c_kq_i+\frac gP c_kp_j\right)
                             =2c_k\Omega_{ij}g/D.           \tag{43}
\]
No denominator or index has been suppressed.

At an axis \(a_i\), the off-group neighbours are \(b_j\). For same-group neighbours the representative quotient normal is
\(d_{ij}/(Q/g)=b_j+(p_j/q_i)a_i\). Therefore top balancing gives
\[
 \sum\frac{\Omega_{ij}}{\chi}r_{ij}
       =ab\lambda_i\left(\sum_j\mu_jb_j+
                    \sum_{j\in J_k}\mu_j(p_j/q_i)a_i\right)
       =ab\lambda_i S_k a_i.                               \tag{44}
\]
Since \(H(a_i)=c_k/S_k\), the off-group first term is
\(ab\lambda_i(4-c_k)\), and the tangential correction in (5)--(6), with (44), subtracts \(ab\lambda_i c_k\). Thus
\[
 D_H(a_i)=ab\lambda_i(4-2c_k),\qquad
 D_H(b_j)=ab\mu_j(4-2c_l).                                 \tag{45}
\]
These axis rays and the kink rays (41) are all rays in the local function fan and all are nonnegative. Its balancing can be checked directly: kink contributions in the first projection for a fixed \(i\in I_k\) sum to \(2c_kab\lambda_i v_i\), adding its axis contribution gives \(4ab\lambda_i v_i\). The second projection similarly gives \(4ab\mu_jw_j\). Both total sums vanish by the original relations. This check retains every same-group pair even when multiple original rays share a projected direction.

Apply the second divisor (7). Kink rays have zero value. The entire first-axis contribution is
\[
 ab\sum_k(4-2c_k)c_k\sum_{i\in I_k}\lambda_i/S_k=4ab,
\]
and the second-axis contribution is \(4ab\). Hence the **complete** coefficient at the chosen junction is
\[
                          (H^2\cdot[X])\{(A,B)\}=8ab.              \tag{46}
\]
This is the two-stage computation at the original singular product junction, not a pushed-forward tripod calculation or a one apparent atom claim.


By (35) the local germ of \(P-P(o)\) is \(\varepsilon H\). Constants have
zero divisor, and both stages of (5) are real linear in the function, so the
complete original-junction coefficient for \(P\) is
\[
                    \mathrm{MA}_{\mathrm{poly},\mathbb{R}}(P)\{o\}
                                  =8\varepsilon^2ab.          \tag{47}
\]
Other homogeneous cuts introduced by \(\gamma\) or the carrier/refinement
do not change this coefficient, by the proved two-stage refinement compatibility.
The calculation uses no pushforward to a tripod, no missing-axis convention and
no singular-face Alexandrov substitution.

## Complete contact failure in the supporting rank-one two-branch case

The complete PA measure is a finite nonnegative zero-cycle on \(\Pi^{(0)}\).
The exact gap from (37) and (39) is \(P-\gamma-u=-b_0\). It is \(-1\) at
\(o\) and zero at every other \(\Pi\)-vertex, giving the full integral
\[
 \int_X(P_\gamma(u)-\gamma-u)
       \mathrm{MA}_{\mathrm{poly},\mathbb R}(P_\gamma(u))
                         =-8\varepsilon^2ab<0.              \tag{48}
\]
Refining for the obstacle can introduce vertices with nonzero bump, but
successive refinement compatibility gives them zero second coefficient.
All singular lower faces, axes, kinks, remote vertices, bounded cycles,
ends and disconnected components are included. The PA operator is this
finite zero-cycle on \(X\), with no point at infinity. The explicit
regularization \(P+1/n\) has identical measures and adds no boundary term.
This reconstruction proves the supporting negative case without granting
a predecessor result. In the broader theorem its coefficient
\(\varepsilon\) is denoted \(\kappa\) to distinguish it from the cap
slope parameter used next.

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


## Author audit, source boundaries and reproducibility

The fallible higher-relation proposal was read in full and reconstructed.
Its expected coefficient four is confirmed by (HR17)--(HR19), retaining
both intermediate contributions. Its real-centre pinning requires a repair:
endpoints with an irrational second coordinate are not permitted. Equations
(HR13)--(HR15) first pin at rational coordinates; rational same-face enclosing
boxes then prove the bound at every real centre without raw continuity.
The cap is proved intrinsic PC via (G1) and the finite cone, and product
projection is proved through grouped tangent families in (G2). No ambient
extension of intrinsic cap slopes or assertion that projected cells form
a permitted factor structure is used.

The earlier complete argument and canonical campaign.result.notes were
read; the accepted rendering was compared to its full generated rendering.
Their mathematical proof bodies are unchanged by the recorded editorial
differences, and all invoked lemmas are reproduced and checked here.
The author audit checks finite rational domains, real weights, all ordinary
cycles, actual saturated primitive normals, every raw competitor, compact
localization of every prescribed real reference, and the complete integral.
The one-dimensional accessible-mass dossier is read as an existing theorem
to avoid recasting it as new; its entire statement and proof are included
below as comparison evidence and are not premises. Appendix M was checked
for scope: its continuous zero-current frontier concerns P06.2 and supplies
no graph-product result. No P06.2 claim is made here.

There are no essential external theorem premises: all used supporting
mathematics is proved directly above. BMPS v1 supplies the exact definitions
and displayed recursive operator; statements with external premises appear
below only as source comparison data. Its literal integral-slope/rational-
constant function convention and rational weights are explicitly replaced
by the declared real scalar extension, without altering rational spatial
domains or the actual saturated lattices. The coefficient convention is fixed
throughout; no literal regularity conclusion is inferred.

The authoritative `P05.2-argument.md` includes every load-bearing proof and
the exact essential source definition bodies. It is assembled by
`compose_argument.py` from fresh evidence snapshots and the new proof
fragments. `P05.2-partial.tex` is a standalone rendering and
`P05.2-partial.pdf` is compiled twice. `status.json` has exactly five keys:
id, status, exact_result, proof_file, concrete_gaps. The status is partial,
proof_file is P05.2-argument.md, and candidate is false, because original
arbitrary-balanced-space P05.2 remains open.

The exact finite diagnostics in `higher-relation-diagnostic.py` use the
inputs in `higher-relation-input.json` and retain all axis weights, quotient
normals, saturated index-one plane bases, first-cycle balancing, both second
contributions, rational cap bends and supported PCCs. They include a cross
star, a nonsaturated whole-star ray span, and an exact irrational-weight
input over Q(sqrt(2)). Their scope is those finite specified germs, not a
universal proof or an envelope enumeration. The earlier two-branch and
real-sum diagnostics are also rerun in this fresh directory as supporting
finite checks, with their exact original inputs.

Rerun in this directory: `python3 snapshot_sources.py`;
`python3 compose_argument.py`; `python3 higher-relation-diagnostic.py`;
`python3 local-recursion.py`; `python3 real-sum-diagnostic.py`;
`python3 build.py`; `python3 final_checks.py`.
Programs, inputs, outputs, environment, commands, source hashes, author audit,
research limits and build logs are retained locally. Hashes bind artifacts
and read-only origins; they do not certify the mathematics. No supervised
heavy-compute facility is exposed or needed; none was launched. No additional
model/subagent, network, external message, installation, authentication,
proxy/CA, HOME/CODEX_HOME change, old-artifact write, SQL mutation/recovery,
or arbitrary deadline was used. Same-model author audit, finite arithmetic
and compilation are not formal verification or priority certification.

Bibliography: A. M. Botero, E. Mazzon and L. Pille-Schneider,
*Monge--Ampère measures on balanced polyhedral spaces*, arXiv:2603.08664v1,
manuscript dated 10 March 2026. Source definitions and full inspected comparison
bodies are below; no sequel in preparation or unavailable source is used.

## Exact essential source definitions, for reviewer access

The following are cached v1 source definitions (newline line numbers; snapshots
preserve PDF formfeeds). For readable display only, nonprinting characters are
omitted, private-use parenthesis fragments are rendered as parentheses, and the
face-order glyph is transcribed as `\preceq`. The literal coefficient convention is displayed so that its
replacement by the declared real scalar extension is explicit. Source claims
outside these definitions are not premises. Formula (5) above is exactly
Definition 2.31's displayed intersection formula; it and the normals have
been reconstructed with the actual saturated lattices.

BMPS v1, lines 257--295:

```text
Definition 2.1 (Rational polyhedron). A rational polyhedron in NR is a subset σ ⊆ NR defined
by finitely many affine integral equalities and inequalities, i.e.,
                           
                      σ = n ∈ NR | f1 (n) + b1 = . . . = fr (n) + br = 0,
                                      fr+1 (n) + br+1 ≥ 0, . . . , fN (n) + bN ≥ 0
for some linear forms f1 , . . . , fN ∈ M and bi ∈ Z.
    We define
      • Nσ,R the linear space spanned by all x − y for x, y ∈ σ;
      • Nσ = Nσ,R ∩ N the induced sublattice, and Mσ its dual lattice;
      • Vσ,R = x + Nσ,R , x ∈ σ, the smallest affine subspace of NR containing σ;
      • the relative interior of σ, denoted by relint(σ) is the interior of σ as a subset of Vσ,R ;
      • the dimension of σ as the dimension of Nσ,R .
Definition 2.2 (Rational polyhedral complex). A rational polyhedral complex is a finite
collection Π of rational polyhedra satisfying two conditions:
      • if σ is in Π, then so is any face of σ;
      • if σ and σ ′ are in Π, then σ ∩ σ ′ is either empty or a face of both σ and σ ′ .
   The polyhedra of Π are called faces and we write τ ≺ σ whenever τ is a face of σ. We denote
the set of all k-dimensional faces of Π by Π(k) . The union of all faces in Π is denoted |Π| ⊆ NR
and called the support of Π.
  The dimension of Π is defined as the maximum of the dimensions of the faces of Π, and Π is
pure dimensional if every inclusion-maximal face in Π has the same dimension.
Definition 2.3 (Refinement). A refinement Π′ of a rational polyhedral complex Π is a rational
polyhedral complex such that
      • |Π′ | = |Π|
      • for every σ ′ ∈ Π′ , there exists σ ∈ Π such that σ ′ ⊆ σ;
we write Π′ ≥ Π. Two rational polyhedral complexes are equivalent if they admit a common
refinement.
Definition 2.4 (Rational polyhedral space).
      • Let X ⊆ NR be a topological space. A rational polyhedral complex Π is a rational polyhedral
        structure on X if |Π| = X.
      • A polyhedral space X ⊆ NR is a topological space together with an equivalence class of
        rational polyhedral structures on X.
      • A polyhedral space X is of dimension d (respectively of pure dimension d) if some (and
        hence any) representative of the equivalence class of rational polyhedral structures on X has
        dimension d (respectively pure dimension d).
                   MONGE–AMPÈRE MEASURES ON BALANCED POLYHEDRAL SPACES                                  7


Remark 2.5. From now on, we will only consider rational polyhedral complexes, so that we will
```

BMPS v1, lines 420--449:

```text
Definition 2.18 (Normal vectors). Let τ ≺ σ be faces of Π with dim(τ ) = dim(σ) − 1. This
implies that there exists f ∈ M and b ∈ Q such that f + b is zero on τ , non-negative on σ and
not-identically zero on σ. A normal vector of σ relative to τ is an element
                                                 nσ/τ ∈ Nσ ⊆ N
such that nσ/τ = vσ/τ − v is a primitive generator of Nσ /Nτ and f (vσ/τ ) > 0, when we pick v ∈ τ
and write Vτ,R = v + Nτ,R , Vσ,R = v + Nσ,R .
Definition 2.19 (Weights). A k-weight on Π is a map

                                                   ω : Π(k) → Q
and the number ω(σ) is called the weight of σ ∈ Π(k) . We say that

      • ω is non-negative if ω(σ) ≥ 0 for all σ ∈ Π(k) ; write ω ≥ 0,
      • ω is strictly positive if ω(σ) > 0 for all σ ∈ Π(k) ; write ω > 0.
10                             BOTERO, MAZZON, AND PILLE-SCHNEIDER


Definition 2.20 (Cycles). A k-cycle on Π is a k-weight c : Π(k) → Q such that for any τ ∈ Π(k−1)
the following balancing condition holds:
                                    X
(2.21)                                   c(σ)nσ/τ = 0 ∈ N/Nτ ,
                                    σ∈Π(k)
                                     τ ≺σ

equivalently this sum is an element in Nτ .

     Denote by
       - Wk (Π) the abelian group of k-weights on Π,
       - Zk (Π) the subgroup of k-cycles,
       - Wk (Π)≥0 , Zk (Π)≥0 , Wk (Π)>0 and Zk (Π)>0 the subsets of non-negative and of strictly
         positive weights and cycles on Π.
```

BMPS v1, lines 499--506:

```text
Definition 2.27 (Balanced polyhedral space). Let X ⊆ NR be a polyhedral space of pure
dimension d.
     • A balancing condition on X is a strictly positive d-cycle [X] on X, i.e., for some (or
       equivalently, any) polyhedral complex Π on which [X] is defined we have [X](σ) > 0 for any
       σ ∈ Π(d) .
     • A balanced polyhedral space is a pair (X, [X]), where X is a polyhedral complex of pure
       dimension and [X] is a balancing condition on X (which will be frequently omitted from
       notation).
```

BMPS v1, lines 509--522:

```text
Definition 2.28 (Piecewise affine functions on Π). Let Π be a polyhedral structure on X. A
continuous function ϕ : X → R is piecewise affine on Π if for any σ ∈ Π we have
                                           ϕ|Vσ,R = ϕσ + bσ
where ϕσ ∈ Mσ is an integral linear function, and bσ ∈ Q. In particular, if x ∈ σ and if we write
Vσ,R = x + Nσ,R , then bσ = ϕσ (0) and ϕ(z) = ϕσ (z − x) + bσ .
   We denote by PA(Π) the set of piecewise affine functions on Π.
Definition 2.29 (Piecewise affine functions on X). A continuous function ϕ : X → R is
piecewise affine if it is piecewise affine on some polyhedral structure on X. The set of piecewise
affine functions on X is denote by PA(X). In other words, we have
                                        PA(X) = lim PA(Π),
                                                −→
                                                   Π
where the direct limit is over the set of all polyhedral structures on X ordered by refinements, and
with respect to the inclusion PA(Π) ⊆ PA(Π′ ) for any Π′ ≥ Π.
```

BMPS v1, lines 532--543:

```text
Definition 2.31. Let ϕ ∈ PA(Π) and c ∈ Zk (Π). The intersection product ϕ · c is the (k − 1)-cycle
on Π defined by
                                                                                         (                               )
                                               X                                              X
(2.32)               (ϕ · c)(τ ) :=                         c(σ)ϕσ (nσ/τ ) − ϕτ (                            c(σ)nσ/τ )
                                          σ∈Π(k) : τ ≺σ                                   σ∈Π(k) : τ ≺σ


where τ ∈ Π(k−1) and nσ/τ are normal vectors relative to τ .

Remark 2.33. Note that (2.32) is well-defined. Indeed, let n′σ/τ be another choice of normal
vectors. We have
```

BMPS v1, lines 691--722:

```text
Definition 3.1 (PAPC functions). A piecewise affine function ϕ on X is polyhedrally convex
(in short PAPC) if
                                      ϕ·c≥0
for any c ∈ Zk (U )≥0 an on open U ⊆ X and any k. The space of piecewise affine polyhedrally
convex functions is denoted PAPC(X) and is endowed with the topology of pointwise convergence.

  The property of being PAPC does not depend on the choice of a polyhedral structure on X, by
Lemma 2.34. If we want to specify the polyhedral complex Π, we write
                                          PAPC(Π) := PAPC(X) ∩ PA(Π).
                   MONGE–AMPÈRE MEASURES ON BALANCED POLYHEDRAL SPACES                                      15


Definition 3.2. A convex combination in X is a triple
                                               (x, (xi )i∈I , (αi )i∈I )
where I is a finite set, xi ∈ X ∩ NQ , αi ∈ [0, 1] such that
                                   X                       X
                                       αi = 1 and x =        αi xi .
                                        i∈I                          i∈I
A convex combination is polyhedral on Π for a polyhedral structure Π on X if there are faces τ
and σi in Π such that x ∈ τ , xi ∈ σi and τ \preceq σi ; it is polyhedral on X if it is polyhedral for some
polyhedral structure Π on X. We will abbreviate polyhedral convex combination with PCC.
Definition 3.3 (PC functions). A function ϕ : X → R is polyhedrally convex (in short PC) if
                                          X
                                   ϕ(x) ≤      αi ϕ(xi )
                                                           i∈I
for any polyhedral convex combination (x, (xi )i∈I , (αi )i∈I ) in X. The space of polyhedrally convex
functions on X is denoted PC(X) and is endowed with the topology of pointwise convergence.

   Note that PC functions are automatically continuous on X by [BBGS22, Theorem 6.2]; moreover,
the restriction of any usual convex function in NR to X is PC. The following lemma is analog to
[BBGS22, Proposition 5.7]. We include a proof since in loc. cit. the authors work with an eucledean
structure, instead of an integral structure.
```

BMPS v1, lines 886--892:

```text
Definition 3.14. The space of γ-bounded PA/PC/PAPC functions are defined as
                              PA(X, γ) := {ϕ ∈ PA(X)| ϕ = γ + O(1)}
                              PC(X, γ) := {ϕ ∈ PC(X)| ϕ = γ + O(1)}
                              PAPC(X, γ) := PA(X, γ) ∩ PC(X, γ)

   The non-emptiness of the space PAPC(X, γ) does not imply that the function γ itself is
polyhedrally convex. Nevertheless, whenever this space is non-empty, there exists a polyhedrally
```

BMPS v1, lines 1013--1016 (conditions are spelled out above and supplemented below):

```text
Definition 3.23 (PC-regularizable functions). The space of PC-regularizable functions on X
is the set of continuous functions on X satisfying one of the equivalent conditions (1) or (2) above.
We denote it by PCreg (X, γ), and endow this space with the topology of uniform convergence.

```

BMPS v1, lines 1354--1362:

```text
Definition 4.4. Let ϕ ∈ PA(X), and let Π be a polyhedral structure on X on which ϕ and [X] are
defined. We write
                                      λi := (ϕd · [X])(vi )
for vi ∈ Π(0) . The polyhedral Monge-Ampère measure of ϕ is the finite atomic measure
                                                   X
                                   MApoly (ϕ) :=        λi δvi .
                                                    vi ∈Π(0)

   It follows from Lemma 2.34 that this is indeed independent of Π.
```

BMPS v1, lines 1741--1743:

```text
Definition 4.15. Let Π be a polyhedral structure on X and γ ∈ PA(Π). We say that γ is positive
at infinity if for any face σ ∈ Π and non-zero v ∈ rec(σ), the slope of γσ in the direction v is strictly
positive.
```

BMPS v1, lines 2261--2265:

```text
Definition 6.2. Let u be a continuous function on X. The envelope Pγ (u) is defined as
                   Pγ (u)(x) := sup{ψ(x) | ψ ≤ (γ + u), ψ ∈ PC(X), ψ ≤ γ + O(1)},
with the convention that Pγ (u) ≡ −∞ if the set of functions {ψ ∈ PC(X)|ψ ≤ γ + u, ψ ≤ γ + O(1)}
is empty.

```


For completeness, the two regularization conditions referred to by Definition
3.23 and its decreasing PA construction are specified in the authentic source
as follows. These statements define the regularization language; their general
equivalence proof is **not** a theorem premise here. The explicit \(P+1/n\)
sequence satisfies both conditions directly, and its PA measure is already
unambiguous by the independently proved two-stage algebra.

```text
Definition 3.20 (PSH functions). A function ϕ : X → R is γ-PSH functions if there exists a
decreasing sequence (ϕj)j in PAPC(X, γ) converging pointwise to ϕ.
The space of γ-PSH functions is denoted PSH(X, γ).

Proposition 3.22. Let ϕ be a continuous function on X. Then the following conditions are
equivalent:
 (1) ϕ ∈ PC(X, γ) ∩ PSH(X, γ);
 (2) ϕ is the uniform limit on X of a sequence of functions in PAPC(X, γ). One can moreover
     take the sequence to be decreasing.

Definition 2.25 (Pullback along refinements). Let Π′ be a refinement of Π and ω ∈ Wk(Π).
The pullback of ω to Π′, still denoted by ω, is the k-weight on Π′ defined by
 ω(σ′) := ω(σ) if there exists σ ∈ Π(k) such that σ′ ⊆ σ; 0 otherwise.
Moreover, if c is a k-cycle on Π, then the pullback of c to Π′ is a k-cycle on Π′
(see for instance [GKM09, Example 2.11(iv)]).

Remark 2.37. Let Π be a polyhedral structure on X and U an open subset of X. We can define
the notions of weight and non-negative weight, cycle, pullback of cycles, piecewise affine function,
and intersection product by replacing Π with Π|U in the above definitions. We then denote
 Wk(U) = lim→ Wk(Π|U), Zk(U) = lim→ Zk(Π|U), PA(U) = lim→ PA(Π|U)
where again the limits are over the set of polyhedral structures on X ordered by refinements.
```

The last two paragraphs transcribe the authentic bodies with mathematical
typesetting normalized as in the preceding extracts. The inherited-balancing
claim citing GKM09 is displayed for completeness and is **not** a premise:
refinement and balancing are independently proved in (5)--(7) and (M).
Only the definitions of inheritance and ordinary local testing are used.
The raw competitors in Definition 6.2 use only **upper** growth; none of the
proofs replace it by the stronger two-sided approximation condition.


## Full available inspected primary proof bodies (comparison only)

The following cached v1 bodies are directly included for independent review. They are not theorem premises; the proofs used in this paper are the reconstructions above. Nonprinting extraction characters are omitted, private-use parenthesis fragments are displayed as ordinary parentheses, and the source script-ell glyph is transcribed as ell in these text quotations. These are typography changes only; the full read-only-origin snapshots retain exact bytes.

BMPS v1: Normals, local cycles, intersection, refinement and mixed algebra, extraction lines 420--629.

```text
Definition 2.18 (Normal vectors). Let τ ≺ σ be faces of Π with dim(τ ) = dim(σ) − 1. This
implies that there exists f ∈ M and b ∈ Q such that f + b is zero on τ , non-negative on σ and
not-identically zero on σ. A normal vector of σ relative to τ is an element
                                                 nσ/τ ∈ Nσ ⊆ N
such that nσ/τ = vσ/τ − v is a primitive generator of Nσ /Nτ and f (vσ/τ ) > 0, when we pick v ∈ τ
and write Vτ,R = v + Nτ,R , Vσ,R = v + Nσ,R .
Definition 2.19 (Weights). A k-weight on Π is a map

                                                   ω : Π(k) → Q
and the number ω(σ) is called the weight of σ ∈ Π(k) . We say that

      • ω is non-negative if ω(σ) ≥ 0 for all σ ∈ Π(k) ; write ω ≥ 0,
      • ω is strictly positive if ω(σ) > 0 for all σ ∈ Π(k) ; write ω > 0.
10                             BOTERO, MAZZON, AND PILLE-SCHNEIDER


Definition 2.20 (Cycles). A k-cycle on Π is a k-weight c : Π(k) → Q such that for any τ ∈ Π(k−1)
the following balancing condition holds:
                                    X
(2.21)                                   c(σ)nσ/τ = 0 ∈ N/Nτ ,
                                    σ∈Π(k)
                                     τ ≺σ

equivalently this sum is an element in Nτ .

     Denote by
       - Wk (Π) the abelian group of k-weights on Π,
       - Zk (Π) the subgroup of k-cycles,
       - Wk (Π)≥0 , Zk (Π)≥0 , Wk (Π)>0 and Zk (Π)>0 the subsets of non-negative and of strictly
         positive weights and cycles on Π.
Definition 2.22 (Local cones). Let τ ≺ σ be faces of Π, the normal cone of σ relative to τ is
the polyhedral cone
                      Cσ/τ := {λ(x − y) | λ ≥ 0, x ∈ σ, y ∈ τ } ⊂ Nσ,R ;
it satisfies NCσ/τ = Nσ and hence dim(Cσ/τ ) = dim(σ).
     Let x ∈ X and τ ∈ Π the unique face such that x ∈ relint(τ ). We define the star of Π at x as
                                       Starx (Π) := {Cσ/τ }τ ≺σ .
For a face δ of Π we write Starδ (Π) := Starx (Π) for any x ∈ relint(δ).

   The set Starx (Π) has the structure of a polyhedral complex whose faces are (not necessarily
strictly convex) cones; such structure is also known as generalized fan; see [CLS11, Definition
6.2.2].
Definition 2.23. Let τ ∈ Π and x ∈ relint(τ ). For any k-weight ω on Π, with k ≥ dim(τ ), the
k-weight ωx on Starx (Π) is
                                    ωx (Cσ/τ ) := ω(σ).
Lemma 2.24. The weight ω is a cycle if and only if ωx is a cycle for all x ∈ X.

Proof. For any ell ≥ dim(τ ), ell-faces of Π containing τ are in bijection with the ell-faces of Starx (Π)
containing Cτ /τ = Nτ,R , and this bijection preserves ell-weights by definition. It remains to see that
it preserves normal vectors, i.e. if τ ≺ σ ′ ≺ σ with dim(σ ′ ) = dim(σ) − 1 and nσ/σ′ ∈ Nσ is a
normal vector, then nσ/σ′ is also a normal vector of Cσ/τ relative to Cσ′ /τ . This follows directly
from the fact that NCσ/τ = Nσ and similarly for σ ′ .                                               □

Definition 2.25 (Pullback along refinements). Let Π′ be a refinement of Π and ω ∈ Wk (Π).
The pullback of ω to Π′ , still denoted by ω, is the k-weight on Π′ defined by
                               (
                         ′       ω(σ) if there exists σ ∈ Π(k) such that σ ′ ⊆ σ
                    ω(σ ) :=
                                 0      otherwise.

  Moreover, if c is a k-cycle on Π, then the pullback of c to Π′ is a k-cycle on Π′ (see for instance
[GKM09, Example 2.11(iv)]).
                  MONGE–AMPÈRE MEASURES ON BALANCED POLYHEDRAL SPACES                            11


Definition 2.26. The space of k-weights (respectively k-cycles) on X is the direct limit
                     Wk (X) = lim Wk (Π)     (respectively    Zk (X) = lim Zk (Π))
                              −→                                       −→
                                  Π                                     Π
over the set of polyhedral structures on X ordered by refinements, with pullback maps Wk (Π) →
Wk (Π′ ) (respectively for Zk ) for any refinement Π′ ≥ Π.
   Similarly,
                Wk (X)≥0 = lim Wk (Π)≥0      (respectively    Zk (X)≥0 = lim Zk (Π)≥0 )
                           −→                                            −→
                              Π                                             Π
are the spaces of non-negative k-weights (respectively k-cycles) on X.

    Note that, if X is of dimension d, then Wd (X)>0 and Zd (X)>0 are well-defined too, while
for k < d the notion of strictly positive k-weights or cycles is not stable under pullback along
refinements.
Definition 2.27 (Balanced polyhedral space). Let X ⊆ NR be a polyhedral space of pure
dimension d.
     • A balancing condition on X is a strictly positive d-cycle [X] on X, i.e., for some (or
       equivalently, any) polyhedral complex Π on which [X] is defined we have [X](σ) > 0 for any
       σ ∈ Π(d) .
     • A balanced polyhedral space is a pair (X, [X]), where X is a polyhedral complex of pure
       dimension and [X] is a balancing condition on X (which will be frequently omitted from
       notation).

2.4. Intersection product. Let X be a polyhedral space.
Definition 2.28 (Piecewise affine functions on Π). Let Π be a polyhedral structure on X. A
continuous function ϕ : X → R is piecewise affine on Π if for any σ ∈ Π we have
                                           ϕ|Vσ,R = ϕσ + bσ
where ϕσ ∈ Mσ is an integral linear function, and bσ ∈ Q. In particular, if x ∈ σ and if we write
Vσ,R = x + Nσ,R , then bσ = ϕσ (0) and ϕ(z) = ϕσ (z − x) + bσ .
   We denote by PA(Π) the set of piecewise affine functions on Π.
Definition 2.29 (Piecewise affine functions on X). A continuous function ϕ : X → R is
piecewise affine if it is piecewise affine on some polyhedral structure on X. The set of piecewise
affine functions on X is denote by PA(X). In other words, we have
                                        PA(X) = lim PA(Π),
                                                −→
                                                   Π
where the direct limit is over the set of all polyhedral structures on X ordered by refinements, and
with respect to the inclusion PA(Π) ⊆ PA(Π′ ) for any Π′ ≥ Π.
Definition 2.30. Let ϕ ∈ PA(Π), τ ∈ Π, and x ∈ relint(τ ). We denote by ϕx the (conical)
piecewise affine function on Starx (Π) such that for any σ ≻ τ
                                        (ϕx )|Cσ/τ = ϕσ − ϕτ ,
where we write VCσ/τ ,R = x + NCσ/τ ,R , Vσ,R = x + Nσ,R , and Vτ,R = x + Nτ,R .
   We have ϕx (λ(z − y)) = λ(ϕσ (z − x) − ϕτ (y − x)) whenever z ∈ σ and y ∈ τ , and in particular
ϕx = 0 on Cτ /τ .
12                                         BOTERO, MAZZON, AND PILLE-SCHNEIDER


Definition 2.31. Let ϕ ∈ PA(Π) and c ∈ Zk (Π). The intersection product ϕ · c is the (k − 1)-cycle
on Π defined by
                                                                                         (                               )
                                               X                                              X
(2.32)               (ϕ · c)(τ ) :=                         c(σ)ϕσ (nσ/τ ) − ϕτ (                            c(σ)nσ/τ )
                                          σ∈Π(k) : τ ≺σ                                   σ∈Π(k) : τ ≺σ


where τ ∈ Π(k−1) and nσ/τ are normal vectors relative to τ .

Remark 2.33. Note that (2.32) is well-defined. Indeed, let n′σ/τ be another choice of normal
vectors. We have
                                  (                )
        X                           X
              c(σ)ϕσ (nσ/τ ) − ϕτ (       c(σ)nσ/τ )
     σ∈Π(k) : τ ≺σ                                    σ∈Π(k) : τ ≺σ
                                                                      (                              )
                             X                                                X
                     −                   c(σ)ϕσ (n′σ/τ ) + ϕτ (                           c(σ)n′σ/τ )
                         σ∈Π(k) : τ ≺σ                                    σ∈Π(k) : τ ≺σ
                                                                                (                                                    )
                             X                                                            X
                     =                 c(σ)ϕσ (nσ/τ − n′σ/τ ) − ϕτ (              c(σ)nσ/τ − c(σ)n′σ/τ )
                         σ∈Π(k) : τ ≺σ                              σ∈Π(k) : τ ≺σ
                                               |    {z    }
                                                             ∈Nτ
                                                                                (                                                    )
                             X                                                            X
                     =                   c(σ)ϕτ (nσ/τ − n′σ/τ ) − ϕτ (                             c(σ)nσ/τ − c(σ)n′σ/τ ) = 0.
                         σ∈Π(k) : τ ≺σ                                             σ∈Π(k) : τ ≺σ

Lemma 2.34. Let ϕ ∈ PA(Π) and c ∈ Zk (Π). Let Π′ be a refinement of Π, denote by c′ and (ϕ · c)′
the pullbacks to Π′ of c and ϕ · c respectively. The equality

                                                               (ϕ · c)′ = ϕ · c′

holds in Zk−1 (Π′ ).


Proof. Let τ ′ ∈ Π′(k−1) and recall that
                                                                                   (                                         )
                                    X                                                        X
                ϕ · c′ :=                            c′ (σ ′ )ϕσ′ (nσ′ /τ ′ ) − ϕτ ′ (                       c′ (σ ′ )nσ′ /τ ′ ) .
                             σ ′ ∈Π′(k) : σ ′ ≻τ ′                                   σ ′ ∈Π′(k) ; σ ′ ≻τ ′


Let τ be the minimal face of Π such that τ ′ ⊆ τ . If dim(τ ) ≥ k + 1, then for any σ ′ ≻ τ ′ , the
faces σ such that σ ′ ⊆ σ have dimension at least k + 1 as they contain τ . This implies that
(ϕ · c′ )(τ ′ ) = 0 = (ϕ · c)′ (τ ′ ).
    If dim(τ ) = k, then there are precisely two faces σ ′ , σ ′′ ∈ Π′(k) containing τ ′ . We have that
σ ′ ∩ σ ′′ = τ ′ , c′ (σ ′ ) = c′ (σ ′′ ), Nσ′ = Nσ′′ , nσ′ /τ ′ = −nσ′′ /τ ′ , and ϕσ′ = ϕσ′′ . This implies

         (ϕ · c′ )(τ ′ ) = c′ (σ ′ ) ϕσ′ (nσ′ /τ ′ ) − ϕσ′ (nσ′ /τ ′ ) − ϕτ ′ (nσ′ /τ ′ − nσ′ /τ ′ = 0 = (ϕ · c)′ (τ ′ ).
                                                                                                  
                      MONGE–AMPÈRE MEASURES ON BALANCED POLYHEDRAL SPACES                                                    13


   If dim(τ ) = k − 1, then we denote by σ the minimal face of Π such that σ ′ ⊆ σ, for any σ ′ ∈ Π′(k)
with σ ′ ≻ τ ′ . As c′ (σ ′ ) = 0 unless dim(σ ′ ) = dim(σ) = k, we have
                                                                  (                        )
                                    X                                                        X
         (ϕ · c′ )(τ ′ ) =                        c′ (σ ′ )ϕσ′ (nσ′ /τ ′ ) − ϕτ ′ (                     c′ (σ ′ )nσ′ /τ ′ )
                                                                                  (                                       )
                                                                                  (                                       )
                                     σ ′ ≻τ ′                                              σ ′ ≻τ ′
                             dim(σ ′ )=dim(σ)=k                                    dim(σ ′ )=dim(σ)=k
                                                                      (                          )
                                 X                                           X
                       =                    c(σ)ϕσ (nσ/τ ) − ϕτ (                      c(σ)nσ/τ )
                             σ∈Π(k) : σ≻τ                               σ∈Π(k) ; σ≻τ
                                                     ′   ′
                       = (ϕ · c)(τ ) = (ϕ · c) (τ ),
which concludes the proof.                                                                                                    □
Lemma 2.35. Let c ∈ Zk (Π), ϕ, ψ ∈ PA(Π), and λ, µ ∈ Q. We have
    (i) (linearity) (λϕ + µψ) · c = λ(ϕ · c) + µ(ψ · c),
   (ii) (balancing condition) ϕ · c ∈ Zk−1 (Π),
  (iii) (commutativity) ψ · (ϕ · c) = ϕ · (ψ · c).

Proof. The linearity of the intersection pairing follows from the definition. For the other two
properties, we reduce to the local fans. Indeed, given any x ∈ X, the equality (ϕ · c)x = ϕx · cx
holds in Zk−1 (Starx (Π)). The image of Starx (Π) along the projection map NR → NR /(x + Nτ,R ) is
a fan in the sense of [AR10, Definition 2.2]. Then the statements follow from [AR10, Proposition
3.7] and Lemma 2.24.                                                                            □

   It follows from Lemmas 2.34 and 2.35 that (2.32) induces intersection pairings
                                               PA(X) × Zk (X) → Zk−1 (X)
where, for ϕ ∈ PA(Π1 ) and c ∈ Zk (Π2 ), the pairing is given by ϕ · c′ for any common refinement Π′
of Π1 and Π2 . For any ϕ1 , . . . , ϕell ∈ PA(X) and any cycle c ∈ Zk (X), we define inductively
(2.36)                                      ϕ1 · . . . · ϕell · c := ϕ1 · (. . . (ϕell · c)) .
In particular, for ϕ = ϕ1 = . . . = ϕell , we simply write ϕ1 · . . . ϕell · c = ϕell · c.
Remark 2.37. Let Π be a polyhedral structure on X and U an open subset of X. We can define
the notions of weight and non-negative weight, cycle, pullback of cycles, piecewise affine function,
and intersection product by replacing Π with Π|U in the above definitions. We then denote
               Wk (U ) = lim Wk (Π|U ),             Zk (U ) = lim Zk (Π|U ),           PA(U ) = lim PA(Π|U )
                         −→                                   −→                                −→
                               Π                                  Π                               Π

where again the limits are over the set of polyhedral structures on X ordered by refinements.
```

BMPS v1: PAPC equivalence and its full source proof, extraction lines 723--786.

```text
Lemma 3.4. The two definitions of PAPC functions are equivalent, i.e.,
                                        PAPC(X) = PA(X) ∩ PC(X).

Proof. We argue by double inclusion. Let ϕ ∈ PAPC(X) and (x, (xi )i∈I , (αi )i∈I ) a polyhedral
convex combination in X. Let Π be a polyhedral complex such that ϕ ∈ PA(Π), and Π′ a refinement
of Π such that x ∈ Π′(0) and xi ∈ ρi ∈ Π′(1) for some ρi ≻ x. Let nρ/x be normal vectors relative to
x for each ρ ∈ Π′(1) with x ≻ ρ. Then there exist βi ∈ Q≥0 such that xi − x = βi nρi /x . Consider
the weight                  (P
                                i∈I : xi ∈ρ αi βi if there exists i such that xi ∈ ρ
                    c(ρ) :=
                             0                    otherwise,
and an open U ⊆ X such that U ∩ Π′(0) = {x}. Then c is a non-negative cycle in Z1 (Π′ |U ) as
                     X                   X                 X
                             c(ρ)nρ/x =     αi βi nρi /x =   αi (xi − x) = 0.
                     ρ∈Π′(1) |U : x≺ρ               i∈I                    i∈I

By Definition 3.1 we have
                                              X                               X
                   0 ≤ (ϕ · c)(x) =                        c(ρ)ϕρ (nρ/x ) =            αi βi ϕρi (nρi /x )
                                        ρ∈Π′(1) |U : x≻ρ                         i∈I
                                        X                         X
                                    =         αi ϕρi (xi − x) =          αi ϕ(xi ) − ϕ(x)
                                        i∈I                        i∈I
which implies that ϕ is polyhedrally convex in the sense of Definition 3.3.
   Let ϕ ∈ PA(X) ∩ PC(X). Let c ∈ Zk (Π|U ) be a non-negative cycle on an open U ⊆ X.
Up to taking a refinement of Π we can assume that ϕ ∈ PA(Π). Let τ ∈ Π(k−1) |U and pick
x ∈ U ∩ relint(τ ) ∩ NQ . Let nσ/τ be normal vectors relative to τ for each σ ∈ Π(k) |U with τ ≺ σ. By
16                                   BOTERO, MAZZON, AND PILLE-SCHNEIDER
              P
                        σ/τ = vτ ∈ Nτ . Up to rescaling c, we can assume that gcd(c(σ))σ≻τ = 1
(2.21) we have σ≻τ c(σ)nP
and write gcd(c(σ))σ≻τ = σ≻τ ασ c(σ) for some ασ ∈ Z. We set
                    eσ/τ := nσ/τ − ασ vτ another normal vector of σ relative to τ ,
                    n
                                 nσ/τ ∈ σ ∩ U for some ε ∈ Q>0 sufficiently small,
                      xσ := x + εe
                            X
                       S :=     c(σ) ≥ 0.
                              σ≺τ

If S = 0, then (ϕ · c)(τ ) = 0, hence ϕ · c has non-negative weight at τ . If S ̸= 0, then
                                                                    
                                           x, (xσ )σ≻τ , ( c(σ)
                                                            S   )σ≻τ


is a polyhedral convex combination as c(σ)                                 c(σ)
                                                                  P
                                       S ∈ [0, 1],                  σ≻τ     S = 1 and
                                                                                                       !
          X c(σ)                     X                             X                     X
                S   xσ = x + Sε               nσ/τ = x + Sε
                                          c(σ)e                          c(σ)nσ/τ − vτ         ασ c(σ)     = x.
          σ≻τ                       σ≻τ                            σ≻τ                   σ≻τ

By Definition 3.3 we have
                                                          !
                               X c(σ)                             X
                     0 ≤ Sε           S   ϕ(xσ ) − ϕ(x)       =                 nσ/τ ) = (ϕ · c)(τ )
                                                                        c(σ)ϕσ (e
                               σ≻τ                                σ≻τ

which implies that ϕ · c is a non-negative cycle in Zk−1 (Π|U ), hence ϕ is polyhedrally convex in the
sense of Definition 3.1.                                                                            □
```

BMPS v1: Uniform decreasing regularization: full source body, extraction lines 1005--1030.

```text
Proposition 3.22. Let ϕ be a continuous function on X. Then the following conditions are
equivalent:
     (1) ϕ ∈ PC(X, γ) ∩ PSH(X, γ);
                  MONGE–AMPÈRE MEASURES ON BALANCED POLYHEDRAL SPACES                             21


   (2) ϕ is the uniform limit on X of a sequence of functions in PAPC(X, γ). One can moreover
       take the sequence to be decreasing.
Definition 3.23 (PC-regularizable functions). The space of PC-regularizable functions on X
is the set of continuous functions on X satisfying one of the equivalent conditions (1) or (2) above.
We denote it by PCreg (X, γ), and endow this space with the topology of uniform convergence.

Proof. (1) =⇒ (2). Assume ϕ ∈ PC(X, γ) ∩ PSH(X, γ) and let (ϕj )j be a decreasing sequence
in PAPC(X, γ) converging pointwise to ϕ. By Lemma 3.16, both ψ := ϕ − γ and ψj := ϕj − γ
extend continuously to the closure of X in NΣ , for a fan Σ containing rec(Π). We denote by ψ,
respectively ψ j those continuous extensions. We claim that if x lies on the boundary on X, then
(ψ j (x))j decreases to ψ(x). Indeed, it follows from the proof of Lemma 3.16 that there exists a
sequence (xl )l in X converging to x, and such that ψ(x) = inf l ψ(xl ) and similarly for ψ j . Since
ψ(xl ) = inf j ψj (xl ), we infer ψ(x) = inf (l,j) ψj (xl ) = inf j ψ j (x) and the claim follows.
As a result, by Dini’s lemma (ψ j )j converges uniformly to ψ on the compactification of X, thus
(ϕj )j converges uniformly to ϕ on X.
   (2) =⇒ (1). Let (ϕj )j be a sequence in PAPC(X, γ) converging uniformly to ϕ on X. For an
index j sufficiently large, we have
                            |ϕ − γ| ≤ |ϕ − ϕj | + |ϕj − γ| ≤ ε + C ≤ C ′ ,
which implies that ϕ ∈ PC(X, γ).                                                                   □

```

BMPS v1: Degree invariance and full source proof, extraction lines 1363--1391.

```text
Definition 4.5. Let c ∈ Z0 (X) be a 0-cycle. The degree of c is the number
                                                X
                                      deg(c) =       c(v)
                                                   v∈Π(0)
whenever c ∈ Z0 (Π). For ϕ ∈ PA(X), the degree of ϕ is the rational number
                                      Z
                            deg(ϕ) :=   MApoly (ϕ) = deg(ϕd · [X]).
                                            X
Lemma 4.6. For any ϕ, ψ ∈ PA(X) such that (ϕ − ψ) is a bounded function on X, we have
deg(ϕ) = deg(ψ). In particular, if ϕ ∈ PA(X, γ) for some γ ∈ PA(X), then deg(ϕ) = deg(γ).

Proof. Let Π be a polyhedral complex on X on which ϕ and ψ are defined. Let
                                   Xd−1
                                c=(     ϕj · ψ d−j−1 · [X]) ∈ Z1 (Π),
                                      j=0

then by multilinearity and commutativity we have the following equality of 0-cycles:
                                (ϕ − ψ) · c = (ϕd · [X]) − (ψ d · [X]).
We are thus left to prove the following: if η ∈ PAb (Π) and c ∈ Z1 (Π), then deg(η · c) = 0, for which
we argue as in [AR10, Lemma 8.3]. The quantity deg(η · c) is the sum over vertices v of Π of the
sum of outgoing slopes of η at v, weighted by c; each bounded edge appears twice, once for each
of its endpoints which have opposite normal vectors, so that the two corresponding slopes cancel
28                                     BOTERO, MAZZON, AND PILLE-SCHNEIDER


out. Since η has slope zero along each unbounded edge - being a bounded affine function - we get
deg(η · c) = 0.                                                                               □

     One can define the mixed Monge–Ampère operator of tuples of piecewise affine functions on X.
```

BMPS v1: Raw envelope properties and full source proof, extraction lines 2261--2293.

```text
Definition 6.2. Let u be a continuous function on X. The envelope Pγ (u) is defined as
                   Pγ (u)(x) := sup{ψ(x) | ψ ≤ (γ + u), ψ ∈ PC(X), ψ ≤ γ + O(1)},
with the convention that Pγ (u) ≡ −∞ if the set of functions {ψ ∈ PC(X)|ψ ≤ γ + u, ψ ≤ γ + O(1)}
is empty.

   If (γ + u) is quasi-γ-PSH, then Pγ (u) ̸≡ −∞. Indeed, let γ + u = ϕ + g with ϕ ∈ PSH(X, γ) and
g ∈ Cb0 (X), then ψ := ϕ + inf X g is a competitor in the supremum defining the envelope.
     The envelope satisfies the following basic properties.
Proposition 6.3. Let notations as above and let c ∈ R. The following hold true:
     (1) if Pγ (u) ̸≡ −∞, then Pγ (u) ∈ PC(X),
     (2) Pγ (u) ≤ γ + u,
     (3) if u is bounded, then Pγ (u) ∈ PC(X, γ),
     (4) if (γ + u) ∈ PSH(X, γ) or (γ + u) ∈ PC(X, γ), then Pγ (u) = γ + u,
     (5) if u ≤ v then Pγ (u) ≤ Pγ (v),
     (6) Pγ (u + c) = Pγ (u) + c,
     (7) Pγ (u) is concave in both arguments in the following sense:
                         Ptγ+(1−t)γ ′ (tu + (1 − t)u′ ) ≥ tPγ (u) + (1 − t)Pγ ′ (u′ ),
     (8) supX |Pγ (u) − Pγ (v)|≤ supX |u − v|.

Proof. If Pγ (u) ̸≡ −∞, then the subset {ψ ∈ PC(X)|ψ ≤ γ + u, ψ ≤ γ + O(1)} ⊂ PC(X) is
non-empty and uniformly bounded from above, so that its pointwise sup defines a PC function by
[BBGS22, Theorem 6.24], and Part (1) follows. Part (2) is clear, and Part (3) follows from the
inequalities:
                            γ + inf u ≤ Pγ (u) ≤ γ + u ≤ γ + sup u.
                                      X                                 X
                   MONGE–AMPÈRE MEASURES ON BALANCED POLYHEDRAL SPACES                                45


Finally, (4)-(6) are clear from the definitions. Part (7) follows from the fact that if ψ ∈ PC(X),
ψ ′ ∈ PC(X) with ψ ≤ γ + u and ψ ′ ≤ γ ′ + u′ , ψ ≤ γ + O(1) and ψ ≤ γ ′ ≤ O(1) then
                               tψ + (1 − t)ψ ′ ∈ PSH(X, tγ + (1 − t)γ ′ )
and is dominated by tu + (1 − t)u′ . Finally, (8) follows from applying (5) to the inequality v +
inf(u − v) ≤ u ≤ v + sup(u − v).                                                                □
```

## Existing one-dimensional accessible-mass dossier (not a new result or premise)

Complete controlling-book input one-dimensional-STATEMENT.tex:

```latex
% P05.2 one-dimensional graph classification, 25 September 2026.

Continue with the finite one-dimensional balanced rational polyhedral
structure $\Pi$ and the local relation cones $K_v$ above.  We may insert one
bivalent vertex in every component without a vertex.  This does not change
any original relation cone or the orthogonality problem.

\begin{definition}
\label{def:frontier-polyhedral-mass-accessible}
Let $\gamma\in\mathrm{PA}_{\mathbf R}(\mathbf X)\cap
\mathrm{PC}(\mathbf X)$.  A vertex $v\in\Pi^{(0)}$ is
$\gamma$-mass-accessible if there is a function
\[
 \varphi\in\mathrm{PA}_{\mathbf R}(\mathbf X)\cap
 \mathrm{PC}(\mathbf X),
 \qquad
 \varphi-\gamma\in\mathrm{PA}_{\mathbf R,b}(\mathbf X),
\]
such that
\[
 \MA_{\mathrm{poly},\mathbf R}(\varphi)\{v\}
 =\sum_{e\in E(v)}w_es_{v,e}(\varphi)>0.
\]
\end{definition}

\begin{lemma}
\label{lem:frontier-polyhedral-ambient-vertex-accessibility}
Let $\gamma$ be positive at infinity.  Then every vertex of $\Pi$ is
$\gamma$-mass-accessible.
\end{lemma}

\begin{lemma}
\label{lem:frontier-polyhedral-accessible-mass-obstruction}
Suppose that $\dim K_v>1$ and that $v$ is
$\gamma$-mass-accessible.  Then $(\mathbf X,\gamma)$ does not have
real-polyhedral orthogonality.  More precisely, there is a bounded
real-piecewise-affine obstacle $u$ such that
\[
 \int_{\mathbf X}
 \bigl(P_\gamma(u)-(\gamma+u)\bigr)
 \MA_{\mathrm{poly},\mathbf R}(P_\gamma(u))<0.
\]
\end{lemma}

\begin{theorem}
\label{thm:frontier-polyhedral-graph-orthogonality-classification}
Let $\mathbf X$ be a one-dimensional balanced rational polyhedral space
admitting a finite structure $\Pi$, and let
$\gamma\in\mathrm{PA}_{\mathbf R}(\mathbf X)\cap
\mathrm{PC}(\mathbf X)$ be positive at infinity.  Then
$(\mathbf X,\gamma)$ has real-polyhedral orthogonality if and only if
\[
                         \dim K_v=1
                         \qquad\text{for every }v\in\Pi^{(0)}.
\]
Thus the repaired one-dimensional classification is local at the vertices:
bounded edges, graph cycles, and lattice saturation introduce no additional
condition.
\end{theorem}

Positivity at infinity enters the converse only through
\Cref{lem:frontier-polyhedral-ambient-vertex-accessibility}: it permits an
ambient polyhedral norm with strictly smaller recession slope on every
unbounded edge.  The statement neither repairs the literal integral-slope
class nor addresses higher-dimensional balanced spaces.

```

Complete controlling-book input one-dimensional-PROOF.tex:

```latex
% P05.2 one-dimensional graph classification proof, 25 September 2026.

\begin{proof}[\Cref{lem:frontier-polyhedral-ambient-vertex-accessibility}]
Choose a rational polyhedral norm $\lVert\cdot\rVert$ on $N_{\mathbf R}$.
On every unbounded edge $e$, let $r_e>0$ be the eventual slope of $\gamma$
in the primitive outgoing direction $u_e$.  Since there are only finitely
many such edges, choose $\varepsilon>0$ such that
\[
                         \varepsilon\lVert u_e\rVert<r_e
                         \qquad\text{for every unbounded }e.
\]
If $\mathbf X$ has no unbounded edge, any positive $\varepsilon$ will do.

Fix a vertex $v$ and choose $C>\gamma(v)$.  The restriction to $\mathbf X$
of the ambient convex function
\[
                         h(x):=C+\varepsilon\lVert x-v\rVert
\]
is polyhedrally convex and is affine on a finite rational polyhedral
refinement.  A finite maximum preserves every polyhedral Jensen inequality,
so the continuous function
\[
                         F:=\max\{\gamma,h\}
\]
is polyhedrally convex and has only finitely many affine pieces on every
edge.  Its breakpoints need not be rational, so one further rational
interpolation is required.

Along every unbounded edge the eventual slope of $\gamma-h$ is positive.
Hence $F=\gamma$ outside a compact subset of $\mathbf X$.  On each edge,
choose finitely many rational points which include its endpoints, meet the
affine germ of $F$ at every incident vertex, and, on an unbounded edge,
include a point beyond which $F=\gamma$.  Let $\varphi$ be the affine
interpolation of the values of $F$ at these points, extended by $\gamma$ on
the remaining unbounded tails.  Secant slopes of a convex function on an
interval are nondecreasing, so $\varphi$ is convex on each edge.  Its
outgoing slopes at every original vertex equal those of $F$; hence all local
nonnegative-cycle inequalities are preserved.  The one-dimensional local
slope criterion gives
\[
 \varphi\in\mathrm{PA}_{\mathbf R}(\mathbf X)\cap
 \mathrm{PC}(\mathbf X),
 \qquad
 \varphi-\gamma\in\mathrm{PA}_{\mathbf R,b}(\mathbf X).
\]

The strict inequality $C>\gamma(v)$ persists on a sufficiently small closed
star about $v$.  Choose the first rational interpolation points inside this
star.  Then $\varphi=h$ on their incident segments, and its outgoing slope
along every incident edge is
$\varepsilon\lVert u_{e/v}\rVert>0$.  Therefore
\[
 \MA_{\mathrm{poly},\mathbf R}(\varphi)\{v\}
 =\varepsilon\sum_{e\in E(v)}w_e\lVert u_{e/v}\rVert>0.
\]
Thus $v$ is $\gamma$-mass-accessible.
\end{proof}

\begin{proof}[\Cref{lem:frontier-polyhedral-accessible-mass-obstruction}]
Choose $\varphi$ as in
\Cref{def:frontier-polyhedral-mass-accessible}.  Let
$s=(s_e)_{e\in E(v)}$ be its outgoing slope vector at $v$, let
$w=(w_e)_{e\in E(v)}$, and put
\[
                         m:=w\mathbin{\cdot}s>0.
\]
The local convexity criterion gives
$\lambda\mathbin{\cdot}s\geq0$ for every $\lambda\in K_v$.

Let $L_v$ be the linear span of $K_v$.  Since $\dim K_v>1$ and
$w\mathbin{\cdot}s>0$, choose a positive rational vector
$c=(c_e)_{e\in E(v)}$ such that the restrictions of $c$ and $s$ to $L_v$
are not proportional.  Multiplying $c$ by a sufficiently large positive
rational number, choose points $x_e$ at integral-affine distance
$\rho_e=c_e^{-1}$ from $v$ such that every segment $[v,x_e]$ contains no
other vertex and $\varphi$ is affine on it.  The slice
\[
                       B_c:=\{\lambda\in K_v:\lambda\mathbin{\cdot}c=1\}
\]
is nonempty and compact.  Set
\[
                       \tau:=\min_{\lambda\in B_c}
                       \lambda\mathbin{\cdot}s\geq0.
\]

Raise $\varphi(v)$ by $\tau$, interpolate affinely to the unchanged values
$\varphi(x_e)$, and leave $\varphi$ unchanged off the closed star.  Denote
the resulting function by $\widetilde\varphi$.  Its outgoing slope vector
at $v$ is
\[
                         \widetilde s=s-\tau c.
\]
The definition of $\tau$ gives
$\lambda\mathbin{\cdot}\widetilde s\geq0$ for every $\lambda\in K_v$,
and a minimizer $\lambda^0\in B_c$ satisfies
\begin{equation}
                  \lambda^0\mathbin{\cdot}\widetilde s=0.
                  \label{eq:frontier-polyhedral-supporting-relation}
\end{equation}
At each $x_e$ the modified slope increases back to the old slope, so
one-variable convexity is preserved.  All other local inequalities are
unchanged.  Thus $\widetilde\varphi$ is polyhedrally convex and remains
$\gamma$-bounded.

Its mass at $v$ is still positive.  This is immediate when $\tau=0$.
If $\tau>0$, the linear functional
$\lambda\mapsto\lambda\mathbin{\cdot}s$ is nonconstant on $B_c$ by the
choice of $c$.  The point
$w/(w\mathbin{\cdot}c)$ lies in the relative interior of $B_c$, so its
value is strictly larger than the minimum.  Hence
\begin{equation}
 \frac{w\mathbin{\cdot}s}{w\mathbin{\cdot}c}>\tau,
 \qquad
 w\mathbin{\cdot}\widetilde s>0.
 \label{eq:frontier-polyhedral-positive-projected-mass}
\end{equation}

Let $b$ be the real-piecewise-affine function which is one at $v$, zero at
every $x_e$, affine on $[v,x_e]$, and zero off the closed star.  Put
\[
                         a:=\widetilde\varphi+b,
                         \qquad
                         u:=a-\gamma.
\]
Then $u$ is bounded and real-piecewise affine, and
$\widetilde\varphi$ is an admissible competitor for $P_\gamma(u)$.

Let $q\leq a$ be any polyhedrally convex envelope competitor and put
\[
 C_0:=\sum_e\frac{\lambda^0_e}{\rho_e},
 \qquad
 \alpha_e:=\frac{\lambda^0_e/\rho_e}{C_0}.
\]
Because $x_e=v+\rho_eu_{e/v}$ and $\lambda^0\in K_v$, the points $x_e$
with coefficients $\alpha_e$ form a polyhedral convex combination with
barycentre $v$.  Since $b(x_e)=0$, polyhedral convexity and
\eqref{eq:frontier-polyhedral-supporting-relation} give
\[
 \begin{aligned}
 q(v)
 &\leq\sum_e\alpha_eq(x_e)
 \leq\sum_e\alpha_e\widetilde\varphi(x_e)\\
 &=\widetilde\varphi(v)
   +\frac{1}{C_0}\sum_e\lambda^0_e\widetilde s_e
 =\widetilde\varphi(v).
 \end{aligned}
\]
Taking the supremum over competitors and using the competitor
$\widetilde\varphi$ shows that, for $P:=P_\gamma(u)$,
\[
                         P(v)=\widetilde\varphi(v),
                         \qquad
                         P\geq\widetilde\varphi.
\]

The one-dimensional real-affine envelope theorem makes $P$
real-piecewise affine.  Since $P-\widetilde\varphi$ is nonnegative and
vanishes at $v$, every outgoing slope of $P$ at $v$ is at least the
corresponding slope of $\widetilde\varphi$.  By
\eqref{eq:frontier-polyhedral-positive-projected-mass},
\[
              \MA_{\mathrm{poly},\mathbf R}(P)\{v\}
              \geq w\mathbin{\cdot}\widetilde s>0.
\]
At $v$ one has $P-a=-1$, while $P-a\leq0$ everywhere and
$\MA_{\mathrm{poly},\mathbf R}(P)$ is nonnegative.  Therefore
\[
 \int_{\mathbf X}(P-a)\MA_{\mathrm{poly},\mathbf R}(P)
 \leq-\MA_{\mathrm{poly},\mathbf R}(P)\{v\}<0.
\]
This is the required failure of orthogonality.
\end{proof}

\begin{proof}[\Cref{thm:frontier-polyhedral-graph-orthogonality-classification}]
If $\dim K_v=1$ at every vertex, orthogonality is
\Cref{thm:frontier-polyhedral-local-rank-one-graph}.

Conversely, suppose that $\dim K_v>1$ at some vertex.  By
\Cref{lem:frontier-polyhedral-ambient-vertex-accessibility}, this vertex is
$\gamma$-mass-accessible.  Then
\Cref{lem:frontier-polyhedral-accessible-mass-obstruction} gives a bounded
real-piecewise-affine obstacle with a strictly negative orthogonality
integral.  Thus orthogonality fails.
\end{proof}

```

## Original Appendix M scope check (no P06.2 premise)

The warning, lines 917--930:

```latex
\begin{warning}{The continuous zero-current problem}
\Cref{prop:ch18-real-pl-zero-current-harmonic} settles the implication for
$\mathbf R$-PL functions under its hypotheses.  For an arbitrary continuous
function $u$ in higher dimension, however, it is not known in this
generality whether $\dprimeddprime[u]=0$ forces harmonicity or classical
pluriharmonicity: there is no residual line bundle or integral skeletal
calibration from which to recover the face-balancing law, and arbitrary CLD
currents cannot simply be pulled back to all curve probes.  CLD further note
in \cite[Remark~7.8.3]{CLD25} that it is not even known whether local
integrability plus $\dprimeddprime[u]=0$ forces continuity.  The published
continuous result on smooth proper algebraic curves is recorded in
\Cref{cor:ch19-continuous-zero-current-harmonic}; see also
\Cref{def:ch16-harmonic-function,sec:ch16-harmonic-ambiguity}.
\end{warning}

```

Its scope limitation, lines 955--959:

```latex

Thus \Cref{prop:p062-proper-full-rank-moment} narrows the warning above only
for functions already carried by one proper full-rank moment.  It supplies no
factorization theorem for a general continuous function and leaves the
unrestricted higher-dimensional zero-current problem open.

```



# Complete supporting proofs supplied for independent reconstruction

These are mathematical evidence, not grants of assumptions. Each application and dependency must be reconstructed. Prior verdicts and hashes do not replace these proofs.
