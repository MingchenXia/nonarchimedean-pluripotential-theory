# Target, conventions, and logical inputs

The target is P05.1 only. Regularity here concerns the actual unrestricted envelope for each bounded admissible obstacle, and its global uniform (equivalently, after an elementary extraction, decreasing uniform) approximation by functions in the fixed coefficient category and the same reference growth class. We do not substitute a density assertion for a geometric classification. Our positive theorems also allow every bounded continuous obstacle, which includes the prescribed bounded piecewise-affine obstacles.

A finite rational carrier has rational affine cells and saturated tangent lattices. In the literal category $\mathrm{PA}_\mathbb Z$, affine slopes are integral on these lattices and constants are rational. The real category $\mathrm{PA}_\mathbb R$ is its finite real linear extension, retaining rational spatial geometry. Real heights do not permit irrational walls. A regularity claim for a coefficient-category pair retains its admitted reference category; a larger bounded-growth approximation statement does not recategorize the reference. For example, on $\mathbb R$ the maximum of $|x|$ and $|x-1|+\sqrt2-1$ has its intervening wall at $\sqrt2/2$; this maximum is not automatically primitive rational-carrier $\mathrm{PA}_\mathbb R$.

For a continuous reference $\gamma$ and $u\in C_b(X)$ put $$P_\gamma(u)(x)=\sup\{q(x):q\text{ is finite-valued printed PC},\ q-\gamma\in C_b^{\rm set}(X),\ q\leq\gamma+u\}.$$ Here $C_b^{\rm set}$ means bounded difference, without adding continuity to the competitor. Printed PC uses the rational-endpoint polyhedral convex-combination inequalities: endpoints lie in cells incident to one common face, their weighted average lies in that face, and the value there is at most the weighted average of endpoint values. We abbreviate these combinations by PCC. We allow real nonnegative coefficients. All statements about continuous PC below refer to its real-endpoint completion, proved where needed. The envelope is always between $\gamma-\|u\|_\infty$ and $\gamma+u$.

This distinction matters. A function equal to zero at rational points and to $-1$ at irrational points of a complete affine line satisfies the printed rational-endpoint inequalities; it is discontinuous. We therefore do not use the printed all-PC density equivalence in BMPS Theorem 6.4 without a continuity repair. Our conclusions assert endpoint regularity directly.

Exactly the five supplied whole mathematical grants A224, B225, R230, S262 and S272, with every supplied clarification, are retained as premises, with no added authority from report labels. A224 concerns the strict-growth obstruction and its coefficient restrictions; B225 concerns balanced support and the continuous maximum principle; R230 constructs the continuous completion and unrestricted continuous envelopes, not regularization; S262 includes all-continuous graph regularization and its corrected fixed-bound weak uniformities; S272 completes mixed raw measures in the genuine actual-real-reference regularizable domain, not in all continuous PC. We freshly prove the geometric regularization results used here. The relevant 282/283/284 and older independent-branch papers are data whose arguments motivated checks; they are not grants. No active audit output was accessed.

<div id="lem:rational" class="lemma">

**Lemma 1** (Rational linear algebra and PA categories). *A nonempty rational polyhedron has rational points dense in each of its faces. A continuous function affine on a finite rational carrier, with arbitrary real coefficients, belongs to the finite real linear extension of the literal category. For continuous PA functions on rational geometry, divisor positivity on all nonnegative local cycles is equivalent to the PCC inequalities; testing local one-cycles suffices. A function with an ambient affine lower support at every point, equal to it at that point, satisfies this positivity condition.*

</div>

<div class="proof">

*Proof.* At a point of a rational polyhedron, impose the equalities of its minimal face. Row reduction over $\mathbb Q$ gives a rational particular solution and rational kernel basis. Approximate the remaining coordinates by rationals, keeping the finitely many strict inactive inequalities. This proves density. The coefficients of affine functions on all cells that agree on common faces form a finite-dimensional vector space defined by rational linear equations. It has a rational basis. Each basis function becomes literal after multiplication by a common positive integer clearing all slope and constant denominators. This proves the scalar-extension assertion.

Here is the continuity repair of the PA convexity test. Two opposite rational rays through a rational point inside a cell are a local positive one-cycle. Positivity of its divisor gives nonnegative bends, and hence ordinary convexity along segments in that cell. At a rational center $x$ of a rational-endpoint PCC write $x_i-x=t_i v_i$, with $v_i$ primitive rational lattice directions and $t_i>0$ rational. The outgoing rays with real weights $\alpha_i t_i$ balance since $\sum\alpha_i(x_i-x)=0$. Divisor positivity at $x$ gives $\sum\alpha_i D_{x_i-x}f(x)\geq0$. Cellwise convexity gives $D_{x_i-x}f(x)\leq f(x_i)-f(x)$, proving Jensen. Repeated collinear rays can first be combined.

To pass to real centers and endpoints, use perspective variables $s_i=\alpha_i x_i$. The constraints $\sum\alpha_i=1$, $\sum s_i\in\tau$, and $A_i s_i\geq\alpha_i b_i$ for the incident rational cells are rational linear constraints. Delete zero coefficients. Rational feasible points in the minimal face approximate the given tuple, with all remaining $\alpha_i>0$. The endpoints $s_i/\alpha_i$ and center are rational. Continuity proves the full real PCC test.

Conversely, for any nonnegative local $k$-cycle, at a generic rational point of a divisor face $\tau$ of dimension $k-1$ subtract an ambient affine extension of the tangential affine part. Its weights $w_\sigma$ satisfy $b=\sum w_\sigma n_{\sigma\tau}\in T\tau$. For rational weights choose $\sigma_0$ with $w_{\sigma_0}>0$, leave all other representatives unchanged and replace $n_{\sigma_0\tau}$ by $n_{\sigma_0\tau}-b/w_{\sigma_0}$. Their weighted sum is zero; a common small rational length keeps their endpoints in the incident cells. For rational weights Jensen gives the nonnegative weighted normal derivative. The cone of balanced weights is defined by rational linear equations, so rational weights are dense in every face of that cone, by the first paragraph. Passage to real weights gives every divisor coefficient. This is precisely the tangent-corrected divisor test. Finally, if an affine lower support is available, all corrected outgoing derivatives are nonnegative separately, and the same formula gives positivity immediately. ◻

</div>

Ordinary foundations used without a fresh set-theoretic reconstruction are completeness of $\mathbb R$, compactness of bounded closed subsets of finite-dimensional Euclidean space, elementary integration and the divergence theorem on polytopes, elementary calculus, and Gaussian elimination. Finite-dimensional convex duality and the polyhedral representation facts needed below are proved explicitly; no unavailable convex-analysis textbook is an essential source theorem.

# Compact balanced local charts

<div id="def:chart" class="definition">

**Definition 2** (The precise compact category). A balanced rational chart space in this section is a Hausdorff, locally polyhedral space with an atlas of homeomorphisms onto relatively open subsets of finite rational polyhedral supports. Every chart support is pure of a fixed dimension and carries strictly positive top weights satisfying balancing at all faces; there is no boundary face with an omitted balancing equation. Coordinate transitions are rational integral-affine lattice isomorphisms on compatible refinements, preserving the PCC and weight data. Locally defined rational PA functions glue as functions. Compactness is of the underlying space. We do not require a single global embedding or a single global bounded-cell decomposition. This excludes compactifications with a boundary unless they separately possess this atlas.

</div>

<div id="lem:star" class="lemma">

**Lemma 3** (Positive spanning of a balanced star). *At every point of a positive balanced embedding chart the conical hull of its tangent support is its full linear span. A finite list of rational generators for the incident cones, including both signs of tangential generators, admits a relation $\sum_i\lambda_i v_i=0$ with every $\lambda_i>0$ rational.*

</div>

<div class="proof">

*Proof.* In dimension zero the assertion is immediate. In positive dimension we first explain the passage from lattice balancing to Euclidean flux. Write $c_\sigma$ for the Euclidean covolume of the saturated tangent lattice of a top cell and $c_\tau$ for that of a facet. The orthogonal projection of the primitive inward normal has length $c_\sigma/c_\tau$. Thus Euclidean density $\mu_\sigma=w_\sigma c_\sigma>0$ has flux vector $\mu_\sigma\nu_{\sigma\tau}=c_\tau w_\sigma n_{\sigma\tau}$ modulo tangents. Summing cancels by balancing. A common Euclidean metric suffices, with no integrality assumption on $w_\sigma$.

If the finite tangent cone were contained in a proper closed halfspace of its span, take a linear form $\ell\geq0$ on it that is strictly positive somewhere. Apply the divergence theorem on each top cone cut by the unit ball, to the constant vector representing $\ell$, tangent-projected in each cell. Internal facet fluxes cancel. Its divergence is zero, so the outer spherical flux is zero. That flux is the positive weighted integral of $\ell(v)$ on the unit angular sections. It is nonnegative everywhere and positive on an open angular patch of some top cone, a contradiction. The same argument in dimension one is the sum of the endpoint fluxes. A finitely generated cone is closed: by eliminating dependent generators one can represent each vector using an independent subset, and the finitely many such inverses bound coefficients on bounded sets. Separation from a point outside that closed convex cone follows by its nearest point and the squared-distance inequality. Hence failure to be the full span would supply exactly the forbidden halfspace.

Since the generators conically span the entire vector space, each $-v_i$ is a nonnegative combination of them. Rational row reduction and elimination of dependent active columns make those coefficients rational. Add these relations for all $i$ to obtain a rational relation with all coefficients strictly positive. ◻

</div>

<div id="lem:completion" class="lemma">

**Lemma 4** (Bounded rational completion in a chart). *A bounded finite-valued printed PC function $q$ in a chart has a unique continuous completion $F$ agreeing with its rational values. It satisfies $q\leq F$ and every real-endpoint PCC inequality. These completions agree across the transitions of Definition <a href="#def:chart" data-reference-type="ref" data-reference="def:chart">2</a>.*

</div>

<div class="proof">

*Proof.* Work near a point in $\operatorname{relint}(\tau)$. On a compact portion of that relative interior choose the star generators $v_i$ and the positive rational relation $\lambda_i$ of Lemma <a href="#lem:star" data-reference-type="ref" data-reference="lem:star">3</a>. There is an $\epsilon>0$ rational such that $z_i=z+\epsilon v_i$ lies in its assigned incident cell for every rational $z$ in that portion. For each incident cone, independent-column elimination gives $$y-z=\sum_i a_i v_i,\qquad a_i\geq0,\qquad \sum_i a_i\leq A\|y-z\|,$$ using generators of that cone and extending by zeros. If $y,z$ are rational the $a_i$ can be chosen rational. The finite constant $A$ is uniform over the finitely many independent subsets.

For sufficiently close $y$ the PCC from $z,z_i$ to $y$, in that incident cell, gives $$q(y)-q(z)\leq 2B\sum_i a_i/\epsilon,$$ where $|q|\leq B$ in the chosen neighborhood. For the opposite inequality set $t=\max_i(a_i/\lambda_i)$ and $b_i=(t\lambda_i-a_i)/\epsilon\geq0$. Then $$z=\frac{y+\sum_i b_i z_i}{1+\sum_i b_i},\qquad
 q(y)-q(z)\geq-2B\sum_i b_i.$$ The center lies in $\tau$, and all endpoints lie in cells incident to $\tau$, so this is a legal PCC. Both sums are bounded by a constant times $\|y-z\|$. We have obtained a Lipschitz comparison to rational points $z$ on $\tau$, uniform on a smaller compact portion.

Within each relative interior, rational values therefore extend continuously. For a rational sequence $y\to p$ from any incident cell, choose rational $z\in\tau$ tending to $p$ with $\|z-p\|\leq\|y-p\|$. The comparison shows $q(y)$ tends to the extension on $\tau$. A finite-face induction gives one continuous function $F$ across all faces. For an arbitrary irrational $p$ choose shrinking rational simplices containing it in its minimal face. Jensen for their rational vertices gives $q(p)\leq F(p)$.

The real-endpoint test follows from rational approximation of the perspective constraints in the proof of Lemma <a href="#lem:rational" data-reference-type="ref" data-reference="lem:rational">1</a>, using continuity of $F$. The completion is unique because rational points are dense. On overlaps, rational integral-affine transitions preserve those points; uniqueness proves gluing. This proof uses only local boundedness, not a global embedded decomposition. ◻

</div>

<div id="lem:maximum" class="lemma">

**Lemma 5** (Strong maximum principle). *For a continuous real-endpoint PC function on a balanced chart space, the set where a attained global maximum is taken is open and closed. On a connected compact such space the function is constant.*

</div>

<div class="proof">

*Proof.* Let $p$ be a maximum point and use a small star there. Lemma <a href="#lem:star" data-reference-type="ref" data-reference="lem:star">3</a> applies also at irrational $p$ because the star directions and balancing equations are unchanged in the relative interior of its face. Choose small anchors $p+\epsilon v_i$. For nearby $y$ in an incident cell write $y-p=\sum a_i v_i$ as above. The reverse relation with $b_i\geq0$ writes $p$ as a PCC of $y$ and the anchors, with a strictly positive coefficient on $y$. Every endpoint value is at most the global maximum. Equality at $p$ therefore forces the value at $y$ to be that maximum. Its set is open, and continuity makes it closed. Compactness supplies a maximum on each connected component. ◻

</div>

<div id="thm:compact" class="theorem">

**Theorem 6** (Compact endpoint classification). *Let $X$ be compact in the precise chart category of Definition <a href="#def:chart" data-reference-type="ref" data-reference="def:chart">2</a>. It has finitely many connected components $D$. Every continuous PC reference $\gamma$ is constant on each $D$. For every $u\in C(X)$ the actual unrestricted printed envelope is $$P_\gamma(u)|_D=\min_D(\gamma+u).$$ It is globally uniformly and decreasingly regularizable in both the literal and real categories, in the same reference class. If $\gamma+u$ is locally literal PA, the displayed constants are rational, and the envelope itself is literal PA. This last assertion requires no global bounded rational-cell structure.*

</div>

<div class="proof">

*Proof.* Polyhedral charts are locally connected. Connected components of a locally connected space are open; in a compact space their disjoint open covering has a finite subcover, so there are finitely many, and each is also closed and compact. Lemmas <a href="#lem:rational" data-reference-type="ref" data-reference="lem:rational">1</a> and <a href="#lem:maximum" data-reference-type="ref" data-reference="lem:maximum">5</a> give the assertion for $\gamma$.

Let $E$ be the defining supremum of all competitors. The constant translate $\gamma-\|u\|_\infty$ is a competitor. Thus $E$ is bounded, finite-valued, and below the continuous obstacle $\gamma+u$. A pointwise supremum preserves every PCC inequality. Apply Lemma <a href="#lem:completion" data-reference-type="ref" data-reference="lem:completion">4</a> in the finite chart cover. The completion $F\geq E$ still lies below the obstacle, by continuity and comparison at rational points. It is continuous PC, and its difference from $\gamma$ is bounded, so it is itself a competitor. Consequently $F\leq E$ and $F=E$. The maximum principle makes $E$ componentwise constant. Its constant on $D$ cannot exceed $\min_D(\gamma+u)$, while that componentwise minimum is itself a PC competitor. This proves the formula for the actual unrestricted envelope, rather than for a modified continuous-only envelope.

Real componentwise constants are real PA. Choose decreasing rational constants converging to the finitely many component minima; for example $2^{-n}\lceil2^n c_D\rceil$ decreases to $c_D$ with error less than $2^{-n}$. Componentwise literal constants give global uniform decreasing approximation. They and the endpoint differ boundedly from the actual reference.

Finally let $p$ minimize a locally literal obstacle on $D$. In a carrying chart take the cell $\tau$ with $p\in\operatorname{relint}(\tau)$. Its affine restriction has a local minimum at a relative interior point; both tangent directions are allowed, so its derivative on the tangent space is zero. It is constant on that cell. There is a rational point $y$ in $\operatorname{relint}(\tau)$, by Lemma <a href="#lem:rational" data-reference-type="ref" data-reference="lem:rational">1</a>; its literal affine value is rational and equals the minimum. This works even if the chart cell is unbounded, and even if $p$ is irrational. All component minima are therefore rational. ◻

</div>

<div id="prop:noncompact" class="proposition">

**Proposition 7** (Why this is not a compact global embedding). *A nonempty finite globally embedded pure positive-dimensional positive balanced rational support is noncompact.*

</div>

<div class="proof">

*Proof.* If compact, all cells are bounded. Use the Euclidean densities from Lemma <a href="#lem:star" data-reference-type="ref" data-reference="lem:star">3</a> and apply the divergence theorem cell by cell to the tangent projection of the ambient vector field $Y(x)=x$. Its divergence on every $d$-cell is $d>0$. Internal facet fluxes cancel by balancing. There is no external boundary. Thus a strictly positive sum of weighted $d$-volumes would equal zero. This contradiction concerns a single global embedding. It says nothing against the compact chart spaces of Theorem <a href="#thm:compact" data-reference-type="ref" data-reference="thm:compact">6</a>. ◻

</div>

# Global affine approximation with rational geometry

<div id="lem:polyhedron" class="lemma">

**Lemma 8** (Finite polyhedral representation). *A polyhedron is the sum of the convex hull of finitely many points and a finitely generated recession cone, with a linear space allowed. For rational spatial inequalities all points and rays can be chosen rational. Conversely the convex hull of finitely many points plus a finitely generated cone is a polyhedron and is closed. Faces are obtained by retaining exactly the point and ray generators where a defining supporting functional is minimal or zero.*

</div>

<div class="proof">

*Proof.* For a homogeneous cone $C=\{Ax\geq0\}$ split off $\ker A$. On its orthogonal complement $\ell(x)=\sum_j(Ax)_j$ is strictly positive on $C\setminus\{0\}$. The section $\ell=1$ is bounded: an unbounded sequence, divided by its norms, would give a unit vector in $C$ with $\ell=0$. A bounded polyhedron is the convex hull of its vertices. Indeed, at a nonvertex choose a nonzero direction annihilating all active equalities, move in both directions until a new independent inequality is active, and express the original point as their convex combination. Boundedness ensures both endpoints; induction on the active rank terminates. There are finitely many possible independent active systems. This proves finite generation of a pointed cone; add both signs of a basis of its lineality space.

Homogenize a polyhedron by $(x,t)$ with $t\geq0$ and $Ax-tb\geq0$. Generators with $t>0$ give points after division by $t$, those with $t=0$ give recession directions. Rational elimination gives rational choices when the input is rational. To prove the converse, write $x=\sum\lambda_i p_i+\sum\mu_j r_j$, $\lambda_i,\mu_j\geq0$, $\sum\lambda_i=1$, and eliminate variables successively. In one elimination, lower bounds on a variable must not exceed every upper bound; if only one sign is present there is no paired constraint. This Fourier–Motzkin step preserves an exact finite system of weak linear inequalities, and rational coefficients when present. The image is therefore a closed polyhedron. Finally equality in a supporting inequality forces all positive point coefficients to attain its minimum and all positive ray coefficients to have zero functional value, proving the face assertion. ◻

</div>

<div id="lem:duality" class="lemma">

**Lemma 9** (Elementary duality). *Every finite convex function on $\mathbb R^d$ is continuous and is the supremum of its affine lower supports. Consequently it equals its double Legendre transform. A finite lower-semicontinuous convex function on a compact polytope is continuous in its relative topology.*

</div>

<div class="proof">

*Proof.* First, finiteness implies continuity. Around $x$ take a cube containing the ball of radius $2r$ and bound the function above by $B$, the maximum of its vertex values. Reflection in $x$ bounds it below on the ball of radius $r$ by $2f(x)-B$. For $y,z$ in the ball of radius $r/2$, extend the ray from $y$ through $z$ to length $r$. Convexity then bounds $f(z)-f(y)$ by $2(B-f(x))\|z-y\|/r$; reverse $y,z$ for the other inequality. This is a local Lipschitz bound. For an affine support at $x$, project $(x,f(x)-t)$ to the closed convex epigraph, for $t>0$. Projection exists by compactness after intersecting with a sufficiently large ball. The squared-distance inequality gives a supporting normal. Let $t\downarrow0$, normalize and take a convergent subsequence of normals; projection distance is at most $t$, so the contact points tend to $(x,f(x))$. The limiting support has nonpositive vertical component. It cannot have zero vertical component, since the epigraph projects onto all $\mathbb R^d$: a nonzero horizontal functional cannot be bounded below on that projection. Dividing by its negative vertical component gives an affine lower support at $x$. Taking all supports proves the double-transform assertion.

For continuity of $g$ on a compact polytope $\Delta$, its maximum is bounded by $B=\max g(v)$ over the finitely many vertices. Fix $p\in\Delta$. Choose $r>0$ smaller than each inactive inequality’s slack divided by its normal norm. For $y\in\Delta$ close to $p$, the point $z=p+r(y-p)/\|y-p\|$ still lies in $\Delta$: inequalities active at $p$ are homogeneous along that ray and the inactive ones remain satisfied. Convexity gives $$g(y)\leq g(p)+(\|y-p\|/r)(B-g(p)).$$ Lower semicontinuity supplies the opposite limiting inequality. This proves relative continuity even at boundary points; no claim about an arbitrary nonpolyhedral compact convex set is needed. ◻

</div>

<div id="thm:affine" class="theorem">

**Theorem 10** (Same-reference global interpolation). *Let $V\simeq\mathbb R^d$ be a complete rational affine plane and let $\gamma\in\mathrm{PAPC}_\mathbb R(V)$ have finite rational carrying geometry and be positive at infinity. Let $f$ be continuous convex with $\|f-\gamma\|_\infty<\infty$. For every $\eta>0$ and every finite rational set $S\subset V$ there is $F\in\mathrm{PAPC}_\mathbb R(V)$, with a finite rational carrier, such that $$f\leq F\leq f+\eta\quad\hbox{on all of }V,\qquad F|_S=f|_S,
 \qquad F^\infty=\gamma^\infty.$$ In particular every such $f$ has global uniform decreasing approximation in the actual reference class. Real slopes and heights of $\gamma$ need not be rational.*

</div>

<div class="proof">

*Proof.* Translate rationally to $V=\mathbb R^d$. A finite convex PA function is a maximum of its finitely many affine pieces, since each piece on a full-dimensional open region is a global support. Write $\gamma=\max_j(\langle a_j,x\rangle+b_j)$, $h=\gamma^\infty=\max_j\langle a_j,x\rangle$, and $\Delta=\operatorname{conv}\{a_j\}$. Positivity at infinity says $h(v)>0$ for every nonzero $v$, so $0$ is interior to $\Delta$. Also $\gamma-h$ is bounded.

The recession cones of a finite rational carrying complex cover $V$. To see this, along a ray some cell contains unboundedly many of its points; its finite inequalities put that direction in its recession cone. The recession function is linear on each such cone. Subdivide into pointed rational cones and choose their rational ray generators $r_k$. Then $$\operatorname{epi}h=\operatorname{cone}\{(r_k,h(r_k)),(0,1)\}.$$ The heights here can be irrational. Every point of the epigraph is obtained from the rays of the cone containing its spatial coordinate, plus a vertical vector.

Let $f^*(p)=\sup_x(\langle p,x\rangle-f(x))$. Its domain is exactly $\Delta$, and it is bounded there. Indeed $f$ differs boundedly from $h$. For $p\in\Delta$, $\langle p,x\rangle\leq h(x)$ yields a finite uniform upper bound, and $x=0$ yields a lower bound. For $p\notin\Delta$, nearest-point separation from $\Delta$ gives a direction $v$ with $\langle p,v\rangle>h(v)$, making the supremum infinite. The transform is convex and lower semicontinuous as a supremum of affine functions. Lemma <a href="#lem:duality" data-reference-type="ref" data-reference="lem:duality">9</a> therefore makes $f^*$ continuous on the compact polytope $\Delta$.

Since $f$ is continuous, the supremum defining $f^*$ can be taken over rational $x$. For each $p\in\Delta$ choose one such point giving error less than $\eta/2$. Continuity of the transform and of this affine function gives a neighborhood where the error is less than $\eta$. A finite subcover gives a finite rational set $A$, to which we add $S$, such that $$f^*(p)-\eta\leq g_A(p):=\max_{x\in A}(\langle p,x\rangle-f(x))\leq f^*(p)
 \quad(p\in\Delta).$$ Form the closed polyhedron $$E_A=\operatorname{conv}\{(x,f(x)):x\in A\}+\operatorname{epi}h.$$ It projects onto all $V$ and is upward closed. It lies in $\operatorname{epi}f$: duality and $\operatorname{dom}f^*=\Delta$ give $f(x+v)\leq f(x)+h(v)$, and convexity then gives the assertion for every convex combination of generators. Hence its vertical fibers have finite lower endpoints. Write $E_A=\operatorname{epi}F_A$. The polyhedral lower boundary is finite convex PA.

Direct maximization of $\langle p,x\rangle-t$ over the point and ray generators gives $$F_A^*(p)=g_A(p)\ (p\in\Delta),\qquad F_A^*(p)=+\infty\ (p\notin\Delta).$$ Double duality thus proves the *global* inequalities $f\leq F_A\leq f+\eta$. The lifted points of $S$ belong to $E_A$, so $F_A(s)\leq f(s)$; equality follows from the lower bound.

Rationality of the carrying geometry needs a separate argument. Each graph face is generated by a subset of the lifted points and a subset of the rays where its supporting functional vanishes. No vertical ray belongs to a graph face. Its spatial projection is therefore the convex hull of rational spatial points plus a cone of rational spatial directions. Lemma <a href="#lem:polyhedron" data-reference-type="ref" data-reference="lem:polyhedron">8</a> makes this a rational polyhedron. Projection is one-to-one on the graph, so graph-face intersections project to common faces. These finitely many projections, and their faces, are a finite rational carrier of $F_A$. Lemma <a href="#lem:rational" data-reference-type="ref" data-reference="lem:rational">1</a> puts it in the actual scalar extension; ordinary convexity supplies affine lower supports and genuine divisor positivity.

Its recession is exactly $h$, not an auxiliary rational approximation to $\gamma$. The recession cone of $E_A$ is $\operatorname{epi}h$: one inclusion is immediate, and for the other divide a sequence $e_0+T v=k_T+c_T$, with $k_T$ in the bounded convex hull and $c_T\in\operatorname{epi}h$, by $T\to\infty$ and use closedness of that cone. Alternatively the already established bounded difference from $f$ gives the same recession. Thus $F_A-\gamma$ is globally bounded.

Finally take $\eta_n=2^{-n}$ and majorants $F_n$ with $0\leq F_n-f\leq2^{-n}$. Put $G_n=F_n+4\cdot2^{-n}$. Then $$G_n-G_{n+1}\geq4\cdot2^{-n}-5\cdot2^{-n-1}>0,
 \qquad0\leq G_n-f\leq5\cdot2^{-n}.$$ These rational constant shifts preserve the carrier and recession and give a decreasing uniform sequence. The unshifted majorants, rather than the shifted sequence, interpolate $S$ exactly. ◻

</div>

# Independent affine branches and arbitrary continuous obstacles

<div class="definition">

**Definition 11**. An independent affine bouquet is $X=\bigcup_{i=1}^r(a+V_i)$, where $a$ is rational, the $V_i$ are rational $d$-dimensional linear subspaces, $\sum_i V_i$ is a direct sum, and each complete plane carries an arbitrary constant strictly positive weight. The tangent lattices are saturated; no unimodularity assumption is made. The case $r=1$ is a complete plane. This is a finite globally embedded balanced rational support.

</div>

<div id="lem:branches" class="lemma">

**Lemma 12** (The actual continuous PC cone). *A continuous function on an independent affine bouquet is PC exactly when its restriction to each plane is ordinarily convex. The restrictions have the same value at $a$ by continuity.*

</div>

<div class="proof">

*Proof.* Translate $a$ to zero. Restrict a rational segment in one plane to a common rational carrying refinement. Between its finitely many crossings the PCC test inside a cell gives convexity. At each crossing, the two nearby rational endpoints and their center in the common face give the two-sided chord inequality; this orders the left and right secant slopes. Concatenating these inequalities proves convexity along the whole segment, including a crossing at zero. Equivalently one can refine the support by the segment’s rational line and use this one-dimensional subdivision. Real-endpoint continuity extends this to arbitrary segments in the plane. No auxiliary face of this subdivision adds a constraint from another branch except at zero.

Conversely, for a PCC centered away from zero, all its incident cells lie in a single plane, and ordinary convexity proves Jensen. For a PCC at zero group its endpoints by branch, writing $\beta_i$ for each group’s total weight. Independence implies that its spatial weighted sum in each $V_i$ is separately zero. Ordinary convexity on that plane gives $$\sum_{j\text{ in branch }i}\alpha_j f(x_j)\geq\beta_i f(0).$$ Summing over the nonempty groups proves the PCC inequality at zero. Endpoints equal to zero contribute directly. This proves every face constraint, not merely a selection of origin circuits. ◻

</div>

<div id="prop:envelope" class="proposition">

**Proposition 13** (Unrestricted envelope continuity in the used domain). *On a locally finite positive balanced rational embedding support, a continuous PC reference and a bounded continuous obstacle have an actual unrestricted envelope that is continuous PC and differs boundedly from the reference. Its dependence on the obstacle is $1$-Lipschitz in the global uniform norm.*

</div>

<div class="proof">

*Proof.* The supremum $E$ is finite and satisfies $\gamma-\|u\|_\infty\leq E\leq\gamma+u$. It is PCC convex. On each compact portion of a chart it is bounded. The proof of Lemma <a href="#lem:completion" data-reference-type="ref" data-reference="lem:completion">4</a> uses only that local bound, so it completes $E$ continuously. The completions agree on overlaps. Rational-point comparison with the two continuous bounds makes the completion $F$ satisfy those same bounds everywhere; hence $F-\gamma$ is globally bounded. It is an eligible competitor below $\gamma+u$ and dominates $E$, giving $E=F$. This independently reconstructs the bounded-envelope portion of R230; it does not prove its stronger completion theorem for arbitrary unbounded printed PC functions. Finally, if $\|u-v\|_\infty\leq\delta$, translating any competitor by $-\delta$ proves $P_\gamma(u)-\delta\leq P_\gamma(v)$, and interchange gives the Lipschitz bound. ◻

</div>

<div id="thm:bouquet" class="theorem">

**Theorem 14** (All-continuous real regularity on independent bouquets). *Let $X$ be an independent affine bouquet and let $\gamma$ be any actual finite rational-carrier $\mathrm{PAPC}_\mathbb R$ reference positive at infinity. Every continuous PC function $f$ with $\|f-\gamma\|_\infty<\infty$ has global uniform decreasing approximation by $\mathrm{PAPC}_\mathbb R(X,\gamma)$ with exact branchwise recession $\gamma^\infty$. Consequently the actual unrestricted envelope is regularizable for every $u\in C_b(X)$, including arbitrary continuous branch data that are not PA. No separability assumption on that data is used.*

</div>

<div class="proof">

*Proof.* By Lemma <a href="#lem:branches" data-reference-type="ref" data-reference="lem:branches">12</a> each $f_i$ is convex and $f_i(a)=f(a)$. Apply Theorem <a href="#thm:affine" data-reference-type="ref" data-reference="thm:affine">10</a> to each plane with the same error $2^{-n}$ and the prescribed rational interpolation set $\{a\}$. Obtain $F_{i,n}\geq f_i$ with $F_{i,n}(a)=f(a)$ and exact recession of the *actual* $\gamma_i$. They glue to $F_n$ on $X$. Refine their rational carriers by a rational orthant fan on each branch, making $a$ a common zero-dimensional face. This operation introduces no walls defined by real heights. The resulting global carrier is finite and rational. Its affine coefficients lie in the scalar extension by Lemma <a href="#lem:rational" data-reference-type="ref" data-reference="lem:rational">1</a>.

Lemma <a href="#lem:branches" data-reference-type="ref" data-reference="lem:branches">12</a> proves all PCC inequalities for $F_n$. To verify genuine PA positivity directly, at $a$ choose a supporting affine function on each branch. Their constant terms are the shared value $f(a)$. Independence extends their linear parts simultaneously to the ambient direct sum, so their common ambient affine function supports $F_n$ on every branch. At a point different from $a$ a small neighborhood meets only its one plane and its ordinary convex support suffices. Lemma <a href="#lem:rational" data-reference-type="ref" data-reference="lem:rational">1</a> thus proves divisor positivity with the saturated normals, for every nonnegative local cycle.

We have $0\leq F_n-f\leq2^{-n}$ on all of $X$. Use the same rational shift $4\cdot2^{-n}$ on every branch, as in Theorem <a href="#thm:affine" data-reference-type="ref" data-reference="thm:affine">10</a>. This keeps the common value synchronized and gives a global decreasing uniform sequence. All its functions differ boundedly from the actual reference and have its exact recession; no reference was changed. Proposition <a href="#prop:envelope" data-reference-type="ref" data-reference="prop:envelope">13</a> puts each actual unrestricted envelope in the continuous PC domain to which this theorem applies. Regularization precedes any use of a completed Monge–Ampere operator. ◻

</div>

<div id="prop:roofs" class="proposition">

**Proposition 15** (Explicit synchronized convex roofs). *For $u\in C_b(X)$ put $b_i=\gamma_i+u_i$. Let $H_i$ be its greatest ordinary convex minorant on the complete plane and set $c=\min_i H_i(a)$. Let $Q_i$ be its greatest convex minorant subject additionally to $Q_i(a)\leq c$. Then $Q_i(a)=c$, and $P_\gamma(u)$ is obtained by gluing the $Q_i$. For finite rational-carrier real-PA $b_i$, this envelope itself has a finite rational real-PA carrier.*

</div>

<div class="proof">

*Proof.* The convex minorant $\gamma_i-\|u\|_\infty$ proves that $H_i$ is finite and boundedly equivalent to $\gamma_i$. Its supremum is convex and finite on a complete plane, hence continuous by Lemma <a href="#lem:duality" data-reference-type="ref" data-reference="lem:duality">9</a>. The shifted function $H_i-(H_i(a)-c)$ is an eligible minorant for $Q_i$, so $Q_i(a)=c$ and it too is finite, continuous, and in the same growth class. Their gluing is PC by Lemma <a href="#lem:branches" data-reference-type="ref" data-reference="lem:branches">12</a>. The actual envelope is continuous by Proposition <a href="#prop:envelope" data-reference-type="ref" data-reference="prop:envelope">13</a>, is convex on each plane, and at $a$ has value at most every $H_i(a)$, hence at most $c$. It is therefore bounded above by $Q_i$ on that plane. The glued $Q_i$ is a competitor, so equality follows. This is an explicit convex-roof description in this geometric sector, not a proposed classification of general singular spaces.

For the last assertion take a pointed rational refinement carrying $b_i$. By Lemma <a href="#lem:polyhedron" data-reference-type="ref" data-reference="lem:polyhedron">8</a> each of its epigraph pieces is generated by finitely many lifted rational spatial vertices, their lifted rational spatial recession rays (with real heights), and the vertical ray. The bounded difference from $\gamma_i$ makes these recession heights exactly $\gamma_i^\infty$ on their cones. The closed convex hull of all pieces is the convex hull of the finite lifted vertices plus $\operatorname{epi}\gamma_i^\infty$, by the same finite-generator argument. Adding $(a,c)$ gives the capped roof. It is bounded below by the shifted $H_i$, so its lower boundary is finite. Every graph face projects to the convex hull of a subset of rational spatial vertices plus a cone of rational spatial rays. The graph-face proof in Theorem <a href="#thm:affine" data-reference-type="ref" data-reference="thm:affine">10</a> supplies a rational carrier, despite real heights and slopes. The common value is $c$, so the branches glue on a rational carrier as before. ◻

</div>

The geometric theorem includes, for example, the union of two independent rational two-planes. It permits a bounded continuous obstacle with mixed coordinate dependence on either plane. It does not include a product of a cross with a line: its planes share a positive-dimensional trace instead of a single point. Approximating that trace by different branch constructions is an additional constraint not solved here.

# The finite noncompact literal obstruction

<div id="thm:literal" class="theorem">

**Theorem 16** (Literal nonregularity on every finite noncompact support). *Let $X$ be a noncompact finite globally embedded rational polyhedral support and let $\gamma\in\mathrm{PAPC}_\mathbb Z(X)$ be positive at infinity. Balancing is not needed. There is a bounded literal rational-carrier obstacle $u$ whose actual unrestricted envelope cannot be uniformly approximated by literal PC PA functions in the same growth class. In particular every nonempty finite globally embedded positive balanced space of positive dimension fails literal regularity.*

</div>

<div class="proof">

*Proof.* Choose a noncompact connected component, a rational point $p$ in it, and rational $C>\gamma(p)$. Put $$\phi=\max\{\gamma,C\},\qquad D=\phi-\gamma.$$ All these functions have rational carrying geometry: their coefficients are rational and the inserted equality walls are rational. Maximum preserves the PCC inequalities; Lemma <a href="#lem:rational" data-reference-type="ref" data-reference="lem:rational">1</a> gives PA divisor positivity. Positivity at infinity makes $\gamma$ proper on the finite support. Explicitly, on each pointed cell its vertex part is bounded, and its affine recession slope has a positive minimum on the unit section of the recession cone; the finite list of cells gives $\gamma(x)\geq\kappa\|x\|-A$ outside a bounded set, for some $\kappa>0$. Thus $D\geq0$ has compact support, is positive at $p$, and vanishes far out in the same component. A finite rational pointed common refinement carries $\gamma,D$. The bounded affine restriction of $D$ on an unbounded cell has zero recession slopes; along any nonzero recession direction it eventually vanishes, so it is identically zero on that cell.

A connected component of a finite polyhedral support is path connected. Moving from $p$ to a far point where $D=0$, some bounded positive-dimensional carrying cell must have a nonzero affine slope $k$ for $D$. Choose a primitive lattice direction $w$ in that cell with $k(w)\ne0$ and a small rational segment $a+[0,L]w$ in its relative interior. Choose an integer $N>|k(w)|$ and define $$f=\gamma+D/N=(1-1/N)\gamma+(1/N)\phi.$$ It is continuous PC with the same growth. Its slope on the segment is $q_0=m+k(w)/N\notin\mathbb Z$, where $m$ is the integral slope of $\gamma$.

We construct a literal obstacle whose envelope is exactly $f$. Fix an ambient integral lattice norm $\rho(x)=\max_j|\ell_j(x)|$, with $\ell_j$ an integral coordinate basis. For each vertex $v$ of the pointed carrying refinement choose a common sufficiently large integer $M$ such that $$D(v)/N+M\rho(x-v)\geq D(x)/N\quad(x\in X).$$ Such a choice exists: near $v$ all incident affine pieces of $D$ have bounded slopes, and outside a fixed neighborhood the bounded numerator divided by $\rho(x-v)$ is bounded. There are finitely many vertices. Define $$u(x)=\min\bigl\{D(x),\ \min_v(D(v)/N+M\rho(x-v))\bigr\}.$$ Its slopes are integral and constants rational, including the shifts by rational $v$; min and max of these finitely many rational affine pieces give rational walls. It is bounded, $D/N\leq u\leq D$, equals $D(v)/N$ at every carrying vertex, and vanishes on every unbounded carrying cell. Thus $f\leq\gamma+u$ is a competitor.

Let $q$ be any unrestricted printed competitor below $\gamma+u$. On a bounded carrying cell express any point as a convex combination of its rational vertices. Their obstacle values equal $f$ and $f$ is affine, so PCC gives $q\leq f$ there. On an unbounded pointed cell express $$y=\sum_j\alpha_j v_j+\sum_k\beta_k r_k,\qquad
 \alpha_j,\beta_k\geq0,\quad\sum_j\alpha_j=1,$$ with rational vertices and rational recession directions. Choose a vertex $v_0$ with $\alpha_0>0$ and a large rational $T$ with $\sum_k\beta_k/T\leq\alpha_0$. Replace the corresponding amount of its weight by endpoints $v_0+Tr_k$ with weights $\beta_k/T$. All endpoints are rational in this cell and their weighted average is $y$. On this whole cell $D=u=0$, so its obstacle is exactly the affine $f=\gamma$. Jensen again proves $q(y)\leq f(y)$. The point $y$ and weights may be real; this is allowed by the printed rational-endpoint test. Thus the actual unrestricted envelope is $f$ everywhere.

Finally let $\psi$ be a literal PC PA approximant. On the selected primitive segment its slopes are nondecreasing integers. Let $k'$ be its right slope at the midpoint. If $k'\leq\lfloor q_0\rfloor$, compare the midpoint with the left endpoint; if $k'\geq\lceil q_0\rceil$, compare the right endpoint with the midpoint. Convexity in the appropriate half gives in either case $$\|\psi-f\|_\infty\geq \frac L4\operatorname{dist}(q_0,\mathbb Z)>0.$$ Indeed the difference of two endpoint errors is at least $(L/2)\operatorname{dist}(q_0,\mathbb Z)$, while each error is at most the uniform norm. This excludes uniform and decreasing-uniform literal regularization. The final balanced assertion follows from Proposition <a href="#prop:noncompact" data-reference-type="ref" data-reference="prop:noncompact">7</a>. No Monge–Ampere measure was assigned to this nonregularizable literal endpoint. ◻

</div>

<div class="corollary">

**Corollary 17** (Coefficient separation in the proved sectors). *For compact balanced chart spaces of Definition <a href="#def:chart" data-reference-type="ref" data-reference="def:chart">2</a>, both coefficient categories have endpoint regularity; literal PA obstacles even have exact literal endpoints. On every positive-dimensional independent affine bouquet, real regularity holds for every bounded continuous obstacle and every actual real reference, whereas literal regularity fails for every literal positive-at-infinity reference. Finite zero-dimensional spaces have regularity in both categories, by componentwise constants and decreasing rational approximation.*

</div>

# Operator order, retained grants, and unresolved original scope

No raw recursion or measure is used to infer regularization. The endpoints in Theorems <a href="#thm:compact" data-reference-type="ref" data-reference="thm:compact">6</a> and <a href="#thm:bouquet" data-reference-type="ref" data-reference="thm:bouquet">14</a> are first placed in their actual genuine regularizable PA domain. Only then may the exact primitive saturated recursion be completed. On a finite globally embedded bouquet, S272 supplies the symmetric positive mixed completion for an arbitrary actual real reference on precisely this domain. The sequence constructed above is an eligible global same-reference sequence. Its mass is the actual $\deg(\gamma)$ under the polyhedral intersection convention; no rational reference is substituted and no probability division by a possibly zero mass is made.

For clarity, the retained quantitative boundary is the one in the whole grants. With $C$ fixed, S272 chooses a rational positive component $\gamma_0$ and $\epsilon>0$ with $\gamma=\gamma'+\epsilon\gamma_0$ in the actual PC coefficient face. Its proper height $H_0=\gamma_0+c$ gives the bound $$\int H_0\,\mathrm{MA}(f_1,\ldots,f_d)
 \leq (2d/\epsilon)C\deg(\gamma)+\int H_0\,\mathrm{MA}(\gamma)
 \quad\text{when }\|f_i-\gamma\|_\infty\leq C.$$ The genuine completed operator has ordinary weak continuity, including bounded-continuous test functions, for uniform convergence to a member of that domain. Its weak and bounded-Lipschitz uniform continuity is retained only on each fixed-$C$ slice; its global vague uniform continuity is not promoted to global weak uniform continuity. This paper does not reprove the whole mixed theory, whose use here is an optional consequence of the supplied S272 grant. It does not assign this operator to arbitrary continuous PC functions on an unclassified space. On compact charts of positive dimension our envelope is locally constant and the primitive divisor is zero; every positive-order iterated raw product of such constants is zero directly, without a noncompact height argument.

S262 already grants real all-continuous regularity on finite balanced embedded graphs, with exact tail slopes and rational chord subdivisions; its literal noncompact negative part is independently reconstructed above. Those graph domains remain retained, rather than narrowed to PA data. A positive reference supplies finite upper bounds on outward slopes, and a positive local balancing relation supplies finite lower bounds. Rational chord interpolation then preserves all relation inequalities at vertices, convex bends on edges, and the actual tail slopes, with global uniform error tending to zero. The full graph proof and the corrected weak/BL qualifications are in the whole grant; this paragraph records a premise, not a fresh proof of the entire grant.

The original P05.1 is still not classified. The exact residual mathematical tasks after this paper are as follows.

1.  For higher-dimensional real-PA references on general singular finite balanced supports, characterize which actual continuous PC envelopes admit global rational-carrier same-reference approximation. The entire coefficient cone at every face, over arbitrary refinements, must be respected. A fixed-fan contact polynomial test or strict origin circuits do not supply this approximation theorem.

2.  For dependent affine branches or branches with a positive-dimensional common intersection, construct simultaneous approximants with the exact common continuous trace and exact recession, or find a geometric obstruction. Our finite interpolation at a point does not synchronize a non-PA trace on a positive-dimensional overlap.

3.  For arbitrary nonseparable obstacles on products of singular graphs or higher-dimensional spaces, prove the needed all-face constrained approximation or classify its failure. A separable envelope formula and regularity of individual factors do not answer this task. Products with one affine factor and positive-dimensional shared traces are not covered by the bouquet theorem.

4.  The compact literal result is complete in Definition <a href="#def:chart" data-reference-type="ref" data-reference="def:chart">2</a>’s boundaryless locally embedded balanced atlas category. If the original abstract category permits only cellwise quasi-embeddings, incompatible rational structures, or boundary compactifications lacking such an atlas, it has not been reduced here to that category, and the corresponding compact literal cases remain an explicit gap. A new proof of the appropriate intrinsic spanning/completion principle or a category reduction is required; global embedded noncompactness cannot be used instead.

5.  There is no all-conical theorem here for arbitrary nonconical obstacles, and no general higher-dimensional geometric necessary-and-sufficient criterion for the original target. We have not asserted that every balanced real pair is regular or that a quadratic finite-distance PCC margin gives a first-order slope floor.

These are mathematical gaps, not permission or compute gaps. No missing heavy-compute facility is needed for the results proved here. The operator’s provider/model/invocation certification is external to this child’s mathematical evidence; the child records its visible environment and commands only. A successful exact check or TeX build is not a mathematical audit. Candidate status for the original task is **false**.

# Source and artifact statement

The source ledger records binding files, exact versions, whole immediate proof units read, applications, recursive foundations not freshly reconstructed, and unused working-data exclusions. Long original source extracts and rendered pixels remain LOCALONLY. `argument.md` is the readable rendering of this whole fresh paper. The safe exact checks, their input, output, commands and environment are recorded alongside it. No historical emitter, supplied orchestration program, active private audit, network source, or nested agent was used. Artifact digests are reproducibility identifiers only. The original P05.1 is the sole active author target; no P05.2 or P05.5 completion is claimed.
