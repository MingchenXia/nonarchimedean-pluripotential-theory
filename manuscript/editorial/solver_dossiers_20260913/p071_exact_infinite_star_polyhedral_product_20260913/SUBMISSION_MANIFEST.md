# P07.1 dependency-closed verifier submission manifest

Date: 13 September 2026 (Asia/Shanghai)

Status: V1 submitted on 19 September 2026 and rejected with two repairable
gaps.  This file is the immutable manifest of the transmitted V1 bytes; the
two repaired proof files no longer have the hashes recorded below.  See
`VERIFICATION_RECEIPT_ASTRA_V1_20260919.md` and
`SUBMISSION_MANIFEST_V2_20260919.md`.

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

The four statement dependencies contain 365 lines and 15538 bytes in
total before separators and the 114-line, 4799-byte principal statement.

## Ordered proof payload

1. `manuscript/editorial/rethlas_packets_20260830/p071_infinite_star_collapse_candidate_20260830/proof.tex`
   - SHA-256: `ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090`
2. `manuscript/editorial/rethlas_packets_20260829/p071_infinite_endpoint_proof_20260829.tex`
   - SHA-256: `dacaa96b68c5ddb260736d40075d229ffbe843dbe4994436c1a18428aa407f5b`
3. `manuscript/editorial/solver_dossiers_20260910/p071_finite_star_polyhedral_product_20260910/PROOF.tex`
   - SHA-256: `fa61399f763e7cb7c5daf4ae58d86ea2a6ee37295beff6322d067cd58ec80135`
4. `manuscript/editorial/solver_dossiers_20260830/p071_stone_polyhedral_corners_v2_20260830/proof.tex`
   - SHA-256: `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb`
5. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/ENVELOPE_LEMMA.tex`
   - SHA-256: `e896124fa97501c4c22b42a853c17ce32d1c01ab8a135a294efe965edfb380f4`
6. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/TERMINAL_INSERTION_LEMMA.tex`
   - SHA-256: `a38a835544b8ffa61c9786b0d133d49d19ccc87ca9041dae490d0803900345ea`
7. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/FINITE_EXACT_STAR_INSERTION_LEMMA.tex`
   - SHA-256: `2c98842839171d8ae9463e5cec202f46f0ac9020f6733298f0ff7f5f5a46f27e`
8. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/COUNTABLE_INSERTION_COROLLARY.tex`
   - SHA-256: `261dcc85f76050be67c0012f36f70d4cadef494e12cdd8d79285e6b5db8e1bc3`
9. `manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/PROOF.tex`
   - SHA-256: `0cc78aa605311e6709cbf33b0580c946b5b50cef610ffff28eb5fb7c1aae6d20`

The eight proof dependencies contain 2074 lines and 89403 bytes in total
before separators and the 272-line, 12215-byte principal proof.

## Completed V1 run archive

Directory:
`manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/VERIFICATION_RUN_ASTRA_20260913/`

The approved submission created `request.json`, `response.json`, and
`headers.json` there.  The endpoint was the locally hosted `/verify` service,
with model `gpt-6-astra`, reasoning effort `xhigh`, and a 3300-second
timeout.  The submitter archived the exact outgoing JSON before opening the
local HTTP connection.

The historical V1 submission was locked behind the exact owner sentence

`我明确批准将冻结的 P07.1 主陈述、主证明、清单中的 4 份前置陈述及 8 份前置证明或引理，发送给本地 http://127.0.0.1:8107/verify 的 gpt-6-astra/xhigh 模型验证器，并保存请求和回执。`

That sentence is present in the thread, and the V1 request was transmitted
only after all fourteen recorded hashes matched.

## Frozen command

From the repository root, after the exact gate and a successful hash
preflight, the submission command is:

```text
/Users/mingchen/Projects/Yethlas/runtime/rethlas-venv-20260828/bin/python manuscript/editorial/tools/submit_rethlas_packet.py manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/STATEMENT.tex manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/PROOF.tex manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/VERIFICATION_RUN_ASTRA_20260913/request.json manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/VERIFICATION_RUN_ASTRA_20260913/response.json manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_product_20260913/VERIFICATION_RUN_ASTRA_20260913/headers.json --statement-dependency manuscript/editorial/rethlas_packets_20260830/p071_infinite_star_collapse_candidate_20260830/statement.tex --statement-dependency manuscript/editorial/rethlas_packets_20260829/p071_infinite_endpoint_statement_20260829.tex --statement-dependency manuscript/editorial/solver_dossiers_20260910/p071_finite_star_polyhedral_product_20260910/STATEMENT.tex --statement-dependency manuscript/editorial/solver_dossiers_20260830/p071_stone_polyhedral_corners_v2_20260830/statement.tex --proof-dependency manuscript/editorial/rethlas_packets_20260830/p071_infinite_star_collapse_candidate_20260830/proof.tex --proof-dependency manuscript/editorial/rethlas_packets_20260829/p071_infinite_endpoint_proof_20260829.tex --proof-dependency manuscript/editorial/solver_dossiers_20260910/p071_finite_star_polyhedral_product_20260910/PROOF.tex --proof-dependency manuscript/editorial/solver_dossiers_20260830/p071_stone_polyhedral_corners_v2_20260830/proof.tex --proof-dependency manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/ENVELOPE_LEMMA.tex --proof-dependency manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/TERMINAL_INSERTION_LEMMA.tex --proof-dependency manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/FINITE_EXACT_STAR_INSERTION_LEMMA.tex --proof-dependency manuscript/editorial/solver_dossiers_20260913/p071_exact_infinite_star_polyhedral_feasibility_20260913/COUNTABLE_INSERTION_COROLLARY.tex --endpoint http://127.0.0.1:8107/verify --timeout-seconds 3300
```

## Historical V1 pre-send invariant

Immediately before V1 submission, all fourteen hashes above were recomputed
and matched.  The exact request, response, and safe HTTP headers are archived,
and their hashes and terminal verdict are recorded in the separate receipt.
