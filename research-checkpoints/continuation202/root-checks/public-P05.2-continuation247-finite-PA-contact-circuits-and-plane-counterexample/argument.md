# Finite slope certificates for contact and global PA obstructions

This is the complete mathematical argument from the standalone paper, converted without omitting proof units. Candidate status is false; the entire original P05.2 remains open. The full unchanged task and grants are retained locally.

## Abstract

For a finite piecewise-affine envelope, noncontact at a vertex forces a nonzero
nonnegative zero-cost relation among its tangent generators. Conversely, any
globally reference-compatible PA function with such a relation and positive
raw top-intersection mass is the exact envelope of an explicitly constructed
bounded obstacle with a strictly negative contact integral. This gives an
obstacle-free algebraic characterization of contact restricted to finite PA
endpoints, and a finite semialgebraic obstruction test on each specified
rational carrying structure. The construction works in arbitrary dimension,
with nonseparable obstacles, primitive saturated normals, and the actual
global reference growth. We demonstrate it on two planes meeting along a
line, computing masses $8,4,4$ and contact integral $-2$. We do not prove
that general continuous envelopes are real-PA regularizable, or extend the
criterion to all regularizable non-PA endpoints. The entire original
classification remains open. Candidate status is false.


## Retained target, conventions, and grants

The unchanged target is necessary and sufficient geometric conditions for
the actual balanced rational pair $(X,\gamma)$, including every admissible
obstacle, genuine envelope regularization and operator antecedents, and
$$
 \int_X\bigl(P_\gamma(u)-(\gamma+u)\bigr)\operatorname{MA}_{\mathrm{poly}}(P_\gamma(u))=0.
$$
The complete supplied family dossier, completion criteria, and assignment
are retained in `input.json` and `retained-task.json`. No
dossier theorem is used as a grant. The only mathematical grants are the
complete accepted caller papers A224, B225, R230 and their supplied
source-preserving clarifications. Their complete bodies and clarifications
are retained under `caller-grants/`.

Throughout, $X\subset N_{\mathbb{R}}$ is the support of a finite rational complex,
pure of dimension $d\geq1$, with strictly positive balanced top weights
$w_\sigma$. Rational weights are the literal BMPS setting; the finite
real-linear calculations also allow specified positive real weights.
For translated cells the saturated tangent lattice is
$$
 N_\sigma=N\cap\operatorname{span}_{\mathbb{R}}(\sigma-\sigma).
$$
An inward normal $n_{\sigma/\tau}$ represents the primitive generator of
$N_\sigma/N_\tau$ pointing into $\sigma$. The raw divisor is
$$
 D_f c(\tau)=\sum_{\sigma\succ\tau}c(\sigma)f_\sigma(n_{\sigma/\tau})
 -f_\tau\left(\sum_{\sigma\succ\tau}c(\sigma)n_{\sigma/\tau}\right).
$$
Linear parts, rather than affine values, occur in this formula. A convex
bend has positive sign. We use the finite recursive measure
$$
 \operatorname{MA}_{\mathrm{poly},*}(f)=\sum_{v\in\Pi(0)}(D_f^d[X])(v)\delta_v,\qquad *={\mathbb{Z}},{\mathbb{R}}.
$$
There is no additional factorial in this recursion. In the literal
category this is BMPS Definition 4.4. In the real category it denotes
the explicitly verified real-linear finite-PA extension of the same
formula, not an operator on every continuous PC function.

The class $\operatorname{PA}_{\mathbb{Z}}$ has integral tangent linear parts and rational
constants; $\operatorname{PA}_{\mathbb{R}}$ has arbitrary real affine coefficients on a finite
*rational* carrying complex. Both classes are continuous.
Set $\operatorname{PAPC}_*=\operatorname{PA}_*\cap\operatorname{PC}_q$, where $\operatorname{PC}_q$ is the printed
rational-endpoint PCC class. A PCC has a common center face contained as
a face in each endpoint cell. Competitors in
$$
 P_\gamma(u)=\sup\{q\in\operatorname{PC}_q:q\leq\gamma+u,\ q\leq\gamma+O(1)\}
$$
are not restricted to either PA coefficient category.
Regularizable means a uniform decreasing limit of relative
$\operatorname{PAPC}_*$ functions. Each PA endpoint measured here has a constant
regularizing sequence; decreasing positive rational constant additions
also work. No measure is assigned to a merely continuous endpoint.

R230 gives the continuous dominating completion of every finite printed-PC
competitor on this domain, preserving continuous obstacles and its actual
growth upper bound. It identifies (2) with the continuous-competitor
envelope for every bounded continuous obstacle. We use this theorem without
reproving it. B225 gives positive spanning of every positive balanced star.
A224's local-support argument motivates a lemma that we reconstruct below
on the present general domain. We do not promote its fan-specific main
theorem to a theorem on arbitrary spaces. All actual grant applications
retain their stated hypotheses.

We make no use of a strict-convexity theorem. Our zero-cost tests discard
zero-coefficient terms. The printed BMPS strictness wording counts endpoint
indices even though coefficients may be zero; that separate degeneracy is
not repaired or used here. A224's strictness claim has its disclosed
active-coefficient convention.

## Genuine finite raw intersections and source conversion

We audit the complete elementary proof units BBGS Proposition 3.12,
Proposition 3.15, Lemma 3.18 and Proposition 3.19, in the fixed 2022
publisher version. Their definitions use inward Euclidean *unit*
conormals and the negative sign appropriate to concave functions. Here is
the conversion, including every weight factor needed in our application.
Choose an auxiliary Euclidean inner product, and let $a_\sigma$ be
the covolume of $N_\sigma$ in its tangent space, with $a_v=1$.
If $\nu_{\sigma/\tau}$ is the unit inward conormal, saturation gives
$$
 \operatorname{pr}_{N_{\tau,{\mathbb{R}}}^{\perp}}n_{\sigma/\tau}
   =\frac{a_\sigma}{a_\tau}\nu_{\sigma/\tau}.
$$
Indeed a basis of $N_\tau$ followed by the primitive lift is a basis of
$N_\sigma$; parallelotope volume is base covolume times height.
Consequently $C(\sigma)=a_\sigma c(\sigma)$ is Euclidean balanced exactly
when $c$ satisfies lattice balancing.

Extend $f_\tau$ to a linear form $\ell$ in the ambient space. Subtract
$\ell$ in (1). Tangential contributions vanish and Euclidean
balancing cancels the remaining contribution of $\ell$. Thus BBGS's
product $B$, with its negative sign, satisfies
$$
 B_{-f}(ac)(\tau)
 =\sum_{\sigma\succ\tau}a_\sigma c(\sigma)f_\sigma(\nu_{\sigma/\tau})
 =a_\tau D_f c(\tau).
$$
To fit BBGS's hyperplane convention, embed $x$ as $(x,1)$ in
$N_{\mathbb{R}}\oplus{\mathbb{R}}$, with the product metric; every relevant tangent vector
has last coordinate zero. This leaves conormals and covolumes unchanged.

For completeness, the elementary proof content imported from BBGS is as
follows. Under subdivision, a new facet inside an old affine cell has
two opposite unit-normal contributions of equal weight, hence zero.
A subdivided old facet keeps its weight and conormal. The zero-weight
cases in higher-dimensional old cells complete the proof of Proposition
3.12. In a codimension-two quotient of a single top cell there are exactly
two boundary facets. If their inward unit directions are $v_1,v_2$,
reflection in their angle bisector exchanges them and also exchanges their
inward perpendicular unit directions. Hence expansions of those two
perpendiculars have the same two coefficients with the roles of $v_1,v_2$
interchanged. Expanding the iterated product and grouping the two
facet terms pairs identical cross terms; the two functions can be
interchanged. This is the entire commutativity mechanism in Proposition
3.15, valid also for a non-simplicial cell since its two-dimensional
codimension-two cone has two boundary rays. Linear functions annihilate
a weight exactly when its conormal sum is zero, as proved in Lemma 3.18
by pairing that sum with all linear forms. Commutativity then implies
that intersection with a PA function preserves this property; subdivision
does so by Proposition 3.12. These are precisely Proposition 3.19's
balancing and subdivision conclusions.

Equation (4) transfers all these conclusions to the primitive
lattice product, step by step, including real affine coefficients.
Tangential lift independence follows directly by replacing $n$ by
$n+t$ in (1): the added terms cancel because the two linear
parts agree on $N_\tau$.
The reconstructed local-support lemma applied to each intermediate nonnegative balanced
cycle shows positivity. Thus $\operatorname{MA}_{\mathrm{poly},*}(f)$ is a genuine, nonnegative,
finite, refinement-independent raw measure for every finite PA PC $f$
used below. At every step the carrying structure and its saturated
lattices are specified; arbitrary analytic multiplicities or ambient
Alexandrov mass are never substituted.

## The finite local slope cone


**Lemma 1 (Local supports imply global PCC inequalities).**

On the present embedded complex, a continuous function with an ambient
affine local support at every point satisfies every real-endpoint PCC.
For a PA function these supports make $D_f c$ nonnegative for every
nonnegative balanced cycle $c$ on a common carrying structure.


**Proof.** 
Restrict to any segment contained in $X$ and subtract its endpoint
chord. If the continuous difference has a positive maximum, its maximum
set lies in the open segment and is nonempty and closed. At a maximum
point, a supporting affine function must have zero segment slope:
otherwise it would exceed the maximum on one side. The support then
makes the maximum set open. Connectedness contradicts the zero endpoint
values. Thus the restriction lies below every chord and is convex.
At a PCC center $x$, the segment to each endpoint $x_i$ lies in its
incident convex cell. If $\ell$ is the linear part of a local support
at $x$, comparison at $x+t(x_i-x)$ with the segment's endpoint
chord gives $f(x_i)\geq f(x)+\ell(x_i-x)$. Sum the endpoint
inequalities with their coefficients; the barycenter cancels the
linear terms. For the divisor, a support at a relative interior point
of $\tau$ agrees with $f_\tau$ on its tangent space. Subtract that
support in (1); balancing cancels its tangent correction,
and each remaining inward slope is nonnegative. Every application
to a divisor uses PA $f$ and a common carrying structure.


Fix a rational point $p\in\operatorname{relint}(\tau)$ of a carrying structure for a
PA function $f$. Let $C_{\sigma/\tau}$ be its tangent cones, including
the common lineality $N_{\tau,{\mathbb{R}}}$, and choose finite nonzero rational
generators $d_1,\ldots,d_m$ of their union. Include a rational basis and
its negatives for lineality. A generator has an incident-cone assignment;
duplicate directions have consistent values because $f$ is continuous.
On each cone write the affine germ as
$$
 f(p+x)=f(p)+h_p(x).
$$
The continuous homogeneous function $h_p$ is linear on each cone.
Put $s_i=h_p(d_i)$, $U=(d_1\ \cdots\ d_m)$, and
$$
 K(U)=\{\lambda\in{\mathbb{R}}_{\geq0}^m:U\lambda=0\}.
$$
At a vertex no tangent quotient is taken. This matters: flat two-sided
directions at a singular vertex must remain in the test.


**Lemma 2 (Finite supports).**

A continuous finite PA function is PC if and only if, at every face
germ, there is an ambient linear form $\ell_p$ with
$$
 \ell_p(d_i)\leq s_i\quad(1\leq i\leq m).
$$
Equivalently $s\cdot\lambda\geq0$ for all $\lambda\in K(U)$.
These conditions give finitely many rational linear inequalities in the
affine coefficients on any specified finite rational structure. No
simplicial or matroid hypothesis is needed.


**Proof.** 
For a PC PA function, R230 gives all real-endpoint inequalities (its
continuous completion is itself). Given $\lambda\in K(U)$, use the
endpoints $p+\varepsilon d_i$ with common sufficiently small positive
$\varepsilon$, in their assigned incident cells. Normalize the nonzero
coefficients by $\sum\lambda_i$. Their center is $p$, and Jensen gives
$\sum\lambda_i s_i\geq0$. At a rational $p$ these endpoints can instead
be chosen rational, so even this local invocation respects the printed
definition directly.

Here is the finite duality argument, without an ungranted Farkas theorem.
The cone
$$
 T={\mathbb{R}}_{\geq0}^m+\operatorname{image}(U^\mathsf{T})
$$
is finitely generated: use the coordinate vectors and both signs of a
basis of the image. A finitely generated cone is closed. To see this,
eliminate dependent active columns in a nonnegative representation by
subtracting a signed dependency until one coefficient vanishes. The
remaining columns are independent. On each of finitely many independent
subsets, the inverse column map bounds the coefficients by a constant
times the represented vector's norm. A converging sequence thus has a
subsequence with convergent coefficients on one fixed subset.
If $s\notin T$, let $z$ be its nearest point in $T$. Squared-distance
minimization gives $\lambda=z-s$ nonnegative on $T$, with
$\lambda\cdot z=0$ and
$\lambda\cdot s=-\|z-s\|^2<0$. Pairing with the coordinate generators
and the image subspace shows $\lambda\geq0$ and $U\lambda=0$, a
contradiction. Therefore $s=b+U^\mathsf{T}\ell_p$ with $b\geq0$.
The reverse implication follows by pairing this identity with $K(U)$.

Linearity on each cone extends the generator inequalities to the entire
cone, giving an affine local support at $p$. The same test at a
rational representative of a face works throughout its relative interior:
the tangent cones and linear parts are unchanged. Thus these are supports
at every real point. Lemma 1 proves every
PCC inequality globally, giving sufficiency without identifying PC with
globally ambient convex functions.

Finally $K(U)$ is a rational polyhedral cone. Its extremal generators
have minimally dependent positive supports, with one-dimensional kernel
on each support. Such supports have at most
$\operatorname{rank}(U)+1$ elements. Gaussian elimination gives rational
generators, and there are finitely many subsets to inspect. These
generators span $K(U)$, by the same finite cone geometry used in R230.
Testing them gives the asserted finite rational inequalities.



At a vertex $v$, call a nonzero $\lambda\in K(U)$ with
$s\cdot\lambda=0$ a *flat relation*. This means equality in a
nontrivial local PCC, not zero raw mass. It does not depend on the chosen
finite generating list: any local directions can be resolved inside
their assigned cones into generators and conversely generator relations
are local PCCs.


**Lemma 3 (Strict affine floor).**

At a vertex, absence of flat relations is equivalent to existence of an
ambient linear form $\ell$ with
$$
 h_v(x)-\ell(x)>0\quad
       \text{for every nonzero }x\text{ in the tangent support}.
$$
In that case $h_v(x)-\ell(x)\geq c\|x\|$ there for some $c>0$.


**Proof.** 
By B225 the generator cone of the positive balanced star is its span,
so $K(U)\cap\{\sum\lambda_i=1\}$ is nonempty and compact.
If there is no flat relation, the minimum of $s\cdot\lambda$ on this
section is a positive number $\theta$. Choose $0<\delta<\theta$.
Then $s-\delta{\bf1}$ pairs nonnegatively with every element of $K(U)$.
The separation argument in Lemma 2 supplies $\ell$ with
$s_i-\ell(d_i)\geq\delta$ for every generator.
On each cone a nonzero vector has a nonnegative generator
representation, so its residual is strictly positive. The union of the
finitely many cone sections on the unit sphere is compact; the continuous
residual has positive minimum $c$. Conversely any such strict residual
pairs positively with every nonzero element of $K(U)$, excluding a flat
relation. Common lineality is handled by its two opposite generators;
a linear germ on it automatically has a flat relation.



## A necessary local contact condition


**Theorem 4 (Noncontact forces a flat relation).**

Let $\gamma$ be a continuous PC reference, $u$ bounded continuous,
and suppose the actual envelope $P_\gamma(u)=f$ is finite PA.
If $f(v)<\gamma(v)+u(v)$ at a vertex of a rational carrying structure
for $f$, its germ at $v$ has a flat relation.
This assertion makes no measure or approximation assumption.


**Proof.** 
Suppose there is no flat relation. Apply Lemma 3. In a
sufficiently small ambient ball about $v$, the space is exactly its
truncated tangent star and $f(v+x)=f(v)+h_v(x)$. Shrink its radius
$r>0$ so that the continuous obstacle gap is greater than some
$\eta>0$ throughout its intersection with $X$.
For $0<t<\min(\eta,cr/2)$, define in this ball
$$
 F(v+x)=\max\{f(v+x),\,f(v)+t+\ell(x)\},
$$
and put $F=f$ outside it. Since $h_v-\ell\geq c\|x\|$, these
definitions agree on the collar $r/2<\|x\|<r$. Also
$0\leq F-f\leq t$, so $F$ is continuous, lies below the obstacle,
and has the same growth upper bound as $f$.

At an interior point of the modified region where the affine floor is
active, that floor is a local support. Where $f$ is active, a local
support of $f$ from Lemma 2 remains a support of $F$.
This also covers tie points, and the collar is unchanged. Lemma
1 therefore proves $F\in\operatorname{PC}_q(X)$.
It is an actual competitor in (2), with $F(v)=f(v)+t$,
contradicting maximality.
The inserted floor need not be PA on a rational structure; competitors
in (2) are not restricted to PA. No operator is assigned to it.



In particular a finite PA endpoint can have positive noncontact raw mass
only on the boundary of the local slope cone specified by a flat
relation. The theorem is not a claim that every such boundary point
is globally growth-compatible.

## Global realization of every compatible PA obstruction


**Theorem 5 (Exact bounded roof obstruction).**

Fix a PA PC reference $\gamma$ in either category $*={\mathbb{Z}},{\mathbb{R}}$.
Let $f\in\operatorname{PAPC}_*(X)$ satisfy $f-\gamma\in\operatorname{PA}_{*,b}(X)$.
Suppose a vertex $v$ has a flat relation and genuine raw mass
$m_v=(D_f^d[X])(v)>0$.
There is an explicitly constructed $u\in\operatorname{PA}_{*,b}(X)$ such that
$$
 P_\gamma(u)=f\in\operatorname{PC}^{\rm reg}_*(X,\gamma),\qquad
 \int_X(f-(\gamma+u))\operatorname{MA}_{\mathrm{poly},*}(f)=-R m_v<0
$$
for a positive rational $R$. In particular the pair cannot have both
all-obstacle endpoint regularity and orthogonality in that category.


**Proof.** 
Choose a lattice basis and the rational polyhedral norm
$\rho(x)=\max_j|x_j|$ in its coordinates. Choose rational $R>0$
so small that the closed norm ball about $v$ meets only cells incident
to $v$, the entire restriction of $f$ in that ball is its linear
germ on each incident cell, and the ball contains no other vertex of
a chosen common finite carrying structure for $f,\gamma,[X]$.
These choices are possible by finiteness and the rational vertex $v$.
Put
$$
 B_R(x)=(R-\rho(x-v))_+,\qquad
 u=f-\gamma+B_R,\qquad a=\gamma+u=f+B_R.
$$
The roof is continuous literal PA on a finite rational hyperplane
subdivision, has integral slopes and rational constants, and vanishes
outside that ball. Thus $u$ is admissible in the asserted category.
The function $f$ is a competitor with the actual reference growth.

Write the flat relation as
$\sum_i\lambda_i d_i=0$, $\lambda_i\geq0$, and
$\sum_i\lambda_i h_v(d_i)=0$, discarding zero coefficients.
The rational points
$$
 y_i=v+\frac{R}{\rho(d_i)}d_i
$$
lie in their assigned incident cells and on the roof boundary. Set
$\beta_i=\lambda_i\rho(d_i)/R$.
Then
$$
 \sum_i\beta_i(y_i-v)=0,\qquad
 \sum_i\beta_i(f(y_i)-f(v))=0.
$$
After normalization this is a printed rational-endpoint PCC at $v$
whose endpoint obstacle values equal $f(y_i)$.
Every competitor $q$ therefore satisfies $q(v)\leq f(v)$.

For rational $x$ with $0<\rho(x-v)<R$, put
$y=v+R(x-v)/\rho(x-v)$.
This is a rational point of the same incident cell, on the roof
boundary. The segment from $v$ to $y$ is in that cell. Jensen
and the affinity of $f$ give $q(x)\leq f(x)$.
Outside the ball the direct obstacle bound already gives $q\leq f$.
These bounds hold for every rational point and also at $v$.
For a real point, use successively smaller rational simplices in its
relative rational face containing it. Their rational vertices have
the preceding bound; Jensen and continuity of $f$ imply $q(x)\leq f(x)$.
Thus maximality over every printed-PC competitor, including discontinuous
ones, proves $P_\gamma(u)=f$. Its upper semicontinuous regularization is
the same continuous function.

The measured endpoint is already PA PC and relative; its constant
decreasing regularization is valid. Refinement independence proved
above ensures that new roof-subdivision vertices contribute no new
atoms to $\operatorname{MA}_{\mathrm{poly},*}(f)$. The only original atom in the roof support
is $v$, where the gap is $-R$. All others have gap zero. Hence
the integral is exactly $-R m_v$. This proof checks the genuine
operator domain rather than declaring a measure of a continuous hull.



This theorem needs global compatibility of $f$, which is the explicitly
stated bounded-difference condition with the *actual* reference.
It does not assert that every abstract bad local germ can be extended
through the remaining complex. Positive growth alone is not used to
replace that condition.


**Corollary 6 (Exact finite-PA-endpoint characterization).**

For a fixed pair and fixed coefficient category, the following are
equivalent:

1.  Every admissible PA obstacle whose actual envelope belongs to
$\operatorname{PAPC}_*(X,\gamma)$ has zero raw contact integral.
1.  Every $f\in\operatorname{PAPC}_*(X,\gamma)$, at every vertex of a rational
carrying structure, satisfies: $m_v(f)>0$ implies absence of a flat
relation.

The second condition contains neither an obstacle nor a contact integral.
This is a classification of the finite PA endpoint sector, not original
P05.2 with all regularizable endpoints.


**Proof.** 
If (2) holds, the finitely many positive atoms of a PA envelope are
contact points by Theorem 4; every term in its atomic
contact integral vanishes. Conversely a violation of (2) gives the
admissible obstacle and negative integral in Theorem 5,
whose endpoint is in the stated PA category.



## A finite algebraic test with actual global growth

Fix a finite rational carrying structure $\Pi$ for $\gamma,[X]$.
Parameterize affine linear parts and constants of $f$ on its cells by
coefficients $z$. Equality of the affine restrictions on shared faces
is a finite rational linear system: test a rational affine basis of each
face. Lemma 2 at every face gives a finite system
$Az\geq0$.
For each generator $r$ of $\operatorname{rec}(\sigma)$, impose
$$
 (f_\sigma-\gamma_\sigma)(r)=0.
$$
These are exactly bounded difference on the whole complex.
Necessity follows along the rays $x+tr$; sufficiency follows by
writing a rational polyhedron as a bounded convex hull plus its
finitely generated recession cone. For cells with lineality use both
signs of a basis. If desired, an ambient rational coordinate
hyperplane arrangement splits every cell into pointed cells, leaving
only finitely many vertices and recession rays. Rational finite
generation and this decomposition follow from the elementary
cone-section argument in R230: remove rational lineality, take a
strictly positive rational section of the pointed cone, and obtain
finitely many rational vertices by successive active-constraint
elimination. Applying it to the homogenized cell gives the claimed
vertex-plus-recession decomposition.

On a specified structure, recursive formula (1) makes
$m_v(z)$ a homogeneous degree-$d$ polynomial in the linear parts,
with the actual top weights and primitive saturated normals as
coefficients. Let $\kappa_{v,j}$ be the finitely many normalized
extreme relations at $v$, and $s_v(z)$ its generator slope vector.
The existence of a bad relative $\operatorname{PA}_{\mathbb{R}}$ function *carried by
this structure* is exactly the finite disjunction of systems
$$
 \text{shared-face equations},\quad Az\geq0,\quad
 (6),\quad
 s_v(z)\cdot\kappa_{v,j}=0,\quad m_v(z)>0.
$$
A flat relation has zero cost on some extreme relation because all
extreme costs are nonnegative. Thus (7) is an actual
semialgebraic obstruction test, not total mass or orthogonality
renamed. A feasible point gives a global certificate and the roof
obstacle. In the literal category impose integral coordinates of
each tangent linear part in a saturated lattice basis and rational
affine constants as well. A real feasible point is not automatically
a literal one.

Nonsimplicial stars use all their generators and shared-face equations;
no replacement by an ambient strong-convexity cone occurs.
Nonsaturated input directions must first be replaced by the saturated
tangent lattice normals in (1); the relation cone alone does
not encode their intersection indices. Genuine common lineality has
a linear restriction of the germ and hence flat opposite generators.
If a germ is invariant modulo an affine function along nonzero common
lineality, its raw top atom is zero: on the generalized carrying fan
every face contains that lineality, so there are no zero-dimensional
faces. Refinement independence keeps that zero result if artificial
cuts create a vertex.

Testing one structure is not testing all rational refinements, and even
testing all structures only gives Corollary 6's finite-PA
sector. No bound on the structures needed for arbitrary envelopes is
proved here.

## A fully realized two-dimensional certificate

In $N={\mathbb{Z}}^3$, let
$$
 X=\{y=0\}\cup\{x=0\},\qquad
 \gamma(x,y,z)=|x|+|y|+|z|\quad\hbox{on }X.
$$
The eight coordinate quadrants of the two planes have weight one.
Each plane is saturated and unimodular. At an $x$ or $y$ axis
the two transverse inward normals are $e_z,-e_z$; at the shared
$z$ axis they are $e_x,-e_x,e_y,-e_y$. Their sums are zero,
so this is a positive balanced two-cycle. The reference is literal
PA, PC as the restriction of an ambient convex norm, and positive
in every nonzero recession direction.

Define on all of $X$
$$
 f=\max\{|x|,|y|-1,0\}+|z|.
$$
It is an ambient convex restriction and literal PA on a finite
rational subdivision at $y=\pm1$, $z=0$, and the coordinate axes.
On the horizontal plane $f=|x|+|z|$; on the vertical plane
$f=(|y|-1)_++|z|$. Thus $f-\gamma$ is bounded between $-1$
and zero and is literal PA. Near the origin its slopes on
$(e_x,-e_x,e_y,-e_y,e_z,-e_z)$ are
$(1,1,0,0,1,1)$. The pair $e_y,-e_y$ gives a flat relation.

For arbitrary six local slopes, write
$$
 A=s_{x+}+s_{x-},\quad B=s_{y+}+s_{y-},\quad
 C=s_{z+}+s_{z-}.
$$
The relation cone has exactly the three opposing-pair extreme relations.
The local PC cone is $A,B,C\geq0$. The first raw divisor weights
on $x^\pm,y^\pm,z^\pm$ are, respectively, $C,C,A+B$.
The second mass is therefore
$$
 m_0=2C(A+B).
$$
For $f$, this gives $A=2,B=0,C=2$ and $m_0=8$.
This polynomial is positive on a flat boundary face of the local PC
cone; the global $f$ above verifies actual growth compatibility.

The complete first intersection cycle has weight two on the whole
$x,y,z$ axes and weight one on each of the two vertical lines
$\{(0,1,z)\}$, $\{(0,-1,z)\}$. Opposite primitive directions at
every vertex balance. At each point $p_\pm=(0,\pm1,0)$, the two
$y$-direction weights are two and the two $z$-direction weights
are one. The outgoing slopes are zero toward the origin, one away
from it, and one in each $z$ direction. Thus each second mass is
$2\cdot0+2\cdot1+1+1=4$. There are no other atoms:
$$
 \operatorname{MA}_{\mathrm{poly}}(f)=8\delta_0+4\delta_{p_+}+4\delta_{p_-}.
$$
For the reference, $A=B=C=2$ and its sole atom has mass $16$.
Both totals are $16$, without implying contact.

Choose $R=1/4$, $\rho=\max(|x|,|y|,|z|)$, and the literal,
bounded, nonseparable obstacle
$$
 u=f-\gamma+(1/4-\rho)_+.
$$
Theorem 5 gives the exact unrestricted envelope
$P_\gamma(u)=f$, a genuine literal and real regularizable PA endpoint.
Only the origin lies inside the roof support. Consequently
$$
 \int_X(f-(\gamma+u))\operatorname{MA}_{\mathrm{poly}}(f)=-\tfrac14\cdot8=-2.
$$
This is not the withdrawn product ansatz229: the roof, endpoint,
separating upper bound and all raw masses are different and proved
above. Pair-level regularity for all other obstacles is not asserted.

## Why finite jet presentation does not finish regularization

Lemma 2 does give a finite linear feasibility system for
PC affine coefficients on a *specified* structure. Together with
shared-face, obstacle, and growth constraints it gives valid finite
PA trial competitors. It does not prove that this structure carries
the unrestricted envelope, that a finite number of hull iterations
suffices, or that all structures have a uniform approximation theorem.
R230 supplies continuity but none of those conclusions.

There is also a precise coefficient obstruction to treating the
real rational-structure category as closed under taking maxima.
On ${\mathbb{R}}$, put $\alpha=\sqrt2-1$ and
$$
 f_1=|x|,\quad f_2=|x-1|+\alpha,\quad
 t=(1+\alpha)/2=\sqrt2/2.
$$
Both $f_i$ are real PA on rational structures, PC, and differ
boundedly from $|x|$. Yet
$$
 \max(f_1,f_2)=\max(x,2t-x)=|x-t|+t
$$
has its unique kink at the irrational point $t$, so no finite rational
structure on ${\mathbb{R}}$ carries it. This is *not* a nonregularizability
example: rational $t_n\downarrow t$ give literal PA PC functions
$$
 H_n=\max(x,2t_n-x)\downarrow \max(f_1,f_2),\qquad
 \|H_n-\max(f_1,f_2)\|_\infty=2(t_n-t).
$$
Thus a finite maximum argument needs its own rational-structure and
approximation audit; the failure of PA closure alone proves no
endpoint regularization failure.

The original residual requirements remain: determine real regularization
for arbitrary nonseparable obstacles; obtain a genuine extended operator
at all such endpoints; characterize the compatible global realizations
of every bad local germ; and prove necessity and sufficiency of a
geometric contact condition for all regularizable endpoints, including
non-PA limits. The literal category has its separate antecedents and
arithmetic constraints. A224's accepted fan obstruction and the
dossier's existing cases do not supply these missing theorems.
The present algebraic characterization is intentionally restricted to
finite PA endpoints and does not close the entire unchanged original.

## Evidence, audit, and reproducibility

The standard-library program `check_certificates.py` computes
positive circuit rays by exact rational Gaussian elimination, checks
the two-plane fan's primitive normals, first-cycle balance, symbolic
mass polynomial, and the full three-atom calculation. It also verifies
the generated obstacle bounds on specified finite rational grids and
the scaled flat-relation PCCs. These are exhaustive finite checks only
for their listed inputs, not proofs of the continuum envelope; the
proofs above supply that assertion independently. The program also
checks the literal decreasing approximations of the irrational-kink
maximum using certified rational brackets for $\sqrt2/2$.

Rerun with:

```text

python prepare_inputs.py
python check_certificates.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
```

Actual commands, output, environment details and hashes are retained
in `execution-commands.md` and `evidence/`.
The entire argument is also retained in `argument.md`;
structured notes are in `notes.json`. Execution and compilation
do not verify mathematics.
No installations, authentication changes, network-setting changes,
private streams, other campaigns, or protected-editor operations were
used. No resource-heavy work was run. No operator-provided supervised
compute service was exposed; these small exact checks needed none.
The requested model route was not independently selectable or verified
by an exposed runtime tool, so no model change is claimed.

The quote-free `source-application-ledger.md` records the exact
primary paths, URLs, versions, complete essential proof units, hypothesis
checks, and actual applications. All four frozen primary SHA-256 hashes
matched the supplied values. Original PDF pages were rendered locally
to resolve extraction glyphs in the endpoint, normal, product and
commutativity formulas. No source theorem flag is treated as a
mathematical grant. In particular BMPS's automatic-continuity sentence,
Theorem 6.4's full-PC density equivalence, and general operator extension
are not applications. BBGS's real-endpoint continuity theorem and
difference-of-concave result are not approximation grants.

## References


- **BMPS.** A. M. Botero, E. Mazzon, L. Pille--Schneider,
*Monge--Ampere measures on balanced polyhedral spaces*,
arXiv:2603.08664v1, submitted 9 March 2026, manuscript 10 March 2026.
https://arxiv.org/pdf/2603.08664v1.

- **BBGS.** A. M. Botero, J. I. Burgos Gil, M. Sombra,
*Convex analysis on polyhedral spaces*, Math. Z. 301 (2022),
1631--1674, publisher version, 24 January 2022.
https://link.springer.com/content/pdf/10.1007/s00209-021-02869-6.pdf.

- **A224.** Supplied accepted caller paper A224,
*A strict-growth contact obstruction on the $U_{3,4*$ Bergman fan},
complete body and harmless clarifications retained locally.

- **B225.** Supplied accepted caller paper B225,
*Positive balancing, compact support, and a polyhedral maximum
principle*, complete body and harmless clarifications retained locally.

- **R230.** Supplied accepted caller paper R230,
*Continuous completion of rational-endpoint polyhedral convexity*,
complete body and harmless clarifications retained locally.
