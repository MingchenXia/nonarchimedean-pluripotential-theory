# Chapter 52 completion audit

Date: 1 October 2026

Base: local Chapter 51 commit `ef14b3d`.

Scope: `parts/part5/ch52_rays_test_curves.tex`, under the sequential
quality programme. Chapter 53 is next; the whole-book goal continues.
Independent Chapter 72 research remains paused.

## Mathematical and expository review

The full source, all assertions, examples, operations and source note were
reviewed. All eleven formal assertions have proofs or exact analytic
imports: three theorems, four lemmas and four propositions. All 25 reusable
environments have labels; there are 70 labels, including six section
labels and the new relative-energy interface.

The principal repairs are:

- The standing background is explicitly smooth, closed and real. A
  zero-obstacle model reference automatically has supremum zero; adding
  a constant to a ray changes its initial value, while translating the
  test-curve parameter adds a linear function of time. These operations
  are distinguished within their actual domains.
- Relative geodesics have exact rooftop-stability, rooftop-recovery and
  Perron source interfaces. The jointly psh supremum theorem supplies the
  interior subgeodesic; the rooftop sandwich supplies its full-mass class;
  barriers, compactness and recovery supply the boundary; psh pasting
  supplies restrictions. Linear supremum uses the exact relative segment
  theorem, rather than a bare maximum-principle claim. The model supremum
  identity is proved directly.
- Relative energy is defined explicitly on bounded-difference potentials
  and extended by its infimum over such majorants. The finite-energy and
  bounded-ray meanings, unnormalized mass factor and energy-affinity
  theorem are stated. The two radial parameters and the dual rescaling
  remain separate from probability normalization.
- Interior positive mass and the model initial level are deductions from
  the test-curve axioms. The nontrivial closed endpoint can have zero mass.
  Forward usc, inverse closed threshold and scalar biconjugacy retain the
  existing proofs and their exceptional-set/extended-real conventions.
- Ideal-envelope monotonicity is proved by a maximum competitor and
  divisorial Lelong minima; concavity is proved by positive combinations
  of competitors. An ideal-model level is explicitly shown to be fixed
  by the ordinary model envelope. Increasing ideal-envelope continuity is
  identified as an analytic theorem, and applies to positive-mass nets.
  Kähler transitions require closed forms.
- Projected sums, concave-envelope joins, finite joins for arbitrary
  suprema, countable representation and directed-net limits retain their
  correct construction. The increasing-envelope locator is explicit.
  Decreasing transition compatibility retains its positive-mass and
  singularity-metric input; it is not inferred from idempotence alone.
- The big-line-bundle filtration proof identifies its exact source and
  proves real concavity via rational coefficients approached from above.
  The bounded-above ideal-good supremum theorem supplies the projected
  ideal-model levels. Full section spaces, multiplier ideals and the
  ideal-volume theorem give the minimal initial model. Ample positive
  curvature is kept in the RWN/Phong--Sturm identification and in the
  statement that the outer model envelope can be omitted.
- In the hyperplane example, a torus Fourier-coefficient bound proves that
  normalized monomials also control arbitrary sections, with an explicit
  vanishing polynomial-dimension error. Degree tails are cofinal by powers.
  Endpoint values avoid zero times minus infinity. Real analytic
  divisorial coefficients agree with Chapter 51's convention. Matching
  first derivatives and local C1,1 regularity exclude extra interface mass.
  The ray is identified as the coordinate-weight product configuration.
  The tempting maximum ray has an explicit curvature-support energy
  calculation proving nonaffinity; the actual product energy is checked
  independently by coordinate change and first variation.
- All legacy inline delimiters have been converted and section navigation
  added. The source note distinguishes the original bounded ample
  correspondence, published big-class relative correspondence, full
  relative energy theorem and later envelope inputs.

## Direct source interfaces

Three primary PDFs were read at the relevant statements and proofs.
Forty-two source pages were rendered and inspected.

| Source and checked version | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Xia, supplied snapshot dated 18 July 2026, matching the historical source pin | Proposition 3.1.13; Definition 3.1.6; Propositions 3.2.11/3.2.13; Propositions 4.2.1/4.2.2/4.2.4 and 4.3.3; Propositions 7.2.1/7.2.2; Theorem 7.4.1; Sections 9.1--9.4, especially Theorem 9.2.1, Example 9.3.1 and Lemma 9.4.9 | 114, 118, 144--146, 154--159, 169, 173, 255--256, 266, 300, 309, 311--312, 320, 322--324, 327, 329--330, 334--337 |
| Darvas--Xia--Zhang, published CMH 100 (2025), 269--322, DOI 10.4171/cmh/586 | Equations (5), (6), (10); Lemma 2.4; Theorem 2.6(ii)--(iii); Lemma 2.8, with positive mass | 11--15 |
| Ross--Witt Nyström, arXiv 1101.1612 v3, 16 July 2013, preceding the 2014 publication | Proposition 7.11, Corollary 7.12, Section 9 and Theorem 9.2 | 32--34, 37--39 |

PDF SHA-256 values, in that order:

1. `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`
2. `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`
3. `70bbaba6da38a9eee0b682ebd3953b3c99ce85c7d2bcf800d6f2dd6dca6456ff`

Xia's PDF is reused from the ignored Chapter 51 cache. The other two are
in `source_material/ch52_audit_20261001`; the published DXZ PDF was obtained
from the publisher's citation PDF URL. Chapter 51 interfaces and explicit
Chapter 65--66 dependencies are reused where cited. No new independent
verification of every historical reference is claimed.

## Calculation and verification

The symbolic, rational and numerical supplement passes 199,941 checks.
It verifies the Legendre stationary equation and strict concavity, the
radial homogeneous Monge--Ampère determinant of the product ray, the
nonzero determinant for the sum, the energy second derivative 2/3,
the truncated curvature-support energy, simplex marginal masses and
energies in dimensions 1--20, finite constrained entropy lattices, and
the closed-endpoint mass-collapse family. Floating-point entropy
comparisons use tolerance 1e-12; they are not reported as exact-rational
proofs. The analytic proofs and exact symbolic calculations remain the
mathematical evidence.

Scoped reviews before and after rendering find no unlabelled reusable
environments, proofless formal assertions, duplicate labels, nesting errors,
legacy inline delimiters, double-dollar displays or TODO/FIXME/TBD markers.
The legacy writing-audit executable is unavailable; no warning counts from
that executable are claimed.

The project reference checker passes: 425 inputs, 12,045 labels, no missing
inputs, duplicate labels, dangling references or structural defects. All
six checker regression tests pass. The research inventory remains 42 atoms
in twelve environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17. Post-render
scoped and reference checks and `git diff --check` pass.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds with workspace-local TeX Live 2025. The final PDF has
4,110 pages and 19,192,417 bytes, SHA-256
`39808bcc7dfaebe8104550debfd9d1c80edc97c59fa8845a2637f109dfd82fc5`.
Final chapter source SHA-256:
`4b62e042d3250af528c549ba405d5207165ff859da775c33adc9916212303a82`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 52 has zero overfull boxes and zero
LaTeX/package warnings. Nineteen overfull boxes elsewhere and thirteen
duplicate PDF destinations in Chapter 70 remain recorded.

All twenty final chapter pages, physical 3029--3048 (printed 2961--2980),
were scanned and inspected at detail size. Physical 3048 is intentionally
blank. Both adjoining pages 3028 and 3049 were inspected. No reviewed
clipping, overlap, bad glyph, formula overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent or
current-model verifier verdict. Generated PDFs are local review artifacts.
Frozen releases, dated checksum ledgers and research atoms are unchanged.
Verified work remains local pending explicit remote-push approval.
