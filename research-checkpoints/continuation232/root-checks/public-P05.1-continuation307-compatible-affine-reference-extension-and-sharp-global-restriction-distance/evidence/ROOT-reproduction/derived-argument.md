# Compatible references and sharp uniform restriction obstruction

Own source-derived proof manuscript. Unreviewed; original P05.1/P05.2 remain OPEN; candidate=false.

Derived from `P05.1-paper.tex`, SHA256 `258fac9a3a5e9eb7e0cb6419653ac8239cdf6fe5d389da08226eef2e5462ed61`, by `python3 make_argument.py`. All theorem/proof prose and mathematical displays in the body are retained. Markdown conversion is presentation, not an independent correctness certificate.

An anisotropic infimal extension of a globally Lipschitz convex function on a rational polyhedron preserves its whole original cell and has an explicitly prescribed trace on the affine hull of a proper face. Such independent extensions can fail polyhedral convexity when glued. We prove a different, compatible extension theorem for actual real affine positive-growth references on finitely many complete rational pages with one common intersection, allowing arbitrary dependence among their quotient directions. Its construction uses finite primal epigraph generators; real heights cause no irrational spatial walls. For a rational piecewise-affine nonlinear target on three proper cells, we then prove that the uniform distance to restrictions of all finite-valued continuous polyhedrally convex functions on the complete book is exactly $(A-1)/2$, attained for every rational $A\geq1$. The lower bound uses legal small rational endpoint combinations and an unbounded integer family, and imposes no PA, reference, or growth condition on its competitors. These results verify the mathematical assertions of working 300–303 in their stated scopes. They do not resolve direct regularization on general original balanced complexes. Original P05.1 and P05.2 remain open; candidate status is false.




## Definitions, hypotheses, and source boundaries

All spaces are finite-dimensional real affine spaces with rational affine coordinates. A rational polyhedron is defined by finitely many rational affine weak inequalities and equations; denominator clearing gives integral equations. A finite rational complex contains the faces of its cells, and two cells intersect in a common face or the empty set. For a lattice $N$, the tangent lattice is the saturated lattice
$$
 N_\sigma=N\cap\operatorname{span}_{\mathbb{R}}(\sigma-\sigma).
$$
An inward facet normal represents the primitive inward class in $N_\sigma/N_\rho$. A positive balanced top weight satisfies that its weighted inward normal sum is tangent to the facet. The literal BMPS weight convention is rational. Whenever positive real weights are used below, we explicitly mean the real linear balancing equations with these same saturated classes; no real-weight MA extension is inferred.

A printed polyhedral convex combination (PCC) consists of rational endpoints $x_j$, real weights $\alpha_j\geq0$ with sum one, and center $x=\sum\alpha_jx_j$. It is legal if there are cells $\sigma_j$ and a face $\rho$ of a rational carrying structure with $x\in\rho$, $x_j\in\sigma_j$, and $\rho\preceq\sigma_j$. A printed $\mathrm{PC}$ function satisfies $f(x)\leq\sum\alpha_j f(x_j)$ for every such test on every permitted structure. Continuity is always an explicit hypothesis when used; the rational-endpoint definition alone does not imply it. Indeed the function zero on rational points and minus one elsewhere on a rational line satisfies every printed test and is discontinuous.

Here $\mathrm{PA}_{\mathbb{R}}$ means continuous real-affine functions on a finite *rational spatial* carrier, or equivalently the finite real scalar extension of literal integral-slope, rational-constant PA functions. This equivalence is proved in Lemma [l:graph](#l:graph). Rational-affine functions can have nonintegral slopes. The term finite-valued means real-valued everywhere, not finite PA. Positive growth of a PA reference means positive slope on every nonzero direction in every cell recession cone. Properness below is proved by a bound $c\|x\|-D$ with $c>0$.

Exactly six whole supplied mathematical grant groups are retained: A224, B225, R230, S262, S272, and S291, including all bound bodies, clarification records, source ledgers, and qualifications. The seven working bodies 296, 297, 299, 300, 301, 302, and 303 are unreviewed data. No inference below uses their labels as premises. In particular the global Lipschitz hypothesis of Section [s:trace](#s:trace) is explicit; working 299 is not invoked to supply it. The central reference and distance theorems use no MA grant or operator. All convex and polyhedral steps used in these theorems are reconstructed here.

The four bound original BMPS/BBGS PDF and text files are the sole primaries. The quote-free source ledger gives complete immediate units and literal-LF locators. BBGS Proposition 3.15 ends at LF670, including its final equality and proof ending. LF locators count splitting on the newline character, not formfeeds. BBGS Remark 5.15, LF1876–1897, leaves general concave versus star-concave PA density open; it supplies no density theorem here. S291 is retained with both correction and reader records, and with native218 original-source/combined FAIL and historical INCONCLUSIVE unchanged. Source identification, read logs, finite checks, and compilation are separate observations, not mathematical acceptance.

The ordinary foundations used are real completeness, finite-dimensional closed bounded compactness, rational Gaussian elimination, elementary norms and convex secants, and nearest-point squared-distance variation. The finite separation and representation arguments needed here are given below. We do not rely on a broad external polyhedral convexity, closure, density, or operator theorem.


## Finite polyhedral tools with real heights


**Lemma: Finite cones, representation, and separation.**  <a id=\"l:cone\"></a>
A finitely generated real cone is closed. Every nonnegative representation can be reduced to an independent subset of its generators. A nonempty polyhedron is $\operatorname{conv} P+\operatorname{cone} R$ for finite point and direction lists; rational inequalities admit rational lists. The points need not be vertices if there is lineality. Conversely every such sum is a closed polyhedron. A point outside a closed convex cone can be strictly separated from it.



**Proof.** 
Suppose $x=\sum a_j u_j$, $a_j\geq0$, with dependent active columns. Choose a nonzero dependence $\sum b_j u_j=0$ on them, changing sign so some $b_j>0$. Replace $a_j$ by $a_j-tb_j$, where $t=\min_{b_j>0}a_j/b_j$. All coefficients stay nonnegative and at least one active coefficient vanishes. Repeat. Each surviving independent subset has a linear inverse on its image, bounding the coefficient sum by $C_I\|x\|$. There are finitely many subsets. A convergent sequence thus has a subsequence with one subset and convergent bounded coefficients. Its limit is in the cone. This proof also handles both signs of a basis representing lineality.

For $C=\{Ax\geq0\}$, its lineality is $\ker A$. Choose a complement, rational if $A$ is rational. On the complement, the sum of the defining nonnegative forms is positive on $C\setminus\{0\}$. Its level-one section is bounded: normalizing an unbounded sequence would produce a unit cone vector where that sum is zero. The section is a compact polytope. At a nonvertex, move in both signs of a nonzero direction annihilating the active equations until an additional independent inequality becomes active. Both endpoints exist by boundedness, and the point is their convex combination. Induction on active rank terminates at vertices. There are finitely many active systems; their full-rank solutions are rational for rational data. This proves finite cone generation, restoring both signs of the lineality basis.

Homogenize $Ax\geq b$ to $Ax\geq tb$, $t\geq0$. Positive-$t$ generators, divided by $t$, give points, and zero-$t$ generators give exactly recession directions. The section $t=1$ is therefore $\operatorname{conv} P+\operatorname{cone} R$. For the converse, introduce nonnegative coefficients with $\sum a_j=1$ and $x=\sum a_jp_j+\sum b_kr_k$. Eliminating one variable pairs every lower bound with every upper bound; a variable with bounds of only one sign imposes no pairing. Repeated finite elimination gives an exact finite system of weak linear inequalities for $x$. It is rational when the lists are rational, and defines a closed polyhedron. Alternatively closedness of the sum follows directly from compactness of $\operatorname{conv} P$ and closedness of the finite cone.

For separation, let $z$ be the nearest point of a closed convex cone $C$ to an outside point $y$. A minimizer exists by restricting to a sufficiently large closed ball. Variation toward $u\in C$ gives $\langle z-y,u-z\rangle\geq0$. Taking $u=0,2z$ yields $\langle z-y,z\rangle=0$. Thus $\langle z-y,u\rangle\geq0$ on $C$ and its value at $y$ is $-\|z-y\|^2<0$.
 ∎



**Lemma: Closure of a finite union hull.**  <a id=\"l:closure\"></a>
For nonempty polyhedra $P_i=\operatorname{conv} A_i+\operatorname{cone} R_i$,
$$
 \overline{\operatorname{conv}\bigl(\bigcup_iP_i\bigr)}
 =\operatorname{conv}\bigl(\bigcup_iA_i\bigr)+\operatorname{cone}\bigl(\bigcup_iR_i\bigr).
$$
No assertion that the unclosed convex hull is already closed is required.



**Proof.** 
The right side is closed by Lemma [l:cone](#l:cone) and contains the union, proving one inclusion. For a source ray $r\in R_i$, anchor $a\in P_i$, and $u$ in the convex hull of the union,
$$
 (1-\delta)u+\delta(a+r/\delta)\longrightarrow u+r
 \quad(\delta\downarrow0).
$$
These are actual convex combinations of source points. Taking limits first in $\delta$ and then in $u$ proves stability of the closed hull under adding $r$, and under every nonnegative multiple. Adding the finitely many ray terms to a point of $\operatorname{conv}\bigcup A_i$ proves the reverse inclusion. This explicitly includes a far-ray, small-mass limit.
 ∎



**Lemma: Full convex supports and recession.**  <a id=\"l:support\"></a>
A finite convex function on a complete real affine space is continuous, locally Lipschitz, and has an affine lower support at each point. A finite full-domain polyhedral epigraph is the epigraph of a maximum of finitely many real affine forms. Its recession function $h$ is the maximum of their linear parts, and its epigraph recession cone is $\operatorname{epi} h$.



**Proof.** 
In coordinates around $x$, bound a convex function above on a cube by the largest of its vertex values, say $B$. Reflection in $x$ bounds it below on a smaller cube by $2f(x)-B$. For two points in a still smaller ball, extend their connecting ray a fixed distance within the bounded region and apply convexity. This bounds their value difference by a fixed multiple of their distance; reversal gives local Lipschitz continuity.

Project $(x,f(x)-\eta)$ onto the closed epigraph. The distance is at most $\eta$. Nearest-point variation gives supporting unit normals. A subsequential limit as $\eta\downarrow0$ supports at $(x,f(x))$ and remains a unit vector. The normal, oriented nonnegatively on the epigraph, has vertical component $b\geq0$. If $b=0$, its nonzero horizontal component would be bounded below on the entire spatial projection, impossible. Hence $b>0$, and division by $b$ gives the asserted affine lower support.

Use the finite inequality description from Lemma [l:cone](#l:cone) for a polyhedral epigraph. Upward stability makes each nontrivial inequality's vertical coefficient nonnegative. A zero vertical coefficient gives no nontrivial spatial inequality because the projection is the full space. Divide the remaining inequalities by their positive vertical coefficients to write $f$ as a finite affine maximum. Replacing their constants by zero gives $h$ and exactly the homogeneous recession inequalities. In particular
$$
 f(x+v)\leq f(x)+h(v),\qquad
 \lim_{T\to\infty}\frac{f(x+Tv)-f(x)}T=h(v).
$$
The limit is independent of $x$.
 ∎



**Lemma: Rational spatial carriers despite real heights.**  <a id=\"l:graph\"></a>
Suppose $E=\operatorname{conv}\{(q_a,c_a)\}+\operatorname{cone}\{(r_b,d_b),(0,1)\}$ is a full-domain epigraph with finite lower fibers, rational spatial $q_a,r_b$, and arbitrary real $c_a,d_b$. Its lower function is genuine $\mathrm{PA}_{\mathbb{R}}$ on a finite rational spatial complex.



**Proof.** 
Closedness follows from compact hull plus finite closed cone. Fibers are closed, nonempty, upward, and bounded below, so their infima are attained. Lemma [l:support](#l:support) gives a finite affine maximum and nonvertical supports everywhere. A face exposed by a lower support is generated by those point generators attaining equality and those ray generators with zero supporting value. This follows by applying the supporting inequality to a nonnegative representation: every positive coefficient must have zero slack. The vertical ray has positive slack and is excluded. Therefore its spatial projection is a rational point hull plus rational cone, hence a rational polyhedron by Lemma [l:cone](#l:cone). Projection is injective on a lower graph face.

All faces of a lower graph face are themselves lower graph faces. Indeed add a sufficiently small multiple of an exposing functional of the subface to the original lower exposing functional; finitely many generator slacks permit the choice, and the vertical coefficient remains positive. There are finitely many faces, since the equality subsets of a finite generator list are finite. If two projected graph faces intersect at $x$, their unique heights both equal the lower function, so their intersection is the projection of their common face. On either affine graph, restrict the other supporting functional. Its equality set exposes precisely that intersection, proving the common-face condition. These rational projections and all their faces cover the whole domain by Lemma [l:support](#l:support). They form the required finite rational complex.

On this complex, affine coefficients that match on shared faces satisfy rational homogeneous linear equations: evaluate at a rational affine basis of each nonempty face. Rational Gaussian elimination supplies a rational basis of the solution space. Multiply each basis function by an integer clearing all denominators of constants and tangent-lattice slopes on the finite cells. Each becomes literal PA. Their real span is exactly the space of matching real coefficients, proving finite real scalar-extension membership. Spatial generating points were not assumed to be vertices, and no arbitrary real-affine maximum wall was declared rational.
 ∎



**Lemma: Affine supports imply printed PC and PA positivity.**  <a id=\"l:pc\"></a>
On a finite embedded complex, a continuous function with an ambient affine local lower support at every point satisfies every legal PCC, even with real endpoints. For a PA function these supports give nonnegative tangent-corrected divisor coefficients against every nonnegative balanced local cycle on a common carrier.



**Proof.** 
On a contained segment subtract the endpoint chord. If the continuous difference has a positive maximum, its maximum set is nonempty, closed, and inside the open segment. At a maximum point, both directions force the local supporting affine slope to be zero. The support then forces the maximum set to be open. Connectedness contradicts the zero endpoint values. Thus the segment restriction is convex. At a PCC center $x$, the segment to endpoint $x_j$ lies in its assigned incident convex cell. Its initial lower support $p$ and convex secants give
$$
 f(x_j)\geq f(x)+p(x_j-x).
$$
Summation cancels the linear terms and proves Jensen.

For the PA assertion, a support at $x\in\operatorname{relint}\rho$ agrees with the affine derivative along $\rho$, by testing both tangent directions. The actual positive-convex divisor coefficient is
$$
 \sum_{\sigma\succ\rho}c_\sigma f_\sigma(n_{\sigma/\rho})
 -f_\rho\left(\sum_{\sigma\succ\rho}c_\sigma n_{\sigma/\rho}\right).
$$
Subtract the ambient support. Balancing cancels its contribution, and every remaining inward derivative is nonnegative. This uses PA on a common carrier, saturated primitive classes, and allows specified nonnegative real weights. There is no MA assertion in this argument.
 ∎



## Exact whole-face traces of Lipschitz extensions
 <a id=\"s:trace\"></a>
Let $\sigma$ be a nonempty rational closed polyhedron, full-dimensional in $V=\operatorname{aff}\sigma$, and let $\tau$ be a nonempty face. Put $H=\operatorname{aff}\tau$. Translate a rational point of $\tau$ to zero and choose a rational splitting $V=W\oplus S$, with $W$ the direction space of $H$. Write $(t,s)$ and use the block $\ell^1$ norm. These are rational coordinate norms, not an irrational orthogonal projection.


**Lemma: Uniform distance to the actual face.**  <a id=\"l:distance\"></a>
One has $\sigma\cap H=\tau$. There is $K<\infty$ such that for every $(t,s)\in\sigma$ some $z\in\tau$ satisfies
$$
 \|t-z\|_1\leq K\|s\|_1.
$$



**Proof.** 
An exposing affine form for $\tau$ is constant on $H$ and takes its minimum on $\sigma$ exactly at $\tau$. This proves the intersection assertion. Write $\sigma=\{A_t t+A_s s\leq b\}$, including equations as pairs of inequalities. Its restricted inequalities $A_t t\leq b$ define $\tau$ on $H$. Feasibility gives restricted violation at most $J\|s\|_1$, where $J$ is the largest absolute coordinate row norm of $A_s$.

Here is the required error bound. For a nonempty full-dimensional relative Euclidean polyhedron $P=\{n_j\cdot x\leq b_j\}$ let $z$ be nearest to $x$ and $w=x-z$. Its active outward normals generate a closed finite cone by Lemma [l:cone](#l:cone). If $w$ were outside, cone separation supplies $v$ with every active $n_j\cdot v\leq0$ and $w\cdot v>0$. Inactive strict slack makes $z+\delta v$ feasible for small $\delta>0$, contradicting nearest-point first variation. Thus $w=\sum\lambda_jn_j$ with nonnegative coefficients on an independent active subset. The finitely many inverse column maps give $\sum\lambda_j\leq C\|w\|$, with one $C$ for all subsets. Therefore, with $\Delta(x)=\max(0,\max_j(n_j\cdot x-b_j))$,
$$
 \|w\|^2=\sum\lambda_j(n_j\cdot x-b_j)
 \leq C\Delta(x)\|w\|.
$$
Cancel when $w\ne0$; the zero case is immediate. Fixed norm equivalence gives the $\ell^1$ version. Apply it to the restricted face system, giving $K=C_1J$. Zero rows can be discarded. If $H$ is a point take $K=0$; if $\tau=H$, take $z=t$ and $K=0$.
 ∎



**Theorem: Exact convex extension and entire affine-face trace.**  <a id=\"t:trace\"></a>
Let $f$ be finite continuous convex and globally $L$-Lipschitz on $\sigma$ in the block norm. Choose rational $M,B>L$ with
$$
 B\geq L(K+1)+MK,
 \qquad N(t,s)=M\|t\|_1+B\|s\|_1.
$$
Then
$$
 F(x)=\inf_{y\in\sigma}\{f(y)+N(x-y)\}
$$
is finite convex and globally Lipschitz on $V$, equals $f$ on the entire $\sigma$, and on the entire $H$ equals
$$
 g_M(h)=\inf_{z\in\tau}\{f_\tau(z)+M\|h-z\|_1\}.
$$
For finitely many cells with the same actual face and trace, use one $M$ and separately sufficiently large $B_i$ to obtain this same whole $H$ trace.



**Proof.** 
Fix $y_0\in\sigma$. The Lipschitz inequality and $N\geq L\|\cdot\|_1$ give
$$
 f(y)+N(x-y)\geq f(y_0)-L\|x-y_0\|_1.
$$
Evaluation at $y_0$ is a finite upper bound. Combining epsilon-minimizers at two points, convexity of $\sigma,f,N$, and letting the error decrease proves convexity. Triangle inequalities give $|F(x)-F(x')|\leq N(x-x')$. If $x\in\sigma$, every candidate is at least $f(x)$ by its Lipschitz bound, and $y=x$ gives equality. These arguments do not need attainment for a general infimum. With the strict displayed $M,B>L$, it also follows from the resulting coercive bound in $y$ that attainment holds.

For $x=(h,0)$ and $y=(t,s)$, choose $z$ by Lemma [l:distance](#l:distance). Then
$$
\begin{aligned}
 f(y)&\geq f_\tau(z)-L(K+1)\|s\|_1,\\
 M\|h-t\|_1&\geq M\|h-z\|_1-MK\|s\|_1.
\end{aligned}
$$
Adding yields a candidate at least $f_\tau(z)+M\|h-z\|_1$, by the bound on $B$. Conversely candidates $(z,0)$ are permitted in $\sigma$. Taking infima proves exact equality on all $H$, including unbounded parts. The same finiteness, convexity, and exactness argument on $\tau$ proves that $g_M$ is finite convex Lipschitz and equals $f_\tau$ on all $\tau$.
 ∎



**Proposition: Preservation of actual-face supports.**  <a id=\"p:preserve\"></a>
Suppose for every $y\in\tau$ one ambient form $p_y$ supports all original $f_i$ on their entire cells, with a uniform finite coordinate bound. Increase $M$ and the $B_i$ to dominate those coordinates and retain the preceding inequalities. The identical $p_y$ supports every $F_i$ on its entire page at every such $y$. This makes no claim at points of $H\setminus\tau$.



**Proof.** 
The choices ensure $p_y(v)\leq N_i(v)$ on $V_i$. For $z\in\sigma_i$,
$$
 f_i(z)+N_i(x-z)\geq f_i(y)+p_y(z-y)+p_y(x-z)
 =f_i(y)+p_y(x-y).
$$
Taking the infimum and using $F_i(y)=f_i(y)$ proves the assertion. Rational splittings can differ by page; their finite coordinate change bounds justify one uniform choice on each finite list.
 ∎



**Proposition: Actual affine auxiliary references.**  <a id=\"p:aux\"></a>
Let $\ell=a+b$ be the actual real affine reference on $\sigma$, with $a(r)>0$ for every nonzero $r\in\operatorname{rec}\sigma$, and $|f-\ell|\leq C$ there. If $G_\ell$ bounds its coordinate slopes, choose $M,B>\max(L,G_\ell)$ and also $B\geq G_\ell(K+1)+MK$. Then
$$
 \Gamma(x)=\inf_{y\in\sigma}\{\ell(y)+N(x-y)\}
$$
is a proper finite convex globally Lipschitz genuine $\mathrm{PA}_\mathbb{R}$ function on rational spatial geometry. It equals the actual $\ell$ on all $\sigma$, has the analogous whole $H$ trace, and $|F-\Gamma|\leq C$ on all $V$. Its original recession slopes are exactly $a$.



**Proof.** 
Theorem [t:trace](#t:trace) applies to $\ell$ with constant $G_\ell$. Two-sided cost comparison passes through infima, proving the relative bound. For coercivity, use the rational decomposition $\sigma=\operatorname{conv}\{q_a\}+\operatorname{cone}\{r_b\}$ from Lemma [l:cone](#l:cone). Positivity excludes nonzero spatial lineality. Choose $c>0$ smaller than all $a(r_b)/\|r_b\|_1$ for nonzero rays, and bound the finitely many point heights below by $c\|q_a\|_1-D$. If there are no rays any $c>0$ permits a sufficiently large $D$. The triangle inequality then gives $\ell(y)\geq c\|y\|_1-D$ on $\sigma$. Hence the infimum is at least $\min(c,M,B)\|x\|_1-D$. This also bounds minimizing points for fixed $x$ and proves attainment by continuity and closedness.

Affinity gives the exact source epigraph
$$
 \operatorname{epi}(\ell+I_\sigma)=\operatorname{conv}\{(q_a,\ell(q_a))\}
 +\operatorname{cone}\{(r_b,a(r_b)),(0,1)\},
$$
where $I_\sigma$ is zero on $\sigma$ and infinity elsewhere. The norm epigraph is generated by $(\pm e_j,N(e_j))$ and $(0,1)$. Adding it to the source epigraph therefore gives the exact $\operatorname{epi}\Gamma$: attainment just proved supplies the reverse inclusion at the lower fiber. Lemma [l:graph](#l:graph) proves its rational carrier and real scalar-extension membership. Equality on the original cell proves its original recession slope, and the coercive bound proves positive recession in every nonzero full-page direction. Agreement of actual affine references on $\tau$ implies agreement on $H$, so common $M$ gives a common entire reference trace too. Separate convexity of these references will not imply PC of their gluing.
 ∎



## The incompatible independent-extension diagnostic
 <a id=\"s:diagnostic\"></a>
In ambient coordinates $(t,a,b)$ put
$$
 e_0=(1,0,0),\quad v_1=(0,1,0),\quad v_2=(0,0,1),\quad
 v_3=(0,-1,-1),\quad \sum_i v_i=0.
$$
Let $V_i=\operatorname{span}(e_0,v_i)$ and $H=\mathbb{R} e_0$. The distinct rational complete pages intersect pairwise exactly in $H$. Page coordinates mean $t e_0+s v_i$. On each choose
$$
 \sigma_i=\{s\geq0,\ 0\leq t+s\leq1\},\quad
 \tau=[0,1]e_0,\quad f_i=\ell_i=s.
$$
The nonzero recession cone consists of positive multiples of $(-1,1)$, on which $\ell_i$ has slope one. The functions are 1-Lipschitz, share zero actual trace, and the common ambient zero form supports them at all $\tau$. Their glued partial-cell function is printed PC: at a $\tau$ center every endpoint value is nonnegative, and elsewhere convexity on its unique page suffices. Lemma [l:pagecells](#l:pagecells) below justifies the unique-page assertion on every carrier. Boundary facets with $t+s=0$ or 1 and $s>0$ have a single incident top cell, so positive balancing fails there. This is not an original balanced counterexample.

Here $K=1$. Choose $M=2$, $B=4$, satisfying $B=L(K+1)+MK$. The independent extensions of both the target and reference are
$$
 F_i(t,s)=\Gamma_i(t,s)
 =\inf_{0\leq u\leq1,\ r\geq0}
 \{r+2|t-u+r|+4|s-r|\}.
$$
Their entire common trace is $2\operatorname{dist}(t,[0,1])$. On $R=\{s\geq0,t+s\leq0\}$ they equal $-2t-s$. To prove this globally on $R$, every candidate satisfies
$$
 r+2|t-u+r|+4|s-r|
 \geq -2t+2u-r+4|s-r|\geq -2t-s.
$$
The last inequality follows separately for $r\leq s$ and $r\geq s$, and equality is achieved at $u=0,r=s$. In fact the displayed affine function is a global support, and equality in its inequalities forces $u=0,r=s\geq0,t+s\leq0$. Thus $R$ is precisely its projected lower face. Its negative $H$ ray is a face of $R$, since $s\geq0$ is active there. Lemma [l:graph](#l:graph) and a rational refinement containing $H$ give genuine page carriers with these incident faces.

At the rational center $x=-e_0$, the rational endpoints $x+v_i/4$ lie in their respective $R$ faces and have mean $x$. This is a legal PCC on the union of the compatible spatial carriers. Its cost is
$$
 \frac13\sum_i F_i(x+v_i/4)-F(x)=\frac74-2=-\frac14.
$$
Consequently equal entire traces and the preserved original-face supports do not make these independent extensions PC on the complete book. At a negative $H$ point a putative common ambient support has tangent coefficient $-2$. Writing $r_i=p(v_i)$, comparison with original $(-r,r)$ gives $r_i\leq-1$, whereas $\sum_i r_i=0$, another contradiction. No measure is assigned to the failed glued reference.


## Compatible extension of actual affine references
 <a id=\"s:reference\"></a>
Assume finitely many distinct complete rational affine $d$-pages $V_i$ have every pairwise intersection exactly one rational affine $H$, with $\dim H<d$. The full-dimensional rational closed cells $\sigma_i\subset V_i$ have the same nonempty actual face $\tau$, with $\operatorname{aff}\tau=H$ and $\sigma_i\cap H=\tau$. Actual real affine references $\ell_i$ agree on $H$ and have strictly positive linear parts on every nonzero original recession direction. Work in their rational affine span $E$ and translate a rational point $y\in\operatorname{relint}\tau$ to zero. The common-form hypothesis is that some ambient $p_0$ supports all these references on the entire original cells at $y$.


**Lemma: Common form from printed affine-star PC.**  <a id=\"l:pzero\"></a>
The common-form hypothesis follows if the original glued affine references satisfy the printed PCC tests. No balancing or independence hypothesis is required.



**Proof.** 
The tangent cone of $\sigma_i$ at $y$ is given by the inequalities active on $\tau$, independent of the choice of $y\in\operatorname{relint}\tau$. Inactive inequalities have strict slack, so small assigned cone directions remain in $\sigma_i$. Choose finite rational generators $w_j$ of these cones, keeping their cell assignments and both signs of a rational $H$ basis. Their actual real costs are $c_j=(\ell_i)_{\rm lin}(w_j)$. For any real $\lambda_j\geq0$ with $\sum\lambda_jw_j=0$, choose a common sufficiently small positive rational $\delta$. The rational endpoints $y+\delta w_j$, weighted by $\lambda_j/\sum\lambda_j$ for a nonzero list, form a legal PCC incident to $\tau$. It gives $\sum\lambda_jc_j\geq0$.

The finite cone generated by $(w_j,c_j)$ and $(0,1)$ therefore excludes $(0,-1)$. It is closed by Lemma [l:cone](#l:cone). Separation gives $q(w)+bt\geq0$ on the cone and strictly negative value at $(0,-1)$. Thus $b>0$, not merely $b\geq0$. Set $p_0=-q/b$. Then $p_0(w_j)\leq c_j$; the opposite $H$ generators force equality with the common trace derivative on $H$. Nonnegative generation extends the inequalities to each whole tangent cone. For $x\in\sigma_i$, $x-y$ is in that cone, so affinity gives the entire-cell support. Its $H$ equality shows it supports at every actual $\tau$ point. Extend the form from the tangent span to $E$ if necessary. An empty nonzero generator list in a zero-dimensional space simply gives the vertical cone and $p_0=0$. Real weights and real costs have never been rounded.
 ∎



**Theorem: Compatible proper affine reference extension.**  <a id=\"t:reference\"></a>
Under these hypotheses and the common-form hypothesis, there are proper finite globally Lipschitz convex functions $\Gamma_i$ on the entire $V_i$, genuine $\mathrm{PA}_\mathbb{R}$ on one common finite rational book carrier, such that
$$
 \Gamma_i=\ell_i\text{ on all }\sigma_i,\qquad
 \Gamma_i|_H=g\text{ on all }H.
$$
At every $h\in H$ one ambient form supports all $\Gamma_i$ on their entire pages. The glued $\Gamma$ is continuous printed PC, positive at infinity. The complete book carries arbitrary specified positive real constant page weights and is balanced with saturated opposite normals. Quotient-normal independence is unnecessary.



**Proof.** 
For each original cell choose exact rational point/recession lists $q_{ia},r_{ib}$ by Lemma [l:cone](#l:cone). Take rational ambient coordinates on $E$ and rational $m>0$ with $m\|v\|_1\geq p_0(v)$ for all $v$. Define
$$
\begin{aligned}
 E_G={}&\operatorname{conv}\{(q_{ia},\ell_i(q_{ia}))\}\\
 &+\operatorname{cone}\{(r_{ib},(\ell_i)_{\rm lin}(r_{ib})),\ (\pm e_j,m),\ (0,1)\}.
\end{aligned}
$$
All indices range over their finite lists. This is exactly the closed source-union hull plus $\operatorname{epi}(m\|\cdot\|_1)$, by Lemma [l:closure](#l:closure). The displayed finite expression is closed and upward; the norm rays give full spatial projection. Every source point, original ray, and norm ray lies above the affine form
$$
 P(x)=\ell_\tau(y)+p_0(x-y).
$$
Consequently all fibers are bounded below by $P$, and evaluating one source point plus norm rays makes them nonempty and finite. They attain their lower endpoint by closedness. Denote that endpoint function by $G$.

For a quantitative proper bound choose $c>0$ below $m$ and all positive ratios $(\ell_i)_{\rm lin}(r_{ib})/\|r_{ib}\|_1$ for nonzero listed rays. The absence of such rays imposes no restriction. Choose $D\geq0$ making all finite point heights at least $c\|q_{ia}\|_1-D$. Every convex point combination and every conic ray combination then has height at least $c$ times the norm of its total spatial coordinate minus $D$, by the triangle inequality. Thus
$$
 G(x)\geq c\|x\|_1-D.
$$
The norm cone is a recession cone of $E_G$, so $G(x+v)\leq G(x)+m\|v\|_1$; reversal proves global Lipschitz continuity. Lemma [l:graph](#l:graph) proves the genuine rational spatial PA carrier. Original epigraph inclusion gives $G\leq\ell_i$ on all $\sigma_i$. On $\tau$ it combines with $G\geq P$ to give $G=\ell_\tau$ and the same $p_0$ support at every actual $\tau$ point.

Set $g=G|_H$. It is proper finite convex Lipschitz, equals $\ell_\tau$ on all actual $\tau$, and satisfies $g\geq\ell_\tau$ on all $H$, since $p_0|_H$ is its affine derivative. Intersect the rational lower-face carrier of $G$ with rational $H$. These are rational polyhedra with common-face intersections and cover $H$; the real affine graph heights restrict. Generate every nonempty trace cell by rational points $h_a$ and recession directions $w_b$. Lift them with their actual $g$ values and slopes. By Lemma [l:support](#l:support), the latter slopes are $h_G(w_b)$, where $h_G$ is the ambient recession function. Hence, including all unbounded trace cells,
$$
 \operatorname{epi} g=\operatorname{conv}\{(h_a,g(h_a))\}
 +\operatorname{cone}\{(w_b,h_G(w_b)),(0,1)\}.
$$
Each generator and its forward ray is in $\operatorname{epi} g$, proving one inclusion by convexity and recession stability. The point/ray representation of the cell containing any given trace point, and its affine graph height, proves the other. If $H$ is a point this is just one graph point and the vertical ray. This also proves the rational real PA trace assertion without ignoring recession.

Choose rational page coordinates and a rational polyhedral norm $N_i$ large enough that
$$
 N_i(v)\geq (\ell_i)_{\rm lin}(v),\qquad N_i(v)\geq h_G(v)
 \quad(v\in V_i).
$$
Such a rational multiple of the page coordinate $\ell^1$ norm exists: bound the finitely many actual affine coordinate slopes and the ambient Lipschitz bound composed with the rational page inclusion. Now define, by exact finite primal generators,
$$
 E_i=\overline{\operatorname{conv}\bigl(\operatorname{epi}(\ell_i+I_{\sigma_i})\cup\operatorname{epi} g\bigr)}+\operatorname{epi} N_i.
$$
Equivalently it is the hull of all original and trace lifted generating points plus the cone of all their exact recession rays, the norm basis rays, and the vertical ray. Lemmas [l:closure](#l:closure) and [l:cone](#l:cone) make this equality and its closedness precise.

All sources and rays lie above *both* $G|_{V_i}$ and $\ell_i$. For $G$, the original points satisfy $G\leq\ell_i$, trace points have equality, original recession rays belong to $\operatorname{rec} E_G$, and trace rays have height $h_G(w_b)$. Norm rays have height at least $h_G$. The epigraph of $G$ is stable under these cones. For $\ell_i$, original points/rays have equality, and trace points lie above it because $g\geq\ell_\tau$. Dividing this last inequality along an unbounded trace ray gives $h_G(w_b)\geq(\ell_i)_{\rm lin}(w_b)$. Norm rays dominate that derivative as well. Closed convexity therefore gives
$$
 E_i\subseteq\operatorname{epi}(G|_{V_i})\cap\operatorname{epi}\ell_i.
$$
Its full-domain attained lower function $\Gamma_i$ consequently satisfies $\Gamma_i\geq G|_{V_i}$ and $\Gamma_i\geq\ell_i$. Original epigraph inclusion gives $\Gamma_i\leq\ell_i$ on all $\sigma_i$, proving exact original equality. Trace epigraph inclusion gives $\Gamma_i|_H\leq g$, and $\Gamma_i\geq G$ gives equality on the entire $H$. Finiteness comes from one source point plus $\operatorname{epi} N_i$; properness comes from $\Gamma_i\geq G$; norm recession gives global Lipschitz continuity. Lemma [l:graph](#l:graph) supplies rational spatial carriers and real scalar-extension membership. In particular this is a primal construction, not an unjustified substitution of $\max(G,\ell_i)$.

At every $h\in H$, let $p_h$ be an ambient lower support of the full-domain $G$ supplied by Lemma [l:support](#l:support). Since every $\Gamma_i\geq G$ and $\Gamma_i(h)=G(h)$, this same $p_h$ supports every $\Gamma_i$ on its whole page. Off $H$ a neighborhood meets just one page, with ordinary convex supports extendable ambiently. Thus Lemma [l:pc](#l:pc) proves all real-endpoint and printed PCCs. Alternatively, at a center in $H$ sum these global supports; off $H$ use whole-page convexity and Lemma [l:pagecells](#l:pagecells).

To obtain one rational carrier, extend every rational page-wall covector and trace-wall equation to $E$ by rational linear algebra. Include equations for all pages and $H$. Restrict the resulting finite ambient hyperplane arrangement to the book, taking its induced subdivisions and faces. It refines all spatial carriers and their subdivisions agree on $H$. Matching real affine data satisfy one rational coefficient system as in Lemma [l:graph](#l:graph). There are no walls newly defined by comparing unrelated real coefficients. The uniform lower bound for $G$ implies strictly positive recession slope on every nonzero ray of every $\Gamma$ cell, by evaluating its affine values along that ray and dividing by its length parameter.

Finally assign each page a specified positive real constant $c_i$. At every facet in its complete-page subdivision, the two saturated primitive inward quotient classes are opposite and their page weights agree. Contributions cancel separately within each page, including facets in $H$ when its codimension is one. Summing pages proves balancing for $\sum_i c_i[V_i]$, regardless of directional dependence. Rational $c_i$ give the literal BMPS cycle convention; real $c_i$ give the expressly stated real balancing convention. The construction is an admitted proper full-book affine-reference extension and asserts nothing about an MA operator.
 ∎


For Section [s:diagnostic](#s:diagnostic), $p_0=0$ and $\ell_i=s$ meet every hypothesis. An additional explicit compatible reference in this example is the restriction of
$$
 R(t,a,b)=\max\{|a|,|b|,-t,t-1\}.
$$
On every original page cell $|a|$ and $|b|$ have maximum $s$, while $-t=s-u\leq s$ and $t-1=u-s-1\leq s$; hence $R=s$. Its whole common trace is $\operatorname{dist}(t,[0,1])$. It is ambient convex rational PA with rational comparison walls, and $R\geq (|t|+|a|+|b|)/3-1$. It is therefore proper and printed PC, with ambient supports at every trace point. This explicit choice and Theorem [t:reference](#t:reference) repair that particular incompatible extension without invalidating its $-1/4$ diagnostic. Affinity is essential in the lower bound by $\ell_i$ throughout the general construction. Substituting a nonlinear target for it would require the common trace to dominate every extrapolated interior support, an additional condition that the next sections refute in general.


## Whole-page convexity without illegal coarsening
 <a id=\"s:page\"></a>
The competitor below is finite-valued; it need not be PA or have finitely many affine pieces. The proofs apply on a finite rational carrier, and also on a locally finite rational carrier by restricting each ray neighborhood or compact segment to its finitely many incident cells.

**Lemma: Cells and local rational ray endpoints.**  <a id=\"l:pagecells\"></a>
A convex polyhedron contained in a finite union of affine pages lies in one page. At a rational point $y$ of a finite book carrier preserving $H$, every rational page direction has sufficiently short rational endpoints in a cell incident to the minimal face containing $y$.



**Proof.** 
If the affine hull of the polyhedron were contained in none of the finitely many pages, its relative interior would be covered by finitely many proper affine subspaces. Such a covering is impossible: choose a nonzero affine equation vanishing on each proper subspace; their product is a nonzero polynomial, which cannot vanish on an open set (successively restrict to lines in each coordinate). Thus one page contains the affine hull. For the second assertion intersect the rational ray from $y$ with the finite carrier. Its intervals have finitely many break parameters. A sufficiently short positive interval lies in one cell; its closedness includes $y$. The minimal face at $y$ is a face of every cell containing $y$, by the complex intersection axiom. A positive rational parameter inside that interval provides the endpoint. Use the minimum of the finitely many choices for a finite direction list.
 ∎



**Lemma: Whole-page convexity.**  <a id=\"l:wholepage\"></a>
Every finite-valued continuous printed PC function on a complete finite rational page book, on a finite or locally finite rational carrier, is ordinarily convex on each entire page. No PA, growth, or reference hypothesis is needed.



**Proof.** 
Within an inherited convex cell, rational endpoint convex inequalities are legal: the center lies in its minimal face, itself a face of that cell. Density of rational points and continuity extend them to arbitrary endpoints and coefficients, giving ordinary convexity there. Density follows by solving the rational equalities of a minimal face and approximating in its rational kernel basis, retaining the inactive strict inequalities.

Consider a segment between rational page endpoints. Rational inequalities cut it into finitely many intervals with rational breakpoints; cells with segments in lower-dimensional faces are included, so degeneracies are harmless. At a breakpoint $q$, take rational nearby endpoints $a,b$ on the left and right intervals. Their assigned closed cells contain $q$ and its minimal face, so the PCC with center $q$ is legal. It gives
$$
 \frac{F(q)-F(a)}{q-a}\leq\frac{F(b)-F(q)}{b-q},
$$
where coordinates along the segment are used. This holds for all sufficiently near rational $a,b$; continuity extends it to real ones. Convexity on the adjacent intervals makes these secants monotone. The left limiting derivative is bounded above by any fixed right secant and below by an interior left secant; the right limiting derivative is bounded below by any fixed left secant and above by an interior right secant. Hence both are finite and the left derivative is at most the right derivative. All earlier left secants are at most all later right secants. A secant crossing the breakpoint is the length-weighted average of these two secants; this proves the ordered-secant criterion across the breakpoint. Concatenating the finitely many intervals proves convexity along the full rational segment. This proof uses actual local breakpoint PCCs, without coarsening the carrier or using distant nonincident cells. Approximate arbitrary real page endpoints by rational ones and use continuity to obtain whole-page convexity.
 ∎



**Lemma: Dependent distant-endpoint inequality.**  <a id=\"l:far\"></a>
In the three-page model of Section [s:diagnostic](#s:diagnostic), for rational $T>0$ put
$$
 y_T=-T e_0,\qquad z_i(T)=y_T+T v_i.
$$
Every finite-valued continuous printed PC $F$ on the complete book satisfies
$$
 F(y_T)\leq\tfrac13\sum_i F(z_i(T)).
$$



**Proof.** 
By Lemma [l:pagecells](#l:pagecells) choose one sufficiently small rational $0<\delta<1$ so $y_T+\delta T v_i$ lies in an actual cell incident to the minimal $H$ face at $y_T$. Their mean is $y_T$ because $\sum v_i=0$. This small rational-endpoint PCC is legal, with weights $1/3$. Whole-page convexity gives
$$
 F(y_T+\delta T v_i)\leq(1-\delta)F(y_T)+\delta F(z_i(T)).
$$
Sum, apply the small PCC, and cancel the $(1-\delta)$ term. The far endpoints may be nonincident. Their inequality was derived rather than assumed to be a direct far PCC.
 ∎



## Exact nonlinear extension obstruction
 <a id=\"s:exact\"></a>
For rational $A\geq1$ on the original cells set
$$
 u=t+s\in[0,1],\qquad \gamma_i=s,\qquad
 f_{A,i}(t,s)=\max(0,-At+(1-A)s)=\max(0,s-Au).
$$
This target is finite continuous rational PA on genuine rational carriers with wall $-At+(1-A)s=0$. It is convex and globally $A$-Lipschitz in the page block $\ell^1$ norm, since its two gradients are zero and $(-A,1-A)$. Its entire actual $\tau$ trace is zero; all target values are nonnegative, so the zero ambient form supports all cells at every $\tau$ point. At a legal center off $\tau$ all assigned cells are on its unique page, where convexity proves Jensen. At a center on $\tau$, zero is at most every endpoint average. Thus it is already printed PC on the partial union, on every rational refinement. Moreover
$$
 f_A-\gamma=\max(-s,-Au)\in[-A,0],
$$
so the global relative bound is $A$. On the only nonzero recession directions, positive multiples of $(-1,1)$, both the actual reference and target have slope one. This target has no regularization failure on its own partial support: its constant PA sequence already works. Its outer facets fail original balancing as described above.


**Theorem: No exact continuous PC extension.**  <a id=\"t:exact\"></a>
For every rational $A>1$, no finite-valued continuous printed PC function on the complete three-page book equals $f_A$ on the entire original partial union. In particular for $A=2$ exact extension would imply $2\leq F(-e_0)\leq1$.



**Proof.** 
Set $T=1$. Each original $z_i=(-1,1)$ has $u=0$ and target value one. Lemma [l:far](#l:far) gives $F(-e_0)\leq1$. In page one take a rational $0<u_*<\min(1,1/(A-1))$ and the interior point $q=(-1,1+u_*)$. The affine expression $L(t,s)=-At+(1-A)s$ has value $1-(A-1)u_*>0$ there, so $f_A=L$ on an open neighborhood within the original cell. Exact agreement makes $F_1=L$ there. A finite convex whole-page function agreeing with an affine function near an interior point has that function as a global support: along the segment from that point to any other point, the initial affine slope is at most every later convex secant. Therefore $F(-e_0)\geq L(-1,0)=A>1$, a contradiction. For $A=2$, $q=(-1,3/2)$ gives the displayed $2\leq F(-e_0)\leq1$.
 ∎



## Sharp global restriction distance with attainment
 <a id=\"s:sharp\"></a>
Let $X_0=\bigcup_i\sigma_i$ and $B=\bigcup_i V_i$ in this fixed model. Take the infimum over *all* finite-valued continuous printed PC functions on $B$, including non-PA functions and without a reference or growth condition:
$$
 D_A=\inf_F\sup_{x\in X_0}|F(x)-f_A(x)|.
$$
An infinite error is permitted and contributes no lower-bound difficulty.


**Theorem: Exact distance.**  <a id=\"t:sharp\"></a>
For every rational $A\geq1$,
$$
 \boxed{D_A=(A-1)/2.}
$$
The infimum is attained by the restriction to $B$ of the ambient convex rational PA function
$$
 F_A(t,a,b)=\max(0,-t)-(A-1)/2.
$$
The lower bound applies to every competitor in the stated continuous PC class.



**Proof.** 
Let $\epsilon=\sup_{X_0}|F-f_A|<\infty$. For every integer $T\geq\max(1,A-1)$, the original $z_i(T)=(-T,T)$ have $u=0$ and $f_A=T$. Lemma [l:far](#l:far) gives
$$
 F(y_T)\leq T+\epsilon.
$$
In page one take $r_1(T)=(-T,T+1)$, with $u=1$ and target value $T+1-A\geq0$. Both $z_1(T)$ and $r_1(T)$ are original points, and
$$
 z_1(T)=\frac1{T+1}y_T+\frac T{T+1}r_1(T).
$$
Whole-page convexity, which is an ordinary secant inequality and need not be a far legal PCC, gives
$$
\begin{aligned}
 F(y_T)&\geq(T+1)F(z_1(T))-T F(r_1(T))\\
 &\geq(T+1)(T-\epsilon)-T(T+1-A+\epsilon)\\
 &=AT-(2T+1)\epsilon.
\end{aligned}
$$
Combine the bounds to get
$$
 \epsilon\geq\frac{(A-1)T}{2(T+1)}.
$$
The integer family is unbounded; since $T/(T+1)=1-1/(T+1)$ tends to one, this proves $\epsilon\geq(A-1)/2$. Explicitly any strictly smaller error is contradicted by an integer whose reciprocal $1/(T+1)$ is below the positive remaining fraction. This is a continuum proof using arbitrarily large integers, not a finite-grid extrapolation. For $A=2$, $T=1$ yields only $1/4$; the unbounded family yields the sharp $1/2$. Infinite errors satisfy the conclusion trivially, and $A=1$ has the trivial zero lower bound.

For attainment, $F_A$ is ambient convex, continuous, and rational PA with the single rational wall $t=0$, integral slopes, and rational constant. It therefore satisfies every ambient Jensen inequality and every printed PCC on the complete book. On an original cell let $G_0=\max(0,s-u)=\max(0,-t)$. The positive-part map is increasing and 1-Lipschitz, so
$$
 0\leq G_0-\max(0,s-Au)\leq(A-1)u\leq A-1.
$$
Subtracting $(A-1)/2$ gives the required global error at most that number on all three unbounded cells. The endpoints of the error interval are attained: at $u=0$ the difference is zero, and at $u=1,s\geq A$ it is $A-1$. Thus the error is exactly $(A-1)/2$, including zero when $A=1$. Lower bound and witness prove both the infimum and its attainment.
 ∎


This theorem strengthens the exact obstruction: arbitrarily accurate extension followed by restriction is also impossible when $A>1$. It is consistent with the affine reference extension of Theorem [t:reference](#t:reference). Its witness has no asserted bounded difference from an arbitrary proper full-book reference; it is constant in the transverse variables for fixed $t$, so in particular it need not belong to such a class. Any further restriction of the competitor class retains the lower bound but need not retain this attaining witness.


## Separate affine approximation and the precise remaining gap
 <a id=\"s:gaps\"></a>
For completeness we reconstruct the full-affine approximation consequence that can legitimately be applied separately after Section [s:trace](#s:trace). It supplies no compatible book extension for a nonlinear target.


**Lemma: Whole-affine rational majorants.**  <a id=\"l:majorant\"></a>
Let $\Gamma$ be finite convex rational-spatial real PA on a complete rational affine $V$, positive in every nonzero recession direction. If $f$ is continuous convex and boundedly relative to $\Gamma$, then for every $\eta>0$ and finite rational $S\subset V$ there is a finite convex rational-spatial real PA $P$ with $f\leq P\leq f+\eta$ everywhere, $P|_S=f|_S$, and exact recession $\Gamma^\infty$. Decreasing uniform approximation follows by rational constant shifts; these shifted functions need not interpolate $S$.



**Proof.** 
By Lemma [l:support](#l:support), $\Gamma=\max_j(a_j\cdot x+b_j)$. Put $h=\max_j a_j\cdot x$ and $\Delta=\operatorname{conv}\{a_j\}$. Then $\Gamma-h$ is bounded. The Legendre transform $f^*(p)=\sup_x(p\cdot x-f(x))$ is finite bounded exactly on $\Delta$, since $f-h$ is bounded. Outside $\Delta$ separation gives a direction with $p\cdot v>h(v)$ and infinite transform; inside, $p\cdot x\leq h(x)$ gives a uniform upper bound, and one fixed $x$ gives a lower bound.

The transform is convex lower semicontinuous and continuous on the entire compact polytope $\Delta$. To check boundary continuity, let $B$ be the maximum of its values at the finite vertices. At $p\in\Delta$, inactive inequality slacks supply a fixed positive ray radius $r$: for nearby $q\in\Delta$, $p+r(q-p)/\|q-p\|\in\Delta$. Active inequalities are preserved along that feasible direction. Convexity bounds
$$
 f^*(q)\leq f^*(p)+(\|q-p\|/r)(B-f^*(p));
$$
lower semicontinuity gives the opposite limiting inequality. A singleton polytope is immediate.

Continuity of $f$ permits rational $x$ in its transform supremum. For each $p\in\Delta$ choose one rational sample approximating the supremum within $\eta/2$. Continuity of the transform and of this sample's affine expression gives a neighborhood with error less than $\eta$. A finite subcover and inclusion of $S$ yield finite rational $A$ with
$$
 f^*(p)-\eta\leq\max_{x\in A}(p\cdot x-f(x))\leq f^*(p)
 \quad(p\in\Delta).
$$
The actual $\operatorname{epi} h$ has finite rational spatial ray generators with real heights. Indeed every direction belongs to the recession cone of some cell of the rational carrier of $\Gamma$: along its ray some finite cell contains an unbounded sequence, and its inequalities force the direction into that recession cone. On each cone $h$ is that cell's linear slope. Generate these rational cones and add their exact lifted heights and the vertical ray; they generate $\operatorname{epi} h$.

Define $E=\operatorname{conv}\{(x,f(x)):x\in A\}+\operatorname{epi} h$. Affine supports show $f(x+v)\leq f(x)+h(v)$: every support slope lies in $\Delta$, as otherwise its linear excess over $h$ along a ray would contradict bounded difference. Thus $E\subseteq\operatorname{epi} f$. The closed full-domain lower fibers give a finite convex $P$, and Lemma [l:graph](#l:graph) proves its rational spatial carrier. Direct maximization over the generators gives $P^*\!=\max_{x\in A}(p\cdot x-f(x))$ on $\Delta$ and infinity elsewhere. The affine supports of Lemma [l:support](#l:support) prove double conjugation for a finite convex full-space function: each support at $x$ attains its value in the double transform, and the defining inequality gives the reverse bound. The transform comparison therefore gives $f\leq P\leq f+\eta$ globally. Its lifted sample points imply equality on $S$. Compact hull plus recession cone has exactly that cone as its recession: divide a forward sequence by its ray parameter, use compactness of the hull and cone closedness. Hence $P^\infty=h$.

Choose errors $\eta_n=2^{-n}$ and unshifted majorants $P_n$. Set $Q_n=P_n+4\eta_n$. Then $4\eta_n\leq Q_n-f\leq5\eta_n$ while $Q_{n+1}-f\leq(5/2)\eta_n$, so $Q_n$ decreases uniformly to $f$. These shifts preserve rational carriers and actual recession. Exact sample interpolation is a property of $P_n$, not of $Q_n$.
 ∎


Apply this lemma separately to $(V_i,\Gamma_i,F_i)$ of Proposition [p:aux](#p:aux): its hypotheses are proved there. Restriction gives single-cell majorants with the actual original recession and prescribed finite rational contacts. It does not give equality of the approximated entire face traces or common ambient supports at every changed trace point. Section [s:diagnostic](#s:diagnostic) shows that the independent pre-approximation extensions can already be non-PC outside $\tau$. Theorem [t:sharp](#t:sharp) further excludes arbitrary accurate complete-page extension/restriction for nonlinear targets in this model. Enlarging a norm or changing an admitted reference cannot remove that lower bound.

What remains open is a *direct original-complex* approximation lemma: for each actual continuous PC target or actual admissible envelope boundedly relative to the given real PA positive-growth reference on a finite positive balanced rational complex, construct genuine finite rational-carrier PC approximants, uniformly on the whole support, satisfying every face test and the same actual growth class. No exact or approximate full-page target extension is assumed in that statement; the sharp theorem refutes that intermediate assumption on the present partial model. We have neither proved nor refuted this direct lemma in general. Its target $f_A$ is already PA PC on the partial support, and that support omits boundary balancing; hence it proves no original balanced regularization failure.

Different overlap subspaces, extra nonincident pages, simultaneous anisotropic norms for several distinct faces, general non-PA contact sufficiency, literal coefficient classifications, and broader compact or abstract chart classifications are excluded. The six grants retain their original qualified scopes: R230 identifies actual envelopes under its positive-spanning/continuous-obstacle hypotheses without PA regularization; S262/S272 attach raw measures only to proved uniform PA completion domains, retain signed/zero finite conventions, and retain weak/BL uniformity only on each fixed relative-bound family. No such operator is assigned here to an intermediate or forbidden extension. Their global vague uniformity is not upgraded to global weak uniformity. Nothing closes original P05.1 or P05.2.


## Reproducibility, checks, and complete coverage

The zero-dimensional complete-page case is a single point, with constant exact extension and vacuous recession and balancing requirements. The proper-face construction includes $\dim H=0$ through its single trace point and vertical ray. If there is just one positive-dimensional page and $\tau=\sigma$, Proposition [p:aux](#p:aux) supplies its proper extension with $\Gamma\geq\ell$ globally; no inter-page condition is needed. Distinct pages with a common nonempty pairwise intersection of their full dimension cannot occur. These degenerate cases introduce no independence assumption.
The source and application ledger maps all seven units E0–E6 of working300, all six G0–G5 of working301, all four N0–N3 of working302, and all four D0–D3 of working303 to the proofs above. The supplied 296/297/299 bodies were read whole as context. The explicit global cell Lipschitz and actual-face support hypotheses remain hypotheses here; 299 was not promoted to a grant. The unbalanced orthant diagnostic from 297 remains an excluded-domain observation, not an original counterexample.

The fresh standard-library program `exact_checks.py` uses rational arithmetic and bounded finite lists. It enumerates active systems for the independent-extension LP, checks the rational $-1/4$ cost and barycenters, original target bounds, recession algebra, the sharp secant identity at listed integer values, and the attaining witness's listed values. An explicit finite-generator reference example is also checked. Its results exhaust those finite lists only. The general separation, exact trace, compatible reference, whole-page convexity, unbounded-family limit, and all-competitor bound are the proofs above, independent of these checks.

Programs, input, actual output, commands, read-span metadata, Python/TeX versions, first display truncation records and repairs, no-shell-escape build logs, build reports, and artifact bindings are retained in this fresh directory. Long primary extracts remain under `LOCALONLY/` and are not republished in notes. Original PDFs were identified by bytes and hashes, not claimed independently visually read in their entirety. No supplied emitter, audit, builder, binder, or orchestrator was executed. No network, nested provider, agent, or heavy compute was used. No supervised compute facility was exposed, and none was required by the bounded checks. Provider/model/single-call certification remains external; this paper claims no runtime change or independent certification of it. Compilation success is not mathematical correctness. The deliverable is an ordinary unreviewed paper with \textbf{candidate=false}.
