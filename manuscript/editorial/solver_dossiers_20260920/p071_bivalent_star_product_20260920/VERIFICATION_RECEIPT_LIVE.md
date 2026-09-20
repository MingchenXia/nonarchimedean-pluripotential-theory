# P07.1 bivalent-star product: verification receipt

Date: 2026-09-20

## Accepted principal bytes

- Statement SHA-256:
  `20063aa4bb331d0b48d23824867d6fcc4ba54964c8bb6d746fb181b479f2135c`.
- Proof SHA-256:
  `e3083a681f91a97b64ccb67ac7b8105a7e3ce5fce30c58eab68acfb4cac23750`.

## Accepted dependency-closed run

- Service: local `gpt-6-astra`, reasoning effort `xhigh`.
- Endpoint: `http://127.0.0.1:8107/verify`.
- Verification status: `final`.
- Verdict: `correct`.
- Checked item: `pi_48270fe4a3ce7d5ad5251d47`.
- Critical errors: `0`.
- Gaps: `0`.
- Materialized proof digest:
  `f639fa0ebf77693df568a8d56e8ad812950254b9e96ec6a37a1b8b5119aed469`.
- Context digest:
  `81420821af93a32701ac8eade9bb3d8d28901c257300327fd3bfcd2136181b52`.
- Adaptive context digest:
  `1771a00d399b7c29c86ae9d810f0f8f72ce8de788a562d68da8220afed07e21d`.
- Item context digest:
  `9403767499c2effb74f7152e31ffdb954edaa248b341e7e2332cb1238c1fec6c`.
- Archived request SHA-256:
  `ed2d037deb01efca13a60f216c6557ef3b471da1b5508578eec6ccde80f9caed`.
- Archived response SHA-256:
  `8b8aa846c23e8d815440d2d3dc8bfac9b3417ed6ce40b0081bd1e8449df9477f`.
- Archived safe headers SHA-256:
  `ede19023e1a5224b12e62aea1ac7d5693d866d681fb57916dfdd9cf3f1e8a533`.

The strict exact-current audit passed against the archived production
verifier source.  It checks byte identity, dependency coverage, and strict
receipt provenance; it is not an independent proof of mathematical truth.
