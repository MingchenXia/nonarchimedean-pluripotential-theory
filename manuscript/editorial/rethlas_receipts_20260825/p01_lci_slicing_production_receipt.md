# P01 complete-intersection slicing: production Rethlas receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)  
**Status:** **VERIFIED FROZEN STANDALONE PROPOSITION; NOT YET INTEGRATED**  
**Verifier:** production Rethlas at `127.0.0.1:8091`  
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The exact standalone source-aware proposition and proof returned
`verification_status = final` and `verdict = correct`.  Rethlas checked one
synthetic proof item, with zero failed or blocked items, zero critical
errors, zero gaps, and no request for expanded proofs.

This receipt controls only the frozen complete-intersection slicing
proposition.  It does not reverse or supersede the separate `final/wrong`
verdict for the rig-smooth global converse, whose rejection artifacts remain
preserved under the prefix `p01_rigsmooth_current_converse_`.

## Run identity

- Run: `20260825T023505Z_66547f68ec32`.
- Proof item: `pi_d75152188902c18ea84618d2`.
- Item title: `theorem synthetic:main`.
- Started: `2026-08-25T02:35:05.537484+00:00`.
- Item elapsed time: `410.982` seconds.
- Reported token count: `196`.
- Adaptive round: `0`; no expanded proof was requested.
- Verifier process: completed with return code `0`; output validated.
- Process-guard command SHA-256:
  `0705d972245c014d0adaf9b30e719e1523267d299095b2db0f1a3d14feaba44b`.
- Both parent and child process guards have state `completed`.

The item log independently attests the requested model, reasoning effort,
proof digest, and validated completion.

## Exact submitted bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p01_lci_slicing_statement_exact_20260825.tex` | 2172 | 46 | `66547f68ec325107732ee307b3e728480b5ffc9c8f08537478e75984eb89f202` |
| `../rethlas_packets_20260825/p01_lci_slicing_source_aware_proof_exact_20260825.tex` | 8756 | 211 | `d62ff2285ed7a7e435ae78477075482bf676bf36360a1e4c46babfdbfbad281b` |
| `../rethlas_packets_20260825/p01_lci_slicing_source_aware_request_20260825.json` | 11664 | 5 | `63c832048d3a4f7004ece12f8b67187b64034e881adf9add4ccf04a954fe28f2` |

Decoding the request with `jq -j '.statement'` and `jq -j '.proof'`
reproduced the frozen statement and proof byte for byte; both `cmp` checks
returned zero.  The request deadline was `2026-08-25T04:30:00+00:00`.

## Verified mathematical scope

Let `X` be good, separated, boundaryless, strict, and pure of dimension
`n >= 2`; let `h` be continuous real PL with positive CLD current.  If
`f_1,...,f_{n-1}` is a regular sequence and
`f=(f_1,...,f_{n-1})` is purely of relative dimension one, with zero fibre
`C`, then for every **ambient** nonnegative smooth compactly supported
function `psi`,

```text
<d'd''[h|_C], psi|_C> >= 0.
```

If the curve current is discrete in a neighbourhood of `z` and an ambient
cutoff is supported in that neighbourhood, equals one near `z`, and meets
the current support only at `z`, its pairing is the coefficient of that
atom, which is therefore nonnegative.

The verified proof uses:

- the deletion regularized maximum from the proof of CLD Proposition 16.9.1;
- CLD Proposition 8.7.2 with `h` as a merely continuous outer factor;
- CLD Corollary 18.6.2, including analytic fibre multiplicities;
- CLD Proposition 18.7.3 with the proof-correct relative dimension
  `n-d=1`, notwithstanding the displayed source typo `d`;
- the local real-PL expression for `h`, which makes
  `h d'd''psi` a compactly supported G-form with tropically continuous,
  hence locally bounded tropically Borel, coefficients.

The item-level mathematical summary is:

> The proof is correct. The regularized maximum construction gives smooth
> psh approximants with the stated deletion and uniform-approximation
> properties; all test-form bidegrees, positivity, closedness, compact
> supports, and integration-by-parts signs are correct. Proposition 8.7.2
> applies with continuous outer factor h, Corollary 18.6.2 identifies the
> Monge--Ampere current with the Gauss fibre including analytic
> multiplicities, and Proposition 18.7.3 applies with the proof-correct
> relative dimension n-d=1 despite the source statement's evident typo
> “d.” The R-PL description of h supplies the required compactly supported
> G-form with locally bounded tropically Borel coefficients, and the cutoff
> hypotheses isolate exactly the atom at z.

## Returned digests and preserved artifacts

- Proof digest:
  `d62ff2285ed7a7e435ae78477075482bf676bf36360a1e4c46babfdbfbad281b`.
- Aggregate context digest:
  `4ec6fb4d7820a726a4f9f10a852149113b729d293005270032d24f4bb291b8b1`.
- Adaptive context digest:
  `7fda516ab5b6e73804b253ee090486fe8cbdc3fa7471594badd7d61a30d898df`.
- Item context digest:
  `74196a95cca62e3daea6a3acb3982b62083dc71abd666ba9dbfb983496f48c6b`.

| Preserved artifact | SHA-256 |
|---|---|
| `p01_lci_slicing_api_response_20260825.json` | `b0cff06f7aa5de49cdfbfffd7dd1409b5969842aa744d418d8593ed069a0ab12` |
| `p01_lci_slicing_run_manifest_20260825.json` | `633e44bfa96e634003bf7ae22de0db1c4a90bf3a740eb26f23827c33391abea4` |
| `p01_lci_slicing_run_verification_20260825.json` | `9970cf6ddb08f647d491837d6518564128f9613ee342dab378e6687f395f7604` |
| `p01_lci_slicing_item_verification_20260825.json` | `14437b1bee900c6b8de037c6b95692560f2f2a3174db7c21420967ff98d7ddc0` |
| `p01_lci_slicing_item_log_20260825.md` | `e53e3b70c6281cef3cdad8588707e8a01bf3712ea1ec90f107e83326e0024fe1` |
| `p01_lci_slicing_process_guard_20260825.json` | `c440324f5e7de50124d9fc45a3937c2717d35bac6a90649ebdd14102a11dfb36` |
| `p01_lci_slicing_process_child_guard_20260825.json` | `dd668541275c4402e1e18805c0983a939b3ae4776e6b2b84cc8d8e0aadb49a62` |

The compact API-response file equals the `jq -c` canonicalization of the
archived run verification.  The production client validator independently
rebuilt the synthetic manifest and accepted the response as schema-valid
`final/correct`, with the expected item id, proof digest, and aggregate
context digest.

## Release firewall

- Do not edit the frozen statement, proof, request, response, logs, guards,
  or this receipt.  Any byte change creates a new proof object.
- Do not enlarge “ambient test functions” to all smooth functions on `C`
  without a separate extension theorem.
- Do not drop the pure-relative-dimension, boundaryless, compact-support,
  G-form, or tightly supported cutoff hypotheses.
- Do not use this proposition as a degree--atom comparison.  It contains no
  residual-degree formula.
- Do not infer the rejected rig-smooth or singular global converse.  P01
  remains narrowed/open.
- No novelty or priority claim is made.
