# Final independent hostile audit of the repaired P21.3 componentwise packet

Date: 29 August 2026

Verdict: **PASS FOR THE EXACT COMBINED BYTES, WITH ONE CLEARLY ISOLATED
CONDITIONAL DEPENDENCY.** No remaining mathematical, citation, scope, label,
compilation, or byte-ledger defect was found in the componentwise statement
and proof. The application of the separately frozen local normal rigid-point
zero-atom lemma is valid hypothesis by hypothesis. This verdict does not
promote that lemma by itself: its exact statement and proof remain a mandatory
quarantine dependency until their own production Rethlas gate is passed.

## Exact combined bytes passed

| artifact | SHA-256 |
|---|---|
| componentwise statement | `5b03b18f255625809a863c1079e9d84df146cb06a8c3b752ce08c58c700aeca8` |
| componentwise proof | `3893a89ffd59f7636a7ab160c4746fecd520b328281ac60f0bbd0401dd2d21e5` |
| compile driver | `125583c11f2faba5e1d48ab3bb8f5f3814a7120ad0a0a5b7c976ba6273d1f111` |
| frozen 12-page PDF | `3000e0aaa412d0e30cda354d3b882a8424763a9f311d2e35499c64f6ab04aeba` |
| frozen final log | `5575cdf0f8d90ce98d918d8faa64b0956ae8a2a53d8ceac6dc73307f41533333` |
| dependency ledger | `6ef287caa6281d49286a1681ef8d405e2bc0655bc1fa893d8765ef70dd682c96` |
| artifact manifest | `630d4314f1d5a07bff9fce4d1bbe040f173c78d37db5f0a3c1d65293f6a97f25` |

The dependency ledger verifies all eight rows, and the artifact manifest
verifies all nine rows. The exact imported dependencies are:

| dependency | statement SHA-256 | proof SHA-256 |
|---|---|---|
| arbitrary-field reduced curve theorem | `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21` | `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af` |
| arbitrary-field nonreduced theorem | `e7b9889f6c063d9952d61c0472290183aac07b58c8d0569cfebc5e9ea73f1a9c` | `25fe49a46b1c5cd62b0d1a5024095b47cdd49c66f594d1d86eec4f9f270c83ec` |
| normal rigid-exception theorem | `cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5` | `cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce` |
| local normal rigid-point zero-atom lemma | `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac` | `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2` |

## Closure of the earlier defects

All defects from the two earlier hostile passes are closed.

1. The classification residual is now correctly defined as
   `S:=T_red-\sum_i c_i\bar\delta_i`; the missing backslash has been repaired.
2. The weighted curvature identity on `X` is first written as an identity
   pushed forward through the nilreduction. Injectivity of `\iota_*` transfers
   it to `X_red` before any component is isolated through the reduced
   normalization. No analytic isomorphism is falsely asserted on the
   nonreduced space.
3. The duplicate zero-atom lemma environment has been removed. The compile
   driver imports exactly one definition of
   `lem:p21p3-componentwise-normal-rigid-zero-atom` from the separate packet.
4. Local holomorphic and differential separation is explicitly established
   before the Radon-measure and Borel-product results are used, both on the
   ambient spaces and on every component normalization.
5. The stray word in the curvature paragraph has been removed. Extracted
   final text contains neither `Pullback The` nor the malformed literal
   `sum_i`.
6. The README, problem statement, source audit, dependency ledger, and
   artifact manifest now describe and hash the repaired design consistently.

## Exact audit of the local zero-atom application

At a point `z` of `Z_{i,W}`, apply the imported lemma with ambient space
`X=\widetilde X_i` and open neighborhood
`\Omega=\widetilde W_i`. Every hypothesis is supplied inside the exact
combined proof:

- the proposition assumes that `K` is complete and nontrivially valued;
- `\widetilde X_i` is proved good, separated, strict, normal, pure
  one-dimensional, and boundaryless;
- finiteness of normalization over the locally finite rigid conductor and
  component-intersection locus proves that `z` is rigid;
- boundarylessness gives
  `z\in\operatorname{Int}(\widetilde X_i/K)` and
  `\Omega^\circ=\widetilde W_i`;
- normality of `\widetilde X_i` gives a normal ordinary analytic local ring at
  `z`;
- `\widetilde W_i` is an open pure one-dimensional neighborhood; and
- CLD Proposition 8.1.5 makes `\bar\nu_i^*U` and `\bar\nu_i^*V` continuous
  CLD-psh functions there.

Consequently the two measures denoted `\mu_i^U` and `\mu_i^V` in the
componentwise proof are exactly the measures in the local lemma, rather than
restrictions of differently normalized currents. Both have zero atom at
`z`. Since the signed difference is supported on the locally finite set
`Z_{i,W}`, singleton neighborhoods show that every possible coefficient is
that zero atom. Hence the signed measure vanishes.

The sets `E_i` are not used in this zero-atom application. They are used
earlier, and only earlier, to invoke the verified current classification on
the conductor complement. Thus no hidden rig-smoothness hypothesis enters
the local lemma step.

This audit validates the application of the exact local statement. The truth
and production status of that local statement remain governed by its own
independent audit and production-verification gate.

## Mathematical audit

### Nilreduction and calculus

Analytic seminorms kill nilpotents, so the reduction has the same points,
topology, completed residue fields, supports, and dimensions. Units lift
across a nilpotent quotient and retain identical pointwise norms. The lifted
and restricted moment charts therefore have identical tropicalizations and
identical Lagerberg representatives. This proves the ordinary-form and
`G`-form identifications, including wedge product, `J`, both differentials,
supports, and all three positivity cones.

On a fixed compact support, the two systems of moment-chart data are cofinal
and their `C^r` seminorms agree. Thus the compact-test identification is a
homeomorphism, not merely an algebraic bijection. Transposition gives the
current and weak-topology identification, and compatibility with closedness
and smooth multiplication. The positive-current measures agree, which gives
the stated locally bounded Borel products and, by decomposition, the products
for differences of positive currents. The proof correctly declines to define
such a product for an arbitrary order-zero current.

The transfinite psh filtration is unchanged because its initial smooth
positive-curvature stage, decreasing-limit successor stages, and local-union
limit stages are all unchanged. The analogous local-uniform-limit argument
handles continuous psh functions.

### Finite normalization and rigid exceptional loci

Excellence gives finite componentwise normalization and coherent conductor
quotient. On a reduced pure curve, the conductor misses every generic point,
and the proper intersection of two distinct components is zero-dimensional.
Local finiteness of irreducible components reduces the union to finitely many
such sets on each relatively compact affinoid neighborhood. Thus the
conductor/intersection locus is closed and locally finite.

On a strict affinoid, every zero-dimensional quotient is Artinian and every
residue field is finite over `K`; hence these points are rigid, not necessarily
`K`-rational. Finite normalization preserves rigidity and local finiteness.
Finite morphisms also preserve strictness and have empty relative boundary,
so each normalization is good, separated, strict, normal, connected, and
boundaryless.

Ducros's graph theorem and injective-arc connectivity, together with the
identification of branches at a rigid point with its normalization fibre,
show that a rigid point on a normal curve is unibranch whereas an interior
point of an injective arc is pluribranch. An arc with endpoints outside the
deleted rigid set therefore cannot cross it. This proves that every
`U_i=\widetilde X_i\setminus Z_i` is nonempty and connected and validates
every hypothesis of the normal rigid-exception theorem for
`E_i\setminus Z_i`.

The complex-analytic normalization/component and generic-cycle skill cards
were used only as hostile checklists for their failure modes. Their stated
input contracts concern proper holomorphic maps or complex Lelong currents
and do not trigger here; no result from those cards is imported into this
non-Archimedean proof. The nilpotent transverse-order skill is likewise
inapplicable because this argument uses nilreduction invariance, not a
transverse jet-order estimate.

### Integration currents and current classification

The fundamental cycle assigns the generic length `m_i` to every reduced
component, while the reduced cycle assigns coefficient one. CLD integration
of analytic cycles and the calibrated degree-one normalization off the rigid
exceptional locus give both displayed current identities. Smooth top-degree
test germs vanish at rigid points, so the identities extend across that
locus. Component local finiteness makes every sum locally finite.

Restricting to a nonempty rig-smooth open subset of one component detects its
coefficient. Therefore equality of the nonreduced and reduced integration
currents is equivalent to every `m_i` being one, which is precisely generic
reducedness along every component.

For a positive closed `(0,0)` current, nilreduction first gives a unique
positive closed current on `X_red`. It is transported through normalization
only over the genuine analytic isomorphism off the conductor; no general
pullback of currents is used. The verified classification there supplies
the coefficients `c_i`. The residual current is supported on a locally
finite rigid set, while every smooth `(1,1)` test form on a curve is supported
where `d_K\geq1` and therefore avoids that set. The residual is zero.
Restriction to a nonempty rig-smooth component locus proves uniqueness. None
of these classification arguments consumes the local zero-atom lemma.

### Curvature splitting and Bedford--Taylor independence

The multiplicity-weighted function-current identity differentiates to the
weighted signed-measure identity on `X`. Since
`\nu_{i,W}^X=\iota\circ\nu_{i,W}^{\mathrm{red}}` and `\iota_*` is injective,
this identity transfers to `X_red`. Only there are the disjoint component
images and normalization isomorphisms used. Positivity of every `m_i`
isolates each signed component measure off the conductor. The unweighted
identity gives the same support conclusion.

The exact local zero-atom application then kills the possible conductor
mass. Thus either the weighted or unweighted equality is equivalent to
componentwise equality, which proves the asserted equivalence. Finally the
classified locally finite sum, locally bounded multiplication by `U-V`,
proper pushforward, and componentwise equality give the displayed
Bedford--Taylor identity for every classified current.

## Labels, sources, build, and scope

The compile closure contains exactly one definition of every consumed label;
in particular the componentwise proposition, normal rigid-exception
proposition, its connectedness and classification items, and the imported
local lemma are neither missing nor multiply defined. The cited CLD support,
nilreduction, positivity, Radon-measure, psh-pullback, proper-pushforward,
fundamental-cycle, and integration results match their uses. The cited
Ducros graph, arc, pluribranch, and normalization-fibre results match the
connectivity argument. Tate's strict affinoid noetherianity,
Nullstellensatz, and finite-algebra results are used only to obtain the stated
rigidity and strictness conclusions.

A rebuild from a previously empty output directory produced the same
12-page compile closure. The final frozen log has no TeX error, undefined
reference or citation, multiply defined label, box warning, missing glyph, or
rerun request. The final manifest verifies that frozen PDF and log.

The residual remark is accurate within the displayed good, separated,
strict, boundaryless P21.3 ambient class. The packet does not treat a
trivially valued field, analytic dimension at least two, or a component
normalization whose non-rig-smooth locus is not contained in a locally finite
rigid set. It also expressly avoids the possibly discontinuous psh quantifier
in CLD Definition 8.6.2.

## Final promotion boundary

The exact combined statement and proof above pass this independent hostile
audit. Production promotion still requires preserving all exact dependency
bytes and obtaining the required production Rethlas result for the local
normal zero-atom lemma and for the combined candidate. No live-book or
open-problem narrowing should precede those separate production gates.

## Addendum — 29 August 2026: transitive canonical-collar dependency closure

Verdict: **PASS FOR THE REPAIRED TRANSITIVE DEPENDENCY CLOSURE.** The first
combined materialization was rejected only because it began with the reduced
curve theorem while its proof named two earlier canonical-collar results that
were absent from the materialized context. The rejection response identifies
exactly
`lem:p21p3-gf-legal-source-localization` and
`prop:p21p3-gf-virtual-annulus-bridge`; it does not identify a defect in the
componentwise theorem bytes. Those theorem bytes remain unchanged at

- statement
  `5b03b18f255625809a863c1079e9d84df146cb06a8c3b752ce08c58c700aeca8`;
  and
- proof
  `3893a89ffd59f7636a7ab160c4746fecd520b328281ac60f0bbd0401dd2d21e5`.

Since the original audit was written, the separately isolated local normal
zero-atom lemma has passed production Rethlas service-evidence run
`20260829T060048Z_469024d04e8e`, final `correct`, with zero critical errors
and zero gaps. Thus that original conditional dependency has now cleared its
own production gate; the present addendum concerns only the omitted
canonical-collar transitive bytes in the first combined materialization.

The repaired dependency ledger now begins with the exact files

| role | path | SHA-256 |
|---|---|---|
| canonical-collar bridge statement | `../../rethlas_packets_20260828/p21p3_curve_rigidity_virtual_annulus_bridge_statement_live_20260828.tex` | `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033` |
| canonical-collar bridge proof | `../../rethlas_packets_20260828/p21p3_curve_rigidity_virtual_annulus_bridge_proof_live_20260828.tex` | `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5` |

and only then lists the reduced statement and proof at hashes
`c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`
and
`01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`.
Thus grouping the ledger by statement/proof preserves the required order:
bridge statement before reduced statement and bridge proof before reduced
proof.

The bridge statement defines the two labels named by Rethlas exactly once:

- `lem:p21p3-gf-legal-source-localization` at statement line 9; and
- `prop:p21p3-gf-virtual-annulus-bridge` at statement line 78.

The bridge proof has a proof environment targeting the lemma at line 9 and a
proof environment targeting the proposition at line 62. The latter proves,
in order, its `ray`, `separation`, and `localization` items. The reduced proof
then explicitly consumes both named labels and exactly those bridge items.
An extraction of all `\cref`, `\Cref`, and `\eqref` targets from the combined
bridge-plus-reduced statement/proof closure finds no missing label and no
duplicate definition.

There is also exact production provenance for the ordering. In the verified
arbitrary-field canonical-collar request
`p21p3_curve_rigidity_arbitrary_field_live_run_20260828/request.json`, the raw
statement is byte-for-byte

`bridge statement + one newline + reduced statement`,

and the raw proof is byte-for-byte

`bridge proof + one newline + reduced proof`.

Their raw payload SHA-256 values are respectively
`f2a1c1b9f2a3d9f60422fc1697d31c5265704a73f0c27f180adc36e65d5bbda6`
and
`745c842490484fdcba1eebe0bee83cf050b3c8050fafdf751a973615414ce4fe`.
The corresponding archived response is final `correct`, with zero critical
errors and zero gaps. Hence the two added files are not newly reconstructed
surrogates: they are the exact verified predecessors of the reduced theorem.

The repaired dependency ledger contains ten rows, has SHA-256
`86bb13c523b4ead6d1eb676c4295e1b6d4234c88a248996827b8148c219aa4d1`,
and all ten rows pass read-only checksum verification.

At the time of this addendum, the earlier artifact manifest still records the
pre-synchronization hashes of the README, problem file, source audit, and
earlier eight-row dependency ledger, so those four rows fail. This is an
administrative refreeze requirement, not a failure of the ten-row transitive
closure. The artifact manifest must be regenerated after the current metadata
and dependency ledger are frozen and before archival or promotion. No rebuild
or theorem-byte edit was performed in this addendum audit.
