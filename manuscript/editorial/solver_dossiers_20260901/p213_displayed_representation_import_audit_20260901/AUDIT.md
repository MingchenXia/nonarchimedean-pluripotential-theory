# Independent audit: importing the displayed representation formula

Date: 1 September 2026. Reviewer: `/root/p213_general_propagation_fresh_audit`.

## Verdict

**PASS for the directly proved displayed source-cell representation; PASS for its import on the actual eligible domains needed by C; PASS for the clause-level acyclic dependency graph below.** No new substantive mathematical gap was found in that formula or in this import. R need not remain an unproved mathematical premise merely because production verification has not occurred.

This verdict does not assert local affine separation. It accepts the explicit formula with arbitrary compact smooth source multipliers and no lower-cell residual, under R's stated analytic hypotheses. It does not import the literal stronger opening hypothesis of CLD Definition 7.5.1 into analytic spaces by inference from differential separation. Neither the separate cross-refinement proof nor a general current-rigidity theorem is used to prove R.

The import is valid on the deliberately chosen paracompact rational-moment domains in C Section 9 and on the full inverse-image coordinate domains in L/Q/O. It is **not** a claim that every arbitrary ordinary open U or W has a global locally finite compact-cell decomposition. This distinction does not obstruct C's finite compact-test argument. An unrelated newly written assembly manuscript remains a separate exact-byte review target; this report is not its advance acceptance, production verification, or authorization to retire an open item.

## Exact objects and review boundary

The representation files are in

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/`.

| Object | Bytes | SHA256 |
| --- | ---: | --- |
| R statement.tex | 2211 | `5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a` |
| R proof.tex | 11486 | `27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a` |
| Earlier R independent audit | 18118 | `3f646a1aa73096965cc71e12bcb9ce38f30e2d44d179adda5cb8492721bdcdba` |
| C endpoint note | 26431 | `f6626819973ecf135a2065786a0bee3fa1847592fc061f5892da7e31a591117c` |

The complete R statement, proof, previous audit and source ledger were read. The R proof was checked against the actual CLD primary statements, not accepted from the older PASS label. The earlier report does accept the displayed formula; its affine/differential-separation qualification is real but is not a rejection of that formula.

The complete existing L/O/Q independent reports were read, and their actual mathematical clauses and dependency boundaries were checked against the research notes. In particular the predecessor V's Sections 3--4 were read directly, and Berkovich's special-formal completion-to-tube result was checked in the primary paper. This is a fresh full review of R and the import/dependency interfaces. It is not advertised as another line-by-line rerun of every Banach-division or residual-divisor calculation in L and O. Those calculations have their separately identified independent mathematical reports; the graph below records exact clauses rather than treating audit labels as proof premises.

All referenced frozen identities and the read-only checker are in this directory. No input, previous audit, live manuscript, inventory, git state or production record was changed.

The final independent checker verified 16 pinned files, seven pinned manifests and all 105 manifest entries, and found the 16-node dependency graph acyclic. During preparation, a transposed A-manifest hash in this new pin list and an unsupported `files` versus `entries` manifest-key assumption in this new checker were corrected. These were reviewer-owned mechanical errors; no target bytes changed. The checks establish identity and graph syntax, not mathematical truth.

## 1. The direct R argument supplies the formula

### Analytic structure, cell decomposition, and coefficient measures

R assumes a complete nontrivially valued field and a good, separated, paracompact, boundaryless analytic space V pure of dimension n>=1, with an ordinary tropical chart F on all of V. CLD 12.9.5 supplies the vertebrated G-tropical structure, and 15.7.1 supplies the level-n tropical structure used for currents. Goodness and separation give local holomorphic, hence differential, separation by 15.2.2--15.2.4. The compact cutoffs and smooth density needed in the argument follow from 15.2.5--15.2.7, with no local-affine-separation assertion.

The maximal-variation set S is closed and pure n-dimensional, and F restricts to a piecewise immersion by 5.2.1 and 5.2.5. Closedness in paracompact Hausdorff V makes S paracompact. The compact injective PL chart cover in 2.2.12 and compatible compact-cell decomposition in 2.2.15 supply the required locally finite F-cells. This is the point where paracompactness genuinely enters; it is not a consequence of mere goodness or separation.

For a positive top form, the functional `rho -> <T,rho omega>` is a positive coefficient measure by 7.2.8 and 7.2.11. General coefficients are handled by local positive differences and symmetry, followed by smooth density. This does not identify the (0,0)-current T itself with a scalar Radon measure on V. The positive cone, not an unjustified strongly-positive spanning claim in an ambient intermediate bidegree, is sufficient for the decomposition. Antisymmetric top components vanish on n-dimensional source pieces and create no omitted pairing.

### Strong support and ALL-chart lower-face nullity

CLD 5.3.1, 5.3.4 and 5.3.6 give three distinct required facts: an F-tropical form with max(p,q)=n is strongly supported on S; this property survives multiplication/wedging by arbitrary smooth source forms and differentiation; and restriction to a strong support detects vanishing. Therefore an F-based top coefficient measure is supported on S. This is not a statement that T is supported on the skeleton of one fixed moment for tests from every other moment.

Let B be the union of lower-dimensional cells. Local finiteness makes B closed; it is PL in S and is ambient PL by 3.2.8(d). For **every** compact analytic domain A and **every** G-tropical chart H on A, 3.2.8(c) makes B intersect A a compact PL set and H restricted to it a PL map. A common finite subdivision shows its image has dimension at most n-1. This verifies the universal quantifier in 16.8.3, not just negligibility in the original F image.

CLD 16.8.5 now applies to the original positive closed current of bidimension (n,n), since the base valuation is nontrivial and V is boundaryless. It makes each coefficient measure null on B. For signed coefficients, apply the positive local decomposition to obtain nullity of total variation. No signed current is passed into the positive-current theorem. No L/O/Q, semistable model, coefficient-propagation result, or rigidity conclusion is a premise of this step.

### Cutoff cancellation and a tangential target measure

At an interior point of a top cell, 2.2.8 allows an ordinary source neighborhood meeting S only inside that cell interior. Hence F is injective on the local source skeleton. For a compact cutoff chi equal to one near the point, the compact set `supp(d'chi) union supp(d''chi)` intersects S away from the point. Its F-image therefore misses F(x). The target ball O can avoid that compact image and simultaneously have its slice Q in the cell plane covered by the chi=1 source region.

The localized pushforward `F_*(chi T)` is legitimate because the multiplied current has compact support; 7.1.10--7.1.11 provide this pairing without properness of F. The derivative error vanishes **as a source form**: the cutoff derivative vanishes off its support, the pulled-back (n-1,n)-form vanishes off S, and on their intersection its target support has been excluded. The d'' argument is the same. Thus the target current is closed on O, without claiming chi T is closed globally.

If a target top form restricts to zero on the cell plane, its source pullback times chi is strongly supported and restricts to zero on S, so it is zero. This establishes tangentiality, not merely set-theoretic support. The factored positive functional is a Radon measure on the Euclidean n-ball Q. Coordinate-deleted primitives show all first distributional derivatives vanish. The local convolution argument then gives a finite constant multiple of Lebesgue measure. Only a Euclidean ball is convolved; no singular tropical support is regularized.

### Recovery of the SOURCE measure and arbitrary multipliers

On the local skeleton above Q, injectivity and the second target-ball condition force every source point into the chi=1 region. The map from that skeleton portion to Q is a homeomorphism. Thus the pushforward equality recovers an individual source Radon measure; it is not merely a sum over unseen sheets.

Strong-support detection expresses every F-based top form on this neighborhood as its scalar coefficient times the reference top form. The source measure equality may then be integrated against **any** compact smooth source rho. R never requires rho to factor through F on the whole analytic neighborhood. This is the exact feature later used by Q and C.

The local constants agree on overlapping interior patches because the same source measure has positive Lebesgue reference mass there. A cell interior is connected. The all-chart lower-face nullity and local finiteness then give the full formula, finite on every compact source support, with no lower-dimensional residual. CLD 4.5.2 permits these per-top-cell constants to define a G-locally constant calibration; it does not require ordinary scalar agreement across adjacent cells.

This independently checks the content accepted by the older R report. The formula itself is proved under its stated analytic hypotheses; it is not an extra conjectural hypothesis generated by the absence of a production receipt.

## 2. Two qualifications that must survive import

First, CLD 7.5.1 literally starts with local affine separation. CLD 6.2.3 distinguishes this from differential separation, and 15.2.4 proves the latter. This review imports only the displayed description identity and the separately constructed nonnegative G-calibration. It does not invoke later results requiring the stronger adjective or declare a source erratum. Future exposition should say “the displayed description identity” rather than asserting every literal hypothesis of Definition 7.5.1 has been verified.

Second, in the R proof's source-recovery paragraph choose the auxiliary projection from the ambient Euclidean ball to its cell plane orthogonally. Then pi(O) is contained in Q, and `a composed with pi` is defined throughout the stated ordinary neighborhood. The frozen instruction to choose an affine projection permits that choice. This is a nonblocking choice clarification, not a new lemma or required alteration of frozen bytes.

## 3. R really applies on C's necessary domains

The original X in C is smooth projective over the original DVR fraction field. Its analytification and every ordinary open under consideration are good, separated, boundaryless and pure of dimension n. Restricting T to an ordinary open preserves positivity and both closedness conditions. What is not automatic for arbitrary opens is global paracompactness, so the following domain bookkeeping is essential.

| Domain used in C or its local inputs | Paracompactness and moment check | R use |
| --- | --- | --- |
| Rational-moment chart for one compact-test summand, C Section 9 | Choose `{chi>0}` with chi compactly supported and positive near the point. The compact superlevels `{chi>=1/j}` exhaust it. It is locally compact Hausdorff, hence sigma-compact and paracompact. Rational units are actual analytic units there. | Apply the proved R formula on this whole ordinary chart. |
| Positive part of a maximal-point tube, C Section 7 | It is the **full** `q^-1(Omega)` for a nonempty open convex Omega. L's proper q and a compact exhaustion of Omega give a compact exhaustion of the whole source. | Apply R to the actual n-coordinate moment on that entire ordinary source. |
| O's shallow collar, used by B/Q | It is the full inverse image of a connected normal box times `(0,delta)` under the actual punctured-tube q. Restricted properness gives the same exhaustion. When the residual exponent is zero, w=0 is excluded in precisely this Q domain, not by pretending the larger tube is punctured. | Apply R on the actual collar, not on a chosen sheet or a compact domain with boundary. |
| Small endpoint test-support neighborhood H | R is already on its eligible ambient rational-moment or coordinate domain. The compactly supported multiplier is extended by zero inside that ambient ordinary domain. H need not carry a new global cell decomposition. One may also shrink to another `{chi>0}` domain. | Use the ambient displayed formula on the identical compact test. |
| Arbitrary W or an arbitrary given U not assumed paracompact | No global compact-cell decomposition is inferred. C's pairwise claim for an already given presentation retains that presentation's hypotheses. The all-test proof uses the smaller eligible domains above. | A global R statement on such a U is neither supplied nor needed. |

A locally compact Hausdorff sigma-compact space is paracompact; no countability assumption on the residue field or second-countability assumption on the entire analytification is used. The compact exhaustions of proper inverse-image domains can be chosen with interiors covering the source. The actual whole-tube identification comes before the application of L and Q, so this exhaustion is about the real source, not the skeleton alone.

Ordinary moment descriptions of arbitrary forms are provided by CLD 15.1.1(b), not merely its G-local clause (a). Rational replacement and compact ordinary cutoffs in C Section 9 preserve those ordinary domains. Therefore every summand in the final compact-test argument has a proved R instance. No claim that all of W is paracompact is necessary.

## 4. The skeleton in R is the one used by L and Q

For the actual n-coordinate moment g on a boundaryless coordinate domain, write q for its tropicalization. The exact primary bridge is

`Sigma_q^(n) = Sigma_g^(n) = Sigma_g = g^-1(S(G_m,K^n))`.

CLD 12.8.3 identifies maximal variation with the full-dimensional characteristic part. Corollary 12.8.4 identifies that part with the whole characteristic skeleton on a boundaryless source. For an n-coordinate moment, 12.9.3--12.9.4 identify the characteristic skeleton with the inverse image of the closed torus Gauss skeleton. Thus it is a closed source subset and not an unrelated skeletal presentation. Boundarylessness is important; the source itself gives a boundary example where the two sets differ.

CLD 14.1.4(b) makes cells of a decomposition into moment cells convenient on a boundaryless source. Proposition 14.2.2 then makes local finite degree constant on a convenient top-cell interior. The dense independent-radius single-Gauss-source argument in L Section 6 fixes that degree at the omitted multiplicity m. The finite unramified coefficient extension retains the unique Gauss lift by 12.1.8(b), and 14.4.3 gives the full canonical factor `[K_p:K]=[kappa(p):k]`. The canonical source coefficient is therefore md.

This is a scalar-extension fact about the torus and the geometric finite map, not about extending an unknown current. It does not assert uniqueness of ordinary analytic sheets at every radius. Properness and the closed skeleton make only finitely many cells relevant over a compact target ball; avoiding their face images permits the identical compact test used to identify one cell's coefficient. Q then uses the proved R formula to pass from those cell constants to arbitrary compact source multipliers. None of this identifies the skeleton of a general m-coordinate moment with the coordinate skeleton; C supplies its separate endpoint form comparison for that purpose.

## 5. The dependency graph is acyclic at the level actually used

The graph must be split by clauses. Treating “L,” “V” or “B” as indivisible packages conceals which conclusions need R and can suggest a spurious cycle. The relevant order is:

1. Primary CLD/ordinary distribution theory proves **R's displayed formula**. No L, V, O, Q, A, B, C or coefficient-propagation theorem occurs in its proof.
2. Direct Banach division, finite analytic geometry and CLD canonical degree prove **L Sections 2--6**: finite projection, properness, domain properties, aggregate target constant, canonical degree and independent-radius Gauss uniqueness. R first enters **L Section 7**, a later optional source interpretation. Neither O nor Q is an input to L.
3. Regular SNC local algebra, henselian unramified lifting, formal metrics and the special-formal generic-fibre theorem prove **V Sections 3--4's model geometry**. The primary Berkovich Proposition 1.3 identifies the entire completion generic fibre with the tube. V's later whole-tube current theorem and its R-dependent source interpretation are not imported into O.
4. **O** uses that actual-model geometry and **L Sections 2--5**, then gives its own ordinary-W collar containment, restricted target constant and compact principal-divisor calculation. O uses neither R nor L Section 7 nor Q. Its finite coefficient functional is therefore available before any source-cell interpretation.
5. **Q** uses **L Sections 2--6 plus R** on the actual proper target-open restriction. It redoes the aggregate target-current calculation on that domain. Q's final residual-functional illustration is explicitly conditional on an independently supplied functional; it is not used to prove O.
6. **A/B geometry** uses primary model/ample-cut facts and the actual vertical augmentations, independently of R. **B's current comparison** combines that geometry with O, Q and the canonical degrees. It is downstream of R, not an input to R.
7. **C's endpoint geometry** uses BFJ/model geometry; its chamber connection uses A/B geometry. **C's coefficient comparison** then uses the downstream B/O/Q results and the now-proved R instances. **C's compact-test conclusion** uses those comparisons and ordinary rational replacement/partitions.

`DEPENDENCY_GRAPH.json` records this directed graph, and the checker verifies a topological order. That mechanical check alone is not mathematical evidence: the preceding clause reads are why its arrows are legitimate. Audit reports are evidence about these arguments, never nodes that replace a mathematical premise. In particular no arrow returns from C's rigidity consequence to R, and no arrow returns from Q's hypothetical residual application to O.

## 6. Remaining obligations and exclusions

No unsupplied mathematical lemma was identified for the **R import and clause dependencies just reviewed**, once the actual eligible domains and exact existing research proofs are used. The two earlier audits of A/B and C remain frozen with their original conditional scope; this separate report supplies the additional R-proof review rather than rewriting history.

The following obligations remain distinct:

- A newly written qualified assembly must be frozen and reviewed as its own exact text. This report does not certify a draft not yet examined.
- Any assembly must retain original-K same-generic-X models, projectivity, smooth connected X, residue characteristic zero, n>=2 for O, nonempty ordinary W, whole proper residual curves, independent normal points, and the full-source/support and degree normalizations. These are scope constraints, not permission to infer a broader theorem.
- Do not upgrade differential separation to local affine separation, or claim a global R decomposition on an arbitrary nonparacompact U/W. The displayed formula on the constructed paracompact domains suffices.
- Production Rethlas verification, editorial integration, novelty/priority determination and open-item retirement are separate processes and are not performed or authorized here. Their absence is not counted as a mathematical defect in the displayed R argument.
- No conclusion is supplied for arbitrary nonalgebraizable or nonprojective spaces, other value groups, residue-positive-characteristic model existence, higher bidegrees, or the general envelope problem. This is not a full-scope P21.3 audit.

## Primary-source record

The main primary text is CLD, [arXiv:1204.6277v2, 25 July 2025](https://arxiv.org/abs/1204.6277v2). Its exact local text is `/private/tmp/CLD25.txt`, 2150944 bytes, SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`. The official version/date was independently confirmed. The directly read interfaces include 2.2.8--2.2.15; 3.2.8; 4.5.2; 5.2.1--5.2.5; 5.3.1--5.3.6; 6.2.1--6.2.6; 7.1.6--7.1.11; 7.2.8--7.2.11; 7.5.1--7.5.4; 12.1.6--12.1.8; 12.8.3--12.8.5; 12.9.1--12.9.5; 14.1.4--14.1.5; 14.2.2; 14.4.3; 14.5.1--14.5.3; 15.1.1; 15.2.2--15.2.9; 15.7.1; and 16.8.3--16.8.5, including the relevant proofs.

The geometry predecessor was checked against Berkovich, [*Vanishing cycles for formal schemes II*, Section 1, Proposition 1.3](https://www.wisdom.weizmann.ac.il/~vova/Inven_1996_125_formalII.pdf), original-DVR scope and special-formal generic-fibre construction. No current assertion or alteration from its later cohomological sections is imported. No local byte hash is invented for this web source, and no PDF visual QA is claimed.

All writes for this audit are confined to this fresh directory. Any later correction must be a sibling or addendum, preserving these final report bytes.
