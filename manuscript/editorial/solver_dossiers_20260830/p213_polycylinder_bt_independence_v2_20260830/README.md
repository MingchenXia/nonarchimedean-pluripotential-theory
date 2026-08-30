# P21.3 strict-open-polycylinder Bedford--Taylor bridge, repaired v2

## Disposition

Quarantined research candidate. It is not integrated and has not been sent
to production verification.

This v2 preserves the failed v1 sibling dossier and repairs both findings of
its independent exact-byte audit:

1. full continuous-pair Bedford--Taylor independence is asserted only when
   standard strict open polycylinders form a genuine basis of the ordinary
   topology, so they refine every open set;
2. the result for one standard strict open polycylinder is stated separately
   as an identity for a pair defined on the whole polycylinder, with an
   explicit denial of the every-open predicate;
3. the analytic framework is restricted to good, topologically separated,
   pure-dimensional spaces without boundary; strictness and a nontrivial
   absolute value are added in the P06.2 polycylinder applications.

The candidate is a precise bridge

```text
P06.2 zero-current regularity on every member of a topology basis
    => ordinary smooth zero Hessian on that basis
    => smooth CLD Leibniz identity
    => continuous-pair Bedford--Taylor independence on every open set.
```

It does not assert that a standard polycylinder has a basis of standard
polycylinders, and it does not retire P21.3 in general.

## Principal files

- `p213_polycylinder_bt_independence_v2_statement_20260830.tex`
- `p213_polycylinder_bt_independence_v2_proof_20260830.tex`
- `SOURCE_MATRIX.md`
- `SCOPE_FIREWALL.md`
- `HOSTILE_SELF_AUDIT.md`
- `p213_polycylinder_bt_independence_v2_compile_20260830.tex`
