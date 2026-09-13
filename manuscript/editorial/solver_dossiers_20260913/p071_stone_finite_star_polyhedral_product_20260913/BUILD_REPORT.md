# Build report

Date: 13 September 2026

Status: local build and regression checks passed.

## Minimal theorem build

- Engine: pdfLaTeX through latexmk.
- Scope: exact `STATEMENT.tex` and `PROOF.tex`, with only the two required
  dependency labels supplied by the harness.
- Final PDF: 6 pages and 205939 bytes.
- The final log contains no warnings, undefined references, overfull boxes,
  underfull boxes, or LaTeX errors.
- Strict Mingchen writing audit: 0 errors and 0 warnings.
- All six pages were rendered; the changed nested-core page and the complete
  packet were visually inspected without clipping, collision, or illegible
  mathematics.

## Full-book regression

- Engine: pdfLaTeX through the manuscript latexmk configuration.
- Final PDF: 3672 pages and 17467844 bytes.
- Final PDF SHA-256:
  `35eaf95acb8a12bbda0a9f7e0fac3c1b4b4d39ccbdf62f69031fa6edb9cdb553`
- Final log SHA-256:
  `f6fac4d918db48a8dce9168b61edaf91313ad8f3677339cd22fb2106e4a7208a`
- The final log contains no LaTeX error, undefined control sequence, fatal
  error, emergency stop, undefined reference or citation, or multiply defined
  label.
- The four temporary hash-string overfull boxes found during the first
  regression pass were removed by using digest prefixes in the typeset book;
  the final log contains none of those new boxes.  Complete hashes remain in
  the inventory and verification receipt.
- Live theorem pages 733–738 and Chapter 72 pages 3390–3391 were rendered and
  visually inspected.  No clipping, collision, bad theorem break, or illegible
  line was found.

## Repository checks

- Chapter 72 inventory checker: PASS with 48 active atoms across 14 formal
  problem environments and tier counts T1=0, T2=5, T3=9, T4=17, T5=17.
- Chapter 69 has no working-tree difference.
- Repository whitespace check passed.
