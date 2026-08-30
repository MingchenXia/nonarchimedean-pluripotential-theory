# P08.1 isolated curve packet

This directory stages the independently audited P08.1 smooth algebraic curve
candidate. It is an isolated editorial packet only: nothing here has been
integrated into the live manuscript, bibliography, Chapter 72, or atomic
inventory, and no production Rethlas call has been made.

The theorem is intentionally untitled. Its scope is a smooth proper connected
**algebraic** curve over an algebraically closed complete non-Archimedean field
with nontrivial absolute value. The packet makes no claim for nonalgebraized
proper analytic curves, non-algebraically-closed fields, trivially valued
fields, or singular curves.

## Frozen files

- `p081_curve_local_global_statement_20260830.tex`: exact theorem statement
  extracted from the audited source.
- `p081_curve_local_global_source_aware_proof_20260830.tex`: exact proof and
  comparison remark, including all labels, `\cref`, and source citations.
- `HOSTILE_AUDIT.md`: exact latest independent hostile audit.
- `SOURCE_MATRIX.md`: production dependency and scope ledger.
- `p081_curve_local_global_compile_20260830.tex`: minimal standalone compile
  harness with a local bibliography.

The two references
`thm:p063-current-psh-ordinary-regularization` and
`thm:ch21-continuous-zhang` are live-manuscript comparison dependencies in the
remark only. They are deliberately not synthesized in the isolated wrapper,
so a standalone compile may report those two references as undefined.
