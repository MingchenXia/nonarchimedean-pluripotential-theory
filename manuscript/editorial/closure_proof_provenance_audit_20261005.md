# Closure proof provenance and fixed-pole diagnostic

Date: 5 October 2026. Baseline: `14da2a0d6a4370341054935b960c1afd8e6a32f7`.
This is a source-provenance correction and a research checkpoint. It does
not admit a new theorem, a general algebraic psh closure repair or a
critical Siu division proof.

## Corrected book language

Chapter 34 previously described the printed diagonal mechanism in BJ22
Lemma 4.6 as resolving the varying-class decreasing-limit issue. At a
point where a reference function is minus infinity, the strict inequality
in its equation (4.5) cannot hold. Equivalently, convergence of continuous
exponentials need not give a positive gap between the functions near a
common zero. The open-negative-set covering step therefore is not supplied
by the printed hypotheses alone.

The closure warning now states this proof boundary. The imported basic
closure proof identifies BJ22 Theorem 4.5 as a published input and does
not describe the abstract diagonal step as independently repaired. The
regularization proof and final source note point back to the same warning.
Appendix L records the issue separately from the changing-divisor-
coefficient error in Theorem 6.21. A repeated chapter-reference phrase in
the compactness warning is also corrected.

Only Chapter 34 and Appendix L change among the 425 active TeX inputs.
Every formal theorem, proposition, lemma, corollary, definition, example
and remark statement in those files retains its exact bytes; label order
is preserved. Two Chapter 34 proof blocks change their source explanation.
No formal environment or label is added. The 108 protected Appendix M--N
inputs, strict division text, Chapter 40, bibliography and styles are
unchanged. Historical production receipts are not extended to new bytes.

The earlier warning about Theorem 6.21 remains controlling: the general
envelope assembly requires `(SD)_k`. No counterexample to the Siu theorem
or to algebraic psh Theorem 4.5 is claimed. The restricted reconstructions
in the preceding research notes remain outside active TeX, pending
independent admission.

## Strengthened abstract candidate, outside active TeX

The [fixed-pole note](abstract_fixed_pole_closure_diagnostic_20261005.md)
uses `K=[0,1]`, `rho(i)=1/i` and
`f_(i,j)=max(log x,(1/i)log x-j)`, with every real translation admitted.
All stages and limits have the identical pole `{0}`. For each fixed `i`,
the stages decrease to the same continuous extended-real function `log x`.
Thus the outer function sequence can be constant while its parameters
tend to zero. Nevertheless, in any decreasing stage net the near-zero
logarithmic slope cannot fall below its first positive slope. A finite
translation cannot overcome that order of vanishing, so the stage
parameters cannot tend to zero.

This strengthens the earlier literal abstract Lemma 4.6 counterexample
candidate. It does not realize the required algebraic family/class map:
the analogous curve functions need degree at least one and cannot be
labeled by `a_i[O(1)]` for `a_i<1`. The note gives the full directed-net
argument and checks the exceptional `i=1` intercept. It remains a
research candidate, with no new independent model call or verifier
receipt. All 42 problem statuses stay fixed.

## Source and literature scope

The controlling BJ22 published PDF is the pinned 191-page version in
`source_material/ch45_audit_20261001/BJ22_published.pdf`. Its Lemma 4.6
statement and proof, physical pages 63--64 (printed 708--709), were freshly
read and viewed earlier in this same continuation, as recorded in the
[joint closure manifest](siu_closure_research_manifest_20261005.json).
The [direct GF manifest](direct_gf_regularization_manifest_20261005.json)
records the intervening targeted reconstruction reading and viewing.
Two additional actual published pages were viewed here: physical page 32
(Rees comparison, Lemma 2.13) and page 67 (curve criterion, Example 4.13).
No fresh full reading of BJ22, its addendum or the Green-functions paper
is claimed at this checkpoint.

At 03:34 UTC, separate arXiv API checks for BJ22's current metadata and a
closure-related updated-date query both returned HTTP 429, with the body
`Rate exceeded.` The attempted URLs, timestamps, response hashes and
query bounds are copied into the new manifest. These failed checks
establish neither a current latest BJ22 version nor absence of recent
related papers. The cached `1801.08229v4` remains a pinned historical
version. The earlier successful, bounded updated-date literature search
and FGK v3 reading remain in their dated records.

## Build and actual-page checks

The final release build has 4,255 pages and 19,812,039 bytes, with SHA-256
`7b58a7cadcdf7ae1694b542c9f80bbbb51dd88923425f03e7f86483584c35948`.
It has no TeX errors, LaTeX/package or pdfTeX warnings, overfull boxes,
unresolved references/citations or rerun requests. The 954 underfull-box
diagnostics remain. Bibliography generation uses 283 entries with no
warnings. The index accepts 728 entries, rejects none and writes 964
lines with no warnings.

The source gate covers 425 inputs, 12,596 unique labels, 173 reference
ranges, 5,493 citation groups, 5,737 citation uses, 283 cited keys and 582
bibliography keys. The reference checker reports no missing inputs,
duplicate labels or dangling references. The atomic inventory checker
passes all 42 atoms in twelve families, with tiers `0,3,7,15,17`.

Navigation checks all 21,439 named destinations, 46,180 internal links,
163 URL links and 2,434 contents entries. All six part entries and all
397 distinct numeric index destinations are valid. No invalid internal,
named or index destination is found.

Extracted text was compared on every page against the preceding published
book PDF `95273bde...`: nine physical pages change, namely 37,
2209--2215 and 3990; the other 4,246 page texts are identical. This is not
a claim of full-book raster identity or a fresh whole-book rereading.
The actual-page review covers those nine pages and neighbouring pages
2208, 2216, 3989 and 3991. All thirteen pages of the preceding `23b6b822...`
intermediate edition were actually viewed in this continuation. For the
release edition, four pages were freshly viewed after the final wording
changes; the other nine occur on rendered contact sheets verified
byte-identical to sheets already viewed. The manifest records this reuse
page by page. No clipping, overflow or incorrect continuation was found.

The PDF, thirteen-page review extract and a source archive are saved under
new edition names. The archive's members are verified against the current
files and include the complete active source closure. It is not freshly
compiled in isolation; the recorded successful build uses the configured
cloud TeX and font environment. Earlier PDF, source, audit and receipt
artifacts are preserved.

## Synchronization and continuation

The completed remote fetch shows no incoming work-branch commits beyond
`14da2a0` and no main-branch commits beyond `0095711` at this check.
Publication uses the ordinary `work` branch and draft PR #2. The main
branch is not updated. Continue the unbounded algebraic closure question
and related polyhedral regularization settings, keeping source conventions,
unclosed inputs and research-only admission boundaries explicit.
