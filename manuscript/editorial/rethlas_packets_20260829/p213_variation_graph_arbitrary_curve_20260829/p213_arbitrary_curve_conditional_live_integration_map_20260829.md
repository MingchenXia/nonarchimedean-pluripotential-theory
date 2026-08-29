# Conditional live-integration map: arbitrary-valued curve currents

Date: 29 August 2026  
Status: read-only plan.  No live manuscript, ledger, inventory, or receipt file
was changed while preparing this map.  The exact revised3 normal-curve packet
has now received production verdict `correct`, with zero critical errors and
zero mathematical gaps.  Every live action below remains conditional on the
dependency-closed componentwise packet receiving the same final verdict.  A
conditional or failed componentwise verdict authorizes none of the edits
below.

## Frozen inputs and ancillary dependency

### Revised3 normal-curve packet

- statement:
  `editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_statement_revised3_20260829.tex`,
  SHA-256
  `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`;
- proof:
  `editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_proof_revised3_20260829.tex`,
  SHA-256
  `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`;
- independent exact-byte hostile audit:
  `p213_variation_graph_arbitrary_curve_independent_hostile_audit_revised3_20260829.md`,
  SHA-256
  `534154de06a9c7c63d5a060c4feac5d47a274af168177a305f64972483134c41`,
  verdict PASS, zero critical errors and zero gaps.
- controlling production receipt:
  `p213_variation_graph_arbitrary_curve_revised3_rethlas_receipt_20260829.md`,
  SHA-256
  `5e3c0e39ce7c7cd520291fe7dc7b1c00760a9b5aa5369779e8488e5cdfe3a101`;
  item `pi_d9543424f0492e1412e0d203`, final `correct`, zero critical
  errors and zero gaps, with proof digest equal to the exact proof hash;
- independent receipt audit:
  `p213_variation_graph_arbitrary_curve_revised3_receipt_independent_audit_20260829.md`,
  SHA-256
  `b64027038ac00cdce475702e8e66ffb5d69b2117ce22a4dfa525d53c011606c4`,
  verdict PASS.

### Conditional-PASS componentwise packet

- statement:
  `editorial/rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_statement_live_ready_20260829.tex`,
  SHA-256
  `91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0`;
- proof:
  `editorial/rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_proof_live_ready_20260829.tex`,
  SHA-256
  `098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1`;
- conditional hostile/source audit:
  `p213_componentwise_arbitrary_valuation_hostile_source_audit_live_ready_20260829.md`,
  SHA-256
  `b5808833e90a41c39fbcc3ea2d864e489e202f6ca7580eec5791b4f2ae35dce6`.

That conditional audit predates the final revised3 proof.  It checks the
componentwise reduction intrinsically, but its obsolete dependency hashes are
not a promotion receipt.  The controlling componentwise gate must materialize
and verify the exact revised3 bytes above together with the following two
zero-atom dependencies and the exact componentwise bytes.

A fresh revised3-binding audit is
`p213_componentwise_arbitrary_valuation_revised3_binding_audit_20260829.md`,
SHA-256
`4a347171150e52a88223415cc8cfff1bb38baeabeb6eb0ce84be29ba5be595c7`.
It records zero intrinsic critical errors and zero intrinsic gaps, verifies
the complete eight-file label set as collision-free, and compiles the exact
revised3 dependency closure without warnings.  It is pre-gate preparation,
not a production receipt.

### Required zero-atom inputs

The nontrivially valued local lemma is already a live Chapter 16 input:

- statement SHA-256
  `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`;
- proof SHA-256
  `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`;
- label `lem:p21p3-componentwise-normal-rigid-zero-atom`.

The trivially valued Gauss--Shilov transfer is production verified but is not
yet a live Chapter 16 input:

- statement:
  `editorial/rethlas_packets_20260829/p213_trivial_gauss_rigid_zero_atom_20260829/p213_trivial_gauss_rigid_zero_atom_statement_20260829.tex`,
  SHA-256
  `ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a`;
- proof:
  `editorial/rethlas_packets_20260829/p213_trivial_gauss_rigid_zero_atom_20260829/p213_trivial_gauss_rigid_zero_atom_proof_20260829.tex`,
  SHA-256
  `789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66`;
- controlling item `pi_b63296e1cb8309bd0f35d29f`, final `correct`,
  zero critical errors and zero gaps;
- receipt SHA-256
  `76a153f49a8b53af9e7c4cae418fe31345ca920594125957cc53424bf349255d`;
- label `lem:p213-trivial-gauss-rigid-zero-atom`.

For the componentwise production request, materialize dependencies in this
order on the statement side and in the same order on the proof side:

1. nontrivially valued normal rigid-point zero atom;
2. trivially valued Gauss--Shilov rigid-point zero atom;
3. revised3 arbitrary-valued normal-curve packet;
4. componentwise arbitrary-valuation packet.

Using the production helper's exact materialization rule, the prepared
revised3-bound files have hashes

- materialized statement:
  `d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6`;
- materialized proof:
  `cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.

The dependency-closed harness has SHA-256
`34f230b9369d4adb337a51984500a4ebe98331fea2387bae5aae11093266b271`
and compiled cleanly to a 24-page PDF with SHA-256
`9ef38e568d572dea9fffac0ae326e9e88646128017285a223b052a617b89fcb3`.
The production request must materialize exactly these two digests; if it does
not, stop and diagnose rather than treating the local hashes as controlling.

The exact production request has now been dispatched and archived as
`p213_componentwise_arbitrary_valuation_revised3_run_20260829_8107/request.json`,
SHA-256
`6920d2582649e1fcedcc3a729242e1ca02fded05502cc878a36f4e8652929365`.
Its decoded statement and proof fields are byte-identical to the two
materialized hashes above.  This confirms request binding only; response
validation and promotion remain pending.

## Baseline for line anchors

The anchors below refer to the following read-only snapshot:

- `manuscript/parts/part2/ch16_bedford_taylor.tex`, SHA-256
  `d4e5fb3b6b76029853b583cd534e57eff878b2cfddf79277d99d0d6385702fa4`;
- `manuscript/parts/part6/ch72_major_open_problems.tex`, SHA-256
  `3fc0c858ad4f9e6f51445be298c236a7a90057f8965dee30540c8cf248a1b6ef`;
- `manuscript/editorial/rethlas_verified_results.md`, SHA-256
  `113d8e6a1fb24ad50f84a3b8ad0061482531d9c6ba8a5123d90a74fbf8145d72`;
- `manuscript/editorial/open_problem_atomic_inventory_20260824.md`, SHA-256
  `f5a3ae064d15b0155210c2f7ab7f538697d00578851f71b753f6d7f07c5490d8`.

If any baseline hash changes before promotion, re-resolve the textual anchors;
do not apply stale line numbers mechanically.

## Chapter 16 insertion map

### 1. Replace the dimension-one overview

In `ch16_bedford_taylor.tex`, replace the overview at current lines
1212--1259, retaining the notation paragraph at lines 1261--1264.  The new
overview should state, in this order:

1. On a connected good separated normal boundaryless pure analytic curve over
   any complete non-Archimedean field, possibly trivially valued, every
   positive closed ordinary `(0,0)` CLD current is `c delta_Y`.  No strictness
   or smoothness hypothesis occurs in this normal case, and the conclusion is
   the full CLD Bedford--Taylor predicate because integration currents have it.
2. On a good separated **strict** boundaryless pure analytic curve, possibly
   reducible and nonreduced and over either kind of valuation, every positive
   closed ordinary `(0,0)` current is a unique locally finite nonnegative sum
   of the integration currents of the normalizations of the reduced
   irreducible components.  The generic multiplicities remain in `delta_X`,
   and continuous-pair curvature equality is invariant under reduction.
3. The canonical-collar/rig-smooth chain printed first below is retained as
   the chronology of the earlier nontrivially valued proof and because its
   exact collars and examples remain useful.  The later variation-graph proof
   is logically independent of that chain: it uses a compact source cutoff,
   the actual analytic calibration coefficient, refinement-invariant ratios,
   residual Riemann--Roch, and graph propagation.
4. The direct trivially valued packet remains for its explicit infinite-star
   models, the two CLD interval structures, the abstract weighted-cross
   counterexample, and the four-punctured no-go calculation.  Its projective
   and algebraic curve classifications are now special cases of the general
   normal theorem, but their direct proofs remain pedagogically useful.

Do not repeat the deleted revised2 smooth-locus dichotomy or its example.

### 2. Keep the existing nontrivial zero-atom input in dependency order

The present statement/proof inputs at current lines 1296--1297 already define
`lem:p21p3-componentwise-normal-rigid-zero-atom`.  Do not duplicate or move
them.  They occur before the insertion block below and therefore begin the
dependency-readable order.

### 3. Insert the two new packets

After the existing nodal/double-thickening example input at current line 1309
and before `\subsubsection{Direct trivially valued cases}` at current line
1311, insert a short unnumbered transition explaining that the preceding
results and example are the earlier rig-smooth chronology and that the
following packets give the controlling arbitrary-valued endpoint.  Then
input, in this exact order,

```tex
\input{editorial/rethlas_packets_20260829/p213_trivial_gauss_rigid_zero_atom_20260829/p213_trivial_gauss_rigid_zero_atom_statement_20260829.tex}
\input{editorial/rethlas_packets_20260829/p213_trivial_gauss_rigid_zero_atom_20260829/p213_trivial_gauss_rigid_zero_atom_proof_20260829.tex}

\input{editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_statement_revised3_20260829.tex}
\begingroup
\emergencystretch=2em
\input{editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_proof_revised3_20260829.tex}
\endgroup

\input{editorial/rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_statement_live_ready_20260829.tex}
\begingroup
\emergencystretch=2em
\input{editorial/rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_proof_live_ready_20260829.tex}
\endgroup
```

Introduce the first two inputs by saying that scalar extension to
`K((varpi))` supplies the trivially valued local estimate, including imperfect
and inseparable residue extensions.  Together with the already printed
nontrivial lemma, this gives the same dependency order as the production
materialization.

The groups do not alter the input bytes.  The componentwise statement contains
a visible pre-promotion quarantine sentence in
`rem:p213-componentwise-av-scope`.  To preserve the production-verified source
bytes, do not edit that sentence.  Add immediately after the proof an unnamed
post-verification note saying that this historical gate sentence is retained
for byte identity and is discharged by the production receipts recorded in
the source notes.

### 4. Reframe the direct trivially valued subsection

At current lines 1314--1325, replace the introductory paragraph by one that
calls the direct package an independent calculation and example bank, not the
controlling classification.  Preserve the exact inputs at current lines
1327--1331.  State explicitly that:

- the interval and abstract-cross results are not consequences of the normal
  analytic-curve theorem;
- the projective-line and smooth algebraic-curve classifications are now
  corollaries, but their direct proofs display the infinite-star finite-moment
  mechanism;
- the four-punctured no-go statement remains the concrete explanation for why
  coarse balancing is insufficient.

### 5. Update the Chapter 16 source notes

At current lines 4104--4209, keep every earlier successful and rejected run as
chronology but reorganize the prose into three layers.

1. **Earlier nontrivial/rig-smooth route.**  Keep the existing hashes and
   receipts for
   `lem:p21p3-gf-legal-source-localization`,
   `prop:p21p3-gf-virtual-annulus-bridge`,
   `prop:p21p3-gfc-smooth-rigidity`,
   `prop:p21p3-curve-rigidity`,
   `prop:p21p3-rigid-exception-extension`,
   `prop:p21p3-curve-rigidity-nonreduced`, and
   `prop:p21p3-componentwise-rigid-exceptions`.  Mark their classification
   scopes as superseded by the new packets, while retaining the collar
   constructions, local zero-atom lemmas, and examples as independent tools.
2. **Controlling arbitrary-valued route.**  Add the exact revised3 hashes,
   independent-audit hash, actual production run/item/digests, and its zero/zero
   verdict.  Preserve the first-revision production rejection and revised2
   auxiliary-gap audit as noncontrolling provenance.  Explain in one sentence
   that revised3 uses actual calibration coefficients rather than identifying
   them with slope gcds, and deletes the unrelated unproved smooth-locus
   dichotomy.
3. **Componentwise endpoint.**  Add the componentwise source hashes, all three
   dependency pairs, the actual materialized hashes, production run/item,
   response proof digest, and zero/zero verdict.  State that the theorem covers
   every good separated strict boundaryless pure analytic curve over an
   arbitrary complete non-Archimedean field, with no reducedness or
   normalization-smoothness assumption.  Its Bedford--Taylor conclusion is for
   continuous psh pairs.  The literal discontinuous-potential predicate remains
   a scope boundary for the componentwise theorem.

At current lines 4239--4259, update the “What is new here, and what is not”
paragraph so that the new controlling labels appear first and the older chain
is described as dated, book-level antecedent work.  Continue to make no novelty
or priority claim.

## Exact label manifest

No label below occurs in the current live `manuscript/parts` snapshot, so the
planned inputs have no live-label collision.

### Revised3 normal-curve packet

Public statement labels:

- `lem:p213-variation-graph-source-cutoff`;
- `eq:p213-source-cutoff-pushforward`;
- `lem:p213-euclidean-one-dimensional-current-revised`;
- `eq:p213-euclidean-edge-decomposition-revised`;
- `eq:p213-euclidean-vertex-balance-revised`;
- `prop:p213-normal-curve-arbitrary-valuation-current-revised`;
- `eq:p213-normal-curve-arbitrary-classification-revised`.

Proof labels:

- `eq:p213-normalized-versus-metric-slope`;
- `eq:p213-normalized-node-relation`;
- `eq:p213-variation-first-order-block-revised`;
- `eq:p213-variation-collision-killer-revised`;
- `eq:p213-variation-normal-local-field-revised`;
- `eq:p213-variation-integral-branch-weight`;
- `eq:p213-variation-residual-normalized-slope`;
- `eq:p213-integral-slope-vector`;
- `eq:p213-primitive-integral-tangent`;
- `eq:p213-cutoff-differential`;
- `eq:p213-euclidean-column-divergence-revised`;
- `eq:p213-euclidean-vertex-distribution-revised`;
- `eq:p213-actual-calibration-coefficient-revised`;
- `eq:p213-intrinsic-branch-ratio-revised`;
- `eq:p213-refinement-expansion-revised`;
- `eq:p213-refinement-both-currents-revised`;
- `eq:p213-divisor-functionals-revised`;
- `eq:p213-T-principal-zero-revised`;
- `eq:p213-Y-principal-zero-revised`;
- `eq:p213-rr-positive-constant-revised`;
- `eq:p213-local-current-equality-revised`.

### Componentwise packet

Public statement labels:

- `prop:p213-componentwise-arbitrary-valuation`;
- `itm:p213-componentwise-av:calculus`;
- `itm:p213-componentwise-av:integration`;
- `eq:p213-componentwise-av-fundamental-cycles`;
- `itm:p213-componentwise-av:classification`;
- `eq:p213-componentwise-av-classification`;
- `itm:p213-componentwise-av:bedford-taylor`;
- `eq:p213-componentwise-av-curvature-equivalence`;
- `eq:p213-componentwise-av-bt-conclusion`;
- `rem:p213-componentwise-av-scope`.

Proof labels:

- `eq:p213-componentwise-av-form-isomorphism`;
- `eq:p213-componentwise-av-test-homeomorphism`;
- `eq:p213-componentwise-av-current-isomorphism`;
- `eq:p213-componentwise-av-conductor-preimage`;
- `eq:p213-componentwise-av-normal-open`;
- `eq:p213-componentwise-av-nonzero-integration`;
- `eq:p213-componentwise-av-classification-off-Z`;
- `eq:p213-componentwise-av-measures`;
- `eq:p213-componentwise-av-function-current-X`;
- `eq:p213-componentwise-av-function-current-red`;
- `eq:p213-componentwise-av-weighted-sum`;
- `eq:p213-componentwise-av-weighted-sum-red`;
- `eq:p213-componentwise-av-unweighted-sum`;
- `eq:p213-componentwise-av-support`;
- `eq:p213-componentwise-av-component-equality`.

### Trivial zero-atom dependency

- `lem:p213-trivial-gauss-rigid-zero-atom`;
- `eq:p213-trivial-gauss-rigid-zero-atom`;
- `rem:p213-trivial-gauss-rigid-zero-atom-index`;
- `eq:p213-trivial-gauss-residue-tensor`;
- `eq:p213-trivial-gauss-shilov-support`;
- `eq:p213-trivial-gauss-pushforward`;
- `eq:p213-trivial-gauss-atom-transfer`.

## Chronology and supersession table

| Earlier live result | Disposition after both gates pass |
|---|---|
| `lem:p21p3-gf-legal-source-localization` | Retain.  It is a specialized legal moment-presentation/local-properness result for strict rig-smooth curves and has content not asserted by the new cutoff lemma.  It is no longer a dependency of the controlling classification. |
| `prop:p21p3-gf-virtual-annulus-bridge` | Retain.  Its exact virtual-annular collar and exact ray-preimage statements are stronger specialized geometry; the new proof deliberately avoids needing a target-only tube. |
| `ex:p21p3-ordinary-annulus-collar`, `ex:p21p3-higher-degree-residual-branch`, `ex:p21p3-reducible-node-bt` | Retain as illustrating examples and chronology. |
| `lem:p21p3-gfc-rigid-zero-atom` | Retain as the earlier rig-smooth special case; the broader local normal lemma below is controlling where needed. |
| `lem:p21p3-componentwise-normal-rigid-zero-atom` | Retain and reuse.  It remains an essential dependency of the arbitrary-valued componentwise curvature argument when the valuation is nontrivial. |
| `prop:p21p3-gfc-smooth-rigidity` | Superseded in theorem scope by `prop:p213-normal-curve-arbitrary-valuation-current-revised`; retain only as dated chronology/corollary. |
| `prop:p21p3-rigid-exception-extension` | Superseded in theorem scope by the same normal-curve proposition; retain as chronology of the removable-rigid-exception route. |
| `prop:p21p3-curve-rigidity` | Superseded by `prop:p213-componentwise-arbitrary-valuation`; retain as the earlier reduced rig-smooth route. |
| `prop:p21p3-curve-rigidity-nonreduced` | Superseded by the new componentwise proposition, including its calculus and generic-multiplicity clauses; retain as chronology. |
| `prop:p21p3-componentwise-rigid-exceptions` | Superseded by the new componentwise proposition, which removes the valuation and non-rig-smooth-locus restrictions; retain as the immediately preceding endpoint and mark its residual-scope remark as historical. |
| `lem:p213-triv-interval-current` | Retain; it concerns CLD interval structures, not merely normal analytic curves. |
| `prop:p213-triv-abstract-cross-counterexample` | Retain; it is an abstract tropical counterexample and is not contradicted by analytic curve rigidity. |
| `prop:p213-triv-p1-current-rigidity`, `prop:p213-triv-algebraic-curve-current-rigidity` | Their conclusions are superseded as special cases of the normal theorem, but retain their direct infinite-star proofs as examples. |
| `prop:p213-triv-four-puncture-no-go` | Retain; it explains why coarse cross weights fail refined analytic balancing. |

No earlier verified bytes or rejection archives should be deleted or
overwritten.

## Chapter 72 open-problem map

In `ch72_major_open_problems.tex`:

1. Replace the current summary at lines 2290--2319 by the arbitrary-valued
   endpoint.  Cite
   `prop:p213-normal-curve-arbitrary-valuation-current-revised` and
   `prop:p213-componentwise-arbitrary-valuation`; explain that the two local
   zero-atom lemmas prevent conductor/intersection cancellation for the two
   valuation regimes.
2. In the problem environment at lines 2321--2345, keep the label
   `prob:frontier-cross-fan-upstairs` but begin with `n\geq2`.  Remove the phrase
   “outside the exact continuous-pair one-dimensional class”.  The remaining
   question is precisely the continuous-pair CLD problem in analytic dimension
   at least two, for `0\leq p\leq n-1`, under the already displayed good,
   separated, strict, boundaryless, pure-dimensional hypotheses.
3. Replace lines 2347--2356 by the statement that **no one-dimensional case
   remains inside the problem's ambient hypotheses**, over either a trivial or
   nontrivial valuation and regardless of reducibility, nilpotents, or
   normalization smoothness.  Non-good, non-separated, non-strict, and boundary
   cases remain outside the displayed problem rather than becoming hidden
   residual atoms.
4. Preserve lines 2358--2452 as historical production chronology.  Append the
   revised3 and dependency-closed componentwise production records with exact
   full hashes, run/item identifiers, response proof digests, and receipts.
   Explicitly identify the earlier rejected revised1 and auxiliary-gap revised2
   packets as noncontrolling.
5. At lines 2454--2461, keep the discontinuous-potential firewall.  State that
   P21.3 remains one T2 atom, now only in dimension at least two.  The inventory
   therefore remains 15 problem environments and 54 active atoms, with tier
   totals `0/6/14/17/17`.
6. At lines 2463--2470, keep the four-puncture warning but replace the final
   reference by `prop:p213-componentwise-arbitrary-valuation` and state that
   coarse tropical pushforward does not decide the higher-dimensional
   residual.

## Atomic inventory map

In `open_problem_atomic_inventory_20260824.md`:

1. Replace lines 423--439 so that P21.3 reads: outside the now-complete
   one-dimensional case of
   `prop:p213-componentwise-arbitrary-valuation`, determine the continuous-pair
   Bedford--Taylor property in dimension at least two or construct a
   counterexample.  Delete the two obsolete one-dimensional residuals
   (trivial valuation and non-rig-smooth normalization).
2. Preserve lines 471--543 as dated chronology.
3. Replace lines 544--549 by a controlling addendum recording the final normal
   and componentwise production receipts and saying that all one-dimensional
   cases within the ambient hypotheses are retired.  P21.3 remains one T2 atom
   only for dimension at least two; counts and tier totals do not change.

Do not delete P21.3 from the inventory, because the higher-dimensional problem
is not solved by these packets.

## Verification ledger and receipts

In `rethlas_verified_results.md`, insert two new entries after the direct
trivially valued curve entry ending at current line 993 and before the Chapter
14 entry beginning at line 995.

### Entry A: arbitrary-valued normal curves

Record:

- status `EXACT FROZEN PACKET VERIFIED / INTEGRATED BYTE-FOR-BYTE`;
- the three public labels from the revised3 statement;
- exact statement/proof hashes `339f8c...` and `d6d027...` in full;
- independent hostile-audit hash `534154...` in full;
- the actual production run, item, model, scrutiny, verdict, counts, and
  response proof digest;
- the actual receipt path;
- scope: arbitrary complete valuation, good separated normal boundaryless pure
  curve, no strictness or smoothness assumption; ordinary CLD currents; full
  Bedford--Taylor conclusion;
- noncontrolling provenance: the calibration-defective first revision and the
  revised2 auxiliary dichotomy gap remain rejected.

### Entry B: arbitrary-valued componentwise curves

Record:

- status `DEPENDENCY-CLOSED EXACT PACKET VERIFIED / INTEGRATED`;
- label `prop:p213-componentwise-arbitrary-valuation` and its four item labels;
- source statement/proof hashes `91ce52...` and `098995...` in full;
- all six exact dependency hashes (two zero-atom pairs and revised3 pair);
- actual materialized statement/proof hashes;
- actual production run/item, model, scrutiny, verdict, counts, response proof
  digest, and receipt;
- exact scope and the continuous-pair firewall;
- inventory consequence: the one-dimensional part of P21.3 is retired, but
  P21.3 remains one T2 atom in dimension at least two, so counts remain
  unchanged.

Suggested immutable receipt names are

- `manuscript/editorial/rethlas_receipts_20260829/p213_normal_curve_arbitrary_valuation_live_integration_receipt_20260829.md`;
- `manuscript/editorial/rethlas_receipts_20260829/p213_componentwise_arbitrary_valuation_live_integration_receipt_20260829.md`.

Each receipt should record pre/post live-file hashes, exact input hashes,
materialized hashes where applicable, request/response/header hashes, run and
item identifiers, proof digest, independent-audit hashes, compile result, and
the pages visually inspected.  Never manufacture a missing identifier.

The older ledger entries at current lines 477--603 and 959--993 remain as
historical verified stages.  Add a one-line “superseded in scope by the
29 August arbitrary-valued endpoint” note where needed; do not alter their
historical hashes or verdicts.

## Post-integration checks

Only after both production gates pass:

1. rehash every live input and compare it byte-for-byte with the receipts;
2. search the entire manuscript for duplicate labels and unresolved
   `\cref`/`\eqref` targets;
3. confirm that no live prose still lists trivial valuation or non-rig-smooth
   normalizations as a one-dimensional residual of P21.3;
4. confirm that P21.3 itself remains present for dimension at least two and
   that the active-atom counts remain unchanged;
5. compile the full book from a clean auxiliary state;
6. inspect every newly typeset Chapter 16 and Chapter 72 page, especially the
   long displayed slope/calibration formulas and the componentwise enumerated
   statement;
7. run an independent post-integration audit checking exact hashes, source
   scope, labels, chronology wording, and open-problem counts.

Until those checks pass, do not mark the one-dimensional residual retired in
the live inventory.
