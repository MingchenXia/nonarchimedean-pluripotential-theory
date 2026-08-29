# Verification objective: P21.3 componentwise rigid exceptions

Date: 29 August 2026

## Candidate conclusion

For a good separated strict boundaryless pure analytic curve over a complete
nontrivially valued field, allow arbitrary nilpotent structure and arbitrary
locally finite collections of reduced irreducible components.  Assume each
component normalization is rig-smooth outside a locally finite set of rigid
points.  Prove:

1. ordinary and `G`-form calculus, compact-test topologies, currents,
   positivity, closedness, admissible products, and continuous psh sheaves
   are invariant under nilreduction;
2. integration currents retain the generic multiplicities of the
   fundamental cycle;
3. every positive closed CLD `(0,0)` current is a unique locally finite
   nonnegative combination of the normalized reduced-component currents;
4. equality of the multiplicity-weighted curvature currents on the
   nonreduced curve is equivalent to equality of the unweighted curvature
   currents on the reduction; and
5. every classified current has Bedford--Taylor independence for continuous
   psh pairs.

## Separately frozen local dependency

The only additional local input is
`lem:p21p3-componentwise-normal-rigid-zero-atom`: at an interior rigid point
whose analytic local ring is normal, the curvature measure of a continuous
CLD-psh function on a pure one-dimensional neighborhood has zero mass at
that point.

The existing rig-smooth zero-atom lemma is insufficient precisely when a
preimage of the conductor or a component intersection lies in the
non-rig-smooth exceptional set of the normalization.  A separate full proof
has now been frozen, has passed independent exact-byte hostile audit, and has
passed production Rethlas service-evidence run
`20260829T060048Z_469024d04e8e` with final `correct`, zero critical errors,
and zero gaps.  No other proof step depends on a new local statement.

## Required hostile checks

- Do not pull an arbitrary current through normalization.  Restrict to the
  conductor complement, where normalization is an analytic isomorphism.
- Prove the conductor/intersection locus and its normalization preimage are
  locally finite rigid sets over the original field.
- Prove deletion of that preimage does not disconnect a normal component.
- Apply the verified normal rigid-exception classification only after every
  hypothesis has been checked on the resulting open curve.
- Retain the generic multiplicities in the function-current identity.
- Derive componentwise support of each signed curvature measure from either
  the weighted or unweighted equality, then use the zero-atom input to kill
  it point by point.
- Distinguish current/calculus invariance under reduction from the failure of
  the integration current to be invariant when a generic multiplicity is
  greater than one.
- Keep the continuous-potential scope separate from the literal possibly
  discontinuous predicate in CLD Definition 8.6.2.

## Promotion gate

The packet-level gates are complete:

1. the separately frozen normal rigid-point zero-atom bytes were preserved
   and passed source, independent, and production verification;
2. the unchanged combined candidate statement and proof passed two
   independent exact-byte audits;
3. the exact transitive dependency closure and candidate were submitted to
   production Rethlas using `gpt-5.6-sol` at `xhigh`;
4. controlling service-evidence run
   `20260829T061505Z_2bf673687e93`, item
   `pi_ee24d64b88f0c4e60ad1acbd`, returned final `correct`, zero critical
   errors, and zero gaps; and
5. the request, response, safe headers, service evidence, receipt, and
   hashes are archived in this packet.

The materialized statement and proof hashes are
`2bf673687e935bcdae91550158344647cb1ca1cd4ae0a5040109aeb5fb2f3cbc`
and
`a27c40fbb1328b008acab07b871f50a778c34bab2b0f1d05e3a6d9d229839716`.
The earlier materialization omitted the canonical-collar bridge and is
permanently retained as a noncontrolling final `wrong` result; the repaired
submission changed only the dependency closure, not the candidate theorem
or proof bytes.

Before narrowing Chapter 72 and the atomic inventory, import the frozen
candidate files unchanged, compile the intended live placement, and inspect
the affected pages visually.
