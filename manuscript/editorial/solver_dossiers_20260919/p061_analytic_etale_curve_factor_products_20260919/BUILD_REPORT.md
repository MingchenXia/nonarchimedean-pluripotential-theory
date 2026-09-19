# Build report

Date: 19 September 2026

## Integrated result

- Corollary 18.8.19,
  `cor:p061-analytic-standard-etale-arbitrary-curve-factor-products`, begins
  on printed page 1097 and physical PDF page 1165 and continues on physical
  page 1166.
- Its proof appears on physical PDF pages 1176--1177.
- The corollary carries arbitrary finite external good strict curve factors
  and one final factor with quasi-smooth reduction through an actual monic
  analytic standard-etale chart over an algebraic-split toric base.  It does
  not assert existence of that chart for an arbitrary analytic etale map.

## Validation

- Strict `mingchen-writing` audit of `STATEMENT.tex` and `PROOF.tex` against
  `bibliography/NonArchimedean.bib`: 0 errors and 0 warnings.
- Build-closure reference audit: 309 files, 11,063 labels, 0 multiply defined
  labels, and 0 dangling references.
- Chapter 72 inventory audit: 46 active atoms in 14 environments, with tier
  counts T1=0, T2=5, T3=8, T4=16, and T5=17.
- `git diff --check` passed.
- The final log contains no fatal TeX error, undefined citation or reference,
  multiply-defined label, rerun request, or overfull vertical box.

## Full-book build

- Final PDF: 3,262 physical pages and 17,373,025 bytes.
- `book.pdf` SHA-256:
  `97434aff2e23b0c5f72241234aad0ad99c9bb5ddf5d7f71019d06aa895bc9e84`.
- `book.log` SHA-256:
  `c5392c6328b136eb58e979ea45d2901403d9f0c10b0d9fec9c6d97c4a5eec605`.

## Visual audit

- The statement on physical pages 1165--1166 and proof on physical pages
  1176--1177 were rendered from the final PDF and inspected.
- The Chapter 18 explanatory paragraph on physical page 1178 and comparison
  ledger update on physical page 1293 were rendered and inspected.
- The Chapter 72 frontier update on physical page 3071 was rendered and
  inspected.

No model-backed verifier was used for this dossier.
