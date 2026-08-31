# Chapter 14 cycle/Tate correction: exact afterpatch addendum

Date: 2026-09-01. Reviewer: /root/p082_independent_reaudit.
Verdict: PASS for the exact final source revision and the bounded integration/dependency checks below. No unresolved defect found in the added double-thickening example. No production verification or new theorem claim.

## 1. Identity, provenance, and scope

Live source reviewed:
 /Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory/manuscript/parts/part2/ch14_currents.tex

Base commit:
 db8918d5a533c5a29336d97f70b500540dd9484f

Base Chapter 14: 160088 bytes, SHA-256
 4dc28ea36f841d71ff6f082a6e458d8c9fec3d150c802f241d5430c37dc9a1c7

Final Chapter 14: 165265 bytes, SHA-256
 0ffe13c44ced54ed77d6bfb1e16679cc5682368d1ca6207c2d7d1fc0f4480870

The first source-correction candidate is frozen in the sibling
p213_ch14_cycle_source_correction_audit_20260901, with proposed_replacement.tex SHA-256
 c8219e4f6951634b12cf9b335a3679ec28535e60a735ddcda62daa2d265cbdfa.

The separate Tate candidate is frozen in the sibling
p213_ch14_tate_measure_source_correction_audit_20260901, with proposed_replacement.tex SHA-256
 22d15d8f39bf0b59a7d704153e5aa7180b522f59affce37afdbe643bad50c95b.

This reviewer authored those two source-based replacement candidates after diagnosing the original passages. Root independently read the complete candidates and their primary sources, then performed the live integration. Accordingly, this addendum is an exact-revision assembly and dependency review; it is NOT a claim of a fresh independent mathematical review of the reviewer's own replacement proofs.

The double-thickening paragraph was authored subsequently by root after the reviewer flagged the old multiplicity-direction error. Its full mathematical verification below is independently performed on root's final text. The initial error diagnosis and that division of work are disclosed rather than portrayed as complete independence from all prior discussion.

No live source or older frozen packet was changed by this reviewer. Only this new audit directory was written. Read-only git show was used to retrieve the user-specified base.

## 2. Complete-byte reconstruction, not merely a diff impression

check_integration.mjs reads the base chapter directly from the specified commit. It reconstructs the final chapter by these uniquely matched substitutions:

1. Replace the COMPLETE Tate example with the frozen Tate candidate, omitting only its leading editorial comments.
2. Replace the COMPLETE line-cycle example with the corresponding portion of the first candidate.
3. Replace the fundamental-cycle theorem/proof block with the remaining portion of that candidate. The theorem statement itself is unchanged.
4. In the automatic-continuity applications table, replace delta_Sigma with [mu_Sigma].
5. In the final examples table, replace the noun phrase "Tate curve skeleton" with "Tate skeleton length measure"; retain the mass v_K(q) and its example reference.
6. Replace only the Dense flat locus item of rem:ch14-fibre-hypotheses with the explicit double-thickening item saved in dense_flat_replacement.tex. Its original is saved in dense_flat_original.tex.

In addition there is exactly ONE typography-only change within the Tate candidate: its inline chi membership condition is moved into an unnumbered display, with the sentence period inside that display. It changes no variable, quantifier, inequality, interval, or mathematical formula. Root made this correction after the first build reported an overfull line. The frozen Tate candidate remains unchanged.

The reconstructed full 165265-byte file equals the actual final chapter byte-for-byte. Thus there is no additional change outside these six content locations and this one layout adjustment. The combined first candidate accounts for two logical blocks but is safely replaced in one exact substring operation.

For chronology only: the version immediately after the original three blocks and two table edits had SHA-256
 3099810f3c5344cc717d608bfc28a6d69c603940ee8f8298db5278440cd2cd98.
The intermediate layout-only revision had SHA-256
 700f948ad9e3f6ef3981ddfd2f83bf6eb9bb23fe36361ff636af7f957ec67d34.
Neither is the final reviewed revision.

## 3. Labels, equation references, and bounded consumers

The COMPLETE ordered list of 102 chapter labels is unchanged from the base. The COMPLETE ordered list of 22 eqref occurrences, including repetitions, is also unchanged. Both lists are stored in EXACT_CHECK.json. This verifies preservation rather than merely counting totals.

In particular:

- ex:ch14-skeleton-current, ex:ch14-line-cycles and thm:current-fundamental-cycle retain their exact labels.
- The original eq:appJ-cld-pl reference is retained and now correctly attached to the untruncated analytic-divisor formula.
- The fundamental-cycle theorem statement is byte-identical to its base statement. Its arbitrary pure-dimensional analytic-subspace scope is neither narrowed nor enlarged.
- All eight distinct labels referenced by the two new candidate blocks resolve in the existing chapter/appendix sources.
- Both source bibliography references use the existing CLD25 key; no bibliography mutation was part of this integration.

There is no remaining literal delta_Sigma notation in Chapter 14. The construction table now names the measure current [mu_Sigma], and the final table attributes mass v_K(q) to the skeleton LENGTH MEASURE, not to the differently graded integration current delta_E.

The live non-editorial references to thm:current-fundamental-cycle in Chapters 11, 14, 15 and 17 were located and the immediately relevant uses read. They continue to call the same statement identifying analytic integration with the fundamental cycle and its generic multiplicities. In particular, the Chapter 15 divisor discussion and Chapter 17 componentwise multiplicity factors require that unchanged interface, not the removed false graded-length argument. The one directly observed contradictory Chapter 14 fibre example has now been replaced and is verified in Section 4.

This is a bounded consistency check, not a new audit of every entire downstream proof or of historical editorial packets. No all-chapter current-rigidity theorem, all-source-cell representation, production status, or inventory retirement is inferred.

## 4. Independent mathematical check of the added double-thickening item

Let Y be a nonempty smooth pure-dimensional analytic space in the standing separated-space setting. Let X be the double thickening with structure sheaf O_Y[epsilon]/(epsilon^2), and let p:Y -> X be the reduction immersion.

### Geometry and support

The thickening is finite over Y, has the same underlying topological space and the same pure dimension. The reduction map p is a finite closed immersion, hence proper. Consequently the whole support of omega=1 is p-compact: its intersection over every compact target subset is compact. No compactness of the entire Y is needed.

At an analytic point x of X, epsilon vanishes in its completed residue field H(x). The base change of the reduction algebra to H(x) is H(x) itself. Hence the analytic fibre Y_x is exactly M(H(x)), a single reduced point over H(x), not a point of length two. Both spaces have equal dimension, so d=0. Integration of 1 over this relative reduced point is 1. Thus the fibre function u_omega is the constant 1 on X. This computation does not apply the projection theorem without its flatness hypothesis; it directly evaluates the displayed fibre integral.

### Current degrees and the multiplier

Because omega=1 is a (0,0)-form on Y, its associated current [omega] is delta_Y, of top bidimension and bidegree (0,0). Similarly [u_omega]=delta_X on X. Thus the pushforward and comparison in the new display have matching current degrees.

The fundamental cycle of the double thickening is twice the reduced Y, component by component. The source-proved identity thm:current-fundamental-cycle therefore gives
 delta_X = 2 p_* delta_Y.
Equivalently,
 p_*[omega] = (1/2) delta_X,
whereas
 [u_omega] = delta_X.
The factor is on the target integration current, exactly as the corrected text says.

The inequality is genuine, not a formal non-equality involving a zero current: nonempty smooth Y has a local nonzero positive compactly supported top-form integral, so delta_Y is nonzero, and therefore delta_X is nonzero. This is also the support property for integration on a reduced pure-dimensional space already stated before these examples. The explicit nonempty hypothesis in root's final text is therefore appropriate, including dimension zero.

### Flatness

At a generic Artinian local ring of any component, the target has length two and its reduced quotient has length one. A finite flat module over an Artinian local ring is free, so its length must be an integer multiple of two. Thus the generic reduction module is not flat, as written.

One can in fact check nonflatness at every point without invoking a generic-flatness theorem: for any nonzero local ring B of Y, put A=B[epsilon]/(epsilon^2). The inclusion J=(epsilon) -> A is injective. Tensoring with A/(epsilon)=B turns it into the zero map from
 J tensor_A B = J/J^2 = J, a nonzero module,
to B. This violates preservation of injections by a flat module. Hence p is nowhere flat, so in particular it has no dense flat locus in either the ordinary or Zariski topology.

No field-extension, reducedness-of-fibres-to-flatness inference, or analytic generic point chosen by analogy with a scheme is needed for this check.

### Exact primary-source status

The source for the projection formula is CLD 16.5.3--16.5.5, printed p455, with dense flat locus explicitly imposed. Most importantly, CLD Remark 16.5.6 immediately following it already states that the formula fails for the nonflat reduction immersion of a nonreduced X, with the discrepancy measured by generic multiplicities. Root's double-thickening paragraph is a concrete, fully computed instance of this existing source observation, NOT a new counterexample claim.

The current multiplier uses CLD Proposition 16.6.3, printed p459; its proof uses the reduction immersion's calibrated degree 1/m from Proposition 13.3.7 and the integration formula Proposition 15.4.3. The precise source bytes remain those pinned in the two predecessor manifests:
 /private/tmp/CLD25.pdf:
 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719
 /private/tmp/CLD25.txt:
 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e
These are the 25 July 2025 arXiv v2 source. The complete relevant p455 was additionally rendered and visually inspected in this integration audit; the preceding source audits inspected the other cited primary pages.

## 5. Final checks and exclusions

The exact checker revalidates all eight announced parent pins, all 30 entries in their manifests, and all 32 parent checksum entries. No parent byte changed. The final live chapter and every authored text file were scanned for control bytes, including embedded CR and DEL, allowing only LF and tab; the count is zero.

EXACT_CHECK.json records the successful full-file reconstruction, lists, source identity and bounded dependency results. The new manifest and SHA256SUMS freeze this report, the checker, the exact dense-flat before/after items, check evidence and primary-page image, together with immutable parent inputs.

This addendum does not claim that the final full book has compiled, or that the final PDF layout has been visually approved. Those are root's separate final-snapshot build and visual-QA tasks. It certifies the exact final source assembly above and the corrected double-thickening calculation, with no further live changes proposed.
