# Current-source build: P07.1 exact CLD infinite-star integration

Date: 30 August 2026 (Asia/Shanghai).

This record supersedes `current_source_build_p171_full_20260830.md` as the
controlling current-source build.  It does not rewrite or replace the dated
24 August release archive.

## Mathematical gates

The structural packet for the exact Chambert--Loir--Ducros star \(X_B\)
passed production Rethlas item `pi_e07ae5472f3ba6d4ebc75d6b`, using
`gpt-5.6-sol` at `xhigh`, with status `final`, verdict `correct`, zero
critical errors, and zero gaps.  Its exact statement/proof SHA-256 values
are

- `bdb2592c40e26f2c64b3e7ab0bb2cdbd74745c5c01fe6d1cbf809ce274c1bf99`;
- `9b21c5893a0c8ee0be61f8c7b453fcf3d621622845a1582a622d0281450bd755`.

The full comparison and approximation theorem passed production Rethlas
item `pi_00f6c73303087d94da9eb724`, with the same model and scrutiny, status
`final`, verdict `correct`, zero critical errors, and zero gaps.  Three
independent exact-byte audits also passed before production submission.  Its
exact statement/proof SHA-256 values are

- `99c1a6a6a712005e73ee3b7cdae297606895b22ce79c80a6411dfd7f4863c963`;
- `ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090`.

The archived request/response/header SHA-256 values for the full theorem are

- request: `44a3a37db22d51823ad99dc209c749d576398e61cb615d0e3cfda29c38fbaa38`;
- response: `b271d51ed81898ccfe68a798b3fc69e165c0c72486ff6c59711995f5b9e581af`;
- headers: `072a4a9070f3df8128f6c9079d0fcc3fafea1c2c31a037380ce4c778a51cf8cf`.

The theorem identifies the first-stage psh sheaf, the full generated psh
sheaf, and the explicit comparison sheaf on the exact CLD star for every
nonempty branch set.  It also gives decreasing smooth-psh approximation on
one fixed neighbourhood and the sharp countable-activity conclusion.  It
does not settle arbitrary higher-dimensional or other nonambient local
models.

## Converged whole-book build

Starting from base commit
`c586681e058d4e4ebe7b9d143d68a3e7c4508cda`, the integrated source was built
with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
```

After repairing only live provenance typography, the build converged.  The
frozen verified statement and proof bytes were unchanged.  The final log
scan found:

- LaTeX errors and undefined control sequences: 0;
- undefined references and citations: 0;
- multiply defined labels and rerun warnings: 0;
- overfull horizontal or vertical boxes: 0.

## Current PDF

- pages: 3,330;
- bytes: 15,987,138;
- SHA-256: `d8551cab39248cda207600526dd7d53a1ac593e562623b5c8441deda0cd84151`.

The synchronized artifact is
`output/pdf/Non-Archimedean_Pluripotential_Theory.pdf`; its hash equals the
final `manuscript/book.pdf` hash.

## Rendered audit

Physical PDF pages 742--750, containing the provenance bridge, theorem,
complete proof, and following example, were rendered and inspected at high
resolution.  Physical pages 3300--3301, containing the Appendix L provenance
record and its continuation, were also inspected.  No clipping, overlap,
malformed display, broken metadata text, or margin intrusion was found.

## Inventory consequence

The theorem removes the blanket infinite-star residual but does not retire
P07.1 or P07.2.  The active inventory therefore remains 53 atomic questions
in 14 formal problem environments, with tier distribution
`(0,5,14,17,17)`.  The residual P07.1 scope is arbitrary higher-dimensional
and other nonambient local models outside the two exact interval structures
and the exact CLD star \(X_B\).

No novelty or priority claim is made.
