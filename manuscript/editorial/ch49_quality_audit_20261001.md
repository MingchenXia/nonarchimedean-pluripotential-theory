# Chapter 49 completion audit

Date: 1 October 2026

Base: local Chapter 48 commit `7f9d2bb`.

Scope: `parts/part4/ch49_linear_growth.tex`, with a dependency correction in
`parts/part4/ch34_fs_pl_psh.tex`, under the sequential quality programme.
Chapter 50 is next; the whole-book goal continues. Independent Chapter 72
research remains paused.

## Mathematical and expository review

The standing hypotheses, assertions, proofs, examples, dictionary and source
discussion were reviewed continuously. All 40 formal assertions have proofs:
ten lemmas, six theorems, seventeen propositions and seven corollaries.
All 77 reusable environments have semantic labels; the chapter has 247
labels. The integral projective unibranch, positive-dimensional ample,
trivially valued signature and probability normalization remain explicit.

Substantive repairs include:

- The finite flag argument attains the degree-wise vanishing maximum.
  Linear growth of divisorial valuations uses intersection with an ample
  class without assuming a prime Weil divisor is Q-Cartier. The numerical
  pseudoeffective-threshold identity does require Q-Cartierness. Its
  converse now supplies conductor descent of sections on a nonnormal base.
- The identity T_omega = T_L is exact, as in published Lemma 4.46. Its
  proof uses fixed-class regularization. Lower semicontinuity passes a
  uniform upper bound to a weak limit; scaling rays have linear T.
- Dirac finiteness, the sharp dimensional bounds and the truncation-energy
  argument retain their full proofs. The converse extreme-point argument
  uses normalized Borel restrictions and the full E1 integrability
  characterization, rather than an unproved bounded-test converse.
- The normalized Green envelope is continuous, has height exactly T, and
  gives the sup-norm isometry for every linear-growth valuation. These are
  Proposition 12.14, proved here using the existing domination principle.
  The earlier suggestion that the height identity was only known torically
  was removed. The measure target I-dual remains a quasi-metric, distinct
  from this sup-norm embedding.
- The section formula uses finite maxima and fixed-class approximation.
  Pointwise convergence of psh functions on the linear-growth locus is
  proved in every characteristic via bounded truncations and Proposition
  9.19. Completeness uses compact T-balls and fixed-potential continuity.
  The strong criterion refers to the semantic Chapter 48 implications.
- SNC-test-configuration statements assume smooth X in characteristic zero.
  Interior Lipschitz estimates and the stronger published closed-face
  equicontinuity theorem are distinguished. Divisorial approximation from
  below need not be monotone; its singular-variety resolution route is
  separate from SNC models with generic fibre X. The existing book-level
  Radon–Riesz counterexample is preserved with its actual proof and scope.
- The toric section may be rational. The retraction-order proof uses local
  regular functions and unit denominators; inequalities are not subtracted
  for arbitrary fractions. Real Fubini–Study weights give rational slopes
  with real constants, not necessarily rational PL functions. General
  invariant extension is explicitly quoted from Appendix B.
- The rational-PL atomic measure formula uses the normalized component
  valuation correctly. Bounded invariant approximation is constructed by
  monomial expansion. Locally uniform convex convergence, fixed total mass
  and a cutoff argument pass to the weak real measure limit. A separate
  corollary gives the finite-energy measure formula without circular use
  in the energy proof.
- The bounded toric energy proof integrates first variation using
  almost-everywhere conjugate differentiability, Fubini and the fundamental
  theorem of calculus. Singular conjugates increase by the explicit
  supremum identity. The full strong/L1 statement for arbitrary nets is
  quoted at its exact published scope; the earlier incomplete general
  convergence argument was removed.
- Worked examples keep the P2 family c max(log|m_0|,-1), its correct atom
  and cubic energy, the SNC pair/cone distinction on a blowup, and the
  conic's endpoint psh construction. The factorial-gap branch is proved
  transcendental in every characteristic. Restriction to an algebraic
  branch gives proper support, rather than the earlier purported
  non-Abhyankar linear-growth example. The origin's energy/T ratio is
  undefined. Historical and nontrivial-base comparisons retain their
  actual scope and normalization.

The Chapter 34 dependency correction explains that a regular SNC test
configuration with generic fibre X requires X smooth; cofinality is used
for smooth X in characteristic zero. The piecewise-affine restriction
proof now pulls back flag ideals to the given SNC model and applies the
vertical-ideal Newton-polyhedron lemma. It does not require a common SNC
resolution in positive characteristic. Its final source SHA-256 is
`da641467d1140f3837e9cda63912621ada4f334637d61d1fa77f2aec48d7a7e2`.
This dependency review does not extend the historical Chapter 34 verdict
to the new bytes.

The redundant task list was removed, 2,443 legacy inline math spans were
normalized, and the convention, scope and P2 tables were reformatted.

An auxiliary exact-rational calculation passes 39,110 comparisons:
simplex widths, Green heights and centroid bounds in dimensions 1–10;
the P2 section metric and its symmetry and Lipschitz estimates; higher
degree section supports; the P2 conjugate, mass, energy and first
variation; the conic polynomial and endpoint; blowup metrics; a rational
certificate for the irrational approximation; factorial-gap inequalities;
and the polar-potential coefficient sum. These supplement the written
proofs and are not an independent verdict.

## Direct source interfaces

The primary source is Boucksom–Jonsson, *Global pluripotential theory over a
trivially valued field*, Ann. Fac. Sci. Toulouse 31 (2022), 647–836,
[published PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf).
Downloaded SHA-256:
`50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.

| Locators | Checked interfaces |
| --- | --- |
| Proposition 1.28; Lemma 4.46 | Divisorial linear growth and the exact section/potential exhaustion identity. |
| Proposition 9.19; Theorem 9.20; Theorem 10.3 | Fixed-measure continuity, the full integrability characterization and uniform pairing estimates. |
| Propositions 11.1, 11.3; Theorem 11.4 | Dirac bounds, extreme points and the all-characteristic pointwise topology proof. |
| Lemma 11.7; Theorems 11.9, 11.11–11.13 | Section metric, completeness, growth, bounded-set weak continuity and the Dirac embedding comparison. |
| Corollary 11.15; Question 11.16; Theorems 11.18–11.19 | Strong criterion, the question addressed by the existing counterexample, divisorial density and countable-field separability. |
| Theorem 12.12; Proposition 12.14 | Continuous Green functions, raw envelope, exact height and sup-norm isometry. |
| Appendix A: Theorem A.1, Corollary A.3, Theorem A.4 | Smooth SNC convergence, singular-variety approximation from below and closed-face equicontinuity. |
| Appendix B, especially printed pp. 830–831 | General invariant extension, measure and energy formulas, Green formulas and the full strong/L1 correspondence. |

The relevant Section 11 proofs, Theorem 9.20, Green-function statements and
proofs, and Appendices A and B were read directly. Seventeen primary-source
pages were rendered and inspected: physical 142, 154–161, 165–166 and
182–187 (printed 787, 799–806, 810–811 and 827–832). The fixed-pairing and
domination interfaces also reuse the direct Chapter 47–48 source review.
The non-Q-PL Green examples use the published Green-function paper at
Theorem 60 and Examples 63 and 65, SHA-256
`d79b777408b951380bd00ce74f9917c7769be391022352468503d0405bc92607`,
whose scope was checked in Chapter 47. The toric and Abhyankar literature
locators are identified in the source note; no new direct inspection of
those separate books or papers is asserted.

This is a direct editorial/source audit. The historical research receipts
for the Radon–Riesz counterexample are not extended to the revised source.
No independent-agent or exact-current model-verifier verdict is claimed.
No research atom changes.

## Mechanical and rendered verification

The manual review checked hypotheses, notation, extended-real domains,
nets, proof structure, attribution and delimiters. The limited scoped scan
before and after rendering finds no unlabelled reusable environments,
proofless assertions, duplicate labels, nesting errors, legacy inline
delimiters, double-dollar displays or TODO/FIXME/TBD markers. The standalone
legacy writing-audit executable is unavailable; its old warning counts are
not asserted.

The reference checker passes with 425 inputs and 12,028 labels, no missing
inputs, duplicate labels, dangling references or structural defects. All
six checker regression tests pass. The research inventory remains 42 atoms
in 12 environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17. The scoped and
reference checks were repeated after rendered review; `git diff --check`
passes.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds with workspace-local TeX Live 2025. The PDF has 4,102 pages
and 19,162,373 bytes, SHA-256
`6ae832e275e4a7778bf9e7aa9e0084f14c3c8a53f8b0ff57b3a62e1459dc9502`.
Final chapter source SHA-256:
`30b61901c2b7fc592440eb8b89a5c03e46f617552bde85dbf1c1e9bab53e0385`.

There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 49 has zero overfull boxes and zero
LaTeX/package warnings. The book retains 20 overfull boxes elsewhere and
13 duplicate PDF destinations in Chapter 70.

All 64 chapter pages, physical 2817–2880 (printed 2749–2812), were scanned.
Detail inspection covered 2818, 2820–2823, 2826–2827, 2831, 2833,
2835–2836, 2843–2844, 2846–2847, 2853–2854, 2857–2858, 2861–2867,
2870, 2872–2873 and 2875–2879: 34 detail pages. Adjoining pages
2815–2816 and 2881 were inspected; 2816 is an intentional blank verso.
The three edited Chapter 34 dependency pages, 2134–2136, were inspected.
Only physical 2854 changed after the first rendered review; it was
inspected again in the final PDF. No clipping, overlap, bad glyph,
formula overflow or hierarchy defect remains in the reviewed chapter.

Generated PDFs remain local review artifacts. Frozen releases and dated
checksum ledgers are unchanged. Verified work is committed locally while
explicit remote-push approval remains pending.
