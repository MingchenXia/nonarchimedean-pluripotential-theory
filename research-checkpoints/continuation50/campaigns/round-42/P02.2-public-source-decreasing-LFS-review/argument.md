# Exact final status

{
  "id": "P02.2",
  "status": "partial",
  "exact_result": "For complete algebraically closed nontrivially valued K, arbitrary classical psh targets on boundaryless algebraic curve domains have fixed-neighborhood decreasing LFS nets, and sequences when K is countably dense. Pullback and proper-fibre constancy give the same for all targets defined on saturated projective bundles and proper-factor products. An uncountable residue field gives a sharp sequence obstruction for the boundary spike on a closed disc and its projective-space products; the spike has an explicit LFS sequence for countable residue and a net in general.",
  "proof_file": "P02.2-argument.md",
  "concrete_gaps": [
    "No necessary-and-sufficient characterization of higher-dimensional good strict spaces for the full arbitrary classical psh starting class.",
    "The sufficient sector requires targets defined on saturated neighborhoods; arbitrary nonsaturated local germs are not handled.",
    "No general nonclosed-field descent of the newly constructed interpolants and fixed perturbation.",
    "No sequence extraction for arbitrary fresh targets over fields lacking a countable dense subset; only nets are proved there.",
    "The boundary obstruction is sharp for its particular function and distinguishes sequences from nets; it does not establish the full failure range."
  ]
}


# Entire final proof

# P02.2: fixed-neighborhood LFS regularization in a proper-fibre sector, and a boundary obstruction

This is an unverified partial mathematical argument. The original characterization of all higher-dimensional good strict analytic spaces remains open here. Only P02.2 is addressed. No unpublished book assertion is used. The results below concern arbitrary classical psh functions, including discontinuous functions and the value $-\infty$.

## 1. Precise results and scope

Let $K$ be complete, algebraically closed, and nontrivially non-Archimedean valued. Let $C$ be an ordinary open subset of the analytification of a smooth connected algebraic $K$-curve. Its genus is unrestricted. The curve is boundaryless. Write $\Gamma=-\log|K^\times|$; it is divisible and dense in $\mathbb R$.

Curve result. For every classical psh function $g:C\to\mathbb R\cup\{-\infty\}$ and every $c\in C$, there is one ordinary open neighborhood $U$ of $c$ and a decreasing net of finite strict-domain real-PL LFS functions on $U$ with pointwise infimum $g|_U$. If $K$ has a countable dense subset in its valuation topology, this net has a decreasing sequence extraction with the same pointwise limit. No continuity of $g$ is assumed. No restriction on the residue field or the residue genera is imposed. The approximants are actual LFS functions in GJR Definition 7.8, rather than a further limiting stage.

Higher-dimensional result. Under these field hypotheses, let $f:X\to C$ be either the actual analytic projective bundle $\mathbb P(E)$ of a locally free analytic sheaf $E$ of rank $r+1$, $r\geq1$, or the product projection $C\times P^{\mathrm{an}}\to C$, where $P$ is a nonempty geometrically connected proper algebraic $K$-variety of positive dimension. Every arbitrary classical psh function on $X$, or on a saturated ordinary open set $f^{-1}(C_0)$, has the preceding decreasing LFS net near each point, on a fixed saturated ordinary neighborhood $f^{-1}(U)$. It has a sequence when $K$ is countably dense. These are higher-dimensional sectors with no torus or invariance hypothesis on the starting function. Properness forces fibre constancy; it is not an imposed restriction on the function.

Boundary result. If $K$ is algebraically closed with uncountable residue field, the closed unit disc has a classical subharmonic function which is not a pointwise limit of a decreasing sequence of continuous functions on any ordinary neighborhood of its Gauss point. Thus it has no decreasing LFS sequence there. The same obstruction occurs on the good strict spaces $D\times\mathbb P^r_K{}^{\mathrm{an}}$, $r\geq1$. For this particular disc function, countability of the residue field is the sharp condition: an explicit decreasing LFS sequence exists when the residue field is countable. This is a sequence obstruction, not a proof of failure for nets.

The higher-dimensional positive result quantifies over all classical psh functions defined on the displayed saturated spaces. It does not establish regularization for arbitrary germs defined only on a nonsaturated small open subset of a projective bundle. A local germ need not extend to a saturated neighborhood. In particular this sector must not be read as a characterization of the full psh sheaf on every open subset of $X$.

## 2. Published foundations and exact conventions

GJR denotes the cached paper arXiv:2111.05741; Thu denotes Thuillier's thesis tel-00010990v1; GRc denotes arXiv:2506.13548v2; GRpl denotes the cached arXiv:2503.05513v1. GRc Definition 4.1 tests pullbacks on analytic curves after every analytic field extension, with upper semicontinuity and values in $\mathbb R\cup\{-\infty\}$. On a smooth boundaryless strict curve this is Thuillier subharmonicity, allowing an identically $-\infty$ connected component: GRc 3.4.1, 4.1.2 and Proposition 3.5. Scalar extension, pullback and decreasing nets preserve this class, by GRc Propositions 3.5 and 4.2.

GJR Definition 5.1 uses the G-topology generated by strictly affinoid domains: a real-PL function is G-locally a finite real linear combination of logarithms of analytic units. Thu 2.1.1 distinguishes the all-domain site $X_G$ from the strict rigid site $X_R$, and Thu Definition 3.2.1 uses all affinoid domains to define its lisse functions. These are not silently identified. GJR Example 5.3 explicitly shows that an irrational bend of a maximum of real-PL functions can fail to be strict-domain real-PL when the value group is $\mathbb Q$.

By GJR Definition 7.8, a real-PL function $h$ is LFS at $x$ precisely when its residue class $L_h(x)\in\operatorname{Pic}(\operatorname{red}(X,x))\otimes\mathbb R$ is semiample. Semiample for a real class means a finite nonnegative real combination of semiample integral classes. GJR 7.9 gives its ordinary-local description as a nonnegative real combination of maxima of negative logarithms of analytic units. The prerequisite that $h$ is real-PL is retained. A logarithm of a unit, and any real constant, has zero residue and is LFS; GJR Lemmas 6.17--6.18 prove the residue statement. For constants choose $a\in K^\times$ with $|a|\neq1$ and write the constant as a real multiple of $\log|a|$.

GJR Proposition 7.10 gives a sequence of uniformly convergent LFS functions near an interior point of a semipositive real-PL function. Its conclusion does not say decreasing. Its proof uses $h+\epsilon h'$ on one neighborhood for this one $h$. Applying it separately to an infinite family can change the neighborhood and is not our construction.

GJR 15.2--15.5 provide finite semistable skeletons and integral PL realization for piecewise $(\mathbb Z,\Gamma)$-linear functions. Thu Theorem 2.3.8 supplies the finite separable semistable extension for a strict affinoid smooth curve; over our algebraically closed $K$ that extension is $K$ itself. Thu Lemma 2.2.22 puts finitely many type-2 points in a skeleton, and then makes them vertices, again over $K$. Its part (i) requires type-2 points for the finite separable extension. We never turn an arbitrary type-3 point into a vertex over $K$.

The skeleton slope-degree formula and harmonicity are used in exactly the form checked in GJR Proposition 15.7 and its proof: at an interior vertex the outgoing slope sum is the degree of the residue line bundle, and vanishing of that sum is harmonicity. GRpl Proposition 5.1, and equivalently GRc Theorem 4.3 on a good strict space, identify subharmonic strict real-PL functions on a smooth curve with nef residue classes. The numbering is important: the cached GRpl version calls the curve comparison Proposition 5.1, although GRc cites another version's Proposition 3.1.

Wanner Corollary 5.4 assumes a finite continuous target and either residue field algebraic over a finite field, projective line, or Mumford curve. Its Dini argument is not used for our arbitrary targets. GJR Proposition 15.11 states a decreasing net of weakly smooth functions; it does not state a sequence or an LFS conclusion.

The cached CD PDF numbers its semiample-residue implication as Proposition 17.8.2, not 6.8.2. Its hypotheses there are a separated almost-good space, an integral paralinear metric on an ordinary-locally trivial line bundle, and a positive residue power generated by global sections. We use the directly stated GJR 7.8--7.9 convention, not a mismatched numbered CD proposition or a claimed comparison of smoothness classes.

## 3. A strict-domain realization lemma

Let $Y$ be a compact connected strictly affinoid smooth curve with a semistable model over $K$, skeleton $\Sigma$, and retraction $\tau:Y\to\Sigma$. Suppose a continuous function $F$ on the finite graph $\Sigma$ is affine on every edge of a subdivision whose vertices are type 2. Slopes and function values can be arbitrary real numbers. Then $F\circ\tau$ is strict-domain real-PL on $Y$.

Here is the local proof, which does not round real breakpoints or invoke Thu's all-domain sheafification. At a type-2 vertex $v$, cut each of the finitely many incident edges at a nearby type-2 point. Distances of the cuts from $v$ belong to $\Gamma$. Refine the semistable model at these cuts; the inverse image of this closed star is a compact strictly analytic neighborhood with that star as skeleton. For each incident edge $e$ define $F_e$ to have value zero at $v$, slope one away from $v$ on $e$, and value zero on the other edges. With edge coordinates normalized at their type-2 endpoints, $F_e$ has integral slopes and intercepts in $\Gamma$. GJR 15.4--15.5 realize $F_e\circ\tau$ as an integral PL function on this strict domain. On this star,

$$F\circ\tau=F(v)+\sum_e s_e(F_e\circ\tau),$$

where $s_e\in\mathbb R$ is the outgoing slope. The constant is real-PL by the preceding constant formula. This proves strict real-PL near $v$. At a type-3 point in the interior of an edge, the function is affine in an annulus coordinate, hence is a real multiple of the logarithm of a unit plus a constant on a sufficiently small strict annulus neighborhood. At points off the skeleton it is locally constant in the open discs contracted by $\tau$, so is real-PL there. Real-PL functions form a sheaf in the ordinary topology, GJR 5.2(4), so these local proofs give the assertion on $Y$.

The local star can include a boundary vertex: the PL realization itself needs no positivity at that boundary. For positivity below we always pass to $Y\setminus\partial Y$. This proof permits arbitrary real coefficients but only value-group vertices. It therefore does not contradict GJR Example 5.3.

## 4. Finite interpolation on one fixed ordinary open set

Fix $c\in C$. Choose a compact connected strictly affinoid neighborhood $Y\subset C$ with $c\in U:=Y\setminus\partial Y$. Here $\partial Y$ is the actual analytic boundary. It is a finite type-2 set over algebraically closed $K$. Since $C$ is boundaryless and separated, GRc 2.11(3)--(4) identifies $U$ with the topological interior of $Y$ in $C$, so $U$ is an ordinary open neighborhood. Shrink inside the connected component of $C$ under consideration. The connected affinoid curve $Y$ has nonempty boundary. Indeed a compact boundaryless connected affinoid of positive dimension would, by the maximum principle applied to all $\log|a|$, have the same value of every $a$ at every point, making its affinoid spectrum a singleton, impossible in positive dimension over algebraically closed $K$.

If $g$ is identically $-\infty$ on this component, the sequence of constants $-j$ already solves the local problem. Otherwise $g$ is finite at all type-2 and type-3 points, by Thu Proposition 3.4.10 or GRc Proposition 3.5(9).

For each finite set $S$ of type-2 points in $Y$ containing $\partial Y$, construct $H_S$ as follows. Refine a semistable model of $Y$ so that $S$ lies in the vertex set of its finite skeleton. Assign the value $g(s)$ at each $s\in S$. On each edge use an affine function and at every other vertex impose zero outgoing slope sum. This finite Dirichlet system has a unique solution: its quadratic energy is strictly positive for a nonzero vertex function which is zero on $S$, because every connected graph component meets the boundary in $S$. Pull it back by the retraction. It is continuous and finite on $Y$, equals $g$ on $S$, and is harmonic on $Y\setminus S$ by the slope-degree formula and GJR 15.7. This is the unique harmonic interpolation used in Thu's proof of Theorem 3.4.2. The construction is independent of the model: uniqueness follows from the harmonic maximum principle with the assigned boundary values. Section 3 proves it is strict-domain real-PL.

For completeness the comparison arguments are as follows. The subharmonic maximum principle on each component of $Y\setminus S$ gives $g\leq H_S$ on $Y$. If $S\subset S'$, compare $H_S$ with $H_{S'}$ on $Y\setminus S'$: on its boundary $S'$ the first function is at least $g=H_{S'}$, and both are harmonic there. Hence $H_S\geq H_{S'}$ on $Y$.

The function $H_S|_U$ is subharmonic. Given an affinoid domain $V\subset U$ and a harmonic function $h$ with $h\geq H_S$ on $\partial V$, first $h\geq g$ on $V$ by subharmonicity of $g$. At $S\cap V$ this is $h\geq H_S$. On $V\setminus S$ compare the two harmonic functions using $\partial V\cup(S\cap V)$ as boundary. It follows that $h\geq H_S$ on $V$. This proves the subharmonic test; it is precisely the comparison in Thu's published interpolation proof. Consequently $H_S$ has nef residues on $U$ by the strict real-PL comparison.

Let $w=\inf_S H_S|_U$. The infimum of this decreasing net is subharmonic, or identically $-\infty$, by Thu 3.1.8(ii). It agrees with $g$ at every type-2 point of $U$, because that point can be included in $S$. In particular it is not identically $-\infty$. At a type-3 point take its annulus segment with type-2 points dense on the segment. Both functions are finite convex continuous on the segment, by Thu Proposition 3.4.6 applied to a surrounding semistable domain. They agree on its type-2 points and therefore agree at the type-3 point. Thu Lemma 3.4.1 says that a subharmonic function is determined by its values on $I(U)$, the type-2 and type-3 points; its proof uses shrinking one-Shilov-point domains and upper semicontinuity to recover the other points. Thus $w=g|_U$, including any type-1 poles. This proves convergence for the type-2-only interpolation net without declaring every all-domain lisse function strict real-PL.

## 5. One perturbation handles every residue class

Choose one initial semistable model of $Y$ with skeleton $\Sigma_0$. Let $B$ be the finite set of its interior vertices whose smooth proper residue curves have positive genus. All positive-genus type-2 points of $U$ lie in $B$. To check this assertion, off the initial vertices a point is either on an open annulus or inside a contracted open disc; a type-2 point there has residue curve $\mathbb P^1_{\widetilde K}$. The description follows from the smooth and nodal tubes of a semistable curve. Adding vertices by the blowups in Thu 2.2.22 only adds these genus-zero points. Hence the set $B$ is unchanged when an interpolation skeleton is refined.

On $\Sigma_0$ solve the graph Dirichlet problem with value zero at $\partial Y$ and outgoing slope sum one at each $b\in B$, zero at every other interior vertex. To see existence without any positivity assumption, for unknown interior vertex values $q_v$ solve

$$\sum_{e=vw}\frac{q_w-q_v}{\ell_e}=\mu_v,\qquad \mu_v=\begin{cases}1&v\in B,\\0&v\notin B.\end{cases}$$

Parallel edges are counted separately. The negative of the coefficient matrix has quadratic form $\sum_{e=vw}(a_v-a_w)^2/\ell_e$, with boundary values zero. It is positive definite, as every connected component meets the boundary. Thus the system is invertible. Extend the solution affinely on edges. It is finite and continuous on the compact graph; by the graph maximum principle it is nonpositive. Put

$$Q=q\circ\tau_0+A,\qquad A=\max_{y\in Y}|q(\tau_0(y))|.$$ 

Then $Q\geq0$ on $Y$. Section 3 proves strict real-PL membership. The outgoing slope sums are nonnegative on $U$, and off the skeleton the function is locally constant. The slope-degree formula and the curve comparison show that $Q$ is subharmonic and has nef residues on $U$. At each $b\in B$ the residue degree is exactly one. It may have negative outgoing slope sums at boundary vertices, which have been removed from $U$; no positivity assertion there is needed.

The required algebraic fact for real residue classes is: on a smooth proper connected curve over an algebraically closed field, every class in $\operatorname{Pic}\otimes\mathbb R$ of strictly positive degree is ample in the real-class sense, hence semiample. Here is the real-coefficient justification. Write the class as $\sum_{i=1}^m a_i L_i$ with integral $L_i$. The integral degrees define a rational linear functional on $\mathbb R^m$. The vector $(a_i)$ lies in its open positive half-space. A small rational simplex in that half-space can be chosen to contain this vector in its interior: approximate the vertices of a surrounding real simplex by rational vectors, preserving containment and positive degree. Express the vector with positive barycentric coefficients. Clearing each rational vertex's denominators expresses the class as a nonnegative real combination of integral positive-degree line bundles. An integral line bundle of positive degree is ample and has a globally generated positive power: for sufficiently large powers its degree is greater than $2g$, and the curve Riemann--Roch/duality criterion applied after subtracting any point gives global generation (degree greater than $2g+1$ separates length-two subschemes as well). This proves the assertion. On $\mathbb P^1$, $\operatorname{Pic}\otimes\mathbb R=\mathbb R[\mathcal O(1)]$, so every nonnegative-degree class is already semiample, including zero.

At an interior type-2 point of a smooth curve, its germ reduction has the smooth proper residue curve as model. This follows also by taking the component at the corresponding semistable vertex in GJR 6.13--6.16. Normalizing and completing that function field gives the unique smooth proper curve; proper birational maps between smooth curves are isomorphisms. Thus representing and testing the residue class on that curve is legitimate. At non-type-2 points the functions under consideration are harmonic locally; their residue class is zero, since the residual function field has transcendence degree zero over the algebraically closed residue field. In particular it is semiample.

For every finite $S$ as above and every $\epsilon>0$, define

$$V_{S,\epsilon}=H_S+\epsilon Q\quad\hbox{on }U.$$ 

This is a strict real-PL function. Its residue class is the sum of the two residue classes by GJR 6.18. At $b\in B$, it has degree at least $\epsilon$, so the algebraic fact makes it ample. At every other type-2 point its residue curve has genus zero and its degree is nonnegative, so its class is semiample. At non-type-2 points it has zero residue. Therefore every $V_{S,\epsilon}$ is LFS at every point of the same ordinary open set $U$, by GJR 7.8. GJR 7.9 also guarantees actual ordinary-local formulas by logarithmic maxima there. No claim that nef equals semiample on an arbitrary higher-dimensional residue variety is made.

Order the pairs by enlargement of $S$ and decrease of $\epsilon$ to zero. Since $Q\geq0$, this is a decreasing LFS net. Its infimum is $g|_U$, by the preceding interpolation convergence and $\epsilon Q\to0$. This handles arbitrary residue Picard classes, not just torsion ones. For example a non-torsion degree-zero class can prevent a particular harmonic real-PL function from being LFS, but the positive-degree perturbation makes its approximants LFS. Non-torsion $\operatorname{Pic}^0$ is therefore not, by itself, a failure criterion for decreasing local approximation.

## 6. Sequence extraction without continuity of the target

Assume now that $K$ has a countable dense subset. A strictly affinoid algebra over $K$ is a separable Banach space: polynomials in its finitely many Tate generators with coefficients in a countable dense set form a countable dense subset, and a quotient of a separable Banach space is separable. On its spectrum, evaluation of $|a|$ is bounded by the Banach norm and satisfies $\big||a(x)|-|b(x)|\big|\leq\|a-b\|$. Therefore a countable dense collection of algebra elements induces the full topology of its compact Hausdorff spectrum and separates points. The spectrum embeds into a countable product of compact real intervals. It is second countable. In particular $Y$ and its open subset $U$ are second countable; every open subset of $U$ is Lindelof.

For each $t\in\mathbb Q$, let $E_t=\{x\in U:g(x)<t\}$. This is ordinary open by upper semicontinuity, and

$$E_t=\bigcup_S\{x\in U:H_S(x)<t\}.$$ 

Lindelofness gives a countable subcover for each $t$. List all finite sets selected by these countably many subcovers as $T_1,T_2,\ldots$ and put $S_j=\partial Y\cup T_1\cup\cdots\cup T_j$. If the list is finite, repeat its final set; if it is empty, use $\partial Y$. The $H_{S_j}$ decrease. For any $x$ and any rational $t>g(x)$, the chosen subcover of $E_t$ supplies an interpolant $H_{T_k}(x)<t$, so $H_{S_j}(x)<t$ for all $j\geq k$. Together with $H_{S_j}\geq g$ this proves $H_{S_j}(x)\downarrow g(x)$. If $g(x)=-\infty$, use every rational $t$; the same argument gives convergence to $-\infty$.

Finally set

$$v_j=H_{S_j}+2^{-j}Q\quad\hbox{on the fixed }U.$$ 

Each $v_j$ is finite LFS by Section 5. Both summands decrease, since $Q\geq0$, so $v_{j+1}\leq v_j$. The limit is $g|_U$. This extraction need not be cofinal in the interpolation net. It is a countable extraction by sublevel covers, not Dini's theorem, and it does not presume a continuous target. Local uniform convergence is claimed only where the target is finite continuous on a compact set, in which case the usual compact decreasing-continuous-function argument applies.

## 7. Actual projective bundles and proper factors

First consider a nonempty geometrically connected proper algebraic variety $P$ over $K$. Over every analytic extension field $F/K$, the analytification of $P_F$ is compact, boundaryless and connected. Properness is preserved by scalar extension and analytification, Berkovich Proposition 2.6.9; GJR 2.3 records goodness, strictness and empty boundary for algebraic analytifications. For connectedness one can check an actual published theorem rather than assume it: Berkovich Theorem 7.1.1 identifies compactly supported cohomology of a compactifiable algebraic scheme with that of its analytification for an abelian torsion sheaf. Apply it in degree zero to a constant nonzero finite sheaf on $P_F$. Since $P_F$ is proper, compactly supported degree zero equals degree zero. Its algebraic connectedness gives only constant sections. A disconnected analytic space would have a nonconstant locally constant section, contradicting that comparison. This works for every complete $F$ and does not assume $F$ algebraically closed. In particular it applies to projective spaces. Because $K$ is algebraically closed, a nonempty $P$ has a $K$-rational closed point, giving a product section.

Let $u$ be any classical psh function on a saturated open subset of one of the stated total spaces. For $c\in C$, its pullback to the fibre over $\mathcal H(c)$ is classical psh by GRc 4.2 scalar extension and functoriality. That fibre is a compact connected boundaryless analytic space: it is $\mathbb P^r_{\mathcal H(c)}{}^{\mathrm{an}}$ for a projective bundle and $P_{\mathcal H(c)}^{\mathrm{an}}$ for a product. Upper semicontinuity gives a maximum unless all values are $-\infty$, in which case constancy is immediate. Otherwise the maximum is finite. By GRc Theorem 6.1 its maximum locus is open, and by upper semicontinuity it is closed. Connectedness makes that locus the whole fibre. Hence $u$ is constant on each fibre.

Define $g(c)$ to be this fibre value. On a projective-bundle trivializing ordinary open subset, the constant projective coordinate $[1:0:\cdots:0]$ is an actual analytic section $s$, and $g=u\circ s$. On a product use the fixed rational point of $P$. Thus $g$ is upper semicontinuous and classically psh on each such base open set by pullback; ordinary sheafiness, GRc 4.2(1), gives it on the base. The section values on overlaps agree because they lie in the same fibre. This proves $u=g\circ f$ and is a field-of-definition descent argument, not an assumption that a function on the total space already came from the base.

Apply Sections 4--6 to $g$, choosing $Y$ inside one base neighborhood when necessary. On $f^{-1}(U)$ put $w_j=v_j\circ f$ in the countable case, or pull back the net otherwise. This set is one fixed ordinary open neighborhood of the entire fibre. Pullback preserves strict real-PL by GJR 5.4(1). It preserves LFS directly: pull back each local formula of GJR 7.9; every analytic unit remains a unit, and the same finite maximum formula gives the pulled function. The functions $w_j$ are finite, decreasing, and converge pointwise to $u$.

Projective transition matrices do not alter any $w_j$, since it is the pullback of one globally defined function on $U$. On overlaps of fibre charts the functions agree exactly, not just in their limit. Different choices of base neighborhoods may give different regularizing sequences, but their restrictions have the same target on the overlap; the local assertion does not demand their global gluing.

For every complete analytic field extension $L/K$, the same functions pull back to $f_L^{-1}(U_L)$, where $U_L$ is the inverse image ordinary open set. By GJR 5.4(2) they are strict real-PL, and the logarithmic formulas prove LFS there. Evaluating at a point above $x$ shows the inequalities and the limiting value are unchanged: the limit is $u\circ\pi_{L/K}$. All construction data and functions were already over $K$; no norm or averaging descent from an unspecified extension is needed. This proves compatibility for pullbacks of the original target. It does not assert that every new psh function over an arbitrary nonseparable $L$ has a sequence: for that fresh target the countably-dense field hypothesis must be checked again.

## 8. A sharp boundary sequence obstruction

Let $D=\mathcal M(K\langle T\rangle)$ and let $\zeta$ be its Gauss point. Its actual analytic boundary is $\{\zeta\}$. Define $b(\zeta)=1$ and $b(x)=0$ for $x\neq\zeta$. It is upper semicontinuous, since its positive upper level sets are either $D$, $\{\zeta\}$ or empty. On $\operatorname{Int}(D)=D\setminus\{\zeta\}$ it is the constant zero and is subharmonic. GRc Proposition 3.5(3) extends subharmonicity from the interior to $D$ for this upper semicontinuous function; GRc 4.1.2 makes it classical psh. Its pullback after every analytic extension is therefore in the same classical class. This argument uses a genuine analytic boundary; the corresponding interior spike on a boundaryless disc is not asserted to be psh.

For algebraically closed $K$, the components of $D\setminus\{\zeta\}$ are the open residue discs $D_a$, $a\in\widetilde K$. Every ordinary neighborhood $N$ of $\zeta$ contains all of $D_a$ for all but finitely many $a$. Indeed $D\setminus N$ is compact and is covered by the disjoint open sets $D_a$, so a finite subcover suffices.

Suppose continuous functions $h_j$ on one ordinary neighborhood $N_0$ of $\zeta$ decrease pointwise to $b$. For each $j,m\geq1$, continuity supplies a neighborhood $N_{j,m}\subset N_0$ of $\zeta$ on which $|h_j(x)-h_j(\zeta)|<1/m$. Each of these neighborhoods excludes only finitely many complete residue discs. If $\widetilde K$ is uncountable, choose $a$ outside the countable union of those finite exceptional sets. Then $D_a\subset N_{j,m}$ for every $j,m$, so every $x\in D_a$ satisfies $h_j(x)=h_j(\zeta)$ for all $j$. Its limiting value must be one, contradicting $b(x)=0$. No continuous decreasing sequence, hence no LFS sequence, exists on $N_0$. In fact this continuity argument forbids any pointwise convergent sequence with this prescribed limit. The dimension-$r+1$ example is $D\times\mathbb P^r_K{}^{\mathrm{an}}$ with target pulled back from $b$. A fixed rational projective point gives a section. Restricting a putative local LFS sequence near $(\zeta,p)$ to this section gives the forbidden continuous sequence on a neighborhood of $\zeta$.

For sharpness for this particular function, suppose instead that $\widetilde K$ is countable, enumerate its elements without repetitions as $a_1,a_2,\ldots$, and choose lifts $t_i\in K^\circ$. Pick $c_0\in K^\times$ with $0<|c_0|<1$, set $\alpha=-\log|c_0|>0$, and for each $j$ choose $d_j\in K$ with $d_j^j=c_0$. Define, with the maximum finite even at a zero of $T-t_i$,

$$b_j=1+\sum_{i=1}^j\frac{j}{\alpha}\max\{\log|T-t_i|,\log|d_j|\}\quad\hbox{on }D.$$ 

Each summand is strict real-PL. Its bend is at the value-group radius $|d_j|$, with domains $|T-t_i|\leq|d_j|$ and $|T-t_i|\geq|d_j|$. On the first domain it is constant; on the second $T-t_i$ is a unit. Thus this is a strict affinoid G-cover, unlike an arbitrary real-radius subdivision. For LFS membership near a zero the term is locally constant. Away from its zero the unscaled maximum is $\max\{-\log|(T-t_i)^{-1}|,-\log|d_j^{-1}|\}$, the GJR 7.9 unit formula. The coefficient is nonnegative; sums and constants have semiample residues, so $b_j$ is LFS everywhere on $D$.

At $\zeta$ every summand is zero, so $b_j(\zeta)=1$. At $x\in D_{a_k}$ all terms except the $k$th are zero, and the $k$th contribution, when included, is $\max\{(j/\alpha)\log|T-t_k|(x),-1\}$. Therefore $0\leq b_j\leq1$, $b_{j+1}\leq b_j$, and at each such $x$ it eventually equals zero. The same is true at $T=t_k$ by the constant branch formula. Hence $b_j\downarrow b$ on the fixed disc $D$. All roots, lifts and strict domains were defined over $K$; pulling back the formula proves LFS, inequalities and convergence to the pulled target over every analytic extension.

Even with uncountable residue field there is a decreasing LFS net for $b$: use finite subsets of residue classes in the displayed sum and a positive integer truncation parameter $n$, with $d_n^n=c_0$, and order by enlargement of the subset and increase of $n$. At each residue disc its class eventually enters the subset and its term tends to $-1$. Thus the obstruction is exactly to sequences for this function, not to nets or to LFS approximation in general.

## 9. Remaining original obligations and evidence limits

The original P02.2 is not solved. The argument gives a sufficient saturated proper-fibre sector, not necessary and sufficient geometry for all higher-dimensional spaces or for every local psh germ. General arbitrary psh functions on nonsaturated higher-dimensional neighborhoods need not descend to curves. No construction is supplied for them. Boundaryless higher-dimensional residue varieties can have nef classes outside the semiample cone; the curve positive-degree argument does not extend to these varieties. We have not proved that this algebraic distinction obstructs approximation, because a perturbation can sometimes remove it. The boundary example gives a sharp residue-cardinality criterion for its specific sequence problem; it does not characterize the full failure range and does not obstruct nets. We have not removed algebraic closure from the positive construction or proved a descent of its newly chosen interpolants and perturbation over general nonclosed fields. Arbitrary targets over nonmetrizable fields receive a net here; a general sequence theorem is not asserted.

Rerun the lightweight evidence with `python collect_sources.py`, `python finite_diagnostics.py`, `python build_documents.py`, and `python verify_artifacts.py` in this workspace. The standalone `P02.2-paper.tex` embeds the entire argument, and the build program runs the existing TeX installation twice. `source-extracts/source-provenance.json` records exact cached hashes, retained literal text and actual PDF pages, numbering differences, and application checks. `finite-diagnostics.json` checks only finite rational graph examples and a finite interpolation grid. The original input is retained byte-identically as `input-original.json`; the parsed assignment and task are in `assignment-original.txt` and `task-original.json`. `status.json` uses only the five requested keys.

Source hashes establish the identity of the inspected files. Finite diagnostics, successful TeX compilation and artifact validation do not certify any infinite or mathematical claim. The mathematical proofs are the arguments above and the exactly identified published foundations; the whole submission remains an unverified draft with candidate false.


# Every actual native canonical note

[
  {
    "id": "n1",
    "summary": "Draft sufficient sector: arbitrary classical psh functions on saturated projective bundles and proper-factor products over arbitrary-genus curve domains admit decreasing LFS nets on fixed ordinary neighborhoods. Sequences are proved when the complete algebraically closed ground field is countably dense. Arbitrary nonsaturated germs remain untreated.",
    "detailedSummary": "For complete algebraically closed nontrivially valued K, a type-2-only harmonic interpolation net on a fixed strict affinoid curve neighborhood is realized as strict-domain real PL. One fixed nonnegative graph potential gives positive residue degree at every positive-genus residue point, making every perturbed interpolant genuinely LFS. Rational sublevel covers yield a sequence without assuming target continuity when K is countably dense. Proper connected fibres force arbitrary classical psh targets on saturated total spaces to descend to the curve. Actual sections, transition-chart agreement, and pullback after every analytic scalar extension are checked. This is a sufficient sector, not the original characterization.",
    "text": "Draft theorem. Let K be complete, algebraically closed and nontrivially valued. Let C be an ordinary open subset of the analytification of a smooth connected algebraic K-curve, of arbitrary genus. For every classical psh g:C→R∪{−∞} and c∈C, there is one ordinary open neighborhood U of c carrying a decreasing net of finite LFS functions with infimum g|U. If K has a countable dense subset, there is a decreasing sequence on that same U. No target continuity or residue-field torsion hypothesis is imposed.\n\nThe corresponding higher-dimensional sufficient sector consists of actual projective bundles f:P(E)→C of positive relative dimension and products C×P^an, where P is a nonempty geometrically connected proper algebraic K-variety of positive dimension. Every arbitrary classical psh function defined on the entire total space, or a saturated ordinary open subset f⁻¹(C₀), has this regularization locally on a fixed saturated neighborhood. This quantifier does not cover arbitrary germs defined only on nonsaturated small open sets.\n\nPublished foundations were checked in the supplied caches. GR arXiv:2506.13548v2 Definition 4.1 includes upper semicontinuous extended-real targets and all analytic scalar extensions in the curve test. Its 4.1.2 identifies the curve class with subharmonicity. GJR arXiv:2111.05741 Definition 5.1 uses strict affinoid domains; Definition 7.8 requires semiample real residue classes for LFS membership. GJR 15.4–15.7 provide strict skeleton realization and the outgoing-slope/residue-degree formula. Thuillier 2.2.22 permits finite separable refinement at type-2 vertices; algebraic closure makes that extension K itself. Thuillier 3.4.1–3.4.2 give harmonic interpolation and determination by type-2/type-3 values; 3.4.6 gives continuity on skeleton segments. The cached GR arXiv:2503.05513 calls the curve nef/subharmonic comparison Proposition 5.1. GR's later citation uses different numbering.\n\nConstruction and proof. Choose a connected compact strictly affinoid neighborhood Y⊂C with c∈U=Y\\∂Y. The actual analytic boundary ∂Y is finite and type 2. Since C is boundaryless and separated, U is its ordinary topological interior in C. Each connected positive-dimensional affinoid component has nonempty boundary. Otherwise compactness and the classical maximum principle applied to every log|a| would make all seminorm evaluations constant and its spectrum a singleton.\n\nIf g is identically −∞ on the connected curve component, use constants −j. Otherwise g is finite at type-2 and type-3 points. For each finite type-2 set S⊂Y containing ∂Y, refine a semistable skeleton to include S as vertices. Assign g(s) at s∈S and solve the finite harmonic Dirichlet system at the other vertices. Pull the affine graph solution back to Y, obtaining H_S. Its uniqueness follows from the harmonic maximum principle and makes it independent of the chosen refinement. It is finite, continuous, harmonic on Y\\S, and equals g on S.\n\nStrict real-PL realization is explicit. At a type-2 star with value-group cuts, use one basis function per incident edge: value zero at the center, slope one on that edge and zero on the other edges. Each basis has integral slopes and value-group intercepts and is integral PL by GJR 15.4–15.5. An arbitrary real-affine star function is its center constant plus the real linear combination determined by its outgoing slopes. At type-3 edge points use an annulus coordinate; off the skeleton the function is locally constant. Ordinary sheafiness of strict real PL gives membership on Y. Arbitrary real breakpoints are not introduced.\n\nSubharmonic comparison gives g≤H_S and H_S≥H_S′ when S⊂S′. To check H_S is subharmonic on U, let a harmonic h dominate H_S on the boundary of an affinoid V⊂U. It first dominates g on V. Hence it dominates H_S at S∩V. Comparing harmonic functions on V\\S then gives h≥H_S on V. Thus H_S has nef residues by the strict curve comparison.\n\nThe decreasing infimum w=inf_S H_S is subharmonic and agrees with g at every type-2 point. At type-3 points, both restrictions to surrounding annulus segments are finite convex continuous functions and agree on dense type-2 points. They therefore agree there as well. Thuillier 3.4.1 recovers all remaining values, including type-1 poles, from type-2/type-3 values. Consequently w=g. This restricts the interpolation construction to type-2 sets instead of identifying all-domain Thuillier lisse functions with strict real PL.\n\nNow fix one initial semistable skeleton Σ₀ of Y. Its finitely many interior positive-genus residue vertices form a set B. Every other type-2 point in U lies in an annulus or open disc and has residue curve P¹; refinements add only genus-zero vertices. Solve on Σ₀ the graph problem q=0 at ∂Y and\nΣ_{e=vw}(q_w−q_v)/ℓ_e=1 for v∈B, and 0 at other interior vertices.\nThe negative coefficient matrix has quadratic form Σ_e(a_v−a_w)²/ℓ_e with zero boundary values, so it is positive definite and the solution exists. Extend q affinely and set Q=q∘τ₀+A, with A=max_Y|q∘τ₀|. Then Q≥0. It is strict real PL, subharmonic on U, and its residue degree is one at each point of B. Boundary slope sums need not be positive, but those boundary points are removed from U.\n\nFor ε>0 put V_{S,ε}=H_S+εQ on U. At positive-genus residue points its residue degree is strictly positive. Every positive-degree real Picard class on a smooth proper curve is ample in the real-class sense: represent it by finitely many integral classes, surround its coefficient vector by a rational simplex in the positive-degree half-space, use positive barycentric coefficients, and clear denominators. This expresses it as a nonnegative real combination of integral positive-degree line bundles, each having a globally generated positive power by curve Riemann–Roch. At genus-zero points a nonnegative-degree class is semiample because Pic(P¹)⊗R=R[O(1)]. At non-type-2 points the residue is zero. Thus every V_{S,ε} is genuinely LFS by GJR 7.8, on the same U. Enlarging S and decreasing ε gives a decreasing LFS net with infimum g.\n\nFor a sequence assume K is countably dense. Its strict affinoid algebras are separable Banach spaces. A countable dense set of algebra elements induces the spectrum topology because ||a(x)|−|b(x)||≤||a−b||. Hence Y and U are second countable. For each rational t, the open set {g<t} is the union of the open sets {H_S<t}. Choose a countable subcover, list all selected finite sets T_k, and let S_j be their cumulative unions with ∂Y. Then H_{S_j} decreases to g at every point, including −∞ values. The actual approximants are v_j=H_{S_j}+2⁻ʲQ. Nonnegativity of Q proves v_{j+1}≤v_j, and each term is LFS. This does not use Dini or assume a continuous target; the selected sequence need not be cofinal in the net.\n\nFor proper factors, compactness and boundarylessness follow from proper analytification, Berkovich 2.6.9. Connectedness over every complete extension F follows by applying Berkovich 7.1.1 to H_c⁰ of a constant finite sheaf on the proper geometrically connected algebraic P_F: analytic disconnection would supply a nonconstant locally constant section. A classical psh function restricted to any fibre over H(c) is constant by the maximum principle, GR 6.1. Local projective coordinate sections, or a rational point of P for products, give g=u∘s, prove that the descended target is classical psh, and show agreement on overlaps. Pull back v_j along f. GJR 5.4 gives strict real PL; GJR 7.9's ordinary-local maxima of logarithms of units pull back to prove LFS membership. Transition charts give exactly the same pulled functions.\n\nAfter any analytic extension L/K, these already-defined functions remain LFS on the inverse-image ordinary open set, with unchanged inequalities and limit u∘π. All construction data were over K. This compatibility concerns pullbacks of the original target; fresh targets over arbitrary nonseparable L are not asserted to have sequences.\n\nThe complete argument is in P02.2-argument.md and embedded in standalone P02.2-paper.tex. Rerun python collect_sources.py, python finite_diagnostics.py, python build_documents.py, and python verify_artifacts.py. The original characterization, nonsaturated higher-dimensional germs, nonclosed-field construction/descent, and general sequence extraction over nonmetrizable fields remain unresolved. The argument is an unverified mathematical draft.\n\nArtifacts: /workspace/research/campaigns/round-42/P02.2-public-source-decreasing-LFS/artifacts/codex-gsYJxq",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Sharp sequence obstruction for one boundary target: the Gauss-point spike on a closed disc has no continuous regularizing sequence when the algebraically closed residue field is uncountable, but has an explicit decreasing LFS sequence when it is countable. Projective-space products give higher-dimensional failures. Nets remain possible.",
    "detailedSummary": "The upper semicontinuous function equal to one at the actual boundary Gauss point and zero elsewhere is classical psh by the published extension-from-interior property. Every Gauss-point neighborhood contains all but finitely many complete residue discs. Countably many continuity neighborhoods leave an untouched residue branch when the residue field is uncountable, contradicting the proposed limit. For countable residue, truncated logarithms with value-group radii give finite LFS approximants on the fixed disc, with explicit monotonicity and convergence. A finite-subset construction gives a net even in the uncountable case.",
    "text": "Let K be complete, algebraically closed and nontrivially valued, D=M(K⟨T⟩), and ζ its Gauss point. Define b(ζ)=1 and b=0 elsewhere. This is upper semicontinuous. The actual analytic boundary of D is {ζ}, and b is the constant zero on Int(D). GR arXiv:2506.13548v2 Proposition 3.5(3) therefore makes b subharmonic on D; 4.1.2 makes it classical psh. This uses a boundary point, not an interior spike.\n\nThe components of D\\{ζ} are the open residue discs D_a indexed by a∈K̃. Any ordinary neighborhood N of ζ contains every complete D_a except finitely many: its compact complement is covered by these disjoint open discs, so has a finite subcover.\n\nSuppose continuous h_j on one neighborhood N₀ converge pointwise to b. For each j,m, continuity supplies N_{j,m}⊂N₀ containing ζ with |h_j(x)−h_j(ζ)|<1/m. Each N_{j,m} omits only finitely many complete residue discs. If K̃ is uncountable, choose a outside the countable union of those exceptional sets. Every x∈D_a then satisfies h_j(x)=h_j(ζ) for all j, by letting m tend to infinity. Its limiting value is one, contradicting b(x)=0. Thus no continuous sequence with this limit exists locally, and in particular no decreasing LFS sequence exists.\n\nOn X=D×P^r_K^an, r≥1, pull b back by projection. It is arbitrary-class classical psh by functoriality. A rational projective point gives a section through (ζ,p). Restricting any purported local LFS sequence to that section yields the forbidden continuous sequence. These are good strict higher-dimensional spaces with a genuine analytic boundary.\n\nThe residue cardinality criterion is sharp for this particular target. If K̃ is countable, enumerate its elements a_i without repetition, choose lifts t_i∈K°, choose c₀ with 0<|c₀|<1, set α=−log|c₀|, and choose d_j with d_j^j=c₀. On the fixed D put\nb_j=1+Σ_{i=1}^j (j/α) max{log|T−t_i|,log|d_j|}.\nThe maximum is finite at zeros. Its bend has radius |d_j| in the value group. The domains |T−t_i|≤|d_j| and |T−t_i|≥|d_j| form a strict affinoid G-cover; the term is constant on the first and the logarithm of a unit on the second. Thus it is strict real PL. Near its zero it is locally constant. Elsewhere the unscaled maximum is max{−log|(T−t_i)⁻¹|,−log|d_j⁻¹|}, the actual GJR 7.9 LFS formula. Nonnegative coefficients, sums and constants preserve semiample residues, so b_j is LFS everywhere.\n\nAt ζ all summands vanish and b_j=1. At x∈D_{a_k}, every summand except the kth vanishes, and after that term is included its value is max{(j/α)log|T−t_k|(x),−1}. Consequently 0≤b_j≤1, b_{j+1}≤b_j, and b_j(x) eventually equals zero. Hence b_j↓b on D. Roots, lifts and domains are over K; pulling back their formulas preserves LFS and convergence to the pulled target under every analytic extension.\n\nFor uncountable K̃ the same formula indexed by finite subsets of residue classes and an increasing positive integer truncation parameter gives a decreasing LFS net with infimum b. Therefore this is a sequence obstruction, not a net obstruction or a characterization of the full failure range.\n\nThe proof and explicit formulas are retained in Section 8 of P02.2-argument.md and P02.2-paper.tex. Published boundary hypotheses and literal excerpts are retained in source-extracts/source-provenance.json. These are unverified mathematical claims, independent of execution checks.\n\nArtifacts: /workspace/research/campaigns/round-42/P02.2-public-source-decreasing-LFS/artifacts/codex-gsYJxq",
    "support": []
  },
  {
    "id": "n3",
    "summary": "Requested proof artifacts, source provenance, preserved inputs and reproducible diagnostics were produced. Both final TeX passes succeeded cleanly. The original P02.2 characterization remains unresolved, so candidate is false.",
    "detailedSummary": "Artifact checks confirmed byte-identical original input, exact assignment/task retention, the five required status keys, seven cached source hashes, 73 retained primary PDF pages, and 16 exact literal excerpts. A nine-page standalone paper compiled twice without reported warnings or overfull boxes. Exact finite diagnostics checked a graph Dirichlet solution and 1,799 interpolation-grid inequalities only; they do not validate analytic realization or the infinite mathematical arguments. The positive theorem has saturated-domain and field hypotheses, while the negative theorem distinguishes sequences from nets.",
    "text": "Deliverables are P02.2-argument.md, standalone P02.2-paper.tex and its nine-page P02.2-paper.pdf, status.json, and source-extracts/source-provenance.json. The argument contains the complete draft proofs described in n1 and n2 and the remaining original obligations. status.json has exactly id, status, exact_result, proof_file, concrete_gaps, with status partial.\n\nPreserved inputs: input.json and input-original.json are byte-identical, 17,867 bytes. assignment-original.txt equals the supplied assignment string; task-original.json retains the parsed task. The read-only public cache hashes matched the supplied source identities. Source retention contains 73 selected actual primary PDF pages and 16 literal cache excerpts totaling 54,346 UTF-8 bytes. Validation checked each excerpt against its recorded byte interval. Actual PDF inspection resolved Thuillier's type-2 finite-extension condition, the all-domain interpolation statement, GJR 7.10's uniform-only conclusion, and CD's numbering as 17.8.2 in this cache.\n\nPrograms and rerun commands: python collect_sources.py; python finite_diagnostics.py > finite-diagnostics.stdout.txt; python build_documents.py > tex-build.stdout.txt; python verify_artifacts.py > artifact-validation.stdout.txt. Environment details are in environment.json: Python 3.12.14 and pdfTeX 1.40.26, TeX Live 2025/dev/Debian. No installation, external computation or heavy computation was used.\n\nBoth final runs of pdflatex -interaction=nonstopmode -halt-on-error P02.2-paper.tex exited zero. Their final diagnostics report a nine-page PDF, 214,150 bytes, with no reported warnings or overfull boxes. Actual stdout and logs are retained separately for both passes, together with tex-build-diagnostics.json.\n\nFinite diagnostics are exhaustive only for their stated finite inputs. On the graph with boundary vertices 0,3 and edges (0,1; length 1), (1,2; length 2), (1,2; length 3), (2,3; length 1), the exact Dirichlet values were q₁=−21/16 and q₂=−27/16. Their outgoing slope sums were respectively 1 and 2; adding 27/16 made the vertex values nonnegative. For the target x², dyadic interpolations, perturbation |x−1/2| and coefficients 2⁻ʲ, all 1,799 comparisons on the grid i/256 passed the stated monotonicity, majorization and error inequalities. These checks do not certify arbitrary targets, analytic realization, residue semiampleness, scalar extension or the original characterization.\n\nRemaining obligations: characterize all higher-dimensional good strict spaces for arbitrary classical psh functions or germs; handle nonsaturated local domains; construct and descend new approximants over nonclosed fields; resolve general sequence extraction without countable-density hypotheses; and establish the full necessary failure range, including the distinction between net and sequence formulations. The proper-fibre sufficient sector and boundary sequence obstruction do not complete those obligations. Candidate remains false. All mathematical notes are unverified drafts; successful execution and source identity checks do not establish their mathematical correctness.\n\nArtifacts: /workspace/research/campaigns/round-42/P02.2-public-source-decreasing-LFS/artifacts/codex-gsYJxq",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Published source versions and application checks

{
  "sources": [
    {
      "id": "GJR",
      "public_source": "https://arxiv.org/pdf/2111.05741",
      "pdf": "/workspace/research/shared-sources/GJR-2111.05741.pdf",
      "literal_extract": "/workspace/research/shared-sources/GJR-2111.05741.txt",
      "pdf_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "extract_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "actual_pdf_pages": [
        2,
        7,
        8,
        30,
        31,
        32,
        33,
        34,
        37,
        38,
        39,
        41,
        42,
        43,
        44,
        45,
        47,
        48,
        77,
        78,
        79,
        80
      ],
      "page_count": 87,
      "application_check": "Strict G-site and Definition 5.1; Example 5.3; residue models and linearity; 7.8--7.10; skeleton realization, slope-degree formula and harmonicity; 15.11 is a net.",
      "retained_pdf": "GJR-selected-pages.pdf",
      "literal_excerpts": [
        {
          "label": "strict PL definition and counterexample",
          "byte_start": 123456,
          "byte_end": 125672,
          "literal_text": "Definition 5.1. A function h: X → R is called piecewise Λ-linear or Λ-PL if there exists a\n                                                                                                    ×\nG-covering {XP i } of X such that for each i, there are finitely many λi j ∈ Λ and f i j ∈ O (X i )\nwith h|X i = j λi j log | f i j |. A Z-PL function is called piecewise linear or PL.\n  We denote the group of PL functions on X by PL(X ), and the group of Λ-PL functions\nby PLΛ (X ). These are subgroups of C(X ).\n5.2. Some remarks:\n   (1) A function h: X → R is PL if and only if there exists a G-covering {X i } of X and\n       f i ∈ O (X i )× such that h|X i = log | f i |.\n   (2) The set of Λ-PL functions on X forms a group since any two G-coverings {X i } and\n       {X ′j } admit the common refinement {X i ∩ X ′j }.\n   (3) The restriction of a Λ-PL function to a strictly analytic domain is Λ-PL.\n   (4) The presheaf U 7→ PLΛ (U) is a sheaf in the G-topology, and therefore in the ana-\n       lytic topology as well.\n   (5) A function h: X → R is Λ-PL if and only if there exists a G-covering {X i } of\n       X suchPthat for each i, there are finitely many λi j ∈ Λ and hi j ∈ PL(X i ) with\n       h|X i = j λi j hi j .\n   (6) A function h: X → R is Q-PL if and only if, locally in the analytic topology, there\n       exists a positive integer N such that N h is PL.\n   (7) If Λ = Z or Λ = Q then the minimum and maximum of two Λ-PL functions is\n       again Λ-PL by [GM19, Proposition 2.12(d)].\nExample 5.3. The assertion of 5.2(7) is not true for Λ strictly containing Q. For example,\nif the value group of K is Q and X = Gan m\n                                            = Spec(K[t ±1])an is the split torus of rank 1, then\nthe tropicalization of any strictly affinoid domain in X is a union of compact intervals with\nrational vertices. We conclude that for Λ = R, the function h := π log |t|+1 = −π trop +1\nis Λ-PL, but max(h, 0) is not Λ-PL as max(h, 0) = ϕ ◦ trop for ϕ(u) = max(−πu + 1, 0),\nand as the piecewise linear function ϕ has a bend at the irrational number 1/π.\n  Here we list some basic functoriality properties of Λ-PL functions.\n"
        },
        {
          "label": "LFS and fixed-germ uniform approximation",
          "byte_start": 186321,
          "byte_end": 190713,
          "literal_text": "Definition 7.8. Let h: X → R be an R-PL function. We say that h is Fubini–Study at a\npoint x ∈ X if Lh (x) is semiample. We say that h is locally Fubini–Study or LFS if it is\nFubini–Study at every point of X .\n  Clearly if h is Fubini–Study at x then it is semipositive at x.\n7.9. It follows from [CD12, Proposition 6.8.2] that h is Fubini–Study at x if and only if\nthere is an open neighbourhood U of x such that h|U is an R≥0 -linear combination of func-\ntions of the form max{− log | f1 |, . . . , − log | f n |} for invertible analytic functions f1 , . . . , f n\non U.\n  The following proposition can be seen as a local analogue of the fact that one can\napproximate a nef Q-line bundle by ample Q-line bundles on a projective variety.\nProposition 7.10. Let h: X → R be an R-PL function that is semipositive at a point x ∈\nInt(X ). Then there exists a strictly analytic neighbourhood U of x and a sequence h1 , h2 , . . .\nof R-PL LFS functions on U such that hi → h|U uniformly.\nProof. We may shrink X to assume it is compact. By Corollary 5.9, we may assume that\nthere exists a formal K ◦ -model X of X and a line bundle L ∈ M (X)R with h = hL , using\nthe notation of 5.7. Since x is inner, the closure VX,x of redX (x) in Xs is proper (with the\nnotation of 6.13): see [CD12, Lemma 6.5.1] and [Vil21, Appendix A]. By Chow’s lemma,\n\f48                               W. GUBLER, P. JELL, AND J. RABINOFF\n\nthere is a proper birational morphism V → VX,x with V projective over K              e . Let L ′ be an\n                                                                                ′\nample line bundle on V . By [CD12, 6.6.5], there is a PL function h on the germ (X , x)\nsuch that (V, L ′ ) is a model of the residue Lh′ (x). Let U be a compact strictly analytic\nneighbourhood of x on which h′ is defined. Then there is a formal K ◦ -model U of U and\na line bundle L′ on U with h′ = hL′ . By Lemma 6.14, there is a compact strictly analytic\nneighbourhood U ′ of x and a formal K ◦ -model U′ of U ′ such that the closure V ′ := VU′ ,x\nof redU′ (x) dominates V . We may assume that U ′ ⊂ U and that this inclusion extends to\na morphism f : U′ → U by using Raynaud’s theorem. Let L ′ |V ′ be the pull-back of L ′ with\nrespect to V ′ → V . Then L ′ |V ′ and f ∗ (L′ )|V ′ are both models for Lh′ (x). We conclude that\nthere is a dominating model V ′′ of red(X , x) such that the pull-backs of L ′ |V ′ and f ∗ (L′ )|V ′\nto V ′′ agree. Using Lemma 6.14 again and the arguments above, we may assume that\nV ′′ = VU′′ ,x for a formal K ◦ -model U′′ of a compact strictly analytic neighbourhood U ′′\nof x contained in U ′ such that the inclusion U ′′ ⊂ U ′ extends to a morphism U′′ → U′ .\nMoreover, we may assume that U ′′ ⊂ X extends to a morphism U′′ → X. Replacing X by\nU′′ and L, L′ by their pull-backs to U′′ , we put ourselves in the following situation:\n     (1) The closure V ′ of redX (x) in Xs dominates V .\n     (2) There is L ∈ M (X)R and L ∈ Pic(V )R such that h = hL and L|V ′ is the pullback of\n         L under V ′ → V , and such that (V, L) is a model of Lh (x).\n     (3) There is a line bundle L′ on X and an ample line bundle L ′ on V such that h′ = hL′\n         and L′ |V ′ is the pullback of L ′ under V ′ → V .\nWe recycle notation now and let U := red−1       X\n                                                     (V ′ ). By anticontinuity of the reduction map,\nthe set U is an open neighbourhood of x. For ǫ ∈ Q>0 let Lǫ := L + ǫ L ′ , Lǫ := L + ǫ L′ ,\nand hǫ := hLǫ = h + ǫh′ . Then hǫ is an R-PL function on X and Lǫ |V ′ is the pullback of Lǫ\nunder V ′ → V . Note that hǫ → h uniformly as ǫ → 0. If h is semipositive at x then L is\nnef by Lemma 6.11, so Lǫ is ample as a consequence of Kleiman’s theorem, see [Laz04,\nCorollary 1.4.10]. It follows that Lǫ |V ′ is semiample. If y ∈ U then redX ( y) ∈ V ′ , so the\nclosure Y of redX ( y) in Xs is contained in V ′ . Since h = hL and h′ = hL′ on all of X ,\nthe pair (Y, Lǫ |Y ) is a model of Lhǫ ( y) by the construction in 6.16. Since Lǫ |Y is again\nsemiample, we see that hǫ is Fubini–Study at y. Thus hǫ is LFS on U.                                 \u0003\n"
        },
        {
          "label": "strict skeleton realization and harmonicity",
          "byte_start": 301207,
          "byte_end": 310349,
          "literal_text": "15.2 (Skeletons of Curves). Metric graphs with boundary arise in non-Archimedean ge-\nometry as follows. Let X be a compact rig-smooth curve over K, i.e., a compact rig-smooth\nstrictly analytic space of pure dimension 1. We assume that X has a strictly semistable\nmodel X over the valuation ring K ◦ . This is a formal K ◦ -model of X (see 2.4) whose spe-\ncial fiber Xs is geometrically reduced with smooth irreducible components and at most\ndouble points as singularities. This is equivalent to [Thu05, Definition 2.2.8], where\nsuch models are called simplement semi-stable. To such a model is associated a weighted\nmetric graph with boundary Σ := S(X), called the skeleton of X. There is a canonical\ninclusion Σ ,→ X . The vertices of Σ correspond to the irreducible components of Xs and\nthe edges correspond to the singular points of Xs , so that Σ is the incidence graph of Xs .\nThe boundary ∂ Σ consists of the vertices of Σ corresponding to non-proper irreducible\ncomponents of Xs . If x ∈ Xs is a singular point with corresponding edge e, then the\nweight of e is defined to be w(e) = [Ke (x) : K\n                                              e ]. There is an étale neighbourhood of x of\nthe form Spf(K{X , Y }/(X Y − ̟)) for some ̟ ∈ K ◦◦ \\ {0}; the length of e is then defined\nto be v(̟). There is a canonical deformation retraction map τ: X → S(X).\n\n15.3 (Subdivisions of the Skeleton). Consider\n                                      p         a subdivision Σ′ of the skeleton Σ = S(X)\nsuch that all vertices of Σ′ are in Σ( Γ ). Vilsmeier [Vil21, Construction 2.6] has de-\nfined a canonical formal scheme X′ with generic fiber X and reduced special fiber, and a\ncanonical morphism ι : X′ → X extending IdX , such that for any edge e′ of Σ′ , the analytic\nsubdomain (τ)−1(e′ ) of X is the generic fiber of an open subset of X′ . Note that X′ is not\nnecessarily an admissible formal scheme, i.e. not necessarily of topologically finite type.\n\f78                             W. GUBLER, P. JELL, AND J. RABINOFF\n\nBy [Gub13b, Propositions 6.7 and 6.9], the formal scheme X′ is admissible if the value\ngroup Γ is discrete or if the vertices of Σ′ are contained in Σ(Γ ).\n15.4 (Piecewise Affine Functions on the Skeleton).\n                                             p         Let Σ = S(X) as in 15.2, let U be a\nsubgraph of Σ with vertices contained in Σ( Γ ), and let h: U → R be a piecewise (Z, Γ )-\nlinear function in the sense of 15.1. Passing to a subdivision of U, we may assume that\nh is (Z, Γ )-linear on each edge of U. The vertices of U induce a subdivision Σ′ of Σ; we\ndenote the associated formal K ◦ -model of X by X′ as in 15.3, with canonical morphism\nι : X′ → X. When Γ dense in R, we assume that all vertices of U are in Σ(Γ ); then\nX′ is an admissible formal scheme. The subset Y := τ−1 (U) is the generic fiber of a\nunique open formal subscheme Y′ in X′ . By the arguments used in the proof of [Vil21,\nProposition 2.11], there is a canonical vertical Cartier divisor D on Y′ with associated\nformal metric on OY determined by − log k1kO (D) = h ◦ τ. See 5.5.\nProposition 15.5. Let X be a compact rig-smooth curve over K and let h: X → R.\n     (1) If X is a strictly semistable model of X over K ◦ , then h = hL for a line bundle\n         L ∈ M (X) if and only if there is a function f : S(X) → R which is (Z, Γ )-linear on\n         each edge such that h = f ◦ τ.\n     (2) If x ∈ ∂ X , then h is harmonic at x if and only if h is R-PL at x.\nProof. The “if” part in (1) follows from 15.4. Conversely, assume that h = hL for L ∈\nM (X). Using the identification L|X = OX , the meromorphic section 1 of L induces a\nvertical Cartier divisor D on X. There is a covering of X by open subsets U such that S(U)\nis either an edge or a vertex of S(X) and such that D|U = div(γ) for some γ ∈ O (U)×,\nwhere U = Uη . It follows from [Ber99, Theorem 5.3 and Step 13 in its proof] that\nh|U = − log |γ| factorizes through a (Z, Γ )-linear function on S(U). This proves (1).\n   Since x ∈ ∂ X , the curve ∂ X is affine and hence the nef condition in Proposition 7.1 is\nvacuous. This proves (2).                                                                 \u0003\n15.6 (Thuillier’s Harmonic Functions). We consider now an arbitrary rig-smooth curve\nX over K. We call a function h: X → R harmonic in the sense of Thuillier if every x ∈ X\nhas a strictly affinoid neighbourhood V , a finite Galois extension K ′ /K, and a strictly\nsemistable model V′ of V ′ := V ⊗K K ′ , such that the pullback h′ of h|V factorizes through\nthe skeleton S(V′ ) and such that h′ |S(V′ ) is a harmonic function on the skeleton S(V′ )\nconsidered as a weighted metric graph with boundary as in 15.2.\n   For x ∈ ∂ X , Proposition 15.5 and Corollary 5.12 show that the above harmonicity\ncondition at x is equivalent to piecewise R-linearity at x, using that the boundary of\nS(X) is ∂ X . Note that Thuillier [Thu05, Section 2.3] used this definition only for strictly\naffinoid or boundaryfree X , so the above definition is slightly more general than his.\nProposition 15.7. Let X be a rig-smooth curve. Then a function h: X → R is harmonic in\nthe sense of Definition 7.2 if and only if h is harmonic in the sense of Thuillier.\nProof. The claim is local on X , so we may assume X strictly affinoid. We first show\nthat the harmonicity notions agree for a piecewise linear function h ∈ PL(X ). By 5.6,\nwe have that h = − log k1kL for a model L of OX on a formal K ◦ -model X of X . Using\nbase change, Proposition 7.6 and [Thu05, Remarque 2.3.17], we are free to pass to a\n\f              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                79\n\nfinite Galois extension of K. Arguing locally, the semistable reduction theorem ([Thu05,\nThéorème 2.3.8] under these hypotheses; see also [BL85, Section 7] and [Duc24, Theo-\nrem 5.1.14(iv), 6.1.3]) shows that we may assume that X is a strictly semistable model.\nBy Proposition 15.5, there is a function f on the skeleton S(X) which is (Z, Γ )-linear on\neach edge such that h = f ◦ τ. For x ∈ S(X) \\ ∂ X with corresponding proper irreducible\ncomponent C := redX (x) of Xs , it follows as in [KRZB16, Theorem 2.6] that the sum of\noutgoing slopes of f at x is equal to deg(L|C ). We conclude that h is harmonic in the\nsense of Thuillier if and only if L is numerically equivalent to 0. The latter is equivalent\nto harmonicity of h in the sense of Definition 7.2, as we have shown in Lemma 7.4.\n   Now we prove the proposition for any function h: X → R. Assume that h is a harmonic\nfunction on X as in Definition 7.2. By Proposition 7.5, the function h is locally an R-linear\ncombination of Z-harmonic functions, so we are reduced to the case handled above since\nthe set of Thuillier-harmonic functions forms a real vector space.\n   Conversely, let h be a harmonic function in the sense of Thuillier. We have to check\nfor any x ∈ X that h is harmonic at x. As above, we are free to pass to a finite Galois\nextension of X , so we may extend scalars and shrink X to assume that X has a strictly\nsemistable model X and that h factorizes through a harmonic function f : S(X) → R. It\nis enough to show that f is an R-linear combination of piecewise (Z, Γ )-linear harmonic\nfunctions f i on S(X). Indeed, by Proposition 15.5, we have that f i ◦ τ is piecewise linear,\nso f i ◦ τ is harmonic by the the first paragraph of this proof, and hence h is harmonic.\n   Suppose first that x ∈ ∂ X = ∂ S(X). After shrinking X, we may assume that S(X)\nis a star around the vertex x, so that f is affine R-linear on each edge. Translating by\na constant function, we may assume f (x) = 0. Then f is an R-linear combination of\npiecewise Z-linear functions f e on S(X): namely, the functions f e that have slope 1 on a\ngiven edge e and slope 0 on the others. Since x ∈ ∂ S(X), Proposition 15.5 yields that\neach f e is harmonic and hence h is harmonic.\n   If x ∈ X \\ ∂ X , then as above, we may assume that S(X) is either an edge containing\nτ(x) in its interior, or that S(X) is a star around the vertex τ(x). In the first case, f is\nan R-multiple of a (Z, Γ )-linear function on the edge, so h is harmonic. In the second\ncase, we may assume that f (τ(x)) = 0. Then f is harmonic if and only if f is linear on\neach edge and the weighted sum of the outgoing slopes at τ(x) is zero. This is a linear\nequation for the slopes which is defined over Q, so there is a basis of solutions defined\nover Q and even over Z. The elements f i of such a basis induce piecewise (Z, Γ )-linear\nfunctions f i which are harmonic on S(X). Since f is an R-linear combination of the f i ,\nwe have that h is harmonic.                                                                \u0003\n\n   Note that Γ is either dense inpR or is a discrete subgroup. In the following, we set\nΛ := Γ if Γ is dense and Λ := Γ (the divisible hull in R) if Γ is discrete. When Γ is\ndiscrete, we may rescale the valuation to assume Γ = Z.\n\n"
        },
        {
          "label": "regularization is a weakly smooth net",
          "byte_start": 312918,
          "byte_end": 316270,
          "literal_text": "Proposition 15.11. Let X be a smooth curve (a rig-smooth curve without boundary) over\na non-trivially valued non-Archimedean field K, and let f be a subharmonic function on X\nas defined in [Thu05, 3.1.2]. Then for any relatively compact open subset U of X , there is\na decreasing net of weakly smooth psh functions f i on U converging pointwise to f |U .\nProof. By Thuillier’s regularization theorem [Thu05, Théorème 3.4.2], there is a decreas-\ning net of piecewise R-linear subharmonic functions on U converging pointwise to f , so\nwe may assume that f is piecewise R-linear. (Note that piecewise R-linear functions are\ncalled lisse in [Thu05, Definition 3.2.1].) As in the proof of [Thu05, Theorem 3.4.2],\nwe may assume that U = Y \\ ∂ Y for a compact strictly analytic domain Y of X . By\n[Thu05, Proposition 3.2.4], there is a finite Galois extension K ′ /K such that Y has a\nstrictly semistable model Y over the valuation ring of K ′ and such that f = F ◦ τ for a\npiecewise R-linear function F on the skeleton S(Y), where τ: Y → S(Y) is the retraction.\nSince the subharmonic functions over K are the Galois-invariant subharmonic functions\nover K ′ and the same holds for weakly smooth functions, it is enough to prove the claim\nover K ′ , so we may assume K = K ′ .\n   Now we can follow Wanner’s arguments [Wan19, Lemma 5.2]. Note that the curvature\nddc ( f |U ) is a discrete measure on U; we denote by S its support. In what follows, we\nallow subdivisions of Σ := S(Y) at arbitrary points in Σ (not just type-II points); we do\nnot claim that the subdivision is the skeleton of a formal model of U. By subdividing the\n\f              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                 81\n\nskeleton, we may assume that Σ contains S, that F is affine on the edges of Σ, and that\nthe points of S are vertices of Σ. For a point x ∈ S, let Σ x be the union of all edges of\nΣ containing x. By further subdividing Σ, we may assume that Σ x ∩ S = {x}. Since x\nis in the support of ddc ( f |U ), the weighted sum of outgoing slopes of F in x is positive.\nThen there is a harmonic function G x ≤ F on Σ x , affine on each edge of Σ x , and with\nF ( y) = G x ( y) if and only if y = x. For ǫ > 0 sufficiently small, the regularized maximum\nmǫ as defined in [Wan19, 4.6] leads to a function\n                      fǫ := mǫ/2 (G x ◦ τ + ǫ, f ) = mǫ/2 (G x + ǫ, F ) ◦ τ\non τ−1 (Σ x ) which agrees with f over a neighbourhood of the boundary of Σ x and agrees\nwith G x ◦ τ + ǫ over a neighbourhood of x in Σ x . We conclude that the functions fǫ ,\nfor varying x S∈ S, can be glued to get a function fǫ defined on Y which agrees with f\non V := Y \\ x∈S τ−1 (Px ) for suitable compact neighbourhoods Px of x in relint(Σ x ).\nSince f is harmonic on U ∩ V by omitting S, we see that fǫ is harmonic on U ∩ V and\non a neighbourhood of S. Since the regularized maximum of two affine functions on a\nsegment is a convex smooth function, we see that fǫ is a smooth psh function over the\ninterior of each edge of any Σ x . Overall, it follows that fǫ is a weakly smooth psh function\non U. In the proof of [Wan19, Lemma 5.2], Wanner extracted from the functions fǫ a\ndecreasing sequence which converges pointwise to f , which proves the proposition. \u0003\n\n                "
        }
      ],
      "literal_segment_warning": "Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection."
    },
    {
      "id": "Thu",
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
      "literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "actual_pdf_pages": [
        36,
        40,
        41,
        42,
        57,
        58,
        65,
        66,
        67,
        68,
        70,
        71,
        72,
        81,
        82,
        83,
        84,
        103,
        104,
        105,
        106
      ],
      "page_count": 198,
      "application_check": "All-domain versus strict rigid sites; type classification; 2.2.22 and finite extension condition; harmonic functions; 3.2.1 all-domain lisse; 3.4.1--3.4.2 interpolation proof; 3.4.6 skeleton continuity; 3.4.10 polar points.",
      "retained_pdf": "Thu-selected-pages.pdf",
      "literal_excerpts": [
        {
          "label": "type-2 refinement, exact finite extension condition",
          "byte_start": 181875,
          "byte_end": 186332,
          "literal_text": "Lemme 2.2.22. \u0016 Soit X         une S - ourbe simplement semi-stable.\n   (i ) Étant donné un sous-ensemble \u001cni Σ ⊂ S(X ), il existe une extension non ar himédienne\nK/k et un é latement admissible Y → X ×S Spf(K ◦ ) tels que Y soit une Spf(K ◦ )- ourbe\nsimplement semi-stable et iK (Σ) ⊂ S0 (Y). L'extension K/k peut être hoisie \u001cnie (séparable)\nsi et seulement si tous les points de Σ sont de type (2).\n   (ii ) Étant donné un ensemble \u001cni Σ′ de points de type (2) ou (3) dans Xη , il existe une\nextension \u001cnie (séparable) k′ /k et un é latement admissible Y ′ → X ×S Spf(k′ ◦ ) tels que Y ′\nsoit une Spf(k′ ◦ )- ourbe simplement semi-stable et ik′ (Σ′ ) ⊂ S(Y ′ ).\nDémonstration. Traitons d'abord le as X = S(a).\n(i) On peut supposer que l'ensemble Σ est réduit à un point x.\n    Considérons une extension non ar himédienne K/k telle que |H(x′ )× | = |K × |, où x′ est le\npoint de S(S(a))K orrespondant à x dans l'identi\u001c ation anonique S(S(a))K = S(S(a)) ;\n  ette extension peut être hoisie si (et seulement si) x est de type (2).\n    Fixons b ∈ K × tel que |T0 (x′ )| = |b| ; |a| ≤ |b| ≤ 1 et l'é latement sur S ×S Spf(K ◦ ) de\nl'Idéal (T0 , b) \u0015 inversible en dehors du point singulier de S(a)s \u0015 donne lieu à un morphisme\nq : Z → S(a) ×S Spf(K ◦ ) tel que Z soit une Spf(K ◦ )- ourbe simplement semi-stable et\nS0 (Z) = S0 (S(a)) ∪ {x′ }.\n(ii) On peut de nouveau supposer Σ′ réduit à un point x. Si x ∈ S(S(a)), il n'y a rien\nà démontrer ; sinon, le point x′ = τ (x) de S(S(a)) est tel que s(x′ ) = 1 et on vient de\nprouver qu'il existe une extension \u001cnie k′ /k telle que le point de S(S(a))k′ orrespondant à\nx′ dans l'identi\u001c ation anonique S(S(a))k′ = S(S(a)) appartienne à S0 (S(a) ×S Spf(k′ ◦ )).\nOn est ainsi ramené au as d'un point x tel que τ (x) ∈ S0 (S(a)). L'appli ation de rédu tion\nS(a)η → S(a)s envoie x sur un point lisse x    e appartenant à la omposante irrédu tible de\npoint générique r(τ (x)).\n   Le omplémentaire E de la omposante onnexe non bornée de S(a)η − {x} ⊂ A1k − {x} est\nun disque fermé de point de Shilov x. Soit y un point dans E tel que l'extension κ(y)/k soit\n\u001cnie, de polyn\u001dme minimal f normalisé de telle sorte que |f (τ (x))| = 1 ; hoisissons également\nb ∈ k× tel que |f (x)| > |b|. L'Idéal I sur S(a) tel que Ixe = f OS(a),xe + bOS(a),xe et I = OS(a)\nsur S(a)s − {ex} est admissible et son é latement q : Z → S(a) fournit une S - ourbe Z dont\n\f44\n\n\n\nla \u001cbre spé iale est la somme amalgamée du diagramme\n\n                                          P1e\n                                              Ok\n                                          0\n\n                                        Spec(e\n                                             k)         e\n                                                        x\n                                                            / S(a)s ,\n\nqui devient simplement semi-stable après une extension \u001cnie k′ /k et telle que S(Z ×S Spf(k′ ◦ )\n ontienne le sous-ensemble ik′ (x).\n   Le as d'une ourbe simplement semi-stable quel onque se déduit dire tement de e qui\npré ède. On peut en e\u001bet supposer que X est munie d'un morphisme étale p : X → S(a) ar\nla question est lo ale sur Xη .\n   Étant donnée une extension non-ar himédienne (resp. une extension \u001cnie) K/k telle\nqu'il existe un é latement admissible q : Z → S(a) ×S Spf(K ◦ ) satisfaisant à la ondition\niK (pη (Σ)) ⊂ S0 (Z) (resp. iK (Σ) ⊂ S(Z)), l'é latement admissible q ′ : Y → X ×S Spf(K ◦ )\ndé\u001cni par le diagramme artésien\n                                          q′\n                                    Y               / X ×S Spf(K ◦ )\n\n                                                                 p\n                                    \u000f                        \u000f\n                                    Z              / S(a) ×S Spf(K ◦ )\n                                              q\n\nfournit une S - ourbe simplement semi-stable Y telle que iK (Σ) ⊂ S0 (Y) (resp. iK (Σ) ⊂\nS(Z ′ )).\n  L'extension K/k peut être hoisie \u001cnie si tous les points de pη (Σ) sont de type (2), don si\ntous les points de Σ sont de type (2).\n     Toutes les extensions \u001cnies peuvent être hoisies séparables.                             2\n   La proposition suivante sera utilisée au hapitre 3 ( f. théorème 3.2.10).\n"
        },
        {
          "label": "all-domain lisse definition",
          "byte_start": 270655,
          "byte_end": 272298,
          "literal_text": "Définition 3.2.1. \u0016 Soit Ω ⊂ X un ouvert.\n   (i ) Une fon tion réelle ϕ ∈ C (Ω, R) est dite lisse s'il existe un re ouvrement lo alement\n                           0\n\n\u001cni V de Ω par des domaines k-a\u001enoïdes Y tel que ϕ|Y ∈ H(Y ). L'ensemble des fon tions\nlisses sur Ω est un sous-espa e ve toriel de C0 (Ω, R), noté A0 (Ω).\n   (ii ) On désigne par A1 (Ω) l'espa e ve toriel des mesures réelles sur Ω dont le support est\nun sous-ensemble lo alement \u001cni de I(Ω). Les éléments de A1 (Ω) seront appelés formes lisses\n(sur Ω).\n\n  (iii ) Le sous-espa e ve toriel de A0 (Ω) (resp. A1 (Ω)) onstituté des fon tions (resp. me-\nsures) dont le support est ompa t se note A0c (Ω) (resp. A1c (Ω)).\n\n   La orrespondan e Ω 7→ A0 (Ω) est un sous-fais eau du fais eau CX\n                                                                  0 des germes de fon tions\n\nréelles ontinues sur X .\n   La dé\u001cnition du fais eau A0X s'étend d'elle même au G-site XG de X : il su\u001et, pour tout\nobjet V de XG , de dé\u001cnir A0 (V ) omme le sous-espa e ve toriel de C0 (V, R) onstitué des\nfon tions ϕ ontinues sur V qui satisfont à la ondition suivante : tout point x ∈ V possède\nun voisinage k-a\u001enoïde W ⊂ V tel que ϕ|W ∈ H(W ). Désignant par A0X le fais eau ainsi\ndé\u001cni sur XG et notant π : XG → |X| le morphisme de sites anonique, l'identité\n                                         A0X = π∗ A0X\nest évidente. La proposition suivante l'est tout autant.\n\nProposition 3.2.2. \u0016 L'homomorphisme            anonique de préfais eaux HX → A0X sur le site\nXG identi\u001ce A0X au fais eau asso ié à HX .\n\n"
        },
        {
          "label": "interpolation, monotonicity and convergence proof",
          "byte_start": 340149,
          "byte_end": 344111,
          "literal_text": "Lemme 3.4.1. \u0016 L'appli ation\n\n                               SH(X) → D0 (X),         u 7→ u|I(X)\nest inje tive et son image est l'ensemble des ourants T ∈ D0 (X) satisfaisant à la ondition\nsuivante :\n              pour tout domaine k-a\u001enoïde V ⊂ X et tout point x ∈ I(V ) − ∂V ,\n                                        T (x) ≤ hT, νxV i.\nDémonstration. Soient u une fon tion sous-harmonique sur X et x un point dans X − I(X).\n  Étant donnée une suite dé roissante (Vn ) de domaines k-a\u001enoïdes de X dont le bord de\nShilov Γ(Vn ) est réduit à un point xn et telle que\n                                                 \\\n                                         {x} =      Vn ,\n                                                  n\n\nle prin ipe du maximum (proposition 3.1.11) implique les inégalités u|Vn ≤ u(xn ) ; la suite\n(u(xn )) est don dé roissante et u(x) ≤ inf n u(xn ). D'autre part, en vertu de la semi- ontinuité\nsupérieure de u,\n                              u(x) ≥ limsupn u(xn ) = inf u(xn ).\n                                                         n\nLa fon tion u est ainsi uniquement déterminée par sa restri tion au sous-ensemble I(X) de\nX.\n  La des ription de l'image de l'appli ation SH(X) → D0 (X) est une appli ation dire te du\npoint (ii) du orollaire 3.3.9.                                                           2\n  Le lemme pré édent nous permettra de ne pas distinguer une fon tion sous-harmonique sur\nX du ourant de degré 0 qu'elle détermine.\n   Une fon tion sous-harmonique sur une surfa e de Riemann est, lo alement, l'enveloppe in-\nférieure d'une famille dé roissante de fon tions sous-harmoniques lisses ([19℄, Theorem 2.5.5).\nCette assertion est également vraie dans un ontexte non ar himédien, la démonstration en\nétant qui plus est élémentaire.\nThéorème 3.4.2. \u0016 Soient Ω un ouvert d'une           ourbe stri tement k-analytique lisse X et\nu ∈ SH(Ω). Pour tout ouvert relativement ompa t Ω′ ⊂ Ω, la restri tion de u à Ω′ est\nl'enveloppe inférieure d'une famille dé roissante de fon tions sous-harmoniques lisses.\nDémonstration. On peut supposer que l'ouvert relativement ompa t Ω′ ⊂ Ω est de la forme\nY − ∂Y , Y ⊂ X étant un domaine k-analytique ompa t.\n   Étant donné un sous-ensemble \u001cni S ⊂ I(Y ) ontenant ∂Y , dé oule des propositions 3.1.19\net 3.1.20 l'existen e d'une unique fon tion uS appartenant à A0 (Y ), harmonique sur Y − S\net oïn idant ave u sur S .\n\f90\n\n\n\n   La sous-harmoni ité de u sur Y − S implique l'inégalité u|Y ≤ uS ; par suite, pour tout\nsous-ensemble \u001cni S ′ de I(Y ) ontenant S , uS majore uS ′ sur le bord S ′ de Y − S ′ et uS ′ ≤\nuS , en vertu du prin ipe du maximum (proposition 3.1.1) appliqué aux fon tions uS et uS ′ ,\nharmoniques sur Y − S ′ . La famille (uS )S est don dé roissante.\n   La fon tion lisse uS est sous-harmonique sur Y −∂Y . Soient en e\u001bet V ⊂ Y −∂Y un domaine\nk-a\u001enoïde et h une fon tion dans H(V ) qui majore uS sur ∂V . Puisque u|Y ≤ uS , h majore\na fortiori u sur ∂V , et don sur tout V par sous-harmoni ité ; omme u et uS oïn ident sur\nS , il s'ensuit que h majore u sur le bord S ′′ = (S ∩ V ) ∪ ∂V de l'ouvert V − S ′′ . Une nouvelle\nappli ation du prin ipe du maximum aux fon tions harmoniques h|V −S ′′ et (uS )|V −S ′′ fournit\nalors l'inégalité\n                                               uS ≤ h\nsur V .\n   La famille (uS )S \u0015 S par ourant l'ensemble \u001cltrant des parties \u001cnies de I(Y ) ontenant\n∂Y \u0015 est minorée en tout point de I(X) ; son enveloppe inférieure u est don une fon tion\nsous-harmonique sur X (proposition 3.1.8). La démonstration s'a hève en invoquant le lemme\n3.4.1 : les fon tions sous-harmoniques u et u|Y −∂Y , trivialement égales sur I(Y ) − ∂Y , sont\nidentiques.                                                                                  2\n"
        },
        {
          "label": "skeleton continuity",
          "byte_start": 348700,
          "byte_end": 350788,
          "literal_text": "Proposition 3.4.6. \u0016 Soient X           une S - ourbe simplement semi-stable et u une fon tion\nsous-harmonique sur Xη ;\n   \u0015 la restri tion U de u au squelette S(X ) de X est une fon tion réelle sous-harmonique (=\n      onvexe ) ontinue ;\n   \u0015 u ≤ U ◦ τX .\nDémonstration. L'inégalité u ≤ U ◦ τX est une onséquen e immédiate du prin ipe du\nmaximum puisque les \u001cbres de la rétra tion τX sont des domaines k-a\u001enoïdes dont le bord\nest réduit à un point.\n   La restri tion U de u au squelette S(X ) est à valeurs \u001cnies ar S(X ) ⊂ I(Xη ) et, ompte\ntenu du théorème 3.4.2, U est l'enveloppe inférieure d'une famille dé roissante de fon tions\nqui sont les restri tions de fon tions lisses et sous-harmoniques sur Xη . Il est par onséquent\nsu\u001esant de prouver qu'une fon tion lisse et sous-harmonique ϕ sur Xη se restreint en une\nfon tion a\u001ene par mor eaux et sous-harmonique sur le polyèdre S(X ).\n   Nous pouvons supposer la ourbe quasi- ompa te puisque la question est lo ale sur S(X ) ;\nl'assertion sera d'autre part démontrée si elle l'est après passage à une extension \u001cnie k′ de k.\nAppliquant la proposition 3.2.4 et le lemme 2.2.22, il existe dans es onditions un é latement\nadmissible q : Y → X tel que :\n   \u0015 Y soit une S - ourbe simplement semi-stable,\n   \u0015 ϕ = Φ ◦ τY , ave Φ = ϕ|S(Y) ∈ A0 (S(Y)).\n   La fon tion Φ est sous-harmonique puisque ddc Φ = ddc ϕ ≥ 0 (théorème 3.2.10).\n\f92\n\n\n\n  D'après la proposition 2.2.26, S(X ) est un domaine polyédral dans S(Y) tel que haque\n omposante onnexe de S(Y)−S(X ) n'ait qu'un seul point frontière. Il en dé oule tout d'abord\nque la restri tion Φ′ de ϕ à S(X ) est une fon tion ontinue et a\u001ene par mor eaux puisque\nΦ′ = Φ|S(X ) . C'est en outre une fon tion sous-harmonique : Φ est en e\u001bet dé roissante au\nvoisinage de la frontière de S(Y) − S(X ) en vertu du prin ipe du maximum, e qui implique\n                                        ddc Φ′ ≥ ddc Φ ≥ 0.\n                                                                                                  2\n"
        }
      ],
      "literal_segment_warning": "Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection."
    },
    {
      "id": "GR-classical",
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "actual_pdf_pages": [
        6,
        7,
        10,
        11,
        12,
        20,
        21,
        22,
        23,
        30,
        31
      ],
      "page_count": 40,
      "application_check": "Classical curve-test class includes minus infinity; extension and pullback; boundary extension in 3.5(3); 4.3 strict real-PL comparison; 6.1 maximum principle.",
      "retained_pdf": "GR-classical-selected-pages.pdf",
      "literal_excerpts": [
        {
          "label": "boundary extension and scalar compatibility",
          "byte_start": 37296,
          "byte_end": 40515,
          "literal_text": "Proposition 3.5. Let X be a k-analytic curve and let u: X → R ∪ {−∞} be an upper\nsemicontinuous function.\n   (1) (Sheafiness) The subharmonic functions form a sheaf on X .\n   (2) (Analytic functions) If f ∈ Γ (X , OX ) then log | f | : X → R ∪ {−∞} is subharmonic.\n   (3) (Boundaries) If u is subharmonic on Int(X ), then u is subharmonic on X .\n   (4) (Cone Property) If u1 , u2 : X → R ∪ {−∞} are subharmonic and λ1 , λ2 ∈ R≥0 then\n       λ1 u1 + λ2 u2 and max{u1 , u2 } are subharmonic.\n   (5) (Limits) The infimum of a decreasing net of subharmonic functions is subharmonic.\n   (6) (Maximum Principle) If u is subharmonic and u attains a local maximum at x ∈\n       Int(X ), then u is constant in a neighborhood of x.\n   (7) (Extension of scalars) Let k′ /k be an analytic extension field. Then u is subharmonic\n       if and only if u ◦ πk′ /k : X k′ → R ∪ {∞} is subharmonic.\n   (8) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If u\n       is subharmonic then u ◦ f is subharmonic, and the converse holds if f is finite and\n       surjective.\n   (9) (Finite Values) If u is subharmonic and u(x) = −∞ for a non-rig-point x ∈ X ,\n       then u ≡ −∞ on the irreducible component of Int(X ) ∪ {x} containing x.\n  Let us make some remarks regarding the content of Proposition 3.5.\n3.5.1. If U ⊂ X is an open subset then U is again a k-analytic curve, so it makes sense\nto speak of subharmonic functions on U. It is immediate from the definition that a sub-\nharmonic function on X restricts to a subharmonic function on U. Hence subharmonic\nfunctions form a presheaf on X . Proposition 3.5(1) asserts that this presheaf is a sheaf.\n3.5.2. The maximum principle (Proposition 3.5(6)) is [Thu05, Proposition 3.4.10] in the\nsmooth, strictly analytic case.\n3.5.3. In the situation of Proposition 3.5(7), it is immediate from Definition 3.4 that\nu ◦ πk′ /k is subharmonic when u is subharmonic. This is the difficult direction in the\nsmooth, strictly analytic case: see [Thu05, Corollaire 3.4.5]. This result is hidden in the\n\f12                                 W. GUBLER AND J. RABINOFF\n\nfact that Definition 3.4 essentially recovers Thuillier’s definition of subharmonicity in that\ncase 3.4.1.\n3.5.4. In the situation of Proposition 3.5(8), it is immediate from Definition 3.4 that u◦ f\nis subharmonic when u is subharmonic. The remark in 3.5.3 applies to a lesser extent in\nthis case: see [Thu05, Proposition 3.1.14].\n3.5.5. For any x ∈ X , the subset Int(X )∪{x} is open in X . This is obvious if x ∈ Int(X ), and\nif x ∈ ∂ X then it follows from the fact that ∂ X is discrete in X . In particular, Int(X ) ∪ {x}\nis again a k-analytic curve, so it makes sense to speak of its irreducible components\nin Proposition 3.5(9). Irreducible components can only meet at rig-points (their inter-\nsections are Zariski-closed), so a non-rig-point x is contained in a unique irreducible\ncomponent of Int(X ) ∪ {x}; this is implicit in Proposition 3.5(9).\n3.5.6. Proposition 3.5(9) implies that if u is subharmonic and u(x) = −∞ for a non-rig-\npoint x ∈ X , then u ≡ −∞ in a neighborhood of x.\n"
        },
        {
          "label": "classical class and strict real-PL comparison",
          "byte_start": 78902,
          "byte_end": 86618,
          "literal_text": "Definition 4.1 (Classically Plurisubharmonic Functions). Let X be a k-analytic space and\nlet u: X → R ∪ {−∞} be an upper semicontinuous function. We say that u is classically\nplurisubharmonic or classically psh provided that, for every analytic extension field k′ /k,\nevery k′ -analytic curve Y , and every morphism f : Y → X k′ , the function u◦πk′ /k ◦ f : Y →\nR ∪ {−∞} is subharmonic on Y in the sense of Definition 3.4.\n4.1.1. Any class of psh functions should respect extension of scalars and should be stable\nunder pullback, so the conditions in Definition 4.1 are necessary. In complex analysis,\nthis condition (without the extension of scalars) is the definition of plurisubharmonicity,\nwhich is why we call the notion “classically psh”.\n4.1.2. If X is a k-analytic curve, then a function u: X → R∪{−∞} is classically psh if and\nonly if it is subharmonic. Indeed, if u is classically psh then taking k′ = k and Y = X in\nDefinition 4.1 shows that u is subharmonic, and if u is subharmonic then it is classically\npsh by Proposition 3.5(7,8).\n4.1.3. In Definition 4.1, one can assume that Y is a connected, smooth, strictly k′ -analytic\ncurve: this follows from Definition 3.4.\n  Classically psh functions satisfy the basic properties of subharmonic functions on curves.\nProposition 4.2. Let X be a k-analytic space.\n   (1) (Sheafiness) The classically psh functions form a sheaf on X .\n   (2) If f ∈ Γ (X , OX ) then log | f |: X → R ∪ {−∞} is classically psh.\n   (3) (Cone Property) If u1 , u2 : X → R∪{−∞} are classically psh and λ1 , λ2 ∈ R≥0 then\n       λ1 u1 + λ2 u2 and max{u1 , u2 } are classically psh.\n   (4) (Limits) The infimum of a decreasing net of classically psh functions is classically\n       psh. For arbitrary pointwise limits, we refer to Theorem 6.5.\n   (5) (Extension of Scalars) Let k′ /k be an analytic extension field. A function u: X →\n       R ∪ {−∞} is classically psh if and only if u ◦ πk′ /k : X k′ → R ∪ {−∞} is classically\n       psh.\n   (6) (Functoriality) Let Y be a k-analytic space and let f : Y → X be a morphism. If\n       u: X → R ∪ {−∞} is classically psh then u ◦ f is classically psh, and the converse\n       holds if f is finite and surjective.\nProof. Properties (1,3,4) follow immediately from Proposition 3.5(1,4,5). For Proposi-\ntion 4.2(2), we consider an analytic function f on X . As | f | is continuous, we deduce\n\f22                                  W. GUBLER AND J. RABINOFF\n\nthat log | f | is a continuous function with values in R ∪ {−∞} and hence it is upper semi-\ncontinuous. Then Proposition 4.2(2) follows from Proposition 3.5(2).\n    To prove Proposition 4.2(5), it is clear from the definitions that if u is classically psh,\nthen u ◦ πk′ /k is classically psh for every analytic extension field k′ /k. To prove the con-\nverse, we assume that k′ /k is an analytic extension field and that u′ := u ◦ πk′ /k is a\nclassically psh function on X k′ . Since the morphism πk′ /k is closed and surjective 2.9,\nit is clear that u is upper semicontinuous. Let k′′ /k be an analytic extension field and\nlet f : Y → X k′′ be a morphism over k′′ from a k′′ -analytic curve Y . We have to show\nthat u ◦ πk′′ /k ◦ f is subharmonic. As in the proof of Proposition 3.5(7), we consider\na simultaneous analytic extension field K of k′ and k′′ . It follows from the above that\nu ◦ πK/k = u′ ◦ πK/k′ is classically psh and hence u ◦ πK/k ◦ f K is subharmonic. We con-\nclude from the commutative diagram (3.10.1) that u ◦ πK/k ◦ f K = u ◦ πk′′ /k ◦ f ◦ πK/k′′ is\nsubharmonic and hence u ◦ πk′′ /k ◦ f is subharmonic by Proposition 3.5(7).\n    Likewise, the proof of Proposition 4.2(6) follows the same lines as the proof of Propo-\nsition 3.5(8). Again, it follows from the definitions if u is a classically psh function on X ,\nthen u ◦ f is a classically psh function on Y . Conversely, we assume that u ◦ f is a clas-\nsically psh function for a finite surjective morphism f : Y → X . Since finite morphisms\nare proper and hence closed, we deduce from upper semicontinuity of u ◦ f and from\nsurjectivity of f that u is upper semicontinuous. It remains to show that u ◦ πk′ /k ◦ g is\nsubharmonic for any analytic extension field k′ /k and any morphism g : Z → X k′ from a\nconnected k′ -analytic curve Z. Setting W := Z ×X k′ Yk′ , we get a morphism g ′ : W → Yk′\nfrom f by base change with respect to f ′ : Yk′ → X k′ as in (3.10.2). Since u ◦ f is classi-\ncally psh, it follows from Proposition 4.2(5) that u ◦ πk′ /k ◦ f ′ = u ◦ f ◦ πk′ /k is classically\npsh. The morphism f is finite and surjective, hence the same holds for f ′ . We con-\nclude that the base change f ′′ : W → Z of the morphism f ′ is finite and surjective. The\nk′ -analytic space W has irreducible components of dimension 1 and maybe isolated irre-\nducible components of dimension 0. Removing the latter, we obtain a k′ -analytic curve\nW ′ as an open and closed subset of W . Since Z is a connected k′ -analytic curve and f ′′\nis a finite surjective map from W onto Z, we get an induced finite surjective morphism\nW ′ → Z. Indeed, as W ′ is also Zariski-closed in W , we deduce from finiteness of f ′′ that\nf ′′ (W ′ ) is a Zariski-closed subset in Z of dimension 1 and hence f ′′ (W ′ ) = Z as Z is a\nconnected k′ -analytic curve. Since the inclusion W ′ → W is obviously finite, the com-\nposition W ′ → Z is also finite. In the following, we replace W by W ′ , which preserves\nthe commutativity of the diagram (3.10.2) and has the advantage that W is a k′ -analytic\ncurve. It follows that u ◦ πk′ /k ◦ f ′ ◦ g ′ = u ◦ πk′ /k ◦ g ◦ f ′′ is subharmonic on W . The\nmorphism of k′ -analytic curves f ′′ : W → Z is finite and surjective, so we deduce from\nProposition 3.5(8) that u ◦ πk′ /k ◦ g is subharmonic.                                           □\n\n  In the paper [GR25], we have studied semipositive R-PL functions on a good strictly\nk-analytic space over a non-trivially valued non-archimedean field k. This turns out to\nbe the same as an R-PL function that is classically psh, as we now show.\n\nTheorem 4.3. Suppose that the valuation on k is nontrivial. Let X be a good, strictly k-\nanalytic space and let h: X → R be an R-PL function. Then h is semipositive if and only if h\nis classically psh.\n\f              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                  23\n\nProof. For x ∈ X , an R-PL function h: X → R induces a residue line bundle Lh (x) ∈\nPic(red(X , x))R on the reduction red(X , x) of the germ (X , x): see 2.17. Recall from\n[GJR21, Definition 7.2] that h is semipositive at x ∈ X if and only if the associated residue\nline bundle Lh (x) is nef. We have shown in [GR25, Proposition 3.1] that for a smooth\nstrictly k-analytic curve, an R-PL function is semipositive if and only if it is subharmonic.\nSince semipositivity is stable under base extension and pull-back [GJR21, Proposition\n7.6], we conclude that a semipositive R-PL function on X is classically psh.\n   The converse follows from [GR25, Corollary 3.5], which shows that an R-PL function h\non X is semipositive if and only if there is an algebraically closed analytic extension field\nF of k such that for every smooth F -analytic curve C and every morphism ϕ : C → X F ,\nwe have h ◦ ϕ semipositive.                                                                □\n                                 "
        },
        {
          "label": "maximum principle",
          "byte_start": 114888,
          "byte_end": 117653,
          "literal_text": "Theorem 6.1 (Local Maximum Principle). Let X be a k-analytic space and let u be a clas-\nsically psh function on X . If u has a local maximum at x ∈ Int(X ), then u is locally constant\nat x.\nProof. We may replace X by a connected, Hausdorff open neighborhood of x in Int(X ) to\nassume that X is connected and boundaryless and that u attains a global maximum at x.\nLet R = u(x). Let Γ be a connected, overconvergent analytic curve in X containing x. We\nclaim that u ≡ R on Γ . Consider the set Γu=R = {z ∈ Γ | u(z) = R}. This set is closed in Γ\nby upper semicontinuity of u, so since Γ is connected, it suffices to show that Γu=R is open\nin Γ .\n   By 5.1.3, there exist an analytic extension field k′ /k, a compact, separated strictly k′ -\nanalytic space C of dimension at most 1, a separated strictly k′ -analytic space C ′ of dimen-\nsion at most 1, and morphisms ψ: C → C ′ and ϕ ′ : C ′ → X k′ , such that ψ(C) ⊂ Int(C ′ )\nand πk′ /k ◦ ϕ(C) = Γ , where ϕ = ϕ ′ ◦ ψ. The composition u ◦ πk′ /k ◦ ϕ ′ is subharmonic\non 1-dimensional connected components of C ′ because u is classically psh.\n   Let y ∈ Γu=R , let z ∈ C be a point lying over y, and let z ′ = ψ(z) ∈ Int(C ′ ), so that\nR = u ◦ πk′ /k ◦ ϕ ′ (z ′ ) = u ◦ πk′ /k ◦ ϕ(z). If {z ′ } is a connected component of C ′ then clearly\nu ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood of z ′ . Otherwise, the connected component of z ′\nin C ′ is a strictly k′ -analytic curve, in which case u ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood\nof z ′ by Proposition 3.5(6) (here we use z ′ ∈ Int(C ′ )). Taking the ψ-inverse image of\nsuch a neighborhood, we see that u ◦ πk′ /k ◦ ϕ ≡ R in a neighborhood of z. Applying\nthis argument to each z ∈ (πk′ /k ◦ ϕ)−1 ( y), we construct an open set V ⊂ C containing\n(πk′ /k ◦ ϕ)−1 ( y) such that u ◦ πk′ /k ◦ ϕ|V ≡ R.\n   The complement C \\ V is a closed subset of the compact space C, so it is a compact\nsubset of C that is disjoint from (πk′ /k ◦ ϕ)−1 ( y). Its image is a compact subset of X that\ndoes not meet y, so there is an open neighborhood W of y such that (πk′ /k ◦ϕ)−1 (W ) ⊂ V .\n\f              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                     31\n\nIt follows that u ≡ R on W ∩ Γ . This proves that Γu=R is open in Γ . As remarked above,\nthis yields u ≡ R on Γ .\n   Let y ∈ X be any point. By Theorem 5.4, there is a connected, overconvergent analytic\ncurve Γ in X containing x and y. We showed above that u ≡ R on Γ , so that u( y) = R.\nAs y was arbitrary, we have u ≡ R on X .                                              □\n\n  "
        }
      ],
      "literal_segment_warning": "Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection."
    },
    {
      "id": "GR-PL",
      "public_source": "https://arxiv.org/pdf/2503.05513",
      "pdf": "/workspace/research/shared-sources/GR-2503.05513-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/GR-2503.05513-20261004.txt",
      "pdf_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "extract_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "actual_pdf_pages": [
        1,
        15,
        16,
        17
      ],
      "page_count": 26,
      "application_check": "Cached v1 has the curve comparison as Proposition 5.1, not Proposition 3.1 cited by the later paper.",
      "retained_pdf": "GR-PL-selected-pages.pdf",
      "literal_excerpts": [
        {
          "label": "cached-version curve comparison",
          "byte_start": 57317,
          "byte_end": 59542,
          "literal_text": "Proposition 5.1. Let X be a smooth, strictly k-analytic curve and let u: X → R be an R-PL\nfunction. Then u is subharmonic at x ∈ X in the sense of Thuillier if and only if Lu (x) is nef.\n\nProof. First we treat the case when k is algebraically closed. As explained in 2.5, there\nexists a compact strictly analytic neighborhood U of x in X , a formal k◦ -model U of U,\nand a formal model L of OU such that u|U = hL . Since k is algebraically closed, we may\nassume that the special fiber Us is reduced, which implies that U is covered by formal\naffines of the form Spf(A ◦ ) for a strictly k-affinoid algebra A [GJR21, §2.4]. It follows\nfrom [Ber90, Proposition 2.4.4] that for every irreducible component Y of Us , there is a\nunique point ξY ∈ U reducing to the generic point of Y . In the formalism of real valued\nforms and currents on Berkovich spaces [CD12], it is well known that d′ d′′ [u]|U is the\ndiscrete measure on U supported on the points ξY of U for Y an irreducible component\nof Us , with multiplicity at ξY equal to degL (Y ). See [CD12, §6.9] for a more general\nstatement. Wanner showed that subharmonicity of u on U is equivalent to the positivity\nof the current d′ d′′ [u]: see [Wan19, Theorems 1 and 2] and use the fact that X is locally\nalgebraic [vdP80]. Thus Ls is nef if and only if u is subharmonic on U. Suppose that u is\nsubharmonic at x. Shrinking U, we may assume that u is subharmonic on U. This implies\nthat Ls is nef, so it follows from [GJR21, Proposition 7.1] that Lu (x) is nef. Conversely, if\nLu (x) is nef, then by [GJR21, Proposition 7.1], we may shrink U so that Ls is nef, which\nas above implies that u is subharmonic on U.\n   It remains to show that subharmonicity of u at x and numerical effectivity of Lu (x)\ncan be checked after extending scalars to the completion of an algebraic closure K =\n(k)∧ . By [GJR21, Proposition 7.6(2)], one can check that Lh (x) is nef after base change\nto K. The same is true for subharmonicity: this follows directly from Thuillier’s definition\nand the fact that the base change of a harmonic function remains harmonic [Thu05,\nProposition 2.3.18].                                                                       \u0003\n\n  "
        }
      ],
      "literal_segment_warning": "Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection."
    },
    {
      "id": "Wanner",
      "public_source": "https://arxiv.org/pdf/1801.04713v3",
      "pdf": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "pdf_sha256": "8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7",
      "extract_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "actual_pdf_pages": [
        1,
        28,
        29,
        30,
        31
      ],
      "page_count": 32,
      "application_check": "Corollary 5.4 assumes continuous finite targets and the stated residue or curve alternatives; its Dini extraction is not used.",
      "retained_pdf": "Wanner-selected-pages.pdf",
      "literal_excerpts": [
        {
          "label": "exact continuous-target corollary and proof",
          "byte_start": 117681,
          "byte_end": 119431,
          "literal_text": "Corollary 5.4. Let X be a smooth proper curve over K. If K    e is algebraic over a finite\nfield or X is the projective line or a Mumford curve, then every continuous psh function\nf : W → R on an open subset W of X an is locally psh-approximable. More precisely, the\nsequence of smooth psh functions can be chosen monotonically decreasing.\nProof. At first, note that in the given situation HX is a subsheaf of C ∞ on X an , which\nis a consequence of [Thu05, Théorème 2.3.21] (see [Wan16, Corollary 5.3.21]). We ad-\nditionally use [Ber90, Theorem 4.4.1] in the case of a Mumford curve. Hence, we may\napply Lemma 5.2.\n   To prove the corollary, we have to show that every point x in W has an open neigh-\nborhood in W such that f is a uniform limit of smooth psh functions. The continuous\npsh function f is subharmonic by Theorem 4.7, and we therefore can use Thuillier’s\nmonotone regularization theorem (see Proposition 2.8). We can find for every x ∈ W a\nrelatively compact neighborhood W ′ of x in W and a decreasing net hfj i of lisse subhar-\nmonic functions on W ′ converging pointwise to f . Let Y be a strictly affinoid domain\nin W ′ having x in its interior Y ◦ . Then the decreasing net hfj i converges uniformly to\nthe continuous function f on the compact set Y by Dini’s theorem. Thus, one can con-\nstruct inductively a decreasing sequence of lisse subharmonic functions on W ′ converging\nuniformly to f on Y and we write (fk )k∈N for this sequence.\n   We have seen in Lemma 5.2 that each fk is the uniform limit of a decreasing sequence\nof smooth psh functions on Y ◦ . Hence, we can choose a decreasing sequence of smooth\npsh functions on Y ◦ converging uniformly to f .                                        \u0003\n"
        }
      ],
      "literal_segment_warning": "Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection."
    },
    {
      "id": "Berkovich",
      "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
      "literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
      "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "actual_pdf_pages": [
        31,
        32,
        48,
        50,
        51,
        125,
        126
      ],
      "page_count": 158,
      "application_check": "Actual PDF pages 51 and 125 contain 2.6.9 and 7.1.1; properness and H_c^0 comparison give analytic connectedness of proper factors.",
      "retained_pdf": "Berkovich-selected-pages.pdf",
      "literal_excerpts": [
        {
          "label": "proper analytification",
          "byte_start": 148715,
          "byte_end": 148950,
          "literal_text": "2.6.9. Proposition. — Let 9 : 3£ -> W be a morphism of finite type between schemes of\nlocally finite type over °K. Then 9 is proper (resp. finite, resp, a closed immersion) if and only if 9^\npossesses the same property. •\n\n      "
        },
        {
          "label": "compact-support comparison and proof",
          "byte_start": 343412,
          "byte_end": 347612,
          "literal_text": "7 . 1 . 1 . Theorem. — Let S£ be a compactifiable scheme over k, and let 3^ he an abelian\ntorsion sheaf on St'. Then for any q ^ 0 there is a canonical isomorphism\n\n                   H^, y} ^ ny, ^an).\n\n       Proof. — Let 9 : W -> !C be a compactifiable morphism between schemes of locally\nfinite type over Spec(e^), where ^ is a A-affinoid algebra (the situation is slightly more\ngeneral for a further use). For a point x e SE we denote by ^ ^e fibre of 9 at x and\nset ^ == ^ ® ^( x ) 8 ? and for an abelian torsion sheaf ^ on ^, we denote by ^ an(! ^x\nthe pullbacks of ^ on ^ ^d ^x? respectively. By the Base Change Theorem for Coho-\nmology with Compact Support for schemes, one has\n\n                   (R<^,^=H^,^).\n\nFurthermore, for a point x e ^an over x, we fix an embedding of fields A(x) 8 <->^{x)\\\nIt gives rise to an isomorphism\n\n                   (^x^^T^^T.\nSince the cohomology with compact support of schemes are preserved under separably\nclosed extensions of the ground field, one has\n\n                  H^x, ^x) ^H^®^^?)°, ^).\n\nFinally, the Weak Base Change Theorem 5.3.1 tells that\n\n                  R^ 9an(^aI% == H^(^|11, ^n).\n\n      We use the above remarks to establish the following two facts.\n\n      7.1.2. Lemma. — In the above situation assume that the dimension of y is at most one.\nThen for any q ^ 0 one has\n\n                  (R3 9. ^ -^ R3 9T\" ^an.\n\nFurthermore, if in addition °K and. W are compactifiable over k and the theorem is true for SK^ then\nit is also true for W.\n\f             fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                                   129\n\n     Proof. — The first statement follows from Theorem 6.1.1 and the above remarks,\nand the homomorphism of Leray spectral sequences\n                     H^, R^y. ^) ==> H^^, ^)\n\n                             i\n                   H^^, R3 9^ ^an) ==> H^0^, ^an)\n                                                          i\nshows that the second statement is also true. •\n\n     7.1.3. Lemma. — In the above situation assume that the morphism 9 is finite and surjective.\nThen if 2^ and W are compactifiable over k and the theorem is true for @<, then it is also true for SC.\n\n      Proof. — Let ^ be an abelian torsion sheaf on 3C. Since 9 is finite and surjecdve,\nthe canonical homomorphism y -> 9^(9* ^\") is injective. Furthermore, by Corol-\nlary 4.3.2, for an abelian sheaf ^ on W one has H^.^, 9^ ^an) ^ H^®^, ^an).\nIn particular, the hypothesis implies that the theorem is true for all sheaves of the\nform 9^ ^S. Thus, one can construct a resolution of ^\", 0 -> 3F -> ^ro ->^\"1 - > . . . ,\nsuch that the theorem is true for all ^ri. The homomorphism of spectral sequences\n                    H^H^^,^-)) ———> H^^,^)\n\n\n                   ^(H^^ , ^\n                             i\n                             0    ran\n                                     ')) ==> H^ - ^\"1,^\"1)\n                                                    4 0\n                                                          i\nshows that the theorem is also true for ^r. •\n      We are now ready to prove the theorem.\n      1) The theorem is true for the direct product (P1)\", where P1 is a the projective line over k.\n— This follows from Lemma 7.1.2.\n      2) The theorem is true for the projective space P^ over k. — Indeed, there exists a finite\nsurjecdve morphism (P1)\" -> P71, and we can use Lemma 7.1.3.\n      3) The theorem is true for any projective scheme over k. — This follows from Lemma 7.1.2.\n      4) The theorem is true for any affine scheme of finite type over k. —- This is so because\nsuch a scheme is isomorphic to an open subscheme of a projective scheme.\n      5) The theorem is true for any proper scheme over k. — For a proper scheme SC we can\nfind an open everywhere dense affine subscheme ^, and so the dimension of the closed\nsubscheme W == 3E\\^U is strictly less than the dimension of^*. Therefore the statement\nis obtained by induction using the exact cohomological sequences associated with the\nembeddings W ^ X <- W and ^an <-^ ^an <- ^an and the five-lemma.\n      6) The theorem is true for any compactifiable scheme. — This is already clear. •\n      "
        }
      ],
      "literal_segment_warning": "Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection."
    },
    {
      "id": "CD",
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
      "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "actual_pdf_pages": [
        496,
        497,
        498
      ],
      "page_count": 608,
      "application_check": "The cached PDF numbers the semiample-residue assertion as 17.8.2; 6.8.2 in GJR refers to another numbering. Use GJR 7.8--7.9 directly.",
      "retained_pdf": "CD-selected-pages.pdf",
      "literal_excerpts": [
        {
          "label": "cached-version semiample residue implication",
          "byte_start": 1774508,
          "byte_end": 1775492,
          "literal_text": "Proposition 17.8.2. — Soit X un espace k-analytique séparé et presque bon, et soit L\nun fibré en droites sur X muni d’une métrique paralinéaire entière. On suppose que L\nest localement trivial pour la topologie usuelle de X.\n  Soit x ∈ X tel qu’il existe une puissance strictement positive du fibré résiduel L  fx\nengendrée par ses sections globales. Alors la métrique de L est tropicalement convexe (et\ndonc psh) au voisinage de x.\nDémonstration. — Quitte à remplacer L par une puissance strictement positive, on sup-\npose que L\n         fx est engendré par ses sections globales. D’après le corollaire 17.4.12, il existe\ndonc une famille finie (a1 , . . . , am ) d’éléments de OX,x×\n                                                                telle que la fonction ∥s∥−1 soit\négale à max(|a1 |, . . . , |am |) au voisinage de x. Il découle alors de la proposition 8.2.1 que\nla métrique de L est tropicalement convexe au voisinage de x.\n\n"
        }
      ],
      "literal_segment_warning": "Original cache formfeed segments can differ from actual PDF pages; authoritative page numbers refer to the retained PDF selection."
    }
  ],
  "application_checks": [
    {
      "id": "strict-real-PL-realization",
      "premises": [
        "GJR 5.1, 15.4--15.7",
        "Thu 2.2.22"
      ],
      "application": "Only type-2 vertices are added; K is algebraically closed, so the finite separable extension is K itself. At a type-2 star the basis has slopes 0 or 1, value 0 at the centre and value-group edge lengths. Each basis is integral PL on a strict domain. Arbitrary real slopes enter only as real coefficients of those bases.",
      "status": "proved in argument"
    },
    {
      "id": "fixed-perturbation",
      "premises": [
        "GJR 7.8, 15.2, 15.7"
      ],
      "application": "One initial finite skeleton contains every positive-genus residue point. The Dirichlet graph potential has positive outgoing-slope sum at those interior vertices and zero elsewhere. A constant makes it nonnegative. Strict PL plus subharmonicity gives nef residues; positive-degree real classes on a proper smooth curve are ample.",
      "status": "proved in argument"
    },
    {
      "id": "arbitrary-target-and-sequence",
      "premises": [
        "Thu 3.4.1--3.4.2, 3.4.6, 3.4.10",
        "GR-classical 4.1.2"
      ],
      "application": "No continuity assumption is added. Interpolants agree with the finite target at type-2 points; type-3 equality follows from skeleton convexity; other points follow from 3.4.1. Lindelof extraction on rational strict sublevel sets uses a countably dense ground field.",
      "status": "proved in argument"
    },
    {
      "id": "proper-factors",
      "premises": [
        "GR-classical 4.2, 6.1",
        "Berkovich 2.6.9, 7.1.1"
      ],
      "application": "Fibres over H(c) are compact and boundaryless. H_c^0 comparison for proper geometrically connected algebraic factors gives topological connectedness over every analytic extension. The maximum principle forces fibre constancy; actual local sections make the descended target classically psh.",
      "status": "proved in argument"
    },
    {
      "id": "boundary-obstruction",
      "premises": [
        "GR-classical 3.5(3), 4.1.2"
      ],
      "application": "The spike is defined on the closed disc, whose actual analytic boundary is its Gauss point. It is zero on the interior, so the boundary extension assertion applies. The no-sequence conclusion uses continuity and the uncountable residue branches only.",
      "status": "proved in argument"
    },
    {
      "id": "OCR-and-numbering",
      "premises": [],
      "application": "Visually inspected actual PDF GJR page 47, Thu pages 57, 103, 104, and CD page 497. Thu 2.2.22(i) says finite separable iff the vertices are type (2). Thu 3.4.2 uses all finite subsets of I(Y), not only type (2). GJR 7.10 states uniform convergence and does not state decreasing convergence. CD in this cache has 17.8.2.",
      "status": "checked against primary PDFs"
    }
  ],
  "proof_status": "Unverified mathematical draft; hashes and execution do not certify proofs."
}

## GJR actual PDF page 2

2
W. GUBLER, P. JELL, AND J. RABINOFF
1. INTRODUCTION
Arakelov theory is an arithmetic intersection theory on arithmetic varieties. The con-
tributions of the Archimedean places are described analytically, while intersection theory
on models over valuation rings is used for the non-Archimedean places. It is an old dream
to handle all places simultaneously in an analytic manner. This would have the advan-
tage of replacing the models, which sometimes do not exist in sufﬁcient generality, by
the underlying Berkovich analytic spaces.
It is here that tropical geometry becomes very helpful. Lagerberg [Lag12] has intro-
duced smooth (p,q)-forms on Rn given in terms of coordinates by
α =
X
|I|=p,|J|=q
αIJd′xi1 ∧··· ∧d′xip ∧d′′x j1 ∧··· ∧d′′x jq
where I (resp. J) consists of i1 < ··· < ip (resp. j1 < ··· < jq) and αIJ are C∞-functions
on Rn. The smooth Lagerberg forms give rise to a bigraded differential sheaf A•,• of
R-algebras on Rn with alternating product ∧and with natural differentials d′ and d′′
(see 2.7). They are the analogues of the differential operators ∂and ∂in complex anal-
ysis.
One deﬁnes smooth Lagerberg forms on a weighted rational polyhedral complex (Π, m)
in Rn by restriction (see 2.7). This is analogous to the deﬁnition of differential forms on
singular complex analytic spaces. In applications, (Π, m) will be a tropical variety. One
has integrals and boundary integrals over (Π, m) satisfying the formula of Stokes.
From now on, we consider a good, d-dimensional strictly analytic Berkovich space X
over a non-trivially valued non-Archimedean ﬁeld K. For the basic notions used from
non-archimedean geometry, we refer to §2.3. For a compact analytic subdomain W of
X, a smooth tropicalization map F : W →Rn is given by F(x) = (−log|fi(x)|)i=1,...,n for
invertible analytic functions fi on W. Chambert-Loir and Ducros [CD12] used smooth
tropicalization maps to lift smooth Lagerberg forms to X. In this way, they obtained a
bigraded differential sheaf A•,•
sm of R-algebras on X with alternating product ∧and with
natural differentials d′ and d′′ (see 2.8).
This opens the door to the dream mentioned above. Many results hold as expected
from complex geometry. Chambert-Loir and Ducros proved that there are analogues of
smooth partitions of unity, of the formula of Stokes and of the Poincaré-Lelong formula.
The d′′-operator induces an analogue of the Dolbeault complex and we can introduce the
tropical Dolbeault cohomology by
(1.0.1)
H p,q
sm (X) := ker(Ap,q
sm(X)
d′′
−→Ap,q+1
sm
(X))/d′′(Ap,q−1
sm
(X)).
It was shown in [Jel16] that the sheaves Ap,q
sm satisfy a local Poincaré Lemma. If X = Y an
for a separated smooth scheme Y of ﬁnite type over K, then Liu [Liu20] showed that
there is an analogue of the cycle class map. However, it was realized in [Jel19b] that the
cohomology groups H1,1
sm (X) can be inﬁnite dimensional and that Poincaré duality can
fail for smooth projective curves X over K. The main problem can be already found in
Thuillier’s thesis [Thu05] and is a result of the fact that not all harmonic functions on
curves are smooth, as explained in Wanner’s master thesis [Wan16].


## GJR actual PDF page 7

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
7
compact Riemann surfaces, and Poincaré duality holds if X is proper. This will be shown
in our companion paper [GJR21]. As a special case, we mention here the following result:
Theorem 1.14. Let Y be a smooth projective curve over K and let b the ﬁrst Betti number
of X = Y an. Then dim(H p,q(X)) is equal to 1 (resp. b) if p + q ∈{0,2} (resp. if p + q = 1).
The idea is to introduce (p,q)-forms on a weighted metric graph with boundary and
to compute the Dolbeault cohomology ﬁrst in this combinatorial setting. We will then
show that if K′/K is a ﬁnite Galois extension such that X ′ := X ⊗K K′ admits a strictly
semistable model, then H p,q(X ′) is canonically isomorphic to the Dolbeault cohomology
of its associated skeleton. By a Galois descent argument, the theorem follows. Although
Theorem 1.14 will be proven in [GJR21], it relies on the foundations developed here. In
particular, we will use the results about the Galois action on weakly smooth forms and
on Dolbeault cohomology discussed in Section 14.
In Section 15, we will restrict ourselves to the case of a rig-smooth curve. We will show
that our notion of harmonic functions agrees with Thuillier’s notion from [Thu05]. If the
curve has a strictly semistable model, then we will compare harmonic functions on the
curve to harmonic functions on the skeleton. At the end, we will give a regularization
result (Theorem 15.11) for subharmonic functions on a rig-smooth curve generalizing a
theorem of Wanner.
1.15. Canonical Tropicalizations for Abelian Varieties. In Section 16, we will show
that for an abelian variety A over K, the canonical tropicalization map trop: Aan →NR is
a harmonic tropicalization. Here, we denote by N the cocharacter lattice of the torus T
involved in Raynaud’s uniformization theory for A. In Section 17, we will give an example
of an abelian threefold with mixed reduction such that the canonical tropicalization is not
a smooth tropicalization map. This shows that weakly smooth forms arise very naturally
for abelian varieties.
Let MR = Hom(N,R) and Λp,qMR := ΛpMR⊗RΛqMR be the bigraded exterior algebra of
MR. Then there is a canonical injective homomorphism Λp,qMR →H p,q(A) for all p,q ∈N.
This was shown by Miriam Prechtel in her thesis [Pre23] based on results of this paper.
We do not know if this is an isomorphism as in the complex case.
1.16. Acknowledgments. We thank the participants of the Oberseminar Arakelov The-
ory in the summer term 2021 for useful comments about an earlier draft of the paper
and Andreas Mihatsch for his remarks on the ﬁrst arXiv version and the referee for the
suggestions to improve the presentation of the paper.
2. PREREQUISITES
2.1. General Notation and Conventions. The set of natural numbers N includes 0. A
set-theoretic inclusion S ⊂T allows equality. For an additive subgroup Λ ⊂R we let
p
Λ
denote its divisible hull. If P is any abelian group, we let PΛ := P ⊗Z Λ be the tensor
product with Λ.
Rings are always assumed to be commutative and with 1. For a ring A, the group of
invertible elements is denoted by A×. A variety over a ﬁeld F is an integral scheme which
is of ﬁnite type and separated over Spec F.


## GJR actual PDF page 8

8
W. GUBLER, P. JELL, AND J. RABINOFF
A space is compact if it is quasi-compact and Hausdorff. A paracompact space is a
Hausdorff space such that every open covering has a locally ﬁnite open reﬁnement.
2.2. Non-Archimedean Fields. Throughout the whole paper, we ﬁx a ﬁeld K that is
complete with respect to a non-trivial non-Archimedean complete absolute value de-
noted | |: K →R. We will call this a non-trivially valued non-Archimedean ﬁeld. A non-
Archimedean extension ﬁeld is a non-Archimedean ﬁeld K′ equipped with an isometric
embedding K ,→K′.
We will make use of Temkin’s theory of graded residue ﬁelds introduced in [Tem04];
see also [Duc24, 2.2] and [Duc12, Section 0]. We use eK to denote the ordinary residue
ﬁeld and eK• for the graded residue ﬁeld. Beware that Temkin and Ducros use eK1 for the
ordinary residue ﬁeld and eK for the graded residue ﬁeld.
We will use the following notation concerning non-Archimedean ﬁelds.
K
A non-Archimedean ﬁeld.
| |
: K →R, the absolute value on K.
v(·)
= −log| · |, the associated valuation.
K◦
The valuation ring of K.
K◦◦
The maximal ideal in K◦.
eK
= K◦/K◦◦, the residue ﬁeld of K.
Γ
= v(K×), the value group of K.
eK≤r
= {x ∈K | |x| ≤r} for r ∈R.
eK<r
= {x ∈K | |x| < r} for r ∈R.
eK r
= eK≤r/eK<r.
eK•
= L
r∈R eK r, the graded residue ﬁeld.
e(L/K)
= [|L×| : |K×|], the ramiﬁcation index of a ﬁeld extension.
f (L/K)
= [eL : eK], the residue degree.
We have
(2.2.1)
[eL• : eK•] = e(L/K)f (L/K)
by [Duc24, 2.2.27.1]. The left hand side is deﬁned as the dimension of eL• as a graded eK•-
vector space, which is the cardinality of any basis as in ordinary linear algebra [Duc24,
2.2.16].
2.3. Non-Archimedean geometry. We will use Berkovich analytic spaces as deﬁned
in [Ber93]. We are mainly concerned with good analytic spaces X over a non-trivially
valued non-Archimedean ﬁeld K. These are the analytic spaces considered in [Ber90], so
this book is our main reference for non-Archimedean geometry. Here, good means that
every x ∈V has a neighbourhood isomorphic to the Berkovich spectrum M(A ) of an
afﬁnoid algebra A .
When considering strictly analytic spaces, we will always use the G-topology generated
by the strictly afﬁnoid domains [Ber93, 1.3]. This is most natural for comparison to rigid
analytic geometry: see [Ber93, 1.6].
We will use the following notation concerning Berkovich analytic spaces. Let X be an
analytic space and let A be a K-afﬁnoid algebra.


## GJR actual PDF page 30

30
W. GUBLER, P. JELL, AND J. RABINOFF
x ∈NΓ. Then Sϕ(X) ∩X ω is the Shilov boundary of X ω by Remark 3.19. Hence we
may assume x ∈Sϕ(X) ∩X ω as otherwise all tropical multiplicities are zero. Using the
notations of 4.14, we let eK(Cx) denote the function ﬁeld of Cx. The homomorphism
Aω →H (x) induces an isomorphism eK(Cx)
∼
−→f
H (x) by [Ber90, Proposition 2.4.4(ii)].
By the deﬁnition of Aω ⊂A ◦
ω, the function ﬁeld of ιs(Cx) is precisely the subﬁeld eK( eM(x))
of Remark 3.8. We have length(OX,x) = 1 because X is reduced, so
mϕ(X, x) = [ f
H (x) : eK( eM(x))] = [Cx : ι(Cx)] = mrel(x)
by Remark 4.2(8).
□
Example 4.16 (Continuation of Example 3.15). We continue with the notation in Exam-
ple 3.15. By [BPR16, Theorem 5.8], for any point P in the interior of an edge e in the
skeleton S, the relative multiplicity mrel(P) is equal to the “expansion factor” of the edge e
with respect to the tropicalization map ϕtrop. In this situation, the expansion factor of
every edge is equal to 1, except for the edge BD, which has expansion factor 0 as it is
crushed to a point.
We claim that mϕ(X, P) = 1 for P ∈{A, B, C, D}. This can be checked directly from
the deﬁnition of mϕ(X, P). We give the proof in case P = A which reduces to the generic
point of the line x = 0 in the special ﬁber of Xmin. By [Ber90, Proposition 2.4.4(ii)],
we have f
H (A) = eK(y). Recall that trop(A) = (1,0). If M = Z2 be the character lattice
of T = G2
m, then eK( eM(A)) is the subﬁeld of f
H (A) generated by the reductions of x/p
and of y/1 = y. This shows f
H (A) = eK( eM(A)), and hence 4.2(8) yields that mϕ(X,A) =
[ f
H (A) : eK( eM(A))] = 1. The proof for the points P = B, C, D is similar.
We conclude that mrel(P) = mϕ(X, P) = 1 for every point P of Sϕ(X). It follows that
mϕ(X,ω) just counts the preimages of ω in Sϕ(X) under ϕtrop; these tropical multiplicities
are indicated in Figure 1.
5. PIECEWISE LINEAR FUNCTIONS
In this section we discuss piecewise linear functions on analytic spaces. Most of these
results are standard in one form or another: for instance, see [CD12, Gub98, GM19].
However, the terminology in the literature is somewhat nonstandard, so it is important
to ﬁx our ideas. We will ﬁnd it useful to work slightly more generally with piecewise
linear functions with slopes contained in an additive subgroup Λ ⊂R, and in some cases
new arguments are needed. In practice we will usually take Λ = Z,Q, or R, in which case
either Λ = Z or Λ is divisible.
In this section, K is a non-Archimedean ﬁeld with a non-trivial valuation v and value
group Γ := v(K×) ⊂R. We consider a good strictly K-analytic space X and an additive
subgroup Λ ⊂R. Recall from 2.3 that a strictly analytic space is good provided that that
every point has a strictly afﬁnoid neighbourhood. Most strictly analytic spaces occurring
in practice are good: for example, any strictly afﬁnoid space, a space with no boundary,
or an analytic subdomain of the analytiﬁcation of an algebraic variety. We restrict our
attention to good spaces as then the coherent modules on the Berkovich space X are
the same as the coherent modules on the space XG endowed with the G-topology [Ber93,
Proposition 1.3.4], which makes it reasonable to work with line bundles on X. We always


## GJR actual PDF page 31

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
31
use the G-topology on X generated by the strictly afﬁnoid domains. Let C(X) be the space
of continuous real functions on X.
Deﬁnition 5.1. A function h: X →R is called piecewise Λ-linear or Λ-PL if there exists a
G-covering {Xi} of X such that for each i, there are ﬁnitely many λi j ∈Λ and fi j ∈O (Xi)×
with h|Xi =
P
j λi j log|fi j|. A Z-PL function is called piecewise linear or PL.
We denote the group of PL functions on X by PL(X), and the group of Λ-PL functions
by PLΛ(X). These are subgroups of C(X).
5.2. Some remarks:
(1) A function h: X →R is PL if and only if there exists a G-covering {Xi} of X and
fi ∈O(Xi)× such that h|Xi = log|fi|.
(2) The set of Λ-PL functions on X forms a group since any two G-coverings {Xi} and
{X ′
j} admit the common reﬁnement {Xi ∩X ′
j}.
(3) The restriction of a Λ-PL function to a strictly analytic domain is Λ-PL.
(4) The presheaf U 7→PLΛ(U) is a sheaf in the G-topology, and therefore in the ana-
lytic topology as well.
(5) A function h: X →R is Λ-PL if and only if there exists a G-covering {Xi} of
X such that for each i, there are ﬁnitely many λi j ∈Λ and hi j ∈PL(Xi) with
h|Xi =
P
j λi jhi j.
(6) A function h: X →R is Q-PL if and only if, locally in the analytic topology, there
exists a positive integer N such that Nh is PL.
(7) If Λ = Z or Λ = Q then the minimum and maximum of two Λ-PL functions is
again Λ-PL by [GM19, Proposition 2.12(d)].
Example 5.3. The assertion of 5.2(7) is not true for Λ strictly containing Q. For example,
if the value group of K is Q and X = Gan
m = Spec(K[t±1])an is the split torus of rank 1, then
the tropicalization of any strictly afﬁnoid domain in X is a union of compact intervals with
rational vertices. We conclude that for Λ = R, the function h := πlog|t|+1 = −πtrop+1
is Λ-PL, but max(h,0) is not Λ-PL as max(h,0) = ϕ ◦trop for ϕ(u) = max(−πu + 1,0),
and as the piecewise linear function ϕ has a bend at the irrational number 1/π.
Here we list some basic functoriality properties of Λ-PL functions.
Lemma 5.4. Let h: X →R be a function.
(1) Let f : X ′ →X be a morphism of good strictly K-analytic spaces. If h ∈PLΛ(X) then
h ◦f ∈PLΛ(X ′).
(2) Let K′/K be a non-Archimedean ﬁeld extension, let X ′ = X b⊗KK′, and let π: X ′ →X
be the structure morphism. If h ∈PLΛ(X) then h ◦π ∈PLΛ(X ′).
(3) Let ι: Xred →X be the inclusion of the reduction of X, and let h′ = h ◦ι. Then
h ∈PLΛ(X) if and only if h′ ∈PLΛ(Xred).
Proof. The ﬁrst two assertions are obvious. For the third, by (1), the only thing to show is
that if h′ is Λ-PL then h is Λ-PL. Let U = M(A ) ⊂X be a strictly afﬁnoid domain, and let
Ured = M(Ared) ⊂Xred be its reduction. Suppose that h′|Ured =
P
λi log|gi| for gi ∈A ×
red.
If fi ∈A lifts gi then fi ∈A × is a unit, and h|U =
P
λi log|fi|. Since Xred has a G-cover
by such afﬁnoid domains, the same is true for X, so h is Λ-PL.
□


## GJR actual PDF page 32

32
W. GUBLER, P. JELL, AND J. RABINOFF
At this point we assume that the reader is familiar with formal geometry as recalled
in 2.4. We give an interpretation of Λ-PL functions in terms of formal geometry which
we will use to prove some more subtle properties of piecewise Λ-linearity. Recall that
a formal K◦-model of a paracompact strictly K-analytic space X is an admissible formal
scheme X over K◦equipped with an identiﬁcation Xη = X.
A frame of a line bundle on an open set is a nowhere vanishing section.
5.5 (Functions from Formal Models of OX). We assume now that X is paracompact. This
allows us to use Raynaud’s theory of formal K◦-models, as in 2.4. We will later apply
this only locally on a good, strictly analytic space, where we can always ﬁnd a compact
strictly analytic neighbourhood (even a strictly afﬁnoid neighbourhood as X is good).
Hence the reader loses nothing by assuming here and in the following that X is compact.
(Paracompactness has the advantage that one can apply these considerations also to the
analytiﬁcation of algebraic varieties over K.)
Let X be a formal K◦-model of X. The isomorphism classes of line bundles L on X
equipped with an identiﬁcation Lη = OX form an abelian group denoted by M(X). Then
L ∈M(X) determines a canonical metric ∥∥L on OX, deﬁned as follows: if s is a frame of
L over a formal open subset U ⊂X, then we set ∥s∥= 1 on Uη. This metric is well-deﬁned
because any two frames differ by a unit with constant absolute value 1.
Equivalently, we get a canonical function hL = −log∥1∥L: X →R with −log∥f ∥L =
−log|f |+hL for an analytic function f on any open subset U of X. If U = Uη for a formal
open subset U of X and if f ∈Γ(U,L) ⊂Γ(Uη,OX) is a frame of L, then by deﬁnition
0 = −log|f | + hL, so hL is PL because X has a G-cover by such U = Uη.
5.6 (PL Functions are Model Functions). If X is paracompact, then [GM19, Proposi-
tion 2.10] yields that h: X →R is PL if and only if there exists a formal K◦-model (X,L)
of (X,OX) such that h = −log∥1∥L.
5.7 (Λ-PL Functions from Formal Models). For paracompact X, we extend 5.6 to the
case of Λ-PL functions as follows. Choose a formal K◦-model X of X, and set M(X)Λ :=
M(X)⊗ZΛ. We have a unique homomorphism h: M(X)Λ −→C(X), written L 7→hL, such
that hλL = −λlog∥1∥L for all L ∈M(X) and λ ∈Λ. Note that if L =
Pm
i=1 λiLi ∈M(X)Λ
then hL =
Pm
i=1 λihLi ∈PLΛ(X) by 5.2(5).
If f : X′ →X is a morphism of formal K◦-models of X, then hf ∗L = hL for all L ∈M(X)Λ.
More generally, if f : X′ →X is any morphism of separated admissible formal schemes
then hf ∗L = hL ◦fη for all L ∈M(X)Λ. (See 2.4 for separatedness of formal models.)
For L ∈M(X)Λ, we get a unique continuous metric ∥∥L on OX deﬁned by −log∥f ∥L =
−log|f | + hL for an analytic function f on any open subset U of X.
We want to extend the result of 5.6 locally in the analytic topology to Λ-coefﬁcients as
in 5.7. To do this we need to show that a Λ-PL function is locally in the analytic topology a
linear combination of PL functions with Λ-coefﬁcients. (For our purposes, we could have
taken the statement of Proposition 5.8 as the deﬁnition of Λ-PL; we chose Deﬁnition 5.1
because it is more compatible with the terminology in the literature.)


## GJR actual PDF page 33

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
33
Proposition 5.8. Suppose that Λ = Z or that Λ is divisible. A function h: X →R is Λ-
PL if and only if for every x ∈X, there exists an open neighbourhood U of x such that
h|U =
Pm
i=1 λihi for ﬁnitely many λ1,...,λm ∈Λ and h1,...,hm ∈PL(U).
Before proving the proposition, we state the desired corollary.
Corollary 5.9. Suppose that Λ = Z or that Λ is divisible. A real function h: X →R is Λ-PL
if and only if for every point x ∈X, there exists a compact strictly analytic neighbourhood
U of x, a formal K◦-model U of U, and L ∈M(U)Λ, such that h|U = hL. In this case, such a
neighbourhood U can be chosen arbitrarily small.
Proof. Suppose that h is Λ-PL. By Proposition 5.8, after shrinking X, we may assume that
h =
Pm
i=1 λihi for λ1,...,λm ∈Λ and PL functions h1,...,hm: X →R. Since every point of
X has a compact strictly analytic neighbourhood, we may also assume that X is compact.
By 5.6, for each i there is a model (Xi,Li) of (X,OX) such that hi = hLi. Finding a model X
dominating all Xi, we may assume all Xi = X. Then h = hL for L =
Pm
i=1 λiLi. Conversely,
if L =
Pm
i=1 λiLi on U for λ1,...,λm ∈Λ and L1,...,Lm ∈M(U) then hL =
Pm
i=1 λihLi is
Λ-PL by 5.2(5). We can choose U sufﬁciently small because U can be taken arbitrarily
small in Proposition 5.8.
□
We will use the following lemma in the proof of Proposition 5.8; we will use it again
several times.
Lemma 5.10. Suppose that Λ is a divisible additive subgroup of R. Let P be an abelian
group, and let x1,..., xr ∈Λ ⊗Z P be a ﬁnite collection of elements. Then there is a Q-
linearly independent subset {λ1,...,λn} ⊂Λ such that each xi has the form
Pn
j=1 λi ⊗xi j
for xi j ∈P.
Proof. Write xi =
Pmi
j=1 λi j⊗yi j. Let λ1,...,λn be a basis of the Q-subspace of Λ generated
by the λi j. Since Λ is divisible, we may assume that every λi j is a Z-linear combination of
λ1,...,λn. Expanding λi j in the sum
Pmi
j=1 λi j⊗yi j and rearranging proves the lemma.
□
Proof of Proposition 5.8. The “if” direction is trivial because a covering by open sets is a
G-covering. Suppose then that h is Λ-PL. If Λ = Z then h is itself PL, so we may assume
Λ is divisible. Fix x ∈X, and replace X by a compact strictly analytic neighbourhood of
x to assume X is compact. Choose a G-covering {Xi}i∈I of X by compact strictly analytic
domains such that h|Xi =
Pmi
j=1 λi j log|fi j| for ﬁnitely many λi j ∈Λ and fi j ∈O (Xi)×. We
may assume that every Xi contains x and that I is a ﬁnite set. By Lemma 5.10, there
are Q-linearly independent elements λ1,...,λm ∈Λ such that for every i ∈I, we have
h|Xi =
Pm
k=1 λkhik with hik = log|gik| for gik ∈O (Xi)×.
We claim that there is a neighbourhood U of x such that for all i, j ∈I and all y ∈
U ∩Xi ∩X j we have
(5.10.1)
hik(y) −hik(x) = hjk(y) −hjk(x).
To prove this, we pick i, j ∈I, set Xi j := Xi ∩X j and consider the smooth tropicalization
map Hi j : Xi j →R2m given by y 7→(hik(y),hjk(y))k=1,...,m. By 3.2 and 3.3, the tropical
variety of the germ (Xi j, x) is the germ at Hi j(x) of a ﬁnite union of (Z,Γ)-polytopes ∆.


## GJR actual PDF page 34

34
W. GUBLER, P. JELL, AND J. RABINOFF
Choosing them sufﬁciently small, we may assume every ∆is contained in Hi j(Xi j). It is
enough to show (5.10.1) for y ∈Ui j :=
S
∆H−1
i j (∆) as Ui j is a neighbourhood of x in Xi j,
hence has the form U ∩Xi j for a neighbourhood U of x in X.
We ﬁx i, j ∈I and pick a polytope ∆as above. Since ∆is a Z-polytope, the set (Hi j(x)+
Q2m) ∩∆is dense in ∆. By construction, there are coordinate functions ℓik,ℓjk of R2m
such that hik = ℓik ◦Hi j and hjk = ℓjk ◦Hi j. Hence it is enough to show (5.10.1) for all
y ∈Xi j with Hi j(y) ∈∆and with ω = Hi j(y) −Hi j(x) ∈Q2m. Using
0 =
X
k
λkhik(y) −
X
k
λkhjk(y) −
X
k
λkhik(x) +
X
k
λkhjk(x)
=
X
k
λk
 hik(y) −hik(x) −hjk(y) + hjk(x)

and hik(y) −hik(x) −hjk(y) + hjk(x) = ℓik(ω) −ℓjk(ω) ∈Q, the Q-linear independence
of λ1,...,λm yields (5.10.1) for all such y. This ﬁnishes the proof of the claim.
Let us ﬁx i ∈I. We deduce from (5.10.1) that there are constants ci jk such that hik =
hjk + ci jk on U ∩Xi j for all j ∈I and k = 1,..., m. Evaluating at a rig-point of U ∩Xi j, we
see that ci jk ∈
p
Γ. Replacing h by an integer multiple, we may assume ci jk = −v(γi jk) ∈Γ
for some γi jk ∈K×. We conclude that γi jkg jk is an invertible function on X j. We claim
that there is a unique piecewise linear function hk: U →R that agrees with log|γi jkg jk| =
ci jk+hjk on U ∩X j for every j ∈I. To see that the functions ci jk+hjk indeed glue, we know
from (5.10.1) that they agree on intersections up to constants and the claim follows as
ci jk + hjk(x) = hik(x) does not depend on j ∈I. We note that
X
k
λkhjk(x) = h(x) =
X
k
λkhik(x) =
X
k
λk
 hjk(x) + ci jk

and hence
P
k λkci jk = 0. For y ∈U ∩X j, we deduce that
h(y) =
X
k
λkhjk(y) =
X
k
λkhjk(y) +
X
k
λkci jk =
X
λkhk(y)
and hence h =
P
λkhk on U. This proves the proposition.
□
With these foundations in place, we can use formal models to show that piecewise
Λ-linearity can sometimes be checked after pull-back, at least when Λ is divisible.
Proposition 5.11. Let f : X ′ →X be a ﬁnite, ﬂat, surjective morphism of good strictly K-
analytic spaces. Suppose that Λ is divisible. If h: X →R is a function and h′ = h ◦f , then
h ∈PLΛ(X) if and only if h′ ∈PLΛ(X ′).
Proof. By Lemma 5.4(1), we only need to show that if h′ is Λ-PL then so is h. By [Ber93,
Proposition 3.2.7], the map f is open. Let x ∈X, choose x′ ∈X ′ mapping to x, and
let U′ be an open neighbourhood of x′ such that h′|U′ =
Pm
i=1 λih′
i for λ1,...,λm ∈Λ
and h′
1,...,h′
m ∈PL(U′). Such a neighbourhood exists by Proposition 5.8. By [Ber93,
Lemma 3.1.2, Deﬁnition 3.2.5], after shrinking U′, the morphism f |U′ : U′ →f (U′) is
ﬁnite and ﬂat. Thus we may replace X ′ by U′ and X by f (U′) to assume h′ =
Pm
i=1 λih′
i
on X ′. Shrinking further, we may assume X and X ′ are compact. By 5.6, each PL function
h′
i is induced by a line bundle on a formal model of X ′. Passing to a dominating formal


## GJR actual PDF page 37

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
37
By a variety over a ﬁeld k we mean an integral, separated k-scheme V of ﬁnite type.
The ﬁeld of rational functions on V is denoted R(V).
6.1 (Riemann–Zariski spaces). Let k be a ﬁeld, let F/k be a ﬁeld extension, and let PF/k
be the set of valuations on F that are trivial on k, up to equivalence. For ν ∈PF/k we let
Oν ⊂F denote the corresponding valuation ring. For a subset A ⊂F we set PF/k{A} = {ν ∈
PF/k | ν(f ) ≥0 for all f ∈A}. Subsets of the form PF/k{f1,..., fn} are said to be afﬁne.
Note that PF/k = PF/k{;} is itself afﬁne. We endow PF/k with the topology generated by
afﬁne subsets. We equip PF/k with the sheaf of rings O : U 7→{f | ν(f ) ≥0 for all ν ∈U}.
For ν ∈PF/k the localization of O at ν is canonically identiﬁed with Oν, so PF/k is a
locally ringed space. It is shown in [Tem00, Corollary 1.3] (see [Tem04, Section 2] for
an erratum) that any afﬁne open subset of PF/k is quasi-compact.
6.2 (Models). We keep the notation in 6.1. Let V be a variety equipped with a k-algebra
homomorphism from the function ﬁeld R(V) to F. We let PF/k{V} denote the set of all val-
uations ν ∈PF/k such that Spec(F) →V extends to a morphism Spec(Oν) →V. Such an
extension is unique if it exists, so there is a map of sets πV : PF/k{V} →V sending ν to the
image of the closed point of Spec(Oν) →V. It is easy to see that PF/k{V} is a ﬁnite union
of afﬁne open subsets, so it is quasi-compact. The morphism πV : PF/k{V} →V is a surjec-
tive morphism of ringed spaces by [CD12, 6.1.1]. Conversely, if U is any quasi-compact
open subset of PF/k then U = PF/k{V} for some such V by [Tem00, Proposition 1.4]; we
call V a model of U.3
Let V and V ′ be varieties equipped with k-algebra homomorphisms R(V) →F and
R(V ′) →F. A dominant morphism V ′ →V, compatible with the morphisms R(V) →F
and R(V ′) →F, is unique if it exists, in which case PF/k{V ′} ⊂PF/k{V}. In this case
we say that V ′ dominates V. We have equality PF/k{V ′} = PF/k{V} if and only if V ′ →
V is proper by the valuative criterion of properness for integral schemes (see [EGAII,
Corollaire 7.3.10(ii)] and [Tem11, Lemma 3.2.1]).
6.3 (Functoriality). Let F ′/k′ be an extension of F/k: that is, F ′ is an extension ﬁeld
of F and k′ is a subﬁeld of F ′ containing k. Restriction of valuations gives a canonical
map ϕ: PF′/k′ →PF/k. The inverse image of PF/k{f1,..., fn} is PF′/k′{f1,..., fn}, so ϕ is
continuous. One checks that ϕ induces a morphism of locally ringed spaces. If k′ = k
then ϕ is surjective, and if F ′ = F then ϕ is injective.
Let V (resp. V ′) be a k-variety (resp. k′-variety) equipped with a k-algebra homomor-
phism R(V) →F (resp. a k′-algebra homomorphism R(V ′) →F ′). As in 6.2, a domi-
nant morphism V ′ →V of k-schemes, compatible with the morphisms R(V) →F and
R(V ′) →F ′, is unique if it exists, in which case ϕ(PF′/k′{V ′}) ⊂PF/k{V}. In this case we
also say that V ′ dominates V.
Lemma 6.4. Let F ′/k′ be an extension of F/k, and let ϕ: PF′/k′ →PF/k be the canonical
morphism. Let V be a k-variety equipped with a k-algebra homomorphism R(V) →F, and
let V ′ be the closure of the image of the canonical k′-morphism Spec(F ′) →V ⊗k k′. Then
PF′/k′{V ′} = ϕ−1(PF/k{V}).
3In [CD12] these are called premodels.


## GJR actual PDF page 38

38
W. GUBLER, P. JELL, AND J. RABINOFF
Proof. This is similar to [Tem11, Lemma 3.2.1]. Let ν′ ∈PF′/k′ and let ν = ϕ(ν′) = ν′|F.
If ν′ ∈PF′/k′{V ′} then we have a k′-morphism Spec(Oν′) →V ′ extending Spec(F ′) →
V ′. Let x ∈V be the image of the closed point of Spec(Oν′) under the composition
Spec(Oν′) →V ′ →V. Then Spec(Oν′) →V factors through Spec(OV,x), so we have a
k-algebra homomorphism OV,x →Oν′. It follows that the image of OV,x is contained in the
intersection Oν = Oν′ ∩F, so Spec(F) →V extends to a morphism Spec(Oν) →V, and
hence ν ∈PF/k{V}. Conversely, suppose that ν ∈PF/k{V}. Then Spec(Oν′) maps to V via
Spec(Oν′) →Spec(Oν) →V, so Spec(F ′) →V ⊗k k′ extends to Spec(Oν′) →V ⊗k k′. The
image of this morphism is contained in V ′, so ν′ ∈PF′/k′{V ′}.
□
As a special case of the next lemma, we see that the poset of models of a quasi-compact
open subset U ⊂PF/k is ﬁltered.
Lemma 6.5. Let F ′/k′ be an extension of F/k, and let ϕ: PF′/k′ →PF/k be the canonical
morphism. Let U′ ⊂PF′/k′ and U ⊂PF/k be quasi-compact open subsets such that ϕ(U′) ⊂U.
Let V ′ and V be models of U′ and U, respectively. Then there is a model W ′ of U′ that
dominates both V and V ′.
Proof. Let W be the closure of the image of the canonical k′-morphism Spec(F ′) →V ⊗kk′,
as in Lemma 6.4. Then this lemma shows that W →V is dominant and ϕ−1(U) =
PF′/k′{W}, so we can replace V by W to assume k = k′ and F = F ′. The given morphisms
Spec(F) →V and Spec(F) →V ′ determine a morphism Spec(F) →V ×k V ′; let W ′ be the
closure of the image of this morphism. This is a variety. The generic point of W ′ maps to
the generic points of V and V ′, so W ′ →V and W ′ →V ′ are dominant. We must show that
PF/k{W ′} = U. For ν ∈U we have unique morphisms Spec(Ov) →V and Spec(Ov) →V ′,
which induces a morphism p: Spec(Ov) →V ×k V ′ extending Spec(F) →V ×k V ′. The
image of p is contained in W ′, so ν ∈PF/k{W ′}.
□
6.6 (Invertible sheaves on Riemann–Zariski spaces). With the notation in 6.1, let U ⊂
PF/k be a quasi-compact open subset. Then U is a ringed space, so it makes sense to
discuss invertible sheaves on U. We let Pic(U) denote the group of isomorphism classes
of invertible sheaves, and for an additive subgroup Λ ⊂R we set Pic(U)Λ = Pic(U) ⊗Z Λ.
Let V be a model of U as in 6.2, with canonical morphism πV : U →V. If LV is an
invertible sheaf on V, then L := π∗
V LV is an invertible sheaf on U. It is an important fact
that every invertible sheaf on U arises in this way. This is explained in [CD12, 6.1.3]. We
call (V, LV) a model of (U, L).
More generally, for an additive subgroup Λ of R we have a group homomorphism
Pic(V)Λ →Pic(U)Λ.
Any element of Pic(U)Λ can be expressed as a ﬁnite sum L =
Pn
i=1 λiLi for λi ∈Λ and Li ∈Pic(U). Choosing a model for each Li and passing to a
dominating model, we see that any L ∈Pic(U)Λ has the form π∗
V LV for a model V of U
and LV ∈Pic(V)Λ. We call such (V, LV) a model of (U, L) as above.
6.7 (Nef line bundles). Let X be a separated k-scheme of ﬁnite type and let L be a line
bundle on X. For an integral, proper closed curve C ⊂X we have a well-deﬁned inter-
section number c1(L).C := deg(L|C) ∈Z. We say that L is numerically effective or nef if
c1(L).C ≥0 for all such curves C, and that L is numerically trivial if c1(L).C = 0 for all C
(equivalently, if L and L−1 are both nef).


## GJR actual PDF page 39

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
39
More generally, let Λ ⊂R be an additive subgroup and let C ⊂X be an integral, proper
closed curve. We have an induced homomorphism L 7→c1(L).C : Pic(X)Λ →Λ, and we
say that L is nef (resp. numerically trivial) if c1(L).C ≥0 (resp. c1(L).C = 0) for all such C.
The set of nef line bundles in Pic(X)Λ forms a monoid (resp. a cone if Λ = R), and the
set of numerically trivial line bundles form a subgroup (resp. an R-subspace).
Here we list some classical properties of nefness. We sketch some proofs because in
the literature, the scheme X is generally assumed to be proper.
Lemma 6.8. Let X be a separated k-scheme of ﬁnite type and let L ∈Pic(X)Λ.
(1) The line bundle L is nef if and only if its image in Pic(X)R is nef.
(2) Let k′/k be a ﬁeld extension and let X ′ = X ⊗k k′, with structure morphism π: X ′ →
X. Then L is nef if and only if π∗L is nef.
(3) Let f : X ′ →X be a morphism of separated, ﬁnite-type k-schemes. If L is nef then
f ∗L is nef, and the converse holds if f is proper and surjective.
(4) Let ι: Xred →X be the reduction map. Then L is nef if and only if ι∗L is nef.
The same statements hold with “nef” replaced by “numerically trivial.”
Proof. The last assertion holds because L is numerically trivial if and only if L and L−1
are nef. Assertion (1) is obvious because nefness is a numerical property, and (4) is clear
because X and Xred have the same integral subcurves.
(2) Since intersection numbers are compatible with base extension, it is clear that
if π∗L is nef, then also L is nef. To prove the converse, we assume that L is nef. First
suppose that k′/k is algebraic. Since every integral proper subcurve C′ of X ′ is deﬁned
over a ﬁnite subextension, we may assume that k′/k is a ﬁnite extension. Then we may
view X ′ as a scheme of ﬁnite type over k and π as a ﬁnite morphism over k. Then π(C′)
is a proper subcurve of X and we get c1(π∗L).C′ = c1(L).π∗(C′) ≥0 by the projection
formula. This proves the algebraic case of (2), so we may assume k is algebraically
closed to prove the claim in general. Let C′ again be an integral proper subcurve of X ′.
Since C′ is deﬁned over a ﬁnitely generated subextension, we may assume that k′ is a
ﬁnitely generated ﬁeld extension of k. Then k′ is the function ﬁeld of a variety V over k.
Let πV : X ×k V →V and πX : X ×k V →X be the structure morphisms. The morphism
π: X ′ →X is the generic ﬁber of πV. Since C′ is projective and ﬂat over k′, the spreading
out property shows that there is a non-empty open subset U of V such that the closure C′
of C′ in π−1
V (U) is ﬂat and projective over U. By [Kol96, Proposition VI.2.9], the degree
of the ﬁber C′
u with respect to π∗
X(L) is independent of the choice of u ∈U. Let η be the
generic point of U and let u be a closed point of U. Since C′
u ∼= C for a proper closed
subcurve C of X, the claim follows from
c1(π∗L).C′ = degπ∗
V (L)(C′
η) = degπ∗
V (L)(C′
u) = degL(C) = c1(L).C ≥0.
(3) If L is nef then f ∗L is nef because if C′ ⊂X ′ is an integral proper k-curve then
f (C′) ⊂X is integral and proper of dimension ≤1, so the claim follows from the projec-
tion formula. Conversely, if f ∗L is nef and if f is a proper surjective map, then L is nef
because every integral proper k-curve C ⊂X is the image of an integral proper k-curve
C′ ⊂X ′ (take the closure of a closed point in the ﬁber over the generic point of C).
□


## GJR actual PDF page 41

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
41
such that V ′ = V ′′ ⊗k′′ k′. After enlarging k′′, we may assume that V ′′ also dominates V;
let f ′: V ′′ →V be the dominating morphism. By Lemma 6.8(2), the line bundle f ′∗L is
nef. Replacing k′ with k′′ and V ′ with V ′′, we may assume that [k′ : k] < ∞. In this case,
the variety V ′ is also a model of U. Any proper k-curve in V ′ is also a proper k′-curve, so
f ∗LV is nef when we consider V ′ as a k-variety. It follows from Lemma 6.11 that L is nef.
Now assume that d = tr.deg(F/k) < ∞, and that tr.deg(k′F/k′) = d. First we reduce
to the case when k is algebraically closed. Let F ′′ be a ﬁeld containing F ′ and an algebraic
closure k of k. Pulling back via PF′′/k′ →PF′/k′, we may replace F ′ with F ′′ to assume
k ⊂F ′. We have tr.deg(kF/k) = tr.deg(F/k) = d, and
tr.deg(k′kF/k′k) = tr.deg(k′kF/k′) = tr.deg(Fk′/k′) = d.
Applying case (1) to the extension kF/k of F/k and using the above displayed equation,
we may replace k by k, F by kF, and k′ by k′k to assume k = k.
Choose a model (V, LV) of (U, L) with dim(V) = d. Since k is algebraically closed, the
scheme V ′ := V ⊗k k′ is a variety. As F/R(V) is algebraic, we have tr.deg(k′R(V)/k′) =
tr.deg(k′F/k′) = d. Let x be the image of Spec(F ′) →V ′, so x maps to the generic point
of V. The residue ﬁeld κ(x) contains both k′ and R(V), so tr.deg(κ(x)/k′) = d. It follows
that x is the generic point of V ′. By Lemma 6.4, the variety V ′ is a model of U′, so ϕ∗LV
is nef by Lemma 6.11, hence LV is nef by Lemma 6.8(3).
□
6.13 (Temkin’s reductions of germs). Let X be a good strictly K-analytic space and let
x ∈X.
Temkin’s reduction red(X, x) of the germ (X, x) is an afﬁne open subset of
P f
H (x)/ek, where f
H (x) is the reduction of the completed residue ﬁeld H (x) at x as in 2.3.
The reduction red(X, x) can be constructed as follows.4 Let U be a compact strictly
analytic neighbourhood of x in X and let U be a formal K◦-model of U. The closure
VU,x of the reduction redU(x) is variety over ek by [BL93a, Proposition 4.7], and there
is a canonical homomorphism R(VU,x) →f
H (x) by [Ber90, 2.4]. We deﬁne red(X, x)
to be P f
H (x)/ek{VU,x}. Then red(X, x) is an afﬁne (open) subset of P f
H (x)/ek by [Tem00,
Lemma 2.2]. Let πU,x : red(X, x) →VU,x be the canonical morphism of 6.2
Reduction of germs (X, x) 7→red(X, x) is functorial in (X, x). It also respects extension
of the ground ﬁeld, in the following sense. Let K′/K be a non-Archimedean extension
ﬁeld, let X ′ = X b⊗KK′ with structure morphism π: X ′ →X, and let x′ ∈X ′ and x = π(x′).
Let ϕ: P f
H (x′)/eK′ →P f
H (x)/eK be the natural morphism. Then ϕ−1(red(X, x)) = red(X ′, x′).
See [Tem00, Lemma 4.2] (and [Tem04, Section 5] for a correction).
We will need the fact that models of the form VU,x as in 6.13 are coﬁnal in the system
of all models of red(X, x).
Lemma 6.14. Let X be a good strictly K-analytic space, let x ∈X, and let V be a model of
red(X, x). Then there exists a compact strictly analytic neighbourhood U of x and a formal
K◦-model U of U such that VU,x dominates V.
4Reductions of germs are much more subtle when X is not good or strictly analytic, and a major moti-
vation of Temkin’s work is to understand goodness and strictness by studying such reductions. In our case,
the construction is relatively simple.


## GJR actual PDF page 42

42
W. GUBLER, P. JELL, AND J. RABINOFF
Proof. Choose a ﬁnite afﬁne open covering V =
S
Vi. Then Vi = Spec(eK[efi j : j ∈Ji])
for ﬁnitely many efi j ∈f
H (x). We pick lifts fi j ∈OX,x. Let U be a strictly afﬁnoid neigh-
bourhood of x with fi j ∈O (U), and let Ui := {x ∈U | |fi j(x)| ≤1, j ∈Ji}. By [Tem00,
Proposition 2.3(ii,iii)], the reductions red(Ui, x) cover red(X, x), so (
S
Ui, x) = (X, x).
We may shrink U to assume that U =
S
Ui is a (strictly afﬁnoid) neighbourhood of x.
We claim that we can ﬁnd a formal K◦-model U of U that is covered by formal opens
Ui with (Ui)η = Ui and fi j ∈O (Ui). Write Ui = M(Ai) for a strictly afﬁnoid algebra Ai.
Choose a surjection from a Tate algebra T onto Ai such that each fi j is the image of a
generator. The image Ai of T ◦in Ai is a ﬂat K◦-algebra topologically of ﬁnite presentation
containing fi j; hence Ui := Spf(Ai) is an admissible formal model of Ui with fi j ∈O (Ui).
By [Bos14, Lemma 8.4.5], there exists an admissible formal K◦-model U of U and a
covering by formal open subschemes U′
i ⊂U such that (U′
i)η = Ui. By Lemma 8.4.4(d)
of loc. cit., there is a formal K◦-model U′′
i of Ui that is an admissible formal blowup of
both Ui and U′
i. By Proposition 8.2.13 of loc. cit., there is an admissible formal blowup
ϕ: U′ →U such that ϕ−1(U′
i) dominates U′′
i . Replacing U by U′ and Ui by ϕ−1(U′
i) proves
the claim.
Consider the closure V ′ := VU,x of redU(x) in Us. By construction the function ﬁeld
R(V ′) contains all efi j, so R(V) ⊂R(V ′) and hence there is a dominant rational map
V ′ →V. Moreover, for each i we have O (Vi) ⊂O ((Ui)s ∩V ′) because fi j ∈O (Ui), so
(Ui)s ∩V ′ →Vi is a morphism, and hence V ′ →V is a morphism.
□
We will also use the following theorem of Temkin.
Theorem 6.15 ([Tem00, Theorem 4.1]). Let f : X ′ →X be a morphism of good strictly
K-analytic spaces, let x′ ∈X ′, and let x = f (x′). Let ϕ: P f
H (x′)/eK →P f
H (x)/eK be the natural
morphism. Then x ∈Int(X ′/X) if and only if ϕ−1(red(X, x)) = red(X ′, x′).
6.16 (Residues of PL functions). Let h: X →R be a PL function on a good strictly K-
analytic space X. For x ∈X, Chambert–Loir and Ducros deﬁne a canonical invertible
sheaf Lh(x) on the ringed space red(X, x), which is called the residue of h at x. It can be
described as follows, using [CD12, Exemple 6.6.8]. Let U be a compact strictly analytic
neighbourhood of x. By 5.6, there exists a formal K◦-model (U,L) of (U,OX|U) such that
h = −log∥1∥L on U. This L restricts to an invertible sheaf LU,x on VU,x, and we get an
invertible sheaf Lh(x) = π∗
U,xLU,x on red(X, x).
Let PL(X, x) denote the group of germs of PL functions on X at x; this is intrinsic to
the germ (X, x). Applying the above to germs of PL functions at x, we obtain a homo-
morphism L: PL(X, x) →Pic(red(X, x)), denoted h 7→Lh(x).
Lemma 6.17. Let (X, x) be a good strictly K-analytic germ. If h ∈PL(X, x) has the form
log|f | for an invertible function f , then Lh(x) = 0 in Pic(red(X, x)).
Proof. Choose a compact strictly analytic space X and a point x ∈X representing (X, x)
such that there exists an invertible function f on X with h = log|f |. Since X is compact,
there exists a formal K◦-model X of X. Let L = OX · f , regarded as a subsheaf of the sheaf
U 7→Γ(Uη,OX) on X. Then ∥1∥L = |f |−1, and hence h = −log∥1∥L. Since L is trivial, so
is LX,x, so we conclude that Lh(x) = 0.
□


## GJR actual PDF page 43

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
43
Now we want to extend 6.16 to Λ-PL functions. Let PLΛ(X, x) denote the group of
germs of Λ-PL functions on (X, x). We call h ∈PLΛ(X, x) Λ-linear if there are f1,..., fr ∈
O ×
X,x and λ1,...,λr ∈Λ such that h =
Pr
j=1 λj log|f j| in a neighbourhood of x.
Lemma 6.18. Suppose that Λ = Z or that Λ is divisible. Then there is a unique homomor-
phism
h 7→Lh(x): PLΛ(X, x) −→Pic(red(X, x))Λ
such that, if h =
Pm
i=1 λihi with λi ∈Λ and hi ∈PL(X, x), then Lh(x) =
Pm
i=1 λi Lhi(x).
The kernel of this homomorphism consists precisely of the Λ-linear functions in PLΛ(X, x).
Proof. We have to show that Lh(x) :=
Pm
i=1 λiLhi(x) is well-deﬁned. If
Pm
i=1 λihi = 0 for
λi ∈Λ and hi ∈PL(X, x), then we need
Pm
i=1 λi Lhi(x) = 0. By Lemma 5.10, we may
assume {λ1,...,λm} is linearly independent over Q. Choose a compact strictly analytic
space X and a point x ∈X representing (X, x) such that each hi extends to a PL function
hi : X →R. Shrinking X, we may assume X is connected and
Pm
i=1 λihi = 0 on X.
We claim that each hi is constant on X. Using [Ber93, Lemma 1.6.2], we see that X
is G-connected and hence the claim is G-local on X. It follows from [BGR84, Proposi-
tion 9.1.4/8] that X is G-locally connected, so we may assume that hi = −log|fi| for
an invertible analytic function fi on a connected strictly analytic domain U ⊂X. Let
T = Gm
m and let ϕ = (f1,..., fm): U →Tan, so ϕtrop = (h1,...,hm). Since
Pm
i=1 λihi = 0,
the tropical variety ϕtrop(U) is contained in the hyperplane H = {(x1,..., xm) ∈Rm |
λ1x1 + ··· + λmxm = 0}. If ϕtrop is not constant, then ϕtrop(U) has positive dimension
because U is connected. It follows from 3.2 that ϕtrop(U) contains a (Z,Γ)-polytope of
dimension one, which is a line segment with rational slopes. The tangent space of this
segment contains a non-zero vector in H of the form (a1,..., an) ∈Qn, which contradicts
the linear independence of {λ1,...,λn} over Q. This proves the claim; moreover, since
ϕtrop(U) is a (Z,Γ)-point in Rn, this shows that hi is a constant function γi for γi ∈
p
Γ .
Choose a positive integer N such that Nγi ∈Γ for all i, so that Nγi = −log|βi| for
βi ∈K×. Then Nhi = −N log|βi|, so LNhi(x) = 0 by Lemma 6.17. Thus N Lh(x) =
Pm
i=1 λiLNhi(x) = 0, so Lh(x) = 0 because Λ is divisible.
To prove the last claim, it is obvious from the deﬁnition of the residue Lh(x) that Λ-
linear functions h ∈PLΛ(X, x) are in the kernel of the homomorphism. Conversely, let
h ∈PLΛ(X, x) with Lh(x) = 0. We note ﬁrst that for Λ = Z, the claim follows from [CD12,
6.6.2]. Indeed, Chambert-Loir and Ducros show that h induces a metric on OX which is
isometric to the trivial metric on a neighbourhood U of x and hence there is f ∈O (U)×
such that h = log|f | on U. It is clear that the case Λ = Z readily yields the case Λ = Q
by clearing denominators.
For Λ divisible, we reduce to Λ = Q as follows. There are h1,...,hr ∈PLQ(X, x) and
λ1,...,λr ∈Λ with h =
Pr
i=1 λihi. By Lemma 5.10 again, we may assume that λ1,...,λr
are Q-linearly independent. It is enough to prove that Lhi(x) = 0 for all i ∈{1,..., r} as
then the special case Λ = Q above shows that hi is Q-linear, and hence that h is Λ-linear.
We argue by contradiction. Then there is a Q-linear form ℓ: Pic(red(X, x))Q →Q with
ℓ(Lhi(x)) ̸= 0 for at least one i ∈{1,..., r}. This extends by linearity to a homomorphism


## GJR actual PDF page 44

44
W. GUBLER, P. JELL, AND J. RABINOFF
ℓ: Pic(red(X, x))Λ →R, and
0 = ℓ(Lh(x)) =
r
X
i=1
λiℓ(Lhi(x))
is a non-trivial Q-linear combination of λ1,...,λr which is a contradiction.
□
6.19 (Functoriality of residues). Let f : (X ′, x′) →(X, x) be a morphism of good strictly
K-analytic germs. For h ∈PLΛ(X, x), we get h′ = h◦f ∈PLΛ(X ′, x′). We have an induced
morphism ef : red(X ′, x′) →red(X, x), and Lh′(x′) = ef ∗Lh(x) by [CD12, 6.6.7]. A similar
statement holds for extension of scalars.
7. SEMIPOSITIVITY AND HARMONIC FUNCTIONS
In this section, we study positivity conditions on piecewise linear functions. We will
introduce the crucial notion of a harmonic function, on which our theory of differential
forms rests. We consider a good strictly K-analytic space X and an additive subgroup
Λ ⊂R. We will always assume that Λ = Z or that Λ is divisible.
We can characterize semipositivity either in terms of formal geometry or residues of
Λ-PL functions, as elaborated in 6. A line bundle L on an admissible formal scheme X
is called nef (resp. numerically trivial) if its restriction to Xs has the same property. In
other words, the line bundle L is nef if the degree of L|C is nonnegative for every closed
integral curve C ⊂Xs which is proper over eK.5
Let X be a formal K◦-model of a paracompact good strictly K-analytic space X. Recall
from 5.5 that M(X) denotes the group of models of OX, and that we have deﬁned a
homomorphism h 7→hL: M(X)Λ →PL(X)Λ. We will also use the residue Lh(x) of h at
x ∈X from 6.16.
Proposition 7.1. Let h: X →R be a Λ-PL function and x ∈X. The following are equivalent:
(1) There exists a paracompact neighbourhood U of x in X, a formal K◦-model U of U,
and a nef (resp. numerically trivial) element L ∈M(U)Λ, such that h|U = hL.
(2) The residue Lh(x) ∈Pic(red(X, x))Λ is nef (resp. numerically trivial).
Proof. The ﬁrst assertion implies the second by the description of Lh(x) in 6.16. We will
prove the nef case, as the numerically trivial case is identical. The following argument
is similar to [GK19, Proposition 6.5]. Suppose that Lh(x) is nef. By Corollary 5.9, there
exists a compact strictly analytic neighbourhood U of x, a formal K◦-model U of U, and an
element L ∈M(U)Λ, such that h = hL. As in 6.16 we let VU,x be the closure of redU(x) and
we let LU,x be the restriction of L to VU,x. Then (VU,x,LU,x) is a model of (red(X, x), Lh(x)),
so LU,x is nef by Lemma 6.11. Let W be a compact, strictly analytic neighbourhood of x
contained in the open set red−1
U (VU,x). By [BL93a, Lemma 4.4], there exists an admissible
formal blowup f : U′ →U such that W = Wη for a formal open subset W ⊂U′. Note that
h|W = hf ∗L|W. We claim that f ∗L|W is nef.
5If X is a proper K◦-model of a proper variety X over K and L is a line bundle on X with L = L |X
such that the restriction of L to the special ﬁber of X is nef, then L is a nef line bundle on X by [GM19,
4.8].


## GJR actual PDF page 45

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
45
By functoriality of reductions, the set-theoretic image of W under f is contained in
VU,x. In particular, if C is any integral, proper subcurve of Ws, then f (C) ⊂VU,x. Since
C is reduced, the schematic image of C is contained in VU,x, so we have a commutative
square of morphisms of ek-schemes:
C
/
f

Ws
f
VU,x
/ Us
Since LU,x is nef, we have f ∗LU,x.C ≥0 by the projection formula.
□
Deﬁnition 7.2. A Λ-PL function h: X →R is called semipositive at a point x ∈X if it
satisﬁes the equivalent conditions of Proposition 7.1, and it is harmonic at x if both h
and −h are semipositive at x. We say that h is semipositive if it is semipositive at all
points of X.
A harmonic function on X is an R-PL function h: X →R which is harmonic at all points
of X. A Λ-PL harmonic function is called Λ-harmonic.
7.3. Some remarks:
(1) A Λ-PL function h is harmonic at x ∈X if and only if Lh(x) is numerically trivial.
Equivalently, there exists a paracompact neighbourhood U of x, a formal K◦-
model U of U, and a numerically trivial element L ∈M(U)Λ, such that h = hL.
(2) Semipositivity and harmonicity are insensitive to the group Λ, in the following
sense: if h ∈PLΛ(X), then h is semipositive at a point x if and only if its image in
PLR(X) is semipositive at x.
(3) Semipositivity and harmonicity of h at x is intrinsic to the germ of h in PLΛ(X, x).
In particular, the semipositive (resp. harmonic) functions on X form a sheaf in
the analytic topology. (They do not form a sheaf in the G-topology).
(4) It follows from Proposition 7.1(1) that the locus of all points x ∈X at which h is
semipositive (resp. harmonic) is open.
(5) The set of semipositive functions at a point forms a monoid (resp. a cone if
Λ = R), and the set of harmonic functions at a point forms a group (resp. an
R-subspace).
(6) If h = log|f | for an invertible analytic function f in a neighbourhood of x, then h
is harmonic at x by Lemma 6.17 (the converse does not hold: see Remark 15.10).
(7) Harmonic functions generalize smooth functions in the same way that numerical
equivalence generalizes rational equivalence in algebraic geometry.
Lemma 7.4. Suppose that X is paracompact. Let X be a formal K◦-model of X and let L ∈
M(X)Λ. Then hL is semipositive (resp. harmonic) if and only if L is nef (resp. numerically
trivial).
Proof. The harmonic case follows from the semipositive case. If L is nef then hL is semi-
positive by deﬁnition. Suppose then that h := hL is semipositive. Let C ⊂Xs be an
integral, proper closed curve. By surjectivity of redX, there exists a point x ∈X reducing
to the generic point of C. Then (C,L|C) is a model of (red(X, x), Lh(x)), so L|C is nef by
Lemma 6.11. In particular, c1(L).C ≥0, so L is nef.
□


## GJR actual PDF page 47

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
47
To prove (2), let ϕ: P f
H (x′)/eK′ →P f
H (x)/eK be the natural morphism. We have seen in 6.13
that ϕ−1(red(X, x)) = red(X ′, x′). The assertions now follow from Lemma 6.12 and
functoriality of residues 6.19. To prove (2′), by Corollary 5.9 we may shrink X such that
X is compact with formal model X and such that there is L ∈M(X)Λ with h = hL. Then
the claim follows from Lemma 6.8(2) and Lemma 7.4.
The claims (3) and (3′) follow from (7.6,1′) since Xred →X is proper and surjective.
□
The following proposition allows us to pass to Galois extensions when studying har-
monic and semipositive functions.
Proposition 7.7. Suppose that Λ is divisible. Let L/K be a (potentially inﬁnite) normal
extension with automorphism group G := Aut(L/K). Let K′ be the completion of L and let
X ′ := X b⊗KK′, with structure morphism π: X ′ →X. Then h 7→h ◦π induces an isomor-
phism from the monoid of semipositive Λ-PL functions on X (resp. the group of Λ-harmonic
functions on X) to the monoid of G-invariant semipositive Λ-PL functions on X ′ (resp. the
group of G-invariant Λ-harmonic functions on X ′).
Proof. This is an immediate consequence of Corollary 5.13 and Proposition 7.6(2′).
□
Our next goal is to approximate locally semipositive metrics by local Fubini–Study
metrics (Proposition 7.10). This will be a crucial ingredient in proving the balancing
condition in Section 9.
Recall that a line bundle on a scheme Y is called semiample if some positive tensor
power is globally generated. We say that L ∈Pic(Y )R is ample (resp. semiample) if there
are ample (resp. semiample) line bundles H1,..., Hr and λ1,...,λr ∈R≥0 such that L =
Pr
j=1 λjH j ∈Pic(Y)R. An ample L is semiample and a semiample L is nef.
Deﬁnition 7.8. Let h: X →R be an R-PL function. We say that h is Fubini–Study at a
point x ∈X if Lh(x) is semiample. We say that h is locally Fubini–Study or LFS if it is
Fubini–Study at every point of X.
Clearly if h is Fubini–Study at x then it is semipositive at x.
7.9. It follows from [CD12, Proposition 6.8.2] that h is Fubini–Study at x if and only if
there is an open neighbourhood U of x such that h|U is an R≥0-linear combination of func-
tions of the form max{−log|f1|,...,−log|fn|} for invertible analytic functions f1,..., fn
on U.
The following proposition can be seen as a local analogue of the fact that one can
approximate a nef Q-line bundle by ample Q-line bundles on a projective variety.
Proposition 7.10. Let h: X →R be an R-PL function that is semipositive at a point x ∈
Int(X). Then there exists a strictly analytic neighbourhood U of x and a sequence h1,h2,...
of R-PL LFS functions on U such that hi →h|U uniformly.
Proof. We may shrink X to assume it is compact. By Corollary 5.9, we may assume that
there exists a formal K◦-model X of X and a line bundle L ∈M(X)R with h = hL, using
the notation of 5.7. Since x is inner, the closure VX,x of redX(x) in Xs is proper (with the
notation of 6.13): see [CD12, Lemma 6.5.1] and [Vil21, Appendix A]. By Chow’s lemma,


## GJR actual PDF page 48

48
W. GUBLER, P. JELL, AND J. RABINOFF
there is a proper birational morphism V →VX,x with V projective over eK. Let L′ be an
ample line bundle on V. By [CD12, 6.6.5], there is a PL function h′ on the germ (X, x)
such that (V, L′) is a model of the residue Lh′(x). Let U be a compact strictly analytic
neighbourhood of x on which h′ is deﬁned. Then there is a formal K◦-model U of U and
a line bundle L′ on U with h′ = hL′. By Lemma 6.14, there is a compact strictly analytic
neighbourhood U′ of x and a formal K◦-model U′ of U′ such that the closure V ′ := VU′,x
of redU′(x) dominates V. We may assume that U′ ⊂U and that this inclusion extends to
a morphism f : U′ →U by using Raynaud’s theorem. Let L′|V ′ be the pull-back of L′ with
respect to V ′ →V. Then L′|V ′ and f ∗(L′)|V ′ are both models for Lh′(x). We conclude that
there is a dominating model V ′′ of red(X, x) such that the pull-backs of L′|V ′ and f ∗(L′)|V ′
to V ′′ agree. Using Lemma 6.14 again and the arguments above, we may assume that
V ′′ = VU′′,x for a formal K◦-model U′′ of a compact strictly analytic neighbourhood U′′
of x contained in U′ such that the inclusion U′′ ⊂U′ extends to a morphism U′′ →U′.
Moreover, we may assume that U′′ ⊂X extends to a morphism U′′ →X. Replacing X by
U′′ and L,L′ by their pull-backs to U′′, we put ourselves in the following situation:
(1) The closure V ′ of redX(x) in Xs dominates V.
(2) There is L ∈M(X)R and L ∈Pic(V)R such that h = hL and L|V ′ is the pullback of
L under V ′ →V, and such that (V, L) is a model of Lh(x).
(3) There is a line bundle L′ on X and an ample line bundle L′ on V such that h′ = hL′
and L′|V ′ is the pullback of L′ under V ′ →V.
We recycle notation now and let U := red−1
X (V ′). By anticontinuity of the reduction map,
the set U is an open neighbourhood of x. For ǫ ∈Q>0 let Lǫ := L + ǫL′, Lǫ := L + ǫL′,
and hǫ := hLǫ = h + ǫh′. Then hǫ is an R-PL function on X and Lǫ|V ′ is the pullback of Lǫ
under V ′ →V. Note that hǫ →h uniformly as ǫ →0. If h is semipositive at x then L is
nef by Lemma 6.11, so Lǫ is ample as a consequence of Kleiman’s theorem, see [Laz04,
Corollary 1.4.10]. It follows that Lǫ|V ′ is semiample. If y ∈U then redX(y) ∈V ′, so the
closure Y of redX(y) in Xs is contained in V ′. Since h = hL and h′ = hL′ on all of X,
the pair (Y,Lǫ|Y) is a model of Lhǫ(y) by the construction in 6.16. Since Lǫ|Y is again
semiample, we see that hǫ is Fubini–Study at y. Thus hǫ is LFS on U.
□
Remark 7.11. Let X be a proper scheme over K. It is shown in [GM19, Section 5] that
a pointwise limit of semipositive Q-PL metrics is semipositive. We expect the analogous
result to hold in our situation. In particular, we expect the converse of Proposition 7.10
to hold true: namely, if an R-PL function h is a uniform limit of R-PL LFS functions on
a strictly analytic neighbourhood U of an interior point x, then h is semipositive at x.
This would imply that if h and h′ are R-PL functions that are semipositive at x, then so is
max{h,h′}. Indeed, we can write h = limhi and h′ = limh′
i for R-PL LFS functions hi,h′
i
in a neighbourhood U of x. By 7.9, the functions max{hi,h′
i} are R-PL LFS functions on
U, and we have max{h,h′} = limmax{hi,h′
i}.
Now we relate semipositivity to positive forms and currents. See 2.8 for the deﬁnitions
of positivity based on the corresponding notions for Lagerberg forms and Lagerberg cur-
rents introduced in 2.7. The next result serves as a replacement for [CD12, Lemmas 5.2.3
and 5.3.3] where the result is claimed for strongly positive forms; this is not correct, as
explained in [BGJK21a, Example 2.3.6].


## GJR actual PDF page 77

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
77
of harmonic functions introduced in Section 7 agrees in the case of a rig-smooth curve
with the harmonic functions in Thuillier’s thesis [Thu05]. This will be important in the
companion paper [GJR21].
First, we recall some notions from the theory of graphs and their relationship to the
structure of non-Archimedean analytic curves. For more details, we refer to [GJR21].
15.1 (Metric Graphs with Boundary). We consider a weighted metric graph (Σ,∂Σ) with
boundary. This is a ﬁnite multigraph with no loop edges endowed with positive edge
lengths assumed to be in Γ. The boundary ∂Σ is any subset of the vertices of Σ. Every
edge is endowed with the additional datum of a weight w(e) ∈Z>0. If we ignore the
boundary, then we get a compact piecewise (Z,Γ)-linear space of dimension at most 1 as
introduced in 2.5. (Note that isolated vertices are allowed.)
A function h: Σ →R is called harmonic if the restriction of h to any edge is afﬁne
R-linear, and if for any vertex x of Σ\∂Σ, we have
P
e−=x w(e)de(h) = 0, where e ranges
over all edges with tail vertex x and de(h) is the outgoing slope of h at x in the direction
of e.
For a subgroup Λ of R containing Γ, we let Σ(Λ) denote the subset of Σ consisting of
all points x such that f (x) ∈Λ for all (Z,Γ)-linear functions f on an edge e containing
x. Let U ⊂Σ be a subgraph with vertices contained in Σ(
p
Γ ). A function h: U →R
is called piecewise (Z,Γ)-linear if there is a subdivision of the subgraph U such that the
vertices of the subdivision are in Σ(
p
Γ) and such that the restriction of h to any edge e
of the subdivision extends to a (Z,Γ)-linear function on the edge of Σ containing e.
15.2 (Skeletons of Curves). Metric graphs with boundary arise in non-Archimedean ge-
ometry as follows. Let X be a compact rig-smooth curve over K, i.e., a compact rig-smooth
strictly analytic space of pure dimension 1. We assume that X has a strictly semistable
model X over the valuation ring K◦. This is a formal K◦-model of X (see 2.4) whose spe-
cial ﬁber Xs is geometrically reduced with smooth irreducible components and at most
double points as singularities. This is equivalent to [Thu05, Deﬁnition 2.2.8], where
such models are called simplement semi-stable. To such a model is associated a weighted
metric graph with boundary Σ := S(X), called the skeleton of X. There is a canonical
inclusion Σ ,→X. The vertices of Σ correspond to the irreducible components of Xs and
the edges correspond to the singular points of Xs, so that Σ is the incidence graph of Xs.
The boundary ∂Σ consists of the vertices of Σ corresponding to non-proper irreducible
components of Xs. If x ∈Xs is a singular point with corresponding edge e, then the
weight of e is deﬁned to be w(e) = [eK(x) : eK]. There is an étale neighbourhood of x of
the form Spf(K{X, Y }/(X Y −̟)) for some ̟ ∈K◦◦\ {0}; the length of e is then deﬁned
to be v(̟). There is a canonical deformation retraction map τ: X →S(X).
15.3 (Subdivisions of the Skeleton). Consider a subdivision Σ′ of the skeleton Σ = S(X)
such that all vertices of Σ′ are in Σ(
p
Γ). Vilsmeier [Vil21, Construction 2.6] has de-
ﬁned a canonical formal scheme X′ with generic ﬁber X and reduced special ﬁber, and a
canonical morphism ι: X′ →X extending IdX, such that for any edge e′ of Σ′, the analytic
subdomain (τ)−1(e′) of X is the generic ﬁber of an open subset of X′. Note that X′ is not
necessarily an admissible formal scheme, i.e. not necessarily of topologically ﬁnite type.


## GJR actual PDF page 78

78
W. GUBLER, P. JELL, AND J. RABINOFF
By [Gub13b, Propositions 6.7 and 6.9], the formal scheme X′ is admissible if the value
group Γ is discrete or if the vertices of Σ′ are contained in Σ(Γ).
15.4 (Piecewise Afﬁne Functions on the Skeleton). Let Σ = S(X) as in 15.2, let U be a
subgraph of Σ with vertices contained in Σ(
p
Γ ), and let h: U →R be a piecewise (Z,Γ)-
linear function in the sense of 15.1. Passing to a subdivision of U, we may assume that
h is (Z,Γ)-linear on each edge of U. The vertices of U induce a subdivision Σ′ of Σ; we
denote the associated formal K◦-model of X by X′ as in 15.3, with canonical morphism
ι: X′ →X. When Γ dense in R, we assume that all vertices of U are in Σ(Γ); then
X′ is an admissible formal scheme. The subset Y := τ−1(U) is the generic ﬁber of a
unique open formal subscheme Y′ in X′. By the arguments used in the proof of [Vil21,
Proposition 2.11], there is a canonical vertical Cartier divisor D on Y′ with associated
formal metric on OY determined by −log∥1∥O (D) = h ◦τ. See 5.5.
Proposition 15.5. Let X be a compact rig-smooth curve over K and let h: X →R.
(1) If X is a strictly semistable model of X over K◦, then h = hL for a line bundle
L ∈M(X) if and only if there is a function f : S(X) →R which is (Z,Γ)-linear on
each edge such that h = f ◦τ.
(2) If x ∈∂X, then h is harmonic at x if and only if h is R-PL at x.
Proof. The “if” part in (1) follows from 15.4. Conversely, assume that h = hL for L ∈
M(X). Using the identiﬁcation L|X = OX, the meromorphic section 1 of L induces a
vertical Cartier divisor D on X. There is a covering of X by open subsets U such that S(U)
is either an edge or a vertex of S(X) and such that D|U = div(γ) for some γ ∈O(U)×,
where U = Uη. It follows from [Ber99, Theorem 5.3 and Step 13 in its proof] that
h|U = −log|γ| factorizes through a (Z,Γ)-linear function on S(U). This proves (1).
Since x ∈∂X, the curve ∂X is afﬁne and hence the nef condition in Proposition 7.1 is
vacuous. This proves (2).
□
15.6 (Thuillier’s Harmonic Functions). We consider now an arbitrary rig-smooth curve
X over K. We call a function h: X →R harmonic in the sense of Thuillier if every x ∈X
has a strictly afﬁnoid neighbourhood V, a ﬁnite Galois extension K′/K, and a strictly
semistable model V′ of V ′ := V ⊗K K′, such that the pullback h′ of h|V factorizes through
the skeleton S(V′) and such that h′|S(V′) is a harmonic function on the skeleton S(V′)
considered as a weighted metric graph with boundary as in 15.2.
For x ∈∂X, Proposition 15.5 and Corollary 5.12 show that the above harmonicity
condition at x is equivalent to piecewise R-linearity at x, using that the boundary of
S(X) is ∂X. Note that Thuillier [Thu05, Section 2.3] used this deﬁnition only for strictly
afﬁnoid or boundaryfree X, so the above deﬁnition is slightly more general than his.
Proposition 15.7. Let X be a rig-smooth curve. Then a function h: X →R is harmonic in
the sense of Deﬁnition 7.2 if and only if h is harmonic in the sense of Thuillier.
Proof. The claim is local on X, so we may assume X strictly afﬁnoid. We ﬁrst show
that the harmonicity notions agree for a piecewise linear function h ∈PL(X). By 5.6,
we have that h = −log∥1∥L for a model L of OX on a formal K◦-model X of X. Using
base change, Proposition 7.6 and [Thu05, Remarque 2.3.17], we are free to pass to a


## GJR actual PDF page 79

FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS
79
ﬁnite Galois extension of K. Arguing locally, the semistable reduction theorem ([Thu05,
Théorème 2.3.8] under these hypotheses; see also [BL85, Section 7] and [Duc24, Theo-
rem 5.1.14(iv), 6.1.3]) shows that we may assume that X is a strictly semistable model.
By Proposition 15.5, there is a function f on the skeleton S(X) which is (Z,Γ)-linear on
each edge such that h = f ◦τ. For x ∈S(X) \ ∂X with corresponding proper irreducible
component C := redX(x) of Xs, it follows as in [KRZB16, Theorem 2.6] that the sum of
outgoing slopes of f at x is equal to deg(L|C). We conclude that h is harmonic in the
sense of Thuillier if and only if L is numerically equivalent to 0. The latter is equivalent
to harmonicity of h in the sense of Deﬁnition 7.2, as we have shown in Lemma 7.4.
Now we prove the proposition for any function h: X →R. Assume that h is a harmonic
function on X as in Deﬁnition 7.2. By Proposition 7.5, the function h is locally an R-linear
combination of Z-harmonic functions, so we are reduced to the case handled above since
the set of Thuillier-harmonic functions forms a real vector space.
Conversely, let h be a harmonic function in the sense of Thuillier. We have to check
for any x ∈X that h is harmonic at x. As above, we are free to pass to a ﬁnite Galois
extension of X, so we may extend scalars and shrink X to assume that X has a strictly
semistable model X and that h factorizes through a harmonic function f : S(X) →R. It
is enough to show that f is an R-linear combination of piecewise (Z,Γ)-linear harmonic
functions fi on S(X). Indeed, by Proposition 15.5, we have that fi ◦τ is piecewise linear,
so fi ◦τ is harmonic by the the ﬁrst paragraph of this proof, and hence h is harmonic.
Suppose ﬁrst that x ∈∂X = ∂S(X). After shrinking X, we may assume that S(X)
is a star around the vertex x, so that f is afﬁne R-linear on each edge. Translating by
a constant function, we may assume f (x) = 0. Then f is an R-linear combination of
piecewise Z-linear functions fe on S(X): namely, the functions fe that have slope 1 on a
given edge e and slope 0 on the others. Since x ∈∂S(X), Proposition 15.5 yields that
each fe is harmonic and hence h is harmonic.
If x ∈X \ ∂X, then as above, we may assume that S(X) is either an edge containing
τ(x) in its interior, or that S(X) is a star around the vertex τ(x). In the ﬁrst case, f is
an R-multiple of a (Z,Γ)-linear function on the edge, so h is harmonic. In the second
case, we may assume that f (τ(x)) = 0. Then f is harmonic if and only if f is linear on
each edge and the weighted sum of the outgoing slopes at τ(x) is zero. This is a linear
equation for the slopes which is deﬁned over Q, so there is a basis of solutions deﬁned
over Q and even over Z. The elements fi of such a basis induce piecewise (Z,Γ)-linear
functions fi which are harmonic on S(X). Since f is an R-linear combination of the fi,
we have that h is harmonic.
□
Note that Γ is either dense in R or is a discrete subgroup. In the following, we set
Λ := Γ if Γ is dense and Λ :=
p
Γ (the divisible hull in R) if Γ is discrete. When Γ is
discrete, we may rescale the valuation to assume Γ = Z.
15.8. Let X be a compact rig-smooth curve over K with strictly semistable model X. As
in 15.2, the skeleton S(X) is viewed as a weighted metric graph with boundary. Let U
be a subgraph of Σ := S(X) with vertices contained in Σ(Λ), then τ−1(U) is a compact
strictly analytic domain in X.


## GJR actual PDF page 80

80
W. GUBLER, P. JELL, AND J. RABINOFF
Proposition 15.9. With the notation above, let f : U →R be a piecewise (Z,Γ)-linear
harmonic function as in 15.1. Then h := f ◦τ: τ−1(U) →R is Z-harmonic.
Proof. Replacing U be a subdivision, we may assume that f is afﬁne (Z,Γ)-linear on each
edge. The vertices of U induce a subdivison of S(X) and hence 15.3 yields a canonical
formal K◦-model X′ of X over X. By 15.4, we get a canonical open formal subscheme Y′ of
X′ with generic ﬁber Y = τ−1(U). It follows from 5.6 and 15.4 that h is piecewise linear,
so by deﬁnition, it is Z-harmonic if and only if it is harmonic. After a ﬁnite, separable
extension of the ground ﬁeld, the graph U becomes a skeleton of Y with respect to some
strictly semistable model (see Remark 5.3.6 in [GJR21]). Thus h is harmonic in the sense
of Thuillier, so by Proposition 15.7, it is harmonic in the sense of Deﬁnition 7.2.
□
Remark 15.10. Let X be a smooth curve (that is, a rig-smooth curve without boundary),
let H be the sheaf of harmonic functions on X, and let F be the subsheaf of R-vector
spaces generated by the germs log|f | for local invertible analytic functions f . Then Thuil-
lier [Thu05, 2.3.4] has shown that F might be a strict subsheaf of H , with equality when
X is potentially locally isomorphic to P1,an or when eK is algebraic over a ﬁnite ﬁeld. It was
shown in [Wan16, 5.2, 5.3] that F is the kernel of d′d′′: A0,0
sm →A1,1
sm and that F is the
sheaf of smooth harmonic functions on X. The latter follows also by Proposition 10.17.
We conclude that there is a non-smooth harmonic function on an open subset of X if and
only if the inclusion F ⊂H is strict. If F = H , then every harmonic tropicalization
map is a smooth tropicalization map, and Asm = A.
Wanner’s regularization theorem [Wan19, Corollary 5.4], obtained for Mumford curves
or in case of an algebraic residue ﬁeld over a ﬁnite ﬁeld, can now be generalized as fol-
lows (compare Remark 15.10).
Proposition 15.11. Let X be a smooth curve (a rig-smooth curve without boundary) over
a non-trivially valued non-Archimedean ﬁeld K, and let f be a subharmonic function on X
as deﬁned in [Thu05, 3.1.2]. Then for any relatively compact open subset U of X, there is
a decreasing net of weakly smooth psh functions fi on U converging pointwise to f |U.
Proof. By Thuillier’s regularization theorem [Thu05, Théorème 3.4.2], there is a decreas-
ing net of piecewise R-linear subharmonic functions on U converging pointwise to f , so
we may assume that f is piecewise R-linear. (Note that piecewise R-linear functions are
called lisse in [Thu05, Deﬁnition 3.2.1].) As in the proof of [Thu05, Theorem 3.4.2],
we may assume that U = Y \ ∂Y for a compact strictly analytic domain Y of X. By
[Thu05, Proposition 3.2.4], there is a ﬁnite Galois extension K′/K such that Y has a
strictly semistable model Y over the valuation ring of K′ and such that f = F ◦τ for a
piecewise R-linear function F on the skeleton S(Y), where τ: Y →S(Y) is the retraction.
Since the subharmonic functions over K are the Galois-invariant subharmonic functions
over K′ and the same holds for weakly smooth functions, it is enough to prove the claim
over K′, so we may assume K = K′.
Now we can follow Wanner’s arguments [Wan19, Lemma 5.2]. Note that the curvature
ddc(f |U) is a discrete measure on U; we denote by S its support. In what follows, we
allow subdivisions of Σ := S(Y) at arbitrary points in Σ (not just type-II points); we do
not claim that the subdivision is the skeleton of a formal model of U. By subdividing the


## Thu actual PDF page 36

22

la
fr
ontièr
e
du
fermé V
de X
;

la
fr
ontièr
e ∂Ω= Ω−Ω
de
l'ouvert Ω= X −V
de X
.
Démonstration.
Dans
tout
espa e
top
ologique,
la
fron
tière
d'un
fermé
 oïn ide
a
v
e 
 elle
de
l'ouv
ert
 omplémen
taire
;
il
sut
don 
de
prouv
er
que ∂V
s'iden
tie
à
la
fron
tière
du
fermé
V
de X
,
ou
en ore
que V −∂V
 oïn ide
a
v
e 
l'in
térieur
top
ologique
de
 e
fermé.
Puisque,
par
dénition, V −∂V = Int(V ),
la
 on lusion
résulte
des
p
oin
ts
(i)
et
(iii)
de
la
prop
osition
3.1.3
de
[3℄.
2
2.1.3.
Courb
es
stri temen
t k
-analytiques.
Convention.
Pré isons
la
terminologie
que
nous
emploierons
:
-
une S
- 
ourb
e
est
un S
-s 
héma
formel
lo
 alemen
t
de
présen
tation
nie,
séparé,
plat
et
pure-
men
t
de
dimension
1
;
-
une
 
ourb
e
stri tement k
-analytique
est
un
espa e
stri temen
t k
-analytique
au
sens
du
 
ha-
pitre
3
de
[3℄,
para ompa t,
puremen
t
de
dimension
1
et
sans
b
or
d.
Remarque
2.1.11.

Quelques
mots
de
 ommen
taire
s'imp
osen
t
quan
t
à
la
dénition
adop-
tée
de
la
notion
de
 ourb
e
analytique.
1.
Les
espa es k
-analytiques
analytiés
de
 ourb
es
lo
 alemen
t
algébriques
sur k
(séparées)
son
t
des
 ourb
es
stri temen
t k
-analytiques
au
sens
pré éden
t.
2.
Du
p
oin
t
de
vue
adopté
par
Berk
o
vi 
h
dans
[4℄,
nous
 onsidérons
les
espa es
stri temen
t
k
-analytiques
para ompa ts
qui
son
t
puremen
t
de
dimension
1,
sans
b
ord
et
tels
que
tout
p
oin
t
admette
un
v
oisinage k
-anoïde.
Ce i
ex lut,
par
exemple,
la
bre
générique X
du
S
-s 
héma
formel X
,
plat
et
puremen
t
de
dimension
1,
obten
u
en
re ollan
t
deux
 opies
de
A1
S = Spf(k◦{T1})
le
long
de
l'ouv
ert Spf(k◦{T1, T −1
1 })
(via
les
immersions
 anoniques).
En
eet,
l'espa e
stri temen
t k
-analytique X
(au
sens
de
[4℄)
est
le
re ollemen
t
de
deux
 opies
du
disque
unité
fermé E(0, 1) = M(k{T1})
le
long
du
domaine k
-anoïde
{|T1| = 1},
via
les
immersions
 anoniques,
et
le
p
oin
t η
de X
 orresp
ondan
t
au
p
oin
t
de
Shilo
v
de E(0, 1)
ne
p
ossède
pas
de
v
oisinage k
-anoïde
dans X
:
il
existerait
sinon
un
é latemen
t
admissible q : Y →X
tel
que Y
soit
un S
-s 
héma
séparé,
 e
qui
est
absurde
puisque
le
morphisme q
est
séparé
tandis
que
le
morphisme
stru tural X →S
ne
l'est
pas.
3.
Un
espa e k
-anoïde Y
puremen
t
de
dimension
1
est
m
uni
d'un
fais eau
stru tural
en
k
-algèbres OY
tel
que,
p
our
tout
ouv
ert U ⊂Y
Γ(U, OY ) = lim
←−V AV ,
V
par ouran
t
l'ensem
ble
des
domaines k
-anoïdes
 on
ten
us
dans U
et AV
désignan
t
l'algèbre
de V
.
Compte
ten
u
du
fait
que
les
homomorphismes
d'algèbres
stri tement k
-
anoïdes
son
t
automatiquemen
t
 on
tin
us
([8℄,
6.1.3),
nous
p
ouv
ons
reform
uler
 omme
suit
la
dénition
des
 ourb
es
stri temen
t k
-analytiques
que
nous
a
v
ons
adoptée
:
une
 
ourb
e
stri tement k
-analytique X
est
la
donné
e
d'un
esp
a 
e
top
olo
gique
p
ar
a 
omp
a t |X|
et
d'un
fais 
e
au
en k
-algèbr
es OX
sur |X|
tels
que
l'esp
a 
e
annelé (|X|, OX)
soit
lo
 
alement
isomorphe
à (Y −∂Y, OY ), Y
étant
un
esp
a 
e
stri tement k
-anoïde
pur
ement
de
dimension
1.
Une
 ourb
e
stri temen
t k
-analytique
est
un
parti ulier
un
espa e
lo
 alemen
t k
-annelé
et,
toujours
en
v
ertu
de
la
 on
tin
uité
des k
-homomorphismes
d'algèbres
stri temen
t k
-
anoïdes,
les
morphismes
de
 ourb
es
stri temen
t k
-analytiques
son
t
les
morphismes
d'espa es
lo
 alemen
t k
-annelés.


## Thu actual PDF page 40

26
toutes
les
 omp
osan
tes
 onnexes
de Xη −S0(X)
adhéren
tes
à ξ
.
Ce i
prouv
e
l'in lusion
{rX (ξ)} ⊂f−1
s (Z).
T
r
oisième
étap
e.
Il
sut
main
tenan
t
de
dénir
le
prolongemen
t f
de f
 omme
le
morphisme
de
S
-s 
hémas
formels (f s, f♯) : X = (Xs, OX ) →Y = (Ys, OY),
où fs : Xs →Ys
est
l'appli ation
 on
tin
ue
que
l'on
vien
t
de
dé rire
en
tre
les
espa es
top
ologiques
et f♯
est
l'homomorphisme
en
tre
les
fais eaux
stru turaux
 ara térisé
par
la
 ondition
suiv
an
te
:
p
our
tous
ouv
erts
anes
U ⊂Xs
et V ⊂Ys
tels fs(U) ⊂V

 'est-à-dire
tels
que f
en
v
oie
le
domaine
anoïde r−1
X (U)
dans
le
domaine
anoïde r−1
Y (V )
, f ♯
est
l'homomorphisme
de
Γ(U, OX ) = Γ(r−1
X (U), OXη)◦
dans
Γ(V, OY) = Γ(r−1
Y (V ), OYη)◦
induit
par
l'homomorphisme
d'algèbres
stri temen
t k
-anoïdes
f ♯: Γ(r−1
X (U), OXη) →Γ(r−1
Y (V ), OYη).
(ii)
Le
morphisme f
est
lo
 alemen
t
de
t
yp
e
ni.
S'il
est
quasi-ni,
sa
bre
au-dessus
de
tout
p
oin
t
fermé
de Ys
ne
 on
tien
t
au un
p
oin
t
générique
de Xs
,
 ondition
qui
s'é rit
de
manière
équiv
alen
te
sous
la
forme
f(S0(X)) ⊂S0(Y).
Ré ipro
quemen
t,
si
 ette
 ondition
est
v
ériée,
le
raisonnemen
t
 onduit
lors
de
la
deuxième
étap
e
mon
tre
que
les
bres
de f
son
t
dis rètes.
2
Domaines
analytiques
 
omp
a ts.
Pr
oposition
2.1.16.

Soit X
une S
- 
ourb
e
quasi- 
omp
a te
dont
la
br
e
générique
est
irr
é
du tible.
(i
)
Si Xs
est
pr
opr
e, Xη
est
pr
opr
e.
(ii
)
Si Xs
n
'est
p
as
pr
opr
e

 'est-à-dir
e
si
l'une
au
moins
de
ses
 
omp
osantes
irr
é
du tibles
est
ane
, Xη
est
un
esp
a 
e
stri tement k
-anoïde.
Démonstration.
Notons
tout
d'ab
ord
que
les
 omp
osan
tes
irrédu tibles
de
la ek
- ourb
e
sé-
parée Xs
son
t
des ek
- ourb
es
algébriques
anes
ou
propres.
La k◦
-algèbre A = Γ(X, OX )
est
top
ologiquemen
t
de
présen
tation
nie
et
le
morphisme
stru tural X →S
se
fa torise
par Y = Spf(A)
:
X

p
@
@
@
@
@
@
@
Y
~~~~~~~
S.
Le
morphisme ps : Xs →Ys
induit
un
isomorphisme
de
 
haque
 omp
osan
te
irrédu tible
ane
de Xs
sur
une
 omp
osan
te
irrédu tible
ane
de Ys
et
 on
tra te
 
ha une
des
 omp
osan
tes
irrédu tibles
propres
de Xs
sur
un
p
oin
t
de Ys
.
La ek
- ourb
e
algébrique Xs
étan
t
 onnexe, Ys
est
un ek
-s 
héma
ane
 onnexe
et
il
y
a
don 
deux
p
ossibilités
:

si Xs
est
une
 ourb
e
propre, Ys
est
un
p
oin
t,
auquel
 as p
est
la
fa torisation
de
Stein
du
morphisme
propre p
;


## Thu actual PDF page 41

27

si
la
 ourb
e Xs
n'est
pas
propre, Ys
est
une ek
- ourb
e
algébrique
ane.
La
 on lusion
est
immédiate
dans
le
premier
 as
:
l'espa e
stri temen
t k
-analytique Xη
est
 ompa t
et
sans
b
ord
(2.1.2),
don 
propre.
En
visageons
main
tenan
t
le
se ond
 as.
Les
morphismes p
et pη
son
t
pr
opr
es,
surje tifs
et,
leurs
fa torisations
de
Stein
étan
t
manifestemen
t
triviales,
à
bres
 onnexes.
Puisque
l'espa e
stri temen
t k
-analytique Xη
est,
par
h
yp
othèse,
irrédu tible,
l'image
de pη
est
un
sous-espa e
stri temen
t k
-analytique
irrédu tible
de Yη
,
né essairemen
t
de
dimension
1
vu
la
surje tivité
de pη
.
On
en
déduit
que pη
est
une
bije
 tion,
et
don 
un
isomorphisme
([3
℄,
2.2.7,
(iii),
 omplété
par
[4℄,
1.2.1,
Remarks,
(i)).
2
Cor
ollaire
2.1.17.

Soit X
une S
- 
ourb
e
formel
le
sép
ar
é
e
dont
la
br
e
générique X
est
irr
é
du tible
et
soit Y1, Y2 ⊂X
deux
domaines
stri tement k
-anoïdes
;
si Y1 ∪Y2 ̸= X
,
Y1 ∪Y2
est
un
domaine
stri tement k
-anoïde.
Démonstration.
Le
 as
de
deux
domaines
stri temen
t k
-anoïdes
d'in
terse tion
vide
est
trivial
: Y1 ∪Y2 = M(AY1 ⊕AY2).
Nous
p
ouv
ons
don 
supp
oser Y1 ∩Y2 ̸= ∅,
auquel
 as Y1 ∪Y2
est
 onnexe.
Il
existe
un
é latemen
t
admissible q : Y →X
et
des
ouv
erts U1, U2 ⊂Ys
tels
que
Yi =
 Y|Ui

η
([25℄,
3).
Le
morphisme q
étan
t
séparé, Y|U1∪U2
est
une S
- ourb
e
don
t
la
bre
générique Y1 ∪Y2
est
irrédu tible.
Si
la ek
- ourb
e U1 ∪U2
est
pr
opr
e,
 'est
une
partie
ouv
erte
et
fermée
de Ys
;
il
en
est
de
même
p
our Y1 ∪Y2 ⊂Xη
et
don Y1 ∪Y2
puisque Xη
est
 onnexe.
La
 on lusion
dé oule
don 
de
la
prop
osition
pré éden
te.
2
Cor
ollaire
2.1.18.

Soit X
une
 
ourb
e
stri tement k
-analytique
irr
é
du tible
;
tout
 
om-
p
a t
stri t K ⊂X
est
l'interse
 tion
d'une
famil
le
dé
 r
oissante
de
domaines
stri tement k
-
anoïdes.
Démonstration.
Les
domaines
stri temen
t k
-anoïdes
forman
t
un
système
fondamen
tal
de
v
oisinages
des
p
oin
ts
de X
,
tout
 ompa t K ⊂X
est
 on
ten
u
dans
un
domaine
stri temen
t
k
-analytique
 ompa t
de X
.
En
v
ertu
du
 orollaire
pré éden
t,
un
domaine
stri temen
t k
-
analytique
 ompa t
distin t
de X
est
un
domaine
stri temen
t k
-anoïde
;
ainsi,
les
domaines
stri temen
t k
-anoïdes
formen
t
un
système
fondamen
tal
de
v
oisinages
des
 ompa ts
stri ts
de X
.
2
Classi 
ation
des
p
oints.
Soien
t x
un
p
oin
t
d'une
 ourb
e
stri temen
t k
-analytique X
et H(x)
son
 orps
résiduel
 omplété.
L'extension
résiduelle ]
H(x)/ek
est
de
degré
de
trans endan e
au
plus
1,
noté s(x),
et
le
group
e
ab
élien |H(x)×|/|k×|
est
de
rang
au
plus
1,
noté t(x)
;
l'inégalité
s(x) + t(x) ≤1
est
toujours
v
ériée.
Reprenan
t
la
terminologie
de
[3℄,
le
p
oin
t x
sera
dit

de
t
yp
e
(2)
si s(x) = 1,

de
t
yp
e
(3)
si t(x) = 1.
Dans
 es
deux
 as,
l'extension ]
H(x)/ek
et
le
group
e
ab
élien |H(x)×|/|k×|
son
t
de
t
yp
e
ni.
Les
p
oin
ts
de
t
yp
e
(2)
ou
(3)
(resp.
de
t
yp
e
(2))
son
t
en ore
 ara térisés
par
la
propriété
suiv
an
te
: x ∈X
est
de
t
yp
e
(2)
ou
(3)
(resp.
de
t
yp
e
(2))
si
et
seulemen
t
s'il
existe
un
domaine
k
-anoïde
(resp.
un
domaine
stri temen
t k
-anoïde Y ⊂X
)
tel
que Γ(Y ) = {x}.
Lorsque s(x) = t(x) = 0,
le
p
oin
t x
est
dit


## Thu actual PDF page 42

28

de
t
yp
e
(1)
lorsque
l'extension
non
ar 
himédienne H(x)/k
se
plonge
dans
la
 omplétion
d'une
 lôture
algébrique
de k
:
c
ka
k
/
O
H(x),
bDDDDDDDD

de
t
yp
e
(4)
sinon.
P
armi
les
p
oin
ts
de
t
yp
e
(1)
guren
t
en
parti ulier
 eux
tels
que
l'extension H(x)/k
soit
nie
;
 e
son
t
les
p
oin
ts
traditionnellemen
t
 onsidérés
en
géométrie
rigide
et
ils
formen
t
un
sous-ensem
ble
partout
dense
de X
,
noté X0
.
Il
est
 lair
qu'un
morphisme
ni f : Y →X
 onserv
e
le
t
yp
e
des
p
oin
ts
:
tous
les
p
oin
ts
de
la
bre f −1(x)
son
t
du
t
yp
e
de x
;
il
en
v
a
de
même
p
our
le
 
hangemen
t
de
base k →c
ka
.
Lemme
2.1.19.

Soient
x
un
p
oint
d'une
 
ourb
e
stri tement
k
-analytique
X
et
px : X b⊗kH(x) →X
la
pr
oje
 tion
 
anonique
;
les
 
onditions
suivantes
sont
é
quivalentes
:
(i
) x
est
de
typ
e (1)
;
(ii
) s(y) = 0
p
our
tout
p
oint y ∈p−1
x (x).
Démonstration.
On
p
eut
supp
oser X = A1
k
.
Soien
t x
un
p
oin
t
dans A1
k
et x∗: k[T] →H(x)
l'homomorphisme
 orresp
ondan
t
;
le H(x)-
p
oin
t x
de A1
H(x)
déni
par
l'homomorphisme
H(x)[T] →H(x),
T 7→x∗T
est
tel
que px(x) = x
et
on
p
ose
r(x) = sup
p−1
x (x)
|T −x|
([3℄,
4.2).
Le
disque
ouv
ert D(x, r(x)) = {y ∈A1
H(x) ; |T −x|(y) < r(x)}
est
trivialemen
t
 on
ten
u
dans
la
bre p−1
x (x)
et
la
 on lusion
dé oule
de
 e
que
le
p
oin
t x
est
de
t
yp
e
(1)
si
et
seulemen
t
si r(x) = 0
([3℄,
4.2).
2
Extension
des
s 
alair
es.
Soien
t X
une
 ourb
e k
-analytique
et K/k
une
extension
non
ar 
himédienne
;
p
osons XK =
X b⊗kK
et
soit pK : XK →X
le
morphisme
 anonique.
Étan
t
donné
un
p
oin
t x ∈X
de
t
yp
e
(2)
ou
(3),
 onsidérons
un
domaine k
-anoïde Y ⊂X
tel
que Γ(Y ) = {x}.
Le
b
ord
de
Shilo
v
du
domaine K
-anoïde YK = Y b⊗kK
de XK
est
 on
ten
u
dans
la
bre
de p−1
K (x)
d'après
[3℄,
2.2.5
et
il
dénit
un
sous-ensem
ble
ni iK(x)
de
p−1
K (x),
formé
de
p
oin
ts
de
t
yp
e
(2)
ou
(3),
qui
ne
dép
end
 lairemen
t
pas
du
 
hoix
de Y
.
Dans
le
 as
d'un
p
oin
t x
de
t
yp
e
(2), eY
est
une ek
- ourb
e
algébrique
(ane)
in
tègre
et iK(x)
est
l'image
ré ipro
que
de
l'ensem
ble
des
p
oin
ts
génériques
de
la eK
- ourb
e
ane eY ⊗
ek eK
par
l'appli ation
de
rédu tion YK →eY ⊗
ek eK
(2.1.1,
R
é
du tions
).
Lemme
2.1.20.

L'ensemble p−1
K (x) −iK(x)
est
un
ouvert
de XK
.
Démonstration.
C'est
éviden
t
puisque YK −Γ(YK)
est
un
ouv
ert
de XK
en
v
ertu
de
la
prop
osition
2.1.12.
2
Pr
oposition
2.1.21.

Soient X
une
 
ourb
e
stri tement k
-analytique
et Ω⊂X
un
ou-
vert
tel
que
tous
les
p
oints
de ∂Ω
soient
de
typ
e
(2)
ou
(3)
;
étant
donné
e
une
extension
non
ar
 himé
dienne K/k
,
tous
les
p
oints
de ∂p−1
K (Ω)
sont
de
typ
e
(2)
ou
(3).


## Thu actual PDF page 57

43
(p ⊗1) : U ⊗S Spf(K◦) →S(a) ⊗S Spf(K◦)
au-dessus
du
p
oin
t
singulier
est,
de
même,
un
eK
-s 
héma
ni
et
réduit
;
puisqu'il
s'iden
tie
à p−1(p(x))⊗
ek eK
,
il
est
de
rang [κ(ex) : ek]
et
don 
[κ(ex) : ek] =
X
ex′∈p−1
e
K (
ex)
[κ(ex′) : eK].
Cette
dernière
iden
tité
se
réé rit
sous
la
forme
wξ(t) =
X
ξ′∈p−1
K (ξ)
X
t′∈Tξ′S(X)K,t′→t
wξ′(t′),
 e
qui
établit
que pK
est
un
isomorphisme
de
p
oly
èdres
en
tiers
p
ondérés
( f.
remarque
1.2.3,
2).
2
La
notation iK
que
nous
emplo
y
ons
dans
le
lemme
suiv
an
t
a
été
dénie
en
2.1.3
(Extension
des
s 
alair
es
).
Rapp
elons
que,
p
our
tout
p
oin
t x
de X
, s(x)
est
le
degré
de
trans endan e
de
l'extension eH(x)/ek
; x
est
dit
de
t
yp
e
(2)
si
et
seulemen
t
si s(x) = 1.
Lemme
2.2.22.

Soit X
une S
- 
ourb
e
simplement
semi-stable.
(i
)
Étant
donné
un
sous-ensemble
ni Σ ⊂S(X),
il
existe
une
extension
non
ar
 himé
dienne
K/k
et
un
é
 latement
admissible Y →X ×S Spf(K◦)
tels
que Y
soit
une Spf(K◦)- 
ourb
e
simplement
semi-stable
et iK(Σ) ⊂S0(Y).
L'extension K/k
p
eut
êtr
e
 hoisie
nie
(sép
ar
able)
si
et
seulement
si
tous
les
p
oints
de Σ
sont
de
typ
e
(2).
(ii
)
Étant
donné
un
ensemble
ni Σ′
de
p
oints
de
typ
e
(2)
ou
(3)
dans Xη
,
il
existe
une
extension
nie
(sép
ar
able) k′/k
et
un
é
 latement
admissible Y′ →X ×S Spf(k′◦)
tels
que Y′
soit
une Spf(k′◦)- 
ourb
e
simplement
semi-stable
et ik′(Σ′) ⊂S(Y′).
Démonstration.
T
raitons
d'ab
ord
le
 as X = S(a).
(i)
On
p
eut
supp
oser
que
l'ensem
ble Σ
est
réduit
à
un
p
oin
t x.
Considérons
une
extension
non
ar 
himédienne K/k
telle
que |H(x′)×| = |K×|,
où x′
est
le
p
oin
t
de S(S(a))K
 orresp
ondan
t
à x
dans
l'iden
ti ation
 anonique S(S(a))K = S(S(a))
;
 ette
extension
p
eut
être
 
hoisie
si
(et
seulemen
t
si) x
est
de
t
yp
e
(2).
Fixons b ∈K×
tel
que |T0(x′)| = |b|
; |a| ≤|b| ≤1
et
l'é latemen
t
sur S ×S Spf(K◦)
de
l'Idéal (T0, b)

in
v
ersible
en
dehors
du
p
oin
t
singulier
de S(a)s

donne
lieu
à
un
morphisme
q : Z →S(a) ×S Spf(K◦)
tel
que Z
soit
une Spf(K◦)- ourb
e
simplemen
t
semi-stable
et
S0(Z) = S0(S(a)) ∪{x′}.
(ii)
On
p
eut
de
nouv
eau
supp
oser Σ′
réduit
à
un
p
oin
t x.
Si x ∈S(S(a)),
il
n'y
a
rien
à
démon
trer
;
sinon,
le
p
oin
t x′ = τ(x)
de S(S(a))
est
tel
que s(x′) = 1
et
on
vien
t
de
prouv
er
qu'il
existe
une
extension
nie k′/k
telle
que
le
p
oin
t
de S(S(a))k′
  orresp
ondan
t
à
x′
dans
l'iden
ti ation
 anonique S(S(a))k′ = S(S(a))
appartienne
à S0(S(a) ×S Spf(k′◦)).
On
est
ainsi
ramené
au
 as
d'un
p
oin
t x
tel
que τ(x) ∈S0(S(a)).
L'appli ation
de
rédu tion
S(a)η →S(a)s
en
v
oie x
sur
un
p
oin
t
lisse ex
appartenan
t
à
la
 omp
osan
te
irrédu tible
de
p
oin
t
générique r(τ(x)).
Le
 omplémen
taire E
de
la
 omp
osan
te
 onnexe
non
b
ornée
de S(a)η −{x} ⊂A1
k −{x}
est
un
disque
fermé
de
p
oin
t
de
Shilo
v x.
Soit y
un
p
oin
t
dans E
tel
que
l'extension κ(y)/k
soit
nie,
de
p
olynôme
minimal f
normalisé
de
telle
sorte
que |f(τ(x))| = 1
;
 
hoisissons
égalemen
t
b ∈k×
tel
que |f(x)| > |b|.
L'Idéal I
sur S(a)
tel
que I
ex = fOS(a),
ex + bOS(a),
ex
et I = OS(a)
sur S(a)s −{ex}
est
admissible
et
son
é latemen
t q : Z →S(a)
fournit
une S
- ourb
e Z
don
t


## Thu actual PDF page 58

44
la
bre
sp
é iale
est
la
somme
amalgamée
du
diagramme
P1
ek
Spec(ek)
0
O
ex
/ S(a)s,
qui
devien
t
simplemen
t
semi-stable
après
une
extension
nie k′/k
et
telle
que S(Z ×S Spf(k′◦)
 on
tienne
le
sous-ensem
ble ik′(x).
Le
 as
d'une
 ourb
e
simplemen
t
semi-stable
quel onque
se
déduit
dire temen
t
de
 e
qui
pré ède.
On
p
eut
en
eet
supp
oser
que X
est
m
unie
d'un
morphisme
étale p : X →S(a)
 ar
la
question
est
lo
 ale
sur Xη
.
Étan
t
donnée
une
extension
non-ar 
himédienne
(resp.
une
extension
nie) K/k
telle
qu'il
existe
un
é latemen
t
admissible q : Z →S(a) ×S Spf(K◦)
satisfaisan
t
à
la
 ondition
iK(pη(Σ)) ⊂S0(Z)
(resp. iK(Σ) ⊂S(Z)),
l'é latemen
t
admissible q′ : Y →X ×S Spf(K◦)
déni
par
le
diagramme
 artésien
Y
q′
/

X ×S Spf(K◦)
p

Z
q / S(a) ×S Spf(K◦)
fournit
une S
- ourb
e
simplemen
t
semi-stable Y
telle
que iK(Σ) ⊂S0(Y)
(resp. iK(Σ) ⊂
S(Z′)).
L'extension K/k
p
eut
être
 
hoisie
nie
si
tous
les
p
oin
ts
de pη(Σ)
son
t
de
t
yp
e
(2),
don 
si
tous
les
p
oin
ts
de Σ
son
t
de
t
yp
e
(2).
T
outes
les
extensions
nies
p
euv
en
t
être
 
hoisies
séparables.
2
La
prop
osition
suiv
an
te
sera
utilisée
au
 
hapitre
3
( f.
théorème
3.2.10).
Pr
oposition
2.2.23.

Soit Y
un
esp
a 
e k
-anoïde
rig-lisse
de
dimension
1.
T
oute
 
om-
p
osante
 
onnexe Ω
de Int(Y )
et
la
r
éunion
d'une
suite
de
domaines k
-anoïdes
tel
le
que,
p
our
tout n
:
- Vn ⊂Vn+1 −∂Vn+1
;
-
la
fr
ontièr
e
de
 haque
 
omp
osante
 
onnexe
de Vn+1 −Vn
ne
r
en 
ontr
e Vn
(r
esp. Vn+1
)
qu'en
un
seul
p
oint.
Démonstration.
Si
l'on
disp
ose
d'une
telle
suite
après
une
extension
non
ar 
himédienne
K/k
,
son
image
par
la
pro
je tion
 anonique p : Y b⊗kK →Y
satisfait
aux
 onditions
imp
osées
 ar p(∂(V b⊗kK)) = ∂V
p
our
tout
domaine k
-anoïde V
([3
℄,
prop
osition
3.1.3,
(iv)).
Nous
p
ouv
ons
don 
supp
oser
que Y
est
un
domaine
sri temen
t k
-anoïde,
bre
générique
d'une
S
- ourb
e
simplemen
t
semi-stable Y
.
La
 omp
osan
te
 onnexe Ω
de Y = Yη
est
l'image
ré ipro
que
par
l'appli ation
de
rédu tion
r : Yη →Ys
d'un
sous-s 
héma
fermé
(réduit) Z
de Ys
,
propre
sur ek
et
 onnexe.
Les
p
oin
ts
de ∂Ω
son
t
en
bije tion
a
v
e 
l'ensem
ble
des
p
oin
ts
génériques
des
 omp
osan
tes
irrédu tibles
anes
de Ys
ren on
tran
t Z
.
L'in
terse tion Ω∩S(Y)
est
un
ouv
ert
de S(Y).
Elle
est
vide
si
et
seulemen
t
si Z
est
un
p
oin
t
fermé
lisse
de Ys
et
la
 on lusion
est
dans
 e
 as
immédiate
puisque Ω
est
la
réunion
d'une
suite
 roissan
te
de
domaines
stri temen
t k
-anoïdes
a
y
an
t
un
unique
p
oin
t
de
Shilo
v


## Thu actual PDF page 65

51
et
l'égalité
Z
{x}
ddcS(f)∗Φ = (degx f)
Z
{f(x)}
ddcΦ
p
our
toute
fon tion Φ ∈A0(S(Y))
s'en
déduit
immédiatemen
t
par
linéarité.
Le
 as
général
se
déduit
du
pré éden
t
en
appliquan
t
la
prop
osition
2.2.21
et
le
lemme
2.2.22.
2
2.3.
F
on tions
harmoniques
2.3.1.
L'espa e H(X).
Étan
t
donnée
une S
- ourb
e X
,
le
b
ord
de
l'espa e k
-analytique Xη
(2.1.2)
est
le
sous-
ensem
ble ∂Xη
de S0(X)
formé
des
p
oin
ts
au-dessus
des
p
oin
ts
génériques
des
 omp
osan
tes
irrédu tibles
anes
de Xs
.
Définition
2.3.1.

Soit X
une S
- 
ourb
e
simplement
semi-stable
;
le
sous-esp
a 
e
ve
 toriel
τ ∗
X H(S(X), ∂Xη)
de C0(|Xη|, R)
est
noté H(X).
Nous
nous
restreindrons,
dans
 e
qui
suit,
à
la
 onsidération
de S
- ourb
es
simplemen
t
simplemen
t
semi-stables X
qui
son
t
quasi- 
omp
a tes
;
 ette
h
yp
othèse
équiv
aut
à
la
 ompa ité
de
l'espa e
top
ologique |Xη|.
Pr
oposition
2.3.2
(i
)
L
orsque
la ek
- 
ourb
e Xs
est
pr
opr
e, H(X)
est
l'esp
a 
e
des
fon tions
r
é
el
les
lo
 
alement
 
onstantes
sur Xη
.
(ii
)
L
orsque ∂Xη
r
en 
ontr
e
 haque
 
omp
osante
 
onnexe
de |Xη|,
l'appli 
ation
de
r
estri tion
H(X) →Hom(∂Xη, R)
est
bije
 tive.
Démonstration.
(i)
Si
la ek
- ourb
e Xs
est
propre,
l'ensem
ble ∂Xη
est
vide
;
l'assertion
dé oule
don 
du
 orollaire
1.2.11.
(ii)
Si
l'ensem
ble ∂Xη
ren on
tre
 
ha une
des
 omp
osan
tes
 onnexes
de |Xη|,
il
ren on
tre
éga-
lemen
t
 
haque
 omp
osan
te
 onnexe
de S(X)
(remarque
2.2.19,3)
et
l'assertion
dé oule
de
la
prop
osition
1.2.15.
2
Comme
annon é
en
in
tro
du tion
de
 e
 
hapitre,
nous
allons
établir
le
résultat
suiv
an
t.
Pr
oposition
2.3.3.

Soient X
, X ′
deux S
- 
ourb
es
simplement
semi-stables
et f : X ′
η →
Xη
un
morphisme
quasi-ni.
L'appli 
ation R -liné
air
e f ∗: C0(|Xη|, R) →C0(|X ′
η|, R)
envoie
le
sous-esp
a 
e H(X)
dans
le
sous-esp
a 
e H(X ′).
Démonstration.
V
u
la
prop
osition
2.2.26,
le
résultat
s'obtien
t
en
 om
binan
t
les
trois
lemmes
suiv
an
ts.
2
Lemme
2.3.4.

Soient X
une S
- 
ourb
e
simplement
semi-stable
et q : Y →X
un
é
 late-
ment
admissible
tel
que Y
soit
une S
- 
ourb
e
simplement
simplement
semi-stable
;
l'isomor-
phisme q∗
η : C0(|Xη|, R)
∼
−→C0(|Yη|, R)
identie
les
sous-esp
a 
es H(X)
et H(Y).


## Thu actual PDF page 66

52
Démonstration.
L'isomorphisme qη
iden
tie ∂Yη
et ∂Xη
.
D'après
la
prop
osition
2.2.26,
le
p
oly
èdre
en
tier S(X)
s'iden
tie
à
un
domaine
p
oly
édral
dans
le
p
oly
èdre
en
tier S(Y)
tel
que,
p
osan
t S(q) = τX ◦qη|S(Y)
,
le
diagramme
Yη
τY /
qη

S(Y)
S(q)

Xη
τX / S(X)
soit
 omm
utatif,
 
haque
 omp
osan
te
 onnexe
de S(Y) −S(X)
ne
ren on
tre S(X)
qu'en
un
seul
p
oin
t
et
l'appli ation S(q)
soit
la
rétra tion
en
v
o
y
an
t
 
ha une
de
 es
 omp
osan
tes
sur
le
p
oin
t
 orresp
ondan
t
de S(X).
Les
espa es k
-analytiques Yη
et Xη
son
t
iden
tiés
via
l'isomorphisme qη
;
on
déduit
du
diagramme
 omm
utatif
pré éden
t
que,
p
our
toute
fon tion F
sur S(X),
la
fon tion f = F ◦τX
sur Xη = Yη
se
fa torise
par τX
sous
la
forme
:
f = (F ◦S(q)) ◦τY.
L'appli ation
linéaire
S(q)∗: A0(S(X)) →A0(S(Y))
induisan
t
un
isomorphisme
de H(S(X), ∂Xη)
sur H(S(Y), ∂Yη)
(prop
osition
1.2.20),
il
en
résulte
que
l'isomorphisme
 anonique
de C0(|Xη|, R)
sur C0(|Yη|, R)
en
v
oie
le
sous-espa e
H(X)
dans H(Y)
et
induit
un
isomorphisme
de
l'un
sur
l'autre.
2
Lemme
2.3.5.

Soient X
une S
- 
ourb
e
simplement
semi-stable
(quasi- 
omp
a te
)
et K/k
une
extension
non-ar
 himé
dienne
;
une
fon tion h ∈C0(|Xη|, R)
app
artient
au
sous-esp
a 
e
H(X)
si
et
seulement
si
la
fon tion p∗
Kh
app
artient
au
sous-esp
a 
e H(X ×S Spf(K◦)).
Démonstration.
Le
morphisme
 anonique pK : Xη b⊗kK →Xη
induit
un
isomorphisme
G-lo
 al
surje tif S(X)K →S(X)
de
p
oly
èdres
en
tiers
p
ondérés
(prop
osition
2.2.21)
et,
les
 omp
osan
tes
irrédu tibles
anes
de
la eK
- ourb
e Xs ⊗
ek eK
étan
t
les
images
ré ipro
ques
des
 omp
osan
tes
irrédu tibles
anes
de Xs
, ∂(Xη b⊗kK) = p−1
K (∂Xη)) ∩S0(X ×S Spf(K◦)).
Ce i
implique,
p
our
tout
fon tion Φ ∈A0(S(X)),
que
la
fon tion p∗
KΦ
appartien
t
à A0(S(X)K)
et
que
le
supp
ort
de
la
mesure ddcΦ = (pK)∗ddcp∗
KΦ
est
 on
ten
u
dans ∂Xη
si
et
seulemen
t
si
 elui
de
la
mesure ddcp∗
KΦ
est
 on
ten
u
dans ∂(Xη b⊗kK).
2
Lemme
2.3.6.

Soient X
, Y
deux S
- 
ourb
es
simplement
semi-stables
et f : Yη →Xη
un
morphisme
quasi-ni
;
l'homomorphisme f ∗: C0(|Yη|, R) →C0(|Xη|, R)
envoie
le
sous-esp
a 
e
H(Y)
dans H(X).
Démonstration.
Appliquan
t
la
prop
osition
2.2.27
et
les
deux
lemmes
pré éden
ts,
on
p
eut
supp
oser
que f
induit
un
morphisme
de Y
dans X
.
On
a
alors
un
diagramme
 omm
utatif
Xη
τX /
f

S(X)
S(f)

Yη
τY / S(Y),
où S(f) = τY ◦f
est
un
morphisme
de
p
oly
èdres
en
tiers.
Étan
t
donnée
une
fon tion H
dans H(S(Y), ∂Yη),
f ∗(H ◦τY) = S(f)∗H ◦τX


## Thu actual PDF page 67

53
et S(f)∗H ∈A0(S(X)).
Il
reste
à
v
érier
que
la
fon tion S(f)∗H
est
harmonique
sur S(X) −
∂Xη
.
C'est
une
 onséquen e
dire te
du
p
oin
t
(iv)
de
la
prop
osition
2.2.27
: f(x) /∈∂Yη
p
our
tout
p
oin
t x ∈S(X) −∂Xη
et
Z
{x}
ddcS(f)∗H = (degx f)
Z
{f(x)}
ddcH = 0.
2
Si X
est
un
espa e
stri temen
t k
-anoïde
et ϕ : X ˜→Xη
est
un
isomorphisme
de X
sur
la
bre
générique
d'une S
- ourb
e
simplemen
t
semi-stable X
,
le
sous-espa e
v
e toriel
réel ϕ∗H(X)
de C0(|X|, R)
ne
dép
end
pas
du
 
hoix
de X
et
de ϕ
;
il
est
noté H(X).
De
manière
générale,
étan
t
donnés
un
espa e k
-analytique X
et
une
 lôture
algébrique ka
de
k
,
le
group
e
de
Galois G
de
la
fermeture
séparable ksep
de k
dans ka
op
ère
par
automorphismes
sur
l'espa e c
ka
-analytique X b⊗kc
ka
.
On
disp
ose
d'un
morphisme G-équiv
arian
t
 anonique
p : X b⊗kc
ka →X
d'espa es
analytiques
et
l'appli ation
 on
tin
ue
sous-ja en
te
est
un
quotien
t
de |X b⊗kc
ka|
par
l'a tion
de G
dans
la
 atégorie
des
espa es
top
ologiques
:
 'est
en
eet
un
quotien
t
dans
la
 atégorie
des
ensem
bles
d'après
le
 orollaire
1.3.6
de
[3
℄
et
l'appli ation
 on
tin
ue p
est
ouv
erte.
Pr
oposition
2.3.7.

Quel
les
que
soient
la S
- 
ourb
e
simplement
semi-stable X
et
l'ex-
tension
nie
galoisienne k′/k
,
l'a tion
du
gr
oup
e G = Gal(k′/k)
sur C0(|Xη ⊗k k′|, R)
stabilise
le
sous-esp
a 
e H(Xη)
et
l'isomorphisme
 
anonique
C0(|Xη|, R) →C0(|Xη ⊗k k′|, R)G
induit
un
isomorphisme
de H(Xη)
sur H(Xη ⊗k k′)G
.
Démonstration.
On
p
eut
supp
oser Xη
 onnexe.
Si Xη
est
propre, H(Xη)
(resp. H(Xη ⊗k k′))
est
l'espa e
des
fon tions
 onstan
tes
sur Xη
(resp.
lo
 alemen
t
 onstan
tes
sur Xη ⊗k k′
)
(prop
osition
2.3.2,
1)
et
l'assertion
est
éviden
te.
Si Xη
n'est
pas
propre,
alors
il
en
est
de
même
p
our
 
haque
 omp
osan
te
 onnexe
de Xη ⊗k k′
et,
d'après
la
prop
osition
2.3.2,2,
les
restri tions
H(Xη) →Hom(∂Xη, R)
et
H(Xη ⊗k k′) →Hom(∂(Xη ⊗k k′, R)
son
t
bije tiv
es.
L'assertion
résulte
ainsi
de
l'iden
tité ∂Xη = ∂(Xη ⊗k k′)G
.
2
2.3.2.
Le
théorème
de
rédu tion
semi-stable.
C'est
i i
qu'in
tervien
t
le
théorème
de
rédu tion
semi-stable.
Théorème
2.3.8.

Soit X
un
esp
a 
e
stri tement k
-anoïde
pur
ement
de
dimension
1
et
rig-lisse
;
il
existe
une
extension
nie
sép
ar
able k′
de k
tel
le
que
le
domaine k′
-anoïde
X ⊗k k′
soit
isomorphe
à
la
br
e
générique
d'une Spf(k′◦)- 
ourb
e
simplement
semi-stable.
Démonstration.
Il
existe
une
extension
nie
séparable k1
de k
et
une
 ourb
e
algébrique C
propre
et
lisse
sur k1
telles
que X ⊗k k1
soit
isomorphe
à
un
domaine
anoïde
de C
([31℄,
theorem
1).
Appliquan
t
le
théorème
de
rédu tion
semi-stable
sous
la
forme
rigide-analytique
établie
par
S.
Bos 
h
et
W.
Lütk
eb
ohmert
dans
[9℄,
il
existe
une
extension
nie
séparable k′
de k1
telle
que C ⊗k1 k′
soit
isomorphe
à
la
bre
générique
d'une Spf(k′◦)- ourb
e C
don
t
la
bre
sp
é iale
est
simplemen
t
semi-stable
;
 'est
automatiquemen
t
une S
- ourb
e
semi-stable


## Thu actual PDF page 68

54
(remarque
2.2.9,
3).
En
 
hoisissan
t
 on
v
enablemen
t k′
,
on
p
eut
en
outre
supp
oser
que
tout
p
oin
t x
du
b
ord
de X ⊗k k′
satisfait
à
la
 ondition |κ(x)×| = |k′×|.
En
visageons X′ = X ⊗k k′
 omme
un
domaine
stri temen
t k′
-anoïde
de Cη
et
soit q :
C′ →C
un
é latemen
t
admissible
tel
que C′
soit
une Spf(k′◦)- ourb
e
simplemen
t
semi-stable,
a
v
e ∂X′ ⊂S0(C′)
(lemme
2.2.22).
L'image
de X′
par
l'appli ation
de
rédu tion C′
η →Cs
est
un
ouv
ert U
et X′
est
isomorphe
à
la
bre
générique
de
la Spf(k′◦)- ourb
e
simplemen
t
semi-stable X = C′
|U
.
2
Soien
t X
un
espa e
stri temen
t k
-anoïde
puremen
t
de
dimension
1
rig-lisse
et k′
, k′′
deux
extensions
nies
galoisiennes
de k
telles
que X ⊗k k′
et X ⊗k k′′
soien
t
isomorphes
aux
bres
génériques
de
 ourb
es
stri temen
t
semi-stables
;
étan
t
donnée
une
extension
nie
galoisienne
K
de k
 oian
t k′
et k′′
,
la
prop
osition
2.3.7
implique
l'iden
tité
des
espa es H(X ⊗k k′)
et
H(X ⊗k K)Gal(K/k′)
(resp. H(X ⊗k k′′)
et H(X ⊗k K)Gal(K/k′′)
),
d'où
dé oule
l'égalité
H(X ⊗k k′)Gal(k′/k) = H(X ⊗k K)Gal(K/k) = H(X ⊗k k′′)Gal(k′′/k).
Le
théorème
pré éden
t
p
ermet
ainsi
de
dénir,
p
our
tout
espa e
stri temen
t k
-anoïde X
puremen
t
de
dimension
1
et
rig-lisse,
un
sous-espa e
v
e toriel H(X)
de C0(|X|, R)
: H(X) =
H(X ⊗k k′)Gal(k′/k) ⊂C0(|X|, R), k′
étan
t
une
extension
nie
galoisienne
de k
telle
que X ⊗kk′
soit
isomorphe
à
la
bre
générique
d'une Spf(k′◦)- ourb
e
simplemen
t
semi-stable.
Désignan
t
par C
la
 atégorie
don
t
les
ob
jets
son
t
les
espa es
stri temen
t k
-anoïdes,
pure-
men
t
de
dimension
1
et
rig-lisses,
et
les
morphismes
les
immersions
anoïdes,
il
dé oule
de
la
prop
osition
2.3.3
que
l'on
vien
t
ainsi
de
dénir
un
fon teur H
sur Cop
à
v
aleurs
dans VectR
.
Nous
aurons
b
esoin
des
deux
résultats
suiv
an
ts.
Lemme
2.3.9.

Pour
tout
esp
a 
e
stri tement k
-anoïde Y
rig-lisse
et
pur
ement
de
di-
mension
1,
l'appli 
ation
de
r
estri tion
C0(|Y |, R) →Hom(Γ(Y ), R)
induit
un
isomorphisme
du
sous-esp
a 
e H(Y )
sur Hom(Γ(Y ), R).
Démonstration.
Soit k′
une
extension
galoisienne
nie
de k
telle
que
l'espa e
stri temen
t
k′
-anoïde Y ⊗kk′
soit
isomorphe
à
la
bre
générique
d'une Spf(k′◦)- ourb
e
simplemen
t
semi-
stable Y
.
La
pro
je tion
 anonique p : Y ⊗k k′ →Y
induit
une
bije tion
de Γ(Y ⊗k k′)Gal(k′/k)
sur Γ(Y )
et
l'appli ation
de
restri tion
C0(|Y |, R) →Hom(Γ(Y ), R)
 oïn ide
a
v
e 
l'appli ation
induite
par
la
restri tion
C0(|Y ⊗k k′|, R) →Hom(Γ(Y ⊗k k′), R)
en
tre
les
sous-espa es
des
in
v
arian
ts
sous Gal(k′/k)
;
puisque H(Y ) = H(Y ⊗k k′)Gal(k′/k)
,
la
 on lusion
dé oule
de
la
prop
osition
2.3.2.
2
Lemme
2.3.10.

Soient Y
un
esp
a 
e
stri tement k
-anoïde
 
onnexe,
de
dimension
1
et
rig-lisse,
et (hn)
une
suite
 r
oissante
de
fon tions
app
artenant
à H(Y ).
L'alternative
suivante
est
vr
aie
:

soit
la
suite (hn)
 
onver
ge,
uniformément
sur Y
,
vers
une
fon tion h ∈H(Y ),

soit
la
suite (hn)
 
onver
ge,
lo
 
alement
uniformément
sur Y −Γ(Y ),
vers ∞.
Démonstration.
Soien
t k′
une
extension
nie
galoisienne
de k
telle
que Y ′ = Y ⊗k k′
soit
isomorphe
à
la
bre
générique
d'une Spf(k′◦)- ourb
e
simplemen
t
no
dale Y′
et p : Y ′ →Y
la
pro
je tion
 anonique.
Si
l'assertion
est
démon
trée
p
our
la
suite (p∗hn)
dans H(Y ′),
elle
l'est
égalemen
t
p
our
la
suite (hn)
:
en
eet,
puisque H(Y ) = H(Y ′)Gal(k′/k)
,
il
sut
de
s'assurer


## Thu actual PDF page 70

56
Soit X
une
 ourb
e
stri temen
t k
-analytique
lisse
et
désignons
momen
tanémen
t
par HX
le
fais eau
sur |X|
asso
 ié
au
préfais eau HX
;
nous
allons
main
tenan
t
v
érier
l'iden
tité HX =
HX
,
établissan
t
ainsi
que HX
est
un
fais eau.
Pr
oposition
2.3.13.

L
es
se
 tions
du
fais 
e
au HX
satisfont
au
prin ip
e
du
maximum
:
quel
que
soit
l'ouvert Ω
de X
,
une
fon tion h ∈Γ(Ω, HX)
admet
un
extr
emum
lo
 
al
en
un
p
oint x
de Ω
si
et
seulement
si
el
le
est
 
onstante
au
voisinage
de x.
Démonstration.
Il
existe
par
h
yp
othèse
un
v
oisinage
stri temen
t k
-anoïde Y
de x
tel
que
h|Y ∈H(Y ).
Soit k′
une
extension
nie
galoisienne
de k
telle
que Y ⊗k k′
soit
isomorphe
à
la
bre
générique
d'une Spf(k′◦)- ourb
e
simplemen
t
semi-stable Y
; h ⊗1 = H ◦τY
a
v
e 
H ∈H(S(Y), Γ(Yη))
et,
le
morphisme
 anonique
d'espa es
analytiques p : Y ⊗k k′ →Y
étan
t
ouv
ert,
il
sut
de
v
érier
que h ⊗1
est
lo
 alemen
t
 onstan
te
en
un
p
oin
t y
de p−1(x).
Si y /∈S(Y), h ⊗1
est
lo
 alemen
t
 onstan
te
au
v
oisinage
de y
;
sinon, H
a
un
extrem
um
lo
 al
sur S(Y) −Γ(Yη)
en y
,
don 
est
lo
 alemen
t
 onstan
te
en
 e
p
oin
t
en
v
ertu
du
prin ip
e
du
maxim
um
sur
les
p
oly
èdres
en
tiers
(prop
osition
1.2.9)
et
il
en
v
a
de
même
de h ⊗1
par
 on
tin
uité
de τY
.
2
Soit Y
un
domaine
stri temen
t k
-anoïde
dans X
;
vu
la
dénition
du
préfais eau HX
,
on
disp
ose
d'une
appli ation R -linéaire
 anonique
de
restri tion H(Y ) →HX(Y −∂Y )
(induite
par
les
restri tions H(Y ) →H(Y ′), Y ′
par ouran
t
l'ensem
ble
des
domaines
stri temen
t k
-
anoïdes
de Y −∂Y
)
et
don 
d'une
appli ation R -linéaire
 anonique
ρ : H(Y ) →Γ(Y −∂Y, HX) ∩C0(Y, R).
Cor
ollaire
2.3.14.

L'appli 
ation
liné
air
e
 
anonique
ρ : H(Y ) →Γ(Y −∂Y, HX) ∩C0(Y, R)
est
un
isomorphisme.
Démonstration.
Considérons
le
diagramme
 omm
utatif
H(Y )
/
ρ

Hom(Γ(Y ), R)
Γ(Y −∂Y, HX) ∩C0(Y, R)
/ Hom(Γ(Y ), R),
dans
lequel
les
è 
hes
horizon
tales
son
t
les
restri tions
;
la
prop
osition
pré éden
te
implique
l'inje tivité
de
l'appli ation
de
restri tion
Γ(Y −∂Y, HX) ∩C0(Y, R) →Hom(∂Y, R) = Hom(Γ(Y ), R)
et
don 
la
bije tivité
de ρ
puisque
l'appli ation H(Y ) →Hom(Γ(Y ), R)
est
un
isomorphisme
(prop
osition
2.3.2).
2
Cor
ollaire
2.3.15.

Pour
toute
 
ourb
e
stri tement k
-analytique
lisse X
,
l'homomor-
phisme
 
anonique
de
pr
éfais 
e
aux HX →HX
est
un
isomorphisme
; HX
est
don 
un
fais 
e
au.
Démonstration.
Le
sous-préfais eau HX
du
fais eau CX
est
séparé
et
l'homomorphisme
 anonique HX →HX
est
don 
inje tif.
Sa
surje tivité
équiv
aut
à
l'assertion
suiv
an
te
:
p
our
tout
ouv
ert U
de X
et
tout
domaine
stri temen
t k
-anoïde Y
de U
,
la
restri tion
à Y
d'une
fon tion h ∈Γ(U, HX)
appartien
t
au
sous-espa e H(Y )
de C0(|Y |, R)
;
 'est
une
 onséquen e
immédiate
du
 orollaire
pré éden
t.
2
Définition
2.3.16.

L
e
fais 
e
au HX
sur
une
 
ourb
e
stri tement k
-analytique
lisse X
est
app
elé
le
fais 
e
au
des
germes
de
fon tions
harmoniques.


## Thu actual PDF page 71

57
Remarque
2.3.17.

La
dénition
du
fais eau HX
rend
éviden
te
les
assertions
suiv
an
tes
:

le
fais eau HX
sur
l'espa e
top
ologique |X|
est
in
v
arian
t
par
les
automorphismes
k
-analytiques
de X
;
plus
généralemen
t,
si X
et Y
son
t
deux
 ourb
es
stri temen
t
k
-analytiques
lisses
et ϕ : X ˜→Y
est
un k
-isomorphisme,
l'isomorphisme
de
fais eaux
ϕ♯: CY ˜→CX
induit
un
isomorphisme
de HY
sur HX
;

p
our
toute
extension
nie
galoisienne k′
de k
,
l'op
ération
de G = Gal(k′/k)
sur CX⊗kk′
stabilise
la
sous-fais eau HX⊗kk′
et
l'isomorphisme
 anonique CX ˜→CG
X⊗kk′
induit
un
isomorphisme
de HX
sur HG
X⊗kk′
.
Étan
t
donné
un
domaine k
-anoïde Y
d'une
 ourb
e k
-analytique
lisse X
,
nous
noterons
H(Y )
le
sous-espa e
v
e toriel
Γ(Y −∂Y, HX) ∩C0(Y, R)
de C0(|Y |, R)
;
vu
le
 orollaire
2.3.14,
 ette
notation
 oïn ide
a
v
e 
 elle
in
tro
duite
pré édem-
men
t
lorsque Y
est
stri temen
t k
-anoïde.
La
 orresp
ondan e Y 7→H(Y )
est
un
préfais eau
sur
le G-site XG
de X
qui
prolonge
évidemmen
t
le
préfais eau
sur
le
site XR
déni
au
début
de
2.3.3.
Pr
oposition
2.3.18.

Soient X
une
 
ourb
e
stri tement k
-analytique
lisse
et K
une
ex-
tension
non
ar
 himé
dienne
de k
;
notant XK
p
our X b⊗kK
et pK
le
morphisme
 
anonique
XK →X
, p∗
KHX ⊂HX
b⊗kK
.
Démonstration.
C'est
une
 onséquen e
immédiate
de
la
dénition
du
fais eau HX
et
du
lemme
2.3.5.
2
A
 
hev
ons
 e
paragraphe
par
le
résultat
suiv
an
t
:
Pr
oposition
2.3.19.

Soient X, Y
deux
 
ourb
es
stri tement k
-analytiques
lisses
et f :
Y →X
un
morphisme.
Pour
toute
fon tion
harmonique h ∈Γ(X, HX),
la
fon tion f ∗h = h◦f
est
harmonique
sur Y
: f ∗h ∈Γ(Y, HY ).
Démonstration.
On
p
eut
supp
oser Y
 onnexe
et f
quasi-ni.
Étan
t
donnés
des
domaines
stri temen
t k
-anoïdes W ⊂Y
et V ⊂X
tels
que f(W) ⊂V
, h|V ∈H(V )
et
don ,
par
appli-
 ation
des
prop
ositions
2.3.3
et
2.3.7, (f ∗h)|W ∈H(W).
La
fon tion f ∗h
est
don 
harmonique
sur Y
.
2
2.3.4.
Le
préfais eau log |O×
X|.
Considéran
t
toujours
une
 ourb
e
stri temen
t k
-analytique
lisse X
,
examinons
main
te-
nan
t
les
liens
en
tre
les
fon tions
harmoniques
sur X
et
les
fon tions
de
la
forme log |f|,
f ∈Γ(X, O×
X).
Pr
oposition
2.3.20.

Pour
toute
se
 tion f ∈Γ(X, O×
X),
la
fon tion log |f|
est
harmo-
nique
sur X
.
Démonstration.
Il
sut
de
v
érier
que
la
restri tion
de
la
fon tion log |f|
à
tout
domaine
stri temen
t k
-anoïde Y ⊂X
appartien
t
au
sous-espa e H(Y ) ⊂C0(|Y |, R)
;
vu
le
lemme
2.3.5
et
le
théorème
2.3.8,
on
p
eut
en
outre
supp
oser
que Y
est
la
bre
générique
d'une S
-
 ourb
e
simplemen
t
semi-stable,
auquel
 as
il
ne
reste
plus
qu'à
in
v
o
quer
le
p
oin
t
(iii)
de
la
prop
osition
2.2.24.
2
Théorème
2.3.21.

Soit X
une
 
ourb
e
stri tement k
-analytique
lisse.
L
e
fais 
e
au
de R -
ve
 toriels
engendr
é
p
ar
les
germes
de
fon tions log |f|, f
étant
un
germe
de
se
 tion
de O×
X
,
est
un
sous-fais 
e
au
de HX
;
le
quotient
est
un
fais 
e
au
gr
atte- iel
sur |X|
et
il
est
nul
si
l'une
des
deux
 
onditions
suivantes
est
vérié
e
:


## Thu actual PDF page 72

58

le
 
orps ek
est
algébrique
sur
un
 
orps
ni
;

la
 
ourb
e X b⊗kc
ka
est
lo
 
alement
isomorphe
à P1
 
ka
.
Démonstration.
Soit FX
le
sous-fais eau
de CX
asso
 ié
au
préfais eau
sur |X|
faisan
t
 orres-
p
ondre
à
un
ouv
ert U
le
sous-espa e
v
e toriel
de C0(U, R)
engendré
par
les
fon tions log |f|,
f ∈Γ(U, O×
X)
;
 'est
un
sous-fais eau
de HX
en
v
ertu
de
la
prop
osition
pré éden
te.
Les
germes
de FX
et HX
 oïn iden
t
en
tout
p
oin
t x
de X
de
t
yp
e
(1),
(3)
ou
(4)
:

si x
est
de
t
yp
e
(1)
ou
(4),
 e
p
oin
t
admet
un
système
fondamen
tal
de
v
oisinages k
-
anoïdes
a
y
an
t
un
unique
p
oin
t
de
Shilo
v
et
les
se tions
de FX
et HX
son
t
don 
 onstan
tes
au
v
oisinage
de x
;

si x
est
de
t
yp
e
(3),
 e
p
oin
t
admet
un
système
fondamen
tal
de
v
oisinages k
-anoïdes
a
y
an
t
exa temen
t
deux
p
oin
ts
de
Shilo
v
;
les
espa es
v
e toriels FX,x
et HX,x
son
t
alors
de
dimension
2,
engendrés
par
les
germes
de
la
fon tion
 onstan
te 1
et
de
la
fon tion
log |f|, f
étan
t
une
se tion
quel onque
de OX
au
v
oisinage
de x
telle
que |f|
ne
soit
pas
lo
 alemen
t
 onstan
te
en x.
Soien
t
main
tenan
t x ∈X
un
p
oin
t
de
t
yp
e
(2), k′
une
extension
nie
galoisienne
de k
et x′
un
p
oin
t
de X′ = X⊗kk′
au-dessus
de x
:
l'égalité FX′,x′ = HX′,x′
implique
l'égalité FX,x = HX,x
.
En
eet,
si V
est
un
v
oisinage
stri temen
t k
-anoïde
de x
dans X
, V ′
est
la
 omp
osan
te
 onnexe
de x′
dans V ⊗k k′
,
et f ′ ∈A×
V ′
,
la
norme f
de f ′
est
un
élémen
t
de A×
V
tel
que
p∗|f||V ′ = |f ′|[k′:k]
;
si
une
fon tion h ∈H(V )
est
telle
que p∗h|V ′
soit
une
 om
binaison
linéaire
de
fon tions log |f|, f ∈A×
V ′
,
 'est
don 
une
 om
binaison
linéaire
de
fon tions log |f|, f ∈A×
V
.
Cette
remarque
préliminaire
p
ermet
de
supp
oser
que X
est
isomorphe
à
la
bre
générique
d'une S
- ourb
e
simplemen
t
semi-stable X
et
que
le
p
oin
t x
 orresp
ond
à
une
 omp
osan
te
irrédu tible
propre
et
géométriquemen
t
 onnexe Cx
de Xs
.
Lemme
2.3.22.

A
ve
 
les
notations
en
vigueur,
l'esp
a 
e
ve
 toriel HX,x/FX,x
est
 
anoni-
quement
isomorphe
à
l'esp
a 
e
ve
 toriel Pic0(Cx) ⊗Z R .
Démonstration.
Soit V
un
v
oisinage
stri temen
t k
-anoïde
de X
.
Il
existe
une
extension
galoisienne
nie k′
de k
et
un
é latemen
t
admissible q : X ′ →X ⊗S Spf(k′◦)
tel
que V ⊗k k′
soit
isomorphe
à
la
bre
générique
du
s 
héma
formel
induit
par X ′
sur
un
ouv
ert U
de X ′
s
.
La
 omp
osan
te
irrédu tible Cx
de Xs
étan
t
supp
osée
géométriquemen
t
 onnexe,
il
y
a
un
unique
p
oin
t x′ ∈X ⊗k k′
au-dessus
de x,
 orresp
ondan
t
à
la
 omp
osan
te
irrédu tible Cx ⊗
ek ek′
de
X ⊗S Spf(S′)
et,
 elle- i
étan
t
propre
et
lisse,
le
morphisme q
induit
un
isomorphisme
de
la
 omp
osan
te
irrédu tible
de X ′
asso
 iée
à x′
sur Cx ⊗
ek ek′
.
À
toute
fon tion h ∈H(V ) = H(V ⊗k k′)Gal(k′/k)
 orresp
ond
naturellemen
t
un R -diviseur
div(h)
sur
la ek′
- ourb
e Cx⊗
ek ek′
,
vue
 omme
 omp
osan
te
irrédu tible
de X ′
s
:
en
eet,
l'ensem
ble
Tx′S(X ′)
est
 anoniquemen
t
iden
tié
à
l'ensem
ble
des
p
oin
ts
singuliers
de X ′
s
appartenan
t
à
Cx ⊗
ek ek′
et,
notan
t ext
le
p
oin
t
 orresp
ondan
t
à
l'élémen
t t
de Tx′S(X ′),
on
p
ose
:
div(h) =
X
t∈Tx′S(X ′)
λx,t(h)[ext].
La
 ondition
d'harmoni ité
de h
en x′
équiv
aut
à
la
 ondition
deg div(h) = 0.
Le
group
e
de
Galois Gal(k′/k)
op
ère
naturellemen
t
sur
la ek′
- ourb
e Cx ⊗
ek ek′
et
son
a tion
est
transitiv
e
sur
 
haque
bre
du
morphisme
 anonique Cx ⊗
ek ek′ →Cx
;
puisque h
est,
par
h
yp
othèse,
in
v
arian
te
sous Gal(k′/k),
 ela
implique
que
le R -diviseur div(h)
sur Cx ⊗
ek ek′
des end
en
un R -diviseur
de
degré
0
sur
sur Cx
,
en ore
noté div(h).


## Thu actual PDF page 81

67
λb < −2M
sur ∂Ω−U
,
la
fon tion g′
ε = f(ζ)−ε+λb
est
 on
tin
ue
sur Ω,
sous-harmonique
sur
Ω
ma
jorée
par f
sur ∂Ω.
C'est
don 
un
élémen
t
de
la
famille F(f),
 e
qui
implique
l'inégalité
g′
ε ≤Pf
et
f(ζ) −ε = lim inf
x∈Ω,x→ζ g′
ε ≤lim inf
x∈Ω,x→ζ Pf(x).
Le
p
oin
t
(iii)
dé oule
de
la
 onjon tion
des
deux
pré éden
ts.
2
Pr
oposition
3.1.20.

Il
existe
une
b
arrièr
e
en
tout
p
oint
de ∂Ω
de
typ
e
(2),
(3)
ou
(4).
Démonstration.
T
out
p
oin
t x ∈X
admet
un
v
oisinage
ouv
ert U
tel
qu'il
existe
un
mor-
phisme
étale p : U →A1
k
.
Les
p
oin
ts x
et p(x)
étan
t
du
même
t
yp
e,
il
est
susan
t,
en
v
ertu
de
la
prop
osition
3.1.13
et
de
la
remarque
3.1.20,
de
traiter
le
 as X = A1
k
.
Soit x ∈A1
k
un
p
oin
t
de
t
yp
e
(2)
ou
(3)
et
soit Ω⊂A1
k
un
ouv
ert
 onnexe
tel
que x ∈∂Ω
;
en
v
ertu
de
sa
 onnexité, Ω
ne
ren on
tre
qu'une
seule
 omp
osan
te
 onnexe
de A1
k −{x}
et
il
sut
d'établir
l'existen e
d'une
barrière
en x
dans
le
 as
où Ω
est
l'une
des
 omp
osan
tes
 onnexes
de A1
k
,
 e
que
l'on
supp
ose
désormais.
Si
la
 omp
osan
te Ω
est
b
ornée,
 onsidérons
un
p
oin
t x ∈Ω
tel
que
l'extension κ(x)/k
soit
nie,
de
p
olynôme
minimal
unitaire f ∈k[T].
En
v
ertu
des
prop
ositions
3.1.7
et
3.1.12,
la
fon tion log |f| −log |f|(x)
est
sous-harmonique
et
stri temen
t
négativ
e
sur Ω
;
puisqu'elle
est
 on
tin
ue
sur Ω,
il
s'agit
bien
d'une
barrière
p
our
le
p
oin
t x
de ∂Ω.
Si
la
 omp
osan
te Ω
n'est
pas
b
ornée,
la
fon tion log |T|(x) −log |T|
est
(sous-)harmonique
et
stri temen
t
négativ
e
sur Ω
d'après
les
prop
ositions
2.3.20
et
3.1.12
;
étan
t
 on
tin
ue
sur Ω,
 ette
fon tion
est
bien
une
barrière
p
our
le
p
oin
t x
de ∂Ω.
Soien
t x ∈A1
k
un
p
oin
t
de
t
yp
e
(4)
et En
une
suite
dé roissan
te
de
disques
fermés
dans A1
k
d'in
terse tion {x}
;
désignons
par yn
le
p
oin
t
de
Shilo
v
de En
.
A
y
an
t
 
hoisi,
p
our
tout
en
tier
naturel n ,
un
p
oin
t xn ∈En
tel
que
l'extension κ(xn)/k
soit
nie,
de
p
olynôme
minimal
unitaire fn ∈k[T],
 onsidérons
la
fon tion
harmonique
et
stri temen
t
négativ
e
gn =
1
deg(fn)
 log |fn|(yn) −log |fn|

sur A1
k −En
;
la
suite (gn)
est
dé roissan
te
et
son
en
v
elopp
e
inférieure g
est
une
fon tion
sous-
harmonique
ou
iden
tiquemen
t
égale
à −∞
sur A1
k
,
harmonique
sur A1
k −{x}
et
s'ann
ulan
t
au
p
oin
t x.
Soien
t K = H(x), p : A1
K →A1
k
le
morphisme
 anonique
et t ∈A1
K(K)
tel
que
p(t) = x.
Les
fon tions p∗gn
et log |T −t|(yn) −log |T −t|
 oïn idan
t
sur A1
K −p−1(En)
p
our
tout n ,
la
fon tion p∗g
est
 on
tin
ue
et
sous-harmonique
sur A1
K −p−1(x)
;
il
en
est
don 
de
même
de g
.
Nous
v
enons
de
prouv
er
qu'il
existe,
p
our
tout
p
oin
t x ∈A1
k
de
t
yp
e
(2),
(3)
ou
(4),
une
fon tion
semi- on
tin
ue
sup
érieuremen
t b : A1
k →R∪{−∞},
n
ulle
au
p
oin
t x,
sous-harmonique
et
stri temen
t
négativ
e
sur A1
k −{x}
;
 ela
fournit
une
barrière
en x
relativ
emen
t
à
tout
ouv
ert
Ω⊂A1
k
tel
que x ∈∂Ω.
2
Le
lemme
2.3.9
se
généralise
au
 as
d'un
domaine k
-anoïde
quel onque
dans X
.
Cor
ollaire
3.1.21.

Pour
tout
domaine k
-anoïde Y
dans X
,
l'appli 
ation
de
r
estri -
tion
H(Y ) →Hom(Γ(Y ), R)
est
un
isomorphisme.


## Thu actual PDF page 82

68
Démonstration.
Il
sut
d'appliquer
les
deux
prop
ositions
pré éden
tes
à
l'ouv
ert
relativ
e-
men
t
 ompa t Int(Y ) ⊂X
.
2
3.2.
F
on tions
lisses,
op
érateur ddc
Disp
osan
t
du
fais eau HX
des
germes
de
fon tions
harmoniques
sur
une
 ourb
e
stri temen
t
k
-analytique
lisse X
et
de
la
résolution
partielle
du
problème
de
Diri 
hlet
obten
ue
à
la
se tion
pré éden
te,
nous
allons
main
tenan
t
dénir
les
fais eaux A0
X
(resp. A1
X
)
des
germes
de
fon tions
lisses
(resp.
formes
lisses
)
sur X
et
un

op
érateur
de
Lapla e
 ddc : A0
X →A1
X
;
 elui- i
sera
 lassiquemen
t
étendu
à
des
espa es
de
distributions
dans
la
se tion
suiv
an
te.
Désignons
par I(X)
l'ensem
ble
des
p
oin
ts
de X
de
t
yp
e
(2)
ou
(3)
;
de
manière
équiv
alen
te,
I(X)
est
l'ensem
ble
des
p
oin
ts
de
Shilo
v
des
domaines k
-anoïdes
de X
.
Plus
pré isémen
t
:
le
b
ord
de
Shilo
v Γ(Y )
d'un
domaine k
-anoïde Y
de X
est
un
sous-ensem
ble
ni
de I(X)
et
toute
partie
nie S
de I(X)
est
la
réunion
des
b
ords
de
Shilo
v
d'un
nom
bre
ni
de
domaines
k
-anoïdes.
3.2.1.
Les
fais eaux A0
X
et A1
X
sur XG
.
Dans
 e
qui
suit, X
désigne
une
 ourb
e
stri temen
t k
-analytique
lisse.
Définition
3.2.1.

Soit Ω⊂X
un
ouvert.
(i
)
Une
fon tion
r
é
el
le ϕ ∈C0(Ω, R)
est
dite
lisse
s'il
existe
un
r
e
 
ouvr
ement
lo
 
alement
ni V
de Ω
p
ar
des
domaines k
-anoïdes Y
tel
que ϕ|Y ∈H(Y ).
L'ensemble
des
fon tions
lisses
sur Ω
est
un
sous-esp
a 
e
ve
 toriel
de C0(Ω, R),
noté A0(Ω).
(ii
)
On
désigne
p
ar A1(Ω)
l'esp
a 
e
ve
 toriel
des
mesur
es
r
é
el
les
sur Ω
dont
le
supp
ort
est
un
sous-ensemble
lo
 
alement
ni
de I(Ω).
L
es
éléments
de A1(Ω)
ser
ont
app
elés
formes
lisses
(sur Ω).
(iii
)
L
e
sous-esp
a 
e
ve
 toriel
de A0(Ω)
(r
esp. A1(Ω))
 
onstituté
des
fon tions
(r
esp.
me-
sur
es)
dont
le
supp
ort
est
 
omp
a t
se
note A0
c(Ω)
(r
esp. A1
c(Ω)).
La
 orresp
ondan e Ω7→A0(Ω)
est
un
sous-fais eau
du
fais eau C0
X
des
germes
de
fon tions
réelles
 on
tin
ues
sur X
.
La
dénition
du
fais eau A0
X
s'étend
d'elle
même
au G-site XG
de X
:
il
sut,
p
our
tout
ob
jet V
de XG
,
de
dénir A0(V )
 omme
le
sous-espa e
v
e toriel
de C0(V, R)
 onstitué
des
fon tions ϕ
 on
tin
ues
sur V
qui
satisfon
t
à
la
 ondition
suiv
an
te
:
tout
p
oin
t x ∈V
p
ossède
un
v
oisinage k
-anoïde W ⊂V
tel
que ϕ|W ∈H(W).
Désignan
t
par A0
X
le
fais eau
ainsi
déni
sur XG
et
notan
t π : XG →|X|
le
morphisme
de
sites
 anonique,
l'iden
tité
A0
X = π∗A0
X
est
éviden
te.
La
prop
osition
suiv
an
te
l'est
tout
autan
t.
Pr
oposition
3.2.2.

L'homomorphisme
 
anonique
de
pr
éfais 
e
aux HX →A0
X
sur
le
site
XG
identie A0
X
au
fais 
e
au
asso
 ié
à HX
.
Remarque
3.2.3
1.
La
prop
osition
pré éden
te
rép
ond
à
la
question
soulev
ée
par
le
p
oin
t
2
de
la
remarque
2.3.11.


## Thu actual PDF page 83

69
2.
P
our
toute
extension
nie
galoisienne k′/k
,
l'homomorphisme
 anonique
A0
X →(A0X⊗kk′)Gal(k′/k)
est
un
isomorphisme
de
fais eaux
sur XG
.
La
prop
osition
suiv
an
te
n'est
guère
surprenan
te,
 ompte
ten
u
de
la
 onstru tion
du
fais eau
HX
.
Pr
oposition
3.2.4.

Une
fon tion
r
é
el
le ϕ
sur
un
ouvert Ω⊂X
est
lisse
si
et
seulement
s'il
existe,
p
our
tout
domaine
stri tement k
-analytique
 
omp
a t Y ⊂Ω,
une
extension
nie
(sép
ar
able
) k′/k
et
une Spf(k′◦)- 
ourb
e
simplement
semi-stable Y
tel
les
que
:
 Yη = Y ⊗k k′
;

la
fon tion Φ = (ϕ ⊗1)|S(Y)
app
artienne
à
l'esp
a 
e A0(S(Y))
;
 ϕ|Y ⊗kk′ = Φ ◦τY
.
Démonstration.
Soit Y ⊂X
un
domaine
stri temen
t k
-analytique
 ompa t.
Étan
t
données
une
extension
nie
galoisienne k′/k
et
une Spf(k′◦)- ourb
e
simplemen
t
semi-
stable Y
de
bre
générique Y ⊗k k′
,
 onsidérons
une
fon tion Φ ∈A0(S(Y))
et
notons S
la
réunion
du
supp
ort
de
la
mesure ddcΦ
et
du
b
ord
de
Shilo
v Γ(Yη)
de Yη
.
Quelle
que
soit
la
 omp
osan
te
 onnexe c
de S(X) −S
,
la
restri tion
de Φ
au
domaine
p
oly
édral c
appartien
t
à
l'espa e H(c)
et
la
fon tion Φ|c ◦τY = (Φ ◦τY)|τ −1
Y (c)
sur
le
domaine k
-analytique τ −1
Y (c)
de Y ⊗k k′
appartien
t
à H(τ −1
Y (c))
;
en
v
ertu
de
la
prop
osition
pré éden
te,
 ela
implique
Φ ◦τY ∈A0(Y ⊗k k′).
La
 ondition
de
l'énon é
est
don 
susan
te.
Considérons
ré ipro
quemen
t
une
fon tion ϕ ∈A0(Y )
et
un
re ouvremen
t
ni V
de Y
par
des
domaines k
-anoïdes V
tels
que ϕ|V ∈H(V )
;
par
appli ation
du
p
oin
t
(ii)
du
lemme
2.2.22,
il
existe
une
extension
nie
(séparable) k′/k
et
une Spf(k′◦)- ourb
e
simplemen
t
semi-
stable Y
,
de
bre
générique Y ⊗k k′
,
don
t
le
squelette S(Y)
 on
tien
t
l'ensem
ble Γ
des
p
oin
ts
de
Shilo
v
des
domaines k′
-anoïdes V ⊗k k′
, V ∈V
.
Désignons
par Φ
la
restri tion
de ϕ′ = ϕ⊗1
au
squelette S(Y)
de Y
.
Les
bres
de
la
rétra tion τY
son
t
des
domaines k′
-anoïdes
don
t
le
b
ord
de
Shilo
v
est
réduit
à
un
p
oin
t
;
la
fon tion ϕ′
,
étan
t
harmonique
sur Y ⊗k k′ −Γ ,
est
par
suite
 onstan
te
 
haque
bre
de τY
en
v
ertu
du
prin ip
e
du
maxim
um
et
ϕ′ = Φ ◦τY.
Vérions
enn
l'appartenan e
de Φ
à
l'espa e A0(S(Y))
:
quel
que
soit
le
p
olytop
e
en
tier
P ⊂S(Y) −Γ
don
t
le
b
ord
est
formé
de
p
oin
ts
de
t
yp
e
(2), W = τ −1
Y (P)
est
un
domaine
stri temen
t k
-anoïde
dans Y
tel
que ϕ′
|W ∈H(τ −1
Y (P))
( orollaire
2.3.14)
;
on
a
don Φ|P =
(ϕ′
|W )|P ∈H(P)
et
la
fon tion
 on
tin
ue Φ
est
bien
ane
par
mor eaux
sur S(Y).
2
La
prop
osition
3.2.2
p
eut
main
tenan
t
être
pré isée
de
manière
à
donner
une
nouv
elle
dé-
nition
du
fais eau A0
X
sur
le
G-site XG
de X
.
Étan
t
donné
un
domaine k
-analytique V ⊂X
,
 on
v
enons
de
désigner
par R log |OX(V )×|
le
sous-espa e
v
e toriel
réel
de C0(V, R)
engendré
par
les
fon tions
de
la
forme log |f|, f ∈OX(V )×
.
La
 orresp
ondan e
R log |O×
X| : V 7→R log |OX(V )×|
est
un
sous-préfais eau
de A0
X
sur XG
puisque R log |OX(V )×| ⊂H(V )
p
our
tout
domaine
k
-anoïde V ⊂X
.
Pr
oposition
3.2.5.

L'homomorphisme
 
anonique R log |O×
X| →A0
X
identie A0
X
au
fais 
e
au
asso
 ié
au
pr
éfais 
e
au R log |O×
X|.


## Thu actual PDF page 84

70
Démonstration.
Soit FX
le
fais eau
sur XG
asso
 ié
au
préfais eau R log |O×
X|.
Quelle
que
soit
l'extension
galoisienne
nie k′/k
,
la
norme Nk′/k : (pk′)∗(OX ⊗k k′)× →O×
X
induit
un
homomorphisme Nk′/k : (pk′)∗FX⊗kk′ →F
tel
que
f =
1
[k′ : k]Nk′/k(f ⊗1)
p
our
toute
se tion f
de F
, pk′
désignan
t
la
pro
je tion
 anonique
de X⊗kk′
sur X
.
Il
sut
don 
de
prouv
er
qu'une
se tion ϕ
de A0
X
pro
vien
t
de FX
après
passage
à
une
extension
galoisienne
nie
de k
.
Soien
t Y ⊂X
un
domaine k
-analytique
 ompa t
et ϕ
une
fon tion
dans A0
X(Y ).
Il
existe
par
h
yp
othèse
un
re ouvremen
t
ni V
de Y
par
des
domaines k
-anoïdes V
tels
que ϕ|V ∈H(V )
et,
 omme
dans
la
démonstration
pré éden
te,
on
p
eut
trouv
er
une
extension
galoisienne
nie
k′/k
et
une Spf(k′◦)- ourb
e
simplemen
t
semi-stable Y
don
t
la
bre
générique
est
un
v
oisinage
de Y ⊗k k′
dans X ⊗k k′
et
don
t
le
squelette S(Y)
 on
tien
t
l'ensem
ble Γ
de
tous
les
p
oin
ts
de
Shilo
v
des
domaines k
-anoïdes V ⊗k k′
, V ∈V
.
Considérons
alors
une
dé omp
osition
élémen
taire D
de S(Y)
telle
que Γ ⊂D[0]
(on
rapp
elle
que D[0]
est
l'ensem
ble
des 0-fa es
des
p
olytop
es
guran
t
dans D
).
Quel
que
soit
le
p
olytop
e
Q ∈D
, τ −1(Q)
est
un
domaine k
-anoïde
et,
par
 onstru tion,
ϕ|Q ∈H(τ −1(Q)) = R log |OX(τ −1(Q))|.
2
Remarque
3.2.6.

Cette
prop
osition
est
à
rappro
 
her
des
 onsidérations
de
2.3.4.
3.2.2.
Un
résultat
de
densité.
Soit E
un
espa e
top
ologique
lo
 alemen
t
 ompa t.
L'ensem
ble
des
fon tions
réelles
 on
ti-
n
ues
sur E
don
t
le
supp
ort
est
 on
ten
u
dans
un
 ompa t K
de E
est
noté C0(E, R)K
et
la
norme supK |.|
en
fait
un
espa e
de
Bana 
h.
La
restri tion
de E
à K
induit
une
isométrie
de C0(E, R)K
sur
le
sous-espa e
v
e toriel
fermé
de
l'espa e
de
Bana 
h C0(K, R)
formé
des
fon tions
s'ann
ulan
t
sur ∂K = K ∩E −K
.
L'espa e
v
e toriel C0
c(E, R)
des
fon tions
réelles
 on
tin
ues
sur E
don
t
le
supp
ort
est
 ompa t
est
m
uni
de
la
top
ologie
lo
 alemen
t
 on
v
exe
limite
indu tiv
e
des
top
ologies
d'espa es
de
Bana 
h
sur
les C0(E, R)K
;
 'est
la
top
ologie
lo
 alemen
t
 on
v
exe
la
plus
ne
rendan
t
 on
tin
ues
les
inje tions C0(E, R)K →C0
c(E, R).
Lorsque E
est
l'espa e
top
ologique
sous-ja en
t
à
une
 ourb
e
stri temen
t k
-analytique
lisse
X
,
il
est
loisible
de
ne
 onsidérer
que
des
 ompa ts K
qui
son
t
des
domaines
stri temen
t
k
-analytiques
(i.e.
des
réunions
nies
de
domaines
stri temen
t k
-anoïdes)
:
tout
 ompa t
de
X
est
en
eet
 on
ten
u
dans
un
domaine
stri temen
t k
-analytique
 ompa t.
Pr
oposition
3.2.7.

L
e
sous-esp
a 
e A0
c(X)
est
dense
dans C0
c(X, R).
Démonstration.
Soien
t K
un
domaine k
analytique
 ompa t
de X
, ε ∈R>0
et f
une
fon tion
 on
tin
ue
sur X
s'ann
ulan
t
en
dehors
de K
.
De
l'uniforme
 on
tin
uité
de f
sur K
dé oule
l'existen e
d'une
famille
nie V
de
domaines k
-anoïdes
dans X
don
t
la
réunion K′
 on
tien
t K
et
telle
que,
p
our
tout V ∈V
et
tous x, y ∈V
, |f(x) −f(y)| ≤ε/2.
Appliquan
t
le
lemme
suiv
an
t
au
domaine k
-analytique
 ompa t K′
et
au
sous-ensem
ble Σ
réunion
des
p
oin
ts
de
Shilo
v
des V ∈V
et
de
la
fron
tière
de K
,
il
existe
une
fon tion g ∈A0(X)
telle
que
gΣ = fΣ
.
Cette
fon tion
s'ann
ule
sur
la
fron
tière
de K′
et
appartien
t
don 
à A0(X)K
.
Étan
t
donné V ∈V
,
la
fon tion g
satisfait,
par
 onstru tion,
à
l'inégalité
|g(x) −g(y)| ≤ε
2


## Thu actual PDF page 103

89
3.4.
F
on tions
sous-harmoniques
et
mesures
de
Radon
p
ositiv
es
Nous
p
oursuiv
ons
dans
 ette
se tion
l'étude
des
fon tions
sous-harmoniques
sur
une
 ourb
e
stri temen
t k
-analytique
lisse X
,
dénies
en
3.1.2,
à
l'aide
de
l'op
érateur ddc
.
Les
notations
in
tro
duites
dans
l'énon é
de
la
prop
osition
3.3.7
seron
t
libremen
t
emplo
y
ées.
3.4.1.
Le
théorème
d'appro
ximation.
En
v
ertu
de
la
prop
osition
3.4.10,
une
fon tion
sous-harmonique u
sur X
dénit
une
fon tion
réelle
sur I(X)
et
détermine
par
 onséquen
t
un
 ouran
t
dans D0(X).
Lemme
3.4.1.

L'appli 
ation
SH(X) →D0(X),
u 7→u|I(X)
est
inje
 tive
et
son
image
est
l'ensemble
des
 
our
ants T ∈D0(X)
satisfaisant
à
la
 
ondition
suivante
:
p
our
tout
domaine k
-anoïde V ⊂X
et
tout
p
oint x ∈I(V ) −∂V
,
T(x) ≤⟨T, νV
x ⟩.
Démonstration.
Soien
t u
une
fon tion
sous-harmonique
sur X
et x
un
p
oin
t
dans X −I(X).
Étan
t
donnée
une
suite
dé roissan
te (Vn)
de
domaines k
-anoïdes
de X
don
t
le
b
ord
de
Shilo
v Γ(Vn)
est
réduit
à
un
p
oin
t xn
et
telle
que
{x} =
\
n
Vn,
le
prin ip
e
du
maxim
um
(prop
osition
3.1.11)
implique
les
inégalités u|Vn ≤u(xn)
;
la
suite
(u(xn))
est
don 
dé roissan
te
et u(x) ≤infn u(xn).
D'autre
part,
en
v
ertu
de
la
semi- on
tin
uité
sup
érieure
de u,
u(x) ≥limsupnu(xn) = inf
n
u(xn).
La
fon tion u
est
ainsi
uniquemen
t
déterminée
par
sa
restri tion
au
sous-ensem
ble I(X)
de
X
.
La
des ription
de
l'image
de
l'appli ation SH(X) →D0(X)
est
une
appli ation
dire te
du
p
oin
t
(ii)
du
 orollaire
3.3.9.
2
Le
lemme
pré éden
t
nous
p
ermettra
de
ne
pas
distinguer
une
fon tion
sous-harmonique
sur
X
du
 ouran
t
de
degré 0
qu'elle
détermine.
Une
fon tion
sous-harmonique
sur
une
surfa e
de
Riemann
est,
lo
 alemen
t,
l'en
v
elopp
e
in-
férieure
d'une
famille
dé roissan
te
de
fon tions
sous-harmoniques
lisses
([19℄,
Theorem
2.5.5).
Cette
assertion
est
égalemen
t
vraie
dans
un
 on
texte
non
ar 
himédien,
la
démonstration
en
étan
t
qui
plus
est
élémen
taire.
Théorème
3.4.2.

Soient Ω
un
ouvert
d'une
 
ourb
e
stri tement k
-analytique
lisse X
et
u ∈SH(Ω).
Pour
tout
ouvert
r
elativement
 
omp
a t Ω′ ⊂Ω,
la
r
estri tion
de u
à Ω′
est
l'envelopp
e
inférieur
e
d'une
famil
le
dé
 r
oissante
de
fon tions
sous-harmoniques
lisses.
Démonstration.
On
p
eut
supp
oser
que
l'ouv
ert
relativ
emen
t
 ompa t Ω′ ⊂Ω
est
de
la
forme
Y −∂Y
, Y ⊂X
étan
t
un
domaine k
-analytique
 ompa t.
Étan
t
donné
un
sous-ensem
ble
ni S ⊂I(Y )
 on
tenan
t ∂Y
,
dé oule
des
prop
ositions
3.1.19
et
3.1.20
l'existen e
d'une
unique
fon tion uS
appartenan
t
à A0(Y ),
harmonique
sur Y −S
et
 oïn idan
t
a
v
e u
sur S
.


## Thu actual PDF page 104

90
La
sous-harmoni ité
de u
sur Y −S
implique
l'inégalité u|Y ≤uS
;
par
suite,
p
our
tout
sous-ensem
ble
ni S′
de I(Y )
 on
tenan
t S
, uS
ma
jore uS′
sur
le
b
ord S′
de Y −S′
et uS′ ≤
uS
,
en
v
ertu
du
prin ip
e
du
maxim
um
(prop
osition
3.1.1)
appliqué
aux
fon tions uS
et uS′
,
harmoniques
sur Y −S′
.
La
famille (uS)S
est
don 
dé roissan
te.
La
fon tion
lisse uS
est
sous-harmonique
sur Y −∂Y
.
Soien
t
en
eet V ⊂Y −∂Y
un
domaine
k
-anoïde
et h
une
fon tion
dans H(V )
qui
ma
jore uS
sur ∂V
.
Puisque u|Y ≤uS
, h
ma
jore
a
fortiori u
sur ∂V
,
et
don 
sur
tout V
par
sous-harmoni ité
;
 omme u
et uS
 oïn iden
t
sur
S
,
il
s'ensuit
que h
ma
jore u
sur
le
b
ord S′′ = (S ∩V ) ∪∂V
de
l'ouv
ert V −S′′
.
Une
nouv
elle
appli ation
du
prin ip
e
du
maxim
um
aux
fon tions
harmoniques h|V −S′′
et (uS)|V −S′′
fournit
alors
l'inégalité
uS ≤h
sur V
.
La
famille (uS)S
 S
par ouran
t
l'ensem
ble
ltran
t
des
parties
nies
de I(Y )
 on
tenan
t
∂Y

est
minorée
en
tout
p
oin
t
de I(X)
;
son
en
v
elopp
e
inférieure u
est
don 
une
fon tion
sous-harmonique
sur X
(prop
osition
3.1.8).
La
démonstration
s'a 
hèv
e
en
in
v
o
quan
t
le
lemme
3.4.1
:
les
fon tions
sous-harmoniques u
et u|Y −∂Y
,
trivialemen
t
égales
sur I(Y ) −∂Y
,
son
t
iden
tiques.
2
Remarque
3.4.3.

La
démonstration
 i-dessus
s'adapte
aisémen
t
dans
un
 on
texte
ar 
hi-
médien
et
p
ermet
de
démon
trer
un
résultat
d'appro
ximation
glob
al
p
our
les
fon tions
sous-
harmoniques
sur
une
surfa e
de
Riemann
(v
oir
la
prop
osition
4.2.14).
La
 ara térisation
des
fon tions
sous-harmoniques
lisses
est
sans
surprise.
Pr
oposition
3.4.4.

Une
fon tion
lisse ϕ ∈A0(X)
sur
une
 
ourb
e
stri tement k
-
analytique
lisse X
est
sous-harmonique
si
et
seulement
si ddcϕ ≥0.
Démonstration.
Soit ϕ
une
fon tion
dans A0(X)
telle
que ddcϕ ≥0.
Soien
t V ⊂X
un
domaine k
-anoïde
et h
une
fon tion
dans H(V )
qui
ma
jore ϕ
sur ∂V
;
il
est
susan
t,
p
our
prouv
er
l'inégalité
ϕ|V ≤h,
d'établir
que ϕ|V
est
ma
jorée
par
la
fon tion h′
dans H(V )
qui
 oïn ide
a
v
e ϕ
sur ∂V
( ar
h′ ≤h
d'après
le
prin ip
e
du
maxim
um).
L'inégalité ddc(h′ −ϕ) = −ddcϕ ≤0
sur V −∂V
implique
que
la
fon tion h′ −ϕ
n'a
pas
de
minim
um
lo
 al
stri t
sur V −∂V
( orollaire
3.2.11,
(ii))
;
elle
attein
t
don 
son
minim
um
en
un
p
oin
t
de ∂V
et,
puisque (h′ −ϕ)|∂V = 0,
ϕ|V ≤h′.
La
fon tion ϕ
est
ainsi
sous-harmonique
sur X
.
Soit
ré ipro
quemen
t ϕ ∈A0(X)
une
fon tion
lisse
et
sous-harmonique.
Étan
t
donné
un
p
oin
t x
du
supp
ort S
de ddcϕ,
 onsidérons
un
domaine k
-anoïde V ⊂X
tel
que S ∩(V −
∂V ) = {x}
et
soit h
la
fon tion h ∈H(V )
qui
est
égale
à ϕ
sur
S.
La
fon tion ϕ|V −h
est
négativ
e
et
elle
s'ann
ule
iden
tiquemen
t
sur ∂V
.
La
forme
lisse (ddc(ϕ−h))|V −∂V = (ddcϕ)|V −∂V
est,
par
h
yp
othèse,
non
n
ulle
et
p
ortée
par
{x}.
La
première
 ondition
implique
l'existen e
d'un
minim
um
lo
 al
stri t
p
our
la
fon tion
(ϕ −h)|V −∂V
et
 elui- i
est
né essairemen
t
réalisé
en
un
p
oin
t y ∈I(Y ) −∂Y
 ar ϕ −h
est
lo
 alemen
t
 onstan
te
en
tout
p
oin
t
de Y −I(Y ).
On
en
déduit
l'inégalité
Z
{y}
ddcϕ > 0


## Thu actual PDF page 105

91
par
appli ation
du
p
oin
t
(ii)
du
 orollaire
3.2.11
et
don y = x, (ddcϕ)|V −∂V ≥0.
Ce i
établit
la
p
ositivité
de
la
forme
lisse ddcϕ.
2
Cor
ollaire
3.4.5.

Soient X
une
 
ourb
e
stri tement k
-analytique
lisse, K/k
une
ex-
tension
non
ar
 himé
dienne
et pK : X b⊗kK →X
la
pr
oje
 tion
 
anonique
;
étant
donné
e
une
fon tion
sous-harmonique u
sur X
,
la
fon tion p∗
Ku
est
sous-harmonique
sur X b⊗kK
.
Démonstration.
Puisqu'il
est
loisible
de
raisonner
lo
 alemen
t,
nous
p
ouv
ons,
en
v
ertu
du
théorème
3.4.2,
supp
oser
que u
est
l'en
v
elopp
e
inférieure
d'une
famille (ϕλ)
de
fon tions
sous-
harmoniques
lisses.
La
fon tion pK∗u
est
alors
l'en
v
elopp
e
inférieure
de
la
famille
de
fon tions
lisses p∗
Kϕλ
et
il
sut
don 
de
traiter
le
 as
d'une
fon tion
sous-harmonique
lisse.
Soit u
une
fon tion
sous-harmonique
lisse
et
v
érions
que
la
mesure ddcp∗
Ku
est
p
ositiv
e.
La
form
ule
ddcp∗
Ku = pK′/K∗ddcp∗
K′u
p
our
toute
extension
non
ar 
himédienne K′/K
(théorème
3.2.10)
p
ermet
d'agrandir K
à
loisir.
Considérons
un
domaine
stri temen
t k
-anoïde Y ⊂X
et
une
extension
nie k′/k
telle
que
Y ⊗k k′
soit
isomorphe
à
la
bre
générique
d'une Spf(k′◦)- ourb
e
simplemen
t
semi-stable Y
et
que
la
fon tion p∗
k′u
s'é riv
e
sous
la
forme U ◦τ
,
a
v
e U ∈A0(S(Y))
(prop
osition
3.2.4)
;
la
sous-harmoni ité
de u
implique
 elle
de U
puisque ddcU = ddcu
(théorème
3.2.10).
Soien
t
main
tenan
t K′
une
extension
non
ar 
himédienne
de k
 oian
t K
et k′
et p : S(Y)K′ →S(Y)
l'appli ation
induite
par
la
pro
je tion
 anonique
de X b⊗kK′
sur X ⊗k k′
.
La
fon tion p∗U
est
sous-harmonique
sur S(Y)K
et
il
en
est
par
 onséquen
t
de
même
p
our p∗
K′u = p∗U ◦τK′
.
Comme
men
tionné
au
début
de
la
démonstration,
la
sous-harmoni ité
de p∗
K′u
implique
 elle
de p∗
Ku.
2
2
L'utilisation
sim
ultanée
du
théorème
d'appro
ximation
et
de
la
 ara térisation
des
fon tions
sous-harmoniques
lisses
p
ermet
égalemen
t
de
rép
ondre
à
une
question
naturelle
men
tionnée
à
la
remarque
3.1.7.
Pr
oposition
3.4.6.

Soient X
une S
- 
ourb
e
simplement
semi-stable
et u
une
fon tion
sous-harmonique
sur Xη
;

la
r
estri tion U
de u
au
squelette S(X)
de X
est
une
fon tion
r
é
el
le
sous-harmonique
(=
 
onvexe
)
 
ontinue
;
 u ≤U ◦τX
.
Démonstration.
L'inégalité u ≤U ◦τX
est
une
 onséquen e
immédiate
du
prin ip
e
du
maxim
um
puisque
les
bres
de
la
rétra tion τX
son
t
des
domaines k
-anoïdes
don
t
le
b
ord
est
réduit
à
un
p
oin
t.
La
restri tion U
de u
au
squelette S(X)
est
à
v
aleurs
nies
 ar S(X) ⊂I(Xη)
et,
 ompte
ten
u
du
théorème
3.4.2, U
est
l'en
v
elopp
e
inférieure
d'une
famille
dé roissan
te
de
fon tions
qui
son
t
les
restri tions
de
fon tions
lisses
et
sous-harmoniques
sur Xη
.
Il
est
par
 onséquen
t
susan
t
de
prouv
er
qu'une
fon tion
lisse
et
sous-harmonique ϕ
sur Xη
se
restrein
t
en
une
fon tion
ane
par
mor eaux
et
sous-harmonique
sur
le
p
oly
èdre S(X).
Nous
p
ouv
ons
supp
oser
la
 ourb
e
quasi- ompa te
puisque
la
question
est
lo
 ale
sur S(X)
;
l'assertion
sera
d'autre
part
démon
trée
si
elle
l'est
après
passage
à
une
extension
nie k′
de k
.
Appliquan
t
la
prop
osition
3.2.4
et
le
lemme
2.2.22,
il
existe
dans
 es
 onditions
un
é latemen
t
admissible q : Y →X
tel
que
:
 Y
soit
une S
- ourb
e
simplemen
t
semi-stable,
 ϕ = Φ ◦τY
,
a
v
e Φ = ϕ|S(Y) ∈A0(S(Y)).
La
fon tion Φ
est
sous-harmonique
puisque ddcΦ = ddcϕ ≥0
(théorème
3.2.10).


## Thu actual PDF page 106

92
D'après
la
prop
osition
2.2.26, S(X)
est
un
domaine
p
oly
édral
dans S(Y)
tel
que
 
haque
 omp
osan
te
 onnexe
de S(Y)−S(X)
n'ait
qu'un
seul
p
oin
t
fron
tière.
Il
en
dé oule
tout
d'ab
ord
que
la
restri tion Φ′
de ϕ
à S(X)
est
une
fon tion
 on
tin
ue
et
ane
par
mor eaux
puisque
Φ′ = Φ|S(X)
.
C'est
en
outre
une
fon tion
sous-harmonique
: Φ
est
en
eet
dé roissan
te
au
v
oisinage
de
la
fron
tière
de S(Y) −S(X)
en
v
ertu
du
prin ip
e
du
maxim
um,
 e
qui
implique
ddcΦ′ ≥ddcΦ ≥0.
2
Remarque
3.4.7.

Ré ipro
quemen
t,
étan
t
donnée
une S
- ourb
e
simplemen
t
semi-stable
X
et
une
fon tion
sous-harmonique F
sur S(X),
la
fon tion τ ∗
X F
est
évidemmen
t
sous-
harmonique
sur X
:
représen
tan
t F
 omme
l'en
v
elopp
e
inférieure
d'une
suite
dé roissan
te
(Φn)
de
fon tions
anes
par
mor eaux
et
sous-harmoniques
sur S(X), τ ∗F
est
l'en
v
elopp
e
inférieure
de
la
suite
des
fon tions
lisses
et
sous-harmoniques τ ∗
X Φn
(v
oir
[32℄
p
our
l'utilisation
de
fon tions
sur X
dénies
via
des
des
(diéren es
de)
fon tions
 on
v
exes
sur
les
p
oly
èdres
S(X)).
3.4.2.
P
arties
p
olaires.
Un
sous-ensem
ble E
d'une
 ourb
e
stri temen
t k
-analytique
lisse X
est
dit
p
olair
e
s'il
admet
un
re ouvremen
t
dénombr
able
par
des
ouv
erts
 onnexes Ω⊂X
sur
lesquels
existe
une
fon tion
u ∈SH(Ω)
telle
que E ∩Ω⊂{u = −∞}.
Remarque
3.4.8
1.
La
 ondition
de
dénom
brabilité
in
tro
duite
dans
 ette
dénition
est
né essaire
à
l'exis-
ten e,
p
our
toute
partie
p
olaire E ⊂X
,
d'une
fon tion
sous-harmonique
globale
sur X
prenan
t
la
v
aleur −∞
en
tout
p
oin
t
de E
,
ainsi
qu'à
une
 ara térisation
 
ap
a itair
e
des
parties
p
olaires
(théorème
3.6.11
et
remarque
3.6.12).
2.
La
 ondition
de
dénom
brabilité,
join
te
à
la
semi- on
tin
uité
sup
érieure
des
fon tions
sous-
harmoniques,
implique
immédiatemen
t
que
tout
sous-ensem
ble
p
olaire
de X
est
 on
ten
u
dans
un
b
or
élien
p
olaire.
Nous
noterons P(X)
l'ensem
ble
des
p
oin
ts x ∈X
tels
que
le
singleton {x}
soit
p
olaire
;
il
est
 lair
que
les
parties
p
olaires
de X
son
t
des
sous-ensem
bles
de P(X).
Remarque
3.4.9.

Les
deux
propriétés
suiv
an
tes
se
déduisen
t
immédiatemen
t
de
la
pro-
p
osition
3.1.14
:
1.
Quel
que
soit
le
morphisme
quasi-ni f : Y →X
, f −1(P(X)) ⊂P(Y ).
2.
P
our
toute
extension
non
ar 
himédienne K/k
, p−1
K (P(X)) ⊂P(X b⊗kK).
Pr
oposition
3.4.10.

Pour
toute
 
ourb
e
stri tement k
-analytique
lisse X
, P(X)
est
exa tement
l'ensemble
des
p
oints
de X
de
typ
e
(1).
Démonstration.
Rapp
elons
qu'un
p
oin
t x
d'une
 ourb
e
stri temen
t k
-analytique
est
de
t
yp
e
(1)
si
l'extension
non
ar 
himédienne H(x)/k
se
plonge
dans
la
 omplétion
d'une
 lôture
algébrique
de k
.
(2.1.3)
T
out
p
oin
t x
de
t
yp
e
(1)
dans A1
k
est
p
olaire
:
étan
t
donnés
une
suite
dé roissan
te (En)
de
disques
fermés
dans A1
k
de
limite {x}
et,
p
our
tout n ,
un
p
oin
t xn ∈En
tel
que
l'extension
κ(xn)/k
soit
nie,
de
p
olynôme
minimal
unitaire fn ∈k[T],
les
fon tions
gn =
1
deg(fn) log |fn|


## GR-classical actual PDF page 6

6
W. GUBLER AND J. RABINOFF
2.7. Grothendieck topology and fibers. For a k-analytic space X, we will also consider
the G-topology generated by the analytic domains of X, as described in [Ber93, §1.3]. We
denote this space by XG to emphasize the use of this Grothendieck topology. For strictly
k-analytic spaces, we often use the G-topology generated by the strictly analytic domains
instead: see [Ber93, §1.6]. In either case, the space XG has a well-behaved sheaf of rings
OXG. If V = M(A ) is an affinoid domain of X, then we have OXG(V) = A . For x ∈X,
we denote by H (x) the completed residue field of the local ring OXG,x with respect to
the valuation on OXG,x/mx induced by the norm corresponding to x. If V is any analytic
domain in X and if x ∈V, then H (x) is the same whether we consider x as belonging
to V (which is itself a k-analytic space), or to X. We call x ∈X a rig-point if H (x) is a
finite extension of k.
If ϕ: Y →X is a morphism, then the fiber ϕ−1(x) over x ∈X is an H (x)-analytic
space, and the underlying topological space has the induced topology [Ber93, §1.4].
2.8. Fiber products. The category of k-analytic spaces admits fiber products by [Ber93,
§1.4]. For analytic spaces X, Y over a k-analytic space S, we denote the fiber product by
X ×S Y . Given x ∈X and y ∈Y over the same point s ∈S, there always exists z ∈X ×S Y
mapping to x and to y with respect to the canonical projections [Duc18, 1.2.13]. For
convenience, we repeat the argument. The completed tensor product H (x)b⊗H (s)H (y)
contains H (x) ⊗H (s) H (y) by a result of Gruson [Gru66, §3.2 Théorème 1(4)], so
H (x)b⊗H (s)H (y) ̸= 0. The Berkovich spectrum of any nonzero Banach ring is nonempty
[Ber90, Theorem 1.2.1], and any z′ ∈M
 H (x)b⊗H (s)H (y)

induces a point z ∈X ×S Y
mapping to x and y. Note that H (z) is a simultaneous analytic extension field of H (x)
and of H (y).
Since Gruson’s result holds for Banach algebras over a non-Archimedean field, the
same argument shows that for two analytic field extensions of k, there is a joint analytic
extension of both.
2.9. Extension of scalars. Let k′/k be an an analytic extension field. Then there is a
base extension functor (·)k′ which associates to a k-analytic space X a k′-analytic space
Xk′, given on a k-affinoid space X = M(A ) by the k′-affinoid space Xk′ = M(A b⊗kk′)
[Ber90, §1.4]. We denote by πk′/k : Xk′ →X the structure map, which is closed and
surjective by [GRW17, Lemma 2.19], [Duc24, (3.1.1.2)].
2.10. The Shilov section. For r = (r1,..., rn) ∈Rn
>0, we consider the k-affinoid do-
main in the closed polydisc M
 k〈r−1
1 T1,..., r−1
n Tn〉

given by the equations |Tj(x)| = rj,
j = 1,..., n. The corresponding k-affinoid algebra is denoted by kr; it consists of the
Laurent series f =
P
λ∈Zn aλT λ such that aλrλ →0 for |λ| →∞. The k-affinoid al-
gebra M(kr) has a unique Shilov boundary point equal to the weighted Gauss point
ηr ∈M
 k〈r−1
1 T1,..., r−1
n Tn〉

given by the weighted Gauss norm ∥∥r from 2.3.
If
r1,..., rn induce linearly independent elements in the Q-vector space R>0/
p
|k×|, then kr
is a non-Archimedean field; it follows that kr = H (ηr). For every k-affinoid algebra A ,
there is always such an r such that A b⊗kr is a strictly kr-affinoid algebra. See [Ber90,
pp. 21–22].


## GR-classical actual PDF page 7

CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES
7
For any k-analytic space X and r ∈Rn
>0, the structure map πkr/k : Xkr →X has a canon-
ical section σ: X →X r mapping x ∈X to the unique Shilov boundary point of the fiber
π−1
kr/k(x) = M(H (x)b⊗kr) = M(H (x)r) (which is the weighted Gauss point ηr). We
call σ the Shilov section. The Shilov section is continuous: see [Ber90, Lemma 3.2.2(i)],
[Duc18, 1.2.16].
2.11. Relative boundary. An important notion in this paper is that of the relative bound-
ary of a morphism ϕ: X →Y of k-analytic spaces. This is a closed subset of X which we
denote by ∂(X/Y ). We will not give the details of this definition, but let us try to explain
the literature on the subject. In [Ber90, §2.5], Berkovich defines the relative boundary
∂(X/Y ) for k-affinoid spaces X and Y . Then in [Ber90, §3.1], he generalizes ∂(X/Y ) for
good k-analytic spaces using that all points of X and Y have k-affinoid neighborhoods.
Berkovich calls ϕ closed if ∂(X/Y ) = ;. Berkovich defines ∂(X/Y ) for arbitrary k-analytic
spaces in [Ber93, 1.5.3(ii)], as follows. A morphism ϕ is closed if for every morphism
Y ′ →Y from a good k-analytic space Y ′, the fiber product X ′ := X ×Y Y ′ is good and the
canonical morphism X ′ →Y ′ is closed in the previous sense. Finally in [Ber93, Defini-
tion 1.5.4], a point x ∈X is defined to be in Int(X/Y ) if x has an open neighborhood U
such that ϕ induces a closed morphism U →Y in the above sense. We refer to [Tem15,
Definition 4.2.4.1] for a more explicit equivalent definition of ∂(X/Y ). Note that in this
paper, we will use the notion closed map in the usual topological sense meaning that it
maps closed sets to closed sets. This is different from Berkovich’s terminology.
The complement Int(X/Y ) := X \∂(X/Y ) is called the relative interior. We will usually
apply this in the case Y = M(k), in which case we call ∂X := ∂(X/M(k)) the boundary
of X and Int(X) := X \ ∂X the interior. If ∂X = ;, we say that X boundaryless. A bound-
aryless space is good by definition. Note that Berkovich calls boundaryless k-analytic
spaces closed.
We list here some properties of the boundary and interior which we will use throughout
the paper:
(1) A point x ∈X is contained in Int(X/Y ) if and only if there is an open neighbor-
hood U of x such that Int(U/Y ) = U: this is part of the above definition.
(2) If ϕ: X →Y is finite, then Int(X/Y ) = X [Ber93, Example 1.5.3(iii)].
(3) If X is an analytic domain in Y , then Int(X/Y ) is the topological interior of X in
Y [Ber93, Proposition 1.5.5(i)].
(4) If X
ϕ→Y
ψ→S are morphisms of k-analytic spaces, then
(2.11.1)
Int(X/Y ) ∩ϕ−1 Int(Y /S) ⊂Int(X/S)
[Ber93, Proposition 1.5.5(ii)], with equality if ψ is locally separated [Tem04,
Corollary 5.7]. Taking S = M(k), this becomes
(2.11.2)
Int(X/Y ) ∩ϕ−1 Int(Y ) ⊂Int(X).
(5) If k′/k is an analytic extension field, then
π−1
k′/k Int(X/Y ) ⊂Int(Xk′/Yk′)


## GR-classical actual PDF page 10

10
W. GUBLER AND J. RABINOFF
Then the graded residue field of A is given by
eA• :=
M
r∈R>0
A≤r/A<r.
We refer to [Tem04] for properties of this functorial construction.
3. SUBHARMONIC FUNCTIONS ON ANALYTIC CURVES
In this section, we generalize Thuillier’s theory [Thu05] of subharmonic functions from
smooth strictly analytic curves to arbitrary k-analytic curves.
3.1 (k-Analytic Curves). By a k-analytic curve we mean a separated k-analytic space of
pure dimension 1. We gather the following facts about k-analytic curves:
(1) A k-analytic curve is good, i.e., every point has an affinoid neighborhood. [Duc24,
Proposition 3.3.7]
(2) A k-analytic curve is paracompact. [Duc24, Théorème 4.5.10]
(3) If X is an affinoid k-analytic curve, then ∂X coincides with the Shilov boundary
of X. [Thu05, 2.1.2]
An analytic domain in a k-analytic curve (for example, an open subset) is again a k-
analytic curve.
3.2 (Thuillier’s Harmonic Functions). Thuillier [Thu05, §2.3] defines a sheaf of harmonic
functions on a smooth, strictly k-analytic curve for a non-trivially valued k, roughly as
follows. If X is affinoid, then a continuous function h: X →R is harmonic if, after passing
to a finite, separable field extension, it coincides with the composition of a harmonic
function on a skeleton of X (in the sense of graph theory) with the retraction to the
skeleton. If X is smooth, then a harmonic function on an open subset of X is defined to be
a continuous function whose restriction to every strictly affinoid subdomain is harmonic.
3.3 (Thuillier’s Subharmonic Functions). For a non-trivally valued k, Thuillier [Thu05,
Définition 3.1.5] defines a subharmonic function on a smooth, strictly k-analytic curve X
to be an upper semicontinuous function u: X →R ∪{−∞} that is not identically −∞
on any connected component of X and that satisfies the following property: for every
strictly k-affinoid domain U ⊂X and every harmonic function h: U →R, if u ≤h on ∂U
then u ≤h on U.
Now we extend this definition to the case of non-smooth curves. The idea is that a
function should be subharmonic if it pulls back to a subharmonic function along any
morphism from a smooth curve. However, an inseparable curve over an imperfect field
does not admit any non-constant morphisms from a smooth curve, so one has to allow
an extension of scalars as well. We also consider the constant function −∞to be sub-
harmonic, following Demailly [Dem85] in the complex case.
Definition 3.4 (Subharmonic functions). Let X be a k-analytic curve and let u: X →
R ∪{−∞} be an upper semicontinuous function. We say that u is subharmonic provided
that, for every non-trivially valued analytic extension field k′/k, every smooth, connected,
strictly k′-analytic curve Y , and every morphism Y →Xk′, the composition
Y −→Xk′
πk′/k
−→X
u
−→R ∪{−∞}


## GR-classical actual PDF page 11

CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES
11
is either subharmonic on Y in the sense of [Thu05, Définition 3.1.5], or is identically −∞.
3.4.1. If X is a smooth, connected, strictly k-analytic curve over a non-trivially valued k,
then an upper semicontinuous function u: X →R ∪{−∞} is subharmonic in our sense
if and only if it is either subharmonic in Thuillier’s sense or is identically −∞. Indeed, if
u is subharmonic in our sense then one can take k = k′ and Y = X to see that it is either
subharmonic in Thuillier’s sense or is identically −∞. Conversely, if u is identically −∞
then it is clearly subharmonic in our sense, and if u is subharmonic in Thuillier’s sense
then it is subharmonic in our sense by [Thu05, Proposition 3.1.14 and Corollaire 3.4.5].
3.4.2. As a special case of (3.4.1), if X is a smooth, connected, strictly k-analytic curve
over a non-trivially valued k, then a function u: X →R (taking finite values) is subhar-
monic in our sense if and only if it is subharmonic in Thuillier’s sense.
Here we collect the basic properties of subharmonic functions, which we will prove
over the course of this section.
Proposition 3.5. Let X be a k-analytic curve and let u: X →R ∪{−∞} be an upper
semicontinuous function.
(1) (Sheafiness) The subharmonic functions form a sheaf on X.
(2) (Analytic functions) If f ∈Γ(X,OX) then log|f | : X →R∪{−∞} is subharmonic.
(3) (Boundaries) If u is subharmonic on Int(X), then u is subharmonic on X.
(4) (Cone Property) If u1,u2: X →R∪{−∞} are subharmonic and λ1,λ2 ∈R≥0 then
λ1u1 + λ2u2 and max{u1,u2} are subharmonic.
(5) (Limits) The infimum of a decreasing net of subharmonic functions is subharmonic.
(6) (Maximum Principle) If u is subharmonic and u attains a local maximum at x ∈
Int(X), then u is constant in a neighborhood of x.
(7) (Extension of scalars) Let k′/k be an analytic extension field. Then u is subharmonic
if and only if u ◦πk′/k : Xk′ →R ∪{∞} is subharmonic.
(8) (Functoriality) Let Y be a k-analytic curve and let f : Y →X be a morphism. If u
is subharmonic then u ◦f is subharmonic, and the converse holds if f is finite and
surjective.
(9) (Finite Values) If u is subharmonic and u(x) = −∞for a non-rig-point x ∈X,
then u ≡−∞on the irreducible component of Int(X) ∪{x} containing x.
Let us make some remarks regarding the content of Proposition 3.5.
3.5.1. If U ⊂X is an open subset then U is again a k-analytic curve, so it makes sense
to speak of subharmonic functions on U. It is immediate from the definition that a sub-
harmonic function on X restricts to a subharmonic function on U. Hence subharmonic
functions form a presheaf on X. Proposition 3.5(1) asserts that this presheaf is a sheaf.
3.5.2. The maximum principle (Proposition 3.5(6)) is [Thu05, Proposition 3.4.10] in the
smooth, strictly analytic case.
3.5.3. In the situation of Proposition 3.5(7), it is immediate from Definition 3.4 that
u ◦πk′/k is subharmonic when u is subharmonic. This is the difficult direction in the
smooth, strictly analytic case: see [Thu05, Corollaire 3.4.5]. This result is hidden in the


## GR-classical actual PDF page 12

12
W. GUBLER AND J. RABINOFF
fact that Definition 3.4 essentially recovers Thuillier’s definition of subharmonicity in that
case 3.4.1.
3.5.4. In the situation of Proposition 3.5(8), it is immediate from Definition 3.4 that u◦f
is subharmonic when u is subharmonic. The remark in 3.5.3 applies to a lesser extent in
this case: see [Thu05, Proposition 3.1.14].
3.5.5. For any x ∈X, the subset Int(X)∪{x} is open in X. This is obvious if x ∈Int(X), and
if x ∈∂X then it follows from the fact that ∂X is discrete in X. In particular, Int(X)∪{x}
is again a k-analytic curve, so it makes sense to speak of its irreducible components
in Proposition 3.5(9). Irreducible components can only meet at rig-points (their inter-
sections are Zariski-closed), so a non-rig-point x is contained in a unique irreducible
component of Int(X) ∪{x}; this is implicit in Proposition 3.5(9).
3.5.6. Proposition 3.5(9) implies that if u is subharmonic and u(x) = −∞for a non-rig-
point x ∈X, then u ≡−∞in a neighborhood of x.
3.6. In order to extend Thuillier’s results, we will pass from a k-analytic curve to a
smooth, strictly k-analytic curve in four steps:
(1) Extend scalars to a field as in 2.10 to make the curve strictly analytic.
(2) If char(k) = p, then extend scalars to the completion of the perfect closure kp−∞.
(3) Replace the analytic curve by the underlying reduced curve.
(4) Pass to the interior of the normalization, which is smooth (see 2.13).
We begin with some lemmas about this process.
Lemma 3.7. Suppose that char(k) = p > 0. Let k′ be the completion of kp−∞. Then k′ is
perfect, and if X is a k-analytic space then πk′/k : Xk′ →X is a homeomorphism such that
π(∂Xk′) = ∂X.
Proof. We leave it as an exercise for the reader to verify that k′ is perfect. The fact that
πk′/k is a homeomorphism is [Duc09, Remarque 0.5], and the assertion about boundaries
is Lemma 2.12.
□
We make the following observation to mirror Lemma 3.7. Its proof is immediate.
Lemma 3.8. Let X be a strictly k-analytic space and let ι: Xred ,→X be the inclusion of the
underlying reduced space. Then ι is a homeomorphism of underlying topological spaces, and
ι(∂Xred) = ∂X.
We refer the reader to [Ber90, before Proposition 3.1.8] for the construction of the
normalization.
Lemma 3.9. Let X be a reduced, strictly k-analytic curve and let ν: eX →X be its normal-
ization. Then the following hold:
(1) eX is rig-smooth if k is perfect.
(2) ν is an isomorphism outside of a discrete set of rig-points of X.
(3) ν induces a bijection ∂eX
∼
−→∂X.
(4) ν is a topological quotient.


## GR-classical actual PDF page 20

20
W. GUBLER AND J. RABINOFF
of subharmonicity, we have h ≤h′ on U. By the same argument as applied to −h, we see
that h = h′ on U, so that h is harmonic on U. As U was arbitrary, h is harmonic.
By 3.12, the following definition recovers Thuillier’s definition of harmonicity on a
smooth, strictly k-analytic curve, and even on a strictly affinoid rig-smooth curve us-
ing [Thu05, Corollaire 2.3.14].
Definition 3.13 (Harmonic functions). Let X be a k-analytic curve for a possibly trivially
valued non-Archimedean field k. A function h: X →R is harmonic if h and −h are both
subharmonic.
The advantage of this definition is that the following basic properties of harmonic func-
tions follow immediately from the corresponding properties of subharmonic functions.
Proposition 3.14. Let X be a k-analytic curve and let h: X →R be a continuous function.
(1) (Sheafiness) The harmonic functions form a sheaf on X.
(2) If f ∈Γ(X,O ×
X ) then log|f | is harmonic.
(3) The harmonic functions on X form a real vector space.
(4) (Limits) If h is locally a uniform limit of harmonic functions, then it is harmonic.
(5) (Maximum Principle) If h is harmonic and h attains a local extremum at x ∈Int(X),
then h is constant in a neighborhood of x.
(6) (Extension of Scalars) Let k′/k be an analytic extension field. Then h is harmonic
if and only if h ◦πk′/k : Xk′ →R is harmonic.
(7) (Functoriality) Let Y be a k-analytic curve and let f : Y →X be a morphism. If h is
harmonic then h◦f is harmonic, and the converse holds if f is finite and surjective.
(8) (Boundaries) If h is harmonic on Int(X), then it is harmonic on X.
We will later see in Theorem 7.6 that (4) holds even for pointwise limits. The fol-
lowing proposition asserts that Definition 3.13 is equivalent to the notion of harmonicity
in [GJR21, Definition 7.2]. We assume that k is non-trivially valued as in ibid.
Proposition 3.15. Let X be a strictly k-analytic curve and let h: X →R be a continuous
function. The function h is harmonic if and only if it is R-PL and the line bundle Lh(x) ∈
Pic(red(X, x))R defined in (2.17) is numerically trivial for every point x ∈X.
Proof. This is [GJR21, Proposition 15.7] in the rig-smooth case; we reduce to this case
in the usual way. If char(k) = p > 0 let k′ be the completion of kp−∞, and otherwise let
k′ = k. Let X ′ = X b⊗kk′ and let π: X ′ →X be the structure morphism. Let ι: X ′
red ,→X ′
be the underlying reduced space and let ν: eX ′ →X ′
red be the normalization, so that eX ′ is
rig-smooth. Let f : eX ′ →X denote the composition π ◦ι ◦ν.
Suppose that h is harmonic. Then h ◦f is harmonic by Proposition 3.14(6,7), so h ◦f
is R-PL and Lh(x′) is numerically trivial for all x′ ∈eX ′ by the rig-smooth case. Then
h is R-PL by Lemma 3.9(6) and [GJR21, Lemma 5.3(3), Corollary 5.11], and Lh(x) is
numerically trivial for all x ∈X by [GJR21, Proposition 7.6(1′,2′)]. Conversely, suppose
that h is R-PL and that Lh(x) is numerically trivial for all x ∈X. The same holds for
h◦f by [GJR21, Proposition 7.6(1′,2′)], so h◦f is harmonic by the rig-smooth case, and
hence h is harmonic by Proposition 3.14(6,7).
□


## GR-classical actual PDF page 21

CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES
21
Remark 3.16. We still assume that X is a strictly k-analytic curve over a non-trivially
valued field k and that h: X →R is continuous. Proposition 3.15 and Proposition 3.14(6)
imply in particular that if h◦πk′/k is harmonic for some analytic extension field k′/k, then
h◦πk′′/k is R-PL for any analytic extension k′′/k, which is by no means obvious. Likewise,
Proposition 3.14(7) implies that if f : Y →X is finite and surjective and h◦f is harmonic,
then h is R-PL, and Proposition 3.14(8) implies that if h|Int(X) is harmonic then h is R-PL.
4. CLASSICALLY PLURISUBHARMONIC FUNCTIONS
In this section we define the notion of a classically plurisubharmonic function. The
definition follows Definition 3.4.
Definition 4.1 (Classically Plurisubharmonic Functions). Let X be a k-analytic space and
let u: X →R ∪{−∞} be an upper semicontinuous function. We say that u is classically
plurisubharmonic or classically psh provided that, for every analytic extension field k′/k,
every k′-analytic curve Y , and every morphism f : Y →Xk′, the function u◦πk′/k◦f : Y →
R ∪{−∞} is subharmonic on Y in the sense of Definition 3.4.
4.1.1. Any class of psh functions should respect extension of scalars and should be stable
under pullback, so the conditions in Definition 4.1 are necessary. In complex analysis,
this condition (without the extension of scalars) is the definition of plurisubharmonicity,
which is why we call the notion “classically psh”.
4.1.2. If X is a k-analytic curve, then a function u: X →R∪{−∞} is classically psh if and
only if it is subharmonic. Indeed, if u is classically psh then taking k′ = k and Y = X in
Definition 4.1 shows that u is subharmonic, and if u is subharmonic then it is classically
psh by Proposition 3.5(7,8).
4.1.3. In Definition 4.1, one can assume that Y is a connected, smooth, strictly k′-analytic
curve: this follows from Definition 3.4.
Classically psh functions satisfy the basic properties of subharmonic functions on curves.
Proposition 4.2. Let X be a k-analytic space.
(1) (Sheafiness) The classically psh functions form a sheaf on X.
(2) If f ∈Γ(X,OX) then log|f |: X →R ∪{−∞} is classically psh.
(3) (Cone Property) If u1,u2: X →R∪{−∞} are classically psh and λ1,λ2 ∈R≥0 then
λ1u1 + λ2u2 and max{u1,u2} are classically psh.
(4) (Limits) The infimum of a decreasing net of classically psh functions is classically
psh. For arbitrary pointwise limits, we refer to Theorem 6.5.
(5) (Extension of Scalars) Let k′/k be an analytic extension field. A function u: X →
R ∪{−∞} is classically psh if and only if u ◦πk′/k : Xk′ →R ∪{−∞} is classically
psh.
(6) (Functoriality) Let Y be a k-analytic space and let f : Y →X be a morphism. If
u: X →R ∪{−∞} is classically psh then u ◦f is classically psh, and the converse
holds if f is finite and surjective.
Proof. Properties (1,3,4) follow immediately from Proposition 3.5(1,4,5). For Proposi-
tion 4.2(2), we consider an analytic function f on X. As |f | is continuous, we deduce


## GR-classical actual PDF page 22

22
W. GUBLER AND J. RABINOFF
that log|f | is a continuous function with values in R∪{−∞} and hence it is upper semi-
continuous. Then Proposition 4.2(2) follows from Proposition 3.5(2).
To prove Proposition 4.2(5), it is clear from the definitions that if u is classically psh,
then u ◦πk′/k is classically psh for every analytic extension field k′/k. To prove the con-
verse, we assume that k′/k is an analytic extension field and that u′ := u ◦πk′/k is a
classically psh function on Xk′. Since the morphism πk′/k is closed and surjective 2.9,
it is clear that u is upper semicontinuous. Let k′′/k be an analytic extension field and
let f : Y →Xk′′ be a morphism over k′′ from a k′′-analytic curve Y . We have to show
that u ◦πk′′/k ◦f is subharmonic. As in the proof of Proposition 3.5(7), we consider
a simultaneous analytic extension field K of k′ and k′′. It follows from the above that
u ◦πK/k = u′ ◦πK/k′ is classically psh and hence u ◦πK/k ◦fK is subharmonic. We con-
clude from the commutative diagram (3.10.1) that u ◦πK/k ◦fK = u ◦πk′′/k ◦f ◦πK/k′′ is
subharmonic and hence u ◦πk′′/k ◦f is subharmonic by Proposition 3.5(7).
Likewise, the proof of Proposition 4.2(6) follows the same lines as the proof of Propo-
sition 3.5(8). Again, it follows from the definitions if u is a classically psh function on X,
then u ◦f is a classically psh function on Y . Conversely, we assume that u ◦f is a clas-
sically psh function for a finite surjective morphism f : Y →X. Since finite morphisms
are proper and hence closed, we deduce from upper semicontinuity of u ◦f and from
surjectivity of f that u is upper semicontinuous. It remains to show that u ◦πk′/k ◦g is
subharmonic for any analytic extension field k′/k and any morphism g : Z →Xk′ from a
connected k′-analytic curve Z. Setting W := Z ×Xk′ Yk′, we get a morphism g′: W →Yk′
from f by base change with respect to f ′: Yk′ →Xk′ as in (3.10.2). Since u ◦f is classi-
cally psh, it follows from Proposition 4.2(5) that u ◦πk′/k ◦f ′ = u ◦f ◦πk′/k is classically
psh. The morphism f is finite and surjective, hence the same holds for f ′. We con-
clude that the base change f ′′: W →Z of the morphism f ′ is finite and surjective. The
k′-analytic space W has irreducible components of dimension 1 and maybe isolated irre-
ducible components of dimension 0. Removing the latter, we obtain a k′-analytic curve
W ′ as an open and closed subset of W. Since Z is a connected k′-analytic curve and f ′′
is a finite surjective map from W onto Z, we get an induced finite surjective morphism
W ′ →Z. Indeed, as W ′ is also Zariski-closed in W, we deduce from finiteness of f ′′ that
f ′′(W ′) is a Zariski-closed subset in Z of dimension 1 and hence f ′′(W ′) = Z as Z is a
connected k′-analytic curve. Since the inclusion W ′ →W is obviously finite, the com-
position W ′ →Z is also finite. In the following, we replace W by W ′, which preserves
the commutativity of the diagram (3.10.2) and has the advantage that W is a k′-analytic
curve. It follows that u ◦πk′/k ◦f ′ ◦g′ = u ◦πk′/k ◦g ◦f ′′ is subharmonic on W. The
morphism of k′-analytic curves f ′′: W →Z is finite and surjective, so we deduce from
Proposition 3.5(8) that u ◦πk′/k ◦g is subharmonic.
□
In the paper [GR25], we have studied semipositive R-PL functions on a good strictly
k-analytic space over a non-trivially valued non-archimedean field k. This turns out to
be the same as an R-PL function that is classically psh, as we now show.
Theorem 4.3. Suppose that the valuation on k is nontrivial. Let X be a good, strictly k-
analytic space and let h: X →R be an R-PL function. Then h is semipositive if and only if h
is classically psh.


## GR-classical actual PDF page 23

CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES
23
Proof. For x ∈X, an R-PL function h: X →R induces a residue line bundle Lh(x) ∈
Pic(red(X, x))R on the reduction red(X, x) of the germ (X, x): see 2.17. Recall from
[GJR21, Definition 7.2] that h is semipositive at x ∈X if and only if the associated residue
line bundle Lh(x) is nef. We have shown in [GR25, Proposition 3.1] that for a smooth
strictly k-analytic curve, an R-PL function is semipositive if and only if it is subharmonic.
Since semipositivity is stable under base extension and pull-back [GJR21, Proposition
7.6], we conclude that a semipositive R-PL function on X is classically psh.
The converse follows from [GR25, Corollary 3.5], which shows that an R-PL function h
on X is semipositive if and only if there is an algebraically closed analytic extension field
F of k such that for every smooth F-analytic curve C and every morphism ϕ: C →X F,
we have h ◦ϕ semipositive.
□
5. CONNECTIVITY BY CURVES
We will prove a maximum principle for classically psh functions by reducing to the
case of curves. For this we will need to prove that it is possible to connect a point of an
analytic space to its neighbors using analytic curves, potentially defined over large field
extensions.
Definition 5.1. Let X be a k-analytic space. An analytic curve in X is a subset Γ ⊂X
satisfying the following property: there is an analytic extension field k′/k, a compact,
separated k′-analytic space C of dimension at most 1, and a morphism ϕ: C →Xk′, such
that Γ = πk′/k ◦ϕ(C).
An analytic curve Γ in X is overconvergent if there exist (k′, C,ϕ) as above such that ϕ
factors as
(5.1.1)
C
Int(C′)
C′
Xk′
←
→
ψ
←
→
ϕ
←-
→
←
→
ϕ′
where C′ is a separated k′-analytic space of dimension at most 1, and ϕ′ and ψ are
morphisms.
5.1.2. The compactness hypothesis in Definition 5.1 is crucial. When X is Hausdorff, it
implies that if Γ,Γ ′ are analytic curves in X such that Γ ∪Γ ′ is connected, then Γ ∩Γ ′ ̸= ;
(the compact sets Γ,Γ ′ are closed, so they cannot be disjoint by connectedness). However,
a non-proper compact curve has a nonempty boundary, which causes problems when
trying to reduce the maximum principle to the case of curves. This is the reason for
introducing overconvergent curves in X.
5.1.3. One can always pass to a larger analytic extension field k′′/k′ in Definition 5.1.
Indeed, we have a commutative diagram
Ck′′
Xk′′
C
Xk′
X.
←
→
ϕk′′
←
↠
←
→
πk′′/k
←
→
πk′′/k′
←
→
ϕ
←
→
πk′/k


## GR-classical actual PDF page 30

30
W. GUBLER AND J. RABINOFF
after recentering, we can assume that ϕ(V) ⊂Bn
+. For x′ ∈V let y′ = ϕ(x′) ∈Bn
+ and
let Σx′ be the connected component of ϕ−1([y′,0]) containing x′. Since [y′,0] ⊂Bn
+ we
have ϕ−1([y′,0]) ⊂Int(Y ), and since Σx′ is connected and x′ ∈V we have Σx′ ⊂V. As
before, there exists an open neighborhood U of x in V such that Σx′ ∩Σx ̸= ; for all
x′ ∈U.
By Lemma 5.9, for any y′ ∈Bn
+ there is a connected, overconvergent analytic curve
Γy′ in Bn
+ containing [y′,0]. For x′ ∈V mapping to y′, we let Γx′ be the connected
component of ϕ−1(Γy′) containing x′, so that Γx′ ⊂V for the same reason that Σx′ ⊂V.
By Lemma 5.2(1,4), this Γx′ is again a connected, overconvergent analytic curve in X.
Clearly Σx′ ⊂Γx′, so for x′ ∈U we have Γx′ ∩Γx ̸= ;. This completes the proof as in the
previous case.
□
6. THE MAXIMUM PRINCIPLES FOR CLASSICALLY PSH FUNCTIONS
In this section, we consider a non-Archimedean field k. We will prove first that the
local maximum principle holds for classically psh functions, and then we will show a
global maximum principle in the affinoid case; more specifically, that that a classically
psh function takes its global maximum at a Shilov point.
Theorem 6.1 (Local Maximum Principle). Let X be a k-analytic space and let u be a clas-
sically psh function on X. If u has a local maximum at x ∈Int(X), then u is locally constant
at x.
Proof. We may replace X by a connected, Hausdorff open neighborhood of x in Int(X) to
assume that X is connected and boundaryless and that u attains a global maximum at x.
Let R = u(x). Let Γ be a connected, overconvergent analytic curve in X containing x. We
claim that u ≡R on Γ. Consider the set Γu=R = {z ∈Γ | u(z) = R}. This set is closed in Γ
by upper semicontinuity of u, so since Γ is connected, it suffices to show that Γu=R is open
in Γ.
By 5.1.3, there exist an analytic extension field k′/k, a compact, separated strictly k′-
analytic space C of dimension at most 1, a separated strictly k′-analytic space C′ of dimen-
sion at most 1, and morphisms ψ: C →C′ and ϕ′: C′ →Xk′, such that ψ(C) ⊂Int(C′)
and πk′/k ◦ϕ(C) = Γ, where ϕ = ϕ′ ◦ψ. The composition u ◦πk′/k ◦ϕ′ is subharmonic
on 1-dimensional connected components of C′ because u is classically psh.
Let y ∈Γu=R, let z ∈C be a point lying over y, and let z′ = ψ(z) ∈Int(C′), so that
R = u◦πk′/k ◦ϕ′(z′) = u◦πk′/k ◦ϕ(z). If {z′} is a connected component of C′ then clearly
u ◦πk′/k ◦ϕ′ ≡R in a neighborhood of z′. Otherwise, the connected component of z′
in C′ is a strictly k′-analytic curve, in which case u ◦πk′/k ◦ϕ′ ≡R in a neighborhood
of z′ by Proposition 3.5(6) (here we use z′ ∈Int(C′)). Taking the ψ-inverse image of
such a neighborhood, we see that u ◦πk′/k ◦ϕ ≡R in a neighborhood of z. Applying
this argument to each z ∈(πk′/k ◦ϕ)−1(y), we construct an open set V ⊂C containing
(πk′/k ◦ϕ)−1(y) such that u ◦πk′/k ◦ϕ|V ≡R.
The complement C \ V is a closed subset of the compact space C, so it is a compact
subset of C that is disjoint from (πk′/k ◦ϕ)−1(y). Its image is a compact subset of X that
does not meet y, so there is an open neighborhood W of y such that (πk′/k◦ϕ)−1(W) ⊂V.


## GR-classical actual PDF page 31

CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES
31
It follows that u ≡R on W ∩Γ. This proves that Γu=R is open in Γ. As remarked above,
this yields u ≡R on Γ.
Let y ∈X be any point. By Theorem 5.4, there is a connected, overconvergent analytic
curve Γ in X containing x and y. We showed above that u ≡R on Γ, so that u(y) = R.
As y was arbitrary, we have u ≡R on X.
□
The global maximum principle for classically psh functions involves the Shilov bound-
ary. For this, we need the following two lemmas. The first is well-known, but we were
unable to find a reference.
Lemma 6.2. Let X be a k-affinoid space of pure dimension d ≥1. Then the Shilov boundary
of X is contained in the relative boundary ∂X of X over k. In particular, ∂X ̸= ;.
Proof. Let k′/k be an analytic field extension such that Xk′ is strictly affinoid. Note that
the base change morphism πk′/k maps ∂Xk′ to ∂X 2.11(5′) and maps the Shilov boundary
onto the Shilov boundary [GRW17, Proposition 2.21], so we may assume that X is strictly
affinoid and k′ non-trivially valued. Choose a formal affine k◦-model X of X. The interior
X \ ∂X consists of the points x ∈X such that the closure of redX(x) in Xs is proper over
the residue field ek by [CD12, Lemme 6.5.1]. Since X is affine, the special fiber Xs is
affine, so x ∈∂X if and only if redX(x) is not a closed point of Xs. Since d ≥1, the
special fiber Xs is of pure dimension d ≥1, and hence the generic points of Xs are not
closed. By [GM19, Proposition A.3], the divisorial points of X (i.e. the points of X which
reduce to the generic points of Xs) are precisely the Shilov points of X. We conclude that
all Shilov points are in the boundary of X.
□
Let X = M(A ) be an affinoid space over k of pure dimension d. By a result of Ducros
[Duc12, Lemme 3.1], the boundary ∂X of X can be expressed as a union of affinoid spaces
of lower dimension, defined over certain extension fields of k. We use his argument to
give a stratification of ∂X. Choose non-nilpotent elements g1,..., gr ∈A such that the
graded reductions eg•
1,..., eg•
r generate the graded ek•-algebra f
A •. Let ri be the spectral
radius of gi. Then for any I ⊂{1,..., r}, we get a morphism
pI : X −→B(I),
x 7→(gi(x))i∈I
to the closed poly-disc B(I) =
Q
i∈I B(0, ri) of dimension s = |I|. Let η(I) be the weighted
Gauss point of B(I) and let kI := H (η(I)), which is the completion of the field of rational
functions k((ti)i∈I) in the variables (ti)i∈I with respect to the weighted Gauss valuation
for the weight (ri)i∈I.
Lemma 6.3. With the above notations, set X I := p−1
I (η(I)). By convention, we set X; = X.
Then:
(1) X I is a kI-affinoid space of pure dimension d −s if non-empty.
(2) ∂X I =
S
i∈{1,...,r}\I X I∪{i}.
(3) X I = {x ∈X | (eg•
i (x))i∈I are algebraically independent in f
H •(x) over ek•}.
(4) If X has pure dimension d, then the Shilov boundary of X is equal to
S
|I|=d X I.


## GR-PL actual PDF page 1

arXiv:2503.05513v1  [math.AG]  7 Mar 2025
ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN
ANALYTIC GEOMETRY
WALTER GUBLER AND JOSEPH RABINOFF
ABSTRACT. In this paper, we generalize results on Zhang’s semipositive model metrics
from the algebraic setting to strictly analytic spaces over a non-trivially valued non-
Archimedean ﬁeld. We prove stability under pointwise limits and under forming the
maximum. We also prove the maximum principle. As tools, we use a local lifting theo-
rem from the special ﬁber to the generic ﬁber of a model and an afﬁnoid Bieri–Groves
theorem.
1. INTRODUCTION
In Diophantine Geometry, an important tool is the height of a proper variety X with
respect to a given metrized line bundle L. This height is deﬁned as an arithmetic self
intersection number introduced by Gillet and Soulé [GS90] in higher dimensions. Zhang
[Zha95] realized that the contribution of a non-Archimedean place v to this arithmetic
intersection product is given by a v-adic metric associated to a model (X ,L ) of (X, L)
over the valuation ring of v. Such a model metric is called semipositive if the model L
is a nef line bundle on the proper variety X . More generally, Zhang introduced semi-
positive continuous metrics as uniform limits of semipositive model metrics. He showed
that the canonical metrics of polarized dynamical systems are semipositive continuous
metrics. This point of view turned out to be very important in the proof of the Bogomolov
conjecture by Ullmo [Ull98] and Zhang [Zha98]. As pointed out in [Gub98], the model
metrics can be studied over any non-trivially valued non-Archimedean ﬁeld working with
Berkovich spaces and their formal models leading to a theory of local heights for proper
varieties.
Let k be a ﬁeld that is complete with respect to a nontrivial, non-Archimedean abso-
lute value. The theory of subharmonic functions on a smooth, strictly analytic k-curve
X has been worked out by Thuillier in his thesis [Thu05]. In higher dimensions, we still
lack a completely satisfactory theory of plurisubharmonic functions on Berkovich spaces.
As work of Boucksom and Jonsson [BJ22] in the algebraic setting suggests, such a the-
ory might be build upon regularization by semipositive piecewise linear functions. This
means that plurisubharmonic functions should be given as decreasing limits of semipos-
itive piecewise linear functions. The latter are the local analogues of semipositive model
metrics. The crucial role of semipositive piecewise linear functions is then supported by
Zhang’s global approach to semipositive continuous metrics.
2020 Mathematics Subject Classiﬁcation. Primary 14G40; Secondary 31C05, 32P05, 32U05.
Key words and phrases. Berkovich spaces, tropicalization, plurisubharmonic functions.
W. Gubler was supported by the collaborative research center SFB 1085 Higher Invariants - Interactions
between Arithmetic Geometry and Global Analysis funded by the Deutsche Forschungsgemeinschaft.
1


## GR-PL actual PDF page 15

ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY
15
5. SEMIPOSITIVE R-PL FUNCTIONS
Let k be a non-trivially valued non-Archimedean ﬁeld. We consider a good, strictly
k-analytic space X. We refer to 2.5 for the deﬁnition of PL functions. Recall from the in-
troduction that an R-PL function u: X →R is called semipositive at x ∈X if the associated
residue line bundle Lu(x) ∈Pic(red(X, x))R is nef, where we refer to [GJR21, 6.16–6.19]
for residue line bundles. Equivalently, there is a strictly afﬁnoid neighbourhood U of x
such that u = hL for a formal k◦-model (U,L) of (U,OU) with L nef [GJR21, Proposition
7.1].
We will show ﬁrst that for an R-PL function on a smooth curve, semipositivity is the
same as subharmonicity in the sense of Thuillier’s thesis [Thu05, Déﬁnition 3.1.5]. Re-
call that Thuillier deﬁnes a subharmonic function on a smooth k-analytic curve X as a
semicontinuous function u: X →R ∪{−∞} which is not identically −∞on any con-
nected component of X and which has the property that for every harmonic function h
on a strictly afﬁnoid domain U of X with u|∂U ≤h|∂U, we have u|U ≤h.
Proposition 5.1. Let X be a smooth, strictly k-analytic curve and let u: X →R be an R-PL
function. Then u is subharmonic at x ∈X in the sense of Thuillier if and only if Lu(x) is nef.
Proof. First we treat the case when k is algebraically closed. As explained in 2.5, there
exists a compact strictly analytic neighborhood U of x in X, a formal k◦-model U of U,
and a formal model L of OU such that u|U = hL. Since k is algebraically closed, we may
assume that the special ﬁber Us is reduced, which implies that U is covered by formal
afﬁnes of the form Spf(A ◦) for a strictly k-afﬁnoid algebra A [GJR21, §2.4]. It follows
from [Ber90, Proposition 2.4.4] that for every irreducible component Y of Us, there is a
unique point ξY ∈U reducing to the generic point of Y . In the formalism of real valued
forms and currents on Berkovich spaces [CD12], it is well known that d′d′′[u]|U is the
discrete measure on U supported on the points ξY of U for Y an irreducible component
of Us, with multiplicity at ξY equal to degL(Y). See [CD12, §6.9] for a more general
statement. Wanner showed that subharmonicity of u on U is equivalent to the positivity
of the current d′d′′[u]: see [Wan19, Theorems 1 and 2] and use the fact that X is locally
algebraic [vdP80]. Thus Ls is nef if and only if u is subharmonic on U. Suppose that u is
subharmonic at x. Shrinking U, we may assume that u is subharmonic on U. This implies
that Ls is nef, so it follows from [GJR21, Proposition 7.1] that Lu(x) is nef. Conversely, if
Lu(x) is nef, then by [GJR21, Proposition 7.1], we may shrink U so that Ls is nef, which
as above implies that u is subharmonic on U.
It remains to show that subharmonicity of u at x and numerical effectivity of Lu(x)
can be checked after extending scalars to the completion of an algebraic closure K =
(k)∧. By [GJR21, Proposition 7.6(2)], one can check that Lh(x) is nef after base change
to K. The same is true for subharmonicity: this follows directly from Thuillier’s deﬁnition
and the fact that the base change of a harmonic function remains harmonic [Thu05,
Proposition 2.3.18].
□
Our next goal is a characterisation of semipositive R-PL functions by restriction to
subcurves as in the complex case. We need the following characterization of boundary
points:


## GR-PL actual PDF page 16

16
W. GUBLER AND J. RABINOFF
5.2. Let X be an admissible formal k◦-scheme and let x ∈Xη. Then x ∈Int(X) = X \∂X
if and only if the closure of redX(x) is a proper ek-scheme. This follows from [CD12,
Lemme 6.5.1] in the separated case and from [Vil21, Corollary A.4] in general.
Theorem 5.3. Let X be a good, strictly k-analytic space, and let h: X →R be an R-PL
function. For x ∈X, the following conditions are equivalent.
(1) The function h is semipositive at x.
(2) There is a neighborhood W of x such for every strictly analytic neighborhood U ⊂W
of x and every Zariski-closed curve C in U, the restriction h|C is semipositive.
Proof. Since semipositivity is an open property that is stable under pullback [GJR21,
Proposition 7.6], it is clear that (1) yields (2).
Assume that h satisﬁes (2). By shrinking W, we may assume that W is a strictly afﬁnoid
neighborhood of x and that there is a formal model W of U and a model L of OW on W
with coefﬁcients in R such that h = hL on W. Let Y ⊂Ws be a curve which is proper over
the residue ﬁeld ek. To prove semipositivity at x, it is enough to show that degL(Y ) ≥0.
Choose any point y ∈W reducing to the generic point η of Y . By Theorem 4.1 as
applied to X = W and X = W, there exist z ∈W with redW(z) = η, a neighborhood U
of z in W, and an irreducible 1-dimensional Zariski-closed subspace C of U containing
z. By shrinking U, we may assume that U is strictly afﬁnoid. By results of Bosch and
Lütkebohmert [Bos14, Theorem 8.4.3] [BL93b, Corollary 5.4(b)], there is a formal model
U of U and a morphism π: U →W extending the inclusion U ,→W on generic ﬁbers. Let
C be the formal closure of C in U. This is an admissible formal model of C whose special
ﬁber Cs is a closed 1-dimensional subscheme of Us containing η′ = redU(z). Functoriality
of reductions shows that π(η′) = η, so the closure Y ′ of η′ is a curve mapping to Y .
Since the closure of η in Ws is the proper curve Y , we conclude from 5.2 that z ∈W \
∂W. The boundary ∂U is the union of ∂W ∩U with the topological boundary of U in
W [Ber90, Proposition 3.1.3], so since U is a neighborhood of z in W, we have z ∈U\∂U.
Applying 5.2 to U and its formal model U shows that Y ′ is proper as well. Therefore,
the map Y ′ →Y is ﬁnite and surjective. Note that Y ′ is an irreducible component of Cs.
Applying (2) to U and C, we have that h|C is semipositive, and so we deduce from [GJR21,
Lemma 7.4] as applied to (π∗L)|C that degπ∗L(Y ′) ≥0. The projection formula then shows
degL(Y) ≥0, as required.
□
To apply results from Thuillier’s thesis [Thu05], we would like to use only smooth an-
alytic curves. To give a variant of the above result suitable for this purpose, we introduce
the following notations:
For a real function h on X and an analytic ﬁeld extension F of k, we denote by hF
the induced function on the base change X F = X b⊗kF of X. We call an R-PL function
h pluriharmonic if ±h are both semipositive. A strictly k-analytic space X is called rig-
smooth if the sheaf of Kähler differentials, considered on the G-topology, is locally free of
rank equal to the local dimension. The space X is smooth if and only if X is rig-smooth and
boundaryless. See [Duc18] for details (Ducros calls rig-smooth spaces quasi-smooth).
Corollary 5.4. Let X be a good, strictly k-analytic space and let h: X →R be an R-PL
function. Then the following conditions are equivalent:


## GR-PL actual PDF page 17

ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY
17
(1) The function h is semipositive (resp. pluriharmonic).
(2) There is an algebraically closed analytic ﬁeld extension F of k such that for every
rig-smooth analytic curve C over F and every morphism ϕ: C →X F, the function
hF ◦ϕ is semipositive (resp. harmonic) on C.
(3) There is an algebraically closed analytic ﬁeld extension F of k such that for every
smooth analytic curve C over F and every morphism ϕ: C →X F, the function hF ◦ϕ
is semipositive (resp. harmonic) on C.
If (2) or (3) is true for an algebraically closed analytic ﬁeld extension F of k, then
it is true for all analytic ﬁeld extensions. This follows from Corollary 5.4 and Propo-
sition [GJR21, Proposition 7.6(2’)] which allows to check semipositivity over any ﬁeld
extension.
Proof. It is enough to prove the claim for semipositive functions, as h is pluriharmonic if
and only if h and −h are semipositive. Since semipositivity is stable under pullback and
extension of scalars [GJR21, Proposition 7.6], clearly (1) yields (2). Since a smooth an-
alytic curve is just a boundaryless rig-smooth curve, it is clear that (2) yields (3). In fact,
these two conditions are equivalent as an R-PL function is automatically semipositive in
every boundary point y of an analytic curve C. Indeed, it follows from 5.2 that red(C, y)
is non-proper and hence there is no condition for semipositivity at y.
It remains to show that that (2) yields (1). Assume that (2) holds. By base change
using [GJR21, Proposition 7.6(2’)], we may assume that k = F. Let x ∈X and let U be
a strictly analytic neighborhood of x. For any Zariski-closed curve Y in U, we will show
that h|Y is semipositive. Replacing Y by Yred and using [GJR21, Proposition 7.6(3’)], we
may assume that Y is reduced. Let ϕ: C →Y be the normalization of Y (see [Ber90]
before Proposition 3.1.8). Then C is a rig-smooth curve because k is perfect (it is alge-
braically closed). By (2), the function h◦ϕ is semipositive on C. Since the normalization
morphism is ﬁnite and surjective, it follows from [GJR21, Proposition 7.6(1’)] that h|Y is
semipositive. By Theorem 5.3, we conclude that h is semipositive at x. Since x was an
arbitrary point of X, we get (1).
□
Corollary 5.5. Let X be a good, strictly k-analytic space and let Λ be either Z or Q. Let
h1,h2: X →R be semipositive Λ-PL functions. Then max(h1,h2) is a semipositive Λ-PL
function.
Corollary 5.5 fails for Λ strictly containing Q, but only because we restrict ourselves to
the G-topology generated by strictly analytic domains. See [GJR21, Example 5.3].
Proof. We ﬁrst note that max(h1,h2) is a Λ-PL function [GJR21, Remark 5.2]. Using
Corollary 5.4, it is enough to prove that max(h1,h2) is semipositive in case of a smooth
analytic curve X. Since the maximum of two subharmonic functions on such a curve is
subharmonic [Thu05, Proposition 3.1.8], the claim follows from Proposition 5.1.
□
Theorem 5.6. Let X be a good, strictly k-analytic space and let (hj)j∈N be a sequence of
semipositive R-PL functions on X converging pointwise to an R-PL function h. Then h is
semipositive.


## Wanner actual PDF page 1

arXiv:1801.04713v3  [math.AG]  8 Nov 2018
COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON
NON-ARCHIMEDEAN CURVES
VERONIKA WANNER
Abstract. We show that a continuous function on the analytiﬁcation of a smooth
proper algebraic curve over a non-archimedean ﬁeld is subharmonic in the sense of
Thuillier if and only if it is psh, i.e. subharmonic in the sense of Chambert-Loir and
Ducros. This equivalence implies that the property psh for continuous functions is
stable under pullback with respect to morphisms of curves. Furthermore, we prove
an analogue of the monotone regularization theorem on the analytiﬁcation of P1 and
Mumford curves using this equivalence.
MSC: Primary 32P05; Secondary 14G22, 14T05, 3205, 32U40
Keywords: Subharmonic functions, Superforms, Berkovich spaces, Tropical geometry
Contents
1.
Introduction
1
2.
Preliminaries on Thuillier’s notion of subharmonic functions
4
3.
Preliminaries on subharmonic functions in the sense of Chambert-Loir and
Ducros
6
4.
Comparison of the two notions of subharmonic functions
15
5.
Stability under pullback and a regularization theorem
28
References
31
1. Introduction
Potential theory studies subharmonic functions and is a very old area of mathematics,
which originates in the 18th century. This theory, and so in particular the theory of
subharmonic functions, can be extended to non-archimedean analytic geometry. This is
for example done by Baker and Rumely in [BR10] for the non-archimedean projective line
and by Thuillier in [Thu05] for general curves. One is interested to develop this theory
for non-archimedean spaces also in higher dimensions, i.e. to develop a pluripotential
theory analogue to the classical one. Ideas and concepts from pluripotential theory have
been already introduced into the theory of non-archimedean analytic spaces by several
authors as Zhang [Zha93], Boucksom, Favre, and Jonsson [BFJ12], Chambert-Loir and
Ducros [CD12], and Gubler and Künnemann [GK14, GK15]. For example, Chambert-
Loir and Ducros deﬁned in [CD12] plurisubharmonic functions with the help of their
real-valued diﬀerential forms and currents on Berkovich spaces. Plurisubharmonicity is
more precisely characterized by positivity of a special current corresponding to the given
function.
Their deﬁnition of plurisubharmonicity is analogous to the one in classical
The author was supported by the collaborative research center SFB 1085 ’Higher Invariants’ funded
by the Deutsche Forschungsgemeinschaft.
1


## Wanner actual PDF page 28

28
V. WANNER
subchart of both [Gub16, Proposition 4.16], we get
ψy,e ◦τX ′ = (φ ◦Trop(π)) ◦tropUx∩U′x
g±
k = (φ′ ◦Trop(π′)) ◦tropUx∩U′x
for the corresponding transition functions π, π′ satisfying ϕUx = π ◦(ϕUx × ϕU′x) and
ϕU′x = π′ ◦(ϕUx × ϕU′x). Since Trop(π) and Trop(π′) are integral aﬃne functions on
Rr+r′, the composition φ◦Trop(π) (resp. φ′◦Trop(π′)) is still a smooth function on Rr+r′
with a convex restriction to every polyhedron. Thus, mε(φ ◦Trop(π), φ′ ◦Trop(π′)) is a
smooth function on Rr+r′, and the properties i) and iv) of mε imply that the restriction
to every polyhedron is convex since the restriction of φ ◦Trop(π) and φ′ ◦Trop(π′) are.
We have
eg±
k = mε(g±
k , ψy,e ◦τX ′) = mε(φ ◦Trop(π), φ′ ◦Trop(π′)) ◦tropUx∩U′x
on Vx ∩V ′
x for every x ∈τ −1
X ′ (Ωy,e), so eg±
k is a smooth psh function on τ −1
X ′ (Ωy,e) by
Proposition 3.20, which proves Step 5.
Altogether, eg±
k are smooth psh function on V . We set
egk := eg+
k −eg−
k ,
then the functions egk satisfy by construction all the required properties in Step 0.
6. Step:
Construction of V ′ and η.
By the construction of V and egk, it is no problem to construct the required set V ′,
i.e. an open subset V ′ of V containing Y such that V ′ ⊂V and egk ∈C∞
c (V ′). Fur-
thermore, let V ′′ be an open neighborhood of V ′ in V with V ′′ ⊂V . The topological
space Xan is a compact Hausdorﬀspace. Urysohn’s Lemma states the existence of a
continuous function η: Xan →[0, 1] with η ≡1 on V ′ and η ≡0 on Xan\V ′′. Thus, η
has compact support in V , i.e. it is the required function in Step 0.
Thus, we have constructed everything as it was described in Step 0 proving the theo-
rem.
□
Corollary 4.8. Let f : W →R be a continuous function. Then f is subharmonic if and
only if f is psh.
Proof. Follows directly from Theorem 4.5 and Theorem 4.7.
□
5. Stability under pullback and a regularization theorem
Due to this equivalence in Corollary 4.8, we know that a continuous psh function
has all the nice properties that are shown for subharmonic functions in [Thu05]. More
precisely, we now know that the property psh for continuous functions is stable under
pullback with respect to morphisms of curves. Furthermore, we show that there is a
monotone regularization theorem in the setting of Chambert-Loir and Ducros under
certain conditions, e.g. if X is P1
K or a Mumford curve.
Corollary 5.1. Let X, X′ be smooth proper algebraic curves over K and ϕ: W ′ →W
be a morphism of K-analytic spaces for open subsets W ⊂Xan and W ′ ⊂(X′)an. If a
continuous function f : W →R is psh on W, then ϕ∗f is psh on ϕ−1(W).
Proof. By Corollary 4.8, the function f is subharmonic on W, and so ϕ∗f is subharmonic
on ϕ−1(W) by Proposition 2.6. Using again Corollary 4.8, ϕ∗f is psh on ϕ−1(W).
□


## Wanner actual PDF page 29

COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 29
To obtain a monotone regularization theorem in the setting of Chambert-Loir and
Ducros for certain X, e.g. for the projective line or a Mumford curve, we use the monotone
regularization theorem in Thuillier’s setting. Hence, we ﬁrst need to show that every
point has an open neighborhood such that every lisse subharmonic, and so psh, function
is globally psh-approximable on it, i.e. it is the uniform limit of smooth psh functions.
Recall the deﬁnition of the sheaf C∞of smooth functions on Xan from Deﬁnition 3.12.
The key tool of this step is to use that for certain X every lisse function f with ddcf = 0 is
automatically smooth (cf. [Thu05, Théorème 2.3.21]). These functions are the harmonic
functions and the corresponding sheaf is denoted by HX (cf. Deﬁnition 2.10). Note that
in general, every smooth function f with d′d′′f = 0 is harmonic.
Lemma 5.2. Let X be a smooth proper algebraic curve such that the sheaf HX of har-
monic functions on Xan is a subsheaf of the sheaf C∞of smooth functions on Xan.
Then every lisse function f : Y →R on a strictly aﬃnoid domain Y of Xan which is
subharmonic on the interior W := Y \∂Y of Y is globally psh-approximable on W. More
precisely, there is a monotone decreasing sequence of continuous functions fk on Y that
are smooth and psh on W, and converge uniformly to f on Y .
Proof. Since f is lisse, we can ﬁnd a strictly semistable model Y such that f = F ◦τY
on Y for a piecewise aﬃne function F on S(Y). We construct continuous functions on
Y converging uniformly to f that are smooth and psh on W using techniques as in the
proof of Theorem 4.7.
Let S be the set of points in S(Y)\∂Y that are contained in the support of the discrete
measure ddcF. Consider in the following a point x in S. Then ddcF > 0 in an open
neighborhood of x because f is subharmonic. The considered point x is either of type
II or III. If x is of type II, we may assume x to be a vertex of S(Y) and we denote by
ex,1, . . . , ex,n the adjacent edges in S(Y) and by xi the second endpoint of ex,i. If x is of
type III, x is contained in the interior of an edge ex with endpoints x1 and x2 and we
denote by ex,1 and ex,2 the segments [x1, x] and [x, x2] of ex. By blowing up Y, we may
assume that no xi belongs to S and that F restricted to every ex,i is aﬃne.
In both situations, type II or III, we can ﬁnd a piecewise aﬃne function Gx on Γx :=
S
i=1,...,n ex,i such that
i) Gx(x) = F(x),
ii) Gx < F on Γx\{x},
iii) ddcGx = 0 in a neighborhood of x, and
iv) (Gx)|ex,i is aﬃne for every i = 1, . . . , n.
Choose εx,i > 0 with F(xi) −Gx(xi) > 2εx,i. Then there is a point yi ∈(x, xi) such
that F(yi) = Gx(yi) + εx,i, F < Gx + εx,i on [x, yi) and F > Gx + εx,i on (yi, xi].
Since S has only ﬁnitely many points and corresponding adjacent edges, we can set
ε0 := minx∈S,i εx,i. Then for every x ∈S, every ex,i = [x, xi], and every 0 < ε ≤ε0 the
following inequalities
Gx(x) + ε −F(x) > ε/2,
F(xi) −(Gx(xi) + ε) > ε/2
(5.1)
hold.
For every x ∈S, the set Vx := (τ −1
Y (Γ◦
x)) is an open neighborhood of x in W and by
construction these sets are pairwise disjoint. We deﬁne for every 0 < ε ≤ε0 the following
function on Y
fε :=
(
m ε
2 (Gx ◦τY + ε, f)
on Vx for x ∈S,
f
on Y \ S
x∈S Vx,
(5.2)


## Wanner actual PDF page 30

30
V. WANNER
where mε is the smooth maximum deﬁned in (4.6) (see proof of Theorem 4.7). By (5.1)
and property iii) of mε/2 in (4.6), the deﬁned function coincides with Gx ◦τY + ε in an
open neighborhood of x and with f in an open neighborhood of xi, where xi is the other
vertex for an adjacent ex,i = [x, xi]. Thus, fε is continuous on Y .
We will later use functions of this form to construct our sequence, but ﬁrst we show
that fε is smooth and psh on W. By construction, there is an open neighborhood W ′ of
W\ S
x∈S Vx such that fε coincides with f and f = F ◦τY is harmonic on W ′. Since we
required that HX is a subsheaf of C∞and every harmonic function is psh by Proposition
2.11 and Theorem 4.7, the function fε is a smooth psh function on W ′.
On the other hand, for every x ∈S the constructed function fε coincides with the
harmonic function Gx ◦τY + ε on an open neighborhood of x, and so it is locally smooth
and psh at x as well. It remains to consider fε on τ −1
Y ((x, xi)) for every x ∈S and
every adjacent ex,i = [x, xi]. Since f and Gx ◦τY + ε are harmonic, and so smooth
and psh on τ −1
Y ((x, xi)), one can show as in Step 5 in the proof of Theorem 4.7 that
fε = m ε
2(Gx ◦τY + ε, f) is still smooth and psh on τ −1
Y ((x, xi)). Altogether, fε is a
smooth psh function on W.
With the help of the function fε deﬁned in (5.2), we construct now a monotonically
decreasing sequence (fk)k∈N of smooth psh functions converging uniformly to f on Y .
For every k ∈N, we deﬁne εk > 0 recursively starting with ε0 from above, and set
fk := fεk. To do so, we need to consider the subsets
Ωk :=
[
x∈S
n
y ∈Vx | |Gx(τY(y)) + εk −f(y)| < εk
2
o
on which fk does not necessarily coincide with max(Gx ◦τY + εk, f) for some x ∈S. For
a given εk, we choose εk+1 such that 0 < εk+1 < εk/3. Then Ωk ∩Ωk+1 = ∅for every
k ∈N and εk →0 for k →∞.
We show that the sequence fk converges pointwise to f and fk+1 ≤fk on Y .
If
y ∈Y \ S
x∈S Vx, then all fk coincide with f, and so both assertions are trivial. We
therefore assume that y ∈Vx for some x ∈S. In the case of y ∈τ −1
Y (x), we have
fk(y) = Gx(x) + εk = F(x) + εk = f(y) + εk,
and so fk(y) ≥fk+1(y) and fk(y) converges to f(y) for k →∞. Now we consider the case
y ∈Vx\{τ −1
Y (x)}. Then we can ﬁnd an εN small enough such that f(y) −(Gx(τY(y)) +
εN) > εN/2. Hence, for every k ≥N we have f(y) −(Gx(τY(y)) + εk) > εk/2, and so
fk(y) = max(Gx ◦τY + εk, f) = f(y).
Thus, fk(y) converges clearly to f(y). Next, consider an arbitrary k ∈N and show
fk(y) ≥fk+1(y). If y /∈Ωk ∪Ωk+1, then
fk+1(y) = max(Gx(τY(y)) + εk+1, f(y)) ≤max(Gx(τY(y)) + εk, f(y)) = fk(y)
since εk > εk+1. If y ∈Ωk, by the choice of εk+1, we have y /∈Ωk+1. Thus,
fk+1(y) = max(Gx(τY(y)) + εk+1, f(y)) ≤max(Gx(τY(y)) + εk, f(y)) ≤fk(y),
where the last inequality is true by property ii) following (4.6). Finally, let y ∈Ωk+1,
and so y /∈Ωk. Then Gx(τY(y)) + εk ≥f(y) as εk+1 < εk/3, and so
fk(y) = max(Gx(τY(y)) + εk, f(y)) = Gx(τY(y)) + εk ≥f(y) + εk/2


## Wanner actual PDF page 31

COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 31
as y /∈Ωk. By property ii) following (4.6), εk+1 < εk/3 and the last inequality, we get
fk+1(y) ≤max(Gx(τY(y)) + εk+1, f(y)) + εk+1/4
≤max(Gx(τY(y)) + εk, f(y) + εk/2)
≤fk(y).
Thus, the sequence fk of continuous functions converges pointwise to the continuous
function f on Y and fk+1 ≤fk. Since Y is compact, fk converge uniformly by Dini’s
theorem. We have already seen above that every fk is smooth and psh on W.
□
Before we use this lemma to prove a monotone regularization theorem in the setting of
Chambert-Loir and Ducros for Mumford curves, we recall the deﬁnition of these curves.
Deﬁnition 5.3. A smooth proper curve X of genus g ≥1 over K is called a Mumford
curve if there is a semistable model X such that all irreducible components of the special
ﬁbre are rational (cf. [Ber90, Theorem 4.4.1]).
Corollary 5.4. Let X be a smooth proper curve over K. If eK is algebraic over a ﬁnite
ﬁeld or X is the projective line or a Mumford curve, then every continuous psh function
f : W →R on an open subset W of Xan is locally psh-approximable. More precisely, the
sequence of smooth psh functions can be chosen monotonically decreasing.
Proof. At ﬁrst, note that in the given situation HX is a subsheaf of C∞on Xan, which
is a consequence of [Thu05, Théorème 2.3.21] (see [Wan16, Corollary 5.3.21]). We ad-
ditionally use [Ber90, Theorem 4.4.1] in the case of a Mumford curve. Hence, we may
apply Lemma 5.2.
To prove the corollary, we have to show that every point x in W has an open neigh-
borhood in W such that f is a uniform limit of smooth psh functions. The continuous
psh function f is subharmonic by Theorem 4.7, and we therefore can use Thuillier’s
monotone regularization theorem (see Proposition 2.8). We can ﬁnd for every x ∈W a
relatively compact neighborhood W ′ of x in W and a decreasing net ⟨fj⟩of lisse subhar-
monic functions on W ′ converging pointwise to f. Let Y be a strictly aﬃnoid domain
in W ′ having x in its interior Y ◦. Then the decreasing net ⟨fj⟩converges uniformly to
the continuous function f on the compact set Y by Dini’s theorem. Thus, one can con-
struct inductively a decreasing sequence of lisse subharmonic functions on W ′ converging
uniformly to f on Y and we write (fk)k∈N for this sequence.
We have seen in Lemma 5.2 that each fk is the uniform limit of a decreasing sequence
of smooth psh functions on Y ◦. Hence, we can choose a decreasing sequence of smooth
psh functions on Y ◦converging uniformly to f.
□
Remark 5.5. Note that there are curves such that the sheaf HX of harmonic functions
is not a subsheaf of the sheaf C∞of smooth functions on Xan. A counter example of such
a curve can be constructed by the proof of [Thu05, Théorème 2.3.21] (see for example
[Wan16, Corollary 5.3.23]). For those curves we do not know whether every psh function
is locally psh-approachable.
References
[Ber90]
Vladimir G. Berkovich. Spectral theory and analytic geometry over non-Archimedean ﬁelds,
volume 33 of Mathematical Surveys and Monographs. American Mathematical Society, Prov-
idence, RI, 1990.
[Ber07]
Vladimir G. Berkovich. Integration of one-forms on p-adic analytic spaces, volume 162 of
Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 2007.


## Berkovich actual PDF page 31

34 
VLADIMIR G. BERKOVICH
by ^v the topological interior of V in X and by Vy the canonical open immersion of
locally ringed spaces ^y ->V. Then {(^<y, Vy)} is an open ^-analytic atlas on X, and the
^-analytic space from [Ber] obtained in this way gives rise to a ^-analytic space from k-^/n
isomorphic to X. Thus, the correspondence X h-> (X, s/y, a) is an equivalence of the
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
(iii) IfP is the class of proper morphisms of good analytic spaces ([Ber], p. 50),
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
u/ 
<p
(ii) For a sequence of morphisms Z -> Y -> X, one has
Int(Z/Y) n ^(In^Y/X)) C Int(Z/X).


## Berkovich actual PDF page 32

fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES 
35
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
set Xo =={x eX| \^[x) : k] < oo }. (We remark that from [Ber], 2.1.15, it follows
that the set Xo is everywhere dense in X.) First of all, ifX= Ji({^) is strictly A-affinoid,
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


## Berkovich actual PDF page 48

fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES 
51
field K{x) k8 is everywhere dense in K(^') and the both fields are quasicomplete, from
Corollary 2.4.2 it follows that G^')^G^^. Therefore there is an exact sequence
0 -> G^, ^ G^, -> G(K(^) k8^)) -> 0.
The latter group is a closed subgroup ofG^ and hence its cohomological dimension is at
most cd,{k). It follows that cd,(K^)) ^ cd^k) + cd,(K(^)). Since d^x')^) = d{K(x)lk),
Lemma 2.5.4 implies that cd;(K(A;')) = d(yi{x)jk).
Suppose now that dim(X) ^ 1 and that the theorem is true for affinoid spaces
whose dimension is at most dim(X) — 1. As in the proof of Theorem 2.5.1 we can
find a morphism/: X ->Y, where Y is a closed disc in A1, such that all of the fibres
ofX has dimension at most dim(X) — 1. Letj ==f(x). By induction,
cd^(A:)) ^ cd^(jO) + W^(j/)),
and, by the first case, cd,(^(j/)) ^ cd^) + d^(y)lk). Since
W^)/^)) + d{^^)fk) = d^{x)lk),
the required inequality follows. •
2.6. GAGA over an affinoid space
Let W be a scheme of locally finite type over X, and let F be the functor from the
category of morphisms Z -> X, where Z is a good analytic space over k, to the cate-
gory of sets which associates with Z -> X the set of morphisms of locally ringed
spaces over ^*, Hom^.(Z, W).
2.6.1. Proposition. — The functor F is representable by a closed morphism of k-analytic
spaces ^an -> X and a morphism of locally ringed spaces n: ^an -> W. The correspondence
^ ^ ^an is a functor which commutes with extensions of the ground field and with fibred products.
Proof. — The ^-analytic space ^an is constructed in the same way as in the case
when X ==^(A) (see [Ber], 3.4.1). Namely, one shows that if W is the affine space
over 3;, A^., then ^an = A^ = X x A^. After that one shows that if W^ exists for ^,
then y exists for any subscheme S C W. In particular, ^ exists for any affine scheme
of finite type over X and for any its open subscheme. Finally, if W is an arbitrary scheme
of locally finite type over ^, then one takes an open covering {^}^i of W by affine
subschemes of finite type over X. One glues together all of the W^s and obtains the
^-analytic space ^an associated with W. That the correspondence W ^ ^an is a functor
possessing the necessary properties follows from the universal property of W^. •
2.6.2. Proposition. — The map n: Y = ^ -> W is surjective, and for any pointy e Y
the ring Q^y is flat over fi^y, where y == n{jy) (i.e., n is a faithfully flat morphism}.


## Berkovich actual PDF page 50

STALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES 
53
y', z' e W over y and z, respectively, with z' e y'. Since the tensor product K{z) ®^ A(z')
is nontrivial, the valuation on K{z) extends to a multiplicative seminorm on it. It follows
that there exists a point z' e ^'an whose image in W is z' and in ^an is z. Thus, we can
extend the field A, and, in particular, we may assume that the valuation on k is nontrivial
and ^ is strictly ^-affinoid. Let W = Spec(B). Replacing B by B/^y, we may assume
that W is reduced and irreducible and that y is its generic point. Since ^an is everywhere
dense in ^an, we may assume that z e ^an. Furthermore, since the ring B is excellent
(it is finitely generated over the excellent ring j^), Reg(^) is an everywhere dense
Zariski open subset of W. Shrinking @^, we may assume that W is regular. In this case
the homomorphism B -> (9^ ^ is injective. From Lemma 2.6.3 it follows that the homo-
morphism B —^ fi^an , is injective. Take a sufficiently small connected strictly affinoid
neighborhood V == e^(^y) of the point z. The latter homomorphism goes through 3S^,
therefore the homomorphism B -> ^y is injective. Since ^an is regular and V is connected,
the ring 8S^ is an integral domain. By Proposition 2.1.1, there exists a point y e V for
which the character 88^ ->^[y) is injective. It follows that the character S8 ->J^(y)
is injective, and therefore ^{y) is the generic point of W. •
Proof of Proposition 2.6.4. — It is clear that TT'^T) C TT-^T). To verify the inverse
inequality, we may assume that T = ^. Since T is constructible, it contains an every-
where dense Zariski open subset of W and, in particular, all of the generic points of W.
From Lemma 2.6.5 it follows that TT-^T) = ^an. •
2.6.6. Corollary. — A constructible set T is open (resp. closed^ resp. everywhere dense)
in W if and only z^r^^T) is open (resp. closed, resp. everywhere dense) in ^an. •
2.6.7. Corollary. — A morphism 9 : S —> W between schemes of locally finite type over S£
is separated if and only if (p^ : ^an -> ^an is separated.
Proof. — Let ^ : S - > S x < y S be the diagonal morphism. If 9 is separated,
then A is a closed immersion, and it follows that so is A"1. Assume that 9^ is separated.
It suffices to verify that the set A(^T) is closed in 3£ X^ 3S. This follows from Corol-
lary 2.6.6 because A(^) is a constructible set and its preimage in ^an x^an ^an
is closed. •
2.6.8. Proposition. — For a morphism 9 : 3£ -> W between schemes of locally finite type
over 3F, one has n~\^{S')) == ^S^}.
Proof. — From the construction of the analytification it follows that the statement
is true when 3S is an open subscheme of W and, if{^}^j is Jan open covering of ^,
then { ^an }^ j is an open covering of ^an. Hence the situation is reduced to the case
when W = Spec(B) and 3S == Spec(G) are affine schemes of finite type over SK. The
inclusion ^(S^) C -n:"1^^)) is evident. To verify the converse inclusion, it suffices


## Berkovich actual PDF page 51

54 
VLADIMIR G. BERKOVICH
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
m 
n
^°, y ®ey „ ^, , ^ n C^, v X . n (^an ,,) ^,
' 
i == 1 
i==w+l
where (^an^.)p is the localization with respect to the complement of the prime ideal of C cor-
responding to the point z.
Proof. — If V is an affinoid domain in ^^ then for its preimage W in ^an one
has 
(S^=0§^®•QG. Since cp^ is finite, from Lemma 2.1.6 it follows that
^any^sC^ n^ ^an^.. The ring ^any®^ 
0^^ is the localization of ^an y0^ G
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


## Berkovich actual PDF page 125

128 
VLADIMIR G. BERKOVICH
where 9 is a proper morphism and j is an open immersion. For a sheaf ^ on ^ one
defines
R^^R^^).
By Nagata's Theorem, any separated morphism of finite type is compactifiable.
7.1.1. Theorem. — Let S£ be a compactifiable scheme over k, and let 3^ he an abelian
torsion sheaf on St'. Then for any q ^ 0 there is a canonical isomorphism
H^, y} ^ ny, ^an).
Proof. — Let 9 : W -> !C be a compactifiable morphism between schemes of locally
finite type over Spec(e^), where ^ is a A-affinoid algebra (the situation is slightly more
general for a further use). For a point x e SE we denote by ^ ^e fibre of 9 at x and
set ^ == ^ ® ^(x)8? and for an abelian torsion sheaf ^ on ^, we denote by ^ an(! ^x
the pullbacks of ^ on ^ ^d ^x? respectively. By the Base Change Theorem for Coho-
mology with Compact Support for schemes, one has
(R<^,^=H^,^).
Furthermore, for a point x e ^an over x, we fix an embedding of fields A(x)8 <->^{x)\
It gives rise to an isomorphism
(^x^^T^^T.
Since the cohomology with compact support of schemes are preserved under separably
closed extensions of the ground field, one has
H^x, ^x) ^H^®^^?)°, ^).
Finally, the Weak Base Change Theorem 5.3.1 tells that
R^ 9an(^aI% == H^(^|11, ^n).
We use the above remarks to establish the following two facts.
7.1.2. Lemma. — In the above situation assume that the dimension of y is at most one.
Then for any q ^ 0 one has
(R3 9. ^ -^ R3 9T" ^an.
Furthermore, if in addition °K and. W are compactifiable over k and the theorem is true for SK^ then
it is also true for W.


## Berkovich actual PDF page 126

fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES 
129
Proof. — The first statement follows from Theorem 6.1.1 and the above remarks,
and the homomorphism of Leray spectral sequences
H^, R^y. ^) ==> H^^, ^)
i 
i
H^^, R3 9^ ^an) ==> H^0^, ^an)
shows that the second statement is also true. •
7.1.3. Lemma. — In the above situation assume that the morphism 9 is finite and surjective.
Then if 2^ and W are compactifiable over k and the theorem is true for @<, then it is also true for SC.
Proof. — Let ^ be an abelian torsion sheaf on 3C. Since 9 is finite and surjecdve,
the canonical homomorphism y -> 9^(9* ^") is injective. Furthermore, by Corol-
lary 4.3.2, for an abelian sheaf ^ on W one has H^.^, 9^ ^an) ^ H^®^, ^an).
In particular, the hypothesis implies that the theorem is true for all sheaves of the
form 9^ ^S. Thus, one can construct a resolution of ^", 0 -> 3F -> ^ro ->^"1 ->...,
such that the theorem is true for all ^ri. The homomorphism of spectral sequences
H^H^^,^-)) ———> H^^,^)
i 
i
^(H^^0, ^ran')) ==> H^4-0^"1,^"1)
shows that the theorem is also true for ^r. •
We are now ready to prove the theorem.
1) The theorem is true for the direct product (P1)", where P1 is a the projective line over k.
— This follows from Lemma 7.1.2.
2) The theorem is true for the projective space P^ over k. — Indeed, there exists a finite
surjecdve morphism (P1)" -> P71, and we can use Lemma 7.1.3.
3) The theorem is true for any projective scheme over k. — This follows from Lemma 7.1.2.
4) The theorem is true for any affine scheme of finite type over k. —- This is so because
such a scheme is isomorphic to an open subscheme of a projective scheme.
5) The theorem is true for any proper scheme over k. — For a proper scheme SC we can
find an open everywhere dense affine subscheme ^, and so the dimension of the closed
subscheme W == 3E\^U is strictly less than the dimension of^*. Therefore the statement
is obtained by induction using the exact cohomological sequences associated with the
embeddings W ^ X <- W and ^an <-^ ^an <- ^an and the five-lemma.
6) The theorem is true for any compactifiable scheme. — This is already clear. •
7.1.4. Corollary. — Let 9 : W -> 3C be a compactifiable morphism between schemes of
locally finite type over Spec(J^), where ^ is a k-affinoid algebra^ and let ^S be an abelian torsion
sheaf on W. Then for any q ^ 0 there is a canonical isomorphism
(R^. ^ ^ R3 9^ ^an.
17


## CD actual PDF page 496

496
CHAPITRE 17. FIBRÉS VECTORIELS MÉTRISÉS
donc que de σ(π(x)), et sa construction est compatible à la restriction à un ouvert V de
U contenant encore π(x). On a ainsi construit un morphisme naturel de F := E⊗κ(π(x))
vers ]
E(x)
1
, qui induit un morphisme de F ⊗κ(π(x)) ^
H (x)
1
vers ]
E(x)
1
. Choisissons i ∈I.
Par construction, les eij(π(x)) pour j variable forment une base de F ; et comme les
(eij) forment une base orthonormée de E(x), les ^
eij(x) forment une base de ]
E(x)
1
. Par
conséquent, le morphisme de F ⊗κ(π(x)) ^
H (x)
1
vers ]
E(x)
1
construit ci-dessus est un
isomorphisme ; nous l’utiliserons pour identifier F à un sous κ(π(x))-espace vectoriel de
]
E(x)
1
.
On a ^
(X, x)
1
= S
i∈I ^
(Xi, x)
1
, et il résulte du lemme 11.9.2 que ^
(Xi, x)
1
est égal à
P ^
H (x)
1
/ek1{Vi} pour tout i ∈I ; c’est donc l’image réciproque de l’ouvert quasi-compact
Pκ(π(x))/ek1{Vi} de Pκ(π(x))/ek1.
Pour tout i ∈I, la famille (eij) étant une base orthonormée de E|Xi, la famille des
^
eij(x) est une base de f
Ex
1| ^
(Xi, x)
1
. Comme ^
eij(x) = eij(π(x)) pour tout (i, j), le lemme
10.6.11 assure que f
Ex
1 est l’image réciproque sur P ^
H (x)1/ek1 d’un fibré vectoriel G sur
Pκ(π(x))/ek1{V }, caractérisé par le fait que sa fibre générique est F et que pour tout i,
la famille des eij(π(x)) forme une base de G au-dessus de Pκ(π(x))/ek1{Vi}. Mais comme
l’image réciproque de E|V sur Pκ(π(x))/ek1{V } satisfait ces deux conditions, elle coïncide
avec G. Ainsi, (V, E) est bien un pré-modèle de (^
(X, x)
1
, f
Ex
1).
Exemple 17.7.11 (Fibré sur une variété propre en valuation triviale)
Supposons que la valuation de k est triviale. Soit X une k-variété algébrique et soit E
un fibré vectoriel sur X ; le paragraphe précédent s’applique et munit le fibré vectoriel Eη
sur Xη d’une métrique formelle. Supposons de plus que X soit propre ; alors on a Xη =
Xan et Eη = Ean.
Soit x un point de Xan ≃Xη et soit ˜x son image sur X ≃Xs. Le couple ({˜x}, E|{˜x}) est
un est alors un prémodèle de ( ^
(Xan, x)
1
, g
Ean
x
1) (où {˜x} est muni de sa structure réduite).
Notons un cas particulier important. Supposons X intègre, soit ξ son point générique,
et soit x le point de Xan correspondant à la flèche Spec(k(ξ), |·|0) →X. Le poitn x est
alors l’unique point de Xan se spécialisant en ξ ; par ce qui précède, (X, E) est alors un
prémodèle, et même un modèle, de ( ^
(Xan, x)
1
, g
Ean
x
1).
§ 17.8. MÉTRIQUES PSH
Définition 17.8.1. — Soit X un espace k-analytique topologiquement séparé, considéré
comme espace G-tropical affiné, et soit L un fibré en droites sur X, localement trivial
pour la topologie usuelle de X.
On dit qu’une métrique continue sur L est psh ( resp. dpsh, resp. tropicalement
convexe, resp. tropicalement dconvexe)
si, pour toute section inversible locale s de L,


## CD actual PDF page 497

§ 17.8. MÉTRIQUES PSH
497
la fonction continue log∥s∥−1 est psh (définition 8.1.1) ( resp. dpsh, resp. tropicalement
convexe, définition 8.2.6, resp. tropicalement d-convexe).
Pour qu’il en soit ainsi, il suffit que L possède une telle section au voisinage de tout
point de X.
Il découle de ces définitions qu’une métrique tropicalement convexe est tropicalement
d-convexe, qu’une métrique psh est d-psh, et qu’une métrique tropicalement convexe,
resp. tropicalement d-convexe, est psh, resp. d-psh.
Si la métrique de L est psh, sa courbure c1(L) est un courant positif.
Comme toute fonction lisse sur Rn est localement différence de deux fonctions psh
lisses (proposition 1.10.2, b)), toute métrique lisse sur L est tropicalement d-convexe.
Si X est presque bon, toute fonction G-lisse est localement différence de deux fonctions
tropicalement d-convexes (proposition 8.8.2, b)), de sorte que toute métrique G-lisse est
tropicalement d-convexe. C’est en particulier le cas des métriques paralinéaires.
Proposition 17.8.2. — Soit X un espace k-analytique séparé et presque bon, et soit L
un fibré en droites sur X muni d’une métrique paralinéaire entière. On suppose que L
est localement trivial pour la topologie usuelle de X.
Soit x ∈X tel qu’il existe une puissance strictement positive du fibré résiduel f
Lx
engendrée par ses sections globales. Alors la métrique de L est tropicalement convexe (et
donc psh) au voisinage de x.
Démonstration. — Quitte à remplacer L par une puissance strictement positive, on sup-
pose que f
Lx est engendré par ses sections globales. D’après le corollaire 17.4.12, il existe
donc une famille finie (a1, . . . , am) d’éléments de O×
X,x telle que la fonction ∥s∥−1 soit
égale à max(|a1|, . . . , |am|) au voisinage de x. Il découle alors de la proposition 8.2.1 que
la métrique de L est tropicalement convexe au voisinage de x.
Remarque 17.8.3. — Voyons comment la proposition précédente permet de redémon-
trer le fait rappelé après la définition 17.8.1 que les métriques paralinéaires strictement
entières sont tropicalement d-convexes (et donc d-psh).
L’assertion est locale. Soit x ∈X. La proposition 10.7.9 assure qu’il existe deux
fibrés en droites M1 et M2 sur ^
(X, x), engendrés par leurs sections globales, tels que
f
Lx ≃M1 ⊗M ∨
2 .
Relevons M1 et M2 en deux fibrés métrisés paralinéaires L1 et L2 sur (X, x), stricte-
ment entiers, et triviaux comme fibrés en droites au voisinage de x (théorème 17.4.9) ;
on dispose aussi d’après ce théorème d’un isomorphisme L ≃L1⊗L∨
2 de fibrés en droites
métrisés au voisinage de x. D’après le premier cas, les métriques de L1 et L2 sont tropi-
calement convexes au voisinage de x. Par conséquent, la métrique de L est tropicalement
d-convexe au voisinage de x.
Proposition 17.8.4. — Soit X un k-espace analytique séparé et sans bord, et soit L
un fibré en droites sur X muni d’une métrique paralinéaire strictement entière.
Soit x ∈X tel que le fibré résiduel f
Lx soit numériquement effectif (10.4.11). Alors la
métrique de L est psh au voisinage de x.
Démonstration. — Soit (V, M) un prémodèle du fibré résiduel eL(x) ; comme X est sans
bord, V est propre ; par le lemme de Chow, on peut supposer que V est projective.
Soit M ′ un fibré ample sur V ; il existe un voisinage compact U de x dans X et une


## CD actual PDF page 498

498
CHAPITRE 17. FIBRÉS VECTORIELS MÉTRISÉS
métrique strictement pl sur le fibré trivial OU dont le fibré résiduel en x est M ′ ; notons
h = log(∥1∥−1) pour M ′ ; d’après la fonction précédente, c’est une fonction psh (et même
tropicalement convexe) sur X.
Pour tout nombre réel ε > 0, on peut munir le fibré en droites L|U de la métrique
∥·∥ε qui est le produit de sa métrique initiale par la fonction exp(−εh). Lorsque ε tend
vers 0, cette métrique tend uniformément vers celle de L sur U. Il suffit donc d’observer
que cette métrique est psh lorsque ε est un nombre rationnel (a posteriori, elle sera psh
pour tout nombre réel positif ε).
Supposons donc ε rationnel ; écrivons ε = m/n avec m, n ⩾1. Alors la métrique ∥·∥ε
est strictement Q-pl ; la métrique (∥·∥ε)N sur L⊗N|U est strictement pl ; il suffit de
prouver qu’elle est psh. Or, le fibré résiduel associé est donné par le prémodèle (V, M ⊗n⊗
(M ′)⊗m). Comme M est numériquement effectif et M ′ est ample, il résulte du critère
de Nakai-Moishezon que ce fibré en droites sur V est ample. D’après la proposition
précédente, la métrique considérée est psh.
17.8.5. — On dit qu’une métrique continue ∥·∥sur L est globalement psh s’il existe une
suite (∥·∥n) de métriques psh lisses sur L telles que les fonctions continues log(∥·∥/∥·∥n)
sur X convergent uniformément vers 0.
On dit qu’une métrique continue sur L est globalement dpsh s’il existe deux fibrés en
droites L1 et L2 sur X, munis de métriques globalement psh, tels que L ≃L1 ⊗L
−1
2 .
Proposition 17.8.6. — Sur l’espace projectif Pn, le fibré en droites O(1) muni de sa
métrique formelle canonique est globalement psh et tropicalement convexe.
Plus précisément, il existe une famille (∥·∥η)η>0 de métriques psh lisses sur O(1), qui
converge uniformément vers sa métrique formelle canonique quand η →0, vérifiant de
plus la propriété suivante : soit x ∈Pn, soit I l’ensemble des i ∈{0, . . . , n} tels que
x ∈D(Ti) ; il existe un voisinage U de x dans T
i∈I D(Ti) tel que, pour i ∈I et η < 1,
la fonction ∥Ti∥η est tropicalisée par le moment (Tj/Ti)j∈I sur U.
Démonstration. — Tout fibré résiduel de ce fibré en droites admet un prémodèle qui
est le fibré O(1) d’une sous-variété de Pn
˜k ; il est en particulier semi-ample. D’après la
proposition 17.8.2, la métrique de Weil est tropicalement convexe. Démontrons qu’elle
est globalement psh.
Pour tout entier p ⩾0 et tout nombre réel η > 0, Demailly définit dans [45],
lemme 5.18, une fonction Mη : Rp →R vérifiant les propriétés suivantes :
a) La fonction Mη est lisse, convexe et croissante en chaque variable ;
b) Pour tout (t1, . . . , tp) ∈Rp,
max(t1, . . . , tp) ⩽Mη(t1, . . . , tp) ⩽max(t1, . . . , tp) + η;
c) Si tj + η ⩽maxi̸=j(ti −η), on a
Mη(t1, . . . , tp) = Mη(t1, . . . , btj, . . . , tp) ;
d) Pour tout t ∈R,
Mη(t1 + t, . . . , tp + t) = Mη(t1, . . . , tp) + t.
Il résulte de la lissité de la fonction Mη et de la propriété d) que l’on définit une
métrique lisse ∥·∥η sur O(1) en posant
log∥sP∥−1
η ([x0 : . . . : xn]) = −log|P(x0, . . . , xn)| + Mη(log|x0|, . . . , log|xn|)
