# P03.1 curvewise scalar-defect localization: source ledger

## Live dependencies

- `def:p031-ground-field-curvewise-psh` and
  `thm:p031-affine-ground-field-perron` in
  `solver_dossiers_20260912/p031_polydisc_ground_field_perron_v3_20260912/`.
- `lem:p031-rigsmooth-curve-envelope` in the production-verified packet
  `rethlas_packets_20260830/p031_perfected_unibranch_curve_envelope_20260830/`.
- `thm:p031-canonical-scalar-retraction-normal-form` and
  `cor:p031-affine-canonical-retraction-reduction` in
  `solver_dossiers_20260920/p031_canonical_retraction_normal_form_v60_20260920/`.
- Gubler--Rabinoff, *Classical plurisubharmonic functions in
  non-Archimedean geometry* (`GR25Classical`), Definition 4.1, Sections
  3.1, 3.4.1 and 4.1.3, and Propositions 3.5(1), 4.2(5), 4.2(6).

## Verifier dependency closure

The successful standalone verification packet additionally includes the
already proved continuous-section regularization identity and compact-fiber
maximum formula, together with their proofs.  Their external inputs are:

- Poineau, *Les espaces de Berkovich sont angéliques* (`Poi13Angelic`),
  Definition 3.2, Corollaries 3.7 and 3.14, and Remark 3.13;
- Berkovich, *Spectral theory and analytic geometry over non-Archimedean
  fields* (`Berk12`), Theorem 1.2.1;
- Gubler--Rabinoff (`GR25Classical`), Section 2.9.

The bibliography is split: `GR25Classical` and `Poi13Angelic` are in
`NonArchimedean.bib`, while `Berk12` is in `ComplexGeometry.bib`.  The full
book build resolves all three keys.

## Scope discipline

The theorem is a formal consequence of these live inputs.  It does not
claim that the canonical retraction is analytic, that composition with it
preserves subharmonicity, or that the scalar-defect locus is removable.
It does not retire P03.1--P03.3.
