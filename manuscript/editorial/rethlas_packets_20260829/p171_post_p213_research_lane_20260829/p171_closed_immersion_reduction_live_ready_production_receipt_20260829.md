# P17.1 finite-level closed-immersion reduction: exact-live production receipt

Date: 29 August 2026

Status: **exact-live production Rethlas PASS; integrated finite-level
reduction; P17.1 remains open**.

The exact-live statement and proof were submitted to production Rethlas after
the exact-byte delta audit.  The service returned `verdict = correct`,
`verification_status = final`, one checked proof item, zero critical errors,
and zero gaps.

- checked item: `pi_9d4f5f4d6c4a36b32834c0a5`;
- statement SHA-256:
  `9be78feb5c4b76ae9f8ec7ec05d26dbaffebab602993dec7b37dcc8668819f81`;
- proof SHA-256:
  `ebb4c34fc1d06909ff2dfc7c0c0d918d1d548222b092e1b5e0472d2eecc4b603`;
- request SHA-256:
  `ea21deb37bfafed89e01f12cc4128e1df4704f2ffb353c76541862ccdf2468f3`;
- response SHA-256:
  `bdc6faf4b8b0a8185480a35531671f8a6db13444067ab7bdb86bac85c23a2435`;
- headers SHA-256:
  `937a22195d37a3cdd83901737696cf1b96c2799c420b43ce4c6474602c6544bc`.

The returned proof digest is exactly the proof hash above.  The result
eliminates the need to extend a resultant theorem from closed immersions to
arbitrary basepoint-free systems at finite level.  It does not construct or
prove continuity of a relative Chow/Deligne norm over an arbitrary Banach
spectrum, so it does not settle or retire P17.1.
