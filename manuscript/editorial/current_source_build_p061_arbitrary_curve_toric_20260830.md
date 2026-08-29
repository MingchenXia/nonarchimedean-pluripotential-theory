# Current-source build: P06.1 arbitrary curve factors and affine toric fixed point

Date: 30 August 2026 (Asia/Shanghai).

This record supersedes
`current_source_build_p061_curve_product_20260830.md` as the controlling
current-source build.  It does not rewrite or replace the dated 24 August
release archive.

## Mathematical gates

The arbitrary-curve-factor theorem removes every reducedness and geometric
reducedness hypothesis from the finite strict-curve factors in the preceding
product theorem.  It also permits the remaining good strict factor to be a
nilpotent thickening of a quasi-smooth space.  Its frozen statement and proof
SHA-256 values are

- `6954b3ebc1f9efb060b4858ce732d9720d62741ba2397c39573312dd6e3ba8f3`;
- `e308ba5df336e38717ac27413c6f669a7fa37535bed613a79f095811c6dba4a7`.

Two independent exact-byte audits passed.  The dependency-closed production
Rethlas request used `gpt-5.6-sol` at `xhigh`; item
`pi_7dceb6442b4d586c4475feca` returned status `final`, disposition
`verified`, verdict `correct`, zero critical errors, and zero gaps.

The affine toric theorem proves local constancy, hence real-PL and GJR
harmonicity, of every classically pluriharmonic germ at the rational
torus-fixed point associated to a full-dimensional strongly convex rational
cone.  It assumes neither simpliciality nor a residue-characteristic
restriction.  Its frozen statement and proof SHA-256 values are

- `edbe69950a0a9c81ca2fd9077a58be96ec6bdb6c27ce9cf2524da5bf653a5ab6`;
- `531e326b4aeb19067fcb88af2f6eb6477a169587d71a3249103777c9131cf8f4`.

Two independent exact-byte audits passed.  The production Rethlas request
used `gpt-5.6-sol` at `xhigh`; item `pi_dfd932c583fee3acd3fefbe3`
returned status `final`, disposition `verified`, verdict `correct`, zero
critical errors, and zero gaps.

Both exact statements and proofs are input byte-for-byte in Chapter 18.
Their scope and residual firewalls are synchronized in Chapter 72, the Part
II introduction, Appendix L, the atomic inventory, and the verification and
provenance ledgers.

The post-integration SHA-256 digests of the seven synchronized live source
files are:

- `manuscript/appendices/appL_provenance.tex`:
  `fdde3d2ce19a914b719f6915d6fa4e6f73cb5ab38289a2a565137f9f2d20c5f5`;
- `manuscript/editorial/open_problem_atomic_inventory_20260824.md`:
  `ead74f25b7dd7e2e41915ea3361daba43c93f421dcf00d3ee99d4a8d81fbdd1e`;
- `manuscript/editorial/rethlas_verified_results.md`:
  `3511d5d2d21595d02e63a0fdeb45565e26a93c985153259ce3619484f6446a8c`;
- `manuscript/editorial/theorem_provenance.md`:
  `3f6af23b9aae3665d870389abab260c9fa2bac55dde250ea10b8371b416e6b60`;
- `manuscript/frontmatter/part2_intro.tex`:
  `f2b9db4758d6a71c75d1af4cfc7f2d2c8e5ea194e2c5fe2b0f34c9079cccef55`;
- `manuscript/parts/part2/ch18_delta_forms.tex`:
  `6e26069e6335aa40f2742c9d80751108509a13f919fc3bd2b682eb8951517da8`;
- `manuscript/parts/part6/ch72_major_open_problems.tex`:
  `8bcc3f7c54ce2568c395448e95ae29266f2f24a57e6ee2feafd9e986192d30e0`.

## Converged whole-book build

Starting from base commit
`2b23b385fe46dd63ad77a3ca2065a6c054b2c68f`, the integrated source was
built with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
```

The build converged.  The exact verified statement and proof bytes remain
unchanged.  The final log scan found:

- LaTeX errors and undefined control sequences: 0;
- undefined references and citations: 0;
- multiply defined labels and rerun warnings: 0;
- overfull horizontal and vertical boxes: 0.

## Current PDF

- pages: 3,352;
- bytes: 16,079,448;
- SHA-256: `c02603eea8319f851fc378630f9c50cd20d23c52e93a3b6ef84fdd94f0b3b953`.

The synchronized artifact is
`output/pdf/Non-Archimedean_Pluripotential_Theory.pdf`; its hash equals the
final `manuscript/book.pdf` hash.

## Rendered audit

All physical PDF pages 997--1006, 3152--3154, 3300--3301, and 3319--3320
were rendered and inspected.  They contain respectively the
arbitrary-curve-factor statement and proofs, the affine toric fixed-point
statement and proof, the narrowed Chapter 72 problem and discussion, and
both Appendix L verification and result-ledger records.  No clipping,
overlap, margin intrusion, malformed formula, missing glyph, long identifier
overflow, orphaned heading, or poor proof break was found.

## Inventory consequence

P06.1 is narrowed but not retired.  Its residual scope consists of arbitrary
nonproduct non-quasi-smooth germs in analytic dimension at least two,
products containing a reduced singular factor of analytic dimension at
least two, and toric germs outside the verified rational fixed-point scope.
The current inventory therefore remains 53 active atomic questions in 14
formal problem environments, with tier distribution `(0,5,14,17,17)`.

No novelty or priority claim is made.
