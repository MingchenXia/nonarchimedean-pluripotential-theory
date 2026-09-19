# P07.1 v16 Stone--exact-star--Euclidean restriction audit

Date: 20 September 2026

## Result

The packet records a formal but previously omitted consequence of the
verified Stone--exact-star--polyhedral theorem.  Taking its convex
polyhedron to be the whole affine space and restricting the resulting
sheaf identity to an arbitrary Euclidean open set gives first-stage
collapse on

`Z x X_B x Omega`.

For an open convex `Omega`, the restricted generator and comparison germs
are the joint branch--Euclidean germs already used in the independent
exact-star--Euclidean theorem.  The result therefore closes the explicitly
listed simultaneous-Stone gap.  It does not retire P07.1; the active
inventory remains 46 atoms in 14 formal problem environments.

## Dependency audit

- The whole affine space is a convex polyhedron under the manuscript's
  finite-half-space convention.
- The cited theorem proves an equality of sheaves, not merely a statement
  about global sections.  Hence the equality restricts to every ordinary
  open subset.
- Each point of the Euclidean open set has an open convex neighbourhood
  compactly contained in it, so the cited fixed-neighbourhood conclusion
  applies without any global convexity hypothesis.
- On an open convex Euclidean domain, the polyhedral generator and
  comparison germs for `P = R^d` agree locally with the independently
  defined branch--Euclidean germs.  No boundary-face condition remains.
- The common countable activity set and the compact-clopen Stone
  factorization are inherited unchanged from the cited theorem.

## Scope firewall

The corollary does not introduce affine directions on the Stone factor,
replace the exact CLD star, weaken joint convexity, or glue nonconvex or
branched chambers.  It corrects the scope ledger rather than claiming a new
regularization mechanism.

## Model-backed verification

- The first run bundled the full proofs of two old dependencies without
  their ancestors.  It returned `wrong`, with zero critical errors and seven
  dependency gaps; it reported no contradiction in the new corollary.
- The second run supplied old statements but not their proofs.  Under the
  verifier's strict dependency semantics it returned `wrong`, with one
  critical dependency error and one gap.
- The final run supplied the complete accepted V2 dependency closure for the
  exact-star--polyhedral theorem, followed by the Stone-parametrized theorem
  and the new corollary.  Local `gpt-6-astra` at `xhigh` returned final
  `correct`, with zero critical errors and zero gaps.  The checked item is
  `pi_145beff1ee11983825be4ef2`; the proof digest is
  `c70dda8876ee0012fded36518105f7816f3a1971e452f91d266127ac30601335`.

The final exact request, response, and safe HTTP headers are retained in
`model_run_full_closure/`.  The statement and proof SHA-256 digests are
`6d4a34f80820347d8d76e61af83e523528ea5e62ec174f2c3969b1ebe2604f9e`
and
`f6576932fcd0f736ca87f82548afa9d6c415ca867045f1285a7b61f5a57835f6`.
