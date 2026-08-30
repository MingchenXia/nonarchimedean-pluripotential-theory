# Exact-live promotion receipt — 30 August 2026

The live manuscript uses the following exact files:

- statement:
  `p061_frobenius_simplicial_toric_live_statement_20260830.tex`,
  SHA-256
  `b2cdce85c771e2ccf6bbd4d0fd8ba274d521d35d3d371a5575c71b77db5aabce`;
- proof:
  `p061_frobenius_simplicial_toric_live_proof_20260830.tex`,
  SHA-256
  `e81b0f7d1156af135c75dcd15ec11b636e2d82131715cfbee0d765fd1c8900e0`.

The live files remove the temporary candidate theorem names and replace the
dependency mnemonics by live cross-references and primary citations.  They do
not enlarge the mathematical scope of the frozen candidate baseline.

`INDEPENDENT_EXACT_AUDIT.md` records an independent hostile audit of these
exact live bytes.  The audit returned PASS and specifically checked the
q-powered rational-domain descent, unit descent in both directions,
reducedness/injectivity, the non-full-cone lattice complement, the
characteristic-dependent factorization, finite affinoid base change,
two-stage scalar descent, and harmonicity.

The exact live statement and proof, together with the frozen D1/D2 inputs and
the dependency and source ledgers, were then submitted to the production
Rethlas endpoint using `gpt-5.6-sol` at `xhigh`.  The archived response
returned `correct`, with zero critical errors and zero gaps; the endpoint
assigned no run or item identifier.  The archive hashes are:

- request:
  `246d058026f2581c0e6c1b28f6231b936e697c1613b78f1fce7cbcbdd773f2b9`;
- response:
  `b4a03f9def9dbb51cdb808951afe6a1a0232a2b54e8493b8a2c37c0eeb2e4467`;
- headers:
  `f327f862ee85670ad3cdff73e3212734eb9c4e2edf391f0325f1a50489a40f26`.

The earlier candidate production response remains a frozen baseline and is
not the controlling exact-live verification.  No novelty or priority claim
is made.
