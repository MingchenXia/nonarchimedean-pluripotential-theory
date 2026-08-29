# P21.3 arbitrary-valuation componentwise candidate: conditional audit

Date: 29 August 2026

## Verdict

**PASS only as a conditional reduction; dependency blocked as a theorem.**
Assuming a future corrected and verified version of
`prop:p213-normal-curve-arbitrary-valuation-current`, the componentwise
argument has no additional critical error or gap.  The current exact
variation-graph proof was rejected in production verification, so the
componentwise proposition is not established and must not be cited or
integrated live.

The audited conditional bytes are:

- statement
  `ef35a42f0d480d14ee610b9c149267b1a27c11395b517bedfd30e8c6fed598bc`;
- proof
  `d6b0348c6389842ab52ee01cc2bb363af81c6f7832f0f12366b595190d3d9564`;
- compile harness
  `79626e3c22f475edab42fe1e463d2c0b3f2b440c662c04eb1e2a44383bfd9e5d`;
- source audit
  `655330c4e0c0969ee8679e8e6d682dc94d67158190ed5a3d406634023ccbe4e5`.

## Reduction checks

The independent hostile pass checked the following points conditionally on
the single normal-curve classification input.

1. Nilreduction preserves the ordinary and G-form calculi, compact-test
   topology, currents, positivity, closedness, psh functions, and the
   stated Borel products, while fundamental cycles still retain generic
   multiplicity.
2. The conductor and pairwise component intersections are zero-dimensional
   and locally finite.  Their inverse images in the normal component curves
   are rigid by Ducros Section 4.2.18; finite residue-field extension makes
   their images rigid as well.  This argument is valid for trivial and
   nontrivial valuations.
3. The germwise strictness argument through CLD Lemma 11.8.5 is compatible
   with finite normalization and avoids a nonexistent compact strict
   neighborhood over a trivially valued field.
4. Removing the locally finite rigid set does not disconnect a connected
   normal curve: deleted points are unibranch, while an interior point of a
   connecting injective arc is pluribranch.
5. Fundamental-cycle identities and the extension of current identities
   across the rigid locus use ordinary top-degree test support, not a false
   measure-atom inference.
6. The current is transported through normalization only on the open locus
   where normalization is an analytic isomorphism; no unsupported pullback
   of an arbitrary current is used.
7. Weighted and unweighted curvature equalities isolate signed component
   measures off the conductor.  The production-verified nontrivially valued
   zero-atom lemma and the production-verified trivially valued Gauss
   transfer then kill every rigid conductor atom.

The first draft used the rejected variation localization merely to prove
that `delta_{U_i}` is nonzero.  That unnecessary dependency has been
removed.  CLD Theorem 12.11.1 makes `U_i` very rich and CLD Corollary
7.3.13 gives `Supp(delta_{U_i})=U_i` directly.

## Compile

The dependency-marked isolated harness compiled cleanly in three passes to
twelve pages.  The log has no TeX error, undefined reference or citation,
or multiply defined label.  Generated output was kept outside the
repository.

The only promotion path is to replace the rejected normal-curve input by
corrected exact bytes, rebind and re-audit this packet, and then obtain a
dependency-closed production verdict.  Until then the packet remains a
draft reduction, not a mathematical result of the book.
