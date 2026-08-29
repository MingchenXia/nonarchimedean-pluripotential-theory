# P21.3 componentwise rigid-exception packet

Date: 29 August 2026

Status: **production verified; not yet a live-book input; eligible for
integration after the live-placement compile and visual checks**.

This packet combines the already verified arbitrary-field curve reductions
with the already verified normal rigid-exception theorem.  It treats
reducible and nonreduced pure curves whose reduced component normalizations
are rig-smooth away from locally finite sets of rigid points.

The proof imports exactly one separately frozen local statement:

- `lem:p21p3-componentwise-normal-rigid-zero-atom`: the curvature measure
  of a continuous CLD-psh function has no atom at an interior rigid point
  whose analytic local ring is normal, on a pure one-dimensional
  neighborhood.

That local statement has its own complete proof and has passed an independent
exact-byte hostile audit at statement hash
`469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`
and proof hash
`661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`.
It passed production Rethlas service-evidence run
`20260829T060048Z_469024d04e8e`, using `gpt-5.6-sol` at `xhigh`, with final
`correct`, zero critical errors, and zero gaps.

The current classification, nilreduction calculus, fundamental-cycle
multiplicities, local finiteness, and uniqueness do **not** depend on that
lemma.  The lemma is used only to split an equality of curvature measures
component by component at the rigid conductor/intersection locus.

## Exact verified dependencies

### Canonical-collar source-localization bridge

- labels: `lem:p21p3-gf-legal-source-localization` and
  `prop:p21p3-gf-virtual-annulus-bridge`;
- statement SHA-256:
  `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033`;
- proof SHA-256:
  `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5`;
- controlling run: `20260828T042906Z_f2a1c1b9f2a3`, together with the
  reduced consequence, final `correct`, zero critical errors, zero gaps.

This transitive dependency supplies the legal analytic moment block, proper
localized tropical pushforward, finite branch separation, canonical collars,
and exact source-preimage identity consumed by the reduced smooth-rigidity
proof.

### Arbitrary-field reduced curve packet

- labels: `lem:p21p3-gfc-rigid-zero-atom`,
  `prop:p21p3-gfc-smooth-rigidity`, and
  `prop:p21p3-curve-rigidity`;
- statement SHA-256:
  `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`;
- proof SHA-256:
  `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`;
- controlling run: `20260828T042906Z_f2a1c1b9f2a3`,
  `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical errors, zero gaps.

### Arbitrary-field nonreduced packet

- label: `prop:p21p3-curve-rigidity-nonreduced`;
- statement SHA-256:
  `e7b9889f6c063d9952d61c0472290183aac07b58c8d0569cfebc5e9ea73f1a9c`;
- proof SHA-256:
  `25fe49a46b1c5cd62b0d1a5024095b47cdd49c66f594d1d86eec4f9f270c83ec`;
- controlling run: `20260828T051601Z_db92555a72e1`,
  `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical errors, zero gaps.

The new proof re-establishes the nilreduction and multiplicity steps because
the old proposition had the stronger rig-smooth-normalization hypothesis;
it does not invoke an item of that proposition outside its hypotheses.

### Normal rigid-exception packet

- label: `prop:p21p3-rigid-exception-extension`;
- statement SHA-256:
  `cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5`;
- proof SHA-256:
  `cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce`;
- controlling run: `20260829T021315Z_cc0c48725114`,
  `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical errors, zero gaps.

This dependency is applied only after removing the conductor preimage from
one normal component.  The packet verifies directly that the resulting
open curve is nonempty, connected, strict, normal, and boundaryless, and
that its remaining exceptional locus is locally finite and rigid.

### Local normal rigid-point zero-atom packet

- label: `lem:p21p3-componentwise-normal-rigid-zero-atom`;
- statement SHA-256:
  `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`;
- proof SHA-256:
  `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`;
- independent exact-byte audit: final `PASS`;
- production Rethlas: service-evidence run
  `20260829T060048Z_469024d04e8e`, item
  `pi_0d4235a44db2b33950f8dd55`, final `correct`, zero critical errors,
  zero gaps.

## Files

- `p213_componentwise_rigid_exceptions_statement_20260829.tex`: the combined
  proposition and residual-scope remark;
- `p213_componentwise_rigid_exceptions_proof_20260829.tex`: full
  source-aware proof of the proposition using the separately frozen lemma;
- `p213_componentwise_rigid_exceptions_source_and_hostile_audit_20260829.md`:
  dependency, source, and boundary-case audit;
- `p213_componentwise_rigid_exceptions_independent_audit_20260829.md` and
  `p213_componentwise_rigid_exceptions_second_independent_audit_20260829.md`:
  the two independent exact-byte `PASS` reports, including the repaired
  transitive-dependency audit;
- `p213_componentwise_rigid_exceptions_problem_20260829.md`: verification
  objective and promotion gate;
- `p213_componentwise_rigid_exceptions_compile_20260829.tex`: standalone
  compile harness;
- `p213_componentwise_rigid_exceptions_dependencies_20260829.sha256`:
  machine-checkable exact dependency ledger;
- `p213_componentwise_rigid_exceptions_rethlas_receipt_20260829.md`:
  controlling production receipt, exact materialized hashes, and archived
  service-evidence hashes;
- `p213_componentwise_rigid_exceptions_run_20260829/`: controlling request,
  response, safe headers, and service evidence for run
  `20260829T061505Z_2bf673687e93`;
- `p213_componentwise_rigid_exceptions_missing_bridge_rejection_20260829.md`
  and `p213_componentwise_rigid_exceptions_rejected_missing_bridge_20260829/`:
  permanent diagnosis and transport evidence for the noncontrolling rejected
  materialization;
- `p213_componentwise_rigid_exceptions_manifest_20260829.sha256`: generated
  artifact ledger.

## Noncontrolling rejected materialization

The first combined production materialization omitted the transitive
canonical-collar bridge.  Rethlas therefore returned final `wrong`, one
critical error, and zero gaps, correctly refusing to treat the imported
smooth-rigidity proof as supported.  The candidate theorem bytes were not
changed.  The response and a precise diagnosis are preserved in
`p213_componentwise_rigid_exceptions_rejected_missing_bridge_20260829/` and
`p213_componentwise_rigid_exceptions_missing_bridge_rejection_20260829.md`.
The repaired production submission prepended the exact bridge before the
reduced theorem.  Service-evidence run
`20260829T061505Z_2bf673687e93`, item
`pi_ee24d64b88f0c4e60ad1acbd`, returned final `correct`, zero critical
errors, and zero gaps with `gpt-5.6-sol` at `xhigh`.  Its materialized
statement and proof hashes are
`2bf673687e935bcdae91550158344647cb1ca1cd4ae0a5040109aeb5fb2f3cbc`
and
`a27c40fbb1328b008acab07b871f50a778c34bab2b0f1d05e3a6d9d229839716`.
This is the controlling result.

## Residual narrowing certified by this packet

Within the good, separated, strict, boundaryless ambient class of P21.3,
the one-dimensional residual consists only of a trivially valued
ground field and component normalizations whose non-rig-smooth locus is not
contained in a locally finite set of rigid points.  Reducibility,
nonreducedness, and generic multiplicities are no longer residual.
Analytic dimension at least two and the literal discontinuous-potential
predicate of CLD Definition 8.6.2 remain untouched.

Both the local lemma and the exact combined statement/proof have now passed
their independent hostile audits and exact-byte production Rethlas gates.
The theorem may be promoted only by importing the frozen candidate files
unchanged and then completing the intended live-placement compile and visual
checks.  The earlier missing-bridge rejection remains part of the permanent
record and is not superseded as transport history.
