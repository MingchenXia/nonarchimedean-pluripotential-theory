# Sequential source reading: positive-weight analytic estimates

8 October 2026. One complete thirty-page source and fourteen selected dependency pages; 44 exact-source/page pairs in 23 individually displayed matching images. The notes retain provisional concerns and later source resolutions. Preparation and searches receive no actual reading credit. No separate-model verification receipt.

## Complete Jubert–Pan v1


# Actual primary reading 01 — physical pages 1–2

Read the complete selected text and displayed sheet_01.png individually, in order, from the fixed arXiv:2610.10216v1 PDF (SHA256 f0e067da80dce5007e29f926c2e328703eb09be3fbd9b1232c2fe28cb21abfcb). This note credits only pages 1–2; preparation has no reading credit.

The setup is a compact Kähler manifold, a compact torus in the reduced automorphism group, a fixed Kähler class and compatibly normalized moment polytope. The extremal equation uses a positive smooth v and positive smooth w, with an extremal affine function multiplying w. The overview removes log-concavity of v in the analytic correspondence, replacing the forward-trace Aubin–Yau estimate by a reverse-trace Chern–Lu estimate. Hessian(log v) cannot be dropped by sign for a general v; the new method must control it through moment-map estimates.

The introductory Theorem A states constants independent of the solution without listing entropy/normalization dependence. This is not yet a safe standalone uniform estimate: inspect the precise Theorem 2.1 and the normalization of its solution family before importing. The two displayed exponents are 2p+2 for tr_hat(omega), and (2p+2)/(n−1) for tr_omega(hat omega); the dimension-one denominator needs separate treatment rather than an invented endpoint. Nothing here settles a non-Archimedean envelope, Siu decomposition, or any canonical open-problem atom.


# Actual primary reading 02 — physical pages 3–4

Read complete text and individually displayed sheet_02.png after note 01. Same fixed v1 PDF. Only pages 3–4 credited.

Claim 2.2 controls the moment-map gradient pairing by background data; the second moment-map derivative contribution cancels against the weighted Laplacian of the reverse trace. Theorem B asserts existence of a (v,w)-extremal metric iff relative weighted Mabuchi is coercive modulo T_C on all T-invariant smooth metrics, with v,w positive smooth. Existence-to-coercivity is imported from AJL23; the reverse direction replaces the log-concave Laplacian estimates in the existing continuity proof, including twisted Theorem 2.3. This is not a self-contained new continuity proof in these pages.

Corollary C additionally assumes an ample L and alpha=2pi c1(L), and tests every T-equivariant dominating smooth test configuration using the relative weighted DF and reduced J^NA_{T_C}. Its algebro-geometric step is attributed to BJ25/Tru26; the analytic estimate alone cannot justify extending to arbitrary nonprojective classes or other stability test families. Primary dependent statements must be checked before importing this equivalence.

The Sasaki application fixes a regular reference Reeb chi inside a commuting compact CR torus and obtains a smooth compact Kähler quotient X_chi; the candidate Reeb xi can be irregular. The deformation family S_chi(xi^D) keeps the underlying Reeb vector field fixed. Page 4 appears to use xi rather than chi in the sentence describing the circle action defining the regular quotient; the definitions and later Section 4 control the intended quotient. Do not generalize to Sasaki manifolds without the regular reference or to orbifold quotients without an orbifold proof.


# Actual primary reading 03 — physical pages 5–6

Read complete text and individually displayed sheet_03.png in sequence. Fixed v1 PDF, pages 5–6 only.

The geometric motivation is that Sasaki weights are log-convex, so the earlier log-concave analytic theorem did not directly apply. Corollary D is explicitly restricted to the deformation family S_chi(xi^D) and the regular quotient, not arbitrary irregular Sasaki structures. AI-use declaration is an author statement, not an independent proof certificate and not a Rethlas receipt.

The source fixes d^c=i(bar partial−partial), dd^c=2i partial bar partial, Ric=−dd^c log omega^n (twice the common Ricci normalization), Delta=tr(dd^c), and m_{omega_phi}=m_omega+d^c phi evaluated on torus generators. Its weighted Ricci, weighted trace, and scalar curvature must be transported together; importing a formula alone into the book's dd^c convention would alter factors. Weighted Laplacian is Delta_hat,v f=Delta_hat f+<d log v(m_hat),df>_hat, with positive measure v(m_hat)hat omega^n. Smoothness on the moment polytope entails a smooth extension sufficient for Dv and D^2v. No new theorem has been entered in the book.


# Actual primary reading 04 — physical pages 7–8

Read full text and individually displayed sheet_04.png in sequence; pages 7–8 only.

Weighted cscK allows sign-changing w; weighted extremal instead starts with w>0 and replaces the cscK right-hand side by w times the affine extremal function. The weighted Futaki vanishing uses omega^n without an additional v factor. Uniqueness is modulo the identity component of the centralizer, and only for maximal T is that specialized to T_C. This distinction matters: Theorem B's unconditional T_C quotient for an arbitrary T is not justified by the stated setup. For trivial T on CP^1, ordinary cscK existence and unbounded noncompact automorphism orbits obstruct coercivity without quotienting by those automorphisms. Do not silently repair a source theorem and claim it was checked as printed.

Page 8 prints the Mabuchi derivative as integral f(w−Scal_v)v omega_phi^n, while condition (1.4) is integral(Scal_v−w)omega^n=0. The stated condition does not make the printed derivative vanish in the constant direction. This is an actual mismatch of formulas, not OCR: the displayed image contains the additional v. The original Lahdili definition and DJL variational functional must control any book formula. The issue might be a transcription error in preliminaries; it does not alone refute the later PDE estimates. Preserve the distinction and do not import this derivative.

Chern–Lu Lemma 1.1 uses an upper background bisectional bound and the source Ricci normalization. Inspect the detailed PDE system and constant dependence next. No claimed open-problem solution.


# Actual primary reading 05 — physical pages 9–10

Read full text and individually displayed sheet_05.png in sequence, pages 9–10 only.

The precise Theorem 2.1 resolves the overview's uniformity omission: Cp depends on L-infinity bounds for phi and F, fixed n,p,omega, a fixed basis of torus generators, sup(v), derivatives of log v through order two, positive min(v), sup|w|, normalized moment coordinates and Ricci moment coordinates. No entropy-only bound or estimate uniform along arbitrary automorphism orbits is stated here. For n=1 the second exponent is undefined, so restrict a literal imported trace statement to n>=2; no claimed failure of the one-dimensional PDE.

The system as printed is v(m_hat)hat omega^n=e^F omega^n and Delta_hat,v F=−w(m_hat)+tr_hat,v Ric(omega). In contrast, the earlier definitions Scal_v=v tr_hat,v Ric_v and Ric_v=Ric(omega)−dd^c F imply the geometric right-hand side is −w/v if Scal_v=w. This is a second normalization inconsistency visible in the primary pages. A safe PDE import must name its prescribed function separately (say h=w_geom/v) and cite the displayed system, without copying the purported equivalence. Positivity of v makes this reparametrization harmless for the estimate's bounded prescribed function but does not repair every variational claim automatically.

Weighted integration by parts is with v(m_hat)hat omega^n=e^F omega^n. Claim 2.2 is proved by the Hamiltonian relation, Cartan's formula and the wedge trace identity: the gradient pairing becomes the fixed background metric g_omega(xi_i,xi_j), and the second derivative equals L_{Jxi_i}(reverse trace)−tr_hat(L_{Jxi_i}omega). These identities are the crucial cancellation to inspect in the next pages.


# Actual primary reading 06 — physical pages 11–12

Read full selected text and individually displayed sheet_06.png in order; pages 11–12 only.

The reverse-trace estimate uses Ric(hat)=Ric(omega)−dd^c F+dd^c log v(m_hat). The derivative of the reverse trace along Jxi cancels against the weighted drift, leaving D^2 log v paired with g_omega(xi_i,xi_j) and D log v paired with tr_hat(L_{Jxi_i}omega). Thus absolute derivative bounds, not concavity, control the remainder. The background Ricci, Lie derivatives and bisectional bounds are fixed; summation multiplicities can be absorbed into basis-dependent Cv.

Set G=−aF−bphi, u=e^G tr_hat omega, H=e^G u^(2p). AM–GM and F bounded with v bounded below give a uniform positive lower reverse trace. The wedge operator Omega=n(n−1)omega wedge hat^(n−2) is positive and closed for n>=2. Its definition and the identity expressing the Ricci pairing through Delta_Omega match the trace identity. This proof is written for n>=2. Equation (2.7) bounds moment differences by fixed polytope size; (2.8) produces the good reverse-trace term after b is sufficiently large relative to a. Weighted integration by parts applied to u^(2p+1) gives (2.9) and a nonnegative gradient contribution. The sign of the troublesome Delta_Omega F term remains to be checked in the next step.


# Actual primary reading 07 — physical pages 13–14

Read all text and individually displayed sheet_07.png in sequence; pages 13–14 only.

The troublesome integral I is split via F=−(G+bphi)/a. I2 is bounded below using Delta_Omega phi <=(n−1)reverse trace and the fixed moment difference controlling the drift of phi. Its contribution is a multiple of the lower-order integral u^(2p+1), not the coercive u^(2p+2) term.

For I1, Omega is closed and integration by parts differentiates both H and v; dropping the derivative of v would be wrong. The source retains it and combines it with the drift using (2.18), turning the remainder into the background pairing <d log v wedge d^c G,omega>_hat. The positive Omega quadratic form and completing a square give the lower bound −p^2(reverse trace)|d log u|^2. Multiplying H converts it to the same gradient integral as (2.10). Need inspect the remaining drift estimate and parameter choice before accepting the final norm bound. No extra source hypotheses have been assumed implicitly.


# Actual primary reading 08 — physical pages 15–16

Read all text and individually displayed sheet_08.png in sequence; pages 15–16 only.

The remaining drift term is handled by expressing the mixed hat/background pairing as <dm_omega,df>_hat and integrating by parts once more. The derivative of v yields both D^2 log v and products of first derivatives; the moment-gradient cross pairing is fixed background data and dd^c m_omega=−L_{Jxi}omega. Lower reverse trace controls H by u^(2p+1). Constant Cv may be enlarged to at least one so the shorthand quadratic derivative bound is legitimate.

The positive background bilinear pairing allows Cauchy–Schwarz and Young, costing one further gradient coefficient and a lower-order term. Equation (2.28) gives I1 >=−(p^2+1)/a times the main gradient integral minus a bounded coefficient times integral u^(2p+1). The final combined inequality has coefficient 2p−(p^2+1)/a; it can be made nonnegative by a>= (p^2+1)/(2p). The good trace coefficient is b−(a+1)A0−C1. No use of a Hessian sign or log-concavity appears in these steps. The final passage from this inequality to the two norm bounds remains on the next page.


# Actual primary reading 09 — physical pages 17–18

Read all text and individually displayed sheet_09.png in sequence; pages 17–18 only.

The choice a=(p^2+1)/(2p) eliminates the gradient coefficient, and b large leaves a positive main trace term. Bounded G converts the weighted u inequality into a reverse-trace moment inequality. Hölder closes it because the total measure e^F omega^n is bounded. Comparing that measure to omega^n uses the two-sided L-infinity bound for F. The forward trace bound uses determinant times reverse trace^(n−1), hence explicitly n>=2. This completes the self-contained local estimate argument apart from standard Chern–Lu/trace/integration identities.

Theorem 2.3 addresses the twisted system with beta+dd^c f>=0 and bounded phi,F+f, not bounded F alone. It states integral e^((k−1)f)(forward trace)^k <=Ck, and under integral e^(−p0 f)<=M obtains L^q for 1<q<p0. The proof additionally normalizes sup(phi)=sup(f)=0; preserve that normalization when restating. The twist beta has a chosen moment map and compatible change under dd^c f; any constants involving those coordinates belong to fixed twist data. The inverse-trace lower bound is no longer uniform, and the proof deliberately retains reciprocal trace terms. Theorem B relies on these twisted estimates plus imported continuity arguments, not only Theorem 2.1.


# Actual primary reading 10 — physical pages 19–20

Read complete text and individually displayed sheet_10.png in sequence; pages 19–20 only.

The twisted argument retains the reciprocal-trace remainder, producing a lower moment of order 2p rather than asserting a nonexistent uniform reverse-trace lower bound. Hölder closes both lower moments because integral v(m_hat)hat omega^n <=sup(v)integral omega^n, independently of F; the cohomological volume suffices. The forward weighted moment follows from determinant comparison and bounded F+f. For smaller exponents choose a larger available reverse-trace moment and Hölder; the printed parameter family p>=1 need not cover them exactly. The final Holder exponents k=q(p0−1)/(p0−q)>q satisfy q(k−1)/(k−q)=p0, giving q<p0, never the endpoint q=p0.

Theorem 2.5 is a one-way coercivity-to-existence assertion citing the unchanged continuity method in DJL26 and its estimates. Theorem B then adds AJL23 Theorem 1, so the maximal-torus issue in existence-to-T_C-coercivity remains load-bearing and requires the original AJL statement. No independent full continuity proof is given here.

The weighted Kähler–Ricci soliton section uses Fano alpha=4pi c1(X), consistent with twice-standard Ricci. Its equation v(m_hat)hat omega^n=e^(−phi+h_omega)omega^n and Ric(hat)=hat+dd^c log v is internally consistent. Theorem 3.1 claims a forward pointwise trace estimate depending on bounded phi and fixed positive smooth v; its direct proof continues next. This source route need not inherit the inconsistent weighted Mabuchi derivative.


# Actual primary reading 11 — physical pages 21–22

Read full text and individually displayed sheet_11.png in order; pages 21–22 only.

The soliton maximum-principle proof controls H=log(reverse trace)−Aphi with A=B+1. At its maximum the Jxi derivative is replaced by A Jxi(phi), bounded through normalized moment differences. The reverse trace is bounded globally using oscillation(phi); determinant comparison then bounds the forward trace. Its reciprocal-trace remainder is controlled by the volume equation and bounded phi,h_omega and positive min(v), as in AM–GM, even though that intermediate lower bound is not repeated here. This smooth estimate is independent of weighted Mabuchi and maximality of T.

Proposition 3.2 adds maximal T and a finite-energy regularization argument imported from HL23 Proposition 3.8. The present proof does not independently supply that approximation. Remark 3.3's log-Fano-pair extension is expressly left to readers; do not mark its singular extension as fully checked or import it as a proved theorem. Section 4 assumes a smooth polarized Kähler manifold with alpha=2pi c1(L); its smooth equivariant test configurations include a compact Kähler total space and a trivialization away from zero. Distinguish these conventions from arbitrary normal algebraic test configurations.


# Actual primary reading 12 — physical pages 23–24

Read all text and individually displayed sheet_12.png in sequence; pages 23–24 only.

Reduced J^NA is the infimum over Lie-algebra twists; irrational twists are continuity extensions of J, not literal test configurations. The smooth dominating test-configuration scope is explicit. The source prints weighted DF as the integral involving Scal_v−w plus 8pi times the ordinary volume; do not import it without checking the primary weighted normalization. Rescaling v,w simultaneously should rescale the weighted invariant, whereas the printed constant does not visibly scale; this is a diagnostic, not a completed independent invariant calculation.

The Sasaki setup requires a smooth compact strictly pseudoconvex integrable CR manifold, a compact CR torus, and a regular positive chi generating a free circle action. Thus the quotient is a principal S^1 bundle over a smooth space. Contact sections are lifted uniquely to vector fields preserving D; positivity is defined through d eta_xi on the CR distribution. These restrictions rule out a blanket application to orbifold or nonregular reference quotients. No singular/log-Fano extension verified here.


# Actual primary reading 13 — physical pages 25–26

Read all text and individually displayed sheet_13.png in sequence; pages 25–26 only.

Section 4 resolves the introduction's quotient notation: X_chi=N/S^1_chi, with free reference action and principal-bundle connection eta_chi. Deforming eta by pi^*d^c phi gives the new horizontal CR structure. The commuting xi keeps its underlying Reeb vector field fixed. The positive affine ell_xi is normalized by eta_chi(xi^D)=pi^*(ell_xi composed m_chi).

Theorem 4.4 attributes the Sasaki/weighted-extremal reduction to AC21 Theorem 1 and ACL21 Proposition 1. Its weights are ell^(−n−1) and ell^(−n−3), where n is the complex dimension of the regular quotient. Algebraically log v=−(n+1)log ell has positive semidefinite Hessian; for nonconstant ell it has a positive direction, so no log-concavity. This algebraic motivation can be explained without independently certifying the full imported Sasaki equivalence. Corollary 4.7 depends on the previously flagged B/C, and is not cleared by this reading. Remark 4.6 claims equivalence of existence in a larger Sasaki polarization via AC/ACL results; no blanket identification of the two deformation spaces is asserted. The cone constructed from the dual polarized line bundle is smooth away from the zero section; do not conflate it with arbitrary singular affine cones.


# Actual primary reading 14 — physical pages 27–28

Read all text and individually displayed sheet_14.png in sequence; pages 27–28 only.

Comparison to Collins–Székelyhidi is explicitly placed in the vanishing-contact-Futaki, constant-transverse-scalar-curvature setting, and normal central fibers are an additional affine-test requirement. A weighted extremal statement cannot be silently converted to cone K-stability with no Futaki restriction. The GF comparison is imported from ACL21, not proved here.

The cKEM application uses maximal T and positive affine ell_f, with v_f=ell_f^(−2n+1), w_f=ell_f^(−2n−1). Corollary 4.8 asserts a uniform algebraic correspondence although Section 4.4 initially fixes only an arbitrary Kähler class; its use of Corollary C requires the extra polarization hypothesis. In addition, identifying constant conformal scalar curvature with a weighted extremal rather than the appropriately normalized weighted cscK equation requires checking the extremal affine/Futaki condition in the original source. Exclude this assertion from a checked book theorem at this stage. Merely knowing positivity/log-convexity of the displayed weights does not certify those implications.

References give published AJL23 in Geometry & Topology 27(8), 3229–3302, and ACL21 in Advances 391, 107969. The direct estimates remain distinct from the overview's unsettled variational and algebro-geometric conventions.


# Actual primary reading 15 — physical pages 29–30

Read complete text and individually displayed sheet_15.png in sequence. All 30 physical pages of the fixed v1 PDF have now actually been read as 15 individually displayed two-page images, with 15 sequential notes; the reference pages are reading credit, not proof certification of the cited works.

The source references DJL25 (JFA 289, 111148) and DJL26 (J. Reine Angew. Math. 832, 255–296), Han–Liu's published existence paper, Lahdili's weighted scalar-curvature/Mabuchi paper and Han–Li's weighted-soliton regularization. Those references supply identifiers only until acquired and read. BJ25 and Tru26 are separately dated source claims, not repairs of the BJ22 homogeneous Siu input. The paper is arXiv:2610.10216v1 submitted 7 October; its typeset closing date is 8 October. Cite the explicit arXiv version rather than inventing journal acceptance or revision.

Provisional integration scope: direct smooth PDE estimates Theorems 2.1, 2.3 and 3.1, with complete constant/normalization hypotheses and an independent prescribed-function letter h. Inspect controlling variational sources to document the observed transcription/hypothesis issues. Do not promote Theorem B/Corollary C or the Sasaki/cKEM/log-Fano equivalences as fully verified by the primary reading. These exclusions do not disprove the main analytic estimate. No original theorem, no Rethlas receipt and no change to canonical open statuses.


## Selected primary dependencies


# Actual dependency reading 01 — published AJL physical pages 2–3

Read full selected text and individually displayed dependency sheet_01.png. Exact published PDF SHA256 d22c49681931ebbd582cb2cda48a5a0178f9c07b782ae34d6ae10cdf2bc690bd. Physical 2 is printed 3229, title/DOI/publication date (9 November 2023), with the Creative Commons attribution license; physical 3 is printed 3230. Only these two pages credited.

The abstract explicitly states maximal complex torus, confirming that maximality is not an inference from a secondary source. Its weighted cscK equation is Scal_v=w, and scalar v is homogeneous linear in v. The momentum polytope is fixed by translation normalization. The geometry is smooth compact Kähler with a reduced Hamiltonian automorphism torus. No proof of the AJL theorem has been read in this selected scope yet; the checkpoint will use its exact hypotheses as a comparison, not recursively certify its full proof.


# Actual dependency reading 02 — published AJL physical pages 6 and 13

Read full text and individually displayed dependency sheet_02.png. Same exact published AJL PDF. Physical 6 is printed 3233; physical 13 is printed 3240. Only these two pages credited.

Theorem 1 explicitly assumes maximal T for coercivity modulo T_C. The immediately following paragraph replaces T_C by the connected centralizer for a nonmaximal torus. Thus the JP26 Theorem B omission is confirmed against its invoked original source, not merely a conjectured boundary objection. The ordinary PDE estimates do not require maximality.

The original weighted Donaldson–Futaki formula on physical 6 includes 8pi integral_X v(mu_omega)omega^[m], with divided powers omega^[m]=omega^m/m!. JP26 physical 23 instead prints 8pi Vol(X,alpha), where its earlier volume has no v. Those are not the same weighted normalization. Do not import the new printed DF formula. Page 13 fixes the same compatible moment-map change mu_phi=mu_0+d^c phi on torus generators and defines weighted cscK by Scal_v=w. These are definition/hypothesis comparisons; the full AJL existence-to-coercivity proof has not been reread.


# Actual dependency reading 03 — published AJL physical pages 14–15

Read full text and individually displayed dependency sheet_03.png; printed 3241–3242. Same fixed published PDF. Two pages credited.

Definition 1.1 gives dM(phi_dot)=integral (w−Scal_v)phi_dot omega^[m] without an extra v. Remark 1.2 gives precisely the unweighted scalar integral condition for invariance under constants; extremal weights incorporate it through the affine function. This confirms the mismatch of the extra v in JP26 physical 8 against the original variational definition. The difference is substantive even though a harmless overall volume/divided-power normalization can be adjusted.

Proposition 1.4 and Theorem 1.5 both name the connected centralizer. Only maximal T identifies it with T_C; the source often assumes maximality when solving the geometric problem. This does not retroactively make an arbitrary-torus statement in JP26 correct as printed. The Fano convention in AJL is alpha=2pi c1, different from JP's twice-standard Ricci alpha=4pi c1; avoid cross-source soliton factor mixing. These pages provide definition/hypothesis clearance, not a full proof reread.


# Actual dependency reading 04 — published AJL physical page 61

Read full selected text and individually displayed one-page dependency sheet_04.png, printed 3288. One page credited; AJL's selected scope totals seven pages in four images.

Remark 7.7 explicitly removes maximality only after replacing T_C by the larger connected reductive centralizer, reinforcing the exact-hypothesis comparison. The proof of Theorem 1 on this page invokes the coercivity principle, convexity, regularity, uniqueness and compactness established elsewhere; those earlier proofs are not wholly reread. The page contains the end of a separate minimizer proof and Remarks 7.6/7.7, which cannot be described as a complete recursive certification of the published theorem. The checked purpose is maximal-torus and weighted-normalization provenance.


# Actual dependency reading 05 — Lahdili v4 physical pages 1–2

Read full text and individually displayed dependency sheet_05.png. Exact arXiv:1808.07811v4 PDF SHA256 48e769d2e01bb748d4477df7b1b697b95464828c1c3663cf7221c08ef47abb56, revised 27 April 2019 (typeset date 30 April). Only pages 1–2 credited, not the published PLMS edition.

The older source defines weighted cscK by Scal_v=c_{v,w}(alpha)w and a weighted extremal equation by an additional affine factor. Its introduction places conformally Kähler Einstein–Maxwell metrics in the weighted cscK equation for ell^(−2m+1),ell^(−2m−1), not a generic weighted extremal equation. This supports the concern that JP26 Section 4.4 must control that affine factor; no blanket cKEM iff weighted extremal statement is accepted. This is a selected comparison, not a recursive proof check of the cKEM reduction. The moment-polytope and maximal-torus special cases are explicit; preprint/journal edition distinctions are preserved.


# Actual dependency reading 06 — Lahdili v4 physical pages 7 and 11

Read full text and individually displayed dependency sheet_06.png in sequence; two pages credited.

Lemma 2 records fixed weighted volume and integrated weighted scalar curvature under the normalized moment map. Its proof of volume invariance invokes an older theorem; do not describe that external theorem as reread. A simpler uniform upper mass bound for the JP twisted proof is sup(v) times the fixed ordinary cohomological volume, so no recursive Duistermaat–Heckman proof is needed for that estimate.

Definition 5, equation (14) on page 11, gives the Mabuchi variation with omega^[n] and no additional v factor, including c_{v,w}(alpha) in the prescribed scalar. This independently agrees with published AJL Definition 1.1 after choosing the normalized prescribed function. The weighted pairing in the preceding formal moment-map discussion is a different object and cannot justify multiplying the Mabuchi variation by v. No use of the zero-denominator slope convention in Definition 3 is made in the new book statement.


# Actual dependency reading 07 — Lahdili v4 physical pages 12 and 19

Read all selected text and individually displayed dependency sheet_07.png; two pages credited.

Page 12 continues variational foundations; the proof of Lemma 4 continues onto an unselected page, so it is not credited as a complete proof. That lemma is not a load-bearing new book import.

Definition 11 and Remark 6 on page 19 give both the base-form correction and its fiber-integral form: 8pi integral_X v(m_omega)omega^[n]. The trivial-test computation makes the necessity of the weighted correction explicit. This independently confirms the published AJL formula and disproves using the JP26 printed ordinary-volume term as the same invariant for general v. Source normalization includes divided powers. The test-configuration slope theorem and positivity proof further downstream are not reread or imported; only exact definition comparisons are cleared.


# Actual dependency reading 08 — Lahdili v4 physical page 20

Read all selected text and individually displayed one-page dependency sheet_08.png. One page credited; Lahdili's selected scope totals seven pages in four images. The combined checkpoint comprises the complete 30-page JP v1 and fourteen selected exact dependency pages, 44 distinct exact-source/page pairs in 23 matching images.

Theorem 7 on page 20 concerns a weighted smooth test-configuration slope under a reduced-central-fiber assumption, with its own time convention. Its proof and the following Lemma 9 continue outside this selected scope and are not certified here. The moment-map/potential construction of Lemma 8 is read through completion on this page, but older global-potential existence is an attributed input. No slope theorem from this paper is a new book import; the load-bearing comparison remains its Definition 5 on page 11 and weighted Futaki normalization on page 19.

Source decisions: keep JP's smooth PDE estimates with explicit positive lower v, bounded potentials/densities and source units. Exclude its printed extra-v Mabuchi derivative, unweighted-volume weighted-DF formula, arbitrary-torus T_C equivalence, and unqualified cKEM/log-Fano conclusions. Do not equate exclusions with a refutation of the directly checked analytic estimate. No independent-model receipt and no canonical problem promotion.

