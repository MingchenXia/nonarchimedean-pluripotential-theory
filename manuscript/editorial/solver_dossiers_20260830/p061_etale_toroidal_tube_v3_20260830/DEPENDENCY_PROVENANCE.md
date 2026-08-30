# Dependency provenance

## Quasi-smooth classical PH theorem

Original frozen packet:

`../../rethlas_packets_20260829/p061_quasismooth_ph_rpl_20260829/`

| artifact | SHA-256 |
|---|---|
| full statement | `0b1b4d161e3b85d342d7be88234a8ed27bfe74be4d24a639ff0456373a7a39e9` |
| full source-aware proof | `fdc6abcc4988644656892172fbdbda4178cb86ca710fd0122a90947e598b0b8b` |
| production response | `2ee6f3ed4f7242b0988ae8a79c8a574a75377e339c2c6965cf3d1b8e55ffce7e` |

The production receipt records model `gpt-5.6-sol`, reasoning effort `xhigh`,
verdict `correct`, zero critical errors, and zero gaps.

Only these exact ranges are needed here:

| role | exact range in original | range SHA-256 |
|---|---|---|
| rigid-etale descent statement | statement lines 5--17 | `5ad0a1873f43bf21ce72bc8fb4dac5a998dc4a0d305cf79d21ec0a1d6167d59f` |
| quasi-smooth theorem statement | statement lines 19--32 | `3a9c3cc22b2ca8ccc2a873afe56e4f97cc2d1ea124c6a4efbcd7b06e9b7b5c72` |
| descent proof plus theorem proof | proof lines 5--146 | `6fe55d02ef2adbd4a95d4a1eef10a3373359695bae8f237e95c270775e4d98c6` |

The local v3 file `p061_quasismooth_needed_proof_excerpt_20260830.tex` is
byte-identical to the last range.  The integral/rational-PL counterexample is
statement lines 34--49 and proof lines 148--195 of the original packet.  No
byte from either range is materialized or invoked here.

## All toric orbits

Frozen dependency:

`../p061_all_toric_orbits_20260830/`

| artifact | SHA-256 |
|---|---|
| statement | `05bda70eb1cf7ebbcc95d1831feadd946afa168f64a7298171381b9f1e865e60` |
| proof | `21c44c47a91a28469fb91a6c00569ed56d12699bae9c956c68c33ad493825b03` |
| production response | `718044118ee65e0d76b7c02b8b553552b8da974367513aa5ed4d57e8b6231f7d` |

The production receipt records verdict `correct`, zero critical errors, and
zero gaps.  This v3 packet uses its product-open-neighbourhood lemma, the
cofinal weighted toric affinoids, and the exact monoid localization at every
toric orbit.  Contrary to the stale v1 source-matrix wording, this dependency
is production verified.

## Frozen v2 preservation and audit

The sibling v2 dossier remains unchanged.  Its principal hashes are

| role | SHA-256 |
|---|---|
| v2 statement | `ad8ecd1a3f1197e9ba2234595f4f43e40099bcd5b04cfe925a53865f452b94bd` |
| v2 proof | `b18a0274e52e6f74ede7ca22e1d9d70ed68bff076f6768e15ff2b972d5c4fb96` |

The independent v2 audit has SHA-256
`d884005655ff604eea9e45d90c243f8751ed8505d92700033d90ac2ef8ae4d10`.
It found zero critical errors and exactly one proof gap: no explicit
rank-zero branch before a maximum over nonzero monoid generators.  V3
repairs only that gap and has not yet been submitted to production.

## Failed v1 preservation

The sibling v1 principal files remain unchanged:

| role | SHA-256 |
|---|---|
| v1 statement | `cdd37196a2a21fcd2cb7c7ebe96f986becd85d668d1ab21802a75001c8978f7b` |
| v1 proof | `e9f8cb3328e6a67fd33c5a9ce4cfae9258e185112e1307e159791b6c9865ca59` |

The v1 production response is retained in the sibling production-run
directory and has verdict `wrong`.  Neither v2 nor v3 rewrites that record.
