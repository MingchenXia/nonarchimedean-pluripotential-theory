# Current-source build: P06.1 finite curve-product integration

Date: 30 August 2026 (Asia/Shanghai).

This record supersedes
`current_source_build_p071_infinite_star_20260830.md` as the controlling
current-source build.  It does not rewrite or replace the dated 24 August
release archive.

## Mathematical gate

The exact curve-product statement and proof passed production Rethlas run
directory `20260829T191019Z_0b5e24145108`, item
`pi_6add90bcf0cfded12d6a074b`, using `gpt-5.6-sol` at `xhigh`, with status
`final`, verdict `correct`, zero critical errors, and zero gaps.  Three
independent exact-byte audits also passed.  The frozen statement/proof
SHA-256 values are

- `96b246d6f6032bce38751095935525a67456c6753e006e7b188778bc945e50bc`;
- `6f6158b5253922539f81e42ab9e6d9e2c48a6b3c8b727e4157351b9591baabe5`.

The theorem proves real-PL and GJR harmonicity for classically
pluriharmonic functions on good finite products of geometrically reduced
good strict analytic curves with a good strict quasi-smooth factor, and on
good strict spaces locally modelled by open analytic subspaces of such
products.  Arbitrary singular germs, non-geometrically-reduced curve-factor
products, and spaces without that local product presentation remain open.

## Converged whole-book build

Starting from base commit
`a0fc1dfd6f67cdd5afdb97f43e36e96da7b59101`, the integrated source was
built with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
```

The build converged.  The exact verified statement and proof bytes remain
unchanged.  The final log scan found:

- LaTeX errors and undefined control sequences: 0;
- undefined references and citations: 0;
- multiply defined labels and rerun warnings: 0;
- overfull horizontal boxes: 0.

## Current PDF

- pages: 3,338;
- bytes: 16,023,200;
- SHA-256: `32c3ce8f34d168b217112437deb76ba977eda9e2abf060099255563027114f4d`.

The synchronized artifact is
`output/pdf/Non-Archimedean_Pluripotential_Theory.pdf`; its hash equals the
final `manuscript/book.pdf` hash.

## Rendered audit

Physical PDF pages 990--991, 3143--3144, 3288, and 3306 were rendered and
inspected at high resolution.  No clipping, overlap, malformed formula,
broken metadata text, redundant proof heading, or margin intrusion was
found.

## Inventory consequence

P06.1 remains active only outside the verified local finite-curve-product
scope.  The current inventory therefore remains 53 atomic questions in 14
formal problem environments, with tier distribution `(0,5,14,17,17)`.

No novelty or priority claim is made.
