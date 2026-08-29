# P17.1 powered normalization/CLN revised6 production Rethlas receipt

Date: 29 August 2026.

## Frozen principal inputs

```text
f79967685839fe37c6b3819936f131a196b1ea75733c56ff609e5cd850c1eeff  p171_powered_archimedean_normalization_cln_revised6_production_statement_20260829.tex
d4b105483ada85492bfe803790953fe50f6fa9e4c42c656ed7776bd48ba9ce71  p171_powered_archimedean_normalization_cln_repair_revised6_20260829.tex
```

The production request prepended the already production-verified exact
weighted Philippon--Gauss dependency:

```text
0ead6bffba18801464f854e22a1d6e67a18d4590803a00e8ce002df2b1a9cf85  ch66_weighted_philippon_gauss_statement.tex
f358e6c377c9bfc16c3e9c013c12e1ac5e98855528a3da65df9c96ee01aba13d  ch66_weighted_philippon_gauss_proof.tex
```

The exact statement and proof strings extracted from the archived request
have SHA-256 values
`c58335009db0858fbabe74cfc3fdbb249ebb4059bbdaaf32e4302a49e0fb5691`
and `bfbb5f6aae7448af20ca8592fac114cb9f3e7cec54eef965d3a4d0436453bc8e`.
These are precisely the helper's documented dependency-then-principal
materializations; no other dependency was included.

## Production result

- checked item: `pi_71bc60a0e41b4b0bffe11320`;
- verdict: `correct`;
- verification status: `final`;
- checked proof items: one;
- critical errors: zero;
- gaps: zero;
- expanded-proof requests: none;
- proof digest:
  `bfbb5f6aae7448af20ca8592fac114cb9f3e7cec54eef965d3a4d0436453bc8e`.

Archive hashes:

```text
841130ad9f16bc769fa8311b137237a55a8dc80587d5ae6fe55f0f07a353b481  request.json
93b3d21c5507eacd69dbb805c156c90bc3f1ff862aca7b6c06edcce814cf2be9  response.json
90cb9b6767f46567df1eaabb7289b65125180c7079420f68d9c7121e1d6dec46  headers.json
```

## Scope decision

PASS for the powered Archimedean normalization, dimension-zero metric,
weighted endpoint dependency, restricted uniform CLN estimate, and
conditional product-net passage exactly as stated.  The final product-net
continuity remains conditional on finite-level continuity.  This receipt does
not certify the missing synchronized tensor/Deligne comparison (Module C) or
the assembled P17.1 bridge.
