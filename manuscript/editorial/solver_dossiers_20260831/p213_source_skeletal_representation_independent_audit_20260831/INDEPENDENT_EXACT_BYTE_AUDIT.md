# Independent exact-byte audit: source-skeletal representation

Date: 2026-08-31. Auditor: /root/p081_weighted_repair_fresh.

## Verdict and gate

No substantive mathematical gap was found in the full displayed source-cell representation theorem, including arbitrary compactly supported smooth source multipliers, under its stated hypotheses. The lower-face nullity, source-cutoff cancellation, and recovery of an individual source measure are justified; none requires equality of canonical-normalized coefficients across different cells.

There is one source-terminology qualification, recorded in §9 below: the literal opening of CLD Definition 7.5.1 assumes local *affine* separation, whereas the analytic hypotheses here give local *differential* separation. This audit accepts the directly proved description formula and the nonnegative G-locally constant calibration, not an unproved implication between those two separation notions. No argument in the displayed representation proof depends on that stronger separation adjective.

This is a fresh independent mathematical audit of the two specified files, not production acceptance, a live integration authorization, or an audit of the separate cross-refinement packet. All production gates remain unchanged. No candidate, earlier audit, live manuscript, or inventory file was edited.

## 1. Exact object and independence

The candidate is:

- statement.tex: 2211 bytes; SHA-256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a.
- proof.tex: 11486 bytes; SHA-256 27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a.

Both are in the sibling p213_skeletal_packets_20260831/skeletal_representation directory. I read both completely and checked their primary-source interfaces independently of earlier verdict labels.

I did not author this packet. The colleague /root/p213_skeletal_hostile identifies the author as the former /root/p213_rigidity_attempt, after it received that colleague's earlier hostile-audit findings. This attribution comes from the colleague's provenance message, not from a reconstructed git history. I previously read the statement as an assumed interface in a separate torsor audit; I explicitly excluded this proof from that earlier mathematical verdict. My later mixed-branch construction does not use this representation theorem. Neither that prior familiarity, the parent's preliminary review, nor the older audit labels is used as acceptance evidence here.

There is no completed ordinary author manifest in the candidate directory. Its FROZEN_PAUSED.md explicitly records that the packet was paused before the source ledger and ordinary manifest were finished. Its five SHA records all match. The cross_refinement statement/proof and remaining_gap.tex were checked for identity only and are not included in this mathematical verdict.

The primary source is Chambert-Loir–Ducros, the 25 July 2025 version, with the exact local PDF and extracted-text hashes in SOURCE_LEDGER.md and MANIFEST.json. This is not an audit against an older numbering of the manuscript.

## 2. Exact scope

The proof handles a complete nontrivially valued non-Archimedean field K and a good, separated, paracompact, boundaryless K-analytic space V, pure of dimension n ≥ 1. The chart F is an actual ordinary tropical chart on all of the ordinary open space V. The current is an ordinary positive CLD current of bidegree (0,0), hence bidimension (n,n), and both d'T and d''T vanish.

There is no smoothness, normality, irreducibility, algebraic closedness, discrete valuation, residue-characteristic, or semistable-model hypothesis. The source results being used apply to this analytic scope. In particular, the argument does not convert an ordinary K-current into a current over another field. Boundarylessness and nontrivial valuation are actually used at CLD Theorem 16.8.5 and may not simply be dropped.

The conclusion is a separate nonnegative constant b_C for each top-dimensional source cell, relative to its chosen affine coordinates. It is not a claim that b_C divided by the canonical analytic calibration is a single constant on V, that arbitrary charts have already been linked by a finite known family, or that P21.3 has been solved.

## 3. Compact cells and the full all-chart negligibility quantifier

Proof lines 12–20 are justified as follows. The analytic structure is a G-tropical vertebrated space by CLD §12.9.5, and a pure-dimensional analytic space has the required tropical-space structure by Theorem 15.7.1. Proposition 5.2.5 makes the maximal-variation locus S closed and pure of dimension n; F restricts to a piecewise immersion. Since S is closed in the paracompact Hausdorff space V, it is paracompact.

Remark 2.2.12 supplies a locally finite cover by compact PL chart domains on which the piecewise immersion is an affine embedding. Proposition 2.2.15 supplies a compact-cell decomposition subordinate to such a cover and adapted to the finitely many local affine functions. Thus every cell is contained in one of the injective chart domains and F is affine and injective on it. Compactness of the cells is not inferred from compactness of V, which was never assumed.

Let B be the union of the lower-dimensional cells. Local finiteness makes B closed in S and therefore in V. It is PL in S; Lemma 3.2.8(d) makes it a PL subset of the ambient G-tropical space. This ambient qualification is essential.

For every compact analytic domain W and every G-tropical chart H on W, Lemma 3.2.8(c) gives a compact PL structure on B ∩ W and says that each PL coordinate of H restricts to a PL function there. After a common finite subdivision its image is a finite union of polyhedra of dimension at most n−1. In particular, that image has n-dimensional Hausdorff measure zero. This verifies exactly the universal quantifier in Definition 16.8.3; checking only the image under the originally fixed F would not suffice.

Theorem 16.8.5 then applies with p=n to the original positive closed T on the boundaryless analytic space. It applies to arbitrary smooth top-degree coefficient forms, not merely to canonical volume forms. Thus every coefficient measure has zero total variation on B. A local positive decomposition also shows this explicitly: if μ=μ_+−μ_- with positive μ_± and both vanish on B, then |μ|≤μ_++μ_- vanishes there. Local nullity globalizes by the Radon property and finite coverings of compact subsets. No positivity theorem is applied to a signed current as though it were positive.

This part of the candidate passes the potentially decisive ALL G-tropical charts test.

## 4. Coefficient measures, positivity, and strong support

Proof lines 22–48 distinguish the current T from the coefficient measures μ_ω. The proof does not incorrectly declare an arbitrary degree-(0,0) current to be a scalar Radon measure on V.

For positive smooth top forms, the functional ρ ↦ ⟨T,ρω⟩ is positive on nonnegative smooth compactly supported functions. CLD Propositions 7.2.8–7.2.9 and §7.2.11, together with local differential separation and smooth density, yield the Radon measure. General coefficient forms are treated locally by positive differences and uniqueness.

Here “positive differences” must mean the positive cone, as written, and not a claim that the strongly positive ambient cone spans every symmetric (n,n)-form when the ambient tropical dimension exceeds n. CLD Proposition 1.2.13 explicitly supplies an interior positive reference form in the symmetric space; the strongly positive spanning assertion would be false in intermediate bidegrees. Since T is symmetric, only the symmetric part matters. On a fixed compact coefficient range, a sufficiently large multiple of a positive reference form bounds that part from above and below. This gives the needed local signed Radon measures and their order-zero bounds. Antisymmetric top-form components restrict to zero on the n-dimensional skeleton and do not create an omitted coefficient.

CLD §5.3.1, Lemma 5.3.4, and Proposition 5.3.6 provide three distinct facts used correctly here:

1. F-tropical forms with max(p,q)=n are strongly supported on S.
2. Strong support persists after multiplication/wedging by arbitrary smooth source forms and after differentiation.
3. Restriction to S detects vanishing of such strongly supported forms.

In particular, an F-tropical top form vanishes as a germ off S. Smooth density then makes its coefficient measure supported on S. This does not assert that T is supported on S for tests belonging to unrelated charts.

## 5. The source cutoff really eliminates its derivative error

Proof lines 76–127 use an ordinary open neighborhood of a point x in the interior of one top cell C. Lemma 2.2.8 implies C° is open in S, so V_x may be chosen with S ∩ V_x ⊂ C°. The map F is injective on that entire local source skeleton.

For the compactly supported cutoff χ, equal to 1 on W_0, the set
D = supp(d'χ) ∪ supp(d''χ)
is compact and does not contain x. Since all of D lies in V_x, injectivity on S ∩ V_x shows F(x) is not in F(D ∩ S). A sufficiently small ambient ball O centered at F(x) therefore avoids that compact image. It can simultaneously satisfy Q=O∩L_C ⊂ F(S∩W_0), because F is an affine homeomorphism on C.

The pushforward R=F_*(χT|V_x) exists because the multiplied current has compact support. The compact-support extension of the action in §7.1.10, and the pushforward construction in §7.1.11, suffice; the map F itself is not asserted proper. Equivalently, every target pullback is paired after the one fixed compact source cutoff, a continuous operation on test-form spaces.

For a target (n−1,n)-test β supported in O, the error d'χ∧F*β vanishes as a source form before pairing:

- outside D, its first factor has zero germ;
- outside S, the second factor has zero germ by the max(p,q)=n strong-support statement;
- on D∩S, F lands outside O, hence outside the compact target test support, and the second factor again has zero germ.

These three cases cover V_x. The same argument handles d''. This proves R is closed on O without asserting χT is closed everywhere. It neither requires a target cutoff whose inverse image is compact nor loses sheets by assuming F is globally injective.

## 6. Tangentiality and constant Euclidean coefficients

Proof lines 129–173 first show that the localized R depends only on restriction of an ambient (n,n)-form to Q⊂L_C. Indeed, if that restriction vanishes, its source pullback multiplied by χ is strongly supported on S and restricts to zero there. The strong-support detection theorem annihilates it as a form. This proves tangentiality, a stronger statement than ordinary support on L_C, and excludes normal coefficient or derivative distributions.

A compactly supported top form on Q can be extended to O by an affine projection and a transverse cutoff. A nonnegative scalar test times the interleaved positive coordinate volume form admits a strongly positive such extension. Consequently the factored functional is a positive Radon measure ν on Q.

Extending a coordinate-deleted primitive, applying d'R=0, and restricting back to L_C gives ν(∂_iφ)=0 for every compactly supported smooth φ and every i. Normal derivatives of the extension restrict to zero and cannot contribute. Convolution on relatively compact Euclidean balls therefore has zero gradient, hence is constant. Testing against a fixed unit-integral smooth function shows those constants converge; distributional convergence and overlapping balls give ν=b dt_1⋯dt_n with a finite b≥0 throughout connected Q.

The only convolution is on an ordinary Euclidean ball, not on a singular tropical support or on the analytic space.

## 7. Recovery of individual source measures and arbitrary multipliers

Proof lines 175–218 are essential and sound. Put θ=F*π*η and let μ_θ be its positive coefficient measure on V_x. It is supported on S∩V_x. The localized pushforward equality gives F_*(χμ_θ)|Q=b dt.

Let H=S∩V_x∩F^{-1}(Q). Every point of H has the same F-value as a point in S∩W_0, by the defining property of Q. Local injectivity forces those two source points to be identical. Thus H is contained in W_0, χ=1 on H, and F|H is a homeomorphism onto Q. Consequently the pushforward equality pulls back to an equality of source Radon measures on H. There are no other local source sheets left to sum.

For any F-tropical top form ω=F*α with α|Q=aη, strong-support detection yields ω=(a∘π∘F)θ on the corresponding ordinary source neighborhood. As noted in §9, π can and should be chosen orthogonal for the ambient ball, so the expression is defined throughout that neighborhood. The coefficient measure identity follows.

Since this is a source Radon-measure identity, it can be integrated against any continuous restriction ρ|H, in particular against every smooth compact source multiplier. There is no assertion that ρ factors through F on the whole analytic neighborhood, and no density assertion about target pullbacks on V is needed. Source injectivity is used only on H after coefficient-measure support has already been established.

Keeping the chosen affine coordinates fixed on L_C as x varies makes these locally defined reference measures agree on overlapping source patches. Positive Lebesgue mass on a nonempty open overlap forces the constants to agree. Connectedness of C° gives the unique b_C for that cell.

## 8. Global assembly and calibrations

The cell-side measure is Radon: locally only finitely many compact cells occur, and the smooth ambient coefficient is bounded on each relevant compact piece. It agrees with μ_ω on S\B, both measures vanish off S, and both give B zero total variation. Hence they agree everywhere.

The compact support of ρ meets only finitely many cells. If α was defined only near F(V), a target cutoff equal to 1 near F(supp ρ) reduces that single evaluation to a globally defined ambient form without changing either side.

CLD Example 4.5.2 explicitly shows that arbitrary constant volume calibrations on the top cells of such a decomposition glue to a G-locally constant calibration. The quotient by lower-dimensional data permits this gluing; no equality of numerical weights at an adjacent face is required. Zero coefficients are allowed in the nonnegative calibration. The interleaved positive volume convention matches the stated nonnegative b_C.

Thus the final integral identity has the content of CLD's source description formula. It is not a hidden proof of canonical-ratio propagation.

## 9. Source terminology and nonblocking presentation notes

### 9.1 Literal affine/differential separation distinction

The first sentence of CLD Definition 7.5.1, pp.172–173, says “locally affinely separated.” Section 6.2.3 distinguishes that condition from local differential separation, and Corollary 15.2.4 proves only the latter for the analytic spaces under consideration. This audit does not promote the latter to the former.

There is also an internal source variation: Example 7.5.2 states only local differential separation, while Example 7.5.3 describes the analytic integration-current situation without the stronger adjective. I do not declare any of these source sentences an erratum.

For the candidate, the directly proved formula is well-defined under its actual hypotheses, and the construction of its calibration is separately justified by §4.5. Nothing in the proof invokes a later skeletal-current theorem requiring the stronger affine hypothesis. The final words “in the sense of Definition 7.5.1” are therefore accepted as referring to the explicit description identity reproduced in the statement. At eventual exposition/integration, add a brief source qualification or say “with the description identity of Definition 7.5.1.” Do not say that the analytic hypotheses have verified every literal assumption in that definition. This is an interface/terminology qualification, not an obstruction to the representation formula.

### 9.2 Projection domain

At proof line176 choose π:E→L to be the orthogonal affine projection for the Euclidean structure defining O. Since the ball is centered on L, π(O)⊂Q. Then a∘π∘F at lines201–205 is defined on all of V_x∩F^{-1}(O). The frozen wording “let π be an affine projection” permits this choice, so no new lemma or hypothesis is needed; making the choice explicit would avoid a minor domain ambiguity.

### 9.3 Useful exact citations

The analytic-to-tropical/vertebrated input in lines12–18 could explicitly cite §12.9.5 and Theorem15.7.1. The final calibration gluing could explicitly cite Example4.5.2. These references support arguments already valid in the frozen text.

If expanding the coefficient-measure paragraph, retain the distinction between positive and strongly positive ambient cones made in §4 of this report.

## 10. Verification evidence and exclusions

The read-only checker confirmed all five recorded frozen input hashes, both primary-source hashes, eight unique labels, nine resolved internal references, the one valid bibliography key, balanced braces and environments, and no prohibited control characters. These are identity/structural checks, not the mathematical evidence for the verdict.

The PDF skill was used for read-only primary-source inspection. Ten whole primary-source pages were rendered and visually inspected; the exact commands, dimensions, page numbers, and image hashes are recorded in VISUAL_QA.json. No PDF was created from the candidate and no TeX compilation was rerun. Temporary page images are regenerable inspection intermediates, not deliverables.

No live chapter, original packet, frozen parent, previous audit, inventory, or production record was changed. No git or production call was made. The separate cross-refinement proof, remaining calibration-compatibility problem, later product/torsor/branch applications, and the complete arbitrary-chart current-rigidity question are not independently certified by this report.

