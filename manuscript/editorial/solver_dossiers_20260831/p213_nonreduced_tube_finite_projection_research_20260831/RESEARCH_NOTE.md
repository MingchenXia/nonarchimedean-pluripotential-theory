# Finite projections of multiplicity tubes and their source coefficients

Date: 2026-08-31. Author: /root.
Status: research candidate; not frozen until a companion manifest exists. Independent and production verification are separate requirements.

## 1. Purpose and exact boundary

A blowup of a reduced normal-crossing special fibre can create a component of multiplicity greater than one. The preceding strictly semistable wall proof therefore cannot simply be applied after an arbitrary model refinement. This note addresses one specific missing local calculation: a completed tube with multiplicities and a genuinely nonconstant formal unit.

The analytic finite-map and current-pushforward statements below do not assume a product decomposition, extract a root of that unit, change the coefficient field of a current, or use the skeletal representation premise (R). They have a direct Banach-algebra proof. Under an explicitly stated unramified-DVR hypothesis, the finite map also has only one source point above a dense set of target Gauss points. Only the final interpretation of an arbitrary current's individual source-cell coefficients uses (R).

This is not yet a global residual-divisor theorem for a nonreduced SNC model. Such a theorem would additionally have to justify the completed local presentation in that geometric setting, the weighted global radius and cutoff argument, and its applicability inside the ordinary open set where the current is defined. Those steps are not hidden in the local statement.

## 2. Analytic statement

Let L be a complete nontrivially valued field. Fix an integer n>=1, an integer m>=1, integers a_1,...,a_n>=0, and an element pi of L with 0<|pi|<1. Write v=-log|.| and ell=v(pi).

Let

\[
 \varepsilon(X,Z_1,\ldots,Z_n)\in
       L^\circ[[X,Z_1,\ldots,Z_n]]
\]

have constant coefficient of absolute value one. Here the notation means an arbitrary formal series whose coefficients have absolute value at most one. On the open unit polydisc this series converges; on every smaller closed polydisc its nonconstant part has norm strictly less than one. In particular epsilon and its inverse are analytic there and |epsilon|=1.

Define the ordinary open torus domain

\[
 B=\{z\in(\mathbf G_{m,L}^{n})^{\mathrm{an}}:
       0<|z_j|<1,\quad
       |\pi|<\prod_{j=1}^n |z_j|^{a_j}\}.
                                                        \tag{2.1}
\]

It has tropical image

\[
 Q=\{u\in\mathbf R^n: u_j>0,\ \sum_j a_j u_j<\ell\}.
                                                        \tag{2.2}
\]

The inequality with the empty or zero exponent sum is interpreted literally; Q is always nonempty and convex. In the open (n+1)-dimensional unit polydisc take the analytic subspace

\[
 D=\{(x,z): x^m\varepsilon(x,z)\prod_jz_j^{a_j}=\pi,\
                       0<|x|<1,\ 0<|z_j|<1\}.
                                                        \tag{2.3}
\]

Projection g:D->B is finite and flat of degree m. It is onto. The map

\[
             q=(v(z_1),\ldots,v(z_n)):D\longrightarrow Q
                                                        \tag{2.4}
\]

is topologically proper. Its source is good, separated, boundaryless and pure n-dimensional. It admits a countable compact exhaustion.

If T is a positive ordinary CLD current of bidegree (0,0) on D, considered over L, and d'T=0, there is a finite constant b>=0 such that

\[
 \langle T,q^*(h\Omega)\rangle=b\int_Q h(u)\,\mathrm du,
 \qquad
 \Omega=\bigwedge_{j=1}^n
                   \mathrm d'u_j\wedge\mathrm d''u_j,
 \quad h\in C_c^\infty(Q).
                                                        \tag{2.5}
\]

For the canonical integration current the constant is m. If D is viewed over a complete subfield K for which L/K is finite, the same assertion about an arbitrary current on that K-analytic space holds, and the canonical constant is m[L:K]. This changes the analytic structure in which the given current is considered; it is not a pullback or base change of that current.

## 3. A bounded division argument

We first prove the only preparation statement needed. Let A be a complete non-Archimedean Banach algebra, let R>0, and give

\[
 \mathcal B=A\{R^{-1}X\}
\]

its weighted Gauss norm. Suppose c in A satisfies ||c||<R^m. Put P=X^m-c.

Division by P is explicit. For k=jm+r, 0<=r<m, set

\[
 \mathcal R_P(X^k)=c^jX^r,\qquad
 \mathcal D_P(X^k)=
       \sum_{i=0}^{j-1}c^iX^{k-m(i+1)}.
                                                        \tag{3.1}
\]

The second sum is zero for j=0. Direct multiplication gives

\[
             X^k=P\mathcal D_P(X^k)+\mathcal R_P(X^k).
                                                        \tag{3.2}
\]

Their weighted norms are bounded by R^k and R^{k-m}, respectively. For a restricted series f=sum f_k X^k, the corresponding series of remainders and quotients therefore converge. They define bounded A-linear maps

\[
 \mathcal R_P:\mathcal B\to A[X]_{<m},\qquad
 \mathcal D_P:\mathcal B\to\mathcal B,\qquad
 \|\mathcal R_P\|\le1,\quad \|\mathcal D_P\|\le R^{-m}.
                                                        \tag{3.3}
\]

The finite free target is given its weighted coefficient norm. The identities

\[
 f=P\mathcal D_Pf+\mathcal R_Pf,\quad
 \mathcal D_P(Pq)=q,\quad \mathcal R_P(Pq)=0
                                                        \tag{3.4}
\]

hold first on polynomials, by (3.1), and then on all restricted series by continuity. This proves uniqueness of division as well as existence.

Now let E in \(\mathcal B\) satisfy ||E||<R^m, and put F=P+E. The bounded operator

\[
           A_E=\mathcal D_P\circ M_E
\]

has norm strictly less than one, so I+A_E is invertible by the convergent Neumann series sum_{j>=0}(-A_E)^j. For any f set

\[
 q=(I+A_E)^{-1}\mathcal D_Pf,\qquad
 r=\mathcal R_P(f-Eq).
                                                        \tag{3.5}
\]

Equation (3.4) implies f=Fq+r. If Fq+r=0 with deg(r)<m, applying \(\mathcal D_P\) gives (I+A_E)q=0, hence q=0 and r=0. Thus this division is unique, and both quotient and remainder depend continuously on f.

In particular \(F\mathcal B\) is the kernel of the continuous remainder map and is closed. The quotient is, as a Banach A-module, free on 1,X,...,X^{m-1}:

\[
                 \mathcal B/(F)\simeq A^m.
                                                        \tag{3.6}
\]

This proof permits arbitrary positive R and makes no extension of L. It does not assume a monic polynomial equation in advance.

## 4. Finite flatness on actual analytic domains

Choose a compact rectangular box P_0 in Q. Its inverse image B_0 in the torus is a product of closed annuli

\[
                   r_j\le |z_j|\le R_j<1
\]

with all r_j>0. Let A be its generalized affinoid algebra with the usual polyannular Gauss norm. The strict inequality P_0 subset Q gives

\[
 \lambda=\pi\prod_jz_j^{-a_j}\in A^\times,\qquad
                         \|\lambda\|<1.
                                                        \tag{4.1}
\]

Expand epsilon in X:

\[
                 \varepsilon(X,z)=\sum_{j\ge0}e_j(z)X^j.
\]

All e_j have A-norm at most one. Moreover e_0 is an A-unit of norm one with inverse of norm one: its constant term has norm one and its remaining z-series has norm strictly less than one.

Choose a real R with ||lambda||^{1/m}<R<1. On A{R^{-1}X}, divide the equation in (2.3) by the unit e_0(z). It becomes

\[
 F=X^m-c+E,\qquad c=\lambda/e_0,\qquad
 E=X^m\sum_{j\ge1}(e_j/e_0)X^j.
                                                        \tag{4.2}
\]

We have ||c||<R^m and ||E||<=R^{m+1}<R^m. Section 3 applies. Hence the closed analytic zero set of F in the R-disc over B_0 is finite free of rank m over B_0.

It is precisely g^{-1}(B_0), not a chosen portion of a fibre. For a point of this zero set, |epsilon|=1 and the equation gives

\[
               |x|^m=|\lambda|,\qquad
                 0<|x|\le\|\lambda\|^{1/m}<R.
                                                        \tag{4.3}
\]

Conversely every point of D over B_0 satisfies the same equality and lies in that disc. Thus no root is discarded at the disc boundary. Positive free rank also shows that every fibre is nonempty.

Small boxes with their interiors in Q give a generalized affinoid neighborhood cover of B; finite flatness and the stated degree therefore hold locally on the target, hence globally. This use of compact analytic domains is only for verifying a morphism property. It is not an assertion that they are ordinary open sets on which an unknown current can be glued.

The source D is an analytic hypersurface in an ordinary open polydisc and is good and separated. A finite morphism has no relative analytic boundary, so D is boundaryless over L because B is. Finite flatness over the pure n-dimensional torus domain gives pure dimension n; equivalently, on the affinoid boxes flat going-down makes each irreducible component dominate a component of the base, and an integral finite map preserves dimension.

The tropicalization B->Q is topologically proper. A compact subset of Q lies in a finite union of compact boxes with closure in Q, whose inverse images are compact affinoid domains. Its own inverse image is a closed subset of that compact union. As g is finite, it is proper, and (2.4) is proper as a composition. The same boxes can be chosen countably and in a compact exhaustion of Q; their finite inverse images give the asserted exhaustion of D.

## 5. Closed positive currents and the canonical constant

For a compactly supported smooth form alpha on Q of any bidegree, q^*alpha has compact analytic support by properness. Pullback is the actual analytic moment pullback. Consequently q_*T is defined by

\[
                   \langle q_*T,\alpha\rangle
                         =\langle T,q^*\alpha\rangle.
                                                        \tag{5.1}
\]

It is a positive current of bidimension (n,n) on Q. In Euclidean superform coordinates such a positive current is a positive Radon measure mu acting on h Omega. The equality d'T=0 implies d'(q_*T)=0 by transposition on compact tests; no extension of a current from an open set occurs here.

For each coordinate u_j, test this equality on the (n-1,n)-form obtained by omitting d'u_j from Omega and multiplying by a scalar test h, with the harmless orientation sign chosen accordingly. It gives integral(partial_j h) dmu=0. Thus every distributional partial derivative of mu is zero.

Here is a direct local justification of the familiar conclusion. Convolve mu on any ball compactly contained in Q with nonnegative smooth approximate identities of sufficiently small support. Each resulting smooth density has all partial derivatives zero on the smaller ball, so is constant there. The distributional limit is a constant multiple of Lebesgue measure on that ball; the constant is fixed, for example, by evaluating a scalar test of integral one supported in a still smaller ball. Overlapping balls give the same constant. Connectedness of Q gives a single finite b>=0, proving (2.5).

The canonical value is a finite-degree computation, not a uniqueness theorem for arbitrary currents. For the actual moment g:D->B subset G_m^n, the map is finite flat of degree m above every target Gauss point. CLD Proposition 14.5.3 therefore gives the constant canonical target calibration m times the standard volume element throughout Q. Its definition of integration yields (2.5) with b=m. If L/K is finite, CLD Remark 14.4.3 multiplies canonical calibration by [L:K], giving m[L:K] on the same space viewed over K.

The argument defining q_*T applies directly to a current originally given on that K-analytic space as well. It does not obtain that current by pullback from either B or an L-analytic current.

## 6. One source point over generic Gauss radii in the DVR case

Impose the following additional hypotheses for this section only. K is complete discretely valued, pi is a uniformizer of K, L/K is a finite unramified extension, and epsilon has its coefficients in L^circ as above. Thus

\[
                          v(L^\times)=\ell\mathbf Z.
                                                        \tag{6.1}
\]

Let u in Q satisfy that ell,u_1,...,u_n are linearly independent over Q. Such u form a dense subset of every nonempty open subset of Q: the excluded set is the countable union of proper rational affine hyperplanes, each with empty interior.

Let eta_u be the Gauss point of B with these radii and H its completed residue field over L. The Gauss valuation has value group

\[
                  \Gamma=v(H^\times)
                       =\ell\mathbf Z+\sum_j u_j\mathbf Z.
                                                        \tag{6.2}
\]

Indeed a Laurent polynomial has a unique term of smallest valuation after grouping equal monomials, by rational independence; its value lies in this group. The same is true of a convergent Laurent series because its maximum norm is attained, and then of its fraction field. Completion does not enlarge the value group: a sequence converging to a nonzero element has eventually the same absolute value as that element.

The fibre algebra of g above eta_u is a finite-dimensional H-algebra of dimension m, by finite freeness. Every residue field F of this algebra is a finite extension of H. At its analytic point the equation and |epsilon|=1 give

\[
                 v(x)=\frac{\ell-\sum_j a_j u_j}{m}.
                                                        \tag{6.3}
\]

The class of the right-hand side modulo Gamma has exact order m. For if its multiple by an integer j belongs to Gamma, comparison of the coefficient of ell in the independent family ell,u_1,...,u_n gives j/m in Z. Consequently the ramification index of F/H is at least m. The fundamental valuation inequality gives

\[
                          [F:H]\ge e(F/H)\ge m.
                                                        \tag{6.4}
\]

Since the ENTIRE fibre algebra has H-dimension m, it must be a single field of degree m, without another factor or any nilpotent length. A finite field extension of a complete non-Archimedean field has a unique extension of its absolute value. Therefore g^{-1}(eta_u) is exactly one analytic point.

This is a proof about the actual fibre algebra, not a restriction of T to that fibre. No current is evaluated at eta_u, sliced, extended in scalars, or pulled through g.

## 7. Conditional individual source-cell interpretation

Retain Section 6's unramified-DVR hypotheses and let T be positive with d'T=d''T=0. Assume explicitly the separately frozen source-calibration representation (R) for T on D with the moment g. Its full-dimensional source skeleton has a locally finite cell structure on which q is affine injective, and R supplies constant nonnegative coefficients b_C and no lower-cell residual contribution to the current's description. Refine this structure to convenient source cells, as permitted by CLD Lemma 14.1.5; the constant coefficients in R restrict unchanged to such refinements.

For every top-dimensional source cell C, q(C^circ) is open in R^n. It contains a point u as in Section 6. The corresponding source point lies over eta_u: for an n-coordinate moment the characteristic skeleton is the inverse image of the torus Gauss skeleton, and on a top cell this is the full-dimensional characteristic part. These are the actual characteristic-skeleton statements of CLD, not a claim inferred from a common target cone.

If the source is considered over K, CLD Corollary 12.1.8(b) says that the inverse image of the target K-Gauss point in the L-torus is its single L-Gauss point with the same radii. Thus Section 6's uniqueness over L is also uniqueness on the source viewed over K. This uses finite scalar extension of the torus and its Gauss point, not scalar extension of T.

By Section 6 the fibre at this u has a single point of degree m. The local degree is constant on the interior of a convenient source cell, by CLD Proposition 14.2.2. Thus the canonical q-coordinate coefficient of each such cell is m over L, and m[L:K] over K.

No two disjoint top-cell interiors can have images overlapping in a nonempty open subset of Q: such an overlap would contain an independent u, yielding two distinct points over eta_u. On a compact region only finitely many cells occur, since q is proper and the source cell structure is locally finite. After excluding the lower-dimensional images of their boundaries, every sufficiently small target ball in the image of C therefore sees precisely its one source sheet.

Choose a compact scalar target test supported in such a ball. Properness supplies a compact analytic inverse image, and an ordinary smooth source cutoff can be chosen to be one near it. Formula R and (2.5), applied to that same actual test, give b_C=b. No arbitrary source form is replaced by an unrelated target test; R is exactly the premise permitting this comparison.

It follows that all displayed full-dimensional source cells have the same ratio

\[
                 \frac{b_C}{m[L:K]}
                         =\frac{b}{m[L:K]}.
                                                        \tag{7.1}
\]

Over L omit [L:K]. This is still a result about this particular completed tube and its coordinate moment. It does not compare different p-tubes along a residual curve, realize every analytic wall, or settle P21.3.

## 8. Necessary restrictions and a check on aggregation

The unramified-DVR hypothesis in Section 6 is substantive. For example take m>=2 and a complete field L containing pi^{1/m} and all m-th roots of unity, with residue characteristic not dividing m; set epsilon=1 and all a_j=0. Then D is the disjoint union of m copies of the open punctured unit polydisc, given by x=zeta pi^{1/m}. Projection g has degree m, but has m separate points over every target Gauss point.

For arbitrary nonnegative constants c_zeta, the current sum c_zeta delta_{D_zeta} is positive and closed. Its q-pushforward coefficient is sum c_zeta. That aggregate does not determine the individual constants. This example contradicts neither Section 6 nor a same-field DVR model with pi a uniformizer: it deliberately violates (6.1) by adjoining its m-th root.

It explains why finite flatness alone is insufficient for individual source coefficients, and why a ramified scalar extension cannot be inserted into Section 7 without a new argument. The example is not a counterexample to P21.3.

## 9. Next geometric step, not claimed here

For a proposed regular SNC model with multiplicities N_i, one expects local equations of the form (2.3) with m=N_0 and a_j the remaining component multiplicities, including the possible extra component at a closed residual point. The global model radii would satisfy sum N_i U_i=ell, rather than the unweighted relation in the frozen strict-semistable proof.

A local collar calculation with rational lifts is then expected to involve r_i=U_i+n_{i,p}s and

\[
 N_0U_0=\ell-\sum_{i=1}^{n-1}N_i r_i+
               \left(\sum_{i=1}^{n-1}N_i n_{i,p}-N_p\right)s.
                                                        \tag{9.1}
\]

The displayed equation only records the required support budget. This note does not claim that the global compact primitive has been constructed, that the p-dependent coefficients annihilate all principal divisors, or that a whole residual-curve tube lies in the arbitrary ordinary open set supporting T. Those are separate proof obligations.

## 10. Source interfaces and verification status

Primary source: Chambert-Loir--Ducros, arXiv:1204.6277v2, 25 July 2025, https://arxiv.org/abs/1204.6277v2. The exact local PDF is /private/tmp/CLD25.pdf (SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719); its extracted text is /private/tmp/CLD25.txt (SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e).

- Sections 7.1.10-7.1.11 and 7.7: proper-support current pairing and signed-transpose differential calculus.
- Corollary 12.1.8(b), printed p.332; Proposition 12.2.8(iv) and the characteristic-skeleton discussion in Sections 12.9.3-12.9.6, printed pp.335-336 and 358-360: Gauss points under finite scalar extension and actual characteristic-skeleton membership. These passages were read directly for Section 7.
- Proposition 14.2.2, printed p.399, and Sections 14.3.2, 14.4.2-14.4.3, 14.5.2-14.5.3, printed pp.407-411: actual finite degrees, canonical source calibration, finite-field factors and target calibration. These passages were read directly in the pinned text for this note.
- The source-representation input in Section 7 remains an explicit premise and requires its own production verification; no acceptance is imported from earlier packets.

The bounded division argument is supplied in full, so this note does not rely on an unchecked generalized Weierstrass-preparation citation. Standard generalized affinoid-domain and finite-morphism facts are the remaining analytic foundations to verify against the manuscript or primary sources in the independent audit.

There is no priority claim. No prior frozen packet, live theorem, open-problem inventory or production workflow was changed while writing this candidate.
