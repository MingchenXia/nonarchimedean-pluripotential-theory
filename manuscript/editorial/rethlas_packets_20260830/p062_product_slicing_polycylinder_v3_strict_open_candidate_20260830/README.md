# P06.2 v3 strict-open candidate

Status: **quarantined; not integrated**.

This is the fail-closed successor to the rejected v2 packet.  It preserves
only the three strict-open results that the production response explicitly
reported as passing:

1. exact fibre slicing for continuous zero-Hessian currents on strict open
   products;
2. affine rigidity on an arbitrary-field strict open annulus;
3. joint affine rigidity on an arbitrary-field strict open polycylinder.

The statement and proof make no closed-domain, half-closed-domain, endpoint,
or absolute-interior extension.  See `REPAIR_LEDGER.md` for the exact verifier
objections and the deletion ledger.

Primary files:

- `p062_product_slicing_polycylinder_v3_strict_open_statement_20260830.tex`
- `p062_product_slicing_polycylinder_v3_strict_open_proof_20260830.tex`
- `p062_product_slicing_polycylinder_v3_strict_open_minimal_compile_20260830.tex`
- `p062_product_slicing_polycylinder_v3_strict_open_minimal_compile_20260830.pdf`
- `REPAIR_LEDGER.md`
- `AUTHOR_SELF_AUDIT.md`
- `SHA256SUMS`

Release requires a new independent exact-byte hostile audit followed by a new
production Rethlas run on these exact frozen statement and proof bytes.
