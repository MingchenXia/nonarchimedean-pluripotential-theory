# Siu dependency boundary in reader routes and energy applications

Date: 5 October 2026. Baseline: `375b88b906d47ce1fb919ddae3d1ee068aea0209`.
This continuation propagates the [4 October correction](bj22_siu_proof_boundary_audit_20261004.md)
into remaining reader summaries and downstream applications. Critical
homogeneous division remains the additional assertion `(SD)_k`. No
counterexample to BJ22 Theorem 6.21, general proof repair, or open-problem
solution is claimed.

## What changed

Sixteen active TeX inputs change. Chapters 1, 7, 23, 32, 34, 36 and 37 now
describe the general unibranch envelope argument as conditional wherever
these reader routes use it. Divisorial determination, decreasing closure,
fixed ample-class regularization and the separately proved smooth regimes
keep their respective scopes. Chapter 45's dictionary distinguishes the
conditional sufficiency direction from the independent ample-class
necessity theorem and the published equivalence of envelopes and
compactness. Its historical conclusion no longer says the general
conjecture is retired or that every later envelope hypothesis is
unconditionally discharged. The last stale paragraph was found during
actual-page review and corrected before the final build.

Chapters 46–50 now retain the envelope property in the class used as an
explicit standing input for dependent compactness, existence and
completeness assertions. Discharging it through Chapters 37–45 requires
`(SD)_k`; an independent theorem can supply only its own established
instances. The Calabi–Yau corollary and its scaling corollary in Chapter 47
explicitly assume that envelope property. Finitary intersection theory
and the fixed-real-ample decreasing approximation have separate
provenance and are not presented as consequences of critical division.
Chapter 67's singular-boundary discussion and Appendix L reflect the
same dependency boundary.

Chapter 57 instead uses the independent all-class envelope theorem of
the published BJ addendum, Theorem A (2024), recorded in Chapter 36.
Its standing variety is a connected smooth complex projective manifold.
That source applies in this regime; the comparison of suprema need not
invoke the conditional general unibranch theorem. The deep comparison
and realization inputs already attributed in that chapter are retained;
this correction does not freshly verify every proof in those papers.

## Why a scaling-and-compactness shortcut is not a repair

The following attempted route was checked and rejected as circular. For
normal projective `X`, homogeneous `psi <= ell_D` and rational `t > 1`,
the separate strict fixed-coefficient division argument gives a residual
`r_t` in the class `t alpha - [D]` with the additive identity
`r_t + ell_D = t psi`. On divisorial points this says
`r_t = t psi - ell_D`; as `t` decreases to one these residuals increase,
since homogeneous `psi` is nonpositive. Their divisorial candidate limit
is the critical residual. This does not by itself establish membership
in the limiting psh class or the additive identity at proper support.

Invoking general normalized psh compactness would reintroduce the missing
input. BJ22 Theorem 5.11 equates that compactness with the envelope
property. The homogeneous compactness statement, Corollary 6.22, itself
uses Theorem 6.21 to remove an ample buffer. Neither is an independent
general endpoint closure theorem. BJ Green-functions Proposition 17 uses
an independently known envelope property in its smooth characteristic-zero
setting. It remains valid in that scope and does not repair arbitrary
normal division as an input to the same envelope argument.

Fresh source readings covered BJ22 text lines 3707–3788 (Theorem 5.11),
4310–4367 (Theorem 6.21 and Corollary 6.22), the Green-functions proof at
610–715, and the addendum's standing scope and Theorem A at 1–90.
Eight selected actual primary pages were viewed: BJ22 physical pages
79–80 and 91–92, addendum pages 2–3, and Green-functions pages 1 and 13
(the former is its publication cover). Earlier full-source checks remain
dated evidence; no fresh full reading of these three papers is claimed.

## Source and artifact checks

The final full book has **4,255 pages**, 19,811,404 bytes, SHA-256
`95273bde05c0994eb82e3f255dbb1b9976ef57d2963c99d604ab021f0f014623`.
There are 425 active TeX inputs, 12,596 unique labels, 173 valid reference
ranges, 5,491 citation groups and 283 cited keys in 582 bibliography
entries. Source references and per-file structure pass. The unchanged
Chapter 72 inventory check passes for 42 active atoms in twelve families.
The catalogue source and its 86-page PDF are byte-preserved.

The 409 other active inputs, all 108 protected Appendix M–N inputs, the
strict-division statement/proof and Chapter 40 are byte-preserved. Formal
environment counts, types, order and label order are unchanged. Seven
counted blocks change: three remarks, two Calabi–Yau corollaries and two
proofs. All other counted theorem/proposition/lemma/corollary/definition/
example/remark/proof blocks in the sixteen changed files are preserved.
The changes restrict hypotheses or correct provenance; they introduce
no new mathematical result or independent production-model receipt.
Historical verification packets are not extended to these modified bytes.

The first build exposed an index hyperlink warning for the grouped pages
`138,\\,139`. The index style now uses comma-space, the separator parsed
by hyperref. Regenerating the index and recompiling removes the malformed
target. The final log has zero TeX errors, package or pdfTeX warnings,
overfull boxes, unresolved references/citations or rerun requests. The
954 underfull diagnostics are retained and disclosed. BibTeX has zero
warnings; makeindex accepts 728 entries, rejects zero and writes 964 lines
with zero warnings.

Navigation checks cover 21,439 named destinations, 46,176 internal links,
2,434 contents entries, six parts and 397 distinct numeric index page
destinations, with no invalid target. The 163 external URL links are
counted; their remote availability is not certified. Fifty-five selected
book pages were actually reviewed in fourteen contact sheets. After the
last Chapter 45 wording change, 52 selected pages remained pixel-identical
to the viewed first review; the three changed pages (47, 2713, 2714) were
freshly viewed. This is a scoped dependency and layout review, not another
complete reading of the 4,255-page book.

The [manifest](siu_downstream_scope_manifest_20261005.json),
[source closure](siu_downstream_scope_source_closure_20261005.sha256) and
[artifact record](siu_downstream_scope_artifacts_20261005.json) pin the
edition, visual scope and exported source archive. The archive contains
the active sources and identified build/support records; member bytes
are checked against the workspace. A fresh isolated archive compilation
is not claimed. The [revision-sensitive literature audit](revision_sensitive_arxiv_audit_20261005.md)
records the separate FGK v3 reading and the bounded updated-date search.
Continue noncircular Siu investigation and related primary-source research.
