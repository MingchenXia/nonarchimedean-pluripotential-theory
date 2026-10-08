# Ordinary calculus, positivity, and exact integration weights

This is an independent mathematical draft. Fix a complete non-Archimedean field \(K\), with trivial valuation permitted, a good separated strict boundaryless pure \(n\)-dimensional analytic space \(X\), \(n\geq2\), and an ordinary open \(N\subset X\). Put \(D=d'd''\). A positive current means a symmetric current nonnegative on middle-positive complementary tests, as in CLD 7.2.1. If \(T\) has bidegree \((p,p)\), put \(q=n-p\) and \(r=q-1\). Tests for \(T\) have type \((q,q)\); tests for \(D(hT)\) have type \((r,r)\). All products and tests below are ordinary CLD products and ordinary smooth tests on the indicated open.

The primary reference is Chambert-Loir--Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2, retained cover 25 July 2025, internal title 29 July 2025, 0h06. Its complete applied statements and immediate proofs were displayed in 31 bounded units. The complete book was retained, not read page by page. The ledger states the imported recursive analytic and measure-theoretic foundations. Previous note bodies, reading records, PASS labels, and ROOT decisions are data, not premises.

The needed primary statements are these. CLD 11.1.7 gives compact neighborhood bases, affinoid neighborhood bases on good spaces, and the analytic-domain structure of ordinary opens. CLD 15.7.1--2 supplies the canonical calibrated level-\(n\) calculus and its analytic-domain restriction for topologically separated pure analytic spaces. CLD 15.2.2--4 proves local differential separation for good separated spaces by separating seminorms with an analytic function, composing its logarithmic norm with a real smooth separator, and extending by zero near its zeros. CLD 6.2.4--8 and 15.2.5--9 gives compact smooth plateaus in prescribed opens, compact scalar density, and finite localization on compact supports. No global paracompactness of \(N\) is assumed. These inputs have no reducedness or nontrivial-valuation assumption.

For clarity, finite nonnegative localization follows directly from these plateau results. Cover a compact set by finitely many relatively compact smaller neighborhoods inside the proposed chart opens, choose nonnegative plateaus on them, and divide their sum into each plateau where the sum is positive. Multiply by a further plateau supported where the sum is positive and equal to one near the compact set. The resulting finite smooth functions sum to one near that set and have compact supports inside the specified opens. Uniform approximation of continuous compact scalars follows from real Stone--Weierstrass on the one-point compactification, followed by multiplication by a prescribed-open plateau. These are uses of scalar density, not pluriharmonic regularization.

There is an essential cone distinction. On a real vector space \(E\), let \(\sigma_a=(-1)^{a(a-1)/2}\). A symmetric \((a,a)\)-form is middle-positive exactly when its coefficient matrix in the convention \(\sigma_a\xi_I\wedge J\xi_J\) is PSD; this is CLD 1.2.6. For \(\lambda=\sum_i d's_i\wedge d''s_i\),
\[
 \lambda^a=a!\sigma_a\sum_{|I|=a}d's_I\wedge J(d's_I).
\]
Thus its matrix is a positive scalar multiple of the identity on the actual \(a\)-th exterior coefficient space. It dominates both signs of every bounded symmetric coefficient matrix. Pullback and wedge preserve middle positivity by CLD 1.2.11--12. The size of this coefficient space is determined by the moment chart, not by the analytic dimension.

Strong-positive domination of all symmetric middle-degree forms is false. In \(\Lambda^2\mathbb R^4\), use the ordered coordinates \(12,13,14,23,24,34\). For \(w=a\wedge b\), the coefficient of \(w\wedge w=0\) is twice
\[
 P(w)=w_{12}w_{34}-w_{13}w_{24}+w_{14}w_{23}=0.
\]
The corresponding linear functional \(L(B)=B_{12,34}-B_{13,24}+B_{14,23}\) vanishes on the span of all decomposable-square generators of the strong-positive cone. It vanishes on the diagonal matrix representing \(\lambda^2\). But \(L(vv^t)=1\) for \(v=e_{12}+e_{34}\). Consequently neither \(c\lambda^2+vv^t\) nor \(c\lambda^2-vv^t\) can be strongly positive for any \(c\). Middle PSD domination remains valid. This proves, rather than merely diagnoses by computation, the needed correction to 367/368 and to the printed strong-domination step in CLD 7.2.9. The retained page 162 pixels confirm that this word occurs in the PDF; CLD 1.2.13 itself states only relative interior for the strong cone. We import no general recognition theorem for arbitrary weakly positive functionals.

Here are the four basic calculus conclusions of 369, with their complete arguments.

First, if a compact symmetric \((q,q)\)-form \(\beta\) on \(N\) has support inside an ordinary \(O\subset N\), then
\[
 \beta=\eta_+-\eta_-,\qquad\eta_\pm\in\mathcal A_c^{q,q}(O),\quad\eta_\pm\geq0.
\]
CLD 6.5.2 applies on \(O\) itself: compact analytic supports on almost-good spaces satisfy its support condition, and good ordinary domains are almost good. Its finite chart proof can also be reconstructed by the preceding localization, middle PSD domination on compact chart images, and summation. Compact outputs extend smoothly by zero to Hausdorff \(N\). They can have larger support than \(\beta\), but stay in \(O\). The compact constant-majorant argument suffices; the erroneous noncompact majorant/composition wording in CLD 1.10.2 is unused.

Second, for each compact diagonal test \(\theta\) complementary to positive \(T\), there is a unique finite signed Radon measure \(\mu_{T,\theta}\), supported in \(\operatorname{supp}\theta\), with
\[
 \int f\,d\mu_{T,\theta}=\langle T,f\theta\rangle
\]
for compact smooth scalars \(f\). For a positive test, CLD 7.2.8 and 7.2.11 gives the positive measure: bound a scalar by its supremum times a nonnegative plateau and extend by scalar density. For general \(\theta\), discard its antisymmetric part and subtract the measures of the preceding middle-positive decomposition. Scalar density gives uniqueness and independence of decomposition. On the complement of \(\operatorname{supp}\theta\), the smooth scalar functional is zero; density there proves the stated support, even if decomposition enlarged the supports. The ordinary multiplication of CLD 7.2.12 therefore satisfies
\[
 \langle bT,\theta\rangle=\int b\,d\mu_{T,\theta},\qquad
 |\langle bT,\theta\rangle|\leq\sup_{\operatorname{supp}\theta}|b|\,|\mu_{T,\theta}|(N).
\]
The repaired order-zero justification uses only the middle cone: on each compact chart image the standard power dominates both signs of a test by a constant times its coefficient norm, cellwise in a finite subdivision; finite localization bounds the functional in the chart \(C^0\) topology. This is the printed 7.2.9 argument with middle positivity throughout, valid for the given middle-positive \(T\). It also shows the locally bounded scalar multiplier is a current in the same calculus.

For \(\beta=\eta_+-\eta_-\) and \(\eta=\eta_++\eta_-\), positivity and uniqueness give the particularly useful bound
\[
 |\langle bT,\beta\rangle|
 \leq\int |b|\,d\mu_{T,\eta}
 \leq\sup_{\operatorname{supp}\eta}|b|\,\langle T,\eta\rangle.                 \tag{1}
\]
The mass is identified by a smooth scalar equal to one on the compact supports. For fixed \(T\), locally uniform convergence \(b_i\to b\) consequently gives \(b_iT\to bT\) on every fixed compact test. No changing-current assertion has been inferred.

Third, for ordinary smooth \(g\) and doubly closed positive \(T\),
\[
 D(gT)=Dg\wedge T.                                                        \tag{2}
\]
On a compact symmetric \((r,r)\)-test \(\alpha\), set \(A=g\,d''\alpha-d''g\wedge\alpha\), of type \((q-1,q)\). Total-degree Leibniz gives
\[
 Dg\wedge\alpha-gD\alpha=-d'A+C,\qquad
 C=d'g\wedge d''\alpha+d''g\wedge d'\alpha.
\]
The identities \(Jd'=d''J\), \(Jd''=-d'J\) give \(JC=-C\). Symmetry of \(T\) kills \(C\), and \(d'T=0\) kills \(d'A\). Signed transposition gives \(\langle DS,\alpha\rangle=\langle S,D\alpha\rangle\), proving (2). Both currents are symmetric, so symmetric tests suffice. Both closedness equations are retained. This replaces the misindexed printed CLD 8.5.3 and 7.7.5 statements by correctly typed direct arguments.

Fourth, if \(Z\subset N\) is ordinary closed and continuous \(h\) is ordinary smooth with \(Dh=0\) on \(N\setminus Z\), then \(R=D(hT)\) is symmetric, supported in \(Z\). Equation (2), restriction, and CLD 7.1.9 proves this. If \(\chi=1\) near \(Z\cap\operatorname{supp}\alpha\), then
\[
 \langle R,\alpha\rangle=\langle R,\chi\alpha\rangle.                      \tag{3}
\]
The compact support of \((1-\chi)\alpha\) misses \(Z\). No order-zero or positivity assertion is needed for \(R\). The same support conclusion holds if, off \(Z\), \(h\) is locally a uniform limit on compact sets of ordinary smooth \(g_i\) with \(Dg_i=0\): (2), fixed-\(T\) continuity, and transposition makes \(D(hT)=0\) there.

All exterior signs use total degree. Moving a type \((a,b)\)-form across a type \((c,d)\)-form gives \((-1)^{(a+b)(c+d)}\), directly by permuting exterior generators and consistently with CLD 1.3.3. The different exponent printed in 3.3.10 is confirmed in the retained page 80 pixels. Also the \(d_K\) in the proof of 3.3.6 must be \(d_{\rm trop}\), as its statement and ensuing argument show. These are explicit algebraic repairs, not permission to change the underlying calculus.

We will also use the exact analytic support statement CLD 15.2.1: a type \((a,b)\) G-form on a topologically separated analytic space has support in \(d_K(x)\geq\max(a,b)\); its support misses a locally Zariski-closed analytic locus \(Y\) of dimension below \(\max(a,b)\). Ordinary forms are G-forms. The immediate proof uses \(d_{\rm trop}(x)\leq d_K(x)\) from 12.4.2, form vanishing in insufficient tropical dimension from 3.3.6, and \(d_K(y)\leq\dim Y\) from analytic dimension theory. Here \(d_K\) is graded residual transcendence degree, equivalently residue-field transcendence degree plus rational value-group rank. A projected skeleton dimension is not a substitute.

Finally, the integration weights are the original ones. For an Artinian local ring \(A\), CLD 13.3.4 uses \(\delta_A(B)=\ell_A(B)/\ell_A(A)\). A composition-series calculation gives multiplicativity through finite local algebras. CLD 13.3.7 sums the finite local fiber modules, giving calibrated degree \(\lambda/\mu\) when the generic module length is \(\lambda\) and the base generic Artinian length is \(\mu\); nilreduction has degree \(1/\mu\). CLD 14.4.2 transports the canonical calibration by this degree; 15.4.2--3 then transports top-form integration. Since top-form supports avoid lower-dimensional component intersections, 16.6.3 gives
\[
 \delta_X=\sum_i m_i\delta_{X_{i,\mathrm{red}}}
\]
with actual generic lengths \(m_i\). The calibration is independent under appending analytic units by its common-moment construction in 14.3.1--5. No normalization or base extension of the arbitrary \(T\) is performed. Boundaryless Stokes gives both closedness equations for \(\delta_X\). Its BT property is tautological because \(h\delta_X=[h]\).

Artifacts in this workspace: P21.3-review-paper.tex, P21.3-proof-companion.md, source-ledger-independent.json, and inputs-LOCALONLY contain the full arguments and retained inputs. Rerun python audit.py and python build_review.py. The arithmetic diagnostic checked all 6561 pairs in \(\{-1,0,1\}^4\times\{-1,0,1\}^4\), with no Plucker violations and witness \(P(v)=1\); this is finite evidence only. The universal identity was proved by exterior algebra above. Source integrity and successful execution do not establish mathematical correctness.
