# Production receipt — 30 August 2026

The live manuscript imports the exact frozen files submitted to production:

- statement: `p081_curve_local_global_statement_20260830.tex`, SHA-256
  `1f2c51f101fd8447fbb6b65a3c0686515efaf982674efaadcaf2271079173e93`;
- proof and comparison remark:
  `p081_curve_local_global_source_aware_proof_20260830.tex`, SHA-256
  `9847a08c98a640ee7def082a73cc1b3ff116980f2882920808557822056f0f2f`.

`HOSTILE_AUDIT.md` records the independent source-aware hostile audit. Its
SHA-256 is
`69d684ac95e6e4dd49fbb09c3585930762a95c7bca8341a863acbe1822710672`.

The exact statement and proof, with `SOURCE_MATRIX.md` and
`HOSTILE_AUDIT.md` included in the submitted dependency closure, were sent
to the production Rethlas endpoint using `gpt-5.6-sol` at `xhigh`. The
response returned `correct`, with zero critical errors and zero gaps; the
endpoint assigned no run or item identifier. The archive hashes are:

- request:
  `307ba899872bfd33720dd863bd58269820d5c0687b848760afef960cb549c7cd`;
- response:
  `7af690cea941960fc8c8bfba39acfacd6cbf0bbe8bf52273431b93945d1af0af`;
- headers:
  `c2d6c04bd79ddd90ddd7e91a6c6bbf64282d5f7cd193bb1e682ff9c89d8d69a3`.

The first two comment lines in the frozen TeX files record their staging
state before submission. They are retained so that the live mathematical
bytes remain exactly those verified in production; this receipt records
their later promotion. No novelty or priority claim is made.
