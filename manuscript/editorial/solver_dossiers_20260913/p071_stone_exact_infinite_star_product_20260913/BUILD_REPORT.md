# Build report

Date: 13 September 2026

Status: isolated packet build and full-book regression passed.

## Minimal theorem build

- Engine: pdfLaTeX through latexmk.
- Scope: exact STATEMENT.tex and PROOF.tex, with the two required dependency
  labels supplied by the harness.
- Final PDF: 7 pages and 213944 bytes.
- Final PDF SHA-256:
  40861960d6faa4fe74222108ffaec16607effb7e56eec332afd6d17b7a3ebcbf
- Final log SHA-256:
  0a542cc34ef54cdd1e1f7b76fcc0c14bb6aba84e6d13612607e95b14911a8c92
- The final log contains no warning, undefined reference, overfull box,
  underfull box, or LaTeX error.
- Strict Mingchen writing audit: 0 errors and 0 warnings.
- All seven pages were rendered and visually inspected without clipping,
  collisions, or illegible mathematics.

## Full-book regression after live integration

- Engine: pdfLaTeX through latexmk, with references converged.
- Final PDF: 3678 pages and 17494890 bytes.
- Final PDF SHA-256:
  7e07c554d1da88259c7661055d1ed733df8ea7bc089f9e772ab42df7ae2cbb41
- Final log SHA-256:
  69eb46924764305dfca3b4a15faf680088a7a97315e0e935a53351b5afea07dd
- The final log contains no fatal error, undefined control sequence,
  undefined reference or citation, or multiply defined label.
- Theorem 16.2.12 is recorded under the heading
  ``Stone-parametrized exact infinite stars'' on printed page 739.
- The live theorem pages 739--744 and the Chapter 72 ledger pages 3397--3398
  were rendered and visually inspected without clipping or collisions.
- The Chapter 72 inventory check passes with 48 active atoms across all
  14 open-problem environments: T1=0, T2=5, T3=9, T4=17, T5=17.
- Chapter 69 remains unchanged.
