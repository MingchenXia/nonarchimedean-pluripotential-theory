# Independent exact-final audit: qualified scalar assembly and ordinary-local extension

Date: 1 September 2026. Reviewer: `/root/p213_general_propagation_fresh_audit`.

## 1. Verdict and the exact boundary of this review

**PASS, in the explicitly stated mathematical scope.** I find no substantive gap in the frozen qualified assembly, including its reconstructed displayed source formula, the projective combination, the new nonprojective algebraic and ordinary-local analytic extensions, and its bidegree-zero Bedford--Taylor consequence. No post-freeze mathematical correction is required for that scope. Section 10 below separates optional wording/citation improvements from mathematical findings.

The accepted scope is: a complete discretely valued field K with residue characteristic zero; a good separated strict boundaryless quasi-smooth K-analytic space of pure dimension n>=2; a positive ordinary CLD current of bidegree (0,0), separately d'- and d''-closed, on a nonempty connected ordinary open W. Within this scope the supplied argument establishes a unique finite c>=0 with T=c delta_W. It also establishes the stated equal-curvature continuous-psh consequence for bidegree-zero T on arbitrary ordinary subopens.

This is not a production Rethlas result, an acceptance of the full P21.3 question, or a priority/novelty judgment. It does not cover positive-bidegree currents, singular analytic spaces, all complete valued fields, or a blanket statement without the stated hypotheses. No external production, book, or git operation was performed.

The target is the complete frozen file

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_qualified_scalar_assembly_research_20260901/RESEARCH_NOTE.md`

with SHA256 `5809b99def2c16becb716eb2eb7c24382a8a31655b9b43902804e585cb53bb5c`, 28664 bytes. The verdict is on these bytes, not an earlier provisional reading or an imagined repaired manuscript.

I did not author the candidate or its constituent research proofs. I previously authored the independent A/B, C, and displayed-R-import reviews in this same delegated audit sequence. That prior familiarity is disclosed, not treated as a second independent reviewer. Those three reports remain frozen. In particular, the conditional C report is not silently upgraded or edited: the present new review assesses the newly supplied assembly and extensions. A PASS label from an earlier report is not a mathematical premise here.

## 2. Exact identities and what was actually checked

The target's complete note and complete source ledger were reread after receipt of the final freeze message. The frozen top-level identities are:

| File | Bytes | SHA256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 28664 | 5809b99def2c16becb716eb2eb7c24382a8a31655b9b43902804e585cb53bb5c |
| SOURCE_LEDGER.md | 5402 | e7e80db8edd6233b00b75840fd9af6a57b4d8c4e6a5a419aa4fae4ad7c5954d0 |
| MANIFEST.json | 9857 | 535c616d5bddd8f86fb6431ca050af294ca58b09493c2ac7aedc37a4dd33fdb2 |
| SHA256SUMS | 5278 | 752b86c361090faf872eeb044ba55550b7e7b3450c7f631e0f93e984f8c49762 |
| INPUT_PINS.json | 8969 | 4daa970bfbd072ea68a6e075f87dbe9aa1524b557f6bd0fc801739d24fbefeb5 |

The independent read-only checker in this directory verifies seven directly pinned files, all 32 target input pins, eight manifests containing 142 entries, and all 38 target checksum lines. All match. It also checks the 22-node combined dependency graph for missing nodes, duplicate nodes, and cycles; none are present. These are identity and graph-syntax results only. The mathematical reasons for accepting the edges are below and in the frozen clause-level R-import review.

The 142-entry count includes the target manifest and the seven prerequisite manifests for R's old audit, L, O, Q, A, B, and C. Identity checks on files recorded there as excluded cross-refinement/remaining-gap/older-access material do not import those assertions. No author freeze or validation script was executed. My checker does not write any file. Authored material was written only in this fresh audit directory with apply_patch.

The complete R statement/proof, prior R audit and ledger, L/O/Q proofs and independent reports, and A/B/C proofs were substantively examined in the preceding audit stages, not merely hashed. The current review rechecks the new manuscript's actual uses and checks the two new extension stages directly. It does not purport to reprove the external resolution or algebraization theorems.

## 3. Primary sources for the new stages

I checked the exact versioned primary references online, including the surrounding hypotheses rather than only search snippets:

- [Temkin, math/0703678v2](https://arxiv.org/pdf/math/0703678v2), 11 September 2008: the introduction's resolution convention and Theorem 1.1; Section 3.3 notation; the complete statement/proof of Proposition 3.3.1 and its 3.3.2 formal-smoothness/Jacobian interface. Resolution preserves the regular locus. The algebraization proof gives an actual pi-adic completion of a finite type algebra over the henselized valuation ring of the chosen dense subfield. The manuscript uses L=K and hence O^h=R, not a smaller subfield or an extension of K.
- [Temkin, 1010.2235v2](https://arxiv.org/pdf/1010.2235v2), 16 December 2011: 3.4.2.1 and 3.4.2.3; 4.2.4.1--4.2.4.3; 4.2.5.4--5; 4.3.2.2; 5.1.1, 5.1.2.1 and 5.2.2.1. These identify inner presentations, relative domain interiors, boundaryless neighborhoods, smoothness compatibility, analytification and affine formal generic fibres. The proof must still check the actual domain and both ordinary interiors; those are the manuscript-specific checks in Section 7 of this report.

These online references are not represented as locally downloaded or byte-pinned PDFs. The independent source check is separate from the exact local manuscript/premise identities. I also inspected Temkin's primary *Local Properties II* while testing the strict-neighborhood issue; no extra theorem from that paper is needed in the accepted dependency chain.

The CLD source remains the pinned 25 July 2025 text, SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`. The preceding R-import review directly checked its measure, support, all-chart nullity and characteristic-skeleton interfaces. BFJ remains the pinned 1201.0187v2 text, SHA256 `df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f`. Original-field Bertini, connectedness, actual blowups and path-connectedness were checked in the A/B and C stages. No field extension is inserted when these stages are combined.

## 4. Section 3: the displayed formula is supplied, not merely assumed

The new reconstruction passes the substantive checks from the separate R-import review. In particular:

1. Its source domain V is explicitly good, separated, paracompact and boundaryless, pure n-dimensional, and carries the actual moment F on all of V. It uses local differential separation for ordinary cutoffs and smooth density. It does not claim local affine separation or invoke the stronger skeletal-current terminology as a black box.
2. Positivity yields measures for top-form coefficients. The argument does not incorrectly identify the current T itself with one scalar Radon measure on V. Symmetrization and differences of positive coefficient forms are legitimate; it does not assert that strongly positive forms span every intermediate symmetric bidegree.
3. Strong support confines an F-based top coefficient to the maximal-variation skeleton. This is a statement about the actual F-based form and its allowed wedges/differentials, not a simultaneous support assertion for unrelated charts.
4. The lower-face set is tested against every compact analytic domain and every G-chart. Compact PL intersection and PL maps give dimension <n for every required image. Thus the precise tropical-negligibility hypothesis of CLD 16.8.3--5 is met. Applying the positive-current theorem and then the positive coefficient decompositions gives total-variation nullity for signed coefficients; it does not apply that theorem directly to an arbitrary signed current.
5. Source localization does not falsely assert that chi T is closed. The compact derivative-support set is disjoint from the chosen target ball on the skeleton; the d chi term vanishes as a form everywhere, by ordinary support and strong support together. Only the pushed current on that ball is declared closed.
6. The chosen affine projection is explicitly orthogonal for the chosen Euclidean ball. Consequently pi(O) is contained in Q, so all composed coefficient functions are defined. Tangential factorization is proved by vanishing of restricted forms, excluding normal derivative distributions rather than deducing their absence from set-theoretic support alone.
7. Euclidean distributional zero derivatives give one finite nonnegative Lebesgue density on each connected Q. The source skeleton over Q is actually mapped homeomorphically onto Q, and chi=1 there. Pullback of the equality of Radon measures therefore recovers the individual source measure and allows arbitrary compact source multipliers rho. No requirement that rho factor through F is hidden in this step.
8. Local constants glue with a fixed cell coordinate convention; locally finite compact cells and lower-face nullity give the full formula on all compact tests. The canonical calibration uses the same cells and coordinates after convenient refinement. Section 3 itself does not identify ratios on different cells.

This supplies precisely the R conclusion used by Q and C. There is no remaining mathematical assumption that the displayed R formula might be unavailable merely because an older packet has not passed a production gate. Equally, there is no import of the unsupported stronger separation adjective.

## 5. Section 4: the projective combination and its source-domain checks

The new assembly discharges C's displayed-R premise without changing C's proof or its frozen audit. The remaining hypotheses match the actual earlier clauses.

The essential analytic domains are the complete model tubes, O's complete collar pieces, Q's full connected target-open inverse images, and the cutoff-positive local chart domains used for compact test descriptions. They are ordinary opens of the same smooth analytification. The finite projection supplies properness of the complete coordinate moment, including after target restriction. Pulling back a compact exhaustion gives sigma-compact locally compact Hausdorff domains and therefore paracompactness. The independent-point support test in C uses a smaller ordinary support neighborhood inside such an eligible ambient domain; it does not demand a fresh global representation on every arbitrary small open.

For arbitrary compact test descriptions, the domains {chi>0} are unions of the compact sets {chi>=1/j}. This provides the missing global hypothesis of R locally where R is actually applied. Nothing requires the given W or every ordinary subopen of W to be paracompact. The finite compact-source partition is available using the ordinary smooth cutoffs. It is not replaced by an infinite G-cover argument for currents.

The required characteristic skeleton agrees with the maximal-variation skeleton for the actual n-coordinate tube moment. This is the CLD 12.8--12.9 interface checked in the R-import review, using the actual analytic torus map and full-dimensional boundaryless source. It is not asserted for an arbitrary lower-rank moment. L's independent Gauss point supplies a unique actual source point and the residue/value-group degree computation needed by Q, rather than merely a count of geometric sheets.

The scalar factors are kept consistent. For an omitted normal indexed 0, the canonical coefficient is N_0 d_p and Q's ratio is b_p/(N_0 d_p). O's residual functional on the entire proper curve gives lambda(p)=c_C d_p. With that omitted normal fixed, the incident ratios are c_C/N_0. Changing the omitted normal changes the current coefficient and canonical coefficient by the same absolute determinant factor N_j/N_0. The source top form in C has two differential blocks, hence its affine pullback uses the squared determinant; this is distinct from the single determinant in transformed Lebesgue coefficient measures. The manuscript does not conflate these two changes.

A uses a determined model function, so the positive set is fully saturated for the actual retraction. Its vertical blowups keep the generic fibre identified with X. B's positive-vertex retraction/tree argument permits a non-pure starting skeleton and supplies controlled new top chambers; it does not assume that the old top-cell adjacency graph is connected. The complete old endpoint tubes and proper residual curves survive the chosen cuts/blowups. The component-indexing qualification from the A/B review is explicitly retained: components of each restricted divisor, not connected components of their entire crossing union.

C captures the chosen original source point on a common SNC model of this same X by the independent rational coordinate values and globally defined vertical-ideal model functions. Its affine agreement with the original moment is local near the endpoint only. The propagation path needs saturation inside W, not equality of the two moments all along the path. The identical compact positive source form then compares the two actual currents; positive canonical mass permits division. The chamber chain compares any two endpoint ratios, and the rational replacement/finite compact-test argument covers analytic-unit charts as well.

Finally, the reference positive test is obtained inside any nonempty W by the same augmentation and positive tube calibration. Thus the common ratio is finite and unique, including the possibility c=0. No geometric connectedness of X or algebraic closure of k is inserted. This verifies the projective statement as a combination of the supplied proofs, not as an inference from a list of earlier PASS labels.

The clause graph remains acyclic: R and L's needed core precede Q; O uses the geometric L clauses and actual model-tube geometry, not R or Q or the older whole-tube current theorem; B's current step is downstream from O and Q; C is downstream from B and Q. The new local extensions only consume the projective conclusion. L Section 7 is not used to justify O or Q, and no whole-current conclusion is fed back into its own representation or comparison proof.

## 6. Section 5: nonprojective smooth algebraic ambient spaces

This is a valid local reduction, not a claim that every nonquasiprojective smooth variety admits a global projective compactification.

At an analytic point one first chooses an affine algebraic neighborhood of its underlying scheme point. A smooth finite type scheme is regular; its irreducible components are disjoint and open-and-closed. The component containing the point can therefore be retained while keeping an affine integral neighborhood U. This uses connectedness/integrality over K only, not geometric integrality.

The projective closure of the closed embedding U in affine space has intersection with that affine space equal to U. It is integral and U lies in its regular locus. Applying the stated resolution leaves this entire U unchanged. The resulting morphism is projective, and the total space/component containing U is projective over K. Characteristic zero makes K perfect, so its regular finite type structure is smooth. Thus the earlier projective conclusion applies to precisely the needed ambient component.

One takes a connected ordinary H inside W intersect U^an. The chosen open immersion identifies H, including its ordinary forms and canonical integration, with the same ordinary open in the resolved projective analytification. Restriction of T to H is legitimate. There is no extension of T over the compactification boundary and no pullback of a general current across a noninvertible birational morphism. The resolution is used only to furnish an ambient space, through an isomorphism over U.

On a nonempty overlap, a still smaller ordinary neighborhood has a compact positive test with nonzero canonical integral by the already established projective result. The equality (c_1-c_2) delta=0 evaluated on that one test forces c_1=c_2. The resulting scalar function is locally constant and hence constant on a connected W. This gluing does not need W to be globally paracompact: equality of currents is local, and each compact test admits a finite subordinate smooth decomposition. There is no requirement that the compactifications at two points coincide.

The title's phrase “algebraic spaces” is read in the body’s expressly stated scope, smooth separated K-varieties/schemes. The argument does not establish an additional statement about general Artin algebraic spaces lacking affine Zariski neighborhoods. This terminology is addressed separately in Section 10 and does not affect the theorem in Section 1.

## 7. Section 6: actual same-K ordinary-local algebraization

This is the principal new geometric bridge. The following checks are needed in order; all are met by the frozen argument.

### 7.1. A strict affinoid neighborhood with a genuine interior point

The first paragraph at line 173 is valid with “neighborhood” in the ordinary topology. Boundarylessness may be applied after ordinary restriction to W. The interior characterization gives an affinoid neighborhood D_0 with x in its intrinsic interior. If strictness of that particular choice is questioned, the inner presentation directly resolves it: write D_0 as a quotient of a polydisc algebra with generators f_i and radii r_i for which |f_i(x)|<r_i. Choose intermediate s_i in the divisible closure of |K*| with |f_i(x)|<s_i<r_i. This is possible because K is nontrivially valued. Restrict to the Weierstrass domain |f_i|<=s_i. Its algebra is a quotient of the polydisc algebra of radii s_i, hence strictly K-affinoid; the strict inequalities at x make it an ordinary neighborhood of x, and the same presentation makes x intrinsic interior. The domain remains inside W. No extension of K is needed to call a polydisc with radii in the divisible value group strict.

This verifies the specific standard-neighborhood assertion in the manuscript. It is not an alternative algebraization construction or an assumption that all affinoid subdomains of a strict space are strict. The explicit inner-presentation definition gives the check even if one does not rely on a shorthand “good and strict” convention.

### 7.2. The formal model meets the algebraization hypotheses

For a strict presentation B=K{T}/J, the contraction J intersect R{T} gives a topologically finite type R-algebra C. The ring R{T} is noetherian and complete, its quotient is complete, and contraction ensures that C has no pi-torsion. Inverting pi recovers B: denominators of the coefficients of a restricted convergent series are uniformly bounded, so K{T}=R{T}[1/pi], and contraction/localization restores J.

An analytic domain in the quasi-smooth Z is quasi-smooth. Its strict affinoid algebra B is regular; equivalently, the generic scheme Spec(C[1/pi]) is regular. This is exactly the rig-regular hypothesis of the formal algebraization input. No assertion that C or its special fibre is regular, semistable, reduced, or SNC is made or needed.

The field in the manuscript is already complete discretely valued and has characteristic zero. Taking the dense subfield L to be K gives O=R and O^h=R. In Proposition 3.3.1's proof, the algebra before the optional descent from O^h is enough: C is its pi-adic completion. This avoids confusing the general definition of algebraizability along some closed subscheme with the more specific completion required here. It also avoids an extension field, alteration, or a change of the original analytic domain D.

### 7.3. The algebraization really contains D as the asserted analytic domain

Let A be the finite type R-algebra so obtained and present it by R[T_1,...,T_s]/I. No flatness or global smoothness assumption on Spec A is silently added. Completion followed by inverting pi has the explicit algebra

    Ahat[1/pi] = K{T_1,...,T_s}/I K{T_1,...,T_s}.

Inside Y^an, for Y=Spec A[1/pi], intersect the algebraic closed subspace given by I with the closed unit polydisc. Its affinoid algebra is the displayed one. Consequently it is analytically isomorphic to the given D, with the displayed coordinate inequalities. This verifies an analytic-domain identification, including the sheaf, not a mere injection of underlying points. Possible irrelevant components or singularities of Y outside this domain do not matter.

The original map D to Z and the map D to Y^an are both actual analytic-domain embeddings over K. They are not finite maps whose degrees would need to be divided out, and they do not supply a pullback theory for arbitrary currents. The argument will restrict to a common ordinary open before transporting T.

### 7.4. Both ordinary interiors are present

This is the essential check at lines 179--183. Intrinsic Int(D) is preserved under the isomorphism of D with its algebraized domain. Because both Z and Y^an are boundaryless, relative interior of D in either ambient space is its intrinsic interior. The domain-interior theorem then makes that set ordinary open in the respective ambient topology.

Thus a small open subset containing x inside this common interior is ordinary open in Z and maps isomorphically onto an ordinary open subset of Y^an. If one starts with separately chosen ordinary neighborhoods on the two sides, their preimages can be intersected inside Int(D); the intersection is still an ordinary neighborhood of x on both sides. There is no inference that the whole closed affinoid D is open in either ambient space. Nor does formal Zariski openness alone supply this conclusion.

This is precisely the same-K ordinary-germ bridge required for the current argument. A G-domain without the interior step would be insufficient. Here the step is present and its hypotheses are met.

### 7.5. Restriction to a smooth algebraic ambient locus and gluing

The common ordinary open H is boundaryless and quasi-smooth, so it is smooth. The algebraic and analytic nonsmooth loci agree under analytification: with a finite polynomial presentation the same Jacobian smoothness condition defines their loci. Thus H is contained in (Y_sm)^an. This is a local smooth-locus assertion, not an inference that all of Y is smooth from smoothness on one affinoid domain. The manuscript's additional Jacobian explanation is important here; a bare citation of global preservation/reflection would leave the local application less explicit.

The dimension of a smooth component is locally constant. The dimension-n open-and-closed part of Y_sm contains the relevant H because H is an ordinary open in the pure n-dimensional Z. Passing to it is permissible. Connected shrinking is supplied by the local path-connectedness of these smooth ordinary germs. Section 5 now applies to the actual given current on H.

An analytic isomorphism preserves ordinary forms, their differentials, positivity, compact supports and canonical integration. Therefore the scalar identity on H transports to a scalar identity near the original x with no multiplicity or residue-degree correction. Those factors occurred in finite projections earlier, not in this isomorphism. Nonempty overlaps have positive compact tests, so the scalar descriptions agree and glue as in Section 6 of this report.

The conclusion does not assume a global algebraization, a global projective compactification, a countable exhaustion of Z, or global paracompactness. Each algebraic ambient variety may vary with x. The compatibility comes from the uniquely determined scalar on ordinary overlaps.

## 8. Section 7: the bidegree-zero consequence

On an ordinary neighborhood where T=c delta, multiplication by a continuous u is the ordinary coefficient-measure multiplication and gives uT=c[u]. This follows for every compact test by equality of the coefficient measures, not by differentiating u as though it were ordinary smooth. The same statement holds for v. Since c is a constant on that neighborhood, both current differentials commute with multiplication by c. Equal curvature currents therefore give

    d'd''(uT)=c d'd''[u]=c d'd''[v]=d'd''(vT).

The identity is local, so it holds on arbitrary ordinary U even if U is disconnected and its components have different scalar values. It does not require u-v to be psh, smooth, or approximable by a special smooth family. For the continuous psh inputs in the statement this is the claimed single-step Bedford--Taylor product. The argument is particular to bidegree-zero T; it supplies no comparison for positive-bidegree currents.

## 9. Hostile tests of possible hidden scope changes

I specifically checked the following failure modes and found that the frozen argument avoids them:

- **Non-algebraically closed residue field:** the projective/model input keeps closed-point degrees d_p and original-k ample cuts; the new steps neither split points nor replace K by an algebraic closure.
- **Connected versus geometrically connected:** the compactification component is smooth integral over K, which is sufficient for the exact BFJ/projective scope. Geometric integrality or geometric connectedness is not introduced.
- **Model versus generic birational modification:** same-X endpoint propagation occurs before the new local compactifications. In Section 5 the resolution is an isomorphism on the entire affine U carrying the current. In Section 6 the bridge is an analytic isomorphism on ordinary opens. These are distinct valid uses, not a reintroduction of the old unsupported generic-modification anchor.
- **Ordinary versus G-open:** the initial compact test domains, full tube/collar domains and final common-interior germs all have the required ordinary openness. The formal generic-fibre domain is not by itself called ordinary open.
- **Paracompactness:** only eligible constructed chart domains receive R. The final W need not be paracompact; finite compact-support localization suffices for the current identity and gluing.
- **Whole proper residual curve versus a punctured piece:** O is used through the full proper-curve functional preserved by A/B. No rational equivalence calculation on an arbitrary punctured curve is substituted.
- **Normalization:** the omitted-normal and residue-degree factors, the determinant in coefficient measures, and the determinant squared in the identical source top form all occur in their correct places. Transport through the final isomorphism contributes no new factor.
- **Representation versus ratio propagation:** the reconstructed R establishes the actual source formula and lower-face nullity independently. Coefficient ratios are propagated by the model/current chain, not assumed in R or in a cross-refinement theorem.

## 10. Findings, optional clarifications, and remaining obligations

### Required mathematical corrections

None found in the exact stated scope. In particular, the ordinary-local algebraic-germ bridge is supplied, not an outstanding alteration/descent premise. The displayed R formula is mathematically available here; its absence from a production workflow is not a mathematical hole in this assembly.

### Optional clarifications, not conditions of PASS

1. **Section 5 title, line 161:** “algebraic spaces” could be read in the technical Artin sense. The first sentence and the proof explicitly treat smooth separated K-varieties with affine Zariski neighborhoods. A future editorial version could title this “smooth algebraic varieties” or “smooth algebraic schemes.” This audit does not extend the argument to general algebraic spaces; no such extension is needed by Section 6, where Y is affine.
2. **Section 6 first paragraph, line 173:** a future exposition could cite the inner-presentation definition 3.4.2.1 in addition to the cited interior facts, making the strict-affinoid-neighborhood check immediately visible. Section 7.1 of this audit verifies that ordinary elementary consequence. This is a citation/explication improvement, not an unproved hypothesis or a required change to frozen bytes.

Any optional change belongs in a sibling or addendum. No input was changed during this review.

### Remaining obligations outside this verdict

The required production Rethlas gate remains unmet and was not attempted. The complete P21.3 scope remains unestablished: positive-bidegree currents, singular analytic spaces, and field hypotheses outside the complete-DVR residue-characteristic-zero setting require separate arguments. This review makes no independent claim for n=1 from this n>=2 assembly, although separate lower-dimensional results may exist. It also does not prove a general envelope theorem, identify all zero-curvature continuous functions as ordinary smooth, or establish equivalence of all psh definitions.

Within the exact scope reviewed above, I do not identify an additional unsupplied mathematical lemma. The external standard theorems are explicit and their relevant hypotheses were checked. The distinction between this mathematical review and production acceptance is retained throughout.

## 11. Reproducibility and freeze convention

`verify.mjs` is a read-only recomputation of exact identities and the dependency graph. Its successful results are: 7 directly pinned files; 32 source input pins; 8 manifests / 142 entries; 38 target checksum lines; 22 graph nodes, acyclic. It neither reads a PASS label as a proof nor exercises a production validator.

The audit package consists of this report, REVIEWED_INPUTS.json, DEPENDENCY_EXTENSIONS.json, verify.mjs, and SHA256SUMS. Once the checksum list is finalized and reported to the parent, these bytes are frozen. Later corrections require a separate sibling or addendum. Earlier audit packages and all research inputs remain untouched.
