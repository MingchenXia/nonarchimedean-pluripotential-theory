# Build and integration report

## Integrated result

The live revision adds:

- the global rational-coefficient gap and rational globalization defect;
- an exact three-level rational/LFS/PL defect ledger;
- conservation of the rational globalization defect under finite flat
  pullback;
- exact LFS and PL gain identities in terms of the two global branch gaps;
- sharp gap-preservation criteria for LFS and full P03 compatibility;
- complete-fiber collapse when the base rational defect vanishes;
- the finite-orbit decomposition of the symmetry-breaking defect into the
  rational--LFS and LFS--PL gap changes.

Chapter 15 contains the full statements and proofs. Chapter 72 and the atomic
inventory record the advance while preserving the unresolved boundary.

## Verification

- Full `latexmk` build: PASS.
- Output: `book.pdf`, 3299 pages, 17,532,969 bytes.
- PDF SHA-256:
  `185ebc7992bf1990c8847e3900fbff5f1048e77a6996856cee741e2dd32c4c7b`.
- Reference closure: 333 files, 11,208 labels, 0 multiply defined labels,
  0 dangling references.
- Log scan: no undefined citation, undefined reference, or multiply defined
  label diagnostic.
- Mingchen strict audit of the live statement and proof: 0 errors,
  0 warnings.
- `git diff --check`: PASS.
- Atomic inventory: PASS, 46 active atomic questions in 14 formal problem
  environments; tiers T1=0, T2=5, T3=8, T4=16, T5=17.

## Automatic second pass

The second pass replaced an ambiguous subtraction reference by explicit
local-versus-global wording, displayed the zero rational defect in the
nonnegative decomposition, and clarified that the common global value equals
each corresponding local envelope value. The full book was rebuilt after
these edits.

## Visual audit

Rendered and inspected page by page:

- Chapter 15 physical PDF pages 765--768 (printed pages 697--700);
- Chapter 72 physical PDF pages 3073--3075 (printed pages 3005--3007).

The new statement, displays, proofs, Chapter 72 summary, and surrounding
transitions are legible. Cross-references are resolved, displays fit the text
area, and no new clipping, collision, or obscuring overfull box appears on the
affected pages.

## Exact live hashes

- `STATEMENT_LIVE.tex`:
  `dd84bd600bf10e909e8c4861757e75bc56b13dde7b6e465e305a5d694ecf10e4`.
- `PROOF_LIVE.tex`:
  `6149b8dee66d59af92230d49875ffcc1e7570685f1123dd997743448ec705c80`.

No model-backed verifier was invoked for this version.
