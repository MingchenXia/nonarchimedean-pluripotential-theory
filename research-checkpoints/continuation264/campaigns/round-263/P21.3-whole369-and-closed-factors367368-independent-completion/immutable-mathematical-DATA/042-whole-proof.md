# A direct removability route for P21.3

Research draft, 8 October 2026. P21.3 is unresolved in this deliverable. The results below are proved partial progress, with their additional hypotheses displayed. No independent correctness verdict is claimed.

## The unchanged target

Let \(K\) be any complete non-Archimedean field, with trivial or nontrivial valuation. Let \(X\) be a good separated strict boundaryless pure \(n\)-dimensional \(K\)-analytic space, \(n\geq2\). For every ordinary open \(W\subseteq X\), every positive ordinary CLD current \(T\) of bidegree \((p,p)\), \(0\leq p\leq n-1\), satisfying both \(\mathrm d'T=0\) and \(\mathrm d''T=0\), and every separately admissible finite continuous psh pair \(U,V\) on \(W\), the target asks whether
\[
 D[U]=D[V]\quad\Longrightarrow\quad D(UT|_W)=D(VT|_W),\qquad D=\mathrm d'\mathrm d''.
\]
Here \([f]=f\delta_X\) uses the original canonical integration current. Its generic Artinian component lengths are retained. We do not replace \(X\) by its reduction, normalize its components, change its field, or replace its currents by tropical pushforwards.

Write \(h=U-V\), \(q=n-p\), and \(r=q-1\). The required equation is \(D(hT|_W)=0\). The testing degree for this equation is \((r,r)\); the testing degree for \(T\) is \((q,q)\). This distinction is used throughout, including \(r=0\) when \(p=n-1\).

The dossier's descriptions of previous positive ranges are context, not incoming mathematical premises. No previous manuscript or review result is used as a theorem. Our only published mathematical inputs are the explicitly checked ordinary CLD calculus below. In particular the proofs do not use generated-psh recognition of either sign of \(h\), a conversion from continuous Psh to CPsh, any current density theorem, a strong-current lift, or scalar descent.

## The new results and their scope

We prove a quantitative cutoff bound for a possible multiplier defect supported on a closed ordinary locus. It controls the ordinary product using the original current's positive coefficient measures. Cutoffs and their decompositions are actual CLD forms on one fixed ordinary open. The bound yields removability when its weighted errors vanish, and a necessary blowup condition for a nonzero defect when the difference has a smooth harmonic trace along the locus.

We also prove a geometric consequence using CLD's analytic dimension support principle. Suppose \(Z\subset W\) is closed and locally is a closed analytic locus of dimension less than \(n-p-1\), and \(h\) is ordinary CLD-smooth with zero smooth Hessian on \(W\setminus Z\). Then \(D(hT)=0\) for every allowed \(T\). This conclusion retains singularities, nilpotents and both valuation regimes. It has an extra hypothesis on the nonsmooth locus and on the smooth Hessian off that locus. We do not deduce that hypothesis from canonical Hessian equality.

These results concern a specified open carrying the pair. Applying them to all ordinary opens requires the additional hypotheses on each such open, or suitable ordinary local hypotheses there. No cover is turned into a basis. When \(p=n-1\), the analytic dimension bound is \(\dim Z<0\), so it removes no nonempty locus. The cutoff theorem still makes sense in that degree, but its vanishing condition is not established for arbitrary currents and pairs.

The exact universal residual is unchanged: prove annihilation for arbitrary admissible pairs and arbitrary positive doubly closed ordinary currents on every ordinary open, including gluing loci for which neither off-locus regularity nor the cutoff bound is known, or construct an admissible analytic counterexample with an actual compact detecting test.


# Checked ordinary calculus and reconstructed lemmas

## Published inputs and applicability

The source is Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2. The retained PDF cover says 25 July 2025; its internal title page says 29 July 2025, 0h06. This is recorded without substituting another version. The full retained text and PDF, rather than historical web units, supplied the immediate statements and proofs. Exact paths, complete proof intervals, hypotheses, recursive foundations and application checks appear in `whole-source-application-ledger.json` and `whole-source-application-ledger.md`.

CLD 11.1.7 says every ordinary open is an analytic domain, and provides compact neighborhood bases. CLD 15.7.1 gives the canonical tropical calculus for every topologically separated pure analytic space, and 15.7.2 identifies its restriction with the calculus of an analytic domain. Their statements impose neither nontrivial valuation nor reducedness. Our original hypotheses meet them; in particular separatedness gives the needed Hausdorff topology. No new nonpure analytic carrier is introduced.

CLD 15.2.2--5 says that good topologically separated spaces are locally holomorphically separated, hence locally differentially separated, and that a compact set has a smooth compact cutoff in a prescribed ordinary neighborhood. CLD 15.2.7 gives compact scalar smooth density. For compact localization, 15.2.9 supplies nonnegative smooth partitions; no global paracompactness of \(W\) is assumed. CLD 6.5.2, in its compact-support case, decomposes every symmetric compact smooth diagonal form as a difference of two middle-positive compact smooth forms. Its support hypothesis is explicitly satisfied on almost-good analytic spaces, hence on our good ordinary domains.

CLD 7.1.1 defines a current as a continuous linear functional on complementary compact smooth tests. Sections 7.1.4--7 supply symmetry, smooth multiplication, restriction and the ordinary sheaf property. Section 7.1.9 identifies support as the complement of the largest ordinary open where the current is zero; a test with compact support disjoint from this support pairs to zero.

CLD 7.2.1 defines middle positivity by symmetry and nonnegativity on middle-positive complementary tests. Sections 7.2.8 and 7.2.11 identify the coefficient functional for a positive complementary form with a unique positive Radon measure; for a compact form this measure has compact support. Section 7.2.12 defines multiplication by any locally bounded Borel scalar using these coefficient measures. For a continuous scalar this is the ordinary order-zero product in the target. No claim about representing an arbitrary signed order-zero current by a single scalar measure is made.

CLD 7.7.1--5 gives the signed transposed current differentials, their square-zero and anticommutation identities, \(DJ=JD\), and
\[
 \langle DS,\alpha\rangle=\langle S,D\alpha\rangle.
\]
Section 7.7.8 says differentiation commutes with ordinary restriction. CLD 1.3.6 and 3.3.10--11 give the corresponding smooth identities, particularly \(J\mathrm d'=\mathrm d''J\), \(J\mathrm d''=-\mathrm d'J\), and the graded Leibniz rule. All tests used below are compact in the fixed open on which the current is defined.

Finally, CLD Proposition 15.2.1 states exactly: for a topologically separated \(K\)-analytic space and a G-form of type \((a,b)\), its support is contained in \(\{x:d_K(x)\geq\max(a,b)\}\); if \(Y\) is a closed Zariski locus in an analytic domain and \(\dim Y<\max(a,b)\), its support does not meet \(Y\). Ordinary smooth forms are among these G-forms. Here
\[
 d_K(x)=\operatorname{trdeg}_{\widetilde K_1}\widetilde{\mathscr H(x)}_1
 +\dim_{\mathbb Q}\bigl(\mathbb Q\otimes_{\mathbb Z}(|\mathscr H(x)^\times|/|K^\times|)\bigr).
\]
Its complete proof uses the tropical dimension bound and CLD 3.3.6, then \(d_K(y)\leq\dim Y\). The dimension notion is analytic dimension, not the dimension of a coarse skeleton. This theorem is not applied to arbitrary closed ordinary subsets by assigning them an unproved analytic dimension.

## Lemma 1: localized positive decomposition

Let \(O\subset N\subset X\) be ordinary opens, and let \(\beta\) be a symmetric compact smooth \((q,q)\)-test on \(N\) with support compactly contained in \(O\). There exist middle-positive compact smooth tests \(\eta_+,\eta_-\) on \(N\), both supported in \(O\), with \(\beta=\eta_+-\eta_-\).

Proof. Apply the compact case of CLD 6.5.2 on the ordinary analytic domain \(O\) to \(\beta|_O\). Its output forms have compact support in \(O\). Extend each by zero to \(N\). Such an extension is smooth because its compact support is closed in the Hausdorff space \(N\) and is disjoint from \(N\setminus O\); extension preserves positivity. The resulting forms give the asserted decomposition. The possible enlargement of support is contained in \(O\), not in an arbitrary larger chart. This is a statement about tests, not a construction of closed currents by partitions.

## Lemma 2: weighted ordinary product bound

For a positive current \(T\) on \(N\), a symmetric compact test \(\beta=\eta_+-\eta_-\), and any continuous real scalar \(b\), put \(\eta=\eta_++\eta_-\). Let \(\mu_{T,\eta}\) be its positive coefficient measure. Then
\[
 |\langle bT,\beta\rangle|
 \leq\int_N |b|\,\mathrm d\mu_{T,\eta}
 \leq\|b\|_{\operatorname{supp}\eta}\langle T,\eta\rangle.\tag{1}
\]

Proof. For each \(\eta_\pm\), CLD 7.2.11 supplies a positive compact measure whose integral on a smooth scalar \(f\) is \(\langle T,f\eta_\pm\rangle\). Smooth scalar density and uniqueness show that addition of the coefficient measures agrees with the coefficient measure of \(\eta\). The ordinary product of 7.2.12 therefore gives \(\langle bT,\beta\rangle=\int b\,\mathrm d\mu_{T,\eta_+}-\int b\,\mathrm d\mu_{T,\eta_-}\). The triangle inequality proves the first estimate. Each measure is supported on its test support. Its total mass is \(\langle T,\eta_\pm\rangle\), as follows by testing a smooth cutoff equal to one there. This proves the second estimate. This reasoning also reconstructs the product bound independently of any previous manuscript's lemma.

## Lemma 3: smooth harmonic multipliers

If \(T\) is positive and doubly closed on \(N\), and \(g\) is ordinary CLD-smooth there, then
\[
 D(gT)=T\wedge Dg.\tag{2}
\]
In particular, zero smooth Hessian \(Dg=0\) implies \(D(gT)=0\).

Proof. Positivity makes \(T\) symmetric. It suffices to test against symmetric compact \((q-1,q-1)\)-forms \(\alpha\), since both currents in (2) are symmetric. Put \(A=g\mathrm d''\alpha-\mathrm d''g\wedge\alpha\), a compact \((q-1,q)\)-form. The smooth Leibniz rule gives
\[
 Dg\wedge\alpha-gD\alpha
 =-\mathrm d'A+C,
 \qquad C=\mathrm d'g\wedge\mathrm d''\alpha+\mathrm d''g\wedge\mathrm d'\alpha.
\]
Because \(g\) and \(\alpha\) are symmetric, the identities for \(J\) give \(JC=-C\). Thus \(T\) annihilates \(C\). Its first closedness equation annihilates \(\mathrm d'A\); both closedness equations are assumed throughout. Hence \(\langle T,Dg\wedge\alpha\rangle=\langle T,gD\alpha\rangle\). Smooth multiplication and current differential duality now prove (2). This proof uses the exact complementary degrees and does not import the inconsistent bidegree/bidimension indexing in the printed CLD 8.5.3 statement.

## Lemma 4: support of the defect and localization of tests

Suppose \(Z\subset N\) is ordinary closed and \(h\in C(N,\mathbb R)\) is ordinary smooth with zero smooth Hessian on \(N\setminus Z\). For positive doubly closed \(T\), set \(R=D(hT)\). Then \(R\) is symmetric and \(\operatorname{supp}R\subset Z\). If \(\alpha\) is a compact test of its complementary degree and \(\chi\) is smooth and equal to one on an ordinary neighborhood of \(Z\cap\operatorname{supp}\alpha\), then
\[
 \langle R,\alpha\rangle=\langle R,\chi\alpha\rangle.\tag{3}
\]

Proof. On \(N\setminus Z\), equation (2) and restriction give \(R=0\). This proves the support assertion by CLD 7.1.9. The product \(hT\) is symmetric, and \(DJ=JD\), so \(R\) is symmetric. The support of \((1-\chi)\alpha\) is disjoint from \(Z\): it is contained in \(\operatorname{supp}\alpha\) and the factor vanishes near every point of its intersection with \(Z\). It is compact. The support property of currents consequently gives (3). We have not inferred an order-zero property for \(R\) and do not need it.


# A weighted cutoff theorem on a fixed ordinary open

## Theorem 5: a quantitative bound for every possible detecting test

Fix one ordinary open \(N\), a positive doubly closed \((p,p)\)-current \(T\) there, an ordinary closed set \(Z\subset N\), and \(h\in C(N,\mathbb R)\) which is ordinary smooth with zero smooth Hessian on \(N\setminus Z\). Set \(R=D(hT)\). Fix a symmetric compact ordinary smooth \((r,r)\)-test \(\alpha\), where \(r=n-p-1\), and put \(S=Z\cap\operatorname{supp}\alpha\).

Let \(O\subset N\) be any ordinary open neighborhood of this compact set \(S\). Choose \(\chi\in C_c^\infty(O)\), extended by zero to \(N\), with \(0\leq\chi\leq1\) and \(\chi=1\) near \(S\). Choose a positive decomposition in \(O\),
\[
 D(\chi\alpha)=\eta_+-\eta_-,\qquad \eta=\eta_++\eta_-,\quad
 \eta_\pm\in\mathcal A_c^{q,q}(O),\quad \eta_\pm\geq0.\tag{4}
\]
Let \(g\) be any ordinary smooth function on \(N\) with zero smooth Hessian. Then
\[
 |\langle D(hT),\alpha\rangle|
 \leq\int_N|h-g|\,\mathrm d\mu_{T,\eta}
 \leq\|h-g\|_{\operatorname{supp}\eta}\langle T,\eta\rangle.\tag{5}
\]
All these objects exist except for any requested bound on the right side. When \(S\) is empty we may take \(\chi=0\) and \(\eta_\pm=0\).

Proof. Existence of a compact smooth cutoff is CLD 15.2.5. Composing such a cutoff with a smooth scalar function that is zero near zero, one near one, and takes values in \([0,1]\), gives the displayed bounds without enlarging its support. Since \(D(\chi\alpha)\) is symmetric, compact, of degree \((q,q)\) and supported in \(O\), Lemma 1 proves (4). Lemma 4, current duality, and Lemma 3 give the exact identity
\[
 \langle D(hT),\alpha\rangle
 =\langle D(hT),\chi\alpha\rangle
 =\langle (h-g)T,D(\chi\alpha)\rangle.\tag{6}
\]
Indeed \(\langle gT,D(\chi\alpha)\rangle=\langle D(gT),\chi\alpha\rangle=0\). Lemma 2 with \(b=h-g\) proves (5). No derivative of the continuous function \(h\) has been taken as a smooth form. No nonsmooth wedge product is used. Both the product and its detecting test are upstairs on the original analytic space.

## Corollary 6: weighted removability

Under the hypotheses of Theorem 5, suppose that for every symmetric compact detecting test \(\alpha\), there is a sequence or net of actual triples \((\chi_j,\eta_{j,\pm},g_j)\) satisfying (4), the cutoff condition near the same \(S\), and \(Dg_j=0\), on the fixed \(N\), for which
\[
 \int_N|h-g_j|\,\mathrm d\mu_{T,\eta_j}\longrightarrow0.\tag{7}
\]
Then \(D(hT)=0\) on \(N\). The sufficient condition \(\|h-g_j\|_{\operatorname{supp}\eta_j}\langle T,\eta_j\rangle\to0\) may replace (7).

Proof. Apply (5) to each triple. Its left side is a fixed nonnegative number, so (7) forces it to be zero. Symmetric tests detect the symmetric current \(D(hT)\), proving the assertion. The sufficient condition follows from the second inequality of (5). The reference functions need not approximate \(h\) off the cutoff supports. Thus this result is distinct from locally uniform smooth harmonic approximation on a whole neighborhood. It is explicitly a sufficient condition, not an existence theorem for the triples.

## A cutoff mass quantity

For the fixed \(T,Z,\alpha\), define
\[
 \mathcal C_{T,\alpha}(S;O)
 =\inf_{\chi,\eta_\pm}\langle T,\eta_++\eta_-\rangle,\tag{8}
\]
where the infimum is over exactly the cutoffs and actual positive decompositions (4) supported in \(O\), with \(\chi=1\) near \(S\). This is a test-dependent cutoff mass, not an identification with any standard pluripotential capacity. It is nonnegative and finite for each such \(O\), because Theorem 5 constructs at least one admissible decomposition and a current is finite on each compact smooth test. It is zero for \(S=\varnothing\). If \(O_1\subset O_2\), then \(\mathcal C(S;O_1)\geq\mathcal C(S;O_2)\), since the smaller open admits fewer competitors. No uniform bound as the open shrinks follows from pointwise finiteness.

## Theorem 7: smooth trace and the necessary blowup of cutoff mass

Keep the hypotheses of Theorem 5 and fix a smooth zero-Hessian \(g\) on \(N\). For a relatively compact ordinary neighborhood \(O\) of \(S\), put
\[
 \omega_g(O)=\sup_{x\in O}|h(x)-g(x)|.
\]
Then
\[
 |\langle D(hT),\alpha\rangle|
 \leq\omega_g(O)\mathcal C_{T,\alpha}(S;O).\tag{9}
\]
In particular, if \(h=g\) on \(S\), and for a sequence of relatively compact neighborhoods \(O_j\) of \(S\) we have
\[
 \omega_g(O_j)\to0,
 \qquad\omega_g(O_j)\mathcal C_{T,\alpha}(S;O_j)\to0,\tag{10}
\]
the detecting pairing is zero. Uniform boundedness of these cutoff masses is one sufficient way to meet (10).

Conversely, if the detecting pairing has absolute value \(d>0\), then every such \(O\) with \(\omega_g(O)>0\) satisfies
\[
 \mathcal C_{T,\alpha}(S;O)\geq d/\omega_g(O).\tag{11}
\]
No such neighborhood can have \(\omega_g(O)=0\). Consequently if \(h=g\) on \(S\), every sequence of neighborhoods with \(\omega_g(O_j)\to0\) has cutoff masses tending to infinity for a nonzero detecting pairing.

Proof. For any admissible competitor, (5) bounds the pairing by \(\omega_g(O)\langle T,\eta\rangle\). The oscillation is finite by continuity and relative compactness. Taking the infimum over competitors proves (9), without assuming that the infimum is attained. If the oscillation is zero, (9) gives zero outright. Otherwise division by that positive number proves (11). These facts prove (10) and the converse assertion. If \(h=g\) on the compact set \(S\), small-oscillation neighborhoods exist: intersect a relatively compact neighborhood of \(S\) with \(\{|h-g|<\varepsilon\}\). Compactness and local compactness allow this at every positive \(\varepsilon\). What is not automatic is the needed bound on their cutoff masses.

Constants are smooth zero-Hessian reference functions. Thus the same result applies when \(h\) has a locally constant trace along the locus, using a finite ordinary localization of each compact test if different constants occur on different local pieces. More generally a local smooth harmonic extension of the trace suffices, with the corresponding cutoff bounds on each ordinary neighborhood.

## Corollary 8: the ordinary local conclusion

Let a specified ordinary open \(W\) have an ordinary cover \((N_a)\). Suppose that on each member the off-locus hypothesis of Theorem 5 and its weighted vanishing conclusion (7), or (10) for every detecting test, hold for \(h|_{N_a}\) and \(T|_{N_a}\). Then \(D(hT)=0\) on \(W\).

Proof. Corollary 6 or Theorem 7 gives zero on each member. Ordinary restriction commutes with differentiation and continuous multiplication. The current sheaf property, or a finite smooth localization of each compact test, gives zero on \(W\). This glues already established identities of the original current. It does not glue approximating currents or turn the cover into an ordinary-open basis.


# Analytic dimension removability

## Theorem 9: a degree-specific analytic exceptional locus

Fix an ordinary open \(W\) in the original ambient space, \(p\in\{0,\ldots,n-1\}\), and \(r=n-p-1\). Let \(Z\subset W\) be ordinary closed. Assume that locally on \(W\), \(Z\) is a closed analytic locus of dimension strictly less than \(r\). Let \(h\) be continuous on \(W\) and ordinary CLD-smooth with zero smooth Hessian on \(W\setminus Z\). Then for every positive doubly closed ordinary current \(T\) of bidegree \((p,p)\) on \(W\),
\[
 D(hT)=0.\tag{12}
\]
In particular this proves the desired Bedford--Taylor equality for any separately admissible continuous psh pair \(U,V\) whose difference has these additional properties. It imposes no approximation, laminarity or prescribed factor hypothesis on \(T\).

Proof. Lemma 4 gives \(\operatorname{supp}D(hT)\subset Z\). On a neighborhood where the analytic locus has dimension less than \(r\), every compact smooth test \(\alpha\) of degree \((r,r)\) has support disjoint from that locus, by the exact CLD 15.2.1(b) support principle. Thus its pairing with \(D(hT)\) is zero by the current support definition. All tests of the complementary degree vanish against the defect, so that current is zero on the neighborhood. The ordinary sheaf property proves (12) on \(W\). Alternatively localizing a given compact test into finitely many such neighborhoods gives the same proof. No positivity or order-zero property of the differentiated defect is needed.

The same proof works for any ordinary closed \(Z\) with the pointwise condition \(d_K(z)<r\) for every \(z\in Z\), using CLD 15.2.1(a). This alternative is a condition on the original analytic points, not a claim about a projected fan.

When the locus is of pure analytic codimension \(c\), the sufficient integer bound is \(c\geq p+2\). More generally use its local analytic dimension bound directly. For \(n=2\), the case \(p=0\) permits zero-dimensional analytic loci and \(p=1\) permits no nonempty analytic locus. For \(n=3\), the bounds are dimension at most one for \(p=0\), at most zero for \(p=1\), and no nonempty locus for \(p=2\). At every dimension, the top allowed degree \(p=n-1\) has scalar detecting tests and receives no nonempty-locus conclusion from this argument.

## Corollary 10: a necessary location for a defect and a dimensional window

Assume only that \(Z\) is ordinary closed and \(h\) is continuous and ordinary smooth with zero smooth Hessian off \(Z\), without imposing Theorem 9's dimension inequality. If \(D(hT)\ne0\), it has a compact smooth detecting test whose support meets \(Z\) at a point \(z\) with \(d_K(z)\geq n-p-1\). For an analytic locus with a uniform local dimension bound, that bound cannot be strictly less than \(n-p-1\).

Proof. A nonzero current has a compact detecting test by its definition as a nonzero functional. Symmetry permits its symmetric part. Its pairing cannot be nonzero if its support is disjoint from \(Z\). CLD 15.2.1(a) says every point in the support of this \((r,r)\)-test has \(d_K\geq r\). This proves the assertion, with all tests on the actual analytic domain.

For comparison, suppose only that the closed analytic locus has dimension less than \(n-1\). The canonical integration current \(\delta_X|_W\) is positive and doubly closed by CLD 7.3.1 and 7.7.4, so Theorem 9 applied with \(p=0\) proves \(D[h]=0\). This observation keeps its actual nonreduced integration weights. It does not say that \(h\) or \(-h\) is psh, or that a separately admissible pair exists with difference \(h\).

For \(p\geq1\), the inequalities
\[
 n-p-1\leq\dim Z<n-1
\]
therefore describe a remaining dimensional window in this particular off-locus route: canonical nullity follows, while dimensional support alone does not settle the multiplier equation in degree \(p\). This is a window of unexcluded possibilities, not a construction of a defect. For \(p=0\) there is no such window. For general ordinary closed gluing loci neither inequality is substituted for the pointwise analytic statement without proof.


# Decision, noncircularity and remaining work

## What the proofs do establish

Theorem 5 is a direct relation-preserving bound for the original ordinary product. It never introduces a functional on a coarse moment image. Each cutoff and each positive decomposition is an actual analytic CLD form; hence any additional analytic-unit moment presentation represents the same form. Closedness is used for the original \(T\), whose two equations remain exact. Neither a positive partition of unity nor a finite list of tests is used to certify an approximating current.

Theorem 7 shows that, when the difference has a smooth harmonic trace on the compact exceptional set meeting a detecting test, a nonzero product Hessian forces the associated cutoff masses to diverge at least inversely with the local oscillation. Pointwise finiteness of every cutoff mass is proved, but a uniform bound is not. This separates a usable direct removability argument from a nonexistent automatic estimate. The weighted form (7) can use nonsmooth residual behavior away from the cutoff supports, so it does not require whole-neighborhood smooth harmonic approximants.

Theorem 9 is an actual analytic partial theorem retaining arbitrary positive doubly closed currents and every original field and singularity regime. It is conditional on an explicit analytic exceptional-locus bound and ordinary smooth zero-Hessian regularity off that locus. It does not classify arbitrary continuous zero-current functions. No novelty priority in the literature is asserted for this consequence of the checked CLD support theorem.

## Attempts to reach the universal statement

We investigated localizing the entire possible defect to a gluing locus and replacing unknown function regularization by positive coefficient-measure estimates. The exact identity (6) succeeds. Turning it into a universal vanishing theorem would require proving both an appropriate off-locus regularity statement and (7) or (10) for every original pair and current. Neither follows from \(D[h]=0\). In particular knowing that each competitor in (8) has finite mass gives no control of its infimum as the support is confined to smaller neighborhoods.

The dimensional route succeeds below the detecting degree. At the critical detecting dimension a smooth test may meet the locus; CLD's support theorem then gives no vanishing. It does not construct a positive closed defect either. The top degree \(p=n-1\) exposes this limit immediately, because its detecting test is a scalar. Residual type--2 loci and their products are not automatically closed analytic loci, and no claim about their analytic dimension is inferred from a skeleton or a tropical pushforward.

The earlier full native104 paper was read as historical data to avoid presenting its scalar polar criterion as a solution. Its finite-test feasibility and quotient-cone conditions remain missing analytic gates. The earlier support paper was likewise read as context; no result from either is a premise here. We have not established a compatible current exhaustion on any general analytic germ, a positive harmonic-test extension with both differential equations and ordinary-product agreement, or a genuine upstairs weighted-gluing counterexample. No current or product has been ascended and descended through a field extension.

## Exact scope decision

The literal original assertion is not answered. The additional off-locus and cutoff or dimension hypotheses are not known for all original equal-curvature pairs on every ordinary open. No actual analytic \(X,U,V,T,\alpha\) with nonzero detecting pairing has been exhibited. Accordingly `candidate=false`. This is a full standalone account of new partial research, not a universal P21.3 paper claiming completion.

The supplied catalogue's retired curve, polycylinder, invariant split-toric and stated approximation ranges are not counted as new solutions. The new support and cutoff results do not alter the task's quantifiers: all ordinary opens, \(n\geq2\), all \(p=0,\ldots,n-1\), both valuations, reducible and nonreduced analytic spaces, the original generic lengths and separately admissible finite continuous psh \(U,V\) remain in the unresolved universal residual.

## Evidence and reproducibility limits

`P21.3-paper.tex` contains the complete standalone proof, and `whole-proof.md` contains the same mathematical sections. `sections/` retains separately bound complete section bodies. `native-notes.json` and `notes.json` record the local notes and their backward support dependencies. `whole-proof-coverage.json`, `exact-scope.json`, `original-scope-and-noncircularity-decision.json`, `decision-evidence.json` and `section-bindings.json` expose the coverage and negative scope decision.

Run `python reproduce.py` in this directory to regenerate the paper and whole proof from the authored section bodies, bind the section contents, reconstruct complete immediate source evidence from the retained full CLD text, and check the artifact schemas and note supports. The checker uses only Python's standard library, does not import or execute supplied programs, and does not compile TeX or open editor tabs. `commands.json` and `environment.json` record the command and environment. `checks-output.json` records artifact integrity checks, which are not a mathematical verification.

No heavy computation, additional model call, subagent, installation, publication, catalogue write or external communication was performed. No supervised heavy-compute service was supplied or needed. The recursive published foundations of CLD are disclosed in the source ledger; they are not represented as independently formalized here. A source hash, reading record, successful script or correct schema is not a mathematical premise.

## Reference

Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, cover dated 25 July 2025, retained internal title dated 29 July 2025. Public primary URL: https://arxiv.org/pdf/1204.6277v2.

