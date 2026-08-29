# Independent receipt audit: revised3-bound componentwise arbitrary-valued curves

Date: 29 August 2026  
Status: production response validated; no live-manuscript edit made by this audit

## Verdict

**PASS: exact-byte production binding confirmed, final verdict `correct`,
0 critical errors, 0 gaps, and 0 failed or blocked items.**

This is a verification and provenance receipt, not a novelty or priority
claim.  It applies only to the exact dependency-closed statement and proof
hashes below.

## Principal and dependency source bytes

The four statement/proof pairs were submitted in this order.

1. Nontrivially valued rigid-point zero atom:
   - statement
     `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`;
   - proof
     `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`.
2. Trivially valued Gauss--Shilov rigid-point zero atom:
   - statement
     `ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a`;
   - proof
     `789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66`.
3. Third-revision arbitrary-valued normal-curve core:
   - statement
     `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`;
   - proof
     `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`.
4. Principal componentwise arbitrary-valued packet:
   - statement
     `91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0`;
   - proof
     `098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1`.

All eight files were rehashed after the response arrived and still have these
exact values.

The resulting materialized files are

- statement: 11920 bytes, SHA-256
  `d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6`;
- proof: 54321 bytes, SHA-256
  `cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.

Binary comparison proves that the decoded `statement` and `proof` fields in
the archived request are exactly these two files.  Their block order is the
order displayed above.  The combined request contains 23 labels and no
duplicate label.

## Independent mathematical and compile gates

- Componentwise conditional hostile audit SHA-256:
  `35af811f8d73fadc2a484f9f90f1ef0825470ad3223eab69195ba5b9269e6fa2`;
  result 0 intrinsic critical errors and 0 intrinsic gaps.
- Revised3 normal-curve hostile audit SHA-256:
  `534154de06a9c7c63d5a060c4feac5d47a274af168177a305f64972483134c41`;
  result PASS 0/0.
- Revised3 dependency-binding audit SHA-256:
  `4a347171150e52a88223415cc8cfff1bb38baeabeb6eb0ce84be29ba5be595c7`.
- Dependency-closed compile harness SHA-256:
  `34f230b9369d4adb337a51984500a4ebe98331fea2387bae5aae11093266b271`.
- Its 24-page, 401739-byte PDF SHA-256:
  `9ef38e568d572dea9fffac0ae326e9e88646128017285a223b052a617b89fcb3`.

The final compile log has no TeX error, package warning, undefined citation,
undefined reference, duplicate label, overfull box, or underfull box.

The first two dependencies already have controlling production receipts.  The
third-revision normal-curve production receipt has SHA-256
`5da9aee07589e72bf9c515097ca6542d51d5fa5b9c116932fd8bc3ea7513456d`
and records final `correct` 0/0 on its exact statement/proof hashes.

## Exact transport archive

Archive directory:
`p213_componentwise_arbitrary_valuation_revised3_run_20260829_8107`.
The directory name is a durable local archive label, not an inferred endpoint
run identifier.

- `request.json`: 69262 bytes, SHA-256
  `6920d2582649e1fcedcc3a729242e1ca02fded05502cc878a36f4e8652929365`;
- `response.json`: 820 bytes, SHA-256
  `87507beab77d5917edc8cd8d1abcf466965222a2c973e6cded58beabd2057a8a`;
- `headers.json`: 183 bytes, SHA-256
  `0733b7bff2ffbe09bba821804d7b4bcbf50842031743a096f5db79c9dc5cdde6`.

The sanitized headers record HTTP status 200, content type
`application/json`, and content length 820, exactly equal to the archived
response length.  They contain no authorization data.

## Exact production result

The response has output schema version 2 and records

- verification status: `final`;
- verdict: `correct`;
- checked item: `pi_1ca3e6d14c7e8596372d863d`;
- proof digest:
  `cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`;
- critical errors: 0;
- gaps: 0;
- failed or blocked items: 0;
- repair hints: empty;
- expanded-proof requests: none.

The proof digest is exactly the materialized proof hash.  The checked-item
attestation names the same item, has disposition `verified`, verdict
`correct`, final round 0, and no expanded proof.  Its context digest is
`06d48a7fca592ef177dedb8f4554fe733abfa6706c6481a6aa6e404541dfabaa`.
The response-level context and adaptive-context digests are respectively

```text
c7537d1c0ab88c5916b4e15486510b10569d208bd32be2213e693e2cc5a896bb
5ae8c5dc5f6b7d45607a8223135a895d52c12c0405c31193cadab2f3a2745166
```

All three are valid 64-hex-character digests.  The response does not contain
an endpoint run identifier, and none is inferred.  This direct wrapper archive
does not contain a separate copied service-manifest bundle; accordingly this
receipt makes no independent claim about such absent files.  The exact final
response and its per-item context attestation are the controlling production
record, as in the immediately preceding revised3 normal-curve gate.

## Promotion consequence

The independent mathematical audit, dependency audit, compile gate, exact
request binding, and production response validation all pass.  The exact
source packets listed above are therefore eligible for controlled live
integration.  Integration must preserve their exact bytes and dependency
order; provenance prose must cite the materialized hashes and checked item.
Any later source mutation requires a fresh audit and production verdict.

