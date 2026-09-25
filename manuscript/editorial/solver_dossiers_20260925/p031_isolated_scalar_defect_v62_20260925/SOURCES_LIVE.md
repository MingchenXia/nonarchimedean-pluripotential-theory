# P03.1 isolated scalar-defect nonremovability: source ledger

## Live dependencies

- `thm:p031-curvewise-scalar-defect-localization` in the immediately
  preceding live P03.1 dossier. It supplies subharmonicity of `h_g`, the
  inequality `h_g <= q_g`, and the containment
  `F_g subset closure(B_g)`.
- Thuillier, *Théorie du potentiel sur les courbes en géométrie analytique
  non archimédienne. Applications à la théorie d'Arakelov*
  (`Thu05`), Proposition 3.1.11: a subharmonic function attaining a local
  maximum is locally constant.
- Gubler--Rabinoff, *Classical plurisubharmonic functions in
  non-Archimedean geometry* (`GR25Classical`), Definition 4.1, for the
  all-scalar-extension curve test used in the corollary.

## Scope discipline

The proof is local on one test curve. It uses only upper semicontinuity of
the already subharmonic function `h_g`, equality `q_g=h_g` off the strict
defect locus, and the curve maximum principle. It does not assert that the
defect locus is closed, discrete, locally finite, polar, or nonempty. It
does not retire P03.1--P03.3.

No model-verifier result is claimed for this packet.
