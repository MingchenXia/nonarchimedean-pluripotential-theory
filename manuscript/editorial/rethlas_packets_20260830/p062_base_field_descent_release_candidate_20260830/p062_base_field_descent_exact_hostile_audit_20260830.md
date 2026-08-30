# Exact-byte hostile audit: P06.2 base-field trace and conditional descent

Date: 30 August 2026

Verdict: **PASS**.  The unconditional arbitrary-field constancy theorem
remains fail-closed; the two exact propositions below do not assert it.

Frozen input digests:

- statement:
  7510083fecda2d561c4ce2a1b35d08377268ef48adda2b242172428dbd39caec;
- proof:
  77a013d4e655d288d8803c9650df5446bed570de2644591edddfc116c323eab2.

The independent audit checked the following points against primary sources.

1. Gubler--Jell--Rabinoff work over an arbitrary complete nontrivially
   valued field.  Their Proposition 11.1 and Example 11.7 give the
   calibrated weight-one split-torus formula in that scope.
2. Burgos Gil--Gubler--Jell--Künnemann, Proposition 2.3.6, gives the
   top-degree toric support formula without an algebraic-closedness
   hypothesis.
3. The proof chooses \(r_i<\rho_i<R_i\) before forming the trace, so every
   radius asserted in the statement is covered.
4. Berkovich, Proposition 1.5.5(i)--(ii), places every translated punctured
   polydisc used in the closed case inside the absolute analytic interior.
5. Rigid-point density and the density of the divisible value group justify
   the algebraically closed scalar-extension exhaustion.
6. Chambert--Loir--Ducros, Section 11.1.9, gives surjectivity of
   \(X_L\to X\).  Sections 12.4.5--12.4.6 make scalar extension an affined
   G-tropical morphism, so Proposition 8.1.5 applies.
7. The open polydisc after scalar extension is separated, pure
   \(n\)-dimensional, and boundaryless; the continuous pullbacks are locally
   integrable.  Thus all hypotheses of Chambert--Loir--Ducros,
   Proposition 8.3.1(a), are present.

No logical gap, source-scope error, or overclaim was found in the frozen
bytes.  The audit explicitly does **not** infer that
\(\mathrm d'\mathrm d''[h]=0\) is stable under arbitrary scalar extension.
