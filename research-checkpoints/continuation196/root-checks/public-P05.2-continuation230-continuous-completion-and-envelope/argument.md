# Continuous completion of rational-endpoint polyhedral convexity

Unverified draft. Original P05.2 remains open; candidate=false. This file contains the complete argument, including proofs and limitations, converted from P05.2-paper.tex.

*Abstract.*

We retain the printed rational-endpoint definition of polyhedral convexity, including its discontinuous functions. On a finite positive balanced rational polyhedral space, every finite-valued function in that class has a unique continuous representative agreeing at every rational point and dominating it everywhere. No boundedness, continuity, or measurability premise is imposed on the original function. The representative is its upper semicontinuous hull and satisfies the corresponding inequalities even with real endpoints. Consequently, for every bounded continuous obstacle and continuous PC reference, the unrestricted printed envelope is continuous and equals the continuous-competitor envelope. An exact positive-spanning criterion characterizes rational-value continuity at the vertex of a finite rational fan. We also identify the unrestricted compact-chart envelope and a uniform-density obstruction for the unrepaired printed PC class. These results do not give real-PA regularization, a general extended Monge--Ampere operator, or the structural contact classification. Original P05.2 remains open; candidate status is false.

## Domain, coefficients, and the exact unresolved target

Let $N$ be a lattice, $V=N\otimes{\mathbb{R}}$, and $X=|\Pi|\subset V$ the support of a finite rational polyhedral complex. Rational means that all affine constraints have rational coefficients; clearing denominators gives the integral-affine convention in the fixed primary version [BMPS](https://arxiv.org/pdf/2603.08664v1). Put $X_{\mathbb{Q}}=X\cap(N\otimes{\mathbb{Q}})$. Every nonempty rational face has dense rational points in its relative interior. For translated cells, use

$$
N_\sigma=N\cap\operatorname{span}_{\mathbb R}(\sigma-\sigma).
$$

A normal $n_{\sigma/\tau}\in N_\sigma$ for a facet $\tau\prec\sigma$ projects to the primitive generator of $N_\sigma/N_\tau$ pointing into $\sigma$. A positive balanced top cycle consists of weights $w_\sigma>0$ such that
$$
\tag{1}
 \sum_{\sigma\succ\tau}w_\sigma n_{\sigma/\tau}\in N_{\tau,{\mathbb{R}}}.

$$
The literal source weights are rational. The geometric proofs also allow positive real weights; no real-weight operator extension is inferred.

A rational-endpoint polyhedral convex combination, or PCC, is

$$
x=\sum_i\alpha_i x_i,\qquad \alpha_i\geq0,\quad\sum_i\alpha_i=1,\quad x_i\in X_{\mathbb{Q}},

$$

with faces $\tau\preceq\sigma_i$ of some rational polyhedral structure on $X$ such that $x\in\tau$ and $x_i\in\sigma_i$. The center and coefficients need not be rational. Write $\operatorname{PC}_q(X)$ for the real-valued functions satisfying every such Jensen inequality. This notation marks the printed definition, rather than changing it. Write $\operatorname{PC}_c(X)=\operatorname{PC}_q(X)\cap C(X)$ and $\operatorname{PC}_q(X,\gamma)=\{q\in\operatorname{PC}_q(X):q-\gamma\text{ is bounded}\}$. A real-endpoint PCC uses the same face constraints but allows arbitrary endpoints in $X$.

The function equal to zero on ${\mathbb{Q}}$ and minus one elsewhere on ${\mathbb{R}}$ belongs to $\operatorname{PC}_q$ and is discontinuous everywhere: each permitted endpoint has value zero, and each center has value at most zero. Thus continuity of every member of $\operatorname{PC}_q$ is false. Our theorem concerns a dominating representative, not equality with the original function.

The class $\operatorname{PA}_{\mathbb{Z}}$ consists of continuous finite piecewise-affine functions with integral tangent slopes and rational constants in rational affine coordinates. The explicitly declared $\operatorname{PA}_{\mathbb{R}}$ allows arbitrary real affine coefficients on a finite *rational* structure. Set $\operatorname{PAPC}_*:=\operatorname{PA}_*\cap\operatorname{PC}_q$ for $*={\mathbb{Z}},{\mathbb{R}}$. In each category let $\operatorname{PC}^{\rm reg}_*(X,\gamma)$ mean uniform decreasing limits of $\operatorname{PAPC}_*$ functions with bounded difference from $\gamma$. No general operator on all continuous $\operatorname{PC}_c$ functions is assumed.

For a continuous PC reference $\gamma$ and bounded continuous $u$, the actual printed envelope is
$$
\tag{2}
 P_\gamma(u)(x)=\sup\{q(x):q\in\operatorname{PC}_q(X),\ q\leq\gamma+u,\ q\leq\gamma+C_q\text{ on }X\text{ for some }C_q\in{\mathbb{R}}\}.

$$
Every bounded obstacle in either PA coefficient category is included. The original problem requires structural necessary and sufficient conditions, all admissible obstacles, genuine membership of these envelopes in the appropriate regularizable operator domain, and the exact contact integral. We resolve the continuity antecedent of (2) on all finite positive balanced spaces. We do not resolve those remaining requirements.

## Finite cone geometry with uniform constants

For a face $\tau\preceq\sigma$, put

$$
C_{\sigma/\tau}=\{t(a-b):t\geq0,\ a\in\sigma,\ b\in\tau\}.

$$

For $z\in\operatorname{relint}(\tau)$ this is the tangent cone of $\sigma$ at $z$, including the lineality $N_{\tau,{\mathbb{R}}}$. This fact and the needed uniform version are proved next.

**Lemma 1 (Uniform rational star geometry).**

Fix a compact set $K\subset\operatorname{relint}(\tau)$. For every $\sigma\succeq\tau$ choose a finite rational generating list for $C_{\sigma/\tau}$, including a rational basis and its negatives for lineality. Let $v_1,\ldots,v_m$ be their union, with zero vectors removed; a generator may carry more than one incident-face assignment. There are constants $r>0$, rational $\varepsilon>0$, and $C>0$, independent of $z\in K$, with the following properties.

For all assigned pairs $(i,\sigma)$, $z+\varepsilon v_i\in\sigma$. If $y\in\sigma$, then $d=y-z\in C_{\sigma/\tau}$ and it has a representation using generators assigned to that cone,
$$
\tag{3}
 d=\sum_i a_i v_i,\qquad a_i\geq0,\qquad\sum_i a_i\leq C\|d\|.

$$
If $d$ is rational the $a_i$ may be chosen rational. Conversely, if $d\in C_{\sigma/\tau}$ and $\|d\|<r$, then $z+d\in\sigma$.

*Proof.*

Write $\sigma$ using rational linear equations for its affine hull and inequalities $A_jx\geq b_j$. An inequality is active on all of $\tau$ precisely when it is active at any point of $\operatorname{relint}(\tau)$. All the other inequalities have positive slack on $K$, with a positive common minimum after taking the finite list. Thus its tangent cone consists exactly of tangent vectors satisfying $A_jd\geq0$ at the active inequalities. To verify equality with the displayed definition of $C_{\sigma/\tau}$, one inclusion follows by subtracting $b\in\tau$ from $a\in\sigma$. For the reverse inclusion choose $z\in\operatorname{relint}(\tau)$ and a sufficiently small $t>0$; inactive slack gives $z+td\in\sigma$ and $d=t^{-1}((z+td)-z)$. The common slack also proves the stated uniform radius $r$. Taking $\varepsilon$ positive rational and sufficiently small handles every assigned generator uniformly.

Here is an elementary justification that the cones have finite rational generating lists. A cone given by finitely many rational homogeneous inequalities has rational lineality. Mod out that lineality. In the pointed quotient, choose a rational linear form strictly positive on the cone away from zero (for instance the sum of a defining inequality list after its joint kernel has been removed). Its section at value one is a bounded rational polytope. This polytope is the convex hull of its finitely many vertices: from a point not yet a vertex, move in both directions in the kernel of its active constraints until an additional independent constraint becomes active, and recurse; boundedness supplies both endpoints and the recursion terminates. The vertices solve rational full-rank systems and hence are rational. Lifting their rays and adjoining a basis and its negatives for lineality supplies the list.

For any representation by a given list, eliminate dependent active columns. If $\sum_i b_i v_i=0$ is a nonzero relation among active columns, change its sign to have a positive entry and subtract $t b_i$ from $a_i$, where $t=\min_{b_i>0}a_i/b_i$. This preserves nonnegativity and the vector represented and removes at least one active column. Iteration leaves an independent subset. On any independent subset the unique coefficient vector is a linear inverse of its column map; consequently its $\ell^1$ norm is at most $C_T\|d\|$. There are finitely many subsets, so take their maximum for $C$. For rational $d$ the independent rational system has a rational solution, by Gaussian elimination. The zero vector uses the empty representation. This proves (3) without a boundedness assumption on any function.

∎

**Definition 2.**

The star at $\tau$ is positively spanning if the cone generated by $\bigcup_{\sigma\succeq\tau} C_{\sigma/\tau}$ is its linear span. Equivalently, for any generating list as above there are $\lambda_i\in{\mathbb{Q}}_{>0}$ with
$$
\tag{4}
 \sum_i\lambda_i v_i=0.

$$

*Proof of the equivalence in the definition.*

A positive relation writes each $-v_i$ as a nonnegative combination of the other generators, so their cone is their span. Conversely, if the cone is the span, express each $-v_i$ as a nonnegative combination of the list. The elimination argument in Lemma 1 makes each representation rational. Add the resulting relations $v_i+\sum_j b_{ij}v_j=0$. Every coefficient is then rational and at least one, proving (4).

∎

**Lemma 3 (Positive balancing implies positive spanning).**

Every star of a finite positive balanced rational complex is positively spanning. The same holds for a positive balanced rational fan with common lineality.

*Proof.*

We reconstruct the relevant geometric result from caller manuscript B rather than import a continuity theorem. The star inherits its top weights. A face $C_{\delta/\tau}$ corresponds to a face $\delta\succeq\tau$ of the original complex, its tangent lattice is $N_\delta$, and its primitive normal classes for adjacent facets are unchanged. This follows from the active-inequality description in Lemma 1: tangent spaces are the original tangent spaces and inward facet signs agree. Thus the inherited star weights are strictly positive and balanced.

It remains to prove positive spanning for such a fan $\Sigma$ of dimension $d\geq1$. Choose a Euclidean inner product. Let $a_\sigma$ be the covolume of $N_\sigma$ in its tangent space and set $c_\sigma=w_\sigma a_\sigma>0$. For a facet $\delta$, the perpendicular projection of its primitive inward normal has length $a_\sigma/a_\delta$. Indeed a basis of the saturated $N_\delta$ followed by that normal is a basis of $N_\sigma$, and its parallelotope volume is base covolume times perpendicular height. Let $\nu_{\sigma/\delta}$ be the inward unit conormal. Projecting (1) gives

$$
\sum_{\sigma\succ\delta}c_\sigma\nu_{\sigma/\delta}=0.
$$

The ordinary divergence formula therefore yields, for every compactly supported $C^1$ ambient vector field $Y$,
$$
\tag{5}
 \sum_{\sigma\in\Sigma(d)}c_\sigma\int_\sigma \operatorname{div}_\sigma Y\,d\operatorname{vol}_d=0.

$$
The outward boundary contributions are minus these unit conormals and cancel at each facet. For unbounded cones truncate beyond the support of $Y$, where the new boundary contribution is zero. Lower faces have zero facet measure. In dimension one this is the ordinary fundamental theorem on weighted edges. The divergence formula used here is elementary, obtainable by triangulating polyhedra and integrating derivatives in one variable; it is not a tropical operator.

Take $Y(x)=b\chi(\|x\|)$ for a constant vector $b$, with a smooth radial cutoff equal to one near zero, nonincreasing, zero far out, and strictly decreasing on an interval. Since $x$ lies in the tangent space of any cone containing it,

$$
\operatorname{div}_\sigma Y(x)=\chi'(\|x\|)\langle b,x\rangle/\|x\|.
$$

Polar integration in each $d$-dimensional tangent space turns (5) into

$$
0=\left(\int_0^\infty\chi'(r)r^{d-1}\,dr\right)
 \sum_{\sigma}c_\sigma\int_{\sigma\cap S(V)}\langle b,\theta\rangle\,dS_{d-1}(\theta).

$$

The first factor is strictly negative. In dimension one the angular integral is the sum over unit directions. If a linear form is nonnegative on the support and positive somewhere, it is positive on a relatively open angular subset of a top cone. That subset has positive angular measure, all other integrals are nonnegative, and every $c_\sigma$ is positive, contradicting the displayed identity. Hence every nonnegative linear form on the support vanishes on its span. The cone generated by the finite support is finitely generated and closed: for a converging sequence of represented vectors, the independent-column elimination in Lemma 1 gives uniformly bounded nonnegative coefficients; a subsequence with one fixed column subset converges to a representation of the limiting vector. If this cone $D$ were proper in its span, choose $y$ in that span outside $D$ and let $p$ be its nearest point in $D$. Existence follows by minimizing distance on a closed bounded portion. Differentiating the squared distance along the segment from $p$ to $z\in D$ gives $\langle p-y,z-p\rangle\geq0$. Taking $z=0,2p$ gives $\langle p-y,p\rangle=0$. Thus $\ell(z)=\langle p-y,z\rangle$ is nonnegative on $D$ while $\ell(y)=-\|p-y\|^2<0$. It is nonzero on the span and hence positive somewhere on the support, contradicting the preceding angular calculation. This proves positive spanning. Dimension zero has only the zero tangent space and needs no generators.

∎

## Two rational Jensen estimates and automatic rational bounds

Fix a face $\tau$ with positively spanning star, a compact inner set $K\subset\operatorname{relint}(\tau)$, the geometry of Lemma 1, and a positive relation (4). Put

$$
\Lambda=\sum_i\lambda_i,\quad \lambda_{\min}=\min_i\lambda_i,\quad H=\frac{C\Lambda}{\varepsilon\lambda_{\min}},\quad
 L=\frac{C}{\varepsilon}\max\{1,\Lambda/\lambda_{\min}\}.

$$

The zero-star case is an isolated rational point and is omitted from these formulas.

**Lemma 4 (Exact transverse estimates).**

Let $q\in\operatorname{PC}_q(X)$, $z\in K\cap X_{\mathbb{Q}}$, and $y\in\sigma\cap X_{\mathbb{Q}}$ for $\sigma\succeq\tau$. Put $d=y-z$ and choose the rational representation (3). Assume $C\|d\|\leq\varepsilon$. All endpoints $z_i=z+\varepsilon v_i$ are rational and lie in their assigned incident faces.

If $m_0\leq q\leq M_0$ at $z,y,z_1,\ldots,z_m$, then
$$
\tag{6}
 |q(y)-q(z)|\leq (M_0-m_0)L\|y-z\|.

$$
There is also a lower inequality requiring no lower bound on $q$:
$$
\tag{7}
 q(y)\geq q(z)+\sum_i b_i(q(z)-q(z_i)),\qquad
 b_i=\frac{t\lambda_i-a_i}{\varepsilon}\geq0,\quad
 t=\max_i\frac{a_i}{\lambda_i},\quad \sum_i b_i\leq H\|d\|.

$$

*Proof.*

Write $A=\sum_i a_i$. The equality

$$
y=(1-A/\varepsilon)z+\sum_i(a_i/\varepsilon)z_i
$$

is a PCC with center in $\sigma$: omit indices $a_i=0$ from its endpoint list, so every remaining generator is assigned to $C_{\sigma/\tau}$ and every endpoint lies in $\sigma$. Its coefficients are nonnegative and sum to one. This constructs a valid combination and does not change the printed weak definition for other combinations with zero coefficients. Hence
$$
\tag{8}
 q(y)-q(z)\leq\sum_i\frac{a_i}{\varepsilon}(q(z_i)-q(z)).

$$
For the other direction, using the positive relation gives

$$
d+\sum_i b_i\varepsilon v_i=d+t\sum_i\lambda_i v_i-\sum_i a_i v_i=0.

$$

Thus $z$ is the PCC of $y$ with unnormalized coefficient one and of the $z_i$ with coefficients $b_i$. Its center lies in $\tau$ and each endpoint lies in a face containing $\tau$, including $y\in\sigma$. Normalizing by $1+\sum b_i$ and rearranging proves (7). Since $t\leq C\|d\|/\lambda_{\min}$,

$$
\sum_i b_i=(t\Lambda-A)/\varepsilon\leq H\|d\|.
$$

Bounding the value differences in (8) and (7) by $M_0-m_0$ proves (6). Every invocation has rational endpoints. No continuity of $q$ is used.

∎

**Lemma 5 (No boundedness premise is needed).**

If every star of $\Pi$ is positively spanning and $q:X\to{\mathbb{R}}$ belongs to $\operatorname{PC}_q(X)$, then its restriction to $X_{\mathbb{Q}}$ is locally bounded above and below at every point of $X$, including irrational points.

*Proof.*

Let $p\in\operatorname{relint}(\tau)$ and choose a compact relative neighborhood $K\subset\operatorname{relint}(\tau)$ of $p$. Take the uniform constants and generators above. A sufficiently small neighborhood of $p$ meets only faces containing $\tau$: there are finitely many closed other faces, none containing $p$. Choose $z\in K\cap X_{\mathbb{Q}}$ sufficiently close to $p$, then a neighborhood $W$ of $p$ sufficiently small, so that $C\|y-z\|\leq\varepsilon$ for all $y\in W$ and every such $y$ belongs to an incident face. The single fixed finite list $z,z_i$ has finite values. Put $M=\max\{q(z),q(z_1),\ldots,q(z_m)\}$. Formula (8) gives $q(y)\leq M$ for every rational $y\in W$. Formula (7) gives

$$
q(y)\geq q(z)-H\|y-z\|(M-q(z)).
$$

The right side has a finite uniform lower bound on a smaller bounded $W$. This uses only values at the fixed rational anchor and its rational endpoints. For an isolated zero-dimensional face, take its own finite value. These cases cover $X$.

∎

## The completion theorem, including irrational centers and shared faces

**Lemma 6 (Rational density in a feasible polyhedron).**

Let $D$ be a nonempty polyhedron defined by rational equations and inequalities. Every point $a\in D$ is a limit of rational points of $D$ in its minimal face. Indeed, collect all constraints active at $a$, solve their rational affine system by Gaussian elimination, and approximate the coordinates in a rational affine basis of its solution space. All inactive inequalities are strict at $a$ and remain satisfied for close approximants. This also proves density in every rational affine face.

**Theorem 7 (Continuous completion of the printed PC class).**

Suppose every star of a finite rational complex $\Pi$ is positively spanning. For each finite-valued $q\in\operatorname{PC}_q(X)$ there is a unique $F\in C(X)$ agreeing with $q$ on $X_{\mathbb{Q}}$. It satisfies all real-endpoint PCC inequalities on every rational polyhedral structure, and
$$
\tag{9}
 q(x)\leq F(x),\qquad F(x)=q^*(x):=\limsup_{y\to x}q(y).

$$
In particular $F\in\operatorname{PC}_c(X)$. It is the least continuous majorant of $q$. No local boundedness or measurability assumption on $q$ is required. Conversely, every finite-valued function $q$ agreeing on $X_{\mathbb{Q}}$ with such an $F$ and satisfying $q\leq F$ belongs to $\operatorname{PC}_q(X)$.

All conclusions apply in every dimension to a finite positive balanced rational polyhedral space.

*Proof.*

Lemma 5 gives local rational two-sided bounds. Fix $p\in\operatorname{relint}(\tau)$ and a smaller compact relative neighborhood $K$ around it. The endpoint lists for all rational $z\in K$ remain in a fixed compact neighborhood: their finitely many translations of $K$ are compact subsets of $X$. A finite cover by the neighborhoods in Lemma 5 provides common bounds $m_0,M_0$ on rational values in these endpoint sets and on a small neighborhood of $K$. Consequently (6), with constants uniform in $z\in K\cap X_{\mathbb{Q}}$, applies to nearby rational $y$ in every incident face.

First take $y,z\in\operatorname{relint}(\tau)\cap X_{\mathbb{Q}}$. The same estimate is a local Lipschitz bound there. For any sequence of rational points tending to $p$ within $\operatorname{relint}(\tau)$, the values are Cauchy and their limit is independent of the sequence. This defines a continuous function $F_\tau$ on $\operatorname{relint}(\tau)$ and agrees with $q$ at every rational point of this relative interior. An isolated rational point uses its given value.

Next consider any rational sequence $y_n\to p$ in $X$, potentially lying in different incident faces. Choose rational $z_n\in\operatorname{relint}(\tau)$ with $\|z_n-p\|\leq\|y_n-p\|+1/n$. For large $n$ these belong to $K$, the $y_n$ belong to incident faces, and the estimate just proved gives

$$
|q(y_n)-q(z_n)|\leq (M_0-m_0)L\|y_n-z_n\|\longrightarrow0.

$$

Thus *every* rational sequence tending to $p$ has value limit $F_\tau(p)$. This proves compatibility across all shared faces and at irrational centers; it defines $F$ on $X$ by the unique rational limit.

To verify continuity in the full topology, fix $p$ and its bounds and constants. For a rational $y$ near $p$ in an incident face, let rational $z\in\operatorname{relint}(\tau)$ tend to $p$ in (6). We obtain

$$
|q(y)-F(p)|\leq (M_0-m_0)L\|y-p\|.

$$

For any real $p'$ sufficiently near $p$, take rational $y\to p'$ within this neighborhood, using the rational-limit property already established at $p'$. The last inequality yields

$$
|F(p')-F(p)|\leq (M_0-m_0)L\|p'-p\|.

$$

This is continuity at $p$. We claim no uniform global Lipschitz constant on the noncompact space. Uniqueness follows from density of $X_{\mathbb{Q}}$.

For domination at an irrational $x\in\operatorname{relint}(\tau)$, choose rational simplices in this relative face containing $x$ whose diameters tend to zero. They exist by enclosing $x$ in small rational coordinate boxes lying in the relative interior and triangulating the boxes; a simplex containing $x$ is enough. Its rational vertices $r_j$ and barycentric coefficients give a PCC with center and endpoints in $\tau$. Therefore

$$
q(x)\leq\sum_j\alpha_j q(r_j)=\sum_j\alpha_j F(r_j)\longrightarrow F(x).

$$

At a rational point this is equality. The same construction works in each relative face, including lower-dimensional ones.

It remains to check all PCC inequalities for $F$, with no unproved passage through irrational endpoints. Fix an arbitrary rational carrying structure and an arbitrary real-endpoint PCC $x=\sum_i\alpha_i x_i$ with its faces $\tau\preceq\sigma_i$. Discard zero-coefficient endpoints; the remaining $\alpha_i$ are strictly positive. Write the rational constraints of $\sigma_i$ as $A_ix_i\geq b_i$, including equations as pairs of inequalities, and those of $\tau$ likewise. Introduce perspective variables $t_i=\alpha_i x_i$. The constraints
$$
\tag{10}
 \alpha_i\geq0,\quad\sum_i\alpha_i=1,\quad A_i t_i\geq b_i\alpha_i,\quad \sum_i t_i\in\tau

$$
define a rational polyhedron. The given $(\alpha_i,t_i)$ is a feasible point. Lemma 6 supplies rational feasible approximants $(\alpha_i^{(n)},t_i^{(n)})$, whose coefficients stay positive for large $n$. Hence

$$
x_i^{(n)}=t_i^{(n)}/\alpha_i^{(n)}\in\sigma_i\cap X_{\mathbb{Q}},
 \quad x^{(n)}=\sum_i t_i^{(n)}\in\tau\cap X_{\mathbb{Q}}.

$$

These are actual rational-endpoint PCCs. Applying the original inequalities and using agreement at rational points gives

$$
F(x^{(n)})=q(x^{(n)})\leq\sum_i\alpha_i^{(n)}q(x_i^{(n)})
 =\sum_i\alpha_i^{(n)}F(x_i^{(n)}).

$$

Continuity and convergence of the perspective variables give the desired real-endpoint inequality. This covers every structure witnessing any PCC; it does not rely on a locality theorem for the original discontinuous class.

Since $q\leq F$ and $F$ is continuous, $q^*\leq F$. Rational sequences attain the limit $F(x)$, so $q^*\geq F$. If $G\in C(X)$ majorizes $q$, then $G\geq F$ on the dense rational set and hence everywhere, proving the least-majorant assertion. Conversely, for rational endpoints, $q(x)\leq F(x)\leq\sum_i\alpha_i F(x_i)=\sum_i\alpha_i q(x_i)$; this is exactly the printed inequality. Finally Lemma 3 checks positive spanning for the balanced case.

∎

**Proposition 8 (Exact criterion at the vertex of a fan).**

For the support of a finite rational fan, every finite-valued $\operatorname{PC}_q$ function has a rational restriction continuous at the origin if and only if

$$
\operatorname{cone}(X)=\operatorname{span}_{\mathbb R}(X).

$$

When this condition holds, each such function satisfies $|q(y)-q(0)|\leq C_q\|y\|$ for all sufficiently small rational $y\in X$. This is a criterion at the fan vertex, not a criterion for all the other stars of an unbalanced fan.

*Proof.*

If the fan has lineality, subdivide it by a rational coordinate hyperplane arrangement in its span so that the origin is a vertex; its support and generated cone remain the same. If $\operatorname{cone}(X)$ is its span, take $K=\{0\}$ in Lemmas 5 and 4. The automatic rational bounds use only the star at this vertex, as does (6) with $z=0$. They give the asserted estimate without requiring properties of the other stars.

If the generated cone is proper in its span, separate it by a linear form $\ell$ nonnegative on $X$ and positive somewhere. The function

$$
q(x)=\begin{cases}0,&\ell(x)=0,\\-1,&\ell(x)>0\end{cases}
$$

satisfies even the real-endpoint PCC inequalities. If its center has $\ell=0$, every active endpoint has $\ell=0$; if its center has $\ell>0$, the endpoint average is at least $-1$. Some rational generator $v$ has $\ell(v)>0$. Hence $q(v/n)=-1$ at a rational sequence tending to zero while $q(0)=0$, proving necessity.

∎

**Remark 9 (A failed strengthening).**

The condition at the origin cannot replace the condition at every face in Theorem 7. The unbalanced fan $X={\mathbb{R}}_{\geq0}^2\cup{\mathbb{R}}_{\leq0}^2$ generates ${\mathbb{R}}^2$, but the star at $(1,0)$ is a half-plane. A concrete finite-valued PC function is $q(x,0)=x$ for $x\geq0$, $q(x,y)=0$ for $x\geq0,y>0$, and $q(x,y)=-x$ on the negative quadrant. Here is a check for every PCC, on any carrying structure. At a negative-quadrant center, $q$ agrees with the ambient linear form $-x$, which it majorizes everywhere, proving Jensen. A positive-quadrant center with $y>0$, or the origin, has value zero and all endpoint values are nonnegative. For a center $(x,0)$ with $x>0$, any endpoint of negative second coordinate is impossible: its segment to the center, contained in its incident convex face, would enter the quadrant $x>0,y<0$ outside $X$. All endpoints therefore have nonnegative second coordinate, and the barycenter equation forces the active ones onto the horizontal axis. There $q=|x|$, giving Jensen. Its rational values jump at $(1,0)$ and cannot have a continuous representative. This diagnostic is outside the positive balanced domain and does not refute Theorem 7.

## The true envelope for every bounded continuous obstacle

**Theorem 10 (Unrestricted-envelope identification).**

Let $X$ satisfy Theorem 7, let $\gamma\in\operatorname{PC}_c(X)$, and let $u\in C_b(X)$. The envelope in (2) is finite, continuous, and satisfies all real-endpoint PCC inequalities. It equals the envelope over continuous PC competitors, and its upper semicontinuous regularization is itself. Moreover
$$
\tag{11}
 \gamma+\inf_Xu\leq P_\gamma(u)\leq\gamma+u\leq\gamma+\sup_Xu.

$$
For $u,v\in C_b(X)$, $\|P_\gamma(u)-P_\gamma(v)\|_\infty\leq\|u-v\|_\infty$.

In particular the result holds for every obstacle in $\operatorname{PA}_{{\mathbb{Z}},b}$ and, separately, $\operatorname{PA}_{{\mathbb{R}},b}$ on every finite positive balanced space, including arbitrary nonseparable product obstacles. Positive growth of $\gamma$ is not needed for this continuity result. No PA or regularizable membership of the envelope is asserted.

*Proof.*

The function $\gamma+\inf_Xu$ is a competitor, proving finiteness and the lower bound in (11); the other bounds follow from the obstacle. A pointwise supremum of a nonempty family of $\operatorname{PC}_q$ functions with a finite upper bound is $\operatorname{PC}_q$: for each permitted PCC every competitor satisfies $q(x)\leq\sum_i\alpha_i q(x_i)\leq\sum_i\alpha_i P(x_i)$, and taking the supremum at $x$ proves the inequality for $P$.

Apply Theorem 7 directly to the finite-valued $P$. Its continuous completion $F$ agrees on rational points and dominates $P$. The continuous obstacle and the upper bound $\gamma+\sup_Xu$ pass from rational points to all points, so $F\leq\gamma+u$ and $F\leq\gamma+\sup_Xu$. Thus $F$ is a competitor in the original unrestricted envelope. Maximality gives $P\geq F$, whence $P=F$ and all the stated continuity assertions.

For completeness, each original competitor $q$ also has a completion $F_q$. Since $q\leq\gamma+u$ and $q\leq\gamma+C_q$ on the dense rational set, continuity gives $F_q\leq\gamma+u$ and $F_q\leq\gamma+C_q$ globally. It is a continuous competitor dominating $q$. This proves equality with the continuous-competitor supremum directly, including its global growth constraint.

Finally set $a=\|u-v\|_\infty$. Adding $a$ to any competitor for $v$ makes it a competitor for $v+a$, and monotonicity in the obstacle gives $P_\gamma(u)\leq P_\gamma(v+a)=P_\gamma(v)+a$. Reverse $u,v$ for the other bound. Maxima, scalar additions, and these suprema preserve $\operatorname{PC}_q$ directly by Jensen; no PA closure assertion is involved.

∎

## Compact chart spaces: unrestricted competitors and a genuine raw endpoint

The globally embedded positive-dimensional finite compact branch is empty. The proof is short: the divergence cancellation (5) applies to a finite balanced complex as well as a fan. If its support were compact, choose $Y(x)=x$ near it with compact support. Each top-cell tangential divergence is $d$, giving

$$
0=d\sum_\sigma w_\sigma a_\sigma\operatorname{vol}_d(\sigma)>0.

$$

This is a contradiction for $d\geq1$. An abstract compact space with local charts is a different category.

**Corollary 11 (Compact locally balanced charts).**

Let $X$ be a compact space with locally embedded rational polyhedral charts, compatible positive balanced weights, and integral-affine lattice-isomorphism transition maps with rational translation. Assume the printed local PCC inequalities define its PC class. Then every continuous PC function is constant on each connected component. For a continuous PC reference $\gamma$ and continuous $u$, the envelope over *all* printed-PC competitors is
$$
\tag{12}
 P_\gamma(u)|_D=\min_{x\in D}(\gamma(x)+u(x))

$$
on each connected component $D$.

If there is a finite bounded rational cell decomposition compatible with these charts and $\gamma,u\in\operatorname{PA}_{\mathbb{Z}}$, the constants in (12) are rational and the endpoint is literal PA and literal regularizable. If $\gamma,u\in\operatorname{PA}_{\mathbb{R}}$, it is real PA and real regularizable. In positive dimension its raw iterated-divisor measure and its contact integral are zero. No measure is assigned here to arbitrary continuous endpoints outside these finite PA assertions.

*Proof.*

The completion proof is local: use a small compact portion of a face in a chart and choose all generator endpoints inside it. Rational-affine chart transitions identify dense rational points on overlaps. The completions agree there and hence, by continuity, throughout the overlap. Thus they give a global continuous completion of every printed-PC competitor; the perspective argument gives all real-endpoint local inequalities.

Here is the maximum principle needed for the continuous completion. If a continuous PC function $F$ has maximum $M$ at $p$, choose a local star at the face containing $p$ and a positive relation as above. For any sufficiently close real $y$ in an incident face write $y-p=\sum_i a_i v_i$, set $t=\max_i a_i/\lambda_i$, and use endpoints $p+\varepsilon v_i$. The same normalized combination as in (7) is a real-endpoint PCC centered at $p$, with strictly positive coefficient at $y$. Every endpoint value is at most $M$, so Jensen forces $F(y)=M$. The maximum set is therefore open as well as closed, and $F$ is constant on the component of $p$. Local polyhedral neighborhoods are locally connected, so components are open; in a compact space each component is compact and there are finitely many components. A maximum on each component proves the first assertion.

A competitor $q$ has continuous completion $F_q$ below the continuous obstacle, by dense rational comparison. On $D$ it is a constant at most the displayed minimum and majorizes $q$. Conversely the componentwise constants in (12) are continuous PC competitors. This proves the exact unrestricted formula without applying a continuous maximum principle to $q$ itself.

On a finite bounded rational carrying decomposition, each affine obstacle attains its minimum on a cell at a vertex. Its vertices are rational and its literal values there are rational; taking finitely many such values proves rationality of the constant. In the real category the constant may be any real number. Both constants are PA in their stated category. A constant sequence, or addition of decreasing positive rational constants, is a valid decreasing uniform regularization.

For this separate chart category use the recursive raw divisor formula in each chart; the lattice and cycle compatibility identifies the primitive normal classes on overlaps. For the measured endpoint all chart coefficients vanish, so they glue to the global zero cycle without any general operator extension. The raw divisor of a constant $k$ against a balanced cycle $c$ is zero from the actual formula
$$
\tag{13}
 (k\cdot c)(\tau)=\sum_{\sigma\succ\tau}c(\sigma)k_\sigma(n_{\sigma/\tau})
 -k_\tau\left(\sum_{\sigma\succ\tau}c(\sigma)n_{\sigma/\tau}\right)=0,

$$
since every linear part is zero. Normals are the saturated primitive inward normals specified above; no additional factorial is inserted into this recursive intersection convention. The first divisor vanishes and so do all further divisors, proving the raw MA and exact contact statements for this finite PA endpoint. This does not extend the operator to general continuous functions.

∎

In dimension zero, the globally embedded finite rational space is a finite set of rational points. Every PCC is confined to a singleton face. Its exact envelope is $\gamma+u$ pointwise, and the genuine zero-fold measure is the given weighted cycle $[X]$. The gap is identically zero. These claims follow directly from the definitions.

## A precise density obstruction in both coefficient categories

**Proposition 12 (Downward irrational modifications have a fixed gap).**

Let $X$ have a positive-dimensional rational cell, and let $\gamma\in\operatorname{PC}_c(X)$. Define

$$
q_\gamma(x)=\begin{cases}\gamma(x),&x\in X_{\mathbb{Q}},\\\gamma(x)-1,&x\notin X_{\mathbb{Q}}.\end{cases}
$$

Then $q_\gamma\in\operatorname{PC}_q(X)$, $q_\gamma-\gamma$ is bounded, and
$$
\tag{14}
 \inf_{f\in C(X)}\|f-q_\gamma\|_\infty=\frac12.

$$
Consequently neither $\operatorname{PAPC}_{\mathbb{Z}}(X,\gamma)$ nor $\operatorname{PAPC}_{\mathbb{R}}(X,\gamma)$ is uniformly dense in the entire printed class $\operatorname{PC}_q(X,\gamma)$, and that class cannot equal either regularizable class. This conclusion concerns unrestricted-PC density; it is not an all-obstacle endpoint nonregularizability theorem.

*Proof.*

For any rational-endpoint PCC, $q_\gamma(x)\leq\gamma(x)\leq\sum_i\alpha_i\gamma(x_i)=\sum_i\alpha_i q_\gamma(x_i)$. Thus $q_\gamma$ is printed PC. Choose an irrational point $p$ in the relative interior of a positive-dimensional rational cell and rational points $r_n\to p$ in that cell. For a continuous $f$ with error at most $\delta$, $f(r_n)\geq\gamma(r_n)-\delta$ gives $f(p)\geq\gamma(p)-\delta$, whereas comparison at $p$ gives $f(p)\leq\gamma(p)-1+\delta$. Hence $\delta\geq1/2$. The continuous function $\gamma-1/2$ realizes error exactly $1/2$. Every PA function and every uniform limit of PA functions is continuous, so the non-density and non-equality conclusions follow in both coefficient categories.

∎

The source's Theorem 6.4 relates an all-PA-obstacle endpoint property to uniform density and equality with the entire PC class. Under the literal rational-endpoint reading, the latter two conditions have the independent obstruction in Proposition 12. We therefore do not import that equivalence or define endpoint regularity by equality with all printed PC functions. For the present target the precise antecedent to be checked is

$$
P_\gamma(u)\in\operatorname{PC}^{\rm reg}_*(X,\gamma)\quad\text{for every admissible }u\in\operatorname{PA}_{*,b},
$$

followed by a genuine operator on those endpoints and the exact contact integral. Theorem 10 does not prove that antecedent. Nor does the discontinuity of $q_\gamma$ imply discontinuity or nonregularizability of an envelope of a continuous obstacle: its completion is just $\gamma$, and the exact envelope is continuous by our theorem.

## What remains for the original classification

The new theorem handles the unrestricted-competitor issue for every finite positive balanced space, in arbitrary dimension and with every bounded continuous obstacle. It includes all admissible PA obstacles in each separately fixed coefficient category. It identifies the upper semicontinuous regularization without redefining the printed endpoint convention. Its positive-spanning criterion depends only on local rational geometry; the actual reference enters the global envelope through a continuous lower competitor and the growth upper bound.

This is a completion criterion, not a contact criterion. On noncompact singular spaces it provides neither uniform global PA approximants with the prescribed reference growth nor a genuine extended MA operator at every envelope. Even a finite PA endpoint with positive raw mass need not have contact merely because the reference grows or the cycle is balanced. The accepted caller manuscript A224 gives such a strict-active-support, positive-growth $U_{3,4}$ example, with a genuine literal PA endpoint; that granted obstruction is retained as context, not claimed as new work or as pair-level real regularity. No unaccepted dossier theorem is an application dependency here.

The missing structural classification still includes the higher-dimensional real coefficient regularization/operator domain, a necessary and sufficient raw local contact condition, and its necessity and sufficiency under global endpoint realization with the actual reference and all obstacles. No theorem in this manuscript solves those requirements, and no raw MA is assigned to the merely continuous envelopes of Theorem 10. The compact-chart conclusion is a separately named category and does not manufacture a compact embedded positive-dimensional cycle. Original P05.2 remains unresolved.

Three failed shortcuts are recorded. First, the original rational-endpoint PC functions cannot be declared continuous; only their dominating completions can. Second, positive spanning at a fan origin is not enough for all stars, as Remark 9 shows. Third, continuity of the exact envelope does not produce real-PA approximants, operator continuity, or contact; applying an operator extension on that premise would omit its domain hypothesis.

## Finite checks, source applications, and reproducibility

The standard-library exact-fraction program `check_star_estimates.py` checks the two barycentric identities, coefficient nonnegativity, face assignments, and Jensen estimates on fixed rational finite lists for a four-ray star, the fine $U_{3,4}$ star, and a translated trivalent star with a bounded-edge truncation. For each cone it enumerates coefficients $0,1/64,\ldots,8/64$ and tests two ambient convex functions, a norm and that norm plus a linear form. All 1,035 barycentric cases and 2,070 convex-function cases passed. The respective star counts were $(36,72)$, $(972,1944)$, and $(27,54)$; maximal sums of the other coefficients in the lower combination were $3/4$, $9/4$, and $1$. These computations exhaust only the specified finite lists; the proofs above establish the continuum statements independently. Inputs, actual output, environment details, structured notes, source responses, and commands are retained in this workspace. Execution success and PDF compilation do not verify mathematical correctness.

The current primary version used for literal definitions is

$$
\text{<https://arxiv.org/pdf/2603.08664v1>}.
$$

Its abstract page currently lists only v1, submitted 9 March 2026; the manuscript date is 10 March 2026. Searches for the title, arXiv identifier, orthogonality, and a sequel found no resolving primary result in the returned results. This is a retrieval observation, not exhaustive bibliographic absence. The version-of-record BBGS article is <https://doi.org/10.1007/s00209-021-02869-6>. We read its endpoint definition, complete Lemma 6.1 and Theorem 6.2 proofs. They use unrestricted real endpoints; the automatic-continuity result is not imported into the printed rational-endpoint class. The geometric positive-spanning result from the accepted B225 grant is independently reconstructed in Lemma 3. The full preserved caller grants and their supplied harmless clarifications are mathematical inputs, not new source retrievals.

The quote-free source ledger specifies literal URLs, versions, units read, actual applications and exclusions. Essential new claims have complete proofs here, rather than borrowed regularization, PA/PC equivalence, or operator-extension theorems. The shell PDF download failed through the existing configured proxy. No network or runtime settings were changed. Saved source artifacts are actual UTF-8 tool-response JSON, not original PDF bytes. Hashes apply only to files actually retained. No installation or resource-heavy local computation was performed; no operator-provided supervised compute facility was exposed. The requested model label was not independently selectable or verified, so no runtime model change is claimed.

Rerun with the existing tools:

“`bash
python check_star_estimates.py
python build_artifacts.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
python record_provenance.py
“`

This manuscript is an unverified draft and candidate status is false.

Primary references: [BMPS v1](https://arxiv.org/pdf/2603.08664v1); [BBGS version of record](https://doi.org/10.1007/s00209-021-02869-6).
