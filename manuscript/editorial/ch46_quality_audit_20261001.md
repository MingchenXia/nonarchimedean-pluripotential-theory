# Chapter 46 completion audit

Date: 1 October 2026

Base commit: `3a9581ee911788c8d934ddf3d02fbf175947d360`.

Scope: `parts/part4/ch46_bj_energy.tex`, following the sequential chapter-quality
programme. Chapter 47 is next. The continuing goal is the whole manuscript;
independent Chapter 72 research remains paused.

## Mathematical and expository review

The chapter's assertions, proofs, definitions, examples, warnings, dictionary,
and provenance discussion were reviewed continuously. All 28 formal assertions
have immediately following proofs: five theorems, eleven propositions, six
lemmas, and six corollaries. All 68 reusable environments have semantic labels,
including the important box and five warnings. There are 173 chapter labels.

The standing signature retains integral projective unibranch varieties over
an algebraically closed trivially valued field, arbitrary characteristic,
real numerical classes, and the ample-class envelope inputs established in
Chapter 45. Auxiliary mixed slots use dimension at least one. The chapter's
probability Monge–Ampère convention is explicitly distinguished from the
book's unnormalized convention, including the factor in the energy.

Substantive revisions include:

- Vertical negativity uses relatively nef classes, an ample perturbation,
  and a base twist before applying the global Hodge-index inequality. It
  does not assert global nefness on the compactified test configuration.
- The atomic measure is proved on a fixed model, with an arbitrary PL test
  function on a dominating model and the explicit pushforward of its
  vertical divisor. PL density then supplies uniqueness as a Radon measure.
- The extension argument keeps fixed-class decreasing nets, states the
  enlarged real PL majorant family used for translations and scaling, and
  uses the finite divisorial maximum formula for joint upper semicontinuity.
- Strictness of the energy bound uses positive atomic weights from a
  relatively ample representative rather than an unsupported equality case
  of Hodge index on a singular model.
- The envelope-dependent continuous-competitor argument is separated from
  the foundational pairing construction. Continuous obstacles, admissibility,
  compactness, and the extremal function have explicit roles.
- Locality first uses the rational PL crossing lemma without resolution.
  Its finite-energy passage uses weighted convergence of signed measures,
  subtracts the two integrable limits, and divides on the strict Borel set.
  Ordinary weak convergence alone is insufficient for that passage.
- Comparison uses Borel strict-inequality sets. Integrability is almost
  everywhere for the actual mixed measures; full mass on the linear-growth
  locus is not inferred from finiteness of potentials there.
- The deferred domination principle has the exact measure hypothesis:
  the dominating finite-energy potential supplies the almost-everywhere
  measure. No difference of two pole values is treated as defined.
- Irrational scaling need not preserve rational PL functions. The argument
  for real scaling instead uses uniform estimates on bounded psh functions
  and decreasing approximation for the energy.
- Homogeneous potentials and their truncations have separate domains.
  The conditional mixed-measure limit assumes convergence of the entire
  truncation family, proves invariance and fixed-point support, and asserts
  no extension of the finite-energy operator outside its domain.
- The curve's proper-support endpoint masses and normalization degree are
  computed explicitly. They do not imply a general bijection between
  invariant measures and nef b-classes. Nonzero homogeneous slices in the
  Legendre discussion may have infinite negative energy.
- Curve, toric surface, mixed-polarization, and discrete-valuation examples
  retain their degree, mass, sign, and normalization factors. Positivity of
  an atomic formula alone is not used to identify the psh range. Zero volume
  and the extremal function alone do not define a relative finite-energy
  theory.

The redundant task list was removed, 1,244 legacy inline math pairs were
normalized, and comparison and dictionary tables were recast in two columns.
The final projection and comparison displays were split into aligned rows
after rendered inspection.

An auxiliary exact-rational check passed 20,184 comparisons. It covers the
projective-line energy and atomic masses for degrees one through seven,
translations and positive class scaling, the two-corner example, the toric
surface energy and mixed masses, and the infimal-convolution allocation at
all relevant breakpoints on a rational grid. These checks supplement the
written geometric and convexity arguments.

## Direct source interfaces

The primary source was Boucksom–Jonsson, *Global pluripotential theory over a
trivially valued field*, Ann. Fac. Sci. Toulouse 31 (2022), 647–836,
[published PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf).
Downloaded SHA-256:
`50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.

The directly checked interfaces are:

| Source locators | Uses and scope |
| --- | --- |
| Proposition 3.14, Lemmas 3.15 and 3.24, Propositions 3.25–3.28 | PL pairing, fixed-model atomic measure, monotonicity, vertical negativity, concavity, telescope and tangent formulas, Dirichlet form. The negativity locator is Lemma 3.24. |
| Example 4.13, Corollary 4.17, Lemma 4.26, Proposition 4.28 | Curve psh criterion, finiteness on the linear-growth locus, finite divisorial maximum formula, and continuous suprema. |
| Theorem 7.1; Propositions 7.2, 7.4, 7.5 and 7.7 | Monotone extension and joint upper semicontinuity, translations and scaling, continuous fixed slots, uniform estimate, and normalization. |
| Definition 7.8; results 7.9–7.20 | Finite-energy class, mixed finiteness, vector-space extension, signed Radon measures, integrability, normalization, decreasing continuity, and the curve graph formula. |
| Proposition 7.21(ii), Theorem 7.40, Lemma 7.43, Corollary 7.44 | Weighted convergence, locality, PL crossing, and comparison. Result 7.21 is a proposition. |
| Corollary 10.6 | Domination with the finite-energy comparison potential's Monge–Ampère measure. It is deferred to Chapter 47, not proved in this chapter. |
| Appendix B | Toric Monge–Ampère formula for bounded toric psh functions and extended-real energy formula; finite energy corresponds to integrability of the conjugate. |

Rendered primary-source pages for vertical negativity, extension, weighted
convergence, crossing/locality, and domination were also inspected. Chapter
interfaces from Chapters 20, 26, 33–35, and 45 were checked where used. This
is a direct editorial/source audit, not an independent-agent or exact-current
model-verifier verdict. No research atom changes.

## Mechanical and rendered verification

The manual house review checked hypotheses, notation, extended-real domains,
proof structure, nets, semantic labels, attribution, and delimiters. A limited
mechanical scan before and after rendered review found no unlabelled reusable
environments, proofless assertions, duplicate chapter labels, environment
nesting errors, legacy inline delimiters, double-dollar displays, or unresolved
TODO/FIXME/TBD markers. The legacy standalone Mingchen writing-audit executable
is unavailable here; its historical warning counts are not asserted.

The project reference checker passes with 425 inputs and 12,022 labels, with
zero missing inputs, duplicate labels, dangling references, or structural
defects. All six checker regression tests pass. The open-problem inventory
remains 42 active atoms in 12 Chapter 72 environments, with tiers T1=0, T2=3,
T3=7, T4=15, T5=17. The scoped scan and reference check were repeated after
rendered review. `git diff --check` passes.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex` build
succeeds with the workspace-local frozen TeX Live 2025 font setup. The PDF has
4,106 pages and 19,196,260 bytes. PDF SHA-256:
`fbcab479ea05550395e759d06b37013843b48ae777b5b7d91fc5b7677323f6e4`.
Final chapter source SHA-256:
`fb2abf67fd3eb5beb412de446259a0be2e236425c177658c2b938c89e4297e7e`.

The final log has no unresolved references or citations, missing glyphs,
rerun requests, or fatal errors. Chapter 46 has zero overfull boxes and zero
LaTeX/package warnings. The full book has 23 overfull boxes outside Chapter 46
and 13 duplicate PDF destinations in Chapter 70; no globally clean layout is
claimed.

All 56 chapter pages, physical 2645–2700 (printed 2575–2630), were scanned;
page 2700 is an intentional blank verso. Full-resolution inspection covered
physical pages 2646, 2650, 2652, 2653, 2656, 2662, 2665, 2666, 2673, 2680,
2682, 2684–2686, 2688, 2690, 2691, 2695, and 2696. The Chapter 45 closing
pages 2643–2644 and Chapter 47 opening 2701 were inspected as adjoining seams.
The two repaired displays were inspected from the final PDF. No clipping,
overlap, bad glyph, formula overflow, or hierarchy defect was found.

The generated full book and chapter excerpt are local review artifacts.
Frozen release artifacts and dated checksum ledgers are unchanged.
