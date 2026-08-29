# P21.3 componentwise rigid exceptions: source and hostile audit

Date: 29 August 2026

Status: **independently audited and production verified; eligible for live
integration after placement checks**.  The combined proposition and its
only new local dependency, the separately frozen normal rigid-point
zero-atom lemma, each have a complete proof and independent exact-byte
`PASS` reports.  The local lemma passed production Rethlas service-evidence
run `20260829T060048Z_469024d04e8e`; the combined exact dependency closure
and theorem passed controlling run `20260829T061505Z_2bf673687e93`.  Both
returned final `correct`, zero critical errors, and zero gaps.

## Dependency byte and label audit

The following files were read byte-for-byte before drafting the packet.

| role | labels consumed | statement SHA-256 | proof SHA-256 | controlling run |
|---|---|---|---|---|
| canonical-collar bridge | `lem:p21p3-gf-legal-source-localization`, `prop:p21p3-gf-virtual-annulus-bridge` | `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033` | `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5` | `20260828T042906Z_f2a1c1b9f2a3` with reduced consequence |
| arbitrary-field reduced theorem | `lem:p21p3-gfc-rigid-zero-atom`, `prop:p21p3-gfc-smooth-rigidity`, `prop:p21p3-curve-rigidity` | `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21` | `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af` | `20260828T042906Z_f2a1c1b9f2a3` |
| arbitrary-field nonreduced theorem | `prop:p21p3-curve-rigidity-nonreduced` | `e7b9889f6c063d9952d61c0472290183aac07b58c8d0569cfebc5e9ea73f1a9c` | `25fe49a46b1c5cd62b0d1a5024095b47cdd49c66f594d1d86eec4f9f270c83ec` | `20260828T051601Z_db92555a72e1` |
| normal rigid-exception theorem | `prop:p21p3-rigid-exception-extension` | `cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5` | `cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce` | `20260829T021315Z_cc0c48725114` |
| local normal rigid-point zero-atom lemma | `lem:p21p3-componentwise-normal-rigid-zero-atom` | `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac` | `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2` | `20260829T060048Z_469024d04e8e`, item `pi_0d4235a44db2b33950f8dd55` |

All controlling service runs used `gpt-5.6-sol` at `xhigh` and returned final
`correct`, zero critical errors, and zero gaps.  The reduced and nonreduced
receipts record 17/19 and 23/25 statement/source checks, respectively.  The
normal rigid-exception receipt records 14 statement checks and 26
primary-source checks.

The old smooth zero-atom lemma is not silently generalized: its printed
hypothesis is rig-smooth.  The new label
`lem:p21p3-componentwise-normal-rigid-zero-atom` is deliberately distinct,
lives in a separate packet, and is imported here by exact bytes.

The first combined materialization omitted the canonical-collar bridge even
though the imported reduced proof explicitly consumes it.  Production
Rethlas rejected that materialization with one critical error and zero gaps.
The candidate component theorem was not modified.  The repaired exact
dependency order is bridge, reduced theorem, normal rigid-exception theorem,
local normal zero-atom lemma, and finally the component theorem.  Two
independent read-only audits confirmed this transitive closure before the
repaired submission.

## Primary-source ledger

### Chambert--Loir--Ducros (`CLD25`)

- Section 11.4.4 and formula (11.4.1.3): finite morphisms have empty
  relative boundary and the boundary-composition formula transports
  boundarylessness to the reduction, components, normalizations, and open
  subspaces used in the proof.
- Sections 11.1.10, 11.2.5, and 11.3.1: excellence of good analytic local
  rings, local finiteness of irreducible components, and finiteness and
  component behavior of normalization.
- Proposition 15.1.3(b) and its form variant: forms are unchanged by a
  nilpotent closed immersion.  The packet separately checks cofinal moment
  data and identical seminorms to obtain the compact-test homeomorphism,
  rather than inferring a topological statement from a sheaf isomorphism.
- Sections 7.1--7.2 and 7.7: currents are continuous duals of compactly
  supported test forms; positive currents admit locally bounded Borel
  products; restriction and current differentials are local.
- Definition 13.2.5, Section 13.5.2, and Proposition 16.6.3: fundamental
  cycle coefficients are the generic lengths and integration agrees with
  analytic cycles.
- Propositions 3.3.6 and 15.2.1(a), together with formula (11.2.3.1): a
  smooth `(1,1)` test form on a curve has support in the locus `d_K >= 1`,
  while a rigid point has `d_K=0`.  Thus the current classification extends
  uniquely across a locally finite rigid conductor locus.
- Propositions 8.1.5 and 8.5.6 and Lemma 8.5.5: analytic pullback preserves
  continuous psh functions; their curvature currents are positive Radon
  measures; finite proper pushforward is compatible with the function
  currents and their differentials.

### Ducros, curve structure (`Ducros24CurveStructure`)

- Theorem 3.5.1 and Section 1.3.5: a connected analytic curve is a graph and
  is connected by injective arcs.
- Section 1.3.12: an interior point of an injective arc is pluribranch.
- Proposition 3.5.2: the number of branches at a rigid point is the
  cardinality of its normalization fibre.  A rigid point on a normal curve
  is therefore unibranch.

These facts prove that removing a locally finite rigid set from a connected
normal curve does not disconnect it.  This is checked for every
`U_i = tilde X_i minus Z_i` before the normal rigid-exception theorem is
invoked.

### Tate, strict affinoids (`Tate71Rigid`)

- Theorem 4.5: strict affinoid algebras are noetherian and satisfy the
  strict affinoid Nullstellensatz.  A zero-dimensional strict affinoid
  algebra is Artinian and all of its analytic points have completed residue
  field finite over `K`.
- Theorem 4.4: finite algebras over strict affinoid algebras are strict.

This is exactly where strictness is consumed.  It proves that the conductor,
component-intersection locus, and their finite normalization preimages are
locally finite sets of rigid points over an arbitrary ground field; no
algebraic-closedness or degree-one point is assumed.

## Logical ledger

1. Nilreduction preserves analytic points and moment tropicalizations.
   Cofinal lifted chart data give a homeomorphism of compact test spaces;
   transposition gives currents, positivity, closedness, and weak topology.
2. Fundamental cycles give the multiplicity-weighted and unweighted
   integration-current identities.  The coefficients `m_i` are retained.
3. The conductor and distinct-component intersections form a closed locally
   finite rigid set `Z`; its normalization preimage `Z_i` is locally finite
   and rigid.
4. The open normal curve `U_i = tilde X_i minus Z_i` is explicitly proved
   nonempty and connected.  Its residual exceptional set
   `E_i minus Z_i` is locally finite rigid and has rig-smooth complement.
5. The verified normal rigid-exception theorem classifies the restriction
   of the current on `U_i`.  The proof never pulls an arbitrary current
   through normalization; it transports it only across the analytic
   isomorphism over `X_red minus Z`.
6. Smooth top-degree tests avoid `Z`, so the componentwise current identity
   extends globally.  Restriction to a nonempty rig-smooth open component
   locus proves uniqueness.
7. Weighted or unweighted equality of curvature currents implies that each
   signed component measure is supported on `Z_i`.
8. The separately frozen normal rigid-point zero-atom lemma kills both positive
   measures at every point of `Z_i`; local finiteness then forces each signed
   component measure to vanish identically.
9. This componentwise equality proves both the weighted/unweighted
   equivalence and Bedford--Taylor independence for every classified
   current.

Items 1--6 are unconditional consequences of the verified dependencies and
the cited sources.  Item 8 has passed independent source and exact-byte
audit and production Rethlas verification.

## Hostile boundary audit

- **No illicit current pullback.**  There is no general pullback of the
  positive current through normalization.  Only restriction and transport
  through the normalization isomorphism away from `Z` are used.
- **No hidden finite-component hypothesis.**  Irreducible components and
  all displayed sums are locally finite; every compact test support meets
  only finitely many terms.
- **No algebraic-closedness shortcut.**  Rigid means finite completed
  residue field over `K`, not `K`-rational.  Finite inseparable extensions
  are allowed.
- **No disconnection gap.**  Normality makes deleted rigid points
  unibranch; an interior point of a connecting arc is pluribranch.  Thus
  `U_i` is connected, and the normal theorem is not applied component by
  component without proving this.
- **No support-at-a-point current.**  A smooth top-degree test germ vanishes
  at a rigid point.  This is the precise reason a current identity already
  valid off `Z` extends across `Z`; it is stronger than a measure atom
  statement and is used only for current classification.
- **Zero atoms are still needed for curvature.**  Curvature measures are
  Radon measures and can have point masses even though smooth top-degree
  test germs vanish there in the current-classification calculation.  The
  two arguments are not conflated.
- **Generic multiplicities cannot cancel.**  The weighted identity retains
  every positive integer `m_i`.  Away from `Z`, component images are
  disjoint, so either the weighted or unweighted equality isolates each
  signed component measure.
- **Nilpotents do not create forms.**  Seminorms kill nilpotents, but the
  integration current still remembers generic lengths.  The packet states
  both facts and never identifies `delta_X` with `delta_Xred` unless all
  generic multiplicities are one.
- **No discontinuous-potential overclaim.**  Every product and curvature
  splitting in the proof uses continuous psh functions.
- **No higher-dimensional inference.**  The proof uses one-dimensional
  conductor, graph, and measure facts and makes no claim in dimension at
  least two.

## The separately frozen lemma: completed source route

The separate proof uses the one-dimensional excellent normal local ring at
the rigid point as a discrete valuation ring, chooses a uniformizer, and
uses CLD's local finite-flat construction to obtain a tube over a disc with
singleton central fibre.  CLD's calibrated-degree comparison and proper
pushforward formula then give a uniform total-variation bound for radial
cutoffs.  The resulting estimate has the form

`log(R/r) * mu_u({z}) <= constant * sup |u|`,

and forces the atom to vanish as admissible radii tend to zero.  The frozen
proof explicitly checks analytic flatness, the imperfect/inseparable ground
field case, boundary control, constant positive degree, smooth extension of
the radial cutoff, and the Radon-measure hypotheses.  Independent exact-byte
audit found no remaining defect.  Production Rethlas service-evidence run
`20260829T060048Z_469024d04e8e`, item
`pi_0d4235a44db2b33950f8dd55`, returned final `correct`, zero critical
errors, and zero gaps.  Only the combined theorem's production and live-book
placement gates remained at that stage.  The combined production gate has
now passed; only the live-placement compile and visual checks remain.

## Controlling combined production record

The frozen candidate statement and proof hashes are
`5b03b18f255625809a863c1079e9d84df146cb06a8c3b752ce08c58c700aeca8`
and
`3893a89ffd59f7636a7ab160c4746fecd520b328281ac60f0bbd0401dd2d21e5`.
After prepending the exact bridge, reduced, normal rigid-exception, and local
zero-atom dependency bytes in logical order, the materialized statement and
proof hashes were
`2bf673687e935bcdae91550158344647cb1ca1cd4ae0a5040109aeb5fb2f3cbc`
and
`a27c40fbb1328b008acab07b871f50a778c34bab2b0f1d05e3a6d9d229839716`.

Production Rethlas service-evidence run
`20260829T061505Z_2bf673687e93`, item
`pi_ee24d64b88f0c4e60ad1acbd`, used `gpt-5.6-sol` at `xhigh` and returned
final `correct`, zero critical errors, and zero gaps.  The returned proof
digest is exactly the materialized proof hash.  Its item report explicitly
records that the complete untruncated localization, virtual-annulus,
classification, zero-atom, normalization, nilreduction, and
Bedford--Taylor argument was checked.  The earlier missing-bridge result
remains archived as a noncontrolling final `wrong`; it is not conflated with
this repaired dependency-closed run.

## Exact residual narrowing

The frozen local lemma and combined packet have both passed production
verification.  Within the displayed good/separated/strict/boundaryless
P21.3 ambient class, the remaining one-dimensional cases are:

1. a trivially valued ground field; and
2. a component normalization whose non-rig-smooth locus is not contained in
   a locally finite set of rigid points.

Reducibility, nonreducedness, arbitrary generic multiplicities, and locally
finite rigid exceptional loci on component normalizations are removed
from the residual list.  Analytic dimension at least two remains open, and
the literal possibly discontinuous CLD Definition 8.6.2 remains a separate
scope boundary rather than a retired atom.
