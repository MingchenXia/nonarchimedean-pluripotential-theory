# Build report

Date: 19 September 2026

## Integrated result

- Corollary 18.8.18,
  `cor:p061-etale-toric-arbitrary-curve-factor-products`, appears on printed
  page 1097 and physical PDF page 1165.
- Its proof appears on physical PDF pages 1174--1175.
- The result carries arbitrary finite external good strict curve factors and
  one final factor with quasi-smooth reduction through the manufactured
  ordinary-etale algebraic-split toric tube.  It does not enlarge the stated
  ordinary-etale, algebraic-splitting, or external-product hypotheses.

## Validation

- Strict `mingchen-writing` audit of `STATEMENT.tex` and `PROOF.tex` against
  `bibliography/NonArchimedean.bib`: 0 errors and 0 warnings.
- Build-closure reference audit: 307 files, 11,062 labels, 0 multiply defined
  labels, and 0 dangling references.
- Chapter 72 inventory audit: 46 active atoms in 14 environments, with tier
  counts T1=0, T2=5, T3=8, T4=16, and T5=17.
- `git diff --check` passed.
- The final log contains no fatal TeX error, undefined citation or reference,
  multiply-defined label, rerun request, or overfull vertical box.

## Full-book build

- Final PDF: 3,260 physical pages and 17,365,733 bytes.
- `book.pdf` SHA-256:
  `891549eb44427f09df36e0503e5279c96809efa95a13cedcd274ce507fe7583a`.
- `book.log` SHA-256:
  `d29b1727beb31de77431fa7175c637d53a80c1725ebba332d32d7b7f8cc388f8`.

## Visual audit

- The statement on physical page 1165 and the proof on physical pages
  1174--1175 were rendered from the final PDF and inspected.
- The Chapter 18 comparison ledger on physical pages 1290--1293 was rendered
  and inspected.  Its overlong unbreakable comparison table was converted to
  a paginating `longtable`, and the ledger tables received nonoverlapping,
  ragged-right columns.  This removed the previous vertical overflow and
  column collisions.
- The Chapter 72 frontier update on physical page 3069 was rendered and
  inspected.

No model-backed verifier was used for this dossier.
