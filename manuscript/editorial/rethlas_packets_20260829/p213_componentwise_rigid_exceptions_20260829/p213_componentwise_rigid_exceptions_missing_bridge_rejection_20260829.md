# Rejected dependency-closure submission: P21.3 componentwise theorem

Date: 29 August 2026

This is a noncontrolling failed production attempt and must remain archived.
The exact candidate statement and proof themselves were unchanged:

- candidate statement SHA-256: `5b03b18f255625809a863c1079e9d84df146cb06a8c3b752ce08c58c700aeca8`;
- candidate proof SHA-256: `3893a89ffd59f7636a7ab160c4746fecd520b328281ac60f0bbd0401dd2d21e5`.

The first materialization prepended the reduced curve theorem, the normal
rigid-exception theorem, and the local normal zero-atom lemma, but omitted the
canonical-collar bridge on which the reduced theorem transitively depends.
Its materialized hashes were:

- statement: `9e819244c341dab4fec3cbab94c7af05494accb4cb16bb961823850d88e88a4a`;
- proof: `8ab5ea0344357961cd945f3c1b77e8d2004d6ff4a4f292d291e046054d9c72c1`.

Production Rethlas returned final `wrong`, one critical error, and zero gaps.
The error was that
`lem:p21p3-gf-legal-source-localization` and
`prop:p21p3-gf-virtual-annulus-bridge` were essential undeclared premises for
the imported smooth-rigidity proof.  The verifier requested their exact
statements or internal proofs before rechecking that dependency and all
downstream conclusions.

No live integration is allowed from this attempt.  The repair is to prepend
the already production-verified exact bridge statement and proof, hashes
`f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033`
and
`ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5`,
and then rerun the complete exact dependency closure.  The candidate theorem
bytes are not altered merely to conceal a missing transitive dependency.
