# P06.2 product slicing and arbitrary-field polycylinders, v2

Date: 30 August 2026

Status: **quarantined v2 repair candidate; author self-audit only**. This
packet has not been submitted to Rethlas and is not authorized for live-book
integration. Promotion requires a new independent exact-byte hostile audit
and a fresh production Rethlas verification.

## Frozen-v1 lineage

The failed v1 files were not edited or overwritten:

- statement SHA-256:
  `ddafa0a3c3e60d92090ef6301b53a9cfb923c58c5467f69c5f988e9fbf4a930b`;
- proof SHA-256:
  `c870aa8a6f44d135e434b979cea04943d6163cccd8cbec27e91bd9eae5bf4cfe`.

The controlling negative production response has SHA-256
`9658be614a25bc74788023c4c83bfec07f054a93b265d895d1d5e66a4779e490`.
It reported exactly two load-bearing gaps. The v2 proof changes only those
two mathematical passages:

1. The fibre-test spreading paragraph is replaced by the ambient-germ and
   compact ambient-partition proof audited in
   `../p062_product_slicing_gap1_repair_20260830/FIBRE_SMOOTH_EXTENSION_MEMO.md`
   (SHA-256
   `687d2b32161d4597e8bf53ccbdf433389ebb3a5e44b15a2cae397f5b72aa9b20`).
2. The polyannulus factorization now contains the iterated Gauss-norm,
   order-independence, and Gauss-section-continuity argument based on
   `../p062_product_slicing_polycylinder_production_run_20260830/GAUSS_COMPATIBILITY_REPAIR.tex`
   (SHA-256
   `fca9c3bd3bb9e9fb5f8374207127a6ada9c7af200a78a9031abb8990e9fbae77`).

The mathematical statements are unchanged from v1. Their v2 file has a
new quarantine header and is frozen separately by `SHA256SUMS`.

## Files

- `p062_product_slicing_polycylinder_v2_statement_20260830.tex`;
- `p062_product_slicing_polycylinder_v2_proof_20260830.tex`;
- `p062_product_slicing_polycylinder_v2_minimal_compile_20260830.tex`;
- `SOURCE_MATRIX.md`;
- `HOSTILE_AUDIT_TARGETS.md`;
- `AUTHOR_SELF_AUDIT.md`;
- `SHA256SUMS`.

The dependency-closed production request must again include the exact
verified statement/proof bytes defining
`prop:p062-rational-centred-traces`,
`prop:p062-finite-flat-continuous-trace`, and
`prop:p062-arbitrary-field-disc`.
