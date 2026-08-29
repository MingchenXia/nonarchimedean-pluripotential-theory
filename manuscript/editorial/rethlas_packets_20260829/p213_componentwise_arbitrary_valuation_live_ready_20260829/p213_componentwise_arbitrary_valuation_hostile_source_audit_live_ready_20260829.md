# P21.3 arbitrary-valuation componentwise theorem: live-ready hostile and source audit

Date: 29 August 2026

## Verdict and gate

**PASS as an exact dependency-bound reduction: zero intrinsic critical errors and
zero intrinsic proof gaps detected.**  The proposition is nevertheless still a
quarantine candidate.  It must not be submitted or integrated before the exact
revised normal-curve packet receives a correct production verdict.  After that
verdict, the dependency-closed componentwise bytes described below require their
own production verification.

The audited live-ready bytes are:

- statement
  `91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0`;
- proof
  `098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1`;
- isolated compile harness
  `3e7ac35df61c6faf2fde3c3505a89e428c2a8c6fb68e12452a72a4a9db3de9db`.

The copy differs from the earlier dependency-blocked draft only in status prose,
filenames, and the replacement of the rejected label by
`prop:p213-normal-curve-arbitrary-valuation-current-revised`.  No mathematical
step was silently changed.

## Exact theorem dependencies

The candidate explicitly depends on the following three packets.

1. Revised arbitrary-valued normal-curve classification:
   - statement
     `8c736e3df2df1efd7b6925dd4edccddfcf03cc1ee0b68250bd1219f80169be5a`;
   - proof
     `9cb4d5eef1370ef97ccf1fa51e9ece16ab418c44092df61bd1a403f3f1d99ed9`;
   - label
     `prop:p213-normal-curve-arbitrary-valuation-current-revised`.
   These are frozen revised bytes, but their production verdict remains the
   controlling promotion gate.

2. Nontrivially valued normal rigid-point zero atom:
   - statement
     `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`;
   - proof
     `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`;
   - label
     `lem:p21p3-componentwise-normal-rigid-zero-atom`;
   - production item `pi_0d4235a44db2b33950f8dd55`, verdict `correct`,
     zero critical errors and zero gaps.

3. Trivially valued Gauss--Shilov transfer of the rigid-point zero atom:
   - principal statement
     `ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a`;
   - principal proof
     `789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66`;
   - label `lem:p213-trivial-gauss-rigid-zero-atom`;
   - dependency-closed production item `pi_b63296e1cb8309bd0f35d29f`, verdict
     `correct`, zero critical errors and zero gaps.

The source copies checked in this audit are CLD25 with SHA-256
`f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`
and Ducros's 2024 curve monograph with SHA-256
`b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`.

## Hostile audit of the componentwise reduction

### Nilreduction and test-space topology

An analytic seminorm annihilates the nilradical, so the nilpotent closed
immersion is a homeomorphism and preserves completed residue fields.  A unit
modulo a nilpotent ideal lifts to a unit by the finite geometric-series
inverse.  The lifted unit has exactly the same pointwise absolute value.  Thus
ordinary moment charts in the two directions have cofinal refinements with
identical tropical images and identical Lagerberg representatives.

CLD Proposition 15.1.3(b) and its stated form and G-form variants support the
sheaf identification.  The proof does not infer the compact-test topology from
the sheaf statement: on each fixed compact support, corresponding finite moment
data have literally the same subdivisions and all the same `C^r` seminorms.
The transpose is consequently an isomorphism of current spaces for the weak
topologies and preserves positivity and both differentials.  CLD Example
7.2.12 applies to locally bounded Borel multiplication of positive currents;
the extension to a locally defined difference of positive currents is
decomposition-independent because equality of positive currents is equality of
all their coefficient measures.

The initial smooth psh cone is the same because smooth forms and positivity are
the same.  CLD Lemmas 8.1.4 and 8.1.8 then identify every transfinite stage:
successor stages use decreasing limits for `Psh` and local uniform limits for
`CPsh`, while limit stages are local unions.  Hence both the psh and continuous
psh sheaves really are nilpotent-invariant.  None of these identifications erases
the generic lengths in the fundamental cycle; that issue is treated separately.

### Normalization, conductor, component intersections, and rigidness

On each good affinoid curve chart, excellence and finiteness of normalization
(CLD Sections 11.1.10 and 11.3.1) make the normalization quotient and conductor
coherent.  Their support is proper on each reduced irreducible component and is
zero-dimensional.  A proper intersection of two distinct pure one-dimensional
components is likewise zero-dimensional.  CLD Section 11.2.5 gives local
finiteness of components, and a zero-dimensional closed analytic subspace of an
affinoid curve is finite.  Therefore the union `Z` and every inverse image `Z_i`
are closed and locally finite; the proof does not use a false global finiteness
claim.

The rigid-point step is source-valid for arbitrary valuation.  Ducros Section
4.2.18 says that the local ring of a normal analytic curve at a nonrigid point is
its residue field.  If a nonrigid point lay in `Z_i`, the proper coherent ideal
defining `Z_i` would have zero stalk in that field.  Coherence would then make the
ideal vanish on a neighborhood, contradicting zero-dimensionality.  Thus every
point of `Z_i` is rigid.  A finite morphism gives an injection of the completed
residue field at the image into a finite extension at the source; a subextension
of a finite extension of `K` is finite.  Hence points of `Z` are rigid as well.

Strictness of the normalizations is checked germwise, which is essential over a
trivially valued field where compact strict representatives need not exist.  In
CLD Lemma 11.8.5, base homogeneous degrees are torsion modulo `|K^x|`.  A
homogeneous element integral over the base graded algebra satisfies a homogeneous
monic relation, so a positive power of its degree belongs to the group generated
by base degrees.  It is therefore torsion modulo `|K^x|`; applying the same lemma
upstairs proves strictness.  Finite maps have empty relative boundary, and the
boundary-composition identity (11.4.1.3) transfers boundarylessness.

Each normal component normalization is connected.  At a deleted rigid point,
Ducros Proposition 3.5.2 makes the point unibranch.  Ducros Theorem 3.5.1 and
Section 1.3.5 make a connected analytic curve connected by injective arcs, while
Section 1.3.12 makes every interior point of such an arc pluribranch.  An arc
between two undeleted points cannot therefore pass through a deleted point.
Thus `U_i = tilde X_i minus Z_i` is nonempty and connected and meets every
hypothesis of the revised normal-curve theorem.  No quasi-smoothness or
rig-smoothness assertion is used.

### Fundamental cycles, classification, and uniqueness

CLD Definition 13.2.5, Section 13.5.2, and Proposition 16.6.3 retain the generic
multiplicities `m_i`.  Normalization has calibrated degree one over the normal
component locus.  CLD Proposition 15.2.1(a), applied to ordinary forms as a
special case of G-forms, says that an ordinary `(1,1)`-form germ vanishes wherever
`d_K<1`; in particular it vanishes on a neighborhood of every rigid point.  This
extends the cycle equalities across `Z` and yields the two stated current
identities.  The argument concerns bidegree `(0,0)` integration currents; it is
not the false claim that a bidegree `(1,1)` curvature measure has no rigid atom.

The integration current on `U_i` is nonzero independently of the variation
packet: CLD Theorem 12.11.1 makes a boundaryless, topologically separated, pure
one-dimensional analytic space very rich, and Corollary 7.3.13 gives full support
of its integration current.  This both detects each `m_i` and proves uniqueness
of every coefficient.

An arbitrary current is never pulled back through a finite normalization.  It is
restricted to `X_red minus Z`, transported only across the analytic isomorphism
there, and then classified on `U_i` by the revised normal-curve theorem.  The
difference from the component sum is supported on `Z`; every compact ordinary
top-degree test form has support disjoint from that locally finite rigid set, so
the difference is zero.  Restriction to one component open and nonvanishing of
`delta_{U_i}` prove uniqueness.  This also rules out cancellation between
different irreducible components.

### Weighted versus unweighted curvature equality

Pullback of continuous psh functions and positivity of their curvature measures
are exactly CLD Proposition 8.1.5 and Lemma 8.5.5.  Multiplying the two
fundamental-cycle identities by a continuous function is legitimate because the
integration currents are positive.  Finite proper pushforward commutes with
`d'd''`; CLD Proposition 8.5.6 gives the same identity for continuous psh
functions.  Consequently equality on `X` is the weighted identity
`sum m_i nu_{i,*} sigma_i=0`, whereas equality on `X_red` is the unweighted
identity `sum nu_{i,*} sigma_i=0`.

Off `Z`, component images are disjoint and each normalization map is an analytic
isomorphism.  Restricting either identity to one component therefore forces
`sigma_i` to vanish there (the positivity of `m_i` matters in the weighted case).
Thus `sigma_i` is a signed Radon measure supported on the locally finite rigid set
`Z_i`.

At each point of `Z_i`, the ambient normalization is good, separated, strict,
normal, pure one-dimensional, and boundaryless.  For a nontrivial valuation the
verified normal rigid-point packet applies; for the trivial valuation the
verified Gauss--Shilov packet applies.  Each of the two positive curvature
measures has zero point mass.  A signed Radon measure supported on a locally
finite set is the locally finite sum of its atoms, so `sigma_i=0`.  Starting from
either the weighted or unweighted identity yields the same componentwise
equality, and the converse is immediate.  This proves the asserted equivalence
without dividing a signed measure by a generic multiplicity at a conductor
point and without using the misindexed printed CLD Corollary 16.8.6.

Finally, the classified current is a locally finite nonnegative sum of component
integration currents.  Multiplication by the continuous function `U-V` is
defined for each positive summand and on compact test supports only finitely many
summands occur.  Proper pushforward and the already proved identity
`sigma_i=0` give `d'd''((U-V)T)=0`.  The conclusion is deliberately restricted to
continuous psh pairs; the packet does not claim the possibly discontinuous
predicate in CLD Definition 8.6.2.

## Explicitly excluded failure modes

The audit found none of the following invalid shortcuts in the exact bytes:

- no assumption that normalization is quasi-smooth or rig-smooth;
- no pullback of an arbitrary current through normalization;
- no replacement of `delta_X` by `delta_{X_red}` before checking generic
  multiplicities;
- no inference of curvature zero-atoms from the vanishing of ordinary
  top-degree form germs at rigid points;
- no use of the exponent printed in CLD Corollary 16.8.6;
- no global finiteness assumption on irreducible components or conductor points;
- no claim for weakly smooth forms, boundary points, or discontinuous psh pairs.

## Compile check

The isolated harness imports the exact two zero-atom statements and the exact
revised variation statement.  It compiled in three passes to a 12-page PDF,
SHA-256
`e06066311c5497fbbe6f77940ea3da6b534032394d3897d816130428a643b659`.
The final log has no TeX error, undefined reference or citation, multiply defined
label, or package warning.  Generated build files were kept outside the
repository.

## Dependency-materialization plan for the next production gate

Only after the revised variation packet returns `correct`, create immutable
materialized files in this order.

1. Materialized statement: byte-concatenate the nontrivial rigid zero-atom
   statement, the trivial Gauss zero-atom statement, the revised variation
   statement, and finally the live-ready componentwise statement.
2. Materialized proof: byte-concatenate the corresponding nontrivial zero-atom
   proof, trivial Gauss proof, revised variation proof, and finally the
   live-ready componentwise proof.
3. Record the four principal input hashes and the two materialized hashes in the
   request ledger; compile the exact materialized pair once more and check label
   uniqueness.
4. Submit those exact materialized bytes for one dependency-closed production
   verdict.  Archive request, response, headers, item identifier, service
   verification, and an exact-byte receipt.
5. Live integration and open-problem inventory changes are permitted only if the
   verdict is `correct` with zero critical errors and zero gaps.

No source defect intrinsic to the componentwise reduction was found.  Its sole
remaining blocker is the external production verdict on the revised variation
dependency, followed by its own dependency-closed production verification.
