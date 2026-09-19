# Source audit

## Published source

Walter Gubler, Philipp Jell, and Joseph Rabinoff, *Forms on Berkovich
spaces based on harmonic tropicalizations*, Bulletin de la Société
Mathématique de France **154** (2026), no. 1, 135--238,
DOI `10.24033/bsmf.2919`. The manuscript bibliography key is `GJR26`.

The inspected publisher PDF was:

- temporary path: `/tmp/GUBLER_JELL_RABINOFF.pdf`;
- SHA-256:
  `acf1c49e853f5f126e02d694eacd4bea0cf018ab5d396830aa09d17b72d2884c`;
- title and authors in PDF metadata agree with the published record;
- 106 PDF pages.

## Exact locators

- Printed p. 175, proof of Proposition 5.11 (PDF page 43): for a finite,
  flat, surjective morphism of good strictly analytic spaces, the proof
  invokes Berkovich Proposition 3.2.7 to state that the map is open. This is
  the source used for the branch-retention step.
- Printed p. 190, §7.9 (PDF page 58): LFS at a point is equivalent to a local
  nonnegative real linear combination of functions
  `max{-log|f_1|,...,-log|f_n|}` with the `f_i` invertible analytic. This
  is the source used for the local LFS normal form and the inclusion of the
  rational subclass.

The characteristic-polynomial spectral-radius identity, rational
common-denominator compression, one-sided rationalization, complete-fiber
baseline argument, and defect identities are proved in the live packet
rather than attributed to these source passages.

## Provenance boundary

The standalone live proof was reconstructed from:

- `p031_rational_lfs_finite_flat_descent_v36_20260913`;
- `p031_local_rational_cofinality_v37_20260913`;
- `p031_finite_flat_pl_defect_balance_v48_20260913`.

It deliberately excludes claims specific to:

- `p031_globalization_defect_balance_v38_20260913`;
- `p031_orbit_maximum_repair_v44_20260913`;
- `p031_local_repair_collar_threshold_v49_20260913`.

No unpublished assertion from those excluded packets is used.
