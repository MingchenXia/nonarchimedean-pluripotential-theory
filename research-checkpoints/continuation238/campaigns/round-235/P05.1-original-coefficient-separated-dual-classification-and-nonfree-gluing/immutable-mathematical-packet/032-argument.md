# Controlling problem, exact coefficients, and the new scope

The controlling `original-task.json` has atom P05.1, a 523-character
statement, a 44,807-character common-notation/source-family body, and a
710-character completion criterion. Its residual asks for the
coefficient-separated classification of balanced rational polyhedral
pairs with a PC PA reference positive at infinity, retaining
higher-dimensional real regularity, arbitrary nonseparable obstacles,
and the compact higher-dimensional literal branch. A new sufficient
geometric class does not complete that classification.

Fix a lattice $N$, a finite-dimensional ambient $N_\mathbb R$, and a
finite pure rational complex containing all its closed faces. Rational
affine equations and inequalities can be made integral by clearing
denominators. A tangent lattice is always the saturated
$$N_\sigma=N\cap\operatorname{span}_\mathbb R(\sigma-\sigma).$$ Facet
normals point inward and represent primitive classes in
$N_\sigma/N_\rho$. Top weights are actual strictly positive real
numbers; balancing means that their weighted normal sum is tangent to
the facet. The formal weights in the frozen BMPS Definition 2.19 are
rational. Real balancing in this paper is proved directly with the same
primitive classes, rather than attributed to that formal definition.

A printed PCC has rational endpoints $x_i$, real $\alpha_i\geq0$ summing
to one, and center $x=\sum\alpha_i x_i$. There must be a rational
carrying structure with faces $\tau\preceq\sigma_i$, $x\in\tau$,
$x_i\in\sigma_i$. The center need not be rational. The class
$\operatorname{PC}_q$ satisfies all these Jensen inequalities. Every use
of continuity below is an explicit hypothesis. Literal PA has integral
tangent slopes and rational constants. The class
$\operatorname{PA}_\mathbb R$ is its finite real scalar extension on
finite rational spatial carriers. We will prove that the real
coefficient tuples we construct belong to this extension. An arbitrary
maximum of irrational affine coefficients is not a rational-carrier
assertion.

The actual reference $\gamma$ is continuous,
$\operatorname{PA}_\mathbb R$, printed PC, and positive at infinity:
each actual affine piece has strictly positive slope on every nonzero
direction in that cell's recession cone. It is never rounded, averaged,
replaced, or altered off a selected subset. The target is
$$f\in C(X)\cap\operatorname{PC}_q,\qquad \|f-\gamma\|_\infty\leq C<\infty.$$
No separability assumption is imposed. A uniform decreasing completion
is constructed before any operator could be applied; this manuscript
assigns no Monge--Ampere measure to an intermediate or to a completed
endpoint.

::: {#def:free .definition}
**Definition 1** (Finite free attachment presentation). *All pages below
are distinct complete rational affine $d$-planes, $d\geq1$. Begin with a
page $Q_0$. Having formed $X_{j-1}$, let
$A_{j-1}=\operatorname{aff}X_{j-1}$. Attach a nonempty finite group
$$B_j=\bigcup_{a=1}^{m_j}Q_{j,a},\qquad E_j=\operatorname{aff}B_j,$$
along a nonempty rational affine $H_j$ of dimension less than $d$.
Require:*

1.  *$H_j$ is contained in one earlier page, called its parent;*

2.  *every new page contains $H_j$, and distinct pages in $B_j$ have
    intersection exactly $H_j$;*

3.  *$E_j\cap A_{j-1}=H_j$.*

*For $m_j=1$, condition (2) just means $H_j\subset Q_{j,1}$. Put
$X_j=X_{j-1}\cup B_j$, and stop at $j=r<\infty$.*
:::

This is a rational geometric condition, checkable by affine Gaussian
elimination. It makes no claim about feasibility of an unknown target on
an unknown PA carrier. It allows $H_j$ and $H_l$ to be different,
parallel, nested, or intersecting as permitted by the stated affine
intersections. Dependence inside any new group is unrestricted. It
excludes an attachment whose span already meets the earlier span in
extra directions, even if its support meets the earlier support only in
the desired trace.

::: {#thm:main .theorem}
**Theorem 2** (Simultaneous approximation on the new class). *Let
$X=X_r$ have a presentation in
Definition [1](#def:free){reference-type="ref" reference="def:free"}.
Give its complete pages arbitrary specified positive real constant
weights, and retain any fixed finite rational original carrier of $X$.
For every admitted actual $\gamma$, every continuous printed-PC $f$ with
bounded difference from $\gamma$, and every $\epsilon>0$, there is a
genuine finite rational-spatial
$P\in\operatorname{PA}_\mathbb R\cap\operatorname{PC}_q$ such that
$$f\leq P\leq f+\epsilon\quad\hbox{on all }X.$$ It has the exact page
recession of $\gamma$. At every real point of every original face there
is one ambient affine form supporting $P$ on the entire original
incident cells. In fact it supports on every entire complete page
containing that point. There is a globally strictly decreasing uniform
approximating sequence with one uniform bound relative to this same
$\gamma$.*
:::

The theorem is an existence and finite-construction theorem, with
samples selected by compactness from actual dual data. It is not an
exact computational oracle for arbitrary continuous functions or
arbitrary real heights. It does not assert that every $P$ comes from
restriction of one globally ambient convex function.

# Elementary foundations and precise real duality

We use ordinary real completeness, finite-dimensional compactness of
closed bounded sets, inverse linear algebra, and convex secant
inequalities. The additional facts needed in the construction are proved
here.

::: {#lem:finite .lemma}
**Lemma 3** (Finite generation, compact hulls, and elimination). *Finite
conic hulls are closed. Compact sets in finite-dimensional space have
compact convex hulls. Every nonempty polyhedron is a finite point hull
plus a finite recession cone, including both signs of lineality
generators. Rational polyhedra admit rational spatial generators. Such
finite point/cone expressions are polyhedra, and rational linear images
of rational polyhedra are rational polyhedra.*
:::

::: proof
*Proof.* In a conic representation with dependent positive columns,
choose a nonzero relation $\sum b_i v_i=0$, with a positive $b_i$ after
changing sign. Subtract $t b_i$ from its coefficients, where
$t=\min_{b_i>0}a_i/b_i$. The representation stays nonnegative and loses
a positive column. Iterate to an independent subset. Each independent
column map has an inverse on its image, bounding coefficients by a
constant times the represented vector's norm. There are finitely many
subsets. A convergent vector sequence thus has a subsequence with one
subset and bounded convergent coefficients; its limit lies in the cone.

For affine combinations, the analogous elimination uses $\sum b_i=0$ as
well. In dimension $s$ it leaves at most $s+1$ points. The hull of a
compact $K$ is the image of $K^{s+1}$ times the compact standard simplex
under the continuous sum map, with repetitions allowed, hence compact.

For a cone given by finite homogeneous inequalities, remove their joint
kernel as its lineality. Choose a rational complement for rational
inequalities. In the pointed complement the sum of the defining
nonnegative forms is strictly positive on nonzero cone vectors. The
section at value one is bounded: an unbounded sequence, normalized and
passed to a unit limit, would give a nonzero joint-kernel vector. A
bounded polyhedron is the hull of finitely many vertices. At a nonvertex
move in both directions of the kernel of active constraints until more
independent constraints become active. Boundedness gives the endpoints;
the original point is their convex combination. Induct on active rank.
Vertices solve finitely many full-rank systems, rational for rational
coefficients. Restoring both signs of a lineality basis proves finite
generation of a cone. Homogenize a polyhedron $Ax\leq b$ as $Au\leq tb$,
$t\geq0$: positive-$t$ generators yield points, and zero-$t$ generators
yield recession directions. Section $t=1$ proves its stated
decomposition.

Conversely introduce nonnegative hull/cone coefficients, sum-one for the
hull, and the coordinate equations for their image. Eliminate each
variable by pairing every lower bound with every upper bound, retaining
rows independent of it. A variable with bounds of only one sign imposes
no additional pair condition. These finite weak inequalities exactly
assert a nonempty interval for that variable. Repetition proves the
finite projected description, rational when the data are rational.
Closedness of compact hull plus finite cone also follows by taking a
convergent compact summand subsequence. These arguments include all
relative affine hulls and zero-dimensional cases. ◻
:::

::: {#lem:support .lemma}
**Lemma 4** (Supports and biconjugacy). *A finite convex function on a
complete real affine space is continuous, locally Lipschitz, and has an
affine support at every point. Its directional derivative at $y$ is
finite continuous sublinear, and is the support function of a nonempty
compact convex subdifferential. It equals its biconjugate. A finite
lower semicontinuous convex function on a compact polytope is continuous
on the whole polytope. Extended by infinity off that polytope, it too
equals its biconjugate, including the boundary.*
:::

::: proof
*Proof.* On a cube about $y$, convexity bounds values above by the
largest vertex value. Reflection in $y$ gives a lower bound on a smaller
cube. Extend any segment in a still smaller cube a fixed distance in
both signs; convex secants bound its slope by oscillation divided by
that distance. This proves local Lipschitzness and continuity.

A point outside a nonempty closed convex set has a nearest point:
restrict a minimizing sequence to a large closed ball and use
compactness. For nearest $w$ to outside $z$, first variation along
$[w,c]$ gives $(w-z)\cdot(c-w)\geq0$. Thus
$(w-z)\cdot(c-z)\geq\|w-z\|^2>0$. Apply this to $(y,F(y)-t)$ below a
continuous convex epigraph. Normalize the inward normals and let
$t\downarrow0$ along a subsequence. Their unit limit supports at
$(y,F(y))$ and has nonnegative vertical component. This component cannot
be zero: projection onto the entire spatial space would force its
horizontal part to vanish. Division gives an affine support. Every such
touching support provides equality in double conjugation at its touching
point; the defining transform inequality supplies the reverse
inequality.

Convex secants give the directional limit $h(v)$; the local Lipschitz
bound makes it finite, bounded by $L\|v\|$, and Lipschitz in $v$.
Scaling proves positive homogeneity. The midpoint inequality at
$y+2tv,y+2tw$ proves $h(v+w)\leq h(v)+h(w)$. Apply the full-space
support argument to $h$ at $v$. Its affine support has zero constant:
testing zero and $2v$, using homogeneity and contact at $v$, gives both
signs of the constant bound. Forms below $h$ are exactly supports of $F$
at $y$, by differentiation in one direction and convex secants in the
other. Testing both signs of $|h|\leq L\|\cdot\|$ bounds those forms;
their set is closed, convex, nonempty, and compact. The support at $v$
attains $h(v)$.

For a finite lsc convex $a$ on a compact polytope $D$, its upper bound
is the largest vertex value $M$. At $p\in D$ work in its relative affine
hull and choose a fixed $u>0$ below each inactive facet slack divided by
its normal norm. For nearby $q\in D$, active rows are respected along
$(q-p)/\|q-p\|$, and inactive rows retain their margin up to distance
$u$. Thus $p+u(q-p)/\|q-p\|\in D$. Convexity yields
$$a(q)\leq a(p)+\frac{\|q-p\|}{u}(M-a(p)).$$ Together with lsc this
proves continuity at all boundary points. If there are no inactive rows
any sufficiently small $u$ works; a singleton is immediate.

For biconjugacy on $D$, strictly separate $(p,t)$ with $p\in D,t<a(p)$
from its closed epigraph by nearest-point variation. The inward normal
$(A,\beta)$ has $\beta\geq0$. Testing the point $(p,a(p))$ gives
$\beta(a(p)-t)>0$, hence $\beta>0$. Division produces an affine minorant
whose value at $p$ exceeds $t$. Let $t\uparrow a(p)$. Outside $D$,
nearest-point spatial separation gives $v(p)>\max_D v$; scaling $v$ and
using $\min_D a> -\infty$ makes the double transform infinite there.
This proves the entire assertion without an external convex-duality
theorem. ◻
:::

# Whole-page convexity and supports with the printed endpoints

::: {#lem:density .lemma}
**Lemma 5** (Rational feasible approximation). *Continuous printed-PC
functions satisfy every real-endpoint PCC with the same rational
incidences.*
:::

::: proof
*Proof.* At any point of a rational polyhedron, impose its active rows
as equalities. Gaussian elimination gives a rational particular solution
and a rational kernel basis; rational coordinates approximate the given
coordinates. All inactive finite slacks remain strict. For a PCC delete
zero coefficients and introduce $t_i=\alpha_i x_i$. Its endpoint-cell
constraints become $A_i t_i\leq\alpha_i b_i$, together with
$\alpha_i\geq0$, $\sum\alpha_i=1$, and $\sum t_i\in\tau$. This is a
rational feasible polyhedron. Close feasible rational approximants
retain $\alpha_i>0$, and their endpoints $t_i/\alpha_i$ and centers are
rational. Apply printed PC and pass to limits using continuity. The
argument covers irrational centers in lower-dimensional faces without
changing the carrier. ◻
:::

::: {#prop:criterion .proposition}
**Proposition 6** (Support criterion on any finite complete-page
arrangement). *For a continuous function on a finite union of distinct
complete rational affine pages, printed PC is equivalent to ordinary
convexity on every whole page and, at each point $y$, existence of one
ambient form supporting every entire page containing $y$.*
:::

::: proof
*Proof.* A convex carrier cell lies in one page. Otherwise its relative
interior would be contained in finitely many proper affine subspaces of
its affine hull. The product of a nonzero affine equation for each such
subspace is a nonzero polynomial and cannot vanish on an open set, by
successive one-variable polynomial uniqueness.

Fix a carrier and a point $y$. A sufficiently small neighborhood meets
only closed cells containing $y$: the other finitely many closed cells
avoid it. Its minimal face is a face of every cell containing it, by the
common-face axiom. For short symmetric endpoints $y\pm tw$ in one
complete page, their assigned cells are therefore incident to this same
minimal face. Lemma [5](#lem:density){reference-type="ref"
reference="lem:density"} proves the local midpoint inequality. To obtain
convexity on a whole real segment subtract its chord, obtaining $q$ with
endpoint values zero. If $q(t_0)>0$, choose sufficiently small
$\delta>0$ so $q(t)+\delta t^2$ has an interior global maximum. At
sufficiently short symmetric parameters around this maximum, the local
midpoint inequality for $q$ makes the mean of the two perturbed values
at least the maximum plus $\delta s^2$, a contradiction. Thus every
segment satisfies convexity. This uses actual short incident PCCs, not a
distant PCC or illegal whole-page coarsening.

Let $L_i$ be the tangent spaces of the pages containing $y$, and
$K_i=\partial f_i(y)$ their compact subdifferentials from
Lemma [4](#lem:support){reference-type="ref" reference="lem:support"}.
Let $S$ be the image of restriction from $(\sum_iL_i)^*$ into
$\prod_iL_i^*$, a closed linear subspace. If $K=\prod_iK_i$ misses $S$,
minimize the squared norm of the orthogonal projection onto $S^\perp$
over compact $K$. For a minimizer $z_0$ put
$a=\operatorname{pr}_{S^\perp}z_0\ne0$. First variation gives
$\langle a,z\rangle\geq\|a\|^2$ for $z\in K$. Represent $-a$ by
directions $w_i\in L_i$ using auxiliary Euclidean duality. Orthogonality
to the restriction image means $\sum_iw_i=0$, and
$$\sum_i f_i'(y;w_i)=\max_{(p_i)\in K}\sum_i p_i(w_i)\leq-\|a\|^2<0.$$
For sufficiently small $t>0$, endpoints $y+tw_i$ have equal-weight
barycenter $y$, lie in actually incident cells, and have negative Jensen
cost. Lemma [5](#lem:density){reference-type="ref"
reference="lem:density"} forbids it. Thus $K$ meets $S$, giving one
ambient support on whole pages.

Conversely a legal endpoint cell lies in a page containing its center.
The common entire-page support at the center bounds each endpoint from
below. Multiply by the PCC coefficients and sum; the affine terms
cancel. This proves every printed PCC on every permitted structure. ◻
:::

# A finite rational primal construction with actual real heights

Let $L$ be a complete rational affine space, translated by a rational
point. If $\gamma$ is convex finite real PA on a rational carrier, its
full-dimensional affine pieces are global supports by convex secants.
Thus $$\gamma(x)=\max_\nu(a_\nu(x)+b_\nu),\quad
h(v)=\max_\nu a_\nu(v),\quad \Delta=\operatorname{conv}\{a_\nu\}.$$
These are its actual coefficients; $\Delta$ need not be rational. The
function $\gamma-h$ is bounded. On each recession cone of its rational
carrier, $h$ equals that cell's linear part. Those cones cover $L$: on
$tv$ some finite cell contains an unbounded subsequence, and division of
its inequalities by $t$ puts $v$ in its recession cone. Bounded
difference identifies its slope with $h(v)$. Positive growth gives
$h(v)>0$ for $v\ne0$, uniformly on the unit sphere. In particular a
carrying cell cannot have nonzero lineality, since its affine slope
would have to be positive on both signs. The zero-dimensional case has a
singleton dual domain and a vertical epigraph ray.

::: {#lem:dual .lemma}
**Lemma 7** (Entire actual dual domain and rational recession lifts).
*For continuous convex $f$ bounded relative to $\gamma$, $\phi=f^*$ is
finite continuous exactly on $\Delta$, including its entire boundary.
Its extension is infinity elsewhere. The recession of $f$ is exactly $h$
and $f(x+v)\leq f(x)+h(v)$. There is a finite exact generating
expression for $\operatorname{epi}h$ using rational spatial rays and
their actual real heights.*
:::

::: proof
*Proof.* Choose $D$ with $|f-h|\leq D$. For $p\in\Delta$,
$p(x)\leq h(x)$ bounds $\phi(p)$ above by $D$, and evaluation at zero
bounds it below by $-f(0)$. For $p\notin\Delta$, nearest-point
separation gives $v$ with $p(v)>h(v)$; $x=tv$ makes the transform
infinite. The transform is convex lsc as a supremum of affine functions.
Lemma [4](#lem:support){reference-type="ref" reference="lem:support"}
gives whole-boundary continuity and $f=\phi^*$. The latter and
$p(v)\leq h(v)$ imply the recession inequality. Bounded difference on
rays gives exact recession.

Generate each rational recession cone of the carrier, including signed
lineality generators if necessary. On each cone $h$ is linear. The union
of the lifted generators $(u,h(u))$, together with $(0,1)$, generates
$\operatorname{epi}h$: a conic representation inside the cone of $v$
gives exact height $h(v)$, and the vertical ray gives higher points.
Convexity and homogeneity prove the reverse inclusion. Spatial
directions are rational even when the heights are irrational. ◻
:::

::: {#lem:graph .lemma}
**Lemma 8** (Rational graph carriers and real scalar extension).
*Suppose a finite full-domain epigraph has the form
$$E=\operatorname{conv}\{(s,c_s)\}+\operatorname{cone}\{(u,d_u),(0,1)\},$$
where all spatial points and directions are rational, all heights are
real, and lower fibers are finite. Its lower function belongs to
$\operatorname{PA}_\mathbb R$ on a finite rational spatial complex.*
:::

::: proof
*Proof.* Lemma [3](#lem:finite){reference-type="ref"
reference="lem:finite"} makes $E$ a closed polyhedron; each fiber is a
nonempty closed upward ray bounded below, with attained bottom. Its
convex lower function has full domain, hence is continuous and has
supports. In a finite inequality description, upward stability gives
nonnegative vertical coefficient on each inward inequality. Full spatial
projection rules out nontrivial purely spatial inequalities. Dividing
the remaining positive vertical coefficients makes the lower function a
finite affine maximum.

A face exposed by a lower support is generated exactly by the point
generators with zero slack and recession generators with zero supporting
value. Every positive coefficient must have zero slack. The vertical ray
has positive slack and is excluded. The face lies on an affine graph, so
spatial projection is an affine isomorphism onto a hull of rational
points plus rational rays. It is a rational polyhedron by
Lemma [3](#lem:finite){reference-type="ref" reference="lem:finite"}.
Every subface of a lower graph face is also lower exposed: add a
sufficiently small exposing functional of the subface to the original
one, preserving its positive vertical coefficient and all nonzero
finite-generator slacks. There are finitely many such faces. If their
projections meet at $x$, their graph heights are the same bottom, so the
intersection is the projection of their common face, a face on each
graph. These projected faces cover the domain and give a finite rational
complex.

Continuous affine tuples on this carrier satisfy rational matching
equations, evaluated on rational affine bases of shared faces. Their
real solution space has a rational basis by Gaussian elimination. Clear
finitely many slope denominators in saturated tangent bases and constant
denominators in each basis tuple. The resulting basis functions are
literal PA. Expressing the actual real tuple in this rational basis
proves finite real scalar-extension membership. This argument does not
compare irrational formulas to create new spatial walls. ◻
:::

::: {#prop:primal .proposition}
**Proposition 9** (Uniform full-page primal majorants). *For every
$\delta>0$ and every finite prescribed rational sample set, there is a
convex genuine rational-spatial real-PA majorant $Q$ with
$$f\leq Q\leq f+\delta\quad\hbox{globally on }L,$$ exact recession $h$,
and equality at those unshifted samples.*
:::

::: proof
*Proof.* Continuity of $f$ permits rational spatial samples in
$\phi(p)=\sup_x(p(x)-f(x))$. For each $p\in\Delta$ choose one rational
sample achieving error less than $\delta/2$. Whole continuity of $\phi$
gives a neighborhood where the same sample has error less than $\delta$.
Compactness supplies a finite set $S$ covering all of $\Delta$; append
prescribed samples. Thus
$$\phi-\delta\leq k_S(p):=\max_{s\in S}(p(s)-f(s))\leq\phi\quad(p\in\Delta).$$
Form $E_S=\operatorname{conv}\{(s,f(s))\}+\operatorname{epi}h$. It is
closed, full spatial domain, and lies in $\operatorname{epi}f$ by
convexity and the recession inequality. Fibers have finite attained
bottoms. Its lower function $Q$ has transform $k_S$ on $\Delta$ and
infinity outside: maximize the functional over the point hull, then the
exact recession cone; outside $\Delta$ a separating ray gives infinity.
Biconjugacy reverses the displayed transform bounds to give
$f\leq Q\leq f+\delta$ everywhere. Sample lifts give equality there.
Lemma [8](#lem:graph){reference-type="ref" reference="lem:graph"} proves
genuine rational-spatial real PA. The compact hull plus exact recession
cone has exactly that cone as recession: divide a forward-ray sequence
by its parameter, the bounded hull disappears, and closedness of the
cone retains the direction. This proves exact recession rather than a
rounded asymptotic slope. ◻
:::

# Extension of a whole trace with every supporting form lifted

This section supplies the mechanism for one new group. It independently
proves the required compact dual identities and strengthens the support
conclusion to an arbitrary trace subgradient. Its common-$H$ mechanism
is consistent with the supplied S298 scope, but no S298 result or
unavailable references are used as premises here.

Let $Q_i$ be complete rational pages with every pairwise intersection
the same rational affine $H$. Translate a rational point of $H$ to zero;
write $L_i$ for their tangent spaces and $E=\sum_iL_i$. Let continuous
convex $f_i$ agree on $H$, be bounded relative to their actual page
references $\gamma_i$, and have one common ambient support at each
$y\in H$. These hypotheses follow from
Proposition [6](#prop:criterion){reference-type="ref"
reference="prop:criterion"} for the restriction of an original target.
Write $h_i,\Delta_i,\phi_i=f_i^*$ as in
Lemma [7](#lem:dual){reference-type="ref" reference="lem:dual"}. On $H$
the actual reference trace is convex rational-spatial real PA, positive
in every nonzero recession direction. Its actual recession $h_H=h_i|_H$
and compact gradient polytope $\Delta_H$ give the conjugate domain of
$f_H$. If $H$ is a point use $\Delta_H=\{0\}$.

Let $r_i:E^*\to L_i^*$, $T:E^*\to H^*$, and $U_i:L_i^*\to H^*$ be
restriction. Define $$D=\{p:r_i p\in\Delta_i\text{ for every }i\},\qquad
\phi(p)=\max_i\phi_i(r_i p),\qquad G=\phi^*.$$

::: {#lem:fibers .lemma}
**Lemma 10** (Simultaneous whole-boundary fibers). *$D$ is nonempty
compact polyhedral, $\phi$ is finite continuous convex on it,
$G|_{L_i}\leq f_i$ and $G|_H=f_H$. The attained fiber minimum
$$k(q)=\min_{p\in D,\ Tp=q}\phi(p)$$ has domain exactly $\Delta_H$ and
equals $f_H^*$ there. The separate minimum of $\phi_i$ on
$U_i^{-1}(q)\cap\Delta_i$ equals the same $k(q)$. Every joint minimizer
consequently satisfies $\phi_i(r_i p)=k(q)$ simultaneously for all
pages. The set $$M=\{p\in D:\phi(p)=k(Tp)\}$$ is compact and maps onto
all of $\Delta_H$, including boundary fibers.*
:::

::: proof
*Proof.* $D$ is closed with finite real inequalities. It is bounded: if
$p_n$ were unbounded, normalize and pass to a unit limit; bounded
$r_i p_n$ would force the limit to vanish on every $L_i$, hence on $E$,
impossible. Common support at any $y\in H$ has simultaneous Fenchel
equalities $$\phi_i(r_i p_y)=p_y(y)-f_H(y),$$ so $p_y\in D$ and $D$ is
nonempty. Finite maxima give whole continuity and convexity of $\phi$.
From $\phi\geq\phi_i\circ r_i$ get $G|_{L_i}\leq f_i$. Fenchel
equalities at each $y$ give the reverse inequality on $H$.

Compact fibers attain minima. Mixing minimizers proves convexity of $k$.
For a convergent sequence of $q$ values, pass to a convergent
subsequence of minimizing $p$ values along the lower limit; this proves
lsc, also for its infinity extension because $T(D)$ is closed. Its
domain $T(D)$ is a compact polytope, so
Lemma [4](#lem:support){reference-type="ref" reference="lem:support"}
proves whole continuity there and biconjugacy. Grouping the transform
supremum by fibers gives $k^*=G|_H=f_H$; hence $k=f_H^*$, including
entire domains, and $T(D)=\Delta_H$.

Repeat this argument for each single-page restriction $U_i$ and
$\phi_i$. Its fiber minimum has conjugate $f_i|_H=f_H$, so biconjugacy
gives the same function $k$ with the same whole domain. Therefore every
$\phi_i(r_i p)\geq k(Tp)$. At a joint minimizer their maximum equals
$k(q)$, forcing equality for every page. Continuity of $k$ and $\phi$
makes $M$ closed in compact $D$, and attainment gives surjectivity. No
independence of restriction coordinates and no rationality of the actual
dual polytopes has been assumed. ◻
:::

::: {#thm:trace .theorem}
**Theorem 11** (Prescribed trace, arbitrary trace support, finite PA
extension). *Suppose $g$ is a finite convex genuine rational-spatial
real-PA function on the entire $H$ such that $$f_H\leq g\leq f_H+a,$$
for some finite $a\geq0$. For every $b>0$ there are convex genuine
rational-spatial real-PA functions $Q_i$ on the whole new pages with
$$f_i\leq Q_i\leq f_i+a+b,
\quad Q_i|_H=g,
\quad Q_i^\infty=h_i.$$ For every $y\in H$ and *every*
$q\in\partial g(y)$ there is one $p\in E^*$ with $Tp=q$ supporting all
$Q_i$ on their entire pages at $y$.*
:::

::: proof
*Proof.* Let $c=g^*$. Since $g$ is bounded relative to the actual trace
reference, Lemma [7](#lem:dual){reference-type="ref"
reference="lem:dual"} gives entire domain $\Delta_H$, whole continuity,
and $k-a\leq c\leq k$. For each page form the closed convex upward set
$$K_i=\operatorname{conv}\bigl(\operatorname{graph}\phi_i\ \cup\
\{(r_i p,c(Tp)):p\in M\}\bigr)+\mathbb R_{\geq0}(0,1).$$ Both generating
sets are compact; Lemma [3](#lem:finite){reference-type="ref"
reference="lem:finite"} makes their hull compact, so $K_i$ is closed.
Its projection is the whole compact $\Delta_i$, and all heights are
uniformly bounded below. Fibers have finite attained bottoms $\psi_i$.
Convexity and closedness give a finite lsc convex function, continuous
on the entire polytope by Lemma [4](#lem:support){reference-type="ref"
reference="lem:support"}.

At original graph sources $\psi_i$ has sources at $\phi_i$; at added
sources Lemma [10](#lem:fibers){reference-type="ref"
reference="lem:fibers"} gives $\phi_i(r_i p)=k(Tp)$ and
$c(Tp)\geq\phi_i(r_i p)-a$. Thus convexity of
$\operatorname{epi}(\phi_i-a)$ implies $$\phi_i-a\leq\psi_i\leq\phi_i.$$
Every source is also at or above $c\circ U_i$: for graph sources
$\phi_i(z)\geq k(U_i z)\geq c(U_i z)$, and added sources have equality.
Convexity gives $\psi_i\geq c\circ U_i$. For any $q\in\Delta_H$, choose
one joint $p\in M$ over it. The added sources and this lower bound give
$$\psi_i(r_i p)=c(q)\quad\hbox{for every }i,
\qquad \min_{U_i z=q}\psi_i(z)=c(q).$$ Set $F_i=\psi_i^*$. These
full-page functions are finite continuous convex, lie between $f_i$ and
$f_i+a$, have exact recession $h_i$ from their compact dual domains and
bounded dual heights, and grouping by the exact fibers gives
$F_i|_H=c^*=g$.

Fix now any $q\in\partial g(y)$. Fenchel equality gives
$g(y)=q(y)-c(q)$, and $q\in\Delta_H$. Choose one joint $p\in M$ with
$Tp=q$. For every page and every $x$,
$$F_i(x)\geq(r_i p)(x)-\psi_i(r_i p)
=p(x)-c(q)=g(y)+p(x-y).$$ This proves a simultaneous lift for the
*chosen* $q$, not merely existence of some support of $g$.

We next make $F_i$ finite PA without changing its trace. A finite
rational carrier of $g$ can be refined by rational coordinate orthants,
if needed, to make its cells pointed. Each cell has finite rational
point/ray generators from Lemma [3](#lem:finite){reference-type="ref"
reference="lem:finite"}; its lifted affine graph uses actual $g$ heights
and recession $h_H$ heights. Let $V$ contain all these finitely many
spatial point generators. Convexity and the recession inequality, in
both directions of inclusion, prove the *entire* identity
$$\operatorname{epi}g=\operatorname{conv}\{(v,g(v)):v\in V\}+\operatorname{epi}h_H.$$
For $H$ a point there is one lift and the vertical ray. Apply
Proposition [9](#prop:primal){reference-type="ref"
reference="prop:primal"} to $F_i$ with tolerance $b$, appending all of
$V$. Its hypotheses hold because $F_i$ is bounded relative to the
unchanged $\gamma_i$. The resulting $Q_i\geq F_i$ have exact recession
$h_i$. Their primal epigraphs contain every trace lift and the
restriction $\operatorname{epi}h_H$ of the exact recession cone. The
whole trace epigraph identity gives $Q_i|_H\leq g$; the reverse bound is
$Q_i\geq F_i$. Hence equality holds on all of $H$, including every
unbounded trace cell. Every previously constructed $F_i$ support at a
trace point is below $Q_i$ and still touches there. This retains
simultaneous lifts for every $q\in\partial g(y)$ and proves all the
assertions. Intermediate $F_i$ and $\psi_i$ receive no measure. ◻
:::

# Finite assembly through several different overlaps

::: {#lem:amalgam .lemma}
**Lemma 12** (Affine support amalgamation). *Let affine $A,E$ meet in
nonempty $H$. If two linear forms on their tangent spaces agree on the
tangent space of $H$, they extend to one linear form on the tangent
space of $\operatorname{aff}(A\cup E)$ whenever that intersection of
tangent spaces is precisely the tangent space of $H$.*
:::

::: proof
*Proof.* Choose an origin in $H$. Define $p(u+v)=p_A(u)+p_E(v)$. Two
decompositions differ by a vector in the intersection, so agreement
there proves well-definedness. Extend by a complementary basis to the
ultimate ambient space if needed. Rationality of the geometry is not a
rationality requirement on the actual form's values. ◻
:::

::: proof
*Proof of Theorem [2](#thm:main){reference-type="ref"
reference="thm:main"}.*
Proposition [6](#prop:criterion){reference-type="ref"
reference="prop:criterion"} supplies full-page convexity and common
supports for the original $f$ and $\gamma$. Choose $t=\epsilon/(r+1)$.
On the root page Proposition [9](#prop:primal){reference-type="ref"
reference="prop:primal"} gives $P_0$ with $f\leq P_0\leq f+t$ and actual
recession. Maintain the induction invariants on $X_{j-1}$: finite
rational-spatial real PA, continuity and page convexity, common
entire-page supports at every real point, exact actual page recession,
and global error at most $jt$. No earlier page value will be changed.

Let $Q_{\rm par}$ be the parent page of $B_j$, and set
$$g_j=P_{j-1}|_{H_j}.$$ This is a genuine convex rational-spatial
real-PA whole trace. It satisfies $f_{H_j}\leq g_j\leq f_{H_j}+jt$ and
has exact actual trace recession. Restricting the original $f$ to the
new group supplies all hypotheses of
Theorem [11](#thm:trace){reference-type="ref" reference="thm:trace"},
including its common supports. Apply it with $a=jt$, $b=t$. It gives new
whole-page functions $Q_{j,a}$ with error at most $(j+1)t$, exact $g_j$
trace and exact actual recession.

At a real $y\in H_j$, the induction hypothesis gives $p_{\rm old}$
supporting all earlier pages containing $y$. Extend it to the whole
tangent space of $A_{j-1}$ if it was initially specified only on
incident pages. The parent is one of those pages. Consequently
$$q=p_{\rm old}|_{T H_j}\in\partial g_j(y),$$ because restriction of its
whole-parent support supports the entire trace.
Theorem [11](#thm:trace){reference-type="ref" reference="thm:trace"}
lifts this *same* $q$ to $p_{\rm new}$ supporting every new page.
Condition $E_j\cap A_{j-1}=H_j$ and
Lemma [12](#lem:amalgam){reference-type="ref" reference="lem:amalgam"}
combine them into one ambient form supporting all incident old and new
pages at $y$.

Away from $H_j$, no point belongs to both an old and a new page, since
$B_j\cap X_{j-1}=H_j$. In the new group away from $H_j$, only one new
page is present, giving ordinary convex supports. All other earlier
supports remain valid. This covers, in particular, every intersection
$H_j\cap H_l$ and every smaller face in such intersections. It never
assumes that a smaller face is exposed in a hull of all incident pages.
It uses the actual common support already present there and lifts its
trace restriction. Continuity follows from the common whole traces and
finite closed-page gluing.
Proposition [6](#prop:criterion){reference-type="ref"
reference="prop:criterion"} proves every printed PCC, not just PCCs
along the newly attached subspace.

Finite rational carriers on each page can be made compatible without
comparing real coefficients. Take rational wall equations for each
polyhedral cell, equations cutting every page intersection into faces,
and all original-carrier wall equations. Extend these rational page
equations to ambient rational equations by rational affine linear
algebra. The induced finite ambient hyperplane arrangement, restricted
to all pages, refines every page carrier and the original complex.
Because it is one arrangement, intersections of cut cells in different
pages are common faces. There are finitely many cells. Matching
coefficients define a rational kernel as in
Lemma [8](#lem:graph){reference-type="ref" reference="lem:graph"},
proving one genuine global $\operatorname{PA}_\mathbb R$ function.
Values, supports and recession have not changed. The induction is
complete, and after $r$ steps the bound is $(r+1)t=\epsilon$.

At any point of an original face, all incident original cells lie in
complete pages containing that point. The common entire-page support
thus works on their entire closed cells. This proves the all-face
assertion for all real points, rather than for finitely many graph
contacts.

For a decreasing sequence take unshifted $Q_n$ with
$0\leq Q_n-f\leq\eta_n$, $\eta_n=2^{-n}$, $n\geq1$, and put
$P_n=Q_n+4\eta_n$ on every page. Then $$4\eta_n\leq P_n-f\leq5\eta_n,
\qquad P_n-P_{n+1}\geq4\eta_n-5\eta_{n+1}=\tfrac32\eta_n>0.$$ Common
shifts retain all trace equalities and all supporting forms, and change
no recession. They yield global uniform convergence and relative norm at
most $C+5/2$. Exact contacts belong to the unshifted construction; they
are not claimed for shifted approximants. ◻
:::

This proof has a finite number of geometric extension steps for each
requested accuracy. Its termination comes from the free-span
presentation and a one-way error budget. It is not repeated single-face
correction on arbitrary incident original proper cells. At a branching
parent, several traces are fixed by the *same* parent PA function;
extending one child never modifies another trace or the parent. Multiple
overlaps inside dependent blocks are handled simultaneously by the
compact dual construction, not by independent page roofs.

# The actual all-obstacle endpoint and original conventions

::: {#prop:balance .proposition}
**Proposition 13** (Positive real balance and PA positivity). *The page
arrangement of Theorem [2](#thm:main){reference-type="ref"
reference="thm:main"} is a finite pure globally embedded balanced
rational space with arbitrary specified positive real constant page
weights. Its approximants have nonnegative tangent-corrected primitive
divisor coefficients against every nonnegative balanced local test
cycle, in every dimension.*
:::

::: proof
*Proof.* Use a common rational hyperplane carrier. Top cells lie in
unique complete pages because distinct $d$-pages meet in lower
dimension. At each facet in a page, the two adjacent top cells have
equal page weight and opposite saturated primitive inward quotient
classes. They cancel separately in each page. Sum the page contributions
at a facet contained in several pages. This proves every facet balancing
equation with actual real weights and omits no boundary face.

For a $k$-dimensional local test cycle $c\geq0$ on a common carrier and
a $(k-1)$-face $\rho$, take a common support $p$ of the approximant at a
relative interior point. Its derivative agrees with the approximant's
face derivative along $\rho$, by testing both tangent signs. The exact
positive-convex primitive formula is
$$(P\cdot c)(\rho)=\sum_{\sigma\succ\rho}c(\sigma)P_\sigma(n_{\sigma/\rho})
-P_\rho\!\left(\sum_{\sigma\succ\rho}c(\sigma)n_{\sigma/\rho}\right).$$
Subtract the supporting form. Balancing cancels its contribution, and
every inward residual derivative is nonnegative, so the coefficient is
nonnegative. A tangent change of normal lift cancels because tangent
derivatives agree. This is valid for real coefficients and specified
nonnegative real test weights without a gcd argument or a unit-normal
substitution. It establishes PA positivity and printed PC in their fixed
meanings; it does not construct a recursive extended operator. ◻
:::

::: {#cor:envelope .corollary}
**Corollary 14** (Every actual $C_b$ envelope). *Under
Theorem [2](#thm:main){reference-type="ref" reference="thm:main"}, for
every $u\in C_b(X)$ the actual unrestricted envelope
$$P_\gamma(u)(x)=\sup\{q(x):q\in\operatorname{PC}_q,\ q\leq\gamma+u,
\ q\leq\gamma+C_q\text{ globally for some }C_q\in\mathbb R\}$$ admits
the genuine globally uniform decreasing real-PA PC approximation just
proved, with the same actual reference growth. In particular every
bounded genuine real-PA obstacle is included, without a separability
condition.*
:::

::: proof
*Proof.* Proposition [13](#prop:balance){reference-type="ref"
reference="prop:balance"} verifies the finite positive all-face balanced
embedded hypotheses. The qualified whole grant R230,
unrestricted-envelope theorem, applies to this actual continuous PC
reference and arbitrary bounded continuous $u$. It gives that this exact
envelope is continuous, printed PC, and
$$\gamma+\inf_Xu\leq P_\gamma(u)\leq\gamma+u\leq\gamma+\sup_Xu.$$
Therefore it is a target of Theorem [2](#thm:main){reference-type="ref"
reference="thm:main"}, which supplies PA approximation as a separate
step. R230 alone does not supply that step. Competitors have not been
replaced by PA or sampled competitors. If desired the upper-only growth
envelope equals the bounded-relative competitor envelope: replace any
competitor by $\max(q,\gamma-\|u\|_\infty)$. The maximum preserves
printed Jensen inequalities and stays below the obstacle. No rational-PA
maximum closure is required for this competitor comparison. ◻
:::

Literal PA is separate. Gaussian elimination in
Lemma [8](#lem:graph){reference-type="ref" reference="lem:graph"}
produces a real linear combination of literal basis functions, not
literal slopes or rational actual heights. Thus neither theorem above
proves literal regularity. The catalogue's noncompact literal
obstruction is part of the controlling context, not a newly supplied
proof grant for this manuscript. We do not reprove or import its absent
input bodies. Likewise the asserted equivalence in frozen BMPS Theorem
6.4 between endpoint regularity and density in all printed PC is not
imported. The function zero on rational points and minus one elsewhere
on a rational line satisfies every printed PCC and is discontinuous; the
endpoint corollary deals with actual continuous-obstacle envelopes using
R230 completion, rather than declaring all raw printed-PC functions
continuous.

For calibration only, if $a_\sigma$ is the Euclidean covolume of the
saturated tangent lattice, a basis for $N_\rho$ followed by a primitive
normal lift is a basis for $N_\sigma$. Base times perpendicular height
gives $$\operatorname{pr}_{T_\rho^\perp}n_{\sigma/\rho}
=\frac{a_\sigma}{a_\rho}\nu_{\sigma/\rho},\qquad a_{\text{point}}=1.$$
This holds at every dimension, not only at top facets. Unit-conormal
flux weights would therefore be $a_\sigma c(\sigma)$. Our positivity
proof uses primitive normals directly. No BBGS negative-concavity sign
or Euclidean weight normalization is substituted into the BMPS
positive-convex formula, and no factorial is appended to that formula.
No contact or MA conclusion is asserted.

# A seven-plane application with dependent directions and two overlaps

In $\mathbb R^6$ with standard lattice let
$$Q_0=\operatorname{span}(e_1,e_2),\quad
v_1=e_3,\ v_2=e_4,\ v_3=-e_3-e_4,\quad
w_1=e_5,\ w_2=e_6,\ w_3=-e_5-e_6.$$ Attach
$Q_{1,i}=\operatorname{span}(e_1,v_i)$ along $H_1=\mathbb Re_1$, and
then $Q_{2,i}=\operatorname{span}(e_2,w_i)$ along $H_2=\mathbb Re_2$.
Each group has dependent transverse sum zero. Its distinct pages meet
exactly in its designated line. The first group span intersects $Q_0$ in
$H_1$, and the second group span meets the earlier span
$\operatorname{span}(e_1,e_2,e_3,e_4)$ exactly in $H_2$. Cross-group
page intersections are the origin. These assertions follow directly by
equating coordinates. They verify
Definition [1](#def:free){reference-type="ref" reference="def:free"}
with $r=2$.

The actual admitted literal reference
$$\gamma(x)=|x_1+x_2|+|x_1-x_2|+\sum_{k=3}^6|x_k|$$ is the restriction
of an ambient convex integral-slope rational-carrier function. Its
recession is strictly positive on every nonzero ambient direction: the
six displayed linear forms have zero joint kernel. Give the seven pages
any strictly positive real weights;
Proposition [13](#prop:balance){reference-type="ref"
reference="prop:balance"} verifies all-face balance. The two lines are
actual unbounded positive-dimensional overlaps; they are different and
meet at the origin. No one rational $H$ is the pairwise intersection of
all pages, so this arrangement is outside the exact common-$H$ geometry
of S298.

A concrete non-PA, nonseparable continuous target is
$$f(x)=\phi(x_1+x_2)+\phi(x_1-x_2)+\sum_{k=3}^6\phi(x_k),
\qquad \phi(t)=\sqrt{1+t^2}-1.$$ Since $\phi''(t)=(1+t^2)^{-3/2}>0$, it
is ambient convex and hence satisfies every printed PCC on $X$. The
elementary inequalities $|t|\leq\sqrt{1+t^2}\leq |t|+1$ give
$-6\leq f-\gamma\leq0$ globally. On the root page, at
$(x_1,x_2)=(1/2,1/2)$, the mixed derivative is $1/(2\sqrt2)-1\ne0$. Thus
its root restriction is not a sum of functions in the two root
coordinates. The theorem regularizes this target and, more generally,
*every* continuous relative-PC target and actual $C_b$ envelope on this
arrangement. The example is an application illustration, not a
replacement for that universal quantifier.

Products with $\mathbb R^k$, $k\geq0$, preserve the presentation:
replace every page, span, and $H_j$ by its product with $\mathbb R^k$.
The affine intersection equalities become their products. Adding
$\sum|z_l|$ to the actual reference gives strictly positive actual
recession; the corollary admits every bounded continuous obstacle on the
product, including obstacles depending jointly on page and product
coordinates. This supplies genuinely several-overlap examples in every
dimension $d=2+k$.

The theorem also admits rational affine translations and
zero-dimensional attachment subspaces. They are already covered by
translating an origin in each $H_j$ for the individual extension step.
No assertion about empty attachment subspaces, compactified pages,
proper original-cell extension, or infinitely many attachment steps is
made.

# Comparison with the exact residual and retained failed routes

This is a new finite feasibility construction for a geometric class with
several distinct positive-dimensional overlaps and dependent attached
groups. The underlying common-$H$ compact dual mechanism is
independently reconstructed, not presented as new general
classification. The new assertion is the assembly theorem, the
arbitrary-trace-support lift needed at old multiple intersections, and
the finite global error bound without revising earlier traces. These
give existence of a finite feasible rational carrier in this class,
rather than only checking a specified carrier.

The full original residual remains unresolved. General finite positive
balanced complexes may have proper noncompact cells, several non-free
overlap directions, or incidence loops that revisit an already
constructed span. For these geometries
Definition [1](#def:free){reference-type="ref" reference="def:free"}(3)
can fail. Then $p_{\rm old}$ and $p_{\rm new}$ must agree on an
intersection larger than $T H_j$, while
Theorem [11](#thm:trace){reference-type="ref" reference="thm:trace"}
controls only the trace restriction. The amalgamation proof has no
conclusion. Changing the reference or pretending those extra matching
equations are independent would not repair it. The present construction
supplies no necessity theorem and no counterexample to density outside
its geometric class.

We considered a general closure of finite cell epigraphs under all
incident-face barycenters. A fixed point would satisfy the desired
common supports if all whole-cell conditions held, but a finite initial
generator list does not prove a finite generator list for that closure.
Aggregating intermediate locations into one mass and one barycenter per
face also does not justify local endpoint assignments after
disaggregation. No finite rational-carrier closure or refinement-uniform
separation constant was established by that route; it is left unproved,
and no result here depends on it. This records an unresolved approach,
not a density obstruction. Nor is cyclic nontermination alone a failure
of density.

The unreviewed ROOT310, ROOT304 and native231 mathematical bodies are
not premises. Their labels are not support IDs. We have used only
native231's bound scope/coverage descriptions to identify the previously
attempted methods, and the complete bound registration-history record as
history. No mathematical limitation theorem from them is imported. Their
formulas would require local reconstructed notes before being used as
mathematical support.

The exact historical binding records provider generation completed with
exit code zero, but Xean registration rejected the native231 FINAL with
"Unknown, dead, or forward support: S306". Its then-input had zero
structured notes, while its task text named five grants. This is a
registration failure described in immutable data, not mathematical
rejection or acceptance. The present input registers exactly B225, R230,
S306, S307 and S298. Only B225 and R230 are mathematical imported
dependencies of our output; all other new essential steps have proofs
here. Missing A224/S262/S272/S291/S292/S295 bodies give no grant through
a bibliography.

The frozen BMPS Definition 2.4 is globally embedded in one
$N_\mathbb R$. The qualified B225 noncompactness theorem therefore
excludes nonempty finite compact positively balanced embedded supports
of positive dimension. This is a source-category statement. It does not
dispose of the catalogue's potentially broader compact-charted or
compactification residual. We do not claim original closure from that
empty source branch, and do not assign a general operator on a broader
chart category. Both B225's explicit-continuity and
bounded-chart-decomposition qualifications are retained.

# Source application, execution, and proof coverage

The only imported mathematical assertions are R230's actual
unrestricted-envelope continuity/identification, with its complete
annotation, and B225's finite embedded noncompactness, with its complete
annotation, for the scope comparison. Their whole authoritative TeX
bodies and annotations were displayed in bounded complete chunks. Their
internal historical claims are retained as history, not recertified by
our execution. No absent theorem mentioned inside either body supplies a
premise here.

The four frozen BMPS/BBGS PDF and text files are the only primaries.
BMPS is arXiv:2603.08664v1, submitted 9 March 2026, manuscript dated 10
March 2026. Its actual current literal-newline locators include
Definitions 2.1--2.4 at 257--291; 2.18--2.20 at 420--449; 2.27--2.29 at
499--522; 2.31--2.33 at 532--562; 3.1--3.4 at 689--786; 3.14 at
886--893; 3.22--3.23 and their complete proof at 1005--1029; slope
positivity 4.15 at 1741--1746; and 6.1--6.6 at 2257--2318. All immediate
units applied were read whole. The printed PA/PC equivalence proof and
Theorem 6.4 were read but not imported; our support and completion
arguments retain actual real domains without their potentially
problematic rational-center/weight steps. Remark 6.6 itself identifies
the unresolved polyhedrality of general polyhedral convex hulls.
Definition 6.2, rather than a PA-only envelope, controls
Corollary [14](#cor:envelope){reference-type="ref"
reference="cor:envelope"}.

These locators refer to the supplied frozen text split by the literal
newline character, preserving formfeeds. Some older grant locators
differ; their original historical claims are not silently rewritten as
fresh source reads. The sole BBGS files were hash-verified but no BBGS
theorem is a new essential application here. In particular no claim to a
fresh read of its entire 3.15 or its PDFs is made; the supplied
mandatory corrections that its whole 3.15 ends at LF670 remain unchanged
history. The ledger contains URLs, versions, exact hashes, actual
applications and exclusions, and our own analysis without long
third-party extracts.

The coverage is complete for the claimed scope:
Lemma [3](#lem:finite){reference-type="ref" reference="lem:finite"}
supplies finite generation and signed lineality;
Lemma [4](#lem:support){reference-type="ref" reference="lem:support"}
supplies supports and all boundary duality;
Lemma [5](#lem:density){reference-type="ref" reference="lem:density"}
supplies actual real-endpoint passage;
Proposition [6](#prop:criterion){reference-type="ref"
reference="prop:criterion"} supplies inherited whole-page convexity and
common supports; Lemmas [7](#lem:dual){reference-type="ref"
reference="lem:dual"}--[8](#lem:graph){reference-type="ref"
reference="lem:graph"} and
Proposition [9](#prop:primal){reference-type="ref"
reference="prop:primal"} supply exact full-page rational primal
geometry; Lemma [10](#lem:fibers){reference-type="ref"
reference="lem:fibers"} supplies simultaneous attained fibers;
Theorem [11](#thm:trace){reference-type="ref" reference="thm:trace"}
supplies whole-trace extension with every supporting form lifted;
Lemma [12](#lem:amalgam){reference-type="ref" reference="lem:amalgam"}
and the main proof supply finite several-overlap assembly;
Proposition [13](#prop:balance){reference-type="ref"
reference="prop:balance"} checks all-face actual-real balance and PA
positivity; Corollary [14](#cor:envelope){reference-type="ref"
reference="cor:envelope"} checks the actual all-$C_b$ endpoint domain.
No coverage entry is a claim of general proper-cell feasibility or
classification.

The own standard-library checker uses only the displayed finite rational
seven-page input, its products for $k=0,1,2,3$, finitely many chosen
support coefficients, and eight dyadic indices. It tests affine
rank/intersection identities, the dependent direction relations, the
explicit support-amalgamation algebra and error budgets. The symbolic
proofs establish the continuum assertions independently. Programs,
input, commands, stdout/stderr, environment details, initial display
limitations, hashes, complete local notes, and no-shell-escape TeX build
logs are preserved. Supplied scripts were neither imported nor executed.
No network, provider nesting, agents, protected runtime/editor mutation,
private ACTIVE data or heavy computation was used. No supervised compute
facility was supplied or needed. The requested model label is task
metadata, not an independently attested provider identity.

Rerun the bounded own work with:

    python exact_checks.py
    pandoc -f latex -t markdown P05.1-paper.tex -o argument.md
    pdflatex -no-shell-escape -interaction=nonstopmode \
      -halt-on-error P05.1-paper.tex
    pdflatex -no-shell-escape -interaction=nonstopmode \
      -halt-on-error P05.1-paper.tex
    python provenance.py

Compilation and finite execution do not establish mathematical
correctness. The notes and paper are ordinary unverified drafts.
**Original P05.1 OPEN; candidate=false.**

::: thebibliography
4 A. M. Botero, E. Mazzon, L. Pille--Schneider, *Monge--Ampere measures
on balanced polyhedral spaces*, arXiv:2603.08664v1, 2026.
<https://arxiv.org/pdf/2603.08664v1>. A. M. Botero, J. I. Burgos Gil, M.
Sombra, *Convex analysis on polyhedral spaces*, Math. Z. 301 (2022),
1631--1674, publisher version.
<https://doi.org/10.1007/s00209-021-02869-6>. Supplied qualified Note
R230, whole authoritative continuous-completion/envelope paper and
mandatory annotation. Supplied qualified Note B225, whole authoritative
balanced-support/maximum-principle paper and mandatory annotation.
:::
