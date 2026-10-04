# Exact new geometric scope and remaining original obligations

{
  "id": "P03.3",
  "status": "partial",
  "exact_result": "Every finite continuous obstacle has a continuous raw and regularized full local-Fubini--Study/semipositive-real-PL envelope on the displayed compact strict rational curve affinoids over a complete algebraically closed nontrivially valued field and on their products with analytic projective space; exact compatibility for every analytic scalar extension of each obstacle. The split node and its projective products give a freshly proved full-family discontinuity obstruction.",
  "proof_file": "P03.3-argument.md",
  "concrete_gaps": [
    "No sharp necessary-and-sufficient classification of good strict analytic domains.",
    "No theorem for every normal or geometrically unibranch higher-dimensional domain.",
    "No continuity theorem for the entire perfected-unibranch curve range or arbitrary obstacles over nonalgebraically closed base fields.",
    "General semistable affinoid graph realization/global cofinality beyond the explicit rational trees is not proved.",
    "Nonsplit and codimension-two singularities and general necessity remain unclassified.",
    "Projective-space products are covered; closed-polydisc products and arbitrary proper factors are not covered."
  ]
}

# Entire final proof

# Full obstacle envelopes on strict rational curves and their projective products

This is a partial result for P03.3, not its sharp geometric classification. The positive theorem concerns every finite continuous obstacle, without an invariance restriction, on the concrete domains below. Its proof bounds the entire locally Fubini--Study/semipositive real-PL competitor union. It also gives exact compatibility for every analytic extension of the field. A separate split-node construction proves a necessary exclusion by a fresh full-family calculation. No supplied book assertion or review verdict is used as a proof.

## 1. Conventions and checked foundations

All spaces are Berkovich analytic spaces. A field is complete and its non-Archimedean valuation is nontrivial. For a good strict space \(Y\), write
\[
\begin{aligned}
\mathcal E_Y(f)&=\{h:Y\longrightarrow\mathbb R:h\leq f,\\
&\hspace{2em}h\text{ is locally Fubini--Study or semipositive real PL}\},\\
E_Yf&=\sup_{h\in\mathcal E_Y(f)}h.
\end{aligned}
\]
The regularization is with respect to the ordinary topology:
\[
(E_Yf)^*(y)=\inf_{W\ni y}\sup_{z\in W}E_Yf(z).
\]
Competitors are globally defined functions satisfying the displayed local conditions, rather than germs chosen independently at each point. Real PL means G-locally a finite real linear combination of logarithms of analytic units on strictly analytic domains. These functions are continuous. The source definition of locally Fubini--Study (LFS) is an R-PL function whose residue line bundle is semiample at every point. Semiample implies nef, so LFS functions are semipositive real PL. Consequently the displayed union equals the full semipositive real-PL class. We retain both names because our constructed global minorants are actually LFS.

The following published foundations are used, with their hypotheses and relevant bodies retained separately. Labels refer to the sources listed in Section 11.

GJR, Definition 5.1, Remarks 5.2 and Lemma 5.4, give continuity and functoriality of real-PL functions. GJR, Definition 7.8 and paragraph 7.9, give the following precise LFS presentation on an ordinary open neighbourhood:
\[
h=\sum_j\lambda_j\max_i\{-\log|u_{ji}|\},
\qquad \lambda_j\geq0,\quad u_{ji}\in\mathcal O^\times.
\]
We verify both invertibility and strict real-PL membership whenever we use this presentation. In particular, arbitrary maxima of real-PL functions are not assumed real PL: GJR, Example 5.3, explicitly disproves that closure property.

GJR, Proposition 7.6, gives semipositivity under analytic pullback and every analytic scalar extension. GR2, Theorem 4.3, states that for a good strictly analytic space over a nontrivially valued field a real-PL function is semipositive if and only if it is classically psh. GR2, Definitions 3.4 and 4.1 and Proposition 4.2, quantify over every analytic field extension and curve morphism; they give logarithms, positive sums, maxima, and pullbacks of classically psh functions. GR2, Theorems 6.1 and 6.4, give respectively the local maximum principle on the relative interior and the maximum on the Shilov boundary of an affinoid. Our uses of these principles are for finite continuous functions.

For clarity, harmonic comparison below follows from those foundations: if \(h\) is classically psh on an affinoid \(A\), and \(H\) is a real linear combination of logarithms of units on \(A\), then \(H\) and \(-H\) are classically psh. Thus \(h-H\) is classically psh, and domination on the Shilov boundary implies domination on \(A\). This agrees with Thuillier, Definition 3.1.5; no theorem about regularization of arbitrary suprema is used.

GR2, Section 2.9, gives closed surjective scalar projection. Ber93, Proposition 2.6.9, gives properness under analytification; Definition 3.5.1 and Proposition 3.5.2, and Corollary 3.7.4, give relative smoothness, its stability, and openness of smooth morphisms. Relative boundary here is the analytic relative boundary, not an affinoid's ordinary topological boundary as an abstract compact space. The old word "closed" in Ber93's relative-boundary definitions means boundaryless; it is distinguished from a topologically closed map. Proper maps in our applications are also topologically closed.

## 2. The sufficient geometric sector

Let \(K\) be algebraically closed. Choose \(a_0,a_1,\ldots,a_m\in K\) and \(R,r_1,\ldots,r_m\in|K^\times|\), with \(R>0\), such that
\[
0<r_i<R,\qquad |a_i-a_0|<R,\qquad
|a_i-a_j|>\max(r_i,r_j)\quad(i\ne j).
\]
Set
\[
D=\{|T-a_0|\leq R\}\setminus\bigcup_{i=1}^m\{|T-a_i|<r_i\}
\subset\mathbb P^{1,\mathrm{an}}_K.
\]
The case \(m=0\) is a closed strict disc. These are actual compact strict rational affinoids: after scaling the outer disc, the inequalities are rational-domain inequalities with constants in \(K^\times\). They are connected, good and separated. Their analytic boundary and Shilov boundary are
\[
B=\{o,b_1,\ldots,b_m\},\qquad
o=\xi_{a_0,R},\quad b_i=\xi_{a_i,r_i},
\]
where \(\xi_{a,r}\) is the Gauss point of the closed disc of centre \(a\) and radius \(r\). Here is also a verification of the boundary assertion used for the new comparisons. In the disc topology of GR2, Appendix A, each removed open disc has the single boundary point \(b_i\), and the outer closed disc has the single boundary point \(o\). Thus the ordinary boundary of \(D\) in the boundaryless projective line is exactly \(B\). The analytic-domain interior formula of GR2, Section 2.11, identifies this with its analytic boundary. The tree decomposition in Section 3 proves connectedness. If a finite continuous classically psh function on \(D\) had its maximum locus disjoint from \(B\), that locus would be nonempty and closed by compactness and open by GR2, Theorem 6.1. Connectedness would make it all of \(D\), a contradiction. The same proof applies to \(\log|G|\) for any nonzero analytic \(G\); its finite maximum locus is closed even if it has zeros. Hence \(B\) is a boundary for analytic functions. It is the Shilov boundary: \((T-a_0)/c_0\), with \(|c_0|=R\), uniquely peaks at \(o\) among \(B\), while \(c_i/(T-a_i)\), with \(|c_i|=r_i\), uniquely peaks at \(b_i\) among \(B\). The inequalities on centres and radii give all other listed values strictly smaller. The minimal affinoid boundary is therefore exactly \(B\). This verification applies verbatim to the smaller rational stars, discs and annuli used below.

**Theorem A.** For every \(f\in C(D,\mathbb R)\), the raw full-union envelope \(E_Df\) is finite and continuous; hence \((E_Df)^*=E_Df\). It is a uniform limit of global LFS minorants of \(f\). For every analytic field extension \(F/K\), with scalar projection \(\pi:D_F\to D\),
\[
E_{D_F}(f\circ\pi)=E_Df\circ\pi.
\]
Both sides are continuous. In particular regularization commutes in this formula without assuming scalar projection is open.

**Theorem B.** For every integer \(d\geq0\), let
\[
X=D\times_K\mathbb P^{d,\mathrm{an}}_K,\qquad p:X\to D.
\]
For every finite continuous, arbitrary obstacle \(f\) on \(X\), set
\[
g(x)=\min_{z\in p^{-1}(x)}f(z).
\]
Then \(g\) is finite continuous and
\[
E_Xf=(E_Dg)\circ p=(E_Xf)^*.
\]
This is the full competitor envelope, and it commutes with pullback of \(f\) under every analytic field extension. The domain \(X\) is compact, good, separated and strictly analytic. It has relative boundary \(p^{-1}(B)\), while the fibres of \(p\) are proper and boundaryless. The case \(d\geq1\) supplies a higher-dimensional sufficient sector, with arbitrary noninvariant obstacles.

## 3. Actual finite trees, retractions and density

We recall the elementary disc description over an algebraically closed field: disc points are closed-disc seminorms or limits along nested discs; two discs are nested or disjoint. Their paths are obtained by varying their radii. This includes type-4 points, and is the usual tree description underlying GR2, Appendix A.1--A.2. Along nonterminal paths use length \(|d\log r|\). Between finitely many type-2 disc points one obtains a finite metric tree. A branch point of such a tree has radius \(|a-a'|\), hence is type 2. A type-3 point has only its two path directions. At a type-2 point the other directions are open discs with centres in \(K\); over our algebraically closed field the residual directions are represented by such centres.

Let \(\Gamma\subset D\) be the hull of \(B\) and finitely many additional type-2 points of \(D\). Include every branching point in its vertex set \(V\). Root the tree at \(o\). For \(v=\xi_{a_v,r_v}\in V\setminus\{o\}\), define the analytic function of seminorms
\[
k_v(x)=\log\max\{|T-a_v|(x),r_v\}-\log R.
\]
The disc nesting rule gives the explicit formula
\[
k_v(x)=-\operatorname{length}\bigl([o,x]\cap[o,v]\bigr).
\tag{3.1}
\]
Here the intersection has finite length even when \(x\) is a rigid point of infinite depth. Formula (3.1) follows directly because the radius of the least common containing disc is \(\max\{|T-a_v|(x),r_v\}\). It also holds for nested-disc limits.

The last point of \([o,x]\) belonging to \(\Gamma\) defines \(\tau_\Gamma(x)\). The finitely many coordinates \(k_v\) separate points of \(\Gamma\): for two distinct points choose a terminal vertex whose root path contains the longer segment after their separation. Their overlap lengths with that path differ. Each \(k_v\) is continuous on \(D\), and its value at \(x\) is its value at \(\tau_\Gamma(x)\). The resulting continuous embedding of compact \(\Gamma\) in a finite Euclidean space has continuous inverse on its image. This proves continuity of \(\tau_\Gamma\), rather than assuming an unconstructed skeleton retraction.

Every component of \(D\setminus\Gamma\) is an open disc attached at one point of \(\Gamma\). All removed original discs terminate behind a vertex of \(B\), so no such component contains an unrecorded hole. It is important that an open component plus its attachment is not being called an affinoid. It can be exhausted by smaller closed strict discs; their Gauss points approach its attachment. This is the exhaustion used in Section 5.

For \(a\in K\), \(r\in|K^\times|\), the functions
\[
u_{a,r}(x)=\log\max\{|T-a|(x),r\}
\]
are finite continuous. Together with constants they separate points of \(D\). Indeed a Berkovich point is determined by its seminorm on \(K[T]\); every polynomial factors into linear terms, so two distinct points differ on some \(|T-a|\). Choose a value-group radius below the larger differing value to preserve that difference after truncation. The real Stone--Weierstrass theorem now shows that the algebra generated by the \(u_{a,r}\) is uniformly dense in \(C(D,\mathbb R)\).

Every expression in finitely many of these functions factors through some actual \(\tau_\Gamma\). If a centre is outside the outer disc its coordinate is constant. If its endpoint lies inside a removed open disc, truncate its root path at that hole's boundary; the coordinate on \(D\) is unchanged. Otherwise include its type-2 endpoint in \(\Gamma\). Thus the finite-tree assertion follows from the explicit coordinates, not an assumed semistable realization theorem.

An algebraic expression in those coordinates need not be affine on edges. Its restriction to finite \(\Gamma\) is continuous, and ordinary linear interpolation approximates it uniformly after finite subdivision. The new subdivision points can be chosen type 2: \(\log|K^\times|\) is divisible and nonzero, hence dense in \(\mathbb R\), and radius variation parametrizes every edge. Consequently, for every \(\varepsilon>0\), there is a finite tree as above and a continuous function \(\varphi\), affine on its subdivided edges, such that
\[
F=\varphi\circ\tau_\Gamma,\qquad \|f-F\|_\infty<\varepsilon.
\tag{3.2}
\]
No regularity, invariance or modulus of continuity is imposed on \(f\). We next compute the full envelope of each \(F\).

## 4. A finite graph calculation and its global analytic realization

For adjacent vertices write their edge length as \(\ell_{vw}>0\). A vector \(q=(q_v)_{v\in V}\) is admissible if
\[
q_v\leq\varphi(v)\quad(v\in V),\qquad
\sum_{w\sim v}\frac{q_w-q_v}{\ell_{vw}}\geq0
\quad(v\in V\setminus B).
\tag{4.1}
\]
There is no sign condition at an analytic boundary vertex. A constant below \(\min_V\varphi\) is admissible. Define \(p_v=\sup q_v\) over these vectors. Then
\[
\min_V\varphi\leq p_v\leq\varphi(v).
\]
The coordinatewise maximum of two admissible vectors is admissible: at a vertex choose the vector attaining its maximum there; every neighbouring maximum is at least that vector's neighbouring value. This is a finite vector calculation, not an assertion about the analytic maximum of two real-PL functions. Choosing one almost maximizing vector per vertex and taking their coordinatewise maximum gives a sequence tending to \(p\). The closed linear inequalities (4.1) show that \(p\) itself is admissible and is the greatest admissible vector.

Let \(P\) be its linear interpolation on \(\Gamma\). For \(v\ne o\), put
\[
d_v=\sum_{w\sim v}\frac{p_w-p_v}{\ell_{vw}}.
\]
The sum of outgoing slopes of \(k_v|_\Gamma\) is \(+1\) at \(v\), \(-1\) at \(o\), and zero at every other vertex. This sign follows from (3.1): from \(v\) toward its parent the value increases at rate 1, and from \(o\) toward \(v\) it decreases at rate 1. Hence
\[
Q(x)=p_o+\sum_{v\in V\setminus\{o\}}d_vk_v(x)
=P(\tau_\Gamma(x)).
\tag{4.2}
\]
To verify the equality, subtract its two edge-affine expressions on \(\Gamma\). The outgoing slope sum vanishes at every vertex other than the root and the difference is zero at the root. Successively remove terminal vertices: their edge slope is zero, and the same becomes true on the smaller tree. The difference is identically zero. This proves the formula without invoking a graph-to-model realization theorem.

The function \(Q\) is globally LFS. For an interior vertex, \(d_v\geq0\). The function \(\log\max\{|T-a_v|,r_v\}\) is strict PL: on \(\{|T-a_v|\leq r_v\}\) it is \(\log|c_v|\), with \(|c_v|=r_v\); on \(\{|T-a_v|\geq r_v\}\) it is \(\log|T-a_v|\), where \(T-a_v\) is an analytic unit. These are strict domains covering \(D\). At a point where the two values agree, choose an ordinary open neighbourhood excluding the zero of \(T-a_v\); there it is
\[
\max\{-\log|(T-a_v)^{-1}|,-\log|c_v^{-1}|\}.
\]
At other points it is locally the constant or the logarithm of a unit. This checks the exact LFS presentation, including the signs and units.

For a boundary vertex \(b_i\), \(|T-a_i|\geq r_i\) on all of \(D\), so \(k_{b_i}=\log|T-a_i|-\log R\) is the logarithm of a global unit plus a constant. Its coefficient \(d_{b_i}\) can have either sign; a negative coefficient is written as a positive coefficient of the logarithm of the inverse unit. Such terms are harmonic and LFS. Every real constant is also a real multiple of the logarithm of a nonzero field element of nonunit norm, using its inverse if necessary. Positive sums of the local presentations just verified prove LFS membership of (4.2). In particular \(Q\) is semipositive real PL and classically psh.

Finally, \(P\leq\varphi\) on each edge because both are affine there and the vertex inequalities hold. Thus \(Q\leq F\) on all of \(D\). This is an actual global minorant, with no globalization condition left as a hypothesis.

## 5. Harmonic comparison controls every analytic competitor

Let \(h\in\mathcal E_D(F)\). It is finite continuous and classically psh by Section 1. We prove that \((h(v))_{v\in V}\) satisfies (4.1).

Fix an interior vertex \(v=\xi_{a,r}\). It has one parent neighbour and finitely many child neighbours. Choose type-2 endpoints strictly between \(v\) and each neighbour, at respective distances \(L_+,L_1,\ldots,L_s>0\). They can approach the neighbours along the edges. The star domain around \(v\) is a closed disc with Gauss point the parent endpoint, minus the open child discs whose boundary points are the child endpoints. It is a strict rational affinoid inside the relative interior of \(D\). Indeed all original holes in those directions lie beyond the chosen child endpoints, and any other original hole is cut off through the parent direction. No branch point lies in an open edge.

Write \(t_+,t_1,\ldots,t_s\) for the values of \(h\) at these endpoints, and set
\[
M=\frac{t_+/L_++\sum_jt_j/L_j}{1/L_++\sum_j1/L_j}.
\tag{5.1}
\]
Choose the centres \(a_j\) of the child discs. On the star domain \(T-a_j\) is a unit. The harmonic function
\[
H=C+\sum_{j=1}^s\frac{M-t_j}{L_j}\log|T-a_j|,
\qquad C\text{ chosen so that }H(v)=M,
\tag{5.2}
\]
has value \(t_j\) at the child endpoint: its log-radius decreases there by \(L_j\), and the other child logarithms remain constant. Toward the parent, every child logarithm increases by \(L_+\); equation (5.1) says exactly that the parent value is \(t_+\). For \(s=0\), use the constant harmonic function \(t_+\). The Shilov boundary of this rational star is its listed endpoints. Harmonic comparison gives \(h(v)\leq M\). Letting the endpoints approach the neighbours and using continuity of \(h\) gives
\[
\sum_{w\sim v}\frac{h(w)-h(v)}{\ell_{vw}}\geq0.
\]
This includes an added interior terminal vertex, where it says \(h(v)\leq h(w)\). The obstacle inequality gives the other conditions in (4.1). Thus \(h(v)\leq p_v\).

For a point on an open edge, take closed strict annuli whose endpoints lie inside that edge and tend to its two vertices. These annuli are contained in \(D\): sibling directions at either vertex are avoided by placing the endpoints strictly within the edge. Their harmonic Dirichlet functions are affine in \(\log|T-a|\), the logarithm of a unit on the annulus. Comparison and passage to the limit give
\[
h(x)\leq\text{the affine interpolation of }h\text{ at the edge's vertices}
\leq P(x)\qquad(x\in\Gamma).
\tag{5.3}
\]
This argument also treats edges terminating at analytic boundary vertices by approaching those vertices from inside; no slope sign is imposed there.

If \(x\notin\Gamma\), its attached open disc can be exhausted by smaller closed strict discs containing \(x\). The singleton-Shilov maximum principle bounds \(h(x)\) by the value of \(h\) at their Gauss points. Those Gauss points approach the attachment \(\tau_\Gamma(x)\). Thus
\[
h(x)\leq h(\tau_\Gamma(x))\leq P(\tau_\Gamma(x))=Q(x).
\]
This uses continuity of each competitor, not continuity of their supremum. Combining this upper bound for every member of the exact full union with the global LFS minorant (4.2) proves
\[
E_DF=Q=P\circ\tau_\Gamma.
\tag{5.4}
\]
It also proves equality for the LFS branch alone. All discarded directions and every possible noninvariant competitor have been accounted for by analytic maximum principles.

## 6. Arbitrary continuous obstacles and curve tests

For continuous obstacles on any of our compact domains the family contains a constant below the minimum. Real constant translation preserves both competitor branches. Therefore the envelope is finite, monotone and translation equivariant, and
\[
\|E_Yf-E_Yf'\|_\infty\leq\|f-f'\|_\infty.
\tag{6.1}
\]
This inequality is pointwise algebra of the full families and does not assume envelope continuity.

Choose \(F_n\) as in (3.2), with error \(\varepsilon_n\downarrow0\). Equation (5.4) makes \(Q_n=E_DF_n\) continuous. By (6.1),
\[
\|Q_n-E_Df\|_\infty\leq\varepsilon_n.
\]
Uniform convergence proves continuity. Moreover \(Q_n-\varepsilon_n\) is a global LFS competitor for \(f\), and
\[
\|Q_n-\varepsilon_n-E_Df\|_\infty\leq2\varepsilon_n.
\tag{6.2}
\]
The approximants are not asserted monotone; no unjustified maximum closure of real PL is being used.

Although P03.3 asks for continuity, the curve tests can be checked explicitly. For every analytic extension \(F/K\) and every smooth strict connected analytic curve mapping to \(D_F\), the pullbacks of the LFS functions in (6.2) are subharmonic by the checked foundations and converge uniformly. Given a strict affinoid in that curve and a harmonic function dominating the limit on its finite boundary, it dominates each approximant up to its uniform error. Harmonic comparison passes this domination through the affinoid. Taking the uniform limit proves the curve test. The scalar/curve quantifiers in GR2, Definition 3.4 and paragraph 4.1.3, then give every analytic-curve test, including those phrased using further scalar extensions and normalization. This proves classical positivity here in addition to continuity. No CLD-v2 conclusion or solution of P03.2 is asserted.

## 7. Every analytic scalar extension: analytic equality, not an openness shortcut

For a finite-tree datum \(F=\varphi\circ\tau_\Gamma\), its signed version of formula (4.2), with charges of \(\varphi\), expresses \(F\) using the same finitely many coordinates \(k_v\). Those coordinates pull back literally under every extension, because the defining centres and radii belong to \(K\).

Let \(F'/K\) be an arbitrary analytic extension, and let \(L\) be the completed algebraic closure of \(F'\). The rational domain \(D_L\) has the same displayed centres, holes and boundary Gauss points. Their finite hull \(\Gamma_L\) has the same edge lengths, branching, and charges as \(\Gamma\): all these lengths and intersections are computed from the unchanged radii and centre distances. The coordinate formula proves
\[
F\circ\pi_{L/K}=\varphi\circ\tau_{\Gamma_L},\qquad
Q\circ\pi_{L/K}=P\circ\tau_{\Gamma_L}.
\]
New residual directions over \(L\) are off this finite hull and are included in the disc comparisons of Section 5.

If \(h\) is any full-union competitor for \(F\circ\pi_{F'/K}\) on \(D_{F'}\), then its pullback to \(D_L\) is semipositive real PL, by GJR, Proposition 7.6 and Lemma 5.4. The entire-family computation (5.4), now over the algebraically closed field \(L\), bounds that pullback by \(Q\circ\pi_{L/K}\). Surjectivity of \(D_L\to D_{F'}\) bounds \(h\) itself by \(Q\circ\pi_{F'/K}\). Conversely the latter function is an LFS minorant on \(D_{F'}\), by its explicit pulled-back local presentation. Hence
\[
E_{D_{F'}}(F\circ\pi_{F'/K})=Q\circ\pi_{F'/K}.
\tag{7.1}
\]
Apply (6.1) on both spaces to \(F_n\) and \(f\). Their errors remain uniform under pullback. Passing to their limits proves Theorem A's exact scalar equality and continuity upstairs. In particular both raw envelopes are already usc, so there is no scalar-regularization gap. Openness of scalar projection has not been used or asserted. The result concerns every obstacle on \(D\) and its pullbacks; it does not claim every unrelated obstacle on a nonalgebraically closed \(D_{F'}\) satisfies the same theorem.

## 8. Proper projective fibres and arbitrary obstacles on the product

This reduction works more generally for any compact good separated strictly \(K\)-analytic base \(A\), with
\[
Z=A\times_K\mathbb P^{d,\mathrm{an}}_K,\qquad p:Z\to A,
\qquad s(x)=(x,[1:0:\cdots:0]).
\]
The fibre at an arbitrary Berkovich point \(x\) is the actual analytic space \(\mathbb P^{d,\mathrm{an}}_{\mathcal H(x)}\). It is compact, connected, good, strict over \(\mathcal H(x)\), and boundaryless. Properness follows from projective analytification and is preserved by base change. Connectedness can be checked directly over any complete field \(H\): in a closed polydisc of common radius \(S\), the Gauss seminorm of \(G(T(z)+W)\) in the variables \(W\), with common radius \(t\in[0,S]\), is a multiplicative seminorm depending continuously on \((z,t)\). On polynomials it is
\[
|G|_{z,t}=\max_{\alpha}|(\partial^{[\alpha]}G)(z)|t^{|\alpha|},
\]
where \(\partial^{[\alpha]}\) denotes the Hasse derivative. It equals the original point at \(t=0\) and the radius-\(S\) Gauss point at \(t=S\), since translation by coordinates of norm at most \(S\) preserves the Gauss norm. This contracts the polydisc, so affine analytic space, their increasing union, is connected. The affine chart is dense in projective space: in a projective coordinate chart at a point on its omitted hyperplane, perform this same Gauss deformation only in the coordinate cutting out that hyperplane. For every positive sufficiently small \(t\) the coordinate has nonzero norm, and the points tend to the original point as \(t\to0\). Therefore projective analytic space is connected. No topological product identification for Berkovich products is assumed.

Take any competitor \(h\) on \(Z\). Pullback to that fibre is semipositive real PL and classically psh, including over the field \(\mathcal H(x)\), by scalar extension followed by analytic pullback. It attains a maximum by compactness. Its maximum locus is nonempty and closed; at every point of that locus the local maximum principle applies because the fibre is boundaryless, making the locus open. Connectedness makes the locus the entire fibre. Thus \(h\) is constant on every fibre. Set \(a=h\circ s\); then \(h=a\circ p\). Analytic restriction along \(s\) preserves real PL and semipositivity. If \(h\) is LFS, its explicit local unit presentation restricts to the same kind of presentation along \(s\). Conversely analytic pullback along \(p\) preserves both branches. This proves an exact family bijection, not just an upper bound for some fibre-invariant subfamily.

For \(f\in C(Z,\mathbb R)\), the fibre minimum \(g\) is attained. It is continuous. Indeed \(p\) is proper and therefore topologically closed; it is relatively smooth and therefore topologically open by Ber93, Corollary 3.7.4. Relative smoothness can be checked on the projective coordinate charts, where the projection is \(\mathbb A^d_A\to A\), exactly the local form in Definition 3.5.1. For any \(t\in\mathbb R\),
\[
\{g\leq t\}=p(\{f\leq t\})\text{ is closed},\qquad
\{g<t\}=p(\{f<t\})\text{ is open}.
\]
These statements use actual analytic projection, not a product-topology argument. The fibrewise equivalence \(a\circ p\leq f\Longleftrightarrow a\leq g\) now gives
\[
E_Zf=(E_Ag)\circ p.
\tag{8.1}
\]
Apply Theorem A for \(A=D\) to prove Theorem B, including global LFS approximation. The absolute analytic boundary of the product is \(p^{-1}(B)\): the projection is relatively boundaryless, and the relative-interior composition formula (GR2, Section 2.11) gives \(\operatorname{Int}(Z)=p^{-1}(\operatorname{Int}(A))\). The maximum principle was applied only on the proper fibre, not on the boundaryful total space.

For scalar extension \(F/K\), a fibre over \(x'\in A_F\) maps surjectively to the fibre over \(x=\pi(x')\); this is scalar projection
\[
\mathbb P^d_{\mathcal H(x')}{}^{\mathrm{an}}
\longrightarrow \mathbb P^d_{\mathcal H(x)}{}^{\mathrm{an}}.
\]
Consequently the fibre minimum of \(f\circ\pi_Z\) is \(g\circ\pi_A\). Apply (8.1) over \(F\), and apply Theorem A's exact scalar equality to the pulled-back \(g\). This proves
\[
E_{X_F}(f\circ\pi_X)=E_Xf\circ\pi_X
\]
for every analytic extension, together with continuity and the same curve-test verification as in Section 6.

For later use, any continuous open surjection \(p\) satisfies \((a\circ p)^*=a^*\circ p\) for locally bounded \(a\): continuity gives the inequality \(\leq\) from pulled-back neighbourhoods, and openness gives \(\geq\) since the image of every neighbourhood of a lift is a neighbourhood of its image. Thus (8.1) also identifies the regularized envelopes on a base where the raw envelope is discontinuous.

## 9. A fresh necessary exclusion: the split node, including projective products

Over any complete nontrivially valued field, let
\[
U=\mathcal M\bigl(K\langle x,y\rangle/(xy)\bigr).
\]
It is the two closed strict branch discs \(D_x,D_y\) meeting at their common rigid origin \(n\). Define the finite continuous obstacle, for \(a>0\), by
\[
f|_{D_x}=0,\qquad f|_{D_y}=-a|y|.
\tag{9.1}
\]
The branch restrictions agree at \(n\); the branches are closed and cover \(U\), so the gluing lemma proves continuity of \(f\). If \(h\) is any competitor in the full union, its restriction along the analytic branch inclusion to \(D_y\) is classically psh. The singleton Shilov boundary is its radius-1 Gauss point \(\eta_y\). Hence
\[
h|_{D_y}\leq h(\eta_y)\leq f(\eta_y)=-a,
\qquad h(n)\leq-a.
\tag{9.2}
\]
For \(r\in|K^\times|\), \(0<r<1\), put \(c_r=a/(-\log r)>0\) and define
\[
h_r|_{D_x}=c_r\log\max\{|x|,r\},\qquad h_r|_{D_y}=-a.
\tag{9.3}
\]
This is an actual global LFS function on \(U\). On the ordinary neighbourhood \(\{|x|<r\}\) of the node it is the constant \(-a\), including the entire other branch. Away from the node on the first branch the unit-max presentation of Section 4 applies; on the second branch it is constant. The bend is at a value-group radius, so it is strict real PL. The glued local LFS presentations verify membership on the singular analytic space itself, not merely after normalization. Also \(h_r\leq f\), since its first-branch values are at most zero and \(-a\leq-a|y|\) on the second disc.

At every \(z\in D_x\setminus\{n\}\), \(|x(z)|>0\) and \(h_r(z)\to0\) as \(r\to0\) in the value group. The constant \(-a\) is also a competitor. Equations (9.2)--(9.3) therefore compute the exact full-family raw envelope:
\[
E_Uf(z)=
\begin{cases}
0,&z\in D_x\setminus\{n\},\\
-a,&z\in D_y\quad\text{including }n.
\end{cases}
\tag{9.4}
\]
On each punctured branch this is locally constant. Both punctured branches accumulate at \(n\) (take nonzero field elements tending to zero). Thus the upper regularization changes the nodal value to zero and leaves the punctured second branch at \(-a\). It is discontinuous. This is a mathematical proof about the full union, independent of the supplied book counterexample. The same calculation holds over every analytic field extension: the branch maximum principle, norms and functions (9.3) pull back literally.

The general reduction of Section 8 applies to \(U\times\mathbb P^{d,\mathrm{an}}\). For the pulled-back obstacle its fibre minimum is (9.1), so the raw envelope is \(E_Uf\circ p\). Smooth openness of \(p\) gives
\[
\bigl(E_{U\times\mathbb P^d}(f\circ p)\bigr)^*=(E_Uf)^*\circ p.
\]
Restriction along the analytic section through a fixed projective point preserves the nodal discontinuity. Thus an unconditional class of all reduced strict curves, or their projective products in every positive dimension, fails P03.3. This proves an exclusion for this concrete branching geometry; it does not prove that normality, geometric unibranchness, or any proposed hypothesis is necessary in all spaces.

## 10. Exact scope and unresolved obligations

Theorems A and B address the full competitor union and all finite continuous obstacles on the displayed actual domains. All finite graph minorants were globally realized by analytic expressions, all omitted directions were controlled by comparison, analytic relative boundary signs were treated explicitly, and every analytic scalar extension was handled without assuming openness of scalar projection. This is substantially more than an invariant toric envelope or the envelope of an equicontinuous selected family: the entire family is bounded above by the constructed envelope for each finite-tree obstacle.

The result does not give sharp necessary and sufficient geometric hypotheses for the original P03.3. In particular the following obligations remain: arbitrary normal or geometrically unibranch higher-dimensional domains; continuity in the broader perfected-unibranch curve range; general semistable affinoids beyond the explicit rational trees, including global real-PL realization/cofinality there; arbitrary obstacles over nonalgebraically closed ground fields; nonsplit and codimension-two singularities and a full necessity theorem. Compactness and a projective factor are restrictions of our sufficient sector, not claimed sharp hypotheses. Products with closed polydiscs are not proper-fibre cases and are not covered by Theorem B. No supplied result concerning those geometries is treated as a proved consequence here. Candidate status is therefore false.

## 11. Primary references and execution evidence

GR2: W. Gubler and J. Rabinoff, *Classically plurisubharmonic functions on Berkovich spaces*, arXiv:2506.13548v2. GR1: the same authors, *On semipositive piecewise linear functions in non-archimedean analytic geometry*, arXiv:2503.05513. GJR: W. Gubler, P. Jell and J. Rabinoff, *Forms on Berkovich spaces based on harmonic tropicalizations*, cached arXiv:2111.05741. Thu: A. Thuillier, *Theorie du potentiel sur les courbes en geometrie analytique non archimedienne. Applications a la theorie d'Arakelov*, thesis, 2005. Ber93: V. G. Berkovich, *Etale cohomology for non-Archimedean analytic spaces*, Publ. Math. IHES 78 (1993), 5--161.

The exact chosen primary pages and bodies are in the source-extracts directory; source-provenance.json records paths, identifiers, selected pages, visual sign/boundary checks, and applications. Original inputs are preserved. The standalone TeX version is P03.3-paper.tex, generated from this complete argument by build-paper.py. Run python3 build-paper.py, then pdflatex -interaction=nonstopmode -halt-on-error P03.3-paper.tex twice. Commands, actual exits and diagnostics are recorded in checks/build-results.json and the two full build logs. The optional exact-rational finite graph implementation is checks/finite_graph.py; rerun python3 checks/finite_graph.py. Its results concern those finite graphs only, not analytic envelopes. Environment details are in environment.json. No model, worker, subagent, external messaging, installation or resource-heavy computation was invoked. None of source hashes, finite tests, successful execution or compilation is a proof certificate.


# All actual native canonical notes

[
  {
    "id": "n1",
    "summary": "Full-family continuity for every finite continuous obstacle on explicit compact strict rational curve affinoids over an algebraically closed nontrivially valued field. Global LFS realization, comparison and compatibility with every analytic scalar extension are proved. This is a sufficient sector, not the sharp classification.",
    "detailedSummary": "Finite type-2 trees uniformly approximate arbitrary continuous obstacles on the displayed rational domains. A greatest admissible vertex vector is globally realized by truncated logarithms with nonnegative interior charges and signed boundary-unit logarithms. Rational-star, annulus and omitted-disc comparisons bound every competitor in the exact union. Translation contractivity proves continuity for arbitrary obstacles and supplies uniform approximation by global LFS minorants. Passing arbitrary scalar extensions through their completed algebraic closures proves exact envelope pullback without assuming scalar projection is open. General semistable affinoids, arbitrary ground fields and the original sharp classification remain unresolved.",
    "text": "This is a partial mathematical theorem concerning the full competitor union.\n\nLet \\(K\\) be complete, algebraically closed and nontrivially valued. Choose centres \\(a_0,\\ldots,a_m\\in K\\) and radii \\(R,r_i\\in|K^\\times|\\) satisfying\n\\[\n0<r_i<R,\\qquad |a_i-a_0|<R,\\qquad |a_i-a_j|>\\max(r_i,r_j)\\quad(i\\ne j).\n\\]\nDefine the actual compact strict rational affinoid\n\\[\nD=\\{|T-a_0|\\le R\\}\\setminus\\bigcup_i\\{|T-a_i|<r_i\\}.\n\\]\nThe case \\(m=0\\) is a closed strict disc. For every finite continuous \\(f\\) on \\(D\\), the raw envelope \\(E_Df\\) over all globally defined locally Fubini–Study or semipositive real-PL minorants is finite and continuous. Consequently \\((E_Df)^*=E_Df\\). Moreover, for every analytic extension \\(F/K\\),\n\\[\nE_{D_F}(f\\circ\\pi)=E_Df\\circ\\pi.\n\\]\nThe upstairs envelope is also continuous. No invariance condition is imposed on \\(f\\) or on competitors.\n\nChecked published foundations. Gubler–Jell–Rabinoff, cached arXiv:2111.05741, Definition 5.1 and Lemma 5.4, define real PL using strict G-local linear combinations of logarithms of analytic units and give continuity and pullback. Definition 7.8 defines LFS as an R-PL function with semiample residue at every point, hence semipositive. Paragraph 7.9 gives the precise ordinary-local presentation\n\\[\nh=\\sum_j\\lambda_j\\max_i\\{-\\log|u_{ji}|\\},\\qquad \\lambda_j\\ge0,\\quad u_{ji}\\in\\mathcal O^\\times.\n\\]\nThe minus signs and invertibility requirement were checked against original PDF page 47. Proposition 7.6 preserves semipositivity under analytic morphisms and every analytic field extension. Gubler–Rabinoff, arXiv:2506.13548v2, Theorem 4.3, identifies semipositive real PL with classical psh on good strict spaces over a nontrivially valued field, without a boundaryless hypothesis. Its Definitions 3.4 and 4.1 quantify over all analytic extensions and curve morphisms. Theorems 6.1 and 6.4 provide the interior local maximum principle and affinoid Shilov maximum principle. These foundations apply to every competitor here. Arbitrary maxima of real-PL functions are not assumed real PL; GJR Example 5.3 expressly warns against that assertion.\n\nBoundary verification. Put \\(o=\\xi_{a_0,R}\\), \\(b_i=\\xi_{a_i,r_i}\\), and \\(B=\\{o,b_i\\}\\). The nested-disc topology described in GR2 Appendix A shows that the ordinary boundary of \\(D\\) in the boundaryless projective line is exactly \\(B\\). The analytic-domain interior formula in GR2 Section 2.11 identifies this with the analytic boundary. The domain is connected by its disc tree. A continuous psh function has its maximum on \\(B\\): otherwise its nonempty closed maximum locus is contained in the interior and is open by the local maximum principle, contradicting connectedness. The same reasoning applies to the finite maximum locus of \\(\\log|G|\\) for nonzero analytic \\(G\\). Thus \\(B\\) is a boundary for analytic functions. It is the Shilov boundary: \\((T-a_0)/c_0\\), with \\(|c_0|=R\\), uniquely peaks at \\(o\\) among \\(B\\), whereas \\(c_i/(T-a_i)\\), with \\(|c_i|=r_i\\), uniquely peaks at \\(b_i\\). The imposed strict inequalities make all the other listed values smaller. This verification also applies to the smaller rational stars, discs and annuli below.\n\nActual finite trees and density. Take the finite hull \\(\\Gamma\\subset D\\) of \\(B\\) and finitely many additional type-2 points, including all branch points as vertices. Root it at \\(o\\), and use length \\(|d\\log r|\\) along radius paths. Branch points have radii equal to centre distances and are type 2. For a nonroot vertex \\(v=\\xi_{a_v,r_v}\\), define\n\\[\nk_v(x)=\\log\\max\\{|T-a_v|(x),r_v\\}-\\log R\n=-\\operatorname{length}([o,x]\\cap[o,v]).\n\\]\nThe equality follows because the least common containing disc has radius \\(\\max(|T-a_v|(x),r_v)\\); it persists for nested-disc limits, including type-4 points. The last point of \\([o,x]\\) in \\(\\Gamma\\) defines \\(\\tau_\\Gamma(x)\\). The finitely many coordinates \\(k_v\\) separate points of \\(\\Gamma\\) and have the same values at \\(x\\) and \\(\\tau_\\Gamma(x)\\). Their continuous embedding of compact \\(\\Gamma\\) has continuous inverse, proving continuity of this actual retraction. Every component off \\(\\Gamma\\) is an attached open disc; original holes are recorded in \\(B\\). Such a component is exhausted by smaller closed strict discs, whose Gauss points approach its attachment. Its closure is not silently assumed affinoid.\n\nThe finite continuous functions \\(u_{a,r}=\\log\\max(|T-a|,r)\\), for \\(a\\in K\\) and \\(r\\in|K^\\times|\\), together with constants separate points of \\(D\\). Indeed seminorms are determined by polynomials, and algebraic closedness factors every polynomial into linear terms. A sufficiently small value-group truncation preserves a differing linear-factor value. Real Stone–Weierstrass therefore makes their generated algebra uniformly dense in \\(C(D,\\mathbb R)\\). Each expression involving finitely many coordinates factors through a finite tree: endpoints outside \\(D\\) are truncated at the relevant boundary, and coordinates from centres outside the outer disc are constant. A continuous function on this finite tree can be uniformly approximated by edge-affine interpolation. Subdivision points can be type 2, since the nonzero divisible group \\(\\log|K^\\times|\\) is dense in \\(\\mathbb R\\). Hence every continuous obstacle has uniform approximants\n\\[\nF=\\varphi\\circ\\tau_\\Gamma,\n\\]\nwhere \\(\\varphi\\) is affine on each subdivided edge. This proves density in the actual analytic category.\n\nFinite graph envelope and global realization. Write \\(\\ell_{vw}>0\\) for edge lengths. Consider all vertex vectors satisfying\n\\[\nq_v\\le\\varphi(v),\\qquad\n\\sum_{w\\sim v}\\frac{q_w-q_v}{\\ell_{vw}}\\ge0\\quad(v\\notin B).\n\\]\nBoundary vertices have no charge sign condition. Constants below \\(\\min\\varphi\\) are admissible. Coordinatewise maxima of admissible vectors remain admissible: choose the vector attaining the maximum at the tested vertex, and all neighbouring maxima are at least its neighbouring values. This is a finite-vector operation, not analytic maximum closure. The coordinatewise supremum \\(p\\) is finite, and taking finite maxima of almost maximizing vectors followed by a limit proves that \\(p\\) itself is admissible and greatest.\n\nLet \\(P\\) interpolate \\(p\\) linearly and set\n\\[\nd_v=\\sum_{w\\sim v}\\frac{p_w-p_v}{\\ell_{vw}},\\qquad\nQ=p_o+\\sum_{v\\ne o}d_vk_v.\n\\]\nThe outgoing charge of \\(k_v\\) is \\(+1\\) at \\(v\\), \\(-1\\) at \\(o\\), and zero elsewhere. Consequently \\(Q=P\\circ\\tau_\\Gamma\\): subtract the two expressions on the tree and remove terminal vertices successively; the difference has zero slope on each removed edge and is zero at the root.\n\nThis is an actual global LFS minorant. At an interior vertex \\(d_v\\ge0\\). A truncated logarithm is strict PL on the two strict domains \\(|T-a_v|\\le r_v\\) and \\(|T-a_v|\\ge r_v\\); on the latter \\(T-a_v\\) is a unit. At a bend, choose an ordinary neighbourhood excluding its zero and use\n\\[\n\\log\\max(|T-a_v|,r_v)\n=\\max\\{-\\log|(T-a_v)^{-1}|,-\\log|c_v^{-1}|\\},\\quad |c_v|=r_v.\n\\]\nNear its centre it is constant. These verify the exact LFS presentation. For \\(v=b_i\\), the coordinate equals \\(\\log|T-a_i|-\\log R\\) on all of \\(D\\), a logarithm of a global unit plus a constant. Its coefficient can have either sign, using an inverse unit for a negative coefficient. Real constants are LFS because the valuation is nontrivial. Thus positive interior terms and signed harmonic boundary terms give a global LFS function. The vertex obstacle inequalities imply \\(P\\le\\varphi\\) on every edge, hence \\(Q\\le F\\).\n\nFull-family upper bound. Let \\(h\\) be any competitor for \\(F\\). It is finite continuous and classically psh. At an interior vertex choose type-2 endpoints inside the adjacent edges, approaching the neighbouring vertices. The intervening rational star is a closed disc minus the open child discs, contained in the interior of \\(D\\); original holes lie beyond its endpoints. Let parent distance and value be \\(L_+,t_+\\), and child distances and values \\(L_j,t_j\\). Define\n\\[\nM=\\frac{t_+/L_++\\sum_jt_j/L_j}{1/L_++\\sum_j1/L_j}.\n\\]\nOn the star the child-centre functions \\(T-a_j\\) are units. The harmonic function\n\\[\nH=C+\\sum_j\\frac{M-t_j}{L_j}\\log|T-a_j|,\\qquad H(v)=M,\n\\]\nhas exactly the specified endpoint values: the corresponding child logarithm decreases by \\(L_j\\) towards its child, and all child logarithms increase by \\(L_+\\) towards the parent. If there are no children, use the constant \\(t_+\\). Since \\(h-H\\) is psh, boundary comparison gives \\(h(v)\\le M\\). Let endpoints tend to neighbours, using continuity of this competitor. Its vertex values satisfy the displayed graph inequalities, and hence \\(h(v)\\le p_v\\).\n\nOn an open edge use smaller closed strict annuli with endpoints inside that edge and approaching its vertices. These avoid sibling holes at either vertex. Harmonic interpolation in log radius bounds \\(h\\) by interpolation of its endpoint values, hence by \\(P\\). At any omitted-disc point, the singleton-Shilov maximum principle on smaller closed discs bounds \\(h\\) by its value at their Gauss points; their limit is the attachment. Therefore \\(h\\le P\\circ\\tau_\\Gamma=Q\\) everywhere. Combined with the constructed global minorant,\n\\[\nE_DF=Q.\n\\]\nEvery competitor in the exact full union has been bounded. Equality also holds for the LFS branch alone.\n\nPassage to arbitrary continuous obstacles. Constant minorants exist by compactness. Both branches allow real constant translation, so the full-family envelope is monotone, translation equivariant and satisfies\n\\[\n\\|E_Yf-E_Yf'\\|_\\infty\\le\\|f-f'\\|_\\infty.\n\\]\nChoose the finite-tree approximants \\(F_n\\) with errors \\(\\varepsilon_n\\to0\\). Their envelopes \\(Q_n\\) are continuous and converge uniformly to \\(E_Df\\), proving continuity. Moreover \\(Q_n-\\varepsilon_n\\) are global LFS minorants of \\(f\\) and converge uniformly to the same envelope. No monotonicity or unjustified real-PL maximum closure is required.\n\nAll scalar extensions. For arbitrary \\(F'/K\\), pass to its completed algebraic closure \\(L\\). The finite hull of the same Gauss endpoints in \\(D_L\\) has identical lengths, branching and charges; these are computed from unchanged centres, distances and radii. The coordinate formulas identify the pulled obstacle with \\(\\varphi\\circ\\tau_{\\Gamma_L}\\) and the pulled \\(Q\\) with \\(P\\circ\\tau_{\\Gamma_L}\\). New residual directions are included in the omitted-disc comparison. Every competitor on \\(D_{F'}\\) pulls back to a semipositive real-PL competitor on \\(D_L\\), where the entire-family computation bounds it by the pulled \\(Q\\). Surjectivity of scalar projection, GR2 Section 2.9, brings this bound down to \\(D_{F'}\\). Conversely the pulled \\(Q\\) is LFS by its explicit presentation. Thus exact pullback holds for finite-tree obstacles. Uniform approximation and envelope contractivity prove the asserted equality for every \\(f\\). Both envelopes are already continuous; scalar openness is unnecessary. This concerns base obstacles and their pullbacks, not unrelated arbitrary obstacles over every nonalgebraically closed extension.\n\nCurve tests and scope. After every analytic extension, pull the uniform LFS minorants back to any smooth strict curve. They are subharmonic. On a strict affinoid in that curve, a harmonic function dominating the limit on the finite boundary dominates each approximant up to its uniform error; comparison and passage to the limit prove the curve test. GR2 Definitions 3.4 and 4.1 then supply the full curve quantifiers, including further extensions. Classical positivity is thus checked separately from continuity; no CLD-v2 conclusion is asserted. The sharp geometric classification, general semistable affinoids and unrestricted higher dimensions are not proved.\n\nArtifacts: P03.3-argument.md contains the complete combined proof, and P03.3-paper.tex is standalone. Exact primary statements and bodies, original-PDF sign checks and application checks are retained in source-extracts and source-provenance.json. Rerun python3 checks/refresh_sources.py, python3 checks/render_sources.py, python3 checks/finite_graph.py, and python3 checks/build.py. The build script executes the generator and two pdflatex -interaction=nonstopmode -halt-on-error P03.3-paper.tex passes. Both final passes exited 0, producing an 11-page PDF with no final warning or overfull diagnostics. Exact-fraction graph diagnostics passed all 27, 27 and 81 cap vectors on three specified trees, 135 total; for annulus caps \\((0,100,2)\\), the greatest vector was \\((0,1,2)\\) with charges \\((1,0,-1)\\), illustrating the permitted negative boundary charge. These are exhaustive finite diagnostics only, not verification of analytic geometry. Original-PDF rendering exited 0; Thuillier's legacy Type-3 fonts emitted 156 retained bounding-box warnings. Environment details and unchanged original inputs are retained. Compilation, hashes and finite tests are execution evidence, not proof certificates.\n\nArtifacts: /workspace/research/campaigns/round-38/P03.3-public-source-geometric-continuity/artifacts/codex-Wl29bI",
    "support": []
  },
  {
    "id": "n2",
    "summary": "The full competitor envelope on a compact strict analytic base times projective space reduces exactly to the base envelope of the fibre-minimum obstacle. Combined with n1, this proves full-family continuity on the displayed rational-curve/projective-space products, with arbitrary obstacles and every scalar extension.",
    "detailedSummary": "Scalar-stable positivity and the maximum principle make every competitor constant on each actual proper projective fibre over a completed residue field. An analytic section descends competitors, and analytic pullback supplies the converse. Proper closedness and relative-smooth openness prove continuity of the fibre minimum. Scalar projections between projective fibres are surjective, preserving that minimum. The reduction covers projective-space factors and handles the total space's relative boundary; it does not cover closed-polydisc products or establish the general higher-dimensional classification.",
    "text": "Let \\(A\\) be any compact good separated strictly \\(K\\)-analytic space over a complete nontrivially valued field. Put\n\\[\nZ=A\\times_K\\mathbb P^{d,\\mathrm{an}}_K,\\qquad p:Z\\to A,\n\\qquad s(x)=(x,[1:0:\\cdots:0]).\n\\]\nFor every finite continuous obstacle \\(f\\), define\n\\[\ng(x)=\\min_{z\\in p^{-1}(x)}f(z).\n\\]\nThen \\(g\\) is finite continuous and the exact full-union raw envelopes satisfy\n\\[\nE_Zf=(E_Ag)\\circ p.\n\\]\nFor the rational domains \\(A=D\\) of n1, this proves continuity of the raw and regularized envelope on every \\(D\\times\\mathbb P^{d,\\mathrm{an}}\\), for every arbitrary continuous obstacle. Exact compatibility with every analytic scalar extension also follows.\n\nProof of the actual proper-fibre mechanism. At every Berkovich point \\(x\\), the fibre is \\(\\mathbb P^{d,\\mathrm{an}}_{\\mathcal H(x)}\\), not an assumed topological product fibre. Projective analytification is proper by Berkovich 1993, Proposition 2.6.9; analytic base change preserves properness. Each fibre is compact, good, strict over \\(\\mathcal H(x)\\), and boundaryless.\n\nIt is connected over any complete field \\(H\\). On a closed polydisc of radius \\(S\\), take the Gauss norm of \\(G(T(z)+W)\\) in \\(W\\) with radius \\(t\\in[0,S]\\). On polynomials this gives\n\\[\n|G|_{z,t}=\\max_\\alpha |(\\partial^{[\\alpha]}G)(z)|t^{|\\alpha|}.\n\\]\nThese multiplicative seminorms depend continuously on \\((z,t)\\), equal \\(z\\) at zero, and equal the radius-\\(S\\) Gauss point at \\(S\\), since bounded translation preserves that Gauss norm. Thus polydiscs are connected and their increasing union, affine analytic space, is connected. Its projective affine chart is dense: at a point on the omitted hyperplane, the same small Gauss deformation in the coordinate defining that hyperplane produces nonzero coordinate norm for every positive \\(t\\) and approaches the original point. Projective analytic space is therefore connected.\n\nTake any competitor \\(h\\) on \\(Z\\). Scalar extension followed by analytic pullback restricts it to a semipositive real-PL, hence classically psh, function on the actual fibre. It attains a maximum by compactness. The maximum locus is nonempty and closed, and it is open by the interior local maximum principle because the fibre has no boundary. Connectedness forces \\(h\\) constant on that fibre. Therefore \\(h=a\\circ p\\), where \\(a=h\\circ s\\).\n\nAnalytic restriction along \\(s\\) preserves real PL and semipositivity by the checked GJR pullback theorems. If \\(h\\) is LFS, its ordinary-local unit-max presentation restricts along \\(s\\), so \\(a\\) is also LFS. Conversely pullback along \\(p\\) preserves both branches. This proves an exact family bijection. The inequality \\(a\\circ p\\le f\\) is equivalent to \\(a\\le g\\), establishing the raw-envelope identity for the entire union.\n\nThe fibre minimum is continuous. The proper projection is topologically closed. It is relatively smooth: on projective coordinate charts it is \\(\\mathbb A^d_A\\to A\\), the local form of Berkovich Definition 3.5.1. Corollary 3.7.4, checked in the original PDF, makes it topologically open. For every real \\(t\\),\n\\[\n\\{g\\le t\\}=p(\\{f\\le t\\})\\text{ is closed},\\qquad\n\\{g<t\\}=p(\\{f<t\\})\\text{ is open}.\n\\]\nThus \\(g\\) is continuous. Applying n1 proves continuity and uniform global LFS approximation on the displayed products. The absolute analytic boundary is \\(p^{-1}(B)\\), by the relative-interior composition formula and relative boundarylessness of \\(p\\). The maximum principle above was applied on the fibre, not on the boundaryful total space.\n\nFor every analytic extension \\(F/K\\), the fibre over \\(x'\\in A_F\\) maps surjectively to the fibre over \\(x=\\pi(x')\\). This is the scalar projection from projective space over \\(\\mathcal H(x')\\) to projective space over \\(\\mathcal H(x)\\). Hence the fibre minimum of \\(f\\circ\\pi_Z\\) is exactly \\(g\\circ\\pi_A\\). Apply the same full-family reduction over \\(F\\), followed by n1's scalar identity for \\(g\\), to obtain\n\\[\nE_{Z_F}(f\\circ\\pi_Z)=E_Zf\\circ\\pi_Z\n\\]\nwhen \\(A=D\\). The uniform approximants also pass every extended analytic-curve test as proved in n1.\n\nFinally any continuous open surjection satisfies \\((a\\circ p)^*=a^*\\circ p\\) for locally bounded \\(a\\). Continuity gives the inequality \\(\\le\\) using pulled-back neighbourhoods; openness gives \\(\\ge\\) because the image of every neighbourhood of a lift is a neighbourhood of its image. Thus the reduction also describes regularization over a base with a discontinuous raw envelope.\n\nArtifacts: the complete proof is in P03.3-argument.md, Sections 2 and 8, and P03.3-paper.tex. Rerun python3 checks/build.py for the generator and two recorded successful TeX passes. This is a genuine higher-dimensional sufficient sector. It does not cover closed-polydisc products, arbitrary proper factors, or all normal/geometrically unibranch higher-dimensional spaces.\n\nArtifacts: /workspace/research/campaigns/round-38/P03.3-public-source-geometric-continuity/artifacts/codex-Wl29bI",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "A fresh exact full-family split-node calculation gives a discontinuous regularized envelope for a finite continuous obstacle. The obstruction persists under scalar extension and projective-space products. This supplies a concrete necessary exclusion, not the original sharp classification.",
    "detailedSummary": "On the split nodal affinoid, take zero obstacle on the x-disc and minus a times the y-coordinate norm on the y-disc. Every competitor is bounded by minus a throughout the y-disc by analytic branch pullback and its singleton-Shilov maximum principle. Explicit global LFS truncated logarithms approach zero at every nonnodal x-point. The raw envelope is exactly zero on the punctured x-branch and minus a on the y-branch including the node. Regularization raises the node to zero and is discontinuous along the other branch. The proper-fibre reduction and smooth openness carry this failure to every projective-space product. General necessity and unrestricted continuity remain unproved; candidate is false.",
    "text": "This counterexample is proved independently; no supplied book claim is assumed.\n\nOver any complete nontrivially valued field let\n\\[\nU=\\mathcal M(K\\langle x,y\\rangle/(xy)).\n\\]\nIts two closed strict branch discs \\(D_x,D_y\\) meet at their common rigid origin \\(n\\). For \\(a>0\\), define\n\\[\nf|_{D_x}=0,\\qquad f|_{D_y}=-a|y|.\n\\]\nThis is finite continuous: it is also the global function \\(-a|y|\\), and the two branch restrictions agree at the node.\n\nFor any competitor in the exact full union, analytic restriction to \\(D_y\\) preserves semipositivity and classical pshness by the published foundations checked in n1. Its singleton Shilov boundary is the radius-one Gauss point \\(\\eta_y\\). Therefore\n\\[\nh|_{D_y}\\le h(\\eta_y)\\le f(\\eta_y)=-a,\n\\qquad h(n)\\le-a.\n\\]\nThis bounds every competitor, including every noninvariant one.\n\nFor \\(r\\in|K^\\times|\\), \\(0<r<1\\), set \\(c_r=a/(-\\log r)>0\\) and define the actual global function\n\\[\nh_r=c_r\\log\\max(|x|,r).\n\\]\nIt equals \\(-a\\) on the entire y-branch. It is LFS on the singular space itself: on the ordinary neighbourhood \\(|x|<r\\) of the node it is constant, and elsewhere the logarithm-of-unit maximum presentation from n1 applies. Its bend lies at a value-group radius, so it is strict real PL. The ordinary-local presentations agree as a globally defined function; this is not merely a normalization construction. Also \\(h_r\\le f\\): first-branch values are at most zero, and second-branch values satisfy \\(-a\\le-a|y|\\).\n\nAt every nonnodal x-point, \\(|x|>0\\) and \\(h_r\\to0\\) as \\(r\\to0\\) in the value group. The constant \\(-a\\) is another competitor. These lower bounds and the full-family upper bounds compute\n\\[\nE_Uf(z)=\\begin{cases}\n0,&z\\in D_x\\setminus\\{n\\},\\\\\n-a,&z\\in D_y\\text{, including }n.\n\\end{cases}\n\\]\nEach punctured branch is open away from the node and has constant raw envelope. Both accumulate at the node, using nonzero field elements tending to zero. Upper regularization therefore changes only the nodal value to zero and retains value \\(-a\\) on the punctured y-branch. It is discontinuous. The same calculation holds after every analytic scalar extension, since the branches, coordinate norms, minorants and maximum-principle bound persist literally.\n\nBy n2, for the pulled obstacle on \\(U\\times\\mathbb P^{d,\\mathrm{an}}\\) the raw envelope is \\(E_Uf\\circ p\\). Smooth openness of \\(p\\) gives\n\\[\n\\bigl(E_{U\\times\\mathbb P^d}(f\\circ p)\\bigr)^*=(E_Uf)^*\\circ p.\n\\]\nIts restriction along the analytic section through a fixed projective point is the nodal regularized envelope. Thus discontinuity persists in every positive-dimensional projective product. This excludes an unconditional continuity theorem for all reduced strict curves and their displayed products. It does not prove that every branched space fails, or that normality or geometric unibranchness is necessary in general.\n\nExact status: partial. The sufficient sectors in n1–n2 do not determine sharp necessary and sufficient hypotheses for original P03.3. Remaining gaps include arbitrary normal or geometrically unibranch higher-dimensional domains, the full perfected-unibranch curve range, general semistable affinoids and their global real-PL cofinality, arbitrary obstacles over nonalgebraically closed base fields, nonsplit singularities, codimension-two singularities, and general necessity. Compactness and projective-space factors are restrictions of the proved sector, not asserted sharp hypotheses.\n\nDeliverables: P03.3-argument.md contains the complete new argument and precise scope; P03.3-paper.tex is standalone; its PDF has 11 pages. status.json has exactly id, status, exact_result, proof_file and concrete_gaps, and reports partial. Exact selected primary bodies and checked applications are retained in source-extracts and source-provenance.json. Original inputs are preserved. Rerun commands are in rerun.md; python3 checks/build.py runs two actual TeX passes, both recorded with exit 0 and no final warnings. python3 checks/check_artifacts.py passed input-preservation, source-transcription, status-key, support-dependency and build-record checks. These are execution observations, not mathematical proof certificates.\n\nArtifacts: /workspace/research/campaigns/round-38/P03.3-public-source-geometric-continuity/artifacts/codex-Wl29bI",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Actual published source provenance and hypothesis checks

{
  "sources": [
    {
      "id": "GR2",
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "selected_full_pages": [
        {
          "pdf_page": 6,
          "literal_file": "source-extracts/GR2-pdf-page-006.literal.txt",
          "literal_page_sha256": "16a443967381a0825f00925dba32d8b6d7a5773574dc3f2219a669e9489db614"
        },
        {
          "pdf_page": 7,
          "literal_file": "source-extracts/GR2-pdf-page-007.literal.txt",
          "literal_page_sha256": "34ccebb67789241783588937145ab4bd19b3f2fad5732f3d4a3fc36c5e24fcae"
        },
        {
          "pdf_page": 8,
          "literal_file": "source-extracts/GR2-pdf-page-008.literal.txt",
          "literal_page_sha256": "8af30646bfa7cfe68b69b95cc3a48344fffd2319f5eca50d7889fa58db231eb9"
        },
        {
          "pdf_page": 10,
          "literal_file": "source-extracts/GR2-pdf-page-010.literal.txt",
          "literal_page_sha256": "1c941ec581ff4e1712be17af6da299996380868b7b1cc5c94ca3f4456614cc76"
        },
        {
          "pdf_page": 11,
          "literal_file": "source-extracts/GR2-pdf-page-011.literal.txt",
          "literal_page_sha256": "a8a605a63d505d7de520e3592c747f99cfe520c5c7f069465c45bd3ca8bf6892"
        },
        {
          "pdf_page": 21,
          "literal_file": "source-extracts/GR2-pdf-page-021.literal.txt",
          "literal_page_sha256": "820cce17e7bafe3746e0e59150d0a98cb7a070832a4f6731ff2109942b63a9a7"
        },
        {
          "pdf_page": 22,
          "literal_file": "source-extracts/GR2-pdf-page-022.literal.txt",
          "literal_page_sha256": "12de51b8102a4ea09f23a92407e01734b60aecf4dc65d919edfccf63d7bee3fd"
        },
        {
          "pdf_page": 23,
          "literal_file": "source-extracts/GR2-pdf-page-023.literal.txt",
          "literal_page_sha256": "d9424c12897c66bf794c303dd5f6a6362dcf63e991e459618c9207f8cd53e682"
        },
        {
          "pdf_page": 30,
          "literal_file": "source-extracts/GR2-pdf-page-030.literal.txt",
          "literal_page_sha256": "4fcca2835bab85572ea9eb5bc15b88bd27ced898c7387e6e89d02b60ecdc131d"
        },
        {
          "pdf_page": 31,
          "literal_file": "source-extracts/GR2-pdf-page-031.literal.txt",
          "literal_page_sha256": "c9a339caa6767c72b0f5588c8c754e5d58ce99743b518ee878e58c675f8e1770"
        },
        {
          "pdf_page": 33,
          "literal_file": "source-extracts/GR2-pdf-page-033.literal.txt",
          "literal_page_sha256": "b5fb4d3dcde384fbda5c5c9668b22686965298ee02b2e1aae3947218deba32bd"
        },
        {
          "pdf_page": 34,
          "literal_file": "source-extracts/GR2-pdf-page-034.literal.txt",
          "literal_page_sha256": "c8a880a346d907b4789080a6784ba89ac6269e6b71996b9e3728299fc05af61b"
        },
        {
          "pdf_page": 37,
          "literal_file": "source-extracts/GR2-pdf-page-037.literal.txt",
          "literal_page_sha256": "3cde75f55297f4c2e03bba0b06d82e95e65297c9514479c42aed2c7143a91e39"
        }
      ],
      "retained_statements_and_bodies": "Sections 2.8-2.11; Definitions 3.4,4.1; Proposition 4.2; Theorems 4.3,6.1,6.4; Appendix A.1-A.2. Theorem 6.5 is retained as a cross-check; uniform-limit curve comparison is proved directly.",
      "pdf_reextract_command": [
        "pdftotext",
        "-layout",
        "-f",
        "6",
        "-l",
        "37",
        "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
        "source-extracts/GR2-selected-range.pdftext.txt"
      ],
      "pdf_reextract_exit": 0,
      "pdf_reextract_diagnostics": ""
    },
    {
      "id": "GR1",
      "public_source": "https://arxiv.org/pdf/2503.05513",
      "pdf": "/workspace/research/shared-sources/GR-2503.05513-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/GR-2503.05513-20261004.txt",
      "pdf_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "extract_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "selected_full_pages": [
        {
          "pdf_page": 2,
          "literal_file": "source-extracts/GR1-pdf-page-002.literal.txt",
          "literal_page_sha256": "ddcd08283157e696e3683cb6208d60423c125b0d56db07a3eb91ec6c90cde4d9"
        },
        {
          "pdf_page": 5,
          "literal_file": "source-extracts/GR1-pdf-page-005.literal.txt",
          "literal_page_sha256": "cddc14223ce1a2f0543db0ffa76e9fe9b7fa980fb2b718855862050d18232f2b"
        },
        {
          "pdf_page": 6,
          "literal_file": "source-extracts/GR1-pdf-page-006.literal.txt",
          "literal_page_sha256": "86b2c84a9d8efe2b512d5281fe7b4f677788a64fbaa480538c5ba639aec54c54"
        },
        {
          "pdf_page": 15,
          "literal_file": "source-extracts/GR1-pdf-page-015.literal.txt",
          "literal_page_sha256": "cb2193be1cd71d0f6b7df6eaeded923f8fc8578b1aee8fc765c7cc3e83fe481e"
        },
        {
          "pdf_page": 16,
          "literal_file": "source-extracts/GR1-pdf-page-016.literal.txt",
          "literal_page_sha256": "d6ea98f6e7709a86b1cdc679db40d2efbeaa4529dc3e84f8ef366684278cc371"
        },
        {
          "pdf_page": 17,
          "literal_file": "source-extracts/GR1-pdf-page-017.literal.txt",
          "literal_page_sha256": "350e1328a92ac311b8534d6d2bf553a27068a222b780164aa10e733cebec94e4"
        }
      ],
      "retained_statements_and_bodies": "PL standing assumptions and boundary caveat; Proposition 5.1 and Corollary 5.4 cross-check Theorem GR2 4.3. No boundaryless approximation theorem is applied to a boundary point.",
      "pdf_reextract_command": [
        "pdftotext",
        "-layout",
        "-f",
        "2",
        "-l",
        "17",
        "/workspace/research/shared-sources/GR-2503.05513-20261004.pdf",
        "source-extracts/GR1-selected-range.pdftext.txt"
      ],
      "pdf_reextract_exit": 0,
      "pdf_reextract_diagnostics": ""
    },
    {
      "id": "GJR",
      "public_source": "https://arxiv.org/pdf/2111.05741",
      "pdf": "/workspace/research/shared-sources/GJR-2111.05741.pdf",
      "literal_extract": "/workspace/research/shared-sources/GJR-2111.05741.txt",
      "pdf_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "extract_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "selected_full_pages": [
        {
          "pdf_page": 31,
          "literal_file": "source-extracts/GJR-pdf-page-031.literal.txt",
          "literal_page_sha256": "0286959703f57c016523108761fe657f3f32a4a8d05746c3159f5a0b7226ba5d"
        },
        {
          "pdf_page": 44,
          "literal_file": "source-extracts/GJR-pdf-page-044.literal.txt",
          "literal_page_sha256": "e3ff8b347c685a8c17412ba618139efd7edaebe2bfc60db406cbf99ce9243a7e"
        },
        {
          "pdf_page": 45,
          "literal_file": "source-extracts/GJR-pdf-page-045.literal.txt",
          "literal_page_sha256": "62690d857bfa11e6dec160c1f908787b9910b171e8aa94e4f3c6282ef51a4702"
        },
        {
          "pdf_page": 46,
          "literal_file": "source-extracts/GJR-pdf-page-046.literal.txt",
          "literal_page_sha256": "23d00fd808ff70a1c1a87294a4cc947979768b62e6dab7165d01be4d4abf54c5"
        },
        {
          "pdf_page": 47,
          "literal_file": "source-extracts/GJR-pdf-page-047.literal.txt",
          "literal_page_sha256": "8c43decece427ba4bcd4a0f891306acf4bafd1d3be07e3c5fc6ead61b1380a73"
        }
      ],
      "retained_statements_and_bodies": "Definition 5.1, Remarks 5.2, Example 5.3, Lemma 5.4, Definition 7.2, Proposition 7.6, Definition 7.8 and paragraph 7.9.",
      "pdf_reextract_command": [
        "pdftotext",
        "-layout",
        "-f",
        "31",
        "-l",
        "47",
        "/workspace/research/shared-sources/GJR-2111.05741.pdf",
        "source-extracts/GJR-selected-range.pdftext.txt"
      ],
      "pdf_reextract_exit": 0,
      "pdf_reextract_diagnostics": ""
    },
    {
      "id": "Thu",
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
      "literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "selected_full_pages": [
        {
          "pdf_page": 76,
          "literal_file": "source-extracts/Thu-pdf-page-076.literal.txt",
          "literal_page_sha256": "324008384af95330bc7280127159497f9c8121cd793553b415e113c956311b7e"
        },
        {
          "pdf_page": 105,
          "literal_file": "source-extracts/Thu-pdf-page-105.literal.txt",
          "literal_page_sha256": "f7ba9960c4751bded0eab0d09c6bd74ce075168e3a43b5f48ae2e03d80fa3acc"
        },
        {
          "pdf_page": 106,
          "literal_file": "source-extracts/Thu-pdf-page-106.literal.txt",
          "literal_page_sha256": "9a0e0286a5793dbb622c011be16c16936abfd044ed3067729197aa02484cbd18"
        }
      ],
      "retained_statements_and_bodies": "Definition 3.1.5 and Proposition 3.4.6 retained. Direct rational-star comparison replaces any new application requiring an unspecified semistable model.",
      "pdf_reextract_command": [
        "pdftotext",
        "-layout",
        "-f",
        "76",
        "-l",
        "106",
        "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
        "source-extracts/Thu-selected-range.pdftext.txt"
      ],
      "pdf_reextract_exit": 0,
      "pdf_reextract_diagnostics": ""
    },
    {
      "id": "Ber93",
      "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
      "literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
      "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "selected_full_pages": [
        {
          "pdf_page": 30,
          "literal_file": "source-extracts/Ber93-pdf-page-030.literal.txt",
          "literal_page_sha256": "5aeb9abd888a25233ee6c39915a1baf48827f7bcb02c6d169f537688e63ef886"
        },
        {
          "pdf_page": 31,
          "literal_file": "source-extracts/Ber93-pdf-page-031.literal.txt",
          "literal_page_sha256": "c5c79951e775de3b50d11840fbfa75790d2702928c86a5ee835de3826af07fc8"
        },
        {
          "pdf_page": 32,
          "literal_file": "source-extracts/Ber93-pdf-page-032.literal.txt",
          "literal_page_sha256": "2ebe758bac68cc0ee86e162dd82a824fcfa9d11a87aac803ed076fbeb8c094f4"
        },
        {
          "pdf_page": 51,
          "literal_file": "source-extracts/Ber93-pdf-page-051.literal.txt",
          "literal_page_sha256": "f61fb36284ca760553475c9ab64e9adf1394f8bb98d9443ddae4670c039a94cd"
        },
        {
          "pdf_page": 64,
          "literal_file": "source-extracts/Ber93-pdf-page-064.literal.txt",
          "literal_page_sha256": "4c0b9e6c16c161c5b159e83091e1abfac65617292f8b07330abca5ddc79e360f"
        },
        {
          "pdf_page": 66,
          "literal_file": "source-extracts/Ber93-pdf-page-066.literal.txt",
          "literal_page_sha256": "19f233709555613c5e5dfc0a2c9c07734e11db46f650ce0a5944cc0c6615c99e"
        },
        {
          "pdf_page": 74,
          "literal_file": "source-extracts/Ber93-pdf-page-074.literal.txt",
          "literal_page_sha256": "52b2b7413e7eb7737cda68f619ea3d85a6516c1ee215d3bb12fd67ccdccee1e1"
        }
      ],
      "retained_statements_and_bodies": "Sections 1.5.3-1.5.5 for properness/relative boundary; Definition 3.5.1, Proposition 3.5.2 for relative smoothness; Corollary 3.7.4 for ordinary topological openness. Proposition 2.6.9 for proper analytification.",
      "pdf_reextract_command": [
        "pdftotext",
        "-layout",
        "-f",
        "30",
        "-l",
        "74",
        "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
        "source-extracts/Ber93-selected-range.pdftext.txt"
      ],
      "pdf_reextract_exit": 0,
      "pdf_reextract_diagnostics": ""
    }
  ],
  "visual_pdf_checks": [
    {
      "file": "source-extracts/GJR-lfs-page47.png",
      "checked": "Definition 7.8 includes R-PL; paragraph 7.9 uses positive real combinations of maxima of NEGATIVE logarithms of INVERTIBLE functions on an ordinary open neighbourhood."
    },
    {
      "file": "source-extracts/GR-psh-page22.png",
      "checked": "Theorem 4.3 requires nontrivial valuation, good space, strict analyticity, and R-PL. No boundaryless hypothesis."
    },
    {
      "file": "source-extracts/Thu-comparison-page76.png",
      "checked": "Printed page 62: Definition 3.1.5 has upper semicontinuity, non-identically-minus-infinity per component and comparison on strict affinoids. No assumed continuity of a raw supremum."
    },
    {
      "file": "source-extracts/Berkovich-open-page74.png",
      "checked": "Printed page 77: Corollary 3.7.4 says a smooth morphism is an open map. It is applied to a projective-space projection, never to an arbitrary scalar projection."
    }
  ],
  "limitations": "Hashes, source recognition, PDF rendering and compilation certify execution only. Every new envelope application is proved in the argument; selected sources are published foundations, not supplied book claims."
}


## Published source GR2, PDF page 6

6                                    W. GUBLER AND J. RABINOFF

2.7. Grothendieck topology and fibers. For a k-analytic space X , we will also consider
the G-topology generated by the analytic domains of X , as described in [Ber93, §1.3]. We
denote this space by X G to emphasize the use of this Grothendieck topology. For strictly
k-analytic spaces, we often use the G-topology generated by the strictly analytic domains
instead: see [Ber93, §1.6]. In either case, the space X G has a well-behaved sheaf of rings
OX G . If V = M (A ) is an affinoid domain of X , then we have OX G (V ) = A . For x ∈ X ,
we denote by H (x) the completed residue field of the local ring OX G ,x with respect to
the valuation on OX G ,x /m x induced by the norm corresponding to x. If V is any analytic
domain in X and if x ∈ V , then H (x) is the same whether we consider x as belonging
to V (which is itself a k-analytic space), or to X . We call x ∈ X a rig-point if H (x) is a
finite extension of k.
   If ϕ : Y → X is a morphism, then the fiber ϕ −1 (x) over x ∈ X is an H (x)-analytic
space, and the underlying topological space has the induced topology [Ber93, §1.4].

2.8. Fiber products. The category of k-analytic spaces admits fiber products by [Ber93,
§1.4]. For analytic spaces X , Y over a k-analytic space S, we denote the fiber product by
X ×S Y . Given x ∈ X and y ∈ Y over the same point s ∈ S, there always exists z ∈ X ×S Y
mapping to x and to y with respect to the canonical projections [Duc18, 1.2.13]. For
convenience, we repeat the argument. The completed tensor product H (x)⊗         b H (s) H ( y)
contains H (x) ⊗H (s) H ( y) by a result of Gruson [Gru66, §3.2 Théorème 1(4)], so
H (x)⊗b H (s) H ( y) ̸= 0. The Berkovich spectrum of any nonzero Banach ring is nonempty
                                                                 
[Ber90, Theorem 1.2.1], and any z ′ ∈ M H (x)⊗     b H (s) H ( y) induces a point z ∈ X ×S Y
mapping to x and y. Note that H (z) is a simultaneous analytic extension field of H (x)
and of H ( y).
  Since Gruson’s result holds for Banach algebras over a non-Archimedean field, the
same argument shows that for two analytic field extensions of k, there is a joint analytic
extension of both.

2.9. Extension of scalars. Let k′ /k be an an analytic extension field. Then there is a
base extension functor (·)k′ which associates to a k-analytic space X a k′ -analytic space
X k′ , given on a k-affinoid space X = M (A ) by the k′ -affinoid space X k′ = M (A ⊗b k k′ )
[Ber90, §1.4]. We denote by πk′ /k : X k′ → X the structure map, which is closed and
surjective by [GRW17, Lemma 2.19], [Duc24, (3.1.1.2)].

2.10. The Shilov section. For r = (r1 , . . . , rn ) ∈ R>0     n
                                                                   , we consider the k-affinoid do-
main in the closed polydisc M k〈r1 T1 , . . . , rn Tn 〉 given by the equations |T j (x)| = r j ,
                                          −1            −1

j = 1, . . . , n. The corresponding      k-affinoid algebra is denoted by k r ; it consists of the
Laurent series f = λ∈Zn aλ T λ such that aλ r λ → 0 for |λ| → ∞. The k-affinoid al-
                           P

gebra M (k r ) has a unique Shilov        boundary point equal to the weighted Gauss point
η r ∈ M k〈r1−1 T1 , . . . , rn−1 Tn 〉 given by the weighted Gauss norm ∥ ∥ r from 2.3. If
                                                                                       p
r1 , . . . , rn induce linearly independent elements in the Q-vector space R>0 / |k× |, then k r
is a non-Archimedean field; it follows that k r = H (η r ). For every k-affinoid algebra A ,
there is always such an r such that A ⊗        b k r is a strictly k r -affinoid algebra. See [Ber90,
pp. 21–22].


## Published source GR2, PDF page 7

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                 7

   For any k-analytic space X and r ∈ R>0n
                                             , the structure map πkr /k : X kr → X has a canon-
ical section σ : X → X r mapping x ∈ X to the unique Shilov boundary point of the fiber
π−1
  k r /k
         (x) = M (H (x)⊗b k r ) = M (H (x) r ) (which is the weighted Gauss point η r ). We
call σ the Shilov section. The Shilov section is continuous: see [Ber90, Lemma 3.2.2(i)],
[Duc18, 1.2.16].

2.11. Relative boundary. An important notion in this paper is that of the relative bound-
ary of a morphism ϕ : X → Y of k-analytic spaces. This is a closed subset of X which we
denote by ∂ (X /Y ). We will not give the details of this definition, but let us try to explain
the literature on the subject. In [Ber90, §2.5], Berkovich defines the relative boundary
∂ (X /Y ) for k-affinoid spaces X and Y . Then in [Ber90, §3.1], he generalizes ∂ (X /Y ) for
good k-analytic spaces using that all points of X and Y have k-affinoid neighborhoods.
Berkovich calls ϕ closed if ∂ (X /Y ) = ;. Berkovich defines ∂ (X /Y ) for arbitrary k-analytic
spaces in [Ber93, 1.5.3(ii)], as follows. A morphism ϕ is closed if for every morphism
Y ′ → Y from a good k-analytic space Y ′ , the fiber product X ′ := X ×Y Y ′ is good and the
canonical morphism X ′ → Y ′ is closed in the previous sense. Finally in [Ber93, Defini-
tion 1.5.4], a point x ∈ X is defined to be in Int(X /Y ) if x has an open neighborhood U
such that ϕ induces a closed morphism U → Y in the above sense. We refer to [Tem15,
Definition 4.2.4.1] for a more explicit equivalent definition of ∂ (X /Y ). Note that in this
paper, we will use the notion closed map in the usual topological sense meaning that it
maps closed sets to closed sets. This is different from Berkovich’s terminology.
   The complement Int(X /Y ) := X \ ∂ (X /Y ) is called the relative interior. We will usually
apply this in the case Y = M (k), in which case we call ∂ X := ∂ (X /M (k)) the boundary
of X and Int(X ) := X \ ∂ X the interior. If ∂ X = ;, we say that X boundaryless. A bound-
aryless space is good by definition. Note that Berkovich calls boundaryless k-analytic
spaces closed.
   We list here some properties of the boundary and interior which we will use throughout
the paper:
   (1) A point x ∈ X is contained in Int(X /Y ) if and only if there is an open neighbor-
       hood U of x such that Int(U/Y ) = U: this is part of the above definition.
   (2) If ϕ : X → Y is finite, then Int(X /Y ) = X [Ber93, Example 1.5.3(iii)].
   (3) If X is an analytic domain in Y , then Int(X /Y ) is the topological interior of X in
       Y [Ber93, Proposition 1.5.5(i)].
             ϕ     ψ
   (4) If X → Y → S are morphisms of k-analytic spaces, then

(2.11.1)                   Int(X /Y ) ∩ ϕ −1 Int(Y /S) ⊂ Int(X /S)

        [Ber93, Proposition 1.5.5(ii)], with equality if ψ is locally separated [Tem04,
        Corollary 5.7]. Taking S = M (k), this becomes

(2.11.2)                      Int(X /Y ) ∩ ϕ −1 Int(Y ) ⊂ Int(X ).

   (5) If k′ /k is an analytic extension field, then

                                π−1
                                 k′ /k
                                       Int(X /Y ) ⊂ Int(X k′ /Yk′ )


## Published source GR2, PDF page 8

8                                      W. GUBLER AND J. RABINOFF

         [Ber93, Proposition 1.5.5(iii)]. Taking Y = M (k), this becomes
                                       π−1
                                        k′ /k
                                              Int(X ) ⊂ Int(X k′ ).
For convenience, we restate these properties in terms of the relative boundary:
   (1′ ) A point x ∈ X is contained in ∂ (X /Y ) if and only if ∂ (U/Y ) ̸= ; for every open
         neighborhood U of x.
   (2′ ) If ϕ is finite, then ∂ (X /Y ) = ;.
   (3′ ) If X is an analytic domain in Y , then ∂ (X /Y ) is the topological boundary of X
         in Y .
               ϕ     ψ
     ′
   (4 ) If X → Y → S are morphisms of k-analytic spaces, then
(2.11.3)                        ∂ (X /S) ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ (Y /S)),
         with equality if ψ is locally separated. Taking S = M (k), this becomes
(2.11.4)                             ∂ X ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ Y ).
    (5′ ) If k′ /k is an analytic extension field, then
                                     ∂ (X k′ /Yk′ ) ⊂ π−1
                                                       k′ /k
                                                             ∂ (X /Y ).
         Taking Y = M (k), this becomes
                                           ∂ X k′ ⊂ π−1
                                                     k′ /k
                                                           ∂ X.
We will need the following lemma, which is a consequence of deep results in [CT21] in
general, although it has an elementary proof for good spaces.
Lemma 2.12. If X is a k-analytic space and k′ /k is an analytic field extension, then
                                          πk′ /k (∂ X k′ ) = ∂ X .
Proof. We have πk′ /k (∂ X k′ ) ⊂ ∂ X by 2.11(5′ ). Let x ∈ ∂ X , and let U ⊂ X be a compact
neighborhood of x. We claim that x ∈ ∂ U. If not, then there is an open neighborhood
V of x in U such that ∂ V = ; by 2.11(1′ ). If V ′ ⊂ V is a smaller open neighborhood of
x in X , then ∂ V ′ = ; as well by 2.11(3′ ) and by (2.11.4) as applied to V ′ → V → M (k).
Thus we may assume that V is open in X , which implies by 2.11(1) that x ∈ Int(X ), a
contradiction. Hence x ∈ ∂ U. If x ′ ∈ π−1      k′ /k
                                                      (x), then x ′ ∈ ∂ Uk′ if and only if x ′ ∈ ∂ X k′
for the same reason. We need to show π−1        k′ /k
                                                      (x) ∩ ∂ X k′ ̸= ;, so we may replace X by U to
assume that X is compact. In this case, the closed subset ∂ X k′ is compact; suppose that
it is disjoint from π−1
                      k′ /k
                            (x). Then πk′ /k (∂ X k′ ) is a closed subset of X not containing x, so
there exists an open neighborhood V of x such that Vk′ = π−1            k′ /k
                                                                              (V ) ⊂ Int(X k′ ). This means
that ∂ Vk′ = ; by 2.11(3,4). But x ∈ ∂ V , and boundarylessness can be checked after
extension of scalars by [CT21, Theorem 11.5]. This contradiction proves the claim. □
2.13. A k-analytic space X is called rig-smooth at x ∈ X if it is flat (in the sense of
[Duc18]) and if the sheaf of Kähler differentials ΩX (considered on the G-topology) is
free at x of rank equal to the dimension of X at y. We call X smooth if it is rig-smooth
and boundaryless. We refer to [Duc18, Chapter 5] for a discussion (note that rig-smooth
is called quasi-smooth there) and comparison to other definitions.


## Published source GR2, PDF page 10

10                                W. GUBLER AND J. RABINOFF

Then the graded residue field of A is given by
                                           M
                                    e• :=
                                    A          A≤r /A<r .
                                           r∈R>0

We refer to [Tem04] for properties of this functorial construction.

                   3. SUBHARMONIC FUNCTIONS ON ANALYTIC CURVES
  In this section, we generalize Thuillier’s theory [Thu05] of subharmonic functions from
smooth strictly analytic curves to arbitrary k-analytic curves.
3.1 (k-Analytic Curves). By a k-analytic curve we mean a separated k-analytic space of
pure dimension 1. We gather the following facts about k-analytic curves:
   (1) A k-analytic curve is good, i.e., every point has an affinoid neighborhood. [Duc24,
        Proposition 3.3.7]
   (2) A k-analytic curve is paracompact. [Duc24, Théorème 4.5.10]
   (3) If X is an affinoid k-analytic curve, then ∂ X coincides with the Shilov boundary
        of X . [Thu05, 2.1.2]
An analytic domain in a k-analytic curve (for example, an open subset) is again a k-
analytic curve.
3.2 (Thuillier’s Harmonic Functions). Thuillier [Thu05, §2.3] defines a sheaf of harmonic
functions on a smooth, strictly k-analytic curve for a non-trivially valued k, roughly as
follows. If X is affinoid, then a continuous function h: X → R is harmonic if, after passing
to a finite, separable field extension, it coincides with the composition of a harmonic
function on a skeleton of X (in the sense of graph theory) with the retraction to the
skeleton. If X is smooth, then a harmonic function on an open subset of X is defined to be
a continuous function whose restriction to every strictly affinoid subdomain is harmonic.
3.3 (Thuillier’s Subharmonic Functions). For a non-trivally valued k, Thuillier [Thu05,
Définition 3.1.5] defines a subharmonic function on a smooth, strictly k-analytic curve X
to be an upper semicontinuous function u: X → R ∪ {−∞} that is not identically −∞
on any connected component of X and that satisfies the following property: for every
strictly k-affinoid domain U ⊂ X and every harmonic function h: U → R, if u ≤ h on ∂ U
then u ≤ h on U.
  Now we extend this definition to the case of non-smooth curves. The idea is that a
function should be subharmonic if it pulls back to a subharmonic function along any
morphism from a smooth curve. However, an inseparable curve over an imperfect field
does not admit any non-constant morphisms from a smooth curve, so one has to allow
an extension of scalars as well. We also consider the constant function −∞ to be sub-
harmonic, following Demailly [Dem85] in the complex case.
Definition 3.4 (Subharmonic functions). Let X be a k-analytic curve and let u: X →
R ∪ {−∞} be an upper semicontinuous function. We say that u is subharmonic provided
that, for every non-trivially valued analytic extension field k′ /k, every smooth, connected,
strictly k′ -analytic curve Y , and every morphism Y → X k′ , the composition
                                        πk′ /k     u
                              Y −→ X k′ −→ X −→ R ∪ {−∞}


## Published source GR2, PDF page 11

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              11

is either subharmonic on Y in the sense of [Thu05, Définition 3.1.5], or is identically −∞.
3.4.1. If X is a smooth, connected, strictly k-analytic curve over a non-trivially valued k,
then an upper semicontinuous function u: X → R ∪ {−∞} is subharmonic in our sense
if and only if it is either subharmonic in Thuillier’s sense or is identically −∞. Indeed, if
u is subharmonic in our sense then one can take k = k′ and Y = X to see that it is either
subharmonic in Thuillier’s sense or is identically −∞. Conversely, if u is identically −∞
then it is clearly subharmonic in our sense, and if u is subharmonic in Thuillier’s sense
then it is subharmonic in our sense by [Thu05, Proposition 3.1.14 and Corollaire 3.4.5].
3.4.2. As a special case of (3.4.1), if X is a smooth, connected, strictly k-analytic curve
over a non-trivially valued k, then a function u: X → R (taking finite values) is subhar-
monic in our sense if and only if it is subharmonic in Thuillier’s sense.
  Here we collect the basic properties of subharmonic functions, which we will prove
over the course of this section.
Proposition 3.5. Let X be a k-analytic curve and let u: X → R ∪ {−∞} be an upper
semicontinuous function.
   (1) (Sheafiness) The subharmonic functions form a sheaf on X .
   (2) (Analytic functions) If f ∈ Γ (X , OX ) then log | f | : X → R ∪ {−∞} is subharmonic.
   (3) (Boundaries) If u is subharmonic on Int(X ), then u is subharmonic on X .
   (4) (Cone Property) If u1 , u2 : X → R ∪ {−∞} are subharmonic and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are subharmonic.
   (5) (Limits) The infimum of a decreasing net of subharmonic functions is subharmonic.
   (6) (Maximum Principle) If u is subharmonic and u attains a local maximum at x ∈
       Int(X ), then u is constant in a neighborhood of x.
   (7) (Extension of scalars) Let k′ /k be an analytic extension field. Then u is subharmonic
       if and only if u ◦ πk′ /k : X k′ → R ∪ {∞} is subharmonic.
   (8) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If u
       is subharmonic then u ◦ f is subharmonic, and the converse holds if f is finite and
       surjective.
   (9) (Finite Values) If u is subharmonic and u(x) = −∞ for a non-rig-point x ∈ X ,
       then u ≡ −∞ on the irreducible component of Int(X ) ∪ {x} containing x.
  Let us make some remarks regarding the content of Proposition 3.5.
3.5.1. If U ⊂ X is an open subset then U is again a k-analytic curve, so it makes sense
to speak of subharmonic functions on U. It is immediate from the definition that a sub-
harmonic function on X restricts to a subharmonic function on U. Hence subharmonic
functions form a presheaf on X . Proposition 3.5(1) asserts that this presheaf is a sheaf.
3.5.2. The maximum principle (Proposition 3.5(6)) is [Thu05, Proposition 3.4.10] in the
smooth, strictly analytic case.
3.5.3. In the situation of Proposition 3.5(7), it is immediate from Definition 3.4 that
u ◦ πk′ /k is subharmonic when u is subharmonic. This is the difficult direction in the
smooth, strictly analytic case: see [Thu05, Corollaire 3.4.5]. This result is hidden in the


## Published source GR2, PDF page 21

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES               21

Remark 3.16. We still assume that X is a strictly k-analytic curve over a non-trivially
valued field k and that h: X → R is continuous. Proposition 3.15 and Proposition 3.14(6)
imply in particular that if h◦πk′ /k is harmonic for some analytic extension field k′ /k, then
h◦πk′′ /k is R-PL for any analytic extension k′′ /k, which is by no means obvious. Likewise,
Proposition 3.14(7) implies that if f : Y → X is finite and surjective and h◦ f is harmonic,
then h is R-PL, and Proposition 3.14(8) implies that if h|Int(X ) is harmonic then h is R-PL.

                     4. CLASSICALLY PLURISUBHARMONIC FUNCTIONS
  In this section we define the notion of a classically plurisubharmonic function. The
definition follows Definition 3.4.
Definition 4.1 (Classically Plurisubharmonic Functions). Let X be a k-analytic space and
let u: X → R ∪ {−∞} be an upper semicontinuous function. We say that u is classically
plurisubharmonic or classically psh provided that, for every analytic extension field k′ /k,
every k′ -analytic curve Y , and every morphism f : Y → X k′ , the function u◦πk′ /k ◦ f : Y →
R ∪ {−∞} is subharmonic on Y in the sense of Definition 3.4.
4.1.1. Any class of psh functions should respect extension of scalars and should be stable
under pullback, so the conditions in Definition 4.1 are necessary. In complex analysis,
this condition (without the extension of scalars) is the definition of plurisubharmonicity,
which is why we call the notion “classically psh”.
4.1.2. If X is a k-analytic curve, then a function u: X → R∪{−∞} is classically psh if and
only if it is subharmonic. Indeed, if u is classically psh then taking k′ = k and Y = X in
Definition 4.1 shows that u is subharmonic, and if u is subharmonic then it is classically
psh by Proposition 3.5(7,8).
4.1.3. In Definition 4.1, one can assume that Y is a connected, smooth, strictly k′ -analytic
curve: this follows from Definition 3.4.
  Classically psh functions satisfy the basic properties of subharmonic functions on curves.
Proposition 4.2. Let X be a k-analytic space.
   (1) (Sheafiness) The classically psh functions form a sheaf on X .
   (2) If f ∈ Γ (X , OX ) then log | f |: X → R ∪ {−∞} is classically psh.
   (3) (Cone Property) If u1 , u2 : X → R∪{−∞} are classically psh and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are classically psh.
   (4) (Limits) The infimum of a decreasing net of classically psh functions is classically
       psh. For arbitrary pointwise limits, we refer to Theorem 6.5.
   (5) (Extension of Scalars) Let k′ /k be an analytic extension field. A function u: X →
       R ∪ {−∞} is classically psh if and only if u ◦ πk′ /k : X k′ → R ∪ {−∞} is classically
       psh.
   (6) (Functoriality) Let Y be a k-analytic space and let f : Y → X be a morphism. If
       u: X → R ∪ {−∞} is classically psh then u ◦ f is classically psh, and the converse
       holds if f is finite and surjective.
Proof. Properties (1,3,4) follow immediately from Proposition 3.5(1,4,5). For Proposi-
tion 4.2(2), we consider an analytic function f on X . As | f | is continuous, we deduce


## Published source GR2, PDF page 22

22                                  W. GUBLER AND J. RABINOFF

that log | f | is a continuous function with values in R ∪ {−∞} and hence it is upper semi-
continuous. Then Proposition 4.2(2) follows from Proposition 3.5(2).
    To prove Proposition 4.2(5), it is clear from the definitions that if u is classically psh,
then u ◦ πk′ /k is classically psh for every analytic extension field k′ /k. To prove the con-
verse, we assume that k′ /k is an analytic extension field and that u′ := u ◦ πk′ /k is a
classically psh function on X k′ . Since the morphism πk′ /k is closed and surjective 2.9,
it is clear that u is upper semicontinuous. Let k′′ /k be an analytic extension field and
let f : Y → X k′′ be a morphism over k′′ from a k′′ -analytic curve Y . We have to show
that u ◦ πk′′ /k ◦ f is subharmonic. As in the proof of Proposition 3.5(7), we consider
a simultaneous analytic extension field K of k′ and k′′ . It follows from the above that
u ◦ πK/k = u′ ◦ πK/k′ is classically psh and hence u ◦ πK/k ◦ f K is subharmonic. We con-
clude from the commutative diagram (3.10.1) that u ◦ πK/k ◦ f K = u ◦ πk′′ /k ◦ f ◦ πK/k′′ is
subharmonic and hence u ◦ πk′′ /k ◦ f is subharmonic by Proposition 3.5(7).
    Likewise, the proof of Proposition 4.2(6) follows the same lines as the proof of Propo-
sition 3.5(8). Again, it follows from the definitions if u is a classically psh function on X ,
then u ◦ f is a classically psh function on Y . Conversely, we assume that u ◦ f is a clas-
sically psh function for a finite surjective morphism f : Y → X . Since finite morphisms
are proper and hence closed, we deduce from upper semicontinuity of u ◦ f and from
surjectivity of f that u is upper semicontinuous. It remains to show that u ◦ πk′ /k ◦ g is
subharmonic for any analytic extension field k′ /k and any morphism g : Z → X k′ from a
connected k′ -analytic curve Z. Setting W := Z ×X k′ Yk′ , we get a morphism g ′ : W → Yk′
from f by base change with respect to f ′ : Yk′ → X k′ as in (3.10.2). Since u ◦ f is classi-
cally psh, it follows from Proposition 4.2(5) that u ◦ πk′ /k ◦ f ′ = u ◦ f ◦ πk′ /k is classically
psh. The morphism f is finite and surjective, hence the same holds for f ′ . We con-
clude that the base change f ′′ : W → Z of the morphism f ′ is finite and surjective. The
k′ -analytic space W has irreducible components of dimension 1 and maybe isolated irre-
ducible components of dimension 0. Removing the latter, we obtain a k′ -analytic curve
W ′ as an open and closed subset of W . Since Z is a connected k′ -analytic curve and f ′′
is a finite surjective map from W onto Z, we get an induced finite surjective morphism
W ′ → Z. Indeed, as W ′ is also Zariski-closed in W , we deduce from finiteness of f ′′ that
f ′′ (W ′ ) is a Zariski-closed subset in Z of dimension 1 and hence f ′′ (W ′ ) = Z as Z is a
connected k′ -analytic curve. Since the inclusion W ′ → W is obviously finite, the com-
position W ′ → Z is also finite. In the following, we replace W by W ′ , which preserves
the commutativity of the diagram (3.10.2) and has the advantage that W is a k′ -analytic
curve. It follows that u ◦ πk′ /k ◦ f ′ ◦ g ′ = u ◦ πk′ /k ◦ g ◦ f ′′ is subharmonic on W . The
morphism of k′ -analytic curves f ′′ : W → Z is finite and surjective, so we deduce from
Proposition 3.5(8) that u ◦ πk′ /k ◦ g is subharmonic.                                           □

  In the paper [GR25], we have studied semipositive R-PL functions on a good strictly
k-analytic space over a non-trivially valued non-archimedean field k. This turns out to
be the same as an R-PL function that is classically psh, as we now show.

Theorem 4.3. Suppose that the valuation on k is nontrivial. Let X be a good, strictly k-
analytic space and let h: X → R be an R-PL function. Then h is semipositive if and only if h
is classically psh.


## Published source GR2, PDF page 23

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                  23

Proof. For x ∈ X , an R-PL function h: X → R induces a residue line bundle Lh (x) ∈
Pic(red(X , x))R on the reduction red(X , x) of the germ (X , x): see 2.17. Recall from
[GJR21, Definition 7.2] that h is semipositive at x ∈ X if and only if the associated residue
line bundle Lh (x) is nef. We have shown in [GR25, Proposition 3.1] that for a smooth
strictly k-analytic curve, an R-PL function is semipositive if and only if it is subharmonic.
Since semipositivity is stable under base extension and pull-back [GJR21, Proposition
7.6], we conclude that a semipositive R-PL function on X is classically psh.
   The converse follows from [GR25, Corollary 3.5], which shows that an R-PL function h
on X is semipositive if and only if there is an algebraically closed analytic extension field
F of k such that for every smooth F -analytic curve C and every morphism ϕ : C → X F ,
we have h ◦ ϕ semipositive.                                                                □
                                 5. CONNECTIVITY BY CURVES
  We will prove a maximum principle for classically psh functions by reducing to the
case of curves. For this we will need to prove that it is possible to connect a point of an
analytic space to its neighbors using analytic curves, potentially defined over large field
extensions.
Definition 5.1. Let X be a k-analytic space. An analytic curve in X is a subset Γ ⊂ X
satisfying the following property: there is an analytic extension field k′ /k, a compact,
separated k′ -analytic space C of dimension at most 1, and a morphism ϕ : C → X k′ , such
that Γ = πk′ /k ◦ ϕ(C).
  An analytic curve Γ in X is overconvergent if there exist (k′ , C, ϕ) as above such that ϕ
factors as
                                          ψ
                                           → Int(C ′ ) -← → C ′
                                      ←
                                  C
                                      ←
(5.1.1)                                                     ←
                                          ϕ →            ϕ′
                                                           →
                                               X k′
where C ′ is a separated k′ -analytic space of dimension at most 1, and ϕ ′ and ψ are
morphisms.
5.1.2. The compactness hypothesis in Definition 5.1 is crucial. When X is Hausdorff, it
implies that if Γ , Γ ′ are analytic curves in X such that Γ ∪ Γ ′ is connected, then Γ ∩ Γ ′ ̸= ;
(the compact sets Γ , Γ ′ are closed, so they cannot be disjoint by connectedness). However,
a non-proper compact curve has a nonempty boundary, which causes problems when
trying to reduce the maximum principle to the case of curves. This is the reason for
introducing overconvergent curves in X .
5.1.3. One can always pass to a larger analytic extension field k′′ /k′ in Definition 5.1.
Indeed, we have a commutative diagram
                                          ←   ϕk′′
                                   Ck′′         → X k′′
                                                                   πk′′ /k
                                      ←



                                                       ←




                                                               ←
                                                πk′′ /k′
                                                                   →
                                   ↠



                                                      →




                                          ←                  ←
                                      C       ϕ→      X k′         → X.
                                                               πk′ /k


## Published source GR2, PDF page 30

30                                   W. GUBLER AND J. RABINOFF

after recentering, we can assume that ϕ(V ) ⊂ B+n . For x ′ ∈ V let y ′ = ϕ(x ′ ) ∈ B+n and
let Σ x ′ be the connected component of ϕ −1 ([ y ′ , 0]) containing x ′ . Since [ y ′ , 0] ⊂ B+n we
have ϕ −1 ([ y ′ , 0]) ⊂ Int(Y ), and since Σ x ′ is connected and x ′ ∈ V we have Σ x ′ ⊂ V . As
before, there exists an open neighborhood U of x in V such that Σ x ′ ∩ Σ x ̸= ; for all
x ′ ∈ U.
     By Lemma 5.9, for any y ′ ∈ B+n there is a connected, overconvergent analytic curve
Γ y ′ in B+n containing [ y ′ , 0]. For x ′ ∈ V mapping to y ′ , we let Γ x ′ be the connected
component of ϕ −1 (Γ y ′ ) containing x ′ , so that Γ x ′ ⊂ V for the same reason that Σ x ′ ⊂ V .
By Lemma 5.2(1,4), this Γ x ′ is again a connected, overconvergent analytic curve in X .
Clearly Σ x ′ ⊂ Γ x ′ , so for x ′ ∈ U we have Γ x ′ ∩ Γ x ̸= ;. This completes the proof as in the
previous case.                                                                                     □

              6. THE MAXIMUM PRINCIPLES FOR CLASSICALLY PSH FUNCTIONS
  In this section, we consider a non-Archimedean field k. We will prove first that the
local maximum principle holds for classically psh functions, and then we will show a
global maximum principle in the affinoid case; more specifically, that that a classically
psh function takes its global maximum at a Shilov point.
Theorem 6.1 (Local Maximum Principle). Let X be a k-analytic space and let u be a clas-
sically psh function on X . If u has a local maximum at x ∈ Int(X ), then u is locally constant
at x.
Proof. We may replace X by a connected, Hausdorff open neighborhood of x in Int(X ) to
assume that X is connected and boundaryless and that u attains a global maximum at x.
Let R = u(x). Let Γ be a connected, overconvergent analytic curve in X containing x. We
claim that u ≡ R on Γ . Consider the set Γu=R = {z ∈ Γ | u(z) = R}. This set is closed in Γ
by upper semicontinuity of u, so since Γ is connected, it suffices to show that Γu=R is open
in Γ .
   By 5.1.3, there exist an analytic extension field k′ /k, a compact, separated strictly k′ -
analytic space C of dimension at most 1, a separated strictly k′ -analytic space C ′ of dimen-
sion at most 1, and morphisms ψ: C → C ′ and ϕ ′ : C ′ → X k′ , such that ψ(C) ⊂ Int(C ′ )
and πk′ /k ◦ ϕ(C) = Γ , where ϕ = ϕ ′ ◦ ψ. The composition u ◦ πk′ /k ◦ ϕ ′ is subharmonic
on 1-dimensional connected components of C ′ because u is classically psh.
   Let y ∈ Γu=R , let z ∈ C be a point lying over y, and let z ′ = ψ(z) ∈ Int(C ′ ), so that
R = u ◦ πk′ /k ◦ ϕ ′ (z ′ ) = u ◦ πk′ /k ◦ ϕ(z). If {z ′ } is a connected component of C ′ then clearly
u ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood of z ′ . Otherwise, the connected component of z ′
in C ′ is a strictly k′ -analytic curve, in which case u ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood
of z ′ by Proposition 3.5(6) (here we use z ′ ∈ Int(C ′ )). Taking the ψ-inverse image of
such a neighborhood, we see that u ◦ πk′ /k ◦ ϕ ≡ R in a neighborhood of z. Applying
this argument to each z ∈ (πk′ /k ◦ ϕ)−1 ( y), we construct an open set V ⊂ C containing
(πk′ /k ◦ ϕ)−1 ( y) such that u ◦ πk′ /k ◦ ϕ|V ≡ R.
   The complement C \ V is a closed subset of the compact space C, so it is a compact
subset of C that is disjoint from (πk′ /k ◦ ϕ)−1 ( y). Its image is a compact subset of X that
does not meet y, so there is an open neighborhood W of y such that (πk′ /k ◦ϕ)−1 (W ) ⊂ V .


## Published source GR2, PDF page 31

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                     31

It follows that u ≡ R on W ∩ Γ . This proves that Γu=R is open in Γ . As remarked above,
this yields u ≡ R on Γ .
   Let y ∈ X be any point. By Theorem 5.4, there is a connected, overconvergent analytic
curve Γ in X containing x and y. We showed above that u ≡ R on Γ , so that u( y) = R.
As y was arbitrary, we have u ≡ R on X .                                              □

  The global maximum principle for classically psh functions involves the Shilov bound-
ary. For this, we need the following two lemmas. The first is well-known, but we were
unable to find a reference.

Lemma 6.2. Let X be a k-affinoid space of pure dimension d ≥ 1. Then the Shilov boundary
of X is contained in the relative boundary ∂ X of X over k. In particular, ∂ X ̸= ;.

Proof. Let k′ /k be an analytic field extension such that X k′ is strictly affinoid. Note that
the base change morphism πk′ /k maps ∂ X k′ to ∂ X 2.11(5′ ) and maps the Shilov boundary
onto the Shilov boundary [GRW17, Proposition 2.21], so we may assume that X is strictly
affinoid and k′ non-trivially valued. Choose a formal affine k◦ -model X of X . The interior
X \ ∂ X consists of the points x ∈ X such that the closure of redX (x) in Xs is proper over
the residue field ek by [CD12, Lemme 6.5.1]. Since X is affine, the special fiber Xs is
affine, so x ∈ ∂ X if and only if redX (x) is not a closed point of Xs . Since d ≥ 1, the
special fiber Xs is of pure dimension d ≥ 1, and hence the generic points of Xs are not
closed. By [GM19, Proposition A.3], the divisorial points of X (i.e. the points of X which
reduce to the generic points of Xs ) are precisely the Shilov points of X . We conclude that
all Shilov points are in the boundary of X .                                                □

   Let X = M (A ) be an affinoid space over k of pure dimension d. By a result of Ducros
[Duc12, Lemme 3.1], the boundary ∂ X of X can be expressed as a union of affinoid spaces
of lower dimension, defined over certain extension fields of k. We use his argument to
give a stratification of ∂ X . Choose non-nilpotent elements g1 , . . . , g r ∈ A such that the
graded reductions e   g1• , . . . , e
                                    g r• generate the graded ek• -algebra A
                                                                          f• . Let ri be the spectral
radius of g i . Then for any I ⊂ {1, . . . , r}, we get a morphism

                                p I : X −→ B(I),       x 7→ (g i (x))i∈I

to the closed poly-disc B(I) = i∈I B(0, ri ) of dimension s = |I|. Let η(I) be the weighted
                                     Q

Gauss point of B(I) and let k I := H (η(I) ), which is the completion of the field of rational
functions k((t i )i∈I ) in the variables (t i )i∈I with respect to the weighted Gauss valuation
for the weight (ri )i∈I .

Lemma 6.3. With the above notations, set X I := p−1
                                                 I
                                                    (η(I) ). By convention, we set X ; = X .
Then:
                 k I -affinoid space of pure dimension d − s if non-empty.
    (1) X I is a S
    (2) ∂ X I = i∈{1,...,r}\I X I∪{i} .
    (3) X I = {x ∈ X | (e   g i• (x))i∈I are algebraically independent in H
                                                                          f• (x) over ek• }.
                                                                                     S
    (4) If X has pure dimension d, then the Shilov boundary of X is equal to |I|=d X I .


## Published source GR2, PDF page 33

               CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                           33

(ri ′ )i ′ ∈I and hence also the completion of ki (r j ) j∈J with respect to the weighted Gauss
norm for the weight (r j ) j∈J identifying the variable t ∈ ki with t i . It follows readily that
for any H ⊂ {1, . . . , r}, we have (X i )H = X {i}∪H as affinoid spaces over k I . Applying this
with H = J and using our induction hypothesis for X i , property (2) for the boundary of
X I = (X i )J follows by induction applied to X i . The same inductive argument shows that
X I is the set of points x ∈ X 1 where (e      g j (x)) j∈J are algebraically independent over eki . We
have seen that X i is non-empty if and only if e           g i (x) is transcendental over ek. Since t = t i
in ki satisfies pi (t) = g i , we conclude that x ∈ X I if and only if (e
                      ∗
                                                                               g l (x))l∈I are algebraically
independent over ek. This proves (3).
   Finally, we claim that the union of the minimal strata X I for |I| = d is the Shilov
boundary of X . If d = 0, this is obious as X = X ; . Now assume that d ≥ 1. If x ∈ X I then
(3) shows that the graded residue field H            f(x)• contains the d algebraically independent
elements (e     g i )i∈I over ek• . Since the reduction Xe in the sense of Temkin [Tem04, Section
3] is of pure dimension d (using [Tem04, Proposition 3.1(v)] for base change to the
strictly affinoid case), we conclude that the reduction of x in Xe is a generic point of Xe .
By [Tem04, Proposition 3.3], we conclude that x is a Shilov point of X . Conversely, for
every a ∈ A , the function |a| takes its maximum in a Shilov point. We conclude from
Lemma 6.2 that |a| takes its maximum in ∂ X ̸= ;. By (2), we conclude that |a| takes its
maximum in one of the strata sets X I . By induction on the dimension d, this occurs when
|I| = d proving (4).                                                                                      □
  We return to the setting where k is any non-Archimedean field which might be trivially
valued. We give now the global maximum principle for affinoids.
Theorem 6.4. Let h be a classically psh function on a k-affinoid space X . Then h takes its
maximum in a Shilov point of X .
  An analogue for θ -psh functions on a proper scheme is in [GM19, Proposition 4.22].
Proof. By base change to a non-trivially valued analytic extension field k′ /k such that X k′
is strictly affinoid, and using that πk′ /k maps the Shilov boundary of X k′ to the Shilov
boundary of X [GRW17, Proposition 2.21],    S we may assume that X is strictly affinoid and
that k is non-trivially valued. Let X = j X j be the partition of X into its irreducible
components. It follows from [GRW17, Proposition 2.15] that the union of the Shilov
points of all X j gives the Shilov points of X . So it is enough to prove the claim for every
X j , and hence we may assume X irreducible. This will be a bit to strong for our inductive
argument later, but the argument shows that we may assume X of pure dimension d.
    If d ≥ 1, then we claim that h takes its maximum in the boundary ∂ X . We prove this
by contradiction. It is clear that the boundary ∂ X is the disjoint union of the boundaries
of the connected components of X , and the same holds if we replace the boundary by the
Shilov boundary, so we may assume X connected. Let M be the set of points of X where
h is maximal. We assumed that M ∩ ∂ X = ;. Since h is continuous, it is clear that M is
a closed subset of X . We know from Theorem 6.1 that if a classically psh function takes
a (local) maximum on X \ ∂ X , then h is locally constant. This implies M open in X . As
M is non-empty and X is connected, we deduce M = X . Since ∂ X ̸= ; as we have d ≥ 1
(see Lemma 6.2), we get M ∩ ∂ X ̸= ;, which is a contradiction.


## Published source GR2, PDF page 34

34                                 W. GUBLER AND J. RABINOFF

    Let now
        S h be a classically psh function on X . We need the description of the boundary
∂ X = X i given in Lemma 6.3, where i runs through {1, . . . , r} and X i = X {i} as before.
We claim by induction on d that h takes its maximum in one of the sets X I with |I| = d,
and hence in the Shilov boundary of X , which proves the theorem. If h is constant, then
this is obvious; this also settles the case d = 0. If h is non-constant, then we have seen
at the beginning of the proof that h takes its maximum in ∂ X , and hence in one of the
X i . Since X i is of dimension d − 1, we are done by induction as the strata sets of ∂ X i are
strata sets of ∂ X using Lemma 6.3.                                                          □
  The following result was suggested by a referee of the paper [GR25]. We are very
grateful for this hint.
Theorem 6.5. Let (u j ) j∈J be a net of classically psh functions on the k-analytic space X
which converges pointwise to an upper semicontinuous function u. Then u is classically psh.
   For a sequence of semipositive R-PL functions converging pointwise to an R-PL func-
tion, the above result was shown in [GR25, Theorem 5.6]. When X is a proper algebraic
variety, this was known before ([GK19, Proposition 7.2] for uniform limits, [GM19, The-
orem 1.3] for pointwise limits).
Proof. Since u is upper semicontinuous, using the definition of classically psh functions,
we may assume that X is a connected smooth curve over a non-trivially valued field.
We may assume that u is not identically −∞. Then for every strictly k-affinoid domain
U of X and every harmonic function h on U with u ≤ h on ∂ U, we have to show that
u ≤ h holds on U. Since u j → u pointwise and since ∂ U is finite, for any ϵ > 0 we have
u j − h ≤ ϵ on ∂ U for all j sufficiently large. Since u j − h is a classically psh function by
Proposition 3.5(4) and since the Shilov boundary of U agrees with ∂ U [Thu05, §2.1.2],
the global affinoid maximum principle in Theorem 6.4 shows that u j − h ≤ ϵ on U for all
j sufficiently large. It follows that u − h ≤ ϵ on U, which implies u ≤ h on U since ϵ was
arbitrary.                                                                                   □

                               7. PLURIHARMONIC FUNCTIONS
  In this section, we consider a k-analytic space X over any non-Archimedean field k.
Following the discussion of harmonic functions on curves in 3.12, we generalize this
notion as follows to higher dimensions.
Definition 7.1. A function h: X → R is called pluriharmonic if h and −h are classically
psh functions (see Definition 4.1).
Proposition 7.2. Pluriharmonic functions are continuous and have the properties:
     (1) (Sheafiness) The pluriharmonic functions form a sheaf on X .
     (2) If f ∈ Γ (X , OX× ) then log | f | is pluriharmonic.
     (3) (Vector Space) The pluriharmonic functions on X form a real vector space which
         we denote by PH(X ).
     (4) (Limits) If a function h: X → R is locally a uniform limit of pluriharmonic functions,
         then h is pluriharmonic.


## Published source GR2, PDF page 37

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                      37

                       APPENDIX A. THE TOPOLOGY OF THE UNIT DISK
  Let k be a non-archimedean field which might be trivially valued. In this appendix, we
give an elementary description of the topology of the unit disc B1k = M (k〈T 〉). These are
well-known facts which we present in the way we need in the body of text.
A.1. A rig-point of B1k is induced by a maximal ideal of k〈T 〉. Let k′ be the completion of
an algebraic closure k a of k and let G be the Galois group of k a /k. By [Ber90, 1.3.5] or
[Duc24, (3.1.1.2)], we may write B1k = B1k′ /G as a topological quotient; we denote the
quotient map by π: B1k′ → B1k . For a rig-point z and 0 < ρ ≤ 1, we define the closed disc
B1k (z, ρ) with center z and radius ρ by taking any z ′ ∈ π−1 (z) and then setting
                                                                              
                         B1k (z, ρ) := π {x ′ ∈ B1k′ | |(T − z ′ )(x ′ )| ≤ ρ} .
This is a closed set in B1k which does not depend on the choice of z ′ and which contains
the center z. We often simply write B1 (z, ρ) = B1k (z, ρ). Moreover, we can choose any rig-
point of B1 (z, ρ) as a center. Note that for any rig-point y ′ of B1k′ , the image π(B1k′ ( y ′ , ρ))
is a closed disc Bk (z, ρ) for a suitable rig-point z as center. In the trivially valued case, we
can simply take z = π( y ′ ) and in the non-trivially valued case, this follows by density of
rigid points [Ber90, Proposition 2.1.15] in a strictly affinoid space. Similarly, we define
the open disc B1+ (z, ρ) with center z and radius ρ using |(T − z ′ )(x ′ )| < ρ as a defining
inequality over k′ . The above remarks also apply to open balls. It follows from the
ultrametric triangle inequality that two open or closed balls are either disjoint or one is
contained in the other.
A.2. The topology of the unit disc B1k is well-known. Roughly speaking, it has the struc-
ture of an infinite tree with all branches connected to the Gauss point η1 at the top (see
[Ber90, Example 1.4.4, §4.2] or [Duc24, §3.4]                                           1
                                               S for more details). We call U ⊂ Bk a stan-
dard open subset if it has the form U = B+ \ i Bi where B+ is either an open ball B+ (z, ρ)
with a rig-point z as center and with ρ ∈ (0, 1) or B+ = B1k , and where the Bi are finitely
many closed balls with rig-points as centers and with positive radii. Since two discs are
either disjoint or one is contained in the other, we see that the union and the intersec-
tion of two standard open subsets are again standard open subsets. We claim that the
standard open subsets form a basis of topology for B1k . In the non-trivially valued case,
this follows from [Ber90, §4.2] using §A.1 to find rig-centers in the balls. In the trivially
valued case, B1k is the union of closed intervals starting in the Gauss point η1 and ending
in the rig points of B1k . The topology is very simple as B1k \ {η1 } is the topological disjoint
union of the half-open intervals (η1 , z] with z ranging over the rig points of B1 . A subset
U of B1k is an open neighborhood of η1 if and only if U ∩ [η1 , z] is open for all rig points
z and equal to [η1 , z] except for finitely many z. We refer to [Ber90, Example 1.4.4]
or [BJ18, §1.1.6] for these facts, from which we deduce easily that the standard open
subsets form also a basis of topology in the trivially valued case.
  The main result of this appendix is the following lemma.
Lemma A.3. Let B1 (z, ρ) be a closed disc as above and let f (T ) be the minimal polynomial
of the center z, i.e., a generator of the corresponding maximal ideal of k〈T 〉. Then there is


## Published source GR1, PDF page 2

2                                   W. GUBLER AND J. RABINOFF

  In this paper, we study semipositivity of piecewise linear functions on a good strictly k-
analytic space X . This completes our study of such functions in [GJR21], and generalizes
results given in [GM19] from the algebraic to the analytic setting.

Piecewise linear functions. Let X be a good strictly k-analytic space X (see Section 2
for more details on the prerequisites on non-Archimedean analytic spaces). We say that
h: X → R is piecewise linear if for any x ∈ X there are finitelyS  many strictly k-analytic
domains Vj and invertible analytic functions g j on Vj such that Vj is a neighbourhood
of x in X and such that h = log |g j | on Vj . An R-PL function is a real function which is
locally an R-linear combination of piecewise linear functions.
   The semipositivity condition can be best described in terms of Temkin’s reduction of
germs. To any point x ∈ X , Temkin associates [Tem00] the reduction red(X , x) of the
germ (X , x); this is a kind of Riemann–Zariski space defined over the residue field ek which
keeps track of all local formal models over the valuation ring of k. There is a canonical
homomorphism u 7→ Lu (x) from the space of germs of PL functions at x to Pic(red(X , x)).
This homomorphism extends to a homomorphism from the space of germs of R-PL func-
tions to Pic(red(X , x)) ⊗ R. We say that an R-PL function h is semipositive at x ∈ X if
Lu (x) is nef in Pic(red(X , x)) ⊗ R. See [GJR21, Section 6] for more details.

Lifting theorems. The idea is to relate the notion of numerical effectivity of the line
bundle Lu (x) on the reduction, which is a condition that is checked on curves embedded
in the special fiber of some formal model, to the plurisubharmonicity of u, which is a
condition that is by definition checked on curves embedded in the generic fiber. This is
made possible by a suitable local lifting theorem, which allows us locally to lift a subvariety
of the special fiber of a formal model to a Zariski-closed subspace of the analytic generic
fiber. This is the technical heart of the paper. We only describe here in the introduction
the affine lifting theorem, given in Theorem 3.1, which is of global nature.
Theorem 1.1. Let X be a strictly k-affinoid space with affine formal model X. Then for every
d-dimensional irreducible closed subvariety W of the special fibre of X, there is an irreducible
Zariski closed subspace Y of X of dimension d such that W is an irreducible component of
the special fibre of the formal closure of Y in X.
   For flat algebraic (but not necessarily affine) schemes over the valuation ring of k,
this was shown in [GK19, Theorem 4.1]. In the analytic setting, Theorem 1.1 does not
imply a global result, as a Zariski-closed subspace of an affinoid domain in an analytic
space does not usually extend to the whole space. This is the reason that we can prove
only locally a lifting theorem in case of an arbitrary good quasi-compact strictly k-analytic
space (Theorem 4.1). The argument is independent of Theorem 1.1 and is due to Antoine
Ducros.

1.2. Semipositivity and restriction to curves. The local lifting theorem shows that
semipositivity of R-PL functions is the analogue of plurisubharmonicity in the complex
setting, where psh is defined in terms of restriction to curves.
Theorem 1.3. Let x be a point of a good strictly analytic space X over k and let h: X → R
be R-PL. Then h is semipositive at x if and only if for every sufficiently small strictly analytic


## Published source GR1, PDF page 5

     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY        5

M (A ) of an affinoid algebra A . We denote by OX the sheaf of analytic functions on a
good analytic space X and by H (x) the completion of the residue field OX ,x /mX ,x . In this
paper, we are mainly concerned with good strictly analytic spaces, which means that we
can choose A above isomorphic to a quotient of a Tate algebra k〈x 1 , . . . , x n 〉. Here, we
recall that
                                      X                                             
                                             m
              k〈x 1 , . . . , x n〉 :=    am x ∈ k¹x 1 , . . . , x n º | lim |am | = 0
                                                              |m|→∞
                                  m

endowed with its Gauss norm. Similarly, we define the subring k◦ 〈x 1, . . . , x n 〉 assuming
all am ∈ k◦ in the above definition. For a (strictly) affinoid algebra A , the subring of
power bounded elements is denoted by A ◦ . The Berkovich spectrum of the Tate algebra
k〈x 1 , . . . , x n 〉 is the closed unit ball of dimension n denoted by Bn .
   For a good strictly k-analytic space X over k, we also consider the G-topology generated
by the strictly affinoid domains. This is most natural for comparison to rigid analytic
geometry: see [Ber93, 1.6].
   An important tool is the relative boundary of a morphism ϕ : X → Y of good k-analytic
spaces. This is a closed subset of X which we denote by ∂ (X /Y ). See [Ber90, §2.5 and
§3.1] for the definition and properties. The complement Int(X /Y ) := X \∂ (X /Y ) is called
the relative interior. Most often we will apply this in the case Y = M (k), in which case
we just set ∂ X := ∂ (X /M (k)). If ∂ X = ;, then we call X boundaryless.
   For a scheme Y of finite type over k, we denote by Y an the Berkovich analytification of
Y . This is a (good) boundaryless strictly k-analytic space. See [Ber90, §3.5] for details.

2.3. Models and formal geometry. Recall that a quasi-compact admissible formal scheme
over k◦ is a quasi-compact formal scheme X over k◦ such that X has an open covering by
affine formal schemes Spf(A) with A a k◦ -algebra which is topologically of finite type and
flat over k◦ . The generic fiber of X is defined on affines by Spf(A)η := M (A ⊗k◦ k), and
the special fibre is defined on affines by Spf(A)s := Spec(A ⊗k◦ ek). There is a canonical re-
duction map red: Xη → Xs which is surjective, anti-continuous, and functorial [GRW17,
Proposition 2.17].
Definition 2.4. Let X be a compact strictly k-analytic space. A formal k◦ -model of X is
a quasi-compact admissible formal scheme X over k◦ with an identification Xη = X . For
details, we refer to [Bos14].
  If L is a line bundle on X , then a formal k◦ -model (X, L) of (X , L) is a formal k◦ -model
X of X and a line bundle L on X with an identification L|X = L.
  A model (X, L) of (X , OX ) gives rise to a metric k kL on OX by requiring that for any
formal open subset U of X and for any frame s of L over U, we have kskL = 1 on Uη . Then
we have an associated (continuous) function hL := − log k1kL on X .
  Let X be a formal k◦ -model of X . The isomorphism classes of line bundles L on X
equipped with an identification L|X = OX form an abelian group denoted by M (X). We
call the elements of the group M (X)Λ := M (X) ⊗Z Λ models of OX with coefficients in Λ.
For L ∈ M (X), we define the metric k kL and the function L by using the above and
Λ-linearity.


## Published source GR1, PDF page 6

6                                    W. GUBLER AND J. RABINOFF

  For generalization of these notions to a paracompact good strictly k-analytic space X ,
we refer to [GJR21, §2.4, 5.4, 5.6].
2.5. PL functions. Let k be a non-trivially valued non-Archimedean field. We fix an
additive subgroup Λ of R which is either divisible or equal to Z. We consider a good,
strictly k-analytic space XP  . A function h: X → R is called Λ-piecewise linear or Λ-PL
if G-locally we have h = j λ j log | f j | for finitely many λ j ∈ Λ and invertible analytic
functions f j . Equivalently, every x ∈ X has a compact strictly analytic neighborhood U,
a formal model U of U, and a formal model L of OU on U with coefficients in Λ, such that
h|U = hL := − log k · kL . See [GJR21, Proposition 5.8].
2.6. Polyhedral geometry. Let R be a subring of R an let Γ be an R-submodule of R. We
say that a function f : Rn → R is (R, Γ )-linear if f is an affine function of the form
                                   f (x) = m1 x 1 + . . . mn x n + c
with m1 , . . . , mn ∈ R and c ∈ Γ . A polyhedron ∆ is a finite intersection of half-spaces
H i := {x ∈ Rn | f i (x) ≥ 0} for affine functions f i . If all f i can be chosen to be (R, Γ )-linear,
we call ∆ an (R, Γ )-polyhedron. A face of ∆ is the intersection of ∆ with the boundary
of a half-space H ⊃ ∆. We allow also ; and ∆ as faces of ∆. A bounded polyhedron is
called a polytope.
   A polyhedral complex is a set C of polyhedra in Rn satisfying the following axioms:
     (1) If ∆ ∈ C , then all faces of ∆ are in C .
     (2) If ∆, ∆′ ∈ C , then ∆ ∩ ∆′ is a face of ∆ and of ∆′ .

                                3. THE AFFINE LIFTING THEOREM
  We fix a field k equipped with a nontrivial, non-Archimedean valuation val: k → R ∪
{∞} and associated absolute value | · | = exp(− val( · )).
  Let X = Spf(A) be an affine admissible formal scheme over k◦ with generic fiber X =
M (A ), where A = A ⊗k◦ k. Set n = dim(X ), and write As = A ⊗k◦ ek and Xs = Spec(As )
for the special fiber of X.
  Let Y ⊂ X be a Zariski-closed subspace, defined by an ideal I ⊂ A . The closure of
Y in X is the Zariski-closed formal subscheme (Y )X = Spf(A/(A ∩ I)) ⊂ X. This is k◦◦ -
torsionfree, so by [BL93a, Proposition 1.1(c)], it is again an admissible formal scheme
over k◦ . Note that the analytic generic fiber of (Y )X is Y . We refer to [Gub98, Proposition
3.3] for details.
Theorem 3.1 (Affine Lifting Theorem). Let X be an affine admissible formal scheme over
k◦ with generic fiber X . Let W ⊂ Xs be an irreducible Zariski-closed subset of dimension d.
Then there is a pure-dimensional Zariski-closed subspace Y ⊂ X of dimension d such that
W is an irreducible component of the special fiber of (Y )X .
   For flat algebraic schemes over k◦ , this was shown in [GK19, Theorem 4.1].
   Under the hypotheses of Theorem 3.1, we let Y = (Y )X for any pure dimensional
Zariski-closed subset Y . Then the special fiber Ys is pure-dimensional of the same di-
mension as Y by [GRW17, Proposition 2.7(3)]. If W is an irreducible component of Ys ,
it follows that dim(Y ) is automatically equal to dim(W ).


## Published source GR1, PDF page 15

     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY         15

                             5. SEMIPOSITIVE R-PL FUNCTIONS
   Let k be a non-trivially valued non-Archimedean field. We consider a good, strictly
k-analytic space X . We refer to 2.5 for the definition of PL functions. Recall from the in-
troduction that an R-PL function u: X → R is called semipositive at x ∈ X if the associated
residue line bundle Lu (x) ∈ Pic(red(X , x))R is nef, where we refer to [GJR21, 6.16–6.19]
for residue line bundles. Equivalently, there is a strictly affinoid neighbourhood U of x
such that u = hL for a formal k◦ -model (U, L) of (U, OU ) with L nef [GJR21, Proposition
7.1].
   We will show first that for an R-PL function on a smooth curve, semipositivity is the
same as subharmonicity in the sense of Thuillier’s thesis [Thu05, Définition 3.1.5]. Re-
call that Thuillier defines a subharmonic function on a smooth k-analytic curve X as a
semicontinuous function u: X → R ∪ {−∞} which is not identically −∞ on any con-
nected component of X and which has the property that for every harmonic function h
on a strictly affinoid domain U of X with u|∂ U ≤ h|∂ U , we have u|U ≤ h.

Proposition 5.1. Let X be a smooth, strictly k-analytic curve and let u: X → R be an R-PL
function. Then u is subharmonic at x ∈ X in the sense of Thuillier if and only if Lu (x) is nef.

Proof. First we treat the case when k is algebraically closed. As explained in 2.5, there
exists a compact strictly analytic neighborhood U of x in X , a formal k◦ -model U of U,
and a formal model L of OU such that u|U = hL . Since k is algebraically closed, we may
assume that the special fiber Us is reduced, which implies that U is covered by formal
affines of the form Spf(A ◦ ) for a strictly k-affinoid algebra A [GJR21, §2.4]. It follows
from [Ber90, Proposition 2.4.4] that for every irreducible component Y of Us , there is a
unique point ξY ∈ U reducing to the generic point of Y . In the formalism of real valued
forms and currents on Berkovich spaces [CD12], it is well known that d′ d′′ [u]|U is the
discrete measure on U supported on the points ξY of U for Y an irreducible component
of Us , with multiplicity at ξY equal to degL (Y ). See [CD12, §6.9] for a more general
statement. Wanner showed that subharmonicity of u on U is equivalent to the positivity
of the current d′ d′′ [u]: see [Wan19, Theorems 1 and 2] and use the fact that X is locally
algebraic [vdP80]. Thus Ls is nef if and only if u is subharmonic on U. Suppose that u is
subharmonic at x. Shrinking U, we may assume that u is subharmonic on U. This implies
that Ls is nef, so it follows from [GJR21, Proposition 7.1] that Lu (x) is nef. Conversely, if
Lu (x) is nef, then by [GJR21, Proposition 7.1], we may shrink U so that Ls is nef, which
as above implies that u is subharmonic on U.
   It remains to show that subharmonicity of u at x and numerical effectivity of Lu (x)
can be checked after extending scalars to the completion of an algebraic closure K =
(k)∧ . By [GJR21, Proposition 7.6(2)], one can check that Lh (x) is nef after base change
to K. The same is true for subharmonicity: this follows directly from Thuillier’s definition
and the fact that the base change of a harmonic function remains harmonic [Thu05,
Proposition 2.3.18].                                                                       

  Our next goal is a characterisation of semipositive R-PL functions by restriction to
subcurves as in the complex case. We need the following characterization of boundary
points:


## Published source GR1, PDF page 16

16                                W. GUBLER AND J. RABINOFF

5.2. Let X be an admissible formal k◦ -scheme and let x ∈ Xη . Then x ∈ Int(X ) = X \ ∂ X
if and only if the closure of redX (x) is a proper ek-scheme. This follows from [CD12,
Lemme 6.5.1] in the separated case and from [Vil21, Corollary A.4] in general.
Theorem 5.3. Let X be a good, strictly k-analytic space, and let h: X → R be an R-PL
function. For x ∈ X , the following conditions are equivalent.
    (1) The function h is semipositive at x.
    (2) There is a neighborhood W of x such for every strictly analytic neighborhood U ⊂ W
        of x and every Zariski-closed curve C in U, the restriction h|C is semipositive.
Proof. Since semipositivity is an open property that is stable under pullback [GJR21,
Proposition 7.6], it is clear that (1) yields (2).
   Assume that h satisfies (2). By shrinking W , we may assume that W is a strictly affinoid
neighborhood of x and that there is a formal model W of U and a model L of OW on W
with coefficients in R such that h = hL on W . Let Y ⊂ Ws be a curve which is proper over
the residue field ek. To prove semipositivity at x, it is enough to show that degL (Y ) ≥ 0.
   Choose any point y ∈ W reducing to the generic point η of Y . By Theorem 4.1 as
applied to X = W and X = W, there exist z ∈ W with redW (z) = η, a neighborhood U
of z in W , and an irreducible 1-dimensional Zariski-closed subspace C of U containing
z. By shrinking U, we may assume that U is strictly affinoid. By results of Bosch and
Lütkebohmert [Bos14, Theorem 8.4.3] [BL93b, Corollary 5.4(b)], there is a formal model
U of U and a morphism π: U → W extending the inclusion U ,→ W on generic fibers. Let
C be the formal closure of C in U. This is an admissible formal model of C whose special
fiber Cs is a closed 1-dimensional subscheme of Us containing η′ = redU (z). Functoriality
of reductions shows that π(η′ ) = η, so the closure Y ′ of η′ is a curve mapping to Y .
Since the closure of η in Ws is the proper curve Y , we conclude from 5.2 that z ∈ W \
∂ W . The boundary ∂ U is the union of ∂ W ∩ U with the topological boundary of U in
W [Ber90, Proposition 3.1.3], so since U is a neighborhood of z in W , we have z ∈ U \∂ U.
Applying 5.2 to U and its formal model U shows that Y ′ is proper as well. Therefore,
the map Y ′ → Y is finite and surjective. Note that Y ′ is an irreducible component of Cs .
Applying (2) to U and C, we have that h|C is semipositive, and so we deduce from [GJR21,
Lemma 7.4] as applied to (π∗L)|C that degπ∗ L (Y ′ ) ≥ 0. The projection formula then shows
degL (Y ) ≥ 0, as required.                                                                
   To apply results from Thuillier’s thesis [Thu05], we would like to use only smooth an-
alytic curves. To give a variant of the above result suitable for this purpose, we introduce
the following notations:
   For a real function h on X and an analytic field extension F of k, we denote by h F
the induced function on the base change X F = X ⊗     b k F of X . We call an R-PL function
h pluriharmonic if ±h are both semipositive. A strictly k-analytic space X is called rig-
smooth if the sheaf of Kähler differentials, considered on the G-topology, is locally free of
rank equal to the local dimension. The space X is smooth if and only if X is rig-smooth and
boundaryless. See [Duc18] for details (Ducros calls rig-smooth spaces quasi-smooth).
Corollary 5.4. Let X be a good, strictly k-analytic space and let h: X → R be an R-PL
function. Then the following conditions are equivalent:


## Published source GR1, PDF page 17

     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY        17

   (1) The function h is semipositive (resp. pluriharmonic).
   (2) There is an algebraically closed analytic field extension F of k such that for every
       rig-smooth analytic curve C over F and every morphism ϕ : C → X F , the function
       h F ◦ ϕ is semipositive (resp. harmonic) on C.
   (3) There is an algebraically closed analytic field extension F of k such that for every
       smooth analytic curve C over F and every morphism ϕ : C → X F , the function h F ◦ϕ
       is semipositive (resp. harmonic) on C.

   If (2) or (3) is true for an algebraically closed analytic field extension F of k, then
it is true for all analytic field extensions. This follows from Corollary 5.4 and Propo-
sition [GJR21, Proposition 7.6(2’)] which allows to check semipositivity over any field
extension.

Proof. It is enough to prove the claim for semipositive functions, as h is pluriharmonic if
and only if h and −h are semipositive. Since semipositivity is stable under pullback and
extension of scalars [GJR21, Proposition 7.6], clearly (1) yields (2). Since a smooth an-
alytic curve is just a boundaryless rig-smooth curve, it is clear that (2) yields (3). In fact,
these two conditions are equivalent as an R-PL function is automatically semipositive in
every boundary point y of an analytic curve C. Indeed, it follows from 5.2 that red(C, y)
is non-proper and hence there is no condition for semipositivity at y.
   It remains to show that that (2) yields (1). Assume that (2) holds. By base change
using [GJR21, Proposition 7.6(2’)], we may assume that k = F . Let x ∈ X and let U be
a strictly analytic neighborhood of x. For any Zariski-closed curve Y in U, we will show
that h|Y is semipositive. Replacing Y by Yred and using [GJR21, Proposition 7.6(3’)], we
may assume that Y is reduced. Let ϕ : C → Y be the normalization of Y (see [Ber90]
before Proposition 3.1.8). Then C is a rig-smooth curve because k is perfect (it is alge-
braically closed). By (2), the function h ◦ ϕ is semipositive on C. Since the normalization
morphism is finite and surjective, it follows from [GJR21, Proposition 7.6(1’)] that h|Y is
semipositive. By Theorem 5.3, we conclude that h is semipositive at x. Since x was an
arbitrary point of X , we get (1).                                                           
Corollary 5.5. Let X be a good, strictly k-analytic space and let Λ be either Z or Q. Let
h1 , h2 : X → R be semipositive Λ-PL functions. Then max(h1 , h2 ) is a semipositive Λ-PL
function.

  Corollary 5.5 fails for Λ strictly containing Q, but only because we restrict ourselves to
the G-topology generated by strictly analytic domains. See [GJR21, Example 5.3].

Proof. We first note that max(h1 , h2 ) is a Λ-PL function [GJR21, Remark 5.2]. Using
Corollary 5.4, it is enough to prove that max(h1 , h2 ) is semipositive in case of a smooth
analytic curve X . Since the maximum of two subharmonic functions on such a curve is
subharmonic [Thu05, Proposition 3.1.8], the claim follows from Proposition 5.1.          

Theorem 5.6. Let X be a good, strictly k-analytic space and let (h j ) j∈N be a sequence of
semipositive R-PL functions on X converging pointwise to an R-PL function h. Then h is
semipositive.


## Published source GJR, PDF page 31

               FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                       31

use the G-topology on X generated by the strictly affinoid domains. Let C(X ) be the space
of continuous real functions on X .
Definition 5.1. A function h: X → R is called piecewise Λ-linear or Λ-PL if there exists a
                                                                                                    ×
G-covering {XP i } of X such that for each i, there are finitely many λi j ∈ Λ and f i j ∈ O (X i )
with h|X i = j λi j log | f i j |. A Z-PL function is called piecewise linear or PL.
  We denote the group of PL functions on X by PL(X ), and the group of Λ-PL functions
by PLΛ (X ). These are subgroups of C(X ).
5.2. Some remarks:
   (1) A function h: X → R is PL if and only if there exists a G-covering {X i } of X and
       f i ∈ O (X i )× such that h|X i = log | f i |.
   (2) The set of Λ-PL functions on X forms a group since any two G-coverings {X i } and
       {X ′j } admit the common refinement {X i ∩ X ′j }.
   (3) The restriction of a Λ-PL function to a strictly analytic domain is Λ-PL.
   (4) The presheaf U 7→ PLΛ (U) is a sheaf in the G-topology, and therefore in the ana-
       lytic topology as well.
   (5) A function h: X → R is Λ-PL if and only if there exists a G-covering {X i } of
       X suchPthat for each i, there are finitely many λi j ∈ Λ and hi j ∈ PL(X i ) with
       h|X i = j λi j hi j .
   (6) A function h: X → R is Q-PL if and only if, locally in the analytic topology, there
       exists a positive integer N such that N h is PL.
   (7) If Λ = Z or Λ = Q then the minimum and maximum of two Λ-PL functions is
       again Λ-PL by [GM19, Proposition 2.12(d)].
Example 5.3. The assertion of 5.2(7) is not true for Λ strictly containing Q. For example,
if the value group of K is Q and X = Gan m
                                            = Spec(K[t ±1])an is the split torus of rank 1, then
the tropicalization of any strictly affinoid domain in X is a union of compact intervals with
rational vertices. We conclude that for Λ = R, the function h := π log |t|+1 = −π trop +1
is Λ-PL, but max(h, 0) is not Λ-PL as max(h, 0) = ϕ ◦ trop for ϕ(u) = max(−πu + 1, 0),
and as the piecewise linear function ϕ has a bend at the irrational number 1/π.
  Here we list some basic functoriality properties of Λ-PL functions.
Lemma 5.4. Let h: X → R be a function.
   (1) Let f : X ′ → X be a morphism of good strictly K-analytic spaces. If h ∈ PLΛ (X ) then
       h ◦ f ∈ PLΛ (X ′ ).
   (2) Let K ′ /K be a non-Archimedean field extension, let X ′ = X ⊗
                                                                    b K K ′ , and let π: X ′ → X
       be the structure morphism. If h ∈ PLΛ (X ) then h ◦ π ∈ PLΛ (X ′ ).
   (3) Let ι : X red → X be the inclusion of the reduction of X , and let h′ = h ◦ ι. Then
       h ∈ PLΛ (X ) if and only if h′ ∈ PLΛ (X red ).
Proof. The first two assertions are obvious. For the third, by (1), the only thing to show is
that if h′ is Λ-PL then h is Λ-PL. Let U = M (A ) ⊂ X be a strictly    Paffinoid domain, and let
                                                           ′                                    ×
Ured = M (Ared ) ⊂ X red be its reduction. Suppose that P h |Ured = λi log |g i | for g i ∈ Ared  .
If f i ∈ A lifts g i then f i ∈ A × is a unit, and h|U = λi log | f i |. Since X red has a G-cover
by such affinoid domains, the same is true for X , so h is Λ-PL.                                 


## Published source GJR, PDF page 44

44                                 W. GUBLER, P. JELL, AND J. RABINOFF

ℓ: Pic(red(X , x))Λ → R, and
                                                     X
                                                     r
                                   0 = ℓ(Lh (x)) =          λi ℓ(Lhi (x))
                                                      i=1

is a non-trivial Q-linear combination of λ1 , . . . , λ r which is a contradiction.                     
6.19 (Functoriality of residues). Let f : (X ′ , x ′ ) → (X , x) be a morphism of good strictly
K-analytic germs. For h ∈ PLΛ (X , x), we get h′ = h ◦ f ∈ PLΛ (X ′ , x ′ ). We have an induced
morphism fe : red(X ′ , x ′ ) → red(X , x), and Lh′ (x ′ ) = fe∗ Lh (x) by [CD12, 6.6.7]. A similar
statement holds for extension of scalars.

                          7. SEMIPOSITIVITY AND HARMONIC FUNCTIONS
   In this section, we study positivity conditions on piecewise linear functions. We will
introduce the crucial notion of a harmonic function, on which our theory of differential
forms rests. We consider a good strictly K-analytic space X and an additive subgroup
Λ ⊂ R. We will always assume that Λ = Z or that Λ is divisible.
   We can characterize semipositivity either in terms of formal geometry or residues of
Λ-PL functions, as elaborated in 6. A line bundle L on an admissible formal scheme X
is called nef (resp. numerically trivial) if its restriction to Xs has the same property. In
other words, the line bundle L is nef if the degree of L|C is nonnegative for every closed
integral curve C ⊂ Xs which is proper over K   e .5
   Let X be a formal K ◦ -model of a paracompact good strictly K-analytic space X . Recall
from 5.5 that M (X) denotes the group of models of OX , and that we have defined a
homomorphism h 7→ hL : M (X)Λ → PL(X )Λ . We will also use the residue Lh (x) of h at
x ∈ X from 6.16.
Proposition 7.1. Let h: X → R be a Λ-PL function and x ∈ X . The following are equivalent:
         (1) There exists a paracompact neighbourhood U of x in X , a formal K ◦ -model U of U,
             and a nef (resp. numerically trivial) element L ∈ M (U)Λ , such that h|U = hL .
         (2) The residue Lh (x) ∈ Pic(red(X , x))Λ is nef (resp. numerically trivial).
Proof. The first assertion implies the second by the description of Lh (x) in 6.16. We will
prove the nef case, as the numerically trivial case is identical. The following argument
is similar to [GK19, Proposition 6.5]. Suppose that Lh (x) is nef. By Corollary 5.9, there
exists a compact strictly analytic neighbourhood U of x, a formal K ◦ -model U of U, and an
element L ∈ M (U)Λ , such that h = hL . As in 6.16 we let VU,x be the closure of redU (x) and
we let LU,x be the restriction of L to VU,x . Then (VU,x , LU,x ) is a model of (red(X , x), Lh (x)),
so LU,x is nef by Lemma 6.11. Let W be a compact, strictly analytic neighbourhood of x
contained in the open set red−1 U
                                    (VU,x ). By [BL93a, Lemma 4.4], there exists an admissible
formal blowup f : U′ → U such that W = Wη for a formal open subset W ⊂ U′ . Note that
h|W = h f ∗ L|W . We claim that f ∗ L|W is nef.
     5
    If X is a proper K ◦ -model of a proper variety X over K and L is a line bundle on X with L = L |X
such that the restriction of L to the special fiber of X is nef, then L is a nef line bundle on X by [GM19,
4.8].


## Published source GJR, PDF page 45

              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                 45

  By functoriality of reductions, the set-theoretic image of W under f is contained in
VU,x . In particular, if C is any integral, proper subcurve of Ws , then f (C) ⊂ VU,x . Since
C is reduced, the schematic image of C is contained in VU,x , so we have a commutative
square of morphisms of ek-schemes:
                                            C    /W
                                                       s
                                        f              f
                                                  
                                        VU,x     /U
                                                       s

Since LU,x is nef, we have f ∗ LU,x .C ≥ 0 by the projection formula.                       
Definition 7.2. A Λ-PL function h: X → R is called semipositive at a point x ∈ X if it
satisfies the equivalent conditions of Proposition 7.1, and it is harmonic at x if both h
and −h are semipositive at x. We say that h is semipositive if it is semipositive at all
points of X .
   A harmonic function on X is an R-PL function h: X → R which is harmonic at all points
of X . A Λ-PL harmonic function is called Λ-harmonic.
7.3. Some remarks:
   (1) A Λ-PL function h is harmonic at x ∈ X if and only if Lh (x) is numerically trivial.
       Equivalently, there exists a paracompact neighbourhood U of x, a formal K ◦ -
       model U of U, and a numerically trivial element L ∈ M (U)Λ , such that h = hL .
   (2) Semipositivity and harmonicity are insensitive to the group Λ, in the following
       sense: if h ∈ PLΛ (X ), then h is semipositive at a point x if and only if its image in
       PLR (X ) is semipositive at x.
   (3) Semipositivity and harmonicity of h at x is intrinsic to the germ of h in PLΛ (X , x).
       In particular, the semipositive (resp. harmonic) functions on X form a sheaf in
       the analytic topology. (They do not form a sheaf in the G-topology).
   (4) It follows from Proposition 7.1(1) that the locus of all points x ∈ X at which h is
       semipositive (resp. harmonic) is open.
   (5) The set of semipositive functions at a point forms a monoid (resp. a cone if
       Λ = R), and the set of harmonic functions at a point forms a group (resp. an
       R-subspace).
   (6) If h = log | f | for an invertible analytic function f in a neighbourhood of x, then h
       is harmonic at x by Lemma 6.17 (the converse does not hold: see Remark 15.10).
   (7) Harmonic functions generalize smooth functions in the same way that numerical
       equivalence generalizes rational equivalence in algebraic geometry.
Lemma 7.4. Suppose that X is paracompact. Let X be a formal K ◦ -model of X and let L ∈
M (X)Λ . Then hL is semipositive (resp. harmonic) if and only if L is nef (resp. numerically
trivial).
Proof. The harmonic case follows from the semipositive case. If L is nef then hL is semi-
positive by definition. Suppose then that h := hL is semipositive. Let C ⊂ Xs be an
integral, proper closed curve. By surjectivity of redX , there exists a point x ∈ X reducing
to the generic point of C. Then (C, L|C ) is a model of (red(X , x), Lh (x)), so L|C is nef by
Lemma 6.11. In particular, c1 (L).C ≥ 0, so L is nef.                                       


## Published source GJR, PDF page 46

46                               W. GUBLER, P. JELL, AND J. RABINOFF

  Combined with 5.6, we see that a PL function h: X → R on a paracompact space X is
semipositive (resp. harmonic) if and only if there exists a formal K ◦ -model X of X and a
nef (resp. numerically trivial) line bundle L ∈ M (X) such that h = hL = − log k1kL .
  We have the following alternative characterization of harmonic functions. We do not
know if the same characterization holds for semipositive functions.
Proposition 7.5. Let h: X → R be a Λ-PL function and let x ∈ X . Then h is harmonic Pm at x
if and only if there exists a strictly analytic neighbourhood U of x such that h|U = i=1 λi hi
for Z-harmonic functions h1 , . . . , hm on U and λ1 , . . . , λm ∈ Λ.
Proof. The proposition is vacuous when Λ = Z, so assume Λ is divisible. The “if” direc-
tion is trivial. Suppose then thatPmh is harmonic at x. By Proposition 5.8, after shrinking
X , we may assume that h = i=1 λi hi for λ1 , . . . , λm ∈ Λ and h1 , . . . , hm ∈ PL(X ). By
Lemma 5.10, we may assume that   Pm λ1 , . . . , λm are Q-linearly independent. By Lemma 6.18,
the residue Lh (x) is equal to i=1 λi Lhi (x). Let V be a model for red(X , x) in the sense
of 6.2 such that each Lhi (x) is the pullback of a line bundle L V,i on V . Let C ⊂ V be an inte-
                                                                            Pm
gral, proper closed curve. Since Lh (x) is numerically trivial, we have i=1 λi c1 (L V,i (x)).C =
0. But c1 (L V,i (x)).C ∈ Z for each i, so by linear independence, we have c1 (L V,i (x)).C = 0
for each i. Thus L V,i is numerically trivial, so hi is harmonic.                              
     Now we gather some functoriality properties of semipositive and harmonic functions.
Proposition 7.6. Let X be a good strictly K-analytic space and let h ∈ PLΛ (X ).
   Let f : X ′ → X be a morphism of good strictly K-analytic spaces and let h′ = h ◦ f .
     (1) For x ′ ∈ X ′ , let x = f (x ′ ). If h is semipositive at x, then h′ is semipositive at x ′ .
           The converse holds if x ′ ∈ Int(X ′ /X ).
    (1′ ) If h is semipositive, then h′ is semipositive. The converse holds if f is proper and
           surjective.
Let K /K be a non-Archimedean field extension, let X ′ = X ⊗
       ′                                                             b K K ′ , let π: X ′ → X be the
structure morphism, let x ′ ∈ X ′ , let x = π(x ′ ), and let h′ = h ◦ π.
     (2) If h is semipositive at x, then h′ is semipositive at x ′ . The converse holds if we have
           tr.deg(Ke ′H  f(x)/K
                              e ′ ) = tr.deg(Hf(x)/K e ), where K
                                                                e ′H
                                                                   f(x) is the smallest subfield of
           Hf(x ) containing H
                 ′                f(x) and K e.′

    (2 ) The function h is semipositive if and only if h′ is semipositive.
       ′

Let ι : X red → X be the inclusion of the reduction of X and let h′ = h ◦ ι.
     (3) For x ′ ∈ X red , the function h is semipositive at x = ι(x ′ ) if and only if h′ is semipos-
           itive at x ′ .
    (3 ) The function h is semipositive if and only if h′ is semipositive.
       ′

The statements (1)–(3) and (1′ )–(3′ ) hold with “semipositive” replaced by “harmonic.”
Proof. In each case, harmonicity follows easily from semipositivity. In all cases, the func-
tion h′ is Λ-PL by Lemma 5.4.
   We prove first (1). If h is semipositive at x then h′ is semipositive at x ′ by Lemma 6.12
and functoriality of reduction. The converse holds if x ∈ Int(X ′ /X ) by Theorem 6.15
and Lemma 6.12(1), using functoriality of residues 6.19. Assertion (1′ ) follows because
a proper morphism has no boundary.


## Published source GJR, PDF page 47

                 FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             47

  To prove (2), let ϕ : PHf(x ′ )/Ke ′ → PHf(x)/Ke be the natural morphism. We have seen in 6.13
that ϕ −1 (red(X , x)) = red(X ′ , x ′ ). The assertions now follow from Lemma 6.12 and
functoriality of residues 6.19. To prove (2′ ), by Corollary 5.9 we may shrink X such that
X is compact with formal model X and such that there is L ∈ M (X)Λ with h = hL . Then
the claim follows from Lemma 6.8(2) and Lemma 7.4.
  The claims (3) and (3′ ) follow from (7.6,1′ ) since X red → X is proper and surjective. 
 The following proposition allows us to pass to Galois extensions when studying har-
monic and semipositive functions.
Proposition 7.7. Suppose that Λ is divisible. Let L/K be a (potentially infinite) normal
extension with automorphism group G := Aut(L/K). Let K ′ be the completion of L and let
X ′ := X ⊗
         b K K ′ , with structure morphism π: X ′ → X . Then h 7→ h ◦ π induces an isomor-
phism from the monoid of semipositive Λ-PL functions on X (resp. the group of Λ-harmonic
functions on X ) to the monoid of G-invariant semipositive Λ-PL functions on X ′ (resp. the
group of G-invariant Λ-harmonic functions on X ′ ).
Proof. This is an immediate consequence of Corollary 5.13 and Proposition 7.6(2′ ).                       
  Our next goal is to approximate locally semipositive metrics by local Fubini–Study
metrics (Proposition 7.10). This will be a crucial ingredient in proving the balancing
condition in Section 9.
  Recall that a line bundle on a scheme Y is called semiample if some positive tensor
power is globally generated. We say that L ∈ Pic(Y )R is ample (resp. semiample) if there
P r ample (resp. semiample) line bundles H1 , . . . , H r and λ1 , . . . , λ r ∈ R≥0 such that L =
are
     λ H ∈ Pic(Y )R . An ample L is semiample and a semiample L is nef.
  j=1 j j

Definition 7.8. Let h: X → R be an R-PL function. We say that h is Fubini–Study at a
point x ∈ X if Lh (x) is semiample. We say that h is locally Fubini–Study or LFS if it is
Fubini–Study at every point of X .
  Clearly if h is Fubini–Study at x then it is semipositive at x.
7.9. It follows from [CD12, Proposition 6.8.2] that h is Fubini–Study at x if and only if
there is an open neighbourhood U of x such that h|U is an R≥0 -linear combination of func-
tions of the form max{− log | f1 |, . . . , − log | f n |} for invertible analytic functions f1 , . . . , f n
on U.
  The following proposition can be seen as a local analogue of the fact that one can
approximate a nef Q-line bundle by ample Q-line bundles on a projective variety.
Proposition 7.10. Let h: X → R be an R-PL function that is semipositive at a point x ∈
Int(X ). Then there exists a strictly analytic neighbourhood U of x and a sequence h1 , h2 , . . .
of R-PL LFS functions on U such that hi → h|U uniformly.
Proof. We may shrink X to assume it is compact. By Corollary 5.9, we may assume that
there exists a formal K ◦ -model X of X and a line bundle L ∈ M (X)R with h = hL , using
the notation of 5.7. Since x is inner, the closure VX,x of redX (x) in Xs is proper (with the
notation of 6.13): see [CD12, Lemma 6.5.1] and [Vil21, Appendix A]. By Chow’s lemma,


## Published source Thu, PDF page 76

62



Remarque 3.1.4.  Puisque, pour tout domaine stri tement k-anoïde Y , l'espa e ve to-
riel H(Y ) est de dimension nie, la limite h d'une suite simplement onvergente de fon tions
harmoniques sur un ouvert Ω de X est harmonique et la onvergen e est lo alement uniforme
sur Ω.

  Les propriétés du fais eau HX énon ées dans les trois paragraphes pré édents permettent,
en re opiant les démonstration du paragraphe 2.2 du hapitre V de [Ahl℄, de résoudre le
problème de Diri hlet par la méthode de Perron ; e i est l'objet de la n de la se tion 3.1.

3.1.2. Fon tions sous-harmoniques.
Définition 3.1.5.  Soit Ω un ouvert de X ; une fon tion u : Ω → R ∪ {−∞} est dite
sous-harmonique si elle est semi- ontinue supérieurement, n'est identiquement égale à −∞
sur au une omposante onnexe de Ω et satisfait à la ondition suivante : pour tout domaine
stri tement k-anoïde Y dans X et toute fon tion h ∈ H(Y ),
                                  (u|∂Y ≤ h|∂Y ) =⇒ (u|Y ≤ h).

     L'assertion suivante n'est pas surprenante.
Proposition 3.1.6.  Soient Ω ⊂ X un ouvert et f ∈ Γ(Ω, OX ) une se tion inversible
sur un ouvert dense de Ω ; la fon tion log |f | est sous-harmonique sur Ω.
Démonstration. La fon tion log |f | est ontinue sur Ω et, f étant inversible sur un ouvert
dense, n'est identiquement égale à −∞ sur au une des omposante onnexes de Ω.
   Soient Y ⊂ Ω un domaine stri tement k-anoïde et h ∈ H(Y ) une fon tion majorant log |f |
sur Γ(Y ) = ∂Y ; puisqu'il sut de prouver l'inégalité log |f ||Y ≤ h après avoir ee tué une
extension nie k′ de k, nous pouvons supposer que Y est la bre générique d'une S - ourbe
simplement semi-stable Y , de squelette S(Y) et de rétra tion τY : Y → S(Y). Dans es
 onditions :
    H = h|S(Y) ∈ H(S(Y), Γ(Y )) et h = H ◦ τY ;
    la fon tion F = log |f ||S(Y) est sous-harmonique sur S(Y) − Γ(Y ) (proposition 2.2.24,
     (iii)) et log |f ||Y ≤ F ◦ τY (proposition 2.2.24, (ii)) ;
la on lusion dé oule alors de l'inégalité F ≤ H sur S(Y).                                  2
Remarque 3.1.7.  Nous verrons plus loin (proposition 3.4.6) que, pour toute S - ourbe
simplement semi-stable X et toute fon tion sous-harmonique u sur Xη − Γ(Xη ), la restri tion
U de u à S(X ) − Γ(Xη ) est sous-harmonique (= onvexe) : ddc U ≥ 0, l'opérateur ddc étant
entendu au sens des ourants, omme expliqué à en 1.2.5.

     Les propriétés suivantes des fon tions sous-harmoniques sont évidentes.
Proposition 3.1.8.  Étant donné un ouvert Ω de X ,
   (i ) l'ensemble des fon tions sous-harmoniques sur Ω est un ne réel stable par max : pour
toutes fon tions u, v sous-harmoniques sur Ω et tous nombres réels positifs µ, ν , les fon tions
µu + νv et max(u, v) sont sous-harmoniques sur Ω ;
   (ii ) l'enveloppe inférieure d'une famille dé roissante de fon tions sous-harmoniques sur Ω
est, sur ha une des omposantes onnexes de Ω, sous-harmonique ou identiquement égale à
−∞ ;
   (iii ) la régularisation semi- ontinue supérieurement de l'enveloppe supérieure d'une famille
 roissante et lo alement bornée de fon tions sous-harmoniques sur Ω est sous-harmonique.

     Le ne des fon tions sous-harmoniques sur un ouvert Ω de X est noté SH(Ω).


## Published source Thu, PDF page 105

                                                                                                 91



par appli ation du point (ii) du orollaire 3.2.11 et don y = x, (ddc ϕ)|V −∂V ≥ 0.
  Ce i établit la positivité de la forme lisse ddc ϕ.                                             2

Corollaire 3.4.5.  Soient X          une ourbe stri tement k-analytique lisse, K/k une ex-
tension non ar himédienne et pK : X ⊗    b k K → X la proje tion anonique ; étant donnée une
fon tion sous-harmonique u sur X , la fon tion p∗K u est sous-harmonique sur X ⊗    b kK.
Démonstration. Puisqu'il est loisible de raisonner lo alement, nous pouvons, en vertu du
théorème 3.4.2, supposer que u est l'enveloppe inférieure d'une famille (ϕλ ) de fon tions sous-
harmoniques lisses. La fon tion pK ∗u est alors l'enveloppe inférieure de la famille de fon tions
lisses p∗K ϕλ et il sut don de traiter le as d'une fon tion sous-harmonique lisse.
   Soit u une fon tion sous-harmonique lisse et vérions que la mesure ddc p∗K u est positive.
La formule
                                   ddc p∗K u = pK ′ /K ∗ ddc p∗K ′ u
pour toute extension non ar himédienne K ′ /K (théorème 3.2.10) permet d'agrandir K à loisir.
Considérons un domaine stri tement k-anoïde Y ⊂ X et une extension nie k′ /k telle que
Y ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable Y
et que la fon tion p∗k′ u s'é rive sous la forme U ◦ τ , ave U ∈ A0 (S(Y)) (proposition 3.2.4) ;
la sous-harmoni ité de u implique elle de U puisque ddc U = ddc u (théorème 3.2.10). Soient
maintenant K ′ une extension non ar himédienne de k oiant K et k′ et p : S(Y)K ′ → S(Y)
l'appli ation induite par la proje tion anonique de X ⊗   b k K ′ sur X ⊗k k′ . La fon tion p∗ U est
sous-harmonique sur S(Y)K et il en est par onséquent de même pour p∗K ′ u = p∗ U ◦ τK ′ .
    Comme mentionné au début de la démonstration, la sous-harmoni ité de p∗K ′ u implique
  elle de p∗K u.                                       2                                          2

   L'utilisation simultanée du théorème d'approximation et de la ara térisation des fon tions
sous-harmoniques lisses permet également de répondre à une question naturelle mentionnée
à la remarque 3.1.7.
Proposition 3.4.6.  Soient X           une S - ourbe simplement semi-stable et u une fon tion
sous-harmonique sur Xη ;
    la restri tion U de u au squelette S(X ) de X est une fon tion réelle sous-harmonique (=
      onvexe ) ontinue ;
    u ≤ U ◦ τX .
Démonstration. L'inégalité u ≤ U ◦ τX est une onséquen e immédiate du prin ipe du
maximum puisque les bres de la rétra tion τX sont des domaines k-anoïdes dont le bord
est réduit à un point.
   La restri tion U de u au squelette S(X ) est à valeurs nies ar S(X ) ⊂ I(Xη ) et, ompte
tenu du théorème 3.4.2, U est l'enveloppe inférieure d'une famille dé roissante de fon tions
qui sont les restri tions de fon tions lisses et sous-harmoniques sur Xη . Il est par onséquent
susant de prouver qu'une fon tion lisse et sous-harmonique ϕ sur Xη se restreint en une
fon tion ane par mor eaux et sous-harmonique sur le polyèdre S(X ).
   Nous pouvons supposer la ourbe quasi- ompa te puisque la question est lo ale sur S(X ) ;
l'assertion sera d'autre part démontrée si elle l'est après passage à une extension nie k′ de k.
Appliquant la proposition 3.2.4 et le lemme 2.2.22, il existe dans es onditions un é latement
admissible q : Y → X tel que :
    Y soit une S - ourbe simplement semi-stable,
    ϕ = Φ ◦ τY , ave Φ = ϕ|S(Y) ∈ A0 (S(Y)).
   La fon tion Φ est sous-harmonique puisque ddc Φ = ddc ϕ ≥ 0 (théorème 3.2.10).


## Published source Thu, PDF page 106

92



  D'après la proposition 2.2.26, S(X ) est un domaine polyédral dans S(Y) tel que haque
 omposante onnexe de S(Y)−S(X ) n'ait qu'un seul point frontière. Il en dé oule tout d'abord
que la restri tion Φ′ de ϕ à S(X ) est une fon tion ontinue et ane par mor eaux puisque
Φ′ = Φ|S(X ) . C'est en outre une fon tion sous-harmonique : Φ est en eet dé roissante au
voisinage de la frontière de S(Y) − S(X ) en vertu du prin ipe du maximum, e qui implique
                                        ddc Φ′ ≥ ddc Φ ≥ 0.
                                                                                                  2
Remarque 3.4.7.  Ré iproquement, étant donnée une S - ourbe simplement semi-stable
X et une fon tion sous-harmonique F sur S(X ), la fon tion τX∗ F est évidemment sous-
harmonique sur X : représentant F omme l'enveloppe inférieure d'une suite dé roissante
(Φn ) de fon tions anes par mor eaux et sous-harmoniques sur S(X ), τ ∗ F est l'enveloppe
inférieure de la suite des fon tions lisses et sous-harmoniques τX∗ Φn (voir [32℄ pour l'utilisation
de fon tions sur X dénies via des des (diéren es de) fon tions onvexes sur les polyèdres
S(X )).

3.4.2. Parties polaires.
  Un sous-ensemble E d'une ourbe stri tement k-analytique lisse X est dit polaire s'il admet
un re ouvrement dénombrable par des ouverts onnexes Ω ⊂ X sur lesquels existe une fon tion
u ∈ SH(Ω) telle que E ∩ Ω ⊂ {u = −∞}.
Remarque 3.4.8
     1. La ondition de dénombrabilité introduite dans ette dénition est né essaire à l'exis-
        ten e, pour toute partie polaire E ⊂ X , d'une fon tion sous-harmonique globale sur X
        prenant la valeur −∞ en tout point de E , ainsi qu'à une ara térisation apa itaire des
        parties polaires (théorème 3.6.11 et remarque 3.6.12).
     2. La ondition de dénombrabilité, jointe à la semi- ontinuité supérieure des fon tions sous-
        harmoniques, implique immédiatement que tout sous-ensemble polaire de X est ontenu
        dans un borélien polaire.

   Nous noterons P(X) l'ensemble des points x ∈ X tels que le singleton {x} soit polaire ; il
est lair que les parties polaires de X sont des sous-ensembles de P(X).
Remarque 3.4.9.  Les deux propriétés suivantes se déduisent immédiatement de la pro-
position 3.1.14 :
     1. Quel que soit le morphisme quasi-ni f : Y → X , f −1 (P(X)) ⊂ P(Y ).
     2. Pour toute extension non ar himédienne K/k, p−1
                                                      K (P(X)) ⊂ P(X ⊗k K).
                                                                        b

Proposition 3.4.10.  Pour         toute ourbe stri tement k-analytique lisse X , P(X) est
exa tement l'ensemble des points de X de type (1).
Démonstration. Rappelons qu'un point x d'une ourbe stri tement k-analytique est de
type (1) si l'extension non ar himédienne H(x)/k se plonge dans la omplétion d'une lture
algébrique de k. (2.1.3)
   Tout point x de type (1) dans A1k est polaire : étant donnés une suite dé roissante (En ) de
disques fermés dans A1k de limite {x} et, pour tout n, un point xn ∈ En tel que l'extension
κ(xn )/k soit nie, de polynme minimal unitaire fn ∈ k[T ], les fon tions
                                                 1
                                       gn =            log |fn |
                                              deg(fn )


## Published source Ber93, PDF page 30

            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                               33

      1.5.2. Corollary. — Let [W, v) and {^f, T') be k-quasiafjinoid spaces, and let 9 : % -> W
he a morphism (resp. an isomorphism) of locally ringed spaces. Then the following are equivalent:
      a) 9 induces a morphism (resp. an isomorphism) of k-quasiafjinoid spaces [%, v) -> (^', v');
      b) there exist open coverings {^},ei °f ou and {^•),eJ °f <r suc^ ^at, for each
pair z, j , 9 induces a morphism (resp. an isomorphism) of k-quasiaffinoid spaces

                  Wn9-TO,v)^(^,v')

(resp. (^ n 9-TO, ^ ^ (?W ^ ^., v')J;
      ^ property b) is true for arbitrary open coverings of W and W. •

       Let X be a locally ringed space. An (open) k-analytic atlas on X is a collection
of A-quasiaffinoid spaces { ( ^ o v j h e l called charts of the atlas such that { ^ } i ^ i is
an open covering of X (each ^ is provided with the locally ringed structure induced
from X) and, for each pair t, j e I, the identity morphism induces an isomorphism of
A-quasiaffinoid spaces (^ n ^., v,) ^> (^ n ^., v^.). Furthermore, suppose that we
are given an open subset W C X and an open immersion v of ^l in a A-affinoid space.
Then (^, v) is compatible with the atlas {(^o^)hgi if, for each i el, the identity
morphism induces an isomorphism of ^-quasiaffinoid spaces (^ n ^, ^) -^ (^ n ^, ^).
Two atlases are said to be compatible if every chart of one atlas is compatible with the
other atlas. From Corollary 1.5.2 it follows that the compatibility of atlases is an equi-
valence relation. A A-analytic space from [Ber] is a locally ringed space X provided
with an equivalence class of ^-analytic atlases.
        Let X, X' be two ^-analytic spaces defined in the above way, and let 9 : X -^ X'
 be a morphism of locally ringed spaces. Then 9 is called a morphism of A-analytic
 spaces if there exists an atlas {(^,, ^)}iei °f X ^d an ^l^ { ( ^ 5 ^)L'eJ
 of X' such that, for each pair z,j, 9 induces a morphism of ^-quasiaffinoid spaces
 (^ n 9-l(^.), vj -> (^., ^.). From Corollary 1.5.2 it follows that the same condition
 holds for any choice of atlases on X and X' defining the same ^-analytic structure, and
 that one can compose morphisms. Thus, one gets a category. This is the category intro-
 duced in [Ber] (and denoted there by k-^n).
        We now construct a functor from the category of A-analytic spaces from [Ber]
 to k-^/n. For each ^-analytic space X from [Ber] we fix an open ^-analytic
 atlas {(^,, ^Jier Let T be the family of the subsets VC X for which there exists i e I
 such that V is an affinoid domain in ^ (in this case V is an affinoid domain in any ^
 that contains V). Then T is a net on X, and there is an evident A-affinoid atlas ^ with
 the net T. The ^-analytic spaces (X, s/, r) obtained in this way is evidently good. Let
  now 9 : X ->X' be a morphism of A-analytic spaces from [Ber]. We denote by a the
 family of all V e T for which there exists V e T' with 9(V) C V. It is clear that (T is a net
  with (T -< T, and the morphism 9 gives rise to a strong morphism (X, ^ / y y a) -> (X', e^/', T').
  Therefore we have the required functor, and it is easy to see that it is fully faithful. Let
  now X be a good ^-analytic space from k-^/n. For an affinoid domain V C X we denote


## Published source Ber93, PDF page 31

34                               VLADIMIR G. BERKOVICH

by ^v the topological interior of V in X and by Vy the canonical open immersion of
locally ringed spaces ^y ->V. Then {(^<y, Vy)} is an open ^-analytic atlas on X, and the
^-analytic space from [Ber] obtained in this way gives rise to a ^-analytic space from k-^/n
isomorphic to X. Thus, the correspondence X h-> (X, s / y , a) is an equivalence of the
category of ^-analytic spaces from [Ber] and the category of good ^-analytic spaces.
       We now extend to the category k-^/n several classes of morphisms that were intro-
duced in [Ber] for good A-analytic spaces. Let P be a class or morphisms of good ^-analytic
spaces which is preserved under compositions, under any base change and under exten-
sions of the ground field. We say that a morphism 9 : Y—> X in k-^/n is of class ? if
for any morphism X' -> X from a good analytic space over k the space Y X x X' is
good and the induced morphism Y X x X' -> X' is of class P. It follows from the definition
that the class P is also preserved under the same operations. Furthermore, ifP contains
locally closed immersions, then P processes the following property: if Y -> X is a locally
separated morphism, then any morphism Z -> Y, for which the composition Z -> X
is of class P, is of class P.

      1.5.3. Examples. — (i) If P is the class of all morphisms of good analytic spaces,
then the morphisms from P are said to be good. For example, finite morphisms and
locally closed immersions are good morphisms.
       (ii) If P is the class of closed morphisms of good analytic spaces ([Ber], p. 49),
then the morphisms from P are said to be closed. For example, finite morphisms and
locally closed immersions are closed morphisms.
       (iii) I f P is the class of proper morphisms of good analytic spaces ([Ber], p. 50),
then the morphisms from P are said to be proper. It follows from the definitions that a
morphism is proper if and only if it is compact and closed. For example, finite morphisms
are closed. Conversely, if a proper morphism has discrete fibres, then it is finite
([Ber], 3.3.8).

      1.5.4. Definition. — The relative interior of a morphism 9 : Y -> X is the set Int(Y/X)
of all points y e Y for which there exists an open neighborhood i^ofjy such that the
induced morphism i^ -> X is closed. The complement of Int(Y/X) is called the relative
boundary of 9 and is denoted by ^(Y/X). IfX ==^(^), these sets are denoted by Int(Y)
and (?(Y) and are called the interior and the boundary of Y, respectively.
      It follows from the definition that ^(Y/X) = 0 if and only if the morphism y is
closed. The following properties of the relative interior are easily deduced from the
definition and [Ber], 3.1.3.

      1.5.5. Proposition. — (i) If Y is an analytic domain in X, then Int(Y/X) coincides
with the topological interior ofY in X.
                                          u/   <p
      (ii) For a sequence of morphisms Z -> Y -> X, one has

                 Int(Z/Y) n ^(In^Y/X)) C Int(Z/X).


## Published source Ber93, PDF page 32

             fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                               35

If 9 is locally separated (resp. and good) then
                   Int(Z/X) C Int(Y/X) (resp. Int(Z/X) = Int(Z/Y) n ^(In^Y/X));.
      (iii) For a morphism f: X' -^X, (w? A^/'-'(In^Y/X)) C Int(YyX'), o^?/' ^
Y ' ^ Y x^X'-^Y.
      (iv) For fl non-Archimedean field K ozw ^, ow? has Tc-^In^Y/X)) C Int(Y §» K/X ® K),
wfer^ TT ^ Y ® K -> Y. •

       1.5.6. Remark. — The notion of a strictly ^-analytic space introduced in [Ber],
p. 48, is not consistent with that introduced in the previous subsection. First of all, if
the valuation on k is trivial, the two notions are completely different. (For example,
the affine line A1 is strictly ^-analytic in the sense of [Ber] but is not such a space in the
sense of § 2.2.) Assume now that the valuation on k is nontrivial. In this case the diffe-
rence is that in [Ber] strictly A-analytic spaces were considered as objects of the whole
category of ^-analytic spaces, but here we consider them as objects of their own cate-
gory st-k-^/n because we do not know whether the faithful functor st-k-^/n ,-> k-s/n is
fully faithful.

1.6. Connection with rigid analytic geometry

       We work here with the category of rigid ^-analytic spaces which is defined in
 [BGR], §9.
       Assume that the valuation on k is nontrivial, and let X be a Hausdorff strictly
^-analytic space. The corresponding rigid A-analytic structure will be defined on the
set Xo =={x e X | \^[x) : k] < oo }. (We remark that from [Ber], 2.1.15, it follows
that the set Xo is everywhere dense in X.) First of all, i f X = Ji({^) is strictly A-affinoid,
then the maximal spectrum Xo = Max(^) is endowed with a rigid ^-analytic space
structure as in [BGR], § 9.3.1. Suppose that X is arbitrary. We say that a subset
 °U C Xo is admissible open if, for any strictly affinoid domain V C X, the intersection ^ h Vo
is an admissible open set in the rigid ^-affinoid space Vo. Furthermore, a covering {^•}^r
of an admissible open subset ^C X^ by admissible open subsets is admissible if, for any
strictly affinoid domain V C X, { ^ n VQ },^ i is an admissible open covering of % n Vo.
In this way we get a G-topology on the set Xo. The sheaves of rings Q^, where V runs
through the strictly affinoid domains in X, are compatible on intersections, and to they
glue together to form a sheaf of rings (9^ on the G-topological space Xo. The locally
G-ringed space (Xo, (P^) satisfies the conditions of Definition 9.3.1/4 from [BGR],
and so we get a rigid ^-analytic space. We remark that the rigid yfe-analytic space cons-
tructed is quasiseparated. (A rigid A-analytic space is called quasiseparated if the inter-
section of two open affinoid domains is a finite union of open affinoid domains.)

       1.6.1. Theorem. —The correspondence X i-> XQ is a fully faithful junctor from the
category of Hausdorff strictly k-analytic spaces to the category of quasiseparated rigid k-andlytic


## Published source Ber93, PDF page 51

54                                  VLADIMIR G. BERKOVICH

to show that if q is a prime ideal of G, then any multiplicative norm on B/p, where p
is the preimage of q in B, extends to a multiplicative norm on G/q. But this follows
from the well known fact that a valuation on a field can be extended to a valuation on
any bigger field. •
      The following statement is proved in the same way as its particular case when
X =^(K) (see [Ber], 3.4.7).

        2.6.9. Proposition. — Let 9 : 3£ -> W be a morphism of finite type between schemes of
locally finite type over °K. Then 9 is proper (resp. finite, resp, a closed immersion) if and only if 9^
possesses the same property. •

      2.6.10. Proposition. — Let 9 : 3£ = Spec(G) -^W == Spec(B) be a finite morphism
between affine schemes of finite type over S£. Let z e 2K andy e ^an be points with <p(z) = TT(^) == y,
and let ^J^\y) == { ^ ..., ^ } and y^'1^) n TT-^Z) == { z^ ..., ^ }, m ^ n. Then
there is an isomorphism of rings
                                            m                n

                    ^°, y ®ey „ ^, , ^ n C^, v X . n                 (^an ,,) ^,
                             '       i == 1     i==w+l


where (^an^.)p is the localization with respect to the complement of the prime ideal of C cor-
responding to the point z.

      Proof. — If V is an affinoid domain in ^^ then for its preimage W in ^an one
      (
has S^=0§^®•QG. Since cp^ is finite, from Lemma 2.1.6 it follows that
^ a n y ^ s C ^ n^ ^an^.. The ring ^any®^         0^^ is the localization of ^an y 0 ^ G
with respect to the complement of^. IfTr(^) = z, then the ring ^an ^. does not change
under this localization. The required statement follows. •


                            § 3. Etale and smooth morphisms

3.1. Quasifinite morphisms

       3.1.1. Definition. — A morphism of^-analytic spaces 9 : Y -> X is said to be finite
at a pointy e Y if there exist open neighborhoods Y^ ofy and ^ofy(j/) such that 9 induces
a finite morphism i^ -> W; 9 is said to be quasifinite if it is finite at any point y e Y.
       It follows from the definition that quasifinite morphisms are locally separated
and closed.

          3.1.2. Lemma. — If a morphism 9 : Y -> X is finite at a point y e Y, then the neigh-
borhoods V and W from the Definition 3 . 1 . 1 can he found arbitrary small.

     Proof. — We may assume that the morphism y is finite. Let x == y(jy) and let
(p-^) == {j/i ===J^25 • • -^A }• Since the map [ Y [ -^ [ X [ is compact, we can find a


## Published source Ber93, PDF page 64

            STALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                         67

9 : Y-> X. By Proposition 3.1.8, the morphism <p is finite at the point y (that corres-
ponds to the points j^). It is clear that die point y is not contained in the support
oftiy^xo? 19e^ ? ls unramified atj/. It is flat atj/, by Proposition 3.2.3.
      Suppose now that X is arbitrary (and Hausdorff). The intersections U^ n U,
are not affinoid now, but they are separated compact ^-analytic spaces, and therefore
we can apply the above construction using the fact that everything is already verified
for separated spaces. The theorem is proved. •

      3.4.2. Corollary. — Let 9 : Y -> X be a morpkism of analytic spaces over k, and let
y eY, x = <p(^). Suppose that the maximal purely inseparable extension of J^(x) in ^[y) is
dense in e^(jy). Then the correspondence U h-> U X x Y induces an equivalence of categories
F^t(X^)^Fft(Y^). •

3.5. Smooth morphisms

      For a ^-analytic spaces X we set A^ = A? X X (the d-dimensional qffine spaces over X).

      3.5.1. Definition. — A morphism of ^-analytic spaces 9 : Y -> X is said to be
smooth at a pointy e Y if there exists an open neighborhood i^ ofy such that the induced
morphism i^ -> X can be represented as a composition of an ^tale morphism V -> A^
with the canonical morphism A^ ->X; 9 is said to be smooth if it is smooth at all points
y eY. If the canonical morphism X -^JK(k) is smooth, then X is said to be smooth.
      We remark that the number d is equal to the dimension of 9 at the pointy, i.e., to
the dimension of the fibre Y^, where x = 9(^)5 at the point y. If this number is inde-
pendent of y^ we say that <p is of pure dimension d. For example, smooth morphisms of
pure dimension 0 are exactly ^tale morphisms. We remark that smooth morphisms are
locally separated and closed. The following proposition follows easily from the definition
of smooth morphisms and Corollary 3.3.8.
      3.5.2. Proposition. — Smooth morphisms are preserved under compositions^ under any
base change functor, and under extensions of the ground field. •

      3.5.3. Proposition. — Suppose we are given a commutative diagram of morphisms of
k-analytic spaces
                    Y ^-> X




       (i) If <p is etale, then 9^x0/80) -^ ^Yo/So-
       (ii) Iff and g are smooth and yaC^xo/so) ^^YG/SG? t^en V ls eta^'
      Since Sl^d ^ is a free O^d -module of rank d and, if X is good, the canonical mor-
phism A^ -> X is flat, then thestatement (i) implies


## Published source Ber93, PDF page 66

            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                            69

ranks of Qx/fc ^d ^y/fc at the points x and^, respectively. Since 9*(t2x/jk) ^^Y/*? ^Y
are equal.
       Suppose now that the point^ is arbitrary. Let K be a big enough non-Archimedean
field such that there exists a pointy e Y' = Y ® K with [^(V) : K] < oo and 7r(y) ==^,
where n is the canonical mapping Y' -> Y. From Proposition 3.3.3 it follows that
9^(^x78') "^ ^YW 5 where 9' is the induced morphism Y ' - > X ' = X ® K . By the
previous case, Q^'^' is a flat fl?x/,a!'"a^?eb^a, where ^'== y^J'). By Corollary 2.1.3,
^x',»' an<^ ^Y',i/' are faithfully flat over tf^a; ^d ^Y,!/? respectively. It follows that (Py y
is flat over ^x,»*
       Consider now the general case. If U is an affinoid domain in S, then, by the first
case, the induced morphism ^"^(U) ->y~ l (U) is dtale and, in particular, it is quasifinite.
From Proposition 3.1.8 it follows that the morphism 9 is quasifinite. This implies
immediately that it is ^tale. •

     3.5.6. Corollary. — In the situation of Proposition 3.3.2 (i) suppose that 9 is smooth.
Then there is an exact sequence

                  0->9^Xo/So) -^Yo/So^^Yo/Xo-^O.              •



      3.5.7. Corollary. — Let 9 : Y ->• X be a smooth morphism^ and let f: Y -> A^ be an
H-morphism defined by some functions f^ .. .,^ e ^(Y). Then f is etale at a pointy e Y if and
only if for some affinoid domain U C X that contains the point x = 9(jQ the elements df^ ..., df^
form a base o/Hp-i^/u aty.

       Proof. — The direct implication is trivial. Suppose that df^ ..., df^ form a base
of Up-i^/u at y. By Proposition 3.5.3, the induced morphism y'^U) -> A^ is Aale
3ity, In particular, the point y is isolated in the fibre f~l{f{y)). From Proposition 3.1.4
it follows that for any affinoid domain VC X that contains the point x the induced
morphism 9~1(V) -> A^ is finite atj/, and therefore, by Proposition 3.1.8, the morphism/
is finite atj/. It is dtale because the elements df^ ..., df^ form a base of Up-i^yy a t j for
any V as above. •

       3.5.8. Proposition. — A morphism 9 : S -> W between schemes of locally finite type
over ££ == Spec(^), where ^ is a k-affinoid algebra^ is smooth if and only if the corresponding
morphism 9^ : ^an -> ^an is smooth.

      Proof. — The direct implication follows from Proposition 3.3.11. Suppose that 9^
is smooth. By Corollary 3.5.4, ^ is flat, and i^an^an is a locally free ff^an-module.
Since the morphisms <3<an -> W and ^an -> S are faithfully flat, it follows that 9 is flat.
Since t^an^an = {0.^1^^ lt follows that £l^y is a locally free ^-module. Therefore 9
is smooth. •


## Published source Ber93, PDF page 74

            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                           77

      3.7.3. Corollary. — Let <p : Y -> X be a smooth morphism of good k-analytic spaces. Then
for any point y e Y there exist ttale morphisms f: X' -> X and g : Y" -> Y' = Y Xx X'

                 Y ^> X

                            I7
                  A         A

                  r
                  Y' -^ X'

                  t- -7
                  Y"
such that y e/'C?(Y")) ^ 9" is an elementary fibration. •

      3.7.4. Corollary. — A smooth morphism is an open map. •

      Proof of Theorem 3.7.2. — All the analytic spaces considered in the proof are
assumed to be good. For numbers 0 < r' ^ r" (resp. 0 < r ' < r") we denote by A(r', r " )
(resp. B(r', r")) the closed (resp. open) annulus E(0, r")\D(0, r') (resp. D(0,r")\E(0,r'))
with center at zero.

       3.7.5. Proposition. — Let 9 : Y -> X be a separated smooth morphism of pure dimension
one, and let x eX. Suppose that the fibre Y^ is isomorphic to the open annulus B(r, R)^^). Then
there exist numbers r < r' < R' < R, an open neighborhood W ofx and an open subset i^ C (p"1^)
such that
      a) Y^ coincides with B(r', R').^,) under the identification of Y^ with B(r, R).^);
      b) i^ is isomorphic to the direct product ^ X B(r', R') over W.

      3.7.6. Lemma. — Let Y be an open subset of A^, and suppose that

                  Y, = D(0, r)^\ U E(^, r^              m ^ 0,
                                     i=l


wA^ r, < r aW | T(^) | < r (^T ^ ^ coordinate function on A1}. Then
       (i) if m == 0, ^ /or ^ w^w&^r 0 < r' < r ^r^ exists an open neighborhood % of x
 such that Y contains the direct product % X D(0, r').
        (ii) if m^ 1, then for any numbers max.([ T(aJ |, r,) < r' < r" < r, ^r<? exists an
 open neighborhood % of x such that Y contains the direct product % X B(r', r").

       proof. — In the case (i) (resp. (ii)) the intersection of all compact sets of the form
 U X E(0,r') (resp. U X A(r', r")), where U runs through compact neighborhoods
 of the point x, coincides with E(0, r')^ (resp. A(V, r")^), and therefore it is contained
 in the open set Y. It follows that there exists a compact neighborhood U of A: with
 U X E(0, r') C Y (resp. U X A(r', r") C Y). •


# Explicit source application checks

# Checked applications of published foundations

These are application checks, not substitute proofs for the new envelope statements.

The exact source definition of LFS is GJR Definition 7.8: an \(\mathbb R\)-PL function with semiample residue at every point. Paragraph 7.9 has maxima of **negative** logarithms of **invertible** analytic functions on an ordinary open neighbourhood and **nonnegative real** coefficients. The original PDF page 47 was rendered and inspected. At a truncated-log bend the zero of \(T-a\) is excluded from the chosen neighbourhood, so the functions used are \((T-a)^{-1}\) and \(c^{-1}\). Near the centre the function is constant. The cutoff \(|c|\) lies in the value group, and the two pieces are strict analytic domains. A sum can have arbitrary real slopes, but no maximum closure for arbitrary real-PL functions is used. GJR Example 5.3 is retained precisely because that closure fails.

GR2 Theorem 4.3 was checked against original PDF page 22. It requires a nontrivial valuation and a good strict analytic space; it does not require boundarylessness. All rational domains, nodal affinoids and projective products used in the proof are good and strict. Competitors are real-valued and continuous because they are R-PL. GR1 Proposition 5.1 is stated for a smooth curve, while GR1 distinguishes smooth from merely rig-smooth by the boundaryless condition. It is not applied directly to the boundaryful rational affinoid. GR2's theorem and boundary conventions supply the applicable foundation instead.

GR2 Proposition 4.2 and GJR Proposition 7.6 preserve positivity under every analytic scalar extension and analytic morphism. Every field in our application extends the original nontrivial valuation; no trivial-field case is inserted. A proper fibre over a Berkovich point is treated over \(\mathcal H(x)\) by scalar extension followed by its analytic inclusion, rather than by pretending it is a ground-field analytic subdomain.

GR2 Theorem 6.1 puts the local maximum point in the analytic relative interior. The star comparisons use smaller rational affinoids inside the base interior; their boundary values are approached by limits, using continuity of each competitor. Boundary vertices have no outgoing-slope sign requirement. The proper projective-fibre argument uses this maximum principle on the fibre, whose boundary is empty, rather than on the boundaryful total space. The rational boundary set is verified in the new proof using disc topology and the analytic-domain boundary formula. Harmonic comparison is applied only to logarithms of units, so negative coefficients are permissible.

Ber93 Definition 3.5.1 and Proposition 3.5.2 identify relative smoothness on the projective-space coordinate charts and preserve it after base change. Corollary 3.7.4 was checked visually on PDF page 74, printed page 77: a smooth morphism is an ordinary open map. It is applied only to \(A\times\mathbb P^d\to A\). Proposition 2.6.9 supplies properness of the projective analytification, then analytic base change gives the product projection. Its compact fibres and topological closedness, together with smooth openness, prove continuity of fibre minima. The analytic product is never identified with the topological product.

GR2 Section 2.9 supplies closed, surjective scalar projection. No scalar projection is asserted open. Its surjectivity is used to bring down the upstairs bound after passing to the completed algebraic closure of an arbitrary extension. Equality of finite-tree data is verified using identical centres, radii and the explicit truncated-log coordinates. Uniform obstacle approximation and family contractivity then prove exact scalar envelope compatibility. This applies to every obstacle on the algebraically closed base and its pullbacks, not to unrelated arbitrary obstacles on every nonalgebraically closed scalar domain.

Thuillier Definition 3.1.5 was compared with original PDF page 76, printed page 62. The comparison inequality is upper-boundary domination implying domination throughout a strict affinoid. Proposition 3.4.6 has an actual simply semistable formal-curve hypothesis. The new proof does not silently assert that hypothesis for a chosen finite tree: it constructs retractions from disc coordinates, graph minorants from global analytic expressions, and comparison stars from explicit rational inequalities. The source skeleton result is retained as a check, not used as an unproved new realization step.

All source caches are public published originals. The supplied book claims, review verdicts and hashes supply no mathematical input. Hashes only identify bytes; compilation and finite graph diagnostics only record execution.
