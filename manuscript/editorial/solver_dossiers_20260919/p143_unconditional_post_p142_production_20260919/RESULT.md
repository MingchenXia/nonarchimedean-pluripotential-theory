# P14.3 unconditional production result

The repaired exact-live request returned HTTP 200 with:

- verification status: `final`;
- verdict: `correct`;
- checked item: `pi_90c4637f53444d88823e88f3`;
- critical errors: 0;
- gaps: 0;
- item disposition: `verified`;
- final expansion round: 0;
- expanded proofs: none.

The response binds the exact target and declared context by:

| field | SHA-256 |
| --- | --- |
| target statement packet | `14856423a8aadb5db2840b824164e85ecb23bb7c243046ca5799224c5882f18f` |
| target proof packet | `a5e5ba15fe0ac81200c9d4aff3cde3e165020e560a317471f20f88704f29f926` |
| premise statement packet | `8868fc47c4216438969283c74deca06ca10347292753156d2ee8ff714081e2eb` |
| proof digest | `665daf046d5e70a33037e964ff7337096620b9d69044cbbe2f756afb552b6f5b` |
| context digest | `2f47f58a997423bf2743336db44e6384db242758c4707c96f423e421ab4adef1` |
| adaptive-context digest | `c6a2dfefb6d5bcc019ce3b397a854c1303254081c443e863ab9c00278a69a540` |
| item-context digest | `edca63df595ba1a6ec3d818ca0da0413ee77d0cc77cc127e13bed3ef21cee1e8` |
| request | `8a87fa6c3d6c9a4ae8588003e86b0083af60cec285918f3ca022685e476d1e28` |
| response | `0d7e70aa1a7d22895f93cbad0f4b7f12f2605e763df674012d3fe58224b12125` |
| headers | `84c621ea7295701ed473fe53c2743cb8ebec4748bdc57b35baf795c74cab52ac` |

The earlier `VERIFICATION_RUN_20260919/` response is preserved as the
diagnostic six-gap result.  The repaired packet removes the duplicate source
metadata, declares all named ancestors exactly, and relies on the separately
accepted P14.2 V15 result without appending a second P14.2 source family.
