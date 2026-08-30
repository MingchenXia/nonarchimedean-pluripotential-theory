# P07.1 dependency-closed production packet

Date: 30 August 2026 (Asia/Shanghai)

Status: **production PASS**.  The offline preparation described below was
subsequently submitted without changing the materialized statement or proof.
See `PRODUCTION_RECEIPT.md` for the exact request, response, header, principal,
dependency, and audit hashes.

The packet places the already production-verified Stone-parameter times one
convex-polyhedron theorem before the frozen generator-convex polyhedral-complex
candidate.  The ordered mathematical fields are in
`statement.materialized.tex` and `proof.materialized.tex`.  Their assembly is
identical to the current production helper's materialization rule.

`request.prepared.json` is a byte-binding artifact, not a request suitable for
submission: its `verification_deadline_utc` is deliberately `null`.  The
production helper must create a fresh `request.json` immediately before the
actual call.  No `response.json` or `headers.json` exists before that call.

The exact source, dependency, materialization, compile, reference, and visual
checks are recorded in `PRE_SUBMISSION_AUDIT.md` and
`MATERIALIZATION_MANIFEST.json`.  Re-running `assemble_prepared_packet.py` is
an offline fail-closed preflight: it rehashes every frozen input and refuses a
differing output.  It opens no socket.

This packet does not authorize a live-manuscript edit.  Promotion still
requires a production Rethlas verdict `correct`, with zero critical errors and
zero gaps, on the exact materialized statement and proof hashes recorded here.
