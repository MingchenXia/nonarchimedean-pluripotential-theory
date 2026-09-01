# P14.8 retry-2 final-path smoke report

Date: 2026-09-01

Binary verdict: **FAIL**.  This installed release is not ready for an
independent final-release audit or a production submission.  Its single
authorized final-path smoke must not be rerun and the path must not be reused.

## Exact inputs and installation

The source is the exact `release_stage` in
`/private/tmp/p148_smoke_infrastructure_repaired_readonly_authored_stage_dossier_v2_20260901`.
The authored top manifest, release-stage manifest, and independent hostile
audit manifest have respective SHA-256 digests

- `0645efed9d2ba12a99501fe07a1988e4e7a09a20e496d21c38937774d1d29d46`;
- `837d5bb55d134bf4040c1083ffb1cf068b6b6c83bbc16bd7e86f2a1d8f247912`;
- `21462160629d17c30157a1f75d8904c87a94d5b96c38c0884318b43ef26af878`.

The source and audit checkers passed again from their repository-preserved
copies before installation.  The final path
`/Users/mingchen/Documents/ChatGPT/Yethlas/runtime/rethlas_hardened_v3_3_3_r5_p148_retry2_final_20260901`
was proved nonexistent before a mechanical copy.  Before the smoke, every one
of the 44 release rows matched the source and `diff -qr` was empty.  The
installation copy alone was made owner-writable, as required to create the
smoke tree; the frozen source remained at directories `0555` and regular files
`0444`.

A diagnostic invocation of the source-stage unit suite on the writable final
copy produced 50 permission assertions: 49 subcases of the test requiring the
*source-stage* tree to be read-only and the related symlink non-following
assertion.  The other 111 tests passed.  This invocation changed no bytes and
created no cache.  It is not the final-release blocker; the complete suite had
already passed four times on the correctly frozen source tree.

After the smoke, the mechanically regenerated final manifest contains the 44
unchanged inherited rows and exactly four smoke-artifact rows.  Its SHA-256 is
`d2ee26df03554aa133fbf9dfd9f28166a2b6a328eb690565925dfd5dac42aab7`.

## What the one smoke established

The runner receipt reports `passed`, return code zero, exactly one completed
`wait_across_catalog_ttl(seconds=310)` call, `StaticModelsManager`, the static
`gpt-5.6-sol` catalog at `xhigh`, equal before/after runtime fingerprints, and
an empty before/after workspace.  The run lasted
`331.4424050839989` seconds.  Its 23 process observations consist of 22 live
samples followed by one terminal sample and cross the 300-second horizon.
Neither stream contains a forbidden cache, refresh, credential,
authentication, transport, TLS, websocket, or endpoint diagnostic.

Frozen smoke hashes are:

| artifact | SHA-256 |
|---|---|
| receipt | `68fc549b39912141e8418385d414616a1e3319bfdc62c54a4ece4100b03aa3b4` |
| stdout JSONL | `9859b7ca52f85b8c7c09b7e1f67eab26fa7671eeea2895a5335c096279482c4b` |
| stderr | `8430b6c103a639a3bc6f8e732504111ea5365235a37bf32b091698bc35385b76` |
| process samples | `218e77793b544ea69036159b3a67fea341785ba1c66bacec91ef81275f21af1d` |

## Exact blocker

The strict final checker fails closed with
`raw smoke terminal marker mismatch`.  The stdout lifecycle contains the
following exact pre-tool pair:

1. the already allowlisted skills-context-budget error item; and
2. an additional completed empty `agent_message`.

It then contains exactly one completed TTL call and the exact terminal
`agent_message` `STATIC_MODEL_SMOKE_OK`.  Hence there are two agent-message
records, although only one is nonempty.  The checker deliberately requires
exactly one agent-message record, so it rejects the receipt.  Removing only the
empty pre-tool record in memory makes the unchanged lifecycle pass the strict
stdout validator; no artifact was edited.

The next release must be a new sibling.  Its runner and checker should jointly
classify at most one empty pre-tool agent message only when it is immediately
paired with the exact bounded skills-context-budget error, while continuing to
require exactly one nonempty terminal message after the completed tool call and
to reject every other empty, extra, misplaced, or nonterminal agent message.
The runner must enforce the same lifecycle before writing a passing receipt.
All P14.8 mathematical bytes, fixed sources, pins, stream separation, PTY,
process sampling, and horizon gates must remain unchanged.  The sibling then
requires a new hostile audit and one smoke at another previously nonexistent
final path.

No production request, live-manuscript edit, inventory retirement, or reuse of
this smoke was performed.
