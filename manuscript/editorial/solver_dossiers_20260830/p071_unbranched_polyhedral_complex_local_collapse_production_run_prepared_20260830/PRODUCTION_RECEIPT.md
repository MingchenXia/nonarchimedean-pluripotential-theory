# P07.1 generator-convex polyhedral-complex production receipt

Date: 30 August 2026 (Asia/Shanghai)

Production status: **PASS**.  The local production Rethlas endpoint, backed by
`gpt-5.6-sol` at `xhigh` reasoning effort, returned HTTP 200 and the final
verdict `correct`.  Its verification report contains zero critical errors and
zero proof gaps.

## Frozen principal inputs

- statement: `2bc8574fecdc46ecafc1e41f24608c6db60cb9e48f696204ef503a83bed0625e`
- proof: `ab3348d8d0dc31c4c661e1358f8b70894eff83890a3c6d6abc412810dea4ca30`
- independent exact-byte reaudit:
  `1f0abda081c5ddcd0eaf9ac11a895af2e6b1b6eaace2fadebd9cb8281a4fd4e2`

The production packet is dependency-closed: it places the already verified
Stone-parameter-times-one-polyhedron theorem before the frozen principal
statement and proof.  The materialized files have hashes

- statement: `e163679c6f1140eb3452e9f052f89f8895b7b1d300e081f6149feec099d47ac7`
- proof: `1505aa473b3092f80d26bde3e8e947c709b138992370599645948ed510e39400`.

The `statement` and `proof` JSON fields in the submitted request hash to those
same two values.  Thus the verdict binds the exact dependency-closed bytes
recorded in this directory.

## Production artifacts

- request: `dd51939097d53f3c1b195388d6312c6b2c5fc15816e88e444b3e5d8ca0dd4985`
- response: `8bab39fea7dd28f75309d021731f23de1386f1801c6a8ae8362452b237b0106f`
- headers: `35f9ddd2168e155c0351c56b4bcae5b3b0d28a4922703d59413aa194280dea57`

The response summary confirms the product-model proof, common compact Stone
quotient, fixed-domain decreasing smooth convex approximation, transport to
generator-convex local developments, chart independence, the two-ray
obstruction, the edge cases, and the Chambert--Loir--Ducros specialization.

## Scope firewall

The verified conclusion applies where the complete local polyhedral-complex
germ admits a generator-preserving convex development.  It does not assert
that topological unbranching, face-to-face gluing, or cellwise positivity
alone produces such a development.  In particular, the verified two-ray
example shows why the generator-preserving hypothesis cannot simply be
deleted.  The unrestricted P07.1 atom therefore remains active.

`MATERIALIZATION_MANIFEST.json`, `PRE_SUBMISSION_AUDIT.md`, and
`request.prepared.json` remain immutable pre-submission records; their
historical fields saying that no endpoint had yet been invoked refer to the
preflight stage and are superseded by this receipt.
