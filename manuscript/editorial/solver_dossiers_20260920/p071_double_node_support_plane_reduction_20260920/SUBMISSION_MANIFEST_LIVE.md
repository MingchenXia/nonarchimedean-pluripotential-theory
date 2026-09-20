# Submission manifest

Date: 2026-09-20

Controlling packet order:

1. `STATEMENT_LIVE.tex`
2. `PROOF_LIVE.tex`

Controlling verifier archive:

1. `model_run_repaired/request.json`
2. `model_run_repaired/response.json`
3. `model_run_repaired/headers.json`

The earlier `model_run_superseded_tex_escape/` archive authenticates
superseded proof bytes containing two missing TeX command markers.  The
later `model_run_superseded_extra_plus/` archive authenticates proof bytes
in which those markers were repaired but a stray plus sign remained between
two convex-envelope constraints.  Both are retained for provenance only
and must not be used as the current receipt.
