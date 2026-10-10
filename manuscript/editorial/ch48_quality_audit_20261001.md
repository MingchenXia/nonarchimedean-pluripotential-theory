# Chapter 48 completion audit

Date: 1 October 2026

Base: local Chapter 47 commit `35b38db`.

Scope: `parts/part4/ch48_strong_topologies.tex`, under the sequential
chapter-quality programme. Chapter 49 is next; the whole-book goal continues.
Independent Chapter 72 research remains paused.

## Mathematical and expository review

The standing hypotheses, assertions, proofs, examples, dictionary, and source
discussion were reviewed continuously. All 31 formal assertions have proofs:
four lemmas, six theorems, twenty propositions, and one corollary. All 64
reusable environments have semantic labels; the chapter has 192 labels.
The positive-dimensional ample, integral projective unibranch, trivially
valued signature and probability normalization remain explicit.

Substantive repairs include:

- Strong potential convergence bounds J before invoking fixed-measure
  continuity. Completeness is proved using bounded J-sublevels, weak
  compactness, energy upper semicontinuity, and Proposition 9.19. The
  published completeness interface is Theorem 12.8, not Theorem 12.4.
  The proof does not assume an admissible envelope of a tail infimum.
- Strong measure completeness uses the quasi-triangle estimate, bounded
  dual energy, uniform pairing estimates, and decreasing approximation.
  No uncontrolled family of almost maximizers is used to infer convergence.
  Polarization independence concerns the measure space and its topology,
  rather than a literal equality of potential spaces.
- The potential gauge is distinguished from the metric d1. Their common
  topology alone does not establish a global comparison of values or
  Cauchy nets. The square-root curve metric has a direct proof.
- Capacity uses the fixed test range [-1,0]. The mixed CLN estimate retains
  its probability normalization. The capacity-integral finite-energy
  criterion is sufficient; it is not asserted as an equivalence.
- Quasicontinuity uses correctly directed regularization indices and
  compact sets without an unsupported nested-exhaustion claim. Decreasing
  convergence in outer capacity includes the relative-open extension
  argument. Sequence extraction from a net is not declared cofinal.
- Negligible-set nullity uses Lemma 13.19 and its actual compact-set proof.
  Theorem 13.29 supplies increasing outer-capacity continuity; it is not
  cited as a general capacitability or strong-subadditivity theorem.
- The lower-semicontinuous obstacle proof supplies uniform bounds,
  continuous obstacle approximation, strong convergence of envelopes and
  their measures, and the fixed-measure pairing limit. Monotone convergence
  is applied to a fixed measure, rather than to moving measures. Signed
  integrals and the empty-set height convention are explicit.
- Curve examples distinguish the graph probability measure of any psh
  profile from the finite-energy operator. Open and closed tails use the
  correct right and left derivatives and retain corner atoms. The
  uncountable-endpoint example explicitly proves that its set is Borel and
  has inner capacity zero but outer capacity one. The quarter-power
  example computes energy through bounded truncations before using MA.
- Scope statements retain the analytic role of ampleness and the envelope
  property. The source history distinguishes d1 from the I gauge and uses
  the trivially valued Green-function examples at their exact locators.

The redundant task list was removed, 1,900 legacy inline math spans were
normalized, and the dictionary and wide curve formulas were reformatted.

An auxiliary exact-rational calculation passes 33,815 comparisons. It checks
degree-dependent two-ray I/J formulas, dual energy and midpoint defects,
root and corner masses, capacity competitors, the optimized measure/capacity
bound, the square-root metric inequality, and the extraction-series bounds.
These supplement the written proofs; they are not an independent verdict.

## Direct source interfaces

The primary source is Boucksom–Jonsson, *Global pluripotential theory over a
trivially valued field*, Ann. Fac. Sci. Toulouse 31 (2022), 647–836,
[published PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf).
Downloaded SHA-256:
`50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.

| Locators | Checked interfaces |
| --- | --- |
| Proposition 9.19; Theorems 10.2–10.3 | Fixed-measure continuity on bounded J-sublevels, quasi-triangle and uniform pairing estimates. |
| Theorems 10.12, 10.14, 10.16 | Strong measure criteria, completeness proof, polarization independence. |
| Theorems 12.4–12.5, 12.8 | Strong potential criteria, increasing-net continuity, completeness under the envelope property. |
| Theorem 13.1; Lemma 13.2 | Lower-semicontinuous obstacle contact and negligible-set nullity. |
| Section 13.2, especially Theorem 13.9 and Corollary 13.10 | Capacity estimates, fixed-class quasicontinuity and capacity convergence. |
| Theorem 13.14; Theorem 13.17 and Lemma 13.19 | Alexander–Taylor comparison and the pluripolar/negligible/outer-capacity-zero equivalence. |
| Theorem 13.29 | Increasing continuity of outer capacity, with its actual statement and proof. |
| Proposition 7.20 and Appendix B | Curve graph measures and the relevant finite-energy examples. |

Rendered primary-source pages for Theorems 10.2, 10.12, 10.14 and 10.16,
quasicontinuity, negligible-set nullity, and Theorem 13.29 were inspected.
The Proposition 9.19, Theorem 12.8, and obstacle interfaces reuse the direct
source review in Chapter 47. Boucksom–Jonsson's published Green-function
paper, SHA-256 `d79b777408b951380bd00ce74f9917c7769be391022352468503d0405bc92607`,
is cited at Theorem 60 and Examples 63 and 65 in the historical discussion;
their valuation scope was checked in Chapter 47. This is a direct
editorial/source audit, not an independent-agent or exact-current
model-verifier verdict. No research atom changes.

## Mechanical and rendered verification

The manual review checked hypotheses, notation, extended-real domains, nets,
proof structure, attribution, and delimiters. The limited scoped scan before
and after rendered review finds no unlabelled reusable environments,
proofless assertions, duplicate labels, nesting errors, legacy inline
delimiters, double-dollar displays, or TODO/FIXME/TBD markers. The standalone
legacy writing-audit executable is unavailable; its historical warning
counts are not asserted.

The reference checker passes with 425 inputs and 12,025 labels, no missing
inputs, duplicate labels, dangling references, or structural defects. All
six checker regression tests pass. The inventory remains 42 atoms in 12
environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17. The scoped scan and
reference checker were repeated after rendering; `git diff --check` passes.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds with the workspace-local TeX Live 2025 setup. The PDF has
4,102 pages and 19,166,119 bytes, SHA-256
`6411d69f4b53765fe84188cc3fbf05491128641b166beb12bae65f2443ffc494`.
Final source SHA-256:
`b89b95716933d4a0851afa4afb9552974f5037f6298eb987973d915f0fed6312`.

There are no unresolved references or citations, missing glyphs, rerun
requests, or fatal errors. Chapter 48 has zero overfull boxes and zero
LaTeX/package warnings. The whole book retains 20 overfull boxes elsewhere
and 13 duplicate PDF destinations in Chapter 70.

All 58 chapter pages, physical 2759–2816 (printed 2691–2748), were scanned;
2816 is an intentional blank verso. Detail inspection covered physical
2760–2763, 2772–2773, 2776, 2778, 2781–2782, 2784–2786, 2788, 2790,
2796–2798, 2803, 2806–2807, 2810–2811, and 2813–2814. Adjoining pages
2757–2758 and 2817 were inspected. Comparison of the final PDF with the
first reviewed excerpt identified only three subsequently changed pages,
2773, 2782 and 2788; all three were inspected again at full resolution.
No clipping, overlap, bad glyph, formula overflow, or hierarchy defect
remains in the reviewed chapter.

Generated PDFs remain local review artifacts. Frozen releases and dated
checksum ledgers are unchanged. Verified work is committed locally while
explicit remote-push approval remains pending.
