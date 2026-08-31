# Primary source interfaces for the product residual-functional audit

Date: 31 August 2026. Reviewer: `/root/p082_independent_reaudit`.

## CLD: compact tests, positivity, and original-field calibration

Chambert-Loir--Ducros, arXiv:1204.6277v2, 25 July 2025.

- Primary record: <https://arxiv.org/abs/1204.6277v2>.
- PDF `/private/tmp/CLD25.pdf`, SHA-256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
- Text `/private/tmp/CLD25.txt`, SHA-256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

| Exact passage | Verified use |
| --- | --- |
| Section 7.1.11, printed p.159 | Proper pushforward of currents is legitimate; the candidate verifies compact preimages of compact target supports directly on each collar. No arbitrary nonproper pushforward is used. |
| Section 7.2.6, p.161 | Positivity is preserved by proper pushforward. The candidate also proves positivity of its scalar distribution directly. |
| Proposition 7.2.8 and its complete proof, pp.161-162 | The cutoff sup-norm bound for a positive scalar functional gives a locally finite Radon measure. The proof does not use this to claim one common measure for all current charts. |
| Proposition 7.2.9, p.162 | Positivity supplies order-zero control in the stated locally differentially separated context. Here the constant-coefficient distribution argument is on the ordinary Euclidean rectangle. |
| Proposition 14.4.2, pp.409-410 | Finite-map pushforward of canonical calibrations uses calibrated degree, not a count of ordinary covering sheets. |
| Remark 14.4.3, p.410 | Viewing a finite-extension-field analytic space over the original field multiplies its canonical calibration by the extension degree. The underlying skeleton assertion and the factor were read directly. |

The operative last step is restriction of the ground-field interpretation of a K_p-analytic collar. It is not Proposition 14.3.6's differently normalized scalar-extension comparison. Since the coefficient extension here is unramified, its degree is the residue degree and the primitive character lattice does not change.

The whole five CLD pages listed above were opened as images from `/private/tmp/p213_residual_source_visual.B9icjh/` and inspected. No source PDF was edited or re-exported.

## Henselian coefficient extension

The Stacks Project, Lemma 10.153.7, tag 04GK:

<https://stacks.math.columbia.edu/tag/04GK>

The complete statement and proof were read through the primary web page. Finite étale algebras over a henselian local ring correspond to finite étale residue algebras. Applying this to the complete DVR R and the finite separable field kappa(p) yields the required local finite étale R-algebra. Applying the lifting property to the completed smooth local ring gives its unique coefficient-algebra embedding with the specified residue map. The finite free rank is the residue-field degree. No local cached source file or hash is asserted for this online page.

The further `R_p[[w]]` identification is checked by the candidate's explicit successive-approximation and regular-dimension argument. On each strictly smaller closed disc both directions of that formal isomorphism converge, giving the formal-fibre description. The proof is not replaced by a split-tube statement with an algebraically closed residue-field hypothesis.

Lütkebohmert's local formal-fibre discussion was consulted in the existing text `/private/tmp/Lutkebohmert_RigidCurvesJacobians.txt`, especially Lemma 4.1.9 and Corollary 4.1.10. Its split residue-field hypotheses and surrounding field conventions were not imported as a direct theorem for the nonsplit case. The audit relies on the displayed completed-ring argument, not an uncaveated citation to that split statement.

## GRW: contextual comparison only

Gubler--Rabinoff--Werner, *Skeletons and tropicalizations*, arXiv:1404.7044v3, 28 February 2016.

- Primary record: <https://arxiv.org/abs/1404.7044v3>.
- PDF `/private/tmp/grw1404.7044v3_p213_residual.pdf`, SHA-256 `f7a909a8508032d8e2e0a0c6f9cd14b06f36cfa465c3e83fa5d40be6033678ad`.
- Text `/private/tmp/grw1404.7044v3_p213_residual.txt`, SHA-256 `851b1820299b758f96db87f37da1ce786b6d169597dc9bebb0f5e3208b1079af`.

Whole printed pages 1, 23, and 24 were visually inspected from the existing source renders. Section 1.1 assumes an algebraically closed, complete, nontrivially valued field. Theorem 6.9 and equation (6.10.2) concern the slope/principal-intersection identity for a rational function. They do not supply an arbitrary-current slicing theorem or construct the functional b_T(p). The candidate's explicit source test supplies that new interface in its restricted product geometry. GRW is not used to deduce the nonsplit original-K case.

## Explicitly conditional representation and prior algebraic step

Representation directory: `../p213_skeletal_packets_20260831/skeletal_representation/`.

- `statement.tex`: `5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a`.
- `proof.tex`: `27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a`.

The statement was read to identify the assumed source-cell formula and its support requirements. Its proof was checked for preservation only, not freshly audited. The source-calibration interpretation is conditional on this input. The collar distribution and principal relation themselves never invoke it.

Earlier obstruction note: `../p213_calibrated_chart_rigidity_research_20260831/OBSTRUCTION_NOTE.md`, SHA-256 `b27c56591db85bfef79e8e34b47637a06bd7df8f9d065b46b5303c64cfd61b86`. Its positive divisor-functional argument had a previous independent bounded audit by this reviewer. In the present proof that argument is applicable only after the actual analytic current test establishes annihilation of every principal divisor. It is not substituted for the analytic interface.

No source cited here establishes the full P21.3 target from this product calculation. No candidate compilation, new PDF, production verdict, live edit, or inventory retirement was performed.
