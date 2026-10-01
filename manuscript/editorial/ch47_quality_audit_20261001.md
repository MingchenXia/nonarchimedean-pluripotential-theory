# Chapter 47 completion audit

Date: 1 October 2026

Base: local Chapter 46 commit `d392917`.

Scope: `parts/part4/ch47_bj_finite_energy.tex`, under the sequential
chapter-quality programme. Chapter 48 is next; the whole-book goal continues.
Independent Chapter 72 research remains paused.

## Mathematical and expository review

The assertions, proofs, examples, standing hypotheses, dictionary, and source
discussion were reviewed continuously. All 40 formal assertions have proofs:
seven lemmas, ten theorems, thirteen propositions, and ten corollaries. All 73
reusable environments have semantic labels; the chapter has 209 labels.

The signature retains integral projective unibranch varieties over an
algebraically closed trivially valued field, arbitrary characteristic, real
ample numerical classes, and the envelope inputs of Chapter 45. Mixed
estimates use dimension at least one. The SNC skeletal example now states
its characteristic-zero hypothesis. Probability Monge–Ampère measures and
energies are distinguished explicitly from the book's unnormalized convention.

Substantive repairs include:

- The Bernstein proof makes the Dirichlet second differences explicit.
  Its Green-kernel calculation gives the stated concavity constant
  `n/((n+1)(n+2))`. The deformation-to-the-normal-cone example verifies both
  sharp I/J comparison constants, with the positive-I qualification when
  comparing their simultaneous equality cases.
- The curve separation argument uses the fixed Dirichlet inner product,
  decreasing approximation, and square-integrable slope vectors. It does
  not extend a varying higher-dimensional pairing to a fixed norm.
- Fenchel inequalities keep the sign and extended-real domain explicit.
  Finiteness on the linear-growth locus does not imply that all measures
  have full mass there. Constant differences avoid subtracting two poles.
- Differentiability uses the published uniform quadratic lower bound for
  equilibrium energy and a proved one-sided upper bound. No perturbation
  is falsely declared psh in the original class.
- Domination uses the Monge–Ampère measure of the comparison potential.
  Uniqueness, the quasi-triangle inequality, general strong completeness,
  and the arbitrary lower-semicontinuous contact theorem are identified
  as exact published interfaces.
- The restricted direct method states its measure-continuity assumption.
  The general Calabi–Yau theorem is quoted through the source's envelope
  equivalence; completeness is Theorem 12.8, not Theorem 12.4. The proof
  does not invent an admissible envelope of a tail infimum.
- The logarithmic curve, product toric, and infinite-energy examples prove
  their energy domains before using the finite-energy operator. Endpoints
  and graph measures outside that domain are distinguished. Restrictions
  of the logarithmic probability measure retain and renormalize the root
  atom together with the ray density.
- Proper-support pole witnesses on a unibranch curve pass through smooth
  normalization and the Chapter 45 reflection package. Green-function
  non-Q-PL examples use the published trivially valued examples, rather
  than a discretely valued theorem.

The redundant task list was removed, 1,900 legacy inline math spans were
normalized, and comparison and dictionary tables use two columns. The final
strict-inclusion display was split into two rows after rendered review.

An auxiliary exact-rational calculation passes 17,317 comparisons: Bernstein
integrals and concavity bounds in dimensions one through ten, degree-dependent
curve I/J values, the projective-space sharpness example, and slopes and masses
of the fully normalized restricted logarithmic measures. These supplement
the written proofs; they are not an independent mathematical verdict.

## Direct source interfaces

The primary source is Boucksom–Jonsson, *Global pluripotential theory over a
trivially valued field*, Ann. Fac. Sci. Toulouse 31 (2022), 647–836,
[published PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf).
Downloaded SHA-256:
`50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.

| Locators | Checked interfaces |
| --- | --- |
| Theorem 3.31; Proposition 7.27; Theorem 7.28 | Quasi-triangle inequality, energy and I/J coefficients, quantitative concavity. |
| Proposition 7.7(iv), results 7.14–7.20, Corollary 7.48 | Normalization, integrability and curve graph measures, polar witness. |
| Propositions 8.1 and 8.3, Theorems 8.5–8.6 | Working versus raw equilibrium energy; uniform quadratic lower bound and continuous first variation. |
| Sections 9.1–9.3, especially Proposition 9.19 | Test-class duality, finite-energy measures, Fenchel equality, almost maximizers, fixed-measure L1 continuity on bounded J-sublevels. |
| Theorem 10.2, Theorem 10.3, Corollaries 10.4 and 10.6, Theorems 10.12 and 10.14 | Quantitative embedding and pairings, uniqueness and domination, strong measure criteria and completeness. |
| Theorems 12.4–12.8, Theorem 12.12, Proposition 12.14 | Strong potential criteria, envelope/Calabi–Yau/completeness equivalence, linear-growth Green functions. |
| Theorem 13.1 and Lemma 13.2; Appendix B | Lower-semicontinuous contact, negligible-set nullity, toric energy and bounded toric measures. |

Boucksom–Jonsson, *Non-Archimedean Green's functions and Zariski
decompositions*, [published PDF](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.579.pdf),
SHA-256 `d79b777408b951380bd00ce74f9917c7769be391022352468503d0405bc92607`,
was checked at Theorem 60 and Examples 63 and 65 (printed pages 29–31).
These give the required trivially valued non-Q-PL examples. Theorem A has
a different valuation hypothesis and is not used for that claim.

Rendered source pages for the quadratic bound, Proposition 9.19, Theorem
12.8, the obstacle theorem, the polar witness, and the Green examples were
inspected. This is a direct editorial/source audit, not an independent-agent
or exact-current model-verifier verdict. No research atom changes.

## Mechanical and rendered verification

The manual review checked hypotheses, notation, extended-real domains, nets,
proof structure, attribution, and delimiters. The limited scoped scan before
and after rendered review found no unlabelled reusable environments, proofless
assertions, duplicate chapter labels, environment nesting errors, legacy inline
delimiters, double-dollar displays, or unresolved TODO/FIXME/TBD markers.
The standalone legacy writing-audit executable is unavailable; its historical
warning counts are not asserted.

The reference checker passes with 425 inputs and 12,020 labels, no missing
inputs, duplicate labels, dangling references, or structural defects. All six
checker regression tests pass. The open-problem inventory remains 42 atoms
in 12 environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17. The scoped scan and
reference checker were repeated after rendering; `git diff --check` passes.

The complete `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds with the workspace-local TeX Live 2025 font setup. The PDF has
4,104 pages and 19,183,549 bytes, SHA-256
`8e0da4accd432fc6dcb9cbbadd17a0844aec2fc0d08d124c8796cf7b242b512a`.
Final source SHA-256:
`5e125a4e3a5d18ada8a4bbdb93a3c231553a4ea77e6810ec1268d1cba67e26a8`.

There are no unresolved references or citations, missing glyphs, rerun
requests, or fatal errors. Chapter 47 has zero overfull boxes and zero
LaTeX/package warnings. The full book retains 23 overfull boxes outside this
chapter and 13 duplicate PDF destinations in Chapter 70.

All 60 chapter pages, physical 2699–2758 (printed 2631–2690), were scanned;
2758 is an intentional blank verso. Detail inspection covered physical
2699, 2703, 2705–2706, 2709, 2711, 2713–2714, 2720, 2727–2728, 2732,
2737, 2741, 2746–2752, and 2755. Adjoining pages 2697–2698 and 2759 were
inspected. The final PDF was compared page by page with the first reviewed
excerpt: only 2703, 2743–2744, and 2755 changed, and all four were inspected
at full resolution. No clipping, overlap, bad glyph, formula overflow, or
hierarchy defect remains in the reviewed chapter.

Generated full-book and chapter PDFs are local review artifacts. Frozen
release artifacts and dated checksum ledgers are unchanged. Verified work
is committed locally while explicit remote-push approval remains pending.
