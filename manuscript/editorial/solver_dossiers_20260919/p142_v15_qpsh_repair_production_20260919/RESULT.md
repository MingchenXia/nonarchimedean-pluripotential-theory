# P14.2 V15 production result

The accepted retry returned HTTP 200 with:

- verification status: `final`;
- verdict: `correct`;
- checked item: `pi_4e14dc8a6a26aa190cd191b5`;
- critical errors: 0;
- gaps: 0;
- item disposition: `verified`;
- final expansion round: 0;
- expanded proofs: none.

The response binds the exact target and declared context by:

| field | SHA-256 |
| --- | --- |
| target statement packet | `c2f8fa3841704dc2dacaf8b4d8d633d8129790f74f555cef9b887f769373060b` |
| target proof packet | `01f9b53eccb4cfa80f754509ed553a55de664709376013c5e162c1f390481d55` |
| proof digest | `86de3f3687ce5160d37bcdff4315e93462dc0138939170957425aea4d9e45f7e` |
| context digest | `8f63b5ed0ca6234e59723fc1abf3b4e0cb64503540a3db5cb0fe573288e981a3` |
| adaptive-context digest | `54981f00909b54f10102efe4ec4ae01ad764a0141b382959c7af0299eb24280c` |
| item-context digest | `1820d78234365919b98b1e3eae688b00a8ea58ac5afd69c529eeb3fd89498dfd` |
| request | `c193cfc0eb461f9f63977290df9d108e188d7fe8b292b3591243f3bbece52361` |
| response | `45fc230c57ecca3616e5a326e1b77170366ec09ebbc6bbb1ba0c6b3a4330bd68` |
| headers | `19c22f4905e9bc043f8495c4f809a1dd09fc66c33b2e03ad3d130d939819ed4e` |

The earlier run under `VERIFICATION_RUN_20260919/` is preserved as the
diagnostic one-gap result.  The retry changes only the declared premise
context by adding the exact statement of
`prop:pseff-one-curve-transform`; the target statement and proof hashes are
unchanged.
