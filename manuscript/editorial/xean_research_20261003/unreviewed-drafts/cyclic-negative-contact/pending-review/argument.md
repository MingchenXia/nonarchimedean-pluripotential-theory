---
title: "A regularizable envelope with negative contact integral on the cyclic triangle squared"
author: "Unverified P05.2 working draft"
date: "3 October 2026"
---

## Exact result and boundary

The requested all-obstacle triangle-square contact theorem is false. On the exact unit-weight graph and actual lattice specified in the assignment, the functions constructed below satisfy
\[
 P_\gamma(u)=\gamma\in\mathrm{PAPC}_{\mathbb R}(G^2,\gamma)
 \subset\mathrm{PC}_{\mathrm{reg},\mathbb R}(G^2,\gamma),\qquad
 \int_{G^2}(P_\gamma(u)-\gamma-u)\,
           \mathrm{MA}_{\mathrm{poly},\mathbb R}(P_\gamma(u))=-8.
 \tag{1}
\]
Here the reference is actual PC and positive at infinity, the obstacle is bounded real PA on finite rational spatial domains, and the raw competitors need not be continuous. This is an actual operator-domain counterexample, with exact envelope equality and a complete negative integral, rather than a regularity-failure alternative or an apparent local atom.

The original P05.2 task is the classification of arbitrary balanced pairs having the contact identity for every admissible obstacle. That classification remains open. In particular, this note does not classify every reference on this graph product, establish all-obstacle regularity for it, settle two arbitrary finite graphs, or address P06.2. Status is partial and candidate is false. The proposed conditional all-obstacle contact gate, even restricted to raw envelopes already in rational real PAPC on this triangle square, is also refuted by (1).

The difference-norm trap on two conical three-ray stars appears in the earlier round-06 draft. Its local calculation is reconstructed here and is not claimed as a new local mechanism. The new result is its actual global realization on the two bounded cyclic graphs, with the required positive-growth reference, raw-envelope comparison for all competitors and remote endpoints, and full recursive negative integral. No result, verdict, receipt or hash from that draft or the predecessor is a premise. This counterexample differs from the predecessor's imposed-contact positive example: its witnessed noncontact vertex has strictly positive complete recursive mass.

## Definitions and source obligations

The controlling source is Chapter 72 of the book, `parts/part6/ch72_major_open_problems.tex`, especially the polyhedral section, and its named Appendix M, `appendices/appM_ch18_frontiers.tex`. The active P05.2 requirement is the exact contact integral for all admissible obstacles; positive growth, balancing and total mass do not suffice. Chapter 72 explicitly leaves arbitrary nonseparable product obstacles and the higher-dimensional real PA case open. Appendix M concerns the analytic zero-current/classical pluriharmonic bridge and supplies no polyhedral product theorem used here.

We use Botero--Mazzon--Pille-Schneider, *Monge--Ampère measures on balanced polyhedral spaces*, arXiv:2603.08664v1, manuscript dated 10 March 2026 (BMPS), solely to fix the following definitions and normalization. Every mathematical implication used for the counterexample is proved below.

* A finite rational spatial complex consists of finitely many rational polyhedra meeting in common faces, with their faces included. A rational polyhedron can be defined by integer affine inequalities after clearing denominators (Definitions 2.1--2.4).
* For a face \(\sigma\), its actual saturated tangent lattice is \(N_\sigma=N\cap\operatorname{span}_{\mathbb R}(\sigma-\sigma)\). For a facet \(\tau\prec\sigma\), a normal lift \(n_{\sigma/\tau}\) represents the primitive positive generator of \(N_\sigma/N_\tau\), pointing into \(\sigma\) (Definition 2.18). A real cycle is balanced when \(\sum_{\sigma\succ\tau}w_\sigma n_{\sigma/\tau}\in N_{\tau,\mathbb R}\) at every tested facet (Definitions 2.19--2.20, explicitly extended from rational to real weights here).
* A real PA function is continuous and real affine on a finite **rational spatial** structure. This is the real span of the literal integral-slope/rational-constant functions on that structure: continuity is a rational linear system, its real solution space has a rational basis, and clearing each basis vector's slope denominators makes it literal PA. Definition 2.28 itself is literal, not this extension. Real coefficients never permit irrational spatial walls in this note. Our actual example has rational coefficients throughout.
* A PCC consists of finitely many rational endpoints \(x_i\in X\cap N_{\mathbb Q}\), real \(\alpha_i\geq0\) summing to one, and the actual centre \(x=\sum_i\alpha_i x_i\). For some allowed rational structure there are faces \(\tau\preceq\sigma_i\) with \(x\in\tau\) and \(x_i\in\sigma_i\) (Definition 3.2). A finite raw PC function satisfies \(q(x)\leq\sum_i\alpha_iq(x_i)\) for every such PCC, on every allowed structure (Definition 3.3). We do not assume continuity of raw competitors.
* PAPC means that \(a\cdot z\geq0\) for every nonnegative real balanced local \(k\)-cycle, every \(k\geq1\), on every ordinary open subset (Definition 3.1 with the explicit real extension). Its derivative definition is (2) below. This tests all cycle dimensions and all refinements, rather than only the given top cycle.
* The reference growth class is \(a=\gamma+O(1)\) (Definition 3.14). The raw envelope is exactly
  \[
  P_\gamma(u)(x)=\sup\{q(x):q\in\mathrm{PC}(X),\ q\leq\gamma+u,
                    \ q\leq\gamma+C_q\text{ for some constant }C_q\}.
  \]
  Competitors have only the displayed upper growth requirement (Definition 6.2).
* A continuous function is real regularizable here if it is a uniform limit of real PAPC functions in the two-sided reference growth class; decreasing approximation is permitted (Proposition 3.22/Definition 3.23). Our explicit sequence supplies this directly, without importing either direction of that proposition as an approximation theorem.
* The PA operator in dimension two is the finite atomic zero-cycle \(a\cdot(a\cdot[X])\), with the formula (2), on the vertices of any structure for \(a\) and \([X]\) (Definition 4.4). There is no division by \(2!\), no probability normalization, and no boundary term at infinity for this finite PA zero-cycle. A regularized operator extending this PA operator agrees with it on our already PAPC envelope; the explicit constant-shift approximants have exactly the same measures.
* Positive at infinity requires a strictly positive linear slope on every nonzero recession vector of every reference affine cell (Definition 4.15). Definition 6.9 assumes regularity when naming a pair's all-obstacle orthogonality property. We refute its contact identity at an envelope in its own operator domain, without assuming other envelopes regularizable.

The complete proof bodies of BMPS Lemmas 2.34--2.35, Lemma 3.4, Proposition 3.22, Proposition 6.3 and Proposition 6.13 were inspected. None is imported as a theorem. Lemma 2.35 refers to external intersection theory, and Proposition 6.13 uses a PC locality theorem; both dependencies are bypassed here. The source's automatic raw-PC continuity assertion and a higher-dimensional extension of its one-dimensional regularization proof are not used. In particular, no PC gluing black box is needed: the actual envelope candidate is a global ambient convex restriction, and the upper comparison uses only admitted global PCCs.

There are **no essential external theorem premises**. The polyhedron fact, PAPC tests, divisor refinement and balancing, raw comparison and local coefficient are proved in this file. Source identifiers, complete inspected boundaries and newline-only excerpts are retained for provenance; they are not proof certificates.

## Divisor algebra with actual primitive normals

For a real PA function \(a\) and balanced real \(k\)-cycle \(z\), the divisor is
\[
 (a\cdot z)(\tau)=
 \sum_{\sigma\succ\tau}z(\sigma)a_{\sigma,\mathrm{lin}}(n_{\sigma/\tau})
 -a_{\tau,\mathrm{lin}}
       \left(\sum_{\sigma\succ\tau}z(\sigma)n_{\sigma/\tau}\right).
 \tag{2}
\]
The last argument is tangent by balancing. Altering a lift by a tangent vector makes the two terms change equally, since the linear parts agree tangentially. The formula is therefore lift-independent, real bilinear and local on ordinary opens. Ambient affine functions have zero divisor.

Refinement compatibility in the dimensions needed here follows directly from (2). At a new tested facet, take its minimal old face. If that old face has dimension larger than the cycle dimension, every inherited incident weight is zero. If it has the cycle dimension, exactly two nonzero inherited pieces meet in that plane with equal weights and affine parts and opposite quotient normals, so their terms cancel. If it has the tested facet dimension, the tangent lattice and incident primitive normal classes are the old ones, and the coefficient is inherited unchanged. Extra incident pieces have zero inherited weight. These cases also preserve balancing of a subdivided cycle. Applying the same argument successively to the first divisor proves refinement compatibility of the second divisor. In particular, inserting vertices in an affine edge produces opposite slopes with identical edge weights and coefficient zero; inserting a vertex inside an affine top cell produces zero first divisor there.

For completeness, balancing of the first divisor of a two-cycle is also elementary. Translate the tested vertex to zero and use a pointed rational local two-fan; harmless rational cuts can make any local lineality pointed. Let \(r,s\) be the primitive boundary vectors of a two-cone. Its saturated plane lattice \(N_C\) has index
\[
 \chi_{rs}=[N_C:\mathbb Zr+\mathbb Zs].
\]
The primitive quotient normal at \(r\) is represented modulo \(\mathbb Rr\) by \(s/\chi_{rs}\): extend primitive \(r\) to a basis of \(N_C\), in which the transverse coordinate of \(s\) has absolute value \(\chi_{rs}\). The representative need not itself be an integral lift; their tangential difference cancels in (2). If cone weights are \(\omega_{rs}\), top balancing gives
\[
 \sum_{C_{rs}\succ r}\frac{\omega_{rs}}{\chi_{rs}}s=t_r r,
 \qquad
 D_a(r)=\sum_{C_{rs}\succ r}\frac{\omega_{rs}}{\chi_{rs}}a(s)-t_ra(r).
 \tag{3}
\]
Here \(a\) is the homogeneous germ after subtracting its value at the vertex. Multiplying \(D_a(r)\) by \(r\) and summing, the first sum is the sum, once for each unordered cone, of
\(\omega_{rs}(a(s)r+a(r)s)/\chi_{rs}\). Replacing \(t_rr\) by its balancing sum in the subtracted term gives exactly the same sum. Thus \(\sum_rD_a(r)r=0\), proving that the first divisor is a real one-cycle. Its complete second coefficient at the vertex is
\[
                      (a^2\cdot[X])\{0\}=\sum_rD_a(r)a(r).
 \tag{4}
\]
This includes every first-divisor face, including original branching axes and newly created diagonal faces.

The normalization is the intersection normalization. On a unit-weight complete plane, \(a(s,t)=|s|+|t|\) has first weight two on each of the four coordinate rays and germ value one on each primitive ray. Formula (4) gives eight, which is \(2!\) times the area four of the slope square. We use (2)--(4) themselves, not an Alexandrov substitution at singular junctions.

## Carrier, functions, and admissibility

Let \(G\subset\mathbb R^2\) be the triangle with
\[
 A=(0,0),\quad B=(1,0),\quad C=(0,1),
\]
the primitive bounded oriented edges \(A\to B=(1,0)\), \(B\to C=(-1,1)\), \(C\to A=(0,-1)\), each of primitive length one, and leaves \((-1,-1)\), \((2,-1)\), \((-1,2)\) at \(A,B,C\), respectively. All weights are one. The outgoing vectors at the three junctions are
\[
\begin{array}{c|ccc}
 A&(1,0)&(0,1)&(-1,-1)\\
 B&(-1,0)&(-1,1)&(2,-1)\\
 C&(0,-1)&(1,-1)&(-1,2).
\end{array}
\]
Every row sums to zero, has rank two, and contains a determinant-one pair. Thus the graph is balanced in the actual saturated lattice \(\mathbb Z^2\); every local relation cone is generated by the strictly positive vector \((1,1,1)\). No lattice change or unfolding of the bounded cycle occurs.

Set \(X=G\times G\subset\mathbb R^4\), with coordinates \((x_1,y_1,x_2,y_2)\), actual lattice \(N=\mathbb Z^2\oplus\mathbb Z^2\), and unit product weights. There are thirty-six top product edge cells. Their tangent plane lattice is the direct sum of the two primitive factor edge lattices. At a codimension-one product face, balancing is the corresponding graph balancing sum with the other factor fixed. Hence \(X\) is a pure two-dimensional finite rational balanced space with precisely the required product weights.

Define on the entire ambient \(\mathbb R^4\)
\[
\begin{split}
 \rho&=|x_1|+|y_1|+|x_2|+|y_2|,\\
 h&=|x_1-x_2|+|y_1-y_2|,\\
 \gamma&=\max\{h,\rho/4-1\},\\
 u&=(1-10\rho)_+,\qquad f=\gamma+u.
\end{split} \tag{5}
\]
Restrictions to \(X\) are understood. The function \(\gamma\) is a finite maximum of twenty rational ambient affine functions: four from the two difference absolute values and sixteen from \(\rho/4-1\). Its affine domains form a finite rational complex. Intersecting that complex with the thirty-six product cells and including faces gives a finite rational structure \(\Pi\) on \(X\), affine for \(\gamma\). Every cell is pointed because it is contained in a product of bounded intervals or pointed rays. The obstacle \(u\) also has finite rational affine domains, is continuous, and satisfies \(0\leq u\leq1\). A common rational refinement exists by intersecting the finitely many rational cells. Thus all coefficients and spatial walls obey the requested real convention; indeed \(4\gamma\) and \(u\) are literal PA, but no literal-category regularity conclusion is drawn.

Both \(h\) and \(\rho/4-1\) are ambient convex, so \(\gamma\) is ambient convex. To check actual PC, choose any finite endpoints and real barycentric coefficients from any admitted PCC. Each affine piece has its value at the centre equal to its weighted endpoint values; taking its maximum gives
\(\gamma(\sum_i\alpha_ix_i)\leq\sum_i\alpha_i\gamma(x_i)\).
This proves every actual PCC, including all real centres, rational structures and remote endpoints. The proof does not impose a locality condition or restrict the endpoints to a chosen candidate structure.

For any cell on which \(\gamma\) is affine, any \(z\) in that cell, and nonzero recession vector \(v\),
\[
 \gamma(z)+t\gamma_{\sigma,\mathrm{lin}}(v)
 =\gamma(z+tv)\geq\tfrac14\rho(z+tv)-1
 \geq\tfrac t4\rho(v)-\tfrac14\rho(z)-1.
\]
Divide by \(t\) and let \(t\to\infty\). Its slope is at least \(\rho(v)/4>0\). This proves positive growth in the exact recession-vector sense, including all mixed product ends.

Here PAPC follows directly for every real local cycle in every positive dimension. Refine an arbitrary local cycle together with the function structure. At a relative-interior point of its tested facet \(\tau\), choose an ambient affine piece \(\ell\) active for \(\gamma\). It is a global supporting affine function. Both tangential directions in \(\tau\) imply \(\ell_{\mathrm{lin}}=\gamma_{\tau,\mathrm{lin}}\) there. For every incident germ, the one-sided normal derivative satisfies \(\gamma_{\sigma,\mathrm{lin}}(n)-\ell_{\mathrm{lin}}(n)\geq0\), since \(\gamma\geq\ell\) with equality at the point. Subtracting \(\ell\) in (2) leaves a nonnegative weighted sum for every nonnegative real incident vector. This proves all ordinary-open, all-dimension, real-weight PAPC tests. It is not merely positivity of \(\gamma\cdot[X]\).

## Exact raw-envelope equality, with global growth and remote endpoints

We first locate the only potentially noncontact vertex of \(\Pi\). On \(G\), any point of norm less than one is on one of the three A-incident edges. The other bounded edge \(BC\) has norm one, and each B- or C-leaf has norm \(1+3t\). Thus \(\rho<1\) on \(X\) lies in the product of the two actual A-stars, before either bounded edge reaches its other endpoint. In that region \(\rho/4-1<0\leq h\), so \(\gamma=h\). The active affine-domain inequalities there are homogeneous, as are the A-star cells and their faces. If \(z\ne0\) has \(\rho(z)<1\), then \((1-\eta)z\) and \((1+\eta)z\), for sufficiently small \(\eta>0\), belong to the same local face as \(z\). The inactive bounded-end and cutoff inequalities remain strict. Therefore \(z\) is not a zero-face of \(\Pi\). Consequently
\[
 v\in\Pi^{(0)},\ v\ne0\quad\Longrightarrow\quad\rho(v)\geq1,
 \quad u(v)=0,\quad f(v)=\gamma(v).
 \tag{6}
\]

At zero, define \(u_1=(1,0)\), \(u_2=(0,1)\), \(u_3=(-1,-1)\), and use rational endpoints
\[
 z_i=\tfrac14(u_i,u_i),\quad \alpha_i=\tfrac13.
 \tag{7}
\]
Their centre is zero, since \(\sum_i u_i=0\). The endpoints lie in the three original product cells formed by the same A-incident edge in both factors, all cofaces of \((A,A)\). Thus (7) is an admitted actual PCC on the original rational product structure. Their \(\rho\) values are \(1/2,1/2,1\); their \(h\), \(\gamma\), \(u\), and \(f\) values are all zero. Every raw competitor \(q\leq f\) therefore satisfies
\[
                        q(0)\leq\tfrac13\sum_iq(z_i)\leq0=\gamma(0).
 \tag{8}
\]
Together with (6), this bounds every raw competitor by \(\gamma\) at every vertex of \(\Pi\), although \(f(0)=1\).

We need a finite polyhedron fact to propagate those bounds without raw continuity. Every nonempty pointed rational polyhedron \(\sigma\) is
\[
 \sigma=\operatorname{conv}\{v_1,\ldots,v_a\}
                  +\operatorname{cone}\{r_1,\ldots,r_b\},
 \tag{9}
\]
where the \(v_i\) are rational vertices and the \(r_j\) are rational recession vectors; \(a\geq1\), and \(b\) may be zero. Here is a proof. Homogenize its rational affine inequalities to a closed rational cone in \((t,z)\), with \(t\geq0\). This cone is pointed: a line would have \(t=0\) and give lineality in the original polyhedron. For any pointed polyhedral cone described by homogeneous inequalities, the sum of their defining forms is strictly positive on every nonzero cone vector; a vector with all inequalities zero would give a line. Its section at value one is bounded, since normalizing an unbounded sequence to the unit sphere would give a nonzero cone vector where that sum vanishes. The section is a compact polyhedron. A line through a point in a positive-dimensional minimal face has terminal points in smaller faces; induction expresses every point as a convex combination of vertices. There are finitely many vertices, obtained by full-rank selections of active rational equations, and hence rational. Their rays generate the cone. A generator of positive homogenizing height gives a vertex of the original polyhedron after normalization: any nontrivial convex decomposition there would contradict extremality of its cone ray. A height-zero generator is a recession direction. Taking the slice \(t=1\) proves (9) and nonemptiness of the vertex set.

Fix an arbitrary \(x\in\sigma\in\Pi\), and write it using (9) as
\[
 x=\sum_i\beta_i v_i+\sum_jt_jr_j,
 \quad \beta_i,t_j\geq0,\quad\sum_i\beta_i=1.
\]
Choose \(i_0\) with \(\beta_{i_0}>0\), put \(T=\sum_jt_j\), and take integers \(L\) so large that \(T/L\leq\beta_{i_0}\). Express \(x\) as a convex combination of the rational vertices and rational endpoints \(v_{i_0}+Lr_j\), subtracting \(T/L\) from the \(v_{i_0}\) coefficient and assigning \(t_j/L\) to the respective far endpoints. The coefficients are allowed to be real, and the centre is the original arbitrary real \(x\). All points lie in \(\sigma\), so this is a same-cell PCC (take \(\tau=\sigma\)); it is admissible on the rational structure \(\Pi\).

If \(q\) is any raw competitor with \(q\leq\gamma+C_q\), the vertex bounds (6)--(8), the PCC inequality and the affine restriction of \(\gamma\) give
\[
 q(x)\leq\gamma(x)+(T/L)\max\{C_q,0\}.
\]
Let \(L\to\infty\). Thus \(q(x)\leq\gamma(x)\) everywhere. This explicitly retains unbounded cells, mixed ends, arbitrary real centres and remote rational endpoints. No bounded-cycle constraint is dropped, no continuous competitor reduction is made, and no local competitor patch is assumed to glue globally.

Conversely, \(\gamma\) is a global actual PC function, \(\gamma\leq f\), and has its own required upper growth bound. It is a raw competitor. The two comparisons prove
\[
                              P_\gamma(u)=\gamma\quad\text{on }G^2.
 \tag{10}
\]
Since \(\gamma+1/j\) is ambient convex, real PA, PAPC against all local tests, and in the two-sided \(\gamma+O(1)\) class, this sequence decreases uniformly to \(\gamma\). All its divisors equal those of \(\gamma\), by (2). This supplies exact regularizability and the actual regularized operator at this envelope. It does not assert regularizability of other obstacles on the pair.

The obstacle is genuinely nonseparable. For \(p=(1/10,0)\) on \(AB\), its values at \((A,A),(p,A),(A,p),(p,p)\) are \(1,0,0,0\), with mixed difference one. Thus \(u\) cannot be written as the sum of two factor functions.

## Complete recursive mass at the noncontact product junction

Near \(0=(A,A)\) the envelope germ is exactly \(h\). In the local quadrant with first ray \(u_i\), second ray \(u_j\), and primitive coordinates \(s,t\geq0\), write
\[
 a_i=(u_i,0),\qquad b_i=(0,u_i),\qquad d_i=a_i+b_i,
 \qquad c_i=|u_{i,x}|+|u_{i,y}|\in\{1,1,2\}.
\]
For \(i=j\), \(h=c_i|s-t|\); split that quadrant into the cones \(\langle a_i,d_i\rangle\), \(\langle b_i,d_i\rangle\). For \(i\ne j\), the entire quadrant is affine, with \(h=c_is+c_jt\). These are all twelve top cones and all nine rays of the actual local function-domain fan.

Every original saturated product plane has basis \(a_i,b_j\). An off-diagonal cone has index one in that basis. In a diagonal plane, the pairs \((a_i,d_i)\), \((b_i,d_i)\) have determinant absolute value one in the basis \((a_i,b_i)\). All nine displayed rays are primitive in \(\mathbb Z^4\). Thus every local cone here has actual index one, with weight one; no ray-generated lattice is substituted for its saturation.

At \(a_i\), the neighbor vectors in (3) are \(b_j\) for \(j\ne i\), and \(d_i\). Their sum is \(a_i\), because \(\sum_jb_j=0\). Hence \(t_{a_i}=1\) and
\[
 D_h(a_i)=\sum_{j\ne i}c_j-c_i=4-2c_i.
\]
The identical calculation gives \(D_h(b_i)=4-2c_i\). At \(d_i\), the neighbors are \(a_i,b_i\), whose sum is \(d_i\); thus \(t_{d_i}=1\) and \(D_h(d_i)=2c_i\), since \(h(d_i)=0\). The full first divisor is therefore:

| Rays | Germ value on primitive ray | First-divisor weight | Tangential multiple |
|---|---:|---:|---:|
| \(a_1,a_2\), each | 1 | 2 | 1 |
| \(a_3\) | 2 | 0 | 1 |
| \(b_1,b_2\), each | 1 | 2 | 1 |
| \(b_3\) | 2 | 0 | 1 |
| \(d_1,d_2\), each | 0 | 2 | 1 |
| \(d_3\) | 0 | 4 | 1 |

Its first projection is \(4(u_1+u_2+u_3)=0\); its second projection is the same. This checks balancing directly. Formula (4), retaining also the zero-valued diagonal rays and the zero-weight branching axes, gives
\[
 \mathrm{MA}_{\mathrm{poly},\mathbb R}(\gamma)\{(A,A)\}
       =2+2+2+2=8.
 \tag{11}
\]
This is the full recursive coefficient, not a relative-interior top-face calculation. The tight PCC (7) only forces the envelope value at the noncontact junction; it does not force this coefficient to vanish.

## Complete negative integral and all other faces

By the PA operator definition and the reconstructed refinement compatibility, the complete measure is a finite zero-cycle supported on \(\Pi^{(0)}\). At every nonzero vertex (6) gives gap zero. At zero, (5) and (10) give gap \(-1\), and (11) gives mass eight. Therefore the **complete** integral is
\[
 \sum_{v\in\Pi^{(0)}}(P_\gamma(u)(v)-f(v))\,
                           (\gamma^2\cdot[X])(v)
                    =(-1)\,8=-8.
 \tag{12}
\]
This argument includes all contact atoms regardless of their coefficients and all zero coefficients. A refinement for the obstacle may introduce vertices in \(0<\rho<1/10\) where the gap is nonzero; those points were not vertices of \(\Pi\), and refinement compatibility proves their complete coefficient is zero. Intermediate diagonal faces and original junction fibres are already included by the successive divisors, and they cannot create an extra zero-cycle outside the vertices of \(\Pi\). The bounded cycles and all thirty-six product edge cells remain present throughout the raw comparison and operator construction. Ends do not carry an additional PA atom at infinity. The constant-shift regularization has a constant sequence of finite measures, so there is no escaping or boundary measure in this construction.

This also explains the limitation concerning stricter prospective theorems. The reference is zero on the small balanced diagonal three-ray curve used in (7). A hypothesis forbidding such a local flat balanced curve is not satisfied here. No conjunction involving an additional strict-convexity package is refuted beyond the actual hypotheses in the assignment.

## Exact finite evidence and failed construction diagnostic

The proof of (12) does not require numerical identification of the other vertices or their masses. Nevertheless `exact_counterexample.py` enumerates the complete rational affine domains and recursively computes every coefficient, including all contact ones. It uses only Python's exact `Fraction` arithmetic and the input in `counterexample-input.json`.

On each actual product edge plane, \(\rho\) is affine. The program restricts the four difference-norm affine pieces and \(\rho/4-1\), intersects the domain where each is maximal with the two primitive parameter intervals/rays, solves all pairs of active rational boundary equations, and retains precisely the two-dimensional domains. This gives 53 top domains and 12 vertices. Every vertex is checked against every incident domain. For every incident tangent cone, both actual primitive boundary rays are obtained from its active inequalities; its saturated index is their determinant in the actual primitive factor basis. Top balancing, consistency of germ values, nonnegativity and balancing of the full first divisor, and (4) are checked at every vertex. Thus this is an exhaustive finite result for these specified rational data, not an enumeration of arbitrary obstacles or a mathematical correctness certificate.

Let
\[
 D_A=(-1,-1),\quad D_B=(5/3,-1/3),\quad D_C=(-1/3,5/3).
\]
The recorded complete output, with paired rows denoting both ordered points, is:

| Points | Gap | Mass, each | Max. index | Contribution, each |
|---|---:|---:|---:|---:|
| AA | -1 | 8 | 1 | -8 |
| BB and CC | 0 | 8 | 1 | 0 |
| AB, BA, AC and CA | 0 | 0 | 1 | 0 |
| BC and CB | 0 | 0 | 1 | 0 |
| \(D_AD_A\) | 0 | 4 | 16 | 0 |
| \(D_BD_B\) and \(D_CD_C\) | 0 | 9 | 16 | 0 |

Here AB denotes \((A,B)\), and similarly for the other concatenated labels. The reference values are one at AB, BA, AC and CA, two at BC and CB, and zero at the other displayed points. The six positive atoms have total mass 46, the six others have zero mass, and the complete finite sum is -8. The largest index is actually sixteen, not a normalization dropped at the distant cutoff points. For example, at \((D_A,D_A)\) the local rays are \((-5,-5,-3,-3)\), \((-3,-3,-5,-5)\), and \((1,1,1,1)\), with germ values \(4,4,0\) and first weights \(1/2,1/2,4\). The two nonzero contributions are two each. In primitive LA-product parameters the ray pairs have indices \(16,2,2\), and (3) yields exactly these real weights. The JSON output records every primitive ray, every neighbor index, every first weight and every coefficient, including the corresponding B- and C-cutoffs. These additional mass totals are finite computational evidence; the theorem (10)--(12) was proved independently of the enumeration.

The supplied rectangle-roof diagnostic is independently reconstructed. For the unit-weight balanced star \(u_1,u_2,u_3\) times an interval, ambient affine functions
\[
 A_i(q,t)=1-t+s_iq,\quad B_i(q,t)=t-s_iq,
 \qquad(s_1,s_2,s_3)=(1/2,-1/2,0)
\]
are PC, and their maximum is PC by the same maximum inequality. Their coordinatewise maximum corner values give branch convex roofs
\[
 H_1=\max\{1-q/2,1+q/2-t\},\quad
 H_2=\max\{1-q/2,q/2+t\},\quad H_3=1.
\]
Each displayed plane is below all four corresponding corner caps. Its triangular face gives the lower lifted hull, proving these roof formulas. At the shared centre \((v,1/2)\) and rational branch endpoints \((\varepsilon u_i,1/2)\) with coefficients \(1/3\), the centre is one and the mean is \(1-\varepsilon/3\). For \(\varepsilon=1/4\) the endpoint values are \(7/8,7/8,1\), mean \(11/12\), defect \(1/12\). Their barycentre is the centre, and the star product rectangles are actual cofaces; thus this is an actual failed PCC. A node assignment dominating both original corner arrays under their maximum caps would have to be their coordinatewise maximum, whose roofs fail this test. Consequently that roof-feasible finite-node set has no greatest assignment under those caps. The actual functional maximum has trace \(\max\{1-t,t\}\), with an additional fibre break. This diagnostic invalidates that coarse reconstruction scheme; by itself it is not a regularity or contact counterexample. The cyclic counterexample (5)--(12) supplies the new contact conclusion separately.

## Audit, artifacts, and unresolved scope

The main checks are: actual graph/product balancing; finite rational walls; recession-vector growth; all real PCC tests for the candidate; all local real-cycle PAPC tests; the zero-vertex PCC; finite pointed-cell generation; raw comparison with remote rational endpoints and real centres; explicit decreasing uniform regularization; actual primitive indices in the full two-stage recursion; and the zero gap at every other original operator vertex. All these checks are arguments in this file, not grants from source documents.

No statement is made that every raw envelope on this pair is PA, continuous or regularizable. No all-reference negative theorem is claimed. A general localization to arbitrary finite graphs and arbitrary real references would need its own growth-preserving construction and rational-domain proof. The local difference trap explains why a positive theorem for all products of two branched graph factors cannot follow merely from their rank-one positive relation cones. Complete affine factors, one-branched-factor positive theorems, arbitrary cycles on other graphs and the full original classification remain separate obligations. This result provides no analytic realization, CLD/delta/BFJ comparison, P05.5 claim, literal-category extension, priority assertion or independent mathematical certification.

All new artifacts are in the assigned fresh workspace. The authoritative argument is `P05.2-argument.md`; `P05.2-partial.tex` and its twice-compiled PDF are standalone renderings. `status.json` has exactly the required five keys. `author-self-audit.md` and `research-notes.md` preserve the scope, failed approaches and remaining obligations. `counterexample-input.json`, `exact_counterexample.py`, `counterexample-output.json` and `domain-enumeration.json` preserve the exact finite calculation. `sources/`, `source-excerpts.txt`, `source-hashes.json`, `environment.json`, `commands.txt` and `build-evidence.json` preserve read-only provenance and execution/build details. Source excerpts use `split('\n')` only, retaining PDF form feeds as ordinary characters, and the named proof boundaries were checked against their identifiers and final proof endings.

Rerun from this directory with `python3 snapshot_sources.py`, `python3 exact_counterexample.py`, and `python3 build.py`. The source-snapshot command requires the recorded read-only paths to remain available; the finite calculation and document build use local files. No supervised heavy-compute service was exposed, and none was required or launched. No subagent, network request, external message, installation, authentication, older-artifact write or SQL access was used. Execution success, source hashes and two successful PDF compilations document reproducibility, not mathematical verification. This remains an unverified proof draft.

Bibliography: BMPS, arXiv:2603.08664v1 (2026), definitions 2.1--2.4, 2.18--2.20, 2.28--2.31, 3.1--3.3, 3.14, 3.23, 4.4, 4.15, 6.2 and 6.9, with the inspected proof boundaries described above. The controlling book, round-06 local product draft, round-10 graph-cylinder draft, round-12 restricted certificate/example, and root rectangle-roof diagnostic are fallible comparison evidence, never theorem premises.



# Complete supporting proofs supplied for independent reconstruction

These are mathematical evidence, not grants of assumptions. Each application and dependency must be reconstructed. Prior verdicts and hashes do not replace these proofs.
