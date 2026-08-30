# Independent exact-byte hostile re-audit: P06.2 endpoint polycylinder v4

Date: 30 August 2026.

## Verdict

**PASS as a frozen, quarantined research candidate.**

- Critical errors: **0**.
- Mathematical/proof gaps: **0**.
- Source/dependency gaps: **0**.
- Frozen-byte mismatches: **0**.
- Compile failures: **0**.
- Undefined references/citations: **0**.
- Nonfatal compile diagnostics: **3 underfull boxes in audit wrappers**.
- Visual legibility defects: **0**.

This verdict does not constitute production verification or authorize live-book
integration.  The new source-correct strict-open bytes are explicitly
quarantined pending production review.

## Exact target and integrity

Frozen dossier:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260830/p062_endpoint_polycylinder_rigid_slicing_v4_20260830/`

| Artifact | SHA-256 | Result |
|---|---|---|
| principal statement | `56ffaad6c42e0a14c56279e263d326120ce03f6ae132d8261deee56ff9ca7663` | match |
| principal proof | `2616ac69cd450010b8f0d108d030bd69d2ff2728cad9641ad7d9d0e1a981a0b7` | match |
| active strict-open statement | `44d43747e47b07c141e1dfbe3932cca29ef24ea0060aee0edfb7529c182f8605` | match |
| active strict-open proof | `9db508b98101b1976af1c14c963e2352aa008a7c440d94e6fe76d7e92e049ecd` | match |
| principal wrapper | `0f234329b64519f3012e5e4e3cfd31911794d9afc73c5d1abbe1de8ce165ae0d` | match |
| principal frozen PDF | `02b840eab83a42435db3428c71ee6a71c5f6e59659af470300c9da1f308a147f` | match |
| strict wrapper | `17bfb9b3cc6ac09e5b1e831457ecdf9149dce67fc9a56d1005ec72db054b6a62` | match |
| strict frozen PDF | `d96e7b1f6b76c0c77e5568a27902faa910df922b2356c2d2b219f1d5890e902a` | match |
| `SHA256SUMS` | `45aeebfbd055a79bb5eca5d20d167df1c91caa3453d375d410b222157f3b1f17` | observed |

Independent `shasum -a 256 -c SHA256SUMS` checks returned `OK` for every
listed artifact before and after the audit.

## Active dependency graph and deletion of the legacy slicing block

**PASS.**

The active mathematical chain is exactly

`endpoint theorem -> strict-core theorem -> principal v4 fibre slicing -> CLD Proposition 15.1.1(b)`.

The active strict-open statement contains only:

1. `prop:p062-arbitrary-field-annulus-v4-source-correct`, lines 6--19; and
2. `thm:p062-arbitrary-field-polycylinder-v4-source-correct`, lines 21--53.

The active strict-open proof contains only the corresponding proof blocks,
lines 7--89 and 91--202.  The former legacy label
`prop:p062-product-fibre-zero-current-candidate`, its statement, and its proof
have no occurrence in either active strict-open file.  There is likewise no
occurrence of `Corollary~15.1.2` in any active TeX dependency.

The strict polycylinder proof, lines 91--202, invokes only the principal v4
slicing proposition at lines 92--96.  Its exact range hash is
`4da2cd94de8dae6210dd616c896fd6277f592e31492abb213b732a81fabaf414`.
The resulting dependency is not circular: the principal slicing proposition
and proof are independent of both strict-open classifications, while only the
later principal endpoint theorem imports them.

## CLD local-moment direction

**PASS.**

The principal slicing proof, lines 37--47, starts with an ordinary smooth form
and invokes CLD Proposition 15.1.1(b) to produce an ordinary-open local moment
presentation.  The range hash is
`46ae9ed416d648a6cfbe1977a521902e106410f3990cd98f6e428d4bb0f57667`.

The locally materialized extraction
`dependencies/CLD25_Proposition_15_1_1_b_lines_21482_21491.txt`, SHA-256
`d2c41ff1bb5b3698e9124458932f20fa20956d70bdcae790320ad8656ddd1f7a`,
is byte-identical to lines 21482--21491 of `/private/tmp/CLD25.txt`, SHA-256
`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.
Clause (b) states precisely the direction used.  Corollary 15.1.2 is not used
to infer a moment presentation anywhere in the active chain.

## Fully open and endpoint annulus routing

**PASS.**

The principal endpoint proof, lines 276--284, makes a disjoint four-way split:

- `r < |S| < R` uses only
  `prop:p062-arbitrary-field-annulus-v4-source-correct`;
- open--closed, closed--open, and closed--closed use only
  `prop:p062-annulus-endpoint-arbitrary-field`.

The strict-core theorem at lines 295--302 similarly uses only the
source-correct strict-open polycylinder theorem.  The combined routing range
has SHA-256
`a53a0457fd144ae03bdf238fadcf23e8abaa5eef26bc9b21191478762219d028`.

The endpoint statement, SHA-256
`a54723f040926d5a309494bb77d3c734c1c9d27bfb9fd18c56fc70ea4d03c9e1`,
lists exactly the three endpoint patterns.  Its proof and production response
hashes are
`461afad5804a3269cb385550af6f4abcb5543d4f3151db56f986490c74e6947e`
and
`6b5aa2445bbd8b1dbe594fc23571c979d64eb5dc839f038101ce97b93181cee4`.
The receipt records verdict `correct`, zero critical errors, and zero gaps for
that exact scope.

The active fully open annulus proof is the previously verified mathematical
block with only labels adjusted to the new source-correct namespace.  Its
lines 7--89 have range SHA-256
`5ac61c2e1f7aa7331646f5c7c085a371e69fddc387618bfeca371565fffd77d6`.
It does not import the deleted slicing proposition.

## Rational-centred, descent, finite trace, and disc dependencies

**PASS.**

The materialized rational-centred/descent statement and proof have SHA-256
values

- `7510083fecda2d561c4ce2a1b35d08377268ef48adda2b242172428dbd39caec`;
- `77a013d4e655d288d8803c9650df5446bed570de2644591edddfc116c323eab2`.

They are byte-identical to the frozen release-candidate originals.  The copied
production response has SHA-256
`112168020192b4dffb65d309898992528dac0c8bdf8ba3aeddfe3bb245597c41`
and verdict `correct`, with zero errors, gaps, and reference issues.

The materialized finite-flat trace/disc statement and proof have SHA-256
values

- `67a8d8a21e23cb34cf9b8f6685efbf2c9eaa6ff484b3696cbc1867a8940e095c`;
- `479643ee3aa534bbfc98adcf69837356d3cd8eff22d92accd1319aabb049553e`.

They are byte-identical to the production materialization and curve-candidate
originals.  The dependency-closed response has SHA-256
`1459e3e5b05666c9537491e945b96b159df4448c502a9c4c930bdd9a204d11ea`
and verdict `correct`, with zero critical errors and gaps.

The strict annulus proof uses these dependencies in their verified directions:
rational-centred split-torus calculation, finite-flat continuous trace, and
open-disc constancy.  The polynomial tube, singleton full-degree Gauss fibre,
inseparable multiplicity, and rigid-density passage are the same verified
mathematical steps; no endpoint conclusion is imported into the fully open
proof.

## Fibre slicing, ordinary neighbourhoods, and current restriction

**PASS.**

- Principal proof lines 14--20 choose a strict affinoid neighbourhood with the
  point in its relative interior and then an ordinary open neighbourhood with
  compact closure in that interior.
- Lines 27--35 place all later supports in the ordinary relative interior of
  the product domain.
- Lines 37--89 construct an exact smooth ambient spread of every compactly
  supported fibre test, using the correct CLD moment direction, equality of
  fibre/ambient completed residue fields, density, ultrametric equality, and a
  finite smooth partition.
- Lines 90--95 extend by zero only after compact support is contained in an
  ordinary relative interior.  No arbitrary current is pulled back through an
  affinoid boundary.
- Lines 97--152 insert a compact cutoff before smooth approximation and justify
  both sides of the continuous-multiplier Fubini limit.
- Lines 154--178 pair the original current only with a legitimate global
  compactly supported smooth test form.  The bidegree calculation includes
  base dimension zero.

Thus the principal slicing proposition supplies exactly the restriction used
by the active strict polycylinder proof, for arbitrary (including nonrigid)
base points.

## Endpoint combinations, finite scalar extension, and dimension zero

**PASS.**

- The principal statement allows nonnegative `p,q` and fixes empty product and
  empty sum conventions.
- Proof lines 181--183 dispose of `p=q=0` before choosing a factor.
- Lines 185--217 construct the coordinatewise interior `Q`, prove
  `Q subset Int(P)`, and prove density via rigid points.
- Lines 219--232 explicitly identify an empty complementary product with
  `M(K)`; slicing therefore includes a zero-dimensional base.
- Lines 234--263 use only finite residue-field extensions when identifying the
  scalar extension of a factor interior with the absolute interior of the
  scalar-extended factor.  No arbitrary complete-extension equality is
  claimed.
- Lines 265--284 apply the disc, fully open annulus, and three endpoint
  classifications with the exact routing audited above.
- Lines 304--349 induct on every included endpoint coordinate.  The disc zero
  section and two finite-extension interior annulus radii reduce the induction
  count, including all mixtures of open, closed, and half-closed factors.
- Lines 351--358 use rigid density and continuity and prove uniqueness for both
  `q=0` and `q>0`.

The active strict-open theorem itself also handles empty factors: if `q=0`,
disc-fibre constancy gives the result (and `p=q=0` is the one-point product);
if `p=0`, the test factor is explicitly set to `gamma=1` with integral one.

No counterexample or missing endpoint/dimension-zero case was found.

## V3-to-v4 exact comparison

After replacing version labels by a common placeholder, the principal
statements are byte-identical.  The normalized principal proof differs only
by routing the fully open annulus and strict core from the old dependency
labels to the source-correct v4 labels and by accurately calling those new
bytes quarantined rather than production-verified.

The active strict-open statement deletes the old fibre-slicing proposition
entirely.  The active strict-open proof deletes its old proof entirely and
changes the strict polycylinder proof's sole slicing call to the principal v4
proposition.  No other mathematical scope is enlarged.

## Independent compilation and visual audit

All required sources and dependencies were copied without editing to
`/private/tmp/p062_v4_audit.M32JmM/`.  Both wrappers were compiled there with

`latexmk -pdf -interaction=nonstopmode -halt-on-error`.

Results:

| Wrapper | Pages | Independent PDF SHA-256 | Errors/undefined refs |
|---|---:|---|---:|
| principal | 8 A4 | `2df94308cada0ee3b236a974f7f3ad560dda03ca99e9ea249067f3f554adf1c8` | 0 |
| active strict dependency | 7 A4 | `45f7c91c38f914a799f6a2169df842486e5bac64ea236a59322b1933b0807cec` | 0 |

The final principal log contains one nonfatal `Underfull hbox` in the
dependency-placeholder paragraph.  The final strict log contains two
nonfatal `Underfull hbox` diagnostics in justified dependency statement text.
There are no overfull boxes, undefined references/citations, multiply-defined
labels, fatal errors, or package errors.

All fifteen pages were rendered at 110 dpi and inspected.  The underfull
paragraphs cause only loose word spacing in audit-only wrapper text.  All
theorem statements, proofs, equations, citations, margins, page breaks, and
bibliographies remain legible, with no clipping, collision, missing glyph,
black rectangle, or broken reference.  The three diagnostics are therefore
recorded but are not a mathematical, source, or compile-failure gate.

## Non-actions and scope

No frozen dossier file and no live-book file was edited.  No production or
research verification service was called.  This report is the only persistent
audit artifact created.

The verdict is limited to the stated standard strict factors and the exact
source/dependency chain.  It does not assert a result for non-strict radii,
arbitrary analytic germs, or arbitrary complete scalar extensions in the
endpoint-interior identity.
