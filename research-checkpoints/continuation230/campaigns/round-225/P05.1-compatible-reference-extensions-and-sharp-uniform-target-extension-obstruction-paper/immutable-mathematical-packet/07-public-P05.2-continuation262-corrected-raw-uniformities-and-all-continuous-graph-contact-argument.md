---
abstract: |
  Global weak uniform continuity of the earlier raw completion claim is
  false. We reconstruct actual literal and real PA counterexamples, and
  replace that guarantee by continuity for weak bounded-continuous
  tests, global uniform continuity for vague compact tests, and weak/BL
  uniform continuity on each fixed relative sup-bound family. A common
  moment bound is proved for every completed tuple in such a family. All
  prior finite circuit/contact, actual rational-reference jet
  realization, genuine mixed raw completion, coupled PA and quadratic
  non-PA obstructions are reconstructed with their domains. Beyond this
  repair, we prove real regularization, a genuine raw operator, and
  exact contact for all bounded continuous obstacles on finite balanced
  graphs, for arbitrary real PA positive-growth references, precisely
  when each positive tangent-relation cone is its actual weight ray. The
  full higher-dimensional and arbitrary-reference original P05.2 remains
  open. These are unverified scoped research results; candidate status
  is false.
author:
- Research draft
date: 7 October 2026
title: |
  Raw polyhedral completion with corrected uniformities and graph
  contact\
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
Section [10](#extension-section){reference-type="ref"
reference="extension-section"} constructs an extension on an explicitly
proved approximation domain.

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
and ROOT249 are unreviewed data, not additional grants. Native194's
unknown-support failure is retained; caller labels are explained in text
and are never local-note supports.

The whole255 source, all seven exact native197 final notes, complete
independent200 FAIL and its binding remain unchanged in `preserved/`.
Its Theorem 11 and native note n4 claimed global weak uniform
continuity. The actual line counterexamples in
Theorem [11](#uniform-failure){reference-type="ref"
reference="uniform-failure"} disprove that claim. The replacement is a
material scope restriction, with each output topology and each common
relative bound quantified explicitly. Favorable review discussion is not
a mathematical grant. Exactly the three complete supplied A224/B225/R230
bodies and their unchanged clarifications are caller grants; new
applications are reconstructed.

R230 gives the continuous dominating completion of every finite
printed-PC competitor on this domain, preserving continuous obstacles
and its actual growth upper bound. It identifies
[\[env\]](#env){reference-type="eqref" reference="env"} with the
continuous-competitor envelope for every bounded continuous obstacle. We
use this theorem without reproving it. B225 gives positive spanning of
every positive balanced star. A224's local-support argument motivates a
lemma that we reconstruct below on the present general domain. We do not
promote its fan-specific main theorem to a theorem on arbitrary spaces.
All actual grant applications retain their stated hypotheses.

We make no use of a strict-convexity theorem. Our zero-cost tests
discard zero-coefficient terms. The printed BMPS strictness wording
counts endpoint indices even though coefficients may be zero; that
separate degeneracy is not repaired or used here. A224's strictness
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
$\ell$ in [\[raw\]](#raw){reference-type="eqref" reference="raw"}.
Tangential contributions vanish and Euclidean balancing cancels the
remaining contribution of $\ell$. Thus BBGS's product $B$, with its
negative sign, satisfies $$\label{convert}
 B_{-f}(ac)(\tau)
 =\sum_{\sigma\succ\tau}a_\sigma c(\sigma)f_\sigma(\nu_{\sigma/\tau})
 =a_\tau D_f c(\tau).$$ To fit BBGS's hyperplane convention, embed $x$
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
are precisely Proposition 3.19's balancing and subdivision conclusions.

Equation [\[convert\]](#convert){reference-type="eqref"
reference="convert"} transfers all these conclusions to the primitive
lattice product, step by step, including real affine coefficients.
Tangential lift independence follows directly by replacing $n$ by $n+t$
in [\[raw\]](#raw){reference-type="eqref" reference="raw"}: the added
terms cancel because the two linear parts agree on $N_\tau$. The
reconstructed local-support lemma applied to each intermediate
nonnegative balanced cycle shows positivity. Thus
$\operatorname{MA}_{\mathrm{poly},*}(f)$ is a genuine, nonnegative,
finite, refinement-independent raw measure for every finite PA PC $f$
used below. At every step the carrying structure and its saturated
lattices are specified; arbitrary analytic multiplicities or ambient
Alexandrov mass are never substituted.

# The finite local slope cone

::: {#localglobal .lemma}
**Lemma 1** (Local supports imply global PCC inequalities). *On the
present embedded complex, a continuous function with an ambient affine
local support at every point satisfies every real-endpoint PCC. For a PA
function these supports make $D_f c$ nonnegative for every nonnegative
balanced cycle $c$ on a common carrying structure.*
:::

::: proof
*Proof.* Restrict to any segment contained in $X$ and subtract its
endpoint chord. If the continuous difference has a positive maximum, its
maximum set lies in the open segment and is nonempty and closed. At a
maximum point, a supporting affine function must have zero segment
slope: otherwise it would exceed the maximum on one side. The support
then makes the maximum set open. Connectedness contradicts the zero
endpoint values. Thus the restriction lies below every chord and is
convex. At a PCC center $x$, the segment to each endpoint $x_i$ lies in
its incident convex cell. If $\ell$ is the linear part of a local
support at $x$, comparison at $x+t(x_i-x)$ with the segment's endpoint
chord gives $f(x_i)\geq f(x)+\ell(x_i-x)$. Sum the endpoint inequalities
with their coefficients; the barycenter cancels the linear terms. For
the divisor, a support at a relative interior point of $\tau$ agrees
with $f_\tau$ on its tangent space. Subtract that support in
[\[raw\]](#raw){reference-type="eqref" reference="raw"}; balancing
cancels its tangent correction, and each remaining inward slope is
nonnegative. Every application to a divisor uses PA $f$ and a common
carrying structure. ◻
:::

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

::: {#supports .lemma}
**Lemma 2** (Finite supports). *A continuous finite PA function is PC if
and only if, at every face germ, there is an ambient linear form
$\ell_p$ with $$\ell_p(d_i)\leq s_i\quad(1\leq i\leq m).$$ Equivalently
$s\cdot\lambda\geq0$ for all $\lambda\in K(U)$. These conditions give
finitely many rational linear inequalities in the affine coefficients on
any specified finite rational structure. No simplicial or matroid
hypothesis is needed.*
:::

::: proof
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
represented vector's norm. A converging sequence thus has a subsequence
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
every real point. Lemma [1](#localglobal){reference-type="ref"
reference="localglobal"} proves every PCC inequality globally, giving
sufficiency without identifying PC with globally ambient convex
functions.

Finally $K(U)$ is a rational polyhedral cone. Its extremal generators
have minimally dependent positive supports, with one-dimensional kernel
on each support. Such supports have at most $\operatorname{rank}(U)+1$
elements. Gaussian elimination gives rational generators, and there are
finitely many subsets to inspect. These generators span $K(U)$, by the
same finite cone geometry used in R230. Testing them gives the asserted
finite rational inequalities. ◻
:::

At a vertex $v$, call a nonzero $\lambda\in K(U)$ with $s\cdot\lambda=0$
a *flat relation*. This means equality in a nontrivial local PCC, not
zero raw mass. It does not depend on the chosen finite generating list:
any local directions can be resolved inside their assigned cones into
generators and conversely generator relations are local PCCs.

::: {#floor .lemma}
**Lemma 3** (Strict affine floor). *Assume explicitly that the finite PA
germ at the vertex is PC, equivalently $s\cdot\lambda\geq0$ for every
$\lambda\in K(U)$. Under this hypothesis, absence of flat relations is
equivalent to existence of an ambient linear form $\ell$ with
$$h_v(x)-\ell(x)>0\quad
       \text{for every nonzero }x\text{ in the tangent support}.$$ In
that case $h_v(x)-\ell(x)\geq c\|x\|$ there for some $c>0$.*
:::

::: proof
*Proof.* By B225 the generator cone of the positive balanced star is its
span, so $K(U)\cap\{\sum\lambda_i=1\}$ is nonempty and compact. The PC
hypothesis makes every relation cost nonnegative. If there is no flat
relation, the minimum of $s\cdot\lambda$ on this section is a positive
number $\theta$. Choose $0<\delta<\theta$. Then $s-\delta{\bf1}$ pairs
nonnegatively with every element of $K(U)$. The separation argument in
Lemma [2](#supports){reference-type="ref" reference="supports"} supplies
$\ell$ with $s_i-\ell(d_i)\geq\delta$ for every generator. On each cone
a nonzero vector has a nonnegative generator representation, so its
residual is strictly positive. The union of the finitely many cone
sections on the unit sphere is compact; the continuous residual has
positive minimum $c$. Conversely any such strict residual pairs
positively with every nonzero element of $K(U)$, excluding a flat
relation. Common lineality is handled by its two opposite generators; a
linear germ on it automatically has a flat relation. ◻
:::

# A necessary local contact condition

::: {#necessary .theorem}
**Theorem 4** (Noncontact forces a flat relation). *Let $\gamma$ be a
continuous PC reference, $u$ bounded continuous, and suppose the actual
envelope $P_\gamma(u)=f$ is finite PA. If $f(v)<\gamma(v)+u(v)$ at a
vertex of a rational carrying structure for $f$, its germ at $v$ has a
flat relation. This assertion makes no measure or approximation
assumption.*
:::

::: proof
*Proof.* The finite envelope is PC: each competitor satisfies Jensen,
and taking the pointwise supremum preserves its inequality. Thus its PA
germ has nonnegative relation costs. Suppose there is no flat relation
and apply the corrected Lemma [3](#floor){reference-type="ref"
reference="floor"} with this established hypothesis. In a sufficiently
small ambient ball about $v$, the space is exactly its truncated tangent
star and $f(v+x)=f(v)+h_v(x)$. Shrink its radius $r>0$ so that the
continuous obstacle gap is greater than some $\eta>0$ throughout its
intersection with $X$. For $0<t<\min(\eta,cr/2)$, define in this ball
$$F(v+x)=\max\{f(v+x),\,f(v)+t+\ell(x)\},$$ and put $F=f$ outside it.
Since $h_v-\ell\geq c\|x\|$, these definitions agree on the collar
$r/2<\|x\|<r$. Also $0\leq F-f\leq t$, so $F$ is continuous, lies below
the obstacle, and has the same growth upper bound as $f$.

At an interior point of the modified region where the affine floor is
active, that floor is a local support. Where $f$ is active, a local
support of $f$ from Lemma [2](#supports){reference-type="ref"
reference="supports"} remains a support of $F$. This also covers tie
points, and the collar is unchanged. Lemma
[1](#localglobal){reference-type="ref" reference="localglobal"}
therefore proves $F\in\operatorname{PC}_q(X)$. It is an actual
competitor in [\[env\]](#env){reference-type="eqref" reference="env"},
with $F(v)=f(v)+t$, contradicting maximality. The inserted floor need
not be PA on a rational structure; competitors in
[\[env\]](#env){reference-type="eqref" reference="env"} are not
restricted to PA. No operator is assigned to it. ◻
:::

In particular a finite PA endpoint can have positive noncontact raw mass
only on the boundary of the local slope cone specified by a flat
relation. The theorem is not a claim that every such boundary point is
globally growth-compatible.

# Global realization of every compatible PA obstruction

::: {#obstruction .theorem}
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
:::

::: proof
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
:::

This theorem needs global compatibility of $f$, which is the explicitly
stated bounded-difference condition with the *actual* reference. It does
not assert that every abstract bad local germ can be extended through
the remaining complex. Positive growth alone is not used to replace that
condition.

::: {#scoped .corollary}
**Corollary 6** (Exact finite-PA-endpoint characterization). *For a
fixed pair and fixed coefficient category, the following are
equivalent:*

1.  *Every admissible PA obstacle whose actual envelope belongs to
    $\operatorname{PAPC}_*(X,\gamma)$ has zero raw contact integral.*

2.  *Every $f\in\operatorname{PAPC}_*(X,\gamma)$, at every vertex of a
    rational carrying structure, satisfies: $m_v(f)>0$ implies absence
    of a flat relation.*

*Here the reference is explicitly PA PC in the chosen category, as
required by Theorem [5](#obstruction){reference-type="ref"
reference="obstruction"}. The second condition contains neither an
obstacle nor a contact integral. This is a classification of the finite
PA endpoint sector, not original P05.2 with all regularizable
endpoints.*
:::

::: proof
*Proof.* If (2) holds, the finitely many positive atoms of a PA envelope
are contact points by Theorem [4](#necessary){reference-type="ref"
reference="necessary"}; every term in its atomic contact integral
vanishes. Conversely a violation of (2) gives the admissible obstacle
and negative integral in Theorem [5](#obstruction){reference-type="ref"
reference="obstruction"}, whose endpoint is in the stated PA category. ◻
:::

# A finite algebraic test with actual global growth

Fix a finite rational carrying structure $\Pi$ for $\gamma,[X]$.
Parameterize affine linear parts and constants of $f$ on its cells by
coefficients $z$. Equality of the affine restrictions on shared faces is
a finite rational linear system: test a rational affine basis of each
face. Lemma [2](#supports){reference-type="ref" reference="supports"} at
every face gives a finite system $Az\geq0$. For each generator $r$ of
$\operatorname{rec}(\sigma)$, impose $$\label{growth}
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
[\[raw\]](#raw){reference-type="eqref" reference="raw"} makes $m_v(z)$ a
homogeneous degree-$d$ polynomial in the linear parts, with the actual
top weights and primitive saturated normals as coefficients. Let
$\kappa_{v,j}$ be the finitely many normalized extreme relations at $v$,
and $s_v(z)$ its generator slope vector. The existence of a bad relative
$\operatorname{PA}_\mathbb R$ function *carried by this structure* is
exactly the finite disjunction of systems $$\label{test}
 \text{shared-face equations},\quad Az\geq0,\quad
 \eqref{growth},\quad
 s_v(z)\cdot\kappa_{v,j}=0,\quad m_v(z)>0.$$ A flat relation has zero
cost on some extreme relation because all extreme costs are nonnegative.
Thus [\[test\]](#test){reference-type="eqref" reference="test"} is an
actual semialgebraic obstruction test, not total mass or orthogonality
renamed. A feasible point gives a global certificate and the roof
obstacle. In the literal category impose integral coordinates of each
tangent linear part in a saturated lattice basis and rational affine
constants as well. A real feasible point is not automatically a literal
one.

Nonsimplicial stars use all their generators and shared-face equations;
no replacement by an ambient strong-convexity cone occurs. Nonsaturated
input directions must first be replaced by the saturated tangent lattice
normals in [\[raw\]](#raw){reference-type="eqref" reference="raw"}; the
relation cone alone does not encode their intersection indices. Genuine
common lineality has a linear restriction of the germ and hence flat
opposite generators. If a germ is invariant modulo an affine function
along nonzero common lineality, its raw top atom is zero: on the
generalized carrying fan every face contains that lineality, so there
are no zero-dimensional faces. Refinement independence keeps that zero
result if artificial cuts create a vertex.

Testing one structure is not testing all rational refinements, and even
testing all structures only gives Corollary
[6](#scoped){reference-type="ref" reference="scoped"}'s finite-PA
sector. No bound on the structures needed for arbitrary envelopes is
proved here.

# A genuinely coupled two-plane obstruction {#coupled-section}

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

Lemma [2](#supports){reference-type="ref" reference="supports"} does
give a finite linear feasibility system for PC affine coefficients on a
*specified* structure. Together with shared-face, obstacle, and growth
constraints it gives valid finite PA trial competitors. It does not
prove that this structure carries the unrestricted envelope, that a
finite number of hull iterations suffices, or that all structures have a
uniform approximation theorem. R230 supplies continuity but none of
those conclusions.

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

# Global realization of finite local jets for rational references {#jet-section}

Here $\gamma$ is rational affine on a finite rational structure, PC, and
positive at infinity. The target coefficient category is the explicitly
real scalar extension, even when $\gamma$ is literal. We do not assert
that the following scaling/gluing is literal.

::: {#jet-realization .theorem}
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
:::

::: proof
*Proof.* The space equals its truncated tangent star in a sufficiently
small rational norm ball about $v$; insert $v$ and the chosen local
rational fan subdivision. The finite linear pieces of $h$ give
$|h(x)|\leq L\rho(x)$ on this tangent support for some $L$. Choose
rational $\varepsilon>0$ so the ambient $\varepsilon\rho(x-v)$ has
recession slopes strictly smaller than those of $\gamma$. The coercive
linear lower bound proved in Lemma [10](#test-dc){reference-type="ref"
reference="test-dc"} permits this choice. Take rational $C>\gamma(v)$
and put $$\Psi(x)=\max\{\gamma(x),C+\varepsilon\rho(x-v)\}.$$ Both
entries have local supports. The maximum is rational-affine PA PC,
agrees with $C+\varepsilon\rho$ near $v$, and differs boundedly from
$\gamma$, because its second entry is below $\gamma$ outside a compact
set. Choose a rational star radius $r>0$, and rational $\delta>0$ with
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
:::

::: {#local-finite .corollary}
**Corollary 8** (Structural finite-PA contact criterion). *For
rational-affine positive-growth $\gamma$, real-category contact for all
bounded real PA obstacles whose actual envelopes are finite relative PA
is equivalent to the following condition on the weighted rational
geometry of $X$: at every rational point and every finite rational
refinement of its tangent star, each PC homogeneous PA jet with a flat
relation has zero raw top atom. This condition contains no actual
reference or global extension premise; its raw recursion uses the
saturated tangent lattices and actual weights.*
:::

::: proof
*Proof.* If the condition holds, apply it to the germ of any
positive-mass finite PA envelope vertex. There can be no flat relation
there, so the corrected noncontact theorem forces contact. Conversely a
bad local jet has a globally realized relative real PA function by
Theorem [7](#jet-realization){reference-type="ref"
reference="jet-realization"}. The exact roof theorem gives an admissible
real PA obstacle with that endpoint and strictly negative contact
integral. Its coefficient and regularizable antecedents are already
checked. ◻
:::

The universal quantifier over rational star refinements is essential.
Each fixed fan has the finite circuit/mass test already proved, but no
bound on the necessary refinements follows. This is now a geometric
criterion for the finite PA endpoint sector and this rational-reference
scope. It still does not classify all regularizable non-PA endpoints or
establish regularity for every continuous obstacle.

# A genuine extension on the regularizable domain {#extension-section}

This section goes beyond finite endpoints. Its reference hypothesis is
*rational affine coefficients on a finite rational structure*, not
arbitrary real coefficients. Literal references satisfy it. We retain
finite pure positively balanced embedded $X$, real finite raw
intersections, and positive growth of the actual reference $\gamma$. We
do not import BMPS Theorem 4.13 or Proposition 4.16: their needed
conclusions in this scope are reconstructed below. In particular no
operator is assigned just because an envelope is continuous.

::: {#raw-ibp .lemma}
**Lemma 9** (Raw degree and integration by parts). *All mixed finite PA
PC functions $a_1,\ldots,a_d$ with bounded difference from $\gamma$ have
total raw mass $M=\deg(\gamma)$. For bounded finite PA $b,c$ and any
intermediate balanced one-cycle $Z$, $$\int bD_c Z=\int cD_b Z.$$ Both
statements allow real coefficients and zero intermediate weights.*
:::

::: proof
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
:::

::: {#test-dc .lemma}
**Lemma 10** (Test functions as differences of relative PC functions).
*Let $\psi$ be a compactly supported ambient continuous PA function with
rational affine coefficients on a finite rational complex in
$N_\mathbb R$. There are rational $\varepsilon>0$ and rational-affine
relative PA PC functions $\theta_0,\theta_1$ on $X$ such that
$\theta_1-\theta_0=\varepsilon\psi|_X$.*
:::

::: proof
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
:::

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

::: {#uniform-failure .theorem}
**Theorem 11** (Failure of global weak uniform continuity). *On the
balanced unit-weight line with actual reference $\gamma(x)=|x|$, the
finite raw operator is not globally uniformly continuous for the weak
uniformity generated by $C_b(\mathbb R)$, even on literal relative PA PC
functions. On the real relative PA domain it is not globally uniformly
continuous for the bounded-Lipschitz metric either.*
:::

::: proof
*Proof.* For integers $n\geq1$, put $A_n=|x-2n|$ and
$B_n=|x-2n-1/(8n)|$. A carrying structure has the rational vertices
$0,2n,2n+1/(8n)$ and their complementary edges. The affine formulas have
slopes $\pm1$ and rational constants. Both functions are ambient convex,
so satisfy every printed rational-endpoint PCC. Their differences from
the actual $|x|$ are bounded, with norms $2n$ and $2n+1/(8n)$; their two
recession slopes are one. They are actual literal PA PC endpoints with
constant decreasing regularizations. Primitive outgoing normals on the
line are $\pm1$. Away from each kink the opposite slopes cancel, while
the two outgoing slopes at the kink are both one. Thus
$$\operatorname{MA}_{\mathrm{poly}}(A_n)=2\delta_{2n},\quad \operatorname{MA}_{\mathrm{poly}}(B_n)=2\delta_{2n+1/(8n)},\quad
 \|A_n-B_n\|_\infty=1/(8n).$$ For the single fixed test
$\psi(x)=\sin(\pi x^2)$, which is bounded and continuous, the absolute
evaluation difference is $2\cos(\pi/(64n^2))\to2$. This violates one
fixed defining entourage of the weak $C_b$ uniformity.

For even $n$ let $a_j=4j$ for even $j$, $a_j=4j+1$ for odd $j$, and let
$b_j$ make the opposite choices, $0\leq j<n$. Set
$A_n=n^{-1}\sum_j|x-a_j|$, $B_n=n^{-1}\sum_j|x-b_j|$. Each sum is a
convex function on the rational line subdivision by these finitely many
integer points, with rational slopes and constants. Its outer slopes are
$-1,1$; hence it has bounded difference from $|x|$ and the prescribed
positive recession growth. It belongs to real PA on finite rational
carrying geometry and is already regularizable there. This need not be
literal PA. Raw linearity in the actual one-cycle gives
$$\operatorname{MA}_{\mathrm{poly}}(A_n)=\frac2n\sum_j\delta_{a_j},\qquad
 \operatorname{MA}_{\mathrm{poly}}(B_n)=\frac2n\sum_j\delta_{b_j}.$$ For
a pair $j=2k,2k+1$, its unnormalized difference is
$$|x-8k|-|x-8k-1|+|x-8k-5|-|x-8k-4|.$$ It vanishes outside $[8k,8k+5]$,
rises linearly from zero to two on $[8k,8k+1]$, equals two on
$[8k+1,8k+4]$, and falls to zero on $[8k+4,8k+5]$. These pair intervals
are disjoint. Therefore $0\leq A_n-B_n\leq2/n$ and the uniform distance
is exactly $2/n$. Let $\eta$ be the continuous eight-periodic linear
interpolation through $(0,1/4),(1,-1/4),(4,-1/4),(5,1/4),(8,1/4)$. It
has sup norm $1/4$ and Lipschitz constant $1/2$; it belongs even to the
convention $\|\eta\|_\infty+\operatorname{Lip}(\eta)\leq1$. Its values
at every $a_j,b_j$ are $1/4,-1/4$, respectively, so the raw measure
evaluation difference is exactly one for every even $n$.

The relative norm of a sum of these shifted absolute values against
$|x|$ is exactly its average shift: the triangle inequality gives the
upper bound, attained on $x\leq0$. Both averages equal
$2(n-1)+1/2=2n-3/2$. They grow without a common fixed bound. These
families are not uniformly convergent to one relative function. The
failure concerns global uniform continuity, not the convergence result
proved next. It is a material restriction of the old guarantee. ◻
:::

We specify all output notions. The vague topology and uniformity are
generated by finite lists of evaluations $\nu\mapsto\int g\,d\nu$,
$g\in C_c(X)$. The weak $C_b$ topology and uniformity use finite lists
with $g\in C_b(X)$. Fix a Euclidean metric on $X$ and define
$$d_{\rm BL}(\mu,\nu)=\sup_{\|g\|_\infty\leq1,\ \operatorname{Lip}(g)\leq1}
              \left|\int g\,d(\mu-\nu)\right|.$$ All measures below have
the same finite raw mass $M$. The domain metric on tuples is
$d_\infty(\mathbf f,\mathbf g)=\sum_i\|f_i-g_i\|_\infty$. For each
category $*$, let $\mathcal D_*(\gamma)$ be the uniform closure of the
actual relative $\operatorname{PAPC}_*$ functions in continuous
functions of bounded difference from the same actual reference. No other
continuous PC function is added by definition.

::: {#radon-lemma .lemma}
**Lemma 12** (Positive-functional representation). *On the closed finite
polyhedral metric space $X$, every positive linear functional $L$ on
$C_c(X)$ satisfying $|L(g)|\leq M\|g\|_\infty$ is integration against a
unique finite positive Radon measure of mass at most $M$.*
:::

::: proof
*Proof.* For open $O$, define
$\alpha(O)=\sup\{L(h):h\in C_c(X),0\leq h\leq1,
\operatorname{supp}h\subset O\}$. It is at most $M$. If
$O\subset\bigcup_iO_i$, the compact support of any such $h$ has a finite
subcover. A continuous partition on a neighborhood of that support, with
compact supports subordinate to the selected opens, exists by taking
finitely many small relatively compact balls, continuous distance
cutoffs, and dividing their sum where it is positive. It splits $h$ into
nonnegative functions $h_i\leq1$ supported in $O_i$. Hence
$\alpha(O)\leq\sum_i\alpha(O_i)$. For disjoint opens finite sums of
admissible tests are again at most one; taking suprema gives
$\alpha(\bigcup_iO_i)\geq\sum_i\alpha(O_i)$, first for finite sums and
then for all finite partial sums.

Set $\mu^*(A)=\inf_{O\supset A}\alpha(O)$ over open supersets. Choosing
open supersets within arbitrary summable errors proves countable
subadditivity, so this is an outer measure. If two sets have positive
distance, their disjoint distance neighborhoods, intersected with any
open superset of their union, give $\mu^*(A\cup B)=\mu^*(A)+\mu^*(B)$.
Here is the Borel measurability step in detail. For a closed $E$ and
arbitrary $A$, put $A_j=A\cap\{\operatorname{dist}(x,E)\geq2^{-j}\}$.
Separated-set additivity gives $\mu^*(A)\geq\mu^*(A\cap E)+\mu^*(A_j)$.
The shells of $A\setminus E$ between successive positive dyadic
distances have finite total outer mass: any finite collection of
even-index shells is pairwise separated and has summed outer mass at
most $M$, and the same is true for odd-index shells. Consequently the
sums of all shell masses converge and their tails tend to zero.
Countable subadditivity then gives
$\mu^*(A\setminus E)\leq\lim_j\mu^*(A_j)$. This is the Caratheodory
inequality for $E$; its reverse is subadditivity. Thus all closed, hence
all Borel, sets are measurable. The restriction $\mu$ is a countably
additive finite measure, since the outer-measure identity for measurable
disjoint sets and continuity of finite partial sums give countable
additivity.

For open $O$ one has $\mu(O)=\alpha(O)$ directly by monotonicity in open
supersets. If $h$ is an admissible test and $K=\operatorname{supp}h$,
then $L(h)\leq\alpha(W)$ for every open $W\supset K$, whence
$L(h)\leq\mu(K)$. This proves inner compact regularity on opens; outer
regularity is the definition of $\mu^*$. For a Borel set, choose an open
superset of arbitrarily small excess measure and apply inner regularity
to its complement in a sufficiently large compact set. Since $\alpha(X)$
is approximated by compactly supported tests, such compact sets exhaust
its mass. This proves inner regularity on all Borel sets as well.

For $g\in C_c(X)$ nonnegative, let $R=\|g\|_\infty$ and $\delta=R/n$.
Tests $h_k$ supported in $\{g>k\delta\}$ satisfy
$\delta\sum_{k=1}^n h_k\leq g$; maximizing each of their functional
values gives the lower bound
$L(g)\geq\delta\sum_{k=1}^n\mu\{g>k\delta\}$. For the upper bound choose
a compact cutoff equal to one on $\operatorname{supp}g$, and for each
$k\geq1$ a test equal to one on the compact set $\{g\geq k\delta\}$ and
supported in $\{g>(k-1)\delta\}$. Their sum times $\delta$, together
with $\delta$ times the first cutoff, majorizes $g$. Thus
$L(g)\leq\delta M+\delta\sum_{k=1}^n\mu\{g>(k-1)\delta\}$. The two sums
differ by at most $\delta M$ and also bracket the integral of $g$ by
elementary pointwise step bounds. Letting $n\to\infty$ proves
$L(g)=\int g\,d\mu$. Signed functions follow by their positive and
negative parts. Conversely, compact cutoffs and inner regularity recover
open-set masses from these integrals, proving uniqueness. ◻
:::

::: {#raw-extension .theorem}
**Theorem 13** (Raw completion with the exact continuity scopes). *Fix
finite pure positively balanced embedded rational $X$ and the actual
rational-affine PA PC positive-growth reference $\gamma$ of this
section. For $*=\mathbb Z,\mathbb R$, the finite raw mixed operator
extends uniquely to $\mathcal D_*(\gamma)^d$. Its outputs are positive
finite Radon measures of raw mass $M=\deg(\gamma)$; the extension is
symmetric, local, and agrees with the finite raw recursion. Arbitrary
uniformly convergent PA approximants give the same limit against every
$C_b$ test.*

*The extension is continuous from the uniform domain topology into the
weak $C_b$ topology (for sequences and nets). It is globally uniformly
continuous into the vague $C_c$-test uniformity. For *each fixed*
$0\leq C<\infty$, on
$$\mathcal F_{*,C}=\{(f_1,\ldots,f_d)\in\mathcal D_*(\gamma)^d:
                   \max_i\|f_i-\gamma\|_\infty\leq C\},$$ it is
uniformly continuous into the weak $C_b$ uniformity and in $d_{\rm BL}$.
These last two assertions have no entire-domain uniform-continuity
conclusion. If $M=0$, all outputs are zero and all the asserted
continuity properties are immediate.*
:::

::: proof
*Proof.* Assume $M>0$. For a compact ambient rational PA test $\psi$,
the preceding DC lemma gives $\theta_1-\theta_0=\varepsilon\psi$ with
actual relative real PA PC functions and fixed $\varepsilon>0$. For two
relative finite PA PC tuples, telescope one factor at a time. The other
factors form positive balanced one-cycles $Z_i$, so bounded edge
integration by parts and raw positivity give $$\label{test-estimate}
 \left|\int\psi\bigl(\operatorname{MA}_{\mathrm{poly}}(\mathbf a)-\operatorname{MA}_{\mathrm{poly}}(\mathbf b)\bigr)\right|
 \leq \frac{2M}{\varepsilon}\sum_i\|a_i-b_i\|_\infty.$$ Indeed
$D_\psi Z_i=(D_{\theta_1}Z_i-D_{\theta_0}Z_i)/\varepsilon$ has total
variation at most $2M/\varepsilon$. This constant depends on the test
and actual reference, *not* on relative sizes of $\mathbf a$ or
$\mathbf b$. Auxiliary real functions are legitimate even when the
approximating tuples are literal, because their finite real raw
recursion has already been established; no new literal endpoint is
inferred.

For a uniform-Cauchy tuple of approximants, the integrals in
[\[test-estimate\]](#test-estimate){reference-type="eqref"
reference="test-estimate"} are Cauchy. Uniform density of compact
rational PA tests in $C_c(X)$, with supports controlled as proved above,
and the common mass $M$ show that every $C_c$ integral is Cauchy:
replacing a test within $\eta$ costs at most $2M\eta$ in a difference.
The limits define a positive linear functional bounded by
$M\|g\|_\infty$. Lemma [12](#radon-lemma){reference-type="ref"
reference="radon-lemma"} gives its unique positive Radon measure $\mu$.

We prove mass and tightness without changing the actual reference.
Choose a fixed rational $c\geq0$ so $H=\gamma+c\geq0$ on $X$. This is
possible by the coercive lower bound; $H$ is a proper height. The raw
reference measure remains $\operatorname{MA}_{\mathrm{poly}}(\gamma)$ by
constant invariance. Put
$J=\int H\operatorname{MA}_{\mathrm{poly}}(\gamma)<\infty$, and for
integers $j\geq1$ set $$q_j=\max(\gamma+c-j,0)-c=\max(\gamma-j,-c).$$
These are relative rational-affine PA PC functions on finite rational
structures; $\gamma-q_j=\min(H,j)$. For a finite tuple with
$\max_i\|a_i-\gamma\|_\infty\leq D$, apply the previously proved
relative IBP identity with $q=q_j$. Split
$a_1-q_j=(a_1-\gamma)+(\gamma-q_j)$. The first two terms have absolute
values at most $DM$ each, by positive mixed measures of mass $M$. The
remaining term replaces $a_1$ by $\gamma$. Repeat through all $d$
factors, obtaining $$\label{moment}
 \int\min(H,j)\operatorname{MA}_{\mathrm{poly}}(\mathbf a)\leq2dDM+J=:K_D.$$
Monotone convergence over $j$ gives the same bound for $\int H$.
Consequently
$\operatorname{MA}_{\mathrm{poly}}(\mathbf a)\{H>T\}\leq K_D/T$.

A particular uniformly convergent family of approximants has one finite
$D$. Choose continuous compact cutoffs $\chi_T$ equal to one on
$\{H\leq T\}$, with $0\leq\chi_T\leq1$. Vague convergence gives
$\int\chi_T\,d\mu\geq M-K_D/T$ and the representation gives
$\mu(X)\leq M$. Hence $\mu(X)=M$. Nonnegative compact tests majorized by
$H$ pass to the limit with the same bound $K_D$. Their suprema, or an
increasing exhaustion of $H$ by compact cutoffs, give
$\int H\,d\mu\leq K_D$. Truncating a fixed $g\in C_b(X)$ by $\chi_T$
costs at most $\|g\|_\infty K_D/T$ for either the approximant or the
limit. Vague convergence of the truncated test, then $T\to\infty$,
proves convergence against *each* $C_b$ test for this uniformly
convergent family. This reasoning has not bounded every relative tuple
by one $D$.

Comparing any two approximating tuples by
[\[test-estimate\]](#test-estimate){reference-type="eqref"
reference="test-estimate"} proves sequence independence. Passing that
estimate along approximants for any two completed tuples gives *the
same* compact-test estimate on the completion. If
$\mathbf f\in\mathcal F_{*,C}$, choose approximants with uniform error
tending to zero, so their relative bounds are $C+o(1)$. Passing each
nonnegative compact height test in
[\[moment\]](#moment){reference-type="eqref" reference="moment"} and
then taking its supremum gives the exact bound
$$\label{completed-moment}
 \int H\,d\operatorname{MA}_{\mathrm{poly}}(\mathbf f)\leq K_C=2dCM+J,
 \qquad \operatorname{MA}_{\mathrm{poly}}(\mathbf f)\{H>T\}\leq K_C/T
       \quad(\mathbf f\in\mathcal F_{*,C}).$$ Thus the common constant
applies to *all* completed tuples in this fixed-$C$ family, not just a
selected sequence. Using approximants within one would also give the
valid weaker constant $K_{C+1}$.

For a fixed $g\in C_c(X)$ approximate it uniformly within $\eta$ by one
compact rational PA test $\psi$. For *all* completed tuples,
$$|\langle g,\operatorname{MA}_{\mathrm{poly}}(\mathbf f)-\operatorname{MA}_{\mathrm{poly}}(\mathbf h)\rangle|
 \leq2M\eta+L_\psi d_\infty(\mathbf f,\mathbf h),\qquad
 L_\psi=2M/\varepsilon_\psi.$$ First choose $\eta$, then the input
distance. Finite lists use the minimum of finitely many input
thresholds. This proves global uniform continuity for the *vague*
uniformity.

Now fix $C$ once and for all and $g\in C_b(X)$. With the preceding
cutoff and a compact rational PA approximation to $\chi_Tg$ within
$\eta$, for every $\mathbf f,\mathbf h\in\mathcal F_{*,C}$ we have
$$\label{weak-fixed-C}
 |\langle g,\operatorname{MA}_{\mathrm{poly}}(\mathbf f)-\operatorname{MA}_{\mathrm{poly}}(\mathbf h)\rangle|
 \leq2\|g\|_\infty K_C/T+2M\eta+
                          L_\psi d_\infty(\mathbf f,\mathbf h).$$ Choose
$T,\eta$, then distance. Each is independent of the two tuples in this
fixed family. The same finite-list argument proves uniform continuity
for the weak $C_b$ uniformity on $\mathcal F_{*,C}$. At one completed
tuple $\mathbf f$, its input ball of radius one is contained in
$\mathcal F_{*,C_f}$ where $C_f=1+\max_i\|f_i-\gamma\|_\infty$. The last
assertion proves ordinary continuity at $\mathbf f$ into weak $C_b$,
including nets. A uniformly convergent family has a common finite $C$;
this is the exact scope of the all-$C_b$ convergence claim.

For the bounded-Lipschitz metric, use the same fixed $C$ and cutoff
$\chi_T$, and let $K=\operatorname{supp}\chi_T$. The restrictions to $K$
of tests $\|g\|_\infty\leq1$, $\operatorname{Lip}(g)\leq1$ have a finite
uniform $\eta$-net. To prove this, cover $K$ by finitely many balls of
radius $r$ and quantize the values at their centers with mesh $s$. Two
tests in the same occupied quantization class differ on $K$ by at most
$2r+2s$. Choose one actual global test from each nonempty class; there
are finitely many classes, and choosing $r,s$ small gives the asserted
net. Let its representatives be $g_1,\ldots,g_l$ and approximate each
$\chi_Tg_k$ by a compact rational PA $\psi_k$ within $\eta$. For any
test $g$, choosing the matching representative bounds the evaluation
difference for all tuple pairs in $\mathcal F_{*,C}$ by $$2K_C/T+4M\eta+
       \bigl(\max_k L_{\psi_k}\bigr)d_\infty(\mathbf f,\mathbf h).$$ All
constants are finite and tuple-independent on the *fixed-$C$* family.
Taking the supremum over $g$ proves $d_{\rm BL}$ uniform continuity
there. The counterexamples in
Theorem [11](#uniform-failure){reference-type="ref"
reference="uniform-failure"} prevent suppressing that quantifier.

Symmetry follows from finite raw symmetry. For locality, let two
limiting tuples agree in an open $O$, and take a compact rational PA
test supported inside $O$. In the telescoping proof $D_\psi Z_i$ is
supported in that compact subset of $O$, since the test is identically
zero on its open complement. Its variation bound therefore multiplies
only the argument difference on that support. Along approximants to the
two tuples this local difference tends to zero. Density of compact tests
with supports inside $O$ proves equality of output restrictions there.
Controlled support density follows by choosing the bump radii smaller
than the positive distance of the compact test support to
$X\setminus O$. Finite constant sequences show agreement with the
original raw operator; positivity has been preserved at every
construction step.

Finally choose approximants $a_n$ with $\|a_n-f\|_\infty\leq2^{-n}$ and
set $b_n=a_n+4\cdot2^{-n}$. Then
$b_n-b_{n+1}\geq2\cdot2^{-n}-(2^{-n}+2^{-n-1})=2^{-n-1}>0$ everywhere,
and $b_n\to f$ uniformly. These rational additions preserve both
coefficient categories and relative growth. Thus uniform completion is
exactly the declared decreasing regularizable domain. Uniqueness follows
from density of finite approximants and the Hausdorff vague measure
topology. No operator is assigned merely from PC continuity. ◻
:::

::: {#contact-stability .corollary}
**Corollary 14** (Stability of domain-checked contact integrals). *For
the actual reference of
Theorem [13](#raw-extension){reference-type="ref"
reference="raw-extension"}, let $u_n,u\in C_b(X)$, $u_n\to u$ uniformly,
and assume the actual envelopes $f_n,f$ belong to
$\mathcal D_*(\gamma)$. Then their exact contact integrals converge. One
may fix any finite $C\geq\sup_n\|u_n\|_\infty,\|u\|_\infty$; all these
envelopes lie in $\mathcal F_{*,C}$ and their measures converge in the
weak $C_b$ topology. This is a convergence theorem with these domain and
common-bound antecedents, not an all-obstacle regularity theorem.*
:::

::: proof
*Proof.* R230 applies on the actual finite positive balanced space with
continuous PC reference and bounded continuous obstacles. It gives
continuous unrestricted envelopes, the sandwich
$\gamma-\|u_n\|_\infty\leq f_n
\leq\gamma+\|u_n\|_\infty$, and $\|f_n-f\|_\infty\leq\|u_n-u\|_\infty$.
Their bounded continuous gaps $f_n-\gamma-u_n$ converge uniformly. The
fixed-$C$ weak convergence theorem and the common mass $M$ then prove
convergence of the gap integrals. Domain membership was assumed, not
deduced from this argument. ◻
:::

# A non-PA regularizable coupled endpoint with an explicit measure {#nonpa-section}

Keep the actual literal reference and balanced $X$ from
Section [7](#coupled-section){reference-type="ref"
reference="coupled-section"}. Define the even convex function
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
Theorem [13](#raw-extension){reference-type="ref"
reference="raw-extension"} supplies its genuine sequence-independent
extended raw measure.

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
[\[nonpa-atoms\]](#nonpa-atoms){reference-type="eqref"
reference="nonpa-atoms"} converge to ordinary Riemann integrals; the two
endpoint half-jumps tend to zero and $a_N\to a$ uniformly. Consequently
the sequence-independent measure is exactly $$\label{nonpa-measure}
 \operatorname{MA}_{\mathrm{poly},\mathbb R}(F)=12\delta_0+
 \sum_{s=\pm1}\int_1^2
 \left(4\delta_{(0,st,0)}+
       \delta_{(0,st,(t-1)^2/2)}+
       \delta_{(0,st,-(t-1)^2/2)}\right)\,dt.$$ This is a positive
measure of total mass twenty-four; its non-atomic part lies on two
segments and four parabolic arcs. Formula
[\[nonpa-measure\]](#nonpa-measure){reference-type="eqref"
reference="nonpa-measure"} specifies pushforward parameter measures, not
unexplained Euclidean arc-length factors.

Set $U=F-\gamma+(1/4-\rho)_+$ and $U_N=F_N-\gamma+(1/4-\rho)_+$. The
$U_N$ are bounded real PA obstacles on finite rational structures,
converging uniformly to the bounded continuous, non-PA obstacle $U$.
Inside the roof ball every $F_N$ and $F$ has exactly the same PA germ as
the coupled endpoint of
Section [7](#coupled-section){reference-type="ref"
reference="coupled-section"}. The rational flat pair, radial-chord, and
shrinking-simplex proof of that section therefore applies literally
there; outside it the direct obstacle bound is $q\leq F_N$ or $q\leq F$.
The function itself is a PC competitor. Thus the unrestricted envelopes
are respectively $F_N,F$, with no continuity assumption on competitors.
The measure in
[\[nonpa-measure\]](#nonpa-measure){reference-type="eqref"
reference="nonpa-measure"} has only its origin atom in the roof, and
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

# The literal antecedent on noncompact finite spaces {#literal-section}

The following is a reconstruction of the dossier's noncompact literal
obstruction, not an additional caller grant or a new claim of priority.
It clarifies the literal branch of the original task before any measure
is assigned to an endpoint.

::: {#literal-general .theorem}
**Theorem 15** (Noncompact literal obstruction). *Let
$X\subset N_\mathbb R$ be a noncompact finite rational polyhedral space,
and let $\gamma$ be literal PA PC and positive at infinity. Then some
bounded literal PA obstacle has an envelope with a positive uniform
distance from every literal PA PC function. Thus the pair fails the
all-PA-obstacle regularity antecedent. Balancing is not needed.*
:::

::: proof
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
literal uniform regularization. No literal extended Monge--Ampere
measure is assigned to this envelope. ◻
:::

In the fixed globally embedded BMPS category, B225's positive-balanced
compact-support theorem applies to every nonempty finite pure positive
balanced $X$ of dimension $d\geq1$. It is therefore noncompact, so
Theorem [15](#literal-general){reference-type="ref"
reference="literal-general"} excludes every such positive-growth literal
pair from the source's pair-level orthogonality domain, whose definition
presupposes regularity. This is a statement about that antecedent, not a
declaration that a nonregularizable endpoint has an orthogonality
measure. In dimension zero finite rational points have pointwise
envelope $\gamma+u$, zero-fold measure $[X]$, and zero gap. Abstract
compact spaces with local charts are a different category; only the
exact compact scope and bounded-decomposition hypotheses of caller
B225/R230 apply there. No compact embedded positive-dimensional cycle is
manufactured.

#### Zero-dimensional antecedents.

On a finite rational set, every point function is PC and the
unrestricted envelope for any bounded continuous obstacle is exactly
$\gamma+u$. In the real category it is finite PA. In the literal
category, even if its values are irrational, choose rational constants
at each point converging from above, and use the finite number of points
to obtain uniform decreasing convergence. Thus this endpoint is
genuinely in the literal completion as well. The raw zero-fold measure
is $[X]$ for every approximant and endpoint, independent of all choices.
Its contact gap vanishes pointwise. This does not produce a compact
embedded positive-dimensional balanced cycle or an operator on arbitrary
abstract chart functions.

# A further sector: every continuous obstacle on a finite graph {#graph-sector}

The new progress beyond the continuity repair is in dimension one. Here
we allow the *actual*
$\gamma\in\operatorname{PA}_\mathbb R(X)\cap\operatorname{PC}_q(X)$ to
have arbitrary real, including irrational, affine coefficients, on a
finite *rational* carrying graph. The graph is globally embedded,
finite, pure, and has actual positive real edge weights $w_e$ satisfying
lattice balancing. Its vertices and edge lengths in primitive
coordinates are rational. The conclusion is for *all* $u\in C_b(X)$, not
just finite PA obstacles. Abstract compact chart spaces are outside this
theorem.

For each vertex $v$ let $u_{e/v}$ be the primitive outgoing direction
and $$K_v=\{\lambda\geq0:\sum_{e\ni v}\lambda_eu_{e/v}=0\}.$$ The actual
weight vector $w_v$ is strictly positive and lies in $K_v$. We may
insert a rational bivalent vertex on a line without vertices; its cone
is one ray, and this does not change the operator or contact.

::: {#graph-slopes .lemma}
**Lemma 16** (Continuous graph slopes and supports). *A continuous
printed-PC function $f$ is ordinarily convex on every edge. Its outgoing
one-sided derivatives $d_{v,e}$ are finite at every vertex, and satisfy
$d_v\cdot\lambda\geq0$ for every $\lambda\in K_v$. Conversely,
continuous edgewise convex functions with these finite vertex
derivatives and inequalities satisfy every PCC. They have ambient affine
local supports at every point.*
:::

::: proof
*Proof.* Contained-edge Jensen inequalities pass from rational to real
endpoints by continuity; thus they give ordinary convexity. For rational
$t>0$ small enough on every germ, the endpoints $v+t u_{e/v}$ are
rational. The weighted relation $w_v$ gives
$\sum_e w_e(f(v+tu_{e/v})-f(v))/t\geq0$. Each quotient is nondecreasing
as $t$ increases, and is bounded above near zero by its finite quotient
at one fixed small radius. Its limit therefore lies in
$[-\infty,\infty)$; none can be $-\infty$, because all $w_e>0$ and all
other terms have fixed finite upper bounds. This proves finite
derivatives. Applying the same endpoint construction to any
$\lambda\in K_v$ and passing $t\downarrow0$ gives the inequality. The
coefficients can be real; the actual endpoints remain rational.

Conversely the finite duality proof in
Lemma [2](#supports){reference-type="ref" reference="supports"}, applied
to the matrix of primitive directions, gives an ambient $\ell_v$ with
$\ell_v(u_{e/v})\leq d_{v,e}$. Convexity on each germ gives
$f(v+tu_{e/v})\geq f(v)+t d_{v,e}$, hence this is a local support at
$v$. At an edge interior point the left and right convex derivatives are
finite; any slope between them is a supporting affine function on its
line and can be extended ambiently. Thus there are supports at every
point, and Lemma [1](#localglobal){reference-type="ref"
reference="localglobal"} proves all real-endpoint PCC inequalities. No
PA or operator premise was used in this lemma. ◻
:::

::: {#graph-density .theorem}
**Theorem 17** (All-continuous real graph regularization). *For the
actual real PA reference $\gamma$ positive at infinity, every
$f\in C(X)\cap\operatorname{PC}_q(X)$ with bounded difference from
$\gamma$ is a uniform decreasing limit of relative
$\operatorname{PAPC}_\mathbb R$ functions on finite rational carrying
structures. In particular every unrestricted envelope $P_\gamma(u)$,
$u\in C_b(X)$, lies in this real regularizable domain. The statement
asserts no literal integral-slope density.*
:::

::: proof
*Proof.* Refine the original graph so $\gamma$ is affine on its edges.
Use the primitive coordinate on each edge. On an unbounded end, for
$t\geq T_e$ write $\gamma(t)=g_et+c_e$, $g_e>0$, with a fixed rational
$T_e$. Convexity of $f$ and bounded relative difference force its
limiting slope to be $g_e$. Indeed secant slopes at infinity tend to
$g_e$, and monotonicity of convex derivatives identifies their limit
with that secant limit. Therefore $r_e(t)=f(t)-g_et$ is convex,
nonincreasing, and bounded. It has a finite limit $l_e$. For any
$\eta>0$ choose rational $S_e\geq T_e$ so $r_e(S_e)-l_e<\eta$. Replace
the tail of $f$ by $f(S_e)+g_e(t-S_e)$, which majorizes $f$ and differs
from it by at most $\eta$. Its slope $g_e$ is at least every preceding
chord slope.

On every bounded edge, and every initial segment $[0,S_e]$ of an end,
choose a sufficiently fine finite mesh of rational coordinates including
all vertices, and interpolate the *actual real values* of $f$. Convex
chords majorize $f$, are uniformly close by uniform continuity on these
finitely many compact intervals, and have nondecreasing slopes. At an
original vertex the new outgoing first chord slope is at least
$d_{v,e}$, on both ends of every bounded edge. Since all relation
coefficients are nonnegative, every vertex relation cost remains
nonnegative. At newly inserted bivalent vertices, monotone edge slopes
give exactly the same condition.
Lemma [16](#graph-slopes){reference-type="ref" reference="graph-slopes"}
proves PC. Shared vertex values are unchanged, so the resulting function
is continuous. Its affine slopes and constants are real, and all mesh
positions are rational; hence it is actual $\operatorname{PA}_\mathbb R$
on a finite rational structure. Each tail has the *actual* $g_e$ slope,
so bounded difference from $\gamma$ is preserved globally. The errors
can be made arbitrarily small on the whole graph, including all ends.
This construction never takes a finite PA maximum with the irrational
reference, and has introduced no irrational carrying wall.

Extract errors $\leq2^{-n}$ and add $4\cdot2^{-n}$ as in
Theorem [13](#raw-extension){reference-type="ref"
reference="raw-extension"}. The resulting relative real PA PC sequence
is strictly decreasing and converges uniformly. Finally R230 applies to
this finite positive balanced embedded graph and the actual continuous
PC reference: for any $u\in C_b$ its unrestricted envelope is
continuous, PC, and satisfies $|P_\gamma(u)-\gamma|\leq\|u\|_\infty$.
The just-proved approximation applies to that actual endpoint. This is
an operator-domain antecedent, not merely CONT PC membership. ◻
:::

::: {#graph-operator .theorem}
**Theorem 18** (Genuine graph raw completion for all real coefficients).
*On the domain in Theorem [17](#graph-density){reference-type="ref"
reference="graph-density"}, the sequence-independent uniform completion
of the primitive one-dimensional raw operator is
$$\Delta f=\sum_v\left(\sum_{e\ni v}w_ed_{v,e}\right)\delta_v
          +\sum_e w_e\,d(f'_+)\big|_{\operatorname{relint}e}.$$ The
second terms are pushforwards in the primitive edge coordinate; there is
no Euclidean arclength or additional factorial. The output is positive,
local, finite, and has mass $M=\sum_{\text{ends }e}w_eg_e
=\deg(\gamma)$. Every uniform PA approximating family converges against
all $C_b$ tests, and agrees with literal raw recursion when restricted
to its actual literal completion domain.*

*For each fixed $C<\infty$, all these completed real outputs with
$\|f-\gamma\|_\infty\leq C$ satisfy the common tail bound
$$\Delta f(X\setminus K_R)\leq\frac{2C}{R}\sum_{\text{ends }e}w_e,
 \quad R>0,$$ where $K_R$ contains all bounded edges and the end
portions $0\leq t\leq T_e+R$. In addition, choose fixed rational $c$
with $H=\gamma+c\geq0$ and let $J=\int H\,d\Delta\gamma$. Every
completed function in that same fixed-$C$ family has
$\int H\,d\Delta f\leq2CM+J$. The map is continuous for weak $C_b$,
globally uniformly continuous for vague $C_c$, and uniformly continuous
for weak $C_b$ and $d_{\rm BL}$ on every such *fixed-$C$* family.*
:::

::: proof
*Proof.* For a convex edge function, $f'_+$ is nondecreasing and right
continuous. Right continuity follows directly from the convex secant
inequalities: the right limit of $f'_+$ at $t$ is bounded above by every
secant from $t$ to $t+h$, and taking $h\downarrow0$ gives $f'_+(t)$
itself. On a compact interval construct positive test functionals from
sums $\sum_i g(\xi_i)(f'_+(t_{i+1})-f'_+(t_i))$. Two such sums on a
common refinement differ by at most the oscillation of $g$ at their mesh
scale times the finite derivative variation. They therefore converge for
continuous tests, are positive and linear, and the positive-functional
lemma constructs their Radon measure. Continuous level cutoffs and right
continuity identify its interval values, including any endpoint jump.
Its Stieltjes measure is determined by $d(f'_+)((a,b])=f'_+(b)-f'_+(a)$.
This determines a positive measure: on finite intervals, step
approximations of the monotone derivative construct its distribution
measure by the same open-set or monotone interval construction as in
Lemma [12](#radon-lemma){reference-type="ref" reference="radon-lemma"}.
Countable additivity follows by continuity of the monotone distribution
from the right and finite interval subdivision; equivalently positive
integration functionals on compact continuous tests and that lemma give
the identical interval values. The finite endpoint derivatives in
Lemma [16](#graph-slopes){reference-type="ref" reference="graph-slopes"}
and the limiting end slope $g_e$ give finite edge mass. Vertex
coefficients are nonnegative by the actual relation $w_v$. On a bounded
edge of primitive length $L$, its interior mass is
$w_e(f'_-(L)-f'_+(0))$; its two endpoint contributions to the vertex sum
are $w_ef'_+(0)$ and $-w_ef'_-(L)$. They cancel exactly. On an unbounded
end the interior mass is $w_e(g_e-d_{v,e})$; adding its vertex
contribution leaves $w_eg_e$. Summing the finite edge list proves the
mass identity. Applied to PA functions this is exactly the actual
primitive-normal recursion, including zero artificial vertices, and
proves $M=\deg(\gamma)$.

For a compact rational ambient PA test $\psi|_X$, edgewise Stieltjes
integration by parts gives $$\label{graph-ibp}
 \int\psi\,d\Delta f=\int f\,d\Delta\psi.$$ Here $\Delta\psi$ is the
signed finite primitive raw divisor of the compact test against $[X]$.
To justify the identity, on each interval where $\psi$ is affine,
integrate its constant derivative against the increments of $f$, and
integrate $\psi$ against the increments of the monotone $f'_+$.
Telescoping interval partitions gives
$\int\psi\,d f'_+=[\psi f']-\int\psi'f'\,dt$. The latter ordinary
integral equals the corresponding affine-test slope times the endpoint
increment of $f$: convex functions with finite endpoint slopes are
Lipschitz on the interval and their increments are the integrals of
their monotone derivatives, as follows by upper and lower secant Riemann
sums. The derivative jumps of $\psi$ supply $\int f\,d\psi'$. At
vertices the boundary terms cancel against the explicit weighted vertex
derivatives on both sides of
[\[graph-ibp\]](#graph-ibp){reference-type="eqref"
reference="graph-ibp"}. Unbounded edges have no outer boundary term
because the test vanishes there. Constants and continuity cancel the
remaining tangent values. This proves the identity without assuming PA
for $f$.

It follows that $|\langle\psi,\Delta f-\Delta h\rangle|
\leq\|\Delta\psi\|_{\rm TV}\|f-h\|_\infty$. Uniform density of compact
rational PA tests, with controlled supports, and mass $M$ give
convergence for every $C_c$ test and sequence independence. Locality
follows directly from the displayed derivative formula, or from
localized tests in [\[graph-ibp\]](#graph-ibp){reference-type="eqref"
reference="graph-ibp"}. For $\|f-\gamma\|_\infty\leq C$, convexity
implies $$f'_+(T_e+R)\geq\frac{f(T_e+R)-f(T_e)}R
                         \geq g_e-2C/R.$$ The end measure beyond that
point is $w_e(g_e-f'_+(T_e+R))\leq2Cw_e/R$. This proves the asserted
common bound for *every* completed function in the family. A uniformly
convergent approximation to a fixed relative function has a common
finite $C$, so compact cutoff truncation upgrades its vague convergence
to every $C_b$ test. At one input use a radius-one uniform neighborhood
with $C_f=1+\|f-\gamma\|_\infty$ to get ordinary weak-$C_b$ continuity.
The compact-test estimate gives global vague uniform continuity. For
each fixed $C$, the common end-tail bound and finite compact-test
approximation give weak-$C_b$ uniform continuity; the finite mesh and
value-quantization net of BL restrictions on $K_R$ from
Theorem [13](#raw-extension){reference-type="ref"
reference="raw-extension"} gives BL uniform continuity with that same
fixed $C$. If $M=0$, positivity gives the zero output and all claims are
immediate. For completeness the moment bound holds for all these outputs
even with irrational coefficients of the actual reference. The
continuous convex $q_j=\max(\gamma-j,-c)$ is boundedly relative to
$\gamma$. It is not asserted to have rational carrying walls;
Theorem [17](#graph-density){reference-type="ref"
reference="graph-density"} places it in the actual real completion by
rational chords. Its measures and those chord approximants have already
been proved to converge for all $C_b$ tests. For finite relative PA $a$,
apply the finite bounded edge IBP identity to actual PA approximants of
$q_j$ and pass to the limit, using the bounded differences as tests.
This gives $$\int(\gamma-q_j)\Delta a
 =\int(\gamma-a)\Delta q_j+\int(a-q_j)\Delta\gamma.$$ The first term and
the part $a-\gamma$ of the second have absolute value at most $CM$ each;
the remaining term is $\int\min(H,j)\Delta\gamma\leq J$. Approximate any
completed $f$ with relative bounds $C+o(1)$ and use all-$C_b$
convergence on the bounded test $\min(H,j)$ to obtain
$\int\min(H,j)\Delta f\leq2CM+J$. Monotone convergence proves the stated
common moment bound for every completed function in the fixed-$C$
family. This application has an actual operator antecedent for $q_j$
before any measure is used. There is no arbitrary-relative-bound weak
uniform guarantee; the line counterexamples still apply. ◻
:::

::: {#graph-contact .theorem}
**Theorem 19** (All-continuous graph contact classification). *For the
finite globally embedded positive balanced rational graph and actual
positive-growth
$\gamma\in\operatorname{PA}_\mathbb R\cap\operatorname{PC}_q$ of this
section, the following are equivalent:*

1.  *Every $u\in C_b(X)$ has a real-regularizable actual envelope and
    $\int(P_\gamma(u)-\gamma-u)\Delta P_\gamma(u)=0$.*

2.  *$K_v=\mathbb R_{\geq0}w_v$ at every vertex.*

*If the second condition fails, an actual bounded real PA obstacle
already has a finite relative real PA PC envelope with a strictly
negative contact integral, even for irrational coefficients of the
actual reference. This is a one-dimensional sector theorem, not the full
original P05.2.*
:::

::: proof
*Proof.* All actual envelopes have their real-domain antecedent and
genuine operator by Theorems [17](#graph-density){reference-type="ref"
reference="graph-density"}--[18](#graph-operator){reference-type="ref"
reference="graph-operator"} and R230. Let $f=P_\gamma(u)$ and suppose
the local cones have one ray. At a noncontact vertex with positive atom,
its derivative vector $d_v$ has $d_v\cdot w_v>0$, hence strictly
positive cost on every nonzero relation. The corrected strict-floor
separation argument applies to this finite derivative vector: it gives
$\ell$ and $c>0$ with $d_{v,e}t-\ell(tu_{e/v})\geq c\|tu_{e/v}\|$ on
every germ. Edge convexity gives the same lower bound for
$f(v+tu)-f(v)-\ell(tu)$. On a small star with positive continuous
obstacle gap, raise $f$ to $\max(f,f(v)+b+\ell(x-v))$ with $b$ less than
the gap and the strict collar margin; outside leave it unchanged.
Supports of $f$ exist by Lemma [16](#graph-slopes){reference-type="ref"
reference="graph-slopes"}, and supports of active entries persist at
ties. The collar makes the localized function continuous and PC by
Lemma [1](#localglobal){reference-type="ref" reference="localglobal"}.
It preserves actual growth and raises $f(v)$, contradicting the
unrestricted envelope. Thus every noncontact vertex has zero atom. No
finite PA germ for $f$ was assumed here.

At an interior noncontact point choose a sufficiently small closed edge
interval $[a,b]$ in the positive-gap set, with oscillation of $f$ less
than the gap there. Replacing $f$ on that interval by its chord raises
it by less than that gap. The incoming derivative at $a$ is at most the
secant slope and the outgoing derivative at $b$ is at least it, so the
glued edge remains convex. All original vertex derivatives are
untouched, hence supports and PCC inequalities remain valid. If $f$ were
not affine there, this would be a competitor raising an interior point.
Consequently $f$ is locally affine throughout the open noncontact
portion of every edge, and its curvature measure vanishes there.
Together with the vertex conclusion, the positive measure is supported
on the closed contact set. Its total mass is finite and the gap is
bounded continuous, giving the exact zero integral.

For necessity suppose $\dim K_v>1$. Since $w_v$ is strictly positive,
$K_v$ has dimension $\dim\ker U_v$. Choose an extreme ray $\kappa$ of
this rational cone. It omits some edge coordinate $e_0$: otherwise an
independent kernel vector would permit small two-sided perturbations of
its strictly positive coefficients, contradicting extremality. The ray
can be chosen rational by the finite circuit proof. Set $s_{e_0}=1$ and
all other $s_e=0$. This homogeneous rational edgewise affine germ $h$ is
nonnegative, has the zero local support, and is PC; $s\cdot\kappa=0$
while its actual raw mass is $s\cdot w_v=w_{e_0}>0$. Real positive
weights are retained exactly.

We realize this germ with the *actual irrational-coefficient* reference,
using graph interpolation rather than irrational PA maximum closure.
Coercivity gives $\gamma\geq a\rho-b_0$. Choose rational $\varepsilon>0$
smaller than $a$, and rational $C>\gamma(v)$. The continuous PC function
$\Psi=\max(\gamma,C+\varepsilon\rho(x-v))$ equals its second entry near
$v$ and equals $\gamma$ outside a compact set. It is *not* asserted to
belong to rational-geometry PA. Choose a rational star radius $r$,
rational $\delta>0$ with $\delta|h|\leq\varepsilon\rho/2$, and rational
$0<t<\varepsilon r/4$. Inside the star set $G=\max(\Psi,C+t+\delta h)$
and outside set $G=\Psi$. The same strict collar and local-support
argument as in the rational jet theorem gives a continuous PC global
$G$, boundedly relative to the actual $\gamma$, with germ
$C+t+\delta h$.

Now apply the *proved graph* chord construction to $G$, choosing its
first rational sample on every germ at $v$ inside that unchanged linear
germ. The first chord is exactly the germ; subsequent meshes, other
vertex slopes, and tail slopes have the properties proved in
Theorem [17](#graph-density){reference-type="ref"
reference="graph-density"}. This produces an actual relative
$F\in\operatorname{PAPC}_\mathbb R$ on finite rational geometry with the
same germ at $v$, flat relation $\kappa$, and raw mass
$\delta w_{e_0}>0$. It need not have rational coefficients elsewhere;
these are allowed real coefficients on rational carrying cells. Both $F$
and the actual $\gamma$ are now on finite rational structures, so
$F-\gamma$ is bounded real PA. The exact rational roof theorem applies
in that real category, producing $u=F-\gamma+(R-\rho(x-v))_+$ with
actual unrestricted envelope $F$ and contact $-R\delta w_{e_0}<0$. All
endpoint and operator antecedents are verified. The intermediate
continuous maximum received no operator from its continuity; it was
replaced by an actual PA function before the roof calculation.

Subdivision adds only bivalent stars with a single relation ray, so the
condition is intrinsic to this carrying graph. The proof uses global
embedded coercivity and does not transfer the necessity construction to
abstract compact charts. It also proves no higher-dimensional
approximation or non-PA contact criterion. ◻
:::

# Material changes, remaining original obligations, and evidence

The full unchanged original asks for necessary and sufficient structural
conditions for every admissible obstacle, in each actual coefficient
category, with all envelope and genuine operator antecedents. It is not
closed here. In particular higher-dimensional real regularization for
all bounded continuous obstacles, a contact criterion for all non-PA
endpoints, and arbitrary irrational-reference mixed completion and
realization are not established. The finite-PA local classifier remains
quantified over every rational refinement, without a bound. The graph
sector is a new all-continuous and arbitrary-real-reference result in
its explicitly one-dimensional embedded scope; it supplies none of these
higher-dimensional missing theorems.

The failed whole247/196 and whole255/200 sources, arguments, ledgers,
reports, bindings and exact native records remain unchanged. Adding PC
to the old floor lemma was material, replacing the separable endpoint
was material, and removing global weak/BL uniform continuity is
material. No failed source has been relabeled accepted.
`material-changes.md` records exact before/after scopes. A224 is context
only; B225 positive spanning and embedded noncompactness, and R230
continuous completion and rational geometry, are used in their complete
granted scopes. None gives an operator to a merely continuous function.

The non-PA measure above has additional exact moments
$\int y^2\,d\operatorname{MA}_{\mathrm{poly},\mathbb R}(F)=12\int_1^2t^2\,dt=28$
and
$\int z^2\,d\operatorname{MA}_{\mathrm{poly},\mathbb R}(F)=4\int_1^2((t-1)^2/2)^2\,dt=1/5$.
Its densities are parameter densities. Every dyadic approximation is on
rational carrying geometry; all initial/final half-jumps, primitive
graph weights, zero walls and artificial vertices are accounted for.

The standard-library program `check_certificates.py` uses exact
fractions to enumerate finite affine triples, primitive normals, raw
first-cycle balances and second atoms, dyadic formulas, moment sums,
coupling corners, flat PCCs and graph interpolation slopes. The fixed
uniformity counterexamples are checked symbolically by exact fractional
phases and piecewise-linear values, with trigonometric values recorded
only as numerical observations. These finite lists are not continuum
proofs. The mathematical arguments above establish the scope
independently. Inputs are in `certificate-input.json`, actual outputs
and logs in `evidence/`, and the entire argument in `argument.md`.
`notes.json` uses only earlier local IDs in support arrays.

The four authorized original frozen primary files were hashed and read
in their complete pertinent definition/proof units. The quote-free
`source-application-ledger.md` records exact units, versions,
applications and exclusions. The BBGS negative-unit-normal to
positive-primitive-normal conversion is at every recursive dimension,
with saturated covolumes and signed/zero intermediate weights. Its
printed 3.19 commuting-step citation to 3.12 uses the actual equality in
3.15. The printed source zero-coefficient strictness degeneracy is
explicitly disclosed and is not used. No broad source density, automatic
rational-endpoint continuity, or extension theorem is imported.

Rerun in this directory with existing tools:

    python prepare_inputs.py
    python check_certificates.py
    python rebuild_paper.py
    pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
    python build_artifacts.py

All programs, inputs, commands, outputs and environment details are
saved. No installation, heavy local compute, network/account/runtime
change, external contact, private stream or other campaign inspection,
or protected-source edit was used. No supervised compute service was
exposed; the small finite checks needed none. No requested model switch
was exposed or claimed. The frozen primary files were not edited or
republished. Compilation and successful execution are reproducibility
observations, not mathematical verification. Original P05.2 remains open
and candidate status is false.

::: thebibliography
9 A. M. Botero, E. Mazzon, L. Pille--Schneider, *Monge--Ampere measures
on balanced polyhedral spaces*, arXiv:2603.08664v1, submitted 9 March
2026, manuscript 10 March 2026. <https://arxiv.org/pdf/2603.08664v1>. A.
M. Botero, J. I. Burgos Gil, M. Sombra, *Convex analysis on polyhedral
spaces*, Math. Z. 301 (2022), 1631--1674, publisher version, 24 January
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
:::
