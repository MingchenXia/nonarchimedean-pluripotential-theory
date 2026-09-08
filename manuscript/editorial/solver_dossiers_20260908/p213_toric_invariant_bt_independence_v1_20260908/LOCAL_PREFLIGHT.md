# Local preflight — P21.3 invariant split-toric candidate

Date: 8 September 2026.

## Source and interface checks

- The primary source BGJKK25 was checked at its publisher/preprint PDF:
  equation (5.5) gives the continuous invariant-function correspondence;
  Proposition 5.3.10(iv) and its proof give the function-current
  pushforward calculation and the differential-commutation calculation.
- The live book contains the required interfaces exactly once:
  `prop:current-pushforward-formal` in Chapter 14,
  `lem:ch19-toric-chart` in Chapter 19,
  `cor:ch16-smooth-h` and `prop:ch16-cell-rigidity` in Chapter 16.
- Bibliography key `BGJKK25` is present in
  `manuscript/bibliography/NonArchimedean.bib` and identifies the published
  2025 Kyoto Journal of Mathematics article.

## Syntax check

`latexmk -pdf -interaction=nonstopmode -halt-on-error SYNTAX_CHECK.tex`
completed after the statement was changed to the live-book macro `\An` and
produced a two-page local harness PDF.  The harness has no
bibliography database by design, so its two `BGJKK25` citation warnings are
expected; the live bibliography key was checked separately above.  The
generic harness replaces `\cref` by visible label text, so it is a syntax
check rather than a live-book reference-resolution check.  The generated
PDF, log, and auxiliary files were then removed; `SYNTAX_CHECK.tex` remains
as the reproducible harness.

The complete live book was also rebuilt successfully after the integration,
with no TeX errors; its PDF has 3,522 pages.

## Verifier status

The local verifier health endpoint responded `{"status":"ok"}`.  The first
submission was superseded because its statement used the non-live `\an`
macro.  The revised exact packet then returned final verdict `correct` for
item `pi_9b5ecb53f97997b14013cd54`, with zero critical errors and zero gaps.
The archived safe headers record HTTP 200.  The V1 and controlling V2
receipts, hashes, and exact integration audit are recorded in
`POST_VERIFICATION_AND_INTEGRATION.md`.
