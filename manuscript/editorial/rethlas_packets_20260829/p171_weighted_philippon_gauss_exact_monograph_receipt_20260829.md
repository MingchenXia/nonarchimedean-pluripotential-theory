# P17.1 weighted Philippon--Gauss continuity: exact monograph-form Rethlas receipt

Date: 29 August 2026

Scope: this is the second, exact-byte verification required by the integration
gate in the 28 August 2026 blueprint receipt.  It certifies the staged
monograph-form statement and proof below.  It does not by itself certify the
relative-resultant comparison or the full answer to Pille--Schneider
Question 4.9.

Production verifier:

- endpoint: `http://127.0.0.1:8107/verify`;
- service configuration: `gpt-5.6-sol`, reasoning effort `xhigh`;
- HTTP status: `200`;
- checked proof item: `pi_0199c891f973cd6f3ffd904e`;
- disposition: `verified`;
- verdict: `correct`;
- verification status: `final`;
- critical errors: `0`;
- gaps: `0`;
- expanded proofs requested: none;
- repair hints: none.

Exact staged mathematical bytes:

- `manuscript/parts/part6/fragments/ch66_weighted_philippon_gauss_statement.tex`
  has SHA-256
  `0ead6bffba18801464f854e22a1d6e67a18d4590803a00e8ce002df2b1a9cf85`;
- `manuscript/parts/part6/fragments/ch66_weighted_philippon_gauss_proof.tex`
  has SHA-256
  `f358e6c377c9bfc16c3e9c013c12e1ac5e98855528a3da65df9c96ee01aba13d`.

The request archive was compared byte-for-byte with both staged files:
`statement_exact=true` and `proof_exact=true`.  The response's
`proof_digest` is
`f358e6c377c9bfc16c3e9c013c12e1ac5e98855528a3da65df9c96ee01aba13d`,
which independently agrees with the proof-file digest.

Exact verification archive:

- `p171_weighted_philippon_gauss_exact_monograph_run_20260829/request.json`
  has SHA-256
  `b3efd04d416d5f81f05d829e677e86c2b3db23efa2d94f4379b665c1448c80ec`;
- `p171_weighted_philippon_gauss_exact_monograph_run_20260829/response.json`
  has SHA-256
  `27c0e0f825993bbb672ca65760c1c16dc7b979c4a0d8d107881a5f3fc8e6a0cf`;
- `p171_weighted_philippon_gauss_exact_monograph_run_20260829/headers.json`
  has SHA-256
  `bbce401260464d1d90468b8de18bd1e1537bd986d39cd27f4caaf684ddb50619`.

Integration decision: the weighted Philippon--Gauss statement and proof have
passed both the archived blueprint verification and this exact monograph-form
verification.  These exact bytes may now be integrated.  Any later
mathematical change requires a new exact-byte verification.
