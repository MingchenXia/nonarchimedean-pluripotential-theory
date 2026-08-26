# Current-source whole-book build after P09.2 — 26 August 2026

This record concerns the current working source after the exact
product--Gauss criterion and its Raynaud application were integrated into
Chapters 19 and 72.  It supersedes the earlier 26 August current-source build
for release decisions about this source state, while preserving that earlier
3,143-page record as dated evidence for the pre-P09.2 source.

- Result: clean, converged whole-book build.
- Command: `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
  from `manuscript/`.
- PDF: `manuscript/book.pdf`, 3,149 pages, 15,176,815 bytes.
- PDF SHA-256:
  `85883cbdcc85be99ce88b62cb8e2ab0a67c0848071585a91fdf1f1e4bd1406fb`.
- Log: `manuscript/book.log`.
- Log SHA-256:
  `0d3b9d316da10c9752dc519b71749e462d6dafc745d059624c4777a64cf30f83`.
- Final-log audit: no TeX error, undefined control sequence, fatal or
  emergency stop, undefined reference or citation, multiply defined label,
  duplicate destination, rerun request, BibTeX warning, or overfull box.
  The log contains 957 underfull-box notices from the long-form book layout;
  none clips or overlaps content on the inspected pages.
- Bibliography and index: generated and included by the converged build;
  the new `Gub16` entry occurs in both the final auxiliary data and
  bibliography.
- `git diff --check`: passed before this record was written.

## Mathematical integration

Chapter 19 directly inputs the exact production-verified statement and proof
of the product--Gauss criterion.  The criterion recognizes when a
nondegenerate quadratic weight of an equivariant integral-PL map is an
ordinary Gubler--K\"unnemann delta-metric and then applies it to ample
cubical metrics on split Raynaud uniformizations.  Chapter 72 no longer
prints P09.2 as a problem: it records that an ample cubical metric is ordinary
delta exactly when the residual Raynaud extension is isotrivial, and hence
that the answer in non-isotrivial mixed reduction is negative.

The exact bytes passed production Rethlas run
`20260826T055627Z_b68659fba1be`, item
`pi_75c74fac9a98efc3719b9773`, using `gpt-5.6-sol` at `xhigh`, with final
`correct`, one checked item, zero critical errors, and zero gaps.  The scope,
independent audits, packet hashes, run artifacts, and historical boundary are
recorded in
`editorial/rethlas_receipts_20260826/p09p2_product_gauss_live_integration_receipt_20260826.md`.

## Source closure and structural checks

- Source closure: 111 files.
- Controlling ledger:
  `editorial/current_source_closure_p09p2_20260826.sha256`.
- Ledger SHA-256:
  `80b962ed85a732950b777f7225eab8b1c88f64eea075bcd7fd5b793c3e1aac9f`.
- Every ledger entry passed `shasum -a 256 -c`.
- Comparison with the converged `book.fls` confirms that the ledger contains
  every repository-local authoring input used by pdfLaTeX, together with the
  bibliography, BibTeX style, index style, and `latexmkrc`.  Relative to the
  109-file pre-P09.2 closure, the only new production inputs are the frozen
  P09.2 statement and proof.
- Their SHA-256 values are
  `b68659fba1be78b30345c112c637d38f41372dc70526fef8ecad6a450f7cbf47`
  and
  `3bfc656409c96a2be52161798efffe726657a3e0b2d2831a5f25a795e8c4d262`.
- The current literal frontier is 15 formal problem environments in Chapter
  72 and one in Chapter 71, hence 16 book-wide and 56 active atoms.
- The retired label `prob:frontier-gjr-remaining` occurs neither in the live
  Chapters 19 and 72 nor in the converged `book.aux`.  Dated standalone slice
  auxiliaries are not current build inputs.
- No exercise environment or exercise heading occurs in the source closure.
- No theorem, lemma, proposition, corollary, or claim has an optional
  conventional name.
- The author field remains empty and the acknowledgements have no body.

## Visual inspection

The rendered pages were inspected at 130 dpi, not merely text-extracted.

- PDF pages 952--957 (printed pages 886--891) contain the complete theorem
  and proof.  The long hypotheses, relative-Gauss norm, common-cell
  calculation, ambient-Hessian contraction, analytic-local bridge, and
  Raynaud conclusion have no clipping, overlap, malformed display, missing
  glyph, or unreadable line.
- PDF page 958 (printed page 892) cleanly begins the following canonical
  measure subsection, so the inserted proof terminates without a bad page
  break.
- PDF page 963 (printed page 897) cleanly displays the mixed-reduction
  non-delta example and its transition to the local--global comparison.
- PDF pages 2968--2969 (printed pages 2902--2903) cleanly display the retired
  open problem, negative answer, proof mechanism, production receipt, and
  transition to the distinct semipositive-decomposition discussion.

Headers, footers, page numbers, hyperlinks, margins, and section hierarchy
are consistent on all inspected pages.  This is build and integration
evidence; it makes no novelty or priority claim.
