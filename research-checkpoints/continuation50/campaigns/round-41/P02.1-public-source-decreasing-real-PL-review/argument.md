# Exact final status

{
  "id": "P02.1",
  "status": "partial",
  "exact_result": "Draft proof of local decreasing strict semipositive real-PL sequences for arbitrary classical psh functions on separated smooth boundaryless second-countable strict analytic curves over complete nontrivially valued fields, and consequently for every arbitrary classical psh function defined on a full projective bundle over an ordinary open subset of a smooth separated algebraic curve over a field with a countable dense subset. Includes minus-infinity values, finite separable mesh realization, strict descent, one fixed neighbourhood, termwise chart overlaps, and pullback through every analytic scalar extension. This is a saturated-domain higher-dimensional sector, not the full arbitrary-germ characterization.",
  "proof_file": "P02.1-argument.md",
  "concrete_gaps": [
    "No sharp characterization or necessity/failure range for arbitrary classical psh germs in dimension at least two.",
    "The fibre argument needs the whole compact projective fibre; arbitrary functions on nonsaturated affine/open fibre charts are not covered.",
    "Smooth normal unibranch examples do not establish sufficiency of normality or unibranchness alone.",
    "No general strict PL descent through nonflat singular-curve or higher-dimensional normalization is proved.",
    "No unrestricted non-second-countable extraction for arbitrary new starting functions, or genuine analytic counterexample to sequential regularization, is provided.",
    "Boundary geometry and general tropical-chart overlap gluing outside the proved sector remain unresolved."
  ]
}


# Entire final proof

---
title: "P02.1: strict real-PL curve regularization and a projective-bundle sector"
author: "Fresh draft; mathematical claims require verification"
date: "2026-10-04"
---

# Result and scope

The original higher-dimensional characterization remains open in this draft. The result proved here concerns **every classical curve-test psh function on a full projective bundle over a curve**, with no continuity, invariance, finiteness, residue-characteristic, residue-genus, or residue-Picard-torsion restriction on that function. The domain must contain the entire projective fibres. This is an unrestricted starting-function sector on genuine smooth, normal, unibranch spaces of dimension at least two. It is not a theorem about every psh germ on every open subset of those spaces.

There are two principal assertions.

**Curve assertion A.** Let $K$ be a complete nontrivially valued non-Archimedean field. Let $C$ be a separated smooth, strictly $K$-analytic space of pure dimension one, called a curve here; smooth means rig-smooth and without relative boundary over $K$. Such curves are good. Suppose the underlying topological space of $C$ is second countable. For every classically psh function $h:C\to\mathbb R\cup\{-\infty\}$ and every $b\in C$, there is a fixed ordinary open neighbourhood $W$ of $b$ and a sequence of finite semipositive **strict GJR real-PL** functions $q_n:W\to\mathbb R$ such that $q_n\downarrow h|_W$ pointwise. If $h|_W$ is finite and continuous, the convergence is uniform on each compact subset of $W$. The general conclusion is pointwise, including points with value $-\infty$.

**Projective-bundle assertion B.** Let $K$ be as above and suppose it has a countable dense subset. Let $C_0$ be a smooth connected separated algebraic curve of finite type over $K$, let $\Omega\subset C_0^{\mathrm{an}}$ be an ordinary open subset, and let $E$ be an algebraic vector bundle of rank $r+1\geq2$ on $C_0$. Write
$$p:X:=\mathbb P(E)^{\mathrm{an}}\times_{C_0^{\mathrm{an}}}\Omega\longrightarrow\Omega.$$
For every classical psh $u:X\to\mathbb R\cup\{-\infty\}$ and every $x\in X$, there is a fixed ordinary open neighbourhood $V=p^{-1}(W)$ of $x$ and finite semipositive strict real-PL functions $v_n:V\to\mathbb R$ with $v_n\downarrow u|_V$ pointwise. The actual functions are $v_n=q_n\circ p$. They are globally defined on this one neighbourhood, independently of a projective trivialization. The same result includes the proper projective factor $X=\Omega\times(\mathbb P_K^r)^{\mathrm{an}}$.

In both assertions every analytic scalar extension preserves the displayed sequence, its strict real-PL membership, semipositivity, and pointwise decreasing limit. No new countability assumption is imposed on the extension field for this pullback statement. Assertion B also holds if the relevant base curve is already known to be second countable; the countable dense field hypothesis is one explicit sufficient way to obtain that topology. Neither that hypothesis nor smoothness is asserted to be necessary for the original problem.

# Checked published foundations

Only the listed public caches are used. The identifiers below are citations to those caches, not local research notes.

* **[GR-classical]** Gubler--Rabinoff, arXiv:2506.13548v2. Definition 3.4 and 3.4.1 identify the curve-test subharmonic class on a connected smooth strict curve with Thuillier's class or the constant $-\infty$. Proposition 3.5(7--9) gives scalar compatibility, finite functoriality, and finiteness at non-rig-points unless the function is identically $-\infty$ on the corresponding interior irreducible component. Definition 4.1 quantifies over every analytic extension field and every analytic curve. Proposition 4.2 gives scalar and morphism pullbacks. Theorem 4.3 identifies **already real-PL** classical psh functions with semipositive real-PL functions on any good strict space over a nontrivially valued field. Theorem 6.1 gives the local maximum principle at interior points. Relevant PDF pages are 10--11, 21--23, and 30--31; pages 5--7 give the basic topology and fibre facts used below.
* **[Thu]** Thuillier's thesis, public HAL version. Printed pages 19--20 distinguish the all-analytic-domain site $X_G$ from the strict rigid site $X_R$. Definition 3.2.1, printed page 68, defines lisse functions using arbitrary affinoid domains. Proposition 3.2.4 and its proof, printed page 69, give a finite separable extension and a semistable skeletal description on a compact strict domain; the proof explicitly treats $\varphi\in A^0(Y)$ for such a compact $Y$. Proposition 2.2.21, printed pages 42--43, describes scalar extension of a semistable skeleton as a surjective G-local isomorphism of weighted integral polyhedra. Theorem 3.2.10, printed pages 73--75, identifies the Laplacian of a skeletal pullback on $Y\setminus\partial Y$ with the graph Laplacian. Its graph sign convention on printed pages 5--7 is the sum of weighted outgoing slopes. Proposition 3.4.4, printed pages 90--91, says lisse functions are subharmonic exactly when their Laplacian is nonnegative. Theorem 3.4.2 and its proof, printed pages 89--90, construct a decreasing **family**, not a sequence, of finite continuous lisse functions $h_S$ on a compact $Y$, subharmonic on $Y\setminus\partial Y$, whose infimum there is $h$. Corollary 3.4.5 gives scalar pullback of subharmonicity.
* **[GJR]** Gubler--Jell--Rabinoff, arXiv:2111.05741. Definition 5.1 and the preceding convention use strict analytic domains for the real-PL G-topology. Lemma 5.4 gives morphism and scalar pullback. Proposition 5.11 gives descent of real-PL membership under a finite flat surjective morphism, with divisible coefficients, in particular $\mathbb R$. Corollary 5.12 gives the corresponding field-extension statement for a completion of an algebraic extension, with its finite case explicitly deduced from 5.11. Sections 5.5--5.7 identify integral model functions with strict PL functions and permit real linear combinations. Sections 15.3--15.4 give admissible subdivisions when all subdivision coordinates lie in the value group and vertical Cartier model functions for piecewise $(\mathbb Z,\Gamma)$-linear skeletal functions. Section 15.8 gives strict domains for the corresponding subgraphs. Proposition 7.6 gives semipositivity under morphism and scalar pullback. These statements are checked on PDF pages 31--36, 45--47, and 77--80.
* **[GR-PL]** Gubler--Rabinoff, arXiv:2503.05513 as cached, Proposition **5.1**, pages 15--16, gives the curve subharmonicity/semipositivity comparison for real-PL functions. Its Corollary **5.4**, pages 16--17, gives the curve-testing comparison. The proof of [GR-classical] Theorem 4.3 refers to these results using earlier labels 3.1 and 3.5. The cached March source has different labels; this draft uses the actual checked statements and does not infer a missing statement from a label.
* **[Ber93]** Berkovich, PMIHES 78 (1993). Proposition 1.5.5, printed pages 34--35, identifies the interior of an analytic domain relative to its ambient space with its ordinary topological interior, and gives composition/base-change rules. Corollary 2.2.7, printed pages 42--43, identifies reduced, normal, and regular loci of algebraic analytifications with their algebraic counterparts. [GJR] page 8 explicitly recalls that algebraic analytifications are good, strict, and boundaryless over a nontrivially valued field.

No unpublished book assertion is a premise. [GJR] Proposition 15.11, pages 80--81, is a weakly smooth regularization **net**. Its proof explicitly permits subdivisions at arbitrary points and explicitly disclaims a formal model for such subdivisions. It is not used as a theorem of strict real-PL regularization. [Wan], cached arXiv:1801.04713v3, Corollary 5.4, page 31, assumes a smooth proper curve, a continuous finite starting function, and residue field algebraic over a finite field or the projective-line/Mumford-curve alternatives for its ordinary CLD-smooth conclusion. Those hypotheses are recorded for comparison only; that conclusion is not used here. The CD cache is hash-checked but no theorem from it is a premise.

# Strict membership cannot follow from the all-domain lisse sheaf

The two sites in [Thu] are genuinely different. A lisse function can have a corner at a point whose annular radius is not in the divisible hull of the ground-field value group. All-domain sheafification of logarithms does not prove strict GJR membership there.

This is visible in [GJR] Example 5.3. Normalize the additive value group to $\Gamma=\mathbb Q$ and put $t=-\log|T|$ on a rank-one torus. The functions $\pi\log|T|+1$ and $0$ are strict real-PL: a real constant is a real multiple of $\log|a|$ for any fixed $a\in K^\times$ with $|a|\ne1$. Their maximum has tropical potential
$$F(t)=\max\{-\pi t+1,0\},$$
with a corner at $t=1/\pi\notin\mathbb Q$. Strict affinoid tropical intervals have rational vertices; the example concludes that this maximum is not strict real-PL. The function is nevertheless classical psh by the cone/max property in [GR-classical], since $\log|T|$ is pluriharmonic and the coefficients are nonnegative. This is a **membership counterexample**, not a counterexample to decreasing regularization. The repair below deliberately avoids maxima of arbitrary real-PL functions and moves all chosen subdivision coordinates into an actual finite-extension value group.

# A one-sided strict approximation lemma on a compact curve domain

**Lemma 1.** Let $C$ be a smooth strict curve over a complete nontrivially valued $K$. Let $Y\subset C$ be a compact strictly affinoid domain and set $W=Y\setminus\partial_KY$. Suppose $f\in A^0(Y)$ is finite and continuous on $Y$ and subharmonic on $W$. For every $\epsilon>0$ there is a continuous strict real-PL function $g$ on all of $Y$, semipositive on $W$, with
$$f\le g\le f+\epsilon\quad\hbox{on }Y.$$

Here $A^0$ is Thuillier's lisse sheaf on the all-domain site. Membership of $f$ in strict real-PL is neither assumed nor deduced from that sheaf.

**Proof: the finite extension and its mesh.** The compact-domain argument of [Thu] Proposition 3.2.4 supplies a finite separable extension $L/K$, a simply semistable formal model $\mathfrak Y$ of $Y_L$, its finite weighted skeleton $\Sigma$, and a continuous piecewise affine real function $F$ with $f_L=F\circ\tau$. Replace $L$ by its finite Galois closure over $K$ and base change the model. A semistable nodal chart has equation $xy=a$, $a\in L^{\circ\circ}\setminus\{0\}$; base change preserves this equation and semistability. [Thu] Proposition 2.2.21 describes the new skeleton and weights. Retractions commute with this extension: in a nodal chart they are determined by $-\log|x|$, and in a smooth tube they retract to the corresponding component vertex. Thus $f$ still factors through the new skeleton, and each lifted edge has the same affine coordinate and slopes as its source edge.

Let $M_0\ge0$ bound the absolute values of the finitely many slopes of $F$. Choose a positive mesh scale $\delta$ with $M_0\delta<\epsilon$ (use $\epsilon/(M_0+1)$ to include $M_0=0$). Put $\Gamma_L=-\log|L^\times|$. Every original edge length lies in $\Gamma_L$. If $\Gamma_L$ is dense, choose $0<\delta\in\Gamma_L$ that satisfies this bound. Cut each original edge at successive multiples of $\delta$ from one endpoint, retaining its other endpoint. If $\Gamma_L=\gamma\mathbb Z$ is discrete, choose an integer $N$ arbitrarily large with $N$ prime to $\operatorname{char}K$ when that characteristic is positive, put $\delta=\gamma/N$, and make the same cuts. All finitely many cut coordinates then lie in $(1/N)\Gamma_L$. Roots of finitely many scalars of valuations $N t$ make these coordinates actual values in a finite separable extension: $X^N-a$ is separable because $N$ is invertible in the field. This also works in mixed characteristic, with no condition on the residue characteristic.

For the later strict-domain membership proof choose an integer $D\ge5$ prime to $\operatorname{char}K$ when necessary. Include the finitely many auxiliary coordinates at fractions $1/D$, $2/D$, $(D-2)/D$, and $(D-1)/D$ of each mesh segment. Adjoin roots of scalars to realize them too. All coordinates used so far have denominators prime to the field characteristic. There is consequently a single finite separable extension realizing them all; take a finite Galois closure $M/K$ containing $L$. In the dense-group case adjoining the finitely many $D$-th roots has the same effect for the auxiliary coordinates. Base change $\mathfrak Y$ to $M$. Each lifted edge has the same mesh coordinates, now in $\Gamma_M=-\log|M^\times|$, and edge mesh size at most $\delta$. This step never claims that an irrational real breakpoint becomes a strict vertex. The original breakpoints can remain irrational; only the replacement mesh is used for the approximant.

**Proof: chord interpolation and positivity.** Write $F_M$ for the pullback skeletal potential. By subharmonicity and [Thu] Theorem 3.2.10 and Proposition 3.4.4, $F_M$ is convex on every original edge and the weighted sum of its outgoing slopes at every original vertex outside the graph boundary is nonnegative. Graph boundary vertices correspond to $\partial_M Y_M$. Convexity includes every corner in an edge, regardless of its value-group coordinate.

Define $G$ to equal $F_M$ at the original and mesh vertices and to be affine between consecutive mesh vertices. On a segment $[s,t]$ this means
$$G(z)=\frac{t-z}{t-s}F_M(s)+\frac{z-s}{t-s}F_M(t).$$
At isolated vertices retain $F_M$. Convexity gives $G\ge F_M$. The Lipschitz bound gives, everywhere on that segment,
$$0\le G(z)-F_M(z)\le M_0(t-s)\le M_0\delta<\epsilon.$$
At an original vertex $v$ the chord slope along each outgoing edge is at least the original outgoing derivative, by convexity in the coordinate measured away from $v$. Every edge weight is positive, so its weighted outgoing-slope sum remains nonnegative. At a new mesh vertex the right chord slope is at least the left chord slope, again by convexity; the two halves have the same edge weight. Thus all new Laplacian masses are nonnegative. No sign is required at vertices in the actual relative boundary $\partial_M Y_M$. [Thu] Proposition 3.2.4 (sufficiency for a piecewise affine skeletal potential) and Theorem 3.2.10 now give a finite continuous lisse subharmonic function
$$g_M^0=G\circ\tau_M\quad\hbox{on }W_M,$$
continuous on all of $Y_M$, with $f_M\le g_M^0\le f_M+\epsilon$ there. Boundary equality for $F_M$ and $G$ is retained, although positivity is only asserted after deleting the boundary.

**Proof: actual strict real-PL membership.** This is separate from the preceding lisse/subharmonic argument. All mesh and auxiliary coordinates lie in $\Gamma_M$. On the subdivided graph cover each mesh vertex by the closed star that runs a fraction $2/D$ into each adjacent mesh segment. Cover the remaining parts by the central intervals with endpoints at fractions $1/D$ and $(D-1)/D$. These form a finite neighbourhood cover of the graph; parallel edges have distinct star endpoints. Their retraction inverse images form a strict analytic G-cover of $Y_M$, by [GJR] 15.3, 15.4 and 15.8. They also cover all residual-disc tubes, because the retraction inverse image of a vertex is included in its star. Auxiliary subdivision is admissible because its vertices are in the actual value group, even when that group is discrete.

On an interval $I$ the function $G$ has the form $c+a t$. The coordinate $t$ is the logarithmic coordinate of a unit on the corresponding annulus, up to sign and a value-group constant. It is integral PL there. A real constant is real-PL: choose $\alpha\in M^\times$ with $\log|\alpha|\ne0$ and write $c=(c/\log|\alpha|)\log|\alpha|$.

On a star $U$ with centre $v$, for each incident mesh edge $e$ let $H_e$ be the function that is zero on all other star arms and equals the distance from $v$ on arm $e$. It is continuous, with integral slope $1$ on that arm and slope $0$ on the others. Its intercepts, in the original annular coordinates, lie in $\Gamma_M$ because $v$ and every star endpoint have coordinates in $\Gamma_M$. Hence $H_e$ is piecewise $(\mathbb Z,\Gamma_M)$-linear in the exact sense of [GJR] 15.1. Section 15.4 supplies a vertical Cartier divisor on an admissible formal model of $\tau_M^{-1}(U)$ whose model function is $H_e\circ\tau_M$. By 5.5--5.6 this function is strict integral PL. On that entire strict star domain,
$$G\circ\tau_M=G(v)+\sum_{e\ni v}a_e(H_e\circ\tau_M),$$
where $a_e\in\mathbb R$ is the outgoing slope of $G$ on arm $e$. Section 5.7 or Definition 5.1 gives strict real-PL membership. This construction imposes no harmonicity or Picard-torsion condition on the star basis functions. Their associated residue line bundles need not be trivial; this is why the construction does not assert ordinary CLD smoothness. Isolated vertices use only the constant formula.

The interval and star formulas agree on every intersection, since each is literally $G\circ\tau_M$. This proves global strict real-PL membership on $Y_M$, not just a collection of germs on unrelated domains. Since it is subharmonic on $W_M$, [GR-classical] 3.4.1 and Theorem 4.3 give semipositivity there.

**Proof: averaging and descent to the stated field.** The skeleton and interpolation need not be invariant under $\operatorname{Gal}(M/K)$. Put
$$\widetilde g_M=\frac1{[M:K]}\sum_{\sigma\in\operatorname{Gal}(M/K)}g_M^0\circ\sigma.$$
Automorphisms preserve $W_M$, strict real-PL membership and subharmonicity. Finite sums with nonnegative real coefficients preserve subharmonicity and, by common refinements of strict G-covers, strict real-PL membership. Since $f_M$ is invariant, $f_M\le\widetilde g_M\le f_M+\epsilon$. The average is invariant and descends to a continuous real function $g$ on $Y$.

For completeness, this continuous descent uses an actual quotient. Over $y\in Y$, the finite $\mathcal H(y)$-algebra $\mathcal H(y)\otimes_KM$ is a product of finite field extensions. The factors correspond to orbits of embeddings of $M$ into an algebraic closure of $\mathcal H(y)$; normality of $M/K$ makes the action of $\operatorname{Gal}(M/K)$ transitive on the factors. Each factor has the unique absolute value extending that of the complete field $\mathcal H(y)$. Therefore the Galois action is transitive on the analytic fibre of $Y_M\to Y$. This finite surjective map between compact Hausdorff spaces is a closed quotient, so an invariant continuous function has a unique continuous descent.

The projection $Y_M\to Y$ is finite, flat and surjective: on affinoid algebras its completed tensor product with the finite-dimensional field $M$ is free of rank $[M:K]$. Apply [GJR] Corollary 5.12 with coefficient group $\mathbb R$, good strict $Y$, and the finite complete algebraic extension $M/K$. It proves $g\in\operatorname{PL}_{\mathbb R}(Y)$ from the proved strict $M$-real-PL membership of $\widetilde g_M$. The corollary's finite case is explicitly a consequence of Proposition 5.11. This is strict descent across the two ground fields, not an all-domain sheaf argument. Scalar compatibility for subharmonicity in [GR-classical] Proposition 3.5(7) proves that $g$ is subharmonic on $W$, since its pullback is subharmonic on $W_M$. Here $W_M=Y_M\setminus\partial_M Y_M$: the finite projection is boundaryless, as is $\mathcal M(M)\to\mathcal M(K)$, and the good composition rule in [Ber93] 1.5.5(ii) gives equality of the relevant interiors first over $K$ and then over $M$. Theorem 4.3 then makes $g|_W$ semipositive. Surjectivity passes the displayed one-sided inequalities to $Y$. This proves Lemma 1.

# Extracting a sequence without continuity of the starting function

**Lemma 2.** Let $Z$ be a second-countable space, $h:Z\to\mathbb R\cup\{-\infty\}$ upper semicontinuous, and $(f_i)_{i\in I}$ a pointwise decreasing directed family of finite continuous functions with $h=\inf_i f_i$. There is a decreasing sequence from that family with pointwise infimum $h$.

For each $a\in\mathbb Q$, the open set $\{h<a\}$ is the union of the open sets $\{f_i<a\}$. Every open subspace of a second-countable space is Lindelof. Select a countable subcover for each rational $a$, and enumerate the countable union of selected indices. Choose successive upper bounds in the directed set, retaining all previous choices. The resulting functions decrease. If $h(z)<a$, a selected index has $f_i(z)<a$ and every later chosen upper bound has the same inequality. Since this holds for every rational $a>h(z)$, the sequence has infimum $h(z)$; when $h(z)=-\infty$ it holds for all rational $a$. The converse inequality follows from $f_i\ge h$. This proves the lemma without Dini's theorem or a finite-valued assumption on $h$.

The field hypothesis in B supplies second countability, as follows. If $K$ has a countable dense subset, a strict affinoid algebra $A$ has a countable norm-dense subset, by taking images of polynomials with coefficients in a countable dense subfield in a presentation by a Tate algebra. One obtains that subfield by adjoining the countable dense set to the prime field. Choose such a dense subset $(a_j)$. For bounded seminorms on $A$, evaluation is uniformly approximated by evaluation on this subset: the inequality $\big||a(x)|-|b(x)|\big|\le\|a-b\|$ uses a quotient Banach norm in a Tate presentation. Consequently evaluation on $(a_j)$ separates points and induces the full topology on $\mathcal M(A)$. A continuous injection of this compact Hausdorff space into $\mathbb R_{\ge0}^{\mathbb N}$ is a homeomorphism onto its image. Thus every such affinoid is compact metrizable and second countable.

Cover an algebraic curve of finite type by finitely many affine charts. Embed each affine chart in an affine space and exhaust it by intersections with closed polydiscs of radii $R^m$, where $R\in|K^\times|$, $R>1$, and $m\ge1$. These intersections are strict affinoids. The ordinary open subsets on which all coordinate norms are $<R^m$ lie inside their respective affinoids and cover the affine chart. Each is second countable by the preceding paragraph. The resulting countable ordinary open cover gives a countable base for the whole analytification; ordinary open subspaces inherit one. No metrizability of arbitrary scalar extensions is needed for pulling back an already chosen sequence.

# Proof of curve assertion A

Work in the connected component of $b$, which is ordinary open for a smooth analytic curve. If $h$ is identically $-\infty$ there, set $q_n=-n$ on any ordinary neighbourhood. Constants are strict real-PL and harmonic, so this deals explicitly with the permitted identically infinite-negative case.

Otherwise [GR-classical] 3.4.1 gives Thuillier subharmonicity. Smoothness and connectedness make this component irreducible; [GR-classical] Proposition 3.5(9) makes $h$ finite at all its non-rig-points. Choose a connected compact strictly affinoid neighbourhood $Y$ of $b$ contained in $C$ with $b$ in its ordinary interior. Such neighbourhoods exist by goodness and strictness. A connected component can be selected using affinoid idempotents. The relative boundary $\partial_KY$ is the finite Shilov boundary, consisting of non-rig-points; its values of $h$ are finite. Since the ambient curve has no boundary, [Ber93] 1.5.5 identifies
$$W=Y\setminus\partial_KY=\operatorname{Int}_C(Y)$$
as one ordinary open neighbourhood of $b$, relatively compact in $C$. This is an actual relative-boundary deletion, not an unspecified tropical relative interior.

Use the construction in [Thu] Theorem 3.4.2 on this particular $Y$. It gives finite continuous $f_S\in A^0(Y)$, indexed by finite subsets $S\subset I(Y)$ containing $\partial_KY$, with $f_S=h$ on $S$, harmonic off $S$, subharmonic on $W$, and
$$h|_W=\inf_S f_S|_W,\qquad f_{S'}\le f_S\quad(S\subset S').$$
The source proof of the infimum assertion includes rigid-point and type-IV values through its determination lemma 3.4.1; no continuity of $h$ is inserted. Lemma 2 extracts a decreasing sequence $f_n$ on $W$. In this directed family upper bounds can simply be finite unions, so the same chosen functions remain finite continuous lisse functions on all of $Y$ and decrease there as well.

Apply Lemma 1 independently to $f_n$ with $\epsilon_n=2^{-n}$, always on this same $Y$ and $W$, obtaining $g_n$ with $f_n\le g_n\le f_n+2^{-n}$. Define
$$q_n=g_n+2^{-n}.$$
The shift is a strict real-PL harmonic constant. Each $q_n$ is finite, strict real-PL and semipositive on $W$. The exact interstage inequality is
$$q_{n+1}\le f_{n+1}+2^{-n}\le f_n+2^{-n}\le g_n+2^{-n}=q_n.$$
Furthermore $h\le q_n$ and $0\le q_n-f_n\le2^{1-n}$. Thus $q_n\downarrow h$ pointwise, including $h=-\infty$ points. The finite extensions and models used in Lemma 1 may vary with $n$, but the descended functions all have domain $Y$ and the semipositive sequence all has domain $W$.

If $h$ is finite continuous on $W$, any compact subset $A\subset W$ has continuous restrictions $q_n|_A\downarrow h|_A$. For a fixed $\eta>0$, the open subsets $\{q_n-h<\eta\}$ increase and cover $A$. Compactness gives one index covering $A$, proving uniform convergence there. This proves the optional continuous conclusion and assertion A.

# Projective fibres, descent, and proof of assertion B

**Compact constancy lemma.** A classical psh function $w$ on a connected compact boundaryless analytic space $F$ is constant, with $-\infty$ allowed. If it is not identically $-\infty$, upper semicontinuity and compactness give a finite attained maximum $m$: local finite upper bounds have a finite subcover, and the supremum is attained by compactness. The set $\{w=m\}$ is nonempty and closed. It is open by [GR-classical] Theorem 6.1, because every point of $F$ is an interior point. Connectedness makes it all of $F$.

For any complete nontrivially valued field $H$, $(\mathbb P_H^r)^{\mathrm{an}}$ has the hypotheses of this lemma. Compactness is given by its finite standard closed unit-polydisc cover, indexed by a coordinate of maximal norm. It is good, strict and boundaryless as an algebraic analytification, as recalled in [GJR] page 8. Connectedness can also be checked in this cover: a closed unit polydisc is connected and every pair of the standard charts meets, for instance at the point with all homogeneous coordinates $1$.

Here is a direct verification of the polydisc fact to avoid an unstated connectedness premise. If $z$ is a point of the closed unit polydisc with coordinate values $z_i$ in $\mathcal H(z)$, evaluate $P(z_1+U_1,\ldots,z_r+U_r)$ with the Gauss norm of polyradius $s\in[0,1]$ over $\mathcal H(z)$. This defines a multiplicative seminorm $H_s(z)$ bounded by the unit-polydisc norm. At $s=0$ it is $z$; at $s=1$ it is the unit Gauss point, since translation by coordinates of norm at most $1$ and its inverse preserve the unit Gauss norm. For each polynomial the value is a maximum of finitely many continuous expressions in $s$, hence the path is continuous; norm density extends continuity to the Tate algebra. Every point has a path to the Gauss point, proving connectedness. The argument applies to each fibre field $H=\mathcal H(b)$ without any countability assumption.

Now let $u$ be arbitrary classical psh on $X$ in B. For $b\in\Omega$, extend scalars to $\mathcal H(b)$ and include the analytic fibre
$$p^{-1}(b)\simeq(\mathbb P_{\mathcal H(b)}^r)^{\mathrm{an}}\longrightarrow X_{\mathcal H(b)}.$$
The fibre-to-extension morphism uses the $\mathcal H(b)$-point of $\Omega_{\mathcal H(b)}$ lying over $b$. [GR-classical] Proposition 4.2 makes the restriction of the scalar pullback of $u$ classical psh on this fibre. The compact constancy lemma proves constancy on the entire fibre, not merely on its rigid points. Thus there is a uniquely defined function $h:\Omega\to\mathbb R\cup\{-\infty\}$ with $u=h\circ p$.

On an ordinary open base set $U$ where the projective bundle trivializes, choose the analytic section $s_U$ corresponding to $[1:0:\cdots:0]$. Then $h|_U=u\circ s_U$. It is upper semicontinuous and classical psh by Proposition 4.2. Sections from different trivializations have the same $u$-value over every base point, by the fibre constancy just proved. These descriptions agree exactly on overlaps. By sheafiness in Proposition 4.2, $h$ is classical psh on $\Omega$, including its possible discontinuities and $-\infty$ values.

The countable dense field hypothesis makes $\Omega$ second countable by the proof preceding assertion A. Apply A at $b=p(x)$ to obtain one $W$ and one sequence $q_n$. The inverse image $V=p^{-1}(W)$ is an ordinary open neighbourhood of $x$. Set $v_n=q_n\circ p$ on all of $V$. [GJR] Lemma 5.4(1) proves actual strict real-PL membership and Proposition 7.6(1) proves semipositivity. These results apply to good strict spaces and do not require $p$ to be finite. Pointwise evaluation gives
$$v_{n+1}(y)\le v_n(y),\qquad\lim_n v_n(y)=h(p(y))=u(y)\quad(y\in V).$$
There are no functions independently chosen in overlapping projective charts: every chart sees exactly the same pullback $q_n\circ p$. Hence the approximants agree on all overlaps, term by term. The image under $p$ of any compact subset of $V$ is compact in $W$, so the optional finite-continuous convergence assertion pulls back too.

The space in B is a genuine higher-dimensional geometric example: $\mathbb P(E)$ is smooth over $K$, with dimension $r+1$. [Ber93] Corollary 2.2.7 passes regularity and normality to its analytification and to its ordinary open subspace $X$. Regular local rings are domains and normal; a normal local ring is unibranch since its normalization is itself. No normalization descent is involved in this proof. Nontrivial projective-bundle transition functions are allowed. In particular $\mathbb A_K^{1,\mathrm{an}}\times(\mathbb P_K^r)^{\mathrm{an}}$ has this sector for all its globally defined classical psh functions, including the pullbacks of $\log|t-a|$ with poles $-\infty$. The proof imposes no torus invariance condition.

# Scalar extension and the precise overlap claim

Let $K'/K$ be **any** analytic extension field, and let $\pi:V_{K'}\to V$ be the scalar projection. [GJR] Lemma 5.4(2) and Proposition 7.6(2) give strict real-PL membership and semipositivity of $v_n\circ\pi$ over $K'$. At each $y'\in V_{K'}$,
$$v_n(\pi(y'))\downarrow u(\pi(y')).$$
Proposition 4.2(5) also verifies that the target scalar pullback is in the original classical curve-test class. The same argument applies to $q_n$ on $W$. The formulas commute with the base-changed projection $p_{K'}$ and with every projective coordinate transition. Finite separable extensions inside Lemma 1 were used only to construct a descended strict function; they do not replace the assertion about all analytic extensions by an assertion about algebraic ones. The extension space may be nonmetrizable. We pull back a sequence already constructed over $K$ and make no countable-extraction claim for arbitrary new functions over $K'$.

If two local constructions are made near two different base points, there is no assertion that their sequences agree on their common base open set. The proof needs no such assertion: at each point it constructs one sequence globally on one $W$, and pulls that single sequence back globally on one $V$. Within the charts used for that construction, all formulas agree exactly. A global regularization sequence on an arbitrary union of these neighbourhoods is not claimed.

# Necessity statements, counterexamples to shortcuts, and remaining obligations

**A sequence obstruction.** If $u=\inf_n v_n$ with finite continuous functions $v_n$ on a neighbourhood $V$, then for every real $a$,
$$\{u<a\}=\bigcup_{n,k\ge1}\{v_n\le a-1/k\}.$$
Every set on the right is closed in $V$. Thus all strict sublevel sets of $u$ must be $F_\sigma$ in that neighbourhood. Strict real-PL functions are continuous, so this is a necessary topological condition for the requested sequence. On a nonmetrizable space upper semicontinuity alone does not prove this condition. The draft constructs no classical psh function violating it, and this is not asserted to be a sharp analytic failure criterion. The Lindelof extraction above is a sufficient argument, not a proof that countable dense fields are necessary.

**Retraction necessity.** If analytic maps $s:B\to X$ and $p:X\to B$ satisfy $p\circ s=\mathrm{id}$, then local semipositive strict real-PL regularization on $X$ of all functions $h\circ p$ implies the corresponding local regularization on $B$: pull the displayed approximants back by $s$ on the ordinary open set $s^{-1}(V)$. Strict membership, semipositivity and decreasing convergence follow from [GJR] 5.4 and 7.6 and pointwise evaluation. Thus the curve factor is a real necessary test for projective bundles with sections; it is not bypassed by the higher-dimensional fibre. This is a proved functorial necessity, not a characterization of all good strict spaces.

**Why saturation and relative boundaries matter.** On a fibre affine coordinate chart, the classical psh function $\log|z_1|$ varies along the projective fibre. The chart omits the hyperplane at infinity; its portion of a fibre is not compact. The compact constancy argument therefore gives no descent for an arbitrary psh function defined only on that ordinary open chart. This is a counterexample to the proposed descent shortcut, not to PL regularization. Similarly a compact closed disc has an actual relative boundary and admits nonconstant classical psh functions, for example $\max\{\log|T|,\log|a|\}$ with $0<|a|<1$. This particular maximum is legal integral PL on its two strict domains. Its maximum lies at a boundary point, so applying the boundaryless maximum principle there would be incorrect.

**Normality and normalization.** The smooth normal unibranch examples in B have no normalization step. Neither normality nor unibranchness is proved sufficient for arbitrary higher-dimensional germs. For a singular curve, finite normalization need not be flat; [GJR] Proposition 5.11 cannot simply be applied to descend strict real-PL functions from it. Even when a normalization is a topological homeomorphism, that fact does not supply strict membership of a descended approximant. Approximating on separate branches and identifying values is also not a proof of monotonicity on one neighbourhood. No singular-curve or higher-dimensional normalization criterion is claimed here.

**Residue and genus range.** The strict star construction in Lemma 1 uses model line bundles and real coefficients, not local ordinary logarithmic harmonicity. Positive-genus residue components and nontorsion residue Picard classes are allowed. The obstruction to identifying every harmonic function with an ordinary CLD-smooth function, discussed in [GJR] Remark 15.10 and [Wan] Corollary 5.4, is therefore not converted into a false restriction or a false smoothness conclusion. No locally Fubini--Study, weakly smooth, or ordinary CLD-smooth approximant claim is needed or made for P02.1.

The following original obligations remain unresolved: a sharp geometric characterization for the full arbitrary classical psh germ class in dimension at least two; constructions for arbitrary germs in ordinary open affine parts of smooth normal unibranch spaces; sharp necessity or genuine failure examples for the regularization property; general singular/unibranch normalization descent; a replacement for second-countable extraction when the field and base topology are unrestricted; boundary cases outside the proved smooth-curve range; and arbitrary chart-overlap gluing outside the globally pulled-back projective-bundle sector. The $F_\sigma$ test, strict-maximum membership example, and failed descent shortcuts do not fill these gaps. Accordingly this draft is partial progress and is not a candidate complete solution of original P02.1.

# Reproducibility and evidence limits

The supplied `input.json` is retained together with its byte-identical copy `input-original.json`. `assignment-original.txt` and `task-original.json` retain the assignment string and task object; `retain_input.py` verifies these identities without replacing a differing original. `source-extracts/source-provenance.json` records all seven supplied hashes, literal cache-page extracts, selected primary PDF pages, rendered OCR checks, and the exact application checks. The programme `retain_sources.py` recreates those extracts only from the listed public caches. It neither accesses prior campaign work nor downloads material.

`graph_diagnostic.py` is a small exact-rational diagnostic of weighted-star chord positivity, one-sided bounds and the interstage shift inequality, for explicitly specified finite examples. Its output is retained in `diagnostics/graph-output.json`. This is a finite diagnostic of the formulas, not an exhaustive result over curves or a proof of membership in an analytic sheaf. The mathematical proofs above, with the checked published foundations, carry those claims.

`P02.1-paper.tex` is a standalone TeX document embedding this entire argument. `rerun.py` regenerates it using the existing Pandoc, compiles it twice using the existing pdfLaTeX without installation, and records return codes, actual warnings, log filenames, PDF information, source hashes and environment versions in `diagnostics/build-diagnostics.json`. Rerun from this directory with `python retain_sources.py` and `python rerun.py`. The resulting PDF is `build/P02.1-paper.pdf`. The schema-limited `status.json` records the partial status and concrete gaps. Successful extraction, exact finite arithmetic, and TeX compilation certify neither the published premises nor the new mathematics. No heavy computation, external worker, software installation, runtime change or network operation is used.


# Every actual native canonical note

[
  {
    "id": "n1",
    "summary": "Draft decreasing strict real-PL regularization for arbitrary classical psh on separated smooth boundaryless second-countable strict curves. Finite separable mesh realization, formal-model membership and Galois descent repair the invalid identification of Thuillier-lisse with strict real-PL. No sharp curve range is claimed.",
    "detailedSummary": "Over a complete nontrivially valued field, arbitrary classical psh functions, including permitted minus-infinity values, admit a local decreasing sequence under the stated curve and topology hypotheses. Thuillier supplies finite continuous lisse functions f_S on a compact strict domain Y, subharmonic on its ordinary interior W. Rational-sublevel Lindelof extraction supplies f_n without continuity of the target. Chord interpolation after finite separable mesh realization gives f_n <= g_n <= f_n+2^-n. Integral formal-model star functions prove actual strict real-PL membership; Galois averaging and GJR Corollary 5.12 descend it. The functions q_n=g_n+2^-n are semipositive, decrease because q_(n+1)<=f_(n+1)+2^-n<=q_n, and converge pointwise, including at minus-infinity points. No residue characteristic, perfection, genus or residue Picard-torsion restriction is added. This is an unverified draft proof of a sufficient curve range, not the original higher-dimensional characterization.",
    "text": "Draft theorem A. Let K be a complete nontrivially valued non-Archimedean field. Let C be a separated, smooth, strictly K-analytic space of pure dimension one. Smooth means rig-smooth and without relative boundary over K; such curves are good. Assume C is second countable. For every classical curve-test psh h:C→R∪{−∞} and every b∈C, there is one fixed ordinary open neighbourhood W of b and finite semipositive strict GJR real-PL functions q_n on W decreasing pointwise to h. Finite continuous targets additionally have uniform convergence on compact subsets. This is a draft mathematical proof, not an independent correctness certificate.\n\nChecked foundations. Gubler–Rabinoff, arXiv:2506.13548v2, Definition 3.4 and 3.4.1 identify the curve-test class on connected smooth strict curves with Thuillier subharmonic functions or the constant −∞. Proposition 3.5(7–9) supplies scalar compatibility, functoriality and finiteness at non-rig-points unless the function is identically −∞ on the relevant interior irreducible component. Definition 4.1 quantifies over all analytic extension fields and analytic curves. Proposition 4.2 gives classical psh pullbacks. Theorem 4.3 says an already strict real-PL function on a good strict space over a nontrivially valued field is semipositive exactly when it is classical psh. These statements were checked on PDF pages 10–11 and 21–23, with relevant proofs on pages 18–19.\n\nThuillier’s public HAL thesis distinguishes the all-domain site X_G from the strict rigid site X_R on printed pages 19–20. Definition 3.2.1, printed page 68, uses arbitrary affinoid domains for lisse functions. Proposition 3.2.4 and its proof, printed page 69, supply a finite separable extension and a semistable skeletal description on a compact strict domain; the proof explicitly treats φ∈A^0(Y) for compact Y. Proposition 2.2.21, printed pages 42–43, describes scalar extension of a semistable skeleton as a surjective G-local isomorphism of weighted integral polyhedra. The graph Laplacian is the sum of weighted outgoing slopes, as defined on printed pages 5–7. Theorem 3.2.10, printed pages 73–75, identifies the Laplacian of a skeletal pullback on Y minus its actual boundary with this graph Laplacian. Proposition 3.4.4, printed pages 90–91, characterizes subharmonic lisse functions by nonnegative Laplacian. Theorem 3.4.2 and its proof, printed pages 89–90, construct a decreasing family, not a sequence, of finite continuous lisse functions on compact Y, subharmonic on Y\\∂Y, with the required pointwise infimum. Corollary 3.4.5 gives scalar pullback of subharmonicity.\n\nGubler–Jell–Rabinoff, arXiv:2111.05741, Definition 5.1 uses strict analytic domains for real-PL membership. Sections 5.5–5.7 give integral model functions and their real linear combinations. Proposition 5.11 gives descent under finite flat surjective morphisms with divisible coefficients. Corollary 5.12 gives descent across a completion of an algebraic field extension; its finite case is explicitly deduced from 5.11. Sections 15.3–15.4 give admissible subdivisions when coordinates lie in the actual value group and vertical Cartier model functions for piecewise (Z,Γ)-linear skeletal functions. Section 15.8 gives strict domains for the corresponding subgraphs. Lemma 5.4 and Proposition 7.6 preserve strict membership and semipositivity under morphism and scalar pullbacks. Relevant checked PDF pages are 31–36, 45–47 and 77–80.\n\nThe cached March Gubler–Rabinoff paper, arXiv:2503.05513, labels its curve comparison Proposition 5.1 and its curve-testing comparison Corollary 5.4, on pages 15–17. The June proof refers to earlier labels 3.1 and 3.5. The actual cached statements, rather than an inferred missing label, were checked. Berkovich PMIHES 78 (1993), Proposition 1.5.5, printed pages 34–35, identifies relative domain interior with ordinary topological interior and gives the good composition rule used below.\n\nThe lisse/strict distinction is indispensable. GJR Example 5.3, page 31, takes value group Q and shows that max{π log|T|+1,0} has a corner at tropical coordinate 1/π and is not strict real-PL, although both inputs are strict real-PL. Thus arbitrary real maxima cannot be used to assert strict membership. GJR Proposition 15.11, pages 80–81, produces a decreasing weakly smooth net and explicitly permits subdivisions that are not formal-model subdivisions. It is not invoked as a strict real-PL regularization theorem.\n\nOne-sided approximation lemma. Suppose Y⊂C is a compact strictly affinoid domain, W=Y\\∂_K Y, and f∈A^0(Y) is finite continuous on Y and subharmonic on W. For every ε>0, there is a continuous strict real-PL g on all of Y, semipositive on W, satisfying f≤g≤f+ε on Y.\n\nFirst obtain, from the compact-domain argument of Thuillier Proposition 3.2.4, a finite separable extension L/K, a simply semistable formal model of Y_L, a finite weighted skeleton Σ, a retraction τ, and a continuous piecewise affine real F with f_L=F∘τ. Replace L by its finite Galois closure and base change the model. Nodal charts xy=a retain their equations after extension. Retractions commute with extension: on a nodal tube they use −log|x|, and on a smooth tube they retract to the corresponding component vertex. Thuillier Proposition 2.2.21 supplies the weighted skeletal compatibility. Lifted edges retain their affine coordinates and slopes.\n\nLet M_0 bound the absolute values of the finitely many slopes of F. Choose a mesh scale δ with M_0δ<ε; choosing δ<ε/(M_0+1) includes M_0=0. Write Γ_L=−log|L*|. Original edge lengths lie in Γ_L. If Γ_L is dense, choose such a positive δ in Γ_L. Cut each edge at successive multiples of δ, retaining its other endpoint. If Γ_L=γZ is discrete, choose an arbitrarily large integer N prime to char K when that characteristic is positive, and take δ=γ/N. These cut coordinates belong to (1/N)Γ_L. They become actual value-group coordinates after adjoining roots of finitely many scalars: X^N−a is separable because N is invertible in the field. Mixed characteristic requires no residue-characteristic restriction.\n\nFor strict star domains, choose an integer D≥5 prime to char K when necessary. Also include auxiliary coordinates at fractions 1/D, 2/D, (D−2)/D and (D−1)/D of every mesh segment. All the finitely many coordinates have denominators prime to the field characteristic. Adjoining appropriate roots realizes them in a single finite separable extension; take a finite Galois closure M/K containing L. In the dense case the additional D-th roots suffice for these auxiliary fractions. Base change the model to M. Every replacement and auxiliary coordinate now lies in the actual Γ_M. Original irrational breakpoints need not become legal vertices: they are replaced by the mesh, not asserted to be strict.\n\nWrite F_M for the lifted potential. Scalar subharmonicity, Thuillier Theorem 3.2.10 and Proposition 3.4.4 imply that F_M is convex on each original edge and has nonnegative weighted outgoing-slope sum at every original vertex outside the graph boundary. Define G to equal F_M at mesh and original vertices and to be affine between consecutive mesh vertices. At isolated vertices retain F_M. On a segment [s,t],\nG(z)=((t−z)F_M(s)+(z−s)F_M(t))/(t−s).\nConvexity gives G≥F_M. The Lipschitz bound gives 0≤G(z)−F_M(z)≤M_0(t−s)≤M_0δ<ε.\n\nAt an original vertex, the chord slope along every outgoing edge is at least the original outgoing derivative. Positive edge weights therefore preserve nonnegative weighted slope sum. At a replacement vertex in an edge, successive chord slopes are nondecreasing, and both halves have the same edge weight. Consequently all new Laplacian masses are nonnegative. No positivity condition is imposed at the actual boundary vertices. The skeletal lisse construction and graph Laplacian formula give g_M^0=G∘τ_M, continuous on Y_M and subharmonic on W_M, satisfying f_M≤g_M^0≤f_M+ε.\n\nActual strict membership is a separate argument. Cover each mesh vertex by its closed star running a fraction 2/D into each adjacent mesh segment, and cover the remaining edge portions by intervals with endpoints at fractions 1/D and (D−1)/D. This is a finite neighbourhood cover of the graph; parallel edges have distinct cut endpoints. Their retraction inverse images are strict analytic domains and form a G-cover of Y_M by GJR 15.3, 15.4 and 15.8. They include residual-disc tubes through the vertex stars. All subdivisions are admissible because their coordinates are actual Γ_M values, even for discrete value groups.\n\nOn an interval, G=c+at. The logarithmic annular coordinate t is integral PL up to sign and a value-group constant. Every real constant is real-PL: c=(c/log|α|)log|α| for any α∈M* with |α|≠1.\n\nOn a star centered at v, define H_e to be distance from v on the chosen arm e and zero on every other arm. Its slopes are 1 and 0; its intercepts belong to Γ_M because the center and endpoints have Γ_M coordinates. Thus it is piecewise (Z,Γ_M)-linear in GJR’s exact definition. Section 15.4 supplies a vertical Cartier divisor on an admissible formal model of the strict star domain with model function H_e∘τ_M. Sections 5.5–5.6 make this function strict integral PL. On the whole star,\nG∘τ_M=G(v)+Σ_e a_e(H_e∘τ_M),\nwhere a_e are its real outgoing slopes. Section 5.7 proves strict real-PL membership. No harmonicity or residue Picard-torsion condition is imposed on the basis functions. Their residue line bundles need not be trivial, so ordinary CLD smoothness is not asserted. Isolated vertices use the constant formula. All interval and star formulas agree on intersections because they are literally the same function G∘τ_M. This proves global strict membership on Y_M. The already proved subharmonicity then gives semipositivity on W_M by the classical/real-PL comparison.\n\nThe interpolation need not be Galois invariant. Average it:\nĝ_M=[M:K]^{-1}Σ_{σ∈Gal(M/K)}g_M^0∘σ.\nIsometric semilinear automorphisms preserve strict domains, analytic units and subharmonicity. Finite positive real sums preserve subharmonicity and strict real-PL membership, using common refinements of strict G-covers. Since f_M is invariant, f_M≤ĝ_M≤f_M+ε.\n\nThis average has an actual continuous descent g on Y. Over y∈Y, the finite algebra H(y)⊗_K M is a product of finite field extensions. Normality of M/K makes the Galois action transitive on its factors, viewed through embeddings into an algebraic closure of H(y). Each factor has the unique absolute value extending that of the complete field H(y). The action is therefore transitive on the analytic fibre. The finite surjective map Y_M→Y is a closed quotient of compact Hausdorff spaces, so an invariant continuous function descends uniquely.\n\nApply GJR Corollary 5.12 to good strict Y, coefficient group R, and the finite complete algebraic extension M/K. It descends the proved strict M-real-PL membership to strict K-real-PL membership. Its finite case is Proposition 5.11: the projection is finite flat surjective, since on affinoid algebras tensoring with finite-dimensional M is free of rank [M:K]. This is strict descent across ground fields, not all-domain sheafification.\n\nClassical curve scalar compatibility, GR Proposition 3.5(7), descends subharmonicity to W. Here W_M=Y_M\\∂_M Y_M: both Y_M→Y and M(M)→M(K) are finite and boundaryless, and Berkovich’s good composition equality identifies the interiors first over K and then over M. GR Theorem 4.3 now proves semipositivity of g on W. Surjectivity passes the inequalities to Y. This proves the one-sided approximation lemma.\n\nCountable extraction lemma. On a second-countable space Z, let h be upper semicontinuous and let f_i be a decreasing directed family of finite continuous functions with h=inf_i f_i. For every rational a, the open set {h<a} is the union of the open sets {f_i<a}. An open subspace of a second-countable space is Lindelof. Choose a countable subcover for each a and enumerate the union of the selected indices. Successive upper bounds in the directed set retain all previous choices and give a decreasing sequence. If h(z)<a, a selected index, and hence every sufficiently late chosen upper bound, has f_i(z)<a. All rational a>h(z) give infimum h(z); if h(z)=−∞, use all rational a. The reverse inequality follows from f_i≥h. No continuity or finite-valued hypothesis on h is used.\n\nA countable dense subset of K supplies second countability for algebraic analytifications of finite type. A strict affinoid algebra has a countable norm-dense subset, obtained from polynomials over a countable dense subfield in a Tate presentation. Evaluation on that subset separates bounded multiplicative seminorms and induces the full topology, because | |a(x)|−|b(x)| |≤||a−b|| in the quotient Banach norm. Hence its compact spectrum embeds homeomorphically into R_{\u0000≥0}^N and is metrizable and second countable. More precisely the product here is indexed by the natural numbers, not a finite N. An affine algebraic chart, embedded in affine space, has an exhaustion by strict affinoid intersections with polydiscs of radii R^m, with R∈|K*| and R>1. The ordinary opens where the coordinate norms are strictly smaller than R^m cover the chart and are second countable subspaces of these affinoids. A finite affine covering gives a countable ordinary open covering and a countable base for the whole analytification. Ordinary open subspaces inherit it.\n\nProof of theorem A. Work in the connected component of b. If h≡−∞ there, q_n=−n gives the result; constants are strict real-PL and harmonic. Otherwise GR 3.4.1 identifies h with Thuillier subharmonicity. A connected smooth curve is irreducible, and GR 3.5(9) makes h finite at all non-rig-points. Choose a connected compact strictly affinoid neighbourhood Y of b with b in its ordinary interior. Goodness and strictness supply it; an affinoid connected component can be selected by idempotents. Its boundary is the finite Shilov boundary of non-rig-points, where h is finite. Because C has no boundary, W=Y\\∂_K Y is precisely the ordinary interior of Y in C, by Berkovich 1.5.5. It is one relatively compact ordinary open neighbourhood of b.\n\nUse Thuillier Theorem 3.4.2 on this particular Y. Its proof supplies finite continuous f_S∈A^0(Y), indexed by finite S⊂I(Y) containing ∂Y, with f_S=h on S, harmonic off S, subharmonic on W, decreasing under inclusions of S, and inf_S f_S=h on W. The source’s determination lemma 3.4.1 handles rigid and type-IV values in this infimum assertion; no continuity of h is inserted. The extraction lemma gives f_n decreasing to h on W. Upper bounds here are finite unions of S, so the chosen functions remain finite continuous lisse functions on all of Y and decrease there too.\n\nApply the one-sided approximation lemma to f_n with ε_n=2^{-n}, always on the same Y and W. Obtain f_n≤g_n≤f_n+2^{-n}. Set q_n=g_n+2^{-n}. The shift is a strict real-PL harmonic constant. Each q_n is finite, strict real-PL and semipositive on W, and\nq_{n+1}≤f_{n+1}+2^{-n}≤f_n+2^{-n}≤g_n+2^{-n}=q_n.\nMoreover h≤q_n and 0≤q_n−f_n≤2^{1−n}. Thus q_n decreases pointwise to h, also when h is −∞. Extensions and models may vary with n, but every descended function has domain Y and every semipositive approximant has the same ordinary domain W.\n\nFor a finite continuous target, the increasing opens {q_n−h<η} cover any compact subset of W. Compactness supplies one index covering it, proving uniform convergence there. For any analytic K'/K, GJR 5.4 and 7.6 preserve strict membership and semipositivity of q_n∘π, and evaluation at each point gives q_n∘π↓h∘π. This pulls back an existing sequence; no extraction for arbitrary new functions over nonmetrizable extension spaces is claimed.\n\nThe complete argument is retained in P02.1-argument.md and embedded in standalone P02.1-paper.tex. Source extracts and application checks are in source-extracts/source-provenance.json. Rerun source retention with python retain_sources.py and diagnostics plus two TeX passes with python rerun.py. No unpublished book assertion is a premise. The next note uses this curve result for a higher-dimensional sector; this note does not solve original P02.1.\n\nArtifacts: /workspace/research/campaigns/round-41/P02.1-public-source-decreasing-real-PL/artifacts/codex-RyjJ79",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Draft higher-dimensional sector: every arbitrary classical psh on a full projective bundle over a second-countable smooth curve descends along compact projective fibres and has local decreasing strict semipositive real-PL pullbacks. The proof requires saturated domains.",
    "detailedSummary": "For complete nontrivially valued K with a countable dense subset, a smooth connected separated algebraic curve C0, an ordinary open Omega⊂C0^an, and an algebraic bundle E of rank r+1≥2, every classical psh u on X=P(E)^an restricted to Omega equals h∘p. Scalar pullback and the published local maximum principle prove constancy on compact connected boundaryless projective H(b)-fibres. Trivialization sections prove classical psh descent and exact overlap agreement. Note n1 supplies one fixed W and q_n, and v_n=q_n∘p is globally strict real-PL and semipositive on p^-1(W), decreasing pointwise to u. Every analytic scalar extension preserves the same sequence, even without metrizability of the extension space. These are smooth normal unibranch spaces of dimension r+1, including proper projective factors. No conclusion for every arbitrary psh germ on nonsaturated fibre charts, or for arbitrary normal/unibranch spaces, follows.",
    "text": "Draft theorem B. Let K be complete and nontrivially valued, with a countable dense subset. Let C0 be a smooth connected separated algebraic curve of finite type over K, Ω⊂C0^an an ordinary open subset, and E an algebraic vector bundle of rank r+1≥2. Let p:X=P(E)^an|_Ω→Ω. For every arbitrary classical psh u:X→R∪{−∞} and every x∈X there is one fixed ordinary open neighbourhood V=p^{-1}(W) and finite semipositive strict real-PL v_n on V decreasing pointwise to u. The construction is v_n=q_n∘p, using n1. The hypothesis on K can be replaced by second countability of the relevant base curve. No continuity, invariance, finiteness, residue-genus or residue-Picard-torsion restriction is placed on u. The product Ω×(P_K^r)^an is included.\n\nCompact constancy lemma. A classical psh function w on a connected compact boundaryless analytic space F is constant, allowing −∞. If not identically −∞, upper semicontinuity and compactness give a finite attained maximum m: local finite upper bounds have a finite subcover, and compactness gives attainment. The set {w=m} is nonempty and closed. It is open by Gubler–Rabinoff arXiv:2506.13548v2, Theorem 6.1, since every point of F is an interior point. Connectedness makes it all of F. This applies to the full classical curve-test class.\n\nFor every complete nontrivially valued H, (P_H^r)^an is compact, connected and boundaryless. Its finite standard closed unit-polydisc covering proves compactness. It is good, strict and boundaryless as an algebraic analytification, as recalled on GJR page 8. Each polydisc is connected, and any two standard charts meet at the homogeneous point with all coordinates 1.\n\nHere is a direct polydisc connectedness proof. For a point z of the closed unit polydisc, use its coordinate values z_i in H(z). Evaluate a polynomial P(z_1+U_1,…,z_r+U_r) with the Gauss norm of polyradius s∈[0,1]. This is a multiplicative seminorm bounded by the unit-polydisc norm. At s=0 it is z. At s=1 it is the unit Gauss point, because translation by coordinates of norm at most 1, and its inverse, preserve the unit Gauss norm. For each polynomial its value is a maximum of finitely many continuous expressions in s; norm density extends continuity to the Tate algebra. Every point has a path to the Gauss point. This works over H=H(b) without a countability assumption on that fibre field.\n\nFor b∈Ω, extend scalars to H(b), then include the analytic fibre p^{-1}(b)≅(P_{H(b)}^r)^an into X_{H(b)}. This uses the H(b)-point of Ω_{H(b)} over b. GR Proposition 4.2 makes the scalar pullback and its restriction classical psh. The compact constancy lemma therefore proves that u is constant on the entire fibre, including non-rigid points. Define h(b) to be this value. Then u=h∘p.\n\nOn an ordinary open base set U where the projective bundle trivializes, choose its analytic section s_U given by [1:0:…:0]. We have h|_U=u∘s_U, so h is upper semicontinuous and classical psh there by GR Proposition 4.2. Sections from different trivializations have the same u-value over every point, by fibre constancy. They agree exactly on overlaps. Classical psh sheafiness proves that h is classical psh on Ω, retaining its possible discontinuities and −∞ values. No quotient-topology assumption for this descent is needed because there are local sections.\n\nThe field hypothesis makes Ω second countable by the affinoid/algebraic argument in n1. Apply n1 to h at b=p(x), obtaining one W and one q_n. Let V=p^{-1}(W) and v_n=q_n∘p. This is an ordinary open neighbourhood of x. GJR Lemma 5.4(1) proves actual strict real-PL membership; Proposition 7.6(1) proves semipositivity. These results require good strict spaces but do not require p to be finite. Pointwise evaluation gives v_{n+1}(y)≤v_n(y) and lim_n v_n(y)=h(p(y))=u(y). The functions are defined globally on all of V. Every projective trivialization sees the same q_n∘p, so all chart overlaps agree term by term. There are no separately selected chart approximants requiring a gluing argument. If h is finite continuous, a compact subset of V has compact image in W, and the locally uniform conclusion of n1 pulls back.\n\nThese are genuine higher-dimensional normal unibranch examples. P(E) is smooth over K and has dimension r+1. Berkovich PMIHES 78 (1993), Corollary 2.2.7, printed pages 42–43, passes regularity and normality to the algebraic analytification and hence its ordinary open subspace X. Regular local rings are normal domains; a normal local ring is unibranch because its normalization is itself. No normalization descent occurs in this proof. Nontrivial projective-bundle transition functions are permitted. For example A_K^{1,an}×(P_K^r)^an has the result for all its globally defined classical psh functions, including pullbacks of log|t−a| with value −∞ at their poles. No torus invariance hypothesis is imposed.\n\nScalar compatibility. For any analytic extension K'/K, let π:V_{K'}→V be the projection. GJR 5.4(2) and 7.6(2) make v_n∘π strict real-PL and semipositive over K'. At each y', v_n(π(y')) decreases to u(π(y')). GR Proposition 4.2(5) also verifies that the target pullback remains classical psh. These formulas commute with p_{K'} and all projective coordinate transitions. Finite separable fields used in n1 only construct descended functions; they do not replace the assertion about every analytic extension by one about algebraic extensions. The extension space may be nonmetrizable. We pull back an existing sequence and do not claim countable extraction for arbitrary new starting functions over K'.\n\nThe overlap conclusion is local in the precise requested sense. A construction at one point supplies one sequence globally on W and one globally on p^{-1}(W), with exact compatibility throughout its charts. Independently constructed sequences near different base points need not agree on their common base open set. No global sequence on an arbitrary union of such neighbourhoods is asserted.\n\nThe domain must contain whole projective fibres. A psh function defined only on a nonsaturated ordinary open chart need not descend. Thus this is an unrestricted starting-function sufficient sector on the displayed X, not a characterization of every arbitrary higher-dimensional psh germ. The complete proof and remaining obligations are retained in P02.1-argument.md, with standalone embedding P02.1-paper.tex. Rerun python retain_sources.py and python rerun.py in the workspace.\n\nArtifacts: /workspace/research/campaigns/round-41/P02.1-public-source-decreasing-real-PL/artifacts/codex-RyjJ79",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Original P02.1 remains open here. Necessary F_sigma sublevels and analytic-retraction tests are proved; strict real maxima and nonsaturated or boundary shortcuts can fail. No sharp analytic regularization counterexample is supplied. Required artifacts and successful two-pass builds are retained.",
    "detailedSummary": "A decreasing sequence of finite continuous approximants forces every strict sublevel set to be F_sigma. Pullback through an analytic section gives a necessary retraction test. GJR Example 5.3 is a strict-membership counterexample at an irrational tropical corner, not a counterexample to regularization. A varying log|z1| on an affine projective-fibre chart defeats fibre constancy on nonsaturated domains; a closed disc defeats compact constancy if its actual boundary is retained. General higher-dimensional germs, sharp necessity/failure, singular normalization descent and unrestricted non-second-countable extraction remain unresolved. Seven supplied source hash pairs and 57 literal pages were checked; eight finite rational graph diagnostics passed. Both final TeX passes returned 0, each with one underfull hbox diagnostic and no label warning. These observations do not certify mathematics; candidate is false.",
    "text": "The results of n1 and n2 do not provide the original characterization. The following necessity statements and limitations distinguish proved facts from shortcut failures.\n\nSequence obstruction. If u=inf_n v_n on an ordinary neighbourhood V, with all v_n finite continuous, then for every real a,\n{u<a}=⋃_{n,k≥1}{v_n≤a−1/k}.\nIf u(x)<a, some v_n(x)<a and then some k supplies the displayed closed-set inequality; the converse is immediate. Every set on the right is closed in V. Thus strict sublevel sets must be F_sigma. Strict real-PL functions are continuous, so this is necessary for the requested sequence. On a nonmetrizable space, upper semicontinuity alone does not supply it. No classical psh function violating this condition is constructed here; it is not claimed to be a sharp analytic failure criterion. The Lindelof extraction of n1 is sufficient, and does not prove countable dense fields necessary.\n\nRetraction necessity. Suppose analytic maps s:B→X and p:X→B satisfy p∘s=id. If every h∘p has local decreasing semipositive strict real-PL regularization near s(b), pull its approximants back by s on the ordinary open s^{-1}(V). GJR 5.4 and 7.6 prove strict membership and semipositivity; pointwise evaluation proves the same decreasing limit h. Therefore the base curve remains a genuine necessary test for a projective bundle with sections. This is a functorial necessity statement, not a classification of all good strict spaces.\n\nStrict-max membership counterexample. GJR Example 5.3, PDF page 31, uses additive value group Q and the rank-one torus. The two functions π log|T|+1 and 0 are strict real-PL, while their maximum has tropical potential max{−πt+1,0} and corner t=1/π∉Q. Strict affinoid tropical intervals have rational vertices, and the published example concludes that this maximum is not strict real-PL. It is classical psh by the classical max/cone property, since log|T| is pluriharmonic. This refutes closure under arbitrary real maxima and the all-domain-lisse identification. It does not show failure of decreasing strict real-PL regularization: the mesh repair in n1 deliberately avoids that inference.\n\nSaturation and actual boundaries. On an affine coordinate chart in a projective fibre, log|z_1| is classical psh and varies along that fibre. The chart omits the hyperplane at infinity, so its fibre portion is not compact. Compact fibre constancy therefore cannot descend every arbitrary psh germ from such a chart. This is a counterexample to the descent shortcut, not to regularization. A compact closed disc also has nonconstant classical psh functions, for example max{log|T|,log|a|} with 0<|a|<1. Here the maximum is legal integral PL on the two strict domains cut at |T|=|a|. Its maximum occurs at the actual relative boundary. A boundaryless maximum principle cannot be applied there.\n\nNormalization limitations. The smooth normal unibranch examples in n2 require no normalization. Their existence does not prove normality or unibranchness sufficient for arbitrary higher-dimensional germs. Singular-curve normalization is finite but need not be flat; GJR Proposition 5.11 cannot simply descend strict PL approximants through it. A topological homeomorphism of a normalization likewise does not establish strict membership downstairs. Identifying values of independently chosen branch approximants does not prove monotonicity on one ordinary neighbourhood. No general singular-curve or higher-dimensional normalization criterion is established.\n\nResidue and genus range. The strict star construction of n1 uses integral model functions and real coefficients, not ordinary local logarithmic harmonicity. Positive-genus residue components and nontorsion residue Picard classes are allowed. GJR Remark 15.10 explains that harmonic functions need not be ordinary CLD smooth. Wanner’s cached arXiv:1801.04713v3, Corollary 5.4, page 31, assumes a smooth proper curve and finite continuous starting functions, with residue field algebraic over a finite field or the projective-line/Mumford alternatives for its decreasing ordinary CLD-smooth conclusion. These are comparison facts only. They are not used to add false restrictions to strict real-PL regularization, or to claim ordinary smoothness. No locally Fubini–Study, weakly smooth or CLD-smooth conclusion is made for the present atom.\n\nRemaining original obligations. A sharp characterization for the full arbitrary classical psh germ class in dimension at least two remains unresolved. So do constructions for arbitrary germs in ordinary affine opens of smooth normal unibranch spaces; sharp necessity and genuine failure examples for the regularization property; general normalization descent; unrestricted extraction when second countability is unavailable; curve boundary cases outside the proved range; and general tropical-chart overlap gluing outside the globally pulled-back bundle sector. Neither the F_sigma test nor the shortcut counterexamples establish the sharp failure range. Original P02.1 therefore remains open in this draft, and candidate=false.\n\nDeliverables. The entire proof and these remaining obligations are in P02.1-argument.md. P02.1-paper.tex is standalone and embeds the argument; build/P02.1-paper.pdf has 11 pages. input.json and input-original.json are byte-identical. assignment-original.txt preserves the exact assignment string, and task-original.json preserves the task object. status.json has exactly the keys id, status, exact_result, proof_file, concrete_gaps, with status partial. Canonical draft notes are also retained in final-notes.json.\n\nSource evidence. All seven supplied PDF/text SHA-256 pairs matched. source-extracts/source-provenance.json records the hashes, 57 byte-preserved literal cache pages, selected primary PDF pages, rendered OCR checks and eleven explicit application checks. The primary PDFs resolved the divisible-hull versus actual-value-group distinction in GJR 15.3–15.4, the all-domain versus strict site distinction, Thuillier’s finite separable compact-domain model statement, and the fact that the published regularization is a decreasing family. The target typo in the statement of Thuillier 3.2.10 was checked against the displayed operator and its unambiguous graph-to-measure formula. Berkovich’s good composition equality was checked on the actual PDF, printed page 35. No unpublished book assertion, earlier campaign note or blocked payload is used.\n\nExecution evidence. The input SHA-256 is b762e362cba2b898b66d57ae5ad05e6154dc89ce74227a782be84f452832084a. The exact-rational program graph_diagnostic.py checks eight specified finite weighted stars, with weights [1,2,2], initial slopes [−3/2,1/2,1/4], corners [1/3,2/5,3/7] and positive slope jumps [7/3,4/5,9/7]. The initial central weighted mass is zero. It exhausts the finite piecewise-affine breakpoint unions to check one-sided chord error, nonnegative weighted masses and the shifted interstage inequality. All eight examples passed. At n=1 there are 64 segments per arm, maximum chord error 7/864 and minimum new weighted mass zero. At n=8 there are 8192 segments per arm, maximum error 7/110592, minimum new mass zero and maximum shifted interstage increase −1/128. These are exact exhaustive results only for the specified finite examples, not for analytic curves or sheaf membership. Output is retained in diagnostics/graph-output.json.\n\nBoth final pdfLaTeX passes returned exit code 0 and produced the 11-page, 322243-byte PDF. Each recorded one Underfull hbox diagnostic, badness 2351, at generated TeX lines 706–717. Neither final pass had a label warning. Initial-build records, including its resolved first-pass label warning, are retained in diagnostics/initial-build. Commands, logs, hashes, versions and actual diagnostics are in diagnostics/build-diagnostics.json; artifact checks are in diagnostics/artifact-checks.json. Existing Python 3.12.14, Pandoc 3.1.11.1, pdfTeX 3.141592653-2.6-1.40.26 and TeX Live 2025/dev/Debian were used. No installation, external worker/model, network operation or resource-heavy computation was performed. The requested native-model configuration is recorded but is not independently attested by local tools.\n\nRerun in the workspace with: python retain_input.py; python retain_sources.py; python rerun.py; python verify_artifacts.py; python assemble_notes.py. The scripts preserve inputs, regenerate source extracts, run the finite diagnostics, regenerate standalone TeX and compile it twice without installing software. Successful hashes, finite arithmetic, artifact checks and TeX compilation are provenance and execution observations, not mathematical correctness certificates.\n\nArtifacts: /workspace/research/campaigns/round-41/P02.1-public-source-decreasing-real-PL/artifacts/codex-RyjJ79",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Published source versions and application checks

{
  "scope": "Only user-listed public source caches; no unpublished book premise.",
  "sources": [
    {
      "id": "GR-2506.13548v2-20261004",
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "source_pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "source_literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "supplied_hashes_match": true,
      "pdf_page_count": 40,
      "selected_pdf_pages": [
        5,
        6,
        7,
        10,
        11,
        18,
        19,
        21,
        22,
        23,
        30,
        31
      ],
      "literal_page_files": [
        {
          "original_pdf_page": 5,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-5-literal.txt",
          "literal_sha256": "a49950e390200fe38a131519342b7421e570c5977ca58f107ab718b452868d1d"
        },
        {
          "original_pdf_page": 6,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-6-literal.txt",
          "literal_sha256": "16a443967381a0825f00925dba32d8b6d7a5773574dc3f2219a669e9489db614"
        },
        {
          "original_pdf_page": 7,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-7-literal.txt",
          "literal_sha256": "34ccebb67789241783588937145ab4bd19b3f2fad5732f3d4a3fc36c5e24fcae"
        },
        {
          "original_pdf_page": 10,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-10-literal.txt",
          "literal_sha256": "1c941ec581ff4e1712be17af6da299996380868b7b1cc5c94ca3f4456614cc76"
        },
        {
          "original_pdf_page": 11,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-11-literal.txt",
          "literal_sha256": "a8a605a63d505d7de520e3592c747f99cfe520c5c7f069465c45bd3ca8bf6892"
        },
        {
          "original_pdf_page": 18,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-18-literal.txt",
          "literal_sha256": "76fc8a1ea9f4433b8caeb28cde4e1dd45ebe167fbb1b6864f39f5f4d5dc811f9"
        },
        {
          "original_pdf_page": 19,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-19-literal.txt",
          "literal_sha256": "97b5dfd831e09ddc0c5525f2ad45dfbdd9a3d42a7efdf3cc24ad84f5909d1d78"
        },
        {
          "original_pdf_page": 21,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-21-literal.txt",
          "literal_sha256": "820cce17e7bafe3746e0e59150d0a98cb7a070832a4f6731ff2109942b63a9a7"
        },
        {
          "original_pdf_page": 22,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-22-literal.txt",
          "literal_sha256": "12de51b8102a4ea09f23a92407e01734b60aecf4dc65d919edfccf63d7bee3fd"
        },
        {
          "original_pdf_page": 23,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-23-literal.txt",
          "literal_sha256": "d9424c12897c66bf794c303dd5f6a6362dcf63e991e459618c9207f8cd53e682"
        },
        {
          "original_pdf_page": 30,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-30-literal.txt",
          "literal_sha256": "4fcca2835bab85572ea9eb5bc15b88bd27ced898c7387e6e89d02b60ecdc131d"
        },
        {
          "original_pdf_page": 31,
          "literal_file": "GR-2506.13548v2-20261004-pdf-page-31-literal.txt",
          "literal_sha256": "c9a339caa6767c72b0f5588c8c754e5d58ce99743b518ee878e58c675f8e1770"
        }
      ],
      "role": "checked foundation"
    },
    {
      "id": "GR-2503.05513-20261004",
      "public_source": "https://arxiv.org/pdf/2503.05513",
      "source_pdf": "/workspace/research/shared-sources/GR-2503.05513-20261004.pdf",
      "source_literal_extract": "/workspace/research/shared-sources/GR-2503.05513-20261004.txt",
      "pdf_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "extract_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "supplied_hashes_match": true,
      "pdf_page_count": 26,
      "selected_pdf_pages": [
        15,
        16,
        17
      ],
      "literal_page_files": [
        {
          "original_pdf_page": 15,
          "literal_file": "GR-2503.05513-20261004-pdf-page-15-literal.txt",
          "literal_sha256": "cb2193be1cd71d0f6b7df6eaeded923f8fc8578b1aee8fc765c7cc3e83fe481e"
        },
        {
          "original_pdf_page": 16,
          "literal_file": "GR-2503.05513-20261004-pdf-page-16-literal.txt",
          "literal_sha256": "d6ea98f6e7709a86b1cdc679db40d2efbeaa4529dc3e84f8ef366684278cc371"
        },
        {
          "original_pdf_page": 17,
          "literal_file": "GR-2503.05513-20261004-pdf-page-17-literal.txt",
          "literal_sha256": "350e1328a92ac311b8534d6d2bf553a27068a222b780164aa10e733cebec94e4"
        }
      ],
      "role": "checked foundation"
    },
    {
      "id": "Thuillier-tel-00010990v1",
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "source_pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
      "source_literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "supplied_hashes_match": true,
      "pdf_page_count": 198,
      "selected_pdf_pages": [
        19,
        20,
        21,
        33,
        34,
        56,
        57,
        67,
        68,
        82,
        83,
        84,
        87,
        88,
        89,
        103,
        104,
        105
      ],
      "literal_page_files": [
        {
          "original_pdf_page": 19,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-19-literal.txt",
          "literal_sha256": "aebb2611830270672c86a69ec643531b306c4e4d5b495163fcd4cac0b685d6a0"
        },
        {
          "original_pdf_page": 20,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-20-literal.txt",
          "literal_sha256": "289b1b2e59ad23ff4b9875bcc381d713588b3b8706c4341827ed272ff46d682d"
        },
        {
          "original_pdf_page": 21,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-21-literal.txt",
          "literal_sha256": "88154d8f2b221ce3ed231444d28e5d283a93a32179bb5b711a01ce597d9e218a"
        },
        {
          "original_pdf_page": 33,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-33-literal.txt",
          "literal_sha256": "71f139e10ca0e74b6a063cff5da84fcc96f82a78685c1ed0bdd0ab386a459527"
        },
        {
          "original_pdf_page": 34,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-34-literal.txt",
          "literal_sha256": "2d187319ff619e8e4fb0cfef8d9319361a1ec7242a10d0a019c3186c82eb9c4f"
        },
        {
          "original_pdf_page": 56,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-56-literal.txt",
          "literal_sha256": "0a9c898955b7442d31c6f407e0753e35f3489396091aec0e6c8db669bc8d4398"
        },
        {
          "original_pdf_page": 57,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-57-literal.txt",
          "literal_sha256": "d75fed2a878784495a3d3fa7cb8e80a3f90dc71860cc88bed3d1ccf7c0543523"
        },
        {
          "original_pdf_page": 67,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-67-literal.txt",
          "literal_sha256": "a3448a8d43697e9dfe073253b39dd0fb86f83c85fe8c38b603a6c8a5fb0487f9"
        },
        {
          "original_pdf_page": 68,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-68-literal.txt",
          "literal_sha256": "e5512c6e28d55e48544a173aa473847563450819ee9234fc058844f154e21daf"
        },
        {
          "original_pdf_page": 82,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-82-literal.txt",
          "literal_sha256": "82559198be47c9e4ad4ebcfadf41e7b0a553cbf084bff6ac37e4a73ee5c44e59"
        },
        {
          "original_pdf_page": 83,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-83-literal.txt",
          "literal_sha256": "32ebe19759bbd036e23d9f89ca035132dde4241a34d71b049bb6311a99581d6c"
        },
        {
          "original_pdf_page": 84,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-84-literal.txt",
          "literal_sha256": "a3f76efe15a703eccbcfbbd259a4c7b8bd887eaec26bb9e45b22376b0133006a"
        },
        {
          "original_pdf_page": 87,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-87-literal.txt",
          "literal_sha256": "05d871769dd9c679ddc109331fa99ffb15b793aa5c3d7892e8d59decf3961e00"
        },
        {
          "original_pdf_page": 88,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-88-literal.txt",
          "literal_sha256": "9742d760c7faa37db072e0e6df2518d581d19f120ebee96d37cf07bcdfea9698"
        },
        {
          "original_pdf_page": 89,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-89-literal.txt",
          "literal_sha256": "5acac5b51df4c7fe43a6a5f356bf2e32f370fb134c1e7ab998c4dc8a0eebbdba"
        },
        {
          "original_pdf_page": 103,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-103-literal.txt",
          "literal_sha256": "86fef36c1bdf192a700801fd2c2958ee81281f4031206e6018f5e988e07c21fd"
        },
        {
          "original_pdf_page": 104,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-104-literal.txt",
          "literal_sha256": "691b77c4935e64bf395dd278a5d726df55eefda99ab02e3ba7a16fdc1e267756"
        },
        {
          "original_pdf_page": 105,
          "literal_file": "Thuillier-tel-00010990v1-pdf-page-105-literal.txt",
          "literal_sha256": "f7ba9960c4751bded0eab0d09c6bd74ce075168e3a43b5f48ae2e03d80fa3acc"
        }
      ],
      "role": "checked foundation"
    },
    {
      "id": "GJR-2111.05741",
      "public_source": "https://arxiv.org/pdf/2111.05741",
      "source_pdf": "/workspace/research/shared-sources/GJR-2111.05741.pdf",
      "source_literal_extract": "/workspace/research/shared-sources/GJR-2111.05741.txt",
      "pdf_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "extract_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "supplied_hashes_match": true,
      "pdf_page_count": 87,
      "selected_pdf_pages": [
        8,
        31,
        32,
        33,
        34,
        35,
        36,
        45,
        46,
        47,
        76,
        77,
        78,
        79,
        80,
        81
      ],
      "literal_page_files": [
        {
          "original_pdf_page": 8,
          "literal_file": "GJR-2111.05741-pdf-page-8-literal.txt",
          "literal_sha256": "be8691d6b8ad34745e22f29c5a31ab8594895fe10d133d1c9b3fb6edb51391ea"
        },
        {
          "original_pdf_page": 31,
          "literal_file": "GJR-2111.05741-pdf-page-31-literal.txt",
          "literal_sha256": "0286959703f57c016523108761fe657f3f32a4a8d05746c3159f5a0b7226ba5d"
        },
        {
          "original_pdf_page": 32,
          "literal_file": "GJR-2111.05741-pdf-page-32-literal.txt",
          "literal_sha256": "560ad364713d4d28899e2c082aed5be081bf83ac79de2856ac3d50b03fcf5d3b"
        },
        {
          "original_pdf_page": 33,
          "literal_file": "GJR-2111.05741-pdf-page-33-literal.txt",
          "literal_sha256": "0e92128758dc6159d301e8651b31c7724b9f0642d9a2e6632498d0f4415c601a"
        },
        {
          "original_pdf_page": 34,
          "literal_file": "GJR-2111.05741-pdf-page-34-literal.txt",
          "literal_sha256": "816aa1351cbe07be7b95fb87c7983a332f5c20cb53f0dd0b2541cf62b4f7cb7a"
        },
        {
          "original_pdf_page": 35,
          "literal_file": "GJR-2111.05741-pdf-page-35-literal.txt",
          "literal_sha256": "a2a103d6505253640eaa4ed1d88ed910c8240b1f6b47db721b545601e4d0fd2c"
        },
        {
          "original_pdf_page": 36,
          "literal_file": "GJR-2111.05741-pdf-page-36-literal.txt",
          "literal_sha256": "fa222cc9320e502ea28a3769382dc27d02062ffed43e756bf089cc621de7156e"
        },
        {
          "original_pdf_page": 45,
          "literal_file": "GJR-2111.05741-pdf-page-45-literal.txt",
          "literal_sha256": "62690d857bfa11e6dec160c1f908787b9910b171e8aa94e4f3c6282ef51a4702"
        },
        {
          "original_pdf_page": 46,
          "literal_file": "GJR-2111.05741-pdf-page-46-literal.txt",
          "literal_sha256": "23d00fd808ff70a1c1a87294a4cc947979768b62e6dab7165d01be4d4abf54c5"
        },
        {
          "original_pdf_page": 47,
          "literal_file": "GJR-2111.05741-pdf-page-47-literal.txt",
          "literal_sha256": "8c43decece427ba4bcd4a0f891306acf4bafd1d3be07e3c5fc6ead61b1380a73"
        },
        {
          "original_pdf_page": 76,
          "literal_file": "GJR-2111.05741-pdf-page-76-literal.txt",
          "literal_sha256": "3facbf65e2796d8327b4ba0116978c80bba7cc8409aa6532caee5c5ca9f8026d"
        },
        {
          "original_pdf_page": 77,
          "literal_file": "GJR-2111.05741-pdf-page-77-literal.txt",
          "literal_sha256": "923061c5e8fc59e1e861c53434793ea9b5cd742aa0a465e373093d81c4934593"
        },
        {
          "original_pdf_page": 78,
          "literal_file": "GJR-2111.05741-pdf-page-78-literal.txt",
          "literal_sha256": "585f759202bd2bf5d2f0da9b799c4bf42281ed8fdde816969e7230ca9bfa31f8"
        },
        {
          "original_pdf_page": 79,
          "literal_file": "GJR-2111.05741-pdf-page-79-literal.txt",
          "literal_sha256": "9a5892b5445ccdb4969fc287d2fd351953a2fed518169f969826bb7b38de1fe2"
        },
        {
          "original_pdf_page": 80,
          "literal_file": "GJR-2111.05741-pdf-page-80-literal.txt",
          "literal_sha256": "57ced0d50b7ed907aceb830a0845ffd65d94591551d18127c21504f5e7fc67b1"
        },
        {
          "original_pdf_page": 81,
          "literal_file": "GJR-2111.05741-pdf-page-81-literal.txt",
          "literal_sha256": "4c69527beea088270b0bc870bdd68f6cc84a0cf3e1df33eb23c0bc61fdbd8de2"
        }
      ],
      "role": "checked foundation"
    },
    {
      "id": "Berkovich-PMIHES-1993-78-5",
      "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "source_pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
      "source_literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
      "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "supplied_hashes_match": true,
      "pdf_page_count": 158,
      "selected_pdf_pages": [
        30,
        31,
        32,
        39,
        40
      ],
      "literal_page_files": [
        {
          "original_pdf_page": 30,
          "literal_file": "Berkovich-PMIHES-1993-78-5-pdf-page-30-literal.txt",
          "literal_sha256": "5aeb9abd888a25233ee6c39915a1baf48827f7bcb02c6d169f537688e63ef886"
        },
        {
          "original_pdf_page": 31,
          "literal_file": "Berkovich-PMIHES-1993-78-5-pdf-page-31-literal.txt",
          "literal_sha256": "c5c79951e775de3b50d11840fbfa75790d2702928c86a5ee835de3826af07fc8"
        },
        {
          "original_pdf_page": 32,
          "literal_file": "Berkovich-PMIHES-1993-78-5-pdf-page-32-literal.txt",
          "literal_sha256": "2ebe758bac68cc0ee86e162dd82a824fcfa9d11a87aac803ed076fbeb8c094f4"
        },
        {
          "original_pdf_page": 39,
          "literal_file": "Berkovich-PMIHES-1993-78-5-pdf-page-39-literal.txt",
          "literal_sha256": "8c9a6828cdee113742ac438df62798f2bef942e48d9ebb079416e11c1100605a"
        },
        {
          "original_pdf_page": 40,
          "literal_file": "Berkovich-PMIHES-1993-78-5-pdf-page-40-literal.txt",
          "literal_sha256": "6e94bd6442061f97dcddbc626d9c09701cdb6bb1e3c2b544efc61adca7fd50a1"
        }
      ],
      "role": "checked foundation"
    },
    {
      "id": "CD-1204.6277v2-20261004",
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "source_pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
      "source_literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
      "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "supplied_hashes_match": true,
      "pdf_page_count": 608,
      "selected_pdf_pages": [],
      "literal_page_files": [],
      "role": "unused hash-checked source"
    },
    {
      "id": "Wanner-1801.04713v3-20261004",
      "public_source": "https://arxiv.org/pdf/1801.04713v3",
      "source_pdf": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.pdf",
      "source_literal_extract": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "pdf_sha256": "8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7",
      "extract_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "supplied_hashes_match": true,
      "pdf_page_count": 32,
      "selected_pdf_pages": [
        2,
        3,
        31
      ],
      "literal_page_files": [
        {
          "original_pdf_page": 2,
          "literal_file": "Wanner-1801.04713v3-20261004-pdf-page-2-literal.txt",
          "literal_sha256": "99c57b5d81dbdac286ef56dcd7d78ac442cd051c4c2ab4f18b5f92327b98f2e8"
        },
        {
          "original_pdf_page": 3,
          "literal_file": "Wanner-1801.04713v3-20261004-pdf-page-3-literal.txt",
          "literal_sha256": "9d4a42a246eba298178b20847cfa3a659101e2bb5225ce60b29e7d91a7378957"
        },
        {
          "original_pdf_page": 31,
          "literal_file": "Wanner-1801.04713v3-20261004-pdf-page-31-literal.txt",
          "literal_sha256": "c36f02dcf2825a53610660c4425f71e7393198beb62f70e8451c9772b2086673"
        }
      ],
      "role": "comparison only"
    }
  ],
  "application_checks": [
    {
      "claim": "Starting class and non-rig finiteness",
      "source": "GR-2506.13548v2-20261004",
      "pages": [
        10,
        11,
        18,
        19,
        21,
        22
      ],
      "check": "Smooth separated pure-dimension-one strict curve; use 3.4.1 including identically -infinity, not a finite-continuous replacement class. Definition 4.1 quantifies over all analytic extensions."
    },
    {
      "claim": "A compact-domain lisse net, not a sequence",
      "source": "Thuillier-tel-00010990v1",
      "pages": [
        103,
        104
      ],
      "check": "Printed 89--90: finite S in I(Y) containing actual boundary; f_S continuous finite on Y, subharmonic on Y minus boundary. The new Lindelof extraction in the argument needs second countability."
    },
    {
      "claim": "Lisse skeletal representation only",
      "source": "Thuillier-tel-00010990v1",
      "pages": [
        82,
        83,
        84
      ],
      "check": "All-domain Definition 3.2.1 is not strict PL. Proposition 3.2.4 proof treats phi in A^0(Y), compact strict Y, and a finite separable extension. Original corners need not lie in the value group."
    },
    {
      "claim": "Skeletal scalar extension and graph positivity",
      "source": "Thuillier-tel-00010990v1",
      "pages": [
        19,
        20,
        21,
        56,
        57,
        87,
        88,
        89,
        104,
        105
      ],
      "check": "Weighted outgoing slopes; 2.2.21 weighted G-local skeletal isomorphism; 3.2.10 graph pullback formula on Y minus boundary; 3.4.4 positivity; new chord proof gives convexity/positive masses at all replacement vertices."
    },
    {
      "claim": "Actual strict approximant membership",
      "source": "GJR-2111.05741",
      "pages": [
        31,
        32,
        33,
        77,
        78,
        79,
        80
      ],
      "check": "All replacement mesh and star/interval cut coordinates are actual Gamma_M values after finite separable roots. 15.3--15.4 supply admissible formal models and integral star basis functions. 5.5--5.7 make their real linear combinations strict R-PL. A finite neighbourhood G-cover has identical formulas on overlaps."
    },
    {
      "claim": "Descent to original K",
      "source": "GJR-2111.05741",
      "pages": [
        34,
        35,
        36,
        46,
        47
      ],
      "check": "Average over finite Galois M/K; continuous quotient descent proved in the argument; projection finite free flat and surjective; 5.12 with divisible group R supplies strict membership across the ground fields; its finite case is explicitly 5.11. GR-classical 3.5(7) supplies subharmonicity descent."
    },
    {
      "claim": "Semipositivity after membership and all pullbacks",
      "source": "GR-2506.13548v2-20261004",
      "pages": [
        22,
        23
      ],
      "check": "Theorem 4.3 requires good strict space and nontrivial valuation; it is applied only after strict R-PL has been proved. GJR 5.4 and 7.6 give morphism/scalar preservation without requiring a finite bundle projection."
    },
    {
      "claim": "Compact projective fibre constancy for arbitrary u",
      "source": "GR-2506.13548v2-20261004",
      "pages": [
        5,
        6,
        7,
        21,
        22,
        30,
        31
      ],
      "check": "Scalar pullback to H(b), inclusion of projective fibre; finite usc maximum on compact boundaryless connected fibre and 6.1. This fails as an argument on nonsaturated fibre charts."
    },
    {
      "claim": "Ordinary neighbourhoods and normal geometry",
      "source": "Berkovich-PMIHES-1993-78-5",
      "pages": [
        30,
        31,
        32,
        39,
        40
      ],
      "check": "1.5.5 identifies domain interior with ordinary topological interior and handles finite scalar boundaries. 2.2.7 gives regularity/normality of algebraic analytifications. No normalization descent is assumed."
    },
    {
      "claim": "Cached numbering reconciliation",
      "source": "GR-2503.05513-20261004",
      "pages": [
        15,
        16,
        17
      ],
      "check": "June proof cites earlier 3.1 and 3.5; actual March cache has Proposition 5.1 and Corollary 5.4, with checked curve hypotheses."
    },
    {
      "claim": "Ordinary smoothness comparison only",
      "source": "Wanner-1801.04713v3-20261004",
      "pages": [
        3,
        31
      ],
      "check": "Corollary 5.4 finite continuous input, smooth proper curve, residue algebraic over finite field or projective line/Mumford. No ordinary smoothness conclusion is inferred from the new PL proof."
    }
  ],
  "primary_pdf_visual_checks": [
    {
      "source": "GJR-2111.05741",
      "pages": [
        77,
        78
      ],
      "resolved": "sqrt(Gamma) is the divisible hull; actual Gamma vertices suffice for admissible subdivisions. 15.4 uses integral slopes and Gamma intercepts, not arbitrary real affine coefficients."
    },
    {
      "source": "Thuillier-tel-00010990v1",
      "pages": [
        34,
        83,
        103,
        104
      ],
      "resolved": "X_G is all-domain; X_R is strict. 3.2.4 says finite separable extension and its proof covers A^0(Y). 3.4.2 is a decreasing family, with compact-domain h_S, not a published sequence."
    },
    {
      "source": "Thuillier-tel-00010990v1",
      "pages": [
        56,
        87
      ],
      "resolved": "2.2.21 states weighted G-local skeletal compatibility. OCR target A^0_Y in 3.2.10 is also a printed typographical inconsistency: the operator displayed immediately above has target A^1_X and (ii) is explicitly in A^1_Y. Only the unambiguous graph-to-measure formula is used."
    },
    {
      "source": "Berkovich-PMIHES-1993-78-5",
      "pages": [
        32
      ],
      "resolved": "The good composition equality in 1.5.5(ii), printed page 35, is Int(Z/X)=Int(Z/Y) intersect psi^-1(Int(Y/X)). Only this equality is used for finite scalar-extension boundary identities; the preceding printed inclusion has inconsistent ambient sets and is not used."
    }
  ],
  "limits": "Literal excerpts and matching hashes are provenance evidence, not verification of the mathematical claims."
}

## GR-2506.13548v2-20261004 cache page 5

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                     5

2.3. Affinoid algebras. Consider the polynomial ring k[T1 , . . . , Tn ] over k. For a col-
lection
     P of weights r1 , . . . , rn ∈ R>0 , the weighted Gauss norm on k[T1 , . . . , Tn ] is given on
              λ
f = λ∈Nn aλ T by
                                                           λ
                                   ∥ f ∥ r = maxn |aλ |r1 1 · · · rnλn .
                                              λ∈N

We denote by k〈r1−1 T1 , . . . , rn−1 Tn 〉 the completion of k[T1 , . . . , Tn ] with respect to the
weighted Gauss norm. A k-affinoid algebra is a Banach algebra A over k isomorphic
as a k-algebra to k〈r1−1 T1 , . . . , rn−1 Tn 〉/I for some n ∈ N and for some (closed) ideal I
of k〈r1−1 T1 , . . . , rn−1 Tn 〉, such that the norm of A is equivalent to the residue norm on
k〈r1−1 T1 , . . . , rn−1 Tn 〉/I. If we can choose all ri = 1, then A is called a strictly k-affinoid
algebra.

2.4. Affinoid spaces. We denote by M (A ) the Berkovich spectrum of a k-affinoid alge-
bra A . It is the set of bounded multiplicative seminorms p on A with p(1) = 1. We
usually denote the points of X = M (A ) by x instead of p, and we write | f (x)| instead of
p( f ) for f ∈ A . We endow X with the topology generated by the functions (| f (·)|) f ∈A .
Then X is a compact space endowed with a canonical sheaf of rings OX , which we call
a k-affinoid space. If A is strictly k-affinoid, then M (A ) is called a strictly k-affinoid
space. See [Ber90] for details.
   The Shilov boundary of a k-affinoid space X = M (A ) is the unique minimal subset Γ
of X such that
                                    max | f (x)| = max | f (x)|
                                     x∈X                x∈Γ

for all f ∈ A . A k-affinoid space has a finite Shilov boundary by [Ber90, Corollary 2.4.5].
    The supremum seminorm | |sup on X = M (A ) is used to define the k◦ -algebra A ◦ :=
{ f ∈ A | | f |sup ≤ 1}, its ideal of topologically nilpotent elements A ◦◦ := { f ∈ A |
| f |sup < 1}, and the canonical reduction Af:= A ◦ /A ◦◦ .

2.5. Non-archimedean analytic spaces. The k-affinoid spaces form the building blocks
for k-analytic spaces. Roughly speaking, a k-analytic space X is given by an atlas of
compact charts formed by k-affinoid spaces. We refer to [Ber93, §1.2] for the precise
definition of the category of k-analytic spaces and properties. If we can use strictly k-
affinoid spaces for the charts of X , then we call X a strictly k-analytic space. A k-analytic
space X is called good if every x ∈ X has a k-affinoid neighborhood. These were the
spaces considered in [Ber90].

2.6. Balls and discs. We call Bn := M (k〈T1 , . . . , Tn 〉) the closed unit ball of dimension n.
The open unit ball is the open subset B+n of Bn given by

                         B+n := {x ∈ X | |T1 (x)| < 1, . . . , |Tn (x)| < 1}.

If n = 1, then we get the closed unit disc B1 and the open unit disc B1+ . The topology of
B1 can be described explicitly in terms of closed discs B1 (x, ρ) and open discs B1+ (x, ρ)
with center x and radius ρ, as explained in Appendix A.2.


## GR-2506.13548v2-20261004 cache page 6

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


## GR-2506.13548v2-20261004 cache page 7

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


## GR-2506.13548v2-20261004 cache page 10

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


## GR-2506.13548v2-20261004 cache page 11

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


## GR-2506.13548v2-20261004 cache page 18

18                                W. GUBLER AND J. RABINOFF

   At this point, one proves that u is subharmonic in Thuillier’s sense directly from Thuil-
lier’s definition, as in the proof of Proposition 3.5(7), this time using [Thu05, Proposi-
tion 2.3.19]. The converse is the difficult direction: see [Thu05, Proposition 3.1.14]. □
  We will need the following lemma in the proof of Proposition 3.5(9). (Note that
Lemma 3.11 itself follows from Proposition 3.5(9) as we have seen in 3.5.5.)
Lemma 3.11. Let X be a strictly k-analytic curve over a non-trivially valued field k and let
u: X → R ∪ {−∞} be a subharmonic function. If x ∈ ∂ X and u(x) = −∞, then u ≡ −∞
on a neighborhood of x.
                                                          −∞
Proof. If char(k) = p > 0 let k′ be the completion of k p , and otherwise let k′ = k. Let
X ′ = X k′ and π = πk′ /k : X ′ → X , let ι : X red
                                                ′
                                                     ,→ X ′ be the inclusion of the underlying
reduced space, and let ν: Xe ′ → X red
                                     ′
                                        be the normalization. Then π and ι are homeomor-
phisms preserving boundaries by Lemmas 3.7 and 3.8, and ν is a boundary-preserving
isomorphism in a neighborhood of the unique point x ′ ∈ Xe ′ lying over x by Lemma 3.9.
The composition u ◦ π ◦ ι ◦ ν is subharmonic, so we may replace X by Xe ′ to assume that
X is rig-smooth. After shrinking X , we may assume that X is strictly affinoid. By [Ber90,
Corollary 1.3.6], if K is the completion of an algebraic closure of k then X K → X is an
open map, and by Lemma 2.12 there is a point of ∂ X K lying over x, so we may extend
scalars to assume that k is algebraically closed.
   By the semistable reduction theorem [Thu05, Théorème 2.3.8], there exists a semistable
(formal) model X of X . Let red: X → Xs denote the reduction map, which is anti-
continuous. Let ξ ∈ Xs be any point. As explained in [BPR13, Theorem 4.6] (see also
[BL85, Propositions 2.2 and 2.3]), if ξ is a generic point then red−1 (ξ) is a single type-2
point of X ; if ξ is a smooth closed point then red−1 (ξ) is isomorphic to an open unit ball;
and if ξ is a node then red−1 (ξ) is isomorphic to an open annulus. In particular, if ξ is a
closed point then red−1 (ξ) is connected and open.
   By [CD12, Lemme 6.5.1], the closure of ζ = red(x) is not proper, so ζ is a generic
point of Xs . Let Y ⊂ Xs denote its closure. Then red−1 (Y ) is an open neighborhood of
x in X . Let ξ ∈ Y be a closed point and let U = red−1 (ξ). Then x is a limit point of U:
one can use [BPR13, Lemma 3.2], or one can see this using retraction to the skeleton
S(X) from [Thu05, Théorème 2.2.10]; in this case, x is a vertex of S(X), and either U
deformation retracts onto x if ξ is smooth, or U contains an edge of S(X) adjacent to
x when ξ is a node. It follows that red−1 (Y ) is contained in the union of {x} with all
connected components U of Int(X ) having x as a limit point. We will show that u ≡ −∞
on every such U.
   We adapt the proof of [Thu05, Lemme 3.1.9]. Suppose that u ̸≡ −∞ on some such
U. Then u|U is subharmonic in Thuillier’s sense as U is smooth and connected and u is
subharmonic in our sense. By [Thu05, Lemme 2.3.9], for every N ∈ Z≥0 , there exists a
unique harmonic function hN : X → R such that hN (x) = −N and
                                           u( y) if u( y) > −∞
                                         
                               hN ( y) =
                                           0        otherwise
for every y ∈ ∂ X \ {x}. By construction, we have u − hN ≤ 0 on ∂ X . By [Thu05,
Corollaire 3.1.12], if the function u − hN attains a local maximum at a point y ∈ U, then


## GR-2506.13548v2-20261004 cache page 19

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                       19

u − hN takes a constant value C on U. By semicontinuity, we have
                                                             
                   −∞ = u(x) − hN (x) ≥ lim sup u(z) − hN (z) = C,
                                                   z→x
                                                   z∈U

which is a contradiction. Thus u−hN does not attain a local maximum on U. It does attain
a maximum on the closure U, which is compact. We have U ⊂ U ∪ ∂ X and u − hN ≤ 0 on
∂ X , so u−hN ≤ 0 on U. Clearly −hN (x) → ∞ as N → ∞, so by [Thu05, Lemme 2.3.10],
we have −hN → ∞ on U. Since u ≤ hN on U for all N , it follows that u ≡ −∞ on U. □
Proof of Proposition 3.5(9). We replace X by Int(X )∪{x} to assume that ∂ X = ; or ∂ X =
{x}. Replacing X by the irreducible component of X containing x (see 3.5.5), we assume
in addition that X is irreducible. Let k′ = k r /k be an analytic extension field for some
r ∈ R>0 n
           as in 2.10 such that X k′ is strictly k′ -analytic. Note that X k′ is again irreducible:
any irreducible component of X k′ is defined over a finite, separable extension of k inside
k′ [Duc18, 1.5.6], but k is algebraically closed in k′ [Duc24, 3.2.11]. The fiber π−1         k′ /k
                                                                                                    (x)
has a unique Shilov boundary point x ′ = σ(x), so by Lemma 3.10, if ∂ X = {x} then
∂ X k′ = {x ′ }; of course, if ∂ X = ; then ∂ X k′ = ; as well. Replacing X by X k′ and x by
x ′ , we may assume that X is strictly k-analytic and irreducible over a non-trivially valued
field k, and that ∂ X = {x} or ∂ X = ;.
                                                             −∞
    If char(k) = p > 0 let k′ be the completion of k p , and otherwise let k′ = k. Let X ′ =
X k′ and let π = πk′ /k : X ′ → X , let ι : X red
                                              ′
                                                  ,→ X ′ be the inclusion of the underlying reduced
space, and let ν: Xe ′ → X red′
                                 be the normalization. Since π and ν are homeomorphisms,
the space X red is again irreducible, so Xe ′ is connected by [Duc09, Proposition 5.16]. Since
              ′

x is not a rig-point of X , there exists a unique point x ′ ∈ Xe ′ lying over x by Lemmas 3.7,
3.8 and 3.9. We must show that u◦π◦ι ◦ν ≡ −∞ on Xe ′ . Since u◦π◦ι ◦ν is subharmonic
by Proposition 3.5(7,8), we may replace X by Xe ′ to assume that X is rig-smooth and
connected (and still that ∂ X = ; or ∂ X = {x} using the quoted lemmas again).
    If ∂ X = ; then X is smooth and connected, so u is either identically −∞ or it is sub-
harmonic in Thuillier’s sense. The latter case is impossible when u(x) = −∞ by [Thu05,
Proposition 3.4.10].
    Suppose then that X is rig-smooth and connected, and that ∂ X = {x} and u(x) = −∞.
By Lemma 3.11, there is an open neighborhood U of x on which u ≡ −∞. Since X
is connected, every connected component of Int(X ) contains x in its closure. Thus U
intersects every connected component C of Int(X ). This implies that u takes the value
−∞ on a non-rig point of C, so the previous paragraph shows that u ≡ −∞ on C. It
follows that u ≡ −∞ on X .                                                                           □
3.12. Now we turn to harmonic functions. Let X be a smooth, strictly k-analytic curve
with k non-trivially valued and let h: X → R be a function. We claim that h is harmonic
in the sense of (3.2) if and only if h and −h are subharmonic (in our sense or Thuillier’s—
see (3.4.2)). This is implicit in Thuillier’s thesis, but it requires justification. Suppose then
that h: X → R is harmonic. Then ±h are subharmonic by [Thu05, Proposition 2.3.13 and
Corollaire 3.1.12]. Conversely, suppose that ±h are subharmonic. This implies that h is
continuous. Let U ⊂ X be a strictly affinoid domain. By [Thu05, Lemme 2.3.9], there
exists a unique harmonic function h′ : U → R that coincides with h on ∂ U. By definition


## GR-2506.13548v2-20261004 cache page 21

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


## GR-2506.13548v2-20261004 cache page 22

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


## GR-2506.13548v2-20261004 cache page 23

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


## GR-2506.13548v2-20261004 cache page 30

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


## GR-2506.13548v2-20261004 cache page 31

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


## GR-2503.05513-20261004 cache page 15

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


## GR-2503.05513-20261004 cache page 16

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


## GR-2503.05513-20261004 cache page 17

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


## Thuillier-tel-00010990v1 cache page 19

                                                                                                 5



     G-lo al de polyèdres entiers pondérés) si, pour tout point x ∈ S et tout élément t ∈ Tx S :
                                    X               X
                        wx (t) =                               wx′ (t′ ),
                                   x′ ∈f −1 (x)   t′ ∈Tx′ S ′ ; Tx f (t′ )=t

     où Tx′ f est l'appli ation de Tx′ S ′ dans Tx S induite par f .
Remarque 1.2.4
   Les polyèdres entiers que l'on ren ontrera au hapitre 2 proviendront des graphes de ré-
du tion de ourbes algébriques nodales, lesquels sont munis d'une dé omposition élémentaire
 anonique. Dans e ontexte, les sous-polytopes de dimension 1 orrespondront aux points
singuliers des ourbes onsidérées et les poids seront simplement les degrés résiduels de es
points.
    Un polyèdre entier de dimmnsion au plus 1 est muni, par défaut, du poids onstant égal à
1 : pour tout x ∈ S tel que dimx (S) = 1, wx ≡ 1.
Définition 1.2.5.  Soit S un polyèdre entier de dimension au plus 1. Un sous-polyèdre
de S est un domaine polyédral S ′ ⊂ S tel que S ′ − ∂S ′ soit ouvert dans S .
Remarque 1.2.6.  Étant donné un polyèdre entier S et un domaine polyédral S ′ ⊂ S ,
l'ensemble Tx S ′ s'identie anoniquement à un sous-ensemble de Tx S pour tout point x ∈ S ′ ;
  ela permet de munir S ′ du poids induit par elui de S . Le domaine polyédral S ′ est un sous-
polyèdre de S si et seulement si Tx S ′ = Tx S pour tout x ∈ S ′ − ∂S ′ .

Convention.       À partir de maintenant, tous les polyèdres entiers onsidérés sont de di-
mension au plus 1 et pondérés ; on parlera simplement de polyèdres entiers.
   Soient P un polytope entier de dimmnsion 1 et x, x′ les deux points du bord de P . L'unique
fon tion tx ∈ Λ(P ) telle que tx ≥ 0, tx (x) = 0 et dont l'image engendre Λ(P )/R est une base
de l'espa e ve toriel {f ∈ ΛR (P ) | f (x) = 0} et l'on note λP,x l'appli ation R-linéaire de
ΛR (P ) dans R telle que
                                         f = f (x) + λP,x (f )tx ,
f ∈ ΛR (P ). De manière équivalente, l'appli ation tx : P → R réalise un isomorphisme de P
sur le polytope entier ([0, tx (x′ )], R ⊕ Zt) et f = t∗x (f (x) + λP,x (f )t).
   S'il n'y a pas de risque de onfusion, ette appli ation sera simplement notée λx .
    L'appli ation R-linéaire λx : ΛR (P ) → R se prolonge en une appli ation R-linéaire de
A0 (P ) dans R, en ore notée λx : si f ∈ A0 (P ), il existe un sous-polytope entier Q de P tel
que dim(Q) = 1, x soit une fa e de Q et f|Q ∈ ΛR (Q) ; le réel λQ,x (f ) ne dépend pas du hoix
de Q.
    La fon tion tx (x′ ) − tx ∈ Λ(P ) est positive sur P , nulle en x′ et son image dans le groupe
abélien Λ(P )/R, oïn idant ave elle de −tx , est un générateur. Il en résulte l'égalité tx′ =
tx (x′ ) − tx et don , pour toute fon tion f ∈ ΛR (P ),
                                        λx (f ) + λx′ (f ) = 0.
Tout point y intérieur à P détermine une dé omposition élémentaire D = {x, y, x′ , P ′ , P ′′ } de
P , où P ′ , P ′′ sont des sous-polytopes entiers de P de dimension 1, de bords {x, y}, {y, x′ }
respe tivement. Étant donnée une fon tion f dans ΛR (P ), f|P ′ ∈ ΛR (P ′ ), f|P ′′ ∈ ΛR (P ′′ ) et
don
                            λP ′ ,x (f ) + λP ′ ,y (f ) = λP ′′ ,x′ (f ) + λP ′′ ,y (f ) = 0 ;
utilisant l'égalité λP ′ ,x (f ) + λP ′′ ,x′ (f ) = 0, il en dé oule nalement :
                                     λP ′ ,y (f ) + λP ′′ ,y (f ) = 0.


## Thuillier-tel-00010990v1 cache page 20

6



  Soient S un polyèdre entier et x un point de S tel que dimx (S) = 1. Étant donnés des
sous-polytopes entiers P1 , . . . , Pn de S tels que
  (i) dim(Pi ) = 1,
  (ii) x soit une fa e de P1 , . . . , Pn et Pi ∩ Pj = {x} si i 6= j ,
  (iii) P1 ∪ . . . ∪ Pn soit un voisinage de x dans S ,
Tx S s'identie à π0 (P1 ∪ . . . ∪ Pn − {x}) et l'appli ation R-linéaire

                                             res                λPi ,x
                                    A0 (S)         / A0 (Pi )            /R

ne dépend que du point t ∈ Tx S asso ié à Pi ; elle est notée λx,t . Rappelant que S est muni
d'un poids w, nous introduisons une forme R-linéaire sur A0 (S) en posant
                                         X
                                   λx =        wx (t)λx,t .
                                              t∈Tx S

   Cette dernière formule garde en sens lorsque x est un point isolé de S : Tx S = ∅ et don
λx (f ) = 0 pour toute fon tion f ∈ A0 (S).
   Il existe, pour toute fon tion f|Q ∈ A0 (S), une dé omposition élémentaire D de S telle que
f|Q ∈ ΛR (Q) pour tout Q ∈ D ; tous les points x ∈ S tels que λx (f ) 6= 0 sont alors ontenus
dans l'ensemble lo alement ni des polytopes Q ∈ D de dimension 0. Notant A1 (S) l'espa e
ve toriel des mesures réelles sur S dont le support est lo alement ni, la formule
                                               X
                                       ddc f =     λx (f )δx
                                                   x∈S

dénit une appli ation linéaire ddc : A0 (S) → A1 (S).
Définition 1.2.7.  Étant donnés un polyèdre entier S et un point x ∈ S , une fon tion
ane par mor eaux h sur S est dite harmonique en x si λx (f ) = 0.
   Pour tout sous-ensemble lo alement ni Γ de S , une fon tion ane par mor eaux sur S est
dite harmonique sur S − Γ si elle est harmonique en tout point de S − Γ, 'est-à-dire si le
support de ddc f est ontenu dans Γ.
  L'ensemble des fon tions ontinues sur S et harmoniques sur S − Γ est un sous-espa e
ve toriel de A0 (S), noté H(S, Γ).
Remarque 1.2.8
    1. Soient Γ une partie lo alement nie de S et D une dé omposition élémentaire de S telle
       que :
           le poids w soit onstant sur haque polytope P ∈ D[1] ;
           Γ ⊂ D[0].
       Étant donnés une fon tion h ∈ H(S, Γ) et un polytope entier P ∈ D[1], la remarque
       pré édente montre que la restri tion de h à P est harmonique sur P − ∂P relativement
       au poids induit par w ; puisque elui- i est onstant, h|P ∈ H(P, ∂P ) = ΛR (P ).
    2. Étant donnés une partie lo alement nie Γ de S et un sous-polyèdre entier S ′ ⊂ S ,
       Γ′ = Γ ∩ S ′ est une partie lo alement nie de S ′ . Pour toute fon tion h ∈ H(S, Γ), la
       fon tion h|S ′ appartient à l'espa e H(S ′ , Γ′ ∪ ∂S ′ ) : en eet, l'inje tion S ′ ֒→ S est un
       isomorphisme au voisinage de tout point de S ′ − ∂S ′ et don λx (h|S ′ ) = λx (h) pour tout
       point x ∈ S ′ − ∂S ′ .
    3. Soit Γ une partie lo alement nie de S ; il existe, pour toute fon tion h ∈ H(S, Γ), une
       dé omposition élémentaire D de S telle que h|P ∈ ΛR (P ) pour tout polytope P ∈ D[1].


## Thuillier-tel-00010990v1 cache page 21

                                                                                                                         7



  4. Soit f : (S ′ , w′ ) → (S, w) un isomorphisme G-lo al de polyèdres pondérés, surje tif ;
     étant donnée une fon tion ϕ ∈ A0 (S),
                                 X      X                         
                c ∗                                     ∗   ′    ′
          f∗ (dd f ϕ) = f∗                    λx′ ,t′ (f ϕ)wx′ (t )
                                     x′ ∈S ′    t′ ∈Tx′ S ′
                                X X                               X                    X                            
                           =                   λx,t (ϕ)                                                    wx′ ′ (t′ )
                               x∈S t∈Tx S                     x′ ∈f −1 (x)   t′ ∈Tx′ S ′ ; Tx′ f (t′ )=t
                                X X
                           =                   λx,t (ϕ)wx (t)
                               x∈S t∈Tx S
                                 c
                           = dd ϕ.


   Il onvient enn de remarquer le fait suivant : quelle que soit la partie lo alement nie
Γ de S , toute fon tion h ∈ H(S, Γ) est lo alement onstante au voisinage des points de ∂S
n'appartenant pas à Γ. En eet, étant donné x ∈ ∂S ∩ (X − Γ), dimx (S) = 1 et il existe
un sous-polytope entier P de S qui est un voisinage de x et tel que h|P ∈ ΛR (P ) ; notant t
l'unique point de Tx S , on a alors 0 = λx (h) = wx (t)λP,x (h|P ), don λP,x (h|P ) = 0 puisque
wx (t) > 0, et h|P est onstante.

1.2.2. Propriétés
  Soient S un polyèdre entier et Γ une partie lo alement nie de S ; nous allons rapidement
passer en revue les prin ipales propriétés atta hées au sous-espa e H(S, Γ) de A0 (S).

Proposition 1.2.9.             (Prin ipe du maximum)
Une fon tion h ∈ H(S, Γ) admet un extremum en un point x ∈ S − Γ si et seulement si h est
lo alement onstante en x.
Démonstration. L'assertion est triviale au voisinage de tout point isolé de S .
  Considérons des sous-polytopes entiers P1 , . . . , Pn de S tels que dim(Pi ) = 1, x soit une fa e
de P1 , . . . , Pn , P1 ∪. . .∪Pn soit un voisinage de x et h|Pi ∈ ΛR (Pi ). Pour tout i ∈ {1, . . . , n}, Pi
détermine un point ti dans Tx S et λx,ti (h) = λPi ,x (h|Pi ). Reprenant les notations introduites
au paragraphe 1.2.1,
                                        h|Pi = h(x) + λPi ,x (h)ti,x
et, la fon tion ti,x étant stri tement positive sur Pi − {x}, h a un minimum (resp. maximum)
lo al en x si etPseulement si λPi ,x (h) ≥ 0 (resp. λPi ,x (h) ≤ 0) pour tout i. Puisque wx (ti ) > 0
pour tout i et 1≤i≤n wx (ti )λPi ,x (h) = 0 par harmoni ité de h en x, il en résulte que h admet
un extremum lo al en x si et seulement si λPi ,x (h) = 0 pour tout i ∈ {1, . . . , n}, 'est-à-dire
si et seulement si h est onstante au voisinage de x.                                               2
Corollaire 1.2.10.  Si S est                  ompa t et si Γ ren ontre toutes les omposantes onnexes
de S ,
                                max h = max h                 et      min h = min h
                                 S              Γ                       S           Γ

pour toute fon tion h ∈ H(S, Γ).
Corollaire 1.2.11.  Supposons S                      ompa t et onnexe ; si Card(Γ) ≤ 1, toute fon tion
dans H(S, Γ) est onstante.


## Thuillier-tel-00010990v1 cache page 33

                                                                                              19



  Les propriétés suivantes sont immédiates pour tout S -s héma formel maximal X :
   le morphisme πX : Xe → Xsréd est un isomorphisme ;
   X est uniquement déterminé par la donné de l'espa e stri tement k-analytique Xη , de
    l'espa e topologique sous-ja ent à sa bre spé iale Xs et de l'appli ation de rédu tion
    r : Xη → Xs .
  Un S -s héma formel topologiquement de présentation nie et plat est maximal si et seule-
ment s'il est intégralement fermé dans sa bre générique.
Le groupe Λ(X ).
  Étant donné un S -s héma formel plat X , désignons par Λk (X ) le sous-groupe du groupe
abélien C0 (|Xη |, R) image de l'homomorphisme anonique
                                         ×
                         Γ(X , OX ) ⊗k◦ k → C0 (|Xη |, R), f 7→ log |f |.
L'homomorphisme f ∗ : C0 (|Yη |, R) → C0 (|Xη |, R) déni par un morphisme de S -s hémas
formels f : X → Y induit un homomorphisme Λk (f ) de Λk (Y) dans Λk (X ).
   Nous désignerons par Λ(X ) le sous-groupe de l'espa e C0 (|Xη |, R) des fon tions réelles
  ontinues sur |Xη | engendré par R et Λk (X ).
Lemme 2.1.6.  Pour tout S -s héma formel plat et lo alement de présentation nie X ,
l'appli ation de restri tion
                            Λ(X ) ⊂ C0 (|Xη |, R) → Hom(S0 (X ), R)
est inje tive et l'homomorphisme
                                Λ(X )/R → Hom(S0 (X ), R)/R
obtenu en tuant les fon tions onstantes est à valeurs dans l'image du sous-groupe
                   {b ∈ Hom(S0 (X ), R) ; b(x) ∈ log |H(x)|× pour tout x}.
Démonstration. Soient U un re ouvrement de Xs par des ouverts anes et X ′ le S -s héma
formel somme des X|U ; en vertu du diagramme ommutatif

                                  Λ(X )       / Hom(S0 (X ), R)


                                                     
                                 Λ(X ′ )     / Hom(S0 (X ′ ), R)

dans lequel les deux è hes verti ales sont inje tives, il est loisible de supposer X ane.
   Lorsque X est ane, X = Xη est un espa e stri tement k-anoïde dont S0 (X ) est le
bord de Shilov ; puisque toute se tion f ∈ Γ(X, OX ) atteint son maximum en un point de
Γ(X) = S0 (X ), une se tion f ∈ Γ(X, OX )× identiquement égale à 1 sur Γ(X) est de module
  onstant sur X et l'appli ation de restri tion C0 (|X|, R) → Hom(S0 (X ), R) est inje tive sur
l'image de l'homomorphisme Γ(X, OX )× → C0 (|X|, R), f 7→ log |f |.
  La se onde assertion est triviale.                                                           2
Les sites XG et XR .
   La dénition des espa es k-analytiques présentée dans [3℄ et étendue dans [4℄ est telle que la
notion de domaine anoïde dans un espa e k-analytique soit bien dénie (exa tement omme
la notion de sous-polytope d'un polyèdre).
   De manière générale, une partie Y d'un espa e k-analytique X est un domaine k-analytique
si elle admet un re ouvrement lo alement ni par des domaines k-anoïdes. Le G-site de X


## Thuillier-tel-00010990v1 cache page 34

20



est la atégorie XG dont les objets sont les domaines k-analytiques de X et les morphismes les
in lusions, munie de la topologie de Grothendie k pour laquelle les familles ouvrantes sont
les re ouvrement pouvant être ranés en un re ouvrement lo alement ni par des domaines
k-anoïdes. La orrespondan e
                                           V 7→ AV ,
où V est un domaine k-anoïde de X et AV est l'algèbre de V , se prolonge en un fais eau
OX sur le G-site XG de X , le fais eau stru tural de X .
   Notons |X| l'espa e topologique sous-ja ent à X ainsi que le site anoniquement asso ié ;
tout point de X admettant un système fondamental de voisinages formé par des domaines
k-analytiques ompa ts, tout ouvert de |X| est la réunion d'une famille lo alement nie de
domaines k-anoïdes et détermine don un objet de XG . On dénit ainsi une è he
                                      πX : XG → |X| ;
 'est un morphisme de sites.
   Un domaine stri tement k-analytique est une partie de X admettant un re ouvrement
lo alement ni par des domaines stri tement k-anoïdes. Lorsque X est un espa e stri tement
k-anoïde (au sens de [4℄, 'est-à-dire tel que tout point admette un système fondamental
de voisinages formé de domaines stri tement k-analytiques ompa ts), nous appelerons site
rigide de X et noterons XR , la sous- atégorie pleine de XG dont les objets sont les domaines
stri tement k-analytiques, munie de la topologie de Grothendie k induite.
Remarque 2.1.7.  Le préfais eau
                                       Y ; C0 (|Y |, R)
sur le site XG est un fais eau : en eet, une fon tion ϕ sur un espa e topologique X est
 ontinue s'il existe un re ouvrement lo alement ni de X par des fermés F tels que ϕ|F soit
 ontinue.
Convention.        Étant donné un espa e k-analytique X , un ouvert (resp. fermé ) de X sera
toujours une partie ouverte (resp. fermée) de l'espa e topologique |X| sous-ja ent à X .
Morphismes nis et plats.
   Soient p : Y → X un morphisme ni et plat d'espa es k-analytiques et x un point de
X . L'anneau semi-lo al OY,p−1 (x) est une OX,x -algèbre libre de rang ni se dé omposant
 anoniquement sous la forme
                                               M
                                  OY,p−1 (x) =       OY,y .
                                                y∈p−1 (x)
Pour tout point y ∈ p−1 (x), OY,y est une OX,x -algèbre libre de rang (degy p), munie d'une
semi-norme multipli ative |.(y)| induite par l'homomorphisme anonique OY,y → H(y) ; elle
prolonge la semi-norme |.(x)| sur OX,x provenant de OX,x → H(x).
                                                                               ×
Proposition 2.1.8.  Pour tout point y ∈ p (x) et tout élément f de OY,y , la norme
                                                  −1
                                   ×
Ny/x (f ) de f est un élément de OX,x tel que
                                 |Ny/x (f )(x)| = |f (y)|degy p .
Démonstration. Soit f ′ l'image de f dans A = OY,y ⊗OX,x H(x). La multipli ation par f
(resp. f ′ ) est un automorphisme de la OX,x -algèbre OY,y (resp. de la H(x)-algèbre A), de
                             ×
déterminant Ny/x (f )(x) ∈ OX,x (resp. N(f ′ ) ∈ H(x)× ) et :
                                   |Ny/x (f )(x)| = |N(f ′ )|


## Thuillier-tel-00010990v1 cache page 56

42



  Le as général s'obtient en re ouvrant Ys par des ouverts onnexes U ontenant au plus
un point singulier de Ys et pour lesquels il existe un morphisme étale pU : Y|U → S(a(U )),
a(U ) ∈ k◦ − {0} induisant un isomorphisme entre les polytopes entiers S(X|U ) et S(S(a(u))).
2
     La démonstration du théorème 2.2.10 est maintenant a hevée.
Proposition 2.2.21.  Soit         X une S - ourbe simplement semi-stable ; quelle que
soit l'extension non ar himédienne K/k, le morphisme anonique d'espa es analytiques
p K : Xη ⊗b k K → Xη envoie S(X ×S Spf(K ◦ )) dans S(X ) et l'appli ation induite est un
isomorphisme G-lo al de polyèdres entiers pondérés.
Démonstration. Les deux assertions de l'énon é sont démontrées si elles le sont pour ha une
des S - ourbes X|U , U par ourant un re ouvrement ouvert de Xs ; nous pouvons don supposer
qu'il existe un morphisme étale q : X → S(a) induisant un isomorphisme du polyèdre entier
S(X ) sur S(S(a)). Considérons le diagramme ommutatif
                                                           pK
                                         b kK
                                      Xη ⊗                        / Xη

                                     qη,K                                    qη
                                                                        
                                          b kK
                                    S(a)η ⊗                     / S(a)η ;
                                                           p′K

il a été noté au début de 2.2.1 que le morphisme p′K induit un isomorphisme du polyèdre entier
S(S(a) ×S Spf(K ◦ )) sur S(S(a)), d'où il dé oule que le morphisme pK dénit une appli ation
de S(X ×S Spf(K ◦ )) dans S(X ) qui est un morphisme de polyèdres entiers s'insérant dans le
diagramme ommutatif
                                                           pK
                                S(X ×S Spf(K ◦ ))                             / S(X )

                                    qη,K                                              qη
                                                                                 
                              S(S(a) ×S Spf(K ◦ )) ′                   / S(S(a)).
                                                           pK

Les è hes p′K et qη sont des isomorphismes et, d'après la proposition 2.2.20, la è he qη,K
est un isomorphisme G-lo al ; le morphisme pK : S(X ×S Spf(K ◦ )) → S(X ) est nalement un
isomorphisme G-lo al de polyèdres entiers.
     Nous é rirons S(X )K en lieu et pla e de S(X ×S Spf(K ◦ )).
  Il reste à vérier la ompatibilité ave les poids. Notons r : Xη → Xs et rK : Xη ⊗ b kK →
                
              ◦            e
 X ×S Spf(K ) s = Xs ⊗ek K les appli ations de rédu tion, qui s'insèrent dans le diagramme
 ommutatif :
                                             r
                                   Xη ⊗                e
                                      b k K K / Xs ⊗ e K
                                                     k
                                      pK                               pK
                                                                        e
                                                                  
                                       Xη              r
                                                                / Xs .

Considérons un point ξ de S0 (X ) et un élément t de Tξ S(X ), e dernier orrespondant à
un point singulier x
                   e de Xs ontenu dans la omposante irrédu tible de point générique r(ξ).
Étant donné un voisinage U de x  e dans X et un morphisme étale p : U → S(a), a ∈ k◦ ,
on peut restreindre U de telle sorte que x
                                         e soit l'unique point de la bre p−1 (p(e
                                                                                 x)) ; elle- i
est alors un κ(p(e      e
                 x)) = k-s héma ni et réduit (p est étale), de rang [κ(e     e
                                                                         x) : k]. La bre de


## Thuillier-tel-00010990v1 cache page 57

                                                                                                 43



(p ⊗ 1) : U ⊗S Spf(K ◦ ) → S(a) ⊗S Spf(K ◦ ) au-dessus du point singulier est, de même, un
Ke -s héma ni et réduit ; puisqu'il s'identie à p−1 (p(x)) ⊗e K                     x) : e
                                                                e , il est de rang [κ(e
                                                                        k
                                                                                           k] et don

                                                       X
                                    x) : e
                                 [κ(e    k] =                            e
                                                                  x′ ) : K].
                                                               [κ(e
                                                     e′ ∈p−1
                                                     x       e)
                                                          e (x
                                                         K


Cette dernière identité se réé rit sous la forme
                                          X                   X
                            wξ (t) =                                          wξ ′ (t′ ),
                                       ξ ′ ∈p−1       t′ ∈Tξ′ S(X )K ,t′ →t
                                             K (ξ)



  e qui établit que pK est un isomorphisme de polyèdres entiers pondérés ( f. remarque 1.2.3,
2).                                                                                         2
    La notation iK que nous employons dans le lemme suivant a été dénie en 2.1.3 (Extension
des s alaires ). Rappelons que, pour tout point x de X , s(x) est le degré de trans endan e de
             e
l'extension H(x)/  e
                   k ; x est dit de type (2) si et seulement si s(x) = 1.
Lemme 2.2.22.  Soit X         une S - ourbe simplement semi-stable.
   (i ) Étant donné un sous-ensemble ni Σ ⊂ S(X ), il existe une extension non ar himédienne
K/k et un é latement admissible Y → X ×S Spf(K ◦ ) tels que Y soit une Spf(K ◦ )- ourbe
simplement semi-stable et iK (Σ) ⊂ S0 (Y). L'extension K/k peut être hoisie nie (séparable)
si et seulement si tous les points de Σ sont de type (2).
   (ii ) Étant donné un ensemble ni Σ′ de points de type (2) ou (3) dans Xη , il existe une
extension nie (séparable) k′ /k et un é latement admissible Y ′ → X ×S Spf(k′ ◦ ) tels que Y ′
soit une Spf(k′ ◦ )- ourbe simplement semi-stable et ik′ (Σ′ ) ⊂ S(Y ′ ).
Démonstration. Traitons d'abord le as X = S(a).
(i) On peut supposer que l'ensemble Σ est réduit à un point x.
    Considérons une extension non ar himédienne K/k telle que |H(x′ )× | = |K × |, où x′ est le
point de S(S(a))K orrespondant à x dans l'identi ation anonique S(S(a))K = S(S(a)) ;
  ette extension peut être hoisie si (et seulement si) x est de type (2).
    Fixons b ∈ K × tel que |T0 (x′ )| = |b| ; |a| ≤ |b| ≤ 1 et l'é latement sur S ×S Spf(K ◦ ) de
l'Idéal (T0 , b)  inversible en dehors du point singulier de S(a)s  donne lieu à un morphisme
q : Z → S(a) ×S Spf(K ◦ ) tel que Z soit une Spf(K ◦ )- ourbe simplement semi-stable et
S0 (Z) = S0 (S(a)) ∪ {x′ }.
(ii) On peut de nouveau supposer Σ′ réduit à un point x. Si x ∈ S(S(a)), il n'y a rien
à démontrer ; sinon, le point x′ = τ (x) de S(S(a)) est tel que s(x′ ) = 1 et on vient de
prouver qu'il existe une extension nie k′ /k telle que le point de S(S(a))k′ orrespondant à
x′ dans l'identi ation anonique S(S(a))k′ = S(S(a)) appartienne à S0 (S(a) ×S Spf(k′ ◦ )).
On est ainsi ramené au as d'un point x tel que τ (x) ∈ S0 (S(a)). L'appli ation de rédu tion
S(a)η → S(a)s envoie x sur un point lisse x    e appartenant à la omposante irrédu tible de
point générique r(τ (x)).
   Le omplémentaire E de la omposante onnexe non bornée de S(a)η − {x} ⊂ A1k − {x} est
un disque fermé de point de Shilov x. Soit y un point dans E tel que l'extension κ(y)/k soit
nie, de polynme minimal f normalisé de telle sorte que |f (τ (x))| = 1 ; hoisissons également
b ∈ k× tel que |f (x)| > |b|. L'Idéal I sur S(a) tel que Ixe = f OS(a),xe + bOS(a),xe et I = OS(a)
sur S(a)s − {ex} est admissible et son é latement q : Z → S(a) fournit une S - ourbe Z dont


## Thuillier-tel-00010990v1 cache page 67

                                                                                                53



et S(f )∗ H ∈ A0 (S(X )). Il reste à vérier que la fon tion S(f )∗ H est harmonique sur S(X ) −
∂Xη . C'est une onséquen e dire te du point (iv) de la proposition 2.2.27 : f (x) ∈ / ∂Yη pour
tout point x ∈ S(X ) − ∂Xη et
                         Z                              Z
                               ddc S(f )∗ H = (degx f )       ddc H = 0.
                          {x}                             {f (x)}
                                                                                                 2
  Si X est un espa e stri tement k-anoïde et ϕ : X → ˜ Xη est un isomorphisme de X sur la
bre générique d'une S - ourbe simplement semi-stable X , le sous-espa e ve toriel réel ϕ∗ H(X )
de C0 (|X|, R) ne dépend pas du hoix de X et de ϕ ; il est noté H(X).
   De manière générale, étant donnés un espa e k-analytique X et une lture algébrique ka de
k, le groupe de Galois G de la fermeture séparable ksep de k dans ka opère par automorphismes
sur l'espa e c                b kc
             ka -analytique X ⊗  ka . On dispose d'un morphisme G-équivariant anonique
                                          p : X⊗  ca → X
                                               b kk
d'espa es analytiques et l'appli ation ontinue sous-ja ente est un quotient de |X ⊗        ca | par
                                                                                        b kk
l'a tion de G dans la atégorie des espa es topologiques : 'est en eet un quotient dans la
  atégorie des ensembles d'après le orollaire 1.3.6 de [3℄ et l'appli ation ontinue p est ouverte.
Proposition 2.3.7.  Quelles que soient la S - ourbe simplement semi-stable X et l'ex-
tension nie galoisienne k′ /k, l'a tion du groupe G = Gal(k′ /k) sur C0 (|Xη ⊗k k′ |, R) stabilise
le sous-espa e H(Xη ) et l'isomorphisme anonique
                                 C0 (|Xη |, R) → C0 (|Xη ⊗k k′ |, R)G
induit un isomorphisme de H(Xη ) sur H(Xη ⊗k k′ )G .
Démonstration. On peut supposer Xη onnexe.
   Si Xη est propre, H(Xη ) (resp. H(Xη ⊗k k′ )) est l'espa e des fon tions onstantes sur Xη
(resp. lo alement onstantes sur Xη ⊗k k′ ) (proposition 2.3.2, 1) et l'assertion est évidente.
   Si Xη n'est pas propre, alors il en est de même pour haque omposante onnexe de Xη ⊗k k′
et, d'après la proposition 2.3.2,2, les restri tions
                                      H(Xη ) → Hom(∂Xη , R)
et
                                H(Xη ⊗k k′ ) → Hom(∂(Xη ⊗k k′ , R)
sont bije tives. L'assertion résulte ainsi de l'identité ∂Xη = ∂(Xη ⊗k k′ )G .                   2

2.3.2. Le théorème de rédu tion semi-stable.
   C'est i i qu'intervient le théorème de rédu tion semi-stable.
Théorème 2.3.8.  Soit X un espa e stri tement k -anoïde purement de dimension 1
et rig-lisse ; il existe une extension nie séparable k′ de k telle que le domaine k′ -anoïde
X ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
Démonstration. Il existe une extension nie séparable k1 de k et une ourbe algébrique C
propre et lisse sur k1 telles que X ⊗k k1 soit isomorphe à un domaine anoïde de C ([31℄,
theorem 1). Appliquant le théorème de rédu tion semi-stable sous la forme rigide-analytique
établie par S. Bos h et W. Lütkebohmert dans [9℄, il existe une extension nie séparable k′
de k1 telle que C ⊗k1 k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe C dont la
bre spé iale est simplement semi-stable ; 'est automatiquement une S - ourbe semi-stable


## Thuillier-tel-00010990v1 cache page 68

54



(remarque 2.2.9, 3). En hoisissant onvenablement k′ , on peut en outre supposer que tout
point x du bord de X ⊗k k′ satisfait à la ondition |κ(x)× | = |k′ × |.
    Envisageons X ′ = X ⊗k k′ omme un domaine stri tement k′ -anoïde de Cη et soit q :
C ′ → C un é latement admissible tel que C ′ soit une Spf(k′ ◦ )- ourbe simplement semi-stable,
ave ∂X ′ ⊂ S0 (C ′ ) (lemme 2.2.22). L'image de X ′ par l'appli ation de rédu tion Cη′ → Cs
est un ouvert U et X ′ est isomorphe à la bre générique de la Spf(k′ ◦ )- ourbe simplement
semi-stable X = C|U′ .                                                                       2
  Soient X un espa e stri tement k-anoïde purement de dimension 1 rig-lisse et k′ , k′′ deux
extensions nies galoisiennes de k telles que X ⊗k k′ et X ⊗k k′′ soient isomorphes aux bres
génériques de ourbes stri tement semi-stables ; étant donnée une extension nie galoisienne
K de k oiant k′ et k′′ , la proposition 2.3.7 implique l'identité des espa es H(X ⊗k k′ ) et
                   ′                                          ′′
H(X ⊗k K)Gal(K/k ) (resp. H(X ⊗k k′′ ) et H(X ⊗k K)Gal(K/k ) ), d'où dé oule l'égalité
                               ′                                              ′′
              H(X ⊗k k′ )Gal(k /k) = H(X ⊗k K)Gal(K/k) = H(X ⊗k k′′ )Gal(k /k) .
Le théorème pré édent permet ainsi de dénir, pour tout espa e stri tement k-anoïde X
purement de dimension 1 et rig-lisse, un sous-espa e ve toriel H(X) de C0 (|X|, R) : H(X) =
                ′
H(X ⊗k k′ )Gal(k /k) ⊂ C0 (|X|, R), k′ étant une extension nie galoisienne de k telle que X ⊗k k′
soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
   Désignant par C la atégorie dont les objets sont les espa es stri tement k-anoïdes, pure-
ment de dimension 1 et rig-lisses, et les morphismes les immersions anoïdes, il dé oule de la
proposition 2.3.3 que l'on vient ainsi de dénir un fon teur H sur Cop à valeurs dans VectR .
  Nous aurons besoin des deux résultats suivants.
Lemme 2.3.9.  Pour tout espa e stri tement k -anoïde Y rig-lisse et purement de di-
mension 1, l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
induit un isomorphisme du sous-espa e H(Y ) sur Hom(Γ(Y ), R).
Démonstration. Soit k′ une extension galoisienne nie de k telle que l'espa e stri tement
k′ -anoïde Y ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-
                                                                                            ′
stable Y . La proje tion anonique p : Y ⊗k k′ → Y induit une bije tion de Γ(Y ⊗k k′ )Gal(k /k)
sur Γ(Y ) et l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
 oïn ide ave l'appli ation induite par la restri tion
                            C0 (|Y ⊗k k′ |, R) → Hom(Γ(Y ⊗k k′ ), R)
                                                                                           ′
entre les sous-espa es des invariants sous Gal(k′ /k) ; puisque H(Y ) = H(Y ⊗k k′ )Gal(k /k) , la
 on lusion dé oule de la proposition 2.3.2.                                                    2
Lemme 2.3.10.  Soient Y un espa e stri tement k -anoïde onnexe, de dimension 1 et
rig-lisse, et (hn ) une suite roissante de fon tions appartenant à H(Y ). L'alternative suivante
est vraie :
    soit la suite (hn ) onverge, uniformément sur Y , vers une fon tion h ∈ H(Y ),
    soit la suite (hn ) onverge, lo alement uniformément sur Y − Γ(Y ), vers ∞.
Démonstration. Soient k′ une extension nie galoisienne de k telle que Y ′ = Y ⊗k k′ soit
isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement nodale Y′ et p : Y ′ → Y la
proje tion anonique. Si l'assertion est démontrée pour la suite (p∗ hn ) dans H(Y ′ ), elle l'est
                                                                      ′
également pour la suite (hn ) : en eet, puisque H(Y ) = H(Y ′ )Gal(k /k) , il sut de s'assurer


## Thuillier-tel-00010990v1 cache page 82

68



Démonstration. Il sut d'appliquer les deux propositions pré édentes à l'ouvert relative-
ment ompa t Int(Y ) ⊂ X .                                                                     2


                            3.2. Fon tions lisses, opérateur ddc
   Disposant du fais eau HX des germes de fon tions harmoniques sur une ourbe stri tement
k-analytique lisse X et de la résolution partielle du problème de Diri hlet obtenue à la se tion
pré édente, nous allons maintenant dénir les fais eaux A0X (resp. A1X ) des germes de fon tions
lisses (resp. formes lisses ) sur X et un  opérateur de Lapla e  ddc : A0X → A1X ; elui- i
sera lassiquement étendu à des espa es de distributions dans la se tion suivante.

   Désignons par I(X) l'ensemble des points de X de type (2) ou (3) ; de manière équivalente,
I(X) est l'ensemble des points de Shilov des domaines k-anoïdes de X . Plus pré isément :
le bord de Shilov Γ(Y ) d'un domaine k-anoïde Y de X est un sous-ensemble ni de I(X) et
toute partie nie S de I(X) est la réunion des bords de Shilov d'un nombre ni de domaines
k-anoïdes.

3.2.1. Les fais eaux A0X et A1X sur XG .
     Dans e qui suit, X désigne une ourbe stri tement k-analytique lisse.
Définition 3.2.1.  Soit Ω ⊂ X un ouvert.
   (i ) Une fon tion réelle ϕ ∈ C (Ω, R) est dite lisse s'il existe un re ouvrement lo alement
                           0

ni V de Ω par des domaines k-anoïdes Y tel que ϕ|Y ∈ H(Y ). L'ensemble des fon tions
lisses sur Ω est un sous-espa e ve toriel de C0 (Ω, R), noté A0 (Ω).
   (ii ) On désigne par A1 (Ω) l'espa e ve toriel des mesures réelles sur Ω dont le support est
un sous-ensemble lo alement ni de I(Ω). Les éléments de A1 (Ω) seront appelés formes lisses
(sur Ω).

  (iii ) Le sous-espa e ve toriel de A0 (Ω) (resp. A1 (Ω)) onstituté des fon tions (resp. me-
sures) dont le support est ompa t se note A0c (Ω) (resp. A1c (Ω)).

   La orrespondan e Ω 7→ A0 (Ω) est un sous-fais eau du fais eau CX
                                                                  0 des germes de fon tions

réelles ontinues sur X .
   La dénition du fais eau A0X s'étend d'elle même au G-site XG de X : il sut, pour tout
objet V de XG , de dénir A0 (V ) omme le sous-espa e ve toriel de C0 (V, R) onstitué des
fon tions ϕ ontinues sur V qui satisfont à la ondition suivante : tout point x ∈ V possède
un voisinage k-anoïde W ⊂ V tel que ϕ|W ∈ H(W ). Désignant par A0X le fais eau ainsi
déni sur XG et notant π : XG → |X| le morphisme de sites anonique, l'identité
                                         A0X = π∗ A0X
est évidente. La proposition suivante l'est tout autant.

Proposition 3.2.2.  L'homomorphisme            anonique de préfais eaux HX → A0X sur le site
XG identie A0X au fais eau asso ié à HX .

Remarque 3.2.3
     1. La proposition pré édente répond à la question soulevée par le point 2 de la remarque
        2.3.11.


## Thuillier-tel-00010990v1 cache page 83

                                                                                              69



  2. Pour toute extension nie galoisienne k′ /k, l'homomorphisme anonique
                                                           ′
                                   A0X → (A0 X⊗k k′ )Gal(k /k)
     est un isomorphisme de fais eaux sur XG .

 La proposition suivante n'est guère surprenante, ompte tenu de la onstru tion du fais eau
HX .
Proposition 3.2.4.  Une fon tion réelle ϕ sur un ouvert Ω ⊂ X est lisse si et seulement
s'il existe, pour tout domaine stri tement k-analytique ompa t Y ⊂ Ω, une extension nie
(séparable ) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y telles que :
    Yη = Y ⊗k k ′ ;
    la fon tion Φ = (ϕ ⊗ 1)|S(Y) appartienne à l'espa e A0 (S(Y)) ;
    ϕ|Y ⊗k k′ = Φ ◦ τY .
Démonstration. Soit Y ⊂ X un domaine stri tement k-analytique ompa t.
   Étant données une extension nie galoisienne k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y de bre générique Y ⊗k k′ , onsidérons une fon tion Φ ∈ A0 (S(Y)) et notons S la
réunion du support de la mesure ddc Φ et du bord de Shilov Γ(Yη ) de Yη . Quelle que soit la
 omposante onnexe c de S(X ) − S , la restri tion de Φ au domaine polyédral c appartient
à l'espa e H(c) et la fon tion Φ|c ◦ τY = (Φ ◦ τY )|τ −1 (c) sur le domaine k-analytique τY−1 (c)
                                                      Y
de Y ⊗k k′ appartient à H(τY−1 (c)) ; en vertu de la proposition pré édente, ela implique
Φ ◦ τY ∈ A0 (Y ⊗k k′ ). La ondition de l'énon é est don susante.
   Considérons ré iproquement une fon tion ϕ ∈ A0 (Y ) et un re ouvrement ni V de Y par
des domaines k-anoïdes V tels que ϕ|V ∈ H(V ) ; par appli ation du point (ii) du lemme
2.2.22, il existe une extension nie (séparable) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y , de bre générique Y ⊗k k′ , dont le squelette S(Y) ontient l'ensemble Γ des points de
Shilov des domaines k′ -anoïdes V ⊗k k′ , V ∈ V . Désignons par Φ la restri tion de ϕ′ = ϕ ⊗ 1
au squelette S(Y) de Y . Les bres de la rétra tion τY sont des domaines k′ -anoïdes dont le
bord de Shilov est réduit à un point ; la fon tion ϕ′ , étant harmonique sur Y ⊗k k′ − Γ, est
par suite onstante haque bre de τY en vertu du prin ipe du maximum et
                                          ϕ′ = Φ ◦ τY .
Vérions enn l'appartenan e de Φ à l'espa e A0 (S(Y)) : quel que soit le polytope entier
P ⊂ S(Y) − Γ dont le bord est formé de points de type (2), W = τY−1 (P ) est un domaine
stri tement k-anoïde dans Y tel que ϕ′|W ∈ H(τY−1 (P )) ( orollaire 2.3.14) ; on a don Φ|P =
(ϕ′|W )|P ∈ H(P ) et la fon tion ontinue Φ est bien ane par mor eaux sur S(Y).              2
   La proposition 3.2.2 peut maintenant être pré isée de manière à donner une nouvelle dé-
nition du fais eau A0X sur le G-site XG de X . Étant donné un domaine k-analytique V ⊂ X ,
 onvenons de désigner par R log |OX (V )× | le sous-espa e ve toriel réel de C0 (V, R) engendré
par les fon tions de la forme log |f |, f ∈ OX (V )× . La orrespondan e
                                       ×
                               R log |OX | : V 7→ R log |OX (V )× |

est un sous-préfais eau de A0X sur XG puisque R log |OX (V )× | ⊂ H(V ) pour tout domaine
k-anoïde V ⊂ X .
                                                                   ×
Proposition 3.2.5.  L'homomorphisme              anonique R log |OX | → A0X identie A0X au
                                        ×
fais eau asso ié au préfais eau R log |OX |.


## Thuillier-tel-00010990v1 cache page 84

70



Démonstration. Soit FX le fais eau sur XG asso ié au préfais eau R log |OX× |. Quelle que
                                                                                   ×
soit l'extension galoisienne nie k′ /k, la norme Nk′ /k : (pk′ )∗ (OX ⊗k k′ )× → OX induit un
homomorphisme Nk′ /k : (pk )∗ FX⊗k k → F tel que
                             ′        ′

                                           1
                                   f=              Nk′ /k (f ⊗ 1)
                                        [k′ : k]
pour toute se tion f de F , pk′ désignant la proje tion anonique de X ⊗k k′ sur X . Il sut don
de prouver qu'une se tion ϕ de A0X provient de FX après passage à une extension galoisienne
nie de k.
    Soient Y ⊂ X un domaine k-analytique ompa t et ϕ une fon tion dans A0X (Y ). Il existe par
hypothèse un re ouvrement ni V de Y par des domaines k-anoïdes V tels que ϕ|V ∈ H(V )
et, omme dans la démonstration pré édente, on peut trouver une extension galoisienne nie
k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y dont la bre générique est un voisinage
de Y ⊗k k′ dans X ⊗k k′ et dont le squelette S(Y) ontient l'ensemble Γ de tous les points de
Shilov des domaines k-anoïdes V ⊗k k′ , V ∈ V .
    Considérons alors une dé omposition élémentaire D de S(Y) telle que Γ ⊂ D[0] (on rappelle
que D[0] est l'ensemble des 0-fa es des polytopes gurant dans D ). Quel que soit le polytope
Q ∈ D , τ −1 (Q) est un domaine k-anoïde et, par onstru tion,
                           ϕ|Q ∈ H(τ −1 (Q)) = R log |OX (τ −1 (Q))|.
                                                                                              2
Remarque 3.2.6.  Cette proposition est à rappro her des onsidérations de 2.3.4.
3.2.2. Un résultat de densité.
   Soit E un espa e topologique lo alement ompa t. L'ensemble des fon tions réelles onti-
nues sur E dont le support est ontenu dans un ompa t K de E est noté C0 (E, R)K et la
norme supK |.| en fait un espa e de Bana h. La restri tion de E à K induit une isométrie
de C0 (E, R)K sur le sous-espa e ve toriel fermé de l'espa e de Bana h C0 (K, R) formé des
fon tions s'annulant sur ∂K = K ∩ E − K .
   L'espa e ve toriel C0c (E, R) des fon tions réelles ontinues sur E dont le support est ompa t
est muni de la topologie lo alement onvexe limite indu tive des topologies d'espa es de
Bana h sur les C0 (E, R)K ; 'est la topologie lo alement onvexe la plus ne rendant ontinues
les inje tions C0 (E, R)K → C0c (E, R).
   Lorsque E est l'espa e topologique sous-ja ent à une ourbe stri tement k-analytique lisse
X , il est loisible de ne onsidérer que des ompa ts K qui sont des domaines stri tement
k-analytiques (i.e. des réunions nies de domaines stri tement k-anoïdes) : tout ompa t de
X est en eet ontenu dans un domaine stri tement k-analytique ompa t.
Proposition 3.2.7.  Le sous-espa e Ac (X) est dense dans Cc (X, R).
                                                0                      0

Démonstration. Soient K un domaine k analytique ompa t de X , ε ∈ R>0 et f une
fon tion ontinue sur X s'annulant en dehors de K . De l'uniforme ontinuité de f sur K
dé oule l'existen e d'une famille nie V de domaines k-anoïdes dans X dont la réunion K ′
 ontient K et telle que, pour tout V ∈ V et tous x, y ∈ V , |f (x) − f (y)| ≤ ε/2. Appliquant
le lemme suivant au domaine k-analytique ompa t K ′ et au sous-ensemble Σ réunion des
points de Shilov des V ∈ V et de la frontière de K , il existe une fon tion g ∈ A0 (X) telle que
gΣ = fΣ . Cette fon tion s'annule sur la frontière de K ′ et appartient don à A0 (X)K .
   Étant donné V ∈ V , la fon tion g satisfait, par onstru tion, à l'inégalité
                                                          ε
                                         |g(x) − g(y)| ≤
                                                          2


## Thuillier-tel-00010990v1 cache page 87

                                                                                            73



Ce i permet d'asso ier au morphisme p un homomorphisme p∗ : A1X → p∗ A1Y ainsi déni :
pour tout ouvert Ω ⊂ X , une se tion ω de A1X s'é rit sous la forme
                                          X
                                    ω=        a(x) δx ,
                                             x∈I(Ω)

a étant une fon tion réelle sur I(Ω) s'annulant en dehors d'un sous-ensemble lo alement ni,
et p∗ ω est la se tion
                        X                    X
                              a(x) p∗ δx =          (degy p)a(p(y)) δy
                       x∈I(Ω)                y∈I(p−1 (Ω))

de A1Y sur p−1 (Ω).
   Le morphisme p envoie I(Y ) dans I(X) s'il est quasi-ni ; sous ette ondition, l'image
dire te au sens des mesures dénit un homomorphisme p∗ : p∗ A1Y → A1X : pour tout ouvert
Ω ⊂ X et tout point y ∈ I(p−1 (Ω)),
                                       p∗ δy = δp(y) .
Lorsque p est ni, don plat, l'endomorphisme p∗ p∗ du fais eau A1X est la multipli ation par
(deg p).
3.2.4. L'opérateur ddc .
  Il est maintenant temps d'introduire un  opérateur de Lapla e 
                                        ddc : A0X → A1X ,
analogue non ar himédien du lapla ien omplexe usuel ddc = ∂∂/iπ auquel la proposition
3.2.4 te tout mystère !
Théorème 3.2.10.  Il existe une manière et une seule de dénir, pour toute extension
non ar himédienne K/k et toute ourbe stri tement K -analytique lisse X , un homomorphisme
de fais eaux ddc : A0X → A0Y satisfaisant aux deux onditions suivantes.
   (i ) Quelles que soient l'extension non ar himédienne K ′ /K et la se tion ϕ de A0X sur un
ouvert Ω ⊂ X ,
                                   ddc ϕ = (pK ′ /K )∗ ddc p∗K ′ /K ϕ.
Le se ond membre est l'image dire te de la mesure ddc p∗K ′ /K ϕ par lq proje tion anonique
pK ′ /K de X ⊗
             b K K ′ sur X .
  (ii ) Quels que soient la Spf(K ◦ )- ourbe simplement semi-stable Y et l'isomorphisme j de
Yη sur un domaine K -analytique ompa t Y ⊂ X ,
                                     ddc (Φ ◦ τY ) = j∗ ddc Φ
dans Γ(Y − ∂Y, A1Y ) pour toute fon tion Φ ∈ A0 (S(Y)).
Démonstration. Considérons une extension non ar himédienne K/k et une ourbe stri -
tement K -analytique lisse X . Soient x un point dans I(X) et Y un voisinage stri tement
K -anoïde de x dans X . Pour toute fon tion ϕ ∈ A0 (Y ), la proposition 3.2.4 garantit l'exis-
ten e d'une extension nie (séparable) K ′ /K ainsi que d'une Spf(K ′ ◦ )- ourbe simplement
nodale Y , de bre générique Y ⊗K K ′ , telles que la fon tion ϕ′ = ϕ ⊗ 1 s'é rive Φ ◦ τY , ave
Φ = ϕ′|S(Y) ∈ A0 (S(Y)). Notons les deux faits suivants :
a) quelle que soit l'extension non ar himédienne K ′′ /K ′ ,
                                ddc Φ = (pK ′′ /K ′ )∗ ddc p∗K ′′ /K ′ Φ


## Thuillier-tel-00010990v1 cache page 88

74



(où pK ′′ /K ′ est le morphisme anonique Y ⊗ b K K ′′ → Y ⊗K K ′ ) en vertu de la proposition
2.2.21 et du point 4 de la remarque 1.2.8 ;
b) pour tout é latement admissible q : Y ′ → Y tel que Y ′ soit une Spf(K ′ ◦ )- ourbe simplement
semi-stable,
                                    ddc Φ = (qη )∗ ddc qη∗ Φ
en vertu de la proposition 2.2.26.
     Vérions que le nombre réel                Z
                                                              ddc Φ
                                                {x}⊗K K ′
ne dépend que du germe de ϕ au point x.
   Étant données une extension nie (séparable) K ′′ /K et une Spf(K ′′ ◦ )- ourbe simplement
semi-stable Z telles que :
    Z = Zη soit un voisinage de {x} ⊗K K ′′ dans Y ⊗K K ′′ ,
    ϕ|Z = Ψ ◦ τZ , ave Ψ ∈ A0 (S(Z)),
 onsidérons une extension nie L de K oiant K ′ et K ′′ . L'appli ation de la proposition
2.2.27 à l'immersion anonique Z ⊗K ′′ L ֒→ Y ⊗K L, ouplée aux remarques a) et b) qui
pré èdent, fournit l'égalité
                             Z                 Z
                                         c
                                       dd Ψ =            ddc Φ.
                                   {x}⊗K K ′′                  {x}⊗K K ′

     À e stade, nous disposons, pour tout point x ∈ I(X), d'une appli ation linéaire
                                     ddcx : A0X,x → A1X,x = R δx ,
uniquement ara térisée par l'égalité
                                                Z                       
                                       c                           c
                                   dd ϕ =                         dd Φ       δx ,
                                                      {x}⊗k k ′

 haque fois que le ouple (K ′ , X ) et la fon tion Φ vérient les onditions de l'énon é de la
proposition 3.2.4.
   Quelle que soit la se tion ϕ de A0X sur un ouvert Ω ⊂ X , l'ensemble des points x ∈ I(Y )
tels que ddcx ϕ 6= 0 est lo alement ni ; nous désignons alors par ddc ϕ l'élément
                                             X
                                                  ddcx ϕ
                                                    x∈I(X)

de A1X (Ω).
  L'homomorphisme ddc : A0X → A1X que l'on vient de dénir satisfait aux deux onditions
de l'énon é (le point (i) dé oulant de la remarque a) i-dessus) et 'est lairement le seul. 2
Corollaire 3.2.11
  (i ) Le noyau de l'homomorphisme ddc : A0X → A1X est le fais eau HX .
  (ii ) Pour tout point x ∈ I(X) et tout germe ϕ ∈ A0X,x admettant un minimum lo al stri t
en x,                                  Z
                                                          ddc ϕ > 0.
                                                    {x}

  (iii ) Quel que soit l'ouvert Ω de X , l'appli ation R-linéaire ddc : A0 (Ω) → A1 (Ω) envoie le
sous-espa e A0c (Ω) dans A1c (Ω).


## Thuillier-tel-00010990v1 cache page 89

                                                                                                            75



Démonstration.
(i) C'est une onséquen e immédiate du théorème pré édent et de la dénition 2.3.1.
(ii) Il sut d'observer que, pour toute S - ourbe simplement semi-stable Y dont la bre gé-
nérique est un voisinage de x et toute fon tion Φ ∈ A0 (S(Y)), la fon tion ϕ = Φ ◦ τY a un
minimum lo al stri t au point x si et seulement si tel est la as pour Φ.
(iii) Étant donnée une fon tion ϕ ∈ A0c (Ω) dont le support est ontenu dans un domaine
k-analytique ompa t Y ⊂ X , il existe un sous-ensemble ni S de I(Y ) tel que ϕ|Y ∈ A0S (Y )
et le support de la mesure ddc ϕ est ontenu dans S .                                      2

Proposition 3.2.12.  Soit Ω ⊂ X un ouvert ; pour toutes fon tions lisses ϕ1 ∈ Ac (Ω)
                                                                                0

et ϕ2 ∈ A (Ω),
         0

                                     Z                             Z
                                                        c
                                             ϕ1 dd ϕ2 =                    ϕ2 ddc ϕ1 .
                                         Ω                             Ω


Démonstration. Supposant Ω onnexe, onsidérons un domaine stri tement k-analytique
 ompa t Y ⊂ Ω tel que :
   le support de ϕ1 soit ontenu dans Y − ∂Y si la ourbe Ω n'est pas propre,
   Y = Ω si la ourbe Ω est propre.
  Soient k′ /k une extension nie et Y une Spf(k′ ◦ )- ourbe simplement semi-stable telles qu'il
existe des fon tions Φ1 , Φ2 ∈ A0 (S(Y)) vériant Yη = Y ⊗k k′ et (ϕi )|Y ⊗k k′ = Φi ◦ τY , i = 1, 2.
Appliquant la proposition 1.2.13 et le théorème 3.2.10, il vient

                         Z                              Z
                                     c
                                 ϕ1 dd ϕ2 =                     ϕ1 ddc ϕ2
                             Ω
                                                        ZY
                                              =                    Φ1 ddc Φ2
                                                            S(Y)
                                                        Z
                                              =                    Φ2 ddc Φ1
                                                            S(Y)
                                                        Z                               Z
                                                                           c
                                              =                 ϕ2 dd ϕ1 =                  ϕ2 ddc ϕ1 .
                                                            Y                           Ω



                                                                                                             2

   Le omportement fon toriel de l'opérateur ddc s'obtient fa ilement à partir de sa dénition
et de la formule pré édente.

Proposition 3.2.13.  Soient X , Y                          deux ourbes stri tement k-analytiques lisses et p :
Y → X un morphisme.
  (i ) Le diagramme

                                                                ddc
                                                A0X                     / A1
                                                                                   X

                                               p∗                                  p∗
                                                                              
                                               p∗ A0Y                  / p∗ A 1
                                                                                   Y
                                                                ddc


## Thuillier-tel-00010990v1 cache page 103

                                                                                               89



          3.4. Fon tions sous-harmoniques et mesures de Radon positives
   Nous poursuivons dans ette se tion l'étude des fon tions sous-harmoniques sur une ourbe
stri tement k-analytique lisse X , dénies en 3.1.2, à l'aide de l'opérateur ddc . Les notations
introduites dans l'énon é de la proposition 3.3.7 seront librement employées.

3.4.1. Le théorème d'approximation.
   En vertu de la proposition 3.4.10, une fon tion sous-harmonique u sur X dénit une fon tion
réelle sur I(X) et détermine par onséquent un ourant dans D0 (X).
Lemme 3.4.1.  L'appli ation

                               SH(X) → D0 (X),         u 7→ u|I(X)
est inje tive et son image est l'ensemble des ourants T ∈ D0 (X) satisfaisant à la ondition
suivante :
              pour tout domaine k-anoïde V ⊂ X et tout point x ∈ I(V ) − ∂V ,
                                        T (x) ≤ hT, νxV i.
Démonstration. Soient u une fon tion sous-harmonique sur X et x un point dans X − I(X).
  Étant donnée une suite dé roissante (Vn ) de domaines k-anoïdes de X dont le bord de
Shilov Γ(Vn ) est réduit à un point xn et telle que
                                                 \
                                         {x} =      Vn ,
                                                  n

le prin ipe du maximum (proposition 3.1.11) implique les inégalités u|Vn ≤ u(xn ) ; la suite
(u(xn )) est don dé roissante et u(x) ≤ inf n u(xn ). D'autre part, en vertu de la semi- ontinuité
supérieure de u,
                              u(x) ≥ limsupn u(xn ) = inf u(xn ).
                                                         n
La fon tion u est ainsi uniquement déterminée par sa restri tion au sous-ensemble I(X) de
X.
  La des ription de l'image de l'appli ation SH(X) → D0 (X) est une appli ation dire te du
point (ii) du orollaire 3.3.9.                                                           2
  Le lemme pré édent nous permettra de ne pas distinguer une fon tion sous-harmonique sur
X du ourant de degré 0 qu'elle détermine.
   Une fon tion sous-harmonique sur une surfa e de Riemann est, lo alement, l'enveloppe in-
férieure d'une famille dé roissante de fon tions sous-harmoniques lisses ([19℄, Theorem 2.5.5).
Cette assertion est également vraie dans un ontexte non ar himédien, la démonstration en
étant qui plus est élémentaire.
Théorème 3.4.2.  Soient Ω un ouvert d'une           ourbe stri tement k-analytique lisse X et
u ∈ SH(Ω). Pour tout ouvert relativement ompa t Ω′ ⊂ Ω, la restri tion de u à Ω′ est
l'enveloppe inférieure d'une famille dé roissante de fon tions sous-harmoniques lisses.
Démonstration. On peut supposer que l'ouvert relativement ompa t Ω′ ⊂ Ω est de la forme
Y − ∂Y , Y ⊂ X étant un domaine k-analytique ompa t.
   Étant donné un sous-ensemble ni S ⊂ I(Y ) ontenant ∂Y , dé oule des propositions 3.1.19
et 3.1.20 l'existen e d'une unique fon tion uS appartenant à A0 (Y ), harmonique sur Y − S
et oïn idant ave u sur S .


## Thuillier-tel-00010990v1 cache page 104

90



   La sous-harmoni ité de u sur Y − S implique l'inégalité u|Y ≤ uS ; par suite, pour tout
sous-ensemble ni S ′ de I(Y ) ontenant S , uS majore uS ′ sur le bord S ′ de Y − S ′ et uS ′ ≤
uS , en vertu du prin ipe du maximum (proposition 3.1.1) appliqué aux fon tions uS et uS ′ ,
harmoniques sur Y − S ′ . La famille (uS )S est don dé roissante.
   La fon tion lisse uS est sous-harmonique sur Y −∂Y . Soient en eet V ⊂ Y −∂Y un domaine
k-anoïde et h une fon tion dans H(V ) qui majore uS sur ∂V . Puisque u|Y ≤ uS , h majore
a fortiori u sur ∂V , et don sur tout V par sous-harmoni ité ; omme u et uS oïn ident sur
S , il s'ensuit que h majore u sur le bord S ′′ = (S ∩ V ) ∪ ∂V de l'ouvert V − S ′′ . Une nouvelle
appli ation du prin ipe du maximum aux fon tions harmoniques h|V −S ′′ et (uS )|V −S ′′ fournit
alors l'inégalité
                                               uS ≤ h
sur V .
   La famille (uS )S  S par ourant l'ensemble ltrant des parties nies de I(Y ) ontenant
∂Y  est minorée en tout point de I(X) ; son enveloppe inférieure u est don une fon tion
sous-harmonique sur X (proposition 3.1.8). La démonstration s'a hève en invoquant le lemme
3.4.1 : les fon tions sous-harmoniques u et u|Y −∂Y , trivialement égales sur I(Y ) − ∂Y , sont
identiques.                                                                                  2
Remarque 3.4.3.  La démonstration i-dessus s'adapte aisément dans un ontexte ar hi-
médien et permet de démontrer un résultat d'approximation global pour les fon tions sous-
harmoniques sur une surfa e de Riemann (voir la proposition 4.2.14).
   La ara térisation des fon tions sous-harmoniques lisses est sans surprise.
Proposition 3.4.4.  Une fon tion lisse ϕ ∈ A (X) sur une ourbe stri tement k -
                                                       0

analytique lisse X est sous-harmonique si et seulement si ddc ϕ ≥ 0.
Démonstration. Soit ϕ une fon tion dans A0 (X) telle que ddc ϕ ≥ 0.
   Soient V ⊂ X un domaine k-anoïde et h une fon tion dans H(V ) qui majore ϕ sur ∂V ;
il est susant, pour prouver l'inégalité
                                            ϕ|V ≤ h,
d'établir que ϕ|V est majorée par la fon tion h′ dans H(V ) qui oïn ide ave ϕ sur ∂V ( ar
h′ ≤ h d'après le prin ipe du maximum).
   L'inégalité ddc (h′ − ϕ) = −ddc ϕ ≤ 0 sur V − ∂V implique que la fon tion h′ − ϕ n'a pas
de minimum lo al stri t sur V − ∂V ( orollaire 3.2.11, (ii)) ; elle atteint don son minimum
en un point de ∂V et, puisque (h′ − ϕ)|∂V = 0,
                                            ϕ|V ≤ h′ .
     La fon tion ϕ est ainsi sous-harmonique sur X .
   Soit ré iproquement ϕ ∈ A0 (X) une fon tion lisse et sous-harmonique. Étant donné un
point x du support S de ddc ϕ, onsidérons un domaine k-anoïde V ⊂ X tel que S ∩ (V −
∂V ) = {x} et soit h la fon tion h ∈ H(V ) qui est égale à ϕ sur S. La fon tion ϕ|V − h est
négative et elle s'annule identiquement sur ∂V .
   La forme lisse (ddc (ϕ− h))|V −∂V = (ddc ϕ)|V −∂V est, par hypothèse, non nulle et portée par
{x}. La première ondition implique l'existen e d'un minimum lo al stri t pour la fon tion
(ϕ − h)|V −∂V et elui- i est né essairement réalisé en un point y ∈ I(Y ) − ∂Y ar ϕ − h est
lo alement onstante en tout point de Y − I(Y ). On en déduit l'inégalité
                                         Z
                                             ddc ϕ > 0
                                           {y}


## Thuillier-tel-00010990v1 cache page 105

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


## GJR-2111.05741 cache page 8

8                             W. GUBLER, P. JELL, AND J. RABINOFF

  A space is compact if it is quasi-compact and Hausdorff. A paracompact space is a
Hausdorff space such that every open covering has a locally finite open refinement.
2.2. Non-Archimedean Fields. Throughout the whole paper, we fix a field K that is
complete with respect to a non-trivial non-Archimedean complete absolute value de-
noted | |: K → R. We will call this a non-trivially valued non-Archimedean field. A non-
Archimedean extension field is a non-Archimedean field K ′ equipped with an isometric
embedding K ,→ K ′ .
   We will make use of Temkin’s theory of graded residue fields introduced in [Tem04];
see also [Duc24, 2.2] and [Duc12, Section 0]. We use K  e to denote the ordinary residue
          e for the graded residue field. Beware that Temkin and Ducros use K
field and K •                                                                  e 1 for the
                           e for the graded residue field.
ordinary residue field and K
We will use the following notation concerning non-Archimedean fields.
        K A non-Archimedean field.
       | | : K → R, the absolute value on K.
     v( · ) = − log | · |, the associated valuation.
       K ◦ The valuation ring of K.
      K ◦◦ The maximal ideal in K ◦ .
        Ke = K ◦ /K ◦◦ , the residue field of K.
         Γ = v(K × ), the value group of K.
     Ke ≤r
            = {x ∈ K | |x| ≤ r} for r ∈ R.
     Ke <r = {x ∈ K | |x| < r} for r ∈ R.
       er = K
       K      e ≤r /K
                    e <r .
              L
       e • = r∈R K
       K             e r , the graded residue field.
 e(L/K) = [|L | : |K × |], the ramification index of a field extension.
                 ×

 f (L/K) = [eL : K e ], the residue degree.
We have
(2.2.1)                         [eL • : K
                                        e • ] = e(L/K) f (L/K)
by [Duc24, 2.2.27.1]. The left hand side is defined as the dimension of eL • as a graded K
                                                                                         e •-
vector space, which is the cardinality of any basis as in ordinary linear algebra [Duc24,
2.2.16].
2.3. Non-Archimedean geometry. We will use Berkovich analytic spaces as defined
in [Ber93]. We are mainly concerned with good analytic spaces X over a non-trivially
valued non-Archimedean field K. These are the analytic spaces considered in [Ber90], so
this book is our main reference for non-Archimedean geometry. Here, good means that
every x ∈ V has a neighbourhood isomorphic to the Berkovich spectrum M (A ) of an
affinoid algebra A .
   When considering strictly analytic spaces, we will always use the G-topology generated
by the strictly affinoid domains [Ber93, 1.3]. This is most natural for comparison to rigid
analytic geometry: see [Ber93, 1.6].
We will use the following notation concerning Berkovich analytic spaces. Let X be an
analytic space and let A be a K-affinoid algebra.


## GJR-2111.05741 cache page 31

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


## GJR-2111.05741 cache page 32

32                              W. GUBLER, P. JELL, AND J. RABINOFF

   At this point we assume that the reader is familiar with formal geometry as recalled
in 2.4. We give an interpretation of Λ-PL functions in terms of formal geometry which
we will use to prove some more subtle properties of piecewise Λ-linearity. Recall that
a formal K ◦ -model of a paracompact strictly K-analytic space X is an admissible formal
scheme X over K ◦ equipped with an identification Xη = X .

     A frame of a line bundle on an open set is a nowhere vanishing section.

5.5 (Functions from Formal Models of OX ). We assume now that X is paracompact. This
allows us to use Raynaud’s theory of formal K ◦ -models, as in 2.4. We will later apply
this only locally on a good, strictly analytic space, where we can always find a compact
strictly analytic neighbourhood (even a strictly affinoid neighbourhood as X is good).
Hence the reader loses nothing by assuming here and in the following that X is compact.
(Paracompactness has the advantage that one can apply these considerations also to the
analytification of algebraic varieties over K.)
   Let X be a formal K ◦ -model of X . The isomorphism classes of line bundles L on X
equipped with an identification Lη = OX form an abelian group denoted by M (X). Then
L ∈ M (X) determines a canonical metric k kL on OX , defined as follows: if s is a frame of
L over a formal open subset U ⊂ X, then we set ksk = 1 on Uη . This metric is well-defined
because any two frames differ by a unit with constant absolute value 1.
   Equivalently, we get a canonical function hL = − log k1kL : X → R with − log k f kL =
− log | f |+hL for an analytic function f on any open subset U of X . If U = Uη for a formal
open subset U of X and if f ∈ Γ (U, L) ⊂ Γ (Uη , OX ) is a frame of L, then by definition
0 = − log | f | + hL , so hL is PL because X has a G-cover by such U = Uη .

5.6 (PL Functions are Model Functions). If X is paracompact, then [GM19, Proposi-
tion 2.10] yields that h: X → R is PL if and only if there exists a formal K ◦ -model (X, L)
of (X , OX ) such that h = − log k1kL .

5.7 (Λ-PL Functions from Formal Models). For paracompact X , we extend 5.6 to the
case of Λ-PL functions as follows. Choose a formal K ◦ -model X of X , and set M (X)Λ :=
M (X)⊗Z Λ. We have a unique homomorphism h: M (X)Λ −→ C(X ), written        Pm L 7→ hL , such
that hλL =P   −λ log k1kL for all L ∈ M (X) and λ ∈ Λ. Note that if L = i=1 λi Li ∈ M (X)Λ
                m
then hL = i=1 λi hLi ∈ PLΛ (X ) by 5.2(5).
   If f : X′ → X is a morphism of formal K ◦ -models of X , then h f ∗ L = hL for all L ∈ M (X)Λ .
More generally, if f : X′ → X is any morphism of separated admissible formal schemes
then h f ∗ L = hL ◦ fη for all L ∈ M (X)Λ . (See 2.4 for separatedness of formal models.)
   For L ∈ M (X)Λ , we get a unique continuous metric k kL on OX defined by − log k f kL =
− log | f | + hL for an analytic function f on any open subset U of X .

   We want to extend the result of 5.6 locally in the analytic topology to Λ-coefficients as
in 5.7. To do this we need to show that a Λ-PL function is locally in the analytic topology a
linear combination of PL functions with Λ-coefficients. (For our purposes, we could have
taken the statement of Proposition 5.8 as the definition of Λ-PL; we chose Definition 5.1
because it is more compatible with the terminology in the literature.)


## GJR-2111.05741 cache page 33

                 FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             33

Proposition 5.8. Suppose that Λ = Z or that Λ is divisible. A function h: X → R is Λ-
       Pm only if for every x ∈ X , there exists an open neighbourhood U of x such that
PL if and
h|U = i=1 λi hi for finitely many λ1 , . . . , λm ∈ Λ and h1 , . . . , hm ∈ PL(U).
  Before proving the proposition, we state the desired corollary.
Corollary 5.9. Suppose that Λ = Z or that Λ is divisible. A real function h: X → R is Λ-PL
if and only if for every point x ∈ X , there exists a compact strictly analytic neighbourhood
U of x, a formal K ◦ -model U of U, and L ∈ M (U)Λ , such that h|U = hL . In this case, such a
neighbourhood U can be chosen arbitrarily small.
Proof.
     PmSuppose that h is Λ-PL. By Proposition 5.8, after shrinking X , we may assume that
h = i=1 λi hi for λ1 , . . . , λm ∈ Λ and PL functions h1 , . . . , hm : X → R. Since every point of
X has a compact strictly analytic neighbourhood, we may also assume that X is compact.
By 5.6, for each i there is a model (Xi , Li ) of (X , OX ) such that hi = hLi . Finding a model X
                                                                              Pm
dominating
       Pm    all X i , we may   assume  all X i = X. Then  h  =  h  L for L =     λ L . Conversely,
                                                                               i=1 i i P
                                                                                         m
if L = i=1 λi Li on U for λ1 , . . . , λm ∈ Λ and L1 , . . . , Lm ∈ M (U) then hL = i=1 λi hLi is
Λ-PL by 5.2(5). We can choose U sufficiently small because U can be taken arbitrarily
small in Proposition 5.8.                                                                         
  We will use the following lemma in the proof of Proposition 5.8; we will use it again
several times.
Lemma 5.10. Suppose that Λ is a divisible additive subgroup of R. Let P be an abelian
group, and let x 1 , . . . , x r ∈ Λ ⊗Z P be a finite collection of elements. Then P            there is a Q-
                                                                                                   n
linearly independent subset {λ1 , . . . , λn } ⊂ Λ such that each x i has the form j=1 λi ⊗ x i j
for x i j ∈ P.
                       P mi
Proof. Write x i = j=1        λi j ⊗ yi j . Let λ1 , . . . , λn be a basis of the Q-subspace of Λ generated
by the λi j . Since Λ is divisible, we may assume that every λi j is a Z-linear combination of
                                                 P mi
λ1 , . . . , λn . Expanding λi j in the sum j=1            λi j ⊗ yi j and rearranging proves the lemma. 
Proof of Proposition 5.8. The “if” direction is trivial because a covering by open sets is a
G-covering. Suppose then that h is Λ-PL. If Λ = Z then h is itself PL, so we may assume
Λ is divisible. Fix x ∈ X , and replace X by a compact strictly analytic neighbourhood of
x to assume X is compact.PChoose a G-covering {X i }i∈I of X by compact strictly analytic
                              mi
domains such that h|X i = j=1    λi j log | f i j | for finitely many λi j ∈ Λ and f i j ∈ O (X i )× . We
may assume that every X i contains x and that I is a finite set. By Lemma 5.10, there
are Q-linearly
       Pm       independent elements λ1 , . . . , λm ∈ Λ such that for every i ∈ I, we have
h|X i = k=1 λk hik with hik = log |g ik | for g ik ∈ O (X i )× .
  We claim that there is a neighbourhood U of x such that for all i, j ∈ I and all y ∈
U ∩ X i ∩ X j we have
(5.10.1)                         hik ( y) − hik (x) = h jk ( y) − h jk (x).
To prove this, we pick i, j ∈ I, set X i j := X i ∩ X j and consider the smooth tropicalization
map H i j : X i j → R2m given by y 7→ (hik ( y), h jk ( y))k=1,...,m . By 3.2 and 3.3, the tropical
variety of the germ (X i j , x) is the germ at H i j (x) of a finite union of (Z, Γ )-polytopes ∆.


## GJR-2111.05741 cache page 34

34                                     W. GUBLER, P. JELL, AND J. RABINOFF

Choosing them sufficiently small, we may       S assume every ∆ is contained in H i j (X i j ). It is
enough to show (5.10.1) for y ∈ Ui j := ∆ H i−1         j
                                                          (∆) as Ui j is a neighbourhood of x in X i j ,
hence has the form U ∩ X i j for a neighbourhood U of x in X .
  We fix i, j ∈ I and pick a polytope ∆ as above. Since ∆ is a Z-polytope, the set (H i j (x)+
Q2m ) ∩ ∆ is dense in ∆. By construction, there are coordinate functions ℓik , ℓ jk of R2m
such that hik = ℓik ◦ H i j and h jk = ℓ jk ◦ H i j . Hence it is enough to show (5.10.1) for all
y ∈ X i j with H i j ( y) ∈ ∆ and with ω = H i j ( y) − H i j (x) ∈ Q2m . Using
                        X                X                X                X
                0=         λk hik ( y) −   λk h jk ( y) −     λk hik (x) +     λk h jk (x)
                        k                   k                    k                      k
                        X                                                      
                   =         λk hik ( y) − hik (x) − h jk ( y) + h jk (x)
                         k

and hik ( y) − hik (x) − h jk ( y) + h jk (x) = ℓik (ω) − ℓ jk (ω) ∈ Q, the Q-linear independence
of λ1 , . . . , λm yields (5.10.1) for all such y. This finishes the proof of the claim.
    Let us fix i ∈ I. We deduce from (5.10.1) that there are constants ci jk such that hik =
h jk + ci jk on U ∩ X i j for all j ∈ I and k = 1, . . . , m. Evaluating at a rig-point of U ∩ X i j , we
                    p
see that ci jk ∈ Γ . Replacing h by an integer multiple, we may assume ci jk = −v(γi jk ) ∈ Γ
for some γi jk ∈ K × . We conclude that γi jk g jk is an invertible function on X j . We claim
that there is a unique piecewise linear function hk : U → R that agrees with log |γi jk g jk | =
ci jk +h jk on U ∩X j for every j ∈ I. To see that the functions ci jk +h jk indeed glue, we know
from (5.10.1) that they agree on intersections up to constants and the claim follows as
ci jk + h jk (x) = hik (x) does not depend on j ∈ I. We note that
                     X                        X                  X                      
                         λk h jk (x) = h(x) =    λk hik (x) =       λk h jk (x) + ci jk
                    k                                 k                    k
             P
and hence        k λ k c i jk = 0. For y ∈ U ∩ X j , we deduce that
                             X                    X                    X                X
                 h( y) =         λk h jk ( y) =       λk h jk ( y) +       λk ci jk =       λk hk ( y)
                             k                    k                    k
                   P
and hence h =           λk hk on U. This proves the proposition.                                         
  With these foundations in place, we can use formal models to show that piecewise
Λ-linearity can sometimes be checked after pull-back, at least when Λ is divisible.
Proposition 5.11. Let f : X ′ → X be a finite, flat, surjective morphism of good strictly K-
analytic spaces. Suppose that Λ is divisible. If h: X → R is a function and h′ = h ◦ f , then
h ∈ PLΛ (X ) if and only if h′ ∈ PLΛ (X ′ ).
Proof. By Lemma 5.4(1), we only need to show that if h′ is Λ-PL then so is h. By [Ber93,
Proposition 3.2.7], the map f is open. Let x ∈ X , choosePx ′ ∈ X ′ mapping to x, and
                                                                  m
let U ′ be an open neighbourhood of x ′ such that h′ |U ′ = i=1 λi h′i for λ1 , . . . , λm ∈ Λ
and h′1 , . . . , h′m ∈ PL(U ′ ). Such a neighbourhood exists by Proposition 5.8. By [Ber93,
Lemma 3.1.2, Definition 3.2.5], after shrinking U ′ , the morphism f |U ′ : U ′ →Pf (U ′ ) is
                                                                                        m
finite and flat. Thus we may replace X ′ by U ′ and X by f (U ′ ) to assume h′ = i=1 λi h′i
on X ′ . Shrinking further, we may assume X and X ′ are compact. By 5.6, each PL function
h′i is induced by a line bundle on a formal model of X ′ . Passing to a dominating formal


## GJR-2111.05741 cache page 35

                FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                                         35

model, we may assume that there is a formal K ◦ -model X′ of X ′ and L′i ∈ M (X′ ) such
that h′i = hL′i for each i.
   Using Raynaud’s theorem [Bos14, Theorem 8.4.3, Lemma 8.4.4], after passing to an
admissible formal blowup, we can extend f to a morphism f : X′ → X for some for-
mal K ◦ -model X of X . By [BL93b, Theorem 5.2, Corollary 5.3(b)], after passing to
admissible formal blowups of X and X′ , we may assume f : X′ → X is flat and quasi-
finite. By [Tem00, Corollary 4.4] the morphism f : X′s → Xs is proper, so it is finite; by
Nakayama’s lemma, the morphism f : X′ → X is finite. Working locally, we may thus
assume X = Spf(A) and X′ = Spf(A′ ) are formal affines, with X connected. Then A′ is a
finite, flat A-module, which is locally of finite presentation by [Bos14, Theorem 7.3.4],
so it is a locally free A-module of some constant rank n by [Sta21, Lemma 02KB]. Thus
we can define the norm N (L′ ) of a line bundle L′ on X′ as in [EGAII, 6.5]. This is a line
bundle on X and a model of OX⊗n = OX , so we get a homomorphism N : M (X′ ) → M (X).
Tensoring with Λ, we have an induced homomorphism N : M (X′ )Λ → M (X)Λ .
   Now we can transfer the considerations in [BE21, 8.5] to the analytic setting. For
L′ ∈ M (X′ ) and x ∈ X , we claim that
                                                Y         my
(5.11.1)                        k1(x)kN (L′ ) =    k1( y)kL′ ,
                                                                 y7→ x

where m y = dimH (x) (O f −1 (x), y ) is the multiplicity of y in f −1 (x). With this in place, letting
L = N (L′ ), it follows that
                                                  X
                                         hL (x) =     m y hL′ ( y).
                                                             y7→ x

Extending by linearity,
                     Pmthe above      equation holds for L′ ∈ M (X′ )Λ and L = N (L′ ) ∈
                   ′
M (X)Λ . Letting L = i=1 λi Li and L = N (L′ ), we have h′ = hL′ , and for x ∈ X we have
                               ′

                     X                 X                         X
            hL (x) =    m y hL′ ( y) =     m y h ◦ f ( y) = h(x)   m y = n h(x).
                          y7→ x                      y7→ x                                 y7→ x

It follows that h = hn−1 L is Λ-PL.
   It remains to prove (5.11.1). Let x ∈ X , and let y1 , . . . , yr be the points of f −1 (x). Let
R j := O f −1 (x), y j , let F := H (x), and let m j := dim F (R j ) = m y j . We have the decomposi-
                                 Q
tion R := O ( f −1 (x)) =          j R j into local Artinian rings. Working locally on X = Spf(A),
by [Sta21, Lemma 0BUT] we may assume that L′ is trivial over X′ = Spf(A′ ). Choose a
frame s′ for L′ and let γ = 1/s′ ∈ (A′ ⊗K ◦ K)× , so k1kL′ = |γ| on X ′ . The norm s := N (s′ )
is a frame of N (L), and 1/s = NA′ /A(γ) ∈ (A ⊗K ◦ K)× , so
                                  k1(x)kN (L′ ) = |NA′ /A(γ)(x)| = |NR/F (γ)|.
Let K j be the residue field of R j , let γ j be the image of γ in R j , and let γ j be the residue
class in K j . A Jordan–Hölder argument (see [Ser97, 2.1c, p.9]) shows that NR j /F (γ j ) =
NK j /F (γ j )[R j :F ]/[K j :F ] . Since the canonical valuation on H ( y j ) extends the canonical valu-
ation on the complete non-archimedean field F = H (x), we have
                 |γ( y j )|[K j :F ] = |γ j |[K j :F ] = |NK j /F (γ j ))| = |NR j /F (γ j )|[K j :F ]/[R j :F ] .


## GJR-2111.05741 cache page 36

36                               W. GUBLER, P. JELL, AND J. RABINOFF

Putting all these together, we deduce
                                     Y                    Y                 Y           mj
        k1(x)kN (L′ ) = |NR/F (γ)| =   |NR j /F (γ j )| =   |γ( y j )|m j =   k1( y j )kL′ .
                                        j                   j                j

This proves the claim in (5.11.1) and hence the proposition.                                      
     Proposition 5.11 gives the following variant of Lemma 5.4(2).
Corollary 5.12. Let X be a good strictly K-analytic space, let K ′ be the completion of an
algebraic field extension of K, let X ′ = X ⊗
                                            b K K ′ , and let π: X ′ → X be the structure morphism.
Suppose that Λ is divisible. If h: X → R is a function and h′ = h ◦ π, then h ∈ PLΛ (X ) if and
only if h′ ∈ PLΛ (X ′ ).
Proof. By Lemma 5.4(2), we only need to show that if h′ is Λ-PL then so is h. When K ′
is a finite extension of K then this is a special case of Proposition 5.11. We reduce to this
case as follows.
    Since piecewise Λ-linearity is a local property in the analytic topology, we may assume
that X is compact. Then X ′ is also compact, so by Proposition 5.8 there are finitely many
                                       ′
compact strictly analytic domains UP   i
                                         such that the interiors Vi′ of the Ui′ cover X ′ and such
that hi := h |Ui′ has the form hi = j λi j h′i j for finitely many h′i j ∈ PL(Ui′ ) and λi j ∈ Λ.
        ′      ′                   ′

By [GM19, Propositions 2.7 and 2.10], the functions h′i j extend to PL functions on X ′ .
                                                                           P
We denote the extensions also by h′i j leading to an extension j λi j h′i j of h′i which we
denote also by h′i . By [GM19, Proposition 2.18(b)], there is a finite subextension F /K of
K ′ /K such that for all i, j, there are PL functions hi j on X F := X ⊗KPF whose pull-backs
to X ′ agree with hi j . Then the pull-back of the Λ-PL function hi := j λi j hi j agrees with
h′i on X ′ . As seen at the beginning, it is enough to show that the pull-back of h to X F is
Λ-PL, so we may replace K by F and X by X F . Piecewise Λ-linearity is a local property, so
we show it in a neighbourhood of any y ∈ X . It follows from [Ber90, Proposition 1.3.5,
Corollary 1.3.6] that the structure map p : X ′ → X is open and surjective, and hence the
sets p(Vi′ ) form an open covering of X . For y ∈ X , we choose i such that y ∈ p(Vi′ ). For
all x ′ ∈ Vi′ and x = p(x ′ ), we have h(x) = h′ (x ′ ) = h′i (x ′ ) = hi (x), proving that h is Λ-PL
on the neighbourhood p(Vi′ ) of y.                                                                 
Corollary 5.13. Suppose that Λ is divisible. Let L/K be a (potentially infinite) normal
extension with automorphism group G := Aut(L/K). Let K ′ be the completion of L and let
X ′ := X ⊗
         b K K ′ , with structure morphism π: X ′ → X . Then h 7→ h◦π induces an isomorphism
          ∼
PLΛ (X ) −→ PLΛ (X ′ )G , where PLΛ (X ′ )G is the space of G-invariant Λ-PL functions on X ′ .
Proof. By [Ber90, Proposition 1.3.5, Corollary 1.3.6], we have X = X ′ /G, so the claim
follows from Corollary 5.12.                                                          

                 6. REDUCTION OF GERMS AND RESIDUES OF PL FUNCTIONS
   We will characterize semipositive and harmonic functions in 7 in the language of
Temkin’s theory of reductions of germs [Tem00], using residues of line bundles with
piecewise linear metrics from [CD12, Section 6]. In this section, we recall the theory
following quite closely [CD12, 6.1], and prove then the preliminary results we need.


## GJR-2111.05741 cache page 45

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


## GJR-2111.05741 cache page 46

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


## GJR-2111.05741 cache page 47

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


## GJR-2111.05741 cache page 76

76                                W. GUBLER, P. JELL, AND J. RABINOFF

suitable non-zero integer m, weQ may assume that h is Z-harmonic and is hence a harmonic
                                         nµ
tropicalization map. Let pµ :      µ∈R R    → Rnµ be the projection to the µ-th factor. It
                                                                S
follows from (14.2.2) that the restriction of pµ∗ (α′µ ) to h′ ( ρ∈R U ρ ) is independent of the
choice of µ. For any µ ∈ R, this shows that the weakly smooth form ω := h∗ (pµ∗ (α′µ)) on
U satisfies π∗ (ω) = ω′ , proving surjectivity and hence the Proposition.                     
  The Galois action on forms respects the differential graded algebra structure on A(X ),
so it induces an action on the Dolbeault cohomology groups H p,q (X ).
Corollary 14.3. We have H p,q (X ) ∼
                                   = H p,q (X ′ )G .
Proof. Since higher cohomology groups of a finite group are torsion [Ser68, Proposi-
tion VII.6], it is clear that W → W G is an exact functor on the category of R-vector spaces
with G-action. We conclude that the fixed point sets of the Dolbeault complex (13.2.1)
for X ′ compute H p,q (X ′ )G , so the claim follows from Proposition 14.2.               
14.4 (Galois Action on Piecewise Smooth Forms). In the same way as 14.1, we can de-
fine the G-action on the sheaf A•,•
                                  ps
                                     of piecewise smooth forms on X . It is clear that
Proposition 14.2 holds also for piecewise smooth forms. By construction, this G-action
is compatible with the G-action on the subsheaf A•,• of weakly smooth forms.
Proposition 14.5. Let X be a good d-dimensional strictly analytic space X over K, let K ′ /K
be a finite Galois extension with Galois group G, and let X ′ be the base change of X to K ′ .
                                       R          R
                    d,d
    (1) For ω ∈ Aps,c   (X ), we have X ′ π∗ (ω) = X ω.
                                                  R              R
    (2) For ω′ ∈ Aps,c
                     d,d
                         (X ′ ) and σ ∈ G, we have X ′ σ∗ (ω′ ) = X ′ ω′ .
Proof. Suppose first that X is compact and that ω is a piecewise smooth preform given
by a PL tropicalization h: X → Rn and a Lagerberg form α ∈ A p,q (h(X )) with h∗ (α) =
ω. Then π∗ (ω) is a piecewise smooth preform on X ′ given by the PL tropicalization
h′ := h ◦ π: X ′ → Rn . Using that h′ (X ′ )d = h(X )d as weighted polytopal complexes by
                                 ′ ∗           ∗ ∗             ∗
Proposition 8.11 andR that (h ) (α) = π (h (α)) = π (ω), it is clear that both integrals in
(1) coincide with h(X ) α. Proposition 11.1 then yields (1) in general.
                          d
   To prove (2), we choose a finite covering (X i′ )i∈I of supp(ω′ ) by compact strictly ana-
lytic domains X i′ such that ω′ |X i′ = h∗i (α′i ) for some α′i ∈ Aps
                                                                   d,d
                                                                       (h(X i′ )) and a piecewise linear
tropicalization hi : X i′ → Rni . Then the compact strictly analytic domains σ−1 (X i′ ) cover
the support of σ∗ (ω′ ), and the restriction of σ∗ (ω′ ) to σ−1 (X i′ ) is given by (σ ◦ hi )∗ (α′i ).
By Proposition 11.1(3), we have
                              Z                        Z          Z
                                               σ∗ (ω) =                α′i =          ω.
                                 σ−1 (X i′ )              hi (X i′ )           X i′

The integrals in (2) can be computed by the inclusion-exclusion formula (11.1.1) as in
the proof of Proposition 11.1, so (2) follows.                                      
                             15. HARMONIC FUNCTIONS ON CURVES
                                                                                  p
   Let K be a non-Archimedean field with nontrivial value group Γ ⊂ R, and let Γ :=
{t ∈ R | ∃k ∈ N>0 such that kt ∈ Γ } be the divisible hull. We will show that our notion


## GJR-2111.05741 cache page 77

              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                77

of harmonic functions introduced in Section 7 agrees in the case of a rig-smooth curve
with the harmonic functions in Thuillier’s thesis [Thu05]. This will be important in the
companion paper [GJR21].
   First, we recall some notions from the theory of graphs and their relationship to the
structure of non-Archimedean analytic curves. For more details, we refer to [GJR21].

15.1 (Metric Graphs with Boundary). We consider a weighted metric graph (Σ, ∂ Σ) with
boundary. This is a finite multigraph with no loop edges endowed with positive edge
lengths assumed to be in Γ . The boundary ∂ Σ is any subset of the vertices of Σ. Every
edge is endowed with the additional datum of a weight w(e) ∈ Z>0 . If we ignore the
boundary, then we get a compact piecewise (Z, Γ )-linear space of dimension at most 1 as
introduced in 2.5. (Note that isolated vertices are allowed.)
   A function h: Σ → R is called harmonic if the restriction
                                                        P         of h to any edge is affine
R-linear, and if for any vertex x of Σ \ ∂ Σ, we have e− =x w(e)de (h) = 0, where e ranges
over all edges with tail vertex x and de (h) is the outgoing slope of h at x in the direction
of e.
   For a subgroup Λ of R containing Γ , we let Σ(Λ) denote the subset of Σ consisting of
all points x such that f (x) ∈ Λ for all (Z, Γ )-linear functionspf on an edge e containing
x. Let U ⊂ Σ be a subgraph with vertices contained in Σ( Γ ). A function h: U → R
is called piecewise (Z, Γ )-linear if there
                                        p is a subdivision of the subgraph U such that the
vertices of the subdivision are in Σ( Γ ) and such that the restriction of h to any edge e
of the subdivision extends to a (Z, Γ )-linear function on the edge of Σ containing e.

15.2 (Skeletons of Curves). Metric graphs with boundary arise in non-Archimedean ge-
ometry as follows. Let X be a compact rig-smooth curve over K, i.e., a compact rig-smooth
strictly analytic space of pure dimension 1. We assume that X has a strictly semistable
model X over the valuation ring K ◦ . This is a formal K ◦ -model of X (see 2.4) whose spe-
cial fiber Xs is geometrically reduced with smooth irreducible components and at most
double points as singularities. This is equivalent to [Thu05, Definition 2.2.8], where
such models are called simplement semi-stable. To such a model is associated a weighted
metric graph with boundary Σ := S(X), called the skeleton of X. There is a canonical
inclusion Σ ,→ X . The vertices of Σ correspond to the irreducible components of Xs and
the edges correspond to the singular points of Xs , so that Σ is the incidence graph of Xs .
The boundary ∂ Σ consists of the vertices of Σ corresponding to non-proper irreducible
components of Xs . If x ∈ Xs is a singular point with corresponding edge e, then the
weight of e is defined to be w(e) = [Ke (x) : K
                                              e ]. There is an étale neighbourhood of x of
the form Spf(K{X , Y }/(X Y − ̟)) for some ̟ ∈ K ◦◦ \ {0}; the length of e is then defined
to be v(̟). There is a canonical deformation retraction map τ: X → S(X).

15.3 (Subdivisions of the Skeleton). Consider
                                      p         a subdivision Σ′ of the skeleton Σ = S(X)
such that all vertices of Σ′ are in Σ( Γ ). Vilsmeier [Vil21, Construction 2.6] has de-
fined a canonical formal scheme X′ with generic fiber X and reduced special fiber, and a
canonical morphism ι : X′ → X extending IdX , such that for any edge e′ of Σ′ , the analytic
subdomain (τ)−1(e′ ) of X is the generic fiber of an open subset of X′ . Note that X′ is not
necessarily an admissible formal scheme, i.e. not necessarily of topologically finite type.


## GJR-2111.05741 cache page 78

78                             W. GUBLER, P. JELL, AND J. RABINOFF

By [Gub13b, Propositions 6.7 and 6.9], the formal scheme X′ is admissible if the value
group Γ is discrete or if the vertices of Σ′ are contained in Σ(Γ ).
15.4 (Piecewise Affine Functions on the Skeleton).
                                             p         Let Σ = S(X) as in 15.2, let U be a
subgraph of Σ with vertices contained in Σ( Γ ), and let h: U → R be a piecewise (Z, Γ )-
linear function in the sense of 15.1. Passing to a subdivision of U, we may assume that
h is (Z, Γ )-linear on each edge of U. The vertices of U induce a subdivision Σ′ of Σ; we
denote the associated formal K ◦ -model of X by X′ as in 15.3, with canonical morphism
ι : X′ → X. When Γ dense in R, we assume that all vertices of U are in Σ(Γ ); then
X′ is an admissible formal scheme. The subset Y := τ−1 (U) is the generic fiber of a
unique open formal subscheme Y′ in X′ . By the arguments used in the proof of [Vil21,
Proposition 2.11], there is a canonical vertical Cartier divisor D on Y′ with associated
formal metric on OY determined by − log k1kO (D) = h ◦ τ. See 5.5.
Proposition 15.5. Let X be a compact rig-smooth curve over K and let h: X → R.
     (1) If X is a strictly semistable model of X over K ◦ , then h = hL for a line bundle
         L ∈ M (X) if and only if there is a function f : S(X) → R which is (Z, Γ )-linear on
         each edge such that h = f ◦ τ.
     (2) If x ∈ ∂ X , then h is harmonic at x if and only if h is R-PL at x.
Proof. The “if” part in (1) follows from 15.4. Conversely, assume that h = hL for L ∈
M (X). Using the identification L|X = OX , the meromorphic section 1 of L induces a
vertical Cartier divisor D on X. There is a covering of X by open subsets U such that S(U)
is either an edge or a vertex of S(X) and such that D|U = div(γ) for some γ ∈ O (U)×,
where U = Uη . It follows from [Ber99, Theorem 5.3 and Step 13 in its proof] that
h|U = − log |γ| factorizes through a (Z, Γ )-linear function on S(U). This proves (1).
   Since x ∈ ∂ X , the curve ∂ X is affine and hence the nef condition in Proposition 7.1 is
vacuous. This proves (2).                                                                 
15.6 (Thuillier’s Harmonic Functions). We consider now an arbitrary rig-smooth curve
X over K. We call a function h: X → R harmonic in the sense of Thuillier if every x ∈ X
has a strictly affinoid neighbourhood V , a finite Galois extension K ′ /K, and a strictly
semistable model V′ of V ′ := V ⊗K K ′ , such that the pullback h′ of h|V factorizes through
the skeleton S(V′ ) and such that h′ |S(V′ ) is a harmonic function on the skeleton S(V′ )
considered as a weighted metric graph with boundary as in 15.2.
   For x ∈ ∂ X , Proposition 15.5 and Corollary 5.12 show that the above harmonicity
condition at x is equivalent to piecewise R-linearity at x, using that the boundary of
S(X) is ∂ X . Note that Thuillier [Thu05, Section 2.3] used this definition only for strictly
affinoid or boundaryfree X , so the above definition is slightly more general than his.
Proposition 15.7. Let X be a rig-smooth curve. Then a function h: X → R is harmonic in
the sense of Definition 7.2 if and only if h is harmonic in the sense of Thuillier.
Proof. The claim is local on X , so we may assume X strictly affinoid. We first show
that the harmonicity notions agree for a piecewise linear function h ∈ PL(X ). By 5.6,
we have that h = − log k1kL for a model L of OX on a formal K ◦ -model X of X . Using
base change, Proposition 7.6 and [Thu05, Remarque 2.3.17], we are free to pass to a


## GJR-2111.05741 cache page 79

              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                79

finite Galois extension of K. Arguing locally, the semistable reduction theorem ([Thu05,
Théorème 2.3.8] under these hypotheses; see also [BL85, Section 7] and [Duc24, Theo-
rem 5.1.14(iv), 6.1.3]) shows that we may assume that X is a strictly semistable model.
By Proposition 15.5, there is a function f on the skeleton S(X) which is (Z, Γ )-linear on
each edge such that h = f ◦ τ. For x ∈ S(X) \ ∂ X with corresponding proper irreducible
component C := redX (x) of Xs , it follows as in [KRZB16, Theorem 2.6] that the sum of
outgoing slopes of f at x is equal to deg(L|C ). We conclude that h is harmonic in the
sense of Thuillier if and only if L is numerically equivalent to 0. The latter is equivalent
to harmonicity of h in the sense of Definition 7.2, as we have shown in Lemma 7.4.
   Now we prove the proposition for any function h: X → R. Assume that h is a harmonic
function on X as in Definition 7.2. By Proposition 7.5, the function h is locally an R-linear
combination of Z-harmonic functions, so we are reduced to the case handled above since
the set of Thuillier-harmonic functions forms a real vector space.
   Conversely, let h be a harmonic function in the sense of Thuillier. We have to check
for any x ∈ X that h is harmonic at x. As above, we are free to pass to a finite Galois
extension of X , so we may extend scalars and shrink X to assume that X has a strictly
semistable model X and that h factorizes through a harmonic function f : S(X) → R. It
is enough to show that f is an R-linear combination of piecewise (Z, Γ )-linear harmonic
functions f i on S(X). Indeed, by Proposition 15.5, we have that f i ◦ τ is piecewise linear,
so f i ◦ τ is harmonic by the the first paragraph of this proof, and hence h is harmonic.
   Suppose first that x ∈ ∂ X = ∂ S(X). After shrinking X, we may assume that S(X)
is a star around the vertex x, so that f is affine R-linear on each edge. Translating by
a constant function, we may assume f (x) = 0. Then f is an R-linear combination of
piecewise Z-linear functions f e on S(X): namely, the functions f e that have slope 1 on a
given edge e and slope 0 on the others. Since x ∈ ∂ S(X), Proposition 15.5 yields that
each f e is harmonic and hence h is harmonic.
   If x ∈ X \ ∂ X , then as above, we may assume that S(X) is either an edge containing
τ(x) in its interior, or that S(X) is a star around the vertex τ(x). In the first case, f is
an R-multiple of a (Z, Γ )-linear function on the edge, so h is harmonic. In the second
case, we may assume that f (τ(x)) = 0. Then f is harmonic if and only if f is linear on
each edge and the weighted sum of the outgoing slopes at τ(x) is zero. This is a linear
equation for the slopes which is defined over Q, so there is a basis of solutions defined
over Q and even over Z. The elements f i of such a basis induce piecewise (Z, Γ )-linear
functions f i which are harmonic on S(X). Since f is an R-linear combination of the f i ,
we have that h is harmonic.                                                                

   Note that Γ is either dense inpR or is a discrete subgroup. In the following, we set
Λ := Γ if Γ is dense and Λ := Γ (the divisible hull in R) if Γ is discrete. When Γ is
discrete, we may rescale the valuation to assume Γ = Z.

15.8. Let X be a compact rig-smooth curve over K with strictly semistable model X. As
in 15.2, the skeleton S(X) is viewed as a weighted metric graph with boundary. Let U
be a subgraph of Σ := S(X) with vertices contained in Σ(Λ), then τ−1 (U) is a compact
strictly analytic domain in X .


## GJR-2111.05741 cache page 80

80                              W. GUBLER, P. JELL, AND J. RABINOFF

Proposition 15.9. With the notation above, let f : U → R be a piecewise (Z, Γ )-linear
harmonic function as in 15.1. Then h := f ◦ τ: τ−1 (U) → R is Z-harmonic.
Proof. Replacing U be a subdivision, we may assume that f is affine (Z, Γ )-linear on each
edge. The vertices of U induce a subdivison of S(X) and hence 15.3 yields a canonical
formal K ◦ -model X′ of X over X. By 15.4, we get a canonical open formal subscheme Y′ of
X′ with generic fiber Y = τ−1 (U). It follows from 5.6 and 15.4 that h is piecewise linear,
so by definition, it is Z-harmonic if and only if it is harmonic. After a finite, separable
extension of the ground field, the graph U becomes a skeleton of Y with respect to some
strictly semistable model (see Remark 5.3.6 in [GJR21]). Thus h is harmonic in the sense
of Thuillier, so by Proposition 15.7, it is harmonic in the sense of Definition 7.2.     
Remark 15.10. Let X be a smooth curve (that is, a rig-smooth curve without boundary),
let H be the sheaf of harmonic functions on X , and let F be the subsheaf of R-vector
spaces generated by the germs log | f | for local invertible analytic functions f . Then Thuil-
lier [Thu05, 2.3.4] has shown that F might be a strict subsheaf of H , with equality when
X is potentially locally isomorphic to P1,an or when K e is algebraic over a finite field. It was
shown in [Wan16, 5.2, 5.3] that F is the kernel of d′ d′′ : A0,0 sm
                                                                    → A1,1
                                                                         sm
                                                                             and that F is the
sheaf of smooth harmonic functions on X . The latter follows also by Proposition 10.17.
We conclude that there is a non-smooth harmonic function on an open subset of X if and
only if the inclusion F ⊂ H is strict. If F = H , then every harmonic tropicalization
map is a smooth tropicalization map, and Asm = A.
  Wanner’s regularization theorem [Wan19, Corollary 5.4], obtained for Mumford curves
or in case of an algebraic residue field over a finite field, can now be generalized as fol-
lows (compare Remark 15.10).
Proposition 15.11. Let X be a smooth curve (a rig-smooth curve without boundary) over
a non-trivially valued non-Archimedean field K, and let f be a subharmonic function on X
as defined in [Thu05, 3.1.2]. Then for any relatively compact open subset U of X , there is
a decreasing net of weakly smooth psh functions f i on U converging pointwise to f |U .
Proof. By Thuillier’s regularization theorem [Thu05, Théorème 3.4.2], there is a decreas-
ing net of piecewise R-linear subharmonic functions on U converging pointwise to f , so
we may assume that f is piecewise R-linear. (Note that piecewise R-linear functions are
called lisse in [Thu05, Definition 3.2.1].) As in the proof of [Thu05, Theorem 3.4.2],
we may assume that U = Y \ ∂ Y for a compact strictly analytic domain Y of X . By
[Thu05, Proposition 3.2.4], there is a finite Galois extension K ′ /K such that Y has a
strictly semistable model Y over the valuation ring of K ′ and such that f = F ◦ τ for a
piecewise R-linear function F on the skeleton S(Y), where τ: Y → S(Y) is the retraction.
Since the subharmonic functions over K are the Galois-invariant subharmonic functions
over K ′ and the same holds for weakly smooth functions, it is enough to prove the claim
over K ′ , so we may assume K = K ′ .
   Now we can follow Wanner’s arguments [Wan19, Lemma 5.2]. Note that the curvature
ddc ( f |U ) is a discrete measure on U; we denote by S its support. In what follows, we
allow subdivisions of Σ := S(Y) at arbitrary points in Σ (not just type-II points); we do
not claim that the subdivision is the skeleton of a formal model of U. By subdividing the


## GJR-2111.05741 cache page 81

              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                 81

skeleton, we may assume that Σ contains S, that F is affine on the edges of Σ, and that
the points of S are vertices of Σ. For a point x ∈ S, let Σ x be the union of all edges of
Σ containing x. By further subdividing Σ, we may assume that Σ x ∩ S = {x}. Since x
is in the support of ddc ( f |U ), the weighted sum of outgoing slopes of F in x is positive.
Then there is a harmonic function G x ≤ F on Σ x , affine on each edge of Σ x , and with
F ( y) = G x ( y) if and only if y = x. For ǫ > 0 sufficiently small, the regularized maximum
mǫ as defined in [Wan19, 4.6] leads to a function
                      fǫ := mǫ/2 (G x ◦ τ + ǫ, f ) = mǫ/2 (G x + ǫ, F ) ◦ τ
on τ−1 (Σ x ) which agrees with f over a neighbourhood of the boundary of Σ x and agrees
with G x ◦ τ + ǫ over a neighbourhood of x in Σ x . We conclude that the functions fǫ ,
for varying x S∈ S, can be glued to get a function fǫ defined on Y which agrees with f
on V := Y \ x∈S τ−1 (Px ) for suitable compact neighbourhoods Px of x in relint(Σ x ).
Since f is harmonic on U ∩ V by omitting S, we see that fǫ is harmonic on U ∩ V and
on a neighbourhood of S. Since the regularized maximum of two affine functions on a
segment is a convex smooth function, we see that fǫ is a smooth psh function over the
interior of each edge of any Σ x . Overall, it follows that fǫ is a weakly smooth psh function
on U. In the proof of [Wan19, Lemma 5.2], Wanner extracted from the functions fǫ a
decreasing sequence which converges pointwise to f , which proves the proposition. 

                16. CANONICAL TROPICALIZATIONS OF ABELIAN VARIETIES
  Let A be an abelian variety over the non-Archimedean field K with non-trivial valuation
v. The uniformization theory of Bosch, Lütkebohmert and Raynaud yields that after
replacing K by a finite separable extension, there is a canonical exact sequence
                                                   q
                                 0 −→ T −→ E −→ B −→ 0
of algebraic groups such that Aan = E an /Λ for a discrete subgroup Λ of E(K). Here B
is the generic fiber of an abelian scheme B over K ◦ and T is a split torus over K (see
[BL91] and [Ber90, 6.5]). Note that the quotient homomorphism p : E an → Aan is only
an analytic morphism, but the Raynaud extension E is algebraic by the GAGA principle,
and the quotient homomorphism q : E → B is locally trivial.
16.1 (Canonical Tropicalizations). We denote the character lattice of the split torus T by
M and we set N := Hom(M , Z). For u ∈ M , the pushout of the Raynaud extension with
respect to the character χu : T → Gm gives rise to a translation invariant extension of B
by Gm , and hence to a rigidified translation invariant line bundle Eu on B (see [BL91]
and [FRSS18, 3.2]). Note that the line bundle q∗ (Eu ) is trivial over E, and the above
pushout construction gives a canonical frame eu : E → q∗ (Eu ). Following [FRSS18, 3.2]),
we define the canonical tropicalization map as the unique map
                                      trop: E an −→ NR
satisfying
                             〈trop(x), u〉 = − log q∗ keu (x)kEu ,
where k kEu is the canonical metric on the rigidified line bundle Eu which is the formal
metric associated to the unique (up to isomorphism) formal K ◦ -model of Eu on the formal


## Berkovich-PMIHES-1993-78-5 cache page 30

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


## Berkovich-PMIHES-1993-78-5 cache page 31

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


## Berkovich-PMIHES-1993-78-5 cache page 32

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


## Berkovich-PMIHES-1993-78-5 cache page 39

42                                VLADIMIR G. BERKOVICH

belong to ^. For every v we take a representation ^ == S^^,/ as above. Then
^ = 2^ ^ ^T^ are well defined elements of J^', and we have a! -==• S^i b^ e ^ s S ' .
Thus ^ = ^ ^'.
       Let Y' be defined by an ideal a' C ^f. Denote by a the ideal of ^ generated
by all of the coefficients a^ from the representations a' == 2^ a^ T^ of elements a1 e a\
We claim that cT^Y') is the closed ^-analytic subset ofX defined by the ideal a. Indeed,
let x e X and x9 == a{x). Then x e (T^Y') ^ A;' e Y' o a' C ^ o a C p,, •
       Take a field K of the form K^_^, n ^ 1, such that the algebra ^ = ^ ® K
is strictly K-affinoid (the valuation on K is nontrivial since n^ 1). First we consider
the case when P + Red, Nor. Since ^ == Px^'? where ^ == <r(^), it follows from
Lemma 2.2.2 (ii) that ja^'p , is a P-ring. By the strictly affinoid case, <B^!^ is a P-ring.
Therefore 0^ is a P-ring, by Lemma 2.2.2 (i). We have
                  P(X) == Tt-^P^)) == (T-^PCX')).

From Lemma 2.2.5 it follows that P(X) is Zariski open in X.
      Let P == Red. It suffices to verify that the subsheaf of ideals ^c ^x consisting
of nilpotent elements is generated by rad(J2/). We may assume that rad(J^) == 0.
Then rad(j^) == 0. Hence ^ == 0. Since fl^a- ls embedded to 0^^^ where ^' == <r(^),
we have ^x == 0-
      Let P == Nor. By the previous case, we may assume that X is reduced. We want
to verify that there exists a e ^ which is not a zero-divisor such that aC^ C 0^.
Since this is true for the subsheaf of M^ generated by the normalization of ^ (see [Ber],
2.1.14 (i)), we may assume that ^ is a (normal) integral domain. By the strictly affinoid
case, there exists a non-zero element a; == S^ ^ T^ e ^ with a9 ^orm C 0^.. It suffices
to show that ^ ^orm C ^x fo1' any v- Let ^ be an open subset of X, and let/be an element
from the full ring of fractions of ^xW- Then al f ^ ^(^W^ where 9 denotes the
canonical map X'->X. But ^(P^W) consists of the series S^r? such that
/ e ^x(^). ^d, tor any affinoid subdomain V C %, ||/, ||v r" -^ 0 as v -> oo. It follows
that a^fe O^U} for any v. •
       2.2.6. Corollary. — Let ^ he one of the properties in Theorem 2.2.1. Then for any good
 k'analytic space Y the set P(Y) is Zariski open in Y. Furthermore, ifYis reduced, then the comple-
 ment to Reg(Y) is nowhere dense in Y. •

       2.2.7. Corollary. — Let P be one of the properties in Theorem 2.2.1. Let W be a scheme of
 locally finite type over k, and let n be the canonical map ^an -> W. Then P^) == TC-^PW).

      Proof. — We may assume that ^ == Spec(B) is an affine scheme, and B is a finitely
 generated A-algebra. Suppose first that the valuation on k is trivial. If/i, ..•,/„ gene-
 rate B over k, then ^an is a union of affinoid subdomains of the type
                   V = O/e ^ 11/M | < r, 1 < i ^ }.
 But if r ^ 1, then 88^ = B. Therefore the required statement follows from Theorem 2.2.1.


## Berkovich-PMIHES-1993-78-5 cache page 40

           STALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                        '43

      SupposenowthatthevaluadononAisnontrivia^andletj/e^^.By^er]^^.!,
fi^any is a faithfully flat ^y-algebra, and i f j / e Max(B), then ^^y == Q^y. Since A
is an excellent ring, we get the required statement, by the reasoning from the proof
of Theorem 2.2.1. •

      2.2.8. Corollary. —For any affinoid subdomain V C X one has Reg(V) = Reg(X) n V.


      Proofs. — If X and V are strictly A-affinoid, this is clear because both sets are
determined by their intersections with X^. The general case is reduced to the strictly
affinoid one by the reasoning from the proof of Theorem 2.2.1. •

           2.2.9. Remark. — The maximal ideal m^ of the local ring 0^ ^ can be strictly
larger than px^x,a;« This is related to the fact that the Zariski topology on an
affinoid subdomain V C X can be strictly stronger than that induced by the Zariski
topology on X. Here is an example. Let /(T) == S,°li ^T" be a formal power
                                                 r^

series in one variable over the residue field A, which is algebraically independent
of T, and set /(T) ^S^i^T", where a, are representatives of ^ in k°. We
claim that for any non-zero g{T^ T^) e k {T^ T^ } one has g(T,f(T)) + 0. Indeed, let
^(T^T^^S^.o^T^T^. Multiplying g by a constant, we may assume that
 1 1 ^ 1 1 = = max |fl,,,| = 1. LetS =={(tj) | |^,| == 1} (it is a finite set) and set

                P(T,,T,)==S,,^,^,T1T^
and             A(T,, T,) == g(T^ T,) - P(T,, T,).

Since || h \\ < 1, we have || A(T,/(T)) || < 1. If^(T,/(T)) == ^ then || P(T,/(T)) || < I.
It follows that ]P(T,y^T)) == 0. This is impossible because/(T) is algebraically inde-
                     /%/
pendent of T over k. Thus, the Zariski closed subset of the two-dimensional disc V of
radius r < 1, which is defined by the equation Tg —^(Ti) == 0, does not extend to a
Zariski closed subset of the two-dimensional unit disc X. If now x is the point ofX, which
corresponds to the multiplicative seminorm on k{T^ T^} :5(Ti, T^) »-^| 5(T,/(T))|,
then m^ =(= 0 because T^ —/(T^) e m^, but ^ == 0.


2.3. The residue fields K{x)

       2.3.1. Definition. — A field K with valuation is said to be quasicomplete if the
valuation extends uniquely to any algebraic extension of K.
       For example, if K is complete with respect to its valuation (i.e. K is a valuation
field in the terminology of [Ber], § 1.1), then it is quasicomplete. The following lemma
easily follows from [BGR], § 3.2.


## Wanner-1801.04713v3-20261004 cache page 2

2                                         V. WANNER


complex analysis. As Thuillier’s notion in the one dimensional case, their notion is
locally analytic and works without any hypotheses on the characteristic. Furthermore,
they introduced the Monge-Ampère measure for plurisubharmonic functions that are
locally approximable by smooth plurisubharmonic functions. This is a partial analogue
of the complex Bedford-Taylor theory. One would desire an analogue of this whole
theory, and also a monotone regularization theorem in this setting would be worthwhile.
Moreover, we do not know if the notion of plurisubharmonicity is stable under pullback.
   The subharmonic functions defined by Thuillier satisfy all required properties (cf.
[Thu05, §3.2]). In this present work, we will show that for a continuous function on the
analytification of a smooth proper algebraic curve his notion coincides with the one by
Chambert-Loir and Ducros.
   Let K be an algebraically closed, complete, non-archimedean, non-trivially valued
field and X be a smooth algebraic curve over K with Berkovich analytification X an . In
Section 2, we summarize Thuillier’s theory of subharmonic functions on open subsets of
the analytification X an . As in the complex potential theory, we use harmonic functions
to define subharmonic functions. The definition of harmonic functions is related to
skeletons of strictly affinoid domains. For every strictly affinoid domain Y and every
strictly semistable formal model Y of Y , which always exists by the semistable reduction
theorem, one obtains a finite graph S(Y) in Y with a retraction map τY : Y → S(Y).
Thuillier has introduced in [Thu05] harmonic functions as continuous functions such
that for every strictly affinoid domain Y and every strictly semistable formal model Y
of Y , we have f |Y = F ◦ τY for a piecewise affine function F on S(Y) such that the
sum of outgoing slopes is zero everywhere in S(Y)\∂Y for the Berkovich boundary ∂Y
of Y . An upper semi-continuous function f : W → [−∞, ∞) on an open subset W of
X an is then called subharmonic if and only if for every strictly affinoid domain Y in
W and every harmonic function h on Y with f ≤ h on ∂Y , we have f ≤ h on Y . In
[Thu05], there is also a notion of smooth functions which we call lisse (to distinct them
from those defined by Chambert-Loir and Ducros). For every lisse function f , Thuillier
defined a measure ddc f on W that is positive if and only if f is subharmonic. He showed
that all the properties of subharmonic functions one would expect from the complex
potential theory are satisfied. In particular, he verified the stability under pullback (see
Proposition 2.6) and proved a version of the monotone regularization theorem with lisse
subharmonic functions (see Proposition 2.8).
   In Section 3, we define plurisubharmonic functions in the sense of Chambert-Loir
and Ducros on the analytification of an arbitrary algebraic variety X of dimension n
over K. In the following, we just say psh. To do this, we will first recall the sheaf of
smooth differential forms Ap,qX on X
                                            an with the differential operators d′ and d′′ . For

an open subset W of X an , we use the notation Ap,q                                     p,q
                                                          X,c (W ) for the sections of AX (W )
with compact support in W . Every form ω ∈ An,n        X,c (W ) defines a unique signed Radon
measureR with compact
                    R support on W , which we denote by µω (see Proposition 3.13) and
write W f ∧ ω := W f dµω . Hence, every continuous function f : W → R on an open
subset W of X an leads to a current on An−1,n−1 X,c    (W ) given by
                                                   Z
                                d′ d′′ [f ](ω) :=     f ∧ d′ d′′ ω.
                                                 W

In [CD12], a function f is called psh if and only if the induced current d′ d′′ [f ] is positive.
Furthermore, we recall the definition of the Monge-Ampère measure corresponding to a
function that is locally approximable, i.e. it is locally the difference of uniform limits of
smooth psh functions. If X is a curve and the Monge-Ampère measure of a function f


## Wanner-1801.04713v3-20261004 cache page 3

  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES                   3


is positive, then f is psh. Note that if X is proper and smooth, model functions on X an
are lisse, locally approximable and the Monge-Ampère measure MA(f ) coincides with
Thuillier’s measure ddc f , which follows from results of Chambert-Loir–Ducros and Katz–
Rabinoff – Zureick-Brown. A definition of model functions can be found in Definition
3.26. These functions and these properties are key ingredients for the proofs in Section
4.
   In Section 4, we show the coincidence of the notions of subharmonic and psh for
continuous functions on the analytification of algebraic curves. We start by showing in
Proposition 4.3 that a lisse subharmonic function is psh. Since the psh functions form a
sheaf (see Proposition 3.19), it remains to show the assertion for an open neighborhood
of every point. The complicated case is a point of type II. The strategy is to find an open
neighborhood such that the lisse function f can be written as an R-linear combination
of model functions. One can deduce that the Monge-Ampère measure of the restriction
of f coincides with the measure ddc f defined by Thuillier since it does for every model
function, and the claim follows.
   Due to the analogue of Thuillier’s monotone regularization theorem (see Proposition
2.8), we get the following theorem.
Theorem 1. Let W be an open subset of X an and f : W → [−∞, ∞) be a subharmonic
function, then f is psh.
   We continue in Section 4 by proving the other implication for continuous functions,
i.e. the following theorem.
Theorem 2. Let W be an open subset of X an and f : W → R be a continuous function.
If f is psh, then f is subharmonic.
   To obtain this result, we first show in Lemma 4.6 that for every non-subharmonic
function f ,Rthere has to beRa specific non-negative model function g with compact support
such that f MA(g) = f ddc g < 0. The proof of the theorem is by contradiction,
and we assume that such a function g exists. RWe approximate g by non-negative
                                                                       R            smooth
functions gk with compact support such that f dMA(g) = limk→∞ f ∧d′ d′′ gk . Since f
is psh, the left hand side of the equation is non-negative, and so f has to be subharmonic.
The idea of the construction of these functions gk is based on [CD12, Proposition 6.3.2]
and we explain the modification in several steps.
   In Section 5, we give some applications of this coincidence of the two notions of
subharmonicity for continuous functions. Since we know that subharmonicity in the
sense of Thuillier is stable under pullback (see Proposition 2.6), we can deduce the
following corollary from the theorems above.
Corollary 3. Let X, X ′ be smooth proper algebraic curves over K and ϕ : W ′ → W
be a morphism of K-analytic spaces for open subsets W ⊂ X an and W ′ ⊂ (X ′ )an . If a
continuous function f : W → R is psh on W , then ϕ∗ f is psh on ϕ−1 (W ).
  Furthermore, if X satisfies some certain properties, e.g. X is the projective line
or a Mumford curve, we obtain a monotone regularization theorem in the setting of
Chambert-Loir and Ducros using the one in Thuillier’s setting (see Proposition 2.8). Note
that we need all harmonic functions on X an to be smooth in the sense of Chambert-Loir
and Ducros to prove the statement.
Corollary 4. Let X be a smooth proper curve over K. If the residue field K  e is algebraic
over a finite field or X is the projective line or a Mumford curve, then every continuous
psh function f : W → R on an open subset W of X an is locally psh-approximable. More
precisely, the sequences of smooth psh functions can be chosen monotonically decreasing.


## Wanner-1801.04713v3-20261004 cache page 31

   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 31


as y ∈
     / Ωk . By property ii) following (4.6), εk+1 < εk /3 and the last inequality, we get
                     fk+1 (y) ≤ max(Gx (τY (y)) + εk+1 , f (y)) + εk+1 /4
                              ≤ max(Gx (τY (y)) + εk , f (y) + εk /2)
                              ≤ fk (y).
  Thus, the sequence fk of continuous functions converges pointwise to the continuous
function f on Y and fk+1 ≤ fk . Since Y is compact, fk converge uniformly by Dini’s
theorem. We have already seen above that every fk is smooth and psh on W .         
  Before we use this lemma to prove a monotone regularization theorem in the setting of
Chambert-Loir and Ducros for Mumford curves, we recall the definition of these curves.
Definition 5.3. A smooth proper curve X of genus g ≥ 1 over K is called a Mumford
curve if there is a semistable model X such that all irreducible components of the special
fibre are rational (cf. [Ber90, Theorem 4.4.1]).

Corollary 5.4. Let X be a smooth proper curve over K. If K    e is algebraic over a finite
field or X is the projective line or a Mumford curve, then every continuous psh function
f : W → R on an open subset W of X an is locally psh-approximable. More precisely, the
sequence of smooth psh functions can be chosen monotonically decreasing.
Proof. At first, note that in the given situation HX is a subsheaf of C ∞ on X an , which
is a consequence of [Thu05, Théorème 2.3.21] (see [Wan16, Corollary 5.3.21]). We ad-
ditionally use [Ber90, Theorem 4.4.1] in the case of a Mumford curve. Hence, we may
apply Lemma 5.2.
   To prove the corollary, we have to show that every point x in W has an open neigh-
borhood in W such that f is a uniform limit of smooth psh functions. The continuous
psh function f is subharmonic by Theorem 4.7, and we therefore can use Thuillier’s
monotone regularization theorem (see Proposition 2.8). We can find for every x ∈ W a
relatively compact neighborhood W ′ of x in W and a decreasing net hfj i of lisse subhar-
monic functions on W ′ converging pointwise to f . Let Y be a strictly affinoid domain
in W ′ having x in its interior Y ◦ . Then the decreasing net hfj i converges uniformly to
the continuous function f on the compact set Y by Dini’s theorem. Thus, one can con-
struct inductively a decreasing sequence of lisse subharmonic functions on W ′ converging
uniformly to f on Y and we write (fk )k∈N for this sequence.
   We have seen in Lemma 5.2 that each fk is the uniform limit of a decreasing sequence
of smooth psh functions on Y ◦ . Hence, we can choose a decreasing sequence of smooth
psh functions on Y ◦ converging uniformly to f .                                        
Remark 5.5. Note that there are curves such that the sheaf HX of harmonic functions
is not a subsheaf of the sheaf C ∞ of smooth functions on X an . A counter example of such
a curve can be constructed by the proof of [Thu05, Théorème 2.3.21] (see for example
[Wan16, Corollary 5.3.23]). For those curves we do not know whether every psh function
is locally psh-approachable.

                                          References
[Ber90]   Vladimir G. Berkovich. Spectral theory and analytic geometry over non-Archimedean fields,
          volume 33 of Mathematical Surveys and Monographs. American Mathematical Society, Prov-
          idence, RI, 1990.
[Ber07]   Vladimir G. Berkovich. Integration of one-forms on p-adic analytic spaces, volume 162 of
          Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 2007.
