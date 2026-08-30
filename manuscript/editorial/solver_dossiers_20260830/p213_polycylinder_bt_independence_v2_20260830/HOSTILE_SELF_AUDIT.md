# Hostile self-audit

## Verdict

**PASS as a quarantined repaired candidate.**

This is a self-audit only. It is not an independent exact-byte audit and not
a production verification receipt.

## Repair ledger against failed v1

1. The ambiguous v1 sentence claiming that "the same conclusion" follows
   from one polycylinder neighbourhood per point has been deleted.
2. The full theorem now repeats the quantifiers `for every open W` and uses a
   genuine ordinary-topology basis.
3. The one-polycylinder result is a separate proposition and explicitly says
   that it is fixed-domain only.
4. `Good` alone has been replaced by the conservative source-supported
   analytic umbrella: good, topologically separated, pure-dimensional, and
   without boundary. Strictness appears only where P06.2 needs it.

## Mathematical obligations checked

1. **Every-open quantifier.** Given arbitrary open `W` and `x in W`, the basis
   hypothesis gives `x in Q subset W`. No atlas-to-basis inference occurs.
2. **Difference current.** From equality of the curvature currents of `u`
   and `v`, linearity gives `d'd''[u-v]=0`; no psh closure under subtraction
   is used.
3. **Continuous multiplier.** A positive CLD current is of order zero in the
   locally differentially separated category. Thus `uT`, `vT`, and `(u-v)T`
   are defined and linear even when the multiplier changes sign.
4. **Bidegree.** Multiplication preserves bidegree. Two differentials send
   `(ell,ell)` to `(ell+1,ell+1)`, and the printed range is exactly
   `0 <= ell <= n-1`.
5. **Leibniz scope.** Positivity supplies symmetry and the statement assumes
   both `d'T=0` and `d''T=0`. For the smooth difference `h`, CLD Lemma 8.5.3
   gives `d'd''(hT)=d'd''h wedge T`; all cross terms vanish.
6. **Smooth Hessian, not merely current Hessian.** The abstract theorem
   assumes ordinary smoothness and zero smooth Hessian separately. The
   concrete theorem obtains both from the exact P06.2 formula rather than
   from an unproved injectivity of smooth forms into currents.
7. **P06.2 output.** Each annulus coordinate `S_j` is an analytic unit, so
   `-log|S_j|` is an ordinary CLD-smooth moment coordinate. The P06.2 formula
   is affine in these coordinates and has zero smooth Hessian.
8. **Analytic isomorphism.** Pullback through a genuine analytic isomorphism
   preserves continuous functions, CLD currents, current equality, ordinary
   CLD smoothness, and the smooth Hessian. No etale-local product is used.
9. **Sheaf step.** The local zero identities are identities of currents on
   ordinary open neighbourhoods and glue by the current sheaf property.
10. **Fixed-polycylinder branch.** P06.2 is applied to `h` on the entire
    domain `P`; the proof neither restricts to nor classifies arbitrary opens
    of `P`.
11. **Ambient source scope.** Topological separatedness plus goodness gives
    local differential separation in CLD. Pure dimension supplies the level
    and bidegree convention. Boundarylessness retains the printed Section
    8.5 scope. The live chapter uses the same conservative umbrella.
12. **Field and endpoint scope.** The P06.2 branches use a complete
    nontrivially valued field and strict open standard factors with radii in
    the value group. Rejected endpoint variants do not re-enter.

## Deliberately absent conclusions

- no full Bedford--Taylor predicate from a mere polycylinder cover;
- no standard-polycylinder basis theorem for a standard polycylinder;
- no extension to arbitrary quasi-smooth, toroidal, log-etale, or etale
  analytic germs;
- no discontinuous-psh Bedford--Taylor predicate;
- no retirement of P21.3;
- no production-verification claim for these v2 bytes.

## Release condition

Before live integration, the exact frozen statement/proof pair still requires
an independent hostile audit and a dependency-closed production verification.
