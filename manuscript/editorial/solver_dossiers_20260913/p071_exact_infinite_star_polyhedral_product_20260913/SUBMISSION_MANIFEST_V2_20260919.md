# P07.1 dependency-closed verifier submission manifest, V2

Date: 19 September 2026 (Asia/Shanghai)

Status: submitted exactly as frozen and accepted by the local
`gpt-6-astra`/`xhigh` verifier; final `correct`, zero critical errors, and
zero gaps.

V2 preserves the V1 statement payload and changes exactly two proof files:
the finite ambient-star--polyhedral proof and the finite exact-star insertion
lemma.  The packet still consists of the principal statement and proof, four
prerequisite statements, and eight prerequisite proofs or lemmas.

## Ordered statement payload

1. `manuscript/editorial/rethlas_packets_20260830/p071_infinite_star_collapse_candidate_20260830/statement.tex`
   - SHA-256: `99c1a6a6a712005e73ee3b7cdae297606895b22ce79c80a6411dfd7f4863c963`
2. `manuscript/editorial/rethlas_packets_20260829/p071_infinite_endpoint_statement_20260829.tex`
   - SHA-256: `779b1304255d6e803cf34d9e429acb085eb5cf827e54c6a30a15ba3058182d9a`
3. `manuscript/editorial/solver_dossiers_20260910/p071_finite_star_polyhedral_product_20260910/STATEMENT.tex`
   - SHA-256: `e1c0263a69764de6ac426cc6dd02049311ec732338c8256e7d9937b910485ec5`
4. `manuscript/editorial/solver_dossiers_20260830/p071_stone_polyhedral_corners_v2_20260830/statement.tex`
   - SHA-256: `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002`
5. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/STATEMENT.tex`
   - SHA-256: `9b3e2c4163f30ad26f606a06d591a064f57994b56aa7910eb012093777f3c1a1`

The four statement dependencies contain 365 lines and 15538 bytes before
separators.  The principal statement contains 114 lines and 4799 bytes.

## Ordered proof payload

1. `manuscript/editorial/rethlas_packets_20260830/p071_infinite_star_collapse_candidate_20260830/proof.tex`
   - SHA-256: `ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090`
2. `manuscript/editorial/rethlas_packets_20260829/p071_infinite_endpoint_proof_20260829.tex`
   - SHA-256: `dacaa96b68c5ddb260736d40075d229ffbe843dbe4994436c1a18428aa407f5b`
3. `manuscript/editorial/solver_dossiers_20260910/p071_finite_star_polyhedral_product_20260910/PROOF.tex`
   - SHA-256: `2a9b3ec1546e3be5434cb887c09ba4526e1ad7e12d1297425a0afa5028a8c259`
4. `manuscript/editorial/solver_dossiers_20260830/p071_stone_polyhedral_corners_v2_20260830/proof.tex`
   - SHA-256: `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb`
5. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/ENVELOPE_LEMMA.tex`
   - SHA-256: `e896124fa97501c4c22b42a853c17ce32d1c01ab8a135a294efe965edfb380f4`
6. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/TERMINAL_INSERTION_LEMMA.tex`
   - SHA-256: `a38a835544b8ffa61c9786b0d133d49d19ccc87ca9041dae490d0803900345ea`
7. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/FINITE_EXACT_STAR_INSERTION_LEMMA.tex`
   - SHA-256: `3b77eb99c7dedef140f5cd5838fca07c50875a894c4460cab02558f1e61592b0`
8. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/COUNTABLE_INSERTION_COROLLARY.tex`
   - SHA-256: `261dcc85f76050be67c0012f36f70d4cadef494e12cdd8d79285e6b5db8e1bc3`
9. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/PROOF.tex`
   - SHA-256: `0cc78aa605311e6709cbf33b0580c946b5b50cef610ffff28eb5fb7c1aae6d20`

The eight proof dependencies contain 2142 lines and 92168 bytes before
separators.  The principal proof contains 272 lines and 12215 bytes.

## V2 repair boundary

- The finite-product proof now derives the necessary slope inequalities
  from normalized junction tuples, applies the finite-dimensional
  alternative, constructs a common ambient affine minorant, and gives an
  explicit mollified maximum whose exact-coordinate region produces one
  compatible node collar.
- The insertion lemma now applies the finite-valued Jensen claim to
  `max{v,K_j}` for `K_j` decreasing to negative infinity, then passes to the
  limit in the finite atomic sum.

No statement, main proof, or other prerequisite proof changed.

## Completed run archive

The V2 run directory is
`VERIFICATION_RUN_ASTRA_V2_20260919/`.  It contains the exact
`request.json`, `response.json`, and safe `headers.json`.  The endpoint,
model, and effort were
`http://127.0.0.1:8107/verify`, `gpt-6-astra`, and `xhigh`.

Because V2 contains changed mathematical bytes, the V1 authorization does
not silently authorize this second transmission.  The exact approval gate is:

`我明确批准将修复后的 P07.1 V2 主陈述、主证明、清单中的 4 份前置陈述及 8 份前置证明或引理，发送给本地 http://127.0.0.1:8107/verify 的 gpt-6-astra/xhigh 模型验证器，并保存请求和回执。`

Immediately before transmission, all fourteen hashes were recomputed and
matched this manifest.  The final response checked item
`pi_8018ede2f3895860d6f74753` and returned `correct`, with zero critical
errors and zero gaps.  The request, response, and header SHA-256 values are

- `55b1ef2a48f52008cac7820cf81a0ac931e9688d504c311adf767b56dbb4475f`;
- `4e43d68634260430b157e261e485a133b50ca3517ddde2d8dbffd74d9c5c1da3`;
- `b2ea5d5f52042d3197d3358bf8460698df26d0d9e92842a8b9c31ed9531f93d9`.

The separate receipt records the proof and context digests.
