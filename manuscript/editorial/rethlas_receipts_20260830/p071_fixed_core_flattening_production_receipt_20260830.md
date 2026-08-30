# P07.1 fixed-core flattening: production receipt

**Date:** 30 August 2026  
**Production run:** `20260829T234341Z_b29ccabac989`  
**Model:** `gpt-5.6-sol`  
**Reasoning effort:** `xhigh`  
**Verdict:** `correct`  
**Critical errors:** 0  
**Gaps:** 0  
**Endpoint status:** HTTP 200  
**Endpoint item identifier:** none assigned

The frozen proposition proves that a decreasing sequence of first-stage CLD
psh functions can be flattened to one decreasing sequence of smooth psh
functions when every row approximation is defined on a neighbourhood of one
common compact core.  A finite-square diagonal gives simultaneous upper
bounds against all earlier rows, and summable tail constants enforce
monotonicity without changing the pointwise limit.  The sheaf consequence is
first-stage collapse under the stated fixed-core realization property.

An independent exact-byte hostile audit passed before production submission.
The production verifier checked every diagonal choice, compactness step,
tail estimate, limit identification, and both sheaf inclusions, and matched
Chambert--Loir--Ducros Definitions 8.1.1 and 8.1.13 and Lemma 8.1.4 to the
official arXiv v2 source.

## Frozen hashes

- statement: `b29ccabac98982c239fcedcc34a701c9a9bb98ca95710d6ed7fbaa3f0f96e4d9`
- proof: `7677ba46620cc4cef8a74d502cdf9fde344e045b04bbc66a4274a5c20b1838c2`
- independent hostile audit:
  `d8481f79acca80d7de43f2b71de48f394f467ca93d641ce45bcf850949071957`
- archived request:
  `5c8f16579022985836c8e944d644c0353481b585c9bcb66bd5c823b51e232c60`
- archived response:
  `7bea0963ca2d37d22b9c93eec4ed960a7fe09e81d3a3eab1f2317eee11a68a80`
- archived safe headers:
  `38a0dc325f242a3e333ad2a9a4c2ee89035c019ad5c05787d1353575843739ad`
- service verification:
  `353ffca9d6912f54f8212dc3df46ac2cd8b8a6eb94794fbd0b2f7bb0d19781b8`
- final service log:
  `b33174c57f643a2e478209657aa0b074898094c234dd9795bdd4098e2e61603f`

The controlling service log begins with the command-line provenance
`-m gpt-5.6-sol --config model_reasoning_effort=xhigh` and records seven
sequential-statement checks, three primary-reference checks, no failed check,
and a schema-valid final verdict.

## Integration scope

Chapter 16 wraps and inputs the exact frozen statement and proof; Chapter 72
records the sharpened residual question.  The proposition does not prove
that arbitrary CLD-local row presentations admit a common compact core, nor
does it provide a uniform early ordinal without that hypothesis.  It
therefore narrows but does not retire P07.1 or P07.2.  The inventory remains
53 atoms in 14 formal problem environments.
