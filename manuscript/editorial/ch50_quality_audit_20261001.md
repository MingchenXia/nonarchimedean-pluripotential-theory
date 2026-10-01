# Chapter 50 completion audit

Date: 1 October 2026

Base: local Chapter 49 commit `716b60b`.

Scope: `parts/part4/ch50_stability.tex`, under the sequential quality
programme. This completes Part IV. Chapter 51 is next; the whole-book
completion goal continues. Independent Chapter 72 research remains paused.

## Mathematical and expository review

The full source, hypotheses, proofs, examples, dictionary and source note
were reviewed. The chapter has 40 formal assertions with proofs or explicit
source interfaces: six lemmas, twelve theorems, twenty propositions and two
corollaries. All 99 reusable environments have labels; there are 352 labels.
The probability normalization of Chapters 46--50, sufficiently divisible
section degrees, envelope hypothesis, and sublc/subklt distinctions remain
explicit. The import register now records principal inputs without claiming
that its short list contains every analytic theorem used in the chapter.

Substantive repairs include:

- A finite flag has at most N+1 distinct members and eventually reaches
  zero. Finite-dimensional d1 uses dimension-weighted sums, the common-basis
  proof identifies the intrinsic relative spectrum, and the three-subspace
  dimension inequality is a sufficient pointwise proof of the triangle
  inequality. Degree-wise normalization is by m, rather than N_m. The
  divisibility-net asymptotic limit is distinguished from an ordinary limsup.
- The raw FS function is bounded and lower semicontinuous, while its upper
  regularization is bounded E1 under the envelope hypothesis. The sup-norm
  adjunction applies to bounded real functions. The full homogenized-norm
  proof supplies the binomial ultrametric estimate, minimality and equality
  of raw FS functions; the exact inverse-norm identity uses the imported
  spectral-radius theorem. A floored half-order norm gives a valid example
  of distinct norms at zero asymptotic distance.
- A normal integral test configuration need not give a homogeneous integral
  norm. The component formula is a floor; homogenization removes it. Uniform
  distance statements use the correct homogeneous domain. The all-real
  finite-type sup-norm isometry is imported directly, without an invalid
  reduction to integral weights. The general volume formula uses obstacle
  energy; under the envelope hypothesis it equals E of regularized FS.
- Quotient and completion theorems retain their exact source scope. The
  compatible metric on E1 is distinguished from the I quasi-metric; general
  measure completeness does not depend on envelopes. The formal MA
  completion deduction is retained with its actual inputs.
- The sharp J/L1 proof assumes concavity on the actual support interval.
  A cone attains the lower constant; an admissible family with an endpoint
  atom approaches the upper constant. The earlier inadmissible two-atom
  example and unsupported extremal classification were removed. Vanishing
  is proved directly from a Dirac spectral measure and distance to a
  translated trivial norm.
- Discrepancy on valuation-space pair cones is separated from its greatest
  lower semicontinuous extension on the whole analytification. Proper-support
  infinite discrepancy requires subklt; the sublc projective-line boundary
  gives a counterexample. The smooth B=0 compact test-configuration skeleton
  formula is a separate source interface. A/T is unbounded already on P2;
  the subklt inequality controls T by A, not conversely.
- Entropy lower semicontinuity is proved for Radon measures and arbitrary
  weak nets using layer-cake sums, inner regularity and continuous minorants.
  It alone supplies neither weak continuity of Mabuchi energy nor a
  finite-energy limit of a minimizing net. Strong density uses fixed-class
  FS regularization. The maximal strong lower semicontinuous extension of
  beta needs entropy recovery and strong continuity of the class derivative;
  density and lower semicontinuity alone are insufficient.
- The infinite-entropy example supplies a bounded T-supported measure and
  a continuous Calabi--Yau potential, hence an actual norm in the FS image.
  Finite divisorial minimum norms use the published measure-support and
  Green-function theorem, rather than a false locality/max-of-Greens proof.
  The filtration threshold deduction first proves that its infimum is real,
  then applies recovery and the divisorial bijection. Rational model testing
  is kept separate from arbitrary real-weight norms.
- Polarization thresholds scale inversely. Divisorial thresholds allow real
  positive rescaling, whereas section-ring and model domains use rational
  polarizations. Mabuchi energy is homogeneous under normalized base change;
  DF generally is not when the original central fibre is nonreduced.
- The new explicit model Proj k[t,x,y,z]/(x^2-tz), with degrees 1,1,2,
  has a normal flat total space and central fibre 2E. Its Q-polarization
  gives v_E=(1/2) ord_p, E.L=1/2, M=0 and DF=1/2. Normalized degree-two
  base change yields a reduced product with both invariants zero. The
  earlier purported nonreduced example from an already reduced base change
  was removed.
- The Ding flag-ideal formula includes the central-fibre boundary: its
  contribution cancels the extra one in Gauss discrepancy. Model scaling
  preserves its domain for positive rational factors; the defining infimum
  explicitly extends to bounded real functions for translations and real
  convex combinations.
- In the log Fano case the exact divisorial threshold is delta minus one,
  by entropy affinity, dual-energy convexity and Dirac testing. The ordinary
  K/divisorial sign and positivity equivalences do not assert numerical
  equality of the ordinary K threshold with the divisorial threshold.
  Li's B=0 scope, Fujita's log-pair theorem, toric delta and LXZ's finite-
  generation/K-stability statements are dated and separated.
- The DNC example on (P1,-K) computes every functional with its displayed
  metric constant. Its anticanonical member has L=-K^log without an extra
  central-fibre shift. The toric F1 destabilization constructs an ample
  product from integral section weights; Q-PL alone does not prove ampleness.
  Reflexive normalization is retained for discrepancy, and polytope methods
  are used only for toric varieties, not arbitrary torus actions.
- The harmonic P1 filtration has curvature on two coordinate rays and a
  diffuse probability MA measure. Its spectral energy, mixed-energy check,
  minimum norm, L1 norm, entropy and Mabuchi value agree. Finite generation
  fails through the curved spectral transform; its maximum is actually
  attained in every even degree. P1 semistability for arbitrary finite-energy
  measures is proved by integrating the pointwise Dirac Fenchel inequality.
- Equation references now have explicit tags. The dictionary, dated table
  and historical discussion reflect the revised scopes, including the
  February 2022 preprint numbering of LXZ Theorem 1.6. Redundant orientation
  prose and legacy inline delimiters were removed; overflowing formulas
  were split and reviewed on the page.

## Direct source interfaces

Seven primary PDFs were read at the relevant statements and proofs. They
are stored in the ignored `source_material/ch50_audit_20261001` directory;
PDF extraction was checked against rendered pages.

| Source and checked version | Principal interfaces |
| --- | --- |
| BJKS1, published 2025, DOI 10.5802/aif.3668 | Theorem 2.16, Corollary 2.18, Theorems 5.1/5.5/5.11, Lemma 6.17, Theorems 6.29/6.30/7.13, Corollary 7.16, Example 7.14, Theorem 7.22, Appendix A: spectral radius, volume, completion, raw/regularized FS, divisorial norms, S and component floors. |
| BJKS2, arXiv 2206.09492 v3, 30 August 2023 | Proposition-Definition 2.6, Theorem 2.15, Theorem 3.10, Theorems 4.14/5.8/5.13, Conjecture 5.15, Appendix A.2--A.6/A.10: derivative continuity, entropy recovery, filtration thresholds and discrepancy extension. |
| BHJ17, arXiv 1504.06568 v3, 30 November 2016 | Propositions 7.15--7.16/7.27/7.29, Theorem 8.6: nonreduced correction, base change, Ding threshold and uniform Ding/Mabuchi comparison. |
| Fuj19, arXiv 1602.00901 v2, 19 September 2016 | Theorem 6.5: the log-pair valuative uniform/semistable criterion. |
| Li17, arXiv 1512.07205 v5, 18 July 2017 | The valuative criterion for Q-Fano varieties, B=0. |
| BJ20, arXiv 1706.04548 v2, 10 February 2020 | Theorem F and Corollaries 7.15--7.17: toric delta and the variety-level threshold package, with log-pair scope distinguished. |
| LXZ22, arXiv 2102.09405 v3, 12 February 2022 | Theorems 1.1/1.2/1.6: finite generation below (n+1)/n, divisorial attainment and special degeneration, K-stability versus uniform K-stability. Theorem 1.3 is a different result and is not cited for that equivalence. |

PDF SHA-256 values, in the table's order:

1. `f68e2a7fff4b0d9eb8541166ace4b4e3dbb974c0eebda876ea65c8dc10e4b743`
2. `a558e535802038554ffd1fd17c81a95504267bff25a706bf6e4bb82e535ed224`
3. `6f86bd9fb98b57a1b31d32ad80c9c2f3638b63ebe1ed43fe30976b6aeed0aa2a`
4. `ddcc87d81e32f4ed6d3ce5a1f2cf3dbe9d6b32ad28194ca89b9d6f7930ab714c`
5. `49d2b82ea319e2d17ce223578347c5a852e0b15ee0697f54c9ae1b48d6097570`
6. `51ea49c150d1a542bb9d6e90bc57874375f2bc68c507e74fe14115dd2f03039a`
7. `a48739fffd7045c61151b3ab5c15209914357a74ab0e9878e7b29ed7f9c73fec`

Twenty primary-source pages were rendered and inspected: BJKS1 physical
34, 60, 62, 67, 75, 78, 84, 88; BJKS2 18, 27, 38, 40, 43;
BHJ17 51, 58; Fuj19 28; Li17 8; BJ20 40; LXZ22 1, 2.
Chapter 34--49 source interfaces are reused where explicitly cited.
No new direct inspection of the other historical references is asserted.

## Calculation and verification

The exact-rational/symbolic supplement passes 321,388 comparisons. It checks
66 flags and all 4,356 pairs in F2^3, all 287,496 triples for the d1 triangle
inequality, joint spectra and integral/d-infinity formulas, 10,201 floor
superadditivity cases and 10,100 homogenization errors. It independently
integrates the DNC L1 expression and checks 99 Ding/Mabuchi and J/L1 cases
each, the harmonic energy/pairing/entropy/L1 expressions, F1 volume and
barycenter, 240 admissible concave-root tail bounds and twelve cone equality
cases. These computations supplement the written proofs.

The scoped review before and after rendering finds no unlabelled reusable
environments, proofless formal assertions, duplicate labels, nesting errors,
legacy inline delimiters, double-dollar displays or TODO/FIXME/TBD markers.
The legacy writing-audit executable is unavailable; no historical warning
counts from that executable are claimed.

The project reference checker passes: 425 inputs, 12,028 labels, no missing
inputs, duplicate labels, dangling references or structural defects. All
six checker regression tests pass. The research inventory remains 42 atoms
in twelve environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17. Post-render
scoped and reference checks pass, as does `git diff --check`.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds with the workspace-local TeX Live 2025 installation. The
PDF has 4,102 pages and 19,154,421 bytes, SHA-256
`330cf8cb045079ac40ab34fdb8d8ecfd12595f7a278a7d54df6adbcd63b48851`.
Final chapter source SHA-256:
`2ebb217676e90ee7657506c62265c365f06b43e63c1233ea53c39147cb48de4f`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 50 has zero overfull boxes and zero
LaTeX/package warnings. Nineteen overfull boxes elsewhere and thirteen
duplicate PDF destinations in Chapter 70 remain recorded.

All 72 chapter pages, physical 2881--2952 (printed 2813--2884), were scanned
in both the pre-final and final builds. Thirty-three pages were inspected
at detail size in the first review; eighteen were inspected in the final
build, for 43 distinct chapter detail pages across the two reviews. Final
detail pages are 2882, 2897, 2905, 2911, 2913, 2919, 2922, 2928--2929,
2932, 2935--2939, 2941--2942 and 2948. All pages reflowed by the final edits
were rescanned. Adjoining physical pages 2880 and 2953 were inspected;
2953 is the Part V title. No reviewed chapter clipping, overlap, bad glyph,
formula overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent or
current-model verifier verdict. No research atom is changed. Generated
PDFs are local review artifacts; frozen releases and dated checksum ledgers
are unchanged. Verified work remains local while explicit remote-push
approval is pending.
