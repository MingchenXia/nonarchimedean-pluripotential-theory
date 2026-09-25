# Model-verifier receipt

Date: 25 September 2026.
Endpoint: `http://127.0.0.1:8107/verify`.
Model configuration: `gpt-6-astra`, reasoning effort `xhigh`.

The dependency-closed request prepends the exact real-polyhedral definitions,
local slope criterion and one-vertex classification from the preceding P05.2
dossier to the principal graph statement and proof.  Review checked the
refinement step, the full cone of local nonnegative-cycle inequalities, the
cutoff slope signs, compactly supported growth control, distinct outgoing
rays in the trivalent case and the stated absence of a higher-rank converse.

The first submission returned `correct`, with zero critical errors and zero
gaps.  A second submission after the proof-environment copyedit returned the
same verdict.  The proof's continuity sentence was then made explicit, and a
third request was submitted so the final archive matches the exact current
bytes.

Final exact-current response:

- server run: `20260925T191853Z_a6da387d529c`;
- verdict: `correct`;
- critical errors: `0`;
- gaps: `0`.

The final request and response SHA-256 values are respectively
`06c65634e5c5d179591dbe3e25dfc4168f75c536f5f08654ca05dcbf2deb72d7`
and
`4dcf06edf6ab3c98ae6cc1753b6d2cde3b98575603e8d8d3187e170eefec29bd`.
The principal statement and proof SHA-256 values are respectively
`aceda8926c966d3937f2f4b0e4f615f825c93248e2243efaac1fc8174572cec3`
and `8a678e9076d01f149ad55d90a098733f4a19ebcc57b034ae7e51a3c624d112d4`.
Direct comparison of the decoded request fields with the dependency-closed
materializations passes byte for byte.

All three request/response histories and safe HTTP headers are preserved.
This is a model-backed mathematical review, not formal verification, peer
review or a novelty certificate.  Its scope is the exact archived
dependency-closed statement and proof in the repaired real-piecewise-affine
category.
