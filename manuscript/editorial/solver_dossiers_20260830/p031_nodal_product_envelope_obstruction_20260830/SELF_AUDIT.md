# Hostile self-audit

Verdict: **PASS FOR INDEPENDENT AUDIT; NOT PRODUCTION VERIFIED.**

## Claim ledger

- The theorem makes no claim about the raw envelope away from the rigid zero
  section.
- The theorem makes no continuity claim for the higher-dimensional
  regularized envelope.
- The theorem assumes a complete nontrivially valued field and uses a strict
  unit polydisc; it makes no trivially valued or non-strict assertion.
- The only new conclusion is persistence of the verified nodal obstruction
  after taking a smooth strict-polydisc factor.

## Checks

1. The two pullback directions give the exact identity
   \(G\circ j=P_U^{\mathrm{raw}}f\); the inequality directions were checked
   separately.
2. The inequality \(G^*\leq F\) uses continuity of \(F\), not a generally
   false commutation of upper regularization with pullback.
3. The lower bound at \(j(o)\) is obtained in the ambient product from the
   points \(j(z_m)\to j(o)\); no equality
   \(G^*\circ j=(G\circ j)^*\) is asserted.
4. The contradiction uses only the value at the node, the upper bound at the
   \(r\)-Gauss point, pullback to the rigid section, and the singleton-Shilov
   affinoid maximum principle.
5. The dimension statement includes every \(d\geq1\), so the resulting
   analytic dimensions are precisely all integers at least two.
6. The statement and proof contain no conventional theorem title and retain
   all internal equation references as \eqref.

## Mechanical checks

minimal_compile.tex compiles in three pages. The final log has no TeX
warning, undefined reference, overfull box, or underfull box. All three
pages were visually inspected on 30 August 2026.
