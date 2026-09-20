# P07.1 trivalent double-junction obstruction: verification receipt

Date: 2026-09-20

## Accepted principal bytes

- Statement SHA-256:
  `160f5a469a9a43cc0750932b40ba36108d547791dbd0e1a55eeba3221c7315f0`.
- Proof SHA-256:
  `563f8b4992f16d95623684533cf4d126ecc74d9d0acf2a4ec527cb6b87318683`.

## Accepted local verification

- Service: local `gpt-6-astra`, reasoning effort `xhigh`.
- Endpoint: `http://127.0.0.1:8107/verify`.
- Verification status: `final`.
- Verdict: `correct`.
- Checked item: `pi_5cdbc27108d6b165871775d9`.
- Critical errors: `0`.
- Gaps: `0`.
- Proof digest:
  `563f8b4992f16d95623684533cf4d126ecc74d9d0acf2a4ec527cb6b87318683`.
- Context digest:
  `ba39118d90eb9ff83c216c932c0d8c96adffd886a6d53d0bc547641754fcd713`.
- Adaptive context digest:
  `aead4b5686f33dec01024647297701731ad33b7ff4a408d0219e01a71b84cda8`.
- Item context digest:
  `5230c965da87fdbca0732cbaff0ef97bbf772bca7720aa9179c57594d5179023`.
- Archived request SHA-256:
  `b2a8ba9f9383e9259bdeb103541f20ba888b8a441d72828b4cd158c7e271c547`.
- Archived response SHA-256:
  `1087324485a0036aa5661fb29e28b1ea5138aba8ec8d7d5f662cd7bcc82eabcc`.
- Archived safe headers SHA-256:
  `bbd28f9381f2a9ca1615fef06b066c35b5c85fc031ae8c5b6dfdc9ab3f217cf4`.

The request proof digest equals the accepted principal proof digest because
the proposition is self-contained after the live book's local generator
definition and no dependency file was prepended.
The strict exact-current audit passed against the independently inspected
production verifier source.  It checks byte identity, item coverage, and
strict receipt provenance; it is not an independent proof of mathematical
truth.

## Rejected precursor retained

- Checked item: `pi_b72f1812c354b429a79086f8`.
- Verdict: `wrong`, with `0` critical errors and `1` gap.
- Request/response/safe-header SHA-256 values:
  `99b9a9a09684a16c6666ad9c371a784fcb0dfafa1902dbd707d38553b4afbfa1`,
  `3dbcd68677cdbd9827f376cc3cce47371896845dbce1ecc2f1dd4a84ac1d133f`,
  and
  `bf9c739a6ed0110c2f5a622efdadb63625ab44c4dca92f029607dadeb0145aca`.

The rejected run identified the shrinking-neighbourhood defect.  The
accepted proof replaces the invalid locality sentence by a scale-convexity
argument on one fixed star-shaped product chart.
