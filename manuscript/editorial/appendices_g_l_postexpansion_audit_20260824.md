# Appendices G--L post-expansion audit

Date: 24 August 2026

**27 August 2026 P06.3 reconciliation addendum.**  The historical audit of
Wanner's published comparison and restricted regularization scope remains
correct.  Appendix L now additionally records the independent book theorem
`thm:p063-current-psh-ordinary-regularization`: for continuous functions on
smooth proper algebraic curves over algebraically closed complete
nontrivially valued fields, current positivity, Thuillier subharmonicity, and
the first ordinary CLD-smooth decreasing-limit stage coincide locally.  The
exact statement/proof hashes are `767cbf81...d5d8a68` and
`d1db3c2d...312bd8`; production run
`20260827T090645Z_767cbf81c723`, `gpt-5.6-sol`/`xhigh`, returned final
`correct`, zero critical errors, and zero gaps, and three independent
exact-byte audits passed.  Appendix L records the exact scope and receipt.
P06.3 is retired; the current frontier is 16 formal environments and 55
active atoms.  This addendum supersedes only the older current-status
sentences below, not their dated source audit.

**Release reconciliation addendum.**  Appendix L has now been synchronized
with the exact-current Chapter 23, 49, 55, and 69 production gates.  It records
the fixed-skeleton, positive-volume BJ, positive-Cao-volume Xia, and
integral/rational toric scopes without publication or priority claims; it also
retains the BJ22 basic-closure and MP reduced entropy-slope non-receipt
boundaries.  The clean whole-book build of this exact synchronized snapshot
remains pending and is not supplied by the focused appendix build recorded
below.  The time-sensitive warning at the end of this historical audit is
therefore discharged as a provenance synchronization, but not as a new
whole-book compile certificate.

## Scope and verdict

This audit covers only the following source files:

- `appendices/appG_tropical_algebra.tex`;
- `appendices/appH_complex_reference.tex`;
- `appendices/appI_stacks.tex`;
- `appendices/appJ_normalizations.tex`;
- `appendices/appK_notation.tex`;
- `appendices/appL_provenance.tex`.

The review addressed mathematical correctness, the exact scope of imported results, notation and normalization, graduate readability, proof boundaries, examples, cross-reference conventions, and the recent edits concerning energy integrals and discrepancies in Appendix J, tropical notation in Appendix K, and the scope of Wanner's theorem in Appendix L.

**Verdict.** No mathematically justified source change was found necessary in Appendices G--L. In particular, this audit did not alter any statement recorded as Rethlas-verified, did not promote any new result, and did not introduce any dependency on arXiv:1710.09731. A focused compilation of the six appendices succeeded, and representative pages were inspected visually.

## File-by-file findings

### Appendix G: tropical algebra and analytic calibration

The algebraic sequence is coherent and correctly normalized:

1. semiring characters and tropical points;
2. graded reduction and initial forms;
3. the relation between analytic seminorms and tropicalization;
4. the calibration of tropical multiplicities and Chambert--Loir--Ducros currents;
5. the balancing statement in the analytic setting.

The proofs of the elementary tropical algebra statements are self-contained. The analytic calibration section correctly separates formal deductions from the foundational CLD inputs. It explicitly imports the construction and normalization results used for integration currents, tropical multiplicities, balancing, and push-forward, rather than presenting those inputs as newly proved facts. The calibration test agrees with the sign convention

\[
  \langle m,\operatorname{trop}(x)\rangle=-\log|\chi^m(x)|.
\]

The appendix contains concrete algebraic examples and normalization checks. It does not contain exercises. All five theorem-like statements have corresponding proof environments.

### Appendix H: complex reference theory

Appendix H accurately functions as a comparison appendix for the complex theory used in Chapters 51 and 52. Its eight theorem-like statements all have proof blocks. Where a result is imported, the proof identifies the precise foundational theorem and explains the deduction needed in the manuscript.

The following scope distinctions were checked:

- non-pluripolar-product total-mass monotonicity is attributed with the hypotheses used in the cited source;
- the bimeromorphic mass comparison is not stated as an unconditional invariance principle outside its hypotheses;
- relative energies and envelope operators are normalized consistently with the main chapters;
- multiplier-ideal, geodesic, and test-curve statements retain the source hypotheses needed for their use.

The appendix includes an illustrative example and explicit normalization tests. No proof was silently replaced by a citation without marking the imported boundary.

### Appendix I: Stacks Project dependency ledger

The appendix is a dependency ledger rather than a substitute for the cited foundational algebraic geometry. Its descriptions were checked against the official Stacks Project pages. In particular:

- [Tag 03H0](https://stacks.math.columbia.edu/tag/03H0): the stated form of Stein factorization and the listed properties agree with the tag;
- [Tag 0BRJ](https://stacks.math.columbia.edu/tag/0BRJ): the normality of the residue extension and the surjection from the decomposition group to the automorphism group are stated with the correct scope;
- [Tag 0BX5](https://stacks.math.columbia.edu/tag/0BX5): the finite-type and quasi-separated hypotheses in the valuative criterion are retained;
- [Tag 0CNF](https://stacks.math.columbia.edu/tag/0CNF): the generic-fibre isomorphism, locally nilpotent kernel, and power-lifting conclusions are recorded accurately;
- [Tag 081T](https://stacks.math.columbia.edu/tag/081T): the hypotheses on the proper morphism, the quasi-compact quasi-separated base, and the quasi-compact open locus are retained in the admissible-blow-up domination statement.

No claim in this appendix extends a Stacks Project result beyond the cited tag. The absence of examples here is appropriate for a compact source-and-dependency ledger and does not create a graduate-readability problem.

### Appendix J: normalization ledger

The recent corrections were checked in detail.

#### Energy integrals

The relative-energy formulas use actual multiplication between the potential difference and the Monge--Ampere measure, for example `(\varphi-\varphi_0)\,\operatorname{MA}(...)`. The formulas no longer contain the malformed punctuation that could be read as a tuple or separated argument. The normalizing factors and mixed-product indices are consistent with the conventions in the complex and non-Archimedean parts.

#### Discrepancy functions

The appendix now correctly distinguishes:

- the total homogeneous log-discrepancy function `A_X`;
- the normalized slice used in the Mesquita--Piccione framework on `X\times\mathbb C`;
- the reduced quantity obtained by subtracting the base contribution.

The product-valuation check confirms that these are not being conflated. In particular, the normalization of a valuation lying over the parameter direction accounts for the unit base discrepancy before the reduced discrepancy is formed.

#### Chambert--Loir measure normalization

The multiplicity `b_E` is paired with the normalized divisorial point `x_E=b_E^{-1}\operatorname{ord}_E`. The resulting formula passes the total-mass check. This is consistent with the conventions used elsewhere in the manuscript for model metrics and divisorial points.

The appendix provides concrete unit tests for the principal normalizations. No source edit was needed.

### Appendix K: notation ledger

The global tropicalization notation is now internally consistent:

\[
  \operatorname{trop}:T^{\mathrm{an}}\longrightarrow N_{\mathbb R},
  \qquad
  \langle m,\operatorname{trop}(x)\rangle=-\log|\chi^m(x)|.
\]

The global map is separated from the local or chart-dependent notation `f_{\mathrm{trop}}` and `\operatorname{Trop}_f(U)`. This prevents the earlier risk of using one symbol simultaneously for an intrinsic torus tropicalization and for a tropicalization attached to a moment map. The signs agree with Appendix G and the tropical chapters.

The appendix is a notation dictionary; examples are supplied where they resolve a genuine normalization ambiguity, while repetitive examples are appropriately left to the substantive chapters.

### Appendix L: provenance and status ledger

The appendix carefully distinguishes established literature, deductions made in the manuscript, first-draft results, and statements awaiting or carrying a Rethlas receipt. It does not turn a provenance entry into a mathematical proof and does not enlarge the scope of cited results.

The Wanner entry was checked against the published abstract and metadata for [Wanner, *Comparison of two notions of subharmonicity on non-Archimedean curves*](https://doi.org/10.1007/s00209-018-2205-z). The manuscript now states the comparison for continuous functions on the analytification of a smooth proper algebraic curve: Thuillier subharmonicity agrees with the current-positive/CLD notion. It separately records that the monotone regularization result is proved for `\mathbb P^1` and Mumford curves. Thus the appendix no longer suggests a general regularization theorem for all smooth proper curves.

The surrounding comparison ledger also correctly avoids claiming a universal CLD--BFJ equivalence beyond the hypotheses established in the relevant chapter. The current wording preserves the distinction between current-positive CLD functions and an approximation-generated hierarchy when the supplementary regularization hypothesis is unavailable.

## Exact-source and exclusion checks

The audit searched all six appendices for direct and indirect references to the user's erroneous Deligne-pairing paper, including the identifier `1710.09731`. No such reference or dependency occurs. This source was not consulted and is completely excluded from the audit.

No literature statement was deliberately strengthened. In particular:

- foundational CLD results remain explicitly imported at their cited locations;
- the Wanner comparison and regularization statements retain their different scopes;
- the Stacks Project ledger keeps the hypotheses appearing in the cited tags;
- first-draft and Rethlas-status labels in Appendix L were not upgraded.

## Convention and proof-boundary audit

Static checks of Appendices G--L found:

- no raw `\ref`, `\autoref`, `\pageref`, or `\vref` commands; object references use `\cref` or `\Cref`, while equation references use `\eqref`;
- no prohibited use of `\mathrm{d}`, `\mathrm{i}`, or `\mathrm{e}` in place of the manuscript macros `\rd`, `\rmi`, and `\rme`;
- no optional conventional names attached to theorem, proposition, lemma, or corollary environments;
- no exercise environments or exercise sections;
- no occurrence of the excluded source identifier;
- no malformed energy-integral punctuation of the previously observed form;
- 190 labels across the six appendices, all accepted by the focused build;
- five theorem-like statements and five proofs in Appendix G;
- eight theorem-like statements and eight proofs in Appendix H.

Appendices I, J, K, and L are ledgers rather than theorem chapters. They do not contain unproved theorem-like environments masquerading as exposition. Imported foundational boundaries are stated as such.

## Compilation and visual validation

A focused `\includeonly` driver was created at

`tmp/pdfs/appendices_g_l_audit_slice.tex`.

It includes Appendices G--L through the manuscript's normal preamble and bibliography configuration. The resulting PDF is

`build_appendices_g_l_audit/appendices_g_l_audit_slice.pdf`.

The build completed successfully with 158 pages and no undefined citation or reference warnings, no overfull horizontal or vertical boxes, and no fatal TeX errors. The log contains only the expected missing-destination warnings caused by cross-links to chapters intentionally omitted by `\includeonly`, together with pre-existing bibliography metadata warnings unrelated to these appendices.

Representative pages were rendered and inspected, including the openings of Appendices G--L, the tropical multiplicity discussion, the complex relative-energy formulas, the Stacks dependency table, the discrepancy and mass-normalization tests, the notation table, the Wanner provenance entry, and the comparison-status ledger. No clipping, overlap, black glyph boxes, broken display, or unreadable table was found.

## Edits made

No manuscript source file in Appendices G--L was changed: every potential issue examined either had already been corrected in the root edits or was already accurately bounded by its cited source. The only added files are this audit report and the reproducible focused-build driver. This conservative outcome avoids unnecessary churn and, in particular, avoids altering verified mathematics merely to produce an edit.

## Residual risks and required final reconciliation

1. **Appendix L is time-sensitive.** It records receipt and provenance status for results developed in Chapters 69 and 72. Those chapters were being audited or expanded concurrently. Before release, Appendix L should be reconciled once more against the final Part VI text, especially the status of the fixed-dual-complex comparison and any changes to `thm:verified-pl-psh-equivalence`. This audit intentionally did not change those status entries.

2. **Frozen literature cutoff.** Appendix L records a literature cutoff of 23 August 2026, while this audit is dated 24 August 2026. This appears to be an intentional frozen cutoff. It should be changed only if the editor decides to perform a new systematic literature search.

3. **Focused-build warnings.** The focused slice necessarily omits destinations defined in other chapters, so its PDF contains missing-destination warnings. These are not broken references in the full manuscript. A final full-book compilation remains necessary after all concurrent edits have settled.

4. **CLD version pinning.** Appendix G's analytic calibration uses precise locations in the cited CLD source. The deductions were checked, but the final bibliography should continue to pin the cited version or edition so that proposition and theorem numbers remain reproducible.

5. **Dependence on main-chapter notation.** Appendix H was checked against the current Chapters 51 and 52. Any later normalization change in those chapters must be propagated to Appendix H and Appendix J together.

Subject to those synchronization checks, Appendices G--L are mathematically and editorially ready for integration into the next full-book build.
