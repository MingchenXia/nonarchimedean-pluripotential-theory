# Build and integration report

## Integrated result

The live revision adds:

- rational LFS fiber-maximum closure for finite flat surjections;
- exact pullback of the global rational LFS envelope;
- local one-sided rational cofinality inside the real LFS class;
- exact local LFS pullback with a complete-fiber baseline;
- exact local PL pullback on boundaryless spaces;
- finite-flat PL defect balance and contraction;
- the finite-orbit four-defect identity without a local section.

Chapter 15 contains the full statements and proofs. Chapter 72 and the atomic
inventory record the advance and preserve the unresolved boundary.

## Verification

- Full `latexmk` build: PASS.
- Output: `book.pdf`, 3297 pages, 17,520,393 bytes.
- PDF SHA-256:
  `e842b324d8c6a80cb43d5fea46449fe69b449f452ffa2c6e65a4c9e1da9546ab`.
- Reference closure: 331 files, 11,194 labels, 0 multiply defined labels,
  0 dangling references.
- Log scan: no undefined citation, undefined reference, or multiply defined
  label diagnostic.
- Mingchen strict audit of the live statement and proof: 0 errors,
  0 warnings.
- `git diff --check`: PASS.
- Atomic inventory: PASS, 46 active atomic questions in 14 formal problem
  environments; tiers T1=0, T2=5, T3=8, T4=16, T5=17.

## Visual audit

Rendered and inspected:

- Chapter 15 physical PDF pages 760--766 (printed pages 692--698);
- Chapter 72 physical PDF pages 3071--3072 (printed pages 3003--3004).

The theorem and proof blocks are legible, displays fit the text area,
cross-references are resolved, and the transition back to the surrounding
chapter is intact. No new clipping, collision, or obscuring overfull box was
found on the affected pages.

## Exact live hashes

- `STATEMENT_LIVE.tex`:
  `3ffcc55e20b4f9159ee7455fbfc45fae4254b125c60dcacd4a6ce4e4617ea67b`.
- `PROOF_LIVE.tex`:
  `bfc9bc71d4e52583b2870f7e70cf57b2258c88a0744fd94dceccd260df97f0b5`.

No model-backed verifier was invoked for this version.
