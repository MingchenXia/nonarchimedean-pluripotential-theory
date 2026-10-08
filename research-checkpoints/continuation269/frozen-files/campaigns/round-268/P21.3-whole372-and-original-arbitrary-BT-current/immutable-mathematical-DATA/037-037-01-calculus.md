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
