# P07.1 gpt-6-astra/xhigh verification receipt, V1

Date: 19 September 2026 (Asia/Shanghai)

Status: final `wrong`; rejected and not eligible for integration.

## Run identity

- endpoint: `http://127.0.0.1:8107/verify`;
- model: `gpt-6-astra`;
- reasoning effort: `xhigh`;
- HTTP status: `200`;
- checked item: `pi_3ebdccaf1caa460632a30f44`;
- proof digest:
  `087f90ea03db1ab7b66072a367c2b6428a68c1c1714c89c8d2d198731f9466aa`;
- context digest:
  `cf23e07e115951d0a31191eb0f187b6d7934fd23c57577acf92ecc0cffcc0825`.

The final report contains zero critical errors and two proof gaps.

## Archived bytes

- `VERIFICATION_RUN_ASTRA_20260913/request.json`:
  `62bcc0d8cc86db2229c8c76090eb9e70683584469b10dd4e10325004cc0f6c52`;
- `VERIFICATION_RUN_ASTRA_20260913/response.json`:
  `ef2775ac863a566e8bd07230025959c46dd3a18137127ccd41c9607ae84c2fc8`;
- `VERIFICATION_RUN_ASTRA_20260913/headers.json`:
  `ba674bb0dcedf426404d7a05e38dcd089fbe3f2ebc6aa93b3c0e12035a9cb68f`.

## Reported gaps

1. In the finite ambient-star product proof, the construction following
   `(spadesuit_6)` imported the common-affine-minorant and smooth
   regularized-maximum argument from a theorem whose proof was absent from
   the packet.  The fixed smaller substar and compatible node collars were
   therefore unsupported inside the transmitted dependency closure.
2. In the finite exact-star insertion lemma, Jensen's inequality for one
   truncation `max{v,K}` did not by itself imply the extended-real claim.
   The proof omitted a decreasing sequence of truncations and passage to the
   limit through the finite atomic sum.

## Disposition

No V1 theorem or lemma was promoted on the strength of this verdict.  The
first gap has been repaired by a self-contained Farkas/separation argument,
an explicit common ambient affine minorant, and a mollified regularized
maximum with a common node collar.  The second has been repaired using
`K_j` decreasing to negative infinity and termwise convergence on the finite
support.  Those changed bytes belong to V2 and require a separate verdict.
