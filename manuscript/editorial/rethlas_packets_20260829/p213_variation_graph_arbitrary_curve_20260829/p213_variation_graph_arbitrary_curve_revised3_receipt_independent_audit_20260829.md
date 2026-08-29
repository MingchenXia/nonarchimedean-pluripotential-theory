# Independent audit of the revised3 production receipt

Date: 29 August 2026  
Disposition: **PASS**, with no remaining discrepancy.

## Exact receipt and transport bytes

- receipt
  `p213_variation_graph_arbitrary_curve_revised3_rethlas_receipt_20260829.md`:
  SHA-256
  `5da9aee07589e72bf9c515097ca6542d51d5fa5b9c116932fd8bc3ea7513456d`;
- request SHA-256
  `d9a4ad02796009280917f1c0d1de216503c5fdcd25aef28c073570e26baebf1f`;
- response SHA-256
  `93c586e3de8884e30e7e7c320e6364cb2bb9c6c35d38593361e34c9a85f06860`;
- sanitized headers SHA-256
  `0f0bcd114f923264cbcfb398d5d8fc10b556eda20373330912c3ef8fe3eca217`.

These four hashes agree exactly with the receipt.  The header archive records
HTTP status 200 and contains only content length, content type, date, and
server fields.

## Request materialization

Extracting the JSON strings byte-for-byte, without adding a terminal newline,
gives

- statement SHA-256
  `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`;
- proof SHA-256
  `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`.

They are identical to the frozen revised3 theorem files and to the two hashes
printed in the receipt.  The source-audit, hostile-audit, and harness hashes
printed in the receipt also rehash exactly as

```text
2a9f76a2c264c726d1c7c1df67b414532400afc537c2a14103be919ddb41a769
534154de06a9c7c63d5a060c4feac5d47a274af168177a305f64972483134c41
eb8a19c8fcf714f32e7c818cf197efce7800a327118088f5f632fd69cac2bbea
```

## Response verification

The archived response records

- `verification_status: final`;
- `verdict: correct`;
- checked item `pi_d9543424f0492e1412e0d203`;
- proof digest
  `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`;
- verification summary: one checked proof item, no failed or blocked items;
- empty `critical_errors` and `gaps` arrays.

Thus the receipt's controlling claims are fully supported by the archived
request, response, and headers.  The proof digest is the exact frozen proof
hash, not merely a prefix or a hash of a different materialization.

## Scope wording

The receipt now repeats the exact field scope: a complete non-Archimedean
field, possibly trivially valued.  It also records the full CLD
Definition 8.6.2 Bedford--Taylor conclusion of the normal-curve proposition,
not merely its continuous-pair specialization.  Both corrections agree with
the frozen statement and require no change to the verified theorem bytes or
transport archives.

No discrepancy remains.  This audit does not authorize componentwise live
integration; that remains governed by its separate production gate.
