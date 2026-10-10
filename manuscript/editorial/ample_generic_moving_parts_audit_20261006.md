# Moving parts over an ample generic fibre

Date: 6 October 2026. Baseline: `e8acba10a811b93db455af9c4185bb3ac0b956f8`.
This checkpoint imports a known algebraic consequence of Fujita
approximation. It follows the full Dervan–Reboulet source review and
supports the conditional comparison already in Chapter 68.

## Mathematical scope

The construction keeps X smooth and complex projective, dimension n at
least one, an ample rational line bundle L and V = (L^n) > 0. A smooth
dominant equivariant compactified model has class M = rho* p1* L + D,
where D is supported over the central fibre. Choose a rational c so that
D + cY0 is effective and B = M + cY0 is globally big. At sufficiently
divisible levels m, mL is globally generated. Resolve the complete series
of mB equivariantly and write A_m = q_m* B - F_m/m with F_m effective.

The sections of mL, multiplied by the canonical section of
m(D + cY0), have no common zero away from the central fibre. The base ideal
and the resolved fixed part are therefore vertical. The moving multiple
mA_m is globally generated; A_m is nef and its generic restriction is L.
Subtracting c q_m*Y0 preserves relative semiampleness and defines a
semipositive PL potential for the original polarization. The total-space
Fujita limit gives A_m^(n+1) tending to vol(B). The model energy is
A_m^(n+1)/((n+1)V) - c; it converges with the same denominator throughout.

This is a top-volume statement. It does not identify that limit with the
energy of a specified discrepancy envelope, arrange a common order with
a prescribed lower potential, supply all mixed positive-product limits,
or prove entropy convergence. Those remain the displayed inputs to the
conditional Chapter 68 comparison. For a merely big generic polarization,
a horizontal fixed part can change the generic moving polarization and
its volume. Vertical coefficient changes cannot make a nonnef generic
pullback relatively semiample. No arbitrary-big extension is admitted.

The positive-product explanation retains q*B - A effective. Arbitrary
nef replacements would make the supremum unbounded. Mixed products use
dominated approximants and are continuous inside the big cone. Order of
pseudo-effective cycle classes need not survive restriction to an
arbitrary effective divisor, so individual central-component masses
cannot be compared by this order alone.

## Primary evidence and versions

All source reading here is reused from the preceding
[big-class stability review](big_class_stability_source_review_20261006.md)
and its pinned selected-reading record. There are no new primary pages
or new full dependency readings at this checkpoint.

The published author-hosted BFJ09 offprint has 30 actual pages. Actual
pages 1–3, 12–20 and 23–28 were displayed in the preceding review.
Definition 2.5 is on printed 290–291 / actual 12–13; Proposition 2.9 on
printed 292 / actual 14; Theorem 3.1 on printed 294 / actual 16. The
top-volume and orthogonality arguments are on printed 295–296 / actual
17–18. Section 4 on printed 301 / actual 23 explains the restriction
issue. Theorem B, printed 281 / actual 3, with proof printed 305–306 /
actual 27–28, applies to every prime divisor in its stated smooth
projective big-line-bundle category. This cleared prime-divisor formula
is distinct from the augmented-base-locus hypothesis in restricted
Fujita approximation for general subvarieties.

ELMNP arXiv:math/0607221v2, revised 10 January 2008 at 16:33:29 UTC,
has 38 actual pages. Actual pages 1 and 6–15 were displayed. Definition
2.6 is on actual 7, Theorem 2.13 on 9, and its proof on 12–14. Applying
the theorem with the subvariety equal to the whole total space is the
ordinary complete-series top-volume case. The new bibliography key
`ELMNP08RestrictedV2` records the exact preprint, separately from the
existing journal entry and its pagination.

BHJ arXiv:1504.06568v3, revised 30 November 2016, has 73 actual pages.
Fourteen selected pages were displayed in the preceding review.
Definition 7.2 and Lemma 7.3 are on actual 47; Proposition 3.12 and
its first-moment proof on actual 25–26 retain the factor (n+1)V.
The new key `BHJ16UniformV3` distinguishes this controlling preprint
from the existing 2017 journal entry. The model formula and translation
law support the relative top-product identity used here.

The complete preceding dependency selection has 58 actual pages from
BFJ, ELMNP, BHJ, BJ18 and Witt Nyström; all selected PDF pages were
displayed and read. It does not claim full reading of all five papers
or full reading of every extracted selected-text file. The complete
40-page Dervan–Reboulet v1 was read and displayed separately. Its full
big-class stability and birational proof chains remain outside active
TeX. The prior source manifest and reading flags remain historical.

## Book changes and preservation

Chapter 46 gains subsection 46.3.6 after the ordered PL estimate and
before the curve example. Equations 46.10e–g record dominated top volume,
the vertical moving parts, and relative energy. Chapter 68 gains a short
pointer at its list of conditional approximation inputs. Appendix L
gains section L.51 with the version, source-page and scope account.
Two version-specific bibliography keys are added. Five new labels and
no new formal theorem environments or index entries are introduced.

All 136 existing formal blocks in the three changed TeX files remain
byte-identical. The other 422 active TeX inputs and all 108 protected
inputs retain their baseline bytes. All 42 canonical statuses in twelve
families, tier counts 0/3/7/15/17, remain fixed. The open toric candidate
and the native 86-page catalogue source and PDF are preserved. The native
editor was not changed or reopened; no catalogue compilation is claimed.
All 52 prior frozen manifests and 103 prior exports are preserved.

## Build, rendered reading and release checks

The first build exposed undefined draft shorthand for the new total-space
classes. The source now uses explicit standard mathcal macros; the failed
v1 build log and draft states remain diagnostic records. The subsequent
v2 build completed. Its final book has 4,382 pages, 20,360,528 bytes and
SHA-256 `0a5ba5e0ebca85cdc4cf6988494204b8f8e13fbd3184d5a54fefe73f78f5cc2c`.
The final log has zero TeX errors, package/PDF warnings, missing characters,
overfull boxes, unresolved references/citations or rerun requests. The
954 nonfatal underfull boxes retain the preceding build's count.

The source closure has 425 active inputs, 12,822 unique labels, 371 cited
keys and 666 bibliography keys. The fresh post-render reference checker
reports no missing input, duplicate label or dangling reference. The
atomic inventory check and whitespace diff check pass. The index accepts
764 entries and rejects none, with no warnings. Its 763 page groups and
419 distinct numeric destinations resolve. The PDF has 21,910 named
destinations, 46,977 internal links, 171 URL links and 2,554 TOC entries
covering six parts; all internal and named destinations pass validation.

All 45 selected matching final book pages were actually displayed and
reread in 23 image sheets: actual 47, 61, 68, 2738–2742, 3631–3634,
4143–4147 and 4355–4382. This includes the affected contents, new
subsection and curve transition, conditional comparison and provenance
transitions, and the complete index and bibliography. The final pages
are readable with no further correction needed. This is a scoped final
review; the complete ordered second reading remains the 4 October record.

The new release records pin the 425-input closure, source gates, final
build log, failed-build diagnostics, actual-page views and reused primary
evidence. Exports consist of the matching full book, the 45-page review
PDF and the complete active source package with inherited support and
provenance. Every ZIP member is compared with the saved workspace bytes
and its CRC is checked. No fresh isolated-archive compilation is claimed.
The current external artifact record is excluded from its own source ZIP.

## Research and publication boundary

This checkpoint is an explanation of known inputs and a direct formal
consequence of the cited Fujita and model-energy formulas. It introduces
no original priority claim, new independent model call or verifier receipt.
Historical receipts are not extended. The BJ22 Theorem 6.21 proof gap,
general Siu/closure boundary and conditional full big-model passage remain
explicit; no theorem counterexample or complete repair is asserted.

Routine synchronization uses the authorized work branch and existing
draft PR 2, with explicit fetches of both main and work. There is no force
push or main-branch update. Continue by reading the special Fujita and
entropy regularization proof and tracing its remaining dependencies.
