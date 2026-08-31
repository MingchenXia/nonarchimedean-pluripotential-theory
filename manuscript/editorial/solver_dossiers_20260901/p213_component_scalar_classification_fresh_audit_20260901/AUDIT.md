# Exact-final independent audit: component scalar classification

Date: 2026-09-01. Reviewer: `/root/p213_general_propagation_fresh_audit`.

## 1. Verdict and precisely what passes

**Mathematical PASS in the exact stated scope.** No substantive mathematical gap or mandatory correction was found in the classification, nilreduction/topology argument, multiplicity convention, weighted-curvature reduction, support argument, codimension-at-least-two consequence, or examples.

Over a complete discretely valued K with residue characteristic zero, for a good separated strict boundaryless pure n-dimensional analytic X, n>=2, the manuscript establishes that every positive separately d'- and d''-closed ordinary (0,0)-current is uniquely

    T = sum_i c_i delta_(X_i,red),   0<=c_i<infinity,

with the pushforward to X understood. This includes nonnormal and nonreduced X. The sum is finite on each compact test support. It does not require one uniform bound on the coefficients across different components. The canonical current is instead sum_i m_i delta_(X_i,red), with its fixed positive generic multiplicities.

For a fixed continuous pair with equal total curvature, the proof correctly reduces p=0 independence for every such T to vanishing of each component curvature defect R_i. It proves that criterion on a fixed ordinary open domain whose own components meet in codimension at least two, and on irreducible ordinary open domains. It does **not** prove it in the divisorial-intersection case. Global irreducibility is not confused with an irreducible ordinary-neighborhood basis.

This is a research mathematical verdict, not production Rethlas, formal verification, novelty certification, a change to a live chapter, or a solution of the full P21.3 problem. The prior quasi-smooth mathematical theorem is used with its original field and dimension restrictions. The normal scalar theorem is not a premise of this sibling. The earlier source-audit PASS and the curve packet are not used as substitutes for the new arguments.

## 2. Frozen identities and coverage

Target: `../p213_component_scalar_classification_research_20260901/`.

| File | Bytes | SHA256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 17360 | 73f5d4323d81abc8b711aa4dd0d37def0f1ebd789ae19ae9e167c3b2502d4b84 |
| SOURCE_LEDGER.md | 3678 | ee8c6bf9cc37ebf3d909ee78d45175398b4fdf75fbcebd70c1989e2f32b4d8c9 |
| MANIFEST.json | 2911 | a264c37c448550648df933e0ca27802cf68db52894e63e92e0dee2c895d18136 |
| SHA256SUMS | 1455 | ad283bddc96fb66395771a1a165c42120f83086a079c31108dd793c7fe7c9ab8 |
| INPUT_PINS.json | 2041 | ef93009cf0760cc904f2575dc23cb9e79f844294737abf0119765e585e7ebb1f |

The entire 128-line note and 13-line ledger were read. All line references below identify that exact frozen note. No target or prior archive was edited, and no production or live-book operation was performed.

The independent read-only checker verifies nine direct pins, seven source input pins, thirteen target checksum entries, and twelve recursively referenced manifests with 199 entries. The extended 34-node clause graph is acyclic. These mechanical results verify identities and graph syntax, not the mathematical claims. In particular a historical comparison file's presence in the manifest does not import its dimension-one theorems into the argument.

The scalar input is the exact quasi-smooth assembly note SHA256 `5809b99def2c16becb716eb2eb7c24382a8a31655b9b43902804e585cb53bb5c`, previously independently reviewed in full. Its conclusion applies to arbitrary connected ordinary opens in the appropriate strict quasi-smooth analytic spaces, not just projective algebraic spaces.

## 3. Source checks specific to this sibling

The pinned [CLD arXiv:1204.6277v2](https://arxiv.org/abs/1204.6277v2) text was reread at 3.3.5–6; 6.4.1–6; 7.1.1–7; 11.4.1 and 11.4.4; 13.2.4–7; 13.5.1–3; 15.1.1–3 including the form variant; 15.2.1 and its proof; and 16.6.1–3 including proof. The integration/Stokes and compact-cutoff interfaces checked in the normal audit were retained. In particular, the support definition and the locally convex test topology were examined, not only the final nullity slogan.

[Ducros, Les espaces de Berkovich sont excellents, published AIF version](https://www.numdam.org/article/AIF_2009__59_4_1443_0.pdf), Definition 4.15 and its union observation, Theorem 4.20 with proof, Proposition 4.22/Corollary 4.23, §5.2.4, Proposition 5.16 and Theorem 5.17 were checked for the actual component/normalization construction. The domain-normality, density and perfect-field regularity interfaces in Theorem 3.4/§3.4, Lemma 4.24 and §6 were also used with their verified hypotheses.

[Conrad, Moishezon spaces in rigid geometry](https://math.stanford.edu/~conrad/papers/moish.pdf), §1.4 and Theorem 2.1.1, gives bounded extension over the original general nontrivially valued field on a normal rigid space. [Temkin, Introduction to Berkovich analytic spaces, 1010.2235v2](https://arxiv.org/pdf/1010.2235v2), the inner-presentation and domain-interior results in §§3.4.2 and 4.2.4, supply strict ordinary neighborhoods. Neither an algebraic closure nor a global rigid model is assumed.

The original Bartenwerfer 1976 proof was not accessible; the exact general theorem is read in Conrad's primary research paper. No claim to have read that original proof or byte-pinned the online PDFs is made. The curve proof is not a higher-dimensional premise: the unit lifting and multiplicity calculations are present and checked directly here, while no curve zero-atom theorem is used.

## 4. Section 2: support means an ordinary zero germ

Lines 24–28 are valid. This was a decisive point of the audit. CLD 3.3.5 defines support as the complement of the largest ordinary open on which the G-form vanishes. Proposition 3.3.6 proves that below the tropical-dimension threshold the form vanishes on a neighborhood: after a finite local chart cover and shrinking, the chart images have dimension below the form degree, so all the chart forms vanish. Thus 15.2.1(b) is a statement about actual support/ordinary germs, not merely pullback of the form to the analytic subset.

If dim A<q and alpha is a compact ordinary (q,q)-form, its compact support K is disjoint from A. The same K is compact in the open subspace Y minus A. Restriction gives a legitimate compact test there, and extension by zero returns alpha because alpha already vanishes near each point of A. Hence agreement of currents on the complement implies agreement on that test. Positivity and closedness are unnecessary for this particular injectivity deduction.

The local dimension version is legitimate by a finite compact-support partition. It does not require a global finite affinoid cover. Conversely, the statement is restricted to closed analytic A with the strict test-degree inequality; no arbitrary closed tropical-null set is treated by this direct form-support argument.

The manuscript also keeps a necessary distinction: uniquely determining values on (q,q)-tests does not by itself preserve closedness of an extension. The derivative tests have different degrees. In Section 4 the candidate component sum is proved closed independently before support injectivity identifies it with T. Thus a possible boundary term has not been ignored.

## 5. Section 3: general normal complements, including divisors

The connected-complement argument is valid for the stated normal N and an arbitrary closed analytic E of local dimension <n. It is not limited to the singular locus and does allow a conductor divisor.

Normality is preserved on analytic domains. In a strict affinoid ordinary neighborhood D=M(B), the ring is normal and each component has dimension n. The smaller-dimensional E intersect D therefore contains no component; its ideal avoids all minimal primes. This is the exact rigid nowhere-density condition. The inner-presentation construction supplies strict affinoid neighborhoods inside any prescribed ordinary open, without changing K: choose intermediate radii in sqrt(|K^*|) strictly above the coordinate values and below the original presentation radii. The inequalities are strict at the chosen point, so the resulting domain is an ordinary neighborhood.

For a hypothetical ordinary disconnection of N minus E, the 0/1 function is ordinary analytic and bounded. On D its compatible restrictions to

    {|f_j|>=|a|^m}=M(B{t}/(f_j*t-a^m))

are actual affinoid functions. The displayed family is rigid-admissible: on an affinoid test in the complement the f_j generate one, and the bounded coefficients of a unit-ideal identity yield a finite covering at one sufficiently large m. This is a substantive admissibility check, not an identification of arbitrary ordinary and G-topological covers.

Conrad's general-normal bounded extension theorem supplies H_D in B. Uniqueness applied to H_D^2-H_D makes it an idempotent. On ordinary overlaps, smaller strict affinoid neighborhoods remain normal with nowhere-dense E, so uniqueness makes the local functions agree. Their ordinary gluing has two nonempty clopen 0/1 level sets, contradicting connectedness. Dimension drop also gives nonemptiness of the complement.

The ring-valued extension agrees at all Berkovich points through equality in Laurent-domain algebras, not just at a selection of classical points. Neither connectedness of each D nor geometric connectedness after base change is assumed. This proof uses no current extension and has no dependency on the normal scalar theorem.

## 6. Section 4: the actual components and the entire smooth pieces

### 6.1. Compact-test local finiteness

Line 44 uses Ducros' actual definition, not a loose topological substitute: Definition 4.15 says that a G-locally finite family of analytic closed sets meets every affinoid domain in only finitely many members. Theorem 4.20 gives this property for Irr(X). Proposition 4.22 fixes the component dimensions under domains. Because X is good, compact sets admit finite covers by affinoid neighborhoods. Therefore only finitely many X_i meet a fixed compact test support. Any subunion of the components is closed analytic by the same definition and local finite-union argument.

This verifies both the arbitrary coefficient family's local finiteness and the closedness of the union of other components used later. Coefficients may grow without a global bound; on each fixed compact all relevant coefficients form a finite set.

### 6.2. Smooth locus and openness of U_i

For reduced X over perfect K the regular/quasi-smooth locus is a dense analytic Zariski open. On each affinoid, minimal-prime localizations are fields, while excellence makes regularity open. Hence the complement S contains no component and has local dimension <n. Analytic-domain comparison identifies the same locus at all Berkovich points.

Regular local rings are domains, so no point of X minus S lies on two analytic components. The subunion of the other components is closed analytic. Thus U_i=X_i minus S is an ordinary open in X, not just a relatively open subset of X_i. It is nonempty by density. It inherits the analytic hypotheses and is quasi-smooth of pure dimension n.

### 6.3. Normalization is used for connectedness, not to pull back T

Ducros §5.2.4 and Theorem 5.17 give a finite surjective normalization N_i of the reduced irreducible X_i, with N_i normal, connected and pure n-dimensional. Inverse images of affinoid neighborhoods are affinoid; finite algebras over strict affinoid algebras are strict. Finite morphisms and closed immersions are boundaryless. The boundary formula over the separated ambient space therefore makes X_i and N_i boundaryless, and goodness and separatedness hold as asserted. These are constructions over K itself.

The inverse image E_i of S intersect X_i is a closed analytic subset of dimension <n: finite morphisms have zero-dimensional fibers and do not increase the dimension of a closed inverse image. Normalization is an isomorphism over the regular locus. Thus N_i minus E_i is analytically isomorphic to the entire U_i. Section 3 makes this complement nonempty and ordinarily connected. This proves connectedness of the entire U_i, not just the existence of connected neighborhoods in it.

Only after this geometric step is T restricted to the ordinary open U_i. At no point is an unknown current pulled back through the possibly noninvertible finite normalization map. The original quasi-smooth theorem now applies with all its hypotheses unchanged and yields one finite c_i>=0 on each U_i.

### 6.4. Global reconstruction and converse

Each delta_i is a proper pushforward of integration on the pure boundaryless reduced X_i. Compact pullback of tests, positivity of pullback, Stokes, and commutation with both differentials prove that it is a positive separately closed current of bidimension (n,n) on X. Compact-test local finiteness makes sum_i c_i delta_i continuous, positive and closed for any individually finite nonnegative coefficients.

On U_i only the i-th summand remains, with exactly its canonical open-restriction normalization. Thus the sum agrees with T on X minus S. Every compact top test has support there, by Section 2, proving equality on X. No hypothetical singular-supported distribution is removed without testing it; all the actual tests lie in the established equality locus.

A positive compact top test of nonzero canonical integral in U_i uniquely recovers c_i. This also prevents infinite coefficients. The same construction works conversely for arbitrary families with each coefficient finite, not only finitely supported families. The phrase “every finite nonnegative family” at line 68 is read in light of lines 12–14 and the already proved locally finite construction; see the optional wording note in Section 11 below.

## 7. Section 5: nil-invariant test topology but multiplicity-sensitive integration

### 7.1. Form sheaves and the analytic unit calculation

Nilreduction has identical analytic points and completed residue fields because all seminorms kill nilpotents. On each affinoid, the nilradical is nilpotent. A unit modulo it lifts to a unit by the finite geometric series calculation at line 74. Its absolute value at every analytic point is unchanged. Ordinary local moments on the reduction therefore lift after ordinary shrinking; moments upstairs restrict with precisely the same tropical coordinate functions.

CLD 15.1.3(b) and its explicit form variant apply because the space is good, hence almost good, and topologically separated. They give the equality of ordinary smooth form sheaves in all bidegrees. The same tropical images and representatives give injectivity as well as local surjectivity: a vanishing relation between forms remains a vanishing relation after restriction or lift. Wedge products, J, both differentials, supports and the positivity cones are unchanged.

### 7.2. Why the compact-test identification is topological

The argument at line 76 requires more than pointwise equality of functions, and it supplies enough. CLD 6.4.1 and 7.1.2 define the compact-test topology through covering chart systems, compact supports and derivative seminorms on fixed tropical images. Ordinary moments form a cofinal local set of charts by 15.1.1. For a fixed compact test presentation, choose finitely many ordinary neighborhoods on which the reduction's moments lift, and a smooth compact-support partition subordinate to them. The partition functions are common smooth functions under the just-proved sheaf identification.

On each such neighborhood the lifted and restricted moment images coincide and the tropical representatives are identical. Thus the corresponding derivative seminorms agree. Multiplication by the fixed partition functions and restriction to the neighborhoods are continuous. The finite sum gives continuity of the inverse identification on each compact chart stage. Equivalently, this is precisely the local chart criterion of CLD 7.1.3. The forward pullback is continuous by 6.4.3/4. Therefore j^* is a homeomorphism of compact-test spaces, not merely an algebraic bijection.

The continuous transpose consequently identifies all current spaces, with positivity and separate closedness preserved. In particular T=j_*T_red is legitimate. For positive order-zero currents the coefficient measures are identified; multiplying by a continuous, locally bounded f commutes with this transpose. No multiplication of an arbitrary higher-order current by a continuous function is being proposed.

The proof is entirely about nilreduction. It does not create an inverse current pullback for a nontrivial normalization or arbitrary finite map. The reduction retains pure dimension, strictness, goodness and separatedness, and its finite immersion into the boundaryless X is boundaryless. Hence the reduced classification applies.

### 7.3. Generic lengths are not erased

CLD 13.2.4–7 defines the finite positive generic length m_i and proves its compatibility with analytic-domain restriction. In particular a component may split on a smaller analytic domain without changing the inherited generic multiplicity on its resulting components. CLD 13.5.2 defines the fundamental cycle, and 16.6.3 proves exactly delta_X=delta_[X]. Its proof explicitly uses the reciprocal calibrated degree of the reduction immersion, rather than treating that immersion as degree one.

Consequently

    delta_X = sum_i m_i delta_i,

whereas an arbitrary classified current has unrestricted nonnegative real c_i. On an irreducible X the scalar relative to delta_X is c_1/m_1. There is no conflict with nil-invariance of test spaces: a distinguished continuous functional may differ by multiplicities even when its test space is canonically identified. Nilpotent structure supported only in smaller-dimensional embedded loci does not introduce new top-current summands.

## 8. Section 6: weighted curvature, supports and the precise threshold

### 8.1. Exact equivalence for a fixed equal-curvature pair

The products u delta_i and v delta_i exist because the component currents are positive of order zero and u,v are continuous. Differentiation is local and does not enlarge support. On a compact test only finitely many components occur, so all sums may be differentiated termwise. This verifies both (6.2) and (6.3), with the m_i retained in the former and arbitrary c_i in the latter.

For the fixed pair satisfying the weighted relation, if every R_i vanishes then independence follows for every classified T. Conversely each delta_i itself is an admissible positive separately closed (0,0)-current, so independence for every T forces R_i=0. This is an exact equivalence. It is not obtained by dividing the total weighted relation componentwise at intersection points.

### 8.2. Support containment is conditional on equal total curvature

Let B_i be the intersection of X_i with the union of all other components. The union is closed analytic and the B_i form a locally finite family. Outside X_i the current R_i is zero by locality. Outside the union of the other components, the canonical identity becomes delta_X=m_i delta_i, so the assumed weighted curvature relation gives m_i R_i=0. These two ordinary open sets cover X minus B_i. Hence Supp(R_i) is contained in B_i.

This reasoning proves (6.5) under (6.2), as fixed in the surrounding text at line 96. It is not a support theorem for arbitrary continuous u,v without the equal-curvature assumption. It also avoids inferring injectivity of proper pushforward from a normalization or of restriction to the underlying analytic subspace.

### 8.3. Codimension two versus codimension one

R_i acts on compact (n-1,n-1)-forms, not top (n,n)-forms. If dim B_i<n-1, every such test has support disjoint from B_i by CLD 15.2.1(b). A current supported there must then vanish. Positivity of R_i is unnecessary and is not assumed. This proves the codimension-at-least-two conclusion exactly as stated, including n=2, where the intersections are zero-dimensional.

If B_i is divisorial, dim B_i=n-1 and this strict inequality fails. The manuscript expressly leaves that case unresolved. A vanishing weighted sum on a shared divisor does not alone force each signed defect to vanish. The one-dimensional zero-atom argument is not imported. The distinction between the classification's test degree n and curvature's test degree n-1 is correct throughout.

### 8.4. Fixed-domain and local-basis scope

“Ordinary domain” here is an ordinary open analytic domain, with the inherited boundaryless hypotheses, not an arbitrary affinoid domain with boundary. The analytic components must be those of that actual open domain. An irreducible such domain has one component and hence no B_i, so the equal-curvature conclusion follows directly. Connectedness alone would not suffice.

For a local statement on an arbitrary U, the asserted irreducible ordinary-neighborhood basis is an additional hypothesis. The manuscript does not claim that global irreducibility guarantees this basis. A nonnormal irreducible space may have several branches in a small ordinary neighborhood. The stated conditional local conclusion avoids this trap.

## 9. Section 7: examples and counterchecks

The divisorial crossing admits independent nonnegative component-current weights. It is not, by itself, a pair u,v exhibiting cancellation of curvature. The manuscript correctly declines to call this a BT counterexample.

For the codimension-two linear crossing, the ambient affine space has 4+(n-2)=n+2 coordinates. Each component has two independent linear equations, hence dimension n. Their intersection has four such equations, hence dimension n-2. Their reduced union is pure n-dimensional and its analytification has the stated analytic properties. The support criterion applies in test degree n-1, so it gives the asserted fixed-domain conclusion for every continuous equal-curvature pair on this union. This is a genuine nonnormal example covered by that consequence, without forcing equal scalar weights on the components.

For a thickening of an irreducible space with generic multiplicity m, the distinguished current is m delta_red, while arbitrary currents have coefficient c delta_red. The conversion factor c/m is correct. The example does not assume the nilpotent order is globally uniform away from generic points, and no extra coefficient for embedded lower-dimensional support is needed.

## 10. Dependency graph and independence

The new classification depends on the original quasi-smooth theorem, primary component/normalization geometry, the independently restated general connected-complement proof, and CLD's form-support and test-topology facts. The normal scalar theorem is absent from its prerequisite graph. The source-audit report is not an automatic verdict on this manuscript; Sections 2, 4, 5 and 6 were all checked separately here.

The new graph appends twelve nodes to the earlier 22-node quasi-smooth graph, for 34 acyclic nodes. In particular:

    normal-complement geometry -> connected entire U_i
    quasi-smooth scalar input + connected U_i + top-test support
        -> reduced classification
    reduced classification + nil test-topology isomorphism
        -> all-pure classification
    all-pure classification + canonical multiplicities
        -> weighted curvature criterion and intersection support
    intersection support + test degree n-1
        -> codimension-two / irreducible-domain conclusion.

The component sum's closedness is established independently before comparison with T. The nilreduction isomorphism does not use the classification it later transports. The curvature criterion is downstream and is not used to prove scalar classification. No curve theorem, production receipt or audit label creates a proof edge. The previous L/O/Q/R clause restrictions remain unchanged.

## 11. Findings and remaining obligations

**Substantive gaps: none found. Required corrections: none.** Three optional future exposition clarifications would make the already valid scope harder to misread:

- Line 68: replace “every finite nonnegative family” by “every family of individually finite nonnegative coefficients”; lines 12–14 and 64 already establish the intended locally finite infinite-family assertion.
- Line 76: cite CLD 6.4.1 and 7.1.2–3 explicitly for the compact-test topology; the stated cofinal presentation argument is valid, as checked in Section 7.2 above.
- Line 102: prepend “under (6.2)” to the support claim, and in line 108 say “ordinary open domain” explicitly. The surrounding proof already imposes these hypotheses.

No frozen input should be edited on account of those optional suggestions. Any subsequent broader assertion must be a separate sibling/addendum with its own exact review.

The remaining mathematical question identified by this manuscript is the divisorial component-curvature cancellation problem for the relevant continuous psh equal-curvature pairs. The present reduction neither proves cancellation impossible nor constructs a pair realizing it. Other retained exclusions are positive-bidegree scalar comparisons, discontinuous potentials, arbitrary valued fields and envelope regularity. Therefore the correct conclusion is the classification and explicitly delimited p=0 consequences, not a full P21.3 claim.

Within those limits the new deductions have been independently checked, and no further missing lemma is identified for this exact manuscript. Production, integration into a live text and novelty assessment are distinct tasks and have not been performed here.
