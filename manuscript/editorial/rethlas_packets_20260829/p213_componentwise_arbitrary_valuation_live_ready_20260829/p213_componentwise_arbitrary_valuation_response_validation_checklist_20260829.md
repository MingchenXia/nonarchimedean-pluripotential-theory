# Response-validation checklist for the revised3-bound componentwise request

Date: 29 August 2026  
Status: request dispatched; response validation pending; no live-manuscript edit

## Independently validated request

The archived request is
`p213_componentwise_arbitrary_valuation_revised3_run_20260829_8107/request.json`.
It has length 69262 bytes and SHA-256
`6920d2582649e1fcedcc3a729242e1ca02fded05502cc878a36f4e8652929365`.
Its only keys are `statement`, `proof`, and `verification_deadline_utc`; the
recorded deadline is `2026-08-29T10:40:00.538005+00:00`.

The decoded request fields have been compared byte-for-byte with the prepared
materialized files.

- `statement` is exactly 11920 bytes and has SHA-256
  `d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6`.
- `proof` is exactly 54321 bytes and has SHA-256
  `cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.
- Binary comparison against the two prepared materialized TeX files succeeds
  with no difference.

The statement blocks occur in the required order:

1. nontrivially valued normal rigid zero atom, beginning at line 1, principal
   label at line 6;
2. trivially valued Gauss--Shilov zero atom, beginning at line 42, principal
   label at line 47;
3. third-revision normal-curve core, beginning at line 79, with source-cutoff,
   Euclidean-current, and classification labels at lines 86, 124, and 148;
4. principal componentwise statement, beginning at line 164, with proposition
   label at line 172 and scope remark at line 263.

The proof blocks occur in the corresponding order, beginning at lines 1, 188,
292, and 795.  The trivial Gauss proof invokes the first zero-atom label; the
componentwise proof invokes both zero-atom labels and the revised3
classification label.  The combined request has 23 labels and no duplicate
label.

## Checklist to apply once the response archive is complete

No item below is to be treated as satisfied merely because the request was
accepted for processing.

1. **Transport.**  Confirm that `headers.json` is valid JSON, records HTTP
   status 200 and `application/json`, contains no authorization data, and that
   its content-length agrees with the archived response byte length.
2. **Archive integrity.**  Record SHA-256 and byte length for `response.json`
   and `headers.json`.  Rehash `request.json` and require the exact request hash
   above; do not validate a response against a reconstructed request.
3. **Schema.**  Parse `response.json` and require output schema version 2,
   `verification_status` equal to `final`, and a nonempty list of checked item
   identifiers.  Reject a transport-only, queued, partial, malformed, or
   deadline response.
4. **Exact proof binding.**  Require `proof_digest` to equal
   `cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.
   This is the decisive exact-byte binding.  The API normally gives no
   separate statement digest, so retain the independent decoded-statement
   comparison above as the statement binding.
5. **Verdict.**  Require top-level `verdict` equal to `correct`.
   In `verification_report`, require both `critical_errors` and `gaps` to be
   empty and the summary to report no failed or blocked item.  Require
   `repair_hints` empty and `needs_expanded_proofs` empty unless a complete,
   separately archived expansion record explains otherwise.
6. **Per-item attestation.**  Require one attestation for every checked item,
   with the same item identifier, disposition `verified`, verdict `correct`,
   and a nonempty 64-hex-character context digest.  No checked item may be
   omitted, failed, blocked, or left pending.
7. **Context and process evidence.**  Require nonempty 64-hex-character
   `context_digest` and `adaptive_context_digest`.  In the durable service
   evidence, confirm model `gpt-5.6-sol`, reasoning effort `xhigh`, completed
   final state, return code zero, no recovery-required state, and the same
   checked item and proof digest.
8. **Receipt.**  Only after Items 1--7 pass, write an exact-byte receipt that
   records all eight source hashes, the two materialized hashes, the request,
   response, and headers hashes, checked item identifier, final verdict, and
   0/0 counts.  Do not infer a run identifier if the endpoint does not supply
   one.
9. **Promotion.**  Live integration, provenance prose, and P21.3 inventory
   retirement remain prohibited unless this exact response passes every
   preceding item.  Any mismatch keeps the componentwise packet quarantined
   even though its independent mathematical audit and compile gate passed.

