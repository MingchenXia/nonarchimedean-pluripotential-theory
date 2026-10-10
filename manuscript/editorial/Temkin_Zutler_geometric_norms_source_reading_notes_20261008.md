# Actual sequential source reading notes, 8 October 2026

The primary-source notes precede the dependency notes. Each records a complete selected-text read and individual matching-image inspection. Later notes retain qualifications rather than rewriting earlier preparation flags.


---

Primary view 01

# Actual primary reading 01: Temkin–Zutler v1, physical pages 1–2

Complete selected text was read, followed by individual display and inspection of the matching image. The controlling arXiv:2608.19481v1 PDF has SHA256 769d96661b6f1227ee6e0535ad707c91ddbf958c985d2fabf800f99500413abd and was posted 19 August 2026. These introductory results are not yet proof clearance.

The paper distinguishes multiplicativity of a fixed seminorm, power multiplicativity/spectrality, and multiplicativity of its spectral seminorm. These are properties of actual seminorms and need not survive replacing the norm by an equivalent one. Geometric versions use the tensor seminorm after every real-valued extension of the ground field; completeness is deliberately not imposed throughout. Seminorm kernels and spectralization kernels must not be conflated with ordinary nilradicals: quasi-nilpotence is an analytic spectral condition.

The statement that the spectral seminorm is the minimal power-multiplicative seminorm dominated by the given seminorm has its extremal direction reversed. If beta is power-multiplicative and beta<=alpha, then beta(a)=beta(a^m)^(1/m)<=alpha(a^m)^(1/m) and hence beta(a)<=rho_alpha(a); rho is the greatest such seminorm, subject to the usual spectral seminorm assumptions. This is a direct convention calculation, not a counterexample to a later theorem. The graded reduced/integral tests, unique maximal spectral point and equal-characteristic p-root test are still only introduction claims. The Berkovich/Poineau peaked or universal point references require exact source inspection before a load-bearing import.

---

Primary view 02

# Actual primary reading 02: Temkin–Zutler v1, physical pages 3–4

Complete selected text and the individually displayed matching image were read. All tensor products use the non-Archimedean projective tensor seminorm, before any completion. The source's spectral isomorphism includes the completed residue fields, not just a homeomorphism. Spectralization quotients by the spectral kernel without completion. The claimed geometric spectral multiplicativity criterion uses the completed ground field inside the completed fraction field of the spectralization, and must retain that precise category.

Lemma 2.2.1's tensor spectralization equality can be explained via the greatest dominated power-multiplicative seminorm: restrictions of a multiplicative spectral point to B and C factor through their spectralizations, giving both directions. Its single maximal point is defined as a point dominating every other point, rather than merely a unique order-theoretic maximal element. For nonemptiness of a seminormed object, keep the usual nonzero separated completion and unital normalization; a nonzero underlying ring with an identically zero seminorm cannot be used blindly. Berkovich's existence and spectral-radius locators are imported inputs, not newly inspected foundation proofs.

Corollary 2.2.2 reduces to the valued fraction field only after spectral multiplicativity, tensor-isometry and division by nonzero elements; the latter isometry points to Lemma 3.4.1 still unread. The paper's defectless condition for a chosen real-valued finite extension is [l:k]=e f, which implies that extension is unibranch. This differs from the sum-over-all-valuations convention for abstract finite extensions. Equal- and mixed-characteristic tests are still introduction claims pending the later proofs.

---

Primary view 03

# Actual primary reading 03: Temkin–Zutler v1, physical pages 5–6

Complete selected text and the individually displayed matching image were read. For a finite defectless chosen extension, an orthogonal basis preserves the tensor norm and identifies the graded tensor product exactly. Geometric spectrality/multiplicativity can then be tested by graded reducedness/integrality; finite dimensionality over the graded field turns the integral graded algebra into a graded field. This exact-basis argument is not licensed for extensions with defect.

The almost-orthogonal discussion separates dense value groups from discrete ones and uses the category of nonexpansive maps. Unit-ball cokernels almost vanish after multiplying by every positive topologically nilpotent scalar, but need not vanish exactly. Dense value groups permit rescaling two tensor factors to strict unit-ball representatives; infima of tensor presentation sizes may be unattained. The non-spherically-complete example begins on page 6 and is not yet read.

Lemma 3.1.1's literal condition (iv), injectivity of the completion map V->V-hat for a normed space, requires clarification: ordinary separated metric completion is always injective, even when extension of scalars to k-hat loses dimension. A two-dimensional k-subspace k+k alpha inside k-hat, with alpha outside k, is a candidate diagnostic of that wording. The intended injectivity of V tensor k-hat -> V-hat would instead detect dimension preservation. Do not import the printed completion-map criterion before resolving this distinction. Conditions involving approximate bases, equivalence to an orthogonal norm and preserved completed dimension must retain their actual hypotheses rather than silently assuming completeness of k.

---

Primary view 04

# Actual primary reading 04: Temkin–Zutler v1, physical pages 7–8

Complete selected text and the individually displayed matching image were read. The type-IV discussion uses an algebraically closed complete field that is not spherically complete, a decreasing sequence of balls with positive limiting radius and empty field intersection, and the associated immediate completed residue field. The tensor difference t tensor 1 - 1 tensor t can have norm equal to the limiting radius even though no strict unit-ball tensor presentation attains it. The asserted identification of the completed tensor with the limiting disc uses more than the displayed upper estimate; it must retain the peaked-point/base-change input, not be treated as proved solely by |t'|<=r_i. No recursive proof of that example's identification is claimed here.

Base-change isometry is justified in the dense value case by torsion-free valuation-ring modules and almost unit-ball comparison. The discrete descent uses a Gauss extension, while the printed descent lemma assumes weak cartesianity; retain complete ground fields or verify applicability before using that shortcut for arbitrary incomplete spaces. Lemma 3.5.1 extends r-orthogonality via tensor isometry and controlled unit-ball torsion. The diagram has obvious repeated U_l symbols where U should occur; avoid copying the typographical map labels.

Corollary 3.5.2 detects loss of multiplicativity when an algebraic element becomes closer to K than to k. Its orthogonality threshold is d(alpha,k)/|alpha|. The proof's chosen radius between the two unnormalized distances should be divided by |alpha| before using it as an r-orthogonality parameter; the direct normalized inequality supplies the intended argument. In the field case, henselianity fixes the extended valuation, whereas a nonfield finite tensor already has zero divisors and a nondegenerate tensor norm cannot be multiplicative. This is not a claimed counterexample to the corollary's statement.

---

Primary view 05

# Actual primary reading 05: Temkin–Zutler v1, physical pages 9–10

Complete selected text and the individually displayed matching image were read. Lemma 3.6.1 identifies the tensor norm with a chosen field valuation when arbitrarily close to orthogonal bases from l remain such over K. The proof compares the actual presentation maximum to that valuation and contradicts any strict norm loss. The degree-p distance criterion imports Gabber–Ramero Proposition 6.3.13 beyond its stated tamely closed scope; that extension is a separate proof obligation, not cleared by reading the abbreviated claim.

Example 3.6.3(a)'s equivalence between K tensor l being a field and the chosen alpha not lying in K needs a Galois or linear-disjointness justification absent from its printed non-Galois degree-p signature. A candidate concrete test is k=Q_3, l=k(alpha) with alpha^3=3 and K=k(alpha') for a different conjugate alpha'=zeta_3 alpha. The chosen alpha is not in K while the polynomial already has root alpha' in K, so its tensor is not a field. This is a prospective direct diagnostic requiring a complete field/valuation check; it does not refute the later separable-closure criterion. The distances to a chosen embedded alpha must not be used as a substitute for irreducibility over K.

Almost-split one-variable valued extensions are infima of translated Gauss valuations. The Gauss power-multiplicativity proof selects the smallest degree attaining the weighted maximum; every other term of the n-fold coefficient at that degree contains an index below it and has smaller norm, leaving the dominant coefficient. Generalizing from Gauss norms to their limit still needs the tensor-seminorm limit justification. Remark 4.1.2 expressly permits a nonzero tensor kernel when the element already lies in the completion of the base. This reinforces the distinction between algebraic tensor injectivity, separated completion and a nondegenerate tensor norm.

---

Primary view 06

# Actual primary reading 06: Temkin–Zutler v1, physical pages 11–12

Complete selected text and the individually displayed matching image were read. The finite-base-change spectral criterion correctly compares the reduced completed tensor product to a field. Passing to henselizations or completions matters because a raw algebraic tensor may have several factors while its tensor seminorm annihilates a branch. The relative separable-closure condition in Theorem 4.3.1 is universal in all valued extensions, not a field test for one arbitrarily fixed extension.

Lemma 4.2.1(iv)'s asserted finite-extension equivalence requires a linear-disjointness check: absence of an embedded proper separable subfield of l in K need not prevent a non-Galois minimal polynomial from splitting into factors of degrees 2 and 3 over K. A generic S5 extension, with l the index-five fixed field of a point stabilizer and K the index-ten fixed field of a 2+3 partition stabilizer, is a candidate exact test; adjoining a Laurent parameter gives complete henselian valued fields. This remains a prospective diagnostic until the group action, embeddings and tensor decomposition are checked. It does not directly refute the universal relative-separable-closure theorem. Remark 4.2.2(i) also needs the existential/universal quantifier over l; the printed statement cannot be independent of l for one fixed extension.

Theorem 4.3.1 uses reduction to the spectralized fraction field, finite algebraic base change, almost-split transcendental base change, filtered colimits and Lemma 4.3.2. The latter's attained-radius case imports the stability theorem from Temkin 2010, Corollary 6.3.6. Its displayed graded reduction k_gr[t] for the valued rational function field needs the appropriate homogeneous fraction/localization interpretation, not a polynomial ring with noninvertible leading forms. The type-IV case asserts convergence of conjugate distances and selected extended valuations before applying Krasner; those valuation-selection and convergence details are not proved here. The alternative uniformization theorem is named but not read. The main criterion is not yet cleared as a book input by this scoped audit.

---

Primary view 07

# Actual primary reading 07: Temkin–Zutler v1, physical pages 13–14

Complete selected text and the individually displayed matching image were read. Residual exponential characteristic p equals 1 in residue characteristic zero. A p-regular element has |pa| below its distance from p-th powers; weak versality decreases each positive distance, whereas p-versality requires one uniform contraction factor. Thick graded reductions keep the mixed-characteristic Frobenius error. Equal-characteristic k^(1/p) supplies actual roots, while general p-versal extensions need not be algebraic.

The key lemma raises almost-orthogonal vectors to p-th powers by choosing approximate coefficient roots, using spectrality and controlling multinomial errors by |p| times the presentation maximum. Its printed proof chooses strictly better roots from a non-strict thickness bound at s^p; that strict error margin is not automatic. For a safe application retain an actual thickness r<s^p, which is what the main theorem's threshold can provide. Non-p-regular coefficients also admit the needed approximation because their distance is at most |p| times their norm, and choose s^p>|p|. The main theorem's displayed threshold should therefore explicitly include |p| alongside gamma and r. The final strict inequality should compare with gamma||x||^p, and the iterated p-power identity has a typographical exponent omission. These convention repairs are not a disproof of geometric spectrality.

The key lemma assumes complete k whereas Theorem 5.3.1 allows incomplete k, so a completion reduction preserving norms and versality must be supplied or the account restricted to complete fields. Likewise Corollary 5.3.2 omits weak cartesianity: over a complete field finite-dimensional normed subspaces have approximate orthogonal bases, but for an incomplete field that assertion is not automatic. The perfectoid claim and residual-characteristic-zero claim remain attributed source statements pending that reduction and the final criterion; no broader arbitrary-incomplete-field theorem is promoted from the abbreviated proof alone.

---

Primary view 08

# Actual primary reading 08: Temkin–Zutler v1, physical page 15

Complete selected text and the individually displayed matching final-page image were read. All fifteen source pages are now covered in eight matching views. Acquisition and preparation remain zero-credit historical artifacts; this full reading is not a recursive foundation audit.

The combined geometric multiplicativity criterion keeps weak cartesianity, the actual multiplicative norm, one p-versal extension on which the tensor seminorm is spectral, and relative separable closure in the henselized fraction field. Henselizations and completions are alternatives only with the preceding category checks. The conclusion over an algebraically closed base imports the established earlier cases rather than eliminating proof obligations by the abstract alone.

Remark 5.3.3 explicitly leaves open how, or whether, the uniform p-versality condition can be weakened for infinite p-rank. Weak p-versality is necessary by the single p-root test and is equivalent to uniform p-versality only in the stated finite-rank situation. This is a possible related research direction, not a solved book problem. The bibliography identifies Berkovich 1990, Gabber–Ramero 2003, Poineau 2013, Temkin 2004 and Temkin 2010; none is credited as recursively read here. Main broad criteria remain subject to the incomplete-field reduction, finite non-Galois tensor test, strict thickness margin and type-IV stability/valuation-convergence qualifications in the previous notes. The finite counterexamples proposed there still require complete checks. No book insertion, original theorem promotion, canonical inventory change or independent model receipt is claimed.

---

Dependency view 01

# Actual dependency reading 01: Poineau published PDF, physical pages 1–2

The complete selected text and individually displayed matching image were read. The file is the published 2013 Bulletin SMF 141(2), 267–297 edition, SHA256 c1d3aea9ca8b8c492c6e7f8291300c54d9187d3365a55de593f60814b2d48db8. Physical page 1 is the journal wrapper; physical page 2 begins printed page 267. Received 27 April 2011 and accepted 20 February 2012 are printed dates, distinct from publication or arXiv revision dates.

The abstract asserts sequential closure and sequential compactness properties, descent of disc points to countable-type subfields, and universality over an algebraically closed field. Canonical lifting in a scalar extension is not uniqueness of the entire fiber. These are introductory claims only; the norm, type-IV and scalar-extension proofs have not yet been read. Only these two physical pages and one image are credited.

---

Dependency view 02

# Actual dependency reading 02: Poineau published PDF, physical pages 3–4

Complete selected text and the individually displayed matching image were read. Printed pages 268–269 introduce Fréchet–Urysohn closure and sequential compactness, and reserve full angelicity for additional hypotheses satisfied by curves and analytifications of algebraic varieties. Do not infer these properties for arbitrary valuation/Riemann–Zariski spaces or arbitrary compact Hausdorff spaces from this introduction.

The universality mechanism is a canonical scalar-extension lift, built from a single Shilov point and limits of disc boundaries; it does not make every scalar-extension fiber a singleton. Non-strict affinoid spaces require graded reductions, motivating the following graded commutative-algebra section. Descent to a countable-type complete subfield supplies metrizability before canonical lifting back. These are descriptions of the proof plan; the graded and tensor arguments are still unread.

---

Dependency view 03

# Actual dependency reading 03: Poineau published PDF, physical pages 5–6

Complete selected text and the individually displayed matching image were read. Outside the purely graded section, k is explicitly complete and may be trivially valued. A k-free polyradius means rational independence modulo the divisible hull of |k^times|, and the associated completed Laurent Gauss extension has a unique dominant weighted monomial. The completed tensor with a Banach algebra is the corresponding convergent Laurent-series space with its weighted maximum norm. This supplies a concrete scalar-extension category distinct from the incomplete seminormed category of Temkin–Zutler.

Graded integrality tests nonzero homogeneous products; a graded field only inverts all nonzero homogeneous elements, and graded fraction fields are homogeneous localizations. The finite-module definition should permit degree shifts of free generators when used in general. The final illustrative assertion about homogeneous polynomials requires infinite order of the new degree modulo the old degree group (or the earlier rational independence), rather than only g outside rho(k): if g^m is already an old degree, distinct monomials can have the same degree. Keep the precise independent-radius condition in any account. Only the start of the graded algebra proof is covered here; its scalar-extension theorem remains unread.

---

Dependency view 04

# Actual dependency reading 04: Poineau published PDF, physical pages 7–8

Complete selected text and the individually displayed matching image were read. The non-strict affinoid graded reduction here is formed with the spectral seminorm, unlike the actual-seminorm graded test used to detect power multiplicativity in Temkin–Zutler. The distinction matters when tensor norms have not been shown spectral. The Laurent description of a one-variable homogeneous fraction field retains the independent-degree qualification from note 03.

Homogeneous Euclidean division and principal homogeneous ideals are ordinary graded algebra inputs; their proofs are explicitly omitted in the source. Algebraic closedness of the graded reduction of a complete algebraically closed field is proved by lifting a nonconstant homogeneous polynomial: a nonzero root has two equal maximal terms, forcing its absolute value to equal the prescribed radius. Coefficient equalities apply to nonzero coefficients only; zero coefficients create no extra requirement. The graded Artin–Tate theorem begins here; its proof follows on the next pages. No scalar-extension tensor norm or universal-point conclusion is yet cleared.

---

Dependency view 05

# Actual dependency reading 05: Poineau published PDF, physical pages 9–10

Complete selected text and the individually displayed matching image were read. The graded Artin–Tate argument needs its usual module formulation: the expansion coefficients gamma_ij belong to B, not necessarily A, and the finitely generated intermediate B0 makes C a finite B0-module, not merely a finite B0-algebra. Include 1 among the chosen module generators; closure of their B0-span under multiplication and containment of algebra generators then gives the module bound. Noetherianity makes B a finite submodule. These are precise repairs of the abbreviated printed wording.

The independent-degree condition is now explicitly defined by a free family in the quotient degree group. It supplies the Laurent presentation and the graded finite-type fraction-field test. In the converse localization argument, Q=product P_i^d-alpha is coprime to every inverted P_i; it cannot become a unit after localization. One need not assert the stronger printed divisibility phrasing. The Kummer factorization of a homogeneous algebraic element separates an algebraic base factor from a monomial root. The graded Nullstellensatz uses a maximal homogeneous algebraically independent family in K (the printed k there is a typo), then Artin–Tate and the finite-type test. These arguments remain in homogeneous graded algebra; they do not assert ordinary ungraded finite-degree finiteness for a Laurent field.

---

Dependency view 06

# Actual dependency reading 06: Poineau published PDF, physical pages 11–12

Complete selected text and the individually displayed matching image were read. Lemma 2.13 reduces independent-degree scalar extension to a Laurent polynomial ring, whose homogeneous leading coefficients establish graded integrality. Theorem 2.14 descends a hypothetical homogeneous zero-divisor relation over an extension through a finite-type coefficient algebra and the graded Nullstellensatz. Its witness algebra must invert P(x) and Q(y), rather than the printed P(x) and P(y); specialization also applies to the coordinates of x and y. With those explicit corrections, the nonzero witnesses survive specialization and contradict Lemma 2.13. The point tuples have the number of polynomial variables, not necessarily the number of ideal generators. One can form the finite witness algebra inside the chosen common graded extension, avoiding an unnecessary claim about its displayed ambient field.

The tensor convention is the infimum over finite presentations of the maximum of products of norms. Completion means separated completion; for modules alone the result is a Banach module, rather than automatically an algebra. Lemma 3.1 states preservation of isometric embeddings by this tensor seminorm and its separated completion. Its proof starts on the next physical page and is not yet credited here. Remark 2.12 distinguishes valued fields from affinoid algebras that happen to be abstract fields with a nonmultiplicative norm; it does not identify those two categories.

---

Dependency view 07

# Actual dependency reading 07: Poineau published PDF, physical pages 13–14

Complete selected text and the individually displayed matching image were read. Lemma 3.1 uses a finite-dimensional subspace containing both an initial presentation and a near-optimal tensor presentation. An arbitrarily close Cartesian basis adapted to its subspace gives a bounded projection and hence ||f||_A <= alpha(||f||_B+epsilon); alpha decreases to 1 and epsilon to 0. The printed dimensions must satisfy s <= r, not s >= r, and the first maximum in the estimate runs over the d presentation terms, not the r basis elements. The argument assumes the article's complete base field convention and imports BGR Proposition 2.6.2/3 for adapted approximately Cartesian bases. That reference has not been separately read in this dependency batch. It does not justify an identical assertion over an arbitrary incomplete base. The trivial valuation reduction uses a free radius and its explicit Laurent Gauss extension.

Definition 3.2 concerns the actual completed tensor norm being multiplicative for every complete valued extension. This is stronger than merely asking that its spectralization be multiplicative. A universal point gives a canonical lifted point from the norm on H(x) completed-tensored with K. Neither that construction nor transitivity asserts that the entire fiber has only one point. Definition 3.4 counts a dense vector subspace, not a dense countable set. Lemma 3.6 announces continuity of completed tensor norms as the point varies; its proof remains on the next page.

---

Dependency view 08

# Actual dependency reading 08: Poineau published PDF, physical pages 15–16

Complete selected text and the individually displayed matching image were read. Lemma 3.6 reduces any completed tensor element to a countable-type closed subspace, uses Berkovich Lemma 5.2.6 for continuity there, and uses Lemma 3.1 to preserve its norm in the original space. The Berkovich lemma is an explicitly imported, not recursively read, input. Corollary 3.7 supplies continuity of the canonical lift for the actual multiplicative tensor norm. Remark 3.8 expressly separates this from spectral multiplicativity and gives a strictly purely inseparable residue-field extension: a canonical lift alone does not make a point universal, since its self-tensor has nonzero nilpotents.

Proposition 3.9 requires stability of the complete base, the precise spectral-value intersection condition, and geometrically integral graded reduction. It passes to a free polyradius and a distinguished strict affinoid algebra. Besides Temkin stability, it imports BGR and Berkovich results and expressly invokes Ducros's correction of the proof of Berkovich Lemma 5.2.2. These inputs are not silently treated as read. Corollary 3.11 isolates a Shilov component by a reduction-localizing affinoid domain and applies this criterion over an algebraically closed base and Theorem 2.14. It says every Shilov point is universal, not that the Shilov boundary or each extension fiber is a singleton. Proposition 3.12's closedness proof is on the next page.

---

Dependency view 09

# Actual dependency reading 09: Poineau published PDF, physical pages 17–18

Complete selected text and the individually displayed matching image were read. Proposition 3.12 passes multiplicativity to a limit of universal points using Lemma 3.6 for tensors of affinoid elements, then clears denominators in the residue fraction field and uses Lemma 3.1 and density to reach H(x). This is a net argument; no unproved first-countability is assumed. Corollary 3.14 combines closedness with Shilov points in arbitrarily small affinoid domains to obtain universality of every point over an algebraically closed complete base, including the trivially valued case treated through graded reduction.

Corollary 3.16 tests actual tensor-norm multiplicativity after extension to the completed algebraic closure. The proof uses the unique Shilov point of that fiber, its isometric evaluation into the completed residue field, universality over the algebraically closed base, and isometry under a further common extension. Its explicit phrase is a unique point in the Shilov boundary, not a unique point in the fiber. Choice of an isometric embedding of the completed algebraic closure into the algebraically closed further field uses completeness and the extension of the base valuation. Section 4 defines Abhyankar points by equality in the dimension inequality; the exclusion in Remark 4.3 concerns proper analytic closed subsets of an irreducible space.

---

Dependency view 10

# Actual dependency reading 10: Poineau published PDF, physical pages 19–20

Complete selected text and the individually displayed matching image were read. Lemma 4.4 isolates a generic reduction component in a strict affinoid domain and injects its function field into the residue field of H(x), obtaining the residue transcendence degree by the Abhyankar inequality. Lemma 4.6 gives an explicit Laurent Gauss lift after a free-radius extension: if the radius already lies in the divisible hull of the point's value group, a value-group rank becomes a residue transcendence degree; otherwise both relative invariants remain unchanged. It again identifies a unique Shilov point in the fiber. Proposition 4.7 preserves the sum under successive free-radius extensions and proves that Shilov points are Abhyankar; Corollary 4.8 uses affinoid neighborhoods for density.

Lemma 4.10 describes the Shilov boundary of a monic polynomial sublevel domain over an equidimensional affinoid base. Its proof passes to strict affinoids, uses the finite polynomial map to a disc over the base, finiteness of the reduction map, equidimensionality and the generic-reduction characterization. The fiberwise union is asserted only under those hypotheses. BGR and Berkovich finiteness/reduction inputs are citations, not newly completed source reads in this batch.

---

Dependency view 11

# Actual dependency reading 11: Poineau published PDF, physical pages 21–22

Complete selected text and the individually displayed matching image were read. Lemma 4.11 is the monic finite-polynomial zero-locus analogue of the preceding Shilov-boundary formula. Lemma 4.12 isolates a type 2 or 3 disc point using a polynomial whose rigid zero lies in a branch away from the outer Gauss point; polynomial norms increase along the path from their zero and are constant off it.

Proposition 4.13 descends an Abhyankar polydisc point by induction, splitting the equality of residue and value invariants between the projected point and its one-dimensional fiber. Its coefficient approximation in H(y) clears a common polynomial denominator q, giving a polynomial Q with leading coefficient q. The printed application of Lemma 4.10 then needs attention: that lemma requires a monic polynomial, while q(y) != 0 alone does not state that q is a unit on W. No independent proof that this domain has no additional boundary component has been supplied here. This is a qualification of the displayed proof step, not a counterexample to Proposition 4.13. The full Weierstrass conclusion is not used as a newly verified foundation for the proposed Chapter 4 norm explanation. Corollary 4.15 starts a finite Noether-normalization and reduction-component isolation argument; its proof continues on the next page.

---

Dependency view 12

# Actual dependency reading 12: Poineau published PDF, physical pages 23–24

Complete selected text and the individually displayed matching image were read. Corollary 4.15 finishes by density of the original algebra in its Weierstrass domain and localization at a reduction separator. Corollaries 4.16 and 4.18 extend the boundary-isolation construction through free-radius strictification and removal of other irreducible components, respectively. The discussion relates finite function values to determination of divisorial valuations, with the de Fernex–Ein–Ishii result explicitly cited rather than reproved. In Remark 4.20, the maximum is the norm of each f_i, not an unindexed f.

Corollary 4.21 uses the domain constructed in Proposition 4.13 and its finitely many defining coefficients to obtain a descended point which dominates its entire fiber on all polynomials. The conclusion is uniqueness in that fiber's Shilov boundary. A finite-type subfield in these analytic statements is understood with its induced valuation and completion as appropriate; it need not itself be complete. The qualification on the displayed Proposition 4.13 proof in note 11 continues to apply to conclusions depending on it. Theorem 4.22 announces the corresponding countable-type descent for arbitrary polydisc points; its proof starts on the next page.

---

Dependency view 13

# Actual dependency reading 13: Poineau published PDF, physical pages 25–26

Complete selected text and the individually displayed matching image were read. Theorem 4.22 inducts on the non-Abhyankar defect in dimension. In its last coordinate it uses decreasing polynomial sublevel domains with one Shilov point tending to x, puts their countably many coefficients in a countable-type field, and uses a dominating universal lift to bound all polynomials by their values at x. The concluding domination identifies that lift with x. The displayed proof replaces the relative algebraic closure of a subfield inside k by an algebraically closed subfield; for a general non-algebraically-closed k this requires a further reduction/descent argument not stated at that step. The global notation assumes only completeness of k. The proof as printed is therefore read with this qualification as well as the coefficient-clearing issue in note 11; neither observation is a counterexample to its statement. This dependency batch does not newly clear its full general signature.

Section 5 defines the Frechet–Urysohn property by sequential realization of every closure point. Proposition 5.2 explicitly assumes an algebraically closed complete base and constructs a tower of countable-type algebraically closed subfields with neighborhood bases and approximating points. Its tower and limit argument continue on the next page. No conclusion about all valuation spaces follows from the polydisc statement.

---

Dependency view 14

# Actual dependency reading 14: Poineau published PDF, physical pages 27–28

Complete selected text and the individually displayed matching image were read. Proposition 5.2 diagonally refines neighborhood bases over an increasing tower and passes to its completed union. A neighborhood of the limiting point contains the inverse image of a finite-stage neighborhood by approximation of finitely many polynomial coefficients; the printed equality with an arbitrary neighborhood U is stronger than needed. The basis inclusion suffices for convergence. Continuity of universal lifts then takes the projected sequence back to the original points. The constructed projected y_n need not be rational in the usual rigid-point sense: the proof uses their canonical-lift property from Theorem 4.22, and does not need the printed condition iv interpreted as rigidity.

Theorem 5.3 reduces to an algebraically closed complete extension by the proper, surjective scalar-extension projection, then to a finite affinoid neighborhood and a closed polydisc embedding. The qualification on the earlier descending-domain input is retained; no new general theorem verification is claimed here. Corollary 5.5 derives openness and closedness from sequential criteria through the Frechet–Urysohn property. This is about Berkovich analytic spaces in the source's convention and is not a claim of first countability or metrizability.

---

Dependency view 15

# Actual dependency reading 15: Poineau published PDF, physical pages 29–30

Complete selected text and the individually displayed matching image were read. Corollaries 5.6–5.9 combine the Frechet–Urysohn property with density to produce sequences of Abhyankar points and, for a nontrivially valued strict affinoid base, points with prescribed residue and value invariants subject to s+t <= the minimum component dimension and t <= the available value-rank bound. Finite normalization preserves the two invariants. Compact subsets are sequentially compact; this does not make arbitrary subsets compact or the ambient space metrizable.

Definition 5.10 requires both relative compactness of relatively countably compact subsets and sequential realization of their closure points. Proposition 5.11 uses Hausdorffness to make a convergent sequence's cluster point unique and deduces closedness of countably compact subsets. Corollary 5.13 additionally uses paracompactness, local compactness and local connectedness to reduce to finitely many connected components and a nested compact exhaustion; its proof continues on the next page. The topology assertions inherit their stated hypotheses and the earlier source inputs; no topology result is newly inserted in the manuscript by this reading.

---

Dependency view 16

# Actual dependency reading 16: Poineau published PDF, physical pages 31–32

Complete selected text and the individually displayed matching image were read. The compact exhaustion finishes Corollary 5.13, and Theorem 5.14 combines it with the sequential closure criterion to give angelicity of every subspace of a paracompact analytic space. Remark 5.15 identifies Hausdorff analytic curves and analytifications of algebraic varieties as common cases of paracompactness. It does not remove that hypothesis from the stated theorem.

The complete bibliography on these pages identifies the norm inputs as Berkovich 1990 and BGR 1984; the corrected strict-universality argument cites Ducros 2009, Lemma 1.8. Its two Temkin references are the 2004 graded local-properties paper and the 2010 stable-modification paper. Reading these bibliographic entries is not reading those sources. The published article ends at printed page 297 (physical page 32); the remaining physical page of the downloaded PDF must still be displayed before full-file coverage is recorded.

---

Dependency view 17

# Actual dependency reading 17: Poineau published PDF, physical page 33

The complete selected text consists only of the preparation's page label. The individually displayed matching image confirms that this final physical PDF page is blank. The downloaded 33-page file has now been read and displayed in full: one opening metadata wrapper, 31 printed article pages 267–297, and this blank closing page. This completes file coverage, not automatic verification of every imported dependency or every theorem signature; the qualifications recorded in notes 01–16 remain controlling.

---

Dependency view 18

# Actual dependency reading 18: Temkin 0707.3953v3, physical pages 36–37

Complete selected text and the individually displayed matching image were read. This is a selected reading of the 2010 arXiv v3, not of the differently paginated published PDF. Physical page 36 first finishes the preceding stable-modification argument; its earlier proof inputs are outside this selected reading. Section 6 works with analytic (complete non-Archimedean) fields. Stability is the absence of defect in every finite extension: e*f equals the field degree. A nonstable field need not itself have a finite immediate extension; such an extension of degree p can appear after a finite extension.

Proposition 6.1.1 seeks a degree-p approximate equation for an immediate extension whose distance infimum is not attained and is strictly larger than |p*b|. Its proof follows on later pages. The critical-coset construction thickens pth-power-minus-linear expressions by errors strictly below s. In mixed characteristic the addition check uses |p|*|c_i|^p < s, as required by the defining condition; the printed |p*c_i|^p bound is not a replacement for it. Lemma 6.1.2 starts with a Hensel argument: an improvement with the linear term as large as the constant would give a nearby root and split the coset, contradicting criticality. Non-discreteness and completeness are explicit hypotheses. The remaining parts of the lemma are on the next page.

---

Dependency view 19

# Actual dependency reading 19: Temkin 0707.3953v3, physical pages 38–39

Complete selected text and the individually displayed matching image were read. Lemma 6.1.2 compares unrestricted and restricted distance infima using the preceding Hensel improvement claim and the bound on the linear coefficient. In reading its converse, that coefficient bound must be established under the positive-infimum hypothesis as well; it is not permissible to assume criticality before it has been proved. This is an explicit logical dependency to retain in any explanatory reproduction.

Proposition 6.1.4 separates degree-p wild extensions into immediate defect, value-group ramification and purely inseparable residue ramification. A critical coset that splits after extension encodes which of the three occurs; whether its positive infimum is attained matters. A prime-to-p root extension of the linear coefficient normalizes the nonzero-linear immediate case. Its proof first handles a Cartesian extension by an orthogonal element. For an inseparable immediate extension, completeness ensures a strictly positive, unattained distance to a pth root. The separable immediate argument introduces a polynomial sublevel domain built from conjugate discs and continues on the next page. The remark relating a subcase to almost etaleness, differentials and the different is an aside explicitly not used in the subsequent proof; its assertions are not independently cleared here. The symbol d in the degree relation is the defect of L/K, regardless of the printed lower-case k subscript.

---

Dependency view 20

# Actual dependency reading 20: Temkin 0707.3953v3, physical pages 40–41

Complete selected text and the individually displayed matching image were read. The immediate degree-p proof controls every nonzero higher derivative on a sufficiently small split disc around the nonsplit limiting disc. Translation fixes coefficient absolute values; terms above degree one can be removed with an error strictly below r^p, and |p|*r_0^p is also made strictly below r^p. A root of the remaining polynomial lies in the limiting disc. The conjugate-distance step can be made explicit: radius-r clusters of roots form blocks of equal size under the transitive Galois action; prime degree allows only singleton or total clusters. Krasner excludes singleton clusters because base elements approach the distance infimum r. Hence all conjugates are within r and |g(c)|=|c-beta|^p for c in K. This supplies an additional justification beyond quoting Krasner alone. Completeness, primeness and the chosen unique extension of the valuation remain essential.

Corollary 6.1.6 tests stability through attainment of minima in special cosets after finite Cartesian extensions. Its converse uses a sufficiently large tame extension to resolve a finite extension into degree-p steps and locates its first defective step. Section 6.2 defines one-dimensional analytic fields as finite over a completed rational function field generated by a topologically transcendental element. Residue transcendence plus rational value rank is at most one; types 2, 3 and 4 are separated accordingly and preserved by finite extension. The definition of k-split begins at the end of the selected page and continues on the next page.

---

Dependency view 21

# Actual dependency reading 21: Temkin 0707.3953v3, physical pages 42–43

Complete selected text and the individually displayed matching image were read. Assumption 6.2.1 requires either an algebraically closed analytic base or a type-4, k-split situation over a tamely closed deeply ramified base (with the stated residue-characteristic-zero alternative). The deep-ramification equation is k^circ = p*k^circ + (k^circ)^p. It supplies a perfect residue field and p-divisible value group, in addition to tame closedness. A type-4 split point is approached by split discs with centers in k; nonsplit discs would contradict equality of distances to k and its algebraic closure.

Proposition 6.2.5 builds an orthogonal Schauder basis in Frobenius strings, retaining orthogonality of the initial string span to pth powers. Type 3 is the explicit Laurent monomial basis after a tame root extension. Type 2 reduces to Lemma 6.2.6 about a finitely generated regular extension of a perfect residue field. That lemma deliberately avoids arbitrary lifts of a basis modulo pth powers: they need not span. It instead uses an integer-valued pole-order filtration on a proper normal model, with kernel the constant field, and lifts a basis compatibly with quotient norms. Its indexing must consistently use balls of radius at most n for lifts of norm n (or shift the printed strictly-less-than-n indexing). The iteration and the analytic lift continue on the next page.

---

Dependency view 22

# Actual dependency reading 22: Temkin 0707.3953v3, physical pages 44–45

Complete selected text and the individually displayed matching image were read. The residue-field basis iteration terminates because nonconstant p^i-th powers have pole order at least p^i. The analytic type-2 lift is made through a discretely valued coefficient subfield and its unramified extension; arbitrary residue lifts over the original nondiscrete field are expressly insufficient. BGR basis results and the henselian lifting theorem are imported inputs. The displayed Frobenius strings include the zeroth power U as in the proposition, despite one intervening sentence's n>=1 wording.

For a split type-4 topologically generated field K=closure(k(z)), decreasing discs give dense polynomial approximation but the powers of an individual translated generator do not form a Schauder basis. Lemma 6.2.7 bounds the leading coefficient using distance to the algebraic closure, strictly when that positive distance is not attained. Page 45 identifies K completed-tensored with a complete field l containing K with l{r^-1*w}, w=z tensor 1 minus 1 tensor phi(z). To reproduce the norm equality one needs both bounds: translated polynomial presentations give the limiting Gauss-norm upper bound; the contractive map z -> phi(z)+w gives the lower bound. Rational denominators over k have all roots outside the limiting radius-r disc (nonattainment of distance to k^a), so they are units there with the expected norms. This extends the map from k(z) to K, and l-polynomials in w are dense. A single upper bound alone would not establish the isometric tensor identification. This addresses the corresponding type-4 norm dependency in the newer source under these exact split hypotheses.

Lemma 6.2.8 rules out a pth root of z in K when |p*z|<r by the resulting Tate algebra's value group or reduction. Lemma 6.2.9 begins the harder special-coset coefficient estimate; its proof continues on the next page. No claim is made for arbitrary nonsplit type-4 extensions.

---

Dependency view 23

# Actual dependency reading 23: Temkin 0707.3953v3, physical pages 46–47

Complete selected text and the individually displayed matching image were read. Lemma 6.2.10 controls the mixed terms of p^n-th powers and the ambiguity of roots. The maxima and sums run over the m given elements, irrespective of the printed n in those indices. Lemma 6.2.9 passes to the Tate algebra from note 22, estimates the coefficient of w in a special coset, and in the Artin–Schreier case removes the p-divisible powers successively. The coefficient bound relies on the original infimum over K: extension to the larger algebra can lower that infimum, but its being at most s ensures the hypothetical large linear coefficient could be improved, leading to the coefficient contradiction. The proof does not assume that extended infima are equal.

The remaining Artin–Schreier estimate approximates the accumulated linear coefficient by a polynomial in a p^N-th root of z; deep ramification controls coefficient-root errors strictly below the leading-term bound, and Lemma 6.2.7 supplies the bound. Proposition 6.2.4 then terminates degree reduction: for types 2 and 3 the special Frobenius Schauder basis gives an attained minimum; for the split type-4 case a special coset is reduced to a constant or a linear topological generator. The mixed-characteristic type-4 reduction continues on the next page. None of these arguments allows replacement of a strict error margin by an unattained infimum equality without choosing an approximation.

---

Dependency view 24

# Actual dependency reading 24: Temkin 0707.3953v3, physical pages 48–49

Complete selected text and the individually displayed matching image were read. The mixed-characteristic polynomial reduction completes Proposition 6.2.4. Theorem 6.3.1 explicitly carries Assumption 6.2.1 and provides an unramified generator, the stated special-coset generator conclusion, and stability of types 2 and 3. Lemma 6.3.2 makes small changes in a generator isometric by factoring rational functions over an algebraic closure. Continuity retains the bound using the smaller actual ratio |z-z'|/r < epsilon. Lemma 6.3.3 compares extension degrees for two close embeddings by a contraction argument with an r-orthogonal basis, epsilon<r<1, and completeness of the finite-dimensional span.

Corollary 6.3.4 uses those estimates after extracting the separable part and approximating inside a finite algebraic extension of k(y), yielding finiteness over any one-dimensional analytic subfield. Theorem 6.3.1's type-2/3 proof then excludes the first immediate degree-p step after a finite tame extension using Propositions 6.2.4 and 6.1.4. Applying this to finite extensions supplies stability. The special-coset cases and the type-4 argument continue on the next page. The aside about nonadditive topological transcendence degree is not used as a theorem input or a newly verified fact in the book.

---

Dependency view 25

# Actual dependency reading 25: Temkin 0707.3953v3, physical pages 50–51

Complete selected text and the individually displayed matching image were read. Theorem 6.3.1 finishes the residue Artin–Schreier case and the type-4 generator case. In type 4 a special coset cannot reduce to a base constant in the split situation: a new element would approximate an algebraic base root better than the base could. The zero-linear case perturbs a generator to a negative pth power, retains the degree by the close-embedding lemmas, and uses Lemma 6.2.8 to ensure the extracted root produces the full degree-p field. Type-4 fields are not claimed stable.

Corollary 6.3.6 is the needed stability result: a type-2 or type-3 one-dimensional analytic field over a stable analytic base is stable. It reduces to the completed Gauss rational field, first to separable finite extensions, then to the completed algebraic closure. The orthogonal basis there is approximated inside a finite coefficient extension k'/k. A detailed descent must ensure both orthogonality and spanning (one may approximate the finitely many representations of initial generators with a strict contraction margin), rather than infer spanning merely from independent nearby vectors. The finite coefficient extension is Cartesian by base stability; the Cartesian tower and its subextension yield the result. Thus the actual source hypothesis includes completeness and stability of the base, and types 2 or 3, not arbitrary type 4 or arbitrary incomplete normed fields.

The selected pages also finish the earlier uniformization theorem by close-generator invariance of residue fields and degrees, then start Appendix A's historical comparison of stable curves and surface desingularization. The theorem's earlier statement and the rest of the appendix are outside this selected source read. This batch now covers physical pages 36–51 in full, 16 of this 60-page arXiv v3 file; it is expressly a partial source read.
