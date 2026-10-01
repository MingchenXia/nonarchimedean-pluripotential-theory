# Chapter 54 completion audit

Date: 1 October 2026

Base: local Chapter 53 commit `3494844`.

Scope: `parts/part5/ch54_operations_trace.tex`, under the sequential quality
programme. Chapter 55 is next; the whole-book goal continues. Independent
Chapter 72 research remains paused.

## Mathematical and expository review

The complete source, nine formal assertions, four examples and conventions
were reviewed. All formal assertions have proofs or exact imports. All 28
reusable environments have semantic labels; there are 92 labels, including
all seven sections.

The principal repairs are:

- Componentwise order uses the order-reflecting evaluation proved in Chapter
  53. Addition now checks compatibility through the test-curve sum theorem.
  The two-background sum formula explicitly uses Kähler perturbations and
  the exact common-smaller-component projection theorem. Translation and
  maximum also explain their transition compatibility.
- Suprema construct compatible components using finite joins and increasing
  ideal-envelope continuity. Choquet reduction selects a countable subfamily
  at one component and applies its uniqueness; it does not assert cofinality
  of arbitrary metric indices. The decreasing-net proof retains its positive
  perturbation mass floor. The level formula for positive rescaling and the
  order-isomorphism proof of its supremum and infimum rules are explicit.
- The existing uniform perturbation estimate is checked as an integrated
  mixed-mass inequality, not an inequality between currents. The decreasing
  volume-drop example retains the two distinct iterated limits. Its strict
  drop occurs even with positive limiting volume.
- Analytic trace uses the normalization of an irreducible analytic subset
  and the normal-space pluripotential interface. Restrictions are taken only
  after smooth-ambient quasi-equisingular approximation. The exact common
  background, mass floor, cross-comparison and decreasing-net hypotheses
  remain visible. The paper's more restrictive continuity lemma is not
  silently identified with the lecture's net theorem.
- Ideal-class saturation now handles the ambient space, divisors and higher
  codimension separately. The trace is an ideal-class input with a P-class
  output. Ideal-goodness does not select a unique raw potential in that
  output class. The exact lecture and accepted-manuscript interfaces are
  identified at their points of use.
- The metric trace proof explicitly deduces pseudoeffectivity of the target
  base class from normalized compactness as the perturbations shrink. Its
  uniform positive mass floor, ideal-model concavity, initial level, retained
  cutoff, transition compatibility and birational identity are checked before
  invoking the inverse-limit definition. Birational pullback on singular
  normalizations uses the stated unibranch-space source.
- A new example proves that ambient trace is the original metric, and that
  point trace records its zero-Lelong cutoff with dimension-zero volume one.
  The existing hyperplane example retains its cutoff level. Equation tags
  follow reading order. Forced page breaks and a trace-calculus minipage
  wrapper were removed; inline math and section navigation are standardized.
- The source note distinguishes the lecture's big standing classes from the
  pseudoeffective base classes allowed by the component proofs and the checked
  operations preprint. Its final layout was tightened after rendered review.

## Direct source interfaces

Three primary PDFs were checked at their actual statements and proofs.
Fifty-seven source pages were rendered and inspected.

| Source and version | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Xia, supplied snapshot dated 18 July 2026, matching the historical pin | Canonical approximation and comparison; positive-floor dS convergence; envelope and operation continuity; Sections 8.1--8.2 trace on normalizations; sum and supremum calculus; Section 13.2 operations and trace; Appendix B.3 normal spaces | 49--50, 143, 145, 226, 228, 231--232, 237, 239--243, 246--247, 254, 274--283, 326--327, 333--334, 443--447, 449--451, 520--521 |
| Xia, arXiv 2312.17150 v3, 22 October 2024 | Proposition 2.8; Section 4 standing scope, operations, decreasing nets, trace domain and Section 4.8 birational functoriality | 5--6, 13--16, 18--20 |
| Darvas--Xia, arXiv 2403.08259 v2, 13 March 2026, accepted manuscript | Definitions 3.1 and 3.5; trace comparison, ideal dependence, sum and scaling; Lemma 3.12 continuity hypotheses and Example 3.13 increasing counterexample | 10--16 |

PDF SHA-256 values, in that order:

1. `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`
2. `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9`
3. `5d6f43d96be101f6aa1a3ddbdd92b5bc49131a0deabbf199e03111d6c0fbaa3c`

The PDFs are reused from ignored Chapter 51 and 53 source caches. Numbered
operations-paper locators refer to v3, separately from its subsequent
publication. The accepted trace manuscript is separately cited from the
older 2024 entry. Its smooth-submanifold results do not alone supply the
chapter's full normal-target, P-valued net calculus; that interface is
checked directly in the supplied lecture.

## Verification and rendered review

The symbolic and exact-rational supplement passes 74,374 checks for the
volume-drop profiles and iterated limits, uniform perturbation polynomial,
increasing trace mass gap and dimensional mass scaling. These checks verify
algebraic calculations; the analytic theorems retain their explicit imports.

Scoped reviews before and after rendering find no unlabelled reusable
environments, proofless formal assertions, duplicate labels, nesting errors,
legacy inline delimiters, double-dollar displays or TODO/FIXME/TBD markers.
The legacy writing-audit executable is unavailable; its warning counts are
not claimed. The reference checker passes for 425 inputs and 12,069 labels,
without missing inputs, duplicates, dangling references or structural errors.
All six checker regression tests pass. The inventory remains 42 atoms in
12 environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17. Post-render scoped and
reference checks and `git diff --check` pass.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds with workspace-local TeX Live 2025. The PDF has 4,114
pages and 19,213,194 bytes, SHA-256
`787504de38d41716a6937381273251e80507ef961df47adea223e52e3e41b18a`.
Final chapter source SHA-256:
`88a938f762f6fa99d4a057b86ac8a86e4d670d6e5c0749806902b616a35f4edd`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 54 has no overfull boxes or LaTeX/package
warnings. Nineteen overfull boxes elsewhere and thirteen duplicate PDF
destinations in Chapter 70 remain recorded.

All twenty chapter pages, physical 3063--3082 (printed 2995--3014), and both
adjoining seams were inspected at detail size. After shortening the closing
source note, its final three pages were reinspected; the preceding pages
retain the reviewed layout. Physical 3082 is intentionally blank. Earlier
chapter renders were also scanned throughout. No reviewed clipping,
overlap, bad glyph, formula overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent verifier
verdict. Generated PDFs remain local review artifacts. Frozen releases,
dated checksum ledgers and research atoms are unchanged. Verified work
remains local pending explicit remote-push approval.
