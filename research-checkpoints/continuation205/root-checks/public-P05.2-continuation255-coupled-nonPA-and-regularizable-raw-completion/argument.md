---
abstract: |
  We explicitly repair the failed whole247 strict-floor lemma by adding
  the PA PC hypothesis, and replace its separable example. On two
  saturated coordinate planes meeting along a line, a genuinely coupled
  literal PA reference and endpoint give raw masses $12,6,6$ and contact
  integral $-3$. The unrestricted envelope proof includes discontinuous
  printed-PC competitors. We reconstruct the finite-PA contact/circuit
  criterion and then prove a sequence-independent uniform extension of
  the raw mixed operator on the regularizable domain for rational-affine
  positive-growth references. A genuinely non-PA real-regularizable
  endpoint has an explicitly computed measure on line segments and
  parabolic arcs, with the same negative contact integral. We also
  reconstruct the noncompact literal regularity obstruction. These are
  scoped theorems, not the entire necessary-and-sufficient
  classification for all real references and all continuous obstacles.
  The original P05.2 remains open; candidate status is false.
author:
- Research draft
date: 7 October 2026
title: |
  Repaired finite contact certificates and a coupled non-PA
  obstruction  
  Scoped progress on the unchanged original P05.2
---

# Retained target, conventions, and grants

The unchanged target is necessary and sufficient geometric conditions
for the actual balanced rational pair $(X,\gamma)$, including every
admissible obstacle, genuine envelope regularization and operator
antecedents, and
$$\int_X\bigl(P_\gamma(u)-(\gamma+u)\bigr)\operatorname{MA}_{\mathrm{poly}}(P_\gamma(u))=0.$$
The complete supplied family dossier, completion criteria, and
assignment are retained in `input.json`; the task object is also in
`retained-task.json`. No dossier theorem is used as a grant. The only
mathematical grants are the complete accepted caller papers A224, B225,
R230 and their supplied source-preserving clarifications. Their complete
bodies and clarifications are retained under `caller-grants/`.

Throughout, $X\subset N_\mathbb R$ is the support of a finite rational
complex, pure of dimension $d\geq1$, with strictly positive balanced top
weights $w_\sigma$. Rational weights are the literal BMPS setting; the
finite real-linear calculations also allow specified positive real
weights. For translated cells the saturated tangent lattice is
$$N_\sigma=N\cap\operatorname{span}_\mathbb R(\sigma-\sigma).$$ An
inward normal $n_{\sigma/\tau}$ represents the primitive generator of
$N_\sigma/N_\tau$ pointing into $\sigma$. The raw divisor is
$$\label{raw}
 D_f c(\tau)=\sum_{\sigma\succ\tau}c(\sigma)f_\sigma(n_{\sigma/\tau})
 -f_\tau\left(\sum_{\sigma\succ\tau}c(\sigma)n_{\sigma/\tau}\right).$$
Linear parts, rather than affine values, occur in this formula. A convex
bend has positive sign. We use the finite recursive measure
$$\operatorname{MA}_{\mathrm{poly},*}(f)=\sum_{v\in\Pi(0)}(D_f^d[X])(v)\delta_v,\qquad *=\mathbb Z,\mathbb R.$$
There is no additional factorial in this recursion. In the literal
category this is BMPS Definition 4.4. In the real category it denotes
the explicitly verified real-linear finite-PA extension of the same
formula, not an operator on every continuous PC function.

The class $\operatorname{PA}_\mathbb Z$ has integral tangent linear
parts and rational constants; $\operatorname{PA}_\mathbb R$ has
arbitrary real affine coefficients on a finite *rational* carrying
complex. Both classes are continuous. Set
$\operatorname{PAPC}_*=\operatorname{PA}_*\cap\operatorname{PC}_q$,
where $\operatorname{PC}_q$ is the printed rational-endpoint PCC class.
A PCC has a common center face contained as a face in each endpoint
cell. Competitors in $$\label{env}
 P_\gamma(u)=\sup\{q\in\operatorname{PC}_q:q\leq\gamma+u,\ q\leq\gamma+O(1)\}$$
are not restricted to either PA coefficient category. Regularizable
means a uniform decreasing limit of relative $\operatorname{PAPC}_*$
functions. Each PA endpoint measured here has a constant regularizing
sequence; decreasing positive rational constant additions also work. No
measure is assigned merely from continuity.
Section <a href="#extension-section" data-reference-type="ref"
data-reference="extension-section">10</a> constructs an extension on an
explicitly proved approximation domain.

The old source and its FAIL verdict are preserved in `preserved/`. The
repair is material: the strict-floor lemma below explicitly assumes a PA
PC germ, or equivalently nonnegative cost on every positive tangent
relation. On the unit balanced line the relative literal function
$f=-|x|$ for $|x|\leq1$ and $f=|x|-2$ elsewhere, with $\gamma=|x|$, has
slopes $(-1,-1)$ at zero. Its positive relations are $(a,a)$; every
nonzero cost is $-2a$, so it has no zero-cost relation. A floor $bx$
would require simultaneously $b<-1$ and $b>1$. The old unconditional
lemma is false. Positive spanning alone does not repair it.

The old endpoint $\max(|x|,|y|-1,0)+|z|$ was $F(q)+|z|$ on the
cross-times-line product. Its obstacle was nonseparable, but its
endpoint was separable. Our new reference and endpoint below are
different functions; we do not relabel the old example. Independent196
and ROOT249 are unreviewed data, not additional grants. Native194’s
unknown-support failure is retained; caller labels are explained in text
and are never local-note supports.

R230 gives the continuous dominating completion of every finite
printed-PC competitor on this domain, preserving continuous obstacles
and its actual growth upper bound. It identifies
<a href="#env" data-reference-type="eqref"
data-reference="env">[env]</a> with the continuous-competitor envelope
for every bounded continuous obstacle. We use this theorem without
reproving it. B225 gives positive spanning of every positive balanced
star. A224’s local-support argument motivates a lemma that we
reconstruct below on the present general domain. We do not promote its
fan-specific main theorem to a theorem on arbitrary spaces. All actual
grant applications retain their stated hypotheses.

We make no use of a strict-convexity theorem. Our zero-cost tests
discard zero-coefficient terms. The printed BMPS strictness wording
counts endpoint indices even though coefficients may be zero; that
separate degeneracy is not repaired or used here. A224’s strictness
claim has its disclosed active-coefficient convention.

# Genuine finite raw intersections and source conversion

We audit the complete elementary proof units BBGS Proposition 3.12,
Proposition 3.15, Lemma 3.18 and Proposition 3.19, in the fixed 2022
publisher version. Their definitions use inward Euclidean *unit*
conormals and the negative sign appropriate to concave functions. Here
is the conversion, including every weight factor needed in our
application. Choose an auxiliary Euclidean inner product, and let
$a_\sigma$ be the covolume of $N_\sigma$ in its tangent space, with
$a_v=1$. If $\nu_{\sigma/\tau}$ is the unit inward conormal, saturation
gives $$\label{height}
 \operatorname{pr}_{N_{\tau,\mathbb R}^{\perp}}n_{\sigma/\tau}
   =\frac{a_\sigma}{a_\tau}\nu_{\sigma/\tau}.$$ Indeed a basis of
$N_\tau$ followed by the primitive lift is a basis of $N_\sigma$;
parallelotope volume is base covolume times height. Consequently
$C(\sigma)=a_\sigma c(\sigma)$ is Euclidean balanced exactly when $c$
satisfies lattice balancing.

Extend $f_\tau$ to a linear form $\ell$ in the ambient space. Subtract
$\ell$ in <a href="#raw" data-reference-type="eqref"
data-reference="raw">[raw]</a>. Tangential contributions vanish and
Euclidean balancing cancels the remaining contribution of $\ell$. Thus
BBGS’s product $B$, with its negative sign, satisfies $$\label{convert}
 B_{-f}(ac)(\tau)
 =\sum_{\sigma\succ\tau}a_\sigma c(\sigma)f_\sigma(\nu_{\sigma/\tau})
 =a_\tau D_f c(\tau).$$ To fit BBGS’s hyperplane convention, embed $x$
as $(x,1)$ in $N_\mathbb R\oplus\mathbb R$, with the product metric;
every relevant tangent vector has last coordinate zero. This leaves
conormals and covolumes unchanged.

For completeness, the elementary proof content imported from BBGS is as
follows. Under subdivision, a new facet inside an old affine cell has
two opposite unit-normal contributions of equal weight, hence zero. A
subdivided old facet keeps its weight and conormal. The zero-weight
cases in higher-dimensional old cells complete the proof of Proposition
3.12. In a codimension-two quotient of a single top cell there are
exactly two boundary facets. If their inward unit directions are
$v_1,v_2$, reflection in their angle bisector exchanges them and also
exchanges their inward perpendicular unit directions. Hence expansions
of those two perpendiculars have the same two coefficients with the
roles of $v_1,v_2$ interchanged. Expanding the iterated product and
grouping the two facet terms pairs identical cross terms; the two
functions can be interchanged. This is the entire commutativity
mechanism in Proposition 3.15, valid also for a non-simplicial cell
since its two-dimensional codimension-two cone has two boundary rays.
Linear functions annihilate a weight exactly when its conormal sum is
zero, as proved in Lemma 3.18 by pairing that sum with all linear forms.
Commutativity then implies that intersection with a PA function
preserves this property; subdivision does so by Proposition 3.12. These
are precisely Proposition 3.19’s balancing and subdivision conclusions.

Equation <a href="#convert" data-reference-type="eqref"
data-reference="convert">[convert]</a> transfers all these conclusions
to the primitive lattice product, step by step, including real affine
coefficients. Tangential lift independence follows directly by replacing
$n$ by $n+t$ in <a href="#raw" data-reference-type="eqref"
data-reference="raw">[raw]</a>: the added terms cancel because the two
linear parts agree on $N_\tau$. The reconstructed local-support lemma
applied to each intermediate nonnegative balanced cycle shows
positivity. Thus $\operatorname{MA}_{\mathrm{poly},*}(f)$ is a genuine,
nonnegative, finite, refinement-independent raw measure for every finite
PA PC $f$ used below. At every step the carrying structure and its
saturated lattices are specified; arbitrary analytic multiplicities or
ambient Alexandrov mass are never substituted.

# The finite local slope cone

<div id="localglobal" class="lemma">

**Lemma 1** (Local supports imply global PCC inequalities). *On the
present embedded complex, a continuous function with an ambient affine
local support at every point satisfies every real-endpoint PCC. For a PA
function these supports make $D_f c$ nonnegative for every nonnegative
balanced cycle $c$ on a common carrying structure.*

</div>

<div class="proof">

*Proof.* Restrict to any segment contained in $X$ and subtract its
endpoint chord. If the continuous difference has a positive maximum, its
maximum set lies in the open segment and is nonempty and closed. At a
maximum point, a supporting affine function must have zero segment
slope: otherwise it would exceed the maximum on one side. The support
then makes the maximum set open. Connectedness contradicts the zero
endpoint values. Thus the restriction lies below every chord and is
convex. At a PCC center $x$, the segment to each endpoint $x_i$ lies in
its incident convex cell. If $\ell$ is the linear part of a local
support at $x$, comparison at $x+t(x_i-x)$ with the segment’s endpoint
chord gives $f(x_i)\geq f(x)+\ell(x_i-x)$. Sum the endpoint inequalities
with their coefficients; the barycenter cancels the linear terms. For
the divisor, a support at a relative interior point of $\tau$ agrees
with $f_\tau$ on its tangent space. Subtract that support in
<a href="#raw" data-reference-type="eqref"
data-reference="raw">[raw]</a>; balancing cancels its tangent
correction, and each remaining inward slope is nonnegative. Every
application to a divisor uses PA $f$ and a common carrying structure. ◻

</div>

Fix a rational point $p\in\operatorname{relint}(\tau)$ of a carrying
structure for a PA function $f$. Let $C_{\sigma/\tau}$ be its tangent
cones, including the common lineality $N_{\tau,\mathbb R}$, and choose
finite nonzero rational generators $d_1,\ldots,d_m$ of their union.
Include a rational basis and its negatives for lineality. A generator
has an incident-cone assignment; duplicate directions have consistent
values because $f$ is continuous. On each cone write the affine germ as
$$f(p+x)=f(p)+h_p(x).$$ The continuous homogeneous function $h_p$ is
linear on each cone. Put $s_i=h_p(d_i)$, $U=(d_1\ \cdots\ d_m)$, and
$$K(U)=\{\lambda\in\mathbb R_{\geq0}^m:U\lambda=0\}.$$ At a vertex no
tangent quotient is taken. This matters: flat two-sided directions at a
singular vertex must remain in the test.

<div id="supports" class="lemma">

**Lemma 2** (Finite supports). *A continuous finite PA function is PC if
and only if, at every face germ, there is an ambient linear form
$\ell_p$ with $$\ell_p(d_i)\leq s_i\quad(1\leq i\leq m).$$ Equivalently
$s\cdot\lambda\geq0$ for all $\lambda\in K(U)$. These conditions give
finitely many rational linear inequalities in the affine coefficients on
any specified finite rational structure. No simplicial or matroid
hypothesis is needed.*

</div>

<div class="proof">

*Proof.* For a PC PA function, R230 gives all real-endpoint inequalities
(its continuous completion is itself). Given $\lambda\in K(U)$, use the
endpoints $p+\varepsilon d_i$ with common sufficiently small positive
$\varepsilon$, in their assigned incident cells. Normalize the nonzero
coefficients by $\sum\lambda_i$. Their center is $p$, and Jensen gives
$\sum\lambda_i s_i\geq0$. At a rational $p$ these endpoints can instead
be chosen rational, so even this local invocation respects the printed
definition directly.

Here is the finite duality argument, without an ungranted Farkas
theorem. The cone
$$T=\mathbb R_{\geq0}^m+\operatorname{image}(U^\mathsf{T})$$ is finitely
generated: use the coordinate vectors and both signs of a basis of the
image. A finitely generated cone is closed. To see this, eliminate
dependent active columns in a nonnegative representation by subtracting
a signed dependency until one coefficient vanishes. The remaining
columns are independent. On each of finitely many independent subsets,
the inverse column map bounds the coefficients by a constant times the
represented vector’s norm. A converging sequence thus has a subsequence
with convergent coefficients on one fixed subset. If $s\notin T$, let
$z$ be its nearest point in $T$. Squared-distance minimization gives
$\lambda=z-s$ nonnegative on $T$, with $\lambda\cdot z=0$ and
$\lambda\cdot s=-\|z-s\|^2<0$. Pairing with the coordinate generators
and the image subspace shows $\lambda\geq0$ and $U\lambda=0$, a
contradiction. Therefore $s=b+U^\mathsf{T}\ell_p$ with $b\geq0$. The
reverse implication follows by pairing this identity with $K(U)$.

Linearity on each cone extends the generator inequalities to the entire
cone, giving an affine local support at $p$. The same test at a rational
representative of a face works throughout its relative interior: the
tangent cones and linear parts are unchanged. Thus these are supports at
every real point. Lemma <a href="#localglobal" data-reference-type="ref"
data-reference="localglobal">1</a> proves every PCC inequality globally,
giving sufficiency without identifying PC with globally ambient convex
functions.

Finally $K(U)$ is a rational polyhedral cone. Its extremal generators
have minimally dependent positive supports, with one-dimensional kernel
on each support. Such supports have at most $\operatorname{rank}(U)+1$
elements. Gaussian elimination gives rational generators, and there are
finitely many subsets to inspect. These generators span $K(U)$, by the
same finite cone geometry used in R230. Testing them gives the asserted
finite rational inequalities. ◻

</div>

At a vertex $v$, call a nonzero $\lambda\in K(U)$ with $s\cdot\lambda=0$
a *flat relation*. This means equality in a nontrivial local PCC, not
zero raw mass. It does not depend on the chosen finite generating list:
any local directions can be resolved inside their assigned cones into
generators and conversely generator relations are local PCCs.

<div id="floor" class="lemma">

**Lemma 3** (Strict affine floor). *Assume explicitly that the finite PA
germ at the vertex is PC, equivalently $s\cdot\lambda\geq0$ for every
$\lambda\in K(U)$. Under this hypothesis, absence of flat relations is
equivalent to existence of an ambient linear form $\ell$ with
$$h_v(x)-\ell(x)>0\quad
       \text{for every nonzero }x\text{ in the tangent support}.$$ In
that case $h_v(x)-\ell(x)\geq c\|x\|$ there for some $c>0$.*

</div>

<div class="proof">

*Proof.* By B225 the generator cone of the positive balanced star is its
span, so $K(U)\cap\{\sum\lambda_i=1\}$ is nonempty and compact. The PC
hypothesis makes every relation cost nonnegative. If there is no flat
relation, the minimum of $s\cdot\lambda$ on this section is a positive
number $\theta$. Choose $0<\delta<\theta$. Then $s-\delta{\bf1}$ pairs
nonnegatively with every element of $K(U)$. The separation argument in
Lemma <a href="#supports" data-reference-type="ref"
data-reference="supports">2</a> supplies $\ell$ with
$s_i-\ell(d_i)\geq\delta$ for every generator. On each cone a nonzero
vector has a nonnegative generator representation, so its residual is
strictly positive. The union of the finitely many cone sections on the
unit sphere is compact; the continuous residual has positive minimum
$c$. Conversely any such strict residual pairs positively with every
nonzero element of $K(U)$, excluding a flat relation. Common lineality
is handled by its two opposite generators; a linear germ on it
automatically has a flat relation. ◻

</div>

# A necessary local contact condition

<div id="necessary" class="theorem">

**Theorem 4** (Noncontact forces a flat relation). *Let $\gamma$ be a
continuous PC reference, $u$ bounded continuous, and suppose the actual
envelope $P_\gamma(u)=f$ is finite PA. If $f(v)<\gamma(v)+u(v)$ at a
vertex of a rational carrying structure for $f$, its germ at $v$ has a
flat relation. This assertion makes no measure or approximation
assumption.*

</div>

<div class="proof">

*Proof.* The finite envelope is PC: each competitor satisfies Jensen,
and taking the pointwise supremum preserves its inequality. Thus its PA
germ has nonnegative relation costs. Suppose there is no flat relation
and apply the corrected Lemma
<a href="#floor" data-reference-type="ref" data-reference="floor">3</a>
with this established hypothesis. In a sufficiently small ambient ball
about $v$, the space is exactly its truncated tangent star and
$f(v+x)=f(v)+h_v(x)$. Shrink its radius $r>0$ so that the continuous
obstacle gap is greater than some $\eta>0$ throughout its intersection
with $X$. For $0<t<\min(\eta,cr/2)$, define in this ball
$$F(v+x)=\max\{f(v+x),\,f(v)+t+\ell(x)\},$$ and put $F=f$ outside it.
Since $h_v-\ell\geq c\|x\|$, these definitions agree on the collar
$r/2<\|x\|<r$. Also $0\leq F-f\leq t$, so $F$ is continuous, lies below
the obstacle, and has the same growth upper bound as $f$.

At an interior point of the modified region where the affine floor is
active, that floor is a local support. Where $f$ is active, a local
support of $f$ from Lemma <a href="#supports" data-reference-type="ref"
data-reference="supports">2</a> remains a support of $F$. This also
covers tie points, and the collar is unchanged. Lemma
<a href="#localglobal" data-reference-type="ref"
data-reference="localglobal">1</a> therefore proves
$F\in\operatorname{PC}_q(X)$. It is an actual competitor in
<a href="#env" data-reference-type="eqref"
data-reference="env">[env]</a>, with $F(v)=f(v)+t$, contradicting
maximality. The inserted floor need not be PA on a rational structure;
competitors in <a href="#env" data-reference-type="eqref"
data-reference="env">[env]</a> are not restricted to PA. No operator is
assigned to it. ◻

</div>

In particular a finite PA endpoint can have positive noncontact raw mass
only on the boundary of the local slope cone specified by a flat
relation. The theorem is not a claim that every such boundary point is
globally growth-compatible.

# Global realization of every compatible PA obstruction

<div id="obstruction" class="theorem">

**Theorem 5** (Exact bounded roof obstruction). *Fix a PA PC reference
$\gamma$ in either category $*=\mathbb Z,\mathbb R$. Let
$f\in\operatorname{PAPC}_*(X)$ satisfy
$f-\gamma\in\operatorname{PA}_{*,b}(X)$. Suppose a vertex $v$ has a flat
relation and genuine raw mass $m_v=(D_f^d[X])(v)>0$. There is an
explicitly constructed $u\in\operatorname{PA}_{*,b}(X)$ such that
$$P_\gamma(u)=f\in\operatorname{PC}^{\rm reg}_*(X,\gamma),\qquad
 \int_X(f-(\gamma+u))\operatorname{MA}_{\mathrm{poly},*}(f)=-R m_v<0$$
for a positive rational $R$. In particular the pair cannot have both
all-obstacle endpoint regularity and orthogonality in that category.*

</div>

<div class="proof">

*Proof.* Choose a lattice basis and the rational polyhedral norm
$\rho(x)=\max_j|x_j|$ in its coordinates. Choose rational $R>0$ so small
that the closed norm ball about $v$ meets only cells incident to $v$,
the entire restriction of $f$ in that ball is its linear germ on each
incident cell, and the ball contains no other vertex of a chosen common
finite carrying structure for $f,\gamma,[X]$. These choices are possible
by finiteness and the rational vertex $v$. Put $$\label{roof}
 B_R(x)=(R-\rho(x-v))_+,\qquad
 u=f-\gamma+B_R,\qquad a=\gamma+u=f+B_R.$$ The roof is continuous
literal PA on a finite rational hyperplane subdivision, has integral
slopes and rational constants, and vanishes outside that ball. Thus $u$
is admissible in the asserted category. The function $f$ is a competitor
with the actual reference growth.

Write the flat relation as $\sum_i\lambda_i d_i=0$, $\lambda_i\geq0$,
and $\sum_i\lambda_i h_v(d_i)=0$, discarding zero coefficients. The
rational points $$y_i=v+\frac{R}{\rho(d_i)}d_i$$ lie in their assigned
incident cells and on the roof boundary. Set
$\beta_i=\lambda_i\rho(d_i)/R$. Then $$\sum_i\beta_i(y_i-v)=0,\qquad
 \sum_i\beta_i(f(y_i)-f(v))=0.$$ After normalization this is a printed
rational-endpoint PCC at $v$ whose endpoint obstacle values equal
$f(y_i)$. Every competitor $q$ therefore satisfies $q(v)\leq f(v)$.

For rational $x$ with $0<\rho(x-v)<R$, put $y=v+R(x-v)/\rho(x-v)$. This
is a rational point of the same incident cell, on the roof boundary. The
segment from $v$ to $y$ is in that cell. Jensen and the affinity of $f$
give $q(x)\leq f(x)$. Outside the ball the direct obstacle bound already
gives $q\leq f$. These bounds hold for every rational point and also at
$v$. For a real point, use successively smaller rational simplices in
its relative rational face containing it. Their rational vertices have
the preceding bound; Jensen and continuity of $f$ imply $q(x)\leq f(x)$.
Thus maximality over every printed-PC competitor, including
discontinuous ones, proves $P_\gamma(u)=f$. Its upper semicontinuous
regularization is the same continuous function.

The measured endpoint is already PA PC and relative; its constant
decreasing regularization is valid. Refinement independence proved above
ensures that new roof-subdivision vertices contribute no new atoms to
$\operatorname{MA}_{\mathrm{poly},*}(f)$. The only original atom in the
roof support is $v$, where the gap is $-R$. All others have gap zero.
Hence the integral is exactly $-R m_v$. This proof checks the genuine
operator domain rather than declaring a measure of a continuous hull. ◻

</div>

This theorem needs global compatibility of $f$, which is the explicitly
stated bounded-difference condition with the *actual* reference. It does
not assert that every abstract bad local germ can be extended through
the remaining complex. Positive growth alone is not used to replace that
condition.

<div id="scoped" class="corollary">

**Corollary 6** (Exact finite-PA-endpoint characterization). *For a
fixed pair and fixed coefficient category, the following are
equivalent:*

1.  *Every admissible PA obstacle whose actual envelope belongs to
    $\operatorname{PAPC}_*(X,\gamma)$ has zero raw contact integral.*

2.  *Every $f\in\operatorname{PAPC}_*(X,\gamma)$, at every vertex of a
    rational carrying structure, satisfies: $m_v(f)>0$ implies absence
    of a flat relation.*

*Here the reference is explicitly PA PC in the chosen category, as
required by Theorem <a href="#obstruction" data-reference-type="ref"
data-reference="obstruction">5</a>. The second condition contains
neither an obstacle nor a contact integral. This is a classification of
the finite PA endpoint sector, not original P05.2 with all regularizable
endpoints.*

</div>

<div class="proof">

*Proof.* If (2) holds, the finitely many positive atoms of a PA envelope
are contact points by Theorem
<a href="#necessary" data-reference-type="ref"
data-reference="necessary">4</a>; every term in its atomic contact
integral vanishes. Conversely a violation of (2) gives the admissible
obstacle and negative integral in Theorem
<a href="#obstruction" data-reference-type="ref"
data-reference="obstruction">5</a>, whose endpoint is in the stated PA
category. ◻

</div>

# A finite algebraic test with actual global growth

Fix a finite rational carrying structure $\Pi$ for $\gamma,[X]$.
Parameterize affine linear parts and constants of $f$ on its cells by
coefficients $z$. Equality of the affine restrictions on shared faces is
a finite rational linear system: test a rational affine basis of each
face. Lemma <a href="#supports" data-reference-type="ref"
data-reference="supports">2</a> at every face gives a finite system
$Az\geq0$. For each generator $r$ of $\operatorname{rec}(\sigma)$,
impose $$\label{growth}
 (f_\sigma-\gamma_\sigma)(r)=0.$$ These are exactly bounded difference
on the whole complex. Necessity follows along the rays $x+tr$;
sufficiency follows by writing a rational polyhedron as a bounded convex
hull plus its finitely generated recession cone. For cells with
lineality use both signs of a basis. If desired, an ambient rational
coordinate hyperplane arrangement splits every cell into pointed cells,
leaving only finitely many vertices and recession rays. Rational finite
generation and this decomposition follow from the elementary
cone-section argument in R230: remove rational lineality, take a
strictly positive rational section of the pointed cone, and obtain
finitely many rational vertices by successive active-constraint
elimination. Applying it to the homogenized cell gives the claimed
vertex-plus-recession decomposition.

On a specified structure, recursive formula
<a href="#raw" data-reference-type="eqref"
data-reference="raw">[raw]</a> makes $m_v(z)$ a homogeneous degree-$d$
polynomial in the linear parts, with the actual top weights and
primitive saturated normals as coefficients. Let $\kappa_{v,j}$ be the
finitely many normalized extreme relations at $v$, and $s_v(z)$ its
generator slope vector. The existence of a bad relative
$\operatorname{PA}_\mathbb R$ function *carried by this structure* is
exactly the finite disjunction of systems $$\label{test}
 \text{shared-face equations},\quad Az\geq0,\quad
 \eqref{growth},\quad
 s_v(z)\cdot\kappa_{v,j}=0,\quad m_v(z)>0.$$ A flat relation has zero
cost on some extreme relation because all extreme costs are nonnegative.
Thus <a href="#test" data-reference-type="eqref"
data-reference="test">[test]</a> is an actual semialgebraic obstruction
test, not total mass or orthogonality renamed. A feasible point gives a
global certificate and the roof obstacle. In the literal category impose
integral coordinates of each tangent linear part in a saturated lattice
basis and rational affine constants as well. A real feasible point is
not automatically a literal one.

Nonsimplicial stars use all their generators and shared-face equations;
no replacement by an ambient strong-convexity cone occurs. Nonsaturated
input directions must first be replaced by the saturated tangent lattice
normals in <a href="#raw" data-reference-type="eqref"
data-reference="raw">[raw]</a>; the relation cone alone does not encode
their intersection indices. Genuine common lineality has a linear
restriction of the germ and hence flat opposite generators. If a germ is
invariant modulo an affine function along nonzero common lineality, its
raw top atom is zero: on the generalized carrying fan every face
contains that lineality, so there are no zero-dimensional faces.
Refinement independence keeps that zero result if artificial cuts create
a vertex.

Testing one structure is not testing all rational refinements, and even
testing all structures only gives Corollary
<a href="#scoped" data-reference-type="ref"
data-reference="scoped">6</a>’s finite-PA sector. No bound on the
structures needed for arbitrary envelopes is proved here.

# A genuinely coupled two-plane obstruction

Let $N=\mathbb Z^3$, $P_{xz}=\{y=0\}$, $P_{yz}=\{x=0\}$, and
$X=P_{xz}\cup P_{yz}$ with cycle $[X]=[P_{xz}]+[P_{yz}]$. Both plane
lattices are saturated coordinate copies of $\mathbb Z^2$; all top cells
of a common rational subdivision have weight one. On a new wall in one
plane the two primitive inward quotient classes are opposites. On the
shared $z$-axis the transverse classes are $\pm e_x,\pm e_y$, whose sum
is zero. Thus this is an actual strictly positive balanced cycle.
Divisor additivity in the cycle, twice, gives
$$D_f^2[X]=D_f^2[P_{xz}]+D_f^2[P_{yz}].$$ This is additivity on a sum of
carrying planes; it asserts no product factorization of $f$ or
identification of PC with ambient convexity.

Define the actual ambient convex functions, restricted to $X$,
$$\gamma=\max(|x|,|y|,|z|)+|z|,\qquad
 f=\max(|x|,|y|-1,|z|)+|z|.$$ Each is a maximum of finitely many
integral affine forms after resolving $|z|$, with integer constants and
rational carrying walls. Thus both are continuous literal PA, separately
real PA, and PC by ordinary ambient Jensen for every permitted PCC.
Shifting just one entry of a maximum by minus one gives
$-1\leq f-\gamma\leq0$ everywhere. The reference satisfies
$\gamma\geq\rho=\max(|x|,|y|,|z|)$, so its slope in every nonzero
recession direction is strictly positive. Near zero on the vertical
plane $f=2|z|$, giving a flat relation on $\pm e_y$; on the horizontal
plane $f=\max(|x|,|z|)+|z|$.

## Every first-cycle weight and primitive normal

Write plane coordinates $(a,b)$ for $(x,z)$ or $(y,z)$, and
$s,t\in\{1,-1\}$. For $h(a,b)=\max(|a|,|b|)+|b|$, all nonzero
first-cycle edges are $$\{(sa,0):a\geq0\}\ \text{with weight }2,
 \quad \{r(s,t):r\geq0\}\ \text{with weight }1.$$ Along the $s$-axis,
adjacent gradients are $(s,1),(s,-1)$; primitive transverse lifts
$(0,1),(0,-1)$ give weight two. On a diagonal the outer and central
gradients are $(s,t),(0,2t)$. The tangent $(s,t)$ and inward lift
$(s,0)$ form a saturated basis, since their determinant is $\pm1$; the
opposite lift points centrally. The difference $(s,-t)$ evaluates to one
on $(s,0)$, giving weight one. Along each nonzero $b$-axis both
gradients are $(0,2t)$, so its weight is zero. There are no further
walls: the six affine forms are $a+b,a-b,-a+b,-a-b,2b,-2b$. The complete
cycle balances at zero, since the two weighted axes cancel and the four
diagonal directions cancel. Its outgoing slopes are one on the axes and
two on the diagonals, so $$(D_h^2[P])(0)=2+2+4\cdot2=12.$$ There are no
other vertices or atoms on this homogeneous plane cycle.

On $P_{yz}$ put $g(a,b)=\max(|a|-1,|b|)+|b|$. Its complete nonzero first
cycle consists of

1.  the central segment $b=0$, $-1\leq a\leq1$, of weight four;

2.  the outward axis rays from $(s,0)$ in direction $(s,0)$, of weight
    two;

3.  the two rays from each $(s,0)$ in directions $(s,t)$, each of weight
    one.

In $|a|<1+|b|$ the function is $2|b|$; outside it is $|a|-1+|b|$. Across
the central segment gradients $(0,2),(0,-2)$ and lifts $\pm e_b$ give
four. On each outward axis use $(s,\pm1)$ and the same lifts to get two.
On a diagonal use $(s,t),(0,2t)$ and lifts $\pm(s,0)$ as above, giving
one. Away from the endpoints the artificial lines $a=\pm1$ and the
nonzero $b$-axis have identical gradients on both sides, hence weight
zero. The six affine forms are $a-1+b,a-1-b,-a-1+b,-a-1-b,2b,-2b$; they
show there are no omitted positive walls.

At $p_s=(0,s,0)$, the weighted primitive directions and outgoing slopes
are $$\begin{array}{c|c|c}
\text{direction}&\text{weight}&\text{slope of }f\\\hline
-s e_y&4&0\\
s e_y&2&1\\
s e_y+e_z&1&2\\
s e_y-e_z&1&2
\end{array}$$ Their weighted sum is
$-4s e_y+2s e_y+(s e_y+e_z)+(s e_y-e_z)=0$. The recursive atom is
$4\cdot0+2\cdot1+1\cdot2+1\cdot2=6$. Subdividing the central segment at
zero adds opposite weight-four $y$ directions of zero slope, hence adds
zero atom there. On the full $X$, the origin also has the
horizontal-plane axes and diagonals just computed; their mass is twelve.
Thus $$\label{new-masses}
 \operatorname{MA}_{\mathrm{poly}}(\gamma)=24\delta_0,\qquad
 \operatorname{MA}_{\mathrm{poly}}(f)=12\delta_0+6\delta_{p_+}+6\delta_{p_-}.$$
All first-cycle vertex balances have been displayed. At an added vertex
on a straight affine first-cycle edge, equal weights and opposite
outgoing slopes cancel. A new wall inside an affine top cell has
opposite normal contributions and zero first weight. New cells in old
higher-dimensional zero-weight strata inherit zero. These facts, or the
fully converted refinement theorem above, give zero artificial mass at
every vertex of the roof subdivision. No factorial is added. The
gradient polygons have areas six for $h$ at zero and three for $g$ at
each endpoint; twice these areas agrees with the raw calculation.
Polygon area is an independent check, not its operator proof.

## Unrestricted envelope and both coupling tests

Set $R=1/4$, $B=(R-\rho)_+$, and $u=f-\gamma+B$. This obstacle is
bounded literal PA on a finite rational arrangement; $\gamma+u=f+B$ and
$f$ is an actual relative PC competitor. For every printed-PC competitor
$q$, including discontinuous ones, the rational endpoints $(0,\pm R,0)$
have obstacle value zero and midpoint zero, so $q(0)\leq0=f(0)$. A
rational point $w$ with $0<\rho(w)<R$ lies on the chord from zero to the
rational boundary point $Rw/\rho(w)$. The entire chord is in one
incident linearity cell of $f$; inside this ball $f$ is homogeneous on
both planes. The boundary obstacle equals $f$, so Jensen gives
$q(w)\leq f(w)$. Outside the ball the obstacle itself gives this bound.
At an arbitrary real point take shrinking rational simplices in its
minimal rational face. All their vertices satisfy the rational bound,
and the printed PCC inequality and continuity of $f$ give $q\leq f$ at
the center. No continuity of $q$ is assumed. Therefore $P_\gamma(u)=f$
on all $X$; its usc regularization is itself. A constant PA regularizing
sequence, or decreasing positive rational additions, works in both
categories. Only the origin has mass in the roof support, so
$$\label{new-contact}
 \int_X(f-(\gamma+u))\operatorname{MA}_{\mathrm{poly}}(f)=-R\cdot12=-3.$$
Both total masses are twenty-four, which does not establish contact.

The precise excluded decomposition is $f(q,z)=F(q)+H(z)$ on
$X=C\times\mathbb R$, $C=\{y=0\}\cup\{x=0\}\subset\mathbb R^2$. At the
four horizontal-plane corners $(x,z)=(0,0),(R,0),(0,R),(R,R)$, the
endpoint and reference values are $0,R,2R,2R$. The mixed difference
$f(R,R)-f(R,0)-f(0,R)+f(0,0)=-R$ is nonzero. The obstacle values there
are $R,0,0,0$, with mixed difference $R$. Thus reference, endpoint, and
obstacle all exclude the stated additive product decomposition. We claim
nothing about every possible reparametrized factorization. Pair-level
regularity for other obstacles is not inferred.

# Why finite jet presentation does not finish regularization

Lemma <a href="#supports" data-reference-type="ref"
data-reference="supports">2</a> does give a finite linear feasibility
system for PC affine coefficients on a *specified* structure. Together
with shared-face, obstacle, and growth constraints it gives valid finite
PA trial competitors. It does not prove that this structure carries the
unrestricted envelope, that a finite number of hull iterations suffices,
or that all structures have a uniform approximation theorem. R230
supplies continuity but none of those conclusions.

There is also a precise coefficient obstruction to treating the real
rational-structure category as closed under taking maxima. On
$\mathbb R$, put $\alpha=\sqrt2-1$ and
$$f_1=|x|,\quad f_2=|x-1|+\alpha,\quad
 t=(1+\alpha)/2=\sqrt2/2.$$ Both $f_i$ are real PA on rational
structures, PC, and differ boundedly from $|x|$. Yet
$$\max(f_1,f_2)=\max(x,2t-x)=|x-t|+t$$ has its unique kink at the
irrational point $t$, so no finite rational structure on $\mathbb R$
carries it. This is *not* a nonregularizability example: rational
$t_n\downarrow t$ give literal PA PC functions
$$H_n=\max(x,2t_n-x)\downarrow \max(f_1,f_2),\qquad
 \|H_n-\max(f_1,f_2)\|_\infty=2(t_n-t).$$ Thus a finite maximum argument
needs its own rational-structure and approximation audit; the failure of
PA closure alone proves no endpoint regularization failure.

# Global realization of finite local jets for rational references

Here $\gamma$ is rational affine on a finite rational structure, PC, and
positive at infinity. The target coefficient category is the explicitly
real scalar extension, even when $\gamma$ is literal. We do not assert
that the following scaling/gluing is literal.

<div id="jet-realization" class="theorem">

**Theorem 7** (Actual-reference jet realization). *At a rational point
$v\in X$, let $h$ be a continuous homogeneous PA PC function on a finite
rational refinement of the tangent star of $X$ at $v$, with $h(0)=0$. If
all affine linear parts of $h$ are rational, then there is a global
rational-affine relative real PA PC function $G$ whose germ at $v$ is
$C+t+\delta h$, for positive rational $\delta,t$ and rational $C$. In
particular flat relations are preserved and the raw atom is
$\delta^d m_0(h)$. If a real-coefficient such jet has a flat relation
and positive raw atom, some rational-coefficient jet on the same
specified structure has these properties and hence is globally realized
with the actual reference.*

</div>

<div class="proof">

*Proof.* The space equals its truncated tangent star in a sufficiently
small rational norm ball about $v$; insert $v$ and the chosen local
rational fan subdivision. The finite linear pieces of $h$ give
$|h(x)|\leq L\rho(x)$ on this tangent support for some $L$. Choose
rational $\varepsilon>0$ so the ambient $\varepsilon\rho(x-v)$ has
recession slopes strictly smaller than those of $\gamma$. The coercive
linear lower bound proved in
Lemma <a href="#test-dc" data-reference-type="ref"
data-reference="test-dc">10</a> permits this choice. Take rational
$C>\gamma(v)$ and put
$$\Psi(x)=\max\{\gamma(x),C+\varepsilon\rho(x-v)\}.$$ Both entries have
local supports. The maximum is rational-affine PA PC, agrees with
$C+\varepsilon\rho$ near $v$, and differs boundedly from $\gamma$,
because its second entry is below $\gamma$ outside a compact set. Choose
a rational star radius $r>0$, and rational $\delta>0$ with
$\delta L\leq\varepsilon/2$. Choose rational $0<t<\varepsilon r/4$.
Inside $\rho(x-v)<r$ define $$G(x)=\max\{\Psi(x),C+t+\delta h(x-v)\},$$
and set $G=\Psi$ outside. On the collar $r/2\leq\rho<r$,
$C+\varepsilon\rho\geq C+t+\delta h$, so these definitions agree. Near
$v$, $\Psi=C+\varepsilon\rho$ and the raised jet is strictly active for
sufficiently small $\rho$; hence the germ is precisely $C+t+\delta h$.
Local supports of $h$ follow from the finite support criterion; supports
of an active entry support the maximum, also at ties. The collar glues
without a new defect. The global support lemma therefore gives every PCC
inequality. All coefficients and all norm-ball, fan and equality walls
are rational, so the structure is finite rational. The modification of
$\Psi$ has compact support and is bounded. Thus $G-\gamma$ is genuinely
bounded with the actual prescribed growth. Raw recursion in the local
star is unchanged by the constant and scales by $\delta^d$; flat
relation costs scale by $\delta$.

For a real-coefficient bad jet, the finitely many shared-face and PC
conditions on its fixed fan are rational linear conditions. Some
rational extreme relation has zero cost: decompose its flat relation
into extreme relations and use nonnegative costs. Adjoin that rational
linear zero-cost equation. Rational points are dense in this feasible
rational polyhedron, including at its boundary, by solving the active
rational equalities as equalities and approximating in their rational
affine solution space (inactive inequalities remain strict). The raw
mass is a continuous degree-$d$ polynomial in the slopes, with the
actual fixed top weights, so its strict positivity persists under a
sufficiently close such rational approximation. This gives the claimed
rational bad jet, and the first construction applies. No arbitrary local
germ is asserted literal-realizable. ◻

</div>

<div id="local-finite" class="corollary">

**Corollary 8** (Structural finite-PA contact criterion). *For
rational-affine positive-growth $\gamma$, real-category contact for all
bounded real PA obstacles whose actual envelopes are finite relative PA
is equivalent to the following condition on the weighted rational
geometry of $X$: at every rational point and every finite rational
refinement of its tangent star, each PC homogeneous PA jet with a flat
relation has zero raw top atom. This condition contains no actual
reference or global extension premise; its raw recursion uses the
saturated tangent lattices and actual weights.*

</div>

<div class="proof">

*Proof.* If the condition holds, apply it to the germ of any
positive-mass finite PA envelope vertex. There can be no flat relation
there, so the corrected noncontact theorem forces contact. Conversely a
bad local jet has a globally realized relative real PA function by
Theorem <a href="#jet-realization" data-reference-type="ref"
data-reference="jet-realization">7</a>. The exact roof theorem gives an
admissible real PA obstacle with that endpoint and strictly negative
contact integral. Its coefficient and regularizable antecedents are
already checked. ◻

</div>

The universal quantifier over rational star refinements is essential.
Each fixed fan has the finite circuit/mass test already proved, but no
bound on the necessary refinements follows. This is now a geometric
criterion for the finite PA endpoint sector and this rational-reference
scope. It still does not classify all regularizable non-PA endpoints or
establish regularity for every continuous obstacle.

# A genuine extension on the regularizable domain

This section goes beyond finite endpoints. Its reference hypothesis is
*rational affine coefficients on a finite rational structure*, not
arbitrary real coefficients. Literal references satisfy it. We retain
finite pure positively balanced embedded $X$, real finite raw
intersections, and positive growth of the actual reference $\gamma$. We
do not import BMPS Theorem 4.13 or Proposition 4.16: their needed
conclusions in this scope are reconstructed below. In particular no
operator is assigned just because an envelope is continuous.

<div id="raw-ibp" class="lemma">

**Lemma 9** (Raw degree and integration by parts). *All mixed finite PA
PC functions $a_1,\ldots,a_d$ with bounded difference from $\gamma$ have
total raw mass $M=\deg(\gamma)$. For bounded finite PA $b,c$ and any
intermediate balanced one-cycle $Z$, $$\int bD_c Z=\int cD_b Z.$$ Both
statements allow real coefficients and zero intermediate weights.*

</div>

<div class="proof">

*Proof.* Refine so every function is affine on every edge of $Z$; cut
lines at rational points if necessary. On an unbounded edge a bounded
affine function has zero slope. For a bounded edge $[v,w]$ of primitive
length $L_e$, its contribution to $\int bD_c Z$ is
$$\frac{Z(e)}{L_e}(b(v)-b(w))(c(w)-c(v)),$$ which is symmetric in $b,c$.
Sum the finite list of edges. Also $\deg(D_b Z)=0$: bounded-edge
outgoing slopes cancel, and unbounded slopes vanish. Replace each mixed
factor $a_i$ by $\gamma$ one at a time; the difference is
$D_{a_i-\gamma}$ of the balanced one-cycle formed by the other $d-1$
factors, so it has degree zero. Positivity was proved by local supports
and balanced preservation above. For later use, the bounded-difference
identity is $$\label{relative-ibp}
 \int(\gamma-q)\operatorname{MA}_{\mathrm{poly}}(a_1,a_2,\ldots,a_d)
 =\int(\gamma-a_1)\operatorname{MA}_{\mathrm{poly}}(q,a_2,\ldots,a_d)
  +\int(a_1-q)\operatorname{MA}_{\mathrm{poly}}(\gamma,a_2,\ldots,a_d).$$
It follows by applying the bounded $b,c$ identity to $b=\gamma-q$,
$c=a_1-\gamma$, then expanding linearly. All measures in this displayed
formula are finite raw measures. ◻

</div>

<div id="test-dc" class="lemma">

**Lemma 10** (Test functions as differences of relative PC functions).
*Let $\psi$ be a compactly supported ambient continuous PA function with
rational affine coefficients on a finite rational complex in
$N_\mathbb R$. There are rational $\varepsilon>0$ and rational-affine
relative PA PC functions $\theta_0,\theta_1$ on $X$ such that
$\theta_1-\theta_0=\varepsilon\psi|_X$.*

</div>

<div class="proof">

*Proof.* Choose the finite rational hyperplane arrangement containing
every wall of $\psi$, with integral normal forms $L_j$ and rational
constants. Across each wall the two gradients of $\psi$ differ by a
scalar multiple of its normal. There are finitely many such multiples.
For a sufficiently large rational $K>0$, $H=K\sum_j|L_j|$ and $H+\psi$
are ambient convex: on a generic segment their slopes increase at every
wall, since the bend $2K$ dominates every negative bend of $\psi$;
limiting generic segments prove the same for all segments. Both are
rational affine on this arrangement.

Positive growth and the finite vertex-plus-recession decompositions give
$\gamma(x)\geq a\rho(x)-b$ on $X$ for some $a>0,b$. Indeed the ratio of
its positive recession linear part to $\rho$ has a positive minimum on
the finite unit recession sections; the finitely many bounded hulls
change only the constant. Take rational $\varepsilon>0$ so small that
$\varepsilon H$ has recession slopes strictly below those of $\gamma$,
using its finite Lipschitz constant. Choose rational $C$ so
$C+\varepsilon H>\gamma$ on a neighborhood of
$\operatorname{supp}\psi\cap X$. Define
$$\theta_0=\max(\gamma,C+\varepsilon H),\qquad
 \theta_1=\theta_0+\varepsilon\psi.$$ The first maximum has local
supports and hence is PC. Near the support of $\psi$, the second
function is $C+\varepsilon(H+\psi)$; outside that support it equals
$\theta_0$. These open descriptions cover $X$ and give local supports
everywhere, including the collar where $\psi=0$. Both functions differ
boundedly from $\gamma$: the added maximum is inactive outside a compact
set. All their affine coefficients are rational, so all new equality
walls are rational and both functions are real PA on finite rational
structures. They need not be literal PA; only the already verified
finite real raw operator is used for them. For an irrational-coefficient
reference these new maximum walls need not be rational, which is why
that category is excluded from this lemma. ◻

</div>

The restrictions of these compact ambient rational PA tests are
uniformly dense in $C_c(X)$, allowing supports in a fixed larger compact
set. Here is a direct construction. For a nonnegative $g\in C_c(X)$, fix
a small uniform-continuity scale $\delta$ for $g$ on the closed finite
polyhedral support $X$. Such a scale exists: outside a compact
neighborhood $g=0$, and inside it a finite compactness cover gives the
scale. Choose an integer $L$ larger than $2\|g\|_\infty/\delta$ and a
sufficiently fine finite rational net of the compact set where $g$ may
be nonzero. Approximate its sampled values by nonnegative rational $a_j$
and set $$G(x)=\max_j(a_j-L\rho(x-v_j))_+.$$ For $\rho(x-v_j)\geq\delta$
the corresponding bump vanishes; for smaller distances it exceeds $g(x)$
by at most the chosen uniform-continuity and sampled-value errors. A net
finer than the error divided by $L$ gives the reverse inequality. Thus
the error can be arbitrarily small. This is compactly supported ambient
rational PA with rational equality walls. Apply the construction
separately to $g_+$ and $g_-$ for a signed function. No false density in
all $C_b(X)$ is asserted.

<div id="raw-extension" class="theorem">

**Theorem 11** (Sequence-independent raw completion). *Let $\gamma$ have
the reference hypotheses of this section. For $*=\mathbb Z,\mathbb R$
the finite raw mixed operator has a unique continuous extension to
tuples of uniform limits of relative $\operatorname{PAPC}_*$ functions.
This includes precisely the stated uniform-decreasing regularizable
domain; no further PC functions are placed in the domain. For any
uniformly convergent PA PC approximants, even if not decreasing, the
mixed raw measures converge weakly against every bounded continuous test
on $X$, independently of all approximants. The limit is a positive
finite Radon measure of total mass $M$, is symmetric and local, and its
restriction to finite endpoints is the original raw operator. The
literal extension is the unique uniform-continuous extension of BMPS’s
raw formula on this domain. The real extension is explicitly so
constructed, with no unproved all-real-reference assertion.*

</div>

<div class="proof">

*Proof.* Fix a test $\psi$ from
Lemma <a href="#test-dc" data-reference-type="ref"
data-reference="test-dc">10</a>. For two relative PA PC tuples
$\mathbf a,\mathbf b$, telescope one argument at a time. At the $i$th
step the other arguments form a positive balanced one-cycle $Z_i$. By
Lemma <a href="#raw-ibp" data-reference-type="ref"
data-reference="raw-ibp">9</a> and
$D_\psi=(D_{\theta_1}-D_{\theta_0})/\varepsilon$,
$$\label{test-estimate}
 \left|\int\psi(\operatorname{MA}_{\mathrm{poly}}(\mathbf a)-\operatorname{MA}_{\mathrm{poly}}(\mathbf b))\right|
 \leq \frac{2M}{\varepsilon}\sum_i\|a_i-b_i\|_\infty.$$ Indeed each
positive mixed measure $D_{\theta_j}Z_i$ has mass $M$, so the signed
$D_\psi Z_i$ has total variation at most $2M/\varepsilon$. This estimate
covers arbitrary real approximant coefficients, since $\theta_j$ are
merely auxiliary functions in the finite real domain.

A uniform-Cauchy approximating tuple therefore has Cauchy integrals for
all these tests. Density and the common mass $M$ make the same true for
every $g\in C_c(X)$: replace $g$ by a test with uniform error $\eta$, at
cost at most $2M\eta$. The limiting functional is positive, linear, and
bounded by $M\|g\|_\infty$. It defines a positive Radon measure $\mu$.
To specify the elementary measure representation being used, for open
$O$ define $$\mu(O)=\sup\{L(g):g\in C_c(X),\ 0\leq g\leq1,
                         \operatorname{supp}g\subset O\}.$$ Define the
outer measure by infima over open supersets. A compact support and a
finite continuous partition subordinate to an open cover show
subadditivity; for disjoint open sets addition of finitely many tests
gives the reverse inequality. Distance cutoffs on this locally compact
closed metric space give separation of disjoint closed sets, hence the
outer measure is a metric outer measure and all Borel sets are
measurable. Approximating each open set from inside by the supports of
its tests gives inner regularity, and its definition gives outer
regularity. Finally partitions of the range of a nonnegative $g\in C_c$
into intervals of length $1/n$, with continuous cutoffs of the
corresponding level sets, bound $L(g)$ between the lower and upper
simple integrals with difference at most $M/n$ times a fixed range
constant. Passing to the limit gives $L(g)=\int g\,d\mu$. This
construction proves existence and uniqueness of the needed Radon
representation without a compactification/operator theorem.

There is no loss of mass at infinity. Add a rational constant so that
$\gamma\geq0$. Uniform approximating tuples obey
$\|a_i-\gamma\|_\infty\leq C$ with one common $C$. The rational-affine
functions $q_j=\max(\gamma-j,0)$ are relative PC PA for integer $j$;
their walls are rational. Iterating
<a href="#relative-ibp" data-reference-type="eqref"
data-reference="relative-ibp">[relative-ibp]</a>, and bounding each of
its first two bounded-difference terms by $CM$, yields $$\label{moment}
 \int\min(\gamma,j)\operatorname{MA}_{\mathrm{poly}}(\mathbf a)
 \leq 2dCM+\int\gamma\operatorname{MA}_{\mathrm{poly}}(\gamma)=:K.$$ The
last integral is finite because the reference raw measure has finite
support. Increasing $j$ gives
$\int\gamma\operatorname{MA}_{\mathrm{poly}}(\mathbf a)\leq K$. Since
$\gamma$ is proper, the mass on $\{\gamma>T\}$ is at most $K/T$. This is
uniform tightness. Compactly supported cutoffs equal to one on
$\{\gamma\leq T\}$ show $\mu(X)=M$ and give the same tail bound for the
limit. Truncating any bounded continuous test to such compact sets then
proves convergence against that test. The moment bound also passes to
the limit by compact truncations.

Applying <a href="#test-estimate" data-reference-type="eqref"
data-reference="test-estimate">[test-estimate]</a> between any two
approximating tuples proves independence. It also proves continuity
under uniform convergence of the limits: take PA approximants to each
limit within an arbitrarily small error and pass to the inequality. A
uniformly convergent family of relative limits has a common $C$, so
tightness upgrades this continuity to bounded-continuous tests. Symmetry
follows from the raw symmetry. For locality take $\psi$ supported in an
open set where each limiting argument agrees. Raw $D_\psi Z_i$ is
supported there, so the same total-variation bound uses only the uniform
argument error on that set; it tends to zero. Density proves equality of
the measures on the open set.

Finally any uniform PA approximation can be replaced by a decreasing one
in the same category. Extract $a_n$ with error at most $2^{-n}$ and
replace it by $a_n+4\cdot2^{-n}$. The consecutive difference is
nonnegative because the added-constant drop is $2\cdot2^{-n}$ and the
possible approximation increase is at most $3\cdot2^{-n}/2$. The added
constants are rational and preserve both coefficient categories. The
sequence decreases uniformly to the limit. Thus this proof uses exactly
the regularizable domain declared earlier, including non-PA endpoints,
rather than assigning an operator on all continuous PC. ◻

</div>

<div id="contact-stability" class="corollary">

**Corollary 12** (Stability of actual contact integrals). *If $u_n\to u$
uniformly in $C_b(X)$, their actual envelopes $f_n,f$ are in the proved
regularizable domain, and $\gamma$ has the hypotheses of
Theorem <a href="#raw-extension" data-reference-type="ref"
data-reference="raw-extension">11</a>, then their exact contact
integrals converge. This proves stability, not the missing domain
membership of arbitrary envelopes.*

</div>

<div class="proof">

*Proof.* R230 applies to this finite positive balanced domain with
continuous reference and bounded continuous obstacles. It makes all
envelopes continuous and gives $\|f_n-f\|_\infty\leq\|u_n-u\|_\infty$.
Their bounded continuous gaps $f_n-\gamma-u_n$ converge uniformly.
Theorem <a href="#raw-extension" data-reference-type="ref"
data-reference="raw-extension">11</a>, its common total mass, and its
bounded-continuous convergence give the asserted integral limit. ◻

</div>

# A non-PA regularizable coupled endpoint with an explicit measure

Keep the actual literal reference and balanced $X$ from
Section <a href="#coupled-section" data-reference-type="ref"
data-reference="coupled-section">7</a>. Define the even convex function
$$a(y)=\begin{cases}
 0,&|y|\leq1,\\
 (|y|-1)^2/2,&1\leq|y|\leq2,\\
 |y|-3/2,&|y|\geq2,
 \end{cases}
 \qquad F=\max(|x|,a(y),|z|)+|z|\quad\hbox{on }X.$$ The derivative of
$a$ increases from zero to one on the positive side, and the negative
side is its reflection; it is convex and continuous. Thus $F$ is a
restriction of an ambient convex continuous function,
$-3/2\leq F-\gamma\leq0$, and its horizontal restriction is still $h$.
Its vertical restriction at $z=0$, $1<y<2$, is a quadratic, so it is not
finite PA on any polyhedral structure, rational or otherwise.

For $n\geq0$ put $N=2^n$, $h_N=1/N$, and let $a_N$ interpolate the
values $a(1+j/N)$ linearly on $[1,2]$, extended by the same zero and
linear outer pieces and reflected evenly. Convex chordal interpolation
has increasing slopes $k_j=(j+1/2)/N$, $0\leq j<N$; the initial jump is
$1/(2N)$, the interior jumps are $1/N$, and the final jump to one is
$1/(2N)$. The dyadic interpolants decrease to $a$ and
$$0\leq a_N-a\leq1/(8N^2).$$ This exact bound follows on each interval
by subtracting the quadratic from its chord: the error is
$(t-t_j)(t_{j+1}-t)/2$. Therefore
$$F_N=\max(|x|,a_N(y),|z|)+|z|\downarrow F,\qquad
 \|F_N-F\|_\infty=1/(8N^2).$$ All slopes and constants of $a_N,F_N$ are
rational. Equality walls of their maxima are rational, so they are real
PA on finite rational complexes. They are actual relative PC functions
with the displayed common growth bound. Thus
$F\in\operatorname{PC}^{\rm reg}_{\mathbb R}(X,\gamma)$ and
Theorem <a href="#raw-extension" data-reference-type="ref"
data-reference="raw-extension">11</a> supplies its genuine
sequence-independent extended raw measure.

Here are all raw atoms of these approximants, without substituting
polygon area for the recursive proof. On the positive vertical
half-plane, put $t_j=1+j/N$, $b_j=a_N(t_j)$ and $\Delta_j=k_j-k_{j-1}$,
with $k_{-1}=0$ and $k_N=1$. At the initial point $(1,0)$ the central
weight-four edge, outward weight-two edge, and graph edges of weight
$1/q$ in primitive directions $(q,\pm p)$, $k_0=p/q$, give mass
$6\Delta_0$. Their balance is $-4e_y+2e_y+(1,k_0)+(1,-k_0)=0$ after
weighting; the outgoing slopes give $0+2k_0+2k_0+2k_0$. For $j\geq1$ the
three atoms are $$\label{nonpa-atoms}
 4\Delta_j\delta_{(0,t_j,0)}+
 \Delta_j\delta_{(0,t_j,b_j)}+
 \Delta_j\delta_{(0,t_j,-b_j)}.$$ To verify their entire first-cycle
neighborhood, the $z=0$ edges have weight two and slopes $-k_{j-1},k_j$;
the vertical wall $y=t_j$ inside $|z|<b_j$ has weight $\Delta_j$ and
primitive directions $\pm e_z$. At $(t_j,0)$ its slopes are one in both
directions, so the second weight is
$2(k_j-k_{j-1})+2\Delta_j=4\Delta_j$. At the upper graph vertex the
first edges have primitive directions $(-q_{j-1},-p_{j-1})$, $(q_j,p_j)$
and $(0,-1)$, with weights $1/q_{j-1},1/q_j,\Delta_j$. Their weighted
vector sum is $(-1,-k_{j-1})+(1,k_j)+(0,-\Delta_j)=0$. Their outgoing
slopes are $-2p_{j-1},2p_j,-1$, giving second weight
$-2k_{j-1}+2k_j-\Delta_j=\Delta_j$. The lower vertex is the reflected
computation. These weights arise from primitive normals, not Euclidean
lengths: for a graph with slope $p/q$ in lowest terms the dual gradient
jump is $(p/q,-1)$; any transverse integral lift $n$ with
$\det((q,p),n)=-1$ lies on the outer side and evaluates to $1/q$. Such a
lift exists by the Euclidean algorithm since $\gcd(p,q)=1$. At the
vertical wall the opposing normal lifts $\pm e_y$ give $k_j-k_{j-1}$. At
$z=0$ use $\pm e_z$. There are no further positive walls: in each affine
interval $a_N$ the only active comparisons are $z=0$ and $z=\pm a_N(y)$;
vertical kink walls contribute only inside that strip. All other
subdivisions have the opposite-normal or opposite-slope zero-mass
cancellations already proved. Negative $y$ contributes the reflected
atoms. The horizontal plane still contributes $12\delta_0$; subdividing
the flat central vertical segment at zero contributes zero. The total is
$12+2\cdot6\sum_j\Delta_j=24$.

For every bounded continuous test, the dyadic sums in
<a href="#nonpa-atoms" data-reference-type="eqref"
data-reference="nonpa-atoms">[nonpa-atoms]</a> converge to ordinary
Riemann integrals; the two endpoint half-jumps tend to zero and
$a_N\to a$ uniformly. Consequently the sequence-independent measure is
exactly $$\label{nonpa-measure}
 \operatorname{MA}_{\mathrm{poly},\mathbb R}(F)=12\delta_0+
 \sum_{s=\pm1}\int_1^2
 \left(4\delta_{(0,st,0)}+
       \delta_{(0,st,(t-1)^2/2)}+
       \delta_{(0,st,-(t-1)^2/2)}\right)\,dt.$$ This is a positive
measure of total mass twenty-four; its non-atomic part lies on two
segments and four parabolic arcs. Formula
<a href="#nonpa-measure" data-reference-type="eqref"
data-reference="nonpa-measure">[nonpa-measure]</a> specifies pushforward
parameter measures, not unexplained Euclidean arc-length factors.

Set $U=F-\gamma+(1/4-\rho)_+$ and $U_N=F_N-\gamma+(1/4-\rho)_+$. The
$U_N$ are bounded real PA obstacles on finite rational structures,
converging uniformly to the bounded continuous, non-PA obstacle $U$.
Inside the roof ball every $F_N$ and $F$ has exactly the same PA germ as
the coupled endpoint of
Section <a href="#coupled-section" data-reference-type="ref"
data-reference="coupled-section">7</a>. The rational flat pair,
radial-chord, and shrinking-simplex proof of that section therefore
applies literally there; outside it the direct obstacle bound is
$q\leq F_N$ or $q\leq F$. The function itself is a PC competitor. Thus
the unrestricted envelopes are respectively $F_N,F$, with no continuity
assumption on competitors. The measure in
<a href="#nonpa-measure" data-reference-type="eqref"
data-reference="nonpa-measure">[nonpa-measure]</a> has only its origin
atom in the roof, and
$$\int_X(F-(\gamma+U))\operatorname{MA}_{\mathrm{poly},\mathbb R}(F)=-3.$$
The same result follows independently from the actual contact stability
corollary and the approximant integrals. Both $F$ and $U$ have the same
nonzero cross-times-$z$ mixed differences as the PA example.

There is a sharp coefficient limit to this example. $F$ is not literally
regularizable. On the primitive $y$-segment $[5/4,7/4]$ at $z=0$, its
left half increment is $3/32$, its right half increment is $5/32$, and
each half has length $1/4$. A literal convex approximant has
nondecreasing integral slopes. If its right-hand midpoint slope is at
most zero, its left half increment is at most zero. If that slope is at
least one, its right increment is at least $1/4=8/32$. In both cases
uniform error $\eta$ satisfies $2\eta\geq3/32$, so
$$\inf_{\psi\in\operatorname{PAPC}_\mathbb Z(X)}\|\psi-F\|_\infty\geq3/64.$$
No literal measure is assigned to $F$. This continuous-obstacle witness
is an unconditional real-domain result, not an assertion of all-obstacle
real regularity or a non-PA envelope for a finite PA obstacle.

# The literal antecedent on noncompact finite spaces

The following is a reconstruction of the dossier’s noncompact literal
obstruction, not an additional caller grant or a new claim of priority.
It clarifies the literal branch of the original task before any measure
is assigned to an endpoint.

<div id="literal-general" class="theorem">

**Theorem 13** (Noncompact literal obstruction). *Let
$X\subset N_\mathbb R$ be a noncompact finite rational polyhedral space,
and let $\gamma$ be literal PA PC and positive at infinity. Then some
bounded literal PA obstacle has an envelope with a positive uniform
distance from every literal PA PC function. Thus the pair fails the
all-PA-obstacle regularity antecedent. Balancing is not needed.*

</div>

<div class="proof">

*Proof.* Choose a rational point $x$ in a noncompact connected component
and rational $C>\gamma(x)$. Put $\phi=\max(\gamma,C)$ and
$D=\phi-\gamma$. These are literal PA; $\phi$ is PC by Jensen for
maxima, and $D\geq0$ has compact support by positive growth. Take a
finite common rational subdivision carrying them and split cells by a
coordinate arrangement so that every cell is pointed. Every unbounded
cell has $D=0$: an affine bounded function has zero slope on its
recession rays, and its value along any such ray must vanish eventually
because $D$ has compact support. Thus a positive cell of $D$ is bounded.

The selected component is path connected through finitely many
polyhedral cells. Since $D(x)>0$ but $D=0$ far out, some bounded
positive-dimensional cell $\sigma$ has nonzero linear part $k$ of $D$.
Choose a primitive $w\in N_\sigma$ with $k(w)\ne0$ and a rational
segment $I=x_0+[0,L]w$ inside its relative interior. Let $N>|k(w)|$ be
an integer and set $$f=\gamma+D/N=(1-1/N)\gamma+\phi/N.$$ It is
continuous real PA on this rational structure, PC by Jensen, and differs
boundedly from $\gamma$. We now produce a *literal* obstacle, not merely
the fractional difference $D/N$.

For every vertex $v$ of this finite structure choose one sufficiently
large integer $M$ so that
$$C_v(y)=D(v)/N+M\rho(y-v)\geq D(y)/N\quad(y\in X).$$ Such a common $M$
exists. On cells incident to $v$ the affine linear parts bound the
difference by a finite slope constant times $\rho$. The finite union of
nonincident closed cells has positive distance from $v$, while $D$ is
globally bounded, so their ratios are bounded as well. Take the maximum
over the finitely many vertices and round up to an integer. Set
$$u_N=\min\left(D,\min_v C_v\right).$$ All entries have integral slopes
and rational constants; minima and norm walls give a finite rational
literal structure. Moreover $D/N\leq u_N\leq D$, $u_N(v)=D(v)/N$ at
every vertex, and $u_N=0$ on every unbounded cell. Thus
$f\leq\gamma+u_N$ and $f$ is a competitor.

Every other competitor $q$ has $q(v)\leq f(v)$ at the vertices. For a
rational point $y$ of a pointed cell, write its vertex-plus-recession
representation $y=\sum_v\alpha_vv+\sum_r\beta_rr$ with rational
nonnegative coefficients and $\sum_v\alpha_v=1$; rational Gaussian
elimination of the feasible rational system gives such coefficients.
Choose $v_0$ with $\alpha_{v_0}>0$ and large rational $T$ with
$\sum\beta_r/T<\alpha_{v_0}$. Replace the indicated portions of the
$v_0$ coefficient by weights $\beta_r/T$ at the endpoints $v_0+Tr$. This
is a PCC in that same cell. Those far endpoints are in its unbounded
part, where obstacle and $f$ agree; their values are
$f(v_0)+T f_\sigma(r)$. Jensen therefore gives exactly $q(y)\leq f(y)$.
If there are no recession terms this is just the vertex combination. The
vertex-plus-recession decomposition follows by homogenizing the rational
cell and using the finite rational generating-cone argument already
supplied by R230; pointedness ensures vertices exist. Shrinking rational
simplices give the same bound at real points. Therefore the unrestricted
envelope is $f$.

On $I$ its slope is $q_0=\gamma_\sigma(w)+k(w)/N\notin\mathbb Z$. For a
literal PA PC function $\psi$, slopes on this contained primitive
segment are nondecreasing integers: ordinary segment convexity follows
from continuity and rational endpoint Jensen. At the midpoint its
right-hand slope is either at most $\lfloor q_0\rfloor$ or at least
$\lceil q_0\rceil$. Compare respectively the left or right half
increments with the affine target. If uniform error is $\eta$, then
$$\eta\geq\frac L4\operatorname{dist}(q_0,\mathbb Z)>0.$$ This excludes
literal uniform regularization. No literal extended Monge–Ampere measure
is assigned to this envelope. ◻

</div>

In the fixed globally embedded BMPS category, B225’s positive-balanced
compact-support theorem applies to every nonempty finite pure positive
balanced $X$ of dimension $d\geq1$. It is therefore noncompact, so
Theorem <a href="#literal-general" data-reference-type="ref"
data-reference="literal-general">13</a> excludes every such
positive-growth literal pair from the source’s pair-level orthogonality
domain, whose definition presupposes regularity. This is a statement
about that antecedent, not a declaration that a nonregularizable
endpoint has an orthogonality measure. In dimension zero finite rational
points have pointwise envelope $\gamma+u$, zero-fold measure $[X]$, and
zero gap. Abstract compact spaces with local charts are a different
category; only the exact compact scope and bounded-decomposition
hypotheses of caller B225/R230 apply there. No compact embedded
positive-dimensional cycle is manufactured.

# What is resolved and what remains

The new coupled finite example, the corrected finite contact/circuit
results, and the explicit non-PA example are proved at actual compatible
global functions, with actual growth and genuine measured endpoints. The
local-jet gluing theorem realizes every rational-coefficient finite PC
germ in the real category with the actual rational-affine reference, and
rational approximation preserves bad jets on their fixed fan. The raw
completion theorem resolves the operator independence issue on the
stated regularizable domain for rational-affine positive-growth
references, including literal references; it does not prove every
continuous envelope is in that domain. Its auxiliary rational maximum
construction is not asserted for arbitrary irrational reference slopes.
The original real-category classification still lacks necessary and
sufficient structural conditions valid for all bounded continuous
obstacles, domain membership of every such envelope, the correct local
contact condition for general non-PA germs, and realizability of every
bad germ with the actual reference. For rational-affine positive-growth
references the new jet realization removes that global compatibility
premise in the finite PA sector. For arbitrary irrational reference
coefficients, the earlier criterion still quantifies only actual global
relative PA functions. A fixed semialgebraic system supplies no uniform
refinement bound. Correct total mass, positive growth, and positive
balancing remain insufficient for contact.

The preserved failed source is not silently edited. The strict-floor PC
assumption is a material hypothesis correction, and the new coupled
reference/endpoint replace the old separable endpoint. The reader196
comments are checked data, not new grants. The only supplied grants used
without reconstruction are the exact B225 positive-spanning and
compact-support statements, R230’s continuous-completion/envelope and
rational cone-generation statements, with all their clarifications. A224
is preserved context; none of its fan-specific conclusions is applied to
this two-plane space. Native note support fields contain only earlier
local IDs returned here.

# Exact evidence and reproduction

The standard-library checker `check_certificates.py` enumerates active
affine triples over exact fractions for both planes, checks primitive
transverse lifts, all displayed first-cycle balances, recursive atoms,
polygon areas independently, finite radial chords, coupling corners,
dyadic chord errors and the non-PA atom formulas. It also checks the
corrected-floor line counterexample and the two lattice covolume
conversions in an oblique saturated plane. These are exhaustive finite
checks only on their printed lists. The mathematical proofs do not infer
continuum maximality, operator independence, or contact from a compiler,
hash, polygon, or finite grid.

The exact frozen BMPS and BBGS byte lengths and supplied SHA-256 hashes
were verified; the files remain read-only. The quote-free source ledger
records complete essential proof units and exact applications. The BBGS
primitive-to-unit conversion is made at every recursive dimension,
including signed or zero intermediate weights. The general source
regularization/operator theorem is not an imported grant. Our added
operator proof uses the reconstructed edge integration identities,
auxiliary rational PA tests, degree bound and tightness argument.

The full argument is in `argument.md`; structured notes are in
`notes.json`; material changes are in `material-changes.md`. The old
TeX, argument, ledger, FAIL report and unregistered notes are retained
without edits under `preserved/`. Commands, outputs, environment
information and provenance are in `evidence/` and
`execution-commands.md`. Rerun with existing tools:

    python check_certificates.py
    python rebuild_paper.py
    pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
    python build_artifacts.py

No software installation, account/runtime/network modification, external
communications, private-stream inspection or protected-file edit was
performed. No resource-heavy computation was launched; no
operator-provided supervised compute service was exposed. The requested
model route was not selectable or independently verified by the exposed
tools, so no model switch is claimed. The managed runtime skill was
read; its environment-status tool was not exposed. Compilation and
execution are reproducibility observations, not mathematical correctness
grants. This is an unverified draft; original P05.2 remains open and
candidate status is false.

<div class="thebibliography">

9 A. M. Botero, E. Mazzon, L. Pille–Schneider, *Monge–Ampere measures on
balanced polyhedral spaces*, arXiv:2603.08664v1, submitted 9 March 2026,
manuscript 10 March 2026. <https://arxiv.org/pdf/2603.08664v1>. A. M.
Botero, J. I. Burgos Gil, M. Sombra, *Convex analysis on polyhedral
spaces*, Math. Z. 301 (2022), 1631–1674, publisher version, 24 January
2022.
<https://link.springer.com/content/pdf/10.1007/s00209-021-02869-6.pdf>.
Supplied accepted caller paper A224, *A strict-growth contact
obstruction on the $U_{3,4}$ Bergman fan*, complete body and harmless
clarifications retained locally. Supplied accepted caller paper B225,
*Positive balancing, compact support, and a polyhedral maximum
principle*, complete body and harmless clarifications retained locally.
Supplied accepted caller paper R230, *Continuous completion of
rational-endpoint polyhedral convexity*, complete body and harmless
clarifications retained locally.

</div>
