# P21.3 trivially valued special packet: live-ready byte adaptation

Date: 29 August 2026

This quarantine directory is a minimal editorial adaptation of the exact
production-verified source packet in
`../p213_trivially_valued_curve_candidate_audit_20260829/`.

The source mathematical packet has exact hashes:

- statement: `87b0ef139a035e9292bb4dcf29e5feb21a15fc28b32872c504cba191d63fca63`;
- proof: `86d694eb756748f7ba8fc6a6f2351ff85d2f2c14924c5bfd7e73d280ee99411d`.

Production item `pi_ba52efc53938ef94632be8c0` returned `correct`,
with zero critical errors and zero gaps.

The live-ready delta is intentionally limited to three editorial changes:

1. remove the opening quarantine-status comment from the statement;
2. remove the opening quarantine-status comment from the proof;
3. replace only the prose of
   `rem:p213-triv-quarantine-scope`, preserving its label, so that it records
   the production verdict and states explicitly that the packet does not
   classify arbitrary normal or nonnormal analytic curves over a trivially
   valued field.

Every lemma/proposition statement, proof paragraph, displayed formula,
equation label, theorem label, citation, and internal reference outside that
scope remark is byte-for-byte unchanged.  These adapted bytes are not yet a
live manuscript input.  They require an exact-byte re-audit and final
live-materialization Rethlas pass before integration.

Final adapted hashes:

- statement:
  `cd1032050a8ce5d3617fbf1952b411a1fe638db2f658aec9b7e0810e3b32d77b`;
- proof:
  `37ed90b0b7f079b0f34d140a79c61c510b1206da6629953696d4a2d98c8a3ee8`;
- compile harness:
  `334b0fc8a06c9afde5f40ce2a24aa86e671d583c2974cbc784200c7b6a68040e`.

The isolated harness compiled cleanly in three passes to a ten-page PDF;
the generated PDF was kept outside the repository and has SHA-256
`1677bcafdd3ca75287ead2cf721b573cc79d2950369228e772cfffd14034501e`.
