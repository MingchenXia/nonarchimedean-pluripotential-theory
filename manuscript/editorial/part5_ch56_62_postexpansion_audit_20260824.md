# Part V, Chapters 56–62: post-expansion audit

Date: 2026-08-24

## Scope and verdict

This audit covers the complete text of Chapters 56–62 (5,235 source lines):

- ch56_valuative_analytification.tex;
- ch57_comparison_bj.tex;
- ch58_tropical_spectra.tex;
- ch59_complex_dual_complexes.tex;
- ch60_mp_psh.tex;
- ch61_transcendental_cy.tex;
- ch62_k_stability_kahler.tex.

All 33 theorems, 32 propositions, 4 lemmas, and 4 corollaries were checked for hypotheses, normalization, proof status, and provenance. The range is publishable as a carefully sourced account after the corrections recorded below, subject to the explicit preprint and imported-theorem risks in the final section. No unmarked manuscript-new theorem was promoted. The two genuine repairs retained in the range have exact Rethlas receipts.

## Source and provenance audit

The audit used the primary text of Mesquita–Piccione (MP24), Mesquita–Piccione–Witt Nyström (MPWN25), Boucksom–Jonsson (BJ22), Darvas–Xia–Zhang (DXZ23), Xia's operations paper (Xia23Operations), and Bingener's cited relative-analytic result, together with the existing source-level Bingener audit. ArXiv metadata/source status for the MP and MPWN preprints was rechecked on 2026-08-24; MPWN25 remains a v1 preprint and still contains the factor-\(n\) inconsistency discussed below.

The exact Bingener dependency is now kept visible:

1. relative analytification is an interior locally-finite-type statement;
2. coherent algebraization is used over an excellent Stein compactum and with proper support/proper ambient hypotheses;
3. Aussage 2.8 concerns proper \(A\)-schemes of finite presentation;
4. the singleton compactum supplies the relevant analytic local ring;
5. this comparison enters divisorial density, which in turn enters the inverse-limit theorem.

The modern reconstruction is cited as such and does not replace the primary Bingener attribution.

The cited-source set in the audited range is BBJ21, BFJ08, BHJ17, BJ22,
BJ25FiniteEnergy, BJ26ComplexNA, BJKS2, Bingener76Stein, DXZ23, Dem12, GZ15,
MP24, MPWN25, Mat16, Siu98, Trusiani26, Xia23Operations, and XiaStein26.

## Exact corrections made

### Chapter 59

- The standing hypothesis was narrowed from a connected compact complex manifold to a connected compact Kähler manifold (and to a normal compact Kähler space only where explicitly allowed).
- The text now distinguishes the more general ideal-spectrum/Stein-local constructions from the Kähler test-configuration system of MP24, Definition 2.5.1. Divisorial density, dual complexes, and model claims are no longer asserted for arbitrary non-Kähler compact complex spaces.
- This repairs a genuine scope overstatement without changing labels or downstream notation.

### Chapter 60

- The model-independence discussion for relative nefness no longer claims that testing strict transforms of curves proves descent. Such a curve test is insufficient in the nonprojective Kähler category.
- Descent is now attributed to the analytic numerical criterion for nef classes, equivalently to pushing down arbitrarily small Kähler perturbations.

### Chapter 61

- The Calabi–Yau surjectivity proof was rewritten to display the actual variational dependencies. For a sup-normalized maximizing net, the exact identity
  \[
  J_\alpha(\phi_i)=-E_\alpha(\phi_i)
  \]
  is justified from \(\operatorname{MA}_\alpha(0)=\delta_{v_{\mathrm{triv}}}\) and
  \(\phi_i(v_{\mathrm{triv}})=0\). This yields the required finite-energy bound.
- The proof now introduces the second maximizing net used in MPWN25, passes to its Monge–Ampère measures, and identifies the two indispensable imported inputs: the mixed potential/measure estimate and the bounded-\(J_\alpha\), weak-convergence fixed-measure integral lemma. The order “first the auxiliary measure, then the convergent subnet” is stated explicitly.
- The locality proof is now a transparent deep-import boundary at MPWN25, Theorem 8.1.1. It records the model core and explains why weak convergence alone cannot handle multiplication by moving functions, but it does not pretend to reconstruct the source's model-neighborhood and mixed-energy passage.
- A long optional proof descriptor was shortened; the resulting slice has no overfull box.

### Chapters 56–58 and 62

No mathematical changes were required after audit:

- Chapter 56 consistently uses \(\log|a|=-v(a)\), \(t=-\log|z|^2\), and \(\sigma(v)(z)=1\). The square-norm convention and Legendre-transform signs agree, including the constant-ray endpoint check.
- Chapter 57 states the Boucksom–Jonsson comparison only in its projective, smooth, pseudo-effective \(\mathbf Q\)-line-bundle scope. Its operations comparison uses divisorial determination and does not claim an all-points transcendental comparison.
- Chapter 58 keeps tropical reconstruction separate from any MP/BJ psh or Monge–Ampère identification. Compactness, localization, and local-to-global arguments were checked against the stated semiring hypotheses.
- Chapter 62 uses the corrected coefficient
  \[
  \operatorname{MA}_\alpha(\phi_D)
  =\frac1{V_\alpha}\sum_E b_E
    \bigl(\rho^*\alpha_{\mathcal X}+[D]\bigr)^n\!\cdot E\,\delta_{v_E}.
  \]
  The factor \(n\) in the energy derivative/intersection identity is forced by the source's own energy definition, equation (9.1.2), and Theorem 9.1.1 even though the v1 displayed derivative omits it. The correction is explicitly Rethlas-verified. Model/finite-energy stability equivalence and the distinction between total and reduced discrepancy were also checked.

## Imported results versus manuscript arguments

The range now follows these boundaries:

- DXZ23 order-bijection, BJ22 projective comparison, Xia's operations theorem, MP model closedness/divisorial determination/ray correspondence/slope formula, MPWN envelope/energy/Calabi–Yau/locality/regularity/K-stability results, and Bingener's comparison theorem are imported results. Their statements are presented with source scope rather than as manuscript discoveries.
- Elementary topology, semiring, valuation, endpoint, and formal variational deductions are proved in the manuscript.
- Where a proof depends on analytic-cycle compactness, mixed-energy estimates, or the model-neighborhood locality passage, the proof heading and body say so explicitly.
- The recent BJ26ComplexNA and Trusiani26 material is orientation-only; no theorem in this range is deduced from it.

The two manuscript repairs carrying exact verification receipts are:

1. mpwn_factor_n_exact.json, verdict correct, proof digest
   403ac2a601abe51c1d0b4a8852f52b42004332088236a00be3e8460c80af7527;
2. mpwn_dual_complex_boundary_exact.json, verdict correct, statement digest
   3beefd710782d6ed51e115d35c3927535c15399b064cc1499e5d9239f861be54,
   proof digest
   95c4ddb6a737d81e4feaa7e39862f2518b7d63f43235d060f351f07d7aa85973.

## Normalization and presentation checks

- Differential, exponential, and imaginary-unit notation was searched throughout the range. No literal \(\backslash\mathrm d\), \(\backslash\mathrm e\), or \(\backslash\mathrm i\) remains; the house macros are used.
- There are no exercises or problem environments.
- The theorem, proposition, lemma, and corollary environments have no optional conventional names.
- There are no duplicate labels among the seven files.
- Every ref, eqref, cref, and Cref target used in the seven files is defined somewhere in the manuscript.
- Citation resolution succeeds in both slice builds.
- The total-versus-reduced log-discrepancy shift is explicit; the trivial valuation has reduced discrepancy zero.
- Probability mass, central-fiber multiplicities \(b_E\), Gauss normalization, the square-norm convention, and the energy derivative factor were independently checked.

## Compilation

Two independent slice builds were run with latexmk in nonstop, halt-on-error mode:

- part5_ch52_ch58_depth_audit.tex: success, 76 pages;
- part5_ch59_ch62_slice.tex: success, 51 pages.

Neither final log contains an overfull/underfull box, undefined citation, duplicate-label warning, or fatal error. The only undefined references in the slice logs are expected references to chapters/appendices deliberately omitted from the slice:

- app:provenance;
- chap:transcendental-metrics;
- chap:transcendental-okounkov-dh;
- sec:ch51-squared-norm.

All four labels are present in the full manuscript.

## Excluded-source firewall

Mingchen Xia's erroneous Deligne-pairing paper arXiv:1710.09731 is completely excluded. Neither that identifier nor “Deligne” occurs in Chapters 56–62. No argument in the audited source chain was found to depend on it. This firewall must be preserved if citations are later consolidated.

## Residual risks

1. MP24 and MPWN25 are preprints, not independently reproved monographs. In particular, the transcendental Calabi–Yau, locality, regularity, and K-stability statements remain deep imported results.
2. MPWN25 v1, Theorem 2.4.3 is a source-level restatement of the cscK/coercivity theorem and is not reconstructed here. The manuscript correctly treats it as an imported preprint claim.
3. The printed entropy-slope normalization in MP24 fails the constant-ray unit test if total discrepancy is used. The manuscript uses the reduced convention where justified and does not claim an independent repair of the full entropy-slope theorem.
4. The factor-\(n\) and dual-complex boundary corrections are mathematically verified, but they are corrections to source-level presentation; the exact receipts above should remain attached to future revisions.
5. Bingener's theorem is used only through the proper finite-presentation/excellent-Stein-compactum chain. Any future attempt to remove properness, finite presentation, or Kähler/model hypotheses would require a new source audit.
6. The DXZ23, BJ22, and Xia operations comparisons remain confined to their algebraic/projective scopes. No transcendental all-points identification is presently established.
7. The 2026 comparison papers are cited only for orientation because their final publication status and exact compatibility with this manuscript's normalizations may change.

