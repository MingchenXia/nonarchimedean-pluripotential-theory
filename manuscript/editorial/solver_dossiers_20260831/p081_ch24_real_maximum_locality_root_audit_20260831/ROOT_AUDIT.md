# Root technical review: real model inputs in Chapter24 locality

31 August 2026. Root read the complete three replacement proofs, both
ancillary replacements, the dependence ledger and the read-only validator.
The fragment author is p081. Root supplied the general approximation/local
test route when assigning this repair, so this is a technical parent review,
not wholly fresh independent review or production acceptance.

No remaining gap was found in these bounded replacements relative to the
stated standard BFJ inputs and the separately gated Chapter20/21 repair.
The maximum and comparison conclusions retain real model inputs and the
same fixed real theta; they are not weakened to rational-input statements.

## Exact scope and proof checks

1. For rational inputs, the corrected maximum theorem gives an actual
   rational model maximum. On one common SNC model, affine restrictions
   along an incident edge imply that a strictly winning value at x_E wins
   weakly at the other endpoint; otherwise the maximum has a genuine
   corner and is not affine. Thus the difference divisor has zero
   coefficients on E and every component meeting E. Clearing rational
   denominators makes its line-bundle restriction to E trivial, so the
   two numerical component products and their b_E-weighted masses agree.
   Nothing requires rational theta or integer intersection coefficients.
2. For real inputs, fixed-form rational approximation supplies uniformly
   convergent rational psh models. The maximum inequality gives uniform
   convergence of their maxima. The already constructed continuous MA
   operator is uniformly continuous in this sense, so both measures
   converge weakly. The limiting maximum is continuous psh, not asserted
   to be model.
3. A compact subset of the fixed strict set has a strictly positive
   minimum gap between the original continuous functions. Approximation
   preserves that inequality on the compact set. The rational formula
   can therefore be tested against every continuous function supported
   there and passed to the weak limit. Open subspaces of the compact
   Hausdorff analytic space are locally compact Hausdorff; compactly
   supported continuous functions extend by zero, and Radon uniqueness
   gives the desired measure restriction. No moving-set weak convergence
   or bounded/plurifine locality theorem is used.
4. The open-locality corollary has its own direct argument for real
   divisors. Equality on an initial edge segment forces equality along
   that entire affine edge. Expressing the difference as a real sum of
   Cartier components disjoint from E gives zero numerical restriction.
   The text no longer assigns an honest line bundle to an arbitrary real
   divisor, and the mixed coefficient argument retains all n slots.
5. Comparison applies the proved real-input strict-locus identity twice
   to phi and psi-epsilon. The maximum is merely continuous; its positive
   total mass is supplied by the earlier bounded operator. Dropping
   contact mass yields the displayed estimate. Continuity from below for
   the fixed measure MA(psi), along epsilon=1/m, gives the original strict
   comparison inequality. This step does not require a model determining
   the maximum.

The three theorem statements and all179 labels are unchanged. The uniform
operator and the bounded operator appear before this locality section;
their proofs use model integration by parts, uniform estimates, monotone
extension and dense tests, not the locality result under repair. The new
fixed-form-density input does not use Chapter24. The dependence route is
therefore acyclic relative to these inputs. This does not independently
certify their entire manuscript proofs.

## Exact objects and exclusions

Manifest SHA256:
408c1c750c116696e2d43a3466038e84e14ab48e37cb6f5995fec5e501eb6185.
Full proposed chapter SHA256:
b831435e0e66562d10d368f359792c017c53160b0acf4e895b4d23f0d7c6238d.

All17 manifest entries are independently rehashed by verify.mjs. The
inspected author validator is rerun read-only, checking exact five-span
assembly, byte-identical statements, label preservation, outside-span
parent preservation, source hashes and the portable cumulative patch.
The alternate incremental patch and cumulative patch must not both be
applied. The Chapter20/21 parent cited by the candidate stays frozen;
its revised1 changes only the separately reviewed exposition/source
corrections, not the density or maximum arguments used here.

This review excludes the remainder of the full copied chapter, including
its author's recorded mass-versus-component-degree terminology in the
later example. It does not approve any live integration, clear the
production gate, or count a new solved open problem. No production call
or live mathematical edit is made here.
