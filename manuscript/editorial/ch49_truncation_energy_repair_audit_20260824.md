# Chapter 49 truncation-energy repair audit

**Date:** 2026-08-24 (Asia/Shanghai)  
**Scope:** `lem:ch49-truncation-energy` and
`rem:ch49-truncation-sharp` in
`parts/part4/ch49_linear_growth.tex`  
**Status:** source repaired and exact intake rebuilt.  The subsequent exact
statement-proof-sharpness submission passed production run
`20260824T041218Z_0c95825dbb06`, final `correct`, zero critical errors, and
zero gaps.  This audit is not itself the receipt; the controlling receipt is
`rethlas_receipts_20260824/ch49_truncation_energy_receipt.md`.

## Trigger

The production check of the superseded full payload
`188eccbbd1752ef86ba9528e41d06bf9a626c5416e771b56e5faf6fa4679f7b9`
returned `wrong` with zero critical errors and eight missing-context gaps.
The archived diagnostic is
`rethlas_packets_20260824/ch49_truncation_energy_failed_gate_20260824.json`.
Its objections concerned unavailable dependency statements and omitted
calculations, not a counterexample to the estimate.

## Repair plan and execution

1. Derive bounded finite energy directly from energy monotonicity between the
   two constant barriers; do not cite bounded finite energy as a black box.
2. State the exact translation, decreasing-pairing, mixed-duality, positivity,
   and mass-one inputs used by the argument.
3. Start at the PL telescoping identity, rewrite every vertical-factor term as
   a difference of two finite psh pairings, and only then pass to the decreasing
   limit.  This removes any hidden subtraction of infinities.
4. Reprove the maximum principle from a fixed-class Fubini--Study
   regularization and compute the reference measure on the trivial test
   configuration, giving `mu_0=delta_(v_triv)` with its normalization visible.
5. For sharpness on projective space, write the weighted Fubini--Study function
   explicitly, prove its range by weight comparison, compute its convex
   conjugate `1+m_1` on the reflected simplex, and integrate it.
6. Reproduce the point-blowup and smooth-conic deformation-to-the-normal-cone
   intersection calculations in the adjacent remark instead of referring to
   remote examples for the numerical conclusions.
7. Rebuild every exact extract, target, packet, manifest, and checksum; test
   byte identity against the live chapter and compile a focused chapter slice.

All seven steps were carried out.  The new equations are numbered
`(49.6a)`--`(49.6e)`, leaving the pre-existing `(49.7)` onward unchanged.

## Mathematical check

For `c-a<=psi<=c`, monotonicity gives
`c-a<=E_omega(psi)<=c`, hence finite energy.  The PL telescope and normalized
mixed duality yield

`(n+1)E_omega(psi)=sum_(j=0)^n integral psi d mu_j`.

The trivial test configuration has one reduced central component of
coefficient `V`, so `mu_0=delta_(v_triv)` and its integral is `c`.  Subtracting
`(n+1)c` leaves exactly `n` probability-measure integrals in `[-a,0]`, giving
the coefficient `n/(n+1)`.

For the standard simplex, the sharpness potential has convex conjugate
`1+m_1` on `-P`; the mean of `m_1` is `-1/(n+1)`, so its energy is
`-n/(n+1)`.  On the point deformation, `(H-E)^3=-1`, giving `-1/3`.  On the
conic deformation, `HE^2=-2`, `E^3=-4`, hence
`(H-cE)^3=-6c^2+4c^3`; at `c=1/2` the energy is `-1/3`, equal to
`-(2/3)(1/2)`.

## Final exact hashes

- live Chapter 49 source:
  `c6755ba48b4c8295b72f6e9e4c22697c9e66acb2621c9304930d601737ec440a`
- exact lemma statement:
  `87943e4ffca417bdd6fde859bc299177a18827a1754ceff8231de8624a3078f2`
- exact proof:
  `9c927a7d5c01d0f169825578cb0e9627cedee32c0fca575cd4b357e30086242b`
- exact sharpness remark:
  `5289e0ab7a676d7e09e584d7a4bc5972a8ef9cb36c9a4f59c36da644dd59027b`
- exact lemma plus proof:
  `aa9be74a09af5db3b9184f04cf9710c2abc9843867d5df5426310045390add25`
- exact full proof payload:
  `312ac46575cb6fba6a0858e4eff38ad78cd223a0560ca0faa731e6c5396c99a2`
- Rethlas target statement:
  `0c95825dbb063f1f257298e2ba12fd03e41645eba09aa320646e18f5b3f378e7`
- intake packet:
  `2b226689372bb931a816a1f7480da5854be40e269bba4b096b68e6c10420de2f`
- manifest:
  `429a57cfba0a2f41e722cd308df76dba30c8c04dc71af963f8a7826ff9bd5dc3`

The manifest digest in this dated list is historical pre-submission
metadata.  Those bytes were not retained, and the digest is not the hash of
the current manifest; the current manifest and its digest are identified in
the production receipt.

`SHA256SUMS` verifies all listed Chapter 49 artifacts.  Each exact extract is
byte-identical to its declared live-source slice.  A focused 59-page build of
the current Chapter 49 source completed without a LaTeX error.  The excluded
arXiv:1710.09731 source is not used.
