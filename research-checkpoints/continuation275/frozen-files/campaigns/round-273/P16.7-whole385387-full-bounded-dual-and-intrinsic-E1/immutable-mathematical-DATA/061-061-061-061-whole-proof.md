# Independent reconstruction and extension of three P21.3 drafts

This is an independent mathematical draft, not a formal verification. The original P21.3 is not solved. All ten items of draft 369, the whole scalar-factor argument of 367, and the whole relative-form argument of 368 are reconstructed below. The factor arguments require a correction to their positive-cone decomposition. A further logarithmic cutoff argument proves removability across a locally analytic locus with a smooth harmonic trace, without assuming a cutoff mass bound. It includes isolated analytic points in every allowed current degree. No priority claim is made.

## 1. The literal target and conventions

Fix a complete non-Archimedean field \(K\), allowing trivial valuation, and a good separated strict boundaryless pure \(n\)-dimensional \(K\)-analytic space \(X\), \(n\geq2\). All opens are ordinary opens, all forms are ordinary CLD smooth forms, and all currents are ordinary CLD currents. Write \(D=d'd''\). A positive current means the middle-positive current: it is symmetric and nonnegative on middle-positive complementary tests. It is doubly closed when both \(d'T\) and \(d''T\) vanish.

The original quantifiers are every ordinary \(W\subset X\), every positive doubly closed \((p,p)\)-current \(T\), \(0\leq p\leq n-1\), and every separately admissible finite continuous individually psh pair \(U,V\) on \(W\). The requested implication is
\[
 D[U]=D[V]\quad\Longrightarrow\quad D((U-V)T|_W)=0.
\]
Here \([f]=f\delta_X\) uses the actual canonical integration current. There is no replacement of the prescribed potential class by CPsh, no restriction to reduced spaces, and no change of integration weights. Set
\[
 h=U-V,\qquad q=n-p,\qquad r=q-1.
\]
Thus \(T\) acts on compact \((q,q)\)-forms and \(D(hT)\) acts on compact \((r,r)\)-forms. In particular the detecting forms are scalars when \(p=n-1\).

The general lemmas below often do not require strictness, psh, or even \(D[h]=0\). Their applications to the target retain every original ambient hypothesis and separately admissible potentials. Extra hypotheses are stated rather than inferred from equal canonical curvature.

The unchanged original task was read before selecting this scope. The settled actual FINAL with hash beginning 49b00d contains three notes and candidate=false. The three expanded local note texts differ from its three actual returned texts. Both sets, the entire 30246-byte TeX, the entire 29136-byte proof, all source application metadata and all sixteen LF-bound literal units were read. Neither set of notes nor any historical review is a correctness premise. Earlier source-reading attribution in the packet is historical; the fresh reading used here is listed in the independent ledger.

## 2. Exact primary inputs and corrections

The primary reference is Chambert-Loir and Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2. The preserved PDF header is dated 25 July 2025 and the internal title 29 July 2025, 0h06. The complete source and PDF are retained locally. The LF-based source ledger lists complete immediate statements and proofs; it preserves formfeeds. Reading a finite collection of complete applied units is not a claim to have read every page of CLD.

CLD 11.1.7 says that ordinary opens are analytic domains, that analytic points have compact neighborhood bases, and that good spaces have affinoid neighborhood bases. Separatedness supplies the Hausdorff topology needed here. CLD 15.7.1 gives the canonical calibrated tropical calculus of level \(n\) for a topologically separated pure \(n\)-space. Its proof verifies local differential separation, decency, richness, harmoniousness and boundary negligibility using the cited analytic foundations. CLD 15.7.2 identifies analytic-domain restriction with restriction of this calculus. These statements impose no reducedness or nontrivial-valuation hypothesis.

CLD 15.2.2--4 proves local differential separation in our category. On an affinoid, distinct seminorms are separated by the absolute value of an analytic function. A compactly supported real smooth function of its logarithmic norm, extended by zero across its zeros, gives an ordinary smooth separator. CLD 15.2.5--9 and 6.2.4--8 then give compact smooth cutoffs in prescribed opens, density of compact smooth scalars in compact continuous scalars, and nonnegative compact localization around a compact test support. Only compact localization is used; global paracompactness of an arbitrary open is not assumed.

The immediate appendix proofs were checked: local separation and smooth composition give plateaus around points, compactness gives a plateau around a compact set, and real Stone-Weierstrass on the one-point compactification gives uniform scalar density. Multiplication by a plateau confines the approximation to a prescribed neighborhood. Compact localization may also be constructed directly: cover a compact set by finitely many smaller neighborhoods, take nonnegative plateaus there, and divide by their positive sum near the compact set, with a further compact plateau. This avoids any global partition assertion.

CLD 6.5.2 says that a symmetric diagonal form whose support lies in a paracompact locally differentially separated open is a difference of two middle-positive forms; compact input support permits compact outputs. Its support condition holds for compact supports on almost-good analytic spaces, hence on our good ordinary domains. Its proof is a finite/local-finite chart decomposition followed by positive decomposition on a compact polyhedral image. CLD 1.10.2 and 1.2.6, 1.2.13 supply the latter. In a fixed finite-dimensional exterior coefficient space, middle positivity is positive semidefiniteness of a symmetric matrix, with the prescribed exterior sign. The powers of a positive definite \((1,1)\)-form are interior order units for this middle cone. Bounded coefficients on a compact set can therefore be dominated by a constant multiple of this power. Multiply chart decompositions by nonnegative compact localizers and add them.

There is an essential correction to both 367 and 368. Their claim that an arbitrary symmetric diagonal test can be dominated by a strongly positive form is false in middle degrees. CLD 1.2.13 explicitly says that the strongly positive cone can span a proper subspace of symmetric forms. In dimension four and degree two, write the coefficient basis as \(12,13,14,23,24,34\). For a decomposable two-vector \(w\),
\[
 w_{12}w_{34}-w_{13}w_{24}+w_{14}w_{23}=0.
\]
The corresponding linear functional of \(ww^t\) vanishes on every strongly positive generator and hence its span. It does not vanish on the matrix \(vv^t\) for \(v=e_{12}+e_{34}\). Adding any multiple of the standard diagonal order unit cannot change this functional. Thus strong domination cannot prove the claimed general signed-measure construction. The printed proof of CLD 7.2.9 contains the same problematic strong-domination step; the PDF on page 162 confirms it. We use the middle cone and 6.5.2 instead. The middle-positive current already present is the required hypothesis; no theorem about all weakly positive functionals is imported.

Other repairs are kept explicit. The commutation exponent printed in CLD 3.3.10 is inconsistent with the exterior algebra; inspection of PDF page 80 confirms the print. The correct rule is
\[
 \omega'\wedge\omega=(-1)^{(a+b)(a'+b')}\omega\wedge\omega'.
\]
It follows directly by moving the total number of exterior generators, and agrees with CLD 1.3.3. CLD 3.3.6's proof writes \(d_K\) where the statement and next lines require tropical dimension; we use its actual tropical-dimension proof. The noncompact majorant wording and final composition in 1.10.2 need repair; only the compact constant-majorant case is needed here. CLD 8.5.3 calls its indexing bidegree but tests as bidimension; we prove the correct complementary-degree identity below. Likewise 7.7.5 is used with complementary tests one degree below the initial bidimension, as its transpose proof requires. These textual issues are not licenses for changing the calculus or the task.

CLD 7.1.1 defines currents as continuous linear functionals on compact complementary forms. Sections 7.1.4--9 define symmetry, smooth wedge, restriction, ordinary sheaf locality, and support. The complete sheaf proof sums finitely localized tests and uses agreement on overlaps; only existing current identities will be glued here. CLD 7.2.1 defines middle positivity. CLD 7.2.8 identifies positive scalar currents with positive Radon measures: positivity bounds a smooth scalar on a compact set by its supremum times a nonnegative plateau, and scalar density gives a unique positive extension to continuous tests. Sections 7.2.11--12 give coefficient measures and ordinary multiplication by locally bounded Borel scalars. Continuous multiplication in the target is exactly that operation.

CLD 1.3.6--7 and 3.3.11 give
\[
 Jd'=d''J,\quad Jd''=-d'J,\quad DJ=JD,
\]
and total-degree Leibniz. CLD 7.7.1--8 defines current differentiation by the signed transpose. For a current of total degree \(m\),
\[
 \langle d'S,\omega\rangle=(-1)^{m+1}\langle S,d'\omega\rangle,
 \qquad
 \langle DS,\alpha\rangle=\langle S,D\alpha\rangle.
\]
The second identity follows from the product of the two transpose signs and \(d''d'=-D\). Differentiation commutes with ordinary restriction. Boundaryless Stokes gives \(d'\delta_X=d''\delta_X=0\), and smooth function currents differentiate as smooth forms. There is no boundary term in any application here.

CLD 15.2.1 states exactly that a G-form of type \((a,b)\) has support contained in \(d_K(x)\geq\max(a,b)\), and its support misses a Zariski-closed locus \(Y\) in an analytic domain if \(\dim Y<\max(a,b)\). Ordinary smooth forms are G-forms. Its full proof combines \(d_{\rm trop}(x)\leq d_K(x)\), from 12.4.2, with 3.3.6; on \(Y\), \(d_K(y)\leq\dim Y\). Here
\[
 d_K(x)=\operatorname{trdeg}_{\widetilde K_1}\widetilde{\mathscr H(x)}_1
 +\dim_{\mathbb Q}\bigl(\mathbb Q\otimes_{\mathbb Z}
 (|\mathscr H(x)^\times|/|K^\times|)\bigr).
\]
This is a condition on actual analytic points. No coarse skeleton dimension is substituted.

Finally the actual integration weights are checked rather than silently normalized. For an Artinian G-local ring \(A\), calibrated finite degree uses \(\ell_A(B)/\ell_A(A)\). CLD 13.3.7 proves that a finite map with generic module length \(\lambda\) over a component of generic length \(\mu\) has calibrated degree \(\lambda/\mu\); for the nilreduction immersion it is \(1/\mu\). The proof sums the finite local fiber modules and divides by the actual Artinian length. CLD 14.4.2 transports canonical calibrations by this calibrated degree, and 15.4.2--3 transports integrals accordingly. On the open with a unique component, integration on its reduction is consequently \(1/\mu\) times integration upstairs. A compact top form avoids the lower-dimensional component intersections by 15.2.1. Local finiteness then gives the complete equality of 16.6.3,
\[
 \delta_X=\sum_i m_i\delta_{X_{i,\mathrm{red}}},
\]
where \(m_i\) are the generic Artinian lengths. This equality is an explanation of the weights, not a reduction of our arbitrary current problem. The canonical calibration itself is defined by positive finite-flat moment degrees in 14.3.1--5; its independence under appending units is built into that construction. CLD 5.8.1--6 gives the resulting top-form measure. No probability normalization occurs.

Recursive background is disclosed in the ledger: Berkovich analytic domains and affinoid compactness/noetherianity, analytic dimension, tropical image dimension, the canonical calibration construction and its degree multiplicativity, and real Radon representation and Stone-Weierstrass. These published foundations are not newly formalized here. The applied immediate proofs were read and their hypotheses checked; neither hashes nor source-reading records prove mathematics.

## 3. Whole reconstruction of 369: four calculus lemmas

### Item 1. Positive decomposition inside the same open

Let \(O\subset N\) be ordinary opens and let \(\beta\) be a compact symmetric \((q,q)\)-form on \(N\) whose support lies in \(O\). Then
\[
 \beta=\eta_+-\eta_-,\qquad
 \eta_\pm\in\mathcal A_c^{q,q}(O),\quad\eta_\pm\geq0,
\]
where the forms are extended by zero to \(N\). Apply the compact case of 6.5.2 on \(O\) itself, with the middle order-unit construction just explained. Each compact output is closed in the Hausdorff \(N\) and lies inside \(O\), so its zero extension is smooth. Its positivity is preserved. Output supports can exceed the input support but remain compact in the same specified open. This decomposes tests, not closed currents.

### Item 2. Signed coefficient measures and the weighted product bound

For a positive \(T\) and any compact diagonal smooth test \(\theta\) of complementary degree, the functional \(f\mapsto\langle T,f\theta\rangle\) on compact smooth scalars is a unique finite signed Radon measure \(\mu_{T,\theta}\). To prove this, discard the antisymmetric part of \(\theta\), decompose its symmetric part into two middle-positive compact forms by Item 1, and subtract their positive coefficient measures from 7.2.8, 7.2.11. The resulting functional is independent of the decomposition because compact smooth scalars are dense in compact continuous scalars. Its support is contained in \(\operatorname{supp}\theta\): on the complement the original smooth functional is zero, and scalar density there proves the assertion. This last fact does not require the positive decomposition to preserve the exact input support.

For \(\beta=\eta_+-\eta_-\) as above, \(\eta=\eta_++\eta_-\), and any continuous real \(b\), the ordinary product gives
\[
 |\langle bT,\beta\rangle|
 \leq\int |b|\,d\mu_{T,\eta}
 \leq\sup_{\operatorname{supp}\eta}|b|\,\langle T,\eta\rangle.
 \tag{1}
\]
Indeed coefficient-measure uniqueness identifies \(\mu_{T,\eta}\) with the sum of the two positive measures. The pairing with \(b\) is their difference of integrals, so the triangle inequality proves the first bound. A smooth plateau equal to one on each support identifies its mass with the corresponding current value, proving the second bound. For a general fixed signed coefficient measure one also has
\[
 |\langle bT,\theta\rangle|\leq
 \sup_{\operatorname{supp}\theta}|b|\,|\mu_{T,\theta}|(N).
 \tag{2}
\]
All these measures are finite for a compact test. Equation (2) proves \(b_iT\to bT\) for every locally uniformly convergent scalar net with fixed positive \(T\).

### Item 3. Correct-degree smooth multiplier identity

For a smooth real \(g\) and a positive doubly closed \(T\),
\[
 D(gT)=Dg\wedge T.\tag{3}
\]
Both sides are symmetric. For a compact symmetric \((r,r)\)-test \(\alpha\), set \(A=g\,d''\alpha-d''g\wedge\alpha\), of type \((r,r+1)=(q-1,q)\). Direct exterior Leibniz gives
\[
 Dg\wedge\alpha-gD\alpha
 =-d'A+C,\qquad
 C=d'g\wedge d''\alpha+d''g\wedge d'\alpha.
\]
The identities for \(J\) give \(JC=-C\). Symmetry of \(T\) annihilates \(C\), and \(d'T=0\) annihilates \(d'A\). The Hessian transpose identity proves (3). An arbitrary test may be replaced by its symmetric part because both currents are symmetric. The assumptions retain both closedness equations, without relying on the misindexed printed 8.5.3. In particular \(Dg=0\) implies \(D(gT)=0\).

### Item 4. Defect support and cutoff localization

Let \(Z\subset N\) be ordinary closed, and let \(h\) be continuous and ordinary smooth with zero smooth Hessian on \(N\setminus Z\). Then \(R=D(hT)\) is symmetric and has support contained in \(Z\). Equation (3) and restriction make it zero on the complement; support is defined by the largest ordinary zero open. Symmetry follows from \(DJ=JD\) and symmetry of the ordinary scalar product. If a smooth \(\chi\) is one near \(Z\cap\operatorname{supp}\alpha\), then
\[
 \langle R,\alpha\rangle=\langle R,\chi\alpha\rangle.\tag{4}
\]
The compact test \((1-\chi)\alpha\) has support disjoint from \(Z\) and therefore from \(\operatorname{supp}R\). This uses no assertion that the differentiated defect is order zero or positive.

## 4. Whole reconstruction of 369: cutoff and support theorems

### Item 5. The exact quantitative cutoff estimate

Keep Item 4's hypotheses on one fixed \(N\), and fix a compact symmetric \((r,r)\)-test \(\alpha\). Let \(S=Z\cap\operatorname{supp}\alpha\). For any ordinary neighborhood \(O\) of this compact set choose \(0\leq\chi\leq1\), compact smooth in \(O\), equal to one near \(S\). The cutoff theorem and smooth scalar composition provide it. Item 1 applied on \(O\) gives
\[
 D(\chi\alpha)=\eta_+-\eta_-,\qquad\eta=\eta_++\eta_-,
 \qquad \eta_\pm\geq0,
 \tag{5}
\]
with compact outputs in that same \(O\). For any smooth \(g\) on \(N\) with \(Dg=0\),
\[
 \begin{split}
 \langle D(hT),\alpha\rangle
 &=\langle D(hT),\chi\alpha\rangle
 =\langle(h-g)T,D(\chi\alpha)\rangle,\\
 |\langle D(hT),\alpha\rangle|
 &\leq\int|h-g|,d\mu_{T,\eta}
 \leq\sup_{\operatorname{supp}\eta}|h-g|\,\langle T,\eta\rangle.
 \end{split}\tag{6}
\]
The first equality is (4); the second is differential duality and (3); the inequalities are (1). If \(S\) is empty take all cutoff forms zero. Every object is an actual form or current upstairs, so moment refinements represent the same identity.

### Item 6. Weighted-error removability

If for each compact symmetric detecting \(\alpha\) a sequence or net of actual triples \((\chi_j,\eta_{j,\pm},g_j)\) as in (5)--(6), on the same \(N\), satisfies
\[
 \int|h-g_j|,d\mu_{T,\eta_j}\longrightarrow0,
\]
then \(D(hT)=0\). Apply (6) to a fixed left-hand pairing and let the right side tend to zero; symmetric tests determine the symmetric defect. The stronger product of supremum error and mass tending to zero suffices. This is an additional existence hypothesis, not a consequence obtained from \(D[h]=0\).

### Item 7. Cutoff mass, trace estimate and necessary blowup

Define
\[
 \mathcal C_{T,\alpha}(S;O)=
 \inf_{\chi,\eta_\pm}\langle T,\eta_++\eta_-\rangle,
 \tag{7}
\]
over the actual competitors (5) supported in \(O\). A competitor exists and each mass is finite, so this infimum is finite and nonnegative for each fixed \(O\). It increases when \(O\) shrinks, and is zero for empty \(S\). It is a test-specific quantity, not identified with a standard capacity.

For relatively compact \(O\) and fixed smooth harmonic \(g\), put \(\omega_g(O)=\sup_O|h-g|\). Taking the infimum in (6) gives
\[
 |\langle D(hT),\alpha\rangle|
 \leq\omega_g(O)\mathcal C_{T,\alpha}(S;O).\tag{8}
\]
No minimizer is assumed. If \(h=g\) on \(S\), compactness and continuity give arbitrarily small-oscillation relatively compact neighborhoods by intersecting a fixed neighborhood with \(\{|h-g|<\varepsilon\}\). A uniform bound on their cutoff masses, or merely a vanishing product in (8), makes the pairing zero. Conversely a detecting pairing of magnitude \(d>0\) forces
\[
 \mathcal C_{T,\alpha}(S;O)\geq d/\omega_g(O)
\]
whenever \(\omega_g(O)>0\); zero oscillation is impossible for such a detector. Thus small oscillation would force mass blowup for a nonzero defect. Pointwise finiteness alone gives no uniform bound. The later logarithmic construction supplies an actual uniform bound in a displayed analytic setting.

### Item 8. Ordinary local conclusion

If Item 6 or Item 7 establishes zero on each member of an ordinary cover of a specified \(W\), the identity holds on \(W\). Differentiation and continuous multiplication commute with restriction; finite localization of a compact test proves the global zero identity. This glues the original current. It does not glue approximate currents, and a specified cover is not an ambient ordinary-open basis.

### Item 9. Analytic dimension removability

If \(Z\) is ordinary closed and locally a closed analytic locus with
\[
 \dim Z<r=n-p-1,
\]
and \(h\) is continuous and ordinary smooth with zero smooth Hessian off \(Z\), then \(D(hT)=0\) for every original positive doubly closed \(T\). By Item 4 its defect is supported on \(Z\). On an ordinary neighborhood where the dimension bound holds, 15.2.1 makes every compact \((r,r)\)-test support disjoint from \(Z\). The support definition makes its pairing zero. All complementary tests vanish, and Item 8 globalizes the identity. The same proof works for ordinary closed \(Z\) with the pointwise condition \(d_K(z)<r\).

For a pure codimension \(c\), the integer bound is \(c\geq p+2\). At \(p=n-1\) it excludes no nonempty locus. For \(n=2\), its bounds are zero-dimensional loci at \(p=0\) and none at \(p=1\); for \(n=3\), dimensions at most one, at most zero, and none. Off-locus ordinary smooth harmonicity remains a premise.

### Item 10. Necessary detecting location and the dimensional window

Under Item 4 alone, a nonzero defect has a compact detecting test, whose symmetric part still detects it. Its support must meet \(Z\). By 15.2.1 every point of that support has \(d_K\geq r\). Thus a detector meets \(Z\) at a point with \(d_K\geq n-p-1\); a uniform analytic dimension bound below that value is impossible.

Applying Item 9 with \(T=\delta_X\), whose positivity and two closedness equations were checked above, gives \(D[h]=0\) when \(\dim Z<n-1\). It retains the actual generic integration lengths. It does not recognize \(h\) or \(-h\) as psh or supply separately admissible \(U,V\). For \(p\geq1\),
\[
 n-p-1\leq\dim Z<n-1
\]
is an unexcluded window of that dimension-only method. It is not a counterexample. There is no such window for \(p=0\).

## 5. Whole reconstructed scalar and relative-form proofs: 367 and 368

### Specified continuous potential class

Let \(\mathcal F(O)\subset C(O,\mathbb R)\) be any prescribed restriction-compatible class of finite real functions. Call a positive doubly closed current \(T\) BT for \(\mathcal F\) if for every ordinary \(O\) and every \(u,v\in\mathcal F(O)\) with \(D[u]=D[v]\), one has \(D((u-v)T|_O)=0\). This may be the original continuous individually psh class. Positivity and double closedness are part of the definition. The initial BT hypothesis in the following statements is explicit.

### Coefficient-measure compatibility for all smooth factors

Let \(T\) be positive, \(h\) continuous, and \(\beta\) any smooth form. For a compact test \(\omega\) complementary to \(\beta\wedge T\), \(\beta\wedge\omega\) has equal complementary type for \(T\). Item 2 applies, including its antisymmetric part. Since \(T\) has even total degree, the left wedge convention gives
\[
 \langle\beta\wedge(hT),\omega\rangle
 =\int h,d\mu_{T,\beta\wedge\omega}.\tag{9}
\]
If \(\beta\wedge T=0\), testing that zero current against all \(f\omega\) with smooth compact scalars and using measure uniqueness makes the measure in (9) zero. Therefore
\[
 \beta\wedge T=0\quad\Longrightarrow\quad\beta\wedge(hT)=0.
 \tag{10}
\]
For smooth \(a\), the same uniqueness gives \(\mu_{T,a\theta}=a\mu_{T,\theta}\), hence \(a(hT)=(ah)T\). If \(C=\gamma\wedge T\) is positive, compare its coefficient measure on \(\omega\) with \(\mu_{T,\gamma\wedge\omega}\) on all smooth scalars. Their equality proves
\[
 hC=\gamma\wedge(hT).\tag{11}
\]
For a continuous scalar \(a\geq0\), \(h(aT)=(ha)T\) follows as well: the smooth-scalar coefficient functional of \(aT\) is integration against \(a\mu_{T,\theta}\); uniqueness proves the claim. This constructs no continuous wedge on an arbitrary signed current. It only uses coefficient measures of the fixed positive \(T\).

### Graded Leibniz with a nonclosed \(hT\)

For any current \(S\), any smooth form \(\beta\) of total degree \(b\), and \(d=d'\) or \(d''\),
\[
 d(\beta\wedge S)=d\beta\wedge S+(-1)^b\beta\wedge dS.
 \tag{12}
\]
Proof on compact tests: for total degree \(m\) of \(S\), write \(\beta\wedge S=(-1)^{bm}S\wedge\beta\). Transpose differentiation introduces \((-1)^{m+b+1}\). Expand \(d(\beta\wedge\omega)=d\beta\wedge\omega+(-1)^b\beta\wedge d\omega\). The term containing \(d\omega\) becomes \((-1)^b\beta\wedge dS\) and the other becomes \(d\beta\wedge S\) with these wedge signs. This proves (12); alternatively it is the correctly tested proof of 7.7.7. It needs no closedness of \(S\).

For a smooth even-degree \((k,k)\)-form \(\gamma\), apply (12) twice:
\[
 D(\gamma\wedge S)=D\gamma\wedge S
 -d''\gamma\wedge d'S+d'\gamma\wedge d''S+\gamma\wedge DS.
 \tag{13}
\]
Let \(T\) and \(C=\gamma\wedge T\) both be doubly closed, with \(T\) positive. First-order Leibniz gives \(d'\gamma\wedge T=d''\gamma\wedge T=0\). Differentiating the second identity gives \(D\gamma\wedge T=0\). For \(S=hT\), (10) gives the same three smooth annihilators of \(S\). Differentiate them, remembering that \(d'\gamma\) and \(d''\gamma\) are odd:
\[
 0=-D\gamma\wedge S-d'\gamma\wedge d''S,
 \qquad
 0=D\gamma\wedge S-d''\gamma\wedge d'S.
\]
Both cross terms in (13) and the \(D\gamma\) term vanish. Consequently
\[
 D(\gamma\wedge(hT))=\gamma\wedge D(hT).\tag{14}
\]
In particular for a smooth scalar \(a\) with \(aT\) doubly closed,
\[
 D((ah)T)=aD(hT).\tag{15}
\]
No positivity or closedness of \(hT\) was assumed, and no two nonsmooth factors were wedged.

### Exact criteria on every ordinary open

If \(T\) is BT for \(\mathcal F\), a smooth real scalar \(a\) has \(aT\) BT for \(\mathcal F\) if and only if \(aT\) is positive and doubly closed. For \(a\geq0\) positivity is automatic, so double closedness alone is equivalent, and it is equivalent to \(d'a\wedge T=d''a\wedge T=0\).

More generally, for any smooth real \((k,k)\)-form \(\gamma\), \(p+k\leq n\), its actual product \(C=\gamma\wedge T\) is BT for \(\mathcal F\) if and only if \(C\) is positive and doubly closed. Neither positivity nor closedness of \(\gamma\) itself is required. The original nontrivial P21.3 current-degree range additionally has \(p+k\leq n-1\); degree \(n\) has no nonzero Hessian test and is automatic. Necessity is in the definition. For sufficiency restrict to arbitrary \(O\) and an admissible pair, put \(h=u-v\), apply the initial BT hypothesis to \(D(hT|_O)\), identify the actual ordinary product by (11), and apply (14). This is a proof for every ordinary open, not just pairs globally defined on a chart. First-order closedness is equivalently \(d'\gamma\wedge T=d''\gamma\wedge T=0\).

### Exact limit scopes

Suppose locally \(a_i\geq0\) is a net of smooth scalars converging locally uniformly to continuous \(a\), with each fixed-current product \(a_iT\) doubly closed and with initial \(T\) BT. Then \(aT\) is positive and doubly closed by (2) and differentiation on fixed compact tests. For any admissible \(h=u-v\) and compact detecting \(\omega\),
\[
 \langle D((a_i-a)hT),\omega\rangle
 =\int(a_i-a)h\,d\mu_{T,D\omega}\longrightarrow0.
\]
The support is compact, the measure finite, and \(h\) bounded there. Each earlier pairing is zero by (15), so the limit is zero. Ordinary localization proves the assertion on every open. Smooth approximation without closedness of every \(a_iT\) does not meet this hypothesis.

For form factors suppose \(\gamma_i\to\gamma\) in coefficients on compact test supports in a fixed finite family of common tropical charts, that the limit \(\gamma\) is smooth, and that each \(\gamma_i\wedge T\) is positive and doubly closed. Expand their difference in the fixed finite exterior monomial bases, localize a fixed test, and use (2) on each monomial times that test. Coefficient convergence proves weak convergence of the products. The same reasoning on \(d'\omega,d''\omega\) proves closedness in the limit; positivity passes on positive tests. Replacing the test by \(D\omega\) and multiplying bounded coefficients by the fixed continuous \(h\) proves BT in the limit using (11)--(14). No convergence in changing charts was asserted. The limit is explicitly a smooth form, not a newly defined nonsmooth wedge.

### The complete torus diagnostic and its permissible companion

Take \(K=\mathbb Q_\ell\) for any prime \(\ell\), \(X=(\mathbb G_{m,K}^2)^{\rm an}\), \(s_j=-\log|T_j|\), and \(T=\delta_X\). This is good, separated, strict, boundaryless, pure of dimension two. \(T\) is positive, doubly closed, and BT for every prescribed continuous potential class tautologically, since \(uT=[u]\). Let \(a=2+s_1^2>0\). Then
\[
 D(a\delta_X)=[2d's_1\wedge d''s_1].
\]
Choose nonzero \(\zeta\geq0\) in \(C_c^\infty(\mathbb R^2)\), and the actual analytic test \(\omega=\zeta(s)d's_2\wedge d''s_2\). Its support lies in a compact closed polyannulus, hence is compact. The identity moment has finite-flat degree one; 14.3.1--5, 14.5.3 and 5.8.4 give its canonical calibration. With the paired positive top-form orientation,
\[
 \langle D(a\delta_X),\omega\rangle
 =2\int_{\mathbb R^2}\zeta(s_1,s_2)\,ds_1ds_2>0.
\]
The factor is exactly two; this is not a probability-normalized measure. Thus \(a\delta_X\) is not doubly closed. It cannot be a counterexample to P21.3. It diagnoses the literal missing closedness premise in printed CLD 8.6.7, already warned about in the supplied book's Chapter 16. Its approximation proof does not preserve closedness. That source assertion is not used as a theorem.

For comparison let \(S=(d's_1\wedge d''s_1)\wedge\delta_X\). The form factor is smooth positive and doubly closed, so the exact criterion makes \(S\) BT. Both \(d'a\wedge S\) and \(d''a\wedge S\) vanish by repeated exterior generators. Thus \(aS\) is doubly closed and BT. The relative criterion permits genuinely nonconstant weights while excluding the preceding nonclosed weighting.

## 6. A further actual removability theorem: logarithmic cutoffs

### Statement

Let \(Z\) be ordinary closed and locally Zariski closed in analytic domains of \(W\). Let \(h\in C(W,\mathbb R)\) be ordinary smooth with zero smooth Hessian on \(W\setminus Z\). Assume that each point of \(Z\) has an ordinary neighborhood \(N\) and a smooth function \(g\) on \(N\) with \(Dg=0\) and \(h=g\) on \(Z\cap N\). Then
\[
 D(hT)=0
\]
for every positive doubly closed \((p,p)\)-current on \(W\), in every degree \(0\leq p\leq n-1\), over either valuation regime, retaining arbitrary singularities and nilpotents. There is no dimension bound on \(Z\) and no assumed cutoff mass bound. The smooth trace and off-locus regularity hypotheses are substantive. They are not proved for every original equal-curvature difference.

### Step A. An explicit smooth concave logarithmic exhaustion

Work locally in an affinoid neighborhood, and then in an ordinary relatively compact subopen \(N\), where \(Z\) is the common zero set of finitely many analytic \(f_1,\ldots,f_m\). This is the defining affinoid notion of a Zariski-closed analytic locus; finite generation is affinoid noetherianity. Choose a bound \(A\) larger than all \(\log|f_i|\) on that neighborhood by at least two. No scaling by a nontrivial field element is needed.

Let \(R_m(s)\) be the convolution of \(\max_i s_i\) with a product of nonnegative smooth probability kernels supported in \([-1/4,1/4]\) in each real coordinate. This real convolution is a mathematical construction, not a new analytic smoothing theorem. It is smooth and convex, differs from \(\max_i s_i\) by at most \(1/4\), and is translation equivariant in the all-ones direction. Smoothness follows by distributional convolution with a smooth compact kernel. If one coordinate is at least one below the maximum of the others, it never attains the maximum throughout the convolution support; the formula then omits that coordinate exactly, using the marginal product kernel. This exact omission allows coordinates \(s_i=-\infty\).

On \(N\setminus Z\) put
\[
 t=A-R_m(\log|f_1|,\ldots,\log|f_m|).
\]
At a zero of one \(f_i\) outside the common zero locus, exact omission holds on a neighborhood. The remaining nonzero functions are analytic units there, so 15.1.1--2 makes \(t\) ordinary smooth. It is nonnegative by the choice of \(A\), tends to infinity approaching \(Z\), and has \(Dt\leq0\) as a smooth \((1,1)\)-form: in each local unit chart convexity of \(R_m\) gives a positive semidefinite Hessian and every \(\log|f_i|\) is affine, with zero smooth Hessian. These are ordinary charts on the actual analytic domain.

Choose a smooth nondecreasing concave \(b:[0,\infty)\to[0,4]\) that equals the identity on \([0,2]\) and is constant for \(s\geq4\). It can be made by integrating a nonnegative smooth nonincreasing derivative that is one up to two and zero after four. For \(L\geq1\) put \(u_L=L b(t/L)\), and give it its constant value on \(Z\). It is smooth on \(N\) since it is constant on an ordinary neighborhood of \(Z\) for each fixed \(L\). Moreover
\[
 0\leq u_L\leq4L,\qquad Du_L\leq0,
 \qquad u_L=t\ \hbox{where }t\leq2L.
\tag{16}
\]
The chain rule proves concavity of its smooth Hessian. If a whole local component lies in \(Z\), the same constant definition applies there; it is still smooth near every point of \(Z\).

### Step B. Uniform curvature and energy bounds from the fixed closed current

Work on the ordinary \(N\) already chosen to carry analytic equations for \(Z\) and the trace \(g\). Let \(\alpha\) be any compact symmetric detecting test there, with \(K=\operatorname{supp}\alpha\). By 15.1.1(b), cover \(K\) by finitely many ordinary opens \(U_j\subset N\) on each of which \(\alpha\) has a smooth moment presentation in unit coordinates \(s_{j,1},\ldots,s_{j,d_j}\). Choose compact subsets of these opens whose interiors cover \(K\), then smooth nonnegative compact plateaus \(\rho_j\) supported in \(U_j\) and equal to one near the respective subsets, using 6.2.4. Thus at every point of \(K\), at least one \(\rho_j\) equals one on a neighborhood. No partition is required to have a single global moment presentation.

On \(U_j\), set
\[
 \lambda_j=\sum_{a=1}^{d_j}d's_{j,a}\wedge d''s_{j,a},\qquad \eta_j=\lambda_j^r.
\]
Both are smooth positive and doubly closed on their indicated opens; \(\eta_j=1\) for \(r=0\). Their pullbacks may be degenerate. The domination below will be proved before pullback, so degeneracy causes no issue. Set
\[
 M_j=|\mu_{T|_{U_j},D\rho_j\wedge\eta_j}|(U_j),\quad
 F_j=\langle T|_{U_j},\rho_j\lambda_j^q\rangle,\quad
 M=\sum_j M_j,\quad F=\sum_j F_j.
\]
These are finite constants for fixed tests, by Item 2. Products carrying \(\rho_j\) have compact support inside \(U_j\), and their zero extensions are ordinary smooth forms on \(N\). The smooth closed-factor case of Section 5 permits using \(T|_{U_j}\wedge\eta_j\) in the smooth identities; alternatively (3), Leibniz and closedness give the same identities directly.

Let
\[
 K_{j,L}=\langle T|_{U_j},\rho_j(-Du_L)\wedge\eta_j\rangle,\qquad
 E_{j,L}=\langle T|_{U_j},\rho_j\,d'u_L\wedge d''u_L\wedge\eta_j\rangle.
\]
Both are nonnegative because their test forms are positive. Smooth duality, both closedness equations for \(\eta_j\), and (16) give
\[
 K_{j,L}=-\langle u_LT|_{U_j},D\rho_j\wedge\eta_j\rangle\leq4LM_j.
\tag{17}
\]
The exact identity \(D(u_L^2)=2u_LDu_L+2d'u_L\wedge d''u_L\) gives
\[
 2E_{j,L}=\langle u_L^2T|_{U_j},D\rho_j\wedge\eta_j\rangle
       -2\langle T|_{U_j},\rho_j u_LDu_L\wedge\eta_j\rangle
 \leq16L^2M_j+8LK_{j,L}\leq48L^2M_j.
\tag{18}
\]
Writing \(K_L=\sum_jK_{j,L}\) and \(E_L=\sum_jE_{j,L}\), we obtain \(K_L\leq4LM\) and \(E_L\leq24L^2M\). These inequalities use ordinary coefficient measures of the fixed \(T\), not uniform control of an arbitrary changing family of tests. No potential derivative is multiplied by a nonsmooth current coefficient.

### Step C. Actual middle-positive decomposition with bounded mass

Fix a smooth nondecreasing \(\theta:\mathbb R\to[0,1]\), zero on \(( -\infty,1]\) and one on \([2,\infty)\). Define \(v_L=\theta(t/L)\), extended as one on \(Z\), and \(\sigma_L=\theta(2t/L)\). These are smooth by constancy near \(Z\). Choose a further compact plateau \(\rho_1=1\) near \(K\) and use \(\chi_L=\rho_1v_L\). It is compact, is one near \(Z\cap K\), and
\[
 \beta_L=D(\chi_L\alpha)=D(v_L\alpha)
 =v_LD\alpha+d'v_L\wedge d''\alpha-d''v_L\wedge d'\alpha
     +Dv_L\wedge\alpha.
\tag{19}
\]
The derivatives of \(\rho_1\) do not meet \(K\). The form is zero when \(t\leq L\), and every derivative of \(v_L\) is supported in \(L\leq t\leq2L\), where \(u_L=t\). Its support lies in \(K\).

Here is the needed algebraic domination in full, separately on each \(U_j\). On the compact coordinate image of \(\operatorname{supp}\rho_j\), the matrices for \(\alpha\) and \(D\alpha\), and the coefficients of \(d'\alpha,d''\alpha\), are bounded. Write \(\lambda=\lambda_j\) and \(\eta=\eta_j\) temporarily. Since powers of \(\lambda\) are middle order units on the finite coordinate space, \(-C\lambda^r\leq\alpha\leq C\lambda^r\) and \(-C\lambda^q\leq D\alpha\leq C\lambda^q\). If an exterior degree exceeds the coordinate dimension its corresponding coefficients are zero, and the same inequalities apply. For the cross term put \(y'=d't\) and \(y''=d''t\). Before pullback enlarge the coordinate space by one formal coordinate \(y\), keeping \(y'\) independent of the old coordinates. Decompose its \(q\)-th exterior power into old \(q\)-vectors and \(y\) wedged with old \(r\)-vectors. The cross term's symmetric matrix has only the two off-diagonal blocks between these summands. Bounded coefficients and
\[
 2|\langle A v,w\rangle|\leq C(|v|^2+|w|^2)
\]
bound both signs of that block by a constant times \(\lambda^q+L^{-2}y'\wedge y''\wedge\lambda^r\), with the \(L^{-1}\) cross coefficient absorbed by putting \(w/L\) in this inequality. Pullback preserves middle positivity, including when \(d't\) is dependent on the old coordinates. This proves the cross-term bound without claiming a strongly positive order unit on the entire symmetric space.

On the transition interval,
\[
 Dv_L=L^{-1}\theta'(t/L)Dt
      +L^{-2}\theta''(t/L)d't\wedge d''t.
\]
There \(Du_L=Dt\leq0\). Wedging \(-C\lambda^r\leq\alpha\leq C\lambda^r\) with the positive form \(-Dt\) or \(d't\wedge d''t\) proves both signs of the last term of (19) are bounded by a constant times \(L^{-1}(-Du_L)\wedge\eta+L^{-2}d'u_L\wedge d''u_L\wedge\eta\). Outside the transition interval those terms are zero. Bounded derivatives of the fixed \(\theta\) are absorbed into \(C\).

Take a common \(C\) for this finite family of coefficient bounds and \(\theta\), independent of \(L\). The zero extensions of the indicated compact terms give a smooth positive compact form on \(N\)
\[
 B_L=C\sum_j\rho_j\sigma_L\left(
 \lambda_j^q+L^{-2}d'u_L\wedge d''u_L\wedge\eta_j
          +L^{-1}(-Du_L)\wedge\eta_j\right)
\tag{20}
\]
such that \(B_L\pm\beta_L\) are middle-positive. Indeed wherever \(\beta_L\) can be nonzero, at least one \(\rho_j\sigma_L\) equals one, and its summand alone dominates both signs; all other summands are positive. Elsewhere \(\beta_L=0\). Put \(\eta_{L,\pm}=(B_L\pm\beta_L)/2\). They are the actual positive compact decomposition required by Item 5, and their sum is \(B_L\). They are supported inside the same ordinary neighborhood
\[
 O_L=\{t>L/3\}\cup Z
\]
of \(Z\cap K\), and inside the fixed compact \(H=\bigcup_j\operatorname{supp}\rho_j\). This set is ordinary open, since it is a strict bound on a continuous regularized norm-max expression, including its zero set. The support begins at \(t\geq L/2\), leaving the strict margin required to be contained in \(O_L\).

Since \(0\leq\sigma_L\leq1\), positivity and (17)--(18) prove the actual uniform estimate
\[
 \langle T,\eta_{L,+}+\eta_{L,-}\rangle
 \leq C(F+L^{-2}E_L+L^{-1}K_L)
 \leq C(F+28M).
\tag{21}
\]
In particular the cutoff mass infima for these shrinking neighborhoods are uniformly bounded. This is stronger than finiteness of one mass in each neighborhood.

### Step D. The trace forces vanishing

On the fixed compact \(H\), the sets \(t\geq L/2\) approach \(Z\). For any \(\varepsilon>0\), continuity and \(h=g\) on \(Z\cap H\) give a neighborhood of that compact zero set where \(|h-g|<\varepsilon\). On the compact complement, the maximum of the finitely many \(|f_i|\) has a positive lower bound; hence \(t\) is bounded above. For large \(L\), all supports in (20) therefore lie in the small-error neighborhood. Thus
\[
 \sup_{\operatorname{supp}B_L}|h-g|\longrightarrow0.
\]
Use the actual triple \((\chi_L,\eta_{L,\pm},g)\) in (6) and (21). Every detecting pairing tends to zero and is therefore zero. Finite ordinary localization proves the statement on \(W\). At \(r=0\) the same proof has \(\eta=1\), so it still works. The theorem has not postulated the desired vanishing cutoff certificates; it has constructed them from analytic equations and the trace.

### Isolated-point corollary

If \(Z\) is closed and locally a zero-dimensional analytic locus, and \(h\) is continuous and ordinary smooth harmonic off \(Z\), then \(D(hT)=0\) in every allowed degree. Locally a zero-dimensional affinoid quotient is Artinian and has finite underlying analytic support. Isolate each point by an ordinary neighborhood and take the constant trace \(g=h(z)\). This meets the preceding theorem. This includes \(p=n-1\), where the dimension-only theorem of 369 gave no nonempty-locus result. The affinoid Artinian/finite-support fact is the standard analytic noetherian dimension foundation, not a classification of arbitrary closed ordinary gluing sets.

## 7. A constructed closed-current approximation, and its limit

There is also a concrete use of the relative factor criterion that constructs approximants rather than assumes their closedness. On \(X=(\mathbb G_{m,K}^n)^{\rm an}\), over any complete \(K\), fix \(I\subset\{1,\ldots,n\}\), \(|I|=p\leq n-1\), and
\[
 S_I=\left(\bigwedge_{j\in I}d's_j\wedge d''s_j\right)\wedge\delta_X.
\]
It is positive, doubly closed and BT for any specified continuous potential class by the smooth-factor theorem, starting from the tautological BT current \(\delta_X\). For a continuous nonnegative \(A:\mathbb R^I\to\mathbb R\), define \(a(x)=A((s_j(x))_{j\in I})\). Convolve \(A\) with nonnegative real smooth probability kernels of support tending to zero. Their functions \(A_i\) are nonnegative, smooth, and converge uniformly on every compact subset; this follows from uniform continuity on a slightly larger compact set. No growth condition at infinity is needed for compact-kernel convolution.

For \(a_i=A_i(s_I)\), each \(d'a_i\wedge S_I\) and \(d''a_i\wedge S_I\) is exactly zero, because every differentiated coordinate already appears in the displayed exterior product. Each \(a_iS_I\) is consequently positive, doubly closed and BT. The fixed-current scalar-net proof then gives the same property for the actual ordinary product \(aS_I\) on every ordinary open. For example \(A(s_1)=|s_1|\) gives a nonsmooth scalar weight with an explicit closed smooth approximation. Finite nonnegative sums are handled by linearity.

This constructs an actual current approximation in one displayed family, compatible with all analytic unit refinements because the equalities are identities of ordinary forms. It is not an exhaustion of arbitrary currents. It falls within smooth-factor weak closure classes already excluded from the residual by the catalogue, so it is not counted as a new solution of the atom. For \(I\) empty it supplies only constant weights of \(\delta_X\).

## 8. Independent whole-review verdicts and the unresolved original

For ALL369 the ten conclusions are proved with their displayed extra hypotheses. Items 1--4 use the middle cone with output compact in the same open, correct degrees, smooth Hessian rather than only canonical nullity off the locus, and actual coefficient measures. Items 5--8 are exact conditional cutoff statements; no uniform mass bound is supplied by the original proof. Items 9--10 are correct below the detecting degree, and give no nonempty-locus conclusion at the top degree. Both actual FINAL and expanded local notes have been reviewed as different data artifacts. The verdict is correct as conditional partial progress after the explicit source/sign repairs in this reconstruction; no universal completion.

For ENTIRE367 the signed-measure proof as written has the strong-cone gap identified in Section 2. After its replacement by the middle-positive construction, the scalar identity, exact criterion, local uniform net theorem, torus diagnostic, and relative nonconstant-weight example all have complete proofs above. The verdict on the submitted proof is requires correction at that step; the reconstructed statements are proved. The detecting weighted torus current is not doubly closed and is not a P21.3 counterexample.

For ENTIRE368 the same decomposition gap requires the same correction. The ordinary scalar-product compatibility, smooth-annihilator inheritance, full graded identity with both cross terms eliminated for nonclosed \(hT\), every-open criterion, and fixed-common-chart convergence to a smooth form are proved above. The verdict on the submitted proof is requires correction at its decomposition step; the reconstructed conditional statements are proved. No nonsmooth form wedge or arbitrary-current density theorem is obtained.

The new logarithmic theorem does provide automatic bounded cutoff masses in a genuine analytic setting and removes isolated analytic points at the top current degree. It still requires off-locus ordinary smooth zero-Hessian regularity and a local ordinary smooth harmonic trace. The isolated-point corollary removes the trace hypothesis there by constants. These hypotheses have not been proved for arbitrary equal-curvature pairs at higher-dimensional residual gluing sets. The construction cannot be applied to a general ordinary closed skeleton by merely naming it analytic.

The remaining exact obligations are all complete fields including trivial valuation; all good separated strict boundaryless pure \(n\geq2\) spaces including singular, reducible and nonreduced ones; all ordinary opens; every \(p=0,\ldots,n-1\); arbitrary positive doubly closed ordinary CLD currents; and separately admissible finite continuous individually psh \(U,V\) with exact upstairs \(D[U]=D[V]\), using actual generic Artinian calibration weights. No theorem here supplies the extra regularity/trace geometry for every such pair. No general relation-preserving positive current exhaustion, positive/differential/product-compatible harmonic-test lift, or admissible analytic counterexample \((X,U,V,T,\alpha)\) has been produced.

In particular one may not use generated-CPsh recognition of both signs of \(h\), a symmetry identity for two nonsmooth factors, scalar extension of potentials as current ascent, or a strong-current lift as ordinary-product compatibility without a further proof. The explicit saturation-family exhaustion does not justify density in the full cone. A cover that proves an identity for one specified open remains different from a genuine basis that works inside every arbitrary open. Existing retired curves, full polycylinders, invariant split-toric and stated approximation classes are not claimed as new resolutions.

The original decision is therefore candidate=false. This draft supplies reconstructed whole proofs, corrections and a further analytic removability theorem. It supplies neither a complete original proof nor a complete admissible analytic counterexample. Integrity checks are not mathematical verification, and no catalogue acceptance, publication, compilation or editor action is requested or asserted.

## 9. Artifacts and rerun boundary

The full standalone paper is P21.3-review-paper.tex; whole-proof.md contains all the same proof sections and the complete independent source-application ledger. The complete preserved primary is in inputs-LOCALONLY/CLD-v2-full.txt and inputs-LOCALONLY/CLD-v2.pdf. The original task, manifest bindings, fresh-read units, proof coverage and separate whole-review verdicts are retained in this directory. Primary bodies and rendered PDF pixels remain local.

Rerun python audit_inputs.py, python create_notes.py, and python finish_artifacts.py from this directory. These are newly authored bounded standard-library scripts. They do not execute or import supplied programs. They verify byte bindings, LF evidence, finite diagnostic identities, note dependencies and artifact structure, and regenerate the notes and standalone TeX from this authored proof. They do not certify universal mathematics. The paper is not compiled and no tabs are opened. No subagents, extra model calls, external messages, publication or catalogue writes were used. No supervised heavy-compute service was provided; no heavy computation was needed or launched.

Reference: A. Chambert-Loir and A. Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2, preserved 2025 version. Public primary URL: https://arxiv.org/pdf/1204.6277v2.

# Complete independent source-application ledger

All intervals are inclusive LF intervals in the bound complete source. Formfeeds are retained. Primary text SHA256: 64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085. PDF SHA256: 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719. Literal bodies remain LOCALONLY.

## S01: CLD 1.3.6--7

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S01.txt, LF 1200--1252, 3472 bytes, SHA256 80173cb9e3c2d2f9f5d59c14dd54332b39655d0b0f1d889ac2685725bb56a511.

Statement and immediate-proof application: J d' = d'' J; J d'' = -d' J; DJ=JD; smooth graded Leibniz.

Hypothesis check: All smooth forms; the full monomial proof is retained.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S02: CLD 3.3.4--12

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S02.txt, LF 3715--3803, 6271 bytes, SHA256 27ed82bac34a4485a5d132ba8a9cd45062c7a398f642373ea7304e8263876151.

Statement and immediate-proof application: Ordinary forms are included among G-forms; support uses ordinary neighborhoods; differential and multiplication identities sheafify.

Hypothesis check: G-tropical spaces and their ordinary smooth subcalculus.

Independent use/correction: 3.3.10 printed commutation exponent repaired from exterior generators and 1.3.3; PDF page 80 inspected. 3.3.6 proof dk corrected to dtrop.

## S03: CLD 6.2.1--9

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S03.txt, LF 7070--7150, 4772 bytes, SHA256 a6076aba5050c5b83aae091f054a7d260a5b592693af32431625a9119b2b173c.

Statement and immediate-proof application: Locally differentially separated spaces have compact cutoffs and scalar density; compact localization requires only the stated compact support condition.

Hypothesis check: Locally compact G-tropical setting; paracompactness only where the statement explicitly requires it.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S04: CLD 6.5.1--3

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S04.txt, LF 7340--7385, 3250 bytes, SHA256 fe5fc249ed619478fa56cb89c5a8afad1632f7e8174bb10d698a76bfc7134c9f.

Statement and immediate-proof application: Every symmetric diagonal form supported in a paracompact locally differentially separated open is a difference of middle-positive forms; compact support gives compact outputs. Compact analytic supports on almost-good spaces meet the hypothesis.

Hypothesis check: The coefficient class is smooth here. Good ordinary analytic domains are almost good.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S05: CLD 7.1.1--9

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S05.txt, LF 7652--7831, 12512 bytes, SHA256 98486d39b381d6ae79277965f7d01ffac5e2892d123cf4aac2159fbc70a589cb.

Statement and immediate-proof application: Currents are continuous complementary-test functionals; smooth multiplication and restriction are defined; currents are an ordinary sheaf; support is the complement of the largest zero open.

Hypothesis check: Tropical level n; sheaf/support assertions use local differential separation.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S06: CLD 7.2.1--4

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S06.txt, LF 7916--7955, 3080 bytes, SHA256 4880c086da86a27c43b343644e1beae57b05110cf43c83cc85ce47eb153d6953.

Statement and immediate-proof application: Middle-positive currents are symmetric and nonnegative on middle-positive complementary tests; positivity is ordinary local.

Hypothesis check: Middle cone throughout, not strongly positive tests in its place.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S07: CLD 7.2.7--12

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S07.txt, LF 7973--8076, 7415 bytes, SHA256 b5e1634d0600f2204eb2c87cc1bdc081e2f6156e5b62360f643b43e10a882c4c.

Statement and immediate-proof application: Positive scalar currents correspond uniquely to positive Radon measures; a positive current paired with a positive complementary form gives such a coefficient measure, compact for a compact test. Locally bounded Borel multiplication is defined by coefficient measures.

Hypothesis check: Tropical level n, local differential separation. T has bidimension q,q and the coefficient test has type q,q.

Independent use/correction: 7.2.9 strong-domination step not imported. Middle-positive 6.5.2 plus scalar 7.2.8 supplies signed measures and order-zero bounds for the given middle-positive T.

## S08: CLD 7.3.1

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S08.txt, LF 8098--8104, 637 bytes, SHA256 18a13b42524a7681021fadbbc0ac0b180abc770f5b81189634f3077c1f8aa317.

Statement and immediate-proof application: Canonical integration defines a positive symmetric current delta_X of bidimension n,n.

Hypothesis check: The original calibrated tropical space, including its original analytic multiplicities.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S09: CLD 7.7.1--8

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S09.txt, LF 9307--9431, 6528 bytes, SHA256 943283615dc00b4389f5c63606689cddd13741d9b0306c6b83e55cef98f47f6d.

Statement and immediate-proof application: The signed transposed differentials are local, square-zero, anticommute, satisfy DJ=JD, and have <DS,alpha>=<S,Dalpha>. Delta_X is doubly closed when boundaryless.

Hypothesis check: Complementary degrees are interpreted from 7.1.1. Smooth support is compact whenever duality is used.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S10: CLD 11.1.7

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S10.txt, LF 14983--15012, 2506 bytes, SHA256 6efe2fa15d3425138409717a7512d91909e0b03be4f3c3e56e267d4bcdfefabd.

Statement and immediate-proof application: Every ordinary open is an analytic domain; analytic spaces have compact neighborhood bases; good spaces have affinoid neighborhood bases.

Hypothesis check: All complete fields, without nontrivial valuation or reducedness assumptions.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S11: CLD 11.2.3

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S11.txt, LF 15303--15348, 3611 bytes, SHA256 0f8682d72514fa5517e844260d1a8920ebac3719673c8486fbc76f54d2c99492.

Statement and immediate-proof application: Analytic dimension is unchanged by reduction; d_K is graded residual transcendence degree, and dim X = sup_x d_K(x).

Hypothesis check: General analytic dimension theory. This is not a license to reduce the currents.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S12: CLD 12.4.2

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S12.txt, LF 17459--17464, 410 bytes, SHA256 a07c43b58b7609adc73e193077e3217257793c6419f503426ccd7987eafcb558.

Statement and immediate-proof application: For every G-tropical chart, dim_trop,x(f) <= d_K(x) <= dim_x(X).

Hypothesis check: Topologically separated K-analytic spaces.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S13: CLD 15.2.1--9

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S13.txt, LF 21605--21696, 5878 bytes, SHA256 027ba59bb9616e1bebf666fb5b0bf4644f143cfeaec2915dffe657d75fd10b25.

Statement and immediate-proof application: Support of a type a,b G-form is contained in d_K >= max(a,b); a closed analytic locus of smaller dimension does not meet that support. Good separated spaces are locally holomorphically and differentially separated; compact cutoffs, density and compact localization are available.

Hypothesis check: 15.2.1 needs topological separation, no strictness, smoothness, nontrivial valuation or reducedness restriction. Analytic loci must be Zariski closed locally in an analytic domain.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S14: CLD 15.7.1--2 and surrounding definitions

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S14.txt, LF 22097--22148, 2961 bytes, SHA256 4d3c398c54e57c876c7940b857171447e9c3a9a1fa86deed8317b928eb0402ef.

Statement and immediate-proof application: A topologically separated pure n-dimensional analytic space has the canonical calibrated tropical level-n calculus; analytic-domain restriction agrees with that calculus.

Hypothesis check: Original pure n-space over the original complete field, without any reducedness or valuation restriction.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S15: CLD A.2.1--6

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S15.txt, LF 29090--29195, 8086 bytes, SHA256 e969de709974fe7a49a2fdf6a9f3fabd7fc09264d99bbbf57a92bb6ffa5104d6.

Statement and immediate-proof application: The compact cutoff and scalar density theorems for a locally separating continuous algebra stable under smooth composition.

Hypothesis check: Locally compact Hausdorff X; the ordinary CLD smooth sheaf meets smooth composition and local separation.

Independent use/correction: See proof-body.md Section 2 and the complete reconstructed proofs; imported reading grants are not premises.

## S16: CLD 1.10.1--2

Version: arXiv:1204.6277v2, cover 25 Jul 2025; internal title 29 Jul 2025, 0h06. Complete evidence: S16.txt, LF 2635--2684, 3726 bytes, SHA256 174778258977e10435e8ca8564510bacbe082e1059fdc13d70ad208457d4e029.

Statement and immediate-proof application: A symmetric diagonal smooth form on a polyhedral subspace is a difference of positive smooth forms.

Hypothesis check: Finite-dimensional affine space and polyhedral subspace; this is a recursive foundation of 6.5.2, not an analytic current assertion.

Independent use/correction: Only compact constant-majorant case applied, proved directly with middle PSD matrices; noncompact majorant wording/composition not imported.

## E01: CLD 1.2.6 matrix interpretation

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E01.txt, LF 886--936, 3678 bytes, SHA256 1fe60dd9c2ce6dc389b7ee0e65fe66efe50ded30f09368ee34b1ea4ba6dc089e.

Statement and immediate-proof application: Middle positivity is PSD with the exterior sign; used in compact order units and logarithmic cross-block domination.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Middle positivity is PSD with the exterior sign; used in compact order units and logarithmic cross-block domination.

## E02: CLD 1.2.11--13 full proofs

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E02.txt, LF 994--1115, 8779 bytes, SHA256 9e74fc180f402213b32c53643ffbc68db1bb8dedc4a61d1b27e44b132007ffc5.

Statement and immediate-proof application: Pullback and wedge preserve middle positivity; interior middle order units. Strong cone only has relative interior and can span a proper subspace.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Pullback and wedge preserve middle positivity; interior middle order units. Strong cone only has relative interior and can span a proper subspace.

## E03: CLD 1.3.3--4

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E03.txt, LF 1165--1188, 1629 bytes, SHA256 701bbaac2944b257b4c458c30244b288fb2a3b16f3e67c76f7242a0187af9afb.

Statement and immediate-proof application: Total-degree exterior commutation and J convention; repairs printed 3.3.10.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Total-degree exterior commutation and J convention; repairs printed 3.3.10.

## E04: CLD 5.8.1--6

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E04.txt, LF 6733--6833, 6132 bytes, SHA256 119f11b8f9f3b3137230f44f8a108dca924608b4ec2e3f000c6f80641d3d15c1.

Statement and immediate-proof application: Complete calibrated top measure construction; ordinary scalar integration.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Complete calibrated top measure construction; ordinary scalar integration.

## E05: CLD 8.5.3--8.6.7

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E05.txt, LF 10287--10397, 7383 bytes, SHA256 c4d0c9b2038f58926aa06129df3f86a26245b06b40c02d0bc0c154fdec4964dd.

Statement and immediate-proof application: Scope diagnostic: bidegree/bidimension repair; exact BT definition, locality, integration, closed smooth factors, weak limits, and missing closedness in literal 8.6.7.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Scope diagnostic: bidegree/bidimension repair; exact BT definition, locality, integration, closed smooth factors, weak limits, and missing closedness in literal 8.6.7.

## E06: CLD 14.2.1--2

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E06.txt, LF 20322--20356, 2708 bytes, SHA256 5e0d772da08f99241073ee9fc0c77d5a1a2ec4855a947896696c033de9cc17fa.

Statement and immediate-proof application: Finite-flat moment degree; identity torus degree one.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Finite-flat moment degree; identity torus degree one.

## E07: CLD 14.3.1--5

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E07.txt, LF 20722--20830, 8297 bytes, SHA256 9a215b5ad4120698b0ddfb99a0650da9f067a004d137d475d9f12fc5e1e57a41.

Statement and immediate-proof application: Canonical calibration and independence under changing moments; generic degree retained.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Canonical calibration and independence under changing moments; generic degree retained.

## E08: CLD 14.4.1--2

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E08.txt, LF 20868--20923, 4056 bytes, SHA256 56fb2d2f430ba2e75b8ce6ff2a5add8348586de1436f6d86fe97cce2fba8b640.

Statement and immediate-proof application: Calibrated finite pushforward: add fiber degrees using multiplicativity; actual nilreduction degree transported.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Calibrated finite pushforward: add fiber degrees using multiplicativity; actual nilreduction degree transported.

## E09: CLD 14.5.2--3

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E09.txt, LF 20953--21008, 3938 bytes, SHA256 b3e76b072c368fe110d67807ed3d4ef09a65b6640445c32143524e63107c5b60.

Statement and immediate-proof application: Calibrated moment image coefficient from finite-flat degree. Identity moment has coefficient one.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Calibrated moment image coefficient from finite-flat degree. Identity moment has coefficient one.

## E10: CLD 15.1.1--3

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E10.txt, LF 21543--21604, 4240 bytes, SHA256 151e0b1e8fc80afdf40c34bdd3e0e7dd3079aa836780e879d13742593232c216.

Statement and immediate-proof application: Ordinary open moment presentations and smooth logarithmic-unit functions. Used in actual cutoff construction; no reduction of currents.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Ordinary open moment presentations and smooth logarithmic-unit functions. Used in actual cutoff construction; no reduction of currents.

## E11: CLD 13.3.4--7

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E11.txt, LF 19232--19308, 5083 bytes, SHA256 e2225237379e8ae177362bd38833a03379cdaa89727ffd0bfb3e0124dcb83050.

Statement and immediate-proof application: Artinian normalization l(M)/l(A), generic length ratio lambda/mu, and inverse generic length for nilreduction.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Artinian normalization l(M)/l(A), generic length ratio lambda/mu, and inverse generic length for nilreduction.

## E12: CLD 15.4.1--3

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E12.txt, LF 21735--21778, 2343 bytes, SHA256 dbfb750b06a6a2b0b88b0ee0175e1fe7617aa83c41f2574b71e23bc588490b92.

Statement and immediate-proof application: Whole finite integral transport proof from calibrated pushforward, applied to explain actual integration multiplicities.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Whole finite integral transport proof from calibrated pushforward, applied to explain actual integration multiplicities.

## E13: CLD 16.6.3

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E13.txt, LF 23434--23462, 1763 bytes, SHA256 bb016e94a2bcf376705c8e8e02ef302cbab9693253af9e04394b6e3dc5ed47b8.

Statement and immediate-proof application: Whole component integration proof with actual generic lengths; no unit-weight replacement.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Whole component integration proof with actual generic lengths; no unit-weight replacement.

## E14: CLD A.2.7--11

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E14.txt, LF 29196--29294, 7262 bytes, SHA256 aca5dd90bd3bb2f394b0d457886fa3f5c7d592581200e5234e02f255b2f506ae.

Statement and immediate-proof application: Whole immediate partition statements/proofs read; only finite compact localization used and reproved directly.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Whole immediate partition statements/proofs read; only finite compact localization used and reproved directly.

## E15: CLD 12.1.2--5

Version: arXiv:1204.6277v2; header 25 July 2025; internal title 29 July 2025. Complete evidence: E15.txt, LF 16503--16600, 6390 bytes, SHA256 0c2055fac2ed00bc012e49d08fe19874b5d4766dcc18b550db2700c5486f1209.

Statement and immediate-proof application: Actual torus, continuous tropical coordinates and canonical skeleton; no assertion of current descent.

Hypothesis check: Original good separated pure ordinary analytic category; see complete checked hypotheses in Section 2 and the corresponding proof.

Independent use/correction: Actual torus, continuous tropical coordinates and canonical skeleton; no assertion of current descent.

## Recursive background and reading limits

Berkovich analytic domains, good affinoid neighborhoods, noetherian affinoid algebras and compactness; no fresh proof of all their foundations.

Analytic dimension and the graded residual invariant: 11.2.3, 12.4.2; deeper image-dimension inputs 12.2.8--10 remain published background.

Canonical analytic tropical structure: 15.7.1 uses 12.4.7,12.10.6,12.11.1,15.6.1,12.9.14; no independent reconstruction of all recursive chapters.

Calibration independence and finite-degree multiplicativity: 14.3--5,13.3 and the cited skeleton/flatness results; their applied immediate units read.

Real Radon representation and Stone-Weierstrass; immediate scalar-density/cutoff proofs read and their application hypotheses checked.

Real compact-kernel convolution, elementary exterior algebra and finite-dimensional PSD inequalities are proved or explained in this manuscript.

