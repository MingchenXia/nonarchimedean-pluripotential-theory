# Exact new geometric scope and remaining original obligations

{
  "id": "P03.1",
  "status": "partial",
  "exact_result": "For every usc obstacle, the full local-Fubini--Study/semipositive-real-PL regularized envelope is classically psh on products of a perfected-bijective-normalization strict curve with a smooth geometrically connected projective factor, and on analytic projective bundles over such curves. Exact global competitor descent and ordinary projection/regularization compatibility are proved. Concrete normal domains and nonnormal geometrically unibranch cusp products are realized. Explicit continuous-obstacle failures are proved for split branches, codimension-two seminormal point gluings including a single irreducible bidisc with two points pinched, and the irreducible nonsplit quadratic-node surface over Q_3.",
  "proof_file": "P03.1-argument.md",
  "concrete_gaps": [
    "No sharp necessary-and-sufficient hypotheses for arbitrary normal or geometrically unibranch higher-dimensional analytic domains.",
    "No general positivity theorem for normal higher-dimensional affinoids beyond the proved projective-fiber sectors.",
    "No full-family scalar-extension cofinality or general scalar regularization compatibility theorem.",
    "The explicit codimension-two point pinching is not asserted to equal the supplied book's exact construction.",
    "No claim of CLD-stage positivity or continuity for arbitrary full-family envelopes."
  ]
}

# Entire final proof

# Full obstacle envelopes on curve bases with projective fibers

This is a partial result for P03.1. It proves classical positivity for every upper-semicontinuous obstacle and the full stated competitor union on actual products with smooth geometrically connected projective factors, and on analytic projective bundles over the indicated curves. It also gives complete explicit proofs of three negative phenomena: split branches, a codimension-two point pinching, and the nonsplit quadratic node after product with an open disc. It does not classify all normal or geometrically unibranch higher-dimensional analytic domains. No supplied book assertion or review verdict is used as a proof. No conclusion about CLD stages or continuity of arbitrary envelopes is asserted.

## 1. Definitions and checked primary foundations

Throughout, \(K\) is a complete nontrivially valued non-Archimedean field. All spaces on which PL functions are considered are good, separated and strictly \(K\)-analytic. Absolute boundary means Berkovich boundary over \(\mathcal M(K)\), not topological boundary in an unspecified ambient space. An analytic field extension is a complete isometrically valued extension; it need not be algebraic.

Write \(\operatorname{SP}_{\mathbb R}(W)\) for the finite semipositive real-PL functions on \(W\). For an obstacle \(f:W\to\mathbb R\cup\{-\infty\}\), define the exact family and envelope

\[
\begin{split}
\mathcal E_W(f)&=\{h:W\to\mathbb R:h\leq f,\ h\text{ is locally Fubini--Study or semipositive real PL}\},\\
P_W f&=\sup_{h\in\mathcal E_W(f)}h,\qquad
(P_W f)^*(x)=\inf_{N\ni x}\sup_{z\in N}P_W f(z).
\end{split}
\]

The infimum uses ordinary open neighborhoods, including the point itself. An empty supremum is identically \(-\infty\).

The following published foundations are used with their precise hypotheses. Their complete selected primary pages, including statements and available proof bodies, are retained separately. The labels here refer to the cached primary versions, not the supplied book.

* [GJR] is Gubler--Jell--Rabinoff, arXiv:2111.05741. Definition 5.1 makes real PL functions continuous and finite, using strict analytic G-coverings and real linear combinations of logs of analytic units. Definitions 7.2 and 7.8 define semipositivity by nef residues and LFS by semiample residues. Consequently LFS is a subclass of \(\operatorname{SP}_{\mathbb R}\). Thus, literally for the union in this assignment,
  \[
  \mathcal E_W(f)=\{h\in\operatorname{SP}_{\mathbb R}(W):h\leq f\}.
  \]
  This identification does not replace the family by a chosen subfamily. Lemma 5.4 and Proposition 7.6 give pullback and arbitrary analytic scalar extension for PL functions and semipositivity. Corollary 5.12 gives descent of real PL along a finite scalar extension; \(\mathbb R\) is divisible, as required. Semipositivity also descends under that extension by Proposition 7.6(2'). Semipositivity is an ordinary-topology sheaf property, as stated in 7.3(3).

* [GR1] is Gubler--Rabinoff, arXiv:2506.13548v2. Definition 4.1 requires subharmonic pullbacks on analytic curves after every analytic field extension. Definition 3.4 allows the identically \(-\infty\) alternative. Remark 3.4.1 identifies this convention with Thuillier's on connected smooth strict curves. Proposition 3.5(3) extends subharmonicity from the absolute interior to an already usc function on the whole curve. Proposition 3.5(7,8) gives scalar stability and finite-surjective descent. Lemmas 3.7--3.9 give the perfected scalar homeomorphism, reduction homeomorphism, and normalization facts. Proposition 4.2 gives analytic pullback and scalar stability of classical psh functions. Theorem 4.3 says that a real-PL function on a good strict space over a nontrivially valued field is semipositive exactly when it is classically psh. Theorem 6.1 gives the local maximum principle in the absolute interior. Theorem 6.4 gives the Shilov-boundary maximum principle on affinoids.

* [Thu] is Thuillier's thesis, HAL tel-00010990v1. The standing curve in Chapter 3 is smooth and strictly analytic; the valuation is nontrivial. Proposition 3.1.8(iii), on printed page 62, states that the usc regularization of the supremum of an increasing locally bounded family of subharmonic functions on an open set is subharmonic. The original PDF says locally bounded, rather than merely locally bounded above. We meet the stronger literal condition below by anchoring finite maxima at a fixed continuous member. This statement is Proposition 3.1.8(iii), not Lemma 3.1.9. Proposition 3.1.14 and Corollary 3.4.5 concern curve and scalar pullback, respectively; [GR1] also checks their role in its extended definition.

* [Ber] is Berkovich, Publications Mathématiques de l'IHÉS 78 (1993). Proposition 2.6.1 gives boundaryless analytification and its compatibility with fiber products and field extension. Proposition 2.6.9 preserves properness under analytification. Proposition 3.5.8 preserves smoothness under analytification, and Proposition 3.5.2 preserves it under base change. Corollary 3.7.4 says that a smooth morphism is an ordinary open map. Smoothness here includes absence of relative boundary; absolute boundary of the base is allowed. Theorem 7.1.1 compares compactly supported étale cohomology of a compactifiable scheme and its analytification for an abelian torsion sheaf. Only its degree-zero proper case is used, to prove analytic connectedness below. Corollaries 2.2.7--2.2.8 transfer regularity from algebraic analytification to affinoid domains.

[GR2], arXiv:2503.05513, was also checked: its current Proposition 5.1 and Corollary 5.4 are the PL curve-comparison statements. [GR1] refers to an older numbering in that paper. The standing convention is that smooth means rig-smooth and boundaryless. We do not apply a smooth-curve theorem directly to a closed disc with absolute boundary.

### An exact local LFS presentation used in the examples

[GJR, 7.9] uses nonnegative combinations of functions \(\max_j(-\log|u_j|)\) with each \(u_j\) invertible on an ordinary open neighborhood, in addition to the real-PL requirement. We use the following elementary rational instance, so no closure of arbitrary real-PL functions under maxima is assumed.

Let \(c\in K^\times\), let \(F_1,\ldots,F_r\) be analytic functions on \(W\), and let \(n\geq1\). Then

\[
H=\frac1n\log\max\{|c|,|F_1|,\ldots,|F_r|\}
\]

is finite continuous, rational PL and LFS. To prove this, fix a point. Functions vanishing there can be discarded on a smaller open neighborhood, because their absolute values are less than \(|c|\). Retained functions are nonzero at the point and become analytic units after shrinking. On a strict affinoid neighborhood, the finitely many rational domains where a selected unit has largest absolute value form a G-covering; on each, \(H\) is \(n^{-1}\) times the log of that unit. This proves rational PL. On the ordinary open neighborhood, write the displayed maximum as

\[
H=\frac1n\max\{-\log|c^{-1}|,-\log|F_j^{-1}|:j\text{ retained}\}.
\]

The coefficient is nonnegative and all functions inside the logs are units. This is precisely the checked LFS presentation. If none is retained, the function is constant there. Every real constant is also real PL and LFS: choose \(0<|\varpi|<1\), express the constant as a real multiple of \(\log|\varpi|\), and choose \(\varpi\) or \(\varpi^{-1}\) to make the coefficient in the negative-log presentation nonnegative. Constant residues are trivial and semiample.

## 2. Two elementary envelope lemmas

### Open projection and upper regularization

If \(p:X\to B\) is a continuous open surjection and \(a:B\to\mathbb R\cup\{-\infty\}\) is locally bounded above, then

\[
(a\circ p)^*=a^*\circ p. \tag{2.1}
\]

Indeed, a base neighborhood \(N\ni p(y)\) pulls back to a neighborhood of \(y\), giving the inequality \((a\circ p)^*(y)\leq a^*(p(y))\). Conversely, every neighborhood \(W\ni y\) has open image containing \(p(y)\), and

\[
\sup_{z\in W}a(p(z))=\sup_{x\in p(W)}a(x)\geq a^*(p(y)).
\]

Taking the infimum gives the reverse inequality. Homeomorphisms are a special case. Regularization also commutes with restriction to an ordinary open subset, because neighborhoods inside that subset are cofinal at its points.

For any surjective open \(p\) and usc \(f:X\to\mathbb R\cup\{-\infty\}\), the fiber infimum

\[
F(x)=\inf_{y\in p^{-1}(x)}f(y) \tag{2.2}
\]

is usc, possibly \(-\infty\): for each real \(t\),

\[
\{F<t\}=p(\{f<t\})
\]

is open. The strict inequality ensures that an infimum below \(t\) is witnessed by an actual fiber value. No minimum or lower semicontinuity is asserted. The fibers are nonempty, so \(F\) never takes \(+\infty\).

### A curve-family lemma with all scalar tests

Let \(C\) be a reduced separated strict analytic curve. If the characteristic is positive, put \(K^{\mathrm p}=\widehat{K^{1/p^\infty}}\); in characteristic zero put \(K^{\mathrm p}=K\). Let

\[
\nu:\widetilde{(C_{K^{\mathrm p}})_{\mathrm{red}}}
\longrightarrow (C_{K^{\mathrm p}})_{\mathrm{red}}
\]

be normalization. Assume \(\nu\) is bijective on underlying Berkovich points. Then the regularized supremum of any nonempty locally upper-bounded family of finite continuous classically psh functions on \(C\) is classically psh. Absolute boundary is allowed. The empty family gives \(-\infty\), also classically psh.

Here is a proof of this lemma rather than an invocation of the supplied curve result. The perfected scalar map is a homeomorphism by [GR1, Lemma 3.7]; reduction is a homeomorphism by Lemma 3.8. Normalization is finite and a topological quotient by Lemma 3.9. Its assumed bijectivity makes it a homeomorphism. Let \(t:\widetilde C\to C\) be their composite. Pullbacks of the family are classically psh by [GR1, Proposition 4.2], and

\[
\left(\sup h\circ t\right)^*=(\sup h)^*\circ t. \tag{2.3}
\]

The perfected ground field is perfect, so \(\widetilde C\) is rig-smooth by Lemma 3.9(1). Its absolute interior is a smooth strict curve. Choose a fixed member \(h_0\). Direct the finite subsets containing \(h_0\) by inclusion and take their maxima. Each maximum is finite continuous and classically psh, although it need not lie in the PL competitor class. Their supremum is still exactly the original supremum. On every sufficiently small neighborhood the maxima have a common finite upper bound and the common continuous lower bound \(h_0\circ t\). They are therefore locally bounded in the literal sense of [Thu, Proposition 3.1.8(iii)]. That proposition, and [GR1, 3.4.1], make (2.3) subharmonic on the absolute interior of \(\widetilde C\).

It is usc on the whole curve. [GR1, Proposition 3.5(3)] extends subharmonicity across its absolute boundary. Descend along the finite surjections normalization and reduction using Proposition 3.5(8), and along the perfected scalar extension using Proposition 3.5(7). The descended function is \((\sup h)^*\). It is subharmonic on \(C\), equivalently classically psh by [GR1, 4.1.2]. Those propositions use the all-extension definition, so this conclusion already includes every further analytic extension, not merely algebraic extensions or ground-field curves. In the nonempty case the regularization is finite: it lies above \(h_0\) and below a finite local upper bound.

## 3. An actual full-family projective-fiber theorem

### Products over an arbitrary good strict base

Let \(B\) be any good separated strict analytic space. Let \(Y\) be a nonempty smooth geometrically connected projective \(K\)-scheme. Set

\[
X=B\times_K Y^{\mathrm{an}},\qquad p:X\to B.
\]

Then

\[
p^*:\operatorname{SP}_{\mathbb R}(B)
\overset{\sim}{\longrightarrow}\operatorname{SP}_{\mathbb R}(X) \tag{3.1}
\]

is a bijection. In particular, for every usc obstacle \(f\) on \(X\), with \(F\) as in (2.2),

\[
\mathcal E_X(f)=p^*\mathcal E_B(F),\qquad
P_X f=(P_BF)\circ p,
\qquad (P_Xf)^*=(P_BF)^*\circ p. \tag{3.2}
\]

These are identities for global competitors on the entire displayed spaces, including empty families. No approximation, globalization assumption or torus symmetry is involved.

We verify each geometric and family step.

First, \(Y^{\mathrm{an}}\) is good, separated, strict and boundaryless by the analytification foundations, and proper by [Ber, Proposition 2.6.9]. It is smooth by Proposition 3.5.8. Its base change to \(B\) makes \(p\) proper and smooth by Proposition 3.5.2 and stability of properness. Thus \(p\) is open by Corollary 3.7.4, even at points above \(\partial B\), and is closed and surjective. Surjectivity follows because its fiber at \(x\) is

\[
p^{-1}(x)=(Y_{\mathcal H(x)})^{\mathrm{an}}, \tag{3.3}
\]

a nonempty projective analytic space. A proper analytic map here is a compact boundaryless map; on these locally compact Hausdorff spaces it is topologically closed. For completeness, near any base point restrict to a compact neighborhood. The intersection of a closed set with its compact inverse image is compact, and its image is closed in that neighborhood. This proves closedness locally and hence globally.

The fiber (3.3) is connected. Here is a checked-foundation proof, avoiding an assumption that a tensor-product fiber is an ordinary product of point sets. Put \(H=\mathcal H(x)\) and choose a prime \(\ell\). The projective scheme \(Y_H\) is connected by geometric connectedness. Its global sections of the constant étale sheaf \(\mathbb Z/\ell\mathbb Z\) form \(\mathbb Z/\ell\mathbb Z\). Properness identifies degree-zero cohomology with compactly supported degree-zero cohomology. [Ber, Theorem 7.1.1] identifies these sections with those on \((Y_H)^{\mathrm{an}}\). If that analytic space had a nontrivial clopen partition, its characteristic function would give a nonconstant section of the constant sheaf, contrary to this identification. Equivalently, a section of the finite constant sheaf is a locally constant function, as is seen from the trivial finite étale cover with \(\ell\) sheets. Thus the analytic fiber is connected. It is compact and boundaryless over \(H\).

Let \(h\in\operatorname{SP}_{\mathbb R}(X)\). It is finite continuous and classically psh by [GR1, Theorem 4.3]. Its restriction to (3.3) is classically psh: pull back first to \(X_H\), then along the natural \(H\)-analytic fiber morphism into \(X_H\). It attains a maximum on that compact fiber. The maximum set is nonempty and closed. Every point of that set lies in the absolute interior of the fiber, so [GR1, Theorem 6.1] makes the set open. Connectedness gives constancy on the entire fiber. Define \(g(x)\) to be that constant. Then \(h=g\circ p\). The closed surjection \(p\) is a quotient, so continuity of \(h\) implies continuity of \(g\). Explicitly, inverse images of closed subsets of \(\mathbb R\) under \(g\) are images under \(p\) of the corresponding closed, saturated inverse images under \(h\).

We must establish that \(g\) is an actual global base competitor. Choose a closed point of \(Y\); its residue field \(M\) is a finite extension of \(K\), complete for the extended valuation. Such a point exists by taking a maximal ideal in a nonempty affine finite-type chart and applying Zariski's lemma. It supplies an \(M\)-point of \(Y_M\) and an analytic section

\[
\sigma_M:B_M\longrightarrow B_M\times_M Y_M^{\mathrm{an}}=X_M.
\]

Restricting \(h_M\) along this section gives

\[
g\circ\pi_{M/K}=h_M\circ\sigma_M
\in\operatorname{SP}_{\mathbb R}(B_M). \tag{3.4}
\]

This is ordinary analytic pullback, not a topological section construction. Corollary 5.12 of [GJR], with \(\Lambda=\mathbb R\) and the finite field extension \(M/K\), shows that \(g\) is real PL on \(B\). Proposition 7.6(2') descends semipositivity. Thus \(g\in\operatorname{SP}_{\mathbb R}(B)\). This proof requires no \(K\)-rational point of \(Y\) and no Galois or orbit presentation. Conversely every such \(g\) pulls back to a member on \(X\), by [GJR, Lemma 5.4 and Proposition 7.6]. Surjectivity of \(p\) gives uniqueness. This proves (3.1).

For these exact families, \(g\circ p\leq f\) is equivalent to \(g\leq F\), with no attainment condition on the infimum. This proves the family and raw-envelope identities (3.2). The last identity follows from the actual geometric openness already proved and (2.1). All raw suprema are locally upper bounded by their usc obstacles. Empty families correspond under the same bijection.

### Projective bundles, without assuming a global section

There is the same conclusion (3.1)--(3.2) for \(p:\mathbb P(\mathcal V)\to B\), where \(\mathcal V\) is an analytic vector bundle of constant rank \(r\geq2\), locally free in the ordinary analytic topology. Indeed, its standard local trivializations are \(B_i\times\mathbb P_K^{r-1,\mathrm{an}}\). They show that \(p\) is a proper smooth surjection with connected compact boundaryless fibers and with local analytic coordinate sections. Properness can be checked over a base neighborhood; over a compact base set take a finite trivializing refinement and the usual finite projective affinoid charts to see compact inverse images. Relative boundarylessness and smoothness are local and are exactly those of the displayed product charts.

Fiber constancy follows as above. On each \(B_i\), restriction along one coordinate section shows that the descended function \(g|_{B_i}\) is real PL and semipositive. These restrictions agree because their values are the fiber constants. The ordinary sheaf properties in [GJR, 5.2(4) and 7.3(3)] give a single global semipositive real-PL function \(g\). Conversely pullback preserves the class. This proves the exact global family identity, even for a bundle lacking a global analytic section. Ordinary openness follows from the smoothness of \(p\), and hence so does regularization compatibility.

### The positive higher-dimensional sector

Assume that the base \(B=C\) satisfies the curve hypothesis of Section 2. Either of the actual geometric spaces just constructed has the following property:

\[
\boxed{\text{For every usc }f:X\to\mathbb R\cup\{-\infty\},
\quad (P_Xf)^*\text{ is classically psh.}} \tag{3.5}
\]

If the family is empty, this is the extended \(-\infty\) convention. Otherwise \(\mathcal E_C(F)\) is a nonempty family of finite continuous classically psh functions, locally upper bounded by the usc \(F\). Its regularized supremum is classically psh by the proved curve lemma. Equation (3.2) and analytic pullback give (3.5).

To spell out all scalar and curve tests, let \(K'/K\) be any analytic extension and let \(\gamma:D\to X_{K'}\) be any analytic curve morphism. If \(u_C=(P_CF)^*\), the pulled function is exactly

\[
(P_Xf)^*\circ\pi_{X,K'/K}\circ\gamma
=u_C\circ\pi_{C,K'/K}\circ p_{K'}\circ\gamma. \tag{3.6}
\]

The morphism \(p_{K'}\circ\gamma:D\to C_{K'}\) is analytic. The definition of classical psh for \(u_C\) makes (3.6) subharmonic, with the extended convention on each test. Thus no openness of an arbitrary scalar projection, no scalar regularization identity, and no equality of full competitor families before and after arbitrary extension is assumed.

There is nevertheless one additional exact scalar fact. For the pulled obstacle \(f\circ\pi_X\), its fiber infimum over \(p_{K'}\) equals \(F\circ\pi_C\). For \(x'\) above \(x\), every point of \(p^{-1}(x)\) has a lift in \(p_{K'}^{-1}(x')\). The lift is obtained from the nonempty Berkovich spectrum of

\[
\mathcal H(y)\widehat\otimes_{\mathcal H(x)}\mathcal H(x').
\]

This nonemptiness, and the induced simultaneous residue-field extension, are the fiber-product foundation explicitly discussed in [GR1, 2.8]. Hence the sets of obstacle values occurring in those two fibers are equal, so their infima are equal. This fact does not identify the larger base competitor family over \(K'\) with the pullbacks of the ground-field family.

Absolute boundary has not been removed. Since \(p\) is boundaryless relative to the separated good base, the boundary formula of [GR1, 2.11] gives

\[
\partial X=p^{-1}(\partial C).
\]

The normalized-curve argument handled \(\partial C\) before descent. Fiberwise constancy used the absolute boundarylessness of the projective fiber over \(\mathcal H(x)\), which holds even if \(x\in\partial C\).

## 4. Concrete normal and geometrically unibranch examples

For a concrete normal sector, take \(C\) to be any good strict analytic domain in the analytification of a smooth separated algebraic \(K\)-curve, and take \(Y\) as in Section 3 with positive dimension. The space \(C\times Y^{\mathrm{an}}\) is an analytic domain in the smooth algebraic analytification of the product. Algebraic smoothness gives regular local rings; [Ber, Corollaries 2.2.7--2.2.8] give regularity of its analytic local rings and affinoid domains. Thus the product is normal. The same argument after every analytic field extension makes \(C\) rig-smooth and normal after extension, so in particular it satisfies Section 2's normalization hypothesis. Its dimension is \(1+\dim Y\). Closed strict discs and strict annuli are included. Analytic projective bundles over such a \(C\) are likewise normal, since locally they are analytic domains in smooth algebraic products. These statements establish geometry of the displayed sectors; they are not abstract realization assumptions.

There are also nonnormal geometrically unibranch examples. Over \(K=\mathbb Q_3\), let

\[
C=\mathcal M\bigl(K\langle u,v\rangle/(v^2-u^3)\bigr),
\qquad \nu:\mathcal M(K\langle T\rangle)\to C,
\quad (u,v)=(T^2,T^3).
\]

The algebra maps injectively to \(K\langle T\rangle\): the expansion \(a(u)+v b(u)\) maps to disjoint even and odd powers, the odd powers starting at degree three. Its image consists of convergent series whose coefficient of \(T\) is zero. Adjoining \(T\), integral because \(T^2=u\), gives the Tate algebra, finite over the cusp algebra; in the fraction field \(T=v/u\). The Tate algebra is normal, so this is the normalization. Away from \(u=0\) the map is an isomorphism. Over \(u=v=0\) its only point is \(T=0\), with the same residue field. These computations hold after every field extension. Thus normalization is universally bijective on points and the cusp has one geometric analytic branch, although it is not normal at the origin.

For every \(Y\) in Section 3, the normalization of \(C\times Y^{\mathrm{an}}\) is the finite birational map from the normal space \(\mathcal M(K\langle T\rangle)\times Y^{\mathrm{an}}\). Normality upstairs follows from the preceding regular-domain argument. At any point over the cusp origin, the normalization fiber algebra over its completed residue field is \(H[T]/(T^2,T^3)\), whose underlying analytic point set is a singleton; outside that section the map is an isomorphism. The same computation after arbitrary residue-field extension gives one branch. Hence this is an actual geometrically unibranch nonnormal higher-dimensional sector satisfying (3.5), for arbitrary noninvariant usc obstacles.

## 5. Split branches and a codimension-two pinching

Fix \(0<|\varpi|<1\), put \(a=-\log|\varpi|>0\), and for \(d\geq1\) set

\[
A_d=K\langle X_1,\ldots,X_d,Y_1,\ldots,Y_d\rangle/
(X_iY_j:1\leq i,j\leq d),\qquad W_d=\mathcal M(A_d).
\]

This is the actual gluing of two closed strict \(d\)-polydiscs along their origins. Indeed,

\[
A_d\simeq K\langle X_1,\ldots,X_d\rangle
\times_K K\langle Y_1,\ldots,Y_d\rangle, \tag{5.1}
\]

where the maps to \(K\) evaluate at the origin. A power series modulo the cross terms has precisely one constant term, an \(X\)-series without constant term, and a \(Y\)-series without constant term. This proves (5.1) and reducedness. The two components have dimension \(d\), so \(W_d\) is pure dimensional. Its normalization is the direct product of the two Tate algebras, finite by adjoining the idempotent \((1,0)\). Outside the common origin \(o\), one of the coordinates has nonzero absolute value and the other component disappears; there the map is an isomorphism and the space is normal.

The ring is seminormal. Here is an algebraic verification rather than a label. For any element \(b\) of the total ring of fractions with \(b^2,b^3\in A_d\), its two component coordinates are integral over the respective normal Tate algebras, hence belong to them. Let their constant terms be \(\alpha,\beta\in K\). Membership of \(b^2,b^3\) in (5.1) gives \(\alpha^2=\beta^2\) and \(\alpha^3=\beta^3\). If either is zero they both are; otherwise their ratio has both square and cube equal to one, and is one. Thus \(\alpha=\beta\), so \(b\in A_d\). This proves the square-and-cube characterization of seminormality in this example. One can also verify the defining subintegral-extension condition directly: any subintegral intermediate ring between \(A_d\) and its normalization has a single prime over the origin with residue field \(K\). Its two evaluation maps into \(K\) must then agree. Every one of its elements has equal constant terms on the two components, so belongs to \(A_d\); the intermediate ring is \(A_d\) itself. Every integral birational subextension lies in the normalization, so this rules out a proper subintegral one.

This verification also holds for analytic local rings. Outside \(o\) the space is normal. At \(o\) the analytic germ ring is the fiber product, over the common residue field \(K\), of the two regular polydisc germ rings. Indeed, arbitrarily small closed polydiscs about the rational origin form a neighborhood basis, and their rings have exactly the description (5.1); taking germs preserves that description. The preceding equal-constant-term argument applies verbatim to those normal germ rings. In particular \(d=2\) is a seminormal two-bidisc point pinching, normal at every point outside a codimension-two locus consisting of \(o\). It is not geometrically unibranch there. This construction need not be identified with the supplied book's particular pinching example.

Define the finite continuous obstacle and rational LFS functions on \(W_d\) by

\[
\begin{split}
f&=-a\max_j |Y_j|,\\
h_n&=\frac1n\log\max\{|\varpi|^n,|X_1|,\ldots,|X_d|\},
\qquad n\geq1.
\end{split} \tag{5.2}
\]

The local presentation in Section 1 proves that every \(h_n\) is finite rational LFS, including at \(o\), where it is constant on a neighborhood. On the \(X\)-component, \(h_n\leq0=f\). On the \(Y\)-component, \(h_n=-a\leq f\). Thus these are global members of the exact family, and the constant \(-a\) is also a member.

Conversely, take any member \(h\) of the full union. By Section 1 it is classically psh. Its restriction to the \(Y\)-polydisc is classically psh. That polydisc has singleton Shilov boundary, the Gauss point \(\eta\), because the Gauss norm dominates evaluation of every Tate series and is itself multiplicative. At \(\eta\), all \(|Y_j|=1\), so \(h(\eta)\leq f(\eta)=-a\). The affinoid maximum principle [GR1, Theorem 6.4] therefore gives \(h\leq-a\) throughout this component, including \(o\). This bounds every competitor, not only the displayed sequence.

At every point of the \(X\)-component other than \(o\), at least one \(|X_i|\) is positive, and (5.2) increases to zero. The obstacle is zero there. Consequently the exact raw envelope is

\[
P_{W_d}f=
\begin{cases}
0&\text{on the punctured }X\text{-component},\\
-a&\text{on the }Y\text{-component, including }o.
\end{cases} \tag{5.3}
\]

The regularization is zero at \(o\): points of the punctured \(X\)-component approach it, and \(f(o)=0\) gives the reverse upper bound. It stays \(-a\) at every other \(Y\)-point, since a nonzero \(Y_j\) supplies a neighborhood avoiding the \(X\)-component. Pull back along the analytic closed-disc axis \(Y_1=T\), with other coordinates zero. The value at \(T=0\) is zero, while its singleton Shilov value is \(-a\). It fails the affinoid maximum principle and hence is not classically psh. For \(d=1\) this is the split-node obstruction; for \(d=2\) it proves that even seminormality and normality off a codimension-two point are insufficient.

Moreover, for any projective factor \(Y\) of Section 3, exact descent (3.2) applies to the pullback of this obstacle on \(W_d\times Y^{\mathrm{an}}\), since that descent theorem did not assume a curve base. The regularized envelope is the pullback of (5.3)'s regularization. After one finite extension giving a point of \(Y\), the same disc axis times that point fails the scalar curve test. This proves persistence with proper projective factors without comparing a smaller family.

### A single irreducible bidisc with two points pinched

The codimension-two obstruction can also be realized irreducibly. Let

\[
B=K\langle T,Z\rangle,\quad P=(0,0),\quad Q=(1,0),\quad
A=\{g\in B:g(P)=g(Q)\},\quad W=\mathcal M(A).
\]

We first prove that this is an actual strict affinoid space and its indicated geometry. Put \(U=T(T-1)\) and \(R_0=K\langle U,Z\rangle\). Reduction by \(T^2=T+U\) gives

\[
B=R_0\oplus T R_0,\qquad
A=R_0\oplus T(U,Z)R_0. \tag{5.4}
\]

Here the analytic decomposition can be checked directly. Reduce each power \(T^m\) to \(a_m(U)+Tc_m(U)\) using the recurrence \((a_{m+1},c_{m+1})=(Uc_m,a_m+c_m)\), starting from \((a_0,c_0)=(1,0)\). The polynomials have integer coefficients and Gauss norms at most one. Applying these bounded operations termwise to a convergent Tate series gives convergent series \(a,c\in R_0\). Substitution \(U=T(T-1)\) embeds \(R_0\) isometrically in \(B\): after scaling a coefficient of maximal norm to one, the nonzero reduction polynomial in \(U,Z\) remains nonzero on substitution \(U=T^2-T\), since \(T^2-T\) and \(Z\) are algebraically independent. If \(a(U,Z)+Tc(U,Z)=0\), substitute \(1-T\) for \(T\), which preserves \(U\), and subtract. This gives \((2T-1)c(U,Z)=0\) in the domain \(B\), hence \(c=0\), then \(a=0\), including in characteristic two. This proves the bounded unique decomposition.

An element \(a(U,Z)+Tc(U,Z)\) has values \(a(0,0)\) and \(a(0,0)+c(0,0)\) at \(P,Q\). Therefore it belongs to \(A\) exactly when \(c\in(U,Z)\). The description shows that \(A\) is a finite \(R_0\)-module and an algebra generated over \(R_0\) by \(TU,TZ\). More concretely, the bounded homomorphism from \(K\langle U,Z,V,R\rangle\) into \(B\), with \(V=TU\), \(R=TZ\), has image exactly \(A\). To obtain surjectivity, write \(c=Uc_1+Zc_2\) by separating the convergent monomials divisible by \(U\) from the remaining monomials, divisible by \(Z\). Then \(a+Tc=a+Vc_1+Rc_2\). These bounded decompositions give a bounded linear right inverse of the surjection onto the closed subspace \(A\). Its quotient and subspace norms are therefore equivalent. Thus \(A\) is a strict affinoid quotient of this Tate algebra. It is a domain as a subring of \(B\), so \(W\) is reduced and irreducible.

Adjoining \(T\) to \(A\) gives \(B\); it is integral by \(T^2-T-U=0\) and birational because \(T=(TU)/U\) in the fraction field. The regular bidisc algebra \(B\) is normal, so this finite map

\[
\nu:\mathcal M(B)\longrightarrow W
\]

is the normalization. Its conductor is \(I=(U,Z)B\). It consists of the functions vanishing at both \(P,Q\); it is contained in \(A\). Conversely a conductor element must vanish at both: multiply it by \(T\) and \(1-T\) and use the equal-value condition. The quotient rings are

\[
B/I\simeq K\times K,\qquad A/I\simeq K.
\]

Thus exactly \(P\) and \(Q\) are identified to a rational point \(\xi\). Outside \(\xi\), the conductor becomes the unit ideal locally, so normalization is an isomorphism. Both points upstairs have codimension two in the bidisc; the finite integral domain \(A\) has dimension two, and \(\xi\) has codimension two. The space is normal everywhere else.

It is seminormal, including as an analytic space. An integral birational subextension lies in \(B\). If it is subintegral, its two evaluations into \(K\) over \(\xi\) must coincide, since its prime and residue field there are unique and equal to those of \(A\). Every element then satisfies \(g(P)=g(Q)\), so the subextension is \(A\). For analytic germs the same argument applies: the finite coherent-module sequence

\[
0\longrightarrow A\longrightarrow B
\overset{g\mapsto g(Q)-g(P)}{\longrightarrow}K_\xi\longrightarrow0
\]

has kernel exactly (5.4). The finite-module/coherent-sheaf correspondence on good affinoids, checked in [Ber, 1.3 and Proposition 1.3.4], makes the germ at \(\xi\) the fiber product over \(K\) of the two normal bidisc germ rings at \(P,Q\). The quotient is a skyscraper at \(\xi\), and the finite normalization pushforward has precisely those two germ factors. The equal-residue-value argument proves the absence of a proper subintegral extension of this germ. Outside it the germs are normal. This proves seminormality of the actual space, rather than only of a proposed realization algebra.

Set \(\rho=|\varpi|\) and define the continuous function on \([0,1]\)

\[
\phi(r)=
\begin{cases}
-a r/\rho&0\leq r\leq\rho,\\
\log r&\rho\leq r\leq1.
\end{cases}
\]

The two expressions agree at \(\rho\), and \(\phi(0)=\phi(1)=0\). The continuous obstacle \(\widetilde f=\phi(|T-1|)\) on the normalization has equal values zero at \(P,Q\). Every other normalization fiber is a singleton. Since the finite normalization is a closed quotient, \(\widetilde f\) descends to a finite continuous obstacle \(f\) on \(W\).

The polynomials \(F_n=T(T-1)^n\) belong to \(A\), because they vanish at both \(P,Q\). Consequently

\[
h_n=\frac1n\log\max\{\rho^n,|F_n|\},\qquad n\geq1, \tag{5.5}
\]

are global rational LFS functions on \(W\), by the precise local presentation in Section 1. On the normalization, \(|T|\leq1\), so

\[
h_n\circ\nu\leq\max\{-a,\log|T-1|\}
\leq\phi(|T-1|)=f\circ\nu.
\]

The last inequality uses \(-a\leq-a r/\rho\) for \(r\leq\rho\), and equality to \(\log r\) for \(r\geq\rho\). Thus each \(h_n\) is a genuine global minorant; the constant \(-a\) is one too.

Consider the bad closed-disc map into the normalization \((T,Z)=(1+\varpi S,0)\), followed by \(\nu\). Its origin maps to \(\xi\), and at its Gauss point \(|T-1|=\rho\), so \(f=-a\). Every full-family competitor pulls back to a classically psh function on this disc. The singleton-Shilov maximum principle gives \(h(\xi)\leq-a\). The baseline attains this, so \(P_Wf(\xi)=-a\).

On the good disc \((T,Z)=(\varpi S,0)\), each nonzero-radius point has \(|T-1|=1\), hence \(f=0\), and (5.5) has supremum zero because \(|F_n|=|T|>0\). The exact raw envelope is therefore zero at these points, which approach \(\xi\). Its regularization equals zero at \(\xi\), while its value at the bad disc's Gauss point is at most \(-a\), since an usc envelope regularization remains below the continuous obstacle. The bad disc again violates the Shilov maximum principle. This proves a full-family failure on an actual irreducible, seminormal, strict analytic surface normal away from one codimension-two point. The construction is not asserted to be the exact supplied book example; its geometry and envelope obstruction have been proved independently.

## 6. An irreducible nonsplit-node surface: an explicit obstruction

The pointwise bijectivity of normalization on a ground-field curve is not a substitute stable under adding an open analytic factor. The following construction proves this in actual geometry, with a global continuous obstacle and explicit rational LFS competitors.

Take \(K=\mathbb Q_3\), let \(\rho=|3|=1/3\), let \(b=-\log\rho>0\), and put \(L=K(\alpha)\) with \(\alpha^2=2\). The polynomial is irreducible because a square unit in \(\mathbb Q_3\) has square residue modulo 3, whereas 2 is not a square in \(\mathbb F_3\); in particular \([L:K]=2\) and \(|\alpha|=1\). Put

\[
C=\mathcal M\bigl(K\langle X,Y\rangle/(X^2-2Y^2)\bigr),
\qquad D=\{z\in\mathbb A_K^{1,\mathrm{an}}:|Z(z)|<1\},
\qquad X_0=C\times_K D.
\]

The symbol \(X\) in the equations is a coordinate; the surface is named \(X_0\).

### Geometry and normalization

The curve algebra injects into \(L\langle T\rangle\) by \(Y=T\), \(X=\alpha T\). Its image consists of the series with constant coefficient in \(K\) and arbitrary coefficients in \(L\) in positive degree. To see this, divide by the monic quadratic relation in \(X\): every element is \(a(Y)+Xc(Y)\), whose images have coefficients \(a_m+\alpha c_{m-1}\) in degree \(m\geq1\), and a constant coefficient in \(K\). The two summands give independent \(K\)-components because \(2\) is nonsquare in \(\mathbb Q_3\). Thus the algebra is an integral domain. Adjoining \(\alpha\), integral by \(\alpha^2=2\) and belonging to the fraction field as \(X/Y\), gives \(L\langle T\rangle\), which is normal. This is a finite birational normalization.

If \(|Y|>0\), the inverse is \(\alpha=X/Y\), so normalization is an isomorphism. If \(|Y|=0\), also \(|X|=0\), and the unique normalization point is \(T=0\); \(\mathcal M(L)\) has one point over \(\mathcal M(K)\). Thus every ground-field Berkovich normalization fiber is a singleton. After scalar extension to \(L\), the equation splits into the two branches \(X=\pm\alpha Y\). On the product surface, the nodal point with \(Z^2-18=0\) has completed residue field \(L\); its normalization fiber is already \(\mathcal M(L\otimes_K L)=\mathcal M(L\times L)\), with two points. This directly explains why pointwise bijectivity on the original curve is not product stable.

The surface is reduced and irreducible, good, separated and strict, of dimension two. One can check irreducibility without confusing it with geometric irreducibility: on every closed-disc chart in \(D\), its algebra is the subalgebra of the integral polydisc algebra \(L\langle T,r^{-1}Z\rangle\) whose constant coefficient in \(T\) belongs to \(K\langle r^{-1}Z\rangle\). It is a domain. These nested charts have nonempty relative interiors and cover \(D\); their unique irreducible components therefore form one analytic irreducible component. Equivalently, the finite normalization

\[
\mathcal M(L\langle T\rangle)\times_K D\longrightarrow X_0
\]

is birational and its source is a connected normal polydisc domain over \(L\), hence irreducible. For a strictly analytic exhaustion over the discretely valued field, one may take \(|Z|^m\leq|3|\), \(m\geq1\); its algebras have the extra presentation variable \(W\) with \(Z^m=3W\). They are the stated radius-\(\rho^{1/m}\) disc algebras. No analytic radius outside the strict category is being silently added.

### A global continuous obstacle

For a point of \(X_0\), set \(r=|Y|\) and \(G=3X-ZY\). Define

\[
\eta(r)=\min\left\{1,\max\left\{0,\frac{r-\rho}{1-\rho}\right\}\right\},
\qquad \chi(R)=\max\{0,1-R/\rho\},
\]

and define the obstacle

\[
f=
\begin{cases}
-3b\,\eta(r)\,\chi\left(\dfrac{|G|}{\rho r}\right)&r>0,\\
0&r=0.
\end{cases} \tag{6.1}
\]

It is real valued and continuous, with \(-3b\leq f\leq0\). Indeed, the ratio is continuous where \(r>0\), while \(\eta\) vanishes on \(r\leq\rho\), giving an entire neighborhood on which the formula is zero near \(r=0\).

### Rational LFS minorants

Put

\[
\delta=Z^2/18-1,\qquad
c_j=\binom{-1/2}{j},\qquad
P_n(t)=\sum_{j=0}^{n-1}c_jt^j,
\]

\[
A_n(Z)=(Z/3)P_n(\delta),\qquad
F_n=X-A_n(Z)Y,\qquad
h_n=\frac1n\log\max\{|3|^{3n},|3^{2n}F_n|\}. \tag{6.2}
\]

These are global polynomials inside the log maximum; the Section 1 presentation proves that \(h_n\) is rational LFS. The coefficient identity

\[
c_j=(-1)^j\binom{2j}{j}/4^j
\]

gives \(|c_j|_3\leq1\). On the whole open disc, \(|Z|<1\) and \(|\delta|\leq\rho^{-2}\), so

\[
|A_n|\leq\rho^{-(2n-1)},\quad
|F_n|\leq\rho^{-(2n-1)},\quad
|3^{2n}F_n|\leq\rho.
\]

Here \(|X|,|Y|\leq1\) comes from the closed node curve. Therefore \(-3b\leq h_n\leq0\) everywhere.

We next prove the stronger local bound exactly where (6.1) is negative. At such a point, \(r>\rho\) and \(R=|G|/(\rho r)<\rho\). Inside its completed residue field put \(t=X/Y\); then \(t^2=2\), \(|t|=1\), and

\[
w=Z/(3t),\qquad |w-1|=R<\rho,
\qquad \delta=w^2-1,\qquad |\delta|<\rho.
\]

The binomial series \(B(\delta)=\sum_{j\geq0}c_j\delta^j\) converges in that complete field. The formal binomial identity gives \((1+\delta)B(\delta)^2=1\). Both \(w\) and \(B(\delta)\) are within absolute distance less than one of 1, so \(wB(\delta)\) is the root \(+1\), not \(-1\), of its square-one equation. Indeed \(|2|_3=1\). Thus \(B(\delta)=w^{-1}\) and

\[
|A_n-t|=|tw(P_n(\delta)-B(\delta))|
\leq |\delta|^n\leq\rho^n.
\]

It follows that \(|F_n|\leq\rho^n|Y|\leq\rho^n\), hence \(|3^{2n}F_n|\leq\rho^{3n}\) and \(h_n=-3b\). Where \(f<0\), therefore, \(h_n=-3b\leq f\); elsewhere \(f=0\) and the global bound applies. Every \(h_n\) is a member of the full obstacle family. In particular the family is nonempty.

### Exact values needed to force a scalar curve failure

Over the actual extension \(L/K\), consider the two analytic closed-disc maps

\[
\gamma_\pm:\mathcal M(L\langle T\rangle)\to (X_0)_L,
\qquad (X,Y,Z)=(\pm\alpha T,T,3\alpha).
\]

They are legitimate maps into the open factor since \(|3\alpha|=\rho<1\). Let \(\xi\in X_0\) be the common ground-field image of \(T=0\). Its \(Z\)-coordinate is the closed quadratic point defined by \(Z^2-18=0\), with completed residue field \(L\).

At the Gauss point on the plus disc, \(r=1\), \(G=0\), and \(f=-3b\). Every competitor \(h\) is classically psh, so its scalar pullback along \(\gamma_+\) obeys the singleton-Shilov maximum principle. Hence \(h(\xi)\leq-3b\). The functions (6.2) equal \(-3b\) at \(\xi\), proving the exact raw value \(s(\xi)=-3b\), where \(s=P_{X_0}f\).

On the minus disc \(\delta=0\), \(A_n=\alpha\), and \(F_n=-2\alpha T\). Since \(|2\alpha|=1\), for every point with \(|T|>0\),

\[
h_n\circ\gamma_-=
\max\{-3b,-2b+n^{-1}\log|T|\},
\qquad \sup_n h_n\circ\gamma_-=-2b. \tag{6.3}
\]

Points of this disc with positive radius approach its origin and project continuously to \(\xi\). Thus \(s^*(\xi)\geq-2b\). For every point, \(s^*\leq f\), because the obstacle is an usc majorant of \(s\). In particular the value of \(s^*\) at the projected Gauss point of the plus disc is at most \(-3b\).

Consequently the scalar curve pullback \(s^*\circ\pi_{L/K}\circ\gamma_+\) has value at least \(-2b\) at its origin and at most \(-3b\) at its singleton Shilov point. It violates the affinoid maximum principle. The regularized envelope is not classically psh. Every upper bound used here applies to the entire competitor union, and every displayed lower bound is realized by genuine global rational LFS minorants. This is not a topological defect datum or a selected invariant envelope.

## 7. Exact scope and remaining gaps

The positive result covers arbitrary obstacles and all noninvariant competitors on the actual normal products and projective bundles of Sections 3--4, and the displayed geometrically unibranch nonnormal cusp products. It includes relative boundary and every analytic scalar extension. Proper connected fibers force the entire competitor class to descend, which is why no local-to-global minorant construction is missing in this sector.

The negative results prove failure for split branches in every dimension, for a seminormal codimension-two point gluing and an irreducible bidisc point pinching, and on an irreducible nonsplit-node surface. In the nonsplit curve alone the normalization is pointwise bijective; adding a proper projective factor falls under Section 3's positive theorem, while adding the displayed open disc admits the explicit negative obstacle. The nature of the added factor therefore matters.

No theorem here proves positivity on an arbitrary normal higher-dimensional affinoid or an arbitrary geometrically unibranch higher-dimensional domain. No characterization of which other projective or proper morphisms permit descent of the exact real-PL family is proved. For general scalar maps we have not established full competitor cofinality, scalar regularization compatibility, or removability of any defect. No necessary-and-sufficient higher-dimensional geometric hypothesis has been obtained. The original sharp-classification completion criterion is unresolved, and the candidate flag is false.

## 8. Reproduction and evidence

All writes are confined to this fresh workspace. The supplied input bytes are retained as `input.json` and `input-original.json`; the supplied task and assignment are also retained as `task-original.json` and `assignment-original.txt`. The public cache files are read only. `prepare_sources.py` retains exact selected primary pages and PDF images in `source-extracts`, with checked applications and byte provenance in `source-provenance.json`. `build_artifacts.py` converts this entire argument into the standalone `P03.1-paper.tex`, runs the available TeX engine twice, and records commands and diagnostics in `execution.json` and `build-pass-1.txt` / `build-pass-2.txt`. The generated TeX embeds the whole proof and does not depend on a hidden argument file. `check_artifacts.py` checks required status keys, local note supports, preserved input bytes, and source-selection records.

Rerun these commands sequentially from this directory:

* `python prepare_sources.py`
* `python build_artifacts.py`
* `python make_notes.py`
* `python check_artifacts.py`

Actual command results are recorded in the execution files. Compilation, hashes, and these administrative checks are execution evidence; they are not mathematical proof certificates. No heavy computation, network request, installation, runtime alteration, external message, or additional model invocation is used.


# All actual native canonical notes

[
  {
    "id": "n1",
    "summary": "Proved full-family classical positivity for every usc obstacle on curve bases with perfected bijective normalization, multiplied by smooth geometrically connected projective factors, and on analytic projective bundles over those curves. Global competitor descent, relative boundary and all scalar curve tests are covered. This is a sufficient geometric sector, not the sharp higher-dimensional classification.",
    "detailedSummary": "The checked GJR definitions identify the exact LFS/semipositive-real-PL union with the full semipositive real-PL class. Every competitor is constant on a connected compact boundaryless projective fiber. A finite extension constructed from an algebraic closed point supplies an analytic section, and published finite real-PL and semipositivity descent recovers a global base competitor without requiring a ground-field point. Projective bundles instead use local sections and ordinary sheaf gluing. Smoothness proves ordinary openness of projection, giving exact fiber-infimum obstacle reduction and regularization compatibility. A fresh curve-family argument uses anchored finite maxima on the interior of the perfected normalization, followed by boundary extension and finite/scalar descent. Concrete normal analytic domains and geometrically unibranch nonnormal cusp products are verified. No positivity theorem for arbitrary normal higher-dimensional affinoids or sharp necessary-and-sufficient classification follows.",
    "text": "This note proves a sufficient sector for P03.1, using checked published foundations and complete new applications. Let \\(K\\) be complete and nontrivially valued. Spaces carrying PL functions are good, separated and strictly analytic. Write \\(\\operatorname{SP}_{\\mathbb R}(W)\\) for finite semipositive real-PL functions, and let \\(P_Wf\\) be the raw envelope over the exact locally Fubini–Study/semipositive-real-PL union.\n\nThe primary definitions matter. Gubler–Jell–Rabinoff, arXiv:2111.05741, Definition 5.1 makes real-PL functions finite and continuous. Definitions 7.2 and 7.8 define semipositivity by nef residues and LFS by semiample residues. Therefore LFS is already a subclass of semipositive real PL, and the literal union is exactly \\(\\mathcal E_W(f)=\\{h\\in\\operatorname{SP}_{\\mathbb R}(W):h\\le f\\}\\). Gubler–Rabinoff, arXiv:2506.13548v2, Theorem 4.3 identifies this class with real-PL functions that are classically psh. Its Definition 4.1 requires curve pullbacks after every analytic field extension. These statements apply over a nontrivially valued field on good strict spaces.\n\nThe precise local LFS presentation used below is GJR 7.9: nonnegative combinations of maxima of negative logs of analytic units, with the real-PL requirement. In particular, for analytic \\(F_1,\\ldots,F_r\\), \\(c\\in K^\\times\\), and integer \\(n\\ge1\\),\n\\[H=\\frac1n\\log\\max\\{|c|,|F_1|,\\ldots,|F_r|\\}\\]\nis rational PL and LFS. Near any point, discard functions vanishing there because their norms become smaller than \\(|c|\\); retained functions become units. Rational dominance domains give a strict G-cover on which \\(H\\) is one unit log divided by \\(n\\). On the ordinary open neighborhood its presentation is \\(n^{-1}\\max(-\\log|c^{-1}|,-\\log|F_j^{-1}|)\\), with positive coefficient and units. Constants are also LFS. This argument does not assume closure of arbitrary real-PL functions under maxima.\n\nWe first prove the curve input. Let \\(C\\) be a reduced separated strict analytic curve. In positive characteristic let \\(K^{\\mathrm p}=\\widehat{K^{1/p^\\infty}}\\); otherwise let \\(K^{\\mathrm p}=K\\). Assume normalization of \\((C_{K^{\\mathrm p}})_{\\mathrm{red}}\\) is bijective on Berkovich points. The regularized supremum of every nonempty locally upper-bounded family of finite continuous classically psh functions on \\(C\\) is classically psh, with absolute boundary allowed.\n\nHere is the proof. GR Lemmas 3.7–3.9 say that perfected scalar extension and reduction are homeomorphisms, that normalization is finite and a topological quotient, and that the normalized curve over the perfect field is rig-smooth. The assumed bijectivity makes normalization a homeomorphism. Their composite \\(t:\\widetilde C\\to C\\) is thus a homeomorphism, and regularization commutes with pullback along it. All family members pull back to classically psh functions. Choose one finite continuous member \\(h_0\\), and direct finite subsets containing it by inclusion. Their finite maxima are continuous psh functions with the same supremum as the original family. They need not be PL competitors, and no such assertion is needed. On every sufficiently small neighborhood they are bounded above uniformly and bounded below by \\(h_0\\circ t\\).\n\nOn \\(\\operatorname{Int}(\\widetilde C)\\), a smooth strict curve, Thuillier's thesis, Proposition 3.1.8(iii), makes the usc regularized supremum subharmonic. The original PDF says increasing and locally bounded; the anchored maxima satisfy both upper and lower local bounds. GR 3.4.1 identifies this with its extended subharmonic convention. The function is usc on the whole normalized curve, so GR Proposition 3.5(3) extends subharmonicity across absolute boundary. Descend through normalization and reduction by finite-surjective descent, Proposition 3.5(8), then through perfected scalar extension by Proposition 3.5(7). The descended function is the original regularized supremum. On a curve, GR 4.1.2 identifies subharmonicity with classical pshness. These propositions use the all-extension definitions, so further analytic scalar extensions are included. The empty family gives identically \\(-\\infty\\), permitted by Definition 3.4. No supplied book curve theorem is used.\n\nNow let \\(B\\) be any good separated strict base and let \\(Y\\) be a nonempty smooth geometrically connected projective \\(K\\)-scheme. Put \\(X=B\\times_KY^{\\mathrm{an}}\\) and let \\(p:X\\to B\\). We prove the exact global bijection\n\\[p^*:\\operatorname{SP}_{\\mathbb R}(B)\\xrightarrow{\\sim}\\operatorname{SP}_{\\mathbb R}(X).\\]\nBerkovich, IHÉS 78 (1993), Propositions 2.6.1, 2.6.9 and 3.5.8 establish boundaryless analytification, projective properness and smoothness; Proposition 3.5.2 preserves smoothness under base change. Thus \\(p\\) is proper and smooth, and Corollary 3.7.4 makes it an ordinary open map, including above absolute-boundary base points. Its fiber at \\(x\\) is \\((Y_{\\mathcal H(x)})^{\\mathrm{an}}\\), nonempty, compact and boundaryless over \\(\\mathcal H(x)\\).\n\nThe fiber is connected, as follows from an exact checked primary statement. Berkovich Theorem 7.1.1 compares compactly supported étale cohomology for a compactifiable scheme and its analytification. Apply degree zero to the proper connected scheme \\(Y_{\\mathcal H(x)}\\) and a finite constant sheaf \\(\\mathbb Z/\\ell\\mathbb Z\\). Properness identifies compactly supported and ordinary sections, whose group downstairs is \\(\\mathbb Z/\\ell\\mathbb Z\\). A nontrivial clopen partition of the analytic fiber would give a nonconstant section upstairs, contradicting the comparison. Hence the fiber is connected.\n\nFor any \\(h\\in\\operatorname{SP}_{\\mathbb R}(X)\\), pull back to \\(X_{\\mathcal H(x)}\\) and restrict along the analytic fiber morphism. GR Proposition 4.2 makes this restriction classically psh. Its finite continuous maximum exists on the compact fiber. The maximum set is nonempty and closed; the fiber is boundaryless, so GR Theorem 6.1 makes it open. Connectedness forces constancy. Thus \\(h=g\\circ p\\) for a unique finite function \\(g\\). A proper map between these locally compact Hausdorff spaces is closed: restrict a closed set to inverse images of compact base neighborhoods and use compactness. Consequently \\(p\\) is a quotient and \\(g\\) is continuous.\n\nIt remains to recover an actual global base competitor. Choose an algebraic closed point of \\(Y\\) in a nonempty affine chart. Zariski's lemma gives a finite residue extension \\(M/K\\), complete for the extended valuation, and an \\(M\\)-point of \\(Y_M\\). This constructs an analytic section \\(\\sigma_M:B_M\\to X_M\\). Then\n\\[g\\circ\\pi_{M/K}=h_M\\circ\\sigma_M\\in\\operatorname{SP}_{\\mathbb R}(B_M).\\]\nGJR Corollary 5.12, with divisible coefficient group \\(\\mathbb R\\), descends real-PLness along this finite scalar extension. Proposition 7.6(2') descends semipositivity. Thus \\(g\\) is a global member on \\(B\\). Conversely pullback preserves the class by GJR Lemma 5.4 and Proposition 7.6. This proves the bijection without a ground-field rational point, Galois action, section palette or globalization assumption.\n\nFor any usc obstacle \\(f\\) on \\(X\\), define \\(F(x)=\\inf_{p(y)=x}f(y)\\). This takes values in \\(\\mathbb R\\cup\\{-\\infty\\}\\), and is usc because \\(\\{F<a\\}=p(\\{f<a\\})\\) is open. The competitor bijection gives\n\\[\\mathcal E_X(f)=p^*\\mathcal E_B(F),\\qquad P_Xf=(P_BF)\\circ p.\\]\nThese identities include empty families. For a continuous open surjection and any locally upper-bounded raw function \\(a\\),\n\\[(a\\circ p)^*=a^*\\circ p.\\]\nOne inequality follows by pulling back base neighborhoods. For the other, every neighborhood \\(W\\ni y\\) has open image containing \\(p(y)\\), and \\(\\sup_Wa\\circ p=\\sup_{p(W)}a\\ge a^*(p(y))\\). Hence\n\\[(P_Xf)^*=(P_BF)^*\\circ p.\\]\nEvery bound and identity concerns the complete competitor family.\n\nThe same conclusions hold for analytic projective bundles \\(p:\\mathbb P(\\mathcal V)\\to B\\), where \\(\\mathcal V\\) is an ordinary locally free analytic vector bundle of constant rank at least two. Local trivializations are products with projective space and prove properness, smoothness, openness and connected boundaryless fibers. Fiber constancy again gives \\(h=g\\circ p\\). Restriction along a coordinate section on each trivializing base open proves that \\(g\\) is semipositive real PL there. GJR's ordinary sheaf properties glue these agreeing restrictions to one global competitor. No global section is assumed.\n\nTake \\(B=C\\) satisfying the proved curve hypothesis. For a nonempty family the base competitors are finite continuous psh functions locally upper bounded by the usc \\(F\\). The curve lemma makes \\(u_C=(P_CF)^*\\) classically psh. The identities above prove \\((P_Xf)^*=u_C\\circ p\\). Explicitly, for every analytic extension \\(K'/K\\) and every curve morphism \\(\\gamma:D\\to X_{K'}\\), its pullback is\n\\[u_C\\circ\\pi_{C,K'/K}\\circ p_{K'}\\circ\\gamma,\\]\nwhich is subharmonic by the classical definition for \\(u_C\\). This verifies all scalar curve tests without assuming openness of arbitrary scalar projections or identifying upstairs competitor families. The obstacle fiber infimum itself does commute with scalar extension: every ground fiber point has a lift over any chosen scalar base point, using the nonempty spectrum of \\(\\mathcal H(y)\\widehat\\otimes_{\\mathcal H(x)}\\mathcal H(x')\\), the checked fiber-product foundation in GR 2.8. Thus the sets of obstacle values in those fibers agree. This does not prove full competitor base-change compatibility.\n\nRelative boundary is included. Projection is boundaryless relative to the separated good curve, so the GR 2.11 boundary formula gives \\(\\partial X=p^{-1}(\\partial C)\\). The curve proof handled base boundary before descent. Projective fiber constancy used boundarylessness over its own completed residue field even above such base points.\n\nThese hypotheses have concrete normal realizations. Take \\(C\\) to be a good strict analytic domain in a smooth separated algebraic curve and \\(Y\\) as above. The product is an analytic domain in a smooth algebraic product. Berkovich Corollaries 2.2.7–2.2.8 give regular analytic local rings and regular affinoid domains, hence normality. The same applies after extension, so the curve normalization hypothesis holds. Projective bundles are normal by their local product charts. Closed strict discs and annuli are included, with absolute boundary allowed; the product dimension is \\(1+\\dim Y\\).\n\nThere are actual nonnormal geometrically unibranch examples. Over \\(\\mathbb Q_3\\), let \\(C=\\mathcal M(K\\langle u,v\\rangle/(v^2-u^3))\\). Its normalization is \\(K\\langle T\\rangle\\), with \\(u=T^2,v=T^3\\). The expansion \\(a(u)+vb(u)\\) maps injectively to disjoint even and odd powers; the image consists of series with no linear \\(T\\)-coefficient. Adjoining integral \\(T\\), with \\(T=v/u\\) in the fraction field, gives the normal Tate algebra finitely. Away from the origin the map is an isomorphism; over it there is one point with the same residue field. These computations persist after every field extension. For \\(C\\times Y^{\\mathrm{an}}\\), the finite birational map from the normal disc product is normalization. At a point of the cusp section its fiber algebra is \\(H[T]/(T^2,T^3)\\), with a single underlying point after every residue extension. Thus these products are geometrically unibranch and nonnormal, and the theorem covers every noninvariant usc obstacle on them.\n\nLimitations: this does not prove the sharp normal/geometrically-unibranch higher-dimensional classification, arbitrary normal affinoid positivity, continuity, or CLD-stage positivity. It establishes the displayed actual geometric sectors only.\n\nArtifacts: P03.1-argument.md contains the expanded complete proof; P03.1-paper.tex embeds it as a standalone paper. P03.1-paper.pdf has 13 pages. The command pdflatex -interaction=nonstopmode -halt-on-error P03.1-paper.tex ran twice with exit code 0 and no reported TeX warnings. Exact selected primary bodies and PDF checks are in source-extracts and source-provenance.json. Rerun sequentially: python prepare_sources.py; python build_artifacts.py; python make_notes.py; python check_artifacts.py. The last run passed 49 administrative checks. Commands, outputs and environment details are retained in rerun-commands.json, execution.json, build-pass-1.txt, build-pass-2.txt and environment.json. Supplied input bytes were preserved. Compilation, hashes and administrative checks are execution evidence, not mathematical correctness certificates.\n\nArtifacts: /workspace/research/campaigns/round-37/P03.1-public-source-geometric-positivity/artifacts/codex-7S9ct1",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Explicit full-family continuous-obstacle failures on split branches and codimension-two point pinchings, including a single irreducible bidisc with two rational points identified. Its strict affinoid algebra, seminormal analytic germs and normality off one codimension-two point are proved; genuine global rational LFS minorants force a closed-disc failure.",
    "detailedSummary": "For two closed polydiscs glued at their origins, the full raw envelope is computed exactly: zero on one punctured component and a negative constant on the other including the origin. Regularization raises the origin and fails a disc test. An additional irreducible example uses the subalgebra of the bidisc consisting of functions with equal values at two rational points. A bounded algebra decomposition proves affinoidness and finite normalization; its conductor and analytic germ kernel prove the stated geometry and seminormality. A continuous obstacle descends from the normalization, while polynomials vanishing at both identified points give global rational LFS minorants. The bad disc bounds every competitor at the pinched point, and the good disc forces regularization to exceed that bound. These independently proved examples establish insufficiency of seminormality and codimension-one normality; they do not classify the geometrically unibranch range.",
    "text": "Use the exact competitor identification, rational LFS presentation and published classical maximum principles checked in n1. Fix \\(0<|\\varpi|<1\\), put \\(\\rho=|\\varpi|\\), and \\(a=-\\log\\rho>0\\).\n\nFirst, for \\(d\\ge1\\), define\n\\[A_d=K\\langle X_1,\\ldots,X_d,Y_1,\\ldots,Y_d\\rangle/(X_iY_j),\\qquad W_d=\\mathcal M(A_d).\\]\nThere is an explicit ring identity\n\\[A_d=K\\langle X_1,\\ldots,X_d\\rangle\\times_KK\\langle Y_1,\\ldots,Y_d\\rangle,\\]\nwith evaluations at the origins. Modulo the cross terms a series has one common constant, an \\(X\\)-series without constant term and a \\(Y\\)-series without constant term. Thus the space is reduced, strict and pure of dimension \\(d\\). Its normalization is the product of the two normal Tate algebras, finite by adjoining the idempotent \\((1,0)\\). Outside the common origin \\(o\\), a nonzero coordinate removes the other component, so normalization is an isomorphism and the space is normal.\n\nIt is seminormal. For an element of the total fraction ring whose square and cube belong to \\(A_d\\), normality puts its two coordinates in the respective Tate algebras. Their constant terms \\(\\alpha,\\beta\\) satisfy \\(\\alpha^2=\\beta^2\\) and \\(\\alpha^3=\\beta^3\\), hence \\(\\alpha=\\beta\\), so the element belongs to \\(A_d\\). More directly, a subintegral intermediate extension in the normalization has a unique prime over \\(o\\) with residue field \\(K\\). Its two evaluations into \\(K\\) must agree, so all its elements have equal constant terms and it equals \\(A_d\\). The same argument works for analytic germs: at \\(o\\) they are the fiber product of the two regular polydisc germ rings over their residue field \\(K\\), obtained by taking arbitrarily small polydisc neighborhoods. Elsewhere the germs are normal. For \\(d=2\\), this gives a seminormal space normal away from a codimension-two point.\n\nSet\n\\[f=-a\\max_j|Y_j|,\\qquad h_n=\\frac1n\\log\\max\\{\\rho^n,|X_1|,\\ldots,|X_d|\\}.\\]\nThe obstacle is finite continuous. The local presentation in n1 proves that each \\(h_n\\) is a global rational LFS function. On the \\(X\\)-component it is at most zero, equal to the obstacle bound; on the \\(Y\\)-component it equals \\(-a\\le f\\). The constant \\(-a\\) is another competitor.\n\nFor any competitor in the full union, its restriction to the \\(Y\\)-polydisc is classically psh. The Gauss norm dominates every Tate-series evaluation and is multiplicative, so the polydisc has a singleton Shilov boundary. There the obstacle equals \\(-a\\). The classical affinoid maximum principle therefore bounds every competitor by \\(-a\\) throughout that component, including \\(o\\). On the punctured \\(X\\)-component at least one coordinate has positive norm, and \\(h_n\\) increases to zero. Thus the exact full raw envelope is zero on that punctured component and \\(-a\\) on the entire \\(Y\\)-component including \\(o\\).\n\nRegularization raises \\(o\\) to zero, because punctured \\(X\\)-points approach it and the continuous obstacle is zero there. Every other \\(Y\\)-point has a neighborhood avoiding the \\(X\\)-component, so its regularized value remains \\(-a\\). Pullback along the closed-disc axis \\(Y_1=T\\), other coordinates zero, has value zero at its origin and \\(-a\\) at its singleton Shilov point. It violates the maximum principle and is not classically psh. This proves split failure for every \\(d\\). The exact descent theorem in n1, which allowed an arbitrary base, also transfers this example to \\(W_d\\times Y^{\\mathrm{an}}\\) for the projective factors there. A finite extension supplying a point of the factor gives the same axis as a scalar curve test.\n\nThe codimension-two obstruction also has an irreducible realization. Let\n\\[B=K\\langle T,Z\\rangle,\\quad P=(0,0),\\quad Q=(1,0),\\quad A=\\{g\\in B:g(P)=g(Q)\\},\\quad W=\\mathcal M(A).\\]\nWe prove affinoidness rather than assume that this pinching is realizable. Put \\(U=T(T-1)\\), \\(R_0=K\\langle U,Z\\rangle\\). Then\n\\[B=R_0\\oplus TR_0,\\qquad A=R_0\\oplus T(U,Z)R_0.\\]\nFor the first decomposition, reduce powers by \\(T^2=T+U\\). If \\(T^m=a_m(U)+Tc_m(U)\\), the recurrence is \\((a_{m+1},c_{m+1})=(Uc_m,a_m+c_m)\\), starting at \\((1,0)\\). These integer-coefficient polynomials have Gauss norms at most one, so reduction of a convergent Tate series gives convergent \\(a,c\\in R_0\\), bounded by its norm. Substitution \\(U=T(T-1)\\) embeds \\(R_0\\) isometrically: scale a coefficient of maximal norm to one and reduce; a nonzero polynomial in \\(U,Z\\) remains nonzero under \\(U=T^2-T\\). Uniqueness follows by substituting \\(1-T\\) and subtracting, obtaining \\((2T-1)c(U,Z)=0\\) in the domain \\(B\\). This also works in characteristic two.\n\nThe two evaluation values of \\(a+Tc\\) differ by \\(c(0,0)\\), proving the formula for \\(A\\). It is generated over \\(R_0\\) by \\(TU,TZ\\) and is a finite module. The bounded map \\(K\\langle U,Z,V,R\\rangle\\to B\\), \\(V=TU,R=TZ\\), has image exactly \\(A\\): split the monomials of \\(c\\in(U,Z)\\) to write \\(c=Uc_1+Zc_2\\), then \\(a+Tc=a+Vc_1+Rc_2\\). These operations give a bounded linear right inverse. Hence the quotient norm and closed subspace norm are equivalent, and \\(A\\) is an actual strict affinoid quotient. It is an integral domain because it embeds in \\(B\\).\n\nAdjoining \\(T\\), integral by \\(T^2-T-U=0\\), gives \\(B\\); it is birational because \\(T=(TU)/U\\) in the fraction field. Since \\(B\\) is normal, \\(\\nu:\\mathcal M(B)\\to W\\) is finite normalization. Its conductor is \\(I=(U,Z)B\\): these functions vanish at \\(P,Q\\), whereas multiplication by \\(T\\) and \\(1-T\\) shows that every conductor element must vanish at both. Moreover\n\\[B/I=K\\times K,\\qquad A/I=K.\\]\nExactly \\(P,Q\\) are identified to a rational point \\(\\xi\\). Outside it normalization is an isomorphism. The space is irreducible of dimension two and normal away from \\(\\xi\\), which has codimension two.\n\nIt is seminormal as an analytic space. Any integral birational extension lies in \\(B\\); if subintegral, its two evaluations at \\(P,Q\\) must agree, so it is contained in \\(A\\) and equals \\(A\\). For germs, use the exact finite-module sequence\n\\[0\\to A\\to B\\xrightarrow{g\\mapsto g(Q)-g(P)}K_\\xi\\to0.\\]\nThe checked finite-module/coherent-sheaf correspondence on good affinoids, Berkovich 1.3 and Proposition 1.3.4, identifies the germ kernel with the equal-residue fiber product of the normal bidisc germs at \\(P,Q\\). The finite pushforward stalk has those two factors: properness allows inverse images of sufficiently small base neighborhoods to lie in any prescribed disjoint neighborhoods of the two fiber points. The same equal-evaluation argument rules out a proper subintegral germ extension. Other germs are normal.\n\nDefine a continuous function on \\([0,1]\\) by\n\\[\\phi(r)=\\begin{cases}-ar/\\rho&0\\le r\\le\\rho,\\\\ \\log r&\\rho\\le r\\le1.\\end{cases}\\]\nThe formulas agree at \\(\\rho\\), and \\(\\phi(0)=\\phi(1)=0\\). On normalization let \\(\\widetilde f=\\phi(|T-1|)\\). Its values at \\(P,Q\\) both equal zero, so it descends through the finite closed quotient to a finite continuous obstacle \\(f\\) on \\(W\\).\n\nThe polynomials \\(F_n=T(T-1)^n\\) belong to \\(A\\), since they vanish at both identified points. Hence\n\\[h_n=\\frac1n\\log\\max\\{\\rho^n,|F_n|\\}\\]\nare genuine global rational LFS functions on \\(W\\). On normalization, \\(|T|\\le1\\), giving\n\\[h_n\\circ\\nu\\le\\max\\{-a,\\log|T-1|\\}\\le\\phi(|T-1|)=f\\circ\\nu.\\]\nThe second inequality is \\(-a\\le-ar/\\rho\\) for \\(r\\le\\rho\\), and equality for \\(r\\ge\\rho\\). Thus they and the constant \\(-a\\) are full-family minorants.\n\nThe bad closed disc \\((T,Z)=(1+\\varpi S,0)\\), composed with normalization, maps its origin to \\(\\xi\\). At its Gauss point \\(|T-1|=\\rho\\), so \\(f=-a\\). Every competitor pulls back to a classically psh function on this disc; its singleton-Shilov maximum principle gives \\(h(\\xi)\\le-a\\). The baseline realizes equality, so the raw envelope at \\(\\xi\\) is \\(-a\\).\n\nOn the good disc \\((T,Z)=(\\varpi S,0)\\), every nonzero-radius point has \\(|T-1|=1\\), obstacle zero, and \\(|F_n|=|T|>0\\). The displayed minorants have supremum zero there, computing the full raw envelope at those points. They approach \\(\\xi\\), so its regularized value is zero. At the bad disc's Gauss point regularization stays at most \\(-a\\), since the continuous obstacle is an usc majorant of the raw envelope. The bad disc therefore fails the Shilov maximum principle.\n\nThis is an independently constructed irreducible, seminormal strict surface normal away from one codimension-two point, with a continuous obstacle and full-family classical-psh failure. It is not asserted identical to the supplied book example, and it does not establish a counterexample within the geometrically unibranch range.\n\nArtifacts and evidence: Section 5 of P03.1-argument.md and the standalone P03.1-paper.tex contain these complete constructions. The final P03.1-paper.pdf has 13 pages and compiled twice with exit code 0. Rerun python prepare_sources.py; python build_artifacts.py; python make_notes.py; python check_artifacts.py. Exact primary selections are in source-extracts and source-provenance.json; commands and diagnostics are retained. The 49 successful administrative checks and compilation do not certify the mathematical proofs.\n\nArtifacts: /workspace/research/campaigns/round-37/P03.1-public-source-geometric-positivity/artifacts/codex-7S9ct1",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Constructed an explicit continuous-obstacle failure for the full competitor family on the irreducible nonsplit quadratic-node surface over \\(\\mathbb Q_3\\). Truncated binomial polynomials give global rational LFS minorants, and a genuine quadratic-extension closed-disc test fails. Pointwise bijective curve normalization is therefore insufficient as a product-stable substitute. The original sharp classification remains unresolved.",
    "detailedSummary": "The nonsplit curve is an integral strict affinoid with finite normalization \\(L\\langle T\\rangle\\), where \\(L=\\mathbb Q_3(\\sqrt2)\\); every ground-field normalization fiber is a singleton. Its product with the strict open disc is an actual reduced irreducible surface, and a quadratic-residue nodal point has two normalization lifts. A continuous cutoff obstacle lies between \\(-3b\\) and zero. Explicit rational LFS functions built from truncated binomial coefficients are bounded globally by zero and equal \\(-3b\\) wherever the obstacle is negative, so they are global minorants. The plus-branch disc bounds every full-family competitor at the node by \\(-3b\\); the minus branch gives raw lower bound \\(-2b\\) at positive radii approaching it. Regularization thus violates the plus disc's singleton-Shilov maximum principle. This proves the nonsplit necessity obstruction, not a failure on a normal or geometrically unibranch higher-dimensional domain and not a complete solution of P03.1.",
    "text": "Use the full-family identification, local rational LFS presentation and classical scalar pullback/maximum principles established and checked in n1. The necessity examples in n2 remain separate from the construction here.\n\nLet \\(K=\\mathbb Q_3\\), \\(\\rho=|3|=1/3\\), \\(b=-\\log\\rho>0\\), and \\(L=K(\\alpha)\\) with \\(\\alpha^2=2\\). The polynomial is irreducible because 2 is nonsquare modulo 3, and \\(|\\alpha|=1\\). Define\n\\[C=\\mathcal M(K\\langle X,Y\\rangle/(X^2-2Y^2)),\\quad D=\\{|Z|<1\\}\\subset\\mathbb A_K^{1,\\mathrm{an}},\\quad X_0=C\\times_KD.\\]\nThe surface is named \\(X_0\\); \\(X\\) is a coordinate.\n\nThe curve algebra injects into \\(L\\langle T\\rangle\\), with \\(Y=T,X=\\alpha T\\). Reduction by the monic quadratic relation writes an element uniquely as \\(a(Y)+Xc(Y)\\). Its image has constant coefficient in \\(K\\) and arbitrary coefficients in \\(L\\) in positive degree: in degree \\(m\\ge1\\) the coefficient is \\(a_m+\\alpha c_{m-1}\\). The two \\(K\\)-components are independent. Thus the curve algebra is a domain. Adjoining integral \\(\\alpha\\), which equals \\(X/Y\\) in the fraction field, gives the normal algebra \\(L\\langle T\\rangle\\), finitely and birationally. This is normalization.\n\nIf \\(|Y|>0\\), normalization is an isomorphism with inverse \\(\\alpha=X/Y\\). Over \\(X=Y=0\\), its fiber is \\(\\mathcal M(L)\\), one point. Hence every ground-field Berkovich normalization fiber on the curve is a singleton. After extension to \\(L\\) the curve has two branches \\(X=\\pm\\alpha Y\\). At the product point with \\(X=Y=0\\) and \\(Z^2=18\\), the completed residue field is \\(L\\), and the normalization fiber is \\(\\mathcal M(L\\otimes_KL)=\\mathcal M(L\\times L)\\), two points.\n\nThe surface is reduced, irreducible, good, separated and strict, of dimension two. For an explicit strict exhaustion of \\(D\\), take \\(|Z|^m\\le|3|\\), whose algebra has the presentation \\(K\\langle Z,W\\rangle/(Z^m-3W)\\). On each such chart the surface algebra is the subalgebra of the integral polydisc algebra \\(L\\langle T,r^{-1}Z\\rangle\\) with constant coefficient in \\(T\\) belonging to \\(K\\langle r^{-1}Z\\rangle\\); it is a domain. The nested charts cover the open disc and their components overlap in nonempty interiors. Equivalently, the finite birational normalization is a connected normal polydisc domain over \\(L\\), hence irreducible. This verifies actual geometry rather than postulating a scalar orbit or abstract realization.\n\nDefine \\(r=|Y|\\), \\(G=3X-ZY\\), and\n\\[\\eta(r)=\\min\\{1,\\max\\{0,(r-\\rho)/(1-\\rho)\\}\\},\\qquad\\chi(R)=\\max\\{0,1-R/\\rho\\}.\\]\nSet the obstacle to\n\\[f=\\begin{cases}-3b\\,\\eta(r)\\,\\chi(|G|/(\\rho r))&r>0,\\\\0&r=0.\\end{cases}\\]\nIt is finite continuous and lies in \\([-3b,0]\\). The ratio is continuous where \\(r>0\\); near \\(r=0\\), \\(\\eta\\) vanishes on the entire region \\(r\\le\\rho\\), eliminating any continuity issue.\n\nFor \\(n\\ge1\\), put\n\\[\\delta=Z^2/18-1,\\quad c_j=\\binom{-1/2}{j},\\quad P_n(t)=\\sum_{j=0}^{n-1}c_jt^j,\\]\n\\[A_n(Z)=(Z/3)P_n(\\delta),\\quad F_n=X-A_n(Z)Y,\\quad h_n=\\frac1n\\log\\max\\{|3|^{3n},|3^{2n}F_n|\\}.\\]\nThese use global polynomials. The precise presentation in n1 makes each \\(h_n\\) a global rational LFS function, including at its zeros.\n\nThe identity \\(c_j=(-1)^j\\binom{2j}{j}/4^j\\) proves \\(|c_j|_3\\le1\\). On the whole surface \\(|Z|<1\\), \\(|X|,|Y|\\le1\\), and \\(|\\delta|\\le\\rho^{-2}\\). Consequently\n\\[|A_n|\\le\\rho^{-(2n-1)},\\quad |F_n|\\le\\rho^{-(2n-1)},\\quad |3^{2n}F_n|\\le\\rho,\\]\nso \\(-3b\\le h_n\\le0\\) globally.\n\nWe prove the stronger bound where \\(f<0\\). Such a point has \\(r>\\rho\\) and \\(R=|G|/(\\rho r)<\\rho\\). In its completed residue field put \\(t=X/Y\\), so \\(t^2=2\\), \\(|t|=1\\), and \\(w=Z/(3t)\\). Then \\(|w-1|=R<\\rho\\) and \\(\\delta=w^2-1\\), with \\(|\\delta|<\\rho\\). The series \\(B(\\delta)=\\sum_{j\\ge0}c_j\\delta^j\\) converges in that complete field. Its formal binomial identity gives \\((1+\\delta)B(\\delta)^2=1\\). Both \\(w\\) and \\(B(\\delta)\\) are within distance less than one of 1, so \\(wB(\\delta)\\) is the root \\(+1\\), not \\(-1\\), of its square-one equation; here \\(|2|_3=1\\). Hence \\(B(\\delta)=w^{-1}\\), and\n\\[|A_n-t|=|tw(P_n(\\delta)-B(\\delta))|\\le|\\delta|^n\\le\\rho^n.\\]\nTherefore \\(|F_n|\\le\\rho^n|Y|\\le\\rho^n\\), giving \\(h_n=-3b\\) wherever \\(f<0\\). There \\(h_n\\le f\\); elsewhere \\(f=0\\) and the global bound applies. Thus all \\(h_n\\) are genuine global members of the full obstacle family. In particular the family is nonempty; the constant \\(-3b\\) is also a minorant.\n\nOver the actual analytic extension \\(L/K\\), consider closed-disc morphisms\n\\[\\gamma_\\pm:\\mathcal M(L\\langle T\\rangle)\\to(X_0)_L,\\qquad(X,Y,Z)=(\\pm\\alpha T,T,3\\alpha).\\]\nThey land in the open factor because \\(|3\\alpha|=\\rho<1\\). Their origins have the same ground-field image \\(\\xi\\), the quadratic-residue nodal point described above.\n\nAt the plus-disc Gauss point, \\(r=1,G=0\\), so \\(f=-3b\\). Every competitor in the full union is classically psh and its scalar pullback obeys the singleton-Shilov maximum principle. Thus \\(h(\\xi)\\le-3b\\) for every competitor. The explicit minorants equal \\(-3b\\) there, proving the exact raw value \\(s(\\xi)=-3b\\), where \\(s=P_{X_0}f\\).\n\nOn the minus disc, \\(\\delta=0,A_n=\\alpha,F_n=-2\\alpha T\\). Since \\(|2\\alpha|=1\\), at every point with \\(|T|>0\\),\n\\[h_n\\circ\\gamma_-=\\max\\{-3b,-2b+n^{-1}\\log|T|\\},\\qquad\\sup_nh_n\\circ\\gamma_-=-2b.\\]\nPositive-radius points approach the origin and project continuously to \\(\\xi\\). Hence \\(s^*(\\xi)\\ge-2b\\). The continuous obstacle is an usc majorant of \\(s\\), so \\(s^*\\le f\\); its value at the projected plus-disc Gauss point is therefore at most \\(-3b\\).\n\nThe pullback \\(s^*\\circ\\pi_{L/K}\\circ\\gamma_+\\) has origin value at least \\(-2b\\) and singleton Shilov value at most \\(-3b\\). It violates the affinoid maximum principle. Thus the full regularized envelope is not classically psh. This is a scalar curve-test counterexample with a continuous obstacle and actual global rational LFS minorants, not merely a topological defect function or an invariant-envelope calculation.\n\nTogether with n2, this supplies explicit branch and codimension-two necessity obstructions. The nonsplit curve alone satisfies n1's pointwise-bijective normalization hypothesis, and products with the proper projective factors there have the positive property. Its product with the displayed open disc fails. Pointwise normalization bijectivity is consequently not a product-stable replacement for the requested higher-dimensional geometry.\n\nThe original target remains unresolved. No sharp necessary-and-sufficient hypotheses for arbitrary normal or geometrically unibranch higher-dimensional domains were obtained. No general normal affinoid theorem, arbitrary scalar-family cofinality, scalar regularization identity or defect removability theorem is proved. The counterexample here is not normal or geometrically unibranch at the revealed branches. No CLD-stage or general continuity conclusion is claimed. This note does not claim a complete solution of P03.1.\n\nArtifacts: P03.1-argument.md contains the complete expanded argument; P03.1-paper.tex is readable and standalone, and P03.1-paper.pdf has 13 pages. Both final TeX builds exited 0 without reported warnings. Exact selected primary bodies and checked PDF applications are retained in source-extracts and source-provenance.json. status.json has exactly id, status, exact_result, proof_file and concrete_gaps, with status partial. The supplied input and assignment were preserved. Rerun sequentially: python prepare_sources.py; python build_artifacts.py; python make_notes.py; python check_artifacts.py. Commands, outputs and environment details are retained; 49 administrative checks passed. No heavy computation, installation, network request, runtime alteration, external message, additional model or worker was used. These are unverified mathematical drafts: compilation and administrative checks do not certify correctness.\n\nArtifacts: /workspace/research/campaigns/round-37/P03.1-public-source-geometric-positivity/artifacts/codex-7S9ct1",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Actual published source provenance and hypothesis checks

{
  "kind": "checked public primary source selections",
  "sources": [
    {
      "id": "GR1",
      "url": "https://arxiv.org/pdf/2506.13548v2",
      "stem": "GR-2506.13548v2-20261004",
      "pdf_hash": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "text_hash": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "selections": [
        [
          "foundations",
          6,
          9
        ],
        [
          "curve-definitions-and-proofs",
          10,
          21
        ],
        [
          "classical-definition-and-PL-positivity",
          21,
          23
        ],
        [
          "local-maximum-principle",
          30,
          31
        ],
        [
          "affinoid-maximum-and-nets",
          33,
          34
        ]
      ],
      "applications": [
        "Definition 3.4 and 4.1 quantify over all analytic extensions.",
        "3.4.1 identifies the extended and Thuillier conventions on smooth connected curves.",
        "Proposition 3.5(3,7,8) supplies boundary extension and scalar/finite descent.",
        "Lemmas 3.7--3.9 supply the perfected/reduced curve normalization facts.",
        "Proposition 4.2(5,6) and Theorem 4.3 supply pullback/scalar stability and PL classical positivity.",
        "Theorem 6.1 makes continuous competitors constant on connected proper boundaryless fibers.",
        "Theorem 6.4 applies to the entire competitor family on closed polydisc and extended-disc tests."
      ],
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "actual_pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "actual_text_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "retained_extracts": [
        {
          "file": "source-extracts/GR1-foundations.literal.txt",
          "pdf_pages": [
            6,
            9
          ],
          "sha256": "778e5d70755a9e86980496671ea876f616ab229abf6c6183ab3275fe486e23f6"
        },
        {
          "file": "source-extracts/GR1-curve-definitions-and-proofs.literal.txt",
          "pdf_pages": [
            10,
            21
          ],
          "sha256": "6ae4d91bbc12e26b6295b3f2ea59e635fdfbd57fe8a3920175937c37ebfaeefc"
        },
        {
          "file": "source-extracts/GR1-classical-definition-and-PL-positivity.literal.txt",
          "pdf_pages": [
            21,
            23
          ],
          "sha256": "8769cce3dac8d179db64cee3769be60bd4f51d8926ce9beb55ec784c7a27a5ef"
        },
        {
          "file": "source-extracts/GR1-local-maximum-principle.literal.txt",
          "pdf_pages": [
            30,
            31
          ],
          "sha256": "fd96671fb3fa25b3c7afb95089d6b2679d36b80b4bc7aab0d34d24b40c55091b"
        },
        {
          "file": "source-extracts/GR1-affinoid-maximum-and-nets.literal.txt",
          "pdf_pages": [
            33,
            34
          ],
          "sha256": "ba29199790e4505c4c76b9986511a8cd7898d028ccda15de9363ff845b919dde"
        }
      ]
    },
    {
      "id": "GR2",
      "url": "https://arxiv.org/pdf/2503.05513",
      "stem": "GR-2503.05513-20261004",
      "pdf_hash": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "text_hash": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "selections": [
        [
          "standing-boundary-conventions",
          4,
          5
        ],
        [
          "curve-comparison",
          15,
          17
        ]
      ],
      "applications": [
        "Standing convention: smooth means rig-smooth and boundaryless.",
        "Proposition 5.1 and Corollary 5.4 are the comparison statements in this cached version.",
        "GR1 references an older GR2 numbering (3.1/3.5); no argument here treats the differing numbers as identical."
      ],
      "pdf": "/workspace/research/shared-sources/GR-2503.05513-20261004.pdf",
      "literal_extract": "/workspace/research/shared-sources/GR-2503.05513-20261004.txt",
      "actual_pdf_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "actual_text_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "retained_extracts": [
        {
          "file": "source-extracts/GR2-standing-boundary-conventions.literal.txt",
          "pdf_pages": [
            4,
            5
          ],
          "sha256": "e3d5a4c5e14257a65c7d66bda6466c55ec9bb2049ac7fde23cbdd6d2c77dbda6"
        },
        {
          "file": "source-extracts/GR2-curve-comparison.literal.txt",
          "pdf_pages": [
            15,
            17
          ],
          "sha256": "e3ab7738ee0f17c455d1519191b8b1c43f3551ff89fbfd31a3f7bd7f13b2b7da"
        }
      ]
    },
    {
      "id": "Thu",
      "url": "https://theses.hal.science/tel-00010990v1/document",
      "stem": "Thuillier-tel-00010990v1",
      "pdf_hash": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "text_hash": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "selections": [
        [
          "field-convention",
          29,
          30
        ],
        [
          "standing-curve-and-supremum",
          75,
          76
        ],
        [
          "curve-pullback",
          78,
          78
        ],
        [
          "scalar-pullback",
          105,
          105
        ]
      ],
      "applications": [
        "Proposition 3.1.8(iii): increasing locally bounded subharmonic family on an open subset of a smooth strict curve.",
        "Anchored finite maxima ensure the two-sided local boundedness literally required.",
        "This result is used only on the interior of a rig-smooth normalized curve.",
        "The PDF was visually checked: the result is 3.1.8(iii), not Lemma 3.1.9."
      ],
      "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
      "literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "actual_pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "actual_text_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "retained_extracts": [
        {
          "file": "source-extracts/Thu-field-convention.literal.txt",
          "pdf_pages": [
            29,
            30
          ],
          "sha256": "74e8f9b2c3027b3a8797241f43cd43e1ab9fa3c0e2cf08ab5464908b4ba49110"
        },
        {
          "file": "source-extracts/Thu-standing-curve-and-supremum.literal.txt",
          "pdf_pages": [
            75,
            76
          ],
          "sha256": "b9db9e7b6cde230bef7ae4c227957fcd7aaca9d04cc40ce7a74dbc7618f3ebcc"
        },
        {
          "file": "source-extracts/Thu-curve-pullback.literal.txt",
          "pdf_pages": [
            78,
            78
          ],
          "sha256": "bcdd9437e7694d59b6298267ab1f4ecb540e84aafa827f9605e95d94bc1a13f6"
        },
        {
          "file": "source-extracts/Thu-scalar-pullback.literal.txt",
          "pdf_pages": [
            105,
            105
          ],
          "sha256": "f7ba9960c4751bded0eab0d09c6bd74ce075168e3a43b5f48ae2e03d80fa3acc"
        }
      ]
    },
    {
      "id": "GJR",
      "url": "https://arxiv.org/pdf/2111.05741",
      "stem": "GJR-2111.05741",
      "pdf_hash": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "text_hash": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "selections": [
        [
          "PL-definition-and-pullback",
          30,
          32
        ],
        [
          "finite-PL-descent",
          34,
          36
        ],
        [
          "residue-and-semipositivity",
          44,
          47
        ]
      ],
      "applications": [
        "Definition 5.1 makes R-PL functions finite continuous and uses the strict G-topology.",
        "Lemma 5.4 and Proposition 7.6 preserve PL/semipositivity under morphisms and arbitrary analytic extensions.",
        "Corollary 5.12 with Lambda=R descends the base function from one finite extension giving a point of the projective factor.",
        "Definition 7.8 says LFS is R-PL with semiample residues, hence semipositive.",
        "The PDF 7.9 presentation uses nonnegative combinations and max of NEGATIVE logs of INVERTIBLE functions.",
        "Only rational common-denominator maxima are used in the new examples; arbitrary R-PL max closure is not assumed."
      ],
      "pdf": "/workspace/research/shared-sources/GJR-2111.05741.pdf",
      "literal_extract": "/workspace/research/shared-sources/GJR-2111.05741.txt",
      "actual_pdf_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "actual_text_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "retained_extracts": [
        {
          "file": "source-extracts/GJR-PL-definition-and-pullback.literal.txt",
          "pdf_pages": [
            30,
            32
          ],
          "sha256": "7e1c063e0475e1d3de20302e384a741f16640b800c8f3d0e9137c1552133e5a0"
        },
        {
          "file": "source-extracts/GJR-finite-PL-descent.literal.txt",
          "pdf_pages": [
            34,
            36
          ],
          "sha256": "7a42bd32d73289286816bc6df6dcd36b86c9211b56b45d24e36222720ff0715d"
        },
        {
          "file": "source-extracts/GJR-residue-and-semipositivity.literal.txt",
          "pdf_pages": [
            44,
            47
          ],
          "sha256": "787a0d01dbeefa39dfe595bcd423df315305dbe80e3a82dd0bdd48facf95fc81"
        }
      ]
    },
    {
      "id": "Ber",
      "url": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "stem": "Berkovich-PMIHES-1993-78-5",
      "pdf_hash": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "text_hash": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "selections": [
        [
          "coherent-finite-modules",
          22,
          23
        ],
        [
          "proper-and-boundary",
          31,
          32
        ],
        [
          "regularity-of-domains",
          36,
          40
        ],
        [
          "analytification-and-properness",
          48,
          51
        ],
        [
          "smooth-morphisms",
          64,
          66
        ],
        [
          "openness",
          73,
          74
        ],
        [
          "proper-connectedness-comparison",
          125,
          127
        ]
      ],
      "applications": [
        "Proposition 1.3.4 and the preceding finite-module discussion identify coherent analytic germ kernels for the explicit irreducible point pinching.",
        "Propositions 2.6.1 and 2.6.9 give boundaryless analytification, base change, and projective properness.",
        "Theorem 7.1.1 in degree zero, for a finite constant sheaf on a proper scheme, proves connectedness of every projective analytic fiber.",
        "Proposition 3.5.8 and 3.5.2 prove the product projection smooth, even when the base has absolute boundary.",
        "Corollary 3.7.4 says a smooth morphism is an open map, in the ordinary topology.",
        "Corollaries 2.2.7--2.2.8 identify regularity on algebraic analytifications and affinoid domains."
      ],
      "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
      "literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
      "actual_pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "actual_text_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "retained_extracts": [
        {
          "file": "source-extracts/Ber-coherent-finite-modules.literal.txt",
          "pdf_pages": [
            22,
            23
          ],
          "sha256": "405313c64b82f04277b484200a8ebdf6558a9a91d7ed48bd73749a25a6cd66c8"
        },
        {
          "file": "source-extracts/Ber-proper-and-boundary.literal.txt",
          "pdf_pages": [
            31,
            32
          ],
          "sha256": "b0e401623ae363ccd5fcc1717a06f8035f88ad57382d59477168b6b9d93ca267"
        },
        {
          "file": "source-extracts/Ber-regularity-of-domains.literal.txt",
          "pdf_pages": [
            36,
            40
          ],
          "sha256": "05f6d42dd1f9cbc8aad0c39fdda3817580bfd1283725e5a935a31e4d69334e09"
        },
        {
          "file": "source-extracts/Ber-analytification-and-properness.literal.txt",
          "pdf_pages": [
            48,
            51
          ],
          "sha256": "8d68d0f58de891353afc5b4cf9fce0c1b70375c455a89f193d707cd3780341c0"
        },
        {
          "file": "source-extracts/Ber-smooth-morphisms.literal.txt",
          "pdf_pages": [
            64,
            66
          ],
          "sha256": "a1f8255eba5cd9e6ef01efd5274961444713adfdb7490175b005d962521e01b9"
        },
        {
          "file": "source-extracts/Ber-openness.literal.txt",
          "pdf_pages": [
            73,
            74
          ],
          "sha256": "dc33ce78989cf9c7b753bc5f4fe46f3872b0fa522856fc812eeebb764149f641"
        },
        {
          "file": "source-extracts/Ber-proper-connectedness-comparison.literal.txt",
          "pdf_pages": [
            125,
            127
          ],
          "sha256": "301c1272c20ff813592b624b421d58f2a0adce99462342c844b1d4011ec38e17"
        }
      ]
    }
  ],
  "pdf_images": [
    {
      "source": "Thu",
      "pdf_page": 76,
      "file": "source-extracts/Thuillier-3.1.8-pdf.png"
    },
    {
      "source": "GJR",
      "pdf_page": 47,
      "file": "source-extracts/GJR-7.8-7.9-pdf.png"
    },
    {
      "source": "Ber",
      "pdf_page": 74,
      "file": "source-extracts/Berkovich-3.7.4-pdf.png"
    },
    {
      "source": "Ber",
      "pdf_page": 125,
      "file": "source-extracts/Berkovich-7.1.1-pdf.png"
    },
    {
      "source": "GR1",
      "pdf_page": 21,
      "file": "source-extracts/GR1-4.1-pdf.png"
    }
  ],
  "proof_scope": "Published foundations are cited; all new geometric applications are proved in P03.1-argument.md and P03.1-paper.tex.",
  "warning": "Hashes identify bytes and rendering records OCR checks; neither verifies mathematics."
}


## Published source GR1, PDF pages 6-9

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
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                9

2.14. Models and formal geometry. A quasi-compact admissible formal scheme over
k◦ is a quasi-compact formal scheme X over k◦ with an open covering by affine formal
schemes Spf(A) for k◦ -algebras A which are topologically of finite type and flat over k◦ .
The generic fiber Xη of X is the strictly k-analytic space obtained by gluing the Berkovich
spectra M (A ⊗k◦ k), and the special fiber Xs is the scheme over ek obtained by gluing the
affine schemes Spec(A ⊗k◦ ek).

Definition 2.15. A formal k◦ -model X for a quasi-compact strictly k-analytic space X is a
quasi-compact admissible formal scheme X over k◦ with an identification Xη = X .

   In the above setting, there is a canonical reduction map redX : X → Xs which is surjec-
tive and anticontinuous [GRW16, Section 2]. We call x ∈ X a divisorial point associated
to the model X if redX (x) is a generic point of the special fiber Xs . Note that the set of
divisorial points is finite: see [GM19, Appendix A]. In ibid, the valuation on k is assumed
to be non-trivial, but this finiteness also holds in the trivially valued case as then Xη is
just the analytification of the special fiber and the generic points of the special fiber have
a unique preimage under the reduction.

2.16. PL functions. We will assume k is non-trivially valued when we discuss PL func-
tions. Let Λ be a subgroup of R which is either divisible or equal to Z. We consider a
good, strictly k-analytic space PX . A function h: X → R is called Λ-piecewise linear or
Λ-PL if G-locally we have h = j λ j log | f j | for finitely many λ j ∈ Λ and invertible ana-
lytic functions f j . Here we use the G-topology of X generated by the strictly k-analytic
domains. We refer to [GJR21, Section 5] for more on Λ-PL functions.

2.17. Reduction of germs. For a good, strictly k-analytic space X over a non-trivially
valued field, Temkin [Tem00] introduced the reduction of the germ (X , x) at x ∈ X as
an open subset of a Zariski–Riemann space PHf(x)/ek of H    f(x)/ek. Roughly speaking, it
is the projective limit of all canonical reductions Spec(A  f) where M (A ) ranges over
all k-affinoid neighborhoods of x. The germ (X , x) is naturally a quasicompact locally
ringed space. See also [CD12, Section 6.1] for an excellent summary. An R-PL function
h: X → R induces a residue line bundle L(h) ∈ Pic(X , x)R . This was introduced in [CD12],
and is explained in [GJR21, Section 6]. We call h semipositive at x if L(h) is nef in the
sense of [GJR21, Section 7]. A semipositive R-PL function is semipositive at all x ∈ X .

2.18. Graded reduction. While the reduction in 2.17 works well for (good) strictly k-
analytic spaces, this concept does not fit very well for non-strictly k-analytic spaces or
in the trivially valued case. To handle the general case, Temkin introduced [Tem04] the
graded reduction of the germ (X , x). We need it only for Lemma 6.3, so we introduce
here only the graded reduction of a k-algebra A endowed with a multiplicative seminorm
ρ. In our applications, the algebra A will be either a k-affinoid algebra endowed with
| |sup or the completed residue field H (x) in a point x of a k-analytic space endowed
with its canonical absolute value. For r ∈ R>0 , we set
               A≤r := {a ∈ A | ρ(a) ≤ r}    and    A<r := {a ∈ A | ρ(a) < r}.


## Published source GR1, PDF pages 10-21

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
12                                 W. GUBLER AND J. RABINOFF

fact that Definition 3.4 essentially recovers Thuillier’s definition of subharmonicity in that
case 3.4.1.
3.5.4. In the situation of Proposition 3.5(8), it is immediate from Definition 3.4 that u◦ f
is subharmonic when u is subharmonic. The remark in 3.5.3 applies to a lesser extent in
this case: see [Thu05, Proposition 3.1.14].
3.5.5. For any x ∈ X , the subset Int(X )∪{x} is open in X . This is obvious if x ∈ Int(X ), and
if x ∈ ∂ X then it follows from the fact that ∂ X is discrete in X . In particular, Int(X ) ∪ {x}
is again a k-analytic curve, so it makes sense to speak of its irreducible components
in Proposition 3.5(9). Irreducible components can only meet at rig-points (their inter-
sections are Zariski-closed), so a non-rig-point x is contained in a unique irreducible
component of Int(X ) ∪ {x}; this is implicit in Proposition 3.5(9).
3.5.6. Proposition 3.5(9) implies that if u is subharmonic and u(x) = −∞ for a non-rig-
point x ∈ X , then u ≡ −∞ in a neighborhood of x.
3.6. In order to extend Thuillier’s results, we will pass from a k-analytic curve to a
smooth, strictly k-analytic curve in four steps:
      (1) Extend scalars to a field as in 2.10 to make the curve strictly analytic.
                                                                                          −∞
      (2) If char(k) = p, then extend scalars to the completion of the perfect closure k p .
      (3) Replace the analytic curve by the underlying reduced curve.
      (4) Pass to the interior of the normalization, which is smooth (see 2.13).
We begin with some lemmas about this process.
                                                                                 −∞
Lemma 3.7. Suppose that char(k) = p > 0. Let k′ be the completion of k p . Then k′ is
perfect, and if X is a k-analytic space then πk′ /k : X k′ → X is a homeomorphism such that
π(∂ X k′ ) = ∂ X .
Proof. We leave it as an exercise for the reader to verify that k′ is perfect. The fact that
πk′ /k is a homeomorphism is [Duc09, Remarque 0.5], and the assertion about boundaries
is Lemma 2.12.                                                                            □
     We make the following observation to mirror Lemma 3.7. Its proof is immediate.
Lemma 3.8. Let X be a strictly k-analytic space and let ι : X red ,→ X be the inclusion of the
underlying reduced space. Then ι is a homeomorphism of underlying topological spaces, and
ι(∂ X red ) = ∂ X .
  We refer the reader to [Ber90, before Proposition 3.1.8] for the construction of the
normalization.
Lemma 3.9. Let X be a reduced, strictly k-analytic curve and let ν: Xe → X be its normal-
ization. Then the following hold:
    (1) Xe is rig-smooth if k is perfect.
    (2) ν is an isomorphism outside of a discrete set of rig-points of X .
                                     ∼
    (3) ν induces a bijection ∂ Xe −→ ∂ X .
    (4) ν is a topological quotient.
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                       13

                                                                             e = ν−1 (U) →
    (5) Let x ∈ X , let U be an open neighborhood of x, and consider the map U
        U. If U is a sufficiently small connected open neighborhood of x, then:
         (a) Ue → U is injective on connected components of U.  e
                                                                 ∼
         (b) Ue → U restricts to an isomorphism U  e \ ν−1 (x) −→ U \ {x}.
         (c) Every connected component of U   e intersects ν−1 (x).
    (6) A function h: X → R is R-PL if and only if h ◦ ν is R-PL.



Proof. The normalization Xe is locally the Berkovich spectrum of a Dedekind domain, so it
is rig-smooth when k is perfect because it is regular; this proves (1). Normalization is an
isomorphism away from codimension 1 as in algebraic geometry, which yields (2). Since
ν is finite, we have ∂ Xe = ν−1 (∂ X ) by the properties (2′ ) and (4′ ) of 2.11, so (3) follows
from (2) because the boundaries do not contain any rig-points. Assertion (4) was noted
in [Duc24, (3.1.3)].
    Now we prove (5). Since normalization is a local construction, we may shrink X to
assume that it is normal away from x. Suppose that ν−1 (x) = {x 1 , . . . , x n }, and choose
disjoint, connected open neighborhoods U1′ , . . . , Un′ of x 1 , . . . , x n , respectively. Let U ′ =
Sn                                                                         ∼
   i=1
       ν(Ui′ ).FSince ν induces an isomorphism Xe \ {x 1 , . . . , x n } −→ X \ {x}, it is clear that
                      n
ν−1 (U ′ ) = i=1 Ui′ . Since ν is a topological quotient, we have that U ′ is open, and ν is
injective on each Ui′ by construction.
    Suppose now that U ⊂ U ′ is a connected open neighborhood of x. By [Ber90, Theorem
3.2.1], U is path-connected. Clearly U satisfies (a) and (b). Let Ui = ν−1 (U) ∩ Ui′ , so that
                      e = ν−1 (U) = n Ui . In order to prove (c), it is enough to show that Ui
                                      F
x i ∈ Ui and U                          i=1
is path-connected. Let y ∈ Ui \ {x i }, and let γ: [0, 1] → U be a path from π( y) to x.
We may assume that γ−1 (x) = {1}, so that γ restricts to a path [0, 1) → U \ {x}. Let
γ
e : [0, 1) → U       e \ ν−1 (x) be the composition of γ|[0,1) with the inverse of the isomorphism
                      ∼
e \ ν−1 (x) −→ U \ {x}. Then γ
U                                        e(0) = y, so the image of γ e is contained in Ui . Extend γ  e
to a function [0, 1] → Ui by setting γ        e(1) = x i . One checks continuity of γ e at 1 using the
fact that an open neighborhood of x is the same as a collection of open neighborhoods
of x 1 , . . . , x n , as in the previous paragraph. This shows that Ui is path-connected.
    In the situation of (6), if h is R-PL then h◦ν is R-PL by [GJR21, Lemma 5.4(1)]. Suppose
then that h ◦ ν is R-PL. Piecewise linearity of h is local on X , and ν is an isomorphism
away from a finite set of (non-normal) rig-points, so it is enough to check that h is R-PL
in a neighborhood of a single rig-point x. Let x ′ ∈ Xe be a preimage ofPx. There is a
                                                                                          n
covering of Xe by strictly affinoid domains on which h ◦ ν has the form i=1 λi log | f i |,
where λi ∈ R and f i ∈ O × . Since x ′ is      Pan rig-point, it is contained in the interior   of one
of these affinoid domains, so h ◦ ν = i=1 λi log | f i | in a neighborhood of x . But if f is
                                                                                          ′

invertible in a neighborhood of a rig-point x ′ , then | f | is constant on a neighborhood of
x ′ (this elementary fact can be seen as a very special case of [Duc12, Theorem 3.4]). It
follows that h◦ν is constant in a neighborhood of x ′ . Suppose that ν−1 (x) = {x 1 , . . . , x n }.
For eachSn i choose an open neighborhood Ui of x i on which h ◦ ν is constant. As above,
U = i=1 ν(Ui ) is an open neighborhood of x, and clearly h is constant, hence R-PL,
on U.                                                                                                 □
14                                  W. GUBLER AND J. RABINOFF

Proof of Proposition 3.5(1). This follows from the corresponding fact for subharmonic
functions on smooth, strictly analytic curves [Thu05, Corollaire 3.1.13], except that one
has to be careful about where a function takes the value −∞. Suppose then that {Ui }
is an open cover of X and that u: X → R ∪ {−∞} is subharmonic on each Ui . Note that
u is upper semicontinuous. Let k′ /k be an analytic extension field with k′ non-trivially
valued, let Y be a smooth, connected, strictly k′ -analytic curve, and let f : Y → X k′ be a
morphism. Assume that u ◦ πk′ /k ◦ f ̸≡ −∞, so we must show that u ◦ πk′ /k ◦ f is sub-
harmonic in Thuillier’s sense. Let Ui′ = π−1 k′ /k
                                                   (Ui ) = (Ui )k′ and let Yi = f −1 (Ui′ ). Since u
is subharmonic on Ui , the composition u ◦ πk′ /k ◦ f |Yi is either subharmonic in Thuillier’s
sense or is identically −∞ on each connected component of Yi .
   Let W1 be the set of all points y ∈ Y that admit a neighborhood on which u ◦ πk′ /k ◦ f
is subharmonic in Thuillier’s sense, and let W2 be the set of all points y ∈ Y that admit a
neighborhood on which u ◦ πk′ /k ◦ f ≡ −∞. Clearly W1 and W2 are open, and they cover
Y since Y is covered by the connected components of the Yi . They are disjoint because if
u ◦ πk′ /k ◦ f is subharmonic in Thuillier’s sense on a connected neighborhood of y ∈ Y ,
then it cannot be identically −∞ on any neighborhood of y [Thu05, Lemme 3.1.9].
Since Y is connected and u ◦ πk′ /k ◦ f ̸≡ −∞, we have Y = W1 . The result now follows
from [Thu05, Corollaire 3.1.13].                                                                  □


Proof of Proposition 3.5(2). Let f be an analytic function on X . The function | f | is con-
tinuous and hence u := log | f | is upper semicontinuous as a continuous function with
values in R ∪ {−∞}. According to our definition of subharmonic functions, we have to
show that after base change of u with respect to an analytic field extension k′ /k with k′
non-trivially valued and then pull-back to a smooth strictly k′ -analytic curve, the resulting
function is subharmonic. This boils down to showing that u is subharmonic in the special
case of a smooth strictly k-analytic curve X . For this, we may assume X connected. If
f = 0, then u is identically −∞ and hence subharmonic in the sense of Definition 3.4. If
f is not identically zero, then the Poincaré–Lelong formula [Thu05, Proposition 3.3.15]
and the characterization in terms of positive currents [Thu05, Proposition 3.4.4] show
that u is subharmonic in the sense of Thuillier.                                            □


  We will use the following lemma in the proofs of Proposition 3.5(3,9). If X is a k-
analytic space and k′ /k is an analytic extension field, then π−1
                                                               k′ /k
                                                                     (x) = M (H (x)⊗
                                                                                   b k k′ )
has a finite Shilov boundary for any Abhyankar point x ∈ X by [Duc24, 3.2.14]; we
denote this boundary by x [k′ ] .

Lemma 3.10. Let X be a k-analytic curve and let k′ /k be an analytic field extension. Then
for all x ∈ ∂ X we have (∂ X k′ ) ∩ π−1
                                     k′ /k
                                           (x) = x [k′ ] .

Proof. Replacing X by an affinoid neighborhood of x, we may assume that X = M (A )
is affinoid. By a result of Ducros [Duc12, Lemme 3.1], there exists a morphism g : X →
B1 (0, s) for some s ∈ R>0 such that x ∈ g −1 (ηs ), where ηs is the maximal point of B1 (0, s).
                CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                                 15

This is discussed in detail in Section 6. Consider the commutative square

                                                          g′
                                                           → B1k′ (0, s)
                                                      ←
                                               X k′




                                                ←




                                                                  ←
                                           πk′ /k                   πk′ /k




                                                                 →
                                               →
                                                          g → B (0, s).
                                                      ←        1
                                                X

Since ∂ B1k′ (0, s) contains (only) its maximal point ηs,k′ , we have (g ′ )−1 (ηs,k′ ) ⊂ ∂ X k′
by (2.11.4) (which is an equality because B1k′ (0, s) is separated). The morphism g is an
Abhyankar presentation of x in the sense of [Duc24, 3.2.12.2], so by Proposition 3.2.13
of ibid, we have x [k′ ] = (g ′ )−1 (ηs,k′ ) ∩ π−1
                                                k′ /k
                                                      (x) ⊂ (∂ X k′ ) ∩ π−1
                                                                         k′ /k
                                                                               (x).
   For the reverse inclusion, let x ∈ (∂ X k′ ) ∩ πk′ /k (x), and suppose that x ′ ∈
                                        ′                   −1
                                                                                         / x [k′ ] . Since
∂ X k′ is the Shilov boundary of X k′ = M (A ⊗         b k k ), by [Ber90, Corollary 2.4.5] there exist
                                                            ′

f ∈ A⊗   b k k and ϵ > 0 such that | f | attains its maximum value at x ′ and such that
              ′

                          
                            y ∈ X k′ | f ( y)| > | f (x ′ )| − ϵ ⊂ X k′ \ x [k′ ] .

In particular, the restriction of f to π−1
                                        k′ /k
                                              (x) does not attain its maximum value on x [k′ ] ,
which cannot happen. Thus x ∈ x [k′ ] , so (∂ X k′ ) ∩ π−1
                                 ′
                                                         k′ /k
                                                               (x) ⊂ x [k′ ] .             □

Proof of Proposition 3.5(3). Suppose that u is subharmonic on Int(X ). Let k′ /k be an
analytic extension field with k′ non-trivially valued, let Y be a smooth, connected, strictly
k′ -analytic curve, and let f : Y → X k′ be a morphism. We must prove that u ◦ πk′ /k ◦
f is subharmonic in Thuillier’s sense or is identically −∞. Since ∂ Y = ;, it follows
from 2.11(4) that f (Y ) ⊂ Int(X k′ ). If πk′ /k ◦ f (Y ) ⊂ Int(X ) then u◦πk′ /k ◦ f is subharmonic
in Thuillier’s sense or is identically −∞ because u is subharmonic on Int(X ). Suppose
then that πk′ /k ◦ f ( y) = x ∈ ∂ X for some y ∈ Y , so that f ( y) ∈ Int(X k′ ) ∩ π−1                 k′ /k
                                                                                                             (x).
    We claim that πk′ /k (x)∩Int(X k′ ) is both open and closed in Int(X k′ ). By [Duc24, Propo-
                         −1

sition 5.3.4], if U is a connected component of π−1               k′ /k
                                                                        (X \ {x}), then the closure of U in
X k′ is contained in πk′ /k (X \ {x}) ∪ x [k′ ] . Let U be the connected component of X k′ \ x [k′ ]
                            −1                                ′

containing U. The above shows that U is closed in U ′ . Since U is open in X (an analytic
space is locally connected [Ber93, Remark 1.2.4(iii)] and hence its connected compo-
nents are open [Sta21, Lemma 04ME]), it is open in U ′ , so U = U ′ since U ′ is connected.
Hence π−1  k′ /k
                 (X \ {x}) is a union of connected components of X k′ \ x [k′ ] , so the same is
true of πk′ /k (x) \ x [k′ ] . Since X k′ \ x [k′ ] is itself a k-analytic space as x [k′ ] is a finite set, its
           −1

connected components are open, so we conclude that π−1                       k′ /k
                                                                                   (x) \ x [k′ ] is open and closed
in X k′ \ x [k′ ] . Since x ∈ ∂ X , we have (πk′ /k (x)) ∩ ∂ X k′ = x [k′ ] by Lemma 3.10, which
                                                         −1

shows Int(X k′ ) ⊂ X k′ \ x [k′ ] and π−1   k′ /k
                                                  (x) \ x [k′ ] = π−1 k′ /k
                                                                            (x) ∩ Int(X k′ ). We conclude that
πk′ /k (x) \ x [k′ ] is both open and closed in Int(X k′ ), as claimed.
  −1

    Since Y is connected, f (Y ) ⊂ Int(X k′ ), and f ( y) ∈ Int(X k′ ) ∩ π−1            k′ /k
                                                                                              (x), we deduce from
the above claim that f (Y ) ⊂ Int(X k′ )∩πk′ /k (x). Hence πk′ /k ◦ f is constant, so u◦πk′ /k ◦ f
                                                      −1

is constant. It follows that u is subharmonic in Thuillier’s sense or is identically −∞. □
16                                        W. GUBLER AND J. RABINOFF

Proof of Proposition 3.5(4,5). These follow quickly from the corresponding facts for sub-
harmonic functions on smooth, strictly analytic curves [Thu05, Proposition 3.1.8].     □

Proof of Proposition 3.5(6). Suppose first that X is strictly k-analytic for k non-trivially
                                                                                −∞
valued. If char(k) = p > 0 then let k′ be the completion of k p ; otherwise let k′ = k.
Let X ′ = X k′ and let π = πk′ /k : X ′ → X , so π is a homeomorphism preserving boundaries
by Lemma 3.7. Let ι : X red    ′
                                  ,→ X ′ be the inclusion of the underlying reduced space and let
ν: Xe ′ → X red′
                  be the normalization. Note that ν and ι are finite, so ∂ Xe ′ = (ι ◦ ν)−1 (∂ X ′ ),
and hence ∂ Xe ′ = (π◦ι ◦ν)−1 (∂ X ). Let Y = Int(Xe ′ ) and let f = ι ◦ν|Y : Y → X ′ . Then Y is
smooth and strictly analytic, so u ◦ π ◦ f is by definition either subharmonic in Thuillier’s
sense or identically −∞ on every connected component of Y .
   Suppose that u attains a local maximum at x ∈ Int(X ). If u(x) = −∞ then u must
be constant in a neighborhood of x by semicontinuity of u. Assume then that u(x) >
−∞. Both π and ι are homeomorphisms, so it suffices to show that u ◦ π ◦ ι : X red                 ′
                                                                                                      →
R ∪ {−∞} is constant in a neighborhood of the unique point x ∈ Int(X red ) mapping to
                                                                                 ′       ′

x. Choose a connected open neighborhood U ⊂ Int(X red                ′
                                                                       ) of x ′ as in Lemma 3.9(5), on
which u ◦ π ◦ ι attains a maximum at x ′ . By Lemma 3.9(3), we have ν−1 (U) ⊂ Y =
Int(Xe ′ ), so u ◦ π ◦ f is again either subharmonic in Thuillier’s sense or identically −∞
on each connected component C of ν−1 (U); since u(x) > −∞ and C ∩ ν−1 (x ′ ) ̸= ;, the
former is true. The function u◦π◦ f attains its maximum on every connected component
of ν−1 (U), so by the maximum principle for subharmonic functions on smooth, strictly
analytic curves [Thu05, Proposition 3.1.11], the function u ◦ π ◦ f is constant on every
connected component of ν−1 (U). It follows that u ◦ π ◦ ι is constant on U.
   Now we reduce to the strictly analytic case handled above. We may assume that X
is affinoid. As explained in 2.10, there is an analytic extension field k′ = k r for some
r ∈ R>0n
             such that X k′ is strictly k′ -analytic. Let σ : X → X k′ be the Shilov section of πk′ /k .
Then x = σ(x) ∈ Int(X k′ ) because π−1
           ′
                                                k′ /k
                                                      (Int(X )) ⊂ Int(X k′ ) by 2.11(5). It is immediate
from the definition that u ◦ πk′ /k is subharmonic, and it attains a local maximum at x ′ ,
so u ◦ πk′ /k is constant in an open neighborhood U ′ of x ′ . Then u is constant on the open
set U = σ−1 (U ′ ).                                                                                   □

Proof of Proposition 3.5(7). It is immediate from the definition that subharmonicity of
u implies subharmonicity of u ◦ πk′ /k . Suppose then that u ◦ πk′ /k is subharmonic. Let
k′′ /k be another analytic extension field with k′′ non-trivially valued, and let f : Y →
X k′′ be a morphism from a smooth, connected, strictly k′′ -analytic curve. Assume that
u ◦ πk′′ /k ◦ f ̸≡ −∞, so we need to show that u ◦ πk′′ /k ◦ f is subharmonic in Thuillier’s
sense. Let K be a non-Archimedean field that is simultaneously an analytic extension of
k′ and k′′ 2.2, and consider the following commutative diagram:

                               ←   fK            πK/k′
                                                 ←
                          YK            → XK          → X k′
                          ←



                                           ←



                                                            ←




(3.10.1)                                     πK/k′′             πk′ /k
                          →



                                          →



                                                            →




                               ←                 ←                ←
                           Y       f
                                       → X k′′         →
                                                  πk′′ /k   X            u → R ∪ {−∞}.
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                 17

Since u ◦ πk′ /k is subharmonic, the composition u ◦ πK/k ◦ f K is, on each connected compo-
nent C of YK , either subharmonic in Thuillier’s sense or identically −∞; since C surjects
onto Y [Duc18, 1.5.6] and u ◦ πk′′ /k ◦ f ̸≡ −∞, the latter does not happen. Replacing
X by Y and k′ /k by K/k′′ , we are reduced to showing that if X is smooth and strictly
k-analytic for k non-trivially valued and u ◦ πk′ /k is subharmonic in Thuillier’s sense, then
so is u.
   We can do this directly using Thuillier’s definition. (The converse is the difficult di-
rection: see [Thu05, Corollaire 3.4.5].) Let U ⊂ X be a strictly k-affinoid domain and
let h: U → R be a harmonic function such that u ≤ h on ∂ U. Then h ◦ πk′ /k : Uk′ =
π−1
  k′ /k
        (U) → R is harmonic by [Thu05, Proposition 2.3.18]. We have πk′ /k (∂ Uk′ ) = ∂ U by
Lemma 2.12, so u ◦ πk′ /k ≤ h ◦ πk′ /k on ∂ Uk′ . Since u ◦ πk′ /k is subharmonic in Thuillier’s
sense, this implies u ◦ πk′ /k ≤ h ◦ πk′ /k on Uk′ , so u ≤ h on U since πk′ /k : Uk′ ↠ U is
surjective. Thus u is subharmonic in Thuillier’s sense, as claimed.                          □

Proof of Proposition 3.5(8). It is immediate that subharmonicity of u implies subharmonic-
ity of u ◦ f . Suppose then that f is finite and surjective and that u ◦ f is subharmonic. Let
k′ /k be an analytic extension field with k′ non-trivially valued and let g : Z → X k′ be a
morphism from a smooth, connected, strictly k′ -analytic curve. Suppose that u◦πk′ /k ◦g ̸≡
−∞, so we need to show that u ◦ πk′ /k ◦ g is subharmonic in Thuillier’s sense. Let
W = Z ×X k′ Yk′ , and consider the following commutative diagram:

                                   ←   g′           πk′ /k
                                                    ←
                          W             → Yk′           → Y
                           ←




                                                             ←
                                            ←




(3.10.2)                f ′′           □       f′                f
                          →



                                            →



                                                             →




                                   ←                ←                ←
                               Z       g→   X k′        →
                                                    πk′ /k   X           u → R ∪ {−∞}.


The composition (u ◦ f ) ◦ πk′ /k ◦ g ′ is subharmonic because it is pulled back from u ◦ f by
an extension of scalars and the morphism g ′ : W → Yk′ . Since f is finite and surjective,
so are f ′ and f ′′ by 2.2, so we may replace X by Z and Y by W to assume X is a smooth,
connected, strictly k-analytic curve for k non-trivially valued and that u ̸≡ −∞. We can
check subharmonicity of u (in Thuillier’s sense) after extending scalars as in the proof of
Proposition 3.5(7), so we may assume in addition that k is perfect.
   Let ι : Yred ,→ Y be the inclusion of the underlying reduced space, and let ν: Ye → Yred be
the normalization. Since k is perfect, the normal curve Ye is rig-smooth, and since Ye → X
is finite and ∂ X = ; (as X is smooth), the curve Ye is smooth as well: see Lemmas 3.8
and 3.9. Both ι and ν are finite and surjective, so f ◦ ι ◦ ν: Ye → X is again finite and
surjective. By Definition 3.4 (with k = k′ ), subharmonicity of u ◦ f means that, on each
connected component C of Ye , the function (u◦ f )◦ι◦ν is either subharmonic in Thuillier’s
sense or is identically −∞. Since C → X is surjective (it is finite, hence it is a closed
map, and it is an open map by [Ber90, Lemma 3.2.4], so its image is all of X since X is
connected), the latter does not happen, so u ◦ f ◦ ι ◦ ν is subharmonic in Thuillier’s sense.
Thus we replace Y by Ye and f by f ◦ ι ◦ ν to assume X and Y are both smooth, and that
u ◦ f is subharmonic in Thuillier’s sense.
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
20                                 W. GUBLER AND J. RABINOFF

of subharmonicity, we have h ≤ h′ on U. By the same argument as applied to −h, we see
that h = h′ on U, so that h is harmonic on U. As U was arbitrary, h is harmonic.
  By 3.12, the following definition recovers Thuillier’s definition of harmonicity on a
smooth, strictly k-analytic curve, and even on a strictly affinoid rig-smooth curve us-
ing [Thu05, Corollaire 2.3.14].
Definition 3.13 (Harmonic functions). Let X be a k-analytic curve for a possibly trivially
valued non-Archimedean field k. A function h: X → R is harmonic if h and −h are both
subharmonic.
   The advantage of this definition is that the following basic properties of harmonic func-
tions follow immediately from the corresponding properties of subharmonic functions.
Proposition 3.14. Let X be a k-analytic curve and let h: X → R be a continuous function.
     (1) (Sheafiness) The harmonic functions form a sheaf on X .
     (2) If f ∈ Γ (X , OX× ) then log | f | is harmonic.
     (3) The harmonic functions on X form a real vector space.
     (4) (Limits) If h is locally a uniform limit of harmonic functions, then it is harmonic.
     (5) (Maximum Principle) If h is harmonic and h attains a local extremum at x ∈ Int(X ),
         then h is constant in a neighborhood of x.
     (6) (Extension of Scalars) Let k′ /k be an analytic extension field. Then h is harmonic
         if and only if h ◦ πk′ /k : X k′ → R is harmonic.
     (7) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If h is
         harmonic then h ◦ f is harmonic, and the converse holds if f is finite and surjective.
     (8) (Boundaries) If h is harmonic on Int(X ), then it is harmonic on X .
   We will later see in Theorem 7.6 that (4) holds even for pointwise limits. The fol-
lowing proposition asserts that Definition 3.13 is equivalent to the notion of harmonicity
in [GJR21, Definition 7.2]. We assume that k is non-trivially valued as in ibid.
Proposition 3.15. Let X be a strictly k-analytic curve and let h: X → R be a continuous
function. The function h is harmonic if and only if it is R-PL and the line bundle Lh (x) ∈
Pic(red(X , x))R defined in (2.17) is numerically trivial for every point x ∈ X .
Proof. This is [GJR21, Proposition 15.7] in the rig-smooth case; we reduce to this case
                                                                         −∞
in the usual way. If char(k) = p > 0 let k′ be the completion of k p , and otherwise let
k′ = k. Let X ′ = X ⊗b k k′ and let π: X ′ → X be the structure morphism. Let ι : X red
                                                                                      ′
                                                                                        ,→ X ′
be the underlying reduced space and let ν: Xe ′ → X red  ′
                                                            be the normalization, so that Xe ′ is
rig-smooth. Let f : Xe ′ → X denote the composition π ◦ ι ◦ ν.
   Suppose that h is harmonic. Then h ◦ f is harmonic by Proposition 3.14(6,7), so h ◦ f
is R-PL and Lh (x ′ ) is numerically trivial for all x ′ ∈ Xe ′ by the rig-smooth case. Then
h is R-PL by Lemma 3.9(6) and [GJR21, Lemma 5.3(3), Corollary 5.11], and Lh (x) is
numerically trivial for all x ∈ X by [GJR21, Proposition 7.6(1′ , 2′ )]. Conversely, suppose
that h is R-PL and that Lh (x) is numerically trivial for all x ∈ X . The same holds for
h ◦ f by [GJR21, Proposition 7.6(1′ , 2′ )], so h ◦ f is harmonic by the rig-smooth case, and
hence h is harmonic by Proposition 3.14(6,7).                                                  □
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


## Published source GR1, PDF pages 21-23

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


## Published source GR1, PDF pages 30-31

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


## Published source GR1, PDF pages 33-34

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


## Published source GR2, PDF pages 4-5

4                                 W. GUBLER AND J. RABINOFF

Rn as introduced above and a smooth function f i : Rn → R such that u|Vi = f i ◦ ϕi,trop on
Vi . We note that R-PL functions are the special case of piecewise smooth functions where
all the f i ’s can be chosen as affine functions.
    In the theory of Chambert-Loir and Ducros [CD12, §5.4], we can associate to every
continuous real function u on X an associated current [u]. The function h is called
plurisubharmonic (or just psh) in the sense of Chambert-Loir and Ducros if the associated
current d′ d′′ [h] is positive. See [CD12, §5.5] for details. Then we can show the following
maximum principle.
Theorem 1.7. Let X be a good, separated, strictly k-analytic space, and let u be a piecewise
smooth function on X which is psh in the sense of Chambert-Loir and Ducros. If u has a
local maximum on x ∈ X \ ∂ X , then u is locally constant at x.
   Since any semipositive R-PL function is psh in the sense of Chambert-Loir and Ducros
[GJR21, Theorem 7.14], the maximum principle holds for semipositive R-PL functions.
We prove Theorem 1.7 by proving a tropical analogue in Theorem 7.4: namely, if C ⊂
Rn is a tropical variety of pure dimension d and if f : C → R is weakly tropically psh,
in the sense that the Lagerberg current d′ d′′ [ f ] is positive, then f satisfies a similar
maximum principle. The proof uses the Bieri–Groves theorem for affinoid varieties given
in Theorem 1.6. Then Theorem 1.7 is shown in Theorem 7.7.
Remark 1.8. We do not know whether an R-PL function that is psh in the sense of
Chambert-Loir and Ducros is necessarily semipositive. This is strongly related to the
question of whether psh functions are stable under pullback, which is likewise unknown.
Acknowledgments. We are very grateful to Antoine Ducros who helped us with the
argument for the local lifting theorem. We thank Mattias Jonsson for comments about
an earlier draft of the paper.

                                    2. PRELIMINARIES
2.1. General Notation and Conventions. Throughout this paper, k will denote a field
that is complete with respect to a nontrivial, non-Archimedean valuation.
   The set of natural numbers N includes 0. We allow equality in a set-theoretic inclusion
S ⊂ T . If P is any abelian group, we let PΛ := P ⊗Z Λ be the tensor product with Λ. For a
field F , we denote by F an algebraic closure of F .
   For a ring A, the group of invertible elements is denoted by A× . A variety over a field
F is an integral scheme which is of finite type and separated over Spec F .
   A topological space is called compact if it is quasi-compact and Hausdorff.
2.2. Non-Archimedean geometry. A non-Archimedean field is a field k endowed with a
non-Archimedean complete absolute value | |: k → R. The corresponding valuation ring
is denoted by k◦ , its unique maximal ideal by k◦◦ and its residue field by ek = k◦ /k◦◦ . An
analytic extension field is a non-Archimedean field k′ equipped with an isometric embed-
ding k ,→ k′ .
   We will use only good Berkovich analytic spaces over k in the terminology from [Ber93].
These are the k-analytic spaces considered in [Ber90]. Here, good means that every
point of the analytic space X has a neighbourhood isomorphic to the Berkovich spectrum
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


## Published source GR2, PDF pages 15-17

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


## Published source Thu, PDF pages 29-30

                                                                                             15



       2. Fon tions harmoniques sur une                      ourbe stri tement
                                     k -analytique lisse



  Dans tout le texte, la notation log désigne le logarithme néperien (ou naturel ).
  Dans e hapitre, k est un orps omplet pour une valeur absolue non ar himédienne |.|,
supposée non triviale. Les éléments de k dont la valeur absolue est inférieure à 1 forment un
sous-anneau k◦ dont le spe tre formel Spf(k◦ ) est noté S . Le orps résiduel de k, quotient de
k◦ par l'idéal maximal k◦◦ = {a ∈ k◦ ; |a| < 1}, est noté ek.
   Après quelques résultats préliminaires sur les espa es k-analytiques, nous allons introduire,
pour toute ourbe k-analytique lisse X , un fais eau d'espa es ve toriels réels HX sur l'espa e
topologique |X| sous-ja ent à X . Par sa dénition même, HX sera un sous-fais eau du fais eau
CX des germes de fon tions réelles ontinues sur |X|, appelé fais eau des germes de fon tions
harmoniques sur X .
   La onstru tion du fais eau HX pro ède d'un raisonnement en quatre étapes.
   Nous expliquons tout d'abord omment asso ier, à toute S - ourbe formelle (stri te-
ment) semi-stable et génériquement lisse X , un sous-espa e H(X ) de l'espa e ve toriel réel
C0 (|Xη |, R).
   Étant donnée une extension non ar himédienne K de k, désignons par C/K la atégo-
rie ayant pour objets les Spf(K ◦ )- ourbes stri tement semi-stables, génériquement lisses et
quasi- ompa t, et dont les morphismes entre X et X ′ sont les isomorphismes de l'espa e K -
analytique Xη sur un domaine K -analytique de Xη′ . La orrespondan e X 7→ H(X ) dénit un
sous-fon teur du fon teur

                                  (C/K)op → VectR
                                         X   7→ C0 (|Xη |, R)

 ompatible  en un sens à pré iser  à l'a tion du groupe de Galois d'une extension galoisienne
nie K ′ /K .
   Invoquant le théorème de rédu tion semi-stable ([9℄), nous obtenons, pour toute ourbe
k-analytique lisse X , un préfais eau HX sur le G-site de X dont la valeur sur un domaine
k-analytique Y de X , isomorphe à la bre générique d'une S - ourbe (formelle) simplement
nodale Y , est H(Y). Ce préfais eau est un sous-préfais eau du fais eau C0 (., R).
   Le préfais eau HX sur le G-site d'une ourbe k-analytique lisse X n'est pas un fais eau.
Le site déni par l'espa e topologique |X| est naturellement un  sous-site  du G-site de X
et la onstru tion s'a hève en vériant que le préfais eau HX sur |X| induit par HX est un
fais eau.



                               2.1. Résultats préliminaires
   Nous ommençons par rassembler divers résultats de géométrie analytique non ar himé-
dienne dont nous aurons besoin et en protons pour introduire un ertain nombre de nota-
tions. Rappelons que, pour tout espa e lo alement annelé X = (|X|, OX ) et tout point x de
|X|, le orps résiduel de l'anneau lo al OX,x se note κ(x).
16



2.1.1. S hémas formels et espa es analytiques.
  Nous renvoyons au livre [3℄ et à l'arti le [4℄ pour les fondements de la géométrie analytique
sur un orps non ar himédien.
  Rappelons tout d'abord que, pour tous réels stri tement positifs r1 , . . . , rn ,
                                         k{r1−1 T1 , . . . , rn−1 Tn }
est la k-algèbre de Bana h des séries formelles
                                X                X
                           f=        aν (f )Tν =   aν T1ν1 . . . Tnνn
                                  ν∈Nn                    ν∈Nn

telles que |aν (f )|rν = |aν |r1ν1 . . . rnνn tende vers 0 lorsque |ν| = ν1 + . . . + νn tend vers +∞,
munie de la norme
                                          ||f || = max |aν |rν .
                                                      ν

Semi-norme spe trale.
   Soit A une k◦ -algèbre topologiquement de présentation nie et plate, de spe tre formel
X = Spf(A). Le sous-k◦ -module A de A = A ⊗k◦ k munit A d'une stru ture de k-algèbre de
Bana h via la norme
                                   |a|A = inf{|λ| ; a ∈ λA}.
La bre générique de X est l'espa e stri tement k-anoïde M(A), noté Xη ; on rappelle qu'il
s'agit de l'ensemble des semi-normes multipli ativeset bornées sur la k-algèbre de Bana h A
qui induise la valeur absolue |.| sur k, muni de la topologie la moins ne rendant ontinues
les évaluations x 7→ |a(x)| = x(a), a ∈ A. Le noyau px d'une semi-norme multipli ative
x : A → R≥0 est un idéal premier de A et l'on note H(x) la omplétion du orps des fra tions
de l'anneau intègre A/px pour la valeur absolue induite par x. Ce orps est le orps résiduel
 omplété du point x de X .
Proposition 2.1.1.  La semi-norme spe trale sur A oïn ide ave la norme |.|A asso iée
au sous-k◦ -module A si et seulement si la ek-algèbre A ⊗k◦ ek est réduite.
Démonstration. La semi-norme spe trale |.|sp sur A s'obtient par la formule limite usuelle
à partir de toute norme ||.|| dénissant la stru ture de k-algèbre de Bana h de A :
                                         |a|sp = lim ||an ||1/n ,
                                                     n
et elle oïn ide ave ||.|| si et seulement si ette norme est pré-multipli ative, 'est-à-dire vérie
||an || = ||a||n pour tous a ∈ A, n ∈ N. Appliquant e i à la norme |.|A asso iée au sous k◦ -
module A de A, il sut de vérier que ette norme est pré-multipli ative si et seulement si la
e
k-algèbre A ⊗k◦ e  k est réduite. Puisque la norme |.|A est à valeurs dans |k| ([8℄, 6.1.1, prop.2),
sa pré-multipli ativité équivaut à la ondition 1 ≤ |xn |A pour tout x ∈ A tel que |x|A = 1.
La véri ation est immédiate : il existe x ∈ A et n > 1 tels que |x|A = 1 et |xn |A < 1 si et
seulement s'il existe x e ∈ A ⊗k ◦ ek et n > 1 tels que xe 6= 0, xen = 0. La norme |.|A est ainsi
pré-multipli ative si et seulement si la ek-algèbre A ⊗k◦ e k est réduite.                        2
   La boule unité de A pour la norme spe trale se note A◦ et l'on introduit également l'idéal
A◦◦ = {a ∈ A ; |a|sp < 1} ; le quotient A e = A◦ /A◦◦ est une e
                                                              k-algèbre de type ni et réduite
( ette dernière propriété provient de la pré-multipli ativité de la norme spe trale). La k◦ -
algèbre A◦ n'est en général pas topologiquement de présentation nie sur k◦ ; 'est toutefois
le as lorsque la k-algèbre A est réduite et que l'une des onditions suivantes est vériée :
    la valuation de k est dis rète (Tate) ;


## Published source Thu, PDF pages 75-76

                                                                                              61



                              3. Théorie du potentiel



                              3.1. Le problème de Diri hlet
  Dans e qui suit, X est une ourbe stri tement k-analytique lisse.
3.1.1. Propriétés fondamentales des fon tions harmoniques.
  Les se tions du fais eau HX satisfont au prin ipe du maximum.
Proposition 3.1.1.  Étant donné un ouvert Ω de X , une fon tion h ∈ Γ(Ω, HX ) admet
un extremum lo al en un point x de Ω si et seulement si elle est onstante au voisinage de x.
  C'est la onjon tion de la proposition 2.3.13 et du orollaire 2.3.14.
   Le problème de Diri hlet est lo alement résoluble : tout point x ∈ X admet un système
fondamental de voisinages ouverts relativement ompa ts Ω tels que l'appli ation de restri tion
                              C0 (Ω, R) ∩ Γ(Ω, HX ) → C0 (∂Ω, R)
soit un isomorphisme. Il sut en eet de prendre pour Ω l'intérieur d'un voisinage stri tement
k-anoïde Y de x dans X et d'appliquer le lemme 2.3.9.
  Le prin ipe de Harna k est valide
Proposition 3.1.2.  Soient Ω un ouvert onnexe de X et (Ωn ) une suite d'ouverts de
X telle que haque point de Ω admette un voisinage ontenu dans presque tous les Ωn : quelle
que soit la suite roissante de fon tions hn ∈ Γ(Ωn , HX ), l'alternative est la suivante :
   soit (hn ) onverge vers +∞ uniformément sur tout ompa t de Ω,

   soit (hn ) onverge vers une fon tion h ∈ Γ(Ω, HX ), uniformément sur tout ompa t de
     Ω.
Démonstration. Puisque tout point de x admet un système fondamental de voisinages stri -
tement k-anoïdes, il dé oule du lemme 2.3.10 que l'ensemble U (resp. U ′ = Ω−U ) des points
de Ω en lesquels la suite (hn ) est majorée (resp. n'est pas majorée) est une partie ouverte ; de
plus, toujours par appli ation de e lemme, la suite (hn ) onverge
   lo alement uniformément vers ∞ sur U ′ ;
   lo alement uniformément sur U vers une fon tion h  né essairement ontinue  telle que,
     pour tout domaine stri tement k-anoïde Y de Ω, la restri tion de h à Y appartienne à
     H(Y ) ; vu la dénition du fais eau HX (2.3.3), la fon tion h est harmonique sur Ω.
                                                                                               2
   Notons également le résultat de onvergen e suivant :
Proposition 3.1.3.  Soient Ω un ouvert de X et (hn ) une suite de fon tions harmo-
niques sur Ω ; si la suite (hn ) est lo alement bornée, on peut en extraire une sous-suite onver-
geant, lo alement uniformément sur Ω, vers une fon tion harmonique.
Démonstration. Nous démontrerons au orollaire 3.3.7 que toute famille lo alement bornée
de fon tions harmoniques sur Ω est automatiquement équi ontinue en tout point de Ω ; bien
entendu, la proposition ne sera pas utilisée d'i i là. Appliquant le théorème d'As oli, on peut
extraire une sous-suite de (hn ) qui onverge lo alement uniformément.
   Il est fa ile de vérier qu'une limite lo alement uniforme de fon tions harmoniques est
harmonique : pour tout domaine k-anoïde V de X , le sous-espa e Γ(V − ∂V ) ∩ C0 (V, R) de
l'espa e de Bana h C0 (V, R) est fermé ar 'est un espa e ve toriel de dimension nie.          2
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


## Published source Thu, PDF pages 78-78

64



puisque Y est onnexe et h non onstante, le prin ipe du maximum pour les fon tions harmo-
niques impliquerait alors h|Y −Γ(Y ) < u(x) et don , par sous-harmoni ité, l'inégalité absurde
u(x) ≤ h(x) < u(x).
   La on lusion est maintenant immédiate : l'ensemble des points de Shilov des voisinages
stri tement k-anoïdes onnexes de x dans U étant une partie dense de U , la fon tion semi-
 ontinue supérieurement u|U est onstante, égale à u(x).                                     2

Corollaire 3.1.12.  Soient Ω ⊂ X un ouvert et u : Ω → R ∪ {−∞} une fon tion semi-
 ontinue supérieurement qui n'est identiquement égale à −∞ sur au une omposante onnexe
de Ω. Les propriétés suivantes sont équivalentes :
   (i ) u est sous-harmonique ;
   (ii ) pour tout ouvert Ω′ ⊂ Ω et pour toute fon tion harmonique h sur Ω′ , la fon tion u|Ω′ −h
satisfait au prin ipe du maximum (proposition 3.1.11) sur Ω′ .
Démonstration. L'impli ation (i) ⇒ (ii) est l'appli ation dire te de la proposition pré é-
dente puisque toute fon tion harmonique est sous-harmonique.
   L'impli ation ré iproque est immédiate : étant donnés un domaine stri tement k-anoïde
V ⊂ Ω et une fon tion h ∈ H(V ) telle que u|∂V ≤ h|∂V , l'appli ation du prin ipe du maximum
à la fon tion u − h sur v − ∂V implique que elle- i atteint son maximum en un point de ∂V ;
elle est don négative. La fon tion u est bien sous-harmonique sur Ω.                            2
   La reformulation pré édente de la dénition 3.1.5 met en éviden e le ara tère lo al de la
sous-harmoni ité.

Corollaire 3.1.13.  Le préfais eau SH sur |X| est un fais eau.

Démonstration. La semi- ontinuité supérieure et le fait de ne pas être identiquement −∞
sur une omposante onnexe sont des propriétés de nature lo ale. La propriété (ii) du orollaire
pré édent est également de nature lo ale.                                                  2

Proposition 3.1.14.  Soit X une ourbe stri tement k -analytique lisse. Étant donnés
une ourbe stri tement k-analytique lisse Y , un morphisme f : Y → X et une fon tion sous-
harmonique u sur X , la fon tion f ∗ u = u ◦ f est sous-harmonique ou identiquement égale à
−∞ sur haque omposante onnexe de Y .
Démonstration.
La ourbe Y peut être supposée onnexe et, l'assertion étant évidente pour un morphisme
 onstant, il sut de traiter le as d'un morphisme quasi-ni.
   Soit u une fon tion sous-harmonique sur X ; puisqu'il est loisible de se lo aliser sur Y pour
établir la sous-harmoni ité de f ∗ u, on peut supposer que le morphisme f est ni. Considérons
alors un domaine stri tement k-anoïde V ⊂ Y et une fon tion h dans H(V ) qui oïn ide
ave f ∗ u sur ∂V = Γ(V ) ; W = f (V ) est un domaine stri tement k-anoïde dans X tel que
f −1 (∂W ) = ∂V en vertu des proposition 3.1.3 (ii) et orollaire 2.5.13 (i) de [3℄ (la première
implique ∂V = f −1 (∂W ) ∩ (V − Int(f )), la se onde fournit l'égalité Int(f ) = V ).
   Soit h′ la fon tion dans H(W ) qui oïn ide ave u sur ∂W . La fon tion f ∗ h′ appartient à
H(f −1 (W )) (proposition 2.3.19) et est égale à h sur ∂f −1 (W ) = ∂V ; le prin ipe du maximum
implique alors l'identité h = f ∗ h′ , d'où dé oule l'inégalité
                                        f ∗ u ≤ f ∗ h = h′
en vertu de la sous-harmoni ité de u.                                                          2

Remarque 3.1.15.  Soit Ω un ouvert relativement ompa t de X ; toute fon tion sous-
harmonique u sur Ω se prolonge de façon unique en une fon tion semi- ontinue supérieurement


## Published source Thu, PDF pages 105-105

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


## Published source GJR, PDF pages 30-32

30                              W. GUBLER, P. JELL, AND J. RABINOFF

x ∈ NΓ . Then Sϕ (X ) ∩ X ω is the Shilov boundary of X ω by Remark 3.19. Hence we
may assume x ∈ Sϕ (X ) ∩ X ω as otherwise all tropical multiplicities are zero. Using the
notations of 4.14, we let Ke (C x ) denote the function field of C x . The homomorphism
                                                  ∼
Aω → H (x) induces an isomorphism K     e (C x ) −→ Hf(x) by [Ber90, Proposition 2.4.4(ii)].
                            ◦                                                            e (M
By the definition of Aω ⊂ Aω , the function field of ιs (C x ) is precisely the subfield K  e (x))
of Remark 3.8. We have length(OX ,x ) = 1 because X is reduced, so
                                f(x) : K
                  mϕ (X , x) = [H      e (M
                                          e (x))] = [C x : ι(C x )] = mrel (x)
by Remark 4.2(8).                                                                              
Example 4.16 (Continuation of Example 3.15). We continue with the notation in Exam-
ple 3.15. By [BPR16, Theorem 5.8], for any point P in the interior of an edge e in the
skeleton S, the relative multiplicity mrel (P) is equal to the “expansion factor” of the edge e
with respect to the tropicalization map ϕtrop . In this situation, the expansion factor of
every edge is equal to 1, except for the edge BD, which has expansion factor 0 as it is
crushed to a point.
   We claim that mϕ (X , P) = 1 for P ∈ {A, B, C, D}. This can be checked directly from
the definition of mϕ (X , P). We give the proof in case P = A which reduces to the generic
point of the line x = 0 in the special fiber of Xmin . By [Ber90, Proposition 2.4.4(ii)],
we have H  f(A) = K e ( y). Recall that trop(A) = (1, 0). If M = Z2 be the character lattice
of T = G2m , then Ke ( M(A))
                       e      is the subfield of H f(A) generated by the reductions of x/p
and of y/1 = y. This shows H     f(A) = K e (M
                                             e (A)), and hence 4.2(8) yields that mϕ (X , A) =
[Hf(A) : K
         e (Me (A))] = 1. The proof for the points P = B, C, D is similar.
   We conclude that mrel (P) = mϕ (X , P) = 1 for every point P of Sϕ (X ). It follows that
mϕ (X , ω) just counts the preimages of ω in Sϕ (X ) under ϕtrop ; these tropical multiplicities
are indicated in Figure 1.

                              5. PIECEWISE LINEAR FUNCTIONS
   In this section we discuss piecewise linear functions on analytic spaces. Most of these
results are standard in one form or another: for instance, see [CD12, Gub98, GM19].
However, the terminology in the literature is somewhat nonstandard, so it is important
to fix our ideas. We will find it useful to work slightly more generally with piecewise
linear functions with slopes contained in an additive subgroup Λ ⊂ R, and in some cases
new arguments are needed. In practice we will usually take Λ = Z, Q, or R, in which case
either Λ = Z or Λ is divisible.
   In this section, K is a non-Archimedean field with a non-trivial valuation v and value
group Γ := v(K × ) ⊂ R. We consider a good strictly K-analytic space X and an additive
subgroup Λ ⊂ R. Recall from 2.3 that a strictly analytic space is good provided that that
every point has a strictly affinoid neighbourhood. Most strictly analytic spaces occurring
in practice are good: for example, any strictly affinoid space, a space with no boundary,
or an analytic subdomain of the analytification of an algebraic variety. We restrict our
attention to good spaces as then the coherent modules on the Berkovich space X are
the same as the coherent modules on the space X G endowed with the G-topology [Ber93,
Proposition 1.3.4], which makes it reasonable to work with line bundles on X . We always
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


## Published source GJR, PDF pages 34-36

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


## Published source GJR, PDF pages 44-47

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


## Published source Ber, PDF pages 22-23

            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                              25

exists i e l such that V C ^ ( X J and ^"^(V) is a O-affinoid domain in X^ (in this
case ^^(V) is a 0-affinoid domain in X^. for any ^ with V C ^.(X^.)). It is easy to see
that T is a net, and there is an evident 0^-afnnoid atlas ^/ with the net X. In this way
we get a 0^-analytic space (X, ja^, r) that satisfies the properties (1)-(4). That X is
unique up to canonical isomorphism follows from Proposition 1.3.2. •
       Let X be a 0^-analytic space. The family of its 0-analytic domains can be considered
as a category, and it gives rise to a Grothendieck topology generated by the pretopology
for which the set of coverings of an analytic domain Y C X is formed by the families
{^i }z e i °^ ^^y^ domains in Y that are quasinets on Y. For brevity, the above
Grothendieck topology is called the G-topology on X, and the corresponding site is
denoted by X^. From Proposition 1.3.2 it follows that any representable presheaf
on XQ is a sheaf. The G-topology on X is a natural framework for working with coherent
sheaves.
       Recall ([Ber], 1.5) that the Tz-dimensional affine space A71 is the set of all mul-
tiplicative semi-norm on the ring of polynomials A[T^, . . ., TyJ that extend the valuation
on k endowed with the evident topology. The family of closed polydiscs with center at
zero E(0; r^, . .., rj == { x e A71 | | T^(^)| ^ r^ 1 ^ i ^ n} defines a ^-affinoid atlas on A".
 (We remark that A71 is a good ^-analytic space.) We remark that the affine line A1 is a ring
object of the category k-^/n. I f X = = e^(j^) is a ^-affinoid space, then Hom(X, A1) = ja^.
       We return to 0-analytic spaces. Applying Proposition 1.3.2 to X' = A1 and the
category k-^/n, we get a structural sheaf (9^ on X^ (this is a sheaf of rings). The category
of (P^-modules is denoted by Mod(Xo). An fl^-module is said to be coherent if there
exists a quasinet T of 0-affinoid domains in X such that, for each V e T, fl^o |vo ls lso"
morphic to the cokernel of a homomorphism of free ^vo"1110^11^15 °f finite rank. For
example, suppose that X = e^(J^) is a 0^-affinoid space. Then a finite j^-module M
defines a coherent (P^{M) by V i - ^ M ® ^ j ^ v , and KiehPs Theorem tells that any
coherent O^-module is isomorphic to (P^(M.) for some M. The latter fact enables one
to define for a coherent (P^mod\i\e F the suppvrt Supp(F) of F. Namely, if X = e^(j^)
is ^-affinoid and F = 6^(M), then Supp(F) is the support of the annihilator of M.
 IfX is arbitrary, then Supp(F) is the set of point x e X such that for some (and therefore
for any) affinoid domain V that contains x the support ofF|^ contains x. Let Coh(X^)
denote the category of coherent 0^-modvles, and let Pic(X^) denote the Picard group
of invertible (P^-modu\es, (One has Pic(X^) == H^X^, 0^).) From KiehPs Theorem
it follows that Coh(XJ and Pic(X^) are the same whether X is considered as an object
 of O^-J^TZ or of k's/n.
        We now consider connection of the above objects with their analogs in the usual
 topology of X. For this we assume that the class O^ is dense. Then all open subsets of X are
0-analytic domains, and there is a morphism of G-topological spaces TT : X^ -^ X which
induces a morphism of the corresponding topoi (^, TC*) : X^ -> X^. The direct image
functor TC^ is simply the restriction functor. In particular, we have the structural sheaf
 0^: == TT^ 0^ on X. The functor TT^ is not fully faithful (see Remark 1.3.8). The inverse
                                                                                           4
26                               VLADIMIR G. BERKOVICH

image functor TC* is as follows. For a sheaf F on X and a 0-affinoid (or 0-special) domain,
one has
                 ^ F(V) = lim F(^),
                             ^3V

where ^ runs through open neighborhoods of V. It is easy to see that F -S- 7^ TT* F.
In particular, the functor TT* is fully faithful.
      Let Mod(X) denote the category of ^-"^dules. The functor TT^ defines an evident
functor Mod(X^) -> Mod(X). The natural functor in the inverse direction is as follows:
                 Mod(X) ~> Mod(X^) : F ^ F^ = TT* F ®,^ ^.
An ^x"1110^^ is said to be coherent if locally (in the usual topology of X) it is isomorphic
to the cokernel of a homomorphism of free modules of finite rank. (For example, if
X =^(c^) is O^-affinoid, then 0^{M) :== TC* ^xoW is a coherent (P^-module.) The
Picard group Pic(X) is the group ofinvertible (P^-mod\i].es. One has Pic(X) = H^X, (P^).

      1.3.4. Proposition. — IfX is a good <£^-analytic space, then
      (i) for any 0^-module F one has F -^ TT^ F^; w particular, the functor
                 Mod(X) -> Mod(XJ : F h-> F^

t^ y^^ faithful',
      (ii) ^ functor F h-> F^ induces an equivalence of categories Goh(X) ^> Goh(X^);
      (iii) a coherent Q^-module F is locally free if and only if F^ is locally free.

        Proof. — (i) It suffices to verify that for any point x e X there is an isomorphism of
stalks F^ -^ (^ Fo)a;. But this easily follows from the definitions because x has an affinoid
neighborhood.
        (ii) By (i), it suffices to verify that for a coherent (P^-mod\ile ^ the C}^-mod\ii.e
F = TT^ y is coherent and F^ ^ y. This also follows easily from the definitions.
        (iii) We may assume that X = «^(J^) is ^-affinoid. It suffices to show that a
finite j^-module M is projective if and only if the (P^'module (P^{M) is locally free.
The direct implication is simple. Conversely, suppose that for some finite affinoid cove-
ring { V, },^ i of X the finite J^y, -modules M ®^ c^. are free. It suffices to verify that M
is flat over s/. For this we take an injective homomorphism of finite j^-modules P —> Q^.
Then the homomorphisms (M ®^ P) ®^ ^^ -> (M ®^ QJ ®^r J^v, are also mjective.
Applying Tate's Acyclicity Theorem to the finite e^-modules M®^P and M®^Q,
we obtain the injectivity of the homomorphism M ®^ P -> M ®^ Q^. •
      1.3.5. Corollary. — If X is a good <J)^-analytic space, then there is an isomorphism
Pic(X)^Pic(XJ. •

      The structural sheaf 0^ will be used only for good spaces X. The group Pic(X^)
will appear in Corollary 4.3.8. We now compare the cohomology groups in both
topologies.


## Published source Ber, PDF pages 31-32

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


## Published source Ber, PDF pages 36-40

            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                             39

       Proof. — It suffices to show that for any pair of affinoid subdomains V C X' and
U C X with <p(V) C U, ^ is a flat ^'algebra. By Lemma 2.1.2, ^-i(u) = ^n® K
is a flat J^-algebra. Since ^y is a flat ja^-i^-algebra ([Ber], 2.2.4 (ii)), then ^ is
a flat <^j-algebra. •
       We now consider an arbitrary A-affinoid algebra ^. We can take a non-Archi-
medean field K over k such that the algebra ^ ' == ^S)K is strictly K-affinoid. By
the previous case, the map X' == e^(j^') -^' = Spec(^) is surjective, and, by
Lemma 2.1.2, the map S K ' -> SE is surjective. It follows that the map n is surjective. •

      3.1.4. Theorem. — The ring ^x,» ls a Noetherian ring faithfully flat over (9^x = j^ .

      Proof. — Suppose first that the valuation of A is nontrivial, the algebra ^ is strictly
A-affinoid and x e Max(J^). In this case 0^ ^ coincides with the algebra of germs of affinoid
functions on Max(^) considered in [BGR], 7.3.2. By [BGR], 7.3.2/7, the ring C^ ^
Noetherian, and, by [BGR], 7.3.2/3, there is an isomorphism ^ ^> ^ ^ ^ ^x x between
^x? Px ^x 5 "^^^^^"^P^tionsofthe rings ^, ^ <g>^ ^x,^ respectively. By [Mat], 8.14,
the ring ^ ^ ^ 0^ ^ is faithfully flat over ^^ and (9^ ^.
       We now consider the general case. We can find a non-Archimedean field K over k
with nontrivial valuation such that the algebra ^f = ^ §) K is strictly K-affinoid,
and there exists a point x ' e Max(ja^') which goes to x under the canonical map
X' = jy{^) ^ X. By Lemma 2.1.2 (resp. Corollay 2.1.3), the algebra e^, (resp. 0^^.)
is faithfully flat over ^ ^ (resp. fix,J- Since ^x',sc' ls faithfully flat over s/^ ,, then O^y,
is faithfully flat over <^^. Furthermore, Corollary 2.1.3 implies that a = a^,a;' n ^x,.e
for any finitely generated ideal a e 0^ ^. From this it follows easily that 0^ ^ is a Noe-
therian ring. •

      2.1.5. Theorem, — The ring 0^^ is Henselian.

       Proof. — We use the following criterion for a local ring A to be Henselian (see [Riay],
1.1.5). A is Henselian if and only if any finite free A-algebra B is a direct product of
local rings.
       Let B be a finite free O^ ^-algebra. We claim that there exist an affinoid neigh-
borhood U of the point x and a finite free j^j-algebra 3S such that B == S8®^ ^x,a;-
Indeed, let b^ . . . , & » be free generators of the 0^ ^-module B and set 1 === SSLi ^ ^
and ^^.==S^.i^^, where ^, a^ e 0^^. The fact that B is an associative and
commutative ring with identity is equivalent to certain identities between the coeffi-
cients ^ and a^. Take a sufficiently small affinoid neighborhood U of the point x
such that all the a^ a^ come from j^j and all the identities are true in .^j. Consider
the free j^j-module 3S == ^/^j b^ + ... + «^u ^» and endow it with the multiplication
^ ^ . = = S ^ i ^ ^ . Then SS is a finite free <a^j-algebra, and, by construction,
B=^®^^.
40                                VLADIMIR G. BERKOVICH

       Furthermore, we may assume that U == X and consider SS as a finite Banach
s/- algebra (see [Ber], 2.1.12). Then we have a finite morphism of A-affinoid spaces
9 : Y = ^fi{88} -> X, and the theorem follows from the following lemma.

       2.1.6. Lemma. — Let <p : Y = ^[S8) -> X == ^{^/) be a finite morphism ofk-affinoid
spaces. Then for any point x e X there is an isomorphism of rings SS®^ Q^^ == FIf^ ^Y,v wner€
^-l{x} ==0i, ...,J^}.

       Proof. — Since 9 is a map of compact spaces, one has y^U) = Uf^i V,, for any
sufficiently small affinoid neighborhood U of x, where V^ are affinoid neighborhoods
of the points y^ such that V, n V, == 0 for i =(= j. Moreover, the domains V^ form a
basis of affinoid neighborhoods ofj^. We have

                 ^^ ^x,. == ^-i(V)^u ^,.= H 38^^ Q^
                                          1=1

Here we used the equality 8S^\.^ == SS ®^ s/^ == 3S ®^ j^^ which follows from the fact
that ^ is a finite Banach e^-module. Therefore, S9®^ 0^^ == IIf^^ ^Y.v,-            •

2.2. Comparison of properties of 0^^ and fi^,

      Let P be a property of local rings which is preserved under localizations with
respect to the complements to prime ideals. A commutative ring A is said to possess
the property P (or A is a P-ring) if all of the local rings A^ , where p runs through prime
ideals of A, possess the property P. More generally, let Y be a locally ringed space. The
set of points y e Y such that (P^y is a P-ring is denoted by P(Y). If P(Y) == Y, then Y
is said to possess the property P.

        2.2.1. Theorem. — Let P be the property of being Red (reduced). Nor (normal), Reg
  (regular), CI (complete intersection), Gor (Gorenstein), CM (Cohen-Macauley). Then P(X)
 is Zariski open in X and P(X) = Tr-^P^)).

       For the definition of these properties and the verification of the fact that P is pre-
 served under localizations see Matsumura's book [Mat]. We shall deduce Theorem 2.2.1
 from known results which are formulated in the following lemmas.

      2.2.2. Lemma. — Let (A, m) -> (B, n) be a faithfully flat homomorphism of local
 Noetherian rings.

       (i) If^ B is a P-ring, then so is A.
       (ii) If A is a P-ring, where P =4= Red, Nor, and n == mB, then B is a P-ring. •

       2.2.3. Lemma. -— Strictly k-afjinoid algebras are excellent rings. •
            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                              41

      2.2.4. Lemma. — Let A be an excellent ring.
      (i) If (p is a prime ideal of A such that Ay is a f-ring, where P = Red or Nor, then the
completion ^p is a 'P-ring.
      (ii) The set of prime ideals (p C A such that Ay is a 'P-ring is open in Spec (A), •

      For Lemma 2.2.2 and the assertion (ii) of Lemma 2.2.4 in the cases P = GI
or Gor see [Mat], § 23-24. Lemma 2.2.3 is proved in [Kiej. The assertions (i) and (ii)
(for P + CI, Gor) of Lemma 2.2.4 are proved in [EGAIV], 7.8.3.
      Proof of Theorem 2.2.1. — From Theorem 2.1.4 and Lemma 2.2.2 (i) it follows
that P(X) C Tr-^P^)). Let A; be a point of X such that J3^ is a P-ring. We have to
show that (P^ „ ls a P-ring.
      Suppose that the valuation ofk is nontrivial and the algebra s/ is strictly A-affinoid.
From Lemmas 2 . 2 . 3 and 2 . 2 . 4 it follows that the set P(<^) is open in SO\ Furthermore,
if x e Max(e^), then ja^p == ^x,^ B"^ therefore B^ ^ is a P-ring. Let x be an arbitrary
point. Since P(^) is open in St', then V C ^~1('P{^!')) for any sufficiently small strictly
aiffinoid neighborhood V of x. IS y e Max(J^y) ^ Max(^), then fi^^y) is a P-ring, and
therefore C^, yls a P-ring. Since (9^ y = ffly ^, then O^^y) is a P-ring, where i^ = Spec(^y)-
It follows that P(^) == ^ because P(^r) is open in Y^. Thus, the algebras ja^y are P-rings
for all sufficientiy small strictly affinoid neighborhoods V of x. Since fl^a; = limj^y,
then fi^ x ls a P-ring. Indeed, this is evident if P == Red or Nor. If P =1= Red, Nor, we
remark that m^ = ^x v ^x a; ^or a sufficiently small strictly affinoid neighborhood V
of x, where px v ls t^le prime ideal of ^/y corresponding to the point x. From
Lemma 2 . 2 . 2 (ii) it follows that €^ ^ is a P-ring.
       We remark that (under the same assumptions) the fact already verified implies
that the subsheaf of ideals ^x ^ ^x consisting of nilpotent elements is coherent and, in
fact, is generated by the nilradical rad(J^) ofj3^. Furthermore, ifX is reduced, then the
subsheaf ^orm of the sheaf e^x °f meromorphic functions consisting of elements, whose
images in all stalks e^x x are integral over fi^ x^ ls coherent, and there exists a e e^,
which is not a zero divisor, such that ^^orm C fi^ •
       We now consider the general case.
      2.2.5. Lemma. — Let K be a field of the form Ky     ,. (see [Ber], § 2 . 1 ^ and
^' ==. ^(§ K. Consider the map a : X -> X' == Ji^'} which sends a point x eX. to the
point x' e X' corresponding to the multiplicative semi-norm S^, a^ T^ i-» max [ ^(^) | r\    TA^^
^, == px^'- Furthermore, if Y' z^ <z Zariski closed subset of X', ^TZ (T'^Y') ij- a Zariski
closed subset of X.

      Proo/*. — Letyi, ' - ")fn be generators of px* Since the canonical epimorphism
^ -^ Px : (^i? • • •? ^n) '-^ ^=1 ^^ ls admissible (see [Ber], 2.1.9), there exists a
 w

constant G > 0 such that any element a e ^ can be represented in the form S^i a,f,
with [I a,\\ < C [[ a |[, 1 ^ i^ n. Let a' = S^ ^ T^ e px" By construction, all the a^
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


## Published source Ber, PDF pages 48-51

            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                              51

field K{x) k8 is everywhere dense in K(^') and the both fields are quasicomplete, from
Corollary 2.4.2 it follows that G^')^G^^. Therefore there is an exact sequence
                  0 -> G^, ^ G^, -> G(K(^) k8^)) -> 0.

The latter group is a closed subgroup ofG^ and hence its cohomological dimension is at
most cd,{k). It follows that cd,(K^)) ^ cd^k) + cd,(K(^)). Since d^x')^) = d{K(x)lk),
Lemma 2 . 5 . 4 implies that cd;(K(A;')) = d(yi{x)jk).
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
52                              VLADIMIR G. BERKOVICH

      Proof. — By Proposition 2.1.1, the map X ->S£ is surjective. Therefore to show
that the map TC : Y —> W is surjective, it suffices to verify that for any point x e X the
map Y^ -> W^ is surjective. One has
                 Y^^^oo^))"1.

Since the morphism of schemes ^ ®kw J^(•v) -^ ^x ls faithfully flat, the situation is
reduced to the case when X ==^(A). In this case it suffices to verify that if W is an
irreducible affine scheme of finite type over k and y is its generic point, then there exists
a point y e Y whose image in W is y. The Noether Normalization Lemma reduces the
problem to the case when W is the affine space A^. In this case, for any point y e Y == A^
associated with a closed polydisc, 7c(j) is the generic point of W = A^.

      2.6.3. Lemma. — The map TT : Y == ^an -> W induces a bijection

                 Yo^o^y^lE^y)^]^}.
J/*j/eYo, then there is an isomorphism of completions ^y-^^y^.

      Proof. — Let y e^o. For n^ 1 we set .2T == Spec(^y/m;*). The scheme S
consists of one point z and is finite over k. Therefore Z = ^an consists of one point 2,
and one has ^ , == ^ y/n1^ r> ^z,»• Furthermore, there is a canonical closed immersion
S -> ^ which takes z to y. Therefore Z -> Y is also a closed immersion, and the
point y^ which is the image of z in Y, is the only preimage of y in Y. (In particular,
YQ ^ ^o.) Moreover, one has
                  ^y/my^^-^Jm;^.

If n == 1, we get m.y == niy (Py^y and ^(y) == K(j^). Hence ^ y r^ ff^y. •
       From Lemma 2.6.3 it follows that fi^ y is flat over ^ y at least in the case when
y eYg. In the general case we take a sufficiently big non-Archimedean field K over k
such that there exists a K-point y ' e Y' = Y <§ K over j/. We set X' == ^(^ (§> K) and
 3;' == Spec(^K). One has Y' == ^'an, where ^/ == W x ^ y S " . Let y' be the image
 of the pointy in W. We know that tfy^ is flat over fl^y- Since ^' is faithfully flat
 over 3C (Lemma 2.1.2), it follows that 0<y'^ is flat over ^y, and therefore ^y'.v' ls
 flat over ^ y . Finally, from Corollary 2.1.3 it follows that 0^,^ is faithfully flat
 over ^y. Hence (Py ^ is flat over fl^y •

       2.6.4. Proposition. — Let T be a constructive subset of W. Then TTT^T) === ^(T).

       2.6.5. Lemma. — Suppose that W is affine of finite type over X. Let y, z ^ points ofW
 with z ey, and let z be a point of°H^ with n{z) == z. TA^ any open neighborhood of z contains
 a point y with ^{jy) = y.

       Proof. — For a non-Archimedean field K over k, we set ^ ' ==== A (§ K, X' == ^(^'),
 ^' == Spec(^), ^' ==W X y S " . Since ^' is faithfully flat over ^, there exists points
           STALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                            53

y', z' e W over y and z, respectively, with z' e y'. Since the tensor product K{z) ®^ A(z')
is nontrivial, the valuation on K{z) extends to a multiplicative seminorm on it. It follows
that there exists a point z ' e ^'an whose image in W is z' and in ^an is z. Thus, we can
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
is true when 3S is an open subscheme of W and, i f { ^ } ^ j is Jan open covering of ^,
then { ^an }^ j is an open covering of ^an. Hence the situation is reduced to the case
when W = Spec(B) and 3S == Spec(G) are affine schemes of finite type over SK. The
inclusion ^(S^) C -n:"1^^)) is evident. To verify the converse inclusion, it suffices
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


## Published source Ber, PDF pages 64-66

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
68                                   VLADIMIR G. BERKOVICH

      3.5.4. Corollary. — Let 9 : Y -> X be a smooth morphism between good k-analytic spaces.
Then 9 is flat, and t2y/x ls ^ locally free (!)^-module whose rank at a point y e Y is equal to the
dimension of 9 at y. •

      3.5.5. Lemma. — Suppose we are given a cartesian diagram

                  Y    -^ X
                  A          A

                   r         r
                  Y' -^ X'

wA^ 9 ^ a G-locally closed immersion and f is flat fuasijinite. Then f^^^V^^) ^^Y'Q/XG'

       Proof, — We may assume that all the spaces are A-affinoid, 9 is a closed immersion,
and/is a finite morphism. Let X = ^(^), Y = Ji{39}, X' == ^(^') and Y' == ^T(^'),
where ^' == S S ^ ^ ^ ' . One has exact admissible sequences 0 ->J -> ^ -> SS ->0and
0 ->J' -> ^f -> 88' -> 0. Since ^' is a flat finite .^-algebra, then the second sequence is
obtained by tensoring of the first one with ^ ' over ^/. In particular, J' == J ®^ j^' = J<^'.
It follows that J7F == J/J2 ®^ ^' == J/J2 ®^ ^'. •

       Proof of Proposition 3.5.3. — (i) Consider the diagram
                                     Ax 8
                                 Y     / . Y
                                 ^^ ————>. ^^ Y
                                              ^      Y
                                                     ^^
                                 A              A

                                 r               r
                  Y ^ Y x ^ Y —> Y X g Y

where Y X x Y is identified with the fibre product of X and Y X g Y over X Xg X.
The morphism ^ is flat quasifinite. By Lemma 3.5.5, the conormal sheaf of the G-locally
closed immersion Y x ^ Y — ^ Y X g Y coincides with ^^(^xo/sa)' Since Ay/x is an open
immersion, then Dy^ == P^xo/so)-
       (ii) Consider first the case when the space S is good. (Then X and Y are also good.)
From the exact sequence 3.3.2 (i) it follows that ^y/x = 0, and therefore the mor-
phism 9 has discrete fibres. By Proposition 3.1.4, 9 is quasifinite. Since t2y/x == O? 1<; ls
unramified. Let y eY, x = ^{y) and s == g{jy). We have to verify that ffl^y is a flat
<Px,a;-algebra. Suppose first that \^{y) : k] < oo. Since (Py^ and 0^^ are flat ffg^-algebras
 (Corollary 3.5.4), then, by Corollary 5.9 from [SGA1], Exp. IV, it suffices to
verify that ^y y/m, ^y y is a flat O^Jm^ 0^^-algebra. Since \^{y) : k) < oo, we have
 ^y y/m, (Py ^ == ^y ,v and ^x.as^a ^x,» == ^x ,»• Therefore we may assume that
S ==^(^). In this case the ring tf^a; Is regular and, in pardcular, normal. Since (Py y
is a finite unramified 0^ ^-algebra, it suffices by Theorem 9.5 (ii) from [SGA1], Exp. I,
 to verify that the canonical homomorphism Q^^ -> (P^y is injective or, equivalently,
 that (P^ ^ and (Py y have the same dimensions. But these dimensions are equal to the
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


## Published source Ber, PDF pages 73-74

76                               VLADIMIR G. BERKOVICH

3.7. The local structure of a smooth morphism

       3.7.1. Definitions. — (i) A morphism <p : Y -> X is said to be an elementary fibration
of pure dimension one (resp. at a pointy e Y) if it can be included to a commutative diagram

                  Y c-^ z <— V = U (X x E,)
                                         »==!




                           X
such that
      a) ^ : Z -> X is a smooth proper morphism whose geometric fibres are irreducible
curves of genus g ^ 0;
      b) Y is an open subset of Z, and V = Z\Y;
      c ) V is an analytic domain in Z isomorphic to a disjoint union 11*"= i (X X E,),
m ^ 1, where E, are closed discs in A1 with center at zero, andj&r is the canonical projection;
      d ) there exists an analytic domain V C V such that the isomorphism
                  V^U^(XxE,)
from c ) extends to an isomorphism V'^-U^^X X E,'), where E,' is a closed disc
in A1 which contains E, and has a bigger radius;
     e ) the pair (Z^, YJ (resp. the triple (Z^, Y^,j/)), where x = 9(^)3 is elementary.
     (ii) A morphism is said to be an elementary fibration if it is a composition of ele-
mentary fibrations of pure dimension one.
     (iii) A morphism 9 : Y -> X is said to be standard of pure dimension one if everything
from (i), except the property e), is true for it. A composition of standard morphisms of
pure dimension one is said to be standard,
     We remark that the geometric fibers of a standard morphism are nonempty and
connected. Furthermore, elementary fibrations (resp. standard morphisms) are preserved
under any base change functor and under any ground field extension functor.

      3.7.2. Theorem. — Let 9 : Y -> X be a smooth morphism of pure dimension one, and
suppose that X (and therefore V) is good. Then for any pointy e Y there exist an etale morphism
f: X' -> X and an open subset Y" C Y7 = Y x^ X'
                  Y -^ X
                  A         A

                  r         r
                  Y' -^ X'

                  t V
                  Y"
such that y has a unique preimage y' in Y" and 9" : Y" -> X' is an elementary jibraiion of pure
dimension one at the point y.
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


## Published source Ber, PDF pages 125-127

128                                VLADIMIR G. BERKOVICH

where 9 is a proper morphism and j is an open immersion. For a sheaf ^ on ^ one
defines
                   R^^R^^).

By Nagata's Theorem, any separated morphism of finite type is compactifiable.

       7 . 1 . 1 . Theorem. — Let S£ be a compactifiable scheme over k, and let 3^ he an abelian
torsion sheaf on St'. Then for any q ^ 0 there is a canonical isomorphism

                   H^, y} ^ ny, ^an).

       Proof. — Let 9 : W -> !C be a compactifiable morphism between schemes of locally
finite type over Spec(e^), where ^ is a A-affinoid algebra (the situation is slightly more
general for a further use). For a point x e SE we denote by ^ ^e fibre of 9 at x and
set ^ == ^ ® ^( x ) 8 ? and for an abelian torsion sheaf ^ on ^, we denote by ^ an(! ^x
the pullbacks of ^ on ^ ^d ^x? respectively. By the Base Change Theorem for Coho-
mology with Compact Support for schemes, one has

                   (R<^,^=H^,^).

Furthermore, for a point x e ^an over x, we fix an embedding of fields A(x) 8 <->^{x)\
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
             fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                                   129

     Proof. — The first statement follows from Theorem 6.1.1 and the above remarks,
and the homomorphism of Leray spectral sequences
                     H^, R^y. ^) ==> H^^, ^)

                             i
                   H^^, R3 9^ ^an) ==> H^0^, ^an)
                                                          i
shows that the second statement is also true. •

     7.1.3. Lemma. — In the above situation assume that the morphism 9 is finite and surjective.
Then if 2^ and W are compactifiable over k and the theorem is true for @<, then it is also true for SC.

      Proof. — Let ^ be an abelian torsion sheaf on 3C. Since 9 is finite and surjecdve,
the canonical homomorphism y -> 9^(9* ^") is injective. Furthermore, by Corol-
lary 4.3.2, for an abelian sheaf ^ on W one has H^.^, 9^ ^an) ^ H^®^, ^an).
In particular, the hypothesis implies that the theorem is true for all sheaves of the
form 9^ ^S. Thus, one can construct a resolution of ^", 0 -> 3F -> ^ro ->^"1 - > . . . ,
such that the theorem is true for all ^ri. The homomorphism of spectral sequences
                    H^H^^,^-)) ———> H^^,^)


                   ^(H^^ , ^
                             i
                             0    ran
                                     ')) ==> H^ - ^"1,^"1)
                                                    4 0
                                                          i
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
130                                 VLADIMIR G. BERKOVICH

      Proof. — The statement is obtained from Theorem 7.1.1, using the remarks from
the beginning of its proof. •
      Let 9 : Y -> X be a morphism of A-analytic spaces, and let G be a sheaf on Y.
We say that the pair (9, G) is quasialgebraic if, for each point x e X, one has Y^ = ^an
and G^ = ^an, where 3£ is a compactifiable scheme over the field J^{x) and ^ is a
sheaf on S. For example, for the canonical projection pr : Y = X X ^an -> X, where W
is a compactifiable scheme over k, the pair (pr, ^ y) is quasialgebraic.

      7.1.5. Corollary. — Let 9 : Y -> X ^ a Hausdorjf morphism of k-analytic spaces, and
letf: X' -> X ^ a morphism of analytic spaces over k, which give rise to a cartesian diagram

                   Y -^-> X
                   r      T
                    r'        r
                   Y' -^> X'

Furthermore, let G be an abelian torsion sheaf on Y and assume that the pair (<p, G) is quasialgebraic.
Then for any q > 0 there is a canonical isomorphism
                  /*(R^G)^R^;(/-G).
      Proof. — Let ^ e X and x ' e X' be a pair of points with x ==/(^'). By hypothesis,
one can find a compactifiable scheme 3£ over ^{x) and a sheaf ^ on 3£ with Y^ = ^aD
and G^ == ^an. One has Y^ = (^(^^^(A;'))^. The statement follows from the Weak
Base Change Theorem 5.3.1, Theorem 7.1.1 and the fact that the cohomology with
compact support of schemes are preserved under separably closed extensions of the
ground field. •

7.2. The trace mapping

     In this subsection we fix an integer n which is prime to the characteristic of the field k.
     Our goal is to extend the construction of the trace mapping from § 5.4 and § 6.2
to any separated smooth morphism <p : Y -^ X of pure dimension d, i.e., to construct a
canonical homomorphism of sheaves
                   Tr^R^^-^ZWx.
As in the Theorems 5.4.1 and 6.2.1, we will characterize the trace mapping by certain
properties.
      Let <p : Y -> X be a Hausdorff morphism of ^-analytic spaces, and let,/: X' -> X
be a morphism of analytic spaces over k. They give rise to a cartesian diagram
                   Y -^ X

                  t-    t-
                  Y' -^ X'


# Explicit source application checks

# Checked exact primary statements and new applications

The literal files retain the unmodified selected primary pages, including OCR artifacts. The following readable transcriptions record the decisive PDF checks and the applications proved in the argument. These checks identify hypotheses and signs; they are not independent verification of the new theorem.

1. Thuillier, PDF page 76, printed page 62, Proposition 3.1.8(iii): “la régularisation semi-continue supérieurement de l'enveloppe supérieure d'une famille croissante et localement bornée de fonctions sous-harmoniques sur \(\Omega\) est sous-harmonique.” The curve is smooth and strict, the field is nontrivially valued, and \(\Omega\) is open. In the application, \(\Omega=\operatorname{Int}(\widetilde C)\); finite maxima containing a fixed finite continuous member are bounded both above and below locally. The closed-disc or relative-boundary case is handled separately by GR1 Proposition 3.5(3), rather than assigned to this statement. The number is 3.1.8, not 3.1.9.

2. GJR, PDF/printed page 47, Definition 7.8 and 7.9: LFS is an \(\mathbb R\)-PL function whose residue is semiample at every point. The local presentation is an \(\mathbb R_{\geq0}\)-linear combination of \(\max\{-\log|f_1|,\ldots,-\log|f_n|\}\) for invertible analytic functions on an ordinary open neighborhood. The negative signs and invertibility were checked visually. Each new example is first shown to be rational PL using rational dominance domains, then the reciprocals of its retained nonvanishing entries give the exact presentation. No assertion that an arbitrary maximum of two real-PL functions is real PL is used.

3. Berkovich, PDF page 74, printed page 77, Corollary 3.7.4: “A smooth morphism is an open map.” This is ordinary openness. For the product projection, smoothness is proved from the smooth projective scheme's analytification and base change. It is relative smoothness over the base, which may have absolute boundary. No openness assertion about an arbitrary scalar projection is imported.

4. Berkovich, PDF page 125, printed page 128, Theorem 7.1.1: for a compactifiable scheme \(\mathcal X\) and an abelian torsion sheaf \(\mathcal F\), \(H_c^q(\mathcal X,\mathcal F)\simeq H_c^q(\mathcal X^{\mathrm{an}},\mathcal F^{\mathrm{an}})\). The subscript \(c\) was checked against the PDF. Our scheme is projective over \(\mathcal H(x)\), hence proper and compactifiable. Both degree-zero groups with \(\mathcal F=\mathbb Z/\ell\mathbb Z\) are ordinary section groups because the spaces are proper/compact. A clopen decomposition upstairs would produce a nonconstant section, so a connected projective scheme has connected analytification in this application.

5. GR1, PDF/printed page 21, Definition 4.1: classical psh means usc and subharmonic under every curve morphism after every analytic field extension. We verify these quantifiers in formula (3.6) of the proof. The main argument neither substitutes ground-field curves for extended curves nor relies on an arbitrary scalar map commuting with regularization.

6. GJR Corollary 5.12 and Proposition 7.6(2'): a finite scalar extension is within the stated algebraic descent range for real PL, and semipositivity descends from that field extension. A finite extension with a rational point of the projective factor is constructed from an actual closed algebraic point. The full base function is recovered, rather than approximated. This is the indispensable new application that avoids an assumed global ground-field section.

7. GR2's cached numbering is Proposition 5.1 and Corollary 5.4. GR1's references to that article use earlier numbering. Only the actual checked current statements are identified here; numbering recognition is not used in place of a proof or as a new envelope theorem.

8. Proper analytic fibers are compact and boundaryless over their completed residue fields, even over absolute-boundary base points. GR1 Theorem 6.1 is applied to finite continuous competitors on those actual fibers; the nonempty closed maximum set is open, so connectedness forces constancy. GR1 Theorem 6.4 is used on closed polydiscs and the scalar-extended closed-disc maps in both obstructions, where the Gauss point is the singleton Shilov boundary. All envelope upper bounds use every competitor in the exact union.

9. Berkovich, PDF pages 22--23, printed pages 25--26, the finite-module/coherent-sheaf discussion and Proposition 1.3.4: on a good affinoid, finite algebra modules give coherent sheaves, and the ordinary and G-topological coherent categories agree. The new pinching algebra has the exact finite-module sequence \(0\to A\to B\to K_\xi\to0\), with the last map the difference of evaluations at the two rational points. This identifies its analytic germ kernel as the equal-residue fiber product of the two normalization germs. Section 5 proves the needed subintegral-extension property for that germ explicitly. The affinoid algebra's bounded decomposition is itself proved by reducing powers under \(T^2=T+U\), so no realization or norm-equivalence assumption remains.

All exact source paths, byte identifiers, selected page spans and corresponding new applications appear in source-provenance.json. Only the public caches supplied in the assignment were accessed. No generated campaign notes or book sources were consulted.
