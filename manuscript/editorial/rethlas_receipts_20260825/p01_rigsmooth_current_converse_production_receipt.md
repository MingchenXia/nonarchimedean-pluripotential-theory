# P01 rig-smooth current converse: production Rethlas receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)  
**Status:** **FINAL/WRONG; FROZEN CANDIDATE REJECTED; NOT INTEGRATED**  
**Verifier:** production Rethlas at `127.0.0.1:8091`  
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The exact source-aware candidate returned `verification_status = final` and
`verdict = wrong`.  Rethlas checked one synthetic proof item.  It reported
one critical error, zero gaps, and no request for expanded proofs.  This
receipt records a rejection of the exact packet below; it is not authority to
insert any part of the rejected theorem into a live chapter.

## Run identity

- Run: `20260825T021510Z_1cc218c613f9`.
- Proof item: `pi_f71271c9a6450fcb5b581304`.
- Item title: `theorem synthetic:main`.
- Started: `2026-08-25T02:15:10.229213+00:00`.
- Item elapsed time: `567.088` seconds.
- Reported token count: `196`.
- Adaptive round: `0`; no expanded proof was requested.
- Verifier process: completed with return code `0`; output validated.
- Process-guard command SHA-256:
  `ed6dc4344aae3cb363e73e018163a062d83566f11f9b6cef43c784de606e22a0`.
- Both the parent and child process guards have state `completed`.

The service cwd was
`/Users/mingchen/.codex/visualizations/2026/08/20/01a01d3c-132d-7ca3-b98a-59682fe837e7/Rethlas_popovici_local/agents/verification`.
The item log independently attests the requested model, reasoning effort,
proof digest, and validated completion.

## Exact submitted bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p01_rigsmooth_current_converse_statement_exact_20260825.tex` | 2362 | 40 | `1cc218c613f9921efe71dbea10a19e93b089d31f1d00002efef8669418550042` |
| `../rethlas_packets_20260825/p01_rigsmooth_current_converse_exact.tex` | 10430 | 253 | `a89f3b6a85de80999a83f8812ec7617c0bb3ee397bc38cd11a169f05c7576767` |
| `../rethlas_packets_20260825/p01_rigsmooth_current_converse_source_aware_request_20260825.json` | 13524 | 5 | `ded33500417c17e58024900516d5fbe9ac6e42f80c24d980b1642ac9fe298e8b` |

Decoding the JSON fields with `jq -j '.statement'` and `jq -j '.proof'`
reproduced the two frozen TeX files byte for byte; both `cmp` checks returned
zero.  The request deadline was `2026-08-25T04:30:00+00:00`.

## Verdict and mathematical obstruction

The item-level report accepts the complete-intersection slicing proposition
as supported by the cited Chambert--Loir--Ducros continuity, fibre-current,
and specialization results, with signs, bidegrees, compact supports, and the
corrected relative dimension consistent.  It nevertheless rejects the
theorem at the step that identifies the atom at the lifted point with

\[
             m_z\deg(\mathcal L|_{\Gamma'}),\qquad m_z>0.
\]

The critical error is source-scope failure.  Gubler--Rabinoff
Proposition~5.1 is stated for smooth strictly analytic curves, and its
explicit coefficient calculation passes to an algebraically closed field
and a formal model with reduced special fibre.  The packet proves only that
the lifted curve is irreducible and an ordinary local complete intersection;
it does not prove rig-smoothness or geometric regularity.  Over a possibly
imperfect field, ordinary regularity does not imply geometric regularity.
Nor does the packet supply a descent theorem or a general model-current
formula establishing the asserted positive, correctly normalized
multiplicity for a singular curve over arbitrary `K` with a possibly
nonreduced formal model.  Hence the negative atom required for the final
contradiction is unproved.

The report also records that Chambert--Loir--Ducros Corollary~18.8.8 does not
repair the submitted argument: its stated equivalence has integral PL scope,
whereas the candidate theorem concerns arbitrary real PL functions.

The prescribed repairs are either:

1. prove that the lifted curve is rig-smooth near the chosen point and give
   a precise base-change/descent reduction to the smooth reduced-model
   coefficient calculation; or
2. cite and correctly apply a model-current formula valid for singular
   curves, arbitrary complete ground fields, real coefficients, and
   nonreduced formal models, explicitly defining the multiplicity and proving
   that it is strictly positive and compatible with the projection formula.

Neither repair is present in the frozen candidate.

## Returned digests and preserved artifacts

- Proof digest:
  `a89f3b6a85de80999a83f8812ec7617c0bb3ee397bc38cd11a169f05c7576767`.
- Aggregate context digest:
  `6a8a9077a6437a94869e19684f36c9dedbe3f8cefb040d5b4dcf8fc1cbb65272`.
- Adaptive context digest:
  `59181e2f078da897ec3e942b798129100c9d2f305a2412f567a33b17b3d6d8b4`.
- Item context digest:
  `9c072537c472b70ae747411128fabfc28ac61a9255f0c4e0607775e4548a565e`.

| Preserved artifact | SHA-256 |
|---|---|
| `p01_rigsmooth_current_converse_api_response_20260825.json` | `ed012aa8ece8bd3c8a7ee6f87dbeb38dcce3a67c5a47916561307c9c6e5e4703` |
| `p01_rigsmooth_current_converse_run_manifest_20260825.json` | `7664789f0e7bcda8e8dc385b768f254fcb105a7300952f70a3ff9e8a8f2071f2` |
| `p01_rigsmooth_current_converse_run_verification_20260825.json` | `a95960e48bd957de9aa5d0af152df8177a5196b7df67d11cb63fccbd1a21953b` |
| `p01_rigsmooth_current_converse_item_verification_20260825.json` | `c08362bf92782f6a94e1e676fd548ae0a02619da3e396d4bb1d89f72cafd6c5b` |
| `p01_rigsmooth_current_converse_item_log_20260825.md` | `bc64f40f043ae37df3391cb7d9ce6d039f3e175550ef897f9da1dc179eb0a461` |
| `p01_rigsmooth_current_converse_process_guard_20260825.json` | `d0c1ab2051b7adf2c5bcb7a9811ed4e372671e70450e933612fefcdbec9e9be9` |
| `p01_rigsmooth_current_converse_process_child_guard_20260825.json` | `07108723329ff75371cb3750a633baeb5970d25a4aff5da531f33235ec1715b2` |

The API-response file is the exact compact JSON content returned by the
service, with its final newline preserved.  Canonicalizing the archived run
verification with `jq -c` gives exactly the same bytes.  The production
client validator rebuilt the synthetic manifest and accepted the response as
schema-valid `final/wrong`, with the expected item id, proof digest, and
aggregate context digest.

## Release firewall

- Do not edit, rewrite, or delete the frozen statement, proof, request,
  response, logs, guards, or this receipt.
- Do not integrate the rejected rig-smooth converse into Chapter~72 or any
  other live chapter.
- The slicing proposition may be reused only through a separately frozen
  packet and a verdict whose target is that proposition itself; this
  whole-packet rejection is not a publication certificate for a subclaim.
- P01 remains narrowed, not solved.  The general singular case retains the
  complete-intersection/excess-intersection obstruction, and the rig-smooth
  route now also retains the verified source-scope/multiplicity obstruction
  above.
- No novelty or priority claim is made.
