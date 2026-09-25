# P03.1 v61 live build report

Date: 2026-09-25

## Integration

The new theorem separates two curvewise gaps for the affine Perron envelope.
The intrinsic curve regularization and the pullback of the extended-field
regularization are subharmonic, whereas every local failure of the retracted
ground-field envelope lies in the closure of the strict scalar-retraction
gap.  The corollary turns that containment into a necessary curve witness for
any affine P03.1 counterexample.  Chapter 15, Chapter 72, and the atomic
inventory record the result.  No converse, removability theorem, P03
retirement, or active-count change is asserted.

The newly supplied PDF
`global-smooth-psh-counterexample (1).pdf` is byte-identical to the source
already archived as
`manuscript/author_sources_20260925/global-smooth-psh-counterexample.pdf`
(SHA-256
`682eec5c367f9cd5d81427173a540b8c87b844ca7803c776344bd21eb117944a`).
That source was already integrated in the P08.1 repair committed as
`ac6e03e2a13fd0533673379bf843d129e6a421d9`, so no duplicate import was made.

## Exact hashes

- `STATEMENT_LIVE.tex`:
  `75db7b80043da2f760290b5b2841fb13a504f5794547e093baf01848ac292f3f`
- `PROOF_LIVE.tex`:
  `76c16fe38955ef598a3977a89c1663e172ed41005232ea7bc7998a5a25f726d3`
- `book.pdf`:
  `062b9a076f7d2aa1bfdf996207237d53bef6236c19ad1e66b7fecb7e9e33f0a5`

## Independent verifier

The first exact `gpt-6-astra`/`xhigh` run returned `wrong`: it found the
affinoid/smoothness mismatch in the witness proof and requested missing
transitive dependencies.  The proof was repaired without weakening the
statement, and the dependency-closed second exact run returned `correct`,
with zero critical errors and zero gaps.  Request, headers, and response for
both runs are archived in this dossier.

## Mechanical checks

- Focused Mingchen-style audit: zero errors and zero warnings.
- Minimal compile: pass, two pages.
- Forced full-book `latexmk` build: pass.
- Output: 4,070 pages, 19,382,784 bytes, PDF 1.5.
- Final log scan: no undefined citation, undefined reference,
  multiply-defined-label, undefined-control-sequence, or LaTeX-error match.
- `git diff --check`: pass.

## Automatic second pass and visual review

The second pass rechecked all quantifiers, local upper boundedness,
continuous-pullback regularization, the ordered strict-locus splitting, the
sheaf step, the separatedness convention, and every non-claim.  It confirmed
that the proof never treats the canonical retraction as analytic.

The final book PDF was inspected on physical pages 793--795 (printed pages
725--727) and physical pages 3773--3774 (printed pages 3705--3706).  The
statement, formulas, corollary, proofs, synthesis paragraphs, and Chapter 72
status text are complete and visually clean, with no clipping, overlap, or
bad page break.
