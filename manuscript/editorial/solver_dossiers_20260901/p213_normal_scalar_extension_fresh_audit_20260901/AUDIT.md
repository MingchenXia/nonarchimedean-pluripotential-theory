# Exact-final independent audit: normal scalar-current extension

Date: 2026-09-01. Reviewer: `/root/p213_general_propagation_fresh_audit`.

## 1. Verdict and its boundary

**Mathematical PASS in the manuscript's stated scope.** The new restriction-injectivity argument, ordinary connectedness of the smooth complement, restoration of the scalar identity on a normal space, continuous equal-curvature consequence, and both examples are valid. No substantive mathematical gap or mandatory correction was identified in the exact frozen text reviewed below.

The normal scalar conclusion is for a complete discretely valued K of residue characteristic zero, a good separated strict boundaryless normal K-analytic space of pure dimension n>=2, and any nonempty connected ordinary open W. The current is an ordinary positive CLD current of bidegree (0,0), separately d'- and d''-closed. The result is one unique finite c>=0 with T=c delta_W.

Section 2 has its own wider scope: two already-defined positive closed currents of bidegree (p,p), q=n-p>0, over any complete nontrivially valued field, with a closed set null for H^q under every compact-domain G-chart. Their common restriction determines them uniquely. This is injectivity, not an existence theorem for extending currents supplied only on the complement.

The proof uses the exact previously reviewed quasi-smooth theorem and the stated standard external theorems. It contains no new unproved normal-extension premise. An old audit PASS is not substituted for a proof, and lack of production status is not treated as a mathematical gap. This review is not production Rethlas, formal verification, a novelty claim, or retirement of the full P21.3 problem. It makes no classification claim on all reduced or nonreduced spaces and no positive-bidegree scalar theorem.

## 2. Exact material reviewed

Target directory:

`../p213_normal_scalar_extension_research_20260901/`

| File | Bytes | SHA256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 18983 | 7dc4789b43c162c4ed693a437cb6ff4a4c0a470f7de8fcfc23b0e3fa8a9756dd |
| SOURCE_LEDGER.md | 5679 | c32ed76cac7b956a051761e3687d7e4df482036f336679fb0d9a0a615c686abe |
| MANIFEST.json | 2128 | d906be97d77b8e4acb8c6f003bf387133cd4cabdf034495fcf8f2c297cc7cbbd |
| SHA256SUMS | 1108 | d0cad95e550f0e011618b18b375e0d1ed01796cb78fc401a68cb350878dc7823 |
| INPUT_PINS.json | 1284 | eab1283c9f7ef6e88dd80430354c9c9e92dfdcc9f6e57abfacaaba1afa5ed79f |

Every line of the 138-line note and 23-line source ledger was read. Line references below refer to that exact RESEARCH_NOTE.md, not a prospective revision. No target bytes were edited. The author's freeze script was not executed in a write mode.

The independent read-only checker verifies nine direct pins, the target's five input pins, eleven target checksum entries, and twelve recursively referenced manifests containing 197 checked entries. It also checks the 31-node extended clause-dependency graph for cycles. Those are provenance/syntax checks only. The mathematical checks are below.

The smooth mathematical input remains RESEARCH_NOTE.md in `../p213_qualified_scalar_assembly_research_20260901/`, SHA256 `5809b99def2c16becb716eb2eb7c24382a8a31655b9b43902804e585cb53bb5c`. Its actual theorem is for arbitrary ordinary opens of the stated strict quasi-smooth analytic spaces; the present argument does not accidentally import only its projective stage.

## 3. Primary-source checks performed

The local [CLD 1204.6277v2](https://arxiv.org/abs/1204.6277v2) text has SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`. This review directly reread 5.11.1; 7.2.8–12; 7.3.1–5; 11.10.1; 15.2.1–9; 15.7.1–2; and 16.8.3–5 with proof. They provide coefficient measures, compact cutoffs/density, singular-space integration and Stokes, ordinary-domain compatibility, and all-chart nullity. The proof of 16.8.5 is local; global paracompactness is not a missing assumption.

[Ducros, Les espaces de Berkovich sont excellents, published AIF version](https://www.numdam.org/article/AIF_2009__59_4_1443_0.pdf), Theorem 3.4 and §3.4, Lemma 4.21/Proposition 4.22, Lemma 4.24, and Proposition 6.3/Remark 6.5/Proposition 6.6, were checked for analytic-domain normality and dimension, ordinary density, and regularity versus quasi-smoothness over perfect K. These statements concern Berkovich spaces, not merely rigid classical points.

[Conrad, Moishezon spaces in rigid geometry](https://math.stanford.edu/~conrad/papers/moish.pdf), §1.4 and Theorem 2.1.1, gives the precise bounded extension theorem on normal rigid spaces across nowhere-dense analytic sets over a general complete nontrivially valued K. Its proof of Lemma 2.1.3 explicitly uses idempotents. [Conrad, Irreducible components of rigid spaces](https://math.stanford.edu/~conrad/papers/irredpaper.pdf), §2.1 terminology, the discussion before Lemma 3.3.2, and the characteristic-zero part of Lemma 3.3.5, confirm the affinoid nowhere-density and codimension assertions. The algebraically-closed-field reduction in a different proof, Theorem 2.3.1, is not used here.

[Temkin, Introduction to Berkovich analytic spaces, 1010.2235v2](https://arxiv.org/pdf/1010.2235v2), 3.4.2.1, 3.4.2.3, §4.2.4, §5.4, and 4.3.1.1, supplies the inner presentation/interior and connected-neighborhood interfaces. The last item, which does not assume smoothness, is sufficient for the connected shrinking used in Section 5.

The original Bartenwerfer 1976 PDF was not accessible in the source investigation. This report therefore does not claim to have read or independently re-proved its original proof. Its exact general theorem is read in Conrad's primary research paper. Online PDFs were read at the cited URLs/versions; no local-byte hashes for those PDFs are invented.

## 4. Section 2: all coefficient measures, not signed mass cancellation

### 4.1. Degree and hypothesis ledger

Lines 32–36 use q=n-p, which is the bidimension and the degree of the coefficient test form. This is the Hausdorff exponent in CLD 16.8.5. Positivity and separate closedness belong to each T_i. The theorem is never applied to the difference T_1-T_2. The nontrivial valuation and boundaryless hypotheses are present. The source-space definition quantifies over every G-chart on every compact analytic domain, rather than one favored tropicalization.

Lines 50–52 correctly distinguish dim A<n-p for positive bidegrees from the p=0 condition dim A<n. The assumption p<n leaves q>0. No unstated p=n assertion is needed.

### 4.2. Why arbitrary alpha has an actual signed Radon coefficient measure

The deduction at lines 38–46 is valid, but its measure content deserves an explicit audit: a general order-zero distribution on an arbitrary tropical space must not automatically be called a Radon measure. Here positivity, the analytic local setting and smooth density supply the necessary stronger conclusion.

Work in an ordinary chart neighborhood, then restrict near a compact test support. The J-antisymmetric part of alpha pairs to zero with the symmetric current. Write the symmetric ambient representative in the basis of exterior q-forms. The cone of positive symmetric-matrix forms on this finite-dimensional space has an interior positive element beta. On the fixed compact set its coefficient matrix is bounded, so for sufficiently large C both alpha+C beta and C beta are positive after pullback. With a smooth cutoff this gives the local difference-of-positive-forms decomposition. This argument uses the positive cone, not the generally different cone of sums of decomposable strongly positive forms.

For each positive form gamma, the scalar functional rho -> <T_i,rho gamma> is positive on nonnegative smooth tests and is controlled on every fixed compact support by a cutoff equal to one there. CLD 15.2.5–7 supplies the cutoff and smooth approximation to continuous compact tests. Riesz representation therefore gives a positive Radon measure. Taking the difference gives mu_i=T_i wedge alpha as an actual signed Radon measure. The same reasoning on overlaps gives the coefficient measure for any ordinary local alpha.

Thus the manuscript's alternative phrase “usual decomposition into positive coefficients” at line 42 is sufficient in the present positivity scope. It is not an assumption that every order-zero current in all settings is a measure, nor an appeal to a strongly-positive spanning assertion.

### 4.3. The nullity really is total-variation nullity

Apply CLD 16.8.5 first to each positive T_i and each positive local gamma. Its negligible-set conclusion for the resulting positive measure is zero mass on every measurable subset of A. For an arbitrary alpha use the preceding difference of positive forms; then

    |T_i wedge alpha| restricted to A = 0.

In particular the domination at line 44 is legitimate. The conclusion is stronger than mu_i(A)=0, which would permit signed cancellation. This also explains why the proof of the CLD theorem for coefficient measures can be used here without inferring negligible subsets from a single signed saturated-fiber integral.

Equality of T_1 and T_2 on Y minus A gives equality of coefficient measures on that open: compact smooth tests determine their continuous-test integrals by density. Their difference vanishes on the open complement and has zero variation on A. Hence it vanishes everywhere. This reasoning applies to the original measures individually before forming their difference.

Finally, CLD 15.2.9 gives a compact-support-local smooth partition. For a particular compact test only finitely many pieces meet its support. Alternatively, once a test is treated as a single local form, a cutoff equal to one near its support recovers its pairing from the coefficient measure. Neither step requires global paracompactness of Y. Lines 46 and 48 have the correct scope.

### 4.4. Closed analytic sets satisfy the all-chart condition

On a compact affinoid piece the closed analytic set is the zero fiber of the map given by finitely many generators of its coherent ideal. The fiber dimension bound is its analytic dimension, so this is a presentation in CLD Definition 11.10.1. A compact analytic domain has a finite such affinoid G-cover. Restricting any of its G-charts to the pieces, each tropical image has dimension at most dim A. Finite unions preserve H^q-nullity when dim A<q. Thus Example 16.8.4 applies with all required quantifiers.

This verifies lines 50–52 without assuming a global finite affinoid cover. In the normal application the local bound n-2 is uniformly below n; no maximum over an uncontrolled infinite collection is used.

## 5. Section 3: normal affinoids and ordinary connectedness

### 5.1. Regular, quasi-smooth and smooth are not conflated at the boundary

At lines 60–62, analytic-domain restriction preserves R_1 and S_2, hence normality. For D=M(B), normality of the Berkovich space agrees with normality of B, and the associated rigid affinoid Sp(B) is normal. A normal noetherian ring is a finite product of normal domains. Ducros' domain dimension results imply that every factor here has dimension n.

Residue characteristic zero implies char K=0 and perfection. The non-quasi-smooth locus on D is therefore its nonregular analytic locus. Excellence makes this locus closed analytic. Normality excludes nonregular primes of height zero or one; the dimension theory for the pure-dimensional strict affinoid then gives dim(S intersect D)<=n-2. In particular its ideal avoids all minimal primes of B, exactly the rigid nowhere-density criterion.

Equally importantly, Ducros §3.4 identifies that locus with the restriction of the ambient non-quasi-smooth locus. This is valid even for boundary points of D. It is not deduced from a smoothness statement only on the affinoid's intrinsic interior. The note expressly uses quasi-smoothness on domains and smoothness on the boundaryless ordinary open. The reduced ideals glue, giving the stated closed analytic S. Ducros Lemma 4.24 gives the ordinary density of the complement.

The same facts hold on every smaller affinoid in the overlap argument, not just the initial domains. This discharges the exact nowhere-density needed by each invocation of bounded extension.

### 5.2. The strict affinoids are actual ordinary neighborhoods over K

Line 70's construction is valid. Boundarylessness and goodness give an affinoid neighborhood with an inner presentation at x. If the coordinate bounds are r_i and values are |f_i(x)|<r_i, choose s_i in sqrt(|K^*|) between them. Since |pi|^Q is dense in the positive reals, no extension of K is required. The Weierstrass domain |f_i|<=s_i has a presentation by K{s^(-1)T}, hence is strictly K-affinoid. Its inequalities are strict at x, so it contains an ordinary neighborhood of x. The intrinsic/relative interior identities identify this with the required ordinary domain interior in W.

This is a construction of a suitable strict neighborhood basis, not the false assertion that every affinoid domain in a strict space is strict. It does not assert that D is itself boundaryless. Normality and purity are inherited by domain restriction as above.

### 5.3. Actual admissibility of the puncture cover

Lines 72–78 supply a genuine bridge. The Laurent domain D_(j,m) has the strict algebra

    B{t}/(f_j t-a^m),

so f_j is invertible there, and the Berkovich domain is exactly |f_j|>=|a|^m. Their union is D minus S at all Berkovich points. The locally constant ordinary analytic h restricts to an element of each actual affinoid algebra.

For a rigid affinoid test mapping into the rigid complement, the f_j have no common maximal zero. The strict affinoid Nullstellensatz gives the unit-ideal relation. Boundedness of its coefficients supplies a uniform positive lower bound for max |f_j|, and finitely many Laurent domains at one m cover the test. Such a finite affinoid-domain covering is admissible. The compatible restrictions of h consequently define a bounded rigid function, not just a function on the set of classical points.

The empty-set convention f_1=1 at line 72 handles the case S intersect D is empty. The domains need not themselves be connected, and the bounded extension theorem does not require connectedness of D.

### 5.4. Extension and ordinary gluing retain all points and the original field

Theorem 2.1.1 applies to normal Sp(B) and its nowhere-dense analytic Z_D. Its extension H_D belongs to B. Restriction equality is equality in every Laurent-domain algebra, hence equality at all Berkovich points. No inference solely from possibly insufficient classical-point topological data is made.

H_D^2-H_D extends zero on the complement, so uniqueness gives its vanishing in B. On an overlap of ordinary interiors, a smaller strict affinoid F lies in that overlap and remains normal with nowhere-dense singular support. The two restrictions extend the same h there, so they agree by the same uniqueness theorem. This is ordinary sheaf gluing of actual analytic functions on an ordinary cover.

The resulting H is an idempotent in O(W). Evaluation in each completed residue field gives only 0 and 1; continuity then makes the two level sets ordinary clopen. Both contain one of the hypothesized nonempty U_i. This contradicts ordinary connectedness. Nonemptiness of W minus S follows from local dimension drop/density. Lines 68–88 therefore prove exactly the connectedness needed for the smooth scalar input.

No algebraic closure, geometric connectedness hypothesis, global rigid model for W, admissible-open/ordinary-open identification, current extension, or paracompactness is inserted. This is a substantive proof beyond simply citing normal connected equals irreducible.

## 6. Section 4: canonical integration on the singular space

### 6.1. Existence, positivity, both differentials, and restriction

Line 96 is justified in the required singular setting. CLD 15.7.1 makes every topologically separated pure n-dimensional analytic space a calibrated tropical space of level n with its analytic boundary. Quasi-smoothness is not one of its hypotheses. Thus CLD 7.3.1 defines delta_W as integration of compact ordinary top forms, and its positive calibration gives a positive, symmetric order-zero current.

For a compact (n-1,n)-test form, CLD 5.11.1 identifies the integral of d' of that form with its boundary integral. The boundary is empty here, so d' delta_W=0. Applying J and symmetry gives d'' delta_W=0 as well. This is separate closedness, not merely d'd''-closedness.

CLD 15.7.2 identifies the analytic-domain structure and calibration with those induced from the ambient tropical space. In particular ordinary-open restriction of the integration current is exactly integration on that open. No residue-degree renormalization, normalization pushforward, or generic multiplicity is silently changed on W^o. This is delta_W restricted to W^o equals delta_(W^o), as used in line 96.

### 6.2. Use of the smooth theorem and restoration

W^o is nonempty, ordinarily connected, good separated strict boundaryless quasi-smooth and pure n-dimensional. T restricts as an ordinary positive separately closed (0,0)-current. The complete smooth theorem's hypotheses match without changing K, n, the ordinary topology, or its current normalization. It furnishes the finite nonnegative c in (4.1).

Both T and c delta_W already exist on W and are positive closed. The closed singular set has dimension <=n-2<n, so the previously proved injectivity applies with p=0 and q=n. It recovers equality on all compact tests, including tests described using neighborhoods meeting S. The proof is not an attempted extension construction for T|W^o.

A compact positive top test of nonzero canonical mass inside the nonempty smooth open determines c and proves uniqueness and finiteness. The zero-current case is included. There is no remaining unknown distribution supported on S under the exact coefficient-measure comparison used in Section 2.

CLD 15.2.1(b) also shows that a top form's support misses a lower-dimensional closed analytic set, yielding a shorter special-purpose route for this particular S. That observation is not needed to validate the frozen proof. The verdict above audits its actual broader Section 2 argument rather than replacing it with a different proof.

## 7. Section 5: continuous multipliers and connected shrinking

Line 106's connected shrinking is available also at singular points. Temkin 4.3.1.1(ii) gives a fundamental family of connected analytic-domain neighborhoods. For any ordinary open O and x in O, one such connected neighborhood lies in O and contains an ordinary neighborhood of x. It lies in the connected component of O containing x. Therefore every component of O is ordinary open, giving the required connected ordinary neighborhood basis. No smooth local-contractibility theorem is being applied to a singular space.

On such a neighborhood the proved scalar identity is T=c delta with a constant c. Continuous u and v are locally bounded; the order-zero positive-current multiplication of CLD 7.2.12 is defined and agrees with uT=c[u] and vT=c[v]. This is coefficient-measure multiplication, not an assertion that u and v are smooth. Differentiating distributionally and using the assumed equality of curvature currents gives the displayed equality. Currents are ordinary sheaves, so the local equalities glue over arbitrary U, including disconnected U.

The result genuinely permits continuous equal-curvature pairs, with the continuous psh case as a subcase. It does not require the difference u-v to be psh. It does not claim any higher-degree BT independence and does not use positivity of a differentiated difference.

## 8. Section 6: both examples checked directly

### 8.1. Quadratic cone, lines 116–122

There are n+1 affine variables and one nonzero hypersurface equation, so the dimension is n. Under the involution on s,t, the invariant monomials have even total s,t-degree. If both exponents are even they are generated by s^2 and t^2; if both are odd factor st first. Reducing using uv=w^2 leaves monomials not involving both u and v, whose images have distinct s,t-exponent pairs. Thus the claimed invariant-ring presentation has no additional relation.

For an element of the fraction field of the invariant ring integral over it, the same monic equation has coefficients in the polynomial ring. It lies in that polynomial ring by integral closedness, and it is invariant as an element of the invariant fraction field. Hence it lies back in the invariant ring. This proves normality; it does not assume the polynomial ring is finite étale over the invariant ring at the vertex.

The derivatives v,u,-2w cut out exactly u=v=w=0 because char K=0. The singular locus has dimension n-2, including the n=2 isolated-vertex case. The normality of analytification follows from the local comparison, and the ordinary affine analytification has all the asserted analytic hypotheses. Therefore this is a genuine singular example within the newly proved scope.

### 8.2. Crossing components, lines 126–132

Take Y_1={u=0}, Y_2={v=0}. Each is an affine n-space and has a positive separately closed integration current. Its closed embedding into Y is topologically proper. Pullback of compact tests is compact, preserves positivity and commutes with d' and d'', so pushforward gives a positive separately closed current of bidimension (n,n) on pure-dimensional Y. This justifies the current construction, not merely its formal cycle notation.

On {v!=0}, only Y_1 remains, and its ordinary-open identification with that open in Y gives coefficient 1 relative to delta_Y. On {u!=0}, the corresponding coefficient is 2. Both opens are nonempty smooth ordinary opens and contain positive compact top tests of nonzero mass. Their different coefficients rule out a single scalar multiple. The two connected affine analytifications intersect, so Y^an is connected. The lower-dimensional intersection has zero coefficient measure by the same all-chart CLD argument.

The example refutes weakening normal to arbitrary connected reduced spaces for the constant-scalar conclusion. It is correctly not labeled a BT counterexample, nor a resolution of the original full question. No general weighted-component classification is being inferred from this one explicit example.

## 9. Acyclic dependency audit

The new mathematical edges are:

    CLD coefficient measures/nullity -> restriction injectivity
    Ducros normality/dimension + bounded extension + affinoid topology
        -> ordinary connected smooth complement
    CLD integration/Stokes -> singular canonical integration current
    reviewed quasi-smooth theorem + the three preceding results
        -> normal scalar theorem -> continuous p=0 equal-curvature result.

No normal scalar conclusion proves any of its three new prerequisites. The bounded-idempotent argument uses analytic functions, not currents. The singular integration current is built independently of the scalar theorem. Restriction injectivity is proved independently for two given currents. The quasi-smooth input does not reference any of these later conclusions.

DEPENDENCY_EXTENSIONS.json appends nine nodes to the previously checked 22-node graph. The full 31-node graph is acyclic. Audit files, source-review verdicts and checksum passes are deliberately not proof nodes. Historical statements imported only for geometry retain their prior clause restrictions; the new normal extension does not revive a stronger unproved R claim, alter L/O/Q dependencies, or require an affinely separated chart where only differential separation is known.

## 10. Findings, optional exposition, and remaining scope

**Substantive defects: none found. Required corrections: none.** The following are optional exposition additions for a future non-frozen revision, not qualifications to the verdict:

- Line 42 could explicitly name the positive symmetric-matrix cone/difference-of-positive-forms argument, to prevent a reader from confusing it with the false general inference “order zero implies measure” or with a strongly-positive spanning claim.
- Line 96 could cite CLD 15.7.2 beside 15.7.1 and mention that d''-closedness follows by J from Stokes. The necessary compatibility is already valid.
- Line 106 could cite Temkin 4.3.1.1 for singular-space connected shrinking; the smooth-space local-contractibility citation would not be the appropriate justification there.

Nothing in this review requires editing frozen bytes. A later reduced/nonreduced classification or a componentwise-curvature assertion requires its own exact scope and independent review. No current-existence theorem across A, general positive-bidegree comparison, arbitrary-valued-field scalar theorem, nonnormal constant-scalar theorem, or full P21.3 result has been certified here.

The earlier source/interface report resolved the literature and topology question before this exact manuscript audit; it was not treated as automatic approval of Sections 2, 4, 5 or the examples. Those sections and the entire frozen argument have now been checked independently as detailed above. Standard external results remain cited mathematical inputs, not unverified new obligations. Production and novelty status are separate from this mathematical PASS.
