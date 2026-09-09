# P14.8 V7 external audit — round 0 record

The first live-audit submission completed in verifier run
`20260909T041705Z_db93024aa3e5__0001_pi_434b44634__round_0` with final
verdict `wrong`, zero critical errors, and three gaps.  The result SHA-256 is
`7837d21604efff244a72e6fac967337be0ddc73248fa9e5f2a45b1b66df42b3a`.

The gaps were procedural and dependency-boundary defects, not a
counterexample to the P14.8 dichotomy:

- the packet asserted its Git binding and prior V6 review without giving the
  model authenticated evidence;
- it did not include the exact strong-openness equivalence that recovers
  divisorial Lelong data from the complete integral multiplier-ideal tower;
- it omitted ambient definitions and included an unnecessary
  (P)-equivalence conclusion whose cited internal dependencies were not
  supplied.

The repaired packet makes the source provenance an explicit conditional
boundary, supplies the ambient, strong-openness, \(\mathcal I\)-preorder, and
nonpluripolar-product excerpts, and limits the Cantor extract to the
\(\mathcal I\)-class/mass endpoint needed by P14.8.  A fresh production
review is required; this record does not support retirement.
