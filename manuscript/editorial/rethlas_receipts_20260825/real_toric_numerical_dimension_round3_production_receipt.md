# Real toric numerical dimension: round-3 production receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)
**Status:** **VERIFIED FROZEN PACKET; NOT YET INTEGRATED INTO A LIVE CHAPTER**
**Verifier:** production Rethlas at `127.0.0.1:8107`
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The exact source-aware theorem and proof returned `verification_status =
final` and `verdict = correct`. Rethlas checked one proof item, with zero
failed or blocked items, zero critical errors, zero gaps, and no request for
an expanded proof. This receipt controls only the frozen packet identified
below. A later live integration needs its own byte-identity and compilation
audit.

## Run identity and verdict

- Run: `20260825T011636Z_99edb45c54cb`.
- Proof item: `pi_9bb081dd3b5d36a64cbc59af`.
- Item title: `theorem synthetic:main`.
- Started: `2026-08-25T01:16:36.394900+00:00`.
- Item elapsed time: `879.950` seconds.
- Reported token count: `235`.
- Adaptive round: `0`; no expanded proof was requested.
- Verifier process: completed with return code `0`; output validated.
- Process-guard command SHA-256:
  `809b35656e1dd657b4e5fb46660bcd6e0d8f918a1e3cb1c0297eb24504780769`.
- The completed process and child guards both have state `completed`.
  Their earlier `blocked_release_pending` state was the server's initial
  post-`Popen`, pre-`communicate` sentinel, not a permission or approval
  request.

The item-level mathematical summary is:

> The complete proof is logically sound. The convex-analytic identification
> of the Newton body, comparison of Cao and non-pluripolar masses via gentle
> quasi-equisingular approximations, toric Monge--Ampere calculation,
> polynomial coefficient comparison, and mixed-volume dimension argument are
> justified. The cited external results match the required scopes and
> hypotheses.

## Exact submitted bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260824/real_toric_numerical_dimension_round3_statement_exact_20260825.tex` | 1398 | 33 | `99edb45c54cb8bae89f5f5dc34abc718ca965a2ac7f1d7bef1693ab4dab372fa` |
| `../rethlas_packets_20260824/real_toric_numerical_dimension_round3_source_aware_proof_exact_20260825.tex` | 15125 | 339 | `e2e16296fa3420e6a40739016a6dccabb9628e17ea2c6ec47ec890e9dfaebfad` |
| `../rethlas_packets_20260824/real_toric_numerical_dimension_round3_source_aware_request_20260825.json` | 17650 | 5 | `799eb4aaee0db33d97e208fa9859cdd099ffa4932d3f356e98ac1390f37de46d` |

The round-3 statement and proof freezes are byte-identical to the controlling
working packet files
`real_toric_numerical_dimension_statement_exact.tex` and
`real_toric_numerical_dimension_source_aware_proof_exact.tex`, respectively.
Decoding the JSON fields with `jq -j '.statement'` and `jq -j '.proof'`
reproduces the two frozen TeX files byte for byte; both `cmp` checks returned
zero. The request deadline was `2026-08-25T04:00:00+00:00`.

## Returned digests and preserved service artifacts

- Proof digest:
  `e2e16296fa3420e6a40739016a6dccabb9628e17ea2c6ec47ec890e9dfaebfad`.
- Aggregate context digest:
  `403e74073fa5632def83ed0953304dd8dc02d9f192f4996ef353d073f8fb66a9`.
- Adaptive context digest:
  `90b45288aceb61a31858534ea63407bc26d92faf7d2c8254e6267d43b4da055a`.
- Item context digest:
  `120379ca2b11d73484acc922076280676bd5e381e4baee3f9f0649e2f8f52162`.

| Preserved artifact | SHA-256 |
|---|---|
| `real_toric_numerical_dimension_round3_api_response_20260825.json` | `ad5250ac8d2b41fc62d1f16b815631c9b6bd4bd74f16ca9e159eff375d311278` |
| `real_toric_numerical_dimension_round3_run_manifest_20260825.json` | `833a66310edb9440261f6957887d29ab457dc14653c1ec2b65731e15a26dc08f` |
| `real_toric_numerical_dimension_round3_run_verification_20260825.json` | `3bd8d5c9e7b45ddc91a71984b603a48e7e693f361b27b2347325dae5f246669a` |
| `real_toric_numerical_dimension_round3_item_verification_20260825.json` | `1a078054c9a17c01de9416bfbd2172ccbadec453328a005830d89cc3cfeb8781` |
| `real_toric_numerical_dimension_round3_item_log_20260825.md` | `f61716ff939e7362796309565ae6830a2138d4c63ba40018e6ad663fa32e3659` |
| `real_toric_numerical_dimension_round3_process_guard_20260825.json` | `9aed2786c723ec9ef508ab339f1b0cfd2d969a7dc622825a7dcd2b54befaa323` |
| `real_toric_numerical_dimension_round3_process_child_guard_20260825.json` | `f8e747971baadc61b44d3ddd2a95d60cf76825c9ff7af16fd254c45350991735` |

The API response is an exact copy of
`/private/tmp/rethlas_real_toric_numerical_dimension_response_round3_20260825.json`.
The other six artifacts are exact copies from the production service result
directories for this run.

## Exact mathematical scope

The verified theorem concerns a maximal-compact-torus-invariant closed
positive `(1,1)`-current \(T\) in an arbitrary pseudoeffective real class on
a smooth projective toric variety. With the **closed** Newton body

\[
 K=\Delta(T)=\overline{\operatorname{dom}F_T^*},
\]

it proves for every \(0\leq k\leq n\)

\[
 \int_X\langle T^k\rangle_{\mathrm{Cao}}\wedge\omega^{n-k}
 =\int_X\langle T^k\rangle_{\mathrm{np}}\wedge\omega^{n-k}
 =n!V(K[k],Q[n-k]),
\]

where both degree-zero products are explicitly declared to equal \(1\).
Consequently

\[
 \nu_{\mathrm{Cao}}(T)=\nu_{\mathrm{np}}(T)=\dim K.
\]

Three scope firewalls are part of the verified bytes.

1. This is a **current-level** theorem. The class-level reading is false:
   on \(\mathbf P^1\), \(T=\lambda[0]\) has zero-dimensional current-level
   body/product but its positive class has numerical dimension one. An
   irrational \(\lambda\) gives the same counterexample in an irrational
   class.
2. On a smooth projective toric variety,
   \(H^{1,1}(X,\mathbf R)=N^1(X)_{\mathbf R}\). The extension is to
   irrational real divisor classes, not to genuinely transcendental Hodge
   directions.
3. The closure in \(\Delta(T)\) is essential. For
   \(F(x)=\log(1+\mathrm e^x)\), the gradient image is \((0,1)\) while the
   conjugate domain is \([0,1]\).

## Authenticated source dependencies

| Archived primary source | Exact use | SHA-256 |
|---|---|---|
| `tmp/pdfs/Cao14_arxiv1210.5692_primary.pdf` | Definitions 2--4; arbitrary-current Cao product and quasi-equisingular approximation convention | `17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6` |
| `tmp/pdfs/SGPT_final_20260718_primary.pdf` | gentle regularization; mixed non-pluripolar mass continuity; toric \(\mathcal I\)-goodness | `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706` |
| `tmp/pdfs/CGSZ19_arxiv1804.03387_primary.pdf` | conjugate-domain/subgradient relation and local complex/real toric Monge--Ampere formula | `aeeff09ceabe6a62cf0879f18b8184fb1ffc4a15afbb331f50371658ecc2916d` |
| `tmp/pdfs/BEGZ10_arxiv0812.3674_primary.pdf` | locality, multilinearity, global definition, and non-pluripolar noncharging | `43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd` |

The multiplier-ideal convention correction is explicit in the proof:

\[
 \mathcal I_{\mathrm C}(a\varphi)=\mathcal I_{\mathrm B}(2a\varphi).
\]

Thus the supplied book's condition is applied with
\(\lambda=2m\) and \(\lambda'=2m(1+\delta)\); the packet makes no claim that
the two written definitions are literally identical.

## Verification history

### Round 1: useful rejection

- Run `20260824T144141Z_1d4f8f942fe1`, item
  `pi_c446657f9d449fbe5fdd0abd`.
- Verdict `final/wrong`; zero critical errors and one gap.
- The gap was exactly the missing factor-two comparison between the two
  multiplier-ideal conventions.
- Statement SHA-256:
  `1d4f8f942fe141bec18cca5a19ad51ce6266d13639b1b8dac955e68c9b02ef5d`.
- Proof SHA-256:
  `24ee3cfb964abf6623ea8f71b8256627a933237fd4bf262d8fe76e0f3f7b9107`.
- Request SHA-256:
  `255b3d52d8c6289a8f73805d602a452d8120dafd77f371cf8f622c77435c2766`.
- Response SHA-256:
  `521fe71dfde371ce58d7a486afa37d30aefafde196ece52e0c4a83c3d7e20d2e`.

The exact failed bytes remain in `../rethlas_packets_20260824/` and are
diagnostic only.

### Round 2: infrastructure timeout, no mathematical verdict

- Run `20260824T145445Z_1d4f8f942fe1`, item
  `pi_3bf76c94344da1b86917a111`.
- Repaired proof SHA-256:
  `1c5e17c07cf9a1419e3aef488f7231e0fae274dfb0e69912813ba58ae80b2b70`.
- Request SHA-256:
  `d9713742f55eb91572c3e839e151af319ebe959851812004498a95ca45cbb54e`.
- The HTTP body reports a verifier timeout after 3499 seconds; the item log
  records 690.137 seconds before its own timeout status. Neither is a
  mathematical verdict.
- Exact timeout-response SHA-256:
  `5fb2dd883d0c6e0da0bc588f755175e4bd461a5a239b1add706e7c472095ece4`.
- The exact proof, request, response, log, process guard, and child guard are
  all preserved in `../rethlas_packets_20260824/` with the prefix
  `real_toric_numerical_dimension_round2_timeout_`.

### Round 3: controlling production pass

The full repaired proof was retained without mathematical shortening, and
the explicit convention
\(\langle T^0\rangle_{\mathrm{Cao}}=
\langle T^0\rangle_{\mathrm{np}}=1\) was added to both copies of the target
statement before freezing and submission. The resulting exact run is the
`final/correct` production pass controlled by this receipt.

## Release firewall

- Do not rewrite or delete the round-1 rejection or round-2 timeout; they are
  part of the audit trail.
- Do not edit the frozen round-3 statement, proof, request, response, logs,
  or guards. Any byte change creates a new proof object and requires a new
  receipt.
- Do not promote the false class-level identity
  \(\nu(\{T\})=\dim\Delta(T)\).
- Do not omit the closure on the Newton body or the \(k=0\) convention.
- This receipt does not certify as-yet-unwritten live prose. The separate
  integration blueprint lists the required live and ledger updates.
