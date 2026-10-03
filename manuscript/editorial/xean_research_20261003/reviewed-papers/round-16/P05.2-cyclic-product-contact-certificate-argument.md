# A generator-contact certificate and a cyclic two-graph example

Unverified mathematical working note, 3 October 2026. This is the authoritative argument for this attempt. Every mathematical dependency of the claims below is proved here. Source definitions fix the convention; earlier theorem statements, audits, native notes, publication receipts, and computation are not premises.

## Exact result and limitation

The universal two-finite-graph theorem requested in the assignment is **not established**. In particular there is no assertion here for every reference and obstacle on the triangle squared. No actual-contact counterexample is established either.

The proved partial result is a finite **generator-contact certificate**: on a finite balanced rational polyhedral space, a real-PA PC candidate in the reference growth class is the actual raw envelope whenever the obstacle majorizes that candidate and agrees with it at the vertices of a pointed rational affine structure for the candidate. The certificate gives actual PAPC regularization and the complete recursive contact identity. It concerns a specified class of obstacles, not an orthogonality property of the pair for arbitrary obstacles.

It yields an explicit uniform family on the specified cyclic graph product, for every
\[
 c>0,\quad r\in\mathbb Q\cap(0,1),\quad\eta>0,\quad\varepsilon>0.
\]
The reference, envelope, and obstacle are
\[
 \begin{aligned}
 \gamma(p,q)&=c(g(p)+g(q)),\\
 H(p,q)&=c\max\{g(p)+g(q),r\},\\
 S(p,q)&=(r-g(p)-g(q))_+,\\
 f&=H+\eta S+\varepsilon T,\qquad u=f-\gamma.
 \end{aligned}                                                \tag{1}
\]
where \(g(x,y)=|x|+|y|\) on the triangle with its three leaves, and \(T\) is the tent on the bounded rectangle \(BC\times BC\) defined below. Both \(H\) and \(u\) are genuinely nonseparable; \(f\) is not PC. There are actual noncontact points at the product junction \((A,A)\) and the bounded rectangle centre. Nevertheless
\[
 P_\gamma(u)=H,\qquad
 \int_{G\times G}(H-f)\,H^2\cdot[G\times G]=0.                \tag{2}
\]
The full operator has fourteen positive atoms, total mass \(128c^2\); all remaining coefficients vanish. Its fan computation includes cones of actual saturated-lattice index two. A finite PCC witness extends the certificate to every bounded nonnegative real-PA replacement for \(\eta S+\varepsilon T\) vanishing at the fourteen positive-mass vertices, on any finite rational spatial domains; no contact at \((A,A)\) is required. References can be changed by arbitrary bounded real-PA shifts, provided the changed reference is itself PC and positive at infinity. These are precise obstacle/reference restrictions. They do not cover arbitrary data.

The original arbitrary-balanced-pair P05.2 classification, the requested universal two-graph theorem, the requested all-data triangle-square case, and P06.2 remain unresolved in this attempt. Status is partial; candidate is false. No literal-category, analytic realization, priority, certification, or formal-verification claim is made.

## Authentic conventions and source boundary

The source is Botero--Mazzon--Pille-Schneider, *Monge--Ampère measures on balanced polyhedral spaces*, arXiv:2603.08664v1, manuscript dated 10 March 2026, abbreviated BMPS. The following are exact mathematical contents of the definitions used here, with their real scalar extension explicitly fixed.

* Definitions 2.1--2.4: a rational spatial polyhedron has rational affine inequalities, and a rational structure is a finite complex of such polyhedra on the actual carrier \(X\subset N_\mathbb R\). Structures are considered up to common refinement. No change of ambient graph embedding or lattice is allowed here.
* Definition 2.18: \(N_\sigma=N\cap\operatorname{span}_\mathbb R(\sigma-\sigma)\); for a facet \(\tau\prec\sigma\), the inward normal is a lift of the primitive positive generator of \(N_\sigma/N_\tau\). Definition 2.20: the weighted sum of inward normals is tangent to the tested facet. Definition 2.19 literally specifies rational weights; this note extends weights and all affine coefficients to real scalars. The carrier weights remain the assignment's positive rational weights.
* Definition 2.28 literally has integral linear parts and rational constants. Here real PA means continuous functions real-affine on a finite **rational spatial** structure. On a fixed rational structure the continuity equations are rational linear equations. Their solution space has a rational basis; scaling its basis vectors clears all slope denominators. Thus this convention is the real span of that structure's literal PA functions. Real values do not license irrational spatial walls.
* Definition 3.2: a PCC has finitely many rational endpoints \(x_i\in X\cap N_\mathbb Q\), arbitrary real \(\alpha_i\geq0\), \(\sum\alpha_i=1\), and actual centre \(x=\sum\alpha_i x_i\). On some permitted rational structure there must be cells \(\tau\preceq\sigma_i\) with \(x\in\tau\), \(x_i\in\sigma_i\). Definition 3.3: a finite raw PC function satisfies \(h(x)\leq\sum\alpha_i h(x_i)\) for every such PCC, on every permitted structure. Raw continuity is not assumed in any comparison below.
* Definition 3.1: PAPC tests \(a\cdot z\geq0\) for every nonnegative balanced local cycle of every positive dimension on every ordinary open subset. The tests here include nonnegative real cycle weights.
* Definition 3.14: the reference class has two-sided growth \(a=\gamma+O(1)\). Definition 6.2: the raw envelope is
\[
 P_\gamma(u)(x)=\sup\{q(x):q\in\mathrm{PC}(X),\ q\leq\gamma+u,
                                  \ q\leq\gamma+C_q\text{ for some }C_q\}. \tag{3}
\]
The competitors themselves need only the upper growth bound displayed in (3).
* Proposition 3.22 / Definition 3.23: uniform limits of PAPC functions in the reference growth class are PC-regularizable; the approximants can be decreasing. We supply the explicit sequence \(H+1/j\), and use no approximation existence theorem.
* Definition 2.31 defines the divisor by (4) below. Definition 4.4 gives \(\operatorname{MA}_{\mathrm{poly}}(a)=a^d\cdot[X]\) as the finite atomic measure at the structure's vertices. Definition 4.15 requires strictly positive affine slope on every nonzero recession vector of every reference affine cell. Definition 6.9 is the exact integral \(\int(P_\gamma(u)-\gamma-u)\operatorname{MA}_{\mathrm{poly}}(P_\gamma(u))=0\) for all bounded PA obstacles, assuming regularity. Proving that definition for the entire pair is not claimed here.

The complete proof bodies of BMPS Lemmas 2.34--2.35 and 3.4, Proposition 3.22, Lemma 4.6, and Proposition 6.13 were inspected. The source Proposition 6.13 is one-dimensional and uses BBGS22 Proposition 5.13 for PC locality. Neither that black box nor a higher-dimensional extension is used. The PC-to-PAPC implication, divisor algebra, and regularization needed here are reconstructed below. The opposite implication of the source's Lemma 3.4 and automatic raw-PC continuity are unnecessary.

The controlling book's Chapter 72 states the one-dimensional rank-one relation classification, allows cycles, gives the complete affine result, and leaves arbitrary nonseparable product obstacles and higher-dimensional real-PA cases open. Its embedded graph theorem and proof were inspected; their local raising argument is not imported. The indicated Appendix M contains analytic regularity/current results, not a replacement polyhedral product theorem, and none of those results is applied.

The previous graph-cylinder argument, its author audit and research notes, and the committed native notes in the round-10 run were read as fallible comparisons. The present argument does **not** use the cylinder theorem or its formula as a premise. In that proof a single graph interpolation follows a complete-affine-fibre partial infimum; two cyclic graph factors have no such affine fibre. The exact missing global reconstruction is described at the end. Source extraction used `text.split('\n')`, never `splitlines()`. Complete source proof boundaries and identifiers are recorded in `source-excerpts.txt`. No receipts or hashes are mathematical evidence of correctness.

## Primitive-normal divisor algebra, reconstructed

For a real PA function \(a\) and a real balanced \(k\)-cycle \(z\), set
\[
 (a\cdot z)(\tau)=\sum_{\sigma\succ\tau}z(\sigma)a_{\sigma,\mathrm{lin}}(n_{\sigma/\tau})
 -a_{\tau,\mathrm{lin}}\left(\sum_{\sigma\succ\tau}z(\sigma)n_{\sigma/\tau}\right). \tag{4}
\]
The second sum is tangential by balancing. Changing a normal lift adds a tangent vector on which the two affine linear parts agree, so the change cancels. The formula is bilinear over \(\mathbb R\), uses only incident germs, and is local on ordinary opens. An ambient affine function has zero divisor on a balanced cycle.

Here are proofs of refinement, balancing, and commutativity, so no intersection-theory theorem is being silently imported. At a new \((k-1)\)-face of a refinement, take its minimal old face. If that face has dimension at least \(k+1\), no inherited \(k\)-weight is present. If it has dimension \(k\), precisely two inherited \(k\)-pieces meet, with equal weight and linear part and opposite primitive quotient normals; their contributions cancel. If it has dimension \(k-1\), its tangent lattice and incident primitive normal classes are the old ones, so (4) is unchanged. These are the only possibilities. The same cancellation preserves inherited balancing.

For balancing of the divisor and commutativity, fix a \((k-2)\)-face, quotient its saturated tangent lattice, and subtract ambient extensions of each function's common tangential linear part. Normal classes and (4) descend. Quotient tangent lattices remain saturated: if a multiple of a quotient class is in a rational tangent subspace, the class itself is in that subspace. Cut by rational hyperplanes, if necessary, to make the local two-dimensional cones pointed. A two-cone with primitive boundary rays \(r,s\) has saturated plane lattice \(N_C\) and index
\[
 \chi_{rs}=[N_C:\mathbb Zr+\mathbb Zs].
\]
Extending \(r\) to a basis of \(N_C\) proves that the primitive inward normal modulo \(\mathbb Rr\) is represented by \(s/\chi_{rs}\). With cone weight \(\omega_{rs}\), balancing at \(r\) is
\[
 \sum_{C_{rs}\succ r}(\omega_{rs}/\chi_{rs})s=t_r r.
\]
The first divisor's ray coefficient is therefore
\[
 D_a(r)=\sum_{C_{rs}\succ r}(\omega_{rs}/\chi_{rs})a(s)-t_ra(r). \tag{5}
\]
Its balancing vector is zero: after substituting the equation for \(t_rr\), each unordered two-cone contributes equal opposite terms \((\omega_{rs}/\chi_{rs})(a(s)r+a(r)s)\). Its subsequent divisor by \(b\) at the quotient origin is
\[
 \sum_{\{r,s\}}(\omega_{rs}/\chi_{rs})[a(s)b(r)+a(r)b(s)]
                      -\sum_r t_ra(r)b(r),                          \tag{6}
\]
which is symmetric. This proves balancing and commutativity in all germs, including lower-face contributions and real coefficients. Refinement already proved that the rational cuts used in the argument change nothing. These identities define the complete recursive operator on every finite rational structure.

For a direct product lattice, a primitive normal of a factor remains primitive in its corresponding product quotient. A factor-pulled-back function has divisor its factor divisor times the other cycle; this follows directly from (4), since the other-factor affine part is zero. In particular, if \(a\) and \(b\) are graph functions and \(D_a,D_b\) their graph divisors, then
\[
 (a+b)^2\cdot[G_1\times G_2]=2D_a\times D_b.                  \tag{7}
\]
The two square terms vanish because a graph cannot support a second divisor. The coefficient 2 is the dimension-two factorial. In dimension \(d\), the lattice-coordinate test \(\sum_{i=1}^d|s_i|\) on weight \(w\) has top coefficient \(2^d d!w\), by expansion and commutativity: only monomials with each coordinate once survive. We never divide by \(d!\).

## PA PC implies PAPC for all real local tests

Let \(a\) be continuous, PC for the actual PCCs, and PA on a finite rational structure. Fix a nonnegative local real \(k\)-cycle on an ordinary open \(U\), and refine its structure together with that of \(a\). At a tested facet \(\tau\), the cone of incident nonnegative weight vectors balanced modulo \(N_\tau\) is defined by rational homogeneous equations and coordinate inequalities. Its section \(\sum c_\sigma=1\) is a bounded rational polytope; hence it is generated by rational vectors. For completeness, a bounded polytope is the convex hull of its vertices: a line through a nonvertex in its minimal face meets smaller-dimensional faces at both ends; induction reduces to vertices. Vertices solve full-rank rational equations and are rational. Thus it suffices to test a nonnegative rational incident vector \((c_\sigma)\), because the divisor coefficient is linear in those weights.

Choose rational \(x\in U\cap\operatorname{relint}\tau\), put
\[
 S=\sum c_\sigma>0,\qquad B=\sum c_\sigma n_{\sigma/\tau}\in N_{\tau,\mathbb Q}.
\]
For small positive rational \(\eta\), the rational points
\[
 x_\sigma=x+\eta(n_{\sigma/\tau}-B/S)
\]
belong to their respective \(\sigma\cap U\). Their quotient directions are inward, while the tangent correction stays inside the facet locally. Their weighted barycentre, using \(c_\sigma/S\), is \(x\). This is a genuine PCC on the common rational structure. Its inequality gives
\[
 0\leq\sum c_\sigma[a(x_\sigma)-a(x)]
 =\eta\left(\sum c_\sigma a_\sigma(n_{\sigma/\tau})-a_\tau(B)\right).
\]
The right side is exactly \(\eta(a\cdot z)(\tau)\). The case \(S=0\) is zero. Rational generation proves the test for every real incident vector, hence every nonnegative real cycle of every positive dimension. Ordinary-open locality follows from the same local formula, not from a PC gluing theorem. Balancing above permits iteration, and every successive cycle of a PAPC function is nonnegative.

## The finite generator-contact certificate

**Proposition.** Let \(X\) be a pure \(d\)-dimensional balanced rational polyhedral space with a finite structure. Let \(\gamma\) be real PA, PC, and positive at infinity. Suppose \(H\) is continuous, real PA and actual PC, with \(H-\gamma\) bounded. Let \(\Pi\) be a finite rational structure on which \(H\) and \([X]\) are affine/constant and every cell is pointed (has no nonzero lineality). If a bounded real-PA obstacle \(u\), on any finite rational spatial structure, has \(f=\gamma+u\) with
\[
 f\geq H\text{ on }X,\qquad f(v)=H(v)\quad(v\in\Pi^{(0)}),       \tag{8}
\]
then the actual raw envelope is \(P_\gamma(u)=H\). It belongs to the real PAPC and regularizable classes in the exact reference growth class, and
\[
 (H-f)\,H^d\cdot[X]=0,\qquad\int_X(H-f)\,\operatorname{MA}_{\mathrm{poly},\mathbb R}(H)=0. \tag{9}
\]
This statement also holds for merely bounded continuous \(f-H\geq0\) satisfying (8). The finite rational domains are required only for the PA version of the obstacle and the constructed operator domain.

We first prove the elementary spatial fact needed for the raw upper comparison. Every nonempty pointed rational polyhedron \(\sigma\) is
\[
 \sigma=\operatorname{conv}(V_\sigma)+\operatorname{cone}(R_\sigma), \tag{10}
\]
where \(V_\sigma\) is its finite nonempty rational vertex set and \(R_\sigma\) is a finite set of rational recession generators. Indeed write the polyhedron in its rational affine hull as \(Ax\leq b\). Its homogenization \(t\geq0, Ax\leq tb\) is a pointed rational cone. Opposite nonzero rays could only have \(t=0\), giving a lineality direction of \(\sigma\), which was excluded. A pointed cone defined by forms \(L_i\geq0\) has the strictly positive rational form \(\sum L_i\) on every nonzero cone point: if all forms vanish there, both signs are in the cone. Its value-one section is bounded (an unbounded sequence normalized to the unit sphere would produce a nonzero cone vector with value zero). By the bounded-polytope argument just given it is generated by finitely many rational vertices. These yield finitely many rational extreme rays of the cone. A ray with \(t>0\), normalized to \(t=1\), gives a vertex of \(\sigma\): a nontrivial convex decomposition of that point would decompose its extreme cone ray. A ray with \(t=0\) gives a recession generator. Intersecting the resulting cone decomposition with \(t=1\) proves (10), including nonemptiness of the vertex set.

Fix a raw competitor \(q\) in (3). There is a finite constant \(M\geq0\) with \(q\leq H+M\), since \(H-\gamma\) is bounded. At every \(v\in V_\sigma\subset\Pi^{(0)}\), (8) gives \(q(v)\leq H(v)\). Let \(x\in\sigma\) be any point, including an irrational centre. Write
\[
 x=\sum_i\lambda_i v_i+\sum_j\mu_j r_j,
 \quad \lambda_i,\mu_j\geq0,\quad\sum_i\lambda_i=1.             \tag{11}
\]
Coefficients in (11) may be real. Choose one vertex \(v_*\) with \(\lambda_*>0\). For a sufficiently large positive integer \(R\), replace a total coefficient \(\sum_j\mu_j/R\) of that vertex by endpoints \(v_*+Rr_j\) with respective coefficients \(\mu_j/R\). All coefficients remain nonnegative, sum to one, and have exactly the same barycentre \(x\). All endpoints are rational and belong to \(\sigma\). Taking \(\tau=\sigma_i=\sigma\) gives an actual same-cell PCC; its centre need not be rational and no raw continuity is needed. Because \(H\) is affine on \(\sigma\), its exact Jensen sum is \(H(x)\). Hence
\[
 q(x)\leq H(x)+M\sum_j\mu_j/R.
\]
Let \(R\to\infty\). If there are no ray terms the same conclusion follows immediately using the vertices alone. Thus \(q\leq H\) everywhere. This proof retains remote rational ray endpoints and works in cells of every dimension. It uses one permitted structure for the upper comparison; every competitor, by definition, satisfies its PCCs.

Conversely \(H\) satisfies every actual PCC on every permitted structure by hypothesis, lies below \(f\), and has the required upper growth. It is therefore a global competitor. Both comparisons prove exact raw equality, not merely a finite LP or a local envelope identity.

The preceding real-cycle argument makes \(H\) PAPC. The functions \(H+1/j\) are PAPC in the same two-sided growth class and decrease uniformly to \(H\); constants have zero divisor. Their full recursive measures equal \(H^d\cdot[X]\). Thus the regularization/operator domain is actual. Recursion on \(\Pi\) puts the top zero-cycle on its finite vertices, where (8) makes the integrand zero. Refining \(\Pi\) together with the obstacle introduces no extra coefficients by the proved refinement formula. This proves (9), including all lower-face terms. No limiting boundary mass is created: this is the finite PA measure on \(X\), and its explicit approximant measures are identical. The integrand is bounded by the prescribed bounded differences.

Pointedness is automatic on a common affine structure for \(H\) and the positive-growth reference: a nonzero lineality direction would give both opposite recession vectors for an affine reference, contradicting its two strictly positive slopes. Subdividing that structure preserves pointedness. This observation does not locate the vertices of the unknown envelope for arbitrary obstacles, which is the certificate's key limitation.

References with bounded real-PA difference can be exchanged in this proposition without a source theorem: their upper growth conditions define the same competitor set, and the fixed obstacle \(f\) is unchanged. The proposition's hypotheses must still be checked for the new reference. In particular a bounded shift alone is not asserted to preserve PC or positive growth without those hypotheses.

**Finite PCC witness variant.** The same raw equality and regularization hold if a noncontact vertex \(v\) in (8) instead has an actual PCC
\[
 (v,(x_i),(\alpha_i)),\qquad f(x_i)=H(x_i),\qquad
                         H(v)=\sum_i\alpha_i H(x_i).          \tag{24}
\]
Indeed raw Jensen gives \(q(v)\leq\sum_i\alpha_i q(x_i)\leq H(v)\). This is precisely the vertex bound used in (11), so the remaining raw proof is unchanged. More generally a finite acyclic network of such tight PCCs propagates vertex bounds from contact points by induction; only the single-level version is needed below. This variant does **not** assert contact automatically: its exact integral is the finite sum
\[
 \sum_{v\in\Pi^{(0)}}(H(v)-f(v))\,(H^d\cdot[X])(v).           \tag{25}
\]
Thus it proves orthogonality if each noncontact vertex has zero full recursive coefficient, and would certify a strictly negative integral if any such coefficient were positive. The coefficients must be computed or proved, rather than assumed from total mass. This distinction also prevents the certificate from concealing a possible actual-contact obstruction on other balanced spaces.

## The actual triangular graph and product

Take \(A=(0,0)\), \(B=(1,0)\), \(C=(0,1)\). The three bounded primitive oriented directions \((1,0),(-1,1),(0,-1)\) all have primitive length one. The leaves from \(A,B,C\) have directions \((-1,-1),(2,-1),(-1,2)\). All six edges have weight one. At the three vertices the outgoing direction lists are
\[
 \begin{array}{c|ccc|ccc|c}
 V&\multicolumn{3}{c|}{\text{outgoing directions}}&\multicolumn{3}{c|}{\text{outgoing slopes of }g}&\kappa_V\\
 A&(1,0)&(0,1)&(-1,-1)&1&1&2&4\\
 B&(-1,0)&(-1,1)&(2,-1)&-1&0&3&2\\
 C&(0,-1)&(1,-1)&(-1,2)&-1&0&3&2.
 \end{array}                                                     \tag{12}
\]
In each row the directions sum to zero and have rank two. Consequently the full kernel is the unit-weight ray; its nonnegative part is exactly that ray. Each star contains a pair with determinant \(\pm1\), and each listed vector has coprime coordinates. Thus the actual primitive directions and saturated tangent lattices meet the assignment; no ray-generated lattice is substituted. The graph has the required bounded cycle. The product uses \(\mathbb Z^2\oplus\mathbb Z^2\), with unit product weights. Its top cell lattice is generated by the primitive direction from each factor and is the actual saturated direct product lattice. The balancing of each factor proves product balancing at every facet by the split normals in (4).

The function \(g=|x|+|y|\) is affine on each of the six original graph edges. On \(AB,AC\) it is distance from \(A\), on \(BC\) it equals one, and on the three leaves it is respectively \(2t,1+3t,1+3t\). The reference in (1) is a restriction of an ambient convex function and therefore satisfies every actual PCC by ordinary Jensen, regardless of endpoint location or centre rationality. Its slope on a product recession vector is a nonnegative linear combination of the strictly positive end slopes \(2,3,3\) in the two factors, multiplied by \(c>0\). A nonzero recession vector has some positive coefficient, so the reference is positive at infinity. All mixed end directions are included.

The candidate \(H\) is also the restriction of an ambient convex function: the maximum of the convex ambient \(c(\|p\|_1+\|q\|_1)\) and the constant \(cr\). Ordinary Jensen proves every actual PCC, including real centres and remote rational endpoints, on every permitted structure. Also
\[
 0\leq H-\gamma\leq cr.                                      \tag{13}
\]
Its structure is the original product structure cut by \(g(p)+g(q)=r\) where relevant. On each product cell that equation has **rational** coefficients, independent of \(c\), because \(r\) is rational. The cuts glue on product boundaries. Only the nine products of the three A-incident edges are cut. In primitive coordinates their cut lines are \(a_is+b_jt=r\), with \(a_i,b_j\in\{1,1,2\}\). These bounded triangles/trapezoids or unbounded remainders have no new interior vertices. The candidate structure's fifteen vertices are the original nine pairs of \(A,B,C\), and
\[
 (A,Q_j),\ (Q_j,A),\quad
 Q_1=A+r(1,0),\quad Q_2=A+r(0,1),\quad Q_3=A+(r/2)(-1,-1).     \tag{14}
\]
All coordinates are rational; all cells are pointed. Thus finite rational spatial domains have been proved directly, without any assertion about arbitrary maxima of real affine functions.

On \(BC\times BC\), let \(s,t\in[0,1]\) be the oriented primitive distances from \(B\) along the two copies of \(BC\), and set
\[
 T(s,t)=\min\{s,1-s,t,1-t\};\qquad T=0\text{ on the other product cells}. \tag{15}
\]
This extension is continuous, since the tent is zero on the entire boundary of the rectangle. Its four affine domains are the rational triangles joining the rectangle edges to its centre. It is bounded between zero and \(1/2\). The function \(S\) in (1) is bounded between zero and \(r\); its domains use precisely the rational candidate cut. Both added functions vanish at every candidate vertex except \((A,A)\), where \(S=r\). Thus \(f(A,A)-H(A,A)=\eta r>0\).

The three endpoints \((Q_1,A),(Q_2,A),(Q_3,A)\), with weights \((1/4,1/4,1/2)\), have barycentre \((A,A)\). Their first-factor displacements are \(r(1,0),r(0,1),-(r/2)(1,1)\), whose weighted sum is exactly zero. They belong to the three closed flat edges incident to the vertex \((A,A)\) of the rational candidate structure. This is an actual PCC with rational endpoints and real coefficients, using the vertex as \(\tau\) and those flat edges as its cofaces. At all three endpoints \(f=H=cr\), and \(H(A,A)=cr\), so (24) is tight. The finite PCC witness variant proves actual raw equality and uniform regularization, even though the product junction is noncontact. Its zero recursive coefficient is computed below, giving (2). No local modification or global gluing is assumed.

The obstacle has finite rational domains, and
\[
 u=(c+\eta)S+\varepsilon T,\qquad
              0\leq u\leq(c+\eta)r+\varepsilon/2.            \tag{16}
\]

These functions are genuinely nonseparable. On the small \(AB\times AB\) rectangle with corners \(A,Q_1\) in each factor, the mixed difference of \(H\) is
\[
 H(Q_1,Q_1)-H(Q_1,A)-H(A,Q_1)+H(A,A)=cr>0.
\]
On \(BC\times BC\), the mixed difference of \(u\), at factor parameters \(0,1/2\), is \(\varepsilon/2>0\). An additive sum of one-factor functions has zero mixed difference. Moreover, \(f\) at the centre of the \(BC\times BC\) rectangle is \(2c+\varepsilon/2\), while at its four corners it is \(2c\). The centre is a rational same-cell PCC of those four corners, so \(f\) is not PC. We have an actual envelope strictly below the obstacle on an open subset, and strictly above the reference near \((A,A)\).

## Complete recursive coefficients, not just top-face masses

At an original pair \((V,W)\ne(A,A)\), \(g(V)+g(W)\geq1>r\), so \(H=\gamma\) in a neighborhood. Write the local first-factor primitive rays as \(u_i\) with slopes \(a_i\), and the second-factor rays as \(v_j\) with slopes \(b_j\). The germ after subtracting its value is \(c(a_is+b_jt)\) in each quadrant. All original product-quadrant plane indices are one. Formula (4) gives first-divisor coefficient \(c\kappa_W\) on each first-factor ray, and \(c\kappa_V\) on each second-factor ray. These first-divisor rays are balanced. Applying (4) again gives
\[
 \operatorname{MA}(H)\{(V,W)\}
 =c^2\kappa_W\sum_i a_i+c^2\kappa_V\sum_j b_j
 =2c^2\kappa_V\kappa_W.                                     \tag{17}
\]
This includes bounded-cycle junctions with negative individual slopes at \(B,C\); the sums in (12) remain positive. At \((A,A)\), \(H=cr\) in a whole neighborhood, so every first and second coefficient is zero.

At \((A,Q_j)\), the second graph is locally an actual primitive line through an interior edge point. Give it primitive coordinate \(\zeta\), positive in the direction away from \(A\), and slope \(b=b_j\in\{1,1,2\}\). In the first factor use the three primitive A-rays \(u_i\) and slopes \(a_i=(1,1,2)\). The exact germ after subtracting \(cr\) is
\[
 K_i(s,\zeta)=c\max\{a_i s+b\zeta,0\},\qquad s\geq0.          \tag{18}
\]
The carrier is the entire three-ray star times the complete local line. In each saturated branch plane, let \(z=(0,1)\), \(h_i=(u_i,0)\), \(d_i=\gcd(a_i,b)\), and
\[
 R_i=(b/d_i)h_i-(a_i/d_i)z.                                 \tag{19}
\]
The primitive rays, in cyclic half-plane order, are \(-z,R_i,h_i,z\). The cones \((-z,R_i)\), \((R_i,h_i)\), \((h_i,z)\) have respective **actual indices**
\[
 b/d_i,\quad a_i/d_i,\quad1.                                \tag{20}
\]
Every cone has inherited weight one. In particular, for \(b=2,a_i=1\), the first index is two; for \(b=1,a_i=2\), the second index is two. The plane lattice is \(\mathbb Zh_i\oplus\mathbb Zz\), which is saturated in the direct product ambient lattice. Formula (20) therefore measures the actual index, rather than an artificial fan-coordinate determinant.

Here is every nonzero first-divisor coefficient from (5), retaining also the zero faces:
\[
 D_K(R_i)=c d_i,\quad D_K(z)=4c,\quad
 D_K(-z)=0,\quad D_K(h_i)=0.                                \tag{21}
\]
For verification, \(K(-z)=K(R_i)=0\), \(K(h_i)=ca_i\), \(K(z)=cb\). At \(R_i\), the neighbor sum is
\[
 (d_i/b)(-z)+(d_i/a_i)h_i=(d_i^2/(a_ib))R_i;
\]
since \(K(R_i)=0\), (5) gives \((d_i/a_i)ca_i=cd_i\). At \(h_i\), its neighbor sum is
\[
 (d_i/a_i)R_i+z=(b/a_i)h_i,
\]
giving \(cb-(b/a_i)ca_i=0\). At \(z\), the incident opposite boundary rays are the \(h_i\), so their sum is zero by actual graph balancing and the coefficient is \(c\sum a_i=4c\). At \(-z\), the sum of neighbors weighted by inverse indices is
\[
 \sum_i(d_i/b)R_i=\sum_i h_i-(4/b)z=(4/b)(-z),
\]
and all function values involved are zero. These are all faces of the local fan. The first divisor balances exactly:
\[
 \sum_i cd_iR_i+4cz=cb\sum_i h_i=0.
\]
The second divisor consequently has coefficient
\[
 \sum_i cd_iK(R_i)+4cK(z)=4c^2b.                            \tag{22}
\]
It is zero on the inactive and artificial rays; no intermediate term is omitted. Interchanging the factors proves the identical coefficient at \((Q_j,A)\). This use of symmetry is justified by (6) and the actual identical factor lattices, not by an assumed factorized Monge--Ampère formula for a nonseparable function.

There are no other possible nonzero top coefficients. The structure described before (14) has exactly its fifteen vertices; a finite recursive zero-cycle on that structure has support there. The common structure with the explicit tent adds just one vertex \((M,M)\), where \(M=(1/2,1/2)\in BC\). In a whole neighborhood of that point \(H=2c\), so its complete recursive coefficient is zero. At any point in the interior of a cut segment, the coarsest local carrier and function-domain fans share the line along that segment; every face contains that line and no zero-dimensional face exists. Equivalently recursion on the unrefined structure already excludes that point. Refinement invariance handles every artificial vertex and every edge fibre. Unbounded remainder cells and all thirty-six original products of graph edges have been included; there is no end or boundary atom in the finite PA operator or its constant-shift approximation.

The exhaustive coefficient table, valid for every \(c,r,\eta,\varepsilon\) in the stated ranges, is

| Point(s) | Number | \(H\) | \(f-H\) | Mass at each |
|---|---:|---:|---:|---:|
| \((A,A)\) | 1 | \(cr\) | \(\eta r\) | 0 |
| One factor \(A\), other \(B\) or \(C\) | 4 | \(c\) | 0 | \(16c^2\) |
| Each factor \(B\) or \(C\) | 4 | \(2c\) | 0 | \(8c^2\) |
| One factor \(A\), other \(Q_1\) or \(Q_2\) | 4 | \(cr\) | 0 | \(4c^2\) |
| One factor \(A\), other \(Q_3\) | 2 | \(cr\) | 0 | \(8c^2\) |
| \((M,M)\), from the obstacle refinement | 1 | \(2c\) | \(\varepsilon/2\) | 0 |

Thus all sixteen tested coefficients have been identified; fourteen are positive. The complete integral is zero, including the actual noncontact product junction \((A,A)\), the bounded-rectangle point \((M,M)\), and their open lift regions. The total mass is
\[
 4(16c^2)+4(8c^2)+4(4c^2)+2(8c^2)=128c^2.                  \tag{23}
\]
Independently, (12) gives factor degree \(8\), and direct expansion (7) gives the reference mass \(2(c\,8)^2=128c^2\). Mass agreement is a consistency check; the contact conclusion follows from every coefficient and the generator-contact proof, not from mass agreement.

For a larger obstacle family, replace \(\eta S+\varepsilon T\) by any bounded nonnegative real-PA \(b\) on finite rational domains with \(b=0\) at the candidate structure's fourteen vertices other than \((A,A)\). No restriction on \(b(A,A)\) is needed: the same three-endpoint PCC bounds every raw competitor there. The witness variant still gives \(P=H\); (17)--(23) still give its complete measure. That measure is supported at the fourteen imposed contact vertices, so the integral remains zero even when \(b\) is nonseparable and has many additional rational domain vertices. Replace \(\gamma\) as well by any PC positive-growth real-PA \(\widetilde\gamma\) with \(\widetilde\gamma-\gamma\) bounded, and use \(u=H+b-\widetilde\gamma\). The competitor set and the explicit bounded-growth check are unchanged. These extensions remain restricted by the imposed fourteen contacts.

## Exact execution evidence

`two_graph_example.py` independently evaluates (5) in the actual ambient \(\mathbb Z^4\), constructs every branch cone with its plane index, computes its tangential neighbor sum, verifies first-cycle balancing, and applies the second divisor. It uses `fractions.Fraction`, not floating point. `example-input.json` fixes \(c=1,r=1/2,\eta=\varepsilon=1\). Its output `two-graph-output.json` records sixteen tested points, fourteen positive atoms, zero negative first-divisor weights, maximum cone index two, total mass 128, complete contact integral zero, and zero coefficients at both noncontact tested points. It also records the concrete coordinates of every point, the tight product-junction PCC, first-divisor ray weights, and the two nonzero mixed differences. These are exhaustive finite results for the described PA candidate after the separate mathematical spatial-coverage proof. Execution does not prove envelope equality or the universal theorem.

The same program records the elementary failed interpolation diagnostic on the actual \(AB\times AB\) rectangle: the bilinear interpolation \(s t\) takes value \(1/4\) at the rational centre \((1/2,1/2)\), while its values at rational endpoints \((0,1),(1,0)\) are both zero. This is a same-cell PCC violation, so bilinear interpolation of feasible corner values is not a valid global upper construction. This diagnostic is not itself a PA function, an actual envelope, a contact obstruction, or a regularity-failure proof.

## Unresolved obligations and failed routes

1. **Global raw upper/lower construction for arbitrary data.** The certificate prescribes obstacle contact at already known candidate generators. For an arbitrary \(f=\gamma+u\), neither the candidate nor its spatial vertices are known, and (8) need not hold. Identifying a finite list of original product nodes does not bound all actual product PCCs. An unknown raw PC competitor is not assumed continuous.
2. **Product rectangles and junction fibres.** One graph's endpoint chord is canonical. On a rectangle, bilinear interpolation fails actual PCCs as just shown. A lower convex roof of corner values repairs that particular interior inequality, but has not been proved compatible across both graph junction systems, arbitrary oblique obstacle domains, all remote PCC endpoints, or cycles. No general greatest feasible product-node assignment theorem is asserted.
3. **Partial infima and global convex lifts.** An affine fibre admits supporting covectors and the cylinder proof's exact Legendre reconstruction. A cyclic graph is not a complete affine space. Replacing it by an ambient dual loses the required global admissibility argument; its bounded-edge periods and remote endpoint constraints persist. Ordinary infima over two fixed Cartesian index sets commute as infima, but this elementary fact says nothing about fibre envelope operations, support feasibility, or joint PC reconstruction. No commuting-envelope theorem is used.
4. **Rational regularization.** A maximum of arbitrary real affine values can have irrational equality walls. The rational walls proved in (14)--(15) come from this family's explicit rational level \(r\) and tent. They do not prove finite rational spatial domains for an arbitrary product envelope, or uniform PAPC regularization if its domains are not finite/rational.
5. **Universal contact.** The complete recursion was checked for this actual candidate, including junction cuts and index-two cones. It does not show that a positive top coefficient of every unknown envelope at every product junction forces obstacle contact. A local PA modification has not been shown to glue to a global actual PC competitor for arbitrary product data. Neither total mass nor rank-one cones by themselves fill this gap.
6. **Counterexamples.** No negative integral has been obtained. A failed reconstruction, a numerical LP, a single apparent noncontact atom, or a regularity-failure alternative would not meet the task's actual-contact counterexample requirement. The example here has an exactly zero complete integral.

The universal target was investigated through the finite-roof route, but no load-bearing global extension theorem emerged. The generator-contact proposition and exact cyclic example are retained as partial mathematical findings, with their extra hypotheses stated. No paper asserting an all-obstacle product theorem has been manufactured.

## Artifacts, rerun commands, and verification limits

All new files are in the assigned fresh workspace. `snapshot_sources.py` makes read-only source snapshots and records `source-hashes.json`, exact newline excerpts, and `environment.json`. `two_graph_example.py` uses `example-input.json` and writes `two-graph-output.json`. `assemble_notes.py` writes the retained local `result-notes.json`. `build.py` renders this entire authoritative argument into standalone `P05.2-partial.tex`, compiles `P05.2-partial.pdf` twice, retains both logs and stdout files, and records `build-evidence.json` and PDF text checks. This is a partial working note, not a claim of the requested universal theorem. `status.json` has exactly the requested five keys. `author-self-audit.md` and `research-notes.md` record proof scope, limitations, and failed routes. `artifact-hashes.json` is a reproducibility manifest.

Rerun from this directory:

```sh
python3 snapshot_sources.py
python3 two_graph_example.py
python3 assemble_notes.py
python3 build.py
```

The first command requires the recorded read-only source paths; the proof and numerical example can be checked independently of those snapshots. No additional model call, subagent, external message, network call, installation, old-artifact write, authentication change, SQL action, or heavy computation was used. No operator-provided supervised heavy-compute facility was found in exposed metadata; none was needed. All computation was small exact arithmetic and document compilation. Source hashes, successful execution, PDF compilation, and this author audit do not establish mathematical correctness. These are unverified proof drafts.

Bibliography: BMPS, arXiv:2603.08664v1 (definitions listed above, proof bodies inspected for scope only); the controlling Chapter 72 and Appendix M (scope only); prior round-10 graph-cylinder argument and actual committed notes (comparison only). No essential external mathematical theorem is invoked without reconstruction in this note.



# Complete supporting proofs supplied for independent reconstruction

These are mathematical evidence, not grants of assumptions. Each application and dependency must be reconstructed. Prior verdicts and hashes do not replace these proofs.
