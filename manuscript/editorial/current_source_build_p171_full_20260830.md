# Current-source build: P17.1 full integration and retirement

Date: 30 August 2026 (Asia/Shanghai).

This record supersedes
`current_source_build_p171_finite_reduction_20260829.md` as the controlling
current-source build.  It does not rewrite or replace the dated 24 August
release archive.

## Mathematical gate

The exact live dependency closure for `thm:p171-full-assembly` passed
production Rethlas item `pi_87b42b938a8d830222bed78f` with status `final`,
verdict `correct`, zero critical errors, and zero gaps.  The materialized
statement/proof SHA-256 values are

- `0ba26fe924a065af31198cfc74aa44e790feb128159eef24458f8ca0b151f8b4`;
- `cdce552b3750faed4dfbb6a0284405094be10b56c138363482cca0464e20f4af`.

The exact principal live statement/proof SHA-256 values are

- `0d95354a4cd2bd15d03020dde630779f4f423b73e9661eb8e65e0511dc765e24`;
- `9cab2f0f679b095b00b2d9f760a4a5315d3a24fe7b295a9d0a9bf414d91e434a`.

The archived request, response, and header hashes are recorded in
`rethlas_receipts_20260830/p171_full_banach_family_live_integration_receipt_20260830.md`.

## Clean build

The entire `manuscript/` tree was synchronized into a clean temporary build
directory.  `latexmk -C` was run first, followed by

```text
latexmk -silent -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
```

The build converged successfully.  The final log scan found:

- undefined control sequences or fatal errors: 0;
- undefined references or citations: 0;
- multiply defined labels or duplicate destinations: 0;
- overfull horizontal or vertical boxes: 0;
- BibTeX warnings: 0.

The PDF metadata has a blank author field, no subtitle, and the title
`Non-Archimedean Pluripotential Theory`.

## Current PDF

- pages: 3,318;
- bytes: 15,938,059;
- SHA-256: `301ec45d8660f3a3a7503f9221d9a80ca7b9a1c384a99de5f43e0f24d4b44394`.

The exact build artifact is
`/private/tmp/nappt_p171_live_build_20260829/book.pdf`.  It remains a
current-source audit artifact; the dated release PDF and source archive under
`output/` are not silently replaced by this record.

## Rendered audit

Representative pages from the new Chapter 66 block (printed pages
2898--2927), the resolved P17.1 chronology in Chapter 72 (printed pages
3070--3071), and the new Appendix L provenance entry (printed pages
3226--3227) were rendered and inspected.  No clipping, overlap, malformed
display, broken link text, or margin intrusion was found.

## Inventory consequence

The literal source now contains 14 active `problem` environments, all in
Chapter 72.  A direct count of `[Tj; open]` atoms in the atomic inventory is
53, with tier distribution `(0,5,14,17,17)`.  P17.1 is retained only as
resolved history.  Its former standalone problem environment has been
removed from the active chapter and the associated output packet has been
converted to resolved chronology.

No novelty or priority claim is made.
