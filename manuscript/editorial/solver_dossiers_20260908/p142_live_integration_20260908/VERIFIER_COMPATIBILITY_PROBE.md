# P14.2 verifier compatibility probe — 8 September 2026

## Status

This is an evidence-only infrastructure probe.  It neither changes the
independently audited P14.2 statement or proof nor supplies a production
verdict, live-book integration authorization, or a Chapter 72 retirement.
P14.2 remains active.

## Observed release incompatibilities

The independently audited `v3.3.3-r5-p142-source-closed-lf-v2` packet was
copied once to a disposable final path and run for its required cache-horizon
smoke.  The smoke made exactly one configured 310-second MCP wait, emitted
the required terminal marker, returned zero from Codex, and reported no
source, target, runtime, workspace, model-catalog, or process-identity drift.
It nevertheless returned `failed`; the receipt is SHA-256
`f7f44164f2c02ac2134e5ef414ca1d5bba410c8b698c3a2eebec672ff46e7c6d`.

The failure was the frozen stderr grammar, not the P14.2 target.  The current
Codex executable is SHA-256
`a30ec314bbd0e3721632234d07db7c99855db3b9f1e32dbe8c791947f07e7629`,
whereas the 1 September checker pins
`a6042937174f72112dbd2d554a4af36936422e0c5ac69e353dc68994458996e9`.
The current executable additionally emitted a bounded SQL log-prune warning,
an analytics-delivery warning, and a recovered response-stream retry; none
was in the old two-form warning grammar.

## Strict disposable repair experiment

A disposable copy was changed only to bind the current executable hash and
to add exact, bounded patterns for the three observed forms.  The patterns
retain all existing forbidden markers and accept neither altered SQL text,
an alternate analytics endpoint, nor a retry count other than `1/5` with
`retries=1` and `max_retries=5`.  The runner, checker, and regression-test
source hashes were respectively
`7b1fb74ed48fd3da4f1a02eefd837984f4d3dc8ad8c2463c429bedd536330815`,
`b7ae4fb1ca9981cd3ff2a46b9208b99501c1e6767ca6f1d093d342952c8b01fc`, and
`8ae6160378d8a418b9041e5e265ae08a15aab14211030168c877467a1cb232de`.

With the pinned verification Python and bytecode disabled, the complete
suite passed **164/164** tests.  The amended parser and checker accepted the
first raw failed stderr log with the exact counts
`state_db=5`, `shell_snapshot_cleanup=1`, `sqlx_log_prune=1`,
`analytics_delivery=1`, and `responses_retry=1`.

That first compatibility smoke then failed only because the current Codex
executable also attempted remote plugin-catalog refreshes.  Its receipt is
SHA-256
`4bc777ccdc40bbb5eff1e0b53ff61b3d932de1bb57b9adad438dcdbf6d1d1883`.
Rather than allowlist those network failures, the next disposable copy added
the supported per-run switches `--disable plugins`, `--disable remote_plugin`,
and `--disable plugin_sharing`; the complete 164-test suite still passed.

The plugin-disabled smoke again made one 310-second MCP wait, returned the
required terminal marker, returned zero, and reached the cache horizon.  Its
receipt, SHA-256
`5d21524d5590346ff7f59ec93330a79426e101c9751e37d5a921d41ff03e5c98`,
still failed closed: the remote model stream emitted a recovered retry whose
diagnostic explicitly contains `websocket`.  The frozen verifier forbids that
transport class, and the experiment deliberately did not weaken that rule.

## Consequence

The current source-closed smoke cannot become P14.2 evidence merely by
allowlisting the observed logs.  A successor verifier must instead provide a
deterministic, independently audited isolation or validation of the model
transport, bind the current executable and source tree, and then pass a new
final-path smoke before the unchanged P14.2 statement/proof can enter
production verification.  Reusing any of these failed receipts, changing the
Chapter 72 count, or calling the mathematical target verified would violate
the inventory's retirement rule.
