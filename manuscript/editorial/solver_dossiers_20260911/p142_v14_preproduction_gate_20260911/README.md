# P14.2 V14 preproduction gate

Date: 11 September 2026.

This dossier archives the exact P14.2 target and the completed production
preflight for the V14 source-closed release.  It does **not** archive a
production mathematical-verification run and does not retire P14.2.

The fixed target hashes are:

| file | SHA-256 |
| --- | --- |
| `target/STATEMENT.tex` | `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2` |
| `target/PROOF.tex` | `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac` |
| `target/EXAMPLE.tex` | `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f` |

The frozen V14 source manifest has SHA-256
`98132fe81883600a33d84d35536293248c7efab563f4ee4d9e59c23fbec6fac8`.
Its 58 rows, 197 source-stage tests, five direct integrity gates, read-only
tree, and exact V13-to-V14 provenance renewal passed independent
`gpt-6-astra`/hostile review with zero critical errors and zero material gaps.

The fresh V14 final-path smoke then passed.  Its receipt records status
`passed`, no errors, exit code zero, one completed MCP call, a
310.005920208-second MCP interval, a 347.227544625-second total interval,
23 live process samples followed by one terminal sample, and no forbidden
diagnostic.  Standard error contains only thirteen exact startup
state-database warnings.  Standard output contains the one exact pre-MCP
skills-budget diagnostic allowed by the pinned contract, one complete MCP
lifecycle, and exactly one post-MCP structured success message.  The 62-row
final manifest has SHA-256
`73489c6753340007c92debb76eb915b63cef5471db52c96c53d98bebfca53d1a`.
An independent final-smoke replay returned zero critical errors and zero
material gaps; see `FINAL_SMOKE_ASTRA_AUDIT.md`.

V13 is preserved separately because its only invocation was stopped after the
caller's restricted execution envelope denied the first process-tree scan.
It produced no model output and completed no MCP call.  No V13 evidence is
reused as a pass; see `V13_FAILED_SMOKE/` and the V14 staging report.

No V14 production request was sent.  The earlier rejected V11 production run
is recorded in `STAGING_REPORT_V14.md` and is not accepted as mathematical
evidence.  The remaining gate is a fresh V14 source-closed production verdict
of `correct` with zero critical errors and zero gaps, followed by independent
replay and live-book integration.
